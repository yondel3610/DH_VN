# =============================================================================
# BRANCHING AND ENDINGS GUIDE
# =============================================================================

# -----------------------------------------------------------------------------
# HOW BRANCHING WORKS IN REN'PY
# -----------------------------------------------------------------------------
#
# 1. VARIABLES - Track player choices
#    Use 'default' to declare variables that persist across saves:
#    default niko_affection = 0
#    default feng_affection = 0
#    default cyrus_approval = 0
#
# 2. MENU STATEMENTS - Present choices to player
#    menu:
#        "Choice 1":
#            # Code for choice 1
#        "Choice 2":
#            # Code for choice 2
#
# 3. CONDITIONAL STATEMENTS - Branch based on variables
#    if niko_affection >= 3:
#        # Special scene with Niko
#    elif niko_affection >= 1:
#        # Neutral scene
#    else:
#        # Negative scene
#
# 4. FLAGS - Boolean variables for major story decisions
#    default saved_niko = False
#    default saved_svante = False
#
# 5. AFFECTION SYSTEMS - Track relationship with characters
#    default niko_affection = 0
#    default svante_affection = 0
#    default yuxuan_affection = 0
#    default chung_affection = 0
#    default magnus_affection = 0
#
# 6. ROUTE LOCKING - Determine which character route the player is on
#    if niko_affection >= 5 and niko_affection >= max(others):
#        $ current_route = "niko"
#    elif svante_affection >= 5 and svante_affection >= max(others):
#        $ current_route = "svante"
#    # etc...
#
# 7. ENDING CONDITIONS - Determine which ending player gets
#    if niko_affection >= 8 and saved_niko and current_route == "niko":
#        jump niko_true_ending
#    elif niko_affection >= 5 and current_route == "niko":
#        jump niko_good_ending
#    elif niko_affection <= 0:
#        jump niko_bad_ending
#
# 8. EXAMPLE OF AFFECTION CHOICE:
#    menu:
#        "Defend the prophets.":
#            $ niko_affection += 1
#            # Continue scene...
#        "Stay silent.":
#            $ niko_affection -= 1
#            # Continue scene...
#
# -----------------------------------------------------------------------------
# ENDING TYPES FOR DRAGON'S HEART
# -----------------------------------------------------------------------------
#
# - True Ending: Save all companions, defeat the Yaoguai King, uncover truth
# - Character Route Endings: Romance endings with each love interest
# - Good Ending: Defeat the Yaoguai King but some companions lost
# - Neutral Ending: Survive but fail to stop the threat
# - Bad Ending: Dorian dies or succumbs to darkness
# - Secret Ending: Unlock special conditions (e.g., save everyone, discover all lore)
#
# -----------------------------------------------------------------------------
# VARIABLES TO TRACK (Add to your game)
# -----------------------------------------------------------------------------
# default niko_affection = 0
# default svante_affection = 0
# default yuxuan_affection = 0
# default chung_affection = 0
# default magnus_affection = 0
# default saved_feng = False
# default saved_cyrus = False
# default saved_olympia = False
# default discovered_truth = False
# default defeated_yaoguai_king = False
# default current_route = "none"    
# default prologue_choice = ""
# default chapter1_choice = ""
# -----------------------------------------------------------------------------

# ┌─────────────────────────────────────────────────────────────────────────┐
# │  GUIDE: HOW BACKGROUNDS AND SPRITES WORK IN REN'PY                      │
# ├─────────────────────────────────────────────────────────────────────────┤
# │                                                                         │
# │  BACKGROUNDS                                                            │
# │  ───────────                                                            │
# │  'scene bg_name with transition'                                        │
# │      → Clears EVERYTHING on screen (all sprites, all overlays)          │
# │        and loads the new background image.                              │
# │      → Use this every time you change LOCATION.                         │
# │      → The old background is automatically removed — you never need     │
# │        to explicitly "hide" a background.                               │
# │                                                                         │
# │  Common transitions for backgrounds:                                    │
# │      with fade        — slow cinematic fade through black (1.0s)        │
# │      with dissolve    — cross-dissolve, smooth (0.5s)                   │
# │      with shock_cut   — instant jarring cut (violence/shock moments)    │
# │      with None        — instant hard cut (no animation at all)          │
# │                                                                         │
# │  Example location change:                                               │
# │      scene bg_tianho_dorians_room with fade                             │
# │      # ↑ Tianho: Dorian's Room fades in. Previous BG is gone.           │
# │                                                                         │
# │  SPRITES                                                                │
# │  ───────                                                                │
# │  'show character_name expression at position'                           │
# │      → Displays a character sprite at the given screen position.        │
# │      → Positions: left, center, right, truecenter                       │
# │      → 'expression' is the pose/emotion variant (e.g. happy, sad)       │
# │                                                                         │
# │  'show character_name expression'  (no position)                        │
# │      → Updates expression only, keeps the character in place.           │
# │                                                                         │
# │  'hide character_name'                                                  │
# │      → Removes the sprite from screen.                                  │
# │      → Use when a character EXITS the scene.                            │
# │      → You DON'T need to hide sprites before a 'scene' command —        │
# │        'scene' wipes them automatically.                                │
# │                                                                         │
# │  'show character_name expression at position with dissolve'             │
# │      → Fades the sprite in smoothly.                                    │
# │                                                                         │
# │  WHEN TO REMOVE A BACKGROUND / SPRITE:                                  │
# │  ───────────────────────────────────────                                │
# │  Background  → Replace it with 'scene new_bg with transition'           │
# │                whenever the scene moves to a new location.              │
# │                The old BG is gone the moment 'scene' runs.              │
# │                                                                         │
# │  Sprite      → 'hide character_name' when they physically leave.        │ 
# │                If you're about to do 'scene', skip the hide —           │
# │                'scene' clears sprites for you.                          │
# │                                                                         │
# │  FULL EXAMPLE:                                                          │
# │      scene bg_tianho_dorians_room with fade    # Room appears           │
# │      show elara happy at right with dissolve   # Elara enters           │
# │      elara "Hello!"                                                     │
# │      show elara sad                             # Expression changes    │
# │      elara "Oh no..."                                                   │
# │      hide elara with dissolve                  # Elara leaves room      │
# │      scene bg_tianho_city_night with dissolve  # CUT: city at night     │
# │      # Elara's sprite is already gone (hidden above).                   │
# │      # If we hadn't hidden her, 'scene' would have wiped her anyway.    │
# └─────────────────────────────────────────────────────────────────────────┘
#

###############################################################################
#  CONTENTS:
#    Section 1  — Character Definitions (Chapter 1 cast)
#    Section 2  — Image Declarations   (all BGs and CGs)
#    Section 3  — Audio Declarations   (all music and SFX)
#    Section 4  — Game Variables       (affection, trackers, visit flags)
#    Section 5  — label chapter_1      (Dorian's Room opening)
#    Section 6  — label ch1_city       (repeatable city exploration menu)
#    Section 7  — City sub-scenes      (Deng / Fanrong / Xiangli / Zhong)
#    Section 8  — label ch1_common_fireworks  (city convergence)
#    Section 9  — label ch1_auditions  (D2 — Niko/Kaito)
#    Section 10 — label ch1_long_shen  (D3 — Cyrus interruption)
#    Section 11 — label ch1_elara_chat (D4 — repeatable night chat)
#    Section 12 — label ch1_battle     (D5–D10 — castle battle + Taotie QTCs)
#    Section 13 — label game_over      (shared GAME OVER screen)
#    Section 14 — label ch1_common_end (post-battle convergence + epilogue)
#
#  NAMING CONVENTIONS (enforced throughout):
#    - All image tags        : lowercase, words separated by underscores
#                              e.g.  bg_tianho_dorians_room
#    - All audio variables   : lowercase, words separated by underscores
#                              e.g.  audio.ost_tianho_festival
#    - All label names       : lowercase, words separated by underscores
#                              e.g.  label ch1_city_deng
#    - All game variables    : lowercase, words separated by underscores
#                              e.g.  niko_affection
#    - Character variables   : short lowercase snake_case
#                              e.g.  long_shen, emperor_minjoon
#    NO SPACES anywhere in any tag, label, variable, or image name.
#
#  PLACEHOLDER PATHS:
#    Search "# PLACEHOLDER" to find every line that needs a real asset.
#
#  GUIDE — BACKGROUNDS, SPRITES, AND TRANSITIONS:
#    See the inline guide block in Section 2 for a full reference.
#
#  BRANCHING GUIDE:
#    See the inline guide block in Section 4 for a full explanation of
#    how affection trackers, flags, and if/elif/else drive different endings.