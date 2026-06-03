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
#                       CHAPTER 1
# ==============================================================
# ==============================================================

# --- Backgrounds: Dorian's Room and Hotel ---
# image dorians_room:
#     "images/Assets/Background/bg_tianho_dorians_room.png"
#     size (1920, 1080) # STANDARD FOR ALL FUTURE BG
#     xalign 0.5
#     yalign 1.0

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
    "images/Assets/Background/throne.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

# ==============================================================
# TODO: NOTE: some CGs are transparent pngs
image cg_blindinglight:
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

image frostcradle_no_blizzard:
    "images/Assets/Background/Frostcradle - No blizzard.png"     
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image frostcradle_cabin:
    "images/Assets/Background/Frostcradle - cabin inside.png"         
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image frostcradle_cabin_on:
    "images/Assets/Background/Frostcradle - lights on -  cabin inside.jpg"         
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image bg_frostcradle_cave: # Inside the Frostcradle in pdf
    "images/Assets/Background/Frostcradle - Inside cave.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

# # --- Backgrounds: Dorian's Cave ---
image dorians_cave_on:
    "images/Assets/Background/dorians_cave_on.png"
    size (1920, 1080) # STANDARD FOR ALL FUTURE BG
    xalign 0.5
    yalign 1.0

image dorians_cave_off:
    "images/Assets/Background/dorians_cave_off.png"
    size (1920, 1080) # STANDARD FOR ALL FUTURE BG
    xalign 0.5
    yalign 1.0

# image violet_tent:
#     "images/Assets/Background/"
#     size (1920, 1080) 
#     xalign 0.5
#     yalign 1.0

# image bg_mjoll_square_festive:
#     "images/Assets/Background/"
#     size (1920, 1080) 
#     xalign 0.5
#     yalign 1.0

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
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

image cg_trio_in_frostcradle:
    "images/Assets/Illustrations/18 , 19 - Yuxuan, Elias, Dorian in Frostcradle.png"
    size (1920, 1080)
    xalign 0.5
    yalign 1.0

