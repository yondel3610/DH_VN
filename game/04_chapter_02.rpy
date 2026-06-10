###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  FILE:  chapter_02.rpy
#  SCENE: CHAPTER 2 — Four Years Later: Mjoll, Mercenary Life & the Blizzard
#
#  CONTENTS:
#    Section 1  — Character Definitions
#    Section 2  — Image Declarations  (backgrounds, CGs, sprites)
#    Section 3  — Audio Declarations  (music, SFX, ambient)
#    Section 4  — Game Variables      (trackers, flags, choice records)
#    Section 5  — label chapter_2     (opening — Icelands / Qiongqi hunt)
#    Section 6  — label ch2_palace    (Mjoll Palace — Gustav's court)
#    Section 7  — label ch2_cave      (Dorian's cave — grief / dinner)
#    Section 8  — label ch2_square_intro  (Town Square — pre-festival setup)
#    Section 9  — label ch2_freetime  (D2 — four-option free time menu)
#    Section 10 — Free time sub-scenes
#                   ch2_food_stalls   (food stalls + D2a: confront or ignore)
#                   ch2_fortune       (Babala + D2b: family or companions)
#                   ch2_spa           (spa + D2c: do nothing or punish)
#                   ch2_rest          (rest with Vasily)
#    Section 11 — label ch2_common_freetime  (free time convergence)
#    Section 12 — label ch2_ceremony  (celebration + D1: dunk tank)
#    Section 13 — label ch2_frost_oni (Frost Oni battle — D4, D5, D6 QTCs)
#    Section 14 — label game_over_freeze     (shared GAME OVER screen — ICE freeze)
#    Section 15 — label ch2_common_end  (post-battle + Yuxuan letter + D3)
#    Section 16 — label ch2_castle_briefing  (assassination mission briefing)
#    Section 17 — label ch2_questions (optional questions to Vasily)
#
#  NAMING CONVENTIONS (enforced throughout)
#    image tags      — bg_name, cg_name, character_name emotion
#    audio variables — audio.ost_name, audio.sfx_name, audio.amb_name
#    label names     — ch2_name (all lowercase, underscores only)
#    game variables  — svante_affection, ice_tracker, yuxuan_affection, etc.
#    NO SPACES in any tag, label, variable, or image name.
#
#  TRACKER SUMMARY:
#    svante_affection : +1 if D1 = Pretend to miss (dunk tank)
#    ice_tracker      : +1 per wrong Frost Oni QTC answer; >=2 = GAME OVER
#    yuxuan_affection : +1 if D3 = Write warm response
#
#  HARD GATE:
#    D6 (frost cloud) wrong answer when ice_tracker >= 2 -> GAME OVER
#
#  PLACEHOLDER PATHS:
#    Search "# PLACEHOLDER" to find every line that needs a real asset.
###############################################################################


# =============================================================================
# SECTION 1: CHARACTER DEFINITIONS
# =============================================================================

# compiled character definitions

# =============================================================================
# SECTION 2: IMAGE DECLARATIONS
# =============================================================================

# 01_bg_cg.rpy

# =============================================================================
# SECTION 3: AUDIO DECLARATIONS
# =============================================================================
# All audio used in Chapter 2.
# Format:  define audio.name = "path/to/file.ogg"
# PLACEHOLDER: Replace each path with your real .ogg audio file.
# =============================================================================

# --- Music ---
define audio.ost_mjoll_theme      = "audio/music/ost_mjoll_theme.ogg"          # PLACEHOLDER
# Cold, sparse — Mjoll's main region theme; strings + low horns

define audio.ost_qiongqi_hunt     = "audio/music/ost_qiongqi_hunt.ogg"         # PLACEHOLDER
# Tense pursuit music — builds from silence to full percussion on the beast's charge

define audio.ost_mjoll_palace     = "audio/music/ost_mjoll_palace.ogg"         # PLACEHOLDER
# Stiff, formal — Gustav's court; harpsichord and cold strings

define audio.ost_cave_grief       = "audio/music/ost_cave_grief.ogg"           # PLACEHOLDER
# Fragile, intimate — Dorian's cave; solo piano or single instrument

define audio.ost_mjoll_festive    = "audio/music/ost_mjoll_festive.ogg"        # PLACEHOLDER
# Lively Mjollian celebration — drums, horns, folk strings

define audio.ost_babala_prophecy  = "audio/music/ost_babala_prophecy.ogg"      # PLACEHOLDER
# Ethereal, suspended — prophecy moment; soft choir and orb-pulse undertone

define audio.ost_frost_oni_battle = "audio/music/ost_frost_oni_battle.ogg"     # PLACEHOLDER
# Urgent, icy battle theme — fast strings, percussive ice-crack motif

define audio.ost_blizzard_days    = "audio/music/ost_blizzard_days.ogg"        # PLACEHOLDER
# Desolate — the days after the attack; low drone, sparse melody

define audio.ost_briefing         = "audio/music/ost_briefing.ogg"             # PLACEHOLDER
# Tense and deliberate — assassination mission briefing; dark undertones

# # --- Sound Effects ---
# define audio.sfx_qiongqi_roar     = "audio/sfx/sfx_qiongqi_roar.ogg"          # PLACEHOLDER
# define audio.sfx_earth_spike      = "audio/sfx/sfx_earth_spike.ogg"           # PLACEHOLDER
# define audio.sfx_wind_blast       = "audio/sfx/sfx_wind_blast.ogg"            # PLACEHOLDER
# define audio.sfx_ice_crack        = "audio/sfx/sfx_ice_crack.ogg"             # PLACEHOLDER
# define audio.sfx_ice_shatter      = "audio/sfx/sfx_ice_shatter.ogg"           # PLACEHOLDER
# define audio.sfx_frost_oni_roar   = "audio/sfx/sfx_frost_oni_roar.ogg"        # PLACEHOLDER
# define audio.sfx_prophecy_thunder = "audio/sfx/sfx_prophecy_thunder.ogg"      # PLACEHOLDER
# define audio.sfx_dunk_splash      = "audio/sfx/sfx_dunk_splash.ogg"           # PLACEHOLDER
# define audio.sfx_heartbeat        = "audio/sfx/sfx_heartbeat.ogg"             # PLACEHOLDER
# define audio.sfx_ground_swallow   = "audio/sfx/sfx_ground_swallow.ogg"        # PLACEHOLDER
# define audio.sfx_vine_attack      = "audio/sfx/sfx_vine_attack.ogg"           # PLACEHOLDER

# --- Ambient ---
define audio.amb_mjoll_wind       = "audio/ambient/amb_mjoll_wind.ogg"         # PLACEHOLDER
# Howling icy wind — looping; plays under most Mjoll exterior scenes

define audio.amb_cave_fire        = "audio/ambient/amb_cave_fire.ogg"          # PLACEHOLDER
# Crackling fireplace — looping; Dorian's cave interior

define audio.amb_crowd_festive    = "audio/ambient/amb_crowd_festive.ogg"      # PLACEHOLDER
# Festival crowd noise — looping; town square celebration


# =============================================================================
# SECTION 4: GAME VARIABLES
# =============================================================================
# Variables set in Chapter 2. Trackers persist into later chapters.
#
# TRACKER SUMMARY:
#   svante_affection  — seeds Chapter 3 trust route
#   ice_tracker       — accumulates per wrong Frost Oni QTC; >=2 = GAME OVER
#   yuxuan_affection  — warm letter gives +1; affects Chapter 4+ Yuxuan scenes
#
# FREE TIME FLAGS:
#   ch2_visited_food, ch2_visited_fortune, ch2_visited_spa, ch2_visited_rest
#   — each set True once visited; spa forces the fortune teller after
#
# BABALA TOPIC FLAG:
#   ch2_babala_asked_family — False = "companions" option also available
#
# CHOICE RECORDS (flavour callbacks in later chapters):
#   ch2_dunk_choice, ch2_food_choice, ch2_spa_choice, ch2_letter_choice
#   ch2_qtc4, ch2_qtc5, ch2_qtc6
# =============================================================================

# added to game_vars

# =============================================================================
# SECTION 5: LABEL CHAPTER_2 — Opening (Icelands / Qiongqi Hunt)
# =============================================================================
# Entry point — jumped to from chapter_01.rpy via 'jump chapter_2'.
# PDF pages 58-61.
# =============================================================================

label chapter_2:
    if demo_mode:
        scene black with fade
        pause 1.0
        centered "Thank you for playing the demo\n\nThe full version continues here."
        pause 2.0
        $ MainMenu(confirm=False)()
        
    $ save_name = "Chapter 2"
    # -------------------------------------------------------------------------
    # OPENING CARD — "Four years later"
    # -------------------------------------------------------------------------

    scene cg_black with fade                    # PLACEHOLDER — black screen (carry from ch1 end)

    play music ost_mjoll_theme fadein 3.0       # PLACEHOLDER — cold Mjoll region theme
    play audio amb_mjoll_wind loop fadein 2.0   # PLACEHOLDER — howling wind loop

    pause 1.0

    show screen chapter_title_screen(
        "2",
        "Four Years Later",
        subtitle="Mjoll — Kingdom of Snow",
        duration=3.0
    )
    pause 3.0

    # -------------------------------------------------------------------------
    # PDF p58 — Icelands, the Qiongqi hunt
    # BG: frostcradle_blizzard
    # -------------------------------------------------------------------------

    scene frostcradle_blizzard with fade           # PLACEHOLDER — frozen wilderness

    "The snow falls steadily, blanketing the area in silence. The only sounds are the crunch of boots and the occasional muttered curses from the mercenaries behind me."

    # show dorian sad at left_char with Dissolve(0.2)
    show mjoll_pavel at right_char with Dissolve(0.2)
    mjoll_pavel "Merciful Enoch, it's freezing. Why does it have to be this cold?"
    show mjoll_helga at left_char with Dissolve(0.2)
    mjoll_helga "Quit complaining, Pavel. We've got bigger things to worry about. You know what this beast did to that caravan last week."
    hide mjoll_pavel
    show mjoll_lars at right_char with Dissolve(0.2)
    mjoll_lars  "Screw what it did to the caravan. It destroyed an entire village. I don't know why only five of us were sent to kill it!"

    hide mjoll_lars
    hide mjoll_helga
    with Dissolve(0.1)
    "Their voices lower, but I can still hear them."

    show mjoll_lars at right_char with Dissolve(0.2)
    mjoll_lars  "Hey... is that him? The Dragon of Gale?"
    show mjoll_pavel at left_char with Dissolve(0.2)
    mjoll_pavel "No way. He's not... The Dragon of Gale wouldn't be out here with us."
    hide mjoll_lars
    show mjoll_helga at right_char with Dissolve(0.2)
    mjoll_helga "Wait… Enoch above… it really is him. I heard he lost his entire family. Wife and kids... all of them gone."
    mjoll_pavel "No wonder he looks dejected. What kind of man comes back from something like that?"
    hide mjoll_helga
    show mjoll_lars at right_char with Dissolve(0.2)
    mjoll_lars  "Shut up. He'll hear you!"
    hide mjoll_lars
    hide mjoll_pavel
    "Vasily shoots them a sharp glare. He snaps his fingers."

    show vasily alt_aggressive at right_char with Dissolve(0.2)
    vasily "Eyes forward. Lose focus out here, start thinking about the wrong things and you'll be nothing but meat for the beasts. Do I make myself clear?"
    show mjoll_lars at left_char with Dissolve(0.2)
    mjoll_lars "Sir!"

    hide vasily
    hide mjoll_lars
    with Dissolve(0.1)

    "The snow around us seemed to grow heavier. I looked around, scanning the barren landscape."
    "Something was off. Too quiet, too still. The wind carried a foul, metallic scent—blood. I stopped in my tracks and raised a hand."

    show dorian normal_alt_annoyed at left_char with Dissolve(0.2)
    dorian "We're here."

    "The mercenaries stiffened, their chatter ceasing immediately. They looked around nervously, hands shaking as they start gripping their weapons."

    show mjoll_lars at right_char with Dissolve(0.2)
    mjoll_lars "Umm… where?"

    "Silence."
    hide dorian
    hide mjoll_lars
    with Dissolve(0.1)
    "Then it came."
    # TODO: add growl sfx
    "A low, guttural growl rumbled through the frozen wilderness, vibrating the ground beneath us. The snow swirled as if alive, the wind howling in response to the beast's presence."
    
    # play sound sfx_qiongqi_roar                 # PLACEHOLDER — Qiongqi roar SFX
    scene cg_qiongqi_fight with shock_cut      # PLACEHOLDER — cg_qiongqi_charge
    play music ost_qiongqi_hunt fadein 0.5      # PLACEHOLDER — hunt battle music
    "The Qiongqi emerged from the shadows, its massive form blending with the storm. It had the body of a lion but twisted and wrong—its fur black as midnight, its eyes burning like embers. Its sharp claws scraped against the frozen ground, leaving deep gouges."

    qiongqi "KRRRIIEEEEEEEEAAAAAAAHHHHH!!!"

    "It charged. A blur of claws and fury."

    scene frostcradle_blizzard with shock_cut
    show qiongqi at right_qq with Dissolve(0.2)
    show vasily alt_aggressive at left_char with Dissolve(0.2)
    vasily "Hold your ground!"
    hide vasily

    show mjoll_lars at left_char with Dissolve(0.2)
    "One mercenary swung his sword wildly, only for the beast to swat him aside like a doll, sending him crashing into the snow. Another let loose an arrow that bounced harmlessly off the Qiongqi's thick hide."
    mjoll_lars  "AHHH!!"
    hide mjoll_lars

    show mjoll_helga at left_char with Dissolve(0.2)   
    mjoll_helga "My arrows aren't working! Use your shield, Lars!"
    hide mjoll_helga

    "The beast lunged at the third mercenary, its claws slicing through his shield as though it were parchment."
    
    show dorian serious at left_char with Dissolve(0.2)
    "I thrust my arms toward the ground. Pillars of jagged earth erupted from beneath the Qiongqi, slamming into its underbelly and knocking it off balance."
    play sound sfx_earth_spike                  # PLACEHOLDER — earth spike SFX

    qiongqi "Krieeeeeeaaahh!!"

    "It screeched in agony, flipping mid-air, crashing to the ground. Clumps of black fur and blood sprayed into the snow."
    hide qiongqi with Dissolve(0.1)
    "But it wasn't finished."
    scene cg_qiongqi_fight with shock_cut
    "It rose, furious—its mouth split open unnaturally wide as it released another piercing howl."

    qiongqi "RAAAAAHHHHHHHRRGHHHH!!!"
    
    # show vasily alt_aggressive at right_char with Dissolve(0.2)
    vasily "Dorian! It's coming for you!"

    "I didn't move."
    "Instead, I rotated my palm. The wind around me shifted. Then roared."

    # hide vasily
    play sound sfx_wind_blast                   # PLACEHOLDER — wind blast SFX

    "A gale burst forth—a spiraling, howling torrent that slammed into the Qiongqi's face, flinging it backward across the battlefield like a rag doll. The snow whipped into a frenzy as the beast clawed at the ice, struggling to find footing."

    # show qiongqi at center_qq with Dissolve(0.2)
    qiongqi "RAAAAAHH!! RAAAHHH!!"
    mjoll_lars  "Helga, your bow! Hit it on its shoulder!"

    "One of the Mjoll soldiers managed to shoot an arrow, and by some stroke of luck—or desperation—it embedded itself in the Qiongqi's shoulder. The beast howled, thrashing violently, but it only seemed angrier."
    scene frostcradle_blizzard with shock_cut
    show qiongqi at right_qq with Dissolve(0.2)
    qiongqi "Krieeeeeewwwaaahh!!"
    show mjoll_helga at left_char with Dissolve(0.2)
    mjoll_helga "Haha! Take that!"
    hide mjoll_helga

    show vasily alt_aggressive at left_char with Dissolve(0.2)
    "Vasily stepped forward, his expression calm but his eyes burning with resolve. He raised his hands, and a blinding light erupted from his palms. The Qiongqi screeched, recoiling from the light."
    scene cg_blindinglight with flash
    hide vasily
    scene frostcradle_blizzard with shock_cut
    show vasily alt_aggressive at left_char
    show qiongqi at right_qq 
    with Dissolve(0.2)
    vasily "Now, friend!"
    hide vasily
    
    show dorian dragon_eyes at left_char with Dissolve(0.2)
    "I didn't hesitate. Summoning a massive portion of earth, I brought a jagged spike of stone hurtling up beneath the Qiongqi's chest, impaling it."
    play sound sfx_earth_spike                  # PLACEHOLDER — earth spike SFX

    qiongqi "Kwaaaaaaaaahhh—"
    "The winds circled my body, responding to my silent fury. With a snap of my hand, a twisting column of wind slammed into the Qiongqi's skull, driving it headfirst into the frozen ground with enough force to shatter bone."
    qiongqi "GRGHHHHHHKKKKHHHHHHH—"
    hide qiongqi
    hide dorian
    with Dissolve(0.1)
    "The monstrous shrieking was cut short. The Qiongqi twitched once… then went still."
    "Dead."
    stop music fadeout 2.0
    
    show dorian normal_alt_annoyed at left_char
    show mjoll_pavel at right_char with Dissolve(0.2)
    mjoll_pavel "He… he literally could have just done this without us."
    hide mjoll_pavel
    show mjoll_lars at right_char with Dissolve(0.2)
    mjoll_lars  "He really is… the Dragon…"
    hide mjoll_lars

    "I stood over it, my breath steady, my gaze cold."

    show dorian serious at left_char
    dorian "Cut off its head. Now."
    show mjoll_lars at right_char with Dissolve(0.2)
    mjoll_lars "Yes, sir."

    "He nodded quickly, drawing his blade and stepping toward the corpse."
    hide mjoll_lars
    "I turned away, wiping the bloodied snow from my gauntlets. Vasily approached, his light fading."

    show vasily alt_think at right_char with Dissolve(0.2)
    vasily "That was quick, friend. You didn't even flinch."
    vasily "Are we even needed anymore, or are we just here for the scenery? Haha."

    "I didn't respond. My eyes were fixed on the distant horizon, where the snow-covered peaks loomed like silent watchers."

    hide vasily
    show dorian sad at left_char with Dissolve(0.2)
    dorian "Time to go back."

    # hide characters here, only bg
    hide dorian
    "The walk back to Mjoll was silent except for the crunch of snow beneath our boots. The soldiers lingered behind me, talking about how they survived the fight with the monster."
    "The Qiongqi's head dangled from my grasp, dripping thick, acrid blood that left a crimson trail in the pure white snow. Its weight didn't bother me—I'd carried far worse."

    jump ch2_palace

# =============================================================================
# SECTION 6: LABEL CH2_PALACE — Mjoll Palace (Gustav's Court)
# =============================================================================
# PDF pages 61-63.
# =============================================================================

label ch2_palace:

    # [COMMENT: mjoll_palace_throne — guards stiffened at gates, incense in throne room]
    scene bg_mjoll_icelands with fade      # PLACEHOLDER — Mjoll throne room
    play music ost_mjoll_palace fadein 2.0      # PLACEHOLDER — stiff court theme

    show dorian sad at left_char with Dissolve(0.2)
    "When we reached the gates of the palace, the guards stiffened, their pale faces betraying their unease. They exchanged glances but didn't dare to stop me. As I pushed through the heavy doors, Vasily trailing close behind."

    hide dorian
    scene mjoll_palace_throne with dissolve

    show dorian sad at left_char with Dissolve(0.2)
    "We enter the throne room; the smell of incense hangs thick in the air. A group of Aldoriths knelt on the cold stone floor, their heads bowed low."
    "At the far end of the room, King Gustav Nordstrom sat upon his gilded throne, his face as hard as the icy mountains that surrounded Mjoll. Beside him, Queen Ekaterina Drakos sat, her dark eyes gleaming."
    
    hide dorian
    show king_gustav at right_char 
    show vasily neutral at left_char
    with Dissolve(0.2)
    vasily "Enoch above. Another punishment?"
    "One of the kneeling Aldoriths—a young man with striking purple hair—raised his head."

    hide vasily
    show svante normal_nervous at left_char with Dissolve(0.2)
    svante "Please, Father! I beg you! I didn't mean to—"
    king_gustav "You dare speak to me that way, boy? You've been given every chance to prove your worth, and yet you continue to disappoint me."

    "The queen leaned forward, her voice a venomous whisper."
    hide svante

    show queen_ekaterina at left_char with Dissolve(0.2)
    queen_ekaterina "Svante should be grateful, Your Highness. Without your guidance, he'd be no better than a stray mutt."
    hide queen_ekaterina
    show kristin_normal at left_char with Dissolve(0.2)             # PLACEHOLDER — Kristin sprite
    kristin         "Quiet, Svante. You'll only make it worse for us. Please…"
    hide kristin_normal
    show boy_ald_normal at left_char with Dissolve(0.2)                # PLACEHOLDER — boy_ald sprite
    boy_ald         "Worse? What more can he take from us that he hasn't already?"
    hide boy_ald_normal
    "I step closer and into the throne room, the soldiers following at a distance, the Qiongqi's head dripping blood onto the pristine marble floor."

    # show dorian serious at left_char with Dissolve(0.2)
    king_gustav "Enough! That goes for all of you. If you disobey, you will be beheaded like your brothers and sisters. IS THAT CLEAR? You are nothing without my name. Nothing!"
    "Yes, Father."

    show queen_ekaterina at left_char with Dissolve(0.2)
    queen_ekaterina "Svante speaks like he's a prince, but look at him—groveling like the dog he is."
    hide queen_ekaterina
    show svante normal_nervous at left_char with Dissolve(0.2)
    svante "I… I'm sorry, Father… Please forgive me… I—"
    hide svante
    hide king_gustav

    show dorian normal_alt_annoyed at left_char with Dissolve(0.2)
    "I step forward then, the Qiongqi's head swinging in my grasp, its blood dripping onto the pristine marble floor. The sound of the impact silences the room."
    "The Aldoriths freeze, their wide eyes darting to me."
    show boy_ald_normal at right_flip with Dissolve(0.2)                # PLACEHOLDER — boy_ald sprite
    boy_ald "It's him…"
    hide boy_ald_normal
    show svante normal_neutral at right_char with Dissolve(0.2)
    svante  "The Dragon of Gale…"
    hide svante
    show king_gustav at right_char with Dissolve(0.2)
    king_gustav "Ah, Dorian. You've returned. Efficient as always. What news of the beast?"

    "I drop the Qiongqi's head unceremoniously onto the floor."

    show dorian normal_alt_annoyed at left_char
    dorian "The beast is dead. Your kingdom is safe, for now. My payment."

    "The king gestures lazily, and a servant scurries forward, pressing a heavy pouch of gold into my hand. I take it without ceremony, glancing briefly at Vasily."

    dorian "Thanks."
    king_gustav     "This particular Qiongqi has terrorized these lands for a month now, devouring livestock, destroying villages, and killing many of my subjects. The people of Mjoll will sleep easier tonight thanks to you."
    hide king_gustav
    show queen_ekaterina at right_flip with Dissolve(0.2)
    queen_ekaterina "You've done this kingdom a great service. And for that, we shall show our gratitude."
    hide queen_ekaterina

    show vasily alt_normal at right_char with Dissolve(0.2)
    vasily "You've done what no one else could, Dorian. The King wants to make a spectacle of this victory, a display of his generosity to the people. He'll reward you handsomely if you make an appearance tomorrow."

    show dorian serious at left_char
    dorian "Tomorrow?"
    vasily "Yes, tomorrow. There'll be a celebration for the people. They wanted to celebrate your slaying of the Qiongqi."

    "I glance down at the bloodied pouch of gold in my hand."

    show dorian normal_alt_calm at left_char
    dorian "I'll be there."
    show dorian serious at left_char
    "As I turn to leave, I hear the Aldoriths' voices behind me, trembling and desperate."
    hide dorian
    hide vasily
    show king_gustav at right_char 
    show svante normal_nervous at left_char
    with Dissolve(0.2)
    svante  "Father, please, I only sought to prove my loyalty! Give me another chance!"
    hide svante
    show kristin_normal at left_char with Dissolve(0.2)                # PLACEHOLDER — Kristin sprite
    kristin "We'll do anything—just let us stay by your side!"
    hide kristin
    king_gustav "You've embarrassed me for the last time. Guards, take them to the dungeon. Perhaps some time in the dark will teach you the value of obedience."
    hide king_gustav
    show queen_ekaterina at right_flip with Dissolve(0.2)
    queen_ekaterina "They're lucky they didn't end up like the others. You're far too kind, my love."
    hide queen_ekaterina
    hide kristin_normal

    "I don't look back as the Aldoriths' pleas turn to sobs, swallowed by the clang of armor and the heavy slam of the dungeon doors."

    scene bg_mjoll_icelands with dissolve

    "Vasily catches up to me as I leave the palace, the snow crunching beneath our boots."

    show dorian serious at left_char 
    show vasily alt_normal at right_char
    with Dissolve(0.2)
    vasily "Dorian, look. You don't have to come tomorrow, you know. But the King won't forget if you don't. And neither will the people."
    dorian "Let them remember what they want. I just want my gold."

    "Vasily places a hand on my shoulder."

    show vasily alt_think at right_char
    vasily "My offer still stands, okay? Let me know if you want to grab a beer or two. On me."

    "I nod. The wind bites at my face as I head back into the streets of Mjoll, my path lit only by the faint glow of lanterns. I clutch the pouch tightly, its weight pulling at my hand."

    hide dorian
    hide vasily
    jump ch2_cave


# =============================================================================
# SECTION 7: LABEL CH2_CAVE — Dorian's Cave (Grief / Dinner Alone)
# =============================================================================
# PDF pages 63-64.
# =============================================================================

label ch2_cave:

    # PDF p63
    # [COMMENT: dorians_cave_on — fur curtain doorway, small fireplace, flickering shadows]
    scene dorians_cave_on with fade               # PLACEHOLDER — cave interior, firelight
    stop music fadeout 2.0
    play music ost_cave_grief fadein 3.0        # PLACEHOLDER — fragile grief theme
    play audio amb_cave_fire loop fadein 2.0    # PLACEHOLDER — crackling fire ambient

    show dorian sad at left_char with Dissolve(0.2)
    "I go back to my small cave, the entrance of which is shielded by a curtain of thick furs, swaying slightly in the icy wind of Mjoll."
    "I duck inside, pulling the curtain closed behind me, shutting out the biting cold. The glow of a small fireplace greets me, casting flickering shadows on the rough stone walls."
    "I kneel by the fireplace, adding another log to the fire. From the small stash of ingredients I've gathered over the years, I begin to prepare dinner."
    "I set out six simple plates, each one mismatched and worn, around a low wooden table I carved myself."
    "I ladle out portions of the stew I've cooked—one for me, and five for them."
    "I sit in my usual spot, looking at their plates."

    # These lines are ghost-voices from memory — no sprites for family here
    # sad dorian sprite
    elara  "Kids, come on. Haven't your father and I taught you some table manners?"
    lucas  "Mom, can we go play in the snow after this?"
    emily  "Mmm the stew tastes good, Dad!"
    daniel "Stop sucking up to dad, Emily!"
    sarah  "Guys, stop moving! You'll get food all over my sketchbook!"
    elara  "Aren't they adorable, Dorian? I miss you, my heart."

    # PDF p64
    "I see their smile, the way they always knew how to make this cold, harsh world feel warm."
    "The fire crackles and I eat slowly, savoring down very bite, even as the food grows colder."

    dorian "I'm sorry… I wasn't there. I should've been there. I…"

    "I ball up my fist and continue eating. After I finished my meal, I head back to my bedroll."
    hide dorian
    scene black with fade
    "I close my eyes, letting the weight of exhaustion pull me under. Tomorrow will come, and with it, another mission, another royal errand, another reason to keep moving."

    
    stop music fadeout 2.0
    stop audio fadeout 1.0

    jump ch2_square_intro


# =============================================================================
# SECTION 8: LABEL CH2_SQUARE_INTRO — Town Square Setup
# =============================================================================
# PDF pages 64-66.
# =============================================================================

label ch2_square_intro:

    # PDF p64
    # [COMMENT: bg_mjoll_square_festive — booths being set up, thin snow falling, merchants bustling]
    scene bg_mjoll_square_festive with fade
    play music ost_mjoll_festive volume 0.4 fadein 2.0  # PLACEHOLDER — light festive theme

    "The city square of Mjoll is already alive with activity as I arrive the next day. The air is brisk, the cold biting but not enough to faze me anymore."
    "Booths are being set up around the square, their wooden frames dusted with a thin layer of snow. Merchants and servants bustle about, their breath forming small clouds in the icy air."
    "I spot Vasily almost immediately, standing near the center of the square. He's barking out orders, pointing left and right."

    show vasily alt_aggressive at right_char with Dissolve(0.2)
    vasily "Make sure the performers don't miss a single beat. We don't want to have any on-the-spot beheadings this time around. We don't want any blood on our booths now, would we?"

    "Sir!"
    "The crowd disperses, and I approach him. When he catches sight of me, his eyebrows shoot up in surprise."

    show vasily alt_normal at right_char
    vasily "Dorian? Already here?"

    "I fold my arms, shrugging slightly."

    show dorian normal_alt_neutral at left_char with Dissolve(0.2)
    dorian "Why wouldn't I be?"
    vasily "Oh, silly me. When have you not been early? You'd show up to your own funeral two hours in advance just to make sure everything's running smoothly."

    "I don't respond, letting the comment hang in the cold air. Vasily studies me for a moment, his expression softening."

    show vasily alt_think at right_char
    vasily "The event doesn't start for another two hours, you know."
    show dorian neutral at left_char
    dorian "I'm aware. Just wanted to check the area."

    "He raises an eyebrow but doesn't press further. Instead, he gestures to the booths around us."

    show vasily alt_normal at right_char
    vasily "The king and queen will be here later, but as you can see, we've got quite the spectacle planned. Feast, performances, and of course…"

    "He leans in slightly, lowering his voice."

    vasily "…the presentation of the Qiongqi's head. It'll be the centerpiece."

    show dorian normal_alt_annoyed at left_char
    dorian "Don't you think it's a little extravagant?"
    vasily "You know His Highness. Also, the people need something to rally around. After everything that's happened, a little morale boost goes a long way."
    
    show dorian sad at left_char
    "I stay silent, my gaze drifting across the square. Children laugh as they chase each other around the booths. Adults are happily chatting with each other as the snow lightly falls."

    vasily "You should get some rest, Dorian. Come back when the festivities start. You've done your part."
    show dorian serious at left_char
    dorian "I'm fine."

    "He sighs, muttering something under his breath."

    show vasily alt_think at right_char
    vasily "Suit yourself. Just don't scare the merchants."

    show dorian normal_alt_neutral at left_char
    "I smirk faintly at his jab but say nothing."

    show vasily alt_normal at right_char
    vasily "Come to think of it…"

    "I glance at him, raising a brow."

    dorian "What?"

    "He folds his arms and smirks."

    show vasily alt_savage at right_char
    vasily "You're already here. Why not help me check the booths? Make sure everything's up and running?"

    "I scoff, shaking my head."

    show dorian normal_alt_annoyed at left_char
    dorian "Not interested."
    vasily "Dorian, come on. When's the last time you did something remotely enjoyable? When's the last time you had fun?"

    "I narrow my eyes at him."

    show dorian sad at left_char
    dorian "Every night. When I spend my time with my family."

    "He nudges my shoulder gently."

    show vasily alt_think at right_char
    vasily "Hmm… Yeah, but you could use a distraction. Look, if you join me, I'll make it worth your while."

    "I raise a skeptical brow."

    show dorian normal_alt_neutral at left_char
    dorian "How?"

    show vasily alt_normal at right_char
    vasily "Gold. From the king, naturally. Consider it… an incentive for your services."

    "I let out a slow breath, crossing my arms as I mull it over."

    show dorian neutral at left_char
    dorian "Fine. Let's get this over with."
    show vasily alt_savage at right_char
    vasily "That's the spirit, friend!"

    "He claps me on the back, his grin widening."
    show vasily neutral at right_char
    "As we begin to walk through the square, Vasily dives into his element, greeting merchants, inspecting goods, and occasionally throwing in a comment or two about how to make things 'more appealing to the people.'"
    "I follow in silence, my eyes scanning the colorful displays and the array of items on sale."
    "The scents of freshly baked bread and spiced meat waft through the air, mingling with the faint chill of the snow. People are beginning to trickle into the square, as we walk on by."

    vasily "See? Not so bad, is it? Unfortunately, the merchant who sells Mjollian Mead-Braised Lamb was mercilessly killed by a yaoguai before coming here so… we might have to settle for less."

    "I grunt in response, earning a chuckle from him."

    show vasily alt_normal at right_char
    vasily "Alright, Dorian. Since you're tagging along, where do you want to go? Completely up to you."

    jump ch2_freetime

# =============================================================================
# SECTION 9: LABEL CH2_FREETIME — D2 Free Time Menu (4 options)
# =============================================================================
# Uses 'call' to visit sub-scenes; each ends with 'return'.
# After the spa, the game forces a visit to the fortune teller before CommonCommon.
# =============================================================================
label ch2_freetime:
    menu:
        "Visit the food stalls." if not ch2_visited_food:
            $ ch2_visited_food = True
            call ch2_food_stalls from _call_ch2_food_stalls
            jump ch2_freetime

        "Visit the fortune teller." if not ch2_visited_fortune:
            $ ch2_visited_fortune = True
            call ch2_fortune from _call_ch2_fortune
            jump ch2_common_freetime

        "Relax at the spa." if not ch2_visited_spa:
            $ ch2_visited_spa = True
            call ch2_spa from _call_ch2_spa
            if not ch2_visited_fortune:
                $ ch2_visited_fortune = True
                call ch2_fortune from _call_ch2_fortune_1
            jump ch2_common_freetime

        "Rest with Vasily." if not ch2_visited_rest:
            $ ch2_visited_rest = True
            call ch2_rest from _call_ch2_rest
            jump ch2_common_freetime

# =============================================================================
# SECTION 10: FREE TIME SUB-SCENE LABELS
# =============================================================================
# -----------------------------------------------------------------------------
# D2-A: FOOD STALLS
# Sub-choice: Confront the guards or Do Nothing
# -----------------------------------------------------------------------------
label ch2_food_stalls:
    # [COMMENT: bg_mjoll_food_stalls — cast iron cauldrons, smoked fish, bread bowls steaming]
    scene bg_mjoll_food_stalls with dissolve    # PLACEHOLDER — Mjollian food stalls

    show dorian neutral at left_char
    show vasily alt_normal at right_char
    with Dissolve(0.2)
    "Vasily and I decided to stroll through the food stalls, the air thick with the aroma of roasted fish, hearty soups, and fresh-baked bread. The snow-covered streets contrast with the vibrant colors of the vendors' booths."

    vasily "Ah, here we go, Dorian. Mjollian cuisine is second to none. Let me guess, you haven't eaten anything decent in weeks."
    show dorian normal_alt_neutral at left_char
    dorian "Hmph."

    "I grunt in response, but my stomach betrays me with a growl. He smirks and gestures toward a booth with a large cast iron cauldron."

    hide vasily
    show vendor_mjoll at right_char with Dissolve(0.2)       # (ladling stew)

    vendor_mjoll "Two Zarybas, fresh and hot! Best in all of Mjoll!"
    hide vendor_mjoll

    show vasily neutral at right_char with Dissolve(0.2)
    "Vasily hands over a few coins and passes me one of the bread bowls."

    show vasily alt_think at right_char
    vasily "Eat, friend. You'll thank me later, hungry grumpy man."

    # [COMMENT: FOOD4 — Zaryba Stew: smoked sturgeon, root vegetables, wild herbs, served in thick crusty bread bowls]
    "I take a bite. The smoky, savory flavor of the sturgeon hits me first, followed by the earthiness of the parsnips and turnips. The bread, soaked in the stew, is soft yet hearty. It's... surprisingly good."

    show dorian neutral at left_char
    dorian "It's… *groans*"
    show vasily alt_normal at right_char
    vasily "See? I told you. Nothing like food to make life a little less bleak."
    show dorian sad at left_char
    dorian "…"
    show vasily alt_think at right_char
    vasily "You know, you could make this easier on yourself. You've been carrying this weight for four years. Maybe it's time to let some of it go."

    "I don't answer, focusing instead on the meal. Vasily knows better than to push further and continues eating."
    "As we get up to leave, I catch sight of the vendor. She stands at the edge of the stall, watching the guards escort two boys carrying heavy crates. Her eyes are filled with tears."

    hide vasily
    hide dorian
    show male_soldier_1 at right_char
    show boy_ald at left_char
    with Dissolve(0.2)            # PLACEHOLDER — Boy Aldorith (straining under crate)
    male_guard  "Come on! Pick up the pace, will ya? Don't make me bring out the whip!"
    boy_ald_spa "Please, sir! We just need a drink!"
    hide male_soldier_1
    show female_guard at right_char with Dissolve(0.2)
    female_guard "You'll get your drink after an hour! Now get back to work!"
    hide female_guard
    hide boy_ald

    show vasily alt_think at right_char
    show dorian serious at left_char
    with Dissolve(0.2)
    vasily "Come on, friend. Don't get any ideas. You can't save everyone."
    "The vendor glances toward me briefly."

    # -----------------------------------------------------------------------
    # D2-A SUB-CHOICE: Confront or Do Nothing
    # -----------------------------------------------------------------------
    menu:
        "Confront the Guards.":
            $ ch2_food_choice = "confront"

            hide vasily
            show dorian serious at left_char with Dissolve(0.2)
            "I clench my fists, stepping toward the guards as they bark orders at the two kids."

            dorian "Let them rest. They're just kids."

            "The guards turn, startled, before recognizing me. One of them straightens up, puffing out his chest."

            show male_soldier_1 at right_char with Dissolve(0.2)
            male_guard "Stay out of this, mercenary. These children are property of the Crown. They do as they're told."

            "The vendor watches silently, her hands trembling."

            show dorian normal_alt_annoyed at left_char
            dorian "They look half-dead. If you push them any further, they'll collapse."
            male_guard "Then they collapse. Not our problem their constitution's weak."

            hide male_soldier_1
            show female_guard at right_char with Dissolve(0.2)
            female_guard "Y-You fool! Th-that mercenary is the Dragon of Gale."
            hide female_guard
            show male_soldier_1 at right_char with Dissolve(0.2)
            male_guard   "What? O-Oh… Um… Sure. Kids, break time!"
            hide male_soldier_1

            "The two kids immediately run to the vendor to get some water."

            show vendor_mjoll at right_char with Dissolve(0.2)   # PLACEHOLDER — Vendor sprite
            vendor_mjoll "Here's some water. Please drink. Are you hungry, my children?"
            hide vendor_mjoll

            show vasily alt_think at right_char with Dissolve(0.2)
            show dorian normal_alt_neutral at left_char
            vasily "*sighs* You just had to make a scene. Let's go."

        "Do nothing.":
            $ ch2_food_choice = "nothing"

            show dorian sad at left_char
            show vasily alt_think at right_char
            with Dissolve(0.2)
            "I glance at the vendor, then at the guards. My fists clench, but I force myself to stay rooted in place."
            "The vendor's gaze meets mine for a moment, her eyes pleading, but I look away. Vasily doesn't say anything—he knows what I'm feeling, even if I don't show it."

            dorian "…"
            vasily "Let's go, Dorian. Nothing to see here."

            "As we walk away, I hear the guards bark another order at the children. A crate crashes to the ground, followed by the sound of a whip cracking. A woman's stifled sob is the last thing I hear as we round the corner."

    show dorian neutral at left_char
    show vasily alt_normal at right_char
    vasily "I know what you're thinking. You want to charge in, right every wrong. But that's not how Mjoll works, Dorian."
    vasily "This place… It survives because of the system. The King and Queen, for all their flaws, keep the kingdom standing."

    show dorian normal_alt_annoyed at left_char
    dorian "You really believe that?"

    "Vasily doesn't answer immediately."

    show vasily alt_think at right_char
    vasily "I believe that survival comes at a cost. You've paid yours. Maybe it's time to stop paying for everyone else's."

    "I stay silent, the taste of the Zaryba still lingering on my tongue, now bitter."

    hide dorian
    hide vasily
    return


# -----------------------------------------------------------------------------
# D2-B: FORTUNE TELLER — BABALA
# Sub-choice: Ask about family or ask about companions
# Both branches converge on the Five Companions prophecy
# -----------------------------------------------------------------------------

label ch2_fortune:
    # [COMMENT: bg_mjoll_violet_tent — dim, violet curtains, crystal orb glowing faintly, incense]
    scene bg_mjoll_violet_tent with dissolve    # PLACEHOLDER — Babala's booth interior
    play music ost_babala_prophecy fadein 2.0   # PLACEHOLDER — ethereal prophecy theme

    show dorian neutral at left_char
    show vasily alt_normal at right_char
    with Dissolve(0.2)
    "Vasily nudges me toward the dimly lit booth draped in heavy, violet curtains. A crooked, hastily-painted sign outside reads: 'Babala: Your Fate Awaits.'"
    
    vasily "Oh she's back in town!"
    show dorian normal_alt_neutral at left_char
    dorian "Really? Who?"
    show vasily alt_aggressive at right_char
    vasily "Babala. She's a fortuneteller. They say she never misses with her fortunes. I'd say it's worth a try. She's—"
    show dorian normal_alt_annoyed at left_char
    dorian "Not interested."
    show vasily alt_normal at right_char
    vasily "Come on, Dorian. I'd say it's worth a try."

    "I glare at him."

    show dorian serious at left_char
    dorian "Fortunes are just words to me, Vasily. Nothing more."
    show vasily alt_savage at right_char
    vasily "Words have power, you know. Besides, maybe she'll tell you about your love life. Don't you think it's time to move on?"

    "I stop in my tracks, the air around us growing cold."

    show dorian angry at left_char
    dorian "I will never remarry, Vasily. Don't bring that up again."

    "The fortune teller, a middle-aged woman, with white eyes, peeks out from the curtains, chuckling softly."
    show dorian normal_alt_annoyed at left_char
    hide vasily
    show babala at right_char with Dissolve(0.2)
    babala "Haha. You are as stubborn as the stone you channel, Dragon of Gale. But even the hardest stone cracks in time."

    "Vasily laughs, patting my shoulder."
    # vasily laugh 042 in files

    # PDF p70
    "We step inside. The booth is small but warm, the scent of incense hanging in the air. A crystal orb glows faintly on the table, and behind it sits Babala."
    "She looks up, her lips curling into a knowing smile."
    show dorian serious at left_char
    babala "The Dragon of Gale. I wondered when you'd visit me."
    hide babala
    show vasily alt_savage at right_char with Dissolve(0.2)
    vasily "He didn't want to come, of course, but I dragged him here. Babala, tell him something interesting—preferably about his love life."
    # v laugh 043
    hide vasily
    show babala at right_char with Dissolve(0.2)
    babala "*laughing* Your friend has a sharp tongue."

    "I glare at Vasily, but Babala's chuckle draws my attention back to her."
    babala "Sit, child of fire. Let the Weaver guide us."
    "I hesitate before sitting across from her. Her gaze turns distant as she places her hands on the crystal orb."

    babala "The Weaver… the one who spun the first threads of existence. From the void, she created the Tetrad—four immortal beings who shaped the world."
    babala "Together, they wove the earths, the waters, the heavens, and all life. But it is the Weaver who holds all fates in their loom."

    "Her voice takes on a reverent tone, and for a moment, the air feels heavier."

    babala "And now, she weaves your threads, Dragon of Gale."

    show dorian sad at left_char
    dorian "Th-that's great, I guess."
    show dorian serious at left_char
    "The crystal orb flickers, and a faint swirl of smoke begins to rise. Babala's eyes widen slightly, and her lips curl into a smile."

    babala "Normally, I allow people to ask one question, but for you, Dragon, I will permit two. Fate bends itself for those who walk in its shadow."
    hide babala
    show vasily alt_think at right_char with Dissolve(0.2)
    vasily "*laughs jealously* Why the special treatment?"

    "Babala doesn't answer him. The swirling smoke grows, curling around me like an embrace. It feels strangely comforting, and I instinctively close my eyes."
    hide vasily
    show babala at right_char with Dissolve(0.2)
    babala "Don't fight it, Dragon. Open your heart to me."

    "She leans forward, her voice dropping to a whisper."

    babala "Do not fight it, Dragon. Let your heart guide your words to the Weaver's threads. Ask me anything you wish to know."

    show dorian normal_alt_neutral at left_char
    dorian "Anything, huh?"

    # -----------------------------------------------------------------------
    # D2-B SUB-CHOICE: Family or Companions
    # -----------------------------------------------------------------------
    menu:
        "How is my family doing?":
            $ ch2_babala_asked_family = True

            show dorian sad at left_char
            dorian "I want to know how is my family doing."

            "Babala's expression softens, and the crystal orb flares with light."

            babala "Your family… they have passed on to Tianlun, the Eternal Realm of Peace. Elara cradles your children in her arms, and their laughter echoes through fields of gold."
            babala "Daniel. Emily. Sarah. Lucas. They are at peace, Dorian. But they watch over you still, their love woven into your every step."

            "My throat tightens, and I can barely speak."

            show dorian neutral at left_char
            dorian "They're… happy?"
            babala "Happier than you can imagine. But they long for you to find your peace as well."

            "Vasily places a hand on my shoulder, his usual teasing replaced with quiet support."

            show dorian sad at left_char
            dorian "Elara…"

            babala "But the threads of fate are not yet finished. We must look to the future."
            hide babala
            show vasily alt_think at right_char with Dissolve(0.2)
            vasily "I think Dorian's had enough—"
            hide vasily
            show babala at right_char with Dissolve(0.2)
            
            # TODO: add audio
            # Thunder — the orb blazes, Babala transforms into the vessel of prophecy
            # play sound sfx_prophecy_thunder     # PLACEHOLDER — thunder crack SFX
    
            babala "Before your time is up, you will hold another daughter in your arms. She will bring you peace, Dragon. A second chance at family, a chance to heal what was broken."
            show dorian serious at left_char
            "Another daughter? How could I even think of raising another child after what happened to Elara and the kids?"

            show dorian neutral at left_char
            dorian "That'll be impossible since I'll never remarry but, thank you."

            "The booth grows colder as her voice rises."

        "How are my companions?":

            show dorian neutral at left_char
            "My thoughts drift to the others—Paladin Feng, Paladin Cyrus, Empress Olympia, the soldiers who stood beside me during the Tragedy of Tianho."

            dorian "I want to know… how are my past companions?"

            babala "Your companions remain strong. Paladin Feng heals slowly but surely; his resolve is unbroken. Empress Olympia rebuilds what was lost, her strength inspiring those around her."
            babala "Paladin Cyrus has moved on… As for Count Vasily…"
            hide babala
            show vasily neutral at right_char
            vasily "You do realize I'm standing right here, don't you?"

            "She glances at him, a smirk tugging at her lips."
            
            hide vasily
            show babala at right_char with Dissolve(0.2)
            babala "He frets over you more than he lets on."
            hide babala
            show vasily alt_aggressive at right_char
            vasily "I do not fret."
            hide vasily
            show babala at right_char with Dissolve(0.2)
            babala "But the threads of fate do not end here. We must look to the future."
            hide babala
            show vasily alt_think at right_char
            vasily "Well, that's enough fortune-telling for one day, don't you think? We sho—"

            # Thunder interrupts Vasily
            # play sound sfx_prophecy_thunder     # PLACEHOLDER — thunder crack SFX
            hide vasily
            show babala at right_char with Dissolve(0.2)
            "A sudden crash of thunder interrupts him. The orb glows fiercely, and Babala's voice grows deeper, more resonant. Smoke surrounds her, and her eyes shine with an unnatural light."
            "The booth grows colder as her voice rises."

    # -----------------------------------------------------------------------
    # Both sub-choices converge on the Five Companions prophecy
    # PDF p71-72 (family) / p72-73 (companions)
    # -----------------------------------------------------------------------

    babala "I see you surrounded by five figures. Five men, each unique and powerful. They will walk beside you, bound by loyalty and something deeper. Together, you will face the storm that looms ahead."
    babala "Beware, Dragon. A great calamity will strike Ena, and only you and your companions may stand against it. The Weaver's threads will guide you, but the path will not be easy."

    "The light fades, and Babala slumps in her chair, panting."

    show dorian neutral at left_char with Dissolve(0.2)
    babala "*pants* You're welcome."
    hide babala

    show vasily alt_normal at right_char with Dissolve(0.2)
    vasily "Well… that's something, isn't it?"

    "As Vasily and I leave the booth, he tries to lighten the mood with a joke."

    show vasily alt_savage at right_char
    vasily "Five men, huh? Looks like you're going to be popular."

    "I shake my head, the weight of Babala's words pressing heavily on my chest."

    dorian "Let's move on, Vasily."

    hide dorian
    hide vasily
    stop music fadeout 2.0

    return


# -----------------------------------------------------------------------------
# D2-C: SPA
# PDF pages 73-76.
# Sub-choice: Do nothing (walk away) or Punish the noblewoman (swallow her)
# After spa, game redirects to fortune teller if not yet visited
# -----------------------------------------------------------------------------

label ch2_spa:
    # [COMMENT: bg_mjoll_spa — heated stone pools, steam, nobles lounging, aldorith workers]
    scene bg_mjoll_spa with dissolve            # PLACEHOLDER — Mjollian spa interior

    show dorian neutral at left_char
    show vasily alt_normal at right_char
    with Dissolve(0.2)
    "The spa's grand facade rises before us, smoke wafting from its chimneys."

    show dorian normal_alt_neutral at left_char
    dorian "Maybe the spa would be a good idea."
    show vasily alt_savage at right_char
    vasily "A spa? Hmm I love it! Perfect!"

    "We step into the spa, the warmth of the heated pools doing little to thaw the chill in my chest. The nobles recline in luxurious pools while aldorith attendants bustle about, their eyes downcast, their bodies worn thin from endless labor."
    "A young aldorith boy, looking no older than ten, struggles with a heavy bucket of steaming water, his hands trembling from the heat. He stumbles, spilling water onto his arm. His face contorts in pain, but he quickly bows his head, attempting to clean the mess with his sleeve."
    hide vasily 
    show girl_ald_spa at right_char_kids with Dissolve(0.2)       # PLACEHOLDER — girl aldorith sprite
    girl_ald_spa "Brother! Let me help you!"

    "Nearby, a noblewoman watches with disdain."
    hide girl_ald_spa
    show dorian serious at left_char
    show noblewoman at right_char with Dissolve(0.2)              # PLACEHOLDER — Noblewoman sprite (fan raised)

    noblewoman  "Disgusting, clumsy brat! Do you think I pay for this kind of incompetence?"
    hide noblewoman
    show boy_ald_spa at right_char_kids with Dissolve(0.2)        # PLACEHOLDER — boy aldorith sprite
    boy_ald_spa "I-I'm sorry, mam! I didn't mean to—"

    "She lashes out with her fan, striking the boy across the face. The sound echoes through the room. He flinches but doesn't cry out."
    hide boy_ald_spa
    "I glance at the boy, my jaw tightening. A pang of something sharp hits my chest—Sarah. Lucas. Emily. Daniel."

    show dorian angry at left_char
    show vasily alt_think at right_char with Dissolve(0.2)
    vasily "Dorian…"
    vasily "I know what you're thinking. But don't. This place… It's not Gale. And it's not Tianho."

    show dorian sad at left_char
    dorian "Tianho. As if I could forget."
    show vasily alt_normal at right_char
    vasily "You think I don't remember, too? I lost people there. You weren't the only one who—"
    show dorian normal_alt_annoyed at left_char
    dorian "Don't. Besides, I don't care. These kids... they're not my problem."
    show dorian serious at left_char

    "The noblewoman sees a young girl scrubbing the floor nearby. Her hands are raw, the skin peeling from the harsh soaps and constant work."
    "She pauses for a moment to wipe sweat from her brow, and the same noblewoman snaps her fan toward her."
    hide vasily
    show noblewoman at right_char with Dissolve(0.2)             # PLACEHOLDER — Noblewoman sprite
    noblewoman   "Don't stop! If I can see my reflection in the marble, you're not scrubbing hard enough!"

    "The girl nods quickly, her small body trembling as she works faster."
    "I glance back at the boy, who's still scrubbing the floor with raw, trembling hands. The noblewoman raises her fan to hit him again, but the girl tries to shield him from the noblewoman's wrath."
    hide noblewoman
    show girl_ald_spa at right_char_kids with Dissolve(0.2)      # PLACEHOLDER — girl aldorith sprite
    girl_ald_spa "P-Please, mam. Forgive us."
    hide girl_ald_spa
    show noblewoman at right_char with Dissolve(0.2)          # PLACEHOLDER — Noblewoman sprite
    noblewoman   "Incompetent aldoriths! I'll have you both dragged out and hanged for disobeying a noble!"
    "The girl freezes, her eyes wide with terror as tears spill down her cheeks. The boy drops to his knees, scrubbing furiously at the floor, his shoulders shaking."

    hide noblewoman
    show boy_ald_spa at right_char_kids           # PLACEHOLDER — boy aldorith sprite
    boy_ald_spa  "Mam, I-I… *crying*"
    hide boy_ald_spa
    show girl_ald_spa at right_char_kids with Dissolve(0.2)    # PLACEHOLDER — girl aldorith sprite
    girl_ald_spa "Please, ma'am. He didn't mean it. We'll do better, I promise— *sniffling*"
    hide girl_ald_spa
    show noblewoman at right_char with Dissolve(0.2)             # PLACEHOLDER — Noblewoman sprite
    noblewoman   "Cry and beg all you want! You'll both be weeping when they tie the noose around your heads!"

    "The boy's shoulders shake, silent sobs wracking his small frame. The girl clutches his arm, her tears falling onto the already-damp floor."

    show dorian serious at left_char
    dorian "…"

    # -----------------------------------------------------------------------
    # D2-C SUB-CHOICE: Do Nothing or Punish the Noblewoman
    # PDF p74-75
    # -----------------------------------------------------------------------
    menu:
        "Do nothing.":
            $ ch2_spa_choice = "nothing"

            show dorian sad at left_char
            "I turn away, forcing my gaze back to the warm pools and the pampered nobles. The boy's muffled sobs and the girl's quiet pleading fade into the background as I try to block it all out."
            hide noblewoman

            show vasily alt_think at right_char with Dissolve(0.2)
            vasily "Come on. Let's get out of here."
            dorian "…"

            hide vasily
            show boy_ald_spa at right_char_kids with Dissolve(0.2)
            boy_ald_spa "Mam, please. We'll do anything… Please! *crying*"
            hide boy_ald_spa
            show noblewoman at right_char with Dissolve(0.2)     # PLACEHOLDER — Noblewoman sprite
            noblewoman  "Get your filthy hands off my feet! Come dawn, you'll hang like the worthless scum you are. And I'll laugh as your bodies sway in the wind."

            show dorian normal_alt_annoyed at left_char
            dorian "Scum…"

            "I force myself to walk away."
            hide noblewoman

        "Punish the noblewoman.":
            $ ch2_spa_choice = "punish"

            show dorian normal_alt_calm at left_char
            "I close my eyes briefly, channeling the energy deep within me. The ground beneath her feet shifts silently, imperceptibly."
            "She doesn't even notice."

            # TODO: add sfx
            # play sound sfx_ground_swallow       # PLACEHOLDER — earth swallow SFX

            show noblewoman at right_char with Dissolve(0.2)
            noblewoman "AAHHHHH!!!!"

            "As she steps back, the marble tiles give way. A small, perfect hole opens beneath her. She gasps, but no sound escapes as the ground swallows her whole. The hole seals as quickly as it appeared, leaving nothing behind."
            hide noblewoman with Dissolve(0.5)

            "The children stare at the empty space, confused."

            show vasily alt_mad at right_char with Dissolve(0.2)
            vasily "Merciful Enoch…"
            vasily "Dorian… what did you just do? What happened to the noblewoman?"

            show dorian serious at left_char
            "I walk away."

            dorian "Like I said, Vasily, I don't care."

    hide dorian
    hide vasily
    scene bg_mjoll_icelands with dissolve

    show dorian neutral at left_char
    show vasily alt_normal at right_char
    with Dissolve(0.2)
    "We step out of the spa, the cold air biting at my skin, a stark contrast to the warmth we just left behind."
    "My interest in the place has completely faded."

    show dorian normal_alt_neutral at left_char
    dorian "Maybe we should try someplace else."

    "Vasily glances at me, his expression unreadable for a moment, before giving a small nod."

    show vasily alt_think at right_char
    vasily "Fair enough. Let's see the other booths."

    hide dorian
    hide vasily
    return

# -----------------------------------------------------------------------------
# D2-D: REST WITH VASILY
# A quiet moment. Vasily naps.
# -----------------------------------------------------------------------------
label ch2_rest:

    # [COMMENT: bg_mjoll_pavilion — cushioned seats, fur-lined blankets, canopy, tucked from noise]
    scene bg_mjoll_pavilion with dissolve       # PLACEHOLDER — quiet canopied pavilion

    show dorian neutral at left_char
    show vasily alt_normal at right_char
    with Dissolve(0.2)

    "I glance at Vasily, raising an eyebrow as I gesture to a small, shaded pavilion tucked away in the corner of the square."
    "It's a simple structure—a cozy area reserved for the royal advisor to escape the noise and chaos. Cushioned seats and thick, fur-lined blankets are arranged beneath the canopy."

    show dorian normal_alt_neutral at left_char
    dorian "You keep telling me I need to relax. Why don't you take your own advice for once?"

    show vasily alt_think at right_char
    vasily "Relax? In the middle of the square? You must be joking."

    show dorian normal_alt_confident at left_char
    dorian "You have your own private area over there. No one will bother us. You look like you haven't slept in days, Vasily."

    show vasily alt_normal at right_char
    "He scoffs, rubbing his temples. After a moment of hesitation, he nods."

    vasily "Fine. But only for a little while. If King Gustav sees me slacking, he might have my head."

    "We make our way to the pavilion, and Vasily settles into one of the cushioned seats, stretching his legs out. I take a spot beside him, leaning back against a pillow."
    "For a brief moment, it feels... peaceful. The noise of the square fades into a dull hum, distant and unimportant. The sun filters through the canopy above, its warmth battling the cold, snowy air."

    show vasily neutral at right_char
    vasily "You know, I can't remember the last time I did this. Just... sat down without thinking about the next task, the next problem."

    "I close my eyes, letting the rare stillness seep into my bones."

    show dorian normal_alt_neutral at left_char
    dorian "You know the king. He never stops bitc—"

    show vasily alt_savage at right_char
    vasily "And you never stop brooding."

    "The silence stretches between us. I catch Vasily dozing off, his head tilting to one side. He mutters something incoherent before settling into a deeper sleep."

    show vasily alt_think at right_char
    vasily "Zzzzz…"

    scene black with fade
    pause 2.0
    scene bg_mjoll_pavilion with dissolve

    "An hour goes by and I wake Vasily up. He stretches and glances at me, the faintest hint of a smile on his face."

    show vasily alt_normal at right_char
    vasily "Alright, Dorian. I'll admit it—you were right. I needed that."

    show dorian normal_alt_confident at left_char
    dorian "Told ya."

    "He pauses."

    show vasily alt_normal at right_char
    vasily "You, too, though. You looked... at peace, for once."
    # vasily 049

    show dorian normal_alt_calm at left_char
    dorian "I agree. Rest is a moment I don't take for granted."

    return


# =============================================================================
# SECTION 11: LABEL CH2_COMMON_FREETIME — Free Time Convergence
# All four free time options converge here.
# =============================================================================

label ch2_common_freetime:

    # [COMMENT: bg_mjoll_square_festive — full crowd gathered, Qiongqi head on pedestal, banners]
    scene bg_mjoll_square_festive with dissolve # PLACEHOLDER — Mjoll square, full celebration

    # TODO: add music
    # play music ost_mjoll_festive volume 0.8     # PLACEHOLDER — festive theme at full volume
    # play audio amb_crowd_festive loop fadein 1.5 # PLACEHOLDER — crowd ambient loop

    show dorian neutral at left_char
    show vasily alt_normal at right_char
    with Dissolve(0.2)

    "It's time for the celebration."
    "As Vasily and I approached the grand setup in the square, the energy was palpable."
    "The monster's severed head was proudly displayed atop a gilded pedestal, its grotesque features preserved and amplified for all to see."
    "A crowd had already gathered, their murmurs of excitement growing louder with every passing moment."
    "The sound of children laughing, merchants yelling, and performers playing instruments filled the air."

    show vasily alt_think at right_char
    vasily "There it is. Your hard work on full display. The people will talk about this for years. They'll honor you in the grand Mjollian tradition. It's my favorite part of these ceremonies."

    dorian "*yawns* I wanted to go back to sleep."

    show vasily alt_normal at right_char
    vasily "You'll get more sleep AFTER the ceremony."

    show dorian normal_alt_annoyed at left_char
    dorian "Besides, didn't you help bringing down that thing? We also had three other soldiers with us. Helga, Lars… And, I forgot the name of the last one."

    show vasily alt_think at right_char
    vasily "Pavel. His name's Pavel, I believe."
    hide vasily
    hide dorian

    "The crowd roared in approval as a herald stepped forward to announce the event. My recognition was grand, as Vasily predicted. I could hear murmurs and shouts of my name from the crowd."

    show herald at center with Dissolve(0.2)             # PLACEHOLDER — Herald sprite

    herald "People of Mjoll! We gather today to honor the Dragon of Gale, the hero who has slain the Qiongqi that terrorized our kingdom!"
    "The applause was thunderous. But I had no desire for recognition, no joy in the spectacle."
    hide herald
    jump ch2_ceremony

# =============================================================================
# SECTION 12: LABEL CH2_CEREMONY — Dunking Ceremony (D1)
# =============================================================================
# COMMON
# D1: Aim dead center (Svante dunked) or Pretend to miss (+svante_affection)
# =============================================================================

label ch2_ceremony:

    show dorian neutral at left_char
    show vasily neutral at right_char
    with Dissolve(0.2)

    "Then my gaze shifted, and I saw it"
    "A large setup on the other side of the square. A series of dunk tanks, each elevated on a platform, filled with freezing water with stalagmites."
    "Above each tank, an aldorith was tied to a precarious seat, their faces pale from the cold."
    hide vasily
    hide dorian

    show boy_ald_normal at center_char
    show svante normal_neutral at right_char
    show kristin_normal at left_char
    with Dissolve(0.2)
    svante "…"
    boy_ald "…"
    kristin "…"

    hide svante
    hide kristin_normal
    hide boy_ald_normal

    show dorian neutral at left_char 
    show vasily alt_savage at right_char
    with Dissolve(0.2)

    vasily "Ah… my favorite tradition. The dunk tanks."

    show dorian normal_alt_annoyed at left_char
    dorian "Favorite?"

    "The man with the violet hair was a standout. His shirt was thin and tattered, barely enough to protect him from the biting wind."
    "The others— a younger girl with silver hair, a gaunt boy, and a frail woman—were dressed similarly, their clothes little more than rags."

    hide dorian
    hide vasily

    show herald at center_char with Dissolve(0.2)
    herald "To mark this grand occasion, we begin with the traditional dunking! And as is custom, the guest of honor shall have the first dunk!"
    herald "And as is custom, the guest of honor shall have the first dunk! Only the Dragon of Gale himself will claim this honor! After which, the dunk will be open to the public!"

    "The crowd erupted into cheers, and my fists clenched at my sides."
    hide herald

    man_1 "I can't wait to see that violet-haired freak drown!"
    woman_2 "Dunk them all! Teach those mutts their place!"

    show kristin_normal at left_char with Dissolve(0.2)
    kristin "*cries* They're… they're so cruel…"

    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "Hey, Kristin. Don't cry. You're making it easier for them."

    "The herald pointed dramatically at the violet-haired aldorith."
    hide svante
    hide kristin_normal
    
    show herald at center_char with Dissolve(0.2)
    herald "And for our first dunk, we have Svante—the metal channeling aldorith! Dragon of Gale, the first throw is yours!"
    hide herald

    show dorian normal_alt_annoyed at left_char 
    show svante normal_sad at right_char
    with Dissolve(0.2)
    "I glanced up at Svante. He met my gaze with his piercing violet eyes."
    show dorian serious at left_char 

    svante "Of course it's me…"
    "A younger aldorith, a girl with silver hair, whispered frantically to him."

    hide svante
    show kristin_normal at right_char with Dissolve(0.2)
    kristin "Svante, brother, please. Don't provoke them. We—"

    "The words barely left her mouth before a guard struck her with the blunt end of his spear."

    kristin "Ahhh!!"

    hide kristin_normal
    show svante normal_angry at right_char with Dissolve(0.2)
    svante "Hey! Don't lay a finger on her! I swear—"

    "Another slap from the guard silenced him, followed by a harsh blow to his stomach. Svante doubled over, coughing violently as the crowd cheered."

    show svante normal_nervous at right_char
    svante "*coughs*"
    hide svante

    show male_guard at right_char with Dissolve(0.2)
    male_guard "Shut up, lowlife."
    hide male_guard
    show man_3 at right_char with Dissolve(0.2)
    man_3 "Yeah! Show that worthless mutt his place!"
    hide man_3
    show male_guard at right_char with Dissolve(0.2)
    male_guard "Wanna beg for my forgiveness?"
    hide male_guard

    show kristin_normal at right_char with Dissolve(0.2)
    kristin "Svante, please!"
    
    hide kristin_normal
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "*coughs* I… I'm sorry."

    "The guard grabbed Svante by his collar, forcing him upright to face me."
    hide svante

    show male_guard at right_char with Dissolve(0.2)
    male_guard "I hope you like ice water, freak. After this, you and your siblings are done for. The Dragon of Gale will see to it."

    "The crowd roared again as Vasily stepped beside me, a smirk tugging at his lips. He is holding out a ball."
    hide male_guard
    show vasily alt_savage at right_char with Dissolve(0.2)
    vasily "Here. It's Mjollian tradition, my friend. It's just a dunk tank, after all. The water's only cold if you let yourself feel it. They're only aldoriths. Filthy mutts."
    hide vasily

    show herald at right_char with Dissolve(0.2)
    herald "Come now, Dragon of Gale. It's tradition. Show us your strength and honor by taking the first shot. The people are watching!"
    hide herald

    show svante normal_sad at right_char with Dissolve(0.2)
    "I looked back at Svante, his violet eyes meeting mine. His expression was unreadable. He looks down, defeated."
    svante "…"

    show dorian sad at left_char
    dorian "…"

    svante "Just do it. Get it over with."
    "The crowd jeered, their shouts urging me to take the shot. Vasily stood beside me."

    # -----------------------------------------------------------------------
    # D1 DECISION — Aim Dead Center or Pretend to Miss
    # PDF p79-81
    # -----------------------------------------------------------------------
    menu:
        "Aim dead center.":
            $ ch2_dunk_choice = "aimed"
            stop sound

            "I raised my arm and aimed straight for the target. The crowd hushed as they watched, anticipation thick in the air. With one swift motion, I threw the ball."
            "The target hit dead center, and the mechanism released."

            # TODO: add sfx
            # play sound sfx_dunk_splash          # PLACEHOLDER — dunk splash SFX

            show svante normal_angry at right_char
            svante "*panting*"

            "The crowd roared with laughter."

            show kristin_normal at left_char
            kristin "B-Brother!"

            man_3 "Look at him squirm!"
            woman_2 "Bet he wishes he wasn't born now!"

            "I stepped back, my face blank. Vasily clapped me on the back, his laughter blending in with the crowd."

            show vasily alt_savage at right_char
            vasily "Haha! Look at that wet mutt! Great job, friend!"

        "Pretend to miss the shot.":
            $ ch2_dunk_choice = "missed"
            $ svante_affection += 1             # +1 Svante affection tracker
            stop sound

            "I raised my arm, aimed, and threw the ball—but it went wide, striking the wood of the tank instead. The crowd groaned in disappointment, their laughter fading into murmurs."

            hide svante 
            show herald at right_char with Dissolve(0.2)
            herald "A miss? Well, no matter! The Dragon of Gale may try again!"

            show dorian normal_alt_annoyed at left_char
            dorian "I won't throw another."

            herald "But it's tradition! The dunking cannot proceed without the first shot!"

            show dorian serious at left_char
            dorian "Then there will be no dunking."

            "The crowd booed, their shouts becoming increasingly hostile. Vasily looked at me, his face an odd mix of amusement and disbelief."

            hide herald
            show vasily alt_think at right_char with Dissolve(0.2)
            vasily "You really know how to ruin a celebration, Dorian. This is Mjollian culture."

            "I ignored him and turned away, my eyes meeting Svante's for a brief moment."

            hide vasily
            show svante alt_base at right_char with Dissolve(0.2)
            svante "I… t-thank you… I—"
            hide svante

            show male_guard at right_char with Dissolve(0.2)
            male_guard "Shut up, all of you, mutts!"

            hide male_guard
            show kristin_normal at right_char with Dissolve(0.2)
            kristin "Brother!"

            hide kristin_normal
            show svante normal_happy at right_char with Dissolve(0.2)
            svante "Kristin!"
            hide svante

            show boy_ald_normal at right_flip with Dissolve(0.2)
            boy_ald "Wait, so does that mean…"
            hide boy_ald_normal

            show svante normal_base at right_char with Dissolve(0.2)
            svante "Thank you…"

            "Svante, though shivering, straightened his posture slightly, his violet eyes locked onto me until he is escorted out by the guards."
            hide svante

            show herald at right_char with Dissolve(0.2)
            herald "Well… There you have it, folks. No first shot has been made. For the first time ever, we will be cancelling today's dunking festivities."
            hide herald
    # Both branches converge — then the Frost Oni attack begins
    jump ch2_frost_oni


# =============================================================================
# SECTION 13: LABEL CH2_FROST_ONI — Frost Oni Attack (D4, D5, D6 QTCs)
# =============================================================================
# PDF pages 81-86.
# ICE tracker accumulates on wrong answers.
# If ice_tracker >= 2 during D6's wrong branch -> GAME OVER.
# =============================================================================
label ch2_frost_oni:

    stop audio fadeout 1.0   # Stop crowd ambient

    "As other festive activities continued, I felt a sudden wave of unease."
    "The ground beneath us trembled violently, cutting through the crowd's laughter like a blade. The quake was sudden, jolting everyone out of their revelry."

    man_3 "Ahhh!!"

    "The herald stumbled forward, gripping the edge of the dunk tank for support, his face pale with terror."

    show herald at right_char with Dissolve(0.2)
    herald "What… what is happening?!"
    hide herald

    "Before anyone could answer, a bone-chilling wind swept through the square. The air seemed to freeze in place, heavy and sharp like needles against the skin."
    "Then, out of the frost-laden mist, they appeared."
    
    # TODO: add sfx
    # play sound sfx_ice_crack                    # PLACEHOLDER — ice crack SFX

    # CG: Frost Oni emerging from the mist
    scene bg_mjoll_blizzard with shock_cut

    # play music ost_frost_oni_battle fadein 0.5  # PLACEHOLDER — Frost Oni battle theme
    "Towering figures, their forms jagged and crystalline, emerged from the haze. Beings of ice, emanating an eerie glow. Long, flowing tendrils of frost extended from their limbs, crackling as they moved. They carried weapons of ice—curved swords and long spears."

    frost_oni "*Crackling sounds*"

    man_2 "W-What are those things?!"
    woman_1 "D-Demons! Demons!"

    "Without warning, one of them raised its spear and hurled it into the crowd. It struck a man through the chest, freezing him solid where he stood."
    "Another slashed its blade across a fleeing woman, leaving behind a trail of ice that consumed her body in seconds."

    woman_1 "Ahhh!!"
    man_3 "Run!! Run!!"

    # PDF p82
    "The herald tried to regain control, his voice breaking as he shouted."

    show herald at center_char with Dissolve(0.2)
    herald "Remain calm! Guards, come quick! P-Protect—"

    "An ice being surged forward, impaling him with its spear."

    herald "Ahhh!! *dying sounds*"
    hide herald with Dissolve(0.5)

    "His words died in his throat, his body encased in frost before shattering into pieces."

    show frost_oni at right_char with Dissolve(0.2)
    frost_oni "Graaaaa!!"

    "The dunk tank was their next target. One of the creatures slammed its massive fist against the frame, shattering it instantly. The water inside spilled out, freezing as it hit the ground."
    "The aldoriths screamed, scattering as the ice beings turned their attention to them."
    hide frost_oni

    show kristin_normal at left_char with Dissolve(0.2)
    kristin "Brother! Svante! Run!"

    show svante normal_angry at right_char with Dissolve(0.2)
    svante "Let's get out of here, Kristin!"

    "I could see him hesitate, his fists clenching, but he eventually turned and fled with the others."

    hide kristin_normal
    hide svante

    show dorian serious at left_char
    show vasily alt_normal at right_char
    with Dissolve(0.2)

    vasily "What in Tetrad's name are these?"

    show dorian dragon_eyes at left_char
    dorian "I don't know."

    "I raised my hands, channeling earth and wind. The ground around me shifted, sharp pillars of stone erupting to block the ice beings' path."
    "I followed up with a gust of wind, sending shards of debris flying toward them."

    # play sound sfx_earth_spike                  # PLACEHOLDER — earth spike SFX

    show vasily alt_aggressive at right_char
    vasily "Dorian, we need to keep them away from the civilians!"

    "The ice beings seemed unfazed by the wind and stone at first, their bodies regenerating as frost crept over the damage."
    "I clenched my fists, slamming a foot into the ground to create another barrier of earth between them and the survivors."
    "One of the creatures turned its glowing eyes on me, its spear raised to strike."
    scene cg_blindinglight with shock_cut
    scene bg_mjoll_blizzard with Dissolve(1)
    "Vasily stepped forward, blasting it with a beam of light magic. The creature stumbled back, cracks forming in its icy surface."

    show vasily alt_savage at right_char with Dissolve(0.2)
    vasily "They're not invincible! Dorian, we need to hit them harder!"

    $ renpy.save("quick-1")
    show dorian serious at left_char with Dissolve(0.2)
    "I nodded, summoning a whirlwind of debris and stone to batter another creature. The crowd was in chaos, but some of the people were starting to flee toward safety."
    "The ice beings let out a bone-chilling screech, their forms twisting as they began to converge on us. My heart pounded, but I stood my ground."
    hide vasily

    show dorian serious at left_char 
    show frost_oni at right_char
    with Dissolve(0.2)
    frost_oni "Graaaaa!!"

    "One of the creatures ran towards me, its icy breath misting the air as it raised its massive spear toward me. It would be difficult for me to physically dodge the spear."
    # play sound sfx_heartbeat loop

    # =====================================================================
    # D4 — TIMED QTC: Frost Spear (wind = safe / dodge = +ICE)
    # PDF p83
    # =====================================================================
    $ _choice_timeout = 5.0
    menu:
        "Use wind to deflect the spear.":          # CORRECT — no ICE
            $ _choice_timeout = 0
            $ ch2_qtc4 = "wind"
            stop sound

            play sound sfx_wind_blast           # PLACEHOLDER
            show dorian dragon_eyes at left_char
            "I summoned a powerful gust of wind just in time, the spear flying off course and shattering against the ground. The ice being let out an enraged screech, its glowing eyes locked on me."

            frost_oni "Graaaaa!!"

        "Dodge to the side.":                      # WRONG — +1 ICE
            $ _choice_timeout = 0
            $ ch2_qtc4 = "dodge"
            $ ice_tracker += 1
            stop sound
            show dorian angry at left_char
            "I tried to move, but the spear grazed my side, leaving a sharp, stinging pain as frost crept along the wound."

            if ice_tracker == 1:
                show dorian angry at left_char_ice_1 with Dissolve(0.7)
                show frost_masked_angry at frost_overlay_1
            elif ice_tracker == 2:
                show dorian angry at left_char_ice_2
                show frost_masked_angry at frost_overlay_2
            elif ice_tracker >= 3:
                show dorian angry at left_char_ice_3
                show frost_masked_angry at frost_overlay_3
        
            # TODO: add freezing ice sfx
            dorian "Ahhh!!"
            hide frost_oni
            show vasily alt_aggressive at right_char with Dissolve(0.2)
            vasily "Dorian!"
            hide vasily
            show frost_oni at right_char
            frost_oni "Graaaaa!!"

    # TODO: fix sfx
    # play sound sfx_heartbeat loop
    show dorian angry at left_char
    "Another creature surged forward, its clawed hand reaching for Vasily. He fired a beam of light magic, but it was too fast, dodging the attack. Its focus turned to me."

    frost_oni "Graaaaa!"
    hide frost_oni
    show vasily alt_mad at right_char with Dissolve(0.2)
    vasily    "Dorian! It's after you!"

    # =====================================================================
    # D5 — TIMED QTC: Ice Claws (wind = +ICE / earthen wall = safe)
    # =====================================================================
    $ _choice_timeout = 5.0
    menu:
        "Try to blast it with wind to push it back.":  # WRONG — +1 ICE
            $ _choice_timeout = 0
            $ ch2_qtc5 = "wind"
            $ ice_tracker += 1
            stop sound

            "I sent a gust of wind toward it, but it barely slowed the creature down. Its icy claws raked across my arm, freezing my flesh."
            "I bit back a scream, but the pain was almost too much."

            

            dorian "Ahhh!! Crap!!"
            vasily "Dorian!!"

            "Vasily launched a blast of light towards the being, shattering it completely."

        "Raise an earthen wall to block its path.":    # CORRECT — no ICE
            $ _choice_timeout = 0
            $ ch2_qtc5 = "wall"
            stop sound

            play sound sfx_earth_spike          # PLACEHOLDER

            "I slammed my hands to the ground, channeling the earth to rise in a jagged wall between us. The creature collided with it, shards of ice breaking off its body."

            vasily "Take this!"
            scene cg_blindinglight with shock_cut
            "Vasily fired another blast, shattering part of its torso."
            scene bg_mjoll_blizzard with Dissolve(1)
    # play sound sfx_heartbeat loop

    "The last ice being stood in the middle of the square, frost swirling around it as it prepared a devastating attack."
    "A frost cloud. I could feel the temperature drop further, the cold biting into my very core."

    if ice_tracker == 1:
        show dorian serious at left_char_ice_1
        show frost_masked_angry at frost_overlay_1
    elif ice_tracker == 2:
        show dorian serious at left_char_ice_2 with Dissolve(0.7)
        show frost_masked_angry at frost_overlay_2
    elif ice_tracker >= 3:
        show dorian serious at left_char_ice_3 with Dissolve(0.7)
        show frost_masked_angry at frost_overlay_3
    else: 
        show dorian serious at left_char

    show vasily neutral at right_char
    with Dissolve(0.2)
    vasily "Brr… It's getting colder…"
    hide vasily

    show babala at right_char with Dissolve(0.2)       
    babala "Hey! Do you boys need some help? I can help you!"

    # =====================================================================
    # D6 — TIMED QTC: Frost Cloud (wind + Babala = safe / earth spike = +ICE)
    # If ice_tracker >= 2 after wrong answer -> GAME OVER
    # =====================================================================
    $ _choice_timeout = 5.0
    menu:
        "Use wind to disperse the frost before it gathers. Allow Babala to help.":  # CORRECT — no ICE 
            $ _choice_timeout = 0
            $ ch2_qtc6 = "wind_babala"
            stop sound

            # play sound sfx_wind_blast           # PLACEHOLDER
            hide babala
            show dorian dragon_eyes at left_char
            show frost_oni at right_char 
            with Dissolve(0.2)
            "I called on the wind, forcing it into a violent cyclone that tore through the frost cloud. The creature let out a shriek of frustration as its attack dissipated, leaving it vulnerable."

            dorian "Now!"
            hide frost_oni
            show babala at right_char with Dissolve(0.2)    
            babala "*gibberish* Taste the wrath of the Weaver!"   

            # play sound sfx_vine_attack          # PLACEHOLDER — vine attack SFX
            hide babala
            show frost_oni at right_char with Dissolve(0.2)
            "All of a sudden, vines surrounded the ice being and smashed it on its vulnerable spot."
            hide frost_oni

            show vasily neutral at right_char
            show dorian serious at left_char
            with Dissolve(0.2)
            vasily "Wow."
            hide vasily
            show babala at right_char with Dissolve(0.2)    
            babala "You're welcome, Dragon."

        "Channel earth to create a spike and impale it. Don't allow her.":   # WRONG — +1 ICE
            $ _choice_timeout = 0
            $ ch2_qtc6 = "spike"
            $ ice_tracker += 1
            stop sound

            show dorian dragon_eyes at left_char
            "I tried to channel the earth beneath it, but my footing slipped on the icy ground."
            "The frost cloud thickened, and the creature unleashed its attack, shards of ice ripping through the square."
            if ice_tracker == 1:
                show dorian angry at left_char_ice_1
                show frost_masked_angry at frost_overlay_1
            elif ice_tracker == 2:
                show dorian angry at left_char_ice_2
                show frost_masked_angry at frost_overlay_2
            elif ice_tracker >= 3:
                show dorian angry at left_char_ice_3 with Dissolve(0.7)
                show frost_masked_angry at frost_overlay_3
            dorian "Gaaah!"
            babala "Dragon!"
            hide babala

    # -----------------------------------------------------------------------
    # POST-QTC CONVERGENCE — ICE CHECK
    # PDF p85
    # -----------------------------------------------------------------------

    if ice_tracker >= 2:

        # GAME OVER — Dorian is frozen solid
        stop music fadeout 1.0
        stop sound
        hide babala
        show dorian sad at left_char
        show vasily neutral at right_char
        with Dissolve(0.2)
        vasily "D-Dorian! Your skin!"

        dorian "C-Cold…"

        "I fell to my knees, frost spreading across my body as the ice takes hold of me. The cold consumed me, dragging me into darkness."
        hide vasily
        show babala at right_char with Dissolve(0.2)    
        babala "Dragon! No!"
        hide babala
        show vasily alt_mad at right_char with Dissolve(0.2)
        vasily "Dorian! No! Dorian!"

        jump game_over_freeze

    else:

        stop music fadeout 2.0
        stop sound
        hide frost_masked_angry with Dissolve(0.6)
        "The ice beings were shattered, their remains scattered across the square. Vasily panted beside me, his magic dimming as exhaustion took hold."
        hide babala

        show vasily alt_normal at right_char
        vasily "You did it, Dorian. You saved them… or what's left of them."

        show dorian normal_alt_calm at left_char
        dorian "What are those things?"
        show dorian serious at left_char

        "The guards approached us, their faces pale and frantic. One of them leaned in and whispered something hurriedly to Vasily."
        "His usual calm demeanor cracked as his eyes widened in shock."

        show vasily alt_aggressive at right_char
        vasily "W-What?! Are you certain? Tetrad above…"

        "The guard nodded, and Vasily swore under his breath. He grabbed a pouch from his belt and thrust it into my hands, his movements rushed."

        show vasily alt_normal at right_char
        vasily "Here. Your payment. I… I need to go. I'll find you later. Stay safe, Dorian."

        "He didn't wait for a reply. Before I could ask what was wrong, he spun on his heel and bolted toward the castle, the guards following closely behind."
        "I stood there, clutching the pouch."
        hide vasily

        "The remaining guards approached cautiously, inspecting the shattered remnants of the ice beings scattered across the bloodied square."

        show babala at right_char with Dissolve(0.2)
        babala "This… This is no ordinary attack. The Weaver's threads are tightening around us."

        "She bent low to inspect one of the larger shards of ice, her fingers brushing the jagged surface. A faint glow pulsed under her touch."

        babala "Yes… the pieces of the Weaver's plan are in motion. You, Dragon of Gale, must steel yourself. For the storms that come will not spare anyone—not kings, not queens, not even you."

        show dorian normal_alt_annoyed at left_char
        dorian "The Weaver? What does this have to do with the gods?"

        babala "You will find out in due time. For now, my work for you is already done."

        "She straightened—well, as much as her hunched back would allow—and let out a dry, croaking laugh. Then, as she turned to shuffle away, her back cracked audibly."

        babala "Ahhh!"

        show dorian normal_alt_neutral at left_char
        dorian "A-Are you alright?"

        "She waved me off, scowling."

        show babala at right_char
        babala "Tch! Damned Weaver and your threads! Snagged me good, you meddling hag!"

        "She spat on the ground, muttering curses under her breath."
        "She shuffled back toward her tent, her curses growing louder with each step. The guards gave her a wide berth, whispering among themselves."
        "I watched her go, a strange unease settling in my chest."
        hide babala
        "I looked back at the shattered remains of the ice beings, their glow still faintly pulsing in the twilight."

        show dorian normal_alt_tense at left_char
        dorian "What are these monsters?"

        jump ch2_common_end


# =============================================================================
# SECTION 14: LABEL game_over_freeze — Shared GAME OVER (ICE Freeze)
# =============================================================================
# Only reached from the Frost Oni ICE tracker check.
# PDF page 85.
# =============================================================================
label game_over_freeze:

    scene black with fade            # PLACEHOLDER — cg_dorian_frozen (frost spreading)
    stop music fadeout 1.0
    stop audio

    pause 1.5

    "The cold consumed everything."
    "And then — nothing."

    pause 2.0

    scene cg_black with fade                    # PLACEHOLDER — pure black

    jump game_over

# =============================================================================
# SECTION 15: LABEL CH2_COMMON_END — Post-Battle / Yuxuan Letter (D3)
# =============================================================================
label ch2_common_end:

    # -------------------------------------------------------------------------
    # TIME SKIP — Several days pass
    # PDF p86-87
    # -------------------------------------------------------------------------

    scene cg_black with fade                    # PLACEHOLDER — black transition

    pause 1.0

    # PDF p86
    # [COMMENT: bg_mjoll_blizzard — abandoned square, snow-covered, eerie silence]
    scene bg_mjoll_blizzard with fade    # PLACEHOLDER — abandoned snowy square

    # play music ost_blizzard_days fadein 3.0     # PLACEHOLDER — desolate days-after theme
    # play audio amb_mjoll_wind loop fadein 2.0   # PLACEHOLDER — wind ambient

    "The days passed in a haze. Five, maybe six—I've lost count."
    "The silence from the castle stretched on, unnerving in its emptiness."
    "No Vasily, no summons, no word. Not even a whisper of gold. Only rumors and idle gossip."
    "They said the ice creatures had come from inside the castle. From someone within. I didn't care."
    "Let them chase their shadows and whisper their theories. It wasn't my concern. My only concern was survival—and, when I could afford it, distraction."

    # [COMMENT: bg_mjoll_blizzard — snow falling heavier than before, vendors complaining]
    # add effects here
    "The biting chill nipped at my skin as I trudged back to my cave. Strangely, the snow was falling heavier than before these past few days."
    "The cold didn't bother me much—it never had. Maybe it was the fire channeling power coursing through me. But for some people, according to the vendors, it's become unbearable."
    "The pouch of gold Vasily had thrust into my hands days ago had been spent sparingly, stretched to buy food and small comforts."

    scene dorians_cave_off with dissolve(0.8)     # PLACEHOLDER — cave at night, fire low

    stop audio fadeout 1.0
    play audio amb_cave_fire loop fadein 2.0    # PLACEHOLDER — fire crackle ambient

    show dorian sad at left_char with Dissolve(0.2)

    # [COMMENT: the fire crackled softly] 
    # TODO: add sfx
    dorian "Elara… Kids… I'm home."

    elara  "…"
    sarah  "…"
    lucas  "…"
    daniel "…"
    emily  "…"

    dorian "Happy birthday, Sarah. I have a surprise for you."

    "I set the bag of food down near the fire, letting the warmth seep into my bones."
    "I pulled out a small, cheap toy from my coat—a makeshift knit doll with one eye missing, the stitches frayed and uneven."
    "It wasn't much. I'd bought it from a street vendor for one gold, a pittance."

    dorian "Tedda. That's her name. She's not much to look at, but I thought… I thought she'd make you smile."

    sarah "…"
    elara "I'm sure she would have loved it, Dorian…"

    "My hands trembled as I placed it on a small wooden shelf near the fire, beside a collection of toys."
    "Emily's ribbon that I bought for her, Lucas's slingshot, Daniel's carved wooden horse. Elara's scarf that I bought for her for our anniversary."

    dorian "Happy birthday, sweetheart. I miss you."

    sarah  "…"
    lucas  "…"
    daniel "…"
    emily  "…"

    "I stayed there, staring into the fire, as the night stretched on."

    elara "My heart, did you check the mail?"

    "I blinked, looking up."

    elara "You always forget the mail. Can you check?"
    dorian "The mail, my heart?"

    "She nodded, her smile unwavering."
    "I walked to the ledge. There, tucked beneath a loose rock, was an envelope I hadn't noticed before."

    "It was an elegant thing, crisp and ivory-colored, sealed with an intricate red-and-gold emblem."
    "There was a mark with a picture of a girl and the words: Cheng Industries."
    "The Tianho seal gleamed faintly in the dim light, the dragon motif coiled with clouds and lotus blossoms."

    "I turned the envelope over, running my fingers across the embossed edges before opening it carefully."
    "Inside was a letter, written in neat, flowing characters."

    hide dorian
    
    # TODO: play paper sfx
    call screen cheng_letter with fade

    show dorian serious at left_char with Dissolve(0.2)

    dorian "Yuxuan… Cheng Yuxuan… I don't recall anyone with that name."

    "The name didn't immediately strike a chord, but I felt like I heard it from somewhere before."

    elara  "You saved him from the fire, remember?"
    daniel "Yeah! Remember when you lifted that beam like it was nothing? It was so cool!"
    show dorian normal_alt_calm at left_char

    "I closed my eyes, the image of Tianho's flames flashing behind my eyelids. The man I saved from the burning building."
    "I sighed, folding the letter carefully and setting it aside."

    elara  "You should write back to him."

    show dorian sad at left_char
    dorian "I don't have time for this, my heart. You know that."

    emily  "Don't lie, Dad. We know you're not doing anything important. You're just sitting here, talking to us."

    dorian "But—"

    elara  "Oh, don't be stubborn. Writing back won't kill you. Besides, it might be good to talk to someone new for a change. You can't spend all your time with Vasily—or just us."

    sarah  "Yeah, dad! Think of it as my birthday gift!"
    daniel "My late birthday gift too, dad!"
    emily  "Mine too!"
    lucas  "Don't forget mine, dad!"

    "I sighed again."

    dorian "Fine…"

    "I reached for the old pen Vasily had given me weeks ago and pulled out a sheet of parchment."
    "Sitting down at the rickety wooden table, the glow of the fire flickering on the cave walls, I dipped the pen in ink. What should I write, though?"

    # =========================================================================
    # D3 — WRITE BACK TO YUXUAN: Warm or Distant response
    # =========================================================================

    menu:
        "Write a warm response.":
            $ ch2_letter_choice = "warm"
            $ yuxuan_affection += 1             # +1 Yuxuan affection tracker
            show dorian normal_alt_calm at left_char
            "I sat for a moment, letting my memories of that night in Tianho run my hand. The ink bottle was nearly empty, but I managed to write carefully:"

            show dorian neutral at left_char
            "Cheng Yuxuan,"
            "It's great to know that the life I saved has grown into such a kind and successful soul. "
            "I would be honored to have tea with you and see how you've rebuilt your life. Perhaps we can trade stories—I have a few to tell myself. "
            "Thank you for your thoughtful letter. It means more to me than you know."
            "Dorian Burnham"

            "Lastly, I placed the address written on Yuxuan's letter. When I finished, I let the ink dry."

            dorian "There. Happy?"
            elara  "Once you send it to the postman, I'll be very happy."

        "Write a distant response.":
            $ ch2_letter_choice = "distant"

            "The fire crackled as I sat at the table, the pen feeling heavy in my hand. I stared at the parchment for a long moment before scrawling a short reply in quick, precise strokes."
            show dorian serious at left_char
            "Cheng Yuxuan,"
            "I am glad to hear you are doing well. I don't have time for travel at the moment. Best of luck to you in Tianho."

            dorian "There. Happy?"
            sarah  "Dad, that's such a cold letter."
            lucas  "Even colder than this weather!"
            elara  "How are you supposed to make new friends if you write like that?"

            "I groaned, grabbing the letter again. With a grumble, I scratched out 'don't' in the second sentence, leaving a messy strikethrough."

            dorian "There. I fixed it. Happy?"
            elara  "You're impossible, you know that?"

    show dorian serious at left_char
    "I folded the letter and tucked it into my pocket. I'd deliver it when I made my next trip into the city."
    "As I turned back to the warmth of the fire, I heard it—a voice calling for me from outside the cave. It was sharp, urgent."

    show messenger at right_char with Dissolve(0.2)             # PLACEHOLDER — Messenger sprite (out of breath)

    messenger "Paladin Dorian! Are you there? Paladin?"

    "I stood, brushing my hands against my tunic before stepping outside. A young messenger, dressed in the livery of Mjoll, stood at the edge of the rocky path leading to my home."
    "His face was pale, his breathing uneven from the climb."

    messenger "You've been summoned to the castle immediately. The situation is… urgent."

    "I narrowed my eyes, my heart sinking at the grim tone of his voice."

    dorian    "What happened?"
    messenger "I'm not permitted to say. But the royal advisor insists you come at once."

    "Vasily."
    "I stepped forward."

    dorian "Let's go."

    "The messenger nodded, and we began the trek back to Mjoll."

    jump ch2_castle_briefing


# =============================================================================
# SECTION 16: LABEL CH2_CASTLE_BRIEFING — Assassination Mission Briefing
# =============================================================================
label ch2_castle_briefing:
    scene mjoll_palace_throne with fade        # PLACEHOLDER — palace hall, aldoriths gearing up
    # play music ost_briefing fadein 2.0          # PLACEHOLDER — tense briefing theme

    show dorian serious at left_char with Dissolve(0.2)

    "The howl of the snowstorm seemed alive, its icy fingers clawing at us even as we slammed the heavy doors shut behind us."

    show messenger at right_char with Dissolve(0.2)
    messenger "C-C-Cold… Cold…"

    show dorian normal_alt_neutral at left_char
    dorian "Are you alright? Are you still cold?"

    messenger "A l-little.."
    hide messenger

    show dorian serious at left_char
    "Inside, the warmth of the Mjoll Castle did little to shake the lingering chill. My boots echoed on the stone floor as I took in the sight before me."
    "A group of aldoriths stood huddled in the grand hall, their faces pale and determined."
    "They were gearing up for battle, strapping on mismatched armor and whispering to one another in low, urgent tones."
    "Some glanced at me briefly, but their eyes quickly darted away. They had no love for me, nor I for them."

    show girl_ald_normal at right_char with Dissolve(0.2)
    girl_ald "Have you heard of the death toll? Enoch above…"
    hide girl_ald_normal

    show boy_ald_normal at right_flip with Dissolve(0.2)
    boy_ald "I know… But we don't have a choice."
    hide boy_ald_normal

    show messenger at right_char with Dissolve(0.2)
    messenger "Paladin… Count Vasily is over there. If you'll excuse me, I'll—"

    show dorian serious at left_char
    dorian "Wait—"

    "I pulled the folded letter from my pocket and handed him a few coins."

    dorian "Please take this to Cheng Yuxuan."

    "The young man nodded, his face still flushed from the cold. Without another word, he bolted back out into the storm."

    hide messenger
    hide dorian

    "My eyes moved across the room until they landed on Vasily."
    show vasily alt_think at right_char with Dissolve(0.2)
    "He stood to the side, leaning heavily on a table, surrounded by three hooded figures draped in deep gray robes—the unmistakable attire of the prophets of the death god."
    "Vasily looked terrible. His face was gaunt, and a dark bruise marred his left eye, swelling the skin around it."
    "The prophets were whispering among themselves, their voices carrying just enough for me to listen to them."

    prophet_1 "The cold is unbearable… the prince must have made a pact with the death god to gain this much power."
    prophet_2 "I disagree. It's unnatural. Not even the Enoch's touch could twist the elements this way."

    show niko alt_annoyed at left_char with Dissolve(0.2)
    niko "You lack faith, brothers. It is obvious that Enoch's hand is all over this—"

    show vasily alt_mad at right_char
    vasily "Enough. Give me a moment."
    show vasily neutral at right_char

    "Vasily straightened when he noticed me approaching, though the movement seemed to pain him. He waved the prophets away with a curt gesture."

    hide niko
    show dorian normal_alt_annoyed at left_char with Dissolve(0.2)
    dorian "What in Tetrad's name happened to you?"
    vasily "You've seen what's happening outside. It's getting colder by the minute."
    dorian "I meant your face, Vasily."
    show dorian serious at left_char

    "He rubbed a hand over his face, wincing as his fingers brushed the bruise."

    show vasily alt_normal at right_char
    vasily "It's from the king. It's unimportant."

    "The fire in the hearth sputtered as the storm outside roared with a deafening fury. He leaned on the table, his knuckles white from the strain."

    show vasily neutral at right_char
    vasily "The storm won't let up, Dorian. It's relentless. Crops have failed, the rivers are freezing over, and entire villages are being swallowed by snow."

    "His voice cracked slightly."

    vasily "The kingdom is falling apart. Trade routes are blocked. Supplies can't get through. We've already lost half of our militia to hypothermia trying to secure the roads."

    show dorian serious at left_char
    "I clenched my fists, the weight of his words settling like a stone in my chest."

    dorian "And no one knows what's causing it?"

    show vasily alt_think at right_char
    vasily "There's a theory."
    hide vasily

    "He turned toward the hooded prophets of the death god. One's face was familiar… yet I could not recall."

    show niko normal_base at right_char with Dissolve(0.2)
    niko "The death god's power lingers, though it is not as strong as it once was. Its source is concentrated in a desolate place west of here. An abandoned mine known as Frostcradle."

    show dorian normal_alt_tense at left_char
    dorian "The Tragedy of Tianho? You're saying this storm is connected to that?"
    show dorian serious at left_char

    show niko normal_serious at right_char
    niko "The energies are unmistakable. Whatever caused the tragedy there has resurfaced. Weaker, yes, but still potent enough to wreak havoc."
    hide niko

    show vasily alt_mad at right_char with Dissolve(0.2)
    vasily "We sent aldoriths to investigate. None of them came back alive."
    "He gestured toward the crowd of aldoriths huddled in the hall. One figure stood apart, his violet hair unmistakable. I think I've seen him before."
    hide vasily

    show svante normal_sad at right_char with Dissolve(0.2)
    svante "I... I saw what happened to them. My brothers, my sisters... they went west, into that cursed place. When they didn't return, I volunteered to go after them."

    "He paused, his voice trembling as he continued."

    svante "They were impaled with ice. That's not all… their bodies were frozen solid. Twisted. The cold... it didn't just kill them. It consumed them."

    "He swallowed hard, his violet eyes glistening."

    svante "T-They… They were my family…"

    "The room was heavy with silence. Even the prophets seemed subdued. Vasily's voice cut through the tension."
    hide svante

    show vasily alt_normal at right_char
    vasily "That's why we're asking you, Dorian. You're not just a warrior—you're the Dragon of Gale. If anyone can survive this... it's you."

    show dorian serious at left_char
    "I stared at him, my jaw tightening."

    dorian "What's the mission?"

    "Vasily's gaze darkened, and for a moment, he hesitated."

    show vasily alt_savage at right_char
    vasily "You're to go west, to the Frostcradle. To the source of the storm. And once you're there…"

    show vasily alt_mad at right_char
    vasily "You are to kill the Prince Elias Drakos."

    show dorian normal_alt_confident at left_char
    dorian "Fine. But I want to be paid upfront."

    "Vasily didn't hesitate. He smiled and snapped his fingers with crisp authority. Svante reached to his belt, unclipping a leather pouch heavy with coin. It clinked as he approached, the weight unmistakable."
    show dorian neutral at left_char
    show vasily alt_savage at right_char
    vasily "We don't usually pay upfront, but given the urgency—and our past dealings—I'll make an exception."
    hide vasily
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "T-T-Three thousand gold pieces. For killing Prince Elias Drakos, sir."

    show dorian normal_alt_neutral at left_char
    "I took the pouch, feeling the satisfying heft of it before slipping it into my pocket. The room remained quiet, save for the occasional hiss of the fire."

    dorian "I have questions."
    
    hide svante
    show vasily alt_think at right_char with Dissolve(0.2)
    vasily "Ask. But make it quick. Time isn't on our side."

    jump ch2_questions


# =============================================================================
# SECTION 17: LABEL CH2_QUESTIONS — Optional Questions to Vasily
# =============================================================================
# PDF pages 94-99.
# Player can ask 3 optional questions before accepting the mission.
# All paths converge on ch2_end.
# =============================================================================
default ch2_asked_king_queen = False
default ch2_asked_elias = False
default ch2_asked_supplies = False
label ch2_questions:
    menu:
        "Where's the king and queen?" if not ch2_asked_king_queen:
            $ ch2_asked_king_queen = True
            
            show dorian normal_alt_neutral at left_char
            show vasily alt_think at right_char
            
            "I glanced around the hall, my eyes drawn to the twin thrones at the head of the room. Both were empty, their gilded frames casting long shadows in the dim light."

            show dorian normal_alt_annoyed at left_char
            dorian "Where's King Gustav?"

            show vasily alt_mad at right_char
            "Vasily's face darkened at the question, his lips pressing into a thin line."

            show vasily alt_sad at right_char
            vasily "The king is… indisposed. He's in his chambers, mourning."

            "His voice was tight, as though every word cost him. I noticed the way his hand trembled slightly as he spoke."

            show dorian serious at left_char
            dorian "And the queen? What of Queen Ekaterina?"

            show vasily alt_shocked at right_char
            vasily "?!"

            "At that, Vasily froze. His shoulders stiffened, and a flicker of pain crossed his eyes. For a moment, he didn't answer, but Svante, standing nearby, stepped forward, his face grim."

            show svante normal_sad at center with Dissolve(0.2)
            svante "She's dead, sir."

            "The words hung heavy in the air, like a stone dropped into a silent pond."

            show dorian normal_alt_annoyed at left_char
            dorian "What?!"

            show svante normal_nervous at center
            svante "We found her in her chambers... with a knife in her heart. Father saw everything."

            "I stared at him, my mind struggling to process the words. Queen Ekaterina, dead? It didn't feel real. The room felt colder. I clenched my fists."

            show niko normal_serious at right_char with Dissolve(0.2)
            niko "Elias killed her. Stabbed her in the heart like the heartless bastard he is."

            "I blinked, trying to process what I'd just heard. King Gustav and Queen Ekaterina. They'd always been there—fixtures of my early missions, handing me my rewards with smiles I'd never trusted but had grown used to."
            "I didn't care about them, not really, but the idea of her being gone was unsettling in a way I couldn't quite shake."

            show dorian normal_alt_tense at left_char
            dorian "I don't… I don't understand. The queen is dead? When did this happen?"

            show vasily alt_think at right_char
            vasily "During the ceremony. When those… beings appeared."

            "Beings of ice. The ones that disrupted the ceremony. I remember."

            show vasily alt_normal at right_char
            vasily "We couldn't even do the funeral because of the trade routes."

            show dorian normal_alt_neutral at left_char
            dorian "Trade routes?"

            show vasily alt_think at right_char
            vasily "Her final wish was to be buried in Hinami. A water burial. But the frozen routes make it impossible to transport her body there."

            show dorian normal_alt_neutral at left_char
            dorian "A Hinami burial? I didn't know Queen Ekaterina had Hinami blood."

            show vasily alt_normal at right_char
            vasily "She did. Only a trace, but enough that she wanted to honor their traditions in death."

            "Queen Ekaterina has Hinami blood… Who knew?"

            show dorian normal_alt_confident at left_char
            dorian "Well. I suppose even queens aren't untouchable."

            "Vasily shot me a sharp look, but he didn't argue. Instead, he turned away, his shoulders slumping."

            show niko normal_base at right_char
            niko "Do you have any other questions?"

            jump ch2_questions

        "Who's this Elias?" if not ch2_asked_elias:
            $ ch2_asked_elias = True

            show dorian normal_alt_neutral at left_char
            show vasily alt_think at right_char

            "Elias. The name wasn't familiar."

            show dorian normal_alt_annoyed at left_char
            dorian "Who's this Elias? This is the first I've heard of him."

            show vasily alt_sad at right_char
            "Vasily's shoulders tensed, and he let out a heavy sigh."

            show vasily alt_normal at right_char
            vasily "The crown prince of Mjoll. Or rather, the former crown prince of Mjoll."

            "I frowned, confused. In all my four years of working as a mercenary here, I'd never heard of any crown prince."

            show dorian normal_alt_tense at left_char
            dorian "A crown prince? Since when? All I know are the aldoriths who have claim to the throne."

            "Svante, standing nearby, looked down."

            show svante normal_sad at center with Dissolve(0.2)
            svante "He was the son of Her Majesty, Queen Ekaterina. The true heir to the throne... but not in the eyes of the king. According to Father—"

            "He paused, the words catching in his throat, and his hands clenched into fists at his sides."

            show svante normal_angry at center
            svante "Elias... Elias is a monster. He's the reason my brothers and sisters… *holding back tears*"

            show vasily alt_mad at right_char
            vasily "After the Queen was killed... Elias disappeared. We searched, but there was no trace of him. His flight from the kingdom is as clear an indication of guilt as any."
            vasily "He fled like a coward, leaving his mother's corpse behind."

            "The pain in his voice, raw and jagged, was almost unbearable. I had never seen Vasily this shaken before."

            show vasily alt_savage at right_char
            vasily "The queen's body was found in her solar… crumpled beside her writing desk. A dagger straight through her heart. No signs of struggle. No mercy."
            vasily "Her own son left her there like refuse."
            vasily "The day after that and the cold became unbearable. The blizzard began."

            show svante normal_mad at center
            svante "The king... Father… he was broken by the queen's death. After that, Elias vanished into the frost, like a shadow… He's the reason the kingdom is falling apart."
            svante "Father… He probably believed in Elias. And he left him with a corpse and a curse. If I could—"
            svante "If I only have the power to brave through this blizzard, I will kill him with my own bare hands!"

            "Prophet: If I may. Me and my prophet brothers can sense the death god's magic in this storm. It's unmistakable."

            show niko normal_serious at right_char with Dissolve(0.2)
            niko "All signs point to Elias. The storm, the cursed frost, the powers he's wielding… they all lead back to him. For all we know, he might have sold his soul to Enoch."

            "I couldn't help but feel the chill of dread that crept up my spine. Everything was pointing to the same conclusion—Elias was behind it all."

            show vasily alt_normal at right_char
            vasily "You're the only one who can save us, Dorian."

            jump ch2_questions

        "Can I take some supplies with me?" if not ch2_asked_supplies:
            $ ch2_asked_supplies = True

            show dorian normal_alt_neutral at left_char
            show vasily alt_think at right_char

            dorian "I might need supplies if I'm to set out for Frostcradle."

            show vasily alt_mad at right_char
            vasily "I'm afraid supplies are running thin, Dorian. The frost has locked us down tighter than we thought. The roads to Mjoll… they're almost impassable now."

            "He sighed heavily, rubbing his temples."

            show vasily alt_think at right_char
            vasily "The blizzards are worsening, and the snow is deepening. It's like the very land itself is trying to bury us. We've sent several expeditions out, but none have returned."

            show svante normal_nervous at center with Dissolve(0.2)
            svante "According to the scouts, even the peasants are feeling the cold, sir. It's getting harder to make trades, and even harder to get shipments in."

            show vasily alt_sad at right_char
            vasily "I don't know how much longer we can last with what we have. We've sent requests to the outer regions, but even the merchants are afraid to travel these roads now."

            show dorian serious at left_char
            dorian "…"

            "I frowned. The weight of their situation was clear."

            show vasily alt_normal at right_char
            vasily "The only ones left with any supplies… are the Cheng Industries bots. They've been sending us what they can."

            "I blinked. I think I've heard that name before. Cheng Industries. Yuxuan's company."

            "As if on cue, a mechanical hum echoed through the hall, and a sleek bot rolled in through the door. It was a little taller than a man, metallic and polished, with a rectangular chest and mechanical arms designed to lift heavy objects."

            show niko normal_base at right_char with Dissolve(0.2)
            niko "Right on cue…"

            show supply_robot base at center with Dissolve(0.2)
            "The bot's sensors glowed softly as it paused."

            "-Here at Cheng's, we bring change… -"

            "An oddly soothing jingle filled the room, the cheerful tone feeling almost out of place."

            supply_robot "Greetings. Supplies delivered—courtesy of Cheng Industries."

            "The bot spun around, unloading several crates of food and supplies with surprising agility. Canned goods, dried meats, and fresh produce packed neatly in the crates, along with a few additional barrels of water."

            show svante normal_happy at center
            svante "Wow. That's… amazing! Do you think they have a robot that talks? I've never seen—"

            show vasily alt_mad at right_char
            vasily "Svante… Did I give you permission to talk about anything other than the incident?"

            show svante normal_nervous at center
            svante "N-No, sir. Sorry, Count."

            show vasily alt_savage at right_char
            vasily "Then shut your mouth. One more slip, and I'll have you and whichever aldorith mutt you're closest to flogged for insubordination."

            show svante normal_sad at center
            svante "Yes, sir. I apologize."

            show niko normal_anger at right_char
            niko "Asshole."

            show vasily alt_mad at right_char
            vasily "What did you just say, Prophet?"

            prophet_1 "P-Perhaps we can move on, sire."

            show vasily alt_normal at right_char
            vasily "*sighs* As I said, Cheng Industries' bots have been delivering supplies. Only a few shipments, and only what they can carry. It's helping, but it's not enough to sustain us. We can't rely on them forever."

            "He fixed me with a hard stare."

            show vasily alt_savage at right_char
            vasily "You need to find Elias. And end him. Mjoll depends on it."

            show dorian normal_alt_confident at left_char
            "I straightened, meeting his gaze with a nod."

            dorian "Got it."

            jump ch2_questions

        "That's all I need.":
            show dorian normal_alt_neutral at left_char
            
            "I exhaled sharply, watching my breath curl into the frigid air like smoke."

            dorian "That's enough questions."

            show vasily alt_normal at right_char
            "Vasily gave a solemn nod. He gestured toward Niko."

            jump ch2_end


label ch2_end:

    # PDF p99 — Niko and Prophet give directions
    niko "Frostcradle lies to the west, buried in the heart of the mountains."

    "The other prophet raised a pale hand, pointing to a crudely drawn map on the table beside him. The inked lines were jagged, as if the cartographer's hand had trembled while drawing."

    "Prophet: Follow the ridge through the Iceclaw Pass. Then just go straight until you reach the Frostcradle."

    "I nodded, already tightening the straps of my pack. I adjusted the thick layers of fur and leather I had donned before leaving the castle."

    vasily "Take care, Dorian. I wouldn't want you to end up like those aldorith mutts."

    dorian "I'll find it."

    "Without another word, I turned on my heel, the weight of my mission pressing heavily on my shoulders."

    scene cg_black with fade                    # PLACEHOLDER — fade to black
    stop music fadeout 2.0
    stop audio fadeout 1.5

    pause 2.0

    # Chapter title card — Chapter 3 header
    show screen chapter_title_screen(
        "3",
        "Frostcradle",
        subtitle="Kingdom of Mjoll — The Cursed Mine",
        duration=3.0
    )
    pause 3.0

    jump chapter_3


# =============================================================================
# END OF CHAPTER 2
# =============================================================================
