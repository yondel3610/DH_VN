# =============================================================================
# Centralized BG and CG .rpy file | formerly the section 2 of each chapter
# All paths are relative to the /game/ folder.
# PLACEHOLDER: Replace all path strings with real asset paths.
# =============================================================================

# =============================================================================
# Syntax: 
# image bg/cg_name:
#     "file/path"
#     size (1920, 1080) # STANDARD FOR ALL FUTURE BG
#     xalign 0.5
#     yalign 1.0
# =============================================================================

# ==============================================================
# ==============================================================
#                       PROLOGUE
# ==============================================================
# ==============================================================
image bg_underground_dim:
    "images/Assets/Background/Underground Lights Off (1).png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image bg_underground_lit:
    "images/Assets/Background/Underground.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image underground_prl:
    "images/Assets/Background/Underground_prologue.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image bg_underground_red:
    "images/Assets/Background/Underground Redpng.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image kristin_kneeling:
    "images/Assets/Illustrations/1 - Kristin Praying.png"
    fit "cover"
    xalign 0.5
    yalign 1.0
# ==============================================================
# ==============================================================
#                       CHAPTER 1
# ==============================================================
# ==============================================================

# --- Backgrounds: Dorian's Room and Hotel ---
image bg_dorians_room:
    "images/dorian_room/0F_DAY_WALL.jpg"
    size (1920, 1080) # STANDARD FOR ALL FUTURE BG
    xalign 0.5
    yalign 1.0

image bg_dorians_room_off:
    "images/dorian_room/0F_EVENING_WALL.jpg"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

# --- Backgrounds: Tianho City ---
image bg_tianho_city_night: 
    "images/Assets/Background/Tianho - night.jpg"
    size (1920, 1080) # STANDARD FOR ALL FUTURE BG
    xalign 0.5
    yalign 1.0

image bg_tianho_city_night_sleeping: # added new 
    "images/Assets/Background/Tianho - sleeping.jpg"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image bg_tianho_city_morning: # added new 
    "images/Assets/Background/Tianho Morning.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

# --- Backgrounds: City Exploration Locations ---
image bg_tianho_deng_blossom:
    "images/Assets/Background/Untitled203_20251007140552.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image bg_tianho_deng_day:
    "images/Assets/Background/Untitled203_20251001050021.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image bg_tianho_deng_night:
    "images/Assets/Background/Untitled203_20251001031452.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image bg_tianho_fanrong_square: #TODO: ask for fanrong square assets | use celeb instead if none 
    "images/Assets/Background/Tianho Celeb.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image bg_tianho_xiangli_stalls: # XIANGLI STALLS ARE def tianho food stalls from files | reuse for BG - Tianho Food Stalls diff lighting
    "images/Assets/Background/Tianho Food Stalls.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image bg_tianho_zhong_promenade: # tianho proper at night in files
    "images/Assets/Background/Tianho - night.jpg"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

# --- Backgrounds: Castle and Ceremony ---
image bg_tianho_castle_interior:
    "images/Assets/Background/throne.png" # PLACEHOLDER ASSET
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

# --- Backgrounds: Night and Dream ---
# image dorians_room_off:
#     "images/Assets/Background/bg_tianho_dorians_room_off.png"
#     size (1920, 1080)
#     xalign 0.5
#     yalign 1.0

# image bg_dream_white:
#     "images/backgrounds/bg_dream_white.png" # 
#     size (1920, 1080)
#     xalign 0.5
#     yalign 1.0

# # --- Backgrounds: Battle ---
# image bg_tianho_castle_interior_battle:
#     "images/backgrounds/bg_tianho_castle_interior_battle.png"
#     size (1920, 1080)
#     xalign 0.5
#     yalign 1.0

image bg_tianho_city_on_fire:
    "images/Assets/Background/Tianho in fire.jpg" # city proper on fire | to be used for battle part of chapter 1
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image tianho_food_stalls_fire: # TIANHO FOOD STALLS ON FIRE ASSET | to be used for battle part of chapter 1
    "images/Assets/Background/Tianho Food Stalls on fire.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image bg_tianho_underground_2:
    "images/Assets/Background/Underground Lights Off (1).png" # TODO: check if correct
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image bg_tianho_throne:
    # "images/Assets/Background/throne.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

# ==============================================================
# TODO: NOTE: some CGs are transparent pngs
image cg_blindinglight: # vasily's powers 9when vasily uses flash or blinding light)
    "images/cg/cg_blindinglight_vasily.jpg"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_dorian_w_kids:
    "images/Assets/Illustrations/2 - Dorian with Elara and Kids.jpeg"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_emperor_arrival:
    "images/Assets/Illustrations/4 - Empress Olympia and Minjoon.png"
    size(1620, 1080)
    xalign 0.5
    yalign 1.0

image cg_taotie_fight:
    "images/Assets/Illustrations/6 - Taotie Fight.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_feng_eye_injury:
    "images/Assets/Illustrations/7 - Taotie scratches Feng_s eye.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_elara_children_death:
    "images/Assets/Illustrations/8 - Yaoguai King kills Elara.jpeg"     
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

# ==============================================================
# ==============================================================
#                       CHAPTER 2
# ==============================================================
# ==============================================================
# --- Backgrounds: Mjoll Exterior ---
image bg_mjoll_icelands: # also mjoll townsquare in pdf
    "images/Assets/Background/Mjoll.jpg"            
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image bg_mjoll_blizzard:
    "images/Assets/Background/Mjoll - blizzard.png"            
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

# --- Backgrounds: Mjoll Palace ---
image bg_mjoll_palace_throne_lightsoff:
    "images/Assets/Background/Mjoll - lights off - throne off.png"           
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image mjoll_palace_throne:
    "images/Assets/Background/Mjoll - throne room.png"           
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image frostcradle_blizzard: # BG – Icelands in pdf   
    "images/Assets/Background/Frostcradle - Blizzard.png"         
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image frostcradle_no_blizzard: # BG - Frostcradle - Normal in pdf
    "images/Assets/Background/Frostcradle - No blizzard.png"     
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image frostcradle_cabin:
    "images/Assets/Background/Frostcradle - cabin inside.png"         
    # fit "cover"
    zoom 0.908
    xalign 0.5
    yalign 1.0

image frostcradle_cabin_on:
    "images/Assets/Background/Frostcradle - lights on -  cabin inside.jpg"         
    # size (1920, 1080)
    zoom 0.908
    xalign 0.5
    yalign 1.0

image bg_frostcradle_cave: # Inside the Frostcradle in pdf
    "images/Assets/Background/Frostcradle - Inside cave.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

# # --- Backgrounds: Dorian's Cave ---
image dorians_cave:
    "images/Assets/Background/dorian_cave.jpg"
    size (1920, 1080) # STANDARD FOR ALL FUTURE BG
    xalign 0.5
    yalign 1.0

image lab_cave_on:
    "images/Assets/Background/lab_cave_on.png"
    size (1920, 1080) # STANDARD FOR ALL FUTURE BG
    xalign 0.5
    yalign 1.0

image lab_cave_off:
    "images/Assets/Background/lab_cave_off.png"
    size (1920, 1080) # STANDARD FOR ALL FUTURE BG
    xalign 0.5
    yalign 1.0

image violet_tent:
    "images/Assets/Background/violet_tent.png"
    fit "cover" 
    xalign 0.5
    yalign 1.0

# ==============================================================
image cg_qiongqi_fight:
    "images/Assets/Illustrations/9 -Quiongqi Fight.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_dorian_vs_yuki:
    "images/Assets/Illustrations/12 - Dorian fight Yuki-onna.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_yuki_cry:
    "images/Assets/Illustrations/13 - Yuki-onna cry.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_dorian_hug_elias:
    "images/Assets/Illustrations/15 - Dorian Elias hug.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_family_into_light:
    "images/Assets/Illustrations/17 - Elara, Daniel, Sarah, Emily, Lucas walk into the light.png"
    zoom 0.65
    xalign 0.5
    yalign 1.0

image cg_trio_in_frostcradle:
    "images/Assets/Illustrations/18 , 19 - Yuxuan, Elias, Dorian in Frostcradle.png"
    # size (1920, 1080)
    zoom 0.65
    xalign 0.5
    yalign 1.0

# ==============================================================
# ==============================================================
#                       THE REST OF THE BG/CG
# ==============================================================
# ==============================================================

# CG 
image plain_white: # for dream sequences or talking to the dead
    "images/cg/plain_white.jpg"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image vasily_attack:
    "images/Assets/Illustrations/10 - vasily attack.jpg"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_kristin_death:
    "images/Assets/Illustrations/20 - Kristin getting killed.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_elias_arrow:
    "images/Assets/Illustrations/21 - Elias getting hit by arrow.jpeg"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_mjoll_massacre:
    "images/Assets/Illustrations/22 - The Massacrer of Mjoll.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image niko_raven:
    "images/Assets/Illustrations/22.1 - Raven.png"
    # fit "contain"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image soldiers_charging:
    "images/Assets/Illustrations/22.2 - SoldiersCharging.png"
    fit "contain"
    xalign 0.5
    yalign 1.0

image cg_dorian_to_family:
    "images/Assets/Illustrations/23 - Dorian paying respects to his family.jpeg"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_niko_save_chung:
    "images/Assets/Illustrations/26 - Niko saves Chung.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_svante_save_chung:
    "images/Assets/Illustrations/27 - Svante saves Chung.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_dorian_redirects:
    "images/Assets/Illustrations/28 - Dorian redirects.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_prosperity_dragon:
    "images/Assets/Illustrations/29 - ProsperityDragon.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_weng_cooking:
    "images/Assets/Illustrations/31 - Weng cooking.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_tim_and_elias:
    "images/Assets/Illustrations/32 - Tim and Elias.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_hundun_attack:
    "images/Assets/Illustrations/32.5 - Hundun attacks.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_chung_slay_hundun:
    "images/Assets/Illustrations/33 - Chung hee slays hundun colored.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_feng_aoi:
    "images/Assets/Illustrations/34 - Feng and Aoi.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_roboto_yuxuan:
    "images/Assets/Illustrations/41 - Roboto carrying Yuxuan_s.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_magnus_battle:
    "images/Assets/Illustrations/42 - Magnus Battle.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_aoi_singing:
    "images/Assets/Illustrations/47 - Aoi singing.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_men_trapped:
    "images/Assets/Illustrations/48 - The men trapped.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_tim_powers:
    "images/Assets/Illustrations/48.5 - Tim shows his powers.jpeg"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_elias_release:
    "images/Assets/Illustrations/49 - Elias releases.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_elias_release_surprised:
    "images/Assets/Illustrations/49.5 - Elias releases surprised.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_dorian_yuxian:
    "images/Assets/Illustrations/50 - Yuxuan kiss Dorian on the cheek.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_dorian_chung:
    "images/Assets/Illustrations/51 - Chung-hee saves Dorian.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_dorian_svante:
    "images/Assets/Illustrations/52 - Svante rests his head.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_dorian_niko:
    "images/Assets/Illustrations/53 - Niko gives charm.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_dorian_magnus:
    "images/Assets/Illustrations/54 - Magnus and Dorian fall down.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_festivities:
    "images/Assets/Illustrations/55 - Festivities.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_yuxuan_saves_dorian:
    "images/Assets/Illustrations/56 - Yuxuan saves Dorian.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_chung_saves_dorian:
    "images/Assets/Illustrations/57 - Chung-hee saves Dorian.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_niko_saves_dorian:
    "images/Assets/Illustrations/58 - Niko saves Dorian.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_svante_saves_dorian:
    "images/Assets/Illustrations/59 - Svante saves Dorian.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_magnus_saves_dorian:
    "images/Assets/Illustrations/60 - Magnus saves Dorian.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

# BG
image tianho_cemetery_morning:
    "images/Assets/Background/Tianho Cemetery Day.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image tianho_cemetery_afternoon:
    "images/Assets/Background/Tianho Cemetery Afternoon.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image tianho_cemetery_morning_alt:
    "images/Assets/Background/tianho_cemetery_morning.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image tianho_cemetery_night:
    "images/Assets/Background/Tianho Cemetery Night.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image underground_magnus:
    "images/Assets/Background/Underground - Magnus.jpg"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image yuxuan_carriage:
    "images/Assets/Background/carriage_visual_novel_bg_by_gin_1994.jpg" # image taken online | placeholder unless no art is given
    fit "contain"
    xalign 0.5
    yalign 1.0

image yuxuan_manor:
    "images/Assets/Background/yuxuan manor.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image yuxuan_manor_off:
    "images/Assets/Background/yuxuan manor dimmed.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image yuxuan_lab_hotspring:
    "images/Assets/Background/Yuxuan_s lab - Hot spring.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image spare_room:
    "images/Assets/Background/Spare Room.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image spare_room_off:
    "images/Assets/Background/Spare Room Lights Off.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image storage_room:
    "images/Assets/Background/Storage Room.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image storage_room_off:
    "images/Assets/Background/Storage Room Lights Off.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image hinami_castle_morning:
    "images/Assets/Background/Hinami Castle Morning.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image hinami_castle_evening:
    "images/Assets/Background/Hinami Castle Evening.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image kyeonjang_palace:
    "images/Assets/Background/throne.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image kyeonjang_room:
    "images/Assets/Background/Kyeongjang Room No Blinders 2.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image kyeonjang_room_blinders:
    "images/Assets/Background/Kyeongjang Room Blinders.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image destroyed_land: # to be used when chung hee appears 
    "images/Assets/Background/Destroyed Land.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cheng_industries_bunk:
    "images/Assets/Background/Cheng industries bunk - lights on.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cheng_industries_bunk_off:
    "images/Assets/Background/Cheng industries bunk - lights off.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image yuxuan_carriage:
    "images/Assets/Background/carriage_visual_novel_bg_by_gin_1994.jpg" # TODO: add credits
    xalign 0.5
    yalign 1.0
    zoom 2.5

image underground_door:
    "images/Assets/Background/wmremove-transformed.png"
    fit "contain"
    zoom 1.02
    xalign 0.5
    yalign 1.0

image underground_door_scan:
    "images/Assets/Background/UndergroundDoorScanning.png"
    fit "contain"
    # zoom 1.1
    xalign 0.5
    yalign 1.0