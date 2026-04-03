###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  FILE:  chapter_03.rpy
#  SCENE: CHAPTER 3 — Frostcradle: The Child in the Ice
#
#  CONTENTS:
#    Section 1  — Character Definitions
#    Section 2  — Image Declarations  (backgrounds, CGs, sprites)
#    Section 3  — Audio Declarations  (music, SFX, ambient)
#    Section 4  — Game Variables      (trackers, flags, choice records)
#    Section 5  — label chapter_3     (opening — journey to Frostcradle)
#    Section 6  — label ch3_mine      (entering the mine / bodies)
#    Section 7  — label ch3_yuki_boss (Yuki-onna boss fight — D1–D4 QTCs)
#    Section 8  — label ch3_truth     (Elias found / Ekaterina's ghost)
#    Section 9  — label ch3_elias_questions (D — optional questions to Elias)
#    Section 10 — label ch3_blizzard_trapped (blizzard days begin)
#    Section 11 — label ch3_yuxuan_arrives   (supply bot / hologram scene)
#    Section 12 — label ch3_mushroom  (D6 — mushroom invitation with Yuxuan)
#    Section 13 — label ch3_breakfast (D7 — 4-option cooking choice)
#    Section 14 — label ch3_vasily_arrives   (Vasily battalion + Kristin death)
#    Section 15 — label ch3_critical_fork    (D5 — give or protect Elias)
#    Section 16 — label ch3_bad_end          (BAD ENDING — give Elias)
#    Section 17 — label ch3_fight_back       (GOOD PATH — draconic fire awakens)
#    Section 18 — label ch3_escape           (escape with Yuxuan; chapter end)
#
#  NAMING CONVENTIONS (enforced throughout):
#    image tags      — bg_name, cg_name, character_name emotion
#    audio variables — audio.ost_name, audio.sfx_name, audio.amb_name
#    label names     — ch3_name (all lowercase, underscores only)
#    game variables  — yuki_tracker, svante_affection, yuxuan_affection, etc.
#    NO SPACES in any tag, label, variable, or image name.
#
#  TRACKER SUMMARY:
#    yuki_tracker      : accumulates in D1–D4; ≥2 = GAME OVER after D4
#    svante_affection  : +1 if D5 = Refuse and fight
#    yuxuan_affection  : +2 if D6 = Join Yuxuan; -1 if D6 = Don't join
#    D7 (cooking)      : 4 soft-branch options; no stat effect
#
#  HARD GATES:
#    D4 wrong answer (dodge instead of fire blast) = GAME OVER
#    D4 correct but yuki_tracker >= 2 = GAME OVER (frost overwhelm)
#    D5 = Give Elias → BAD ENDING branch (irreversible)
#
#  PLACEHOLDER PATHS:
#    Search "# PLACEHOLDER" to find every line that needs a real asset.
###############################################################################


# =============================================================================
# SECTION 1: CHARACTER DEFINITIONS
# =============================================================================
# Characters from prologue.rpy, chapter_01.rpy, and chapter_02.rpy are
# already loaded by Ren'Py — do NOT redefine them here.
# Only NEW characters introduced in Chapter 3 are defined below.
# =============================================================================

define yuki_onna      = Character("Yuki-onna",         color="#aee8f8")  # Pale ice blue — spirit form
define ekaterina_ghost= Character("Queen Ekaterina",   color="#d8b4fe")  # Soft violet — ghost/vision
define elias          = Character("Elias",             color="#fcd34d")  # Warm yellow — toddler, innocent
define niko_raven     = Character("Niko",              color="#e0c8a0")  # Parchment — raven form
define weng           = Character("Miss Weng",         color="#f97316")  # Orange — Yuxuan's chef/caretaker
define boy_ald_soldier= Character("Boy Aldorith",      color="#cd5c5c")  # Muted red — Gustav's soldier
define girl_ald_soldier=Character("Girl Aldorith",     color="#cd5c5c")  # Muted red — Gustav's soldier


# =============================================================================
# SECTION 2: IMAGE DECLARATIONS
# =============================================================================
# Naming convention:
#   bg_  = background scene
#   cg_  = full-screen event illustration
#   Sprites: "character_name emotion"  (two-word tag, underscores between words)
#
# All paths are relative to the /game/ folder.
# Search "# PLACEHOLDER" to find every line needing a real asset.
# =============================================================================

# --- Backgrounds: Journey and Exterior ---
image bg_mjoll_icelands_journey  = "images/backgrounds/bg_mjoll_icelands_journey.png"    # PLACEHOLDER
# Dorian trekking alone through deep snow toward the Iceclaw Pass; mountains ahead

image bg_frostcradle_exterior    = "images/backgrounds/bg_frostcradle_exterior.png"      # PLACEHOLDER
# Frostcradle mine entrance — gaping maw in the mountainside; jagged icicle framing

# --- Backgrounds: Inside Frostcradle ---
image bg_frostcradle_interior    = "images/backgrounds/bg_frostcradle_interior.png"      # PLACEHOLDER
# Deep mine tunnel — bodies frozen mid-pose; icicles jutting from walls and ceiling

image bg_frostcradle_boss_arena  = "images/backgrounds/bg_frostcradle_boss_arena.png"    # PLACEHOLDER
# Wide underground chamber — crystalline ice floor; eerie blue light; Yuki-onna's domain

image bg_frostcradle_blizzard    = "images/backgrounds/bg_frostcradle_blizzard.png"      # PLACEHOLDER
# Same interior chamber but blizzard howling through cracks; snow billowing inside

image bg_frostcradle_aftermath   = "images/backgrounds/bg_frostcradle_aftermath.png"     # PLACEHOLDER
# Frostcradle post-battle — scorched walls, steam rising from melted ice, charred remains

# --- Backgrounds: The Shack ---
image bg_shack_interior          = "images/backgrounds/bg_shack_interior.png"            # PLACEHOLDER
# Crude wooden shack inside the mine — lantern, makeshift straw bed, small firepit

image bg_shack_morning           = "images/backgrounds/bg_shack_morning.png"             # PLACEHOLDER
# Same shack, daylight filtering through cracks; warmer, cozy, Elias's drawings on wall

# --- Backgrounds: Vision / White World ---
image bg_white_void              = "images/backgrounds/bg_white_void.png"                # PLACEHOLDER
# Pure white — used for Ekaterina's ghost vision and Magnus's amulet flash

image bg_mjoll_palace_vision     = "images/backgrounds/bg_mjoll_palace_vision.png"       # PLACEHOLDER
# Desaturated/ghostly Mjoll palace — Gustav's study; tinted cold blue for vision sequence

# --- Backgrounds: Bad Ending ---
image bg_mjoll_town_normal       = "images/backgrounds/bg_mjoll_town_normal.png"         # PLACEHOLDER
# Mjoll town square in peace — years later; prosperous but hollow

image bg_mjoll_palace_normal     = "images/backgrounds/bg_mjoll_palace_normal.png"       # PLACEHOLDER
# Gustav's palace in normal lighting — wealth, chandeliers, parties in background

image bg_mjoll_cliffside         = "images/backgrounds/bg_mjoll_cliffside.png"           # PLACEHOLDER
# Cliff edge in moonlight — vast frozen wasteland below; Dorian's suicide scene

# --- Backgrounds: Escape ---
image bg_carriage_interior       = "images/backgrounds/bg_carriage_interior.png"         # PLACEHOLDER
# Interior of Yuxuan's carriage — cushioned benches, warm blankets, window to snowy road

# --- CGs (Full-screen Event Illustrations) ---
image cg_yuki_onna_reveal        = "images/cg/cg_yuki_onna_reveal.png"                   # PLACEHOLDER
# Yuki-onna emerging from the darkness — translucent form, frost trailing bare feet

image cg_ice_wall_smash          = "images/cg/cg_ice_wall_smash.png"                     # PLACEHOLDER
# Dorian's fist striking the ice wall — frost crawling up his arm (wrong D1 choice)

image cg_ice_spear_deflect       = "images/cg/cg_ice_spear_deflect.png"                  # PLACEHOLDER
# Dorian rolling aside from spear shards, fire burst mid-dodge (correct D3)

image cg_yuki_onna_shatter       = "images/cg/cg_yuki_onna_shatter.png"                  # PLACEHOLDER
# Yuki-onna shattering into snowflakes — fire blast from Dorian's concentrated beam

image cg_dorian_frozen_ch3       = "images/cg/cg_dorian_frozen_ch3.png"                  # PLACEHOLDER
# Dorian encased in spreading frost — GAME OVER image for YUKI tracker fail

image cg_elias_found             = "images/cg/cg_elias_found.png"                        # PLACEHOLDER
# Elias in the corner of the shack — toddler with wooden spoon, terrified eyes

image cg_ekaterina_vision        = "images/cg/cg_ekaterina_vision.png"                   # PLACEHOLDER
# Queen Ekaterina's ghost — ethereal, snow swirling, mournful smile, hand raised

image cg_ekaterina_sacrifice     = "images/cg/cg_ekaterina_sacrifice.png"                # PLACEHOLDER
# Ekaterina plunging the blade into her chest — the sacrifice vision; stark and devastating

image cg_elias_hug               = "images/cg/cg_elias_hug.png"                          # PLACEHOLDER
# Elias throwing his arms around Dorian's neck — desperate, clinging, warm

image cg_supply_bot_arrives      = "images/cg/cg_supply_bot_arrives.png"                 # PLACEHOLDER
# The Cheng Industries supply bot rolling into the shack; Elias's eyes wide with wonder

image cg_family_farewell         = "images/cg/cg_family_farewell.png"                    # PLACEHOLDER
# Dream: Elara and the four children fading into golden light — Dorian's goodbye vision

image cg_kristin_death           = "images/cg/cg_kristin_death.png"                      # PLACEHOLDER
# Kristin crumpling in the snow — blade strike mid-sentence; blood pooling

image cg_elias_shot              = "images/cg/cg_elias_shot.png"                         # PLACEHOLDER
# Arrow striking Elias — he crumples; Dorian's hand reaching in horror

image cg_draconic_fire_awakens   = "images/cg/cg_draconic_fire_awakens.png"              # PLACEHOLDER
# Dorian's body erupting in gold-crimson draconic fire — flames warping the air

image cg_battalion_falls         = "images/cg/cg_battalion_falls.png"                    # PLACEHOLDER
# Wide-angle: the entire battalion consumed by fire and earth — smoke, steam, chaos

image cg_svante_falls            = "images/cg/cg_svante_falls.png"                       # PLACEHOLDER
# Svante's foot slipping on crumbling ground — falling; arms outstretched

image cg_bad_end_cliff           = "images/cg/cg_bad_end_cliff.png"                      # PLACEHOLDER
# Dorian at the cliff edge — pale moonlight, foot at the rim, looking down

image cg_escape_carriage         = "images/cg/cg_escape_carriage.png"                    # PLACEHOLDER
# Yuxuan's carriage rolling through snow — Dorian and Elias visible inside window

image cg_chaos_images            = "images/cg/cg_chaos_images.png"                       # PLACEHOLDER
# Abstract chaotic flash: Magnus's winged silhouette, fractured visions, blinding light

image cg_black                   = "images/cg/cg_black.png"                              # PLACEHOLDER
# Pure black — fade-outs, unconscious moments, chapter transitions


# =============================================================================
# SECTION 3: AUDIO DECLARATIONS
# =============================================================================
# All audio used in Chapter 3.
# Format:  define audio.name = "path/to/file.ogg"
# PLACEHOLDER: Replace each path with your real .ogg audio file.
# =============================================================================

# --- Music ---
define audio.ost_frostcradle_approach = "audio/music/ost_frostcradle_approach.ogg"  # PLACEHOLDER
# Tense, sparse — solo trek through Iceclaw Pass; strings and distant wind instruments

define audio.ost_yuki_onna_battle     = "audio/music/ost_yuki_onna_battle.ogg"      # PLACEHOLDER
# Ethereal yet urgent — Yuki-onna fight; crystalline tones over driving percussion

define audio.ost_ekaterina_truth      = "audio/music/ost_ekaterina_truth.ogg"       # PLACEHOLDER
# Mournful and haunting — the ghost's revelation; solo cello or viola

define audio.ost_blizzard_days        = "audio/music/ost_blizzard_days.ogg"         # PLACEHOLDER
# Quiet, intimate warmth — days in the shack; acoustic strings, gentle piano

define audio.ost_supply_bot_jingle    = "audio/music/ost_supply_bot_jingle.ogg"     # PLACEHOLDER
# The Cheng Industries jingle — cheerful, slightly off-key; brief comedic earworm

define audio.ost_mushroom_walk        = "audio/music/ost_mushroom_walk.ogg"         # PLACEHOLDER
# Tender, curious — Yuxuan mushroom scene; soft piano with gentle warmth

define audio.ost_vasily_arrives       = "audio/music/ost_vasily_arrives.ogg"        # PLACEHOLDER
# Low, dread-filled — Vasily's battalion marching; military drums beneath dark strings

define audio.ost_critical_fork        = "audio/music/ost_critical_fork.ogg"         # PLACEHOLDER
# Suspended tension — the choice moment; near-silence with a single high string note

define audio.ost_bad_end_luxury       = "audio/music/ost_bad_end_luxury.ogg"        # PLACEHOLDER
# Hollow grandeur — the BAD END years; waltz tempo that feels empty and wrong

define audio.ost_draconic_awakening   = "audio/music/ost_draconic_awakening.ogg"    # PLACEHOLDER
# Explosive, divine rage — draconic fire erupts; full orchestra, brass-forward

define audio.ost_escape_carriage      = "audio/music/ost_escape_carriage.ogg"       # PLACEHOLDER
# Bittersweet relief — riding to Tianho; gentle melody with warmth returning

define audio.ost_family_dream         = "audio/music/ost_family_dream.ogg"          # PLACEHOLDER
# Gentle, fading — the family farewell dream; the same theme as ost_cave_grief, quieter

# --- Sound Effects ---
define audio.sfx_yuki_scream          = "audio/sfx/sfx_yuki_scream.ogg"             # PLACEHOLDER
define audio.sfx_ice_wall_crash       = "audio/sfx/sfx_ice_wall_crash.ogg"          # PLACEHOLDER
define audio.sfx_ice_spear_launch     = "audio/sfx/sfx_ice_spear_launch.ogg"        # PLACEHOLDER
define audio.sfx_fire_blast           = "audio/sfx/sfx_fire_blast.ogg"              # PLACEHOLDER
define audio.sfx_fire_burst           = "audio/sfx/sfx_fire_burst.ogg"              # PLACEHOLDER
define audio.sfx_frost_crawl          = "audio/sfx/sfx_frost_crawl.ogg"             # PLACEHOLDER
define audio.sfx_amulet_surge         = "audio/sfx/sfx_amulet_surge.ogg"            # PLACEHOLDER
define audio.sfx_heartbeat            = "audio/sfx/sfx_heartbeat.ogg"               # PLACEHOLDER
define audio.sfx_arrow_hit            = "audio/sfx/sfx_arrow_hit.ogg"               # PLACEHOLDER
define audio.sfx_earth_eruption       = "audio/sfx/sfx_earth_eruption.ogg"          # PLACEHOLDER
define audio.sfx_draconic_roar        = "audio/sfx/sfx_draconic_roar.ogg"           # PLACEHOLDER
define audio.sfx_blade_strike         = "audio/sfx/sfx_blade_strike.ogg"            # PLACEHOLDER
define audio.sfx_carriage_rumble      = "audio/sfx/sfx_carriage_rumble.ogg"         # PLACEHOLDER
define audio.sfx_thunder_vision       = "audio/sfx/sfx_thunder_vision.ogg"          # PLACEHOLDER

# --- Ambient ---
define audio.amb_frostcradle_wind     = "audio/ambient/amb_frostcradle_wind.ogg"    # PLACEHOLDER
# Cold hollow echo — wind through the mine tunnels; looping; plays through most mine scenes

define audio.amb_blizzard_howl        = "audio/ambient/amb_blizzard_howl.ogg"       # PLACEHOLDER
# Heavy blizzard roar — looping; the trapped days in the shack

define audio.amb_shack_fire           = "audio/ambient/amb_shack_fire.ogg"          # PLACEHOLDER
# Soft fireplace crackle — looping; warm counterpoint to the blizzard outside

define audio.amb_carriage_wheels      = "audio/ambient/amb_carriage_wheels.ogg"     # PLACEHOLDER
# Steady wheel-on-road rhythm — looping; escape carriage scene


# =============================================================================
# SECTION 4: GAME VARIABLES
# =============================================================================
# Variables set in Chapter 3. Trackers persist into later chapters.
#
# TRACKER SUMMARY:
#   yuki_tracker      — accumulates during the boss fight (D1–D4)
#                       ≥2 after D4 correct answer = GAME OVER (frost too deep)
#                       D4 wrong answer (dodge) = instant GAME OVER
#   svante_affection  — +1 if D5 = Refuse and fight (seeds Chapter 4 trust)
#   yuxuan_affection  — +2 if D6 = Join Yuxuan; -1 if D6 = Don't join
#
# NOTE: yuki_tracker was first seeded in chapter_01.rpy (stumble on stairs).
#       It is NOT re-defaulted here — it persists from Ch1 and accumulates.
#       If yuki_tracker was already 1 from Chapter 1, it carries into this fight.
#
# CHOICE RECORDS (for optional flavour callbacks in later chapters):
#   ch3_d1, ch3_d2, ch3_d3, ch3_d4   — boss fight QTC choices
#   ch3_d5                             — "gave" or "refused" (critical fork)
#   ch3_d6                             — "joined" or "skipped"
#   ch3_d7                             — "omelette" / "soup" / "fried" / "rice"
# =============================================================================

# --- New trackers introduced in Chapter 3 ---
# yuki_tracker already declared in chapter_01.rpy — not redeclared here

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
# SECTION 5: LABEL CHAPTER_3 — Opening (Journey to Frostcradle)
# =============================================================================
# Entry point — jumped to from chapter_02.rpy via 'jump chapter_3'.
# Dorian sets out alone into the blizzard toward Frostcradle.
# His family's ghost-voices accompany him as comfort.
# =============================================================================

label chapter_3:

    # -------------------------------------------------------------------------
    # OPENING — Trek through the Iceclaw Pass
    # BG: bg_mjoll_icelands_journey
    # Music: ost_frostcradle_approach (tense, sparse)
    # -------------------------------------------------------------------------

    scene cg_black with fade                            # PLACEHOLDER — carry from ch2 end
    pause 1.0

    # Chapter title card — uses screen defined in prologue.rpy
    show screen chapter_title_screen(
        "3",
        "Frostcradle",
        subtitle="The Child in the Ice",
        duration=3.0
    )
    pause 3.0

    scene bg_mjoll_icelands_journey with fade           # PLACEHOLDER — solo trek, deep snow
    play music ost_frostcradle_approach fadein 2.0      # PLACEHOLDER — tense approach OST
    play audio amb_frostcradle_wind loop fadein 1.5     # PLACEHOLDER — hollow mine wind

    "The wind howled like a living thing as I trudged westward. Each step was a battle against the biting cold that seeped through every layer of clothing I wore."
    "My boots crunched against the frost-bitten ground, the sound muffled by the relentless storm."
    "If it wasn't for my fire channeling gift, I would have frozen by now."
    "The snow grew deeper as I climbed higher, the jagged peaks of the Iceclaw Pass looming in the distance."

    # Family ghost-voices — no sprites; they exist only as warmth in Dorian's mind
    elara "We're almost there, my heart. Let's keep moving."
    lucas "Let's go, dad! We're almost at the Frost… Frostcray—"
    emily "It's Frostcradle, Lucas."

    "I adjusted my pack and pressed on."
    "It felt like hours. The further I went, the quieter the world became."
    "Then, I saw it."

    # -------------------------------------------------------------------------
    # FROSTCRADLE EXTERIOR
    # BG: bg_frostcradle_exterior
    # -------------------------------------------------------------------------

    scene bg_frostcradle_exterior with dissolve         # PLACEHOLDER — mine entrance, icicle framing

    sarah "Look, daddy! The Frostcradle!"
    lucas "It… doesn't look like a cradle."
    emily "Maybe it's just a metaphor, Lucas."
    elara "Dorian… are you ready?"

    "I nodded, taking a deep breath."

    jump ch3_mine


# =============================================================================
# SECTION 6: LABEL CH3_MINE — Entering the Mine / Bodies
# =============================================================================
# Dorian enters and finds the frozen corpses of all who tried to reach Elias.
# The Yuki-onna is first seen and speaks. Battle begins.
# =============================================================================

label ch3_mine:

    scene bg_frostcradle_interior with dissolve         # PLACEHOLDER — mine tunnel interior

    "I entered the mine, and it was as silent as a graveyard."
    "The first body I found wasn't whole."
    "An aldorith. His hair was frozen to the icy floor, his body contorted unnaturally. Jagged shards of ice jutted through his chest and limbs like stakes."
    "His eyes were wide open, clouded over with frost, his face twisted into a silent scream."

    elara "It's cruel, my heart… Who would do such a thing…"

    "Further inside, it became worse."
    "A soldier, frozen mid-run, his arm outstretched toward something — or someone. His other arm was embedded in a wall of ice."
    "I could see his teeth through his partially frozen, shattered cheek, his mouth frozen wide as though he had been begging for mercy."

    daniel "Dad… Be brave. Like you taught me."
    dorian "I will, Daniel. Thank you."
    sarah  "Go, dad! Go!"

    "I swallowed hard, shaking my head. I balled up my fists, the leather gloves worn and familiar."
    "I pushed forward, every step crunching against frost and ice. I found more bodies. Mercenaries this time. One hung suspended from the ceiling, impaled by an icicle that had burst through his abdomen."

    emily  "Dad… Last chance. Do you really want to go this far?"
    dorian "We're here now, Emily. No turning back."

    "The words echoed in the cavern, bouncing off the icy walls. For a moment, even the voices of my family fell silent."
    "And then I heard her. And saw her."

    # CG: Yuki-onna first reveal — full screen, shock cut
    play sfx sfx_yuki_scream                            # PLACEHOLDER — yuki wail SFX
    scene cg_yuki_onna_reveal with shock_cut            # PLACEHOLDER — cg_yuki_onna_reveal
    pause 1.0
    scene bg_frostcradle_interior with dissolve         # Return to mine bg

    yuki_onna "Leave… now…"

    "I turned toward the voice. She wasn't human."
    "Translucent skin, pale as fresh snow, glowed faintly in the darkness. Frost trailed from her bare feet, spreading like veins over the ground."

    yuki_onna "Like ice, life is very fragile… I told you… Leave…"

    "The cold thickened, pressing against my lungs, numbing my fingers even as I summoned my fire to fight it off. The flames sputtered faintly."

    yuki_onna "Again… Leave… now…"
    dorian    "Who are you?!"

    "She didn't answer. Instead, she stepped closer, her form gliding across the icy terrain as though she were weightless."
    "Then I felt it. The death god's energy radiating from her, sharp and suffocating, like a thousand needles pressing into my skin."

    elara     "Dorian, be careful."
    dorian    "I will."

    "And the flames around me surged brighter."

    yuki_onna "One last chance… Leave now… or die…"

    jump ch3_yuki_boss


# =============================================================================
# SECTION 7: LABEL CH3_YUKI_BOSS — Yuki-onna Boss Fight (D1–D4 QTCs)
# =============================================================================
# Four timed choices. yuki_tracker accumulates on wrong answers.
# D4 wrong answer = instant GAME OVER.
# D4 correct but yuki_tracker >= 2 = GAME OVER (frost too deep to survive).
#
# QTC NOTE: All menus are standard 'menu:' blocks for playtesting.
# Replace with 'call screen timed_choice([...])' once the QTE UI is ready.
# =============================================================================

label ch3_yuki_boss:

    scene bg_frostcradle_boss_arena with dissolve       # PLACEHOLDER — boss arena, crystalline ice
    play music ost_yuki_onna_battle fadein 1.0          # PLACEHOLDER — Yuki-onna battle OST

    yuki_onna "Leave us!"

    elara "My heart, use your fire!"

    "She moved again, her form darting across the battlefield like a specter, each step leaving trails of ice and frost."
    "The spirit raised her hand, summoning a massive wall of ice to block my path."

    play sound sfx_heartbeat loop                       # Tension SFX

    # =====================================================================
    # D1 — TIMED QTC: Ice Wall (circle with fire = safe / smash = +YUKI)
    # =====================================================================

    menu:

        "Circle around the ice wall and melt the edges with fire bursts.":  # ✓ CORRECT
            $ ch3_d1 = "fire_circle"
            stop sound

            play sound sfx_fire_burst                   # PLACEHOLDER — fire burst SFX

            "I focus my fire, melting a narrow passage through the edge of the wall. The flames hold, and I step through before the frost can overwhelm me."

            elara     "Good, my heart. Be quick, but don't waste your strength."
            yuki_onna "I told you to leave!"

        "Try to smash through the ice wall with brute force.":              # ✗ WRONG — +1 YUKI
            $ ch3_d1 = "smash"
            $ yuki_tracker += 1
            stop sound

            play sound sfx_ice_wall_crash               # PLACEHOLDER — wall crash SFX

            scene cg_ice_wall_smash with shock_cut      # PLACEHOLDER — cg_ice_wall_smash
            pause 0.5
            scene bg_frostcradle_boss_arena with dissolve

            "I swing my fist, but the wall's frost shoots up my sword and numbs my arm. The ice cracks, but the spirit's frost engulfs my legs."

            dorian    "Ahh!!"
            yuki_onna "You should have left… Now you will die!"
            emily     "Dad! Quickly! Thaw the ice out!"

    # D1 converge
    play sound sfx_heartbeat loop

    yuki_onna "What's the matter? Are you cold?"

    elara  "She's bound to this place. Her strength fades when she's far from her ice. Force her to move."
    daniel "Go to the rocks, dad!"

    "The spirit glided toward me, the frost beneath her feet thickening with every step."

    yuki_onna "Die!!"

    # =====================================================================
    # D2 — TIMED QTC: Lure to rocks = safe / Stand ground = +YUKI
    # =====================================================================

    menu:

        "Lure her toward the rocky terrain.":       # ✓ CORRECT
            $ ch3_d2 = "lure"
            stop sound

            "I retreat, leading her toward the jagged rocks at the edge of the clearing. Her frost spread slower over the uneven ground, and the ice beneath her faltered, cracks forming in the once-seamless sheet."

            yuki_onna "You… You…"

            "She breathes on the rocky terrain, ice forming on the surface. Her breath clouds the air as she struggles to push forward."

            dorian "What the…"
            lucas  "She's freezing the area, dad. Be on your guard!"

        "Stand your ground and overpower her frost with fire.":             # ✗ WRONG — +1 YUKI
            $ ch3_d2 = "stand"
            $ yuki_tracker += 1
            stop sound

            play sound sfx_frost_crawl                  # PLACEHOLDER — frost crawl SFX

            "I plant my feet and summon flames, pushing them outward in a desperate attempt to hold her frost at bay. But her power surges, the frost intensifying faster than I could burn it back."
            "The ground turns to slick ice, and I slip, leaving myself open. Her claws slash through my armor, raking across my side."

            dorian    "Ahh!!"
            yuki_onna "This will be your end…"

    # D2 converge — ice spears phase
    stop sound

    "The yuki-onna's icy presence grows stronger. With a flick of her wrist, dozens of jagged ice spears materialize around her, glimmering like frozen starlight."

    yuki_onna "You'll die alongside those who are foolish enough to come here!"

    play sound sfx_ice_spear_launch                     # PLACEHOLDER — spear launch SFX
    play sound sfx_heartbeat loop

    elara "Dorian, don't panic! Try to dodge and look for the gaps. Use your fire wisely!"

    # =====================================================================
    # D3 — TIMED QTC: Fire wall = +YUKI / Dodge and burst = safe
    # =====================================================================

    menu:

        "Raise a wall of fire to block all the spears at once.":            # ✗ WRONG — +1 YUKI
            $ ch3_d3 = "fire_wall"
            $ yuki_tracker += 1
            stop sound

            play sound sfx_fire_blast                   # PLACEHOLDER — fire wall SFX

            "The ice spears shatter against the flames, but the fragments rain down like shards of glass, slicing into my armor. The frost burns as it touches my skin."

            yuki_onna "Give in to the cold…"
            dorian    "Never!"

        "Dodge swiftly and use a burst of fire to deflect the closest spears.":  # ✓ CORRECT
            $ ch3_d3 = "dodge_burst"
            stop sound

            scene cg_ice_spear_deflect with dissolve    # PLACEHOLDER — cg_ice_spear_deflect
            pause 0.6
            scene bg_frostcradle_boss_arena with dissolve

            play sound sfx_fire_burst                   # PLACEHOLDER — deflection burst SFX

            "I roll to the side, summoning a controlled burst of fire to melt the nearest shards. The heat pushes back the frost, giving me just enough space to avoid the worst of her attack."

            elara "Good, but stay alert! She won't stop with just one attack."
            emily "Dad, take care, please!"

    # D3 converge — final spear phase
    stop sound

    "She raised her hands, frost swirling around her as she summoned a massive spike of ice, its jagged surface glowing with an unnatural light."

    yuki_onna "You… will… die!!"

    elara "She's channeling her energy. Don't hesitate—stop her now!"
    sarah "Use your fire, dad!"
    lucas "Do it, dad!"

    yuki_onna "Farewell…"

    play sound sfx_heartbeat loop

    # =====================================================================
    # D4 — TIMED QTC: Dodge = instant GAME OVER / Fire blast = check YUKI
    # =====================================================================

    menu:

        "Try to dodge the spear.":                                          # ✗ WRONG — instant GAME OVER
            $ ch3_d4 = "dodge"
            stop sound

            play sound sfx_frost_crawl                  # PLACEHOLDER — frost spreading SFX

            "I dive to the side, but the spear grazes my shoulder. Frost spreads instantly, freezing my flesh in a searing burst of pain."

            dorian "Argh—!"

            "The frost continues to crawl up my arm, encasing me in ice. I struggle to move, but the cold is overwhelming."

            scene cg_dorian_frozen_ch3 with fade        # PLACEHOLDER — cg_dorian_frozen_ch3
            stop music fadeout 1.0
            stop audio fadeout 1.0

            yuki_onna "Like ice, life is very fragile. You should have known before coming here."
            yuki_onna "I told you to leave… And you refused…"
            yuki_onna "Now you will die in frost… Like them…"

            "The frost consumes me entirely, and the last thing I feel is the crushing weight of ice."

            jump game_over                              # ← HARD GATE: instant GAME OVER

        "Channel all your fire energy into a focused blast, aiming directly at the spear.":  # ✓ CORRECT
            $ ch3_d4 = "fire_blast"
            stop sound

            play sound sfx_fire_blast                   # PLACEHOLDER — concentrated fire blast

            "I plant my feet, channeling every ounce of fire I have into a concentrated beam aimed directly at the spear. The flames roar to life, colliding with the ice mid-air. The spear melts instantly, the water hissing into steam."

            yuki_onna "No!!"

    # -----------------------------------------------------------------------
    # POST-D4 CONVERGENCE — YUKI TRACKER CHECK
    # -----------------------------------------------------------------------
    # yuki_tracker >= 2: Dorian took too many hits — frost overwhelms him
    # yuki_tracker <= 1: Victory — Yuki-onna shatters

    if yuki_tracker >= 2:

        # GAME OVER — Dorian's wounds too severe to survive
        play sound sfx_frost_crawl                      # PLACEHOLDER — frost spreading SFX

        scene cg_dorian_frozen_ch3 with fade            # PLACEHOLDER — cg_dorian_frozen_ch3
        stop music fadeout 1.0
        stop audio fadeout 1.0

        dorian "Argh—!"

        "The frost continues to crawl up my arm, encasing me in ice. I struggle to move, but the cold is overwhelming."

        yuki_onna "Like ice, life is very fragile. You should have known before coming here."

        "The frost consumes me entirely, and the last thing I feel is the crushing weight of ice."

        pause 1.0

        jump game_over                                  # ← YUKI overflow: GAME OVER

    else:

        # ✓ VICTORY — Yuki-onna shatters
        play sound sfx_fire_blast                       # PLACEHOLDER — final blast

        scene cg_yuki_onna_shatter with flash           # PLACEHOLDER — cg_yuki_onna_shatter
        pause 1.0
        scene bg_frostcradle_interior with dissolve     # Return to mine bg

        stop music fadeout 2.0

        "Her icy form flickers and cracks, her strength waning as the fire consumes her energy."

        elara     "You did it, my heart!"
        yuki_onna "AHHH!!"

        "The yuki-onna lets out a piercing wail before shattering into a flurry of snowflakes. The frost in the air dissipates, leaving only the warmth of my flames behind."
        "Her form dissolves into a cascade of glittering snowflakes, drifting through the air. They swirl ahead of me, shimmering faintly in the darkness of the Frostcradle."

        elara "Follow her, Dorian. There's something she wants to show you."

        "The snowflakes drifted into a tunnel, leading deeper into the mine. My fists tightened as I followed cautiously."

        jump ch3_truth


# =============================================================================
# SECTION 8: LABEL CH3_TRUTH — Elias Found / Ekaterina's Ghost Vision
# =============================================================================
# The shack. Elias attacks Dorian with kitchen objects. The amulet is touched.
# Vision: Queen Ekaterina reveals the full truth — Gustav, Vasily, the sacrifice.
# Returns to the shack with Elias asleep.
# =============================================================================

label ch3_truth:

    scene bg_shack_interior with fade                   # PLACEHOLDER — crude wooden shack interior
    play music ost_ekaterina_truth fadein 2.0           # PLACEHOLDER — mournful OST
    play audio amb_shack_fire loop fadein 1.5           # PLACEHOLDER — fireplace crackle

    "Eventually, I emerged into a small chamber carved into the rock. At its center was a crude, weathered shack."
    "The snowflakes glided toward it, their light dimming as they disappeared through the cracks in the wood."
    "I pushed the door open with one hand, the other ready in case of an ambush."
    "The inside was warmer than I expected, lit by the flickering glow of a small lantern. Supplies were scattered haphazardly."
    "And then, something hit me. Hard."

    "A wooden block collided with my shoulder."

    dorian "Argh! Hey!"

    # CG: Elias in the corner — full screen reveal
    scene cg_elias_found with dissolve                  # PLACEHOLDER — cg_elias_found
    pause 1.5
    scene bg_shack_interior with dissolve               # Return to shack bg

    "A toddler. Probably three years old. Barely the size of Lucas, crouched in the corner. His face pale, his eyes wide with fear, his tiny hands clutching a wooden spoon."

    elias "Go away! Go away!"

    "The toddler let out a frightened cry as the spoon flew through the air, bouncing harmlessly off my chest."
    "I blinked, utterly dumbfounded, as he grabbed the next available object — a dented tin cup — and launched it."

    dorian "Seriously?"

    "The cup clattered to the floor, and I exhaled sharply, lowering my hands."

    dorian "Hey! Calm down!"

    "I took a step forward. He grabbed a small tin plate and flung it."

    dorian "Enough!"

    "I lunged forward, catching his wrist mid-throw. He screamed."

    elias "Let me go! Let me go!"

    "I tightened my grip just enough to keep him from wriggling free, crouching to his level."

    dorian "Stop. I'm not going to hurt you."

    elias "Let me go! *crying*"

    "Something stirred a pang of unease in my chest. I looked closer, scanning him for any sign of the death god's energy. Nothing. Not on him, at least."
    "That's when I noticed the amulet hanging around his neck, faintly glowing with a sinister light. The energy practically oozed from it, but the toddler himself… He wasn't the source."

    dorian "What's your name, kid?"

    elias "*sobbing* E-Elias…"

    "The name hit me like a punch to the gut. Elias. Elias Drakos. The former crown prince. The 'monster' Vasily and the prophets had warned me about."

    dorian "You're Elias Drakos?"

    "The toddler nodded weakly, his small frame sagging under the weight of his fear and exhaustion."

    "This can't be right. This is the killer?"

    dorian "Alright, Elias. You're tired. Let's get you some rest."
    elias  "N-No! You'll hurt me!"

    dorian "If I wanted to hurt you, I'd have done it already. Now sit."

    "He hesitated before collapsing onto the straw bed, his body too weary to fight anymore."

    dorian "Good. Now sleep."

    "Elias curled up, his small hands clutching the amulet tightly. Within moments, his breathing evened out."
    "I sat next to his bed, watching him in silence. My mind swirled with questions."

    "I reached out and touched the amulet."

    play sound sfx_amulet_surge                         # PLACEHOLDER — amulet surge SFX

    "The instant my fingers grazed its cold surface, a surge of power slammed through me, like a tidal wave of energy crashing against my very soul. My vision blurred, and my knees buckled."

    dorian "What the—?!"

    # -------------------------------------------------------------------------
    # AMULET VISION — Magnus's desperate call
    # BG: bg_white_void
    # -------------------------------------------------------------------------

    scene bg_white_void with flash                      # PLACEHOLDER — white void
    play sound sfx_thunder_vision                       # PLACEHOLDER — thunder crack SFX

    scene cg_chaos_images with dissolve                 # PLACEHOLDER — cg_chaos_images (fractured visions)
    pause 1.0
    scene bg_white_void with dissolve

    "Then came the light. Blinding, searing. It pierced my mind like a dagger, splintering into a kaleidoscope of fractured images."
    "A man with massive wings, his face obscured, his voice a thunderous whisper that echoed in my skull."

    "Magnus: Help!"
    "Magnus: Come…"
    "Magnus: To Tianho…"
    "Magnus: NOW!"
    "Magnus: AAHHHH!!!"

    "I recoiled, clutching my head as an unbearable headache tore through me. The pain was sharp, relentless, as if my skull were being split open."
    "And then... silence."

    # -------------------------------------------------------------------------
    # EKATERINA'S GHOST — the truth revealed
    # -------------------------------------------------------------------------

    scene cg_ekaterina_vision with dissolve             # PLACEHOLDER — cg_ekaterina_vision
    pause 2.0
    scene bg_white_void with dissolve

    # show ekaterina_ghost at center with dissolve       # PLACEHOLDER — Ekaterina ghost sprite

    "When I opened my eyes, she stood before me. Queen Ekaterina Drakos."
    "She stood before me, her figure ethereal and shimmering. Snow swirled around her ghostly figure."

    ekaterina_ghost "Dragon of Gale. It's time you learned the truth."
    dorian          "Queen Ekaterina… what is this? What's happening?"

    "She raised her hand, the air around us growing colder."

    ekaterina_ghost "All of this is because of the amulet Elias is wearing."
    ekaterina_ghost "Vasily... my Vasily... was his loyal hand, aiding him in his research."

    "My stomach turned at the name. Vasily? This didn't make sense."

    # -------------------------------------------------------------------------
    # THE VISION — palace study; Gustav and the amulet
    # BG: bg_mjoll_palace_vision
    # -------------------------------------------------------------------------

    scene bg_mjoll_palace_vision with dissolve          # PLACEHOLDER — ghostly palace vision

    ekaterina_ghost "The night before the ceremony, I had Elias with me. Elias wanted to hug his father because it was his birthday — but we stumbled upon Gustav in his study, hunched over the amulet, its cursed light glowing in the dark. Vasily was with him."
    ekaterina_ghost "I heard him speaking of a divine weapon underneath Tianho and how he would use it to subjugate the land. And then he saw us — he was frantic, shouting, desperate. He saw me and screamed at me to leave."

    "The vision shifted. I saw her clutching Elias's tiny hand, rushing through dimly lit corridors. Vasily caught up to them, his face pale with dread."

    dorian          "You stole the amulet? Why?"
    ekaterina_ghost "I didn't want Mjoll to suffer the same fate as Tianho. Whatever Gustav is planning, I don't want any part of it."

    vasily          "What have you done, Ekaterina?! The king is furious! He wants both of your heads!"

    dorian          "Vasily?"
    ekaterina_ghost "Vasily... my secret lover. Elias's true father. Not Gustav. He begged me to flee, but there was no escaping Gustav's wrath. Not for me. Not for my son."
    ekaterina_ghost "I knew the power of our militia. I knew there was no escape. Gustav's militia would hunt us to the ends of the earth."
    ekaterina_ghost "I lashed out at him. 'Why bring Elias into this?! He's innocent!' But Vasily had no answers. He promised to plead with the king, but I knew better."
    ekaterina_ghost "That night, I made my choice. I recalled an old chant from Hinami, one my mother taught me — a chant that could transform a soul into something eternal. Something powerful. But it required death."
    ekaterina_ghost "I waited until Vasily was with you during the ceremony."

    # CG: Ekaterina's sacrifice — the blade
    scene cg_ekaterina_sacrifice with fade              # PLACEHOLDER — cg_ekaterina_sacrifice
    pause 2.0
    scene bg_mjoll_palace_vision with dissolve

    dorian          "You… killed yourself."
    ekaterina_ghost "Yes, I took my blade and plunged it into my heart, praying the chant would work. My spirit became one with the cold, with the storm. I became what you see now — a guardian of frost."

    # -------------------------------------------------------------------------
    # THE VISION CONTINUES — spirit protecting Elias in Frostcradle
    # BG: bg_frostcradle_interior
    # -------------------------------------------------------------------------

    scene bg_frostcradle_interior with dissolve         # PLACEHOLDER — mine interior (vision tint)

    yuki_onna "I took him to the abandoned mine, Frostcradle. I thought I could protect him here, away from Gustav, away from the militia."
    yuki_onna "The amulet amplified my abilities. I had Elias wear it so I can draw from its power."
    yuki_onna "Those who came near... those who sought to harm him... I killed them. I froze them. Mercenaries, soldiers, Aldoriths — they all fell to protect my son."

    dorian    "So the bodies I saw earlier were—"
    yuki_onna "Yes. All who sought to harm my child."
    yuki_onna "My child… Elias."

    # -------------------------------------------------------------------------
    # EKATERINA'S PLEA — white void, fading
    # BG: bg_white_void
    # -------------------------------------------------------------------------

    scene bg_white_void with fade                       # PLACEHOLDER — white void, fading light

    yuki_onna "My power is waning. Soon, I'll be nothing but a memory in the wind. But before I fade, I'll create one last blizzard — one so fierce, no one will ever come near Elias again."

    "The air around us grew colder, her form flickering like a dying flame."

    dorian    "You'd doom the people of Mjoll to starvation and death just to save one child?!"
    yuki_onna "I DON'T CARE. You've seen how they wish to kill my child. I heard you were a father once, Dorian. Wouldn't you do the same for your children?"
    dorian    "I—"

    "Her voice broke, and for the first time, I saw tears coming out of her eyes."

    ekaterina_ghost "*weeping* My Elias… Now that I'm gone… I don't know what will become of him…"
    ekaterina_ghost "I know I've done terrible things. But please, Dorian... I have nothing left to give. No treasure, no kingdom, no legacy."
    ekaterina_ghost "Please. I beg you, Dorian. Save him. Protect my son. I couldn't in life, but maybe... maybe you can."

    "She wept in silence for what seemed like hours."

    ekaterina_ghost "Elias… my child… forgive me…"

    "And then she was gone."

    # -------------------------------------------------------------------------
    # RETURN TO SHACK — Dorian collapses; Elias asleep
    # BG: bg_shack_interior
    # -------------------------------------------------------------------------

    scene bg_shack_interior with fade                   # PLACEHOLDER — shack interior

    stop music fadeout 2.0

    "The vision faltered. I was back in the room, staring at the sleeping toddler and the glowing amulet around his neck. Ekaterina's words echoed in my ears."
    "Save him. Protect him."
    "I looked down at Elias, his tiny chest rising and falling."
    "I feel… light. My body feels heavy. I fall on the floor."

    pause 1.5   # Dorian unconscious — a beat of silence

    jump ch3_elias_questions


# =============================================================================
# SECTION 9: LABEL CH3_ELIAS_QUESTIONS — Optional Questions to Elias
# =============================================================================
# Dorian recovers. He and Elias eat. Player can ask Elias optional questions.
# All paths converge on the blizzard scene.
# =============================================================================

label ch3_elias_questions:

    # Dorian wakes to Elias trying to open a jar
    play music ost_blizzard_days fadein 3.0             # PLACEHOLDER — quiet blizzard days OST
    play audio amb_blizzard_howl loop fadein 1.5        # PLACEHOLDER — howling blizzard ambient

    "The cold floor bit into my cheek as I stirred awake. The roar of the blizzard echoed through the mining cave like a living beast."
    "When I opened my eyes, I was greeted by the dim light of the shack. Elias was in the corner, fumbling with what appeared to be a jar."
    "His tiny hands struggled against the lid, his face scrunched up in determination."

    dorian "What are you doing?"

    "The sound startled him, and he froze."

    elias "Ahhh!"

    dorian "Hey. I'm not going to hurt you."

    "Elias clutched the edge of a blanket like it was a shield, his gaze flickering between me and the jar."
    "I noticed it more clearly. Old and scratched — a preserve jar. Fruits, most likely. His little hands had been trying to open it."

    dorian "You were trying to get this open, right?"

    "I reached for the jar slowly. He tensed. I gave the lid a firm twist. It popped open with ease."

    dorian "There. All yours."

    "He hesitated, then inched forward cautiously, still clutching the blanket. His tiny hands darted out to grab the jar, pulling it close. He buried his face in it and began to eat."

    dorian "You need to wipe your face. Hold on."

    "I knelt and opened my pack. My hands brushed against something familiar. Emily's ribbon. Lucas's slingshot. Daniel's carved wooden horse. Elara's scarf. And Tedda — the knit doll with the missing eye."

    dorian "How did these get here?"

    "I turned back to Elias, who was licking his fingers, his small face sticky with syrup. I offered him the cloth."

    dorian "Alright. Hold still."

    "I wiped his face gently, the cloth coming away sticky and stained. He squirmed a little but didn't resist."

    dorian "How old are you?"

    "Elias hesitated, then held up three fingers."

    elias "Fow."
    dorian "Four, huh? You sure about that?"

    "He nodded, with a serious expression on his face. I sat back against the creaky shack wall and decided to try a few questions."

    dorian "Alright. I have some questions."

    jump ch3_question_menu


label ch3_question_menu:

    menu:

        # -----------------------------------------------------------------------
        # QUESTION 1: Did your mom bring you here?
        # -----------------------------------------------------------------------
        "Did your mom bring you here?" if not ch3_asked_mom:

            $ ch3_asked_mom = True

            dorian "Did your mom bring you here?"

            "Elias paused, his cheeks stuffed like a chipmunk's. He swallowed loudly before mumbling."

            elias "Uh-huh. Mommy say... um... stay here, an'... an' don't open da door... 'cause... 'cause bad mans come in an'—"

            "He stuffed another piece of fruit into his mouth mid-sentence."

            elias "An' Mama say... no cry, 'cause... 'cause Mommy's gonna be back. But she not..."

            "His little face scrunched up in thought, and he trailed off, licking his fingers again."

            dorian "Well… I'm not getting any answers from you, am I?"
            elias  "Um… Huh?"

            jump ch3_question_menu

        # -----------------------------------------------------------------------
        # QUESTION 2: What's that amulet you're wearing?
        # -----------------------------------------------------------------------
        "What's that amulet you're wearing?" if not ch3_asked_amulet:

            $ ch3_asked_amulet = True

            dorian "What's that amulet you're wearing?"

            "At this, Elias froze. His sticky hands darted to the amulet, clutching it protectively."

            elias "This? They Mommy say... uh... um... Mommy say, don't give it! Don't give it to bad guys. No, no, no!"

            "He shook his head so hard his hair flopped around."

            elias "She say... it's... uh... it's super 'portant! Like... magic, or somethin'…"

            "He blinked at me, then tilted his head."

            elias  "Are you a bad guy, mister?"
            dorian "What do you think? I opened the jar for you, didn't I?"

            "Elias squinted at me suspiciously before shoving another chunk of fruit into his mouth."

            elias "Okay. I believe you, mister."

            jump ch3_question_menu

        # -----------------------------------------------------------------------
        # QUESTION 3: Who are those people frozen at the entrance?
        # -----------------------------------------------------------------------
        "Who are those people frozen at the entrance?" if not ch3_asked_bodies:

            $ ch3_asked_bodies = True

            "I gestured toward the cave entrance, where the bodies I had seen earlier were frozen."

            dorian "Who are those guys? The ones outside?"

            "Elias glanced toward the entrance, his expression scrunching up."

            elias "The bad guys… and they make Mommy go WHOOSH!"

            "He threw his arms up, making a dramatic gusting sound."

            elias "And they go... um... like statues. Mommy say, 'Leave!' An' dey didn't... so, um, they go 'brrrrrrrrrr!'"

            "He shivered for emphasis, then giggled, poking at the jar."

            elias  "They're not scary, mister. Mommy's scarier!"
            dorian "I can imagine."

            jump ch3_question_menu

        # -----------------------------------------------------------------------
        # Done asking — converge to blizzard
        # -----------------------------------------------------------------------
        "I'm done asking questions for now.":

            elias "Okay! You ask lotsa stuffs, mister. I like da fruit. Got more?"

            "I sighed, grabbing the cloth again."

            dorian "First, let's clean you up — again."

            jump ch3_blizzard_trapped


# =============================================================================
# SECTION 10: LABEL CH3_BLIZZARD_TRAPPED — Blizzard Days in the Shack
# =============================================================================
# Days pass. Dorian refuses to bond with Elias — until the Tedda moment breaks him.
# The family farewell dream. Elias calls Dorian "daddy" for the first time.
# =============================================================================

label ch3_blizzard_trapped:

    "The roar of the blizzard outside echoed loudly through the mining cave."
    "I wiped his face gently again, making his tiny face and little fingers spotless."

    "Then my stomach growled — how long it had been since my last meal? Hours? Half a day. I was starving."

    dorian "Kid, is there any food in here?"

    "The toddler looked up from where he was fiddling with the now-empty jar. He pointed a finger toward the corner."

    elias "Uhhh... um... fishies over there, mister! An' veggies... Mommy say dey for soup. But I don't know how."

    "I found what he meant. A pile of provisions — ice-cold fish wrapped in rough parchment, some frozen vegetables, and a sack of rice."
    "Tianho white-scaled fish. My mother used to cook these when I was a kid."

    dorian "*sighs* I'm going to cook some stew. Want some?"

    "Elias's face lit up, and he nodded eagerly."

    elias "Y-Yes. I'm hungry too, mister!"

    "I cooked. He watched intently as I worked, his eyes following every movement."
    "Eventually, I ladled the finished stew into a couple of old wooden bowls. The fish had cooked perfectly — tender, flaky, the broth rich with sweetness."

    dorian "Here. Don't spill it."

    "Elias took a cautious sip, then let out a happy hum, his legs kicking excitedly."

    elias "Mmm! It's hot... but it's yummy! You're a good cooker!"
    dorian "It's cook, not cooker."

    "I rolled my eyes, taking a sip of my own bowl."

    # -------------------------------------------------------------------------
    # THE BLIZZARD — Dorian checks the storm
    # -------------------------------------------------------------------------

    scene bg_frostcradle_blizzard with dissolve         # PLACEHOLDER — blizzard howling through cracks

    "Dorian: Stay here, kid. I'll be right back."

    "I stepped toward the mine entrance. The icy wind hit me like a wall, cutting through my cloak and stinging my face."

    elara  "You know what Gustav will do to that child."
    dorian "It's a bounty, my heart. You know how bounties work."
    elara  "Well then, why did you accept it?"
    dorian "Nobody told me that the target was a toddler. How in Tetrad's name was I supposed to know?"
    elara  "You've seen Mjoll. You've seen how they treat the aldoriths. You know what Gustav will do to that child if he gets a hold of him."
    dorian "It's not my decision. It's not my place. The task was to kill him, Elara. I didn't... I couldn't. So maybe bringing him to Gustav is the compromise."
    elara  "A compromise? You think handing a defenseless child over to that monster is a compromise?"
    dorian "I'm not a savior, Elara. I never was. I… wasn't strong enough to save you… and the kids."
    dorian "I'm a mercenary now. This isn't—"
    elara  "This isn't who you are. I know you've buried the man you used to be under all that guilt, but I know he's still there. And you know it too, or that boy would already be dead."
    dorian "Once the blizzard stops, I'm giving the boy to King Gustav. I'm a man of my word."
    elara  "*sigh* I understand, my heart."

    "I stood there for a long moment, the blizzard howling in my ears."

    "Then I turned back and saw Elias standing behind me, wrapped in a blanket."

    elias "Hello, mister. Who are you talking to?"

    dorian "What are you doing here? I thought I told you to stay put."
    dorian "Come on. Let's head back, Elias."

    # -------------------------------------------------------------------------
    # DAYS PASS — Dorian refuses to bond
    # -------------------------------------------------------------------------

    scene bg_shack_interior with dissolve               # PLACEHOLDER — shack interior

    "A couple of days passed. The blizzard showed no sign of letting up."
    "I didn't speak to Elias. Not once."
    "He tried, of course. In his small, curious voice, he'd ask questions. 'Why is it so cold?' or 'What's your favorite food?'"
    "I ignored them all. It was easier that way."
    "I told myself it was better this way. No attachments. No guilt. When the storm passed, I would take him to King Gustav, collect my bounty, and move on."
    "That's how it had to be."
    "Until the morning I woke up to the sound of soft giggles."

    "I blinked groggily. My eyes landed on Elias, sitting cross-legged on the floor with something clutched tightly in his hands."

    "It took me a second to realize what it was."
    "Tedda."

    "My chest tightened. That was my gift for Sarah."

    dorian "That's for Sarah. Put that down."

    "Elias froze, his wide eyes looking up at me, startled and afraid. He clutched Tedda tighter."

    elias "I… I'm sorry, mister. I-I—"
    dorian "I said put it down."

    "He flinched at the harshness of my tone, his bottom lip trembling. Slowly, he placed Tedda on the floor and backed away."
    "I bent down, picking up Tedda. My fingers trembled, and I hated that they did."
    "Behind me, I heard the faint sound of a sniffle."

    elias "I'm sorry, mister. I didn't mean to make you mad."

    "I stood there, staring down at the bear."

    dorian "This bear's name is Tedda. This was for Sarah. My daughter."

    "I wasn't sure why I said it. Maybe I just needed to say her name."

    dorian "She's not here anymore. I'm her dad… and everything I do is to protect her."

    "Elias looked down at his lap, his small hands fiddling with the edge of his blanket."

    elias "I… I wish I had a daddy…"

    "His words hit me like a blow. I stared at him, stunned."

    elias "My daddy doesn't love me. He… he wants me dead."

    "I was shocked. I didn't know that he knew King Gustav wanted him dead."

    elias "Mommy saved me… from him. She kept me safe. But now she's…"

    "His voice cracked, and tears spilled down his cheeks."

    elias "…gone too."

    "He buried his face in the blanket, his small body shaking with silent sobs. I stood there, frozen, clutching Tedda."
    "Before I could stop myself, I knelt beside him, holding out the bear."

    dorian "Here."

    "Elias peeked up at me, his tear-streaked face glowing with surprise. His small hands hesitated before gently taking Tedda from me. He hugged the bear tightly."

    dorian "If Tedda will make you happy, you can have her."
    elias  "T-Thank you, mister."

    # CG: Elias throwing his arms around Dorian's neck
    scene cg_elias_hug with dissolve                    # PLACEHOLDER — cg_elias_hug
    pause 2.0
    scene bg_shack_interior with dissolve

    "Elias reached out with both arms and threw them around my neck."
    "He hugged me."
    "His small arms clung to me with all the strength in his tiny body, desperate and shaking, like he was afraid I'd vanish if he let go."

    elias "Mommy told me in a dweam. She's gone… She won't be come back…"

    "I didn't answer. Didn't have the words."
    "So I just held him."
    "He didn't speak again. Neither did I."
    "Only the sound of the blizzard filled the silence — soft and endless."
    "And for a long time, we stayed like that."

    elias "Thank you, mister."

    jump ch3_yuxuan_arrives


# =============================================================================
# SECTION 11: LABEL CH3_YUXUAN_ARRIVES — Supply Bot / Hologram Scene
# =============================================================================
# The Cheng Industries supply bot rolls in. Yuxuan's hologram activates.
# Dorian tells Yuxuan everything about Ekaterina and Elias.
# Magnus vision interrupts — Dorian collapses. Elias saves him.
# The family farewell dream.
# =============================================================================

label ch3_yuxuan_arrives:

    "Then I heard it — a faint whirring sound cut through the silence. It grew louder, and I turned toward the noise."

    # CG: supply bot rolls in
    scene cg_supply_bot_arrives with dissolve           # PLACEHOLDER — cg_supply_bot_arrives
    pause 1.5
    scene bg_shack_interior with dissolve

    elias "What's that? Is it alive?"
    dorian "No, it's not alive. It's a supply bot. Made by Cheng Industries."
    elias "A suh-ply bot?"

    play music ost_supply_bot_jingle fadein 0.5         # PLACEHOLDER — cheerful Cheng Industries jingle

    "Roboto: Here at Cheng's, we bring change…"

    stop music fadeout 1.5

    elias "It sings, mister! It's so cute!"

    "As the jingle faded, a soft hum emanated from the bot. A hologram flickered to life above its chest."

    # show yuxuan hologram at right              # PLACEHOLDER — Yuxuan hologram sprite

    yuxuan "Praise the Prosperity Dragon! Dorian, I'm so happy to see you again!"

    "I blinked, caught off guard. I awkwardly forced a smile, though I didn't remember his face at all. I only remembered writing him a letter."

    dorian "Nice to meet you again, Yuxuan."
    yuxuan "I got your letter! So I've been asking around, trying to track you down in Mjoll. When I heard you might be in the Frostcradle, I figured you could use some help."
    yuxuan "So, I hijacked one of our bots already en route to Mjoll and had it rerouted here."

    "The bot turned around and opened a compartment on its chest to reveal a neatly organized cache of goods: dried meats, vegetables, warm blankets, fire-starting kits, and even a few luxury items like hot drink packets and a sealed tin of sweets."

    yuxuan "The blizzard's getting worse, so I thought you'd appreciate a little extra help. Everything in here is yours — no charge, of course."

    "Elias' eyes widened, his eyes sparkled as he stared at the supplies."

    elias "Mister, look! It's got food! And bwankets! And… and CANDIES!"

    "He tugged at my sleeve eagerly, practically bouncing on the spot."

    dorian "T-Thanks, Yuxuan. You didn't have to go out of your way."
    yuxuan "Nonsense! You saved my hide back in Tianho, remember? Consider this payback."

    elias "Wow, there's so many TWEATS! Tedda, look! Tweats just for us!"

    "Elias practically squealed as he reached for the tin of sweets, scurrying off to a corner of the shack."

    dorian "Hey — we haven't had a proper meal, first!"

    "Yuxuan chuckled through the hologram."

    yuxuan "Wait… Who's Tedda? Is there another person here?"
    dorian "That's just the knit doll with the missing eye."
    yuxuan "Oh… I thought it was another person. Anyway, Dorian… Have you handled the situation yet?"
    dorian "What situation?"
    yuxuan "Have you killed the Prince? The one who murdered the Queen. You know, to stop the blizzard?"
    yuxuan "King Gustav upped the bounty. He already tripled it."

    "The question hung heavily in the air. I took a deep breath and pointed to the corner."

    dorian "You're looking at him."

    "Yuxuan's holographic face froze mid-smile, his mouth dropping open as his gaze followed my hand to Elias. The toddler was sitting cross-legged, happily stuffing candies into his mouth while making Tedda 'dance' beside him."

    elias "*giggling* Tedda says, 'Candy is the best thing ever!' Right, Tedda?"

    yuxuan "W-WHAT?! That's… that's the Prince?!"

    "I crossed my arms and nodded."

    yuxuan "I… I'm confused. By the way they described what he did, I thought the Prince would be… older. At least of age! Not…"

    "I sighed, the weight of everything pressing on my chest. Taking a deep breath, I leaned closer to the hologram."

    "I told Yuxuan everything. How Queen Ekaterina became the frost spirit Yuki-onna and that she's the one who caused the blizzard, not Elias."

    "Yuxuan's expression softened with horror and sympathy as he absorbed the information."

    yuxuan "Heavens. Prosperity Dragon save Her Majesty's soul. That's too tragic!"
    yuxuan "And even King Gustav and Count Vasily want him dead…"

    dorian "Yeah. Kid's got it rough."

    yuxuan "But… what do you plan to do, Dorian? You can't exactly just…"

    dorian "I don't know…"

    dorian "C'mon, Elias. I'll cook you up something proper before you finish half of that candy."

    elias "Okay, mister."

    # -------------------------------------------------------------------------
    # MAGNUS VISION INTERRUPTS — Dorian collapses
    # -------------------------------------------------------------------------

    "I started toward the makeshift cooking area, but before I could take another step, a sharp pain pierced through my head like a hot blade. My knees buckled, and the room tilted. My vision blurred."

    scene bg_white_void with flash                      # PLACEHOLDER — white void flash

    play sound sfx_amulet_surge                         # PLACEHOLDER — amulet surge SFX

    "Magnus: Come to Tianho, Dragonkin…"
    "Magnus: My power flows through you now. Only you can open the…"
    "Magnus: Hurry… please…"

    "And then, darkness."

    scene bg_shack_interior with dissolve               # Return to shack

    "I hit the ground hard, my body trembling as icy tendrils of pain radiated through my chest."

    elias "Mister! Mister, wake up! What's wrong?"
    yuxuan "Dorian?! What happened?!"

    dorian "I… don't know…"

    yuxuan "Elias, listen to me! You have to help him. The bot can't administer aid — it's not designed for that. Only you can do this!"
    elias  "Umm… okay. But I don't know how!"

    yuxuan "Stay calm! First, you… um… need to… Prosperity Dragon save us… Where's a doctor when you need him?"

    "I felt his tiny hands on my face, shaking me gently."

    elias "Mister? Please wake up! Please don't leave me!"
    yuxuan "Elias, hold his hand. Talk to him. Sometimes, power responds to emotion. Tell him he's safe, that you're here. It might help ground him."
    elias "Mister… please don't leave. I'll be good, I promise. I'll share all my candies with you and Tedda! Just… don't go."

    "His voice broke into soft sobs as he clung to me."

    yuxuan "Elias, the necklace! It's reacting to him. Take it off and give it to him — quickly!"
    elias  "O-Okay…"

    play sound sfx_amulet_surge                         # PLACEHOLDER — amulet energy settling

    "I felt the weight of the amulet as Elias placed it on my chest. The energy around me shifted immediately, the chaotic sparks focusing, centering."

    "Magnus: Yes… Yes…"

    "And then everything went black."

    # -------------------------------------------------------------------------
    # FAMILY FAREWELL DREAM
    # BG: bg_white_void
    # Music: ost_family_dream
    # -------------------------------------------------------------------------

    scene bg_white_void with fade                       # PLACEHOLDER — white void, warm golden light
    play music ost_family_dream fadein 3.0              # PLACEHOLDER — gentle farewell OST

    # CG: family farewell — full screen
    scene cg_family_farewell with dissolve              # PLACEHOLDER — cg_family_farewell
    pause 2.0
    scene bg_white_void with dissolve

    elara  "Dorian… my heart."

    "I turned to see her, standing with Daniel, Sarah, Emily, and Lucas. They smiled at me, their faces serene."

    daniel "Goodbye, Dad. It's time for us to go."
    sarah  "You don't need us anymore, Dad. You're strong now."
    emily  "We'll always be with you, in your heart."
    lucas  "Until we meet again, Dad."

    "Tears blurred my vision, but I couldn't bring myself to move or speak."

    dorian "D-Don't go…"

    "Elara stayed behind as the children faded into the light. She walked toward me, her hand brushing against my cheek."

    elara "I'll miss you, my heart. But Ena needs you. Our mission here is done."
    elara "Go, my heart. Ena is counting on you."
    elara "Until we meet again."

    "The warmth of her touch lingered as she, too, faded into the golden light."

    dorian "No!!"

    # -------------------------------------------------------------------------
    # WAKING — Elias curled up beside Dorian
    # -------------------------------------------------------------------------

    scene bg_shack_interior with fade                   # PLACEHOLDER — shack interior, firelight
    stop music fadeout 2.0
    play audio amb_shack_fire loop fadein 2.0           # PLACEHOLDER — fire crackle

    "I woke with tears streaming down my face, my body trembling."
    "Then I felt it — a small, warm body pressed tightly against mine."
    "Elias was curled up beside me, his tiny arms wrapped around my torso, clutching me. Tedda was squished between us."

    "As I wept silently, Elias stirred, mumbling softly in his sleep."

    elias "Please don't take Daddy away…"

    "My heart broke all over again. And before I knew it, I found myself holding him close."
    "The only sounds were the crackling of the fire and Elias' soft breathing."
    "And as the firelight flickered, I held onto him."

    jump ch3_mushroom


# =============================================================================
# SECTION 12: LABEL CH3_MUSHROOM — D6: Yuxuan Mushroom Invitation
# =============================================================================
# Morning after the dream. Yuxuan spots Blisscap mushrooms nearby.
# D6: Join Yuxuan (++yuxuan_affection) or Don't Join (-yuxuan_affection).
# Both paths converge on D7 the cooking choice.
# =============================================================================

label ch3_mushroom:

    scene bg_shack_morning with dissolve                # PLACEHOLDER — shack morning, warmer light

    play music ost_blizzard_days fadein 2.0             # PLACEHOLDER — quiet days OST

    "The next morning, I woke up early. Elias was still asleep, his small body curled tightly around Tedda."
    "I found that I was wearing the amulet Elias had been wearing. Oddly enough, it stopped glowing. I stood up, removed it and placed it on a small table."
    "A soft whirring sound made me glance toward the corner. The bot came to life with a low hum, the hologram of Yuxuan flickering into existence."

    yuxuan "Good morning, Dorian!"
    dorian "Morning, Yuxuan. You're up early."
    yuxuan "I never really sleep much. Or even eat. Too many projects to think about, you know? But… that's not what I called."
    yuxuan "You're not going to believe this, but there's a rare mushroom growing just outside the shack! I spotted it on the bot's scanners earlier."
    yuxuan "It's called a Blisscap. They only grow here in Mjoll, and their taste? Oh, it's incredible — earthy, with just a hint of sweetness. It'd be perfect for breakfast."

    dorian "Really? Is it edible?"
    yuxuan "Completely! Trust me, I wouldn't suggest it if it weren't."
    yuxuan "It's just outside, Dorian. Still inside the cave, so the blizzard won't get in the way. I could guide you to it, you know, if you're up for it. Please?"

    "His smile lingered a little longer than it needed to."

    # -----------------------------------------------------------------------
    # D6 DECISION — Join Yuxuan or Don't Join
    # -----------------------------------------------------------------------

    menu:

        "Join Yuxuan.":                                 # ✓ ++yuxuan_affection
            $ ch3_d6 = "joined"
            $ yuxuan_affection += 2                     # Double affection gain — exclusive bonding scene

            dorian "Alright, Yuxuan. Show me where it is."
            yuxuan "Great! Follow the bot, and I'll guide you."

            scene bg_frostcradle_interior with dissolve # PLACEHOLDER — mine interior, quieter

            play music ost_mushroom_walk fadein 2.0     # PLACEHOLDER — tender, curious OST

            "As I stepped outside, the air in the cave was cooler, but it wasn't unbearable."
            "Yuxuan's hologram flickered as he pointed toward a faint patch of glowing blue mushrooms near the cave wall."

            yuxuan "There. Aren't they beautiful? The glow is caused by a natural compound in their spores. It's harmless, I promise."

            "I crouched down, gently plucking a few of the mushrooms."

            yuxuan "You know… seeing you here, alive, after everything in Tianho — it's, um… it's really nice. I never got to say thank you. For what you did."

            dorian "You don't owe me anything, Yuxuan."
            yuxuan "Maybe not. But that doesn't mean I'm not grateful. You didn't have to save me back then, but you did. And… it meant a lot."
            yuxuan "I… I'm just so happy I finally get to meet you again. You were my hero, you know? Still are."

            "He paused, his holographic image flickering faintly."

            yuxuan "Paladin Dorian Burnham. The Dragon of Gale. I never forgot your name."

            "The title felt foreign now, like it belonged to someone else entirely."

            dorian "I'm just a mercenary now, Yuxuan. I'm not a paladin anymore. I resigned years ago. That man you remember? I apologize. But he's gone."

            "The silence that followed was almost unbearable."

            yuxuan "Maybe you've changed. Maybe you've been through things that I can't even imagine. But you're still the man who saved me. You're still him."

            "He paused, the air between us heavy with unspoken words."

            yuxuan "Thanks for humoring me. I, uh… I hope breakfast turns out great."

            dorian "It will. Thanks to you, Yuxuan."

            stop music fadeout 2.0

            scene bg_shack_morning with dissolve        # Return to shack for cooking

        "Don't join.":                                  # ✗ -yuxuan_affection
            $ ch3_d6 = "skipped"
            $ yuxuan_affection -= 1                     # Minor affection loss

            dorian "Thanks, but I'll pass. I've already got breakfast going."

            "Yuxuan's hologram faltered slightly, but he recovered quickly."

            yuxuan "Of course. No problem. I just thought… well, never mind. If you change your mind, the bot will be here."
            dorian "Appreciate it, Yuxuan. But I think I'll stick with what we've got for now."
            yuxuan "Understood. Well, if you need anything else, just let me know."

            "With that, the hologram flickered off."
            "A few minutes later, Yuxuan's bot returned, its mechanical arms extending to offer me a small container filled with glowing Blisscap mushrooms."

            yuxuan "Here you go. Breakfast is on me. Well, technically on the cave, but you get the idea."

            dorian "Thank you, Yuxuan."

    # Both D6 paths converge here — cooking choice
    jump ch3_breakfast


# =============================================================================
# SECTION 13: LABEL CH3_BREAKFAST — D7: Cooking Choice (4 Soft Branches)
# =============================================================================
# Four breakfast options. No stat effect — purely flavour.
# All converge on Elias waking up and calling Dorian "daddy" for the first time.
# =============================================================================

label ch3_breakfast:

    "I moved to the fireplace, spreading the ingredients out on a makeshift wooden counter: a couple of golden fish, a white-scaled fish fillet, some string beans, a handful of other vegetables, and the glowing Blisscaps."

    dorian "Alright. Let's see what we can do with this."

    # -----------------------------------------------------------------------
    # D7 DECISION — 4-option cooking choice (all soft, no stat effect)
    # -----------------------------------------------------------------------

    menu:

        # -----------------------------------------------------------------------
        # OPTION 1: Golden Fish Omelette
        # -----------------------------------------------------------------------
        "Golden Fish Omelette.":
            $ ch3_d7 = "omelette"

            "I decided to make a Golden Fish Omelette for us."
            "I cracked the eggs into a bowl, whisking them with a pinch of salt and a sprinkle of dried herbs. I sliced thin pieces of golden fish and added them to the mix, along with a small handful of finely chopped Blisscaps for flavor."

            yuxuan "C-Careful, Dorian! Don't let it stick to the pan. Maybe a bit more oil?"
            dorian "I know how to cook, you know."

            "I frowned, adding a touch more oil as the edges began to crisp. I folded the omelette in half, the golden fish glinting faintly against the soft yellow of the eggs."
            "The result was decent — it looked nice. Yuxuan made me add a little herbs. 'For garnishing', he said."

        # -----------------------------------------------------------------------
        # OPTION 2: White-Scaled Fish Soup
        # -----------------------------------------------------------------------
        "Hearty White-Scaled Fish and Vegetable Soup.":
            $ ch3_d7 = "soup"

            "I decided to make soup with vegetables and some white-scaled fish."
            "I tossed the white-scaled fish into a pot of water, letting it simmer as I added diced vegetables — carrots, onions, and string beans. Healthy for growing little kids like Elias."
            "The Blisscaps went in last, their faint glow dissipating as they softened in the broth."

            dorian "Is that how you cook them, Yuxuan?"
            yuxuan "Uh… maybe add some salt? It looks a little bland."

            "I sprinkled in a pinch, tasting the broth with a wooden spoon. It wasn't bad, but it lacked something."

            dorian "Maybe some dried herbs…"

            "The bot handed me a small pouch of spices, and I added a pinch of dried basil. The soup took on a richer aroma."

        # -----------------------------------------------------------------------
        # OPTION 3: Pan-Fried Golden Fish with Blisscaps
        # -----------------------------------------------------------------------
        "Pan-Fried Golden Fish with Scrambled Blisscaps and Veggies.":
            $ ch3_d7 = "fried"

            "I decided to just pan-fry the Golden Fish and some vegetables."
            "I seasoned the golden fish with salt and pepper, frying it in a pan until the skin was crispy and golden brown. Meanwhile, I sautéed the Blisscaps and vegetables in a separate pan."

            yuxuan "D-Dorian! You're burning the veggies!"
            dorian "Dragon's bollocks! *grumbling*"

            "I plated the fish on a bed of the sautéed Blisscaps and veggies, adding a small garnish of string bean slices for color."

        # -----------------------------------------------------------------------
        # OPTION 4: String-Bean and White-Scaled Fish Fried Rice
        # -----------------------------------------------------------------------
        "String-Bean and White-Scaled Fish Fried Rice.":
            $ ch3_d7 = "rice"

            "I decided to make some fried rice with some string beans and white-scaled fish."
            "I chopped the white-scaled fish into small pieces, stir-frying it with cooked rice, chopped string beans, and a handful of diced vegetables. The Blisscaps added a faint glow as I mixed them in."

            yuxuan "A little soy sauce might help."
            dorian "We… don't have soy sauce. Oh — sorry. We have some."

            "I splashed in a small amount, the rice taking on a richer, darker hue."
            "Not bad."
            "I plated the fried rice, sprinkling a pinch of dried herbs on top for good measure."

    # -----------------------------------------------------------------------
    # ALL COOKING OPTIONS CONVERGE — Elias wakes up
    # -----------------------------------------------------------------------

    "Elias woke up and toddled over, rubbing his eyes."

    elias "Good morning, da— I mean, mister!"

    "I smiled, kneeling to his level to hug him."

    dorian "Morning, Elias. Hungry?"

    "He nodded enthusiastically."

    dorian "Dig in!"

    "Elias sat cross-legged on the floor, the warm meal before him."

    yuxuan "If I had a mouth, I'd eat every bite. My compliments, Chef Burnham."

    "Somewhere in the background, I could faintly hear an old woman's voice."

    weng  "Master Yuxuan, you must eat something. You've been working so hard."

    dorian "Who's that, Yuxuan?"
    yuxuan "Oh just no one… Just my chef. I'm going to eat, Miss Weng! Just wait!"

    "The sound of the raging blizzard outside filled the brief silence."

    elias "Mister…"
    dorian "Yes, Elias?"

    "He hesitated, fiddling with Tedda's paw."

    elias "Is… is it okay if I call you daddy?"

    "The question hit me harder than I expected. My chest tightened, but I quickly ruffled his messy hair with a soft smile."

    dorian "Whatever makes you happy."

    "Elias beamed, his face lighting up with pure joy as he hugged Tedda tightly."

    elias "Okay, daddy."

    # -------------------------------------------------------------------------
    # MORE BLIZZARD DAYS — bonding montage; then the storm breaks
    # -------------------------------------------------------------------------

    play audio amb_blizzard_howl loop fadein 2.0        # PLACEHOLDER — blizzard ambient

    "The blizzard raged on for several long, frigid days. Inside the cozy confines of the shack within the cave, we weathered the storm together."
    "Yuxuan kept us company through his bot most of the time."

    yuxuan "Dorian! This bot is powered by solar cells I designed myself. They're ten times more efficient than the industry standard. Did you know—"
    yuxuan "Dorian, are you even listening? You're not, are you?"

    dorian "I'm listening, Yuxuan. Solar cells. Revolutionary. Got it."

    "Elias spent hours creating grand adventures for Tedda. His little voice brought warmth to the cold as he made the bear 'fight' monsters or embark on daring rescues."
    "When he wasn't playing with Tedda, Elias would draw with crayons Yuxuan had included in the supply bot. He'd proudly show me his creations — crude, colorful scribbles that strangely resembled me."

    elias "This is you, Daddy. See? You're big and strong! And this is me, and this is Tedda. Oh! And this is Mister Yuxuan."
    dorian "You're quite the artist, Elias. I'll make sure to hang these somewhere special."

    elias "Good night, Daddy."
    dorian "Good night, Elias."
    yuxuan "Good night to both of you. May the howling blizzard only make our little shack feel warmer."

    # -------------------------------------------------------------------------
    # THE STORM BREAKS
    # -------------------------------------------------------------------------

    stop audio fadeout 3.0                              # Blizzard stops — silence

    "The next day, I woke up to an eerie silence. No howling winds. No biting cold seeping through the cracks of the shack."
    "Heart pounding, I scrambled to my feet, careful not to wake Elias."

    scene bg_frostcradle_exterior with dissolve         # PLACEHOLDER — frostcradle exterior, storm cleared

    "Snow stretched endlessly in every direction. But the storm — after what felt like an eternity — had finally stopped."
    "Relief washed over me, and I turned, ready to hurry back to the shack and tell Elias the good news."

    jump ch3_vasily_arrives


# =============================================================================
# SECTION 14: LABEL CH3_VASILY_ARRIVES — Vasily's Battalion + Kristin's Death
# =============================================================================
# Vasily emerges with a full battalion demanding Elias's death.
# Niko briefly challenges the narrative — is dismissed.
# Kristin speaks out — and is immediately killed.
# Svante's grief is weaponised by Vasily to turn him against Elias.
# =============================================================================

label ch3_vasily_arrives:

    play music ost_vasily_arrives fadein 1.0            # PLACEHOLDER — dark military OST

    "But as I stepped forward, a voice stopped me in my tracks."

    vasily "Hello, friend. Took you quite some time to finish the mission."

    "I froze. The voice was calm, almost casual. Slowly, I turned around."

    dorian "V-Vasily... What brings you here?"

    "He stepped closer, his boots crunching softly against the cave floor."

    vasily "Oh, you know. Just passing through. Thought I'd check on an old friend."
    vasily "Imagine my surprise when I heard rumors. A seasoned mercenary hiding in a cave. Abandoning his mission. It's... disappointing, Dorian."
    vasily "What else am I here for, friend? We're here for the contract."

    dorian "We?"

    "Vasily snapped his fingers. The sound echoed through the cave, and within moments, soldiers began marching into view. An entire battalion."

    vasily "Under orders from His Majesty, the Prince is to be executed. Immediately."
    vasily "So tell me, friend. Have you killed the Prince yet?"
    dorian "You… didn't tell me the Prince was a toddler, Vasily."
    vasily "Does it matter? The contract was clear. Elias Drakos is to be eliminated. His age doesn't change what he's done… or what's at stake."
    dorian "Look, I-I'll give you the money back. Every coin. I'll pay you back and walk away from this."

    "Vasily barked out a laugh."

    vasily "The prided mercenary of Mjoll, reduced to bargaining over coin? I'll even double your pay. Triple it, if that's what it takes."
    vasily "Just give us the Prince, and we'll call it even. No hard feelings."

    "Before I could answer, a guttural cry broke the silence."

    svante "That snake of a prince deserves to die!"

    "The violet-haired aldorith stormed forward, his sword drawn, his eyes bloodshot."

    svante "Hundreds of innocent people were killed because of the blizzard! Dozens of my brothers and sisters died because of him!"

    "Tears streaked his face as he pointed his blade toward me."

    svante "Kill the Prince! Show no mercy!"

    boy_ald_soldier "My brother is right! He killed our family through this blizzard! He deserves to die!"

    "A man with striking blue hair stepped forward from the shadows — Niko, in a hooded robe."

    niko "Hey… is it true? The Prince… is he really just a toddler?"
    vasily "What of it, Prophet?"
    niko  "It just doesn't add up. I no longer sense the death god's energy here. The presence that once lingered is gone."
    niko  "A toddler committing murder? The Queen's death? I examined her body. The wound — it's surgical. Precise. A toddler didn't do this."

    "Another robed man rushed forward, grabbing Niko's arm."

    "Prophet: Hehe, forgive my fellow brother in Enoch, Count. He tends to let his curiosity get the better of him."
    "Prophet: Please, pay him no mind."

    niko "No. I'm serious. Something doesn't make sense, and—"

    "Without a word, Vasily reached into a pouch at his belt and pulled out a heavy bag of coins, tossing it at the man's feet."

    vasily "Here. Your payment. The services of the death god's Prophets are no longer required."
    niko   "Tsk."

    "The other prophet scooped up the coins and bowed deeply."

    "Prophet: Thank you, Count. May Enoch's blessings be with you. We will trouble you no further. Come, Niko."
    niko   "But brother—"
    "Prophet: You know the First Law of Enoch: 'To hinder death is to defy Him.' We are not to interfere. Not even if the innocent must suffer."
    niko   "I understand, brother. Praise be to His Word."
    "Prophet: Praise be. Now come. Let us leave this place."

    "He dragged the blue-haired prophet away, but Niko shot me one last look before disappearing over the crowd."

    "The murmurs among the soldiers grew louder. An aldorith with silver hair stepped forward, her voice trembling but resolute."

    kristin "Count Vasily… maybe they have a point. If the pieces don't fit, we have a duty to—"
    svante  "What are you doing, Kristin?"
    kristin "Thinking, Svante, dear brother. For myself. You should try it sometime."
    svante  "Shut it, Kristin! You dare question King Gustav? Our Father?"
    kristin "Brother, you used to think for yourself. What happened to you? Since when did you let blind faith replace reason?"
    kristin "I was there, Svante. I saw the Queen's body with the prophets. The wound didn't match the story of Father. Don't you see? This isn't right!"
    kristin "Brother, please believe me."
    svante  "I… I…"

    "The air grew colder as Vasily stepped forward, his expression dark."

    vasily  "Enough."

    "He snapped his fingers. Kristin turned to him, her eyes wide with fear."

    kristin "Count, please. I'm just—"

    # CG: Kristin's death — no build-up, instantaneous; the horror is in the speed
    play sound sfx_blade_strike                         # PLACEHOLDER — blade strike SFX
    scene cg_kristin_death with shock_cut               # PLACEHOLDER — cg_kristin_death
    pause 1.0
    scene bg_frostcradle_exterior with dissolve

    "The blade struck her before she could finish. She crumpled to the ground, her blood pooling in the snow."

    boy_ald_soldier "Done, sir."
    vasily          "Any more aldoriths willing to share their dissenting opinion?"
    vasily          "Hmph. Your Father never tolerates treason. Remember that."

    "Svante dropped to his knees beside Kristin's lifeless body, his cries piercing the silence."

    svante  "K-Kristin… No…"
    kristin "B-Brother… I'm sorry… Tell mother I—"
    svante  "Kristin! KRISTIN!"

    "Vasily turned to him, his voice cold."

    vasily "It's the Prince's fault, Svante. His crime is sowing doubt on Kristin."
    svante "K… K-Kristin *cries*"
    vasily "If it weren't for him, Kristin would still be alive. King Gustav is right."

    "Svante's tear-streaked face twisted into a mask of rage."

    svante "E-Elias… that boy… he's the reason…"

    "Vasily turned back to me, his expression softening."

    vasily "Dorian, think about it. Don't throw everything away for this child. You know how this ends if you don't do the right thing."

    "He placed a hand on my shoulder, firm yet gentle."

    vasily "His Majesty hated that you took too long, you know… But I'll make sure King Gustav knows what you've done for him. A fresh start, Dorian. You'll be back in his good graces."
    vasily "A mansion, Dorian. Wealth. Comfort. You don't have to keep running, keep hiding. You've saved me countless times, and I'm here to save you."
    vasily "I mean it, Dorian. You're my friend. Don't ruin everything for one child. Let me help you."
    vasily "Well, Dorian? What's it going to be?"

    jump ch3_critical_fork


# =============================================================================
# SECTION 15: LABEL CH3_CRITICAL_FORK — D5: Give or Refuse Elias
# =============================================================================
# THE pivotal decision of the chapter. Irreversible.
# Give Elias → ch3_bad_end (BAD ENDING branch — years later suicide).
# Refuse    → ch3_fight_back (GOOD PATH — draconic fire awakening).
# =============================================================================

label ch3_critical_fork:

    play music ost_critical_fork fadein 1.0             # PLACEHOLDER — suspended tension OST
    play sound sfx_heartbeat loop                       # PLACEHOLDER — heartbeat loop

    menu:

        # -----------------------------------------------------------------------
        # CHOICE 1: Give Elias — BAD ENDING (irreversible)
        # -----------------------------------------------------------------------
        "Give Elias to Vasily.":

            $ ch3_d5 = "gave"
            stop sound
            stop music fadeout 1.0

            "A long silence."

            dorian "Go ahead. The kid's inside the shack."

            "Vasily smiled."

            vasily "Aldoriths, go inside and kill the prince. Now."

            boy_ald_soldier "What? That's it? You're not going to punish this traitor for—"
            vasily "Do it. Now."
            boy_ald_soldier "Yes, sir."
            girl_ald_soldier "On it, sir!"

            svante "Leave the prince to me. Kristin… sister… you'll be avenged."

            "Vasily turned to me, his eyes soft."

            vasily "You made the right choice, friend. Now let us take care of business. I'm sure you'd rather… not see how the prince will be dealt with."

            dorian "Thanks, Vasily."

            jump ch3_bad_end

        # -----------------------------------------------------------------------
        # CHOICE 2: Refuse and Fight — GOOD PATH (+svante_affection)
        # -----------------------------------------------------------------------
        "Refuse. Protect Elias.":

            $ ch3_d5 = "refused"
            $ svante_affection += 1                     # +1 Svante affection — his doubt is seeded here
            stop sound

            dorian "No, Vasily. I can't do this. I beg you just… take the coin."
            dorian "I'll return every piece the King gave me for this mission. No harm, no foul. We can both walk away from this."

            vasily "You don't get it, do you? This isn't about the coin, Dorian. It's about loyalty. It's about trust."
            vasily "The prince needs to die."
            vasily "You're putting me in a bad spot, old friend. I vouched for you. I said you'd get the job done, no questions asked."

            svante "That boy — that prince — is the reason my sister is dead! You're protecting a murderer! You're as guilty as he is!"

            dorian "Look. I beg you. Just take the money. We all can—"

            elias "Daddy?"

            "My heart dropped. I spun around, and there he was — Elias — standing at the entrance of the shack, clutching Tedda tightly. His small face pale, his wide eyes flicking between me and the soldiers."

            dorian "Elias! Get back inside! Now!"

            "I turned back to Vasily, my hand instinctively moving to the hilt of my blade."

            dorian "You see? He's just a child, Vasily. Look at him. Does he look like a killer to you?"

            vasily "The prince needs to die. My loyalty stands with the king."

            boy_ald_soldier  "Long live King Gustav!"
            girl_ald_soldier "Long live King Gustav!"
            svante           "L-Long live King Gustav!"

            dorian "Enough!"

            "My shout echoed through the cave, silencing the crowd. I stepped forward, placing myself between Elias and the soldiers."

            dorian "If you want him, you'll have to go through me."

            vasily "Don't do this, old friend. You're throwing your life away for a child who doesn't even belong to you. Is it even worth it?"
            dorian "Yes. Yes, he is."
            vasily "So be it."

            jump ch3_fight_back


# =============================================================================
# SECTION 16: LABEL CH3_BAD_END — BAD ENDING (Give Elias)
# =============================================================================
# Elias is killed offscreen. Years pass.
# Dorian lives in hollow luxury, avoids Yuxuan, loses everything inside.
# Ends at the cliffside: Dorian's suicide. BAD END / CREDITS.
# =============================================================================

label ch3_bad_end:

    scene bg_mjoll_town_normal with fade                # PLACEHOLDER — Mjoll town, years later

    play music ost_bad_end_luxury fadein 3.0            # PLACEHOLDER — hollow grandeur OST

    "Years passed."
    "Mjoll welcomed me back like a long-lost hero. Vasily was true to his word — he always was. The mansion he promised became mine, a grand, sprawling estate with lush gardens, gilded halls, and guards at every gate."
    "The missions resumed soon enough."

    scene bg_mjoll_palace_normal with dissolve          # PLACEHOLDER — palace interior, parties

    vasily "You've done well for yourself, my friend. Look at you now. Comfortable, respected… untouchable."
    vasily "Ladies, calm down. This is Dorian, the legendary mercenary of Mjoll you're speaking to!"

    "But his words rang hollow, like the clinking of glasses in empty halls."
    "I never saw Elias again."
    "It wasn't hard to imagine where he might've ended up. I stopped asking questions. Stopped wondering. Wondering only made the nights longer."
    "As for Yuxuan? I avoided him entirely. The thought of facing him, of seeing the disappointment or anger in his eyes, was unbearable."
    "And Elara…"
    "Would she be proud of me?"
    "I already knew the answer."

    "The parties became a regular occurrence, each one more extravagant than the last."

    vasily "Another grand event next week, my friend. King Gustav will be there. You'll come, won't you?"
    dorian "Of course, Vasily."

    # -------------------------------------------------------------------------
    # THE CLIFF — Dorian's end
    # BG: bg_mjoll_cliffside
    # -------------------------------------------------------------------------

    scene bg_mjoll_cliffside with fade                  # PLACEHOLDER — cliff edge, moonlight

    stop music fadeout 3.0

    "One evening, I left the party early."
    "The wind was bitter, cutting through my coat as I stood at the edge of the cliff. Below, the snow stretched endlessly, a vast, frozen wasteland illuminated by the pale light of the moon."
    "I stared out at the expanse, my mind swirling with memories I could no longer suppress. Elias's innocent smile. Yuxuan's sarcastic quips."
    "And Elara. Always Elara."
    "I could almost hear her voice, soft and loving, like it used to be when she whispered my name."

    scene cg_bad_end_cliff with dissolve                # PLACEHOLDER — cg_bad_end_cliff
    pause 2.0

    "The snow beneath my boots crunched softly as I took a step closer to the edge."

    dorian "Elara, I'll see you soon."

    "For a moment, everything was silent. The world seemed to hold its breath, waiting."
    "And then I let go."

    scene cg_black with fade                            # PLACEHOLDER — black
    stop audio

    pause 3.0

    "GAME OVER — BAD END"

    pause 1.0

    return   # Returns to Ren'Py main menu / credits


# =============================================================================
# SECTION 17: LABEL CH3_FIGHT_BACK — GOOD PATH: Draconic Fire Awakens
# =============================================================================
# Elias is shot by an arrow — Dorian's draconic fire erupts for the first time.
# The entire battalion is destroyed.
# Niko (in raven form) heals Elias in the background.
# Only Svante survives — he falls through crumbling ground.
# Dorian collapses. Yuxuan finds them.
# =============================================================================

label ch3_fight_back:

    play music ost_vasily_arrives fadein 0.5            # PLACEHOLDER — battle music returns

    "Vasily raised his hand, an orb of light forming in his palm. He hurled it toward Elias with a flick of his wrist."

    play sound sfx_earth_eruption                       # PLACEHOLDER — earth wall SFX

    "I slammed my hands into the ground, the earth trembling beneath my feet as an earthen wall erupted from the cave floor. The light ball struck it with a deafening explosion."

    "Before I could catch my breath, pain tore through my leg as an arrow sank deep into my thigh."

    dorian "ARGH!"

    "I stumbled, blood pouring from the wound. I tore the arrow free, the pain white-hot and blinding."
    "Before I could recover, another arrow whistled through the air."
    "Time seemed to slow as I saw it — its sharp tip gleaming, its deadly path aimed directly at Elias."

    play sound sfx_arrow_hit                            # PLACEHOLDER — arrow hit SFX
    scene cg_elias_shot with shock_cut                  # PLACEHOLDER — cg_elias_shot
    pause 0.8
    scene bg_frostcradle_exterior with dissolve

    elias            "Ah!!"
    boy_ald_soldier  "He's hit! The bastard prince is down!"
    girl_ald_soldier "Praise be to Enoch! Someone check if he's dead!"
    boy_ald_soldier  "Positive! The wound is grave — straight through the gut!"

    dorian "No! Elias! No!"

    "A ragged scream tore from my throat. Vasily's smirk widened as he approached the boy."

    vasily "Such is the fate of all who goes against His Highness' wishes."

    dorian "Elias!! Please!!"

    "He didn't respond. His eyes fluttered shut, and the world around me seemed to fade. All I could hear was the pounding of my heart and Vasily's laughter."
    "My vision blurred, tears streaming down my face."
    "And then, I heard it."

    # -------------------------------------------------------------------------
    # DRACONIC FIRE AWAKENS
    # -------------------------------------------------------------------------

    scene cg_black with fade                            # PLACEHOLDER — black: the voice from darkness

    stop music fadeout 1.0

    prosperity_dragon "Never shall it be said that my children are weak. Rise up, Dorian!"
    prosperity_dragon "Do not mourn. Fight!"

    scene cg_draconic_fire_awakens with flash           # PLACEHOLDER — cg_draconic_fire_awakens
    pause 1.5

    play music ost_draconic_awakening fadein 0.5        # PLACEHOLDER — explosive awakening OST

    scene bg_frostcradle_exterior with dissolve

    "The air around me shifted. Heat radiated outward from my body, intense and suffocating. My hands, still trembling, began to glow, flames flickering to life on my fingertips."
    "I looked down at Elias, tears streaking my face, and something inside me shattered. The grief twisted, transformed into something raw and feral."
    "Rage."

    dorian "You'll pay for this, Vasily… You'll pay for this."

    vasily "D… Draconic fire?! In Enoch's name…"
    vasily "Friend… wait… we can talk about this—"

    "I didn't let him finish."

    play sound sfx_draconic_roar                        # PLACEHOLDER — draconic roar SFX

    scene cg_battalion_falls with shock_cut             # PLACEHOLDER — cg_battalion_falls
    pause 2.0
    scene bg_frostcradle_aftermath with dissolve        # PLACEHOLDER — scorched aftermath bg

    "With a roar that shook the cave, I raised my hands, fire erupting in a torrent that roared like a beast unleashed. It surged toward him, engulfing him completely. His screams were drowned out by the crackling inferno."

    vasily           "Ahhh!! Ahhhh!!!"
    girl_ald_soldier "What in the name of Enoch—"

    "The ground beneath her erupted, jagged pillars of molten rock spearing upward."

    boy_ald_soldier "C-Charge! Charge!"

    "They came at me in waves, arrows flying, swords raised. But I killed them."
    "I raised one hand, and the earth quaked. Chasms opened beneath their feet, swallowing them whole. With the other, I sent firestorms spiraling into their ranks."

    "Female soldier: No!! Ahhh!!!!"
    "Male soldier: Ahhhh!!!"
    "Boy Aldorith: Mercy!! Enoch save me!! Ahhh!!"
    "Girl Aldorith: We're just obeying orders! Don't kill us!! Ahh!!"

    # -------------------------------------------------------------------------
    # NIKO HEALS ELIAS (raven form — in the background during the battle)
    # -------------------------------------------------------------------------

    elias      "D-Daddy… I-It hurts… it hurts! *cries*"
    niko_raven "Shh… hey, hey. Little one. Are you alright?"
    elias      "N-No! G-Get away! Don't hurt me! *cries*"
    niko_raven "Hey, hey. Look at me. See? Just a bird. A talking, friendly bird."
    elias      "A… A bird?"
    niko_raven "Yes. Talking, friendly, very handsome bird. Came just for you."
    elias      "It… it hurts… I'm scared… I don't wanna die… *cries*"
    niko_raven "Now where does it hurt?"
    elias      "M-My tummy… I-It's cold… it's so cold…"
    niko_raven "Then hold this. One of my feathers. See? Strong. Safe."
    niko_raven "Big bird's going to help you. It might tickle, might sting — but I promise, you'll feel better soon. Bird's honor."
    elias      "*crying*"
    niko_raven "Wait — what's this? Is this your friend?"
    elias      "T-Tedda… Her name is Tedda. She's… friend."
    niko_raven "Tedda, huh? A brave guardian. Good. You hold her tight. You've got her… and now you've got me."
    elias      "I… I don't wanna die… like Mommy *cries*"
    niko_raven "Not today. Not while the wind still moves and the roots still breathe. I'm going to patch you up, little prince. I promise. Just breathe with me."
    elias      "O… Okay."

    # -------------------------------------------------------------------------
    # SVANTE ALONE — the last one standing
    # -------------------------------------------------------------------------

    "One by one, they fell. Then… the violet-haired aldorith was the only one left."
    "He fell to his knees, tears streaming down his face, his sword clattering to the ground."

    svante "P-Please! Mercy! I-I didn't mean for this! It wasn't supposed to happen like this! Kristin — she's dead, and now—"

    "His words dissolved into incoherent sobs as he clutched at the hem of my cloak."
    "I raised a hand, fire flickering at my fingertips."

    svante "Please! I believed my sister! But you saw what they did to her! I don't— *crying*"
    svante "I'm sorry! I'm sorry! Please, sir! I—"

    "The fire in my hand flared, my rage begging for release. I took a step forward, the heat forcing him to crawl backward."
    "And then his foot slipped."

    play sound sfx_earth_eruption                       # Ground crumbling SFX
    scene cg_svante_falls with shock_cut                # PLACEHOLDER — cg_svante_falls
    pause 0.5
    scene bg_frostcradle_aftermath with dissolve

    svante "AHHHH!!!"

    "The ground beneath him crumbled. He screamed as he fell, his voice cutting off abruptly."
    "Silence."
    "The cave was still, save for the hiss of steam and the crackle of dying flames."

    stop music fadeout 2.0
    play sound sfx_heartbeat loop                       # Fading heartbeat — Dorian exhausted

    "I clenched my fists, the flames flickering out, leaving behind only the charred remains of what had been a battalion."
    "I staggered, the heat around me dying down as exhaustion took hold."

    stop sound

    "My legs gave out beneath me, and I crumpled to the ground."

    dorian "Elias…"
    dorian "I'm sorry… I'm so sorry..."

    "The last of my strength slipped away, and the world around me faded into darkness."

    jump ch3_escape


# =============================================================================
# SECTION 18: LABEL CH3_ESCAPE — Yuxuan Finds Them / Escape to Tianho
# =============================================================================
# Yuxuan's bot finds Dorian. They escape in a carriage.
# Dorian wakes to find Elias alive beside him.
# Chapter ends with 'jump chapter_4'.
# =============================================================================

label ch3_escape:

    scene cg_black with fade                            # PLACEHOLDER — black; unconscious
    stop audio fadeout 1.5

    pause 1.5

    "A faint whirring sound pulled me from the void. It was mechanical, distant, but growing louder."
    "Then I heard a voice, sharp and familiar, cutting through the haze."

    yuxuan "Dorian! Goodness, what happened here?!"

    "I forced my eyes open, just for a moment. A faint hologram flickered before me — Yuxuan's face, distorted by static, but unmistakably horrified."

    yuxuan "Prosperity Dragon bless me. I need to get you to safety…. Miss Weng! Call the—"

    "The bot hovered closer, scanning the scene. I wanted to respond, to explain, but my body betrayed me."
    "My head lolled to the side, and everything went dark again."

    # -------------------------------------------------------------------------
    # CARRIAGE — waking up safe
    # BG: bg_carriage_interior
    # Music: ost_escape_carriage
    # -------------------------------------------------------------------------

    scene bg_carriage_interior with fade                # PLACEHOLDER — carriage interior
    play music ost_escape_carriage fadein 3.0           # PLACEHOLDER — bittersweet relief OST
    play audio amb_carriage_wheels loop fadein 1.5      # PLACEHOLDER — carriage wheels ambient

    "The next time I stirred, the world felt different. Softer. Warmer."
    "I blinked against the light filtering through the carriage windows, the soft sway of motion beneath me. My head throbbed with a dull ache."

    dorian "Elias…"

    "Panic surged through me until I looked to my side and saw him."
    "He was there, curled up on the bench across from me, Tedda clutched tightly in his arms. His chest rose and fell with shallow but steady breaths."

    elias  "Daddy…"
    dorian "I'm here, Elias. I'm right here. We're going to be okay."

    "I reached out, brushing his hair from his face. Tears welled up in my eyes."

    "A voice spoke from outside the carriage."

    yuxuan "Dorian! You're awake! Praise the Prosperity Dragon!"

    "The door creaked open, and Yuxuan stepped inside. For the first time, it wasn't just his hologram from a supply bot. It was him. In the flesh."
    "His smile was as warm and earnest as I remembered from the hologram, but seeing him here, in person, was something else entirely."
    "His robes shimmered with an opulent sheen. Deep crimson fabric. The stitching alone probably cost more than I'd made in the last decade."

    elias "Daddy, it's him! Mister Yuxuan!"

    "Behind him, two guards flanked the door, their armor marked with the logo of Cheng Industries."

    yuxuan "Thank the Prosperity Dragon I decided to check in. If I hadn't sent the bot when I did…"

    "He trailed off, shaking his head."

    dorian "Y-Yuxuan."
    dorian "Good to see you in person."
    yuxuan "The pleasure's all mine, Dorian! I'm so happy to finally meet you again!"

    "He glanced toward the driver."

    yuxuan "We're taking you both to Tianho. We'll be hiding there."

    "At the mention of Tianho, something stirred in me. It had been years since I'd set foot there. Elara and my family. It's been a while."

    "Elias stirred on the bench, his eyelids fluttering open. His gaze met mine, his small hand reaching out."

    elias "Daddy… I'm happy you're alright."

    "I took his hand, squeezing it gently."

    dorian "I promise, Elias. We'll be okay. I'll protect you. No matter what."

    # CG: escape carriage — warm closing image
    scene cg_escape_carriage with dissolve              # PLACEHOLDER — cg_escape_carriage
    pause 2.0
    scene bg_carriage_interior with dissolve

    "The carriage rocked gently as it moved, the muffled sound of hooves against the road."
    "We were alive. We were together."
    "And for the moment, that was enough."

    # -------------------------------------------------------------------------
    # END OF CHAPTER 3 — Chapter Title Card + Transition
    # -------------------------------------------------------------------------

    scene cg_black with fade                            # PLACEHOLDER — fade to black
    stop music fadeout 2.0
    stop audio fadeout 1.5

    pause 2.0

    show screen chapter_title_screen(
        "4",
        "The Massacrer of Mjoll",
        subtitle="Kingdom of Mjoll — Aftermath",
        duration=3.0
    )
    pause 3.0

    # 'jump chapter_4' — must exist in chapter_04.rpy
    # Stub file:
    #   label chapter_4:
    #       "Chapter 4 coming soon."
    #       return

    jump chapter_4


# =============================================================================
# END OF CHAPTER 3
# =============================================================================
