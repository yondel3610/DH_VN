# =============================================================================
#                               GAME VARIABLES
# =============================================================================
# prologue
default prologue_choice = ""
default quick_timer_active = False
default tutorial_shown = False

# =============================================================================
# from Chpater 1
# --- Affection / relationship trackers (persist across all chapters) ---
default niko_affection    = 0   # Niko romance/trust tracker
default feng_affection    = 0   # Feng respect/loyalty tracker

# --- Chapter-specific trackers ---
default yuki_tracker      = 0   # YUKI — unlocks Yuki-onna content in later chapters

# --- City exploration visit flags ---
# True once the player visits that location (Zhong locks after first visit)
default city_visited_deng    = False
default city_visited_fanrong = False
default city_visited_xiangli = False
default city_visited_zhong   = False   # Locks permanently after first visit

# --- Elara chat topic flags (for the repeatable D4 menu) ---
default elara_talked_cyrus   = False
default elara_talked_feng    = False
default elara_talked_olympia = False
# Note: Talking about Emperor Min-joon ends the chat loop — no flag needed

# --- Chapter 1 choice records (for optional flavour callbacks later) ---
default ch1_audition_choice  = ""   # "intervene" or "silent"
default ch1_cyrus_choice     = ""   # "obey" or "told_off"
default ch1_gate_qtc         = ""   # "nothing" / "shield" / "fireball"
default ch1_castle_qtc       = ""   # "freeze" / "spikes"
default ch1_stair_qtc        = ""   # "wind" / "stumble"

# =============================================================================
# from Chapter 2
default svante_affection     = 0      # Svante trust/romance tracker
default ice_tracker          = 0      # ICE damage — >=2 = frozen GAME OVER
default yuxuan_affection     = 0      # Yuxuan relationship tracker

default ch2_visited_food     = False  # Free time: food stalls visited
default ch2_visited_fortune  = False  # Free time: fortune teller visited
default ch2_visited_spa      = False  # Free time: spa visited
default ch2_visited_rest     = False  # Free time: rest with Vasily visited

default ch2_babala_asked_family = False  # True after Babala topic 1 chosen

default ch2_dunk_choice      = ""    # "aimed" or "missed"
default ch2_food_choice      = ""    # "confront" or "nothing"
default ch2_spa_choice       = ""    # "nothing" or "punish"
default ch2_letter_choice    = ""    # "warm" or "distant"
default ch2_qtc4             = ""    # "wind" or "dodge"
default ch2_qtc5             = ""    # "wind" or "wall"
default ch2_qtc6             = ""    # "wind_babala" or "spike"

# =============================================================================
# from Chapter 3
# --- Chapter 3 choice records ---
default ch3_d1    = ""   # "fire_circle" or "smash"
default ch3_d2    = ""   # "lure" or "stand"
default ch3_d3    = ""   # "fire_wall" or "dodge_burst"
default ch3_d4    = ""   # "dodge" (game over) or "fire_blast"
default ch3_d5    = ""   # "gave" or "refused"
default ch3_d6    = ""   # "joined" or "skipped"
default ch3_d7    = ""   # "omelette" / "soup" / "fried" / "rice"

# --- Elias question flags (for the optional question menu in ch3_truth) ---
default ch3_asked_mom       = False
default ch3_asked_amulet    = False
default ch3_asked_bodies    = False

# =============================================================================
# from Chapter 4

default chunghee_affection   = 0      # Chung-hee trust/romance tracker
# yuxuan_affection already defined in chapter_02.rpy

default ch4_yuxuan_interrupted = False  # True if player chose "Interrupt Yuxuan yourself"
default ch4_chunghee_choice    = ""     # "naive" or "inspiring" — D(Chung) speech choice
default ch4_carriage_qtc1      = ""     # "earth" or "sleep_powder"
default ch4_carriage_qtc2      = ""     # "stumble" or "wind"
default ch4_draconic_choice    = ""     # "tianho" "family" "mjoll" or "self"

# =============================================================================
# from Chapter 5
default ch5_food_choice          = ""      # "tianho" "gale" "hinami" or "mjoll"
default ch5_roboto_witness       = ""      # "yes" or "no" (Roboto stumble testimony)
default ch5_chunghee_speech      = ""      # "naive" or "inspiring"
default ch5_magnus_q1            = False   # Asked Magnus about Min-joon vision
default ch5_magnus_q2            = False   # Asked Magnus about Tragedy of Tianho
default ch5_magnus_q3            = False   # Asked Magnus about this place
default ch5_magnus_q4            = False   # Asked Magnus about the amulet

# =============================================================================
# from Chapter 6
default ch6_yaoguai_tracker  = 0    # Accumulates on wrong Yaoguai QTC answers
default ch6_d1_elias_choice  = ""
default ch6_first_qtc        = ""
default ch6_second_qtc       = ""
default ch6_vasily_qtc       = ""
default ch6_darkness_qtc     = ""
default ch6_ice_qtc          = ""

# =============================================================================
# from Chapter 7
default ch7_d1_choice         = ""    # "svante"/"niko"/"chunghee"/"yuxuan"
default ch7_drink_choice      = ""    # "drink"/"refuse"
default feng_affection        = 0
default aoi_affection         = 0

# =============================================================================
# from Chapter 8
default wing_tracker    = 0      # correct battle QTCs; >= 3 = proceed to peace
default ch8_d1_choice   = ""    # door opening: "niko"/"svante"/"yuxuan"/"chunghee"
default ch8_d2_choice   = ""    # "spearheads"/"lanterns"
default ch8_d3_choice   = ""    # "stand"/"dodge"
default ch8_d4_choice   = ""    # "fire_wind"/"earth_anchor"
default ch8_d5_choice   = ""    # "fire_magnus"/"reason"
default ch8_read_letter = False
default ch8_puzzle_seen = False
default ch8_puzzle_pass = False

# =============================================================================
# from Chapter 9
default ch9_elias_choice   = ""      # "stay" or "rush"
default ch9_lab_choice     = ""      # "library" "bedroom" "tavern" or "kitchen"
default ch9_chung_pressed  = False
default ch9_yuxuan_ate     = False
default ch9_niko_ate       = False
default ch9_svante_photo   = False
default ch9_magnus_song    = False
default ch9_story_promised = False

default huli_jing_approval  = 0     # +1 per exile judgment, max 3
default love_route_locked   = ""    # "yuxuan" "niko" "svante" "chunghee" "magnus"

# =============================================================================
# from Chapter 10
default yking_score  = 0    # +1 per correct timed choice, max 3 — gates good/bad ending
default feng_score   = 0    # +1 if Feng alerted and arrived
default aoi_score    = 0    # +1 if Aoi was present in Tianho