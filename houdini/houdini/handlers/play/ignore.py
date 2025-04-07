from houdini import handlers
from houdini.data.buddy import IgnoreList, IgnoreListCollection
from houdini.data.penguin import Penguin
from houdini.handlers import Priority, XMLPacket, XTPacket


@handlers.handler(XMLPacket('login'), priority=Priority.Low)
@handlers.allow_once
async def load_ignore_inventory(p):
    p.ignore = await IgnoreListCollection.get_collection(p.id)


@handlers.handler(XTPacket('n', 'gn'))
@handlers.allow_once
async def handle_get_ignore_list(p):
    ignore_query = IgnoreList.load(parent=Penguin.on(Penguin.id == IgnoreList.ignore_id)).where(
        IgnoreList.penguin_id == p.id)

    async with p.server.db.transaction():
        ignore_list = ignore_query.gino.iterate()
        ignores = [f'{ignore.ignore_id}|{ignore.parent.safe_nickname(p.server.config.lang)}'
                   async for ignore in ignore_list]

    await p.send_xt('gn', *ignores)


@handlers.handler(XTPacket('n', 'rn'))
async def handle_ignore_remove(p, ignored_id: int):
    if ignored_id in p.ignore:
        await p.ignore.delete(ignored_id)
        await p.send_xt('rn', ignored_id)


@handlers.handler(XTPacket('n', 'an'))
async def handle_ignore_add(p, ignored_id: int):
    if ignored_id not in p.ignore:
        if ignored_id in p.server.penguins_by_id:
            nickname = p.server.penguins_by_id[ignored_id].safe_name
        else:
            nickname = await Penguin.select('nickname').where(Penguin.id == ignored_id).gino.scalar()
        await p.ignore.insert(ignore_id=ignored_id)
        await p.send_xt('an', ignored_id, nickname)
