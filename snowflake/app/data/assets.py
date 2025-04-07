
from app.engine.place import SnowLobby, SnowBattle, TuskBattle
from app.objects.asset import Asset

import app.session

# Assets taken from: /game/mpassets/publishdata/r5309/pubdata/spriteList_tokenized.gml.gz
# TODO: Automatically load assets from the spriteList file

common_assets = [
    Asset(1, "blank_png"),
    Asset(6740009, "Empty Tile"),
    Asset(6740010, "open"),
    Asset(6740011, "enemy"),
    Asset(6740012, "penguin"),
    Asset(6740013, "penguin_spawn_occupied"),
    Asset(6740014, "penguin_spawn_unoccupied"),
    Asset(6740015, "enemy_spawn_unoccupied"),
    Asset(6740016, "enemy_spawn_occupied"),
    Asset(6740017, "obstacle"),
    Asset(7940001, "water_spawn"),
    Asset(7940002, "enemy_spawn_unoccupied"),
    Asset(7940003, "enemy_spawn_occupied"),
    Asset(7940004, "obstacle"),
    Asset(7940005, "penguin_spawn_occupied"),
    Asset(7940006, "Empty Tile"),
    Asset(7940007, "blankblue"),
    Asset(7940008, "blankgreen"),
    Asset(7940009, "blankgrey"),
    Asset(7940010, "blankpurpl"),
    Asset(7940011, "blankwhite"),
    Asset(7940012, "Empty Tile"),
    Asset(7940013, "open"),
    Asset(7940014, "enemy"),
    Asset(7940015, "penguin"),
    Asset(7940016, "penguin_spawn_occupied"),
    Asset(7940017, "penguin_spawn_unoccupied"),
    Asset(7940018, "enemy_spawn_unoccupied"),
    Asset(7940019, "enemy_spawn_occupied"),
    Asset(7940020, "obstacle")
]

ui_assets = [
    Asset(100395, "reghealthbar_animation"),
    Asset(100040, "ui_target_red_attack_intro_anim"),
    Asset(100041, "ui_target_red_attack_idle_anim"),
    Asset(100042, "ui_target_green_attack_selected_intro_anim"),
    Asset(100043, "ui_target_green_attack_selected_idle_anim"),
    Asset(100044, "ui_target_white_heal_intro_anim"),
    Asset(100045, "ui_target_white_heal_idle_anim"),
    Asset(100046, "ui_target_green_heal_selected_intro_anim"),
    Asset(100047, "ui_target_green_heal_selected_idle_anim"),
    Asset(100048, "ui_healfx_anim"),
    Asset(100063, "ui_tile_move"),
    Asset(100064, "ui_tile_attack"),
    Asset(100065, "ui_tile_heal"),
    Asset(100067, "ui_attack_numbers_anim"),
    Asset(100120, "ui_card_fire"),
    Asset(100121, "ui_card_snow"),
    Asset(100122, "ui_card_water"),
    Asset(100195, "ui_confirm"),
    Asset(100250, "ui_heal_numbers_anim"),
    Asset(100266, "ui_card_pattern3x3"),
    Asset(100267, "ui_card_pattern3x2"),
    Asset(100268, "ui_card_pattern2x3"),
    Asset(100269, "ui_card_pattern2x2"),
    Asset(100270, "ui_tile_no_move"),
    Asset(100300, "ui_tile_frame"),
    Asset(8740005, "ui_card_member_snow"),
    Asset(8740006, "ui_card_member_water"),
    Asset(8740007, "ui_card_member_fire"),
    Asset(100334, "effect_rageloop_anim"),
    Asset(100335, "effect_explosion_anim"),
    Asset(100336, "effect_shield_loop"),
    Asset(100337, "effect_shieldpop_anim"),
    Asset(100339, "effect_resisualfiredamage_anim"),
    Asset(100392, "effect_rageattack_anim"),
    Asset(100396, "effect_ragehit_anim"),
    Asset(8740008, "effect_revivebeam_anim"),
]

background_assets = [
    Asset(100380, "env_mountaintop_bg"),
    Asset(100394, "rock_mountaintop"),
    Asset(6740003, "cragvalley_bg"),
    Asset(6740004, "cragvalley_fg"),
    Asset(6740006, "forest_bg"),
    Asset(6740007, "forest_fg"),
    Asset(6740008, "crag_rock")
]

enemy_assets = [
    Asset(100379, "snowman_spawn_anim"),
    Asset(100297, "tank_idle_anim"),
    Asset(100299, "tank_attack_anim"),
    Asset(100302, "tank_hit_anim"),
    Asset(100303, "tank_move_anim"),
    Asset(100304, "tank_ko_anim"),
    Asset(100240, "tank_swipe_horiz_anim"),
    Asset(100241, "tank_swipe_vert_anim"),
    Asset(100305, "sly_idle_anim"),
    Asset(100306, "sly_attack_anim"),
    Asset(100307, "sly_move_anim"),
    Asset(100308, "sly_hit_anim"),
    Asset(100309, "sly_ko_anim"),
    Asset(100310, "sly_projectile_anim"),
    Asset(1840011, "sly_daze_anim"),
    Asset(100311, "scrap_idle_anim"),
    Asset(100312, "scrap_attack_anim"),
    Asset(100313, "scrap_attackeffect_anim"),
    Asset(100314, "scrap_attacklittleeffect_anim"),
    Asset(100315, "scrap_projectileeast_anim"),
    Asset(100316, "scrap_projectilenorth_anim"),
    Asset(100317, "scrap_projectilenortheast_anim"),
    Asset(100318, "scrap_hit_anim"),
    Asset(100319, "scrap_move_anim"),
    Asset(100320, "scrap_ko_anim"),
    Asset(1840012, "scrap_dazed_anim")
]

ninja_assets = [
    Asset(30044, "waterninja_move_ghost"),
    Asset(30070, "fireninja_move_ghost"),
    Asset(100018, "snowninja_move_ghost"),
    Asset(100361, "snowninja_idle_anim"),
    Asset(100322, "waterninja_idle_anim"),
    Asset(100340, "fireninja_idle_anim"),
    Asset(100321, "waterninja_attack_anim"),
    Asset(100323, "waterninja_move_anim"),
    Asset(100324, "waterninja_hit_anim"),
    Asset(100325, "waterninja_kostart_anim"),
    Asset(100326, "waterninja_koloop_anim"),
    Asset(100327, "waterninja_celebrate_anim"),
    Asset(100328, "waterninja_powercard_fishdrop_anim"),
    Asset(100329, "waterninja_powercard_summon_anim"),
    Asset(100330, "waterninja_powercard_water_loop_anim"),
    Asset(100331, "waterninja_revived_anim"),
    Asset(100332, "waterninja_revive_other_intro_anim"),
    Asset(100333, "waterninja_revive_other_loop_anim"),
    Asset(8740010, "waterninja_member_revive"),
    Asset(100341, "fireninja_move_anim"),
    Asset(100342, "fireninja_hit_anim"),
    Asset(100343, "fireninja_attack_anim"),
    Asset(100344, "fireninja_powerbottle_anim"),
    Asset(100345, "fireninja_powerskyfire_anim"),
    Asset(100346, "fireninja_projectile_angleup_anim"),
    Asset(100347, "fireninja_projectile_angledown_anim"),
    Asset(100348, "fireninja_projectile_down_anim"),
    Asset(100349, "fireninja_projectile_downfar_anim"),
    Asset(100350, "fireninja_projectile_right_anim"),
    Asset(100351, "fireninja_projectile_rightfar_anim"),
    Asset(100352, "fireninja_projectile_up_anim"),
    Asset(100353, "fireninja_projectile_upfar_anim"),
    Asset(100354, "fireninja_celebratestart_anim"),
    Asset(100355, "fireninja_celebrateloop_anim"),
    Asset(100356, "fireninja_kostart_anim"),
    Asset(100357, "fireninja_koloop_anim"),
    Asset(100358, "fireninja_revived_anim"),
    Asset(100359, "fireninja_reviveother_anim"),
    Asset(100360, "fireninja_reviveotherloop_anim"),
    Asset(100378, "fireninja_power_anim"),
    Asset(8740009, "fireninja_member_revive"),
    Asset(100362, "snowninja_attack_anim"),
    Asset(100363, "snowninja_heal_anim"),
    Asset(100364, "snowninja_hit_anim"),
    Asset(100365, "snowninja_kostart_anim"),
    Asset(100366, "snowninja_koloop_anim"),
    Asset(100367, "snowninja_move_anim"),
    Asset(100368, "snowninja_celebrate_anim"),
    Asset(100370, "snowninja_beam_anim"),
    Asset(100371, "snowninja_powercard_anim"),
    Asset(100372, "snowninja_projectileangle_anim"),
    Asset(100373, "snowninja_projectilehoriz_anim"),
    Asset(100374, "snowninja_projectilevert_anim"),
    Asset(100375, "snowninja_revive_anim"),
    Asset(100376, "snowninja_reviveothersintro_anim"),
    Asset(100377, "snowninja_reviveothersloop_anim"),
    Asset(8740003, "snowninja_igloodrop_anim1"),
    Asset(8740004, "snowninja_igloodrop_anim2"),
    Asset(8740011, "snowninja_member_revive")
]

tusk_assets = [
    Asset(100272, "ui_target_red_attack_tusk_intro"),
    Asset(100273, "ui_target_red_attack_idle_tusk_anim"),
    Asset(100291, "ui_target_green_attack_selected_intro_tusk_anim"),
    Asset(100293, "ui_target_green_idle_tusk"),
    Asset(100381, "sensei_attackstart_anim"),
    Asset(100382, "sensei_attackloop_anim"),
    Asset(100383, "sensei_idle_anim"),
    Asset(100384, "sensei_lose_anim"),
    Asset(100385, "sensei_powerupfire_anim"),
    Asset(100386, "sensei_powerupfireloop_anim"),
    Asset(100387, "sensei_powerupsnow_anim"),
    Asset(100388, "sensei_powerupsnowloop_anim"),
    Asset(100389, "sensei_powerupwater_anim"),
    Asset(100390, "sensei_powerupwaterloop_anim"),
    Asset(100391, "sensei_win_anim"),
    Asset(100271, "tusk_healthbar_animation"),
    Asset(1840002, "tusk_idle_anim"),
    Asset(1840003, "tusk_hit_anim"),
    Asset(1840005, "tusk_pushattack_anim"),
    Asset(1840006, "tusk_lose_anim"),
    Asset(1840007, "tusk_win_anim"),
    Asset(1840008, "tusk_icicle_drop_anim"),
    Asset(1840010, "tank_daze_anim"),
    Asset(8740001, "tusk_iciclesummon1_anim"),
    Asset(8740002, "tusk_iciclesummon2_anim"),
    Asset(6740001, "tusk_stun_anim"),
    Asset(1840001, "tusk_background_under"),
    Asset(6740005, "tusk_background_over"),
    Asset(6740002, "effect_tusk_push")
]

sound_assets = [
    Asset(1840002, "mus_mg_201303_cjsnow_gamewindamb"),
    Asset(1840003, "sfx_mg_2013_cjsnow_snowmantankhit"),
    Asset(1840004, "sfx_mg_2013_cjsnow_snowmanslyhit"),
    Asset(1840005, "sfx_mg_2013_cjsnow_snowmanscraphit"),
    Asset(1840006, "sfx_mg_2013_cjsnow_snowmandeathexplode"),
    Asset(1840007, "sfx_mg_2013_cjsnow_penguinground"),
    Asset(1840008, "sfx_mg_2013_cjsnow_penguinhitsuccess"),
    Asset(1840009, "sfx_mg_2013_cjsnow_snowmenappear"),
    Asset(1840010, "sfx_mg_2013_cjsnow_impactsly"),
    Asset(1840011, "sfx_mg_2013_cjsnow_impactscrap"),
    Asset(1840012, "sfx_mg_2013_cjsnow_impactpowercardsnow"),
    Asset(1840013, "sfx_mg_2013_cjsnow_footsteptank"),
    Asset(1840014, "sfx_mg_2013_cjsnow_footstepsly_loop"),
    Asset(1840015, "sfx_mg_2013_cjsnow_footstepscrap_loop"),
    Asset(1840016, "sfx_mg_2013_cjsnow_footsteppenguinfire"),
    Asset(1840017, "sfx_mg_2013_cjsnow_footsteppenguin"),
    Asset(1840018, "sfx_mg_2013_cjsnow_attackwater"),
    Asset(1840019, "sfx_mg_2013_cjsnow_attacktank"),
    Asset(1840020, "sfx_mg_2013_cjsnow_attacksnow"),
    Asset(1840021, "sfx_mg_2013_cjsnow_attacksly"),
    Asset(1840022, "sfx_mg_2013_cjsnow_attackscrap"),
    Asset(1840023, "sfx_mg_2013_cjsnow_attackpowercardwater"),
    Asset(1840024, "sfx_mg_2013_cjsnow_attackpowercardsnow"),
    Asset(1840025, "sfx_mg_2013_cjsnow_attackpowercardfire"),
    Asset(1840026, "sfx_mg_2013_cjsnow_attackfire"),
    Asset(1840028, "sfx_mg_2013_cjsnow_tusklaugh"),
    Asset(1840029, "sfx_mg_2013_cjsnow_impactsenseisnow"),
    Asset(1840030, "sfx_mg_2013_cjsnow_hittusk"),
    Asset(1840031, "sfx_mg_2013_cjsnow_hitsensei"),
    Asset(1840032, "sfx_mg_2013_cjsnow_attacktuskicicle02"),
    Asset(1840033, "sfx_mg_2013_cjsnow_attacktuskicicle01"),
    Asset(1840034, "sfx_mg_2013_cjsnow_attacktuskearthquake"),
    Asset(1840035, "sfx_mg_2013_cjsnow_attacksenseiwater"),
    Asset(1840036, "sfx_mg_2013_cjsnow_attacksenseisnow"),
    Asset(1840037, "sfx_mg_2013_cjsnow_attacksenseifire"),
    Asset(1840038, "sfx_mg_2013_cjsnow_uitargetselect"),
    Asset(1840039, "sfx_mg_2013_cjsnow_uitargetred"),
    Asset(1840040, "sfx_mg_2013_cjsnow_uiselecttile"),
    Asset(1840041, "mus_mg_201303_cjsnow_tuskthemecaveamb"),
    Asset(1840042, "SFX_MG_2013_CJSnow_UIPlayerReady_VBR8"),
    Asset(1840043, "SFX_MG_CJSnow_PowercardReviveStart"),
    Asset(1840044, "SFX_MG_CJSnow_PowercardReviveEnd")
]

SnowLobby.assets.update(common_assets)
SnowBattle.assets.update(common_assets)
SnowBattle.assets.update(ui_assets)
SnowBattle.assets.update(ninja_assets)
SnowBattle.assets.update(enemy_assets)
SnowBattle.assets.update(background_assets)
SnowBattle.sound_assets.update(sound_assets)
TuskBattle.assets.update(common_assets)
TuskBattle.assets.update(ui_assets)
TuskBattle.assets.update(tusk_assets)
TuskBattle.assets.update(ninja_assets)
TuskBattle.sound_assets.update(sound_assets)

app.session.assets.update(common_assets)
app.session.assets.update(ui_assets)
app.session.assets.update(ninja_assets)
app.session.assets.update(enemy_assets)
app.session.assets.update(background_assets)
app.session.assets.update(tusk_assets)
app.session.sound_assets.update(sound_assets)
