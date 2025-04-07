import ujson

from houdini import handlers
from houdini.data import db
from houdini.data.quest import PenguinQuestTask, Quest, QuestAwardFurniture, QuestAwardItem, QuestAwardPuffleItem, \
    QuestTask
from houdini.handlers import XTPacket
from houdini.handlers.play.navigation import handle_join_player_room, handle_join_room, handle_join_server


async def get_player_quest_status(p):
    query = Quest.load(tasks=QuestTask,
                       items=QuestAwardItem,
                       furniture=QuestAwardFurniture,
                       pet=QuestAwardPuffleItem,
                       complete=PenguinQuestTask.on((PenguinQuestTask.penguin_id == p.id) &
                                                    (QuestTask.id == PenguinQuestTask.task_id))).gino

    def has_award(quest):
        for award in quest.items:
            if award.item_id not in p.inventory:
                return False
        for award in quest.furniture:
            if award.furniture_id not in p.furniture:
                return False
        for award in quest.pet:
            if award.puffle_item_id not in p.puffle_items:
                return False
        return True

    def encode_quest(quest):
        tasks_complete = [task.id in quest.complete for task in quest.tasks]
        quest_status = 'prize claimed' if has_award(quest) else 'complete' if all(tasks_complete) else 'available' \
            if quest.in_progress else 'not available'
        return {
            'id': quest.id,
            'status': quest_status,
            'tasks': tasks_complete
        }

    async with db.transaction():
        player_quest_status = {
            'quests': [encode_quest(quest) async for quest in query.iterate()]
        }

    return ujson.dumps(player_quest_status)


AwardTypes = {
    QuestAwardItem: ('item_id', 'penguinItem'),
    QuestAwardFurniture: ('furniture_id', 'furnitureItem'),
    QuestAwardPuffleItem: ('puffle_item_id', 'puffleItem')
}


async def get_quest_settings(p):
    query = Quest.load(items=QuestAwardItem,
                       furniture=QuestAwardFurniture,
                       pet=QuestAwardPuffleItem,
                       tasks=QuestTask).gino

    def encode_award(award):
        award_id, award_type = AwardTypes[type(award)]
        return {
            'id': getattr(award, award_id),
            'type': award_type,
            'n': award.quantity if hasattr(award, 'quantity') else 1
        }

    def encode_task(task):
        return {
            'type': 'room' if task.room_id is not None else '',
            'description': task.description,
            'data': task.room_id if task.room_id is not None else task.data
        }

    async with db.transaction():
        quest_settings = {
            'ver': 1, 'spawnRoomId': p.room.id,
            'quests': [
                {
                    'id': quest.id,
                    'name': quest.name,
                    'awards': [encode_award(award) for award in quest.awards],
                    'tasks': [encode_task(task) for task in quest.tasks]
                } async for quest in query.iterate()
            ]}

    return ujson.dumps(quest_settings)


async def init_all_quests(p):
    query = Quest.load(tasks=QuestTask,
                       complete=PenguinQuestTask.on((PenguinQuestTask.penguin_id == p.id) &
                                                    (QuestTask.id == PenguinQuestTask.task_id))).gino

    async with db.transaction():
        async for quest in query.iterate():
            for task in quest.tasks:
                if task.id not in quest.in_progress.union(quest.complete):
                    await PenguinQuestTask.create(task_id=task.id, penguin_id=p.id)

    await load_active_quests(p)


async def load_active_quests(p):
    p.active_quests = await Quest.load(tasks=QuestTask,
                                       items=QuestAwardItem,
                                       furniture=QuestAwardFurniture,
                                       pet=QuestAwardPuffleItem,
                                       complete=PenguinQuestTask.on((PenguinQuestTask.penguin_id == p.id) &
                                                                    (PenguinQuestTask.task_id == QuestTask.id) &
                                                                    (PenguinQuestTask.complete == False))).gino.all()


@handlers.handler(XTPacket('j', 'js'), after=handle_join_server)
@handlers.allow_once
async def handle_quest_join_server(p):
    p.server.cache.delete(f'quest.status.{p.id}')

    await load_active_quests(p)
    quest_settings = p.server.cache.get(f'quest.settings.{p.room.id}')
    quest_status = p.server.cache.get(f'quest.status.{p.id}')
    quest_settings = await get_quest_settings(p) if quest_settings is None else quest_settings
    quest_status = await get_player_quest_status(p) if quest_status is None else quest_status
    p.server.cache.set(f'quest.settings.{p.room.id}', quest_settings)
    p.server.cache.set(f'quest.status.{p.id}', quest_status)

    await p.send_xt('nxquestsettings', quest_settings)
    await p.send_xt('nxquestdata', quest_status)


async def set_task_cleared(p, task_id):
    p.server.cache.delete(f'quest.status.{p.id}')

    await PenguinQuestTask.update.values(complete=True) \
        .where((PenguinQuestTask.task_id == task_id) &
               (PenguinQuestTask.penguin_id == p.id)).gino.status()
    return await p.send_xt('nxquestdata', await get_player_quest_status(p))


@handlers.handler(XTPacket('j', 'jr'), after=handle_join_room)
async def handle_quest_join_room(p):
    if p.active_quests is not None:
        for quest in p.active_quests:
            for task in quest.tasks:
                if task.id in quest.in_progress and task.room_id == p.room.id:
                    await set_task_cleared(p, task.id)
                    p.active_quests.remove(quest)


@handlers.handler(XTPacket('j', 'jp'), after=handle_join_player_room)
async def handle_quest_join_player_room(p):
    if p.active_quests is not None:
        for quest in p.active_quests:
            for task in quest.tasks:
                igloo_quest_completed = task.id == 3 and p.room.igloo and p.room.penguin_id == p.id
                if task.id in quest.in_progress and igloo_quest_completed:
                    await set_task_cleared(p, task.id)
                    p.active_quests.remove(quest)


@handlers.handler(XTPacket('nx', 'nxquestaward'))
async def handle_quest_award(p, quest_id: int):
    p.server.cache.delete(f'quest.status.{p.id}')

    quest = await Quest.load(items=QuestAwardItem,
                             furniture=QuestAwardFurniture,
                             pet=QuestAwardPuffleItem).where(Quest.id == quest_id).gino.first()
    for award in quest.items:
        await p.add_inventory(p.server.items[award.item_id])
    for award in quest.furniture:
        await p.add_furniture(p.server.furniture[award.furniture_id])
    for award in quest.pet:
        await p.add_puffle_item(p.server.puffle_items[award.puffle_item_id])
    await p.send_xt('nxquestdata', await get_player_quest_status(p))


@handlers.handler(XTPacket('nx', 'nxquestactivate'))
@handlers.allow_once
async def handle_quest_activate(p):
    p.server.cache.delete(f'quest.status.{p.id}')

    await init_all_quests(p)
    await p.send_xt('nxquestdata', await get_player_quest_status(p))


@handlers.handler(XTPacket('nx', 'gas'))
@handlers.allow_once
async def handle_get_action_status(p):
    await p.send_xt('gas', int(p.special_dance), int(p.special_wave),
                    int(p.special_snowball))


@handlers.handler(XTPacket('nx', 'mcs'))
async def handle_map_category_setting(p, map_category: int):
    if 0 <= map_category <= 4:
        await p.update(map_category=map_category).apply()


@handlers.handler(XTPacket('nx', 'pcos'))
@handlers.allow_once
@handlers.player_attribute(opened_playercard=False)
async def handle_playercard_opened_setting(p):
    await p.update(opened_playercard=True).apply()


@handlers.handler(XTPacket('nx', 'swave'))
@handlers.allow_once
@handlers.player_attribute(special_wave=False)
async def handle_special_wave(p):
    await p.update(special_wave=True).apply()


@handlers.handler(XTPacket('nx', 'sdance'))
@handlers.allow_once
@handlers.player_attribute(special_dance=False)
async def handle_special_dance(p):
    await p.update(special_dance=True).apply()


@handlers.handler(XTPacket('nx', 'ssnowball'))
@handlers.allow_once
@handlers.player_attribute(special_snowball=False)
async def handle_special_snowball(p):
    await p.update(special_snowball=True).apply()
