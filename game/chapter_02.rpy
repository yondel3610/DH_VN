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
# Naming convention:
#   bg_  = background scene
#   cg_  = full-screen event illustration
#   Sprites: "character_name emotion"  (two-word tag, no underscores between)
#
# All paths are relative to the /game/ folder.
# Search "# PLACEHOLDER" to find every line needing a real asset.
# =============================================================================

# --- Backgrounds: Mjoll Exterior ---
image bg_mjoll_icelands          = "images/backgrounds/bg_mjoll_icelands.png"             # PLACEHOLDER
# Snow-blanketed frozen wilderness — dark sky, blizzard conditions, sparse pine trees

image bg_mjoll_blizzard          = "images/backgrounds/bg_mjoll_blizzard.png"             # PLACEHOLDER
# Same icelands but heavy snowfall — near-whiteout conditions, harsher

# --- Backgrounds: Mjoll Palace ---
image bg_mjoll_palace_exterior   = "images/backgrounds/bg_mjoll_palace_exterior.png"      # PLACEHOLDER
# Stone-and-ice fortress gate — guards posted, torchlight, imposing

image bg_mjoll_palace_throne     = "images/backgrounds/bg_mjoll_palace_throne.png"        # PLACEHOLDER
# Grand throne room — gilded stone, fur banners, cold light through high windows

image bg_mjoll_palace_hall       = "images/backgrounds/bg_mjoll_palace_hall.png"          # PLACEHOLDER
# Inner palace hall — aldoriths gearing up, torches, dim warmth

# --- Backgrounds: Dorian's Cave ---
image bg_mjoll_cave              = "images/backgrounds/bg_mjoll_cave.png"                 # PLACEHOLDER
# Small rocky cave interior — fur curtain doorway, fireplace glow, worn wooden table

image bg_mjoll_cave_night        = "images/backgrounds/bg_mjoll_cave_night.png"           # PLACEHOLDER
# Same cave at night — deeper shadow, fire lower, toy shelf visible

# --- Backgrounds: Town Square ---
image bg_mjoll_square_prep       = "images/backgrounds/bg_mjoll_square_prep.png"          # PLACEHOLDER
# Mjoll town square during setup — merchants arranging stalls, thin snow falling

image bg_mjoll_square_festive    = "images/backgrounds/bg_mjoll_square_festive.png"       # PLACEHOLDER
# Same square during celebration — crowd gathered, banners, Qiongqi head on pedestal

image bg_mjoll_square_battle     = "images/backgrounds/bg_mjoll_square_battle.png"        # PLACEHOLDER
# Same square mid-Frost Oni attack — crowd fleeing, ice shards, frost mist

image bg_mjoll_square_blizzard   = "images/backgrounds/bg_mjoll_square_blizzard.png"      # PLACEHOLDER
# Mjoll square days later — abandoned, snow-covered, eerie silence

# --- Backgrounds: Free Time Locations ---
image bg_mjoll_food_stalls       = "images/backgrounds/bg_mjoll_food_stalls.png"          # PLACEHOLDER
# Mjollian food stall row — cast iron cauldrons, smoked fish, steaming bread bowls

image bg_mjoll_violet_tent       = "images/backgrounds/bg_mjoll_violet_tent.png"          # PLACEHOLDER
# Babala's fortune-teller booth interior — violet curtains, crystal orb, incense smoke

image bg_mjoll_spa               = "images/backgrounds/bg_mjoll_spa.png"                  # PLACEHOLDER
# Mjollian spa interior — heated stone pools, steam, nobles lounging, aldorith workers

image bg_mjoll_pavilion          = "images/backgrounds/bg_mjoll_pavilion.png"             # PLACEHOLDER
# Quiet canopied pavilion — cushioned seats, fur blankets, sheltered from crowd noise

# --- CGs (Full-screen Event Illustrations) ---
image cg_qiongqi_charge          = "images/cg/cg_qiongqi_charge.png"                     # PLACEHOLDER
# The Qiongqi beast mid-charge — lion-bodied, black fur, ember eyes, fangs bared

image cg_qiongqi_death           = "images/cg/cg_qiongqi_death.png"                      # PLACEHOLDER
# Qiongqi impaled on earth spike, blood on snow — Dorian standing over it

image cg_svante_dunk_in          = "images/cg/cg_svante_dunk_in.png"                     # PLACEHOLDER
# Svante plunging into the freezing dunk tank — crowd cheering, lips turning blue

image cg_svante_spared           = "images/cg/cg_svante_spared.png"                      # PLACEHOLDER
# Ball striking wood to the side of the target — Svante staring at Dorian in disbelief

image cg_frost_oni_entrance      = "images/cg/cg_frost_oni_entrance.png"                 # PLACEHOLDER
# Frost Oni emerging from ice mist — crystalline forms, spears raised, crowd fleeing

image cg_babala_prophecy         = "images/cg/cg_babala_prophecy.png"                    # PLACEHOLDER
# Babala mid-prophecy — orb blazing, smoke surrounding her, eyes luminous white

image cg_dorian_cave_dinner      = "images/cg/cg_dorian_cave_dinner.png"                 # PLACEHOLDER
# Dorian eating alone at six-plate table — ghost-versions of family visible, firelight

image cg_noblewoman_swallowed    = "images/cg/cg_noblewoman_swallowed.png"               # PLACEHOLDER
# Earth tiles opening beneath the noblewoman — her expression frozen in a gasp

image cg_yuxuan_letter           = "images/cg/cg_yuxuan_letter.png"                      # PLACEHOLDER
# The ivory Cheng Industries letter — embossed emblem, neat calligraphy, firelight

image cg_dorian_frozen           = "images/cg/cg_dorian_frozen.png"                      # PLACEHOLDER
# Dorian encased in spreading frost — used for ICE GAME OVER ending

image cg_black                   = "images/cg/cg_black.png"                              # PLACEHOLDER
# Pure black screen — fade-outs, unconscious moments, chapter end


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

# --- Sound Effects ---
define audio.sfx_qiongqi_roar     = "audio/sfx/sfx_qiongqi_roar.ogg"          # PLACEHOLDER
define audio.sfx_earth_spike      = "audio/sfx/sfx_earth_spike.ogg"           # PLACEHOLDER
define audio.sfx_wind_blast       = "audio/sfx/sfx_wind_blast.ogg"            # PLACEHOLDER
define audio.sfx_ice_crack        = "audio/sfx/sfx_ice_crack.ogg"             # PLACEHOLDER
define audio.sfx_ice_shatter      = "audio/sfx/sfx_ice_shatter.ogg"           # PLACEHOLDER
define audio.sfx_frost_oni_roar   = "audio/sfx/sfx_frost_oni_roar.ogg"        # PLACEHOLDER
define audio.sfx_prophecy_thunder = "audio/sfx/sfx_prophecy_thunder.ogg"      # PLACEHOLDER
define audio.sfx_dunk_splash      = "audio/sfx/sfx_dunk_splash.ogg"           # PLACEHOLDER
define audio.sfx_heartbeat        = "audio/sfx/sfx_heartbeat.ogg"             # PLACEHOLDER
define audio.sfx_ground_swallow   = "audio/sfx/sfx_ground_swallow.ogg"        # PLACEHOLDER
define audio.sfx_vine_attack      = "audio/sfx/sfx_vine_attack.ogg"           # PLACEHOLDER

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
# SECTION 5: LABEL CHAPTER_2 — Opening (Icelands / Qiongqi Hunt)
# =============================================================================
# Entry point — jumped to from chapter_01.rpy via 'jump chapter_2'.
# PDF pages 58-61.
# =============================================================================

label chapter_2:

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
    # BG: bg_mjoll_icelands
    # -------------------------------------------------------------------------

    scene bg_mjoll_icelands with fade           # PLACEHOLDER — frozen wilderness

    # [COMMENT: bg_mjoll_icelands — snow falls steadily, silent, sparse pines]

    "The snow falls steadily, blanketing the area in silence. The only sounds are the crunch of boots and the occasional muttered curses from the mercenaries behind me."

    # show mjoll_pavel nervous at left           # PLACEHOLDER — Pavel sprite (nervous)
    # show mjoll_helga steady at center          # PLACEHOLDER — Helga sprite (steady)
    # show mjoll_lars tense at right             # PLACEHOLDER — Lars sprite (tense)

    # PDF p58
    mjoll_pavel "Merciful Enoch, it's freezing. Why does it have to be this cold?"
    mjoll_helga "Quit complaining, Pavel. We've got bigger things to worry about. You know what this beast did to that caravan last week."
    mjoll_lars  "Screw what it did to the caravan. It destroyed an entire village. I don't know why only five of us were sent to kill it!"

    "Their voices lower, but I can still hear them."

    mjoll_lars  "Hey... is that him? The Dragon of Gale?"
    mjoll_pavel "No way. He's not... The Dragon of Gale wouldn't be out here with us."
    mjoll_helga "Wait… Enoch above… it really is him. I heard he lost his entire family. Wife and kids... all of them gone."
    mjoll_pavel "No wonder he looks dejected. What kind of man comes back from something like that?"
    mjoll_lars  "Shut up. He'll hear you!"

    "Vasily shoots them a sharp glare. He snaps his fingers."

    # show vasily commanding at center           # PLACEHOLDER — Vasily sprite (sharp authority)

    vasily "Eyes forward. Lose focus out here, start thinking about the wrong things and you'll be nothing but meat for the beasts. Do I make myself clear?"
    mjoll_lars "Sir!"

    "The snow around us seemed to grow heavier. I looked around, scanning the barren landscape."
    "Something was off. Too quiet, too still. The wind carried a foul, metallic scent—blood. I stopped in my tracks and raised a hand."

    dorian "We're here."

    # PDF p59
    "The mercenaries stiffened, their chatter ceasing immediately. They looked around nervously, hands shaking as they start gripping their weapons."

    mjoll_lars "Umm… where?"

    "Silence."
    "Then it came."
    "A low, guttural growl rumbled through the frozen wilderness, vibrating the ground beneath us. The snow swirled as if alive, the wind howling in response to the beast's presence."
    "The Qiongqi emerged from the shadows, its massive form blending with the storm. It had the body of a lion but twisted and wrong—its fur black as midnight, its eyes burning like embers. Its sharp claws scraped against the frozen ground, leaving deep gouges."

    # CG: the Qiongqi emerges — full screen, shock entrance
    play sound sfx_qiongqi_roar                 # PLACEHOLDER — Qiongqi roar SFX
    scene cg_qiongqi_charge with shock_cut      # PLACEHOLDER — cg_qiongqi_charge
    pause 0.8
    scene bg_mjoll_icelands with dissolve       # Return to icelands bg

    play music ost_qiongqi_hunt fadein 0.5      # PLACEHOLDER — hunt battle music

    # PDF p59 — Qiongqi speaker tag used for all beast lines in this scene
    # [COMMENT: The PDF uses "Qiongqi:" for this beast's sounds. frost_oni tag is reserved for the ice beings later]
    frost_oni "KRRRIIEEEEEEEEAAAAAAAHHHHH!!!"

    "It charged. A blur of claws and fury."

    vasily "Hold your ground!"

    "One mercenary swung his sword wildly, only for the beast to swat him aside like a doll, sending him crashing into the snow. Another let loose an arrow that bounced harmlessly off the Qiongqi's thick hide."

    mjoll_lars  "AHHH!!"
    mjoll_helga "My arrows aren't working! Use your shield, Lars!"

    "The beast lunged at the third mercenary, its claws slicing through his shield as though it were parchment."
    "I thrust my arms toward the ground. Pillars of jagged earth erupted from beneath the Qiongqi, slamming into its underbelly and knocking it off balance."

    play sound sfx_earth_spike                  # PLACEHOLDER — earth spike SFX

    # PDF p59
    frost_oni "Krieeeeeeaaahh!!"

    "It screeched in agony, flipping mid-air, crashing to the ground. Clumps of black fur and blood sprayed into the snow."
    "But it wasn't finished."
    "It rose, furious—its mouth split open unnaturally wide as it released another piercing howl."

    frost_oni "RAAAAAHHHHHHHRRGHHHH!!!"

    vasily "Dorian! It's coming for you!"

    "I didn't move."

    # PDF p60
    "Instead, I rotated my palm. The wind around me shifted. Then roared."

    play sound sfx_wind_blast                   # PLACEHOLDER — wind blast SFX

    "A gale burst forth—a spiraling, howling torrent that slammed into the Qiongqi's face, flinging it backward across the battlefield like a rag doll. The snow whipped into a frenzy as the beast clawed at the ice, struggling to find footing."

    frost_oni "RAAAAAHH!! RAAAHHH!!"

    mjoll_lars  "Helga, your bow! Hit it on its shoulder!"

    "One of the Mjoll soldiers managed to shoot an arrow, and by some stroke of luck—or desperation—it embedded itself in the Qiongqi's shoulder. The beast howled, thrashing violently, but it only seemed angrier."

    frost_oni "Krieeeeeewwwaaahh!!"

    mjoll_helga "Haha! Take that!"

    "Vasily stepped forward, his expression calm but his eyes burning with resolve. He raised his hands, and a blinding light erupted from his palms. The Qiongqi screeched, recoiling from the light."

    vasily "Now, friend!"

    "I didn't hesitate. Summoning a massive portion of earth, I brought a jagged spike of stone hurtling up beneath the Qiongqi's chest, impaling it."

    play sound sfx_earth_spike                  # PLACEHOLDER — earth spike SFX

    # PDF p60
    frost_oni "Kwaaaaaaaaahhh—"

    "The winds circled my body, responding to my silent fury. With a snap of my hand, a twisting column of wind slammed into the Qiongqi's skull, driving it headfirst into the frozen ground with enough force to shatter bone."

    frost_oni "GRGHHHHHHKKKKHHHHHHH—"

    "The monstrous shrieking was cut short. The Qiongqi twitched once… then went still."
    "Dead."

    # CG: Qiongqi dead on snow
    scene cg_qiongqi_death with dissolve        # PLACEHOLDER — cg_qiongqi_death
    pause 1.5
    scene bg_mjoll_icelands with dissolve       # Return to icelands bg

    stop music fadeout 2.0

    # PDF p60
    mjoll_pavel "He… he literally could have just done this without us."
    mjoll_lars  "He really is… the Dragon…"

    "I stood over it, my breath steady, my gaze cold."

    dorian "Cut off its head. Now."
    mjoll_lars "Yes, sir."

    "He nodded quickly, drawing his blade and stepping toward the corpse."
    "I turned away, wiping the bloodied snow from my gauntlets. Vasily approached, his light fading."

    # PDF p60-61
    vasily "That was quick, friend. You didn't even flinch."
    vasily "Are we even needed anymore, or are we just here for the scenery? Haha."

    "I didn't respond. My eyes were fixed on the distant horizon, where the snow-covered peaks loomed like silent watchers."

    dorian "Time to go back."

    # PDF p61
    "The walk back to Mjoll was silent except for the crunch of snow beneath our boots. The soldiers lingered behind me, talking about how they survived the fight with the monster."
    "The Qiongqi's head dangled from my grasp, dripping thick, acrid blood that left a crimson trail in the pure white snow. Its weight didn't bother me—I'd carried far worse."

    jump ch2_palace


# =============================================================================
# SECTION 6: LABEL CH2_PALACE — Mjoll Palace (Gustav's Court)
# =============================================================================
# PDF pages 61-63.
# =============================================================================

label ch2_palace:

    # PDF p61
    # [COMMENT: bg_mjoll_palace_throne — guards stiffened at gates, incense in throne room]
    scene bg_mjoll_palace_throne with fade      # PLACEHOLDER — Mjoll throne room
    play music ost_mjoll_palace fadein 2.0      # PLACEHOLDER — stiff court theme

    "When we reached the gates of the palace, the guards stiffened, their pale faces betraying their unease. They exchanged glances but didn't dare to stop me. As I pushed through the heavy doors, Vasily trailing close behind."
    "We enter the throne room; the smell of incense hangs thick in the air. A group of Aldoriths knelt on the cold stone floor, their heads bowed low."
    "At the far end of the room, King Gustav Nordstrom sat upon his gilded throne, his face as hard as the icy mountains that surrounded Mjoll. Beside him, Queen Ekaterina Drakos sat, her dark eyes gleaming."

    # show king_gustav throne at center          # PLACEHOLDER — King Gustav sprite (throne, hard face)
    # show queen_ekaterina beside him            # PLACEHOLDER — Queen Ekaterina sprite (gleaming dark eyes)
    # show svante kneeling at left               # PLACEHOLDER — Svante sprite (purple hair, kneeling)
    # show kristin kneeling at left              # PLACEHOLDER — Kristin sprite (kneeling, silver hair)

    vasily "Enoch above. Another punishment?"

    "One of the kneeling Aldoriths—a young man with striking purple hair—raised his head."

    svante "Please, Father! I beg you! I didn't mean to—"

    king_gustav "You dare speak to me that way, boy? You've been given every chance to prove your worth, and yet you continue to disappoint me."

    "The queen leaned forward, her voice a venomous whisper."

    queen_ekaterina "Svante should be grateful, Your Highness. Without your guidance, he'd be no better than a stray mutt."
    kristin         "Quiet, Svante. You'll only make it worse for us. Please…"
    boy_ald         "Worse? What more can he take from us that he hasn't already?"

    "I step closer and into the throne room, the soldiers following at a distance, the Qiongqi's head dripping blood onto the pristine marble floor."

    # PDF p62
    king_gustav "Enough! That goes for all of you. If you disobey, you will be beheaded like your brothers and sisters. IS THAT CLEAR? You are nothing without my name. Nothing!"
    "Aldoriths: Yes, Father."
    queen_ekaterina "Svante speaks like he's a prince, but look at him—groveling like the dog he is."
    svante "I… I'm sorry, Father… Please forgive me… I—"

    "I step forward then, the Qiongqi's head swinging in my grasp, its blood dripping onto the pristine marble floor. The sound of the impact silences the room."
    "The Aldoriths freeze, their wide eyes darting to me."

    boy_ald "It's him…"
    svante  "The Dragon of Gale…"

    king_gustav "Ah, Dorian. You've returned. Efficient as always. What news of the beast?"

    "I drop the Qiongqi's head unceremoniously onto the floor."

    dorian "The beast is dead. Your kingdom is safe, for now. My payment."

    "The king gestures lazily, and a servant scurries forward, pressing a heavy pouch of gold into my hand. I take it without ceremony, glancing briefly at Vasily."

    dorian "Thanks."

    king_gustav     "This particular Qiongqi has terrorized these lands for a month now, devouring livestock, destroying villages, and killing many of my subjects. The people of Mjoll will sleep easier tonight thanks to you."
    queen_ekaterina "You've done this kingdom a great service. And for that, we shall show our gratitude."

    vasily "You've done what no one else could, Dorian. The King wants to make a spectacle of this victory, a display of his generosity to the people. He'll reward you handsomely if you make an appearance tomorrow."

    dorian "Tomorrow?"
    vasily "Yes, tomorrow. There'll be a celebration for the people. They wanted to celebrate your slaying of the Qiongqi."

    "I glance down at the bloodied pouch of gold in my hand."

    dorian "I'll be there."

    # PDF p62-63
    "As I turn to leave, I hear the Aldoriths' voices behind me, trembling and desperate."

    svante  "Father, please, I only sought to prove my loyalty! Give me another chance!"
    kristin "We'll do anything—just let us stay by your side!"

    king_gustav "You've embarrassed me for the last time. Guards, take them to the dungeon. Perhaps some time in the dark will teach you the value of obedience."

    queen_ekaterina "They're lucky they didn't end up like the others. You're far too kind, my love."

    "I don't look back as the Aldoriths' pleas turn to sobs, swallowed by the clang of armor and the heavy slam of the dungeon doors."

    # PDF p63
    "Vasily catches up to me as I leave the palace, the snow crunching beneath our boots."

    vasily "Dorian, look. You don't have to come tomorrow, you know. But the King won't forget if you don't. And neither will the people."
    dorian "Let them remember what they want. I just want my gold."

    "Vasily places a hand on my shoulder."

    vasily "My offer still stands, okay? Let me know if you want to grab a beer or two. On me."

    "I nod. The wind bites at my face as I head back into the streets of Mjoll, my path lit only by the faint glow of lanterns. I clutch the pouch tightly, its weight pulling at my hand."

    jump ch2_cave


# =============================================================================
# SECTION 7: LABEL CH2_CAVE — Dorian's Cave (Grief / Dinner Alone)
# =============================================================================
# PDF pages 63-64.
# =============================================================================

label ch2_cave:

    # PDF p63
    # [COMMENT: bg_mjoll_cave — fur curtain doorway, small fireplace, flickering shadows]
    scene bg_mjoll_cave with fade               # PLACEHOLDER — cave interior, firelight
    stop music fadeout 2.0
    play music ost_cave_grief fadein 3.0        # PLACEHOLDER — fragile grief theme
    play audio amb_cave_fire loop fadein 2.0    # PLACEHOLDER — crackling fire ambient

    "I go back to my small cave, the entrance of which is shielded by a curtain of thick furs, swaying slightly in the icy wind of Mjoll."
    "I duck inside, pulling the curtain closed behind me, shutting out the biting cold. The glow of a small fireplace greets me, casting flickering shadows on the rough stone walls."

    "I kneel by the fireplace, adding another log to the fire. From the small stash of ingredients I've gathered over the years, I begin to prepare dinner."
    "I set out six simple plates, each one mismatched and worn, around a low wooden table I carved myself."
    "I ladle out portions of the stew I've cooked—one for me, and five for them."

    # CG: Dorian alone at the six-plate table — ghost-family visible as warm light
    scene cg_dorian_cave_dinner with dissolve   # PLACEHOLDER — cg_dorian_cave_dinner
    pause 2.0
    scene bg_mjoll_cave with dissolve           # Return to cave bg

    "I sit in my usual spot, looking at their plates."

    # These lines are ghost-voices from memory — no sprites for family here
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
    # [COMMENT: bg_mjoll_square_prep — booths being set up, thin snow falling, merchants bustling]
    scene bg_mjoll_square_prep with fade        # PLACEHOLDER — town square, setup in progress
    play music ost_mjoll_festive volume 0.4 fadein 2.0  # PLACEHOLDER — light festive theme

    "The city square of Mjoll is already alive with activity as I arrive the next day. The air is brisk, the cold biting but not enough to faze me anymore."
    "Booths are being set up around the square, their wooden frames dusted with a thin layer of snow. Merchants and servants bustle about, their breath forming small clouds in the icy air."

    "I spot Vasily almost immediately, standing near the center of the square. He's barking out orders, pointing left and right."

    # show vasily commanding at center           # PLACEHOLDER — Vasily sprite (in his element)

    vasily "Make sure the performers don't miss a single beat. We don't want to have any on-the-spot beheadings this time around. We don't want any blood on our booths now, would we?"
    "All: Sir!"

    "The crowd disperses, and I approach him. When he catches sight of me, his eyebrows shoot up in surprise."

    vasily "Dorian? Already here?"

    "I fold my arms, shrugging slightly."

    dorian "Why wouldn't I be?"
    vasily "Oh, silly me. When have you not been early? You'd show up to your own funeral two hours in advance just to make sure everything's running smoothly."

    "I don't respond, letting the comment hang in the cold air. Vasily studies me for a moment, his expression softening."

    vasily "The event doesn't start for another two hours, you know."
    dorian "I'm aware. Just wanted to check the area."

    "He raises an eyebrow but doesn't press further. Instead, he gestures to the booths around us."

    # PDF p64-65
    vasily "The king and queen will be here later, but as you can see, we've got quite the spectacle planned. Feast, performances, and of course…"

    "He leans in slightly, lowering his voice."

    vasily "…the presentation of the Qiongqi's head. It'll be the centerpiece."

    "I nod, glancing at the large wooden platform being constructed in the center of the square."

    dorian "Don't you think it's a little extravagant?"
    vasily "You know His Highness. Also, the people need something to rally around. After everything that's happened, a little morale boost goes a long way."

    "I stay silent, my gaze drifting across the square. Children laugh as they chase each other around the booths. Adults are happily chatting with each other as the snow lightly falls."

    # PDF p65
    vasily "You should get some rest, Dorian. Come back when the festivities start. You've done your part."
    dorian "I'm fine."

    "He sighs, muttering something under his breath."

    vasily "Suit yourself. Just don't scare the merchants."

    "I smirk faintly at his jab but say nothing."

    vasily "Come to think of it…"

    "I glance at him, raising a brow."

    dorian "What?"

    "He folds his arms and smirks."

    vasily "You're already here. Why not help me check the booths? Make sure everything's up and running?"

    "I scoff, shaking my head."

    dorian "Not interested."
    vasily "Dorian, come on. When's the last time you did something remotely enjoyable? When's the last time you had fun?"

    "I narrow my eyes at him."

    dorian "Every night. When I spend my time with my family."

    "He nudges my shoulder gently."

    vasily "Hmm… Yeah, but you could use a distraction. Look, if you join me, I'll make it worth your while."

    "I raise a skeptical brow."

    dorian "How?"

    # PDF p65-66
    vasily "Gold. From the king, naturally. Consider it… an incentive for your services."

    "I let out a slow breath, crossing my arms as I mull it over."

    dorian "Fine. Let's get this over with."
    vasily "That's the spirit, friend!"

    "He claps me on the back, his grin widening."
    "As we begin to walk through the square, Vasily dives into his element, greeting merchants, inspecting goods, and occasionally throwing in a comment or two about how to make things 'more appealing to the people.'"
    "I follow in silence, my eyes scanning the colorful displays and the array of items on sale."
    "The scents of freshly baked bread and spiced meat waft through the air, mingling with the faint chill of the snow. People are beginning to trickle into the square, as we walk on by."

    # PDF p66
    vasily "See? Not so bad, is it? Unfortunately, the merchant who sells Mjollian Mead-Braised Lamb was mercilessly killed by a yaoguai before coming here so… we might have to settle for less."

    "I grunt in response, earning a chuckle from him."

    vasily "Alright, Dorian. Since you're tagging along, where do you want to go? Completely up to you."

    jump ch2_freetime


# =============================================================================
# SECTION 9: LABEL CH2_FREETIME — D2 Free Time Menu (4 options)
# =============================================================================
# PDF pages 66-77.
# Uses 'call' to visit sub-scenes; each ends with 'return'.
# After the spa, the game forces a visit to the fortune teller before Common.
# =============================================================================

label ch2_freetime:

    menu:

        "Visit the food stalls.":
            $ ch2_visited_food = True
            call ch2_food_stalls
            jump ch2_freetime

        "Visit the fortune teller.":
            $ ch2_visited_fortune = True
            call ch2_fortune
            jump ch2_freetime

        "Relax at the spa." if not ch2_visited_spa:
            $ ch2_visited_spa = True
            call ch2_spa
            # After spa the PDF directs to fortune teller if not yet visited
            if not ch2_visited_fortune:
                $ ch2_visited_fortune = True
                call ch2_fortune
            jump ch2_freetime

        "Rest with Vasily.":
            $ ch2_visited_rest = True
            call ch2_rest
            jump ch2_freetime

        "Head to the celebration.":
            jump ch2_common_freetime


# =============================================================================
# SECTION 10: FREE TIME SUB-SCENE LABELS
# =============================================================================

# -----------------------------------------------------------------------------
# D2-A: FOOD STALLS
# PDF pages 66-69.
# Sub-choice: Confront the guards or Do Nothing
# -----------------------------------------------------------------------------

label ch2_food_stalls:

    # PDF p66
    # [COMMENT: bg_mjoll_food_stalls — cast iron cauldrons, smoked fish, bread bowls steaming]
    scene bg_mjoll_food_stalls with dissolve    # PLACEHOLDER — Mjollian food stalls

    "Vasily and I decided to stroll through the food stalls, the air thick with the aroma of roasted fish, hearty soups, and fresh-baked bread. The snow-covered streets contrast with the vibrant colors of the vendors' booths."

    vasily "Ah, here we go, Dorian. Mjollian cuisine is second to none. Let me guess, you haven't eaten anything decent in weeks."
    dorian "Hmph."

    "I grunt in response, but my stomach betrays me with a growl. He smirks and gestures toward a booth with a large cast iron cauldron."

    # show vendor_mjoll cheerful at right        # PLACEHOLDER — Vendor sprite (ladling stew)

    # PDF p66-67
    vendor_mjoll "Two Zarybas, fresh and hot! Best in all of Mjoll!"

    "Vasily hands over a few coins and passes me one of the bread bowls."

    vasily "Eat, friend. You'll thank me later, hungry grumpy man."

    # [COMMENT: FOOD4 — Zaryba Stew: smoked sturgeon, root vegetables, wild herbs, served in thick crusty bread bowls]
    "I take a bite. The smoky, savory flavor of the sturgeon hits me first, followed by the earthiness of the parsnips and turnips. The bread, soaked in the stew, is soft yet hearty. It's... surprisingly good."

    # PDF p67
    dorian "It's… *groans*"
    vasily "See? I told you. Nothing like food to make life a little less bleak."
    dorian "…"
    vasily "You know, you could make this easier on yourself. You've been carrying this weight for four years. Maybe it's time to let some of it go."

    "I don't answer, focusing instead on the meal. Vasily knows better than to push further and continues eating."

    "As we get up to leave, I catch sight of the vendor. She stands at the edge of the stall, watching the guards escort two boys carrying heavy crates. Her eyes are filled with tears."

    # show male_guard harsh at left              # PLACEHOLDER — Male Guard sprite
    # show boy_ald_spa struggling at center      # PLACEHOLDER — Boy Aldorith (straining under crate)

    male_guard  "Come on! Pick up the pace, will ya? Don't make me bring out the whip!"
    boy_ald_spa "Please, sir! We just need a drink!"
    female_guard "You'll get your drink after an hour! Now get back to work!"

    vasily "Come on, friend. Don't get any ideas. You can't save everyone."

    "The vendor glances toward me briefly."

    # -----------------------------------------------------------------------
    # D2-A SUB-CHOICE: Confront or Do Nothing
    # -----------------------------------------------------------------------

    menu:

        "Confront the Guards.":
            $ ch2_food_choice = "confront"

            # PDF p67-68
            "I clench my fists, stepping toward the guards as they bark orders at the two kids."

            dorian "Let them rest. They're just kids."

            "The guards turn, startled, before recognizing me. One of them straightens up, puffing out his chest."

            male_guard "Stay out of this, mercenary. These children are property of the Crown. They do as they're told."

            "The vendor watches silently, her hands trembling."

            dorian "They look half-dead. If you push them any further, they'll collapse."
            male_guard "Then they collapse. Not our problem their constitution's weak."

            female_guard "Y-You fool! Th-that mercenary is the Dragon of Gale."
            male_guard   "What? O-Oh… Um… Sure. Kids, break time!"

            "The two kids immediately run to the vendor to get some water."

            vendor_mjoll "Here's some water. Please drink. Are you hungry, my children?"

            vasily "*sighs* You just had to make a scene. Let's go."

        "Do nothing.":
            $ ch2_food_choice = "nothing"

            # PDF p68
            "I glance at the vendor, then at the guards. My fists clench, but I force myself to stay rooted in place."
            "The vendor's gaze meets mine for a moment, her eyes pleading, but I look away. Vasily doesn't say anything—he knows what I'm feeling, even if I don't show it."

            dorian "…"
            vasily "Let's go, Dorian. Nothing to see here."

            "As we walk away, I hear the guards bark another order at the children. A crate crashes to the ground, followed by the sound of a whip cracking. A woman's stifled sob is the last thing I hear as we round the corner."

    # Both sub-choices converge — PDF p68-69
    vasily "I know what you're thinking. You want to charge in, right every wrong. But that's not how Mjoll works, Dorian."
    vasily "This place… It survives because of the system. The King and Queen, for all their flaws, keep the kingdom standing."

    dorian "You really believe that?"

    "Vasily doesn't answer immediately."

    # PDF p69
    vasily "I believe that survival comes at a cost. You've paid yours. Maybe it's time to stop paying for everyone else's."

    "I stay silent, the taste of the Zaryba still lingering on my tongue, now bitter."

    return


# -----------------------------------------------------------------------------
# D2-B: FORTUNE TELLER — BABALA
# PDF pages 69-73.
# Sub-choice: Ask about family or ask about companions
# Both branches converge on the Five Companions prophecy
# -----------------------------------------------------------------------------

label ch2_fortune:

    # PDF p69
    # [COMMENT: bg_mjoll_violet_tent — dim, violet curtains, crystal orb glowing faintly, incense]
    scene bg_mjoll_violet_tent with dissolve    # PLACEHOLDER — Babala's booth interior

    play music ost_babala_prophecy fadein 2.0   # PLACEHOLDER — ethereal prophecy theme

    "Vasily nudges me toward the dimly lit booth draped in heavy, violet curtains. A crooked, hastily-painted sign outside reads: 'Babala: Your Fate Awaits.'"

    vasily "Oh she's back in town!"
    dorian "Really? Who?"
    vasily "Babala. She's a fortuneteller. They say she never misses with her fortunes. I'd say it's worth a try. She's—"
    dorian "Not interested."
    vasily "Come on, Dorian. I'd say it's worth a try."

    "I glare at him."

    dorian "Fortunes are just words to me, Vasily. Nothing more."
    vasily "Words have power, you know. Besides, maybe she'll tell you about your love life. Don't you think it's time to move on?"

    "I stop in my tracks, the air around us growing cold."

    dorian "I will never remarry, Vasily. Don't bring that up again."

    "The fortune teller, a middle-aged woman, with white eyes, peeks out from the curtains, chuckling softly."

    # show babala seated at center               # PLACEHOLDER — Babala sprite (white eyes, knowing smile)

    babala "Haha. You are as stubborn as the stone you channel, Dragon of Gale. But even the hardest stone cracks in time."

    "Vasily laughs, patting my shoulder."

    # PDF p70
    "We step inside. The booth is small but warm, the scent of incense hanging in the air. A crystal orb glows faintly on the table, and behind it sits Babala."
    "She looks up, her lips curling into a knowing smile."

    babala "The Dragon of Gale. I wondered when you'd visit me."
    vasily "He didn't want to come, of course, but I dragged him here. Babala, tell him something interesting—preferably about his love life."
    babala "*laughing* Your friend has a sharp tongue."

    "I glare at Vasily, but Babala's chuckle draws my attention back to her."

    babala "Sit, child of fire. Let the Weaver guide us."

    "I hesitate before sitting across from her. Her gaze turns distant as she places her hands on the crystal orb."

    babala "The Weaver… the one who spun the first threads of existence. From the void, she created the Tetrad—four immortal beings who shaped the world."
    babala "Together, they wove the earths, the waters, the heavens, and all life. But it is the Weaver who holds all fates in their loom."

    "Her voice takes on a reverent tone, and for a moment, the air feels heavier."

    babala "And now, she weaves your threads, Dragon of Gale."

    dorian "Th-that's great, I guess."

    "The crystal orb flickers, and a faint swirl of smoke begins to rise. Babala's eyes widen slightly, and her lips curl into a smile."

    babala "Normally, I allow people to ask one question, but for you, Dragon, I will permit two. Fate bends itself for those who walk in its shadow."
    vasily "*laughs jealously* Why the special treatment?"

    "Babala doesn't answer him. The swirling smoke grows, curling around me like an embrace. It feels strangely comforting, and I instinctively close my eyes."

    babala "Don't fight it, Dragon. Open your heart to me."

    "She leans forward, her voice dropping to a whisper."

    babala "Do not fight it, Dragon. Let your heart guide your words to the Weaver's threads. Ask me anything you wish to know."

    dorian "Anything, huh?"

    # -----------------------------------------------------------------------
    # D2-B SUB-CHOICE: Family or Companions
    # -----------------------------------------------------------------------

    menu:

        "How is my family doing?":
            $ ch2_babala_asked_family = True

            # PDF p71
            dorian "I want to know how is my family doing."

            "Babala's expression softens, and the crystal orb flares with light."

            babala "Your family… they have passed on to Tianlun, the Eternal Realm of Peace. Elara cradles your children in her arms, and their laughter echoes through fields of gold."
            babala "Daniel. Emily. Sarah. Lucas. They are at peace, Dorian. But they watch over you still, their love woven into your every step."

            "My throat tightens, and I can barely speak."

            dorian "They're… happy?"
            babala "Happier than you can imagine. But they long for you to find your peace as well."

            "Vasily places a hand on my shoulder, his usual teasing replaced with quiet support."

            dorian "Elara…"

            babala "But the threads of fate are not yet finished. We must look to the future."
            vasily "I think Dorian's had enough—"

            # Thunder — the orb blazes, Babala transforms into the vessel of prophecy
            play sound sfx_prophecy_thunder     # PLACEHOLDER — thunder crack SFX

            # CG: Babala in full prophecy — luminous eyes, smoke billowing
            scene cg_babala_prophecy with flash # PLACEHOLDER — cg_babala_prophecy
            pause 1.0
            scene bg_mjoll_violet_tent with dissolve

            babala "Before your time is up, you will hold another daughter in your arms. She will bring you peace, Dragon. A second chance at family, a chance to heal what was broken."

            # PDF p71 — internal thought
            "Another daughter? How could I even think of raising another child after what happened to Elara and the kids?"

            dorian "That'll be impossible since I'll never remarry but, thank you."

            "The booth grows colder as her voice rises."

        "How are my companions?":

            # PDF p72
            "My thoughts drift to the others—Paladin Feng, Paladin Cyrus, Empress Olympia, the soldiers who stood beside me during the Tragedy of Tianho."

            dorian "I want to know… how are my past companions?"

            babala "Your companions remain strong. Paladin Feng heals slowly but surely; his resolve is unbroken. Empress Olympia rebuilds what was lost, her strength inspiring those around her."
            babala "Paladin Cyrus has moved on… As for Count Vasily…"

            vasily "You do realize I'm standing right here, don't you?"

            "She glances at him, a smirk tugging at her lips."

            babala "He frets over you more than he lets on."
            vasily "I do not fret."
            babala "But the threads of fate do not end here. We must look to the future."
            vasily "Well, that's enough fortune-telling for one day, don't you think? We sho—"

            # Thunder interrupts Vasily
            play sound sfx_prophecy_thunder     # PLACEHOLDER — thunder crack SFX

            scene cg_babala_prophecy with flash # PLACEHOLDER — cg_babala_prophecy
            pause 1.0
            scene bg_mjoll_violet_tent with dissolve

            "A sudden crash of thunder interrupts him. The orb glows fiercely, and Babala's voice grows deeper, more resonant. Smoke surrounds her, and her eyes shine with an unnatural light."

            "The booth grows colder as her voice rises."

    # -----------------------------------------------------------------------
    # Both sub-choices converge on the Five Companions prophecy
    # PDF p71-72 (family) / p72-73 (companions)
    # -----------------------------------------------------------------------

    babala "I see you surrounded by five figures. Five men, each unique and powerful. They will walk beside you, bound by loyalty and something deeper. Together, you will face the storm that looms ahead."

    babala "Beware, Dragon. A great calamity will strike Ena, and only you and your companions may stand against it. The Weaver's threads will guide you, but the path will not be easy."

    "The light fades, and Babala slumps in her chair, panting."

    babala "*pants* You're welcome."

    vasily "Well… that's something, isn't it?"

    # PDF p73
    "As Vasily and I leave the booth, he tries to lighten the mood with a joke."

    vasily "Five men, huh? Looks like you're going to be popular."

    "I shake my head, the weight of Babala's words pressing heavily on my chest."

    dorian "Let's move on, Vasily."

    stop music fadeout 2.0

    return


# -----------------------------------------------------------------------------
# D2-C: SPA
# PDF pages 73-76.
# Sub-choice: Do nothing (walk away) or Punish the noblewoman (swallow her)
# After spa, game redirects to fortune teller if not yet visited
# -----------------------------------------------------------------------------

label ch2_spa:

    # PDF p73
    # [COMMENT: bg_mjoll_spa — heated stone pools, steam, nobles lounging, aldorith workers]
    scene bg_mjoll_spa with dissolve            # PLACEHOLDER — Mjollian spa interior

    "The spa's grand facade rises before us, smoke wafting from its chimneys."

    dorian "Maybe the spa would be a good idea."
    vasily "A spa? Hmm I love it! Perfect!"

    "We step into the spa, the warmth of the heated pools doing little to thaw the chill in my chest. The nobles recline in luxurious pools while aldorith attendants bustle about, their eyes downcast, their bodies worn thin from endless labor."
    "A young aldorith boy, looking no older than ten, struggles with a heavy bucket of steaming water, his hands trembling from the heat. He stumbles, spilling water onto his arm. His face contorts in pain, but he quickly bows his head, attempting to clean the mess with his sleeve."

    girl_ald_spa "Brother! Let me help you!"

    "Nearby, a noblewoman watches with disdain."

    # show noblewoman contemptuous at right      # PLACEHOLDER — Noblewoman sprite (fan raised)

    noblewoman  "Disgusting, clumsy brat! Do you think I pay for this kind of incompetence?"
    boy_ald_spa "I-I'm sorry, mam! I didn't mean to—"

    "She lashes out with her fan, striking the boy across the face. The sound echoes through the room. He flinches but doesn't cry out."

    "I glance at the boy, my jaw tightening. A pang of something sharp hits my chest—Sarah. Lucas. Emily. Daniel."

    # PDF p74
    vasily "Dorian…"
    vasily "I know what you're thinking. But don't. This place… It's not Gale. And it's not Tianho."

    dorian "Tianho. As if I could forget."
    vasily "You think I don't remember, too? I lost people there. You weren't the only one who—"
    dorian "Don't. Besides, I don't care. These kids... they're not my problem."

    "The noblewoman sees a young girl scrubbing the floor nearby. Her hands are raw, the skin peeling from the harsh soaps and constant work."
    "She pauses for a moment to wipe sweat from her brow, and the same noblewoman snaps her fan toward her."

    noblewoman   "Don't stop! If I can see my reflection in the marble, you're not scrubbing hard enough!"

    "The girl nods quickly, her small body trembling as she works faster."

    "I glance back at the boy, who's still scrubbing the floor with raw, trembling hands. The noblewoman raises her fan to hit him again, but the girl tries to shield him from the noblewoman's wrath."

    girl_ald_spa "P-Please, mam. Forgive us."
    noblewoman   "Incompetent aldoriths! I'll have you both dragged out and hanged for disobeying a noble!"

    "The girl freezes, her eyes wide with terror as tears spill down her cheeks. The boy drops to his knees, scrubbing furiously at the floor, his shoulders shaking."

    boy_ald_spa  "Mam, I-I… *crying*"
    girl_ald_spa "Please, ma'am. He didn't mean it. We'll do better, I promise— *sniffling*"
    noblewoman   "Cry and beg all you want! You'll both be weeping when they tie the noose around your heads!"

    "The boy's shoulders shake, silent sobs wracking his small frame. The girl clutches his arm, her tears falling onto the already-damp floor."

    dorian "…"

    # -----------------------------------------------------------------------
    # D2-C SUB-CHOICE: Do Nothing or Punish the Noblewoman
    # PDF p74-75
    # -----------------------------------------------------------------------

    menu:

        "Do nothing.":
            $ ch2_spa_choice = "nothing"

            # PDF p74-75
            "I turn away, forcing my gaze back to the warm pools and the pampered nobles. The boy's muffled sobs and the girl's quiet pleading fade into the background as I try to block it all out."

            vasily "Come on. Let's get out of here."
            dorian "…"

            boy_ald_spa "Mam, please. We'll do anything… Please! *crying*"
            noblewoman  "Get your filthy hands off my feet! Come dawn, you'll hang like the worthless scum you are. And I'll laugh as your bodies sway in the wind."

            dorian "Scum…"

            "I force myself to walk away."

        "Punish the noblewoman.":
            $ ch2_spa_choice = "punish"

            # PDF p75
            "I close my eyes briefly, channeling the energy deep within me. The ground beneath her feet shifts silently, imperceptibly."
            "She doesn't even notice."

            play sound sfx_ground_swallow       # PLACEHOLDER — earth swallow SFX

            noblewoman "AAHHHHH!!!!"

            "As she steps back, the marble tiles give way. A small, perfect hole opens beneath her. She gasps, but no sound escapes as the ground swallows her whole. The hole seals as quickly as it appeared, leaving nothing behind."

            # CG: noblewoman being swallowed by the earth
            scene cg_noblewoman_swallowed with shock_cut  # PLACEHOLDER — cg_noblewoman_swallowed
            pause 0.5
            scene bg_mjoll_spa with dissolve

            "The children stare at the empty space, confused."

            vasily "Merciful Enoch…"
            vasily "Dorian… what did you just do? What happened to the noblewoman?"

            "I walk away."

            dorian "Like I said, Vasily, I don't care."

    # Both sub-choices converge — PDF p75-76
    "We step out of the spa, the cold air biting at my skin, a stark contrast to the warmth we just left behind."
    "My interest in the place has completely faded."

    dorian "Maybe we should try someplace else."

    "Vasily glances at me, his expression unreadable for a moment, before giving a small nod."

    vasily "Fair enough. Let's see the other booths."

    return


# -----------------------------------------------------------------------------
# D2-D: REST WITH VASILY
# PDF pages 76-77.
# A quiet moment. Vasily naps.
# -----------------------------------------------------------------------------

label ch2_rest:

    # PDF p76
    # [COMMENT: bg_mjoll_pavilion — cushioned seats, fur-lined blankets, canopy, tucked from noise]
    scene bg_mjoll_pavilion with dissolve       # PLACEHOLDER — quiet canopied pavilion

    "I glance at Vasily, raising an eyebrow as I gesture to a small, shaded pavilion tucked away in the corner of the square."
    "It's a simple structure—a cozy area reserved for the royal advisor to escape the noise and chaos. Cushioned seats and thick, fur-lined blankets are arranged beneath the canopy."

    dorian "You keep telling me I need to relax. Why don't you take your own advice for once?"

    vasily "Relax? In the middle of the square? You must be joking."
    dorian "You have your own private area over there. No one will bother us. You look like you haven't slept in days, Vasily."

    "He scoffs, rubbing his temples. After a moment of hesitation, he nods."

    vasily "Fine. But only for a little while. If King Gustav sees me slacking, he might have my head."

    "We make our way to the pavilion, and Vasily settles into one of the cushioned seats, stretching his legs out. I take a spot beside him, leaning back against a pillow."
    "For a brief moment, it feels... peaceful. The noise of the square fades into a dull hum, distant and unimportant. The sun filters through the canopy above, its warmth battling the cold, snowy air."

    vasily "You know, I can't remember the last time I did this. Just... sat down without thinking about the next task, the next problem."

    "I close my eyes, letting the rare stillness seep into my bones."

    dorian "You know the king. He never stops bitc—"
    vasily "And you never stop brooding."

    "The silence stretches between us. I catch Vasily dozing off, his head tilting to one side. He mutters something incoherent before settling into a deeper sleep."

    vasily "Zzzzz…"

    pause 2.0

    # PDF p77
    "An hour goes by and I wake Vasily up. He stretches and glances at me, the faintest hint of a smile on his face."

    vasily "Alright, Dorian. I'll admit it—you were right. I needed that."
    dorian "Told ya."

    "He pauses."

    vasily "You, too, though. You looked... at peace, for once."
    dorian "I agree. Rest is a moment I don't take for granted."

    return


# =============================================================================
# SECTION 11: LABEL CH2_COMMON_FREETIME — Free Time Convergence
# =============================================================================
# PDF page 77.
# All four free time options converge here.
# =============================================================================

label ch2_common_freetime:

    # PDF p77
    # [COMMENT: bg_mjoll_square_festive — full crowd gathered, Qiongqi head on pedestal, banners]
    scene bg_mjoll_square_festive with dissolve # PLACEHOLDER — Mjoll square, full celebration
    play music ost_mjoll_festive volume 0.8     # PLACEHOLDER — festive theme at full volume
    play audio amb_crowd_festive loop fadein 1.5 # PLACEHOLDER — crowd ambient loop

    "It's time for the celebration."
    "As Vasily and I approached the grand setup in the square, the energy was palpable. The monster's severed head was proudly displayed atop a gilded pedestal, its grotesque features preserved and amplified for all to see."
    "A crowd had already gathered, their murmurs of excitement growing louder with every passing moment. The sound of children laughing, merchants yelling, and performers playing instruments filled the air."

    vasily "There it is. Your hard work on full display. The people will talk about this for years. They'll honor you in the grand Mjollian tradition. It's my favorite part of these ceremonies."
    dorian "*yawns* I wanted to go back to sleep."
    vasily "You'll get more sleep AFTER the ceremony."
    dorian "Besides, didn't you help bringing down that thing? We also had three other soldiers with us. Helga, Lars… And, I forgot the name of the last one."
    vasily "Pavel. His name's Pavel, I believe."

    "The crowd roared in approval as a herald stepped forward to announce the event. My recognition was grand, as Vasily predicted. I could hear murmurs and shouts of my name from the crowd."

    # show herald proud at center                # PLACEHOLDER — Herald sprite

    herald "People of Mjoll! We gather today to honor the Dragon of Gale, the hero who has slain the Qiongqi that terrorized our kingdom!"

    "The applause was thunderous. But I had no desire for recognition, no joy in the spectacle."

    jump ch2_ceremony


# =============================================================================
# SECTION 12: LABEL CH2_CEREMONY — Dunking Ceremony (D1)
# =============================================================================
# PDF pages 77-81.
# D1: Aim dead center (Svante dunked) or Pretend to miss (+svante_affection)
# =============================================================================

label ch2_ceremony:

    # PDF p78
    "Then my gaze shifted, and I saw it: a large setup on the other side of the square. A series of dunk tanks, each elevated on a platform, filled with freezing water with stalagmites. Above each tank, an aldorith was tied to a precarious seat, their faces pale from the cold."

    # show svante dunk_seat at center            # PLACEHOLDER — Svante sprite (tied to dunk seat, defiant)
    # show kristin frightened at left            # PLACEHOLDER — Kristin sprite (shaking)

    svante       "…"
    boy_ald      "…"
    kristin      "…"

    vasily "Ah… my favorite tradition. The dunk tanks."
    dorian "Favorite?"

    "The man with the violet hair was a standout. His shirt was thin and tattered, barely enough to protect him from the biting wind. The others— a younger girl with silver hair, a gaunt boy, and a frail woman—were dressed similarly, their clothes little more than rags."

    herald "To mark this grand occasion, we begin with the traditional dunking! And as is custom, the guest of honor shall have the first dunk!"
    herald "And as is custom, the guest of honor shall have the first dunk! Only the Dragon of Gale himself will claim this honor! After which, the dunk will be open to the public!"

    "The crowd erupted into cheers, and my fists clenched at my sides."

    "Man 1: I can't wait to see that violet-haired freak drown!"
    "Woman 2: Dunk them all! Teach those mutts their place!"

    kristin "*cries* They're… they're so cruel…"
    svante  "Hey, Kristin. Don't cry. You're making it easier for them."

    "The herald pointed dramatically at the violet-haired aldorith."

    herald "And for our first dunk, we have Svante—the metal channeling aldorith! Dragon of Gale, the first throw is yours!"

    "I glanced up at Svante. He met my gaze with his piercing violet eyes."

    svante "Of course it's me…"

    "A younger aldorith, a girl with silver hair, whispered frantically to him."

    kristin "Svante, brother, please. Don't provoke them. We—"

    "The words barely left her mouth before a guard struck her with the blunt end of his spear."

    kristin "Ahhh!!"
    svante  "Hey! Don't lay a finger on her! I swear—"

    "Another slap from the guard silenced him, followed by a harsh blow to his stomach. Svante doubled over, coughing violently as the crowd cheered."

    svante "*coughs*"

    # PDF p79
    male_guard "Shut up, lowlife."
    "Male 3: Yeah! Show that worthless mutt his place!"
    male_guard "Wanna beg for my forgiveness?"

    kristin "Svante, please!"
    svante  "*coughs* I… I'm sorry."

    "The guard grabbed Svante by his collar, forcing him upright to face me."

    male_guard "I hope you like ice water, freak. After this, you and your siblings are done for. The Dragon of Gale will see to it."

    "The crowd roared again as Vasily stepped beside me, a smirk tugging at his lips. He is holding out a ball."

    vasily "Here. It's Mjollian tradition, my friend. It's just a dunk tank, after all. The water's only cold if you let yourself feel it. They're only aldoriths. Filthy mutts."

    herald "Come now, Dragon of Gale. It's tradition. Show us your strength and honor by taking the first shot. The people are watching!"

    "I looked back at Svante, his violet eyes meeting mine. His expression was unreadable. He looks down, defeated."

    svante "…"
    dorian "…"
    svante "Just do it. Get it over with."

    "The crowd jeered, their shouts urging me to take the shot. Vasily stood beside me."

    play sound sfx_heartbeat loop               # Tension SFX during the choice

    # -----------------------------------------------------------------------
    # D1 DECISION — Aim Dead Center or Pretend to Miss
    # PDF p79-81
    # -----------------------------------------------------------------------

    menu:

        "Aim dead center.":
            $ ch2_dunk_choice = "aimed"
            stop sound

            # PDF p80
            "I raised my arm and aimed straight for the target. The crowd hushed as they watched, anticipation thick in the air. With one swift motion, I threw the ball."
            "The target hit dead center, and the mechanism released."

            play sound sfx_dunk_splash          # PLACEHOLDER — dunk splash SFX

            # CG: Svante plunging into the icy tank
            scene cg_svante_dunk_in with shock_cut  # PLACEHOLDER — cg_svante_dunk_in
            pause 0.8
            scene bg_mjoll_square_festive with dissolve

            svante "*panting*"

            "The crowd roared with laughter."

            kristin "B-Brother!"
            "Man 3: Look at him squirm!"
            "Woman 2: Bet he wishes he wasn't born now!"

            "I stepped back, my face blank. Vasily clapped me on the back, his laughter blending in with the crowd."

            vasily "Haha! Look at that wet mutt! Great job, friend!"

        "Pretend to miss the shot.":
            $ ch2_dunk_choice = "missed"
            $ svante_affection += 1             # +1 Svante affection tracker
            stop sound

            # PDF p80
            "I raised my arm, aimed, and threw the ball—but it went wide, striking the wood of the tank instead. The crowd groaned in disappointment, their laughter fading into murmurs."

            # CG: ball striking the wood — Svante's stunned expression
            scene cg_svante_spared with dissolve  # PLACEHOLDER — cg_svante_spared
            pause 0.8
            scene bg_mjoll_square_festive with dissolve

            herald "A miss? Well, no matter! The Dragon of Gale may try again!"

            dorian "I won't throw another."
            herald "But it's tradition! The dunking cannot proceed without the first shot!"
            dorian "Then there will be no dunking."

            "The crowd booed, their shouts becoming increasingly hostile. Vasily looked at me, his face an odd mix of amusement and disbelief."

            vasily "You really know how to ruin a celebration, Dorian. This is Mjollian culture."

            "I ignored him and turned away, my eyes meeting Svante's for a brief moment."

            svante "I… t-thank you… I—"

            male_guard "Shut up, all of you, mutts!"

            # PDF p81
            kristin "Brother!"
            svante  "Kristin!"
            "Boy aldorith: Wait, so does that mean…"
            svante  "Thank you…"

            "Svante, though shivering, straightened his posture slightly, his violet eyes locked onto me until he is escorted out by the guards."

            herald "Well… There you have it, folks. No first shot has been made. For the first time ever, we will be cancelling today's dunking festivities."

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

    # PDF p81
    "The ground beneath us trembled violently, cutting through the crowd's laughter like a blade. The quake was sudden, jolting everyone out of their revelry."

    "Man 3: Ahhh!!"

    "The herald stumbled forward, gripping the edge of the dunk tank for support, his face pale with terror."

    herald "What… what is happening?!"

    "Before anyone could answer, a bone-chilling wind swept through the square. The air seemed to freeze in place, heavy and sharp like needles against the skin. Then, out of the frost-laden mist, they appeared."

    play sound sfx_ice_crack                    # PLACEHOLDER — ice crack SFX

    # CG: Frost Oni emerging from the mist
    scene cg_frost_oni_entrance with shock_cut  # PLACEHOLDER — cg_frost_oni_entrance
    pause 1.0
    scene bg_mjoll_square_battle with dissolve  # PLACEHOLDER — square mid-battle bg

    play music ost_frost_oni_battle fadein 0.5  # PLACEHOLDER — Frost Oni battle theme

    "Towering figures, their forms jagged and crystalline, emerged from the haze. Beings of ice, emanating an eerie glow. Long, flowing tendrils of frost extended from their limbs, crackling as they moved. They carried weapons of ice—curved swords and long spears."

    frost_oni "*Crackling sounds*"

    "Man 2: W-What are those things?!"
    "Woman 1: D-Demons! Demons!"

    "Without warning, one of them raised its spear and hurled it into the crowd. It struck a man through the chest, freezing him solid where he stood."
    "Another slashed its blade across a fleeing woman, leaving behind a trail of ice that consumed her body in seconds."

    "Woman 1: Ahhh!!"
    "Man 3: Run!! Run!!"

    # PDF p82
    "The herald tried to regain control, his voice breaking as he shouted."

    herald "Remain calm! Guards, come quick! P-Protect—"

    "An ice being surged forward, impaling him with its spear."

    herald "Ahhh!! *dying sounds*"

    "His words died in his throat, his body encased in frost before shattering into pieces."

    frost_oni "Graaaaa!!"

    "The dunk tank was their next target. One of the creatures slammed its massive fist against the frame, shattering it instantly. The water inside spilled out, freezing as it hit the ground. The aldoriths screamed, scattering as the ice beings turned their attention to them."

    kristin "Brother! Svante! Run!"
    svante  "Let's get out of here, Kristin!"

    "I could see him hesitate, his fists clenching, but he eventually turned and fled with the others."

    vasily "What in Tetrad's name are these?"
    dorian "I don't know."

    "I raised my hands, channeling earth and wind. The ground around me shifted, sharp pillars of stone erupting to block the ice beings' path. I followed up with a gust of wind, sending shards of debris flying toward them."

    play sound sfx_earth_spike                  # PLACEHOLDER — earth spike SFX

    vasily "Dorian, we need to keep them away from the civilians!"

    "The ice beings seemed unfazed by the wind and stone at first, their bodies regenerating as frost crept over the damage. I clenched my fists, slamming a foot into the ground to create another barrier of earth between them and the survivors."
    "One of the creatures turned its glowing eyes on me, its spear raised to strike. Vasily stepped forward, blasting it with a beam of light magic. The creature stumbled back, cracks forming in its icy surface."

    vasily "They're not invincible! Dorian, we need to hit them harder!"

    "I nodded, summoning a whirlwind of debris and stone to batter another creature. The crowd was in chaos, but some of the people were starting to flee toward safety."
    "The ice beings let out a bone-chilling screech, their forms twisting as they began to converge on us. My heart pounded, but I stood my ground."

    frost_oni "Graaaaa!!"

    # PDF p82-83
    "One of the creatures ran towards me, its icy breath misting the air as it raised its massive spear toward me. It would be difficult for me to physically dodge the spear."

    play sound sfx_heartbeat loop

    # =====================================================================
    # D4 — TIMED QTC: Frost Spear (wind = safe / dodge = +ICE)
    # PDF p83
    # =====================================================================

    menu:

        "Use wind to deflect the spear.":          # CORRECT — no ICE
            $ ch2_qtc4 = "wind"
            stop sound

            play sound sfx_wind_blast           # PLACEHOLDER

            "I summoned a powerful gust of wind just in time, the spear flying off course and shattering against the ground. The ice being let out an enraged screech, its glowing eyes locked on me."

            frost_oni "Graaaaa!!"

        "Dodge to the side.":                      # WRONG — +1 ICE
            $ ch2_qtc4 = "dodge"
            $ ice_tracker += 1
            stop sound

            "I tried to move, but the spear grazed my side, leaving a sharp, stinging pain as frost crept along the wound."

            dorian "Ahhh!!"
            vasily "Dorian!"
            frost_oni "Graaaaa!!"

    # D4 converge — second creature attacks — PDF p83
    play sound sfx_heartbeat loop

    "Another creature surged forward, its clawed hand reaching for Vasily. He fired a beam of light magic, but it was too fast, dodging the attack. Its focus turned to me."

    frost_oni "Graaaaa!"
    vasily    "Dorian! It's after you!"

    # =====================================================================
    # D5 — TIMED QTC: Ice Claws (wind = +ICE / earthen wall = safe)
    # PDF p83-84
    # =====================================================================

    menu:

        "Try to blast it with wind to push it back.":  # WRONG — +1 ICE
            $ ch2_qtc5 = "wind"
            $ ice_tracker += 1
            stop sound

            "I sent a gust of wind toward it, but it barely slowed the creature down. Its icy claws raked across my arm, freezing my flesh. I bit back a scream, but the pain was almost too much."

            dorian "Ahhh!! Crap!!"
            vasily "Dorian!!"

            "Vasily launched a blast of light towards the being, shattering it completely."

        "Raise an earthen wall to block its path.":    # CORRECT — no ICE
            $ ch2_qtc5 = "wall"
            stop sound

            play sound sfx_earth_spike          # PLACEHOLDER

            "I slammed my hands to the ground, channeling the earth to rise in a jagged wall between us. The creature collided with it, shards of ice breaking off its body."

            vasily "Take this!"

            "Vasily fired another blast, shattering part of its torso."

    # D5 converge — the last Frost Oni — PDF p84
    play sound sfx_heartbeat loop

    "The last ice being stood in the middle of the square, frost swirling around it as it prepared a devastating attack. A frost cloud. I could feel the temperature drop further, the cold biting into my very core."

    vasily "Brr… It's getting colder…"

    # show babala at right with dissolve         # PLACEHOLDER — Babala sprite (hobbling in)

    babala "Hey! Do you boys need some help? I can help you!"

    # =====================================================================
    # D6 — TIMED QTC: Frost Cloud (wind + Babala = safe / earth spike = +ICE)
    # If ice_tracker >= 2 after wrong answer -> GAME OVER
    # PDF p84-85
    # =====================================================================

    menu:

        "Use wind to disperse the frost before it gathers. Allow Babala to help.":  # CORRECT — no ICE
            $ ch2_qtc6 = "wind_babala"
            stop sound

            play sound sfx_wind_blast           # PLACEHOLDER

            "I called on the wind, forcing it into a violent cyclone that tore through the frost cloud. The creature let out a shriek of frustration as its attack dissipated, leaving it vulnerable."

            dorian "Now!"
            babala "*gibberish* Taste the wrath of the Weaver!"

            play sound sfx_vine_attack          # PLACEHOLDER — vine attack SFX

            "All of a sudden, vines surrounded the ice being and smashed it on its vulnerable spot."

            vasily "Wow."
            babala "You're welcome, Dragon."

        "Channel earth to create a spike and impale it. Don't allow her.":   # WRONG — +1 ICE
            $ ch2_qtc6 = "spike"
            $ ice_tracker += 1
            stop sound

            "I tried to channel the earth beneath it, but my footing slipped on the icy ground. The frost cloud thickened, and the creature unleashed its attack, shards of ice ripping through the square."

            dorian "Gaaah!"
            babala "Dragon!"

    # -----------------------------------------------------------------------
    # POST-QTC CONVERGENCE — ICE CHECK
    # PDF p85
    # -----------------------------------------------------------------------

    if ice_tracker >= 2:

        # GAME OVER — Dorian is frozen solid
        stop music fadeout 1.0
        stop sound

        vasily "D-Dorian! Your skin!"
        dorian "C-Cold…"

        "I fell to my knees, frost spreading across my body as the ice takes hold of me. The cold consumed me, dragging me into darkness."

        babala "Dragon! No!"
        vasily "Dorian! No! Dorian!"

        jump game_over_freeze

    else:

        # VICTORY — Frost Oni defeated — PDF p85-86
        stop music fadeout 2.0
        stop sound

        "The ice beings were shattered, their remains scattered across the square. Vasily panted beside me, his magic dimming as exhaustion took hold."

        vasily "You did it, Dorian. You saved them… or what's left of them."

        dorian "What are those things?"

        "The guards approached us, their faces pale and frantic. One of them leaned in and whispered something hurriedly to Vasily. His usual calm demeanor cracked as his eyes widened in shock."

        vasily "W-What?! Are you certain? Tetrad above…"

        "The guard nodded, and Vasily swore under his breath. He grabbed a pouch from his belt and thrust it into my hands, his movements rushed."

        vasily "Here. Your payment. I… I need to go. I'll find you later. Stay safe, Dorian."

        "He didn't wait for a reply. Before I could ask what was wrong, he spun on his heel and bolted toward the castle, the guards following closely behind. I stood there, clutching the pouch."

        # PDF p86
        "The remaining guards approached cautiously, inspecting the shattered remnants of the ice beings scattered across the bloodied square."

        babala "This… This is no ordinary attack. The Weaver's threads are tightening around us."

        "She bent low to inspect one of the larger shards of ice, her fingers brushing the jagged surface. A faint glow pulsed under her touch."

        babala "Yes… the pieces of the Weaver's plan are in motion. You, Dragon of Gale, must steel yourself. For the storms that come will not spare anyone—not kings, not queens, not even you."

        dorian "The Weaver? What does this have to do with the gods?"
        babala "You will find out in due time. For now, my work for you is already done."

        "She straightened—well, as much as her hunched back would allow—and let out a dry, croaking laugh. Then, as she turned to shuffle away, her back cracked audibly."

        babala "Ahhh!"
        dorian "A-Are you alright?"

        "She waved me off, scowling."

        babala "Tch! Damned Weaver and your threads! Snagged me good, you meddling hag!"

        "She spat on the ground, muttering curses under her breath."
        "She shuffled back toward her tent, her curses growing louder with each step. The guards gave her a wide berth, whispering among themselves."
        "I watched her go, a strange unease settling in my chest."
        "I looked back at the shattered remains of the ice beings, their glow still faintly pulsing in the twilight."

        dorian "What are these monsters?"

        jump ch2_common_end


# =============================================================================
# SECTION 14: LABEL game_over_freeze — Shared GAME OVER (ICE Freeze)
# =============================================================================
# Only reached from the Frost Oni ICE tracker check.
# PDF page 85.
# =============================================================================

label game_over_freeze:

    scene cg_dorian_frozen with fade            # PLACEHOLDER — cg_dorian_frozen (frost spreading)
    stop music fadeout 1.0
    stop audio

    pause 1.5

    "The cold consumed everything."
    "And then — nothing."

    pause 2.0

    scene cg_black with fade                    # PLACEHOLDER — pure black

    pause 1.0

    "Reload your last save and take fewer hits from the Frost Oni."

    pause 1.0

    return   # Returns to Ren'Py main menu


# =============================================================================
# SECTION 15: LABEL CH2_COMMON_END — Post-Battle / Yuxuan Letter (D3)
# =============================================================================
# PDF pages 86-91.
# =============================================================================

label ch2_common_end:

    # -------------------------------------------------------------------------
    # TIME SKIP — Several days pass
    # PDF p86-87
    # -------------------------------------------------------------------------

    scene cg_black with fade                    # PLACEHOLDER — black transition

    pause 1.0

    # PDF p86
    # [COMMENT: bg_mjoll_square_blizzard — abandoned square, snow-covered, eerie silence]
    scene bg_mjoll_square_blizzard with fade    # PLACEHOLDER — abandoned snowy square

    play music ost_blizzard_days fadein 3.0     # PLACEHOLDER — desolate days-after theme
    play audio amb_mjoll_wind loop fadein 2.0   # PLACEHOLDER — wind ambient

    "The days passed in a haze. Five, maybe six—I've lost count."
    "The silence from the castle stretched on, unnerving in its emptiness. No Vasily, no summons, no word. Not even a whisper of gold. Only rumors and idle gossip."

    # PDF p87
    "They said the ice creatures had come from inside the castle. From someone within. I didn't care. Let them chase their shadows and whisper their theories. It wasn't my concern. My only concern was survival—and, when I could afford it, distraction."

    # [COMMENT: bg_mjoll_square_blizzard — snow falling heavier than before, vendors complaining]
    "The biting chill nipped at my skin as I trudged back to my cave. Strangely, the snow was falling heavier than before these past few days."
    "The cold didn't bother me much—it never had. Maybe it was the fire channeling power coursing through me. But for some people, according to the vendors, it's become unbearable."
    "The pouch of gold Vasily had thrust into my hands days ago had been spent sparingly, stretched to buy food and small comforts."

    scene bg_mjoll_cave_night with dissolve     # PLACEHOLDER — cave at night, fire low

    stop audio fadeout 1.0
    play audio amb_cave_fire loop fadein 2.0    # PLACEHOLDER — fire crackle ambient

    # [COMMENT: the fire crackled softly]
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

    # PDF p87-88
    "It was an elegant thing, crisp and ivory-colored, sealed with an intricate red-and-gold emblem. There was a mark with a picture of a girl and the words: Cheng Industries."
    "The Tianho seal gleamed faintly in the dim light, the dragon motif coiled with clouds and lotus blossoms."

    # CG: the Cheng Industries letter — ivory envelope, embossed emblem
    scene cg_yuxuan_letter with dissolve        # PLACEHOLDER — cg_yuxuan_letter
    pause 1.5
    scene bg_mjoll_cave_night with dissolve     # Return to cave

    "I turned the envelope over, running my fingers across the embossed edges before opening it carefully."
    "Inside was a letter, written in neat, flowing characters."

    # PDF p88-89 — Yuxuan's letter read as narration blocks
    "Dearest Paladin Dorian,"
    "I hope this letter finds you well, though I fear it may be too long since we last spoke. I often think of the day you saved me from the tragedy that befell Tianho. Without your bravery, I would not be alive to write these words today. For that, I am eternally grateful. For the Prosperity Dragon, and to you."
    "Word has reached me that you were seen in Mjoll, alive and—dare I hope—well. Knowing this fills my heart with relief. You've been on my mind these past years, and I've often wondered how you've managed, given the burdens you carry."
    "Please, do not hesitate to reach out if ever you are in need of anything. Cheng Industries owes you a debt that cannot be repaid with gold alone. Your kindness and courage have left an indelible mark on my life."
    "If you are interested, I would like to invite you to have tea with me. The city may have changed, but my doors will always remain open to you. Perhaps I can repay a fraction of what you have given me, even if it's only with the comfort of good tea and company."
    "Prosperity Dragon willing, we will see again."
    "With deepest gratitude and fondness, Cheng Yuxuan."

    dorian "Yuxuan… Cheng Yuxuan… I don't recall anyone with that name."

    # PDF p89
    "The name didn't immediately strike a chord, but I felt like I heard it from somewhere before."

    elara  "You saved him from the fire, remember?"
    daniel "Yeah! Remember when you lifted that beam like it was nothing? It was so cool!"

    "I closed my eyes, the image of Tianho's flames flashing behind my eyelids. The man I saved from the burning building."
    "I sighed, folding the letter carefully and setting it aside."

    elara  "You should write back to him."
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

    # PDF p90
    "I reached for the old pen Vasily had given me weeks ago and pulled out a sheet of parchment. Sitting down at the rickety wooden table, the glow of the fire flickering on the cave walls, I dipped the pen in ink. What should I write, though?"

    # =========================================================================
    # D3 — WRITE BACK TO YUXUAN: Warm or Distant response
    # PDF p90
    # =========================================================================

    menu:

        "Write a warm response.":
            $ ch2_letter_choice = "warm"
            $ yuxuan_affection += 1             # +1 Yuxuan affection tracker

            "I sat for a moment, letting my memories of that night in Tianho run my hand. The ink bottle was nearly empty, but I managed to write carefully:"

            "Cheng Yuxuan,"
            "It's great to know that the life I saved has grown into such a kind and successful soul. I would be honored to have tea with you and see how you've rebuilt your life. Perhaps we can trade stories—I have a few to tell myself. Thank you for your thoughtful letter. It means more to me than you know."
            "Dorian Burnham"

            "Lastly, I placed the address written on Yuxuan's letter. When I finished, I let the ink dry."

            dorian "There. Happy?"
            elara  "Once you send it to the postman, I'll be very happy."

        "Write a distant response.":
            $ ch2_letter_choice = "distant"

            "The fire crackled as I sat at the table, the pen feeling heavy in my hand. I stared at the parchment for a long moment before scrawling a short reply in quick, precise strokes."

            "Cheng Yuxuan,"
            "I am glad to hear you are doing well. I don't have time for travel at the moment. Best of luck to you in Tianho."

            dorian "There. Happy?"
            sarah  "Dad, that's such a cold letter."
            lucas  "Even colder than this weather!"
            elara  "How are you supposed to make new friends if you write like that?"

            "I groaned, grabbing the letter again. With a grumble, I scratched out 'don't' in the second sentence, leaving a messy strikethrough."

            dorian "There. I fixed it. Happy?"
            elara  "You're impossible, you know that?"

    # -----------------------------------------------------------------------
    # Both letter choices converge — PDF p91
    # -----------------------------------------------------------------------

    "I folded the letter and tucked it into my pocket. I'd deliver it when I made my next trip into the city."
    "As I turned back to the warmth of the fire, I heard it—a voice calling for me from outside the cave. It was sharp, urgent."

    # show messenger urgent at right             # PLACEHOLDER — Messenger sprite (out of breath)

    messenger "Paladin Dorian! Are you there? Paladin?"

    "I stood, brushing my hands against my tunic before stepping outside. A young messenger, dressed in the livery of Mjoll, stood at the edge of the rocky path leading to my home. His face was pale, his breathing uneven from the climb."

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
# PDF pages 91-99.
# =============================================================================

label ch2_castle_briefing:

    # PDF p91
    # [COMMENT: bg_mjoll_palace_hall — aldoriths huddled, gearing up for battle, torches low]
    scene bg_mjoll_palace_hall with fade        # PLACEHOLDER — palace inner hall, aldoriths gearing up
    play music ost_briefing fadein 2.0          # PLACEHOLDER — tense briefing theme

    "The howl of the snowstorm seemed alive, its icy fingers clawing at us even as we slammed the heavy doors shut behind us."

    messenger "C-C-Cold… Cold…"
    dorian    "Are you alright? Are you still cold?"
    messenger "A l-little.."

    "Inside, the warmth of the Mjoll Castle did little to shake the lingering chill. My boots echoed on the stone floor as I took in the sight before me."
    "A group of aldoriths stood huddled in the grand hall, their faces pale and determined. They were gearing up for battle, strapping on mismatched armor and whispering to one another in low, urgent tones."
    "Some glanced at me briefly, but their eyes quickly darted away. They had no love for me, nor I for them."

    # PDF p92
    "Girl aldorith: Have you heard of the death toll? Enoch above…"
    "Boy aldorith: I know… But we don't have a choice."

    messenger "Paladin… Count Vasily is over there. If you'll excuse me, I'll—"
    dorian    "Wait—"

    "I pulled the folded letter from my pocket and handed him a few coins."

    dorian "Please take this to Cheng Yuxuan."

    "The young man nodded, his face still flushed from the cold. Without another word, he bolted back out into the storm."

    "My eyes moved across the room until they landed on Vasily. He stood to the side, leaning heavily on a table, surrounded by three hooded figures draped in deep gray robes—the unmistakable attire of the prophets of the death god."
    "Vasily looked terrible. His face was gaunt, and a dark bruise marred his left eye, swelling the skin around it."
    "The prophets were whispering among themselves, their voices carrying just enough for me to listen to them."

    # show vasily bruised at center              # PLACEHOLDER — Vasily sprite (bruised, gaunt)
    # show niko hooded at right                  # PLACEHOLDER — Niko sprite (hooded prophet)
    # show svante grim at left                   # PLACEHOLDER — Svante sprite (grim, resolute)

    "Prophet 1: The cold is unbearable… the prince must have made a pact with the death god to gain this much power."
    "Prophet 2: I disagree. It's unnatural. Not even the Enoch's touch could twist the elements this way."

    niko "You lack faith, brothers. It is obvious that Enoch's hand is all over this—"

    vasily "Enough. Give me a moment."

    "Vasily straightened when he noticed me approaching, though the movement seemed to pain him. He waved the prophets away with a curt gesture."

    dorian "What in Tetrad's name happened to you?"
    vasily "You've seen what's happening outside. It's getting colder by the minute."
    dorian "I meant your face, Vasily."

    "He rubbed a hand over his face, wincing as his fingers brushed the bruise."

    # PDF p93
    vasily "It's from the king. It's unimportant."

    "The fire in the hearth sputtered as the storm outside roared with a deafening fury. He leaned on the table, his knuckles white from the strain."

    vasily "The storm won't let up, Dorian. It's relentless. Crops have failed, the rivers are freezing over, and entire villages are being swallowed by snow."

    "His voice cracked slightly."

    vasily "The kingdom is falling apart. Trade routes are blocked. Supplies can't get through. We've already lost half of our militia to hypothermia trying to secure the roads."

    "I clenched my fists, the weight of his words settling like a stone in my chest."

    dorian "And no one knows what's causing it?"

    vasily "There's a theory."

    "He turned toward the hooded prophets of the death god. One's face was familiar… yet I could not recall."

    "Prophet: This storm is no mere act of nature. It reeks of the energies of the death god. We have felt this power before... during the Tragedy of Tianho."

    "The mention of Tianho sent a chill down my spine. Elara. The kids."

    niko "The death god's power lingers, though it is not as strong as it once was. Its source is concentrated in a desolate place west of here. An abandoned mine known as Frostcradle."

    dorian "The Tragedy of Tianho? You're saying this storm is connected to that?"

    "The man nodded; his eyes gleaming."

    niko "The energies are unmistakable. Whatever caused the tragedy there has resurfaced. Weaker, yes, but still potent enough to wreak havoc."

    vasily "We sent aldoriths to investigate. None of them came back alive."

    "He gestured toward the crowd of aldoriths huddled in the hall. One figure stood apart, his violet hair unmistakable. I think I've seen him before."

    svante "I... I saw what happened to them. My brothers, my sisters... they went west, into that cursed place. When they didn't return, I volunteered to go after them."

    "He paused, his voice trembling as he continued."

    # PDF p93-94
    svante "They were impaled with ice. That's not all… their bodies were frozen solid. Twisted. The cold... it didn't just kill them. It consumed them."

    "He swallowed hard, his violet eyes glistening."

    svante "T-They… They were my family…"

    "The room was heavy with silence. Even the prophets seemed subdued. Vasily's voice cut through the tension."

    # PDF p94
    vasily "That's why we're asking you, Dorian. You're not just a warrior—you're the Dragon of Gale. If anyone can survive this... it's you."

    "I stared at him, my jaw tightening."

    dorian "What's the mission?"

    "Vasily's gaze darkened, and for a moment, he hesitated."

    vasily "You're to go west, to the Frostcradle. To the source of the storm. And once you're there…"
    vasily "You are to kill the Prince Elias Drakos."

    dorian "Fine. But I want to be paid upfront."

    "Vasily didn't hesitate. He smiled and snapped his fingers with crisp authority. Svante reached to his belt, unclipping a leather pouch heavy with coin. It clinked as he approached, the weight unmistakable."

    vasily "We don't usually pay upfront, but given the urgency—and our past dealings—I'll make an exception."

    svante "T-T-Three thousand gold pieces. For killing Prince Elias Drakos, sir."

    "I took the pouch, feeling the satisfying heft of it before slipping it into my pocket. The room remained quiet, save for the occasional hiss of the fire."

    dorian "I have questions."
    vasily "Ask. But make it quick. Time isn't on our side."

    jump ch2_questions


# =============================================================================
# SECTION 17: LABEL CH2_QUESTIONS — Optional Questions to Vasily
# =============================================================================
# PDF pages 94-99.
# Player can ask 3 optional questions before accepting the mission.
# All paths converge on ch2_end.
# =============================================================================

label ch2_questions:

    menu:

        "Where's the king and queen?":

            # PDF p94-96
            "I glanced around the hall, my eyes drawn to the twin thrones at the head of the room. Both were empty, their gilded frames casting long shadows in the dim light."

            dorian "Where's King Gustav?"

            "Vasily's face darkened at the question, his lips pressing into a thin line."

            vasily "The king is… indisposed. He's in his chambers, mourning."

            "His voice was tight, as though every word cost him. I noticed the way his hand trembled slightly as he spoke."

            dorian "And the queen? What of Queen Ekaterina?"

            vasily "?!"

            "At that, Vasily froze. His shoulders stiffened, and a flicker of pain crossed his eyes. For a moment, he didn't answer, but Svante, standing nearby, stepped forward, his face grim."

            svante "She's dead, sir."

            "The words hung heavy in the air, like a stone dropped into a silent pond."

            dorian "What?!"

            svante "We found her in her chambers... with a knife in her heart. Father saw everything."

            # PDF p95
            "I stared at him, my mind struggling to process the words. Queen Ekaterina, dead? It didn't feel real. The room felt colder. I clenched my fists."

            niko "Elias killed her. Stabbed her in the heart like the heartless bastard he is."

            "I blinked, trying to process what I'd just heard. King Gustav and Queen Ekaterina. They'd always been there—fixtures of my early missions, handing me my rewards with smiles I'd never trusted but had grown used to."
            "I didn't care about them, not really, but the idea of her being gone was unsettling in a way I couldn't quite shake."

            dorian "I don't… I don't understand. The queen is dead? When did this happen?"

            vasily "During the ceremony. When those… beings appeared."

            "Beings of ice. The ones that disrupted the ceremony. I remember."

            vasily "We couldn't even do the funeral because of the trade routes."
            dorian "Trade routes?"
            vasily "Her final wish was to be buried in Hinami. A water burial. But the frozen routes make it impossible to transport her body there."

            dorian "A Hinami burial? I didn't know Queen Ekaterina had Hinami blood."
            vasily "She did. Only a trace, but enough that she wanted to honor their traditions in death."

            "Queen Ekaterina has Hinami blood… Who knew?"

            # PDF p96
            dorian "Well. I suppose even queens aren't untouchable."

            "Vasily shot me a sharp look, but he didn't argue. Instead, he turned away, his shoulders slumping."

            niko "Do you have any other questions?"

            jump ch2_questions

        "Who's this Elias?":

            # PDF p96
            "Elias. The name wasn't familiar."

            dorian "Who's this Elias? This is the first I've heard of him."

            "Vasily's shoulders tensed, and he let out a heavy sigh."

            vasily "The crown prince of Mjoll. Or rather, the former crown prince of Mjoll."

            "I frowned, confused. In all my four years of working as a mercenary here, I'd never heard of any crown prince."

            dorian "A crown prince? Since when? All I know are the aldoriths who have claim to the throne."

            "Svante, standing nearby, looked down."

            svante "He was the son of Her Majesty, Queen Ekaterina. The true heir to the throne... but not in the eyes of the king. According to Father—"

            "He paused, the words catching in his throat, and his hands clenched into fists at his sides."

            svante "Elias... Elias is a monster. He's the reason my brothers and sisters… *holding back tears*"

            vasily "After the Queen was killed... Elias disappeared. We searched, but there was no trace of him. His flight from the kingdom is as clear an indication of guilt as any."
            vasily "He fled like a coward, leaving his mother's corpse behind."

            "The pain in his voice, raw and jagged, was almost unbearable. I had never seen Vasily this shaken before."

            vasily "The queen's body was found in her solar… crumpled beside her writing desk. A dagger straight through her heart. No signs of struggle. No mercy."
            vasily "Her own son left her there like refuse."
            vasily "The day after that and the cold became unbearable. The blizzard began."

            # PDF p96-97
            svante "The king... Father… he was broken by the queen's death. After that, Elias vanished into the frost, like a shadow… He's the reason the kingdom is falling apart."
            svante "Father… He probably believed in Elias. And he left him with a corpse and a curse. If I could—"
            svante "If I only have the power to brave through this blizzard, I will kill him with my own bare hands!"

            "Prophet: If I may. Me and my prophet brothers can sense the death god's magic in this storm. It's unmistakable."

            niko "All signs point to Elias. The storm, the cursed frost, the powers he's wielding… they all lead back to him. For all we know, he might have sold his soul to Enoch."

            "I couldn't help but feel the chill of dread that crept up my spine. Everything was pointing to the same conclusion—Elias was behind it all."

            vasily "You're the only one who can save us, Dorian."

            jump ch2_questions

        "Can I take some supplies with me?":

            # PDF p97-98
            dorian "I might need supplies if I'm to set out for Frostcradle."

            vasily "I'm afraid supplies are running thin, Dorian. The frost has locked us down tighter than we thought. The roads to Mjoll… they're almost impassable now."

            "He sighed heavily, rubbing his temples."

            vasily "The blizzards are worsening, and the snow is deepening. It's like the very land itself is trying to bury us. We've sent several expeditions out, but none have returned."

            svante "According to the scouts, even the peasants are feeling the cold, sir. It's getting harder to make trades, and even harder to get shipments in."

            vasily "I don't know how much longer we can last with what we have. We've sent requests to the outer regions, but even the merchants are afraid to travel these roads now."

            dorian "…"

            "I frowned. The weight of their situation was clear."

            vasily "The only ones left with any supplies… are the Cheng Industries bots. They've been sending us what they can."

            "I blinked. I think I've heard that name before. Cheng Industries. Yuxuan's company."

            # PDF p97-98 — supply bot arrives
            "As if on cue, a mechanical hum echoed through the hall, and a sleek bot rolled in through the door. It was a little taller than a man, metallic and polished, with a rectangular chest and mechanical arms designed to lift heavy objects."

            niko "Right on cue…"

            # PDF p98
            "The bot's sensors glowed softly as it paused."

            "-Here at Cheng's, we bring change… -"

            "An oddly soothing jingle filled the room, the cheerful tone feeling almost out of place."

            "Supply Bot: Greetings. Supplies delivered—courtesy of Cheng Industries."

            "The bot spun around, unloading several crates of food and supplies with surprising agility. Canned goods, dried meats, and fresh produce packed neatly in the crates, along with a few additional barrels of water."

            svante "Wow. That's… amazing! Do you think they have a robot that talks? I've never seen—"

            vasily "Svante… Did I give you permission to talk about anything other than the incident?"
            svante "N-No, sir. Sorry, Count."
            vasily "Then shut your mouth. One more slip, and I'll have you and whichever aldorith mutt you're closest to flogged for insubordination."
            svante "Yes, sir. I apologize."

            niko "Asshole."

            vasily "What did you just say, Prophet?"
            "Prophet 1: P-Perhaps we can move on, sire."

            vasily "*sighs* As I said, Cheng Industries' bots have been delivering supplies. Only a few shipments, and only what they can carry. It's helping, but it's not enough to sustain us. We can't rely on them forever."

            "He fixed me with a hard stare."

            vasily "You need to find Elias. And end him. Mjoll depends on it."

            "I straightened, meeting his gaze with a nod."

            dorian "Got it."

            jump ch2_questions

        "That's all I need.":

            # PDF p98-99
            "I exhaled sharply, watching my breath curl into the frigid air like smoke."

            dorian "That's enough questions."

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
