###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  FILE:  chapter_04.rpy
#  SCENE: CHAPTER 4 — Aftermath in Mjoll / Chung-hee's POV / Tianho
#
#  CONTENTS:
#    Section 1  — Character Definitions (NEW for Chapter 4)
#    Section 2  — Image Declarations
#    Section 3  — Audio Declarations
#    Section 4  — Game Variables
#    Section 5  — label chapter_4            (Mjoll Palace — aftermath)
#    Section 6  — label ch4_kyeongjang       (Kyeongjang Palace — Chung-hee birthday)
#    Section 7  — label ch4_kyeongjang_night (Kyeongjang Room — amulet / Ji-hye)
#    Section 8  — label ch4_chunghee_qtc     (Timed Choice: What to do with Ji-hye)
#    Section 9  — label ch4_common_1         (Common 1 — Captain Sunwoo arrives)
#    Section 10 — label ch4_common_2         (Common 2 — Chung-hee departs)
#    Section 11 — label ch4_tianho_dorian    (Tianho — Dorian's room, 8 months later)
#    Section 12 — label ch4_cemetery         (Tianho Memorial — graves visit)
#    Section 13 — label ch4_yuxuan_convo     (Waiting for Yuxuan — choices)
#    Section 14 — label ch4_cemetery_exit    (Memorial Gate — chaos begins)
#    Section 15 — label ch4_battlefield      (Empty Battlefield — Chung-hee found)
#    Section 16 — label ch4_niko_raven       (Niko appears as raven / heals Chung-hee)
#    Section 17 — label ch4_svante_capture   (Svante captured / Yuxuan returns)
#    Section 18 — label ch4_tunnel_escape    (Tunnel — escape underground)
#    Section 19 — label ch4_prosperity_dragon (White Screen — Prosperity Dragon)
#    Section 20 — label ch4_bad_end_bomb     (Bad End — bomb)
#    Section 21 — label ch4_draconic_fire    (Common — draconic fire unleashed)
#    Section 22 — label ch4_underground      (Underground — Chapter 5 opening)
#
#  NAMING CONVENTIONS:
#    image tags      — bg_name, cg_name, character_name emotion
#    audio variables — audio.ost_name, audio.sfx_name, audio.amb_name
#    label names     — ch4_name (all lowercase, underscores only)
#    game variables  — chunghee_affection, yaoguai_tracker, etc.
#    NO SPACES in any tag, label, variable, or image name.
#
#  POV NOTE:
#    Sections 6-9 are Chung-hee's POV. Dorian's POV resumes from Section 11.
#
#  TRACKER SUMMARY:
#    chunghee_affection : +1 Ch4 D(Chung) naïve/inspiring choice
#    yuxuan_affection   : +1 Ch4 D1 interrupt Yuxuan yourself
#
#  PLACEHOLDER PATHS:
#    Search "# PLACEHOLDER" to find every line that needs a real asset.
###############################################################################


# =============================================================================
# SECTION 1: CHARACTER DEFINITIONS (NEW FOR CHAPTER 4)
# =============================================================================
# All characters from prologue, ch1, ch2, ch3 already loaded by Ren'Py.
# Only new characters introduced in Chapter 4 are defined here.
# =============================================================================

define chung_hee      = Character("Hyon Chung-hee",   color="#a78bfa")  # Soft violet — deaf-mute Emperor of Kyeongjang
define captain_sunwoo = Character("Captain Sunwoo",    color="#60a5fa")  # Sky blue — Imperial Guard captain
define ji_hye         = Character("Royal Advisor Ji-hye", color="#f9a8d4")  # Soft pink — Chung-hee's aunt/advisor
define tian_xun       = Character("Tian Xun",          color="#f97316")  # Orange — volatile explosives fanatic
define aoi            = Character("Aoi",               color="#67e8f9")  # Cyan — cold water channeler from Hinami
define tim            = Character("Tim",               color="#4ade80")  # Green — green-haired child prodigy
define tedda_alive    = Character("Tedda",             color="#fbbf24")  # Warm yellow — animated stuffed bear
define carriage_driver = Character("Carriage Driver",  color="#9ca3af")  # Grey — Cheng Industries driver
define prophet        = Character("Prophet",           color="#c4b5fd")  # Soft purple — Niko's fellow brother
define courtier_1     = Character("Courtier 1",        color="#d1d5db")  # Light grey — Kyeongjang courtier
define courtier_2     = Character("Courtier 2",        color="#d1d5db")  # Light grey — Kyeongjang courtier
define servant        = Character("Servant",           color="#9ca3af")  # Grey — Kyeongjang servant
define dae_hyun       = Character("Park Dae-hyun",     color="#6b7280")  # Grey — Head of Infrastructure

# Cheng-hee's mind-channeling dialogue uses the same chung_hee speaker —
# described in narration as "a voice entered our minds" / "a voice filled my head".
# All Chung-hee dialogue is rendered as his mental broadcast regardless of label context.


# =============================================================================
# SECTION 2: IMAGE DECLARATIONS
# =============================================================================
# Search "# PLACEHOLDER" to find every line needing a real asset.
# =============================================================================

# --- Backgrounds: Mjoll Palace ---
# (already declared in chapter_02.rpy — bg_mjoll_palace_throne, bg_mjoll_palace_hall)

# --- Backgrounds: Kyeongjang ---
image bg_kyeongjang_palace       = "images/backgrounds/bg_kyeongjang_palace.png"           # PLACEHOLDER
# Grand celebration hall — gilded columns, dancing performers, feast laid out

image bg_kyeongjang_room         = "images/backgrounds/bg_kyeongjang_room.png"             # PLACEHOLDER
# Dark storeroom lit by moonlight — shelves of scrolls, golden chest at center

# --- Backgrounds: Tianho ---
image bg_tianho_dorian_room      = "images/backgrounds/bg_tianho_dorian_room.png"          # PLACEHOLDER
# Simple small house interior — warm, modest, jasmine scent implied

image bg_tianho_memorial_gate    = "images/backgrounds/bg_tianho_memorial_gate.png"        # PLACEHOLDER
# Cemetery main entrance — afternoon light, people moving in/out

image bg_tianho_memorial         = "images/backgrounds/bg_tianho_memorial.png"             # PLACEHOLDER
# Cemetery interior — weathered gravestones, soft afternoon light, rustling leaves

image bg_tianho_memorial_2       = "images/backgrounds/bg_tianho_memorial_2.png"           # PLACEHOLDER
# Cemetery interior angle 2 — wider view, Yuxuan visible at distance

image bg_empty_battlefield       = "images/backgrounds/bg_empty_battlefield.png"           # PLACEHOLDER
# Cemetery aftermath — scattered bodies, blood on dirt, smoke in air

image bg_frostcradle_bloodied    = "images/backgrounds/bg_frostcradle_bloodied.png"        # PLACEHOLDER
# Same as Frostcradle bloodied from ch3 — memory flashback trigger

image bg_tianho_underground_1    = "images/backgrounds/bg_tianho_underground_1.png"        # PLACEHOLDER
# Natural cave tunnel — dark, damp, rough stone walls

# --- CGs ---
image cg_dorian_family_graves    = "images/cg/cg_dorian_family_graves.png"                 # PLACEHOLDER
# Dorian kneeling before five gravestones — Elara, Daniel, Emily, Sarah, Lucas

image cg_chung_hee_amulet        = "images/cg/cg_chung_hee_amulet.png"                    # PLACEHOLDER
# Chung-hee holding the emerald amulet — its green glow illuminating his face

image cg_prosperity_dragon_white = "images/cg/cg_prosperity_dragon_white.png"             # PLACEHOLDER
# White screen with draconic fire swirling — Prosperity Dragon's presence

image cg_bomb_bad_end            = "images/cg/cg_bomb_bad_end.png"                        # PLACEHOLDER
# Dorian reaching toward his family in golden light — bad end image

image cg_draconic_fire_surge     = "images/cg/cg_draconic_fire_surge.png"                 # PLACEHOLDER
# Dorian unleashing sphere of draconic fire toward the bomb — Tian Xun silhouette


# =============================================================================
# SECTION 3: AUDIO DECLARATIONS
# =============================================================================
# Search "# PLACEHOLDER" to find every line needing a real asset.
# =============================================================================

# --- Music ---
define audio.ost_mjoll_aftermath  = "audio/music/ost_mjoll_aftermath.ogg"       # PLACEHOLDER
# Dark, heavy aftermath theme — cold strings, low drums

define audio.ost_kyeongjang_celeb = "audio/music/ost_kyeongjang_celeb.ogg"      # PLACEHOLDER
# Grand Kyeongjang celebration — stately orchestral, celebratory

define audio.ost_kyeongjang_quiet = "audio/music/ost_kyeongjang_quiet.ogg"      # PLACEHOLDER
# Quiet Kyeongjang night — sparse piano, melancholy

define audio.ost_tianho_memorial  = "audio/music/ost_tianho_memorial.ogg"       # PLACEHOLDER
# Gentle grief theme — Dorian at the graves

define audio.ost_cemetery_chaos   = "audio/music/ost_cemetery_chaos.ogg"        # PLACEHOLDER
# Tension — Mjoll soldiers arriving, explosions

define audio.ost_prosperity_dragon= "audio/music/ost_prosperity_dragon.ogg"     # PLACEHOLDER
# Divine — Prosperity Dragon's voice, draconic fire

define audio.ost_underground_move = "audio/music/ost_underground_move.ogg"      # PLACEHOLDER
# Tense escape — underground tunnel movement

# --- Sound Effects ---
define audio.sfx_explosion_boom   = "audio/sfx/sfx_explosion_boom.ogg"         # PLACEHOLDER
define audio.sfx_arrow_volley     = "audio/sfx/sfx_arrow_volley.ogg"           # PLACEHOLDER
define audio.sfx_earth_pillar     = "audio/sfx/sfx_earth_pillar.ogg"           # PLACEHOLDER
define audio.sfx_wind_blast       = "audio/sfx/sfx_wind_blast.ogg"             # PLACEHOLDER  (already in ch2 but re-declared for ch4 scope)
define audio.sfx_carriage_crash   = "audio/sfx/sfx_carriage_crash.ogg"         # PLACEHOLDER
define audio.sfx_metal_barrier    = "audio/sfx/sfx_metal_barrier.ogg"          # PLACEHOLDER
define audio.sfx_shadow_surge     = "audio/sfx/sfx_shadow_surge.ogg"           # PLACEHOLDER
define audio.sfx_draconic_fire    = "audio/sfx/sfx_draconic_fire.ogg"          # PLACEHOLDER
define audio.sfx_tunnel_seal      = "audio/sfx/sfx_tunnel_seal.ogg"            # PLACEHOLDER
define audio.sfx_amulet_pulse     = "audio/sfx/sfx_amulet_pulse.ogg"           # PLACEHOLDER

# --- Ambient ---
define audio.amb_kyeongjang_feast = "audio/ambient/amb_kyeongjang_feast.ogg"   # PLACEHOLDER
define audio.amb_cemetery         = "audio/ambient/amb_cemetery.ogg"           # PLACEHOLDER
define audio.amb_tianho_afternoon = "audio/ambient/amb_tianho_afternoon.ogg"   # PLACEHOLDER
define audio.amb_rain_heavy       = "audio/ambient/amb_rain_heavy.ogg"         # PLACEHOLDER
define audio.amb_tunnel           = "audio/ambient/amb_tunnel.ogg"             # PLACEHOLDER


# =============================================================================
# SECTION 4: GAME VARIABLES
# =============================================================================

default chunghee_affection   = 0      # Chung-hee trust/romance tracker
# yuxuan_affection already defined in chapter_02.rpy

default ch4_yuxuan_interrupted = False  # True if player chose "Interrupt Yuxuan yourself"
default ch4_chunghee_choice    = ""     # "naive" or "inspiring" — D(Chung) speech choice
default ch4_carriage_qtc1      = ""     # "earth" or "sleep_powder"
default ch4_carriage_qtc2      = ""     # "stumble" or "wind"
default ch4_draconic_choice    = ""     # "tianho" "family" "mjoll" or "self"


# =============================================================================
# SECTION 5: LABEL CHAPTER_4 — Mjoll Palace Aftermath
# =============================================================================
# Entry point — jumped to from chapter_03.rpy via 'jump chapter_4'.
# PDF pages 149-151.
# =============================================================================

label chapter_4:

    # PDF p149
    scene cg_black with fade                    # PLACEHOLDER — black screen
    play music ost_mjoll_aftermath fadein 2.0   # PLACEHOLDER — dark aftermath theme

    show screen chapter_title_screen(
        "4",
        "The Massacrer of Mjoll",
        subtitle="Mjoll / Kyeongjang / Tianho",
        duration=3.0
    )
    pause 3.0

    # [COMMENT: bg_mjoll_palace_throne — Mjoll throne room, Gustav on throne, soldiers present]
    scene bg_mjoll_palace_throne with fade      # PLACEHOLDER — Mjoll throne room

    # PDF p149
    king_gustav "Count Vasily… dead."
    king_gustav "My right hand man… I… I can't believe this."
    king_gustav "And the amulet? Tell me you at least retrieved the damn amulet!"
    mjoll_lars  "N-No, Your Majesty. We searched the site thoroughly, but it… it's gone."
    mjoll_helga "We believe… we believe sir Dor – I mean, Dorian took it."
    king_gustav "That traitorous snake! After everything I gave him—after all my trust!"
    king_gustav "How many? How many died?"
    mjoll_lars  "Nearly all, Your Majesty. We lost nearly the entire battalion."
    king_gustav "By Enoch… Nearly all…"

    # PDF p150
    mjoll_pavel "Your Majesty… We have the two survivors with us. They're outside."
    king_gustav "Send them in."

    # show girl_ald_soldier weeping at left      # PLACEHOLDER — Girl Aldorith soldier sprite
    girl_ald_soldier "It… *crying* It wasn't human… He wasn't human…"
    mjoll_lars       "Miss, please. Take a breath. Tell us what happened."
    girl_ald_soldier "Flames… everywhere… He burned them… He burned them all alive!"
    girl_ald_soldier "If I hadn't run… I would have… I would have— I would hav—burned with them! *weeping*"

    mjoll_pavel "And we have Svante, Your Majesty."

    # show svante broken at right               # PLACEHOLDER — Svante sprite (broken, weeping)
    svante "He's a monster… A massacrer… He… he killed them all…"
    svante "Count Vasily… Kristin… My brothers… sisters… Everyone… gone… It was a massacre… *weeping*"

    king_gustav "I am sorry, my son."
    svante      "F-Father…"

    king_gustav "I've heard troubling whispers. Whispers of your sister—TAINTED by the Prince's lies, doubting me."
    svante      "Kristin, she—"
    king_gustav "She deserved her fate. Her death was just. Her betrayal brought shame to you and your ailing mother. Surely it must have pleased you to see her cut down for my name."
    svante      "I—"
    king_gustav "You are loyal, my son, and for that, you will be rewarded. But I see the grief in your eyes—the weight of Count Vasily and the others lost."
    svante      "The man… he was surrounded by fire, Father. It was like… it was part of him. He burned everything. Everyone. I barely escaped."

    king_gustav "A massacre…"
    girl_ald_soldier "Massacrer… He's a massacrer! *weeping*"
    mjoll_helga "Miss, please calm down."

    king_gustav "Dorian the Dragon of Gale… Now the Massacrer of Mjoll."
    king_gustav "I want him hunted down. I don't care how many Aldoriths it takes or how long. Find him. Kill him. He is an enemy of this land. Do you hear me?"
    "Aldoriths: Yes, Father!"
    svante      "Y-Yes, Father…"

    messenger   "A letter from the Emperor of Kyeongjang, Your Majesty."

    # PDF p151
    mjoll_pavel "K-Kyeongjang, Your Majesty?"
    king_gustav "Hmm… Fascinating…"
    mjoll_pavel "…"
    mjoll_helga "…"
    mjoll_lars  "…"
    svante      "…"

    king_gustav "Forget Dorian. We have a new target."
    king_gustav "Aldoriths. Our sights are now set on the Emperor of Kyeongjang."
    "Aldoriths: Yes, Father!!"
    mjoll_lars  "Yes, Your Highness!"
    svante      "The Empreror of Kyeongjang…"

    jump ch4_kyeongjang


# =============================================================================
# SECTION 6: LABEL CH4_KYEONGJANG — Chung-hee's Birthday (Chung-hee POV)
# =============================================================================
# PDF pages 151-154.
# POV: Hyon Chung-hee, Emperor of Kyeongjang.
# All Chung-hee dialogue is his internal/mind-channeled voice.
# =============================================================================

label ch4_kyeongjang:

    # PDF p151 — 8 months later
    scene cg_black with fade                    # PLACEHOLDER — time skip black

    pause 1.0

    "8 months later"
    "Somewhere in the Kyeongjang Empire"

    # [COMMENT: bg_kyeongjang_palace — grand hall, celebration in full swing]
    scene bg_kyeongjang_palace with fade        # PLACEHOLDER — Kyeongjang palace hall
    play music ost_kyeongjang_celeb fadein 2.0  # PLACEHOLDER — grand celebration theme
    play audio amb_kyeongjang_feast loop fadein 2.0  # PLACEHOLDER — feast ambient

    # PDF p151 — Chung-hee's POV header
    "Hyon Chung-hee's POV"

    "The grand hall was alive with celebration today."
    "Though I could not hear the cacophony of cheers or the music of the orchestra, I could feel the energy pulsing through the room. I can hear their thoughts."
    "They were as clear as if spoken aloud."

    servant     "Happy birthday, Pyeha. May your days be long and prosperous."
    woman_1     "Pyeha's birthday… what can we possibly gift someone so divine?"
    man_1       "Just focus on your singing. Don't falter. Not today."

    "I sat upon the throne of Kyeongjang, looking at the scrumptious feast laid before me."

    # PDF p152
    "The scent of lotus blossoms and spiced incense permeated the air, mingling with the aroma of roasted pheasants, glazed fruits, and elaborate pastries laid out for the feast."
    "The dancers twirled gracefully before me, their silken robes catching the light with each spin. I watched, entranced, my attention so absorbed that I barely noticed him approaching."

    "Captain Kang Sunwoo, clad in the pristine silver and navy uniform of the Imperial Guard, bowed low before the throne, his posture respectful and precise."

    # show captain_sunwoo bow at right           # PLACEHOLDER — Sunwoo sprite (bow)

    captain_sunwoo "Pyeha, I humbly wish you a most joyous birthday. May your reign continue to bring light and prosperity to Kyeongjang for many decades to come."
    chung_hee      "Captain Sunwoo, I appreciate your words. Please, enjoy the feast. It is as much for you as it is for me."

    "He hesitated for a moment, his sharp eyes flickering."

    captain_sunwoo "Pyeha, forgive me for addressing you on such a day of celebration, but I must say this—things are looking brighter for Kyeongjang."
    captain_sunwoo "Trade has flourished within our borders, and our crops yield twice what they did last year. Under your divine hand, the people see you as their protector, their guiding light."
    captain_sunwoo "The Tetrad themselves could not have chosen a better ruler."

    "Before I could respond, another figure stepped forward—Ya Ji-hye, my royal advisor. She was a woman of middle age, her hair streaked with silver, her demeanor sharp and dignified. She bowed deeply, her head nearly touching the floor."

    # show ji_hye bow at center                  # PLACEHOLDER — Ji-hye sprite (deep bow)

    ji_hye "Pyeha, on this most auspicious day, I offer my humblest and most heartfelt birthday wishes. May your reign be eternal, and may Kyeongjang continue to prosper under your divine leadership."
    ji_hye "You are the pillar of this empire, the sun that shines upon its people."

    "I inclined my head, granting her silent permission to continue. Satisfied, she bowed once more and retreated into the crowd."
    "Next, Park Dae-hyun, Head of Infrastructure, approached. He was a man of practicality, his hands calloused from years of overseeing the empire's great projects. His bow was deep and deliberate."

    dae_hyun "Pyeha, I too wish you the happiest of birthdays. May your wisdom guide Kyeongjang for generations to come."

    "Beyond my advisors, I felt the pulse of the celebration itself. Courtiers raised their cups in my honor, their thoughts brimming with admiration and awe."

    courtier_1 "To Pyeha, the living embodiment of Kyeongjang's strength!"
    courtier_2 "The Emperor's wisdom surpasses all. He is untouchable. Eternal."

    "And as is tradition, a song filled the hall, sung by a chorus of voices, though I could not hear it. Still, their thoughts resonated in my mind like a hymn:"

    # PDF p153
    "You are untouchable. Eternal. A god among men."

    captain_sunwoo "Pyeha, the people adore you. Kyeongjang grows stronger with each passing day under your rule. You are their guiding star"
    ji_hye         "Pyeha has done what other kingdoms could not. Kyeongjang is self-made, unshaken by the tragedy of Tianho."

    "Upon the mention of the tragedy of Tianho, I could see the unease in their thoughts."

    woman_1  "The tragedy of Tianho… it all began when they tried to reconnect with the world. Look where it led them."
    man_1    "(thinking): Kyeongjang cannot make the same mistake. Pyeha must keep us strong and protected."
    man_2    "(thinking): The world beyond Kyeongjang brought only ruin to Tianho. Our Lord Emperor won't let that happen to us."
    vendor   "Your Majesty, Tianho was mighty, but their trust in outsiders doomed them. Let us not follow their folly. Kyeongjang is strong because we are self-sufficient. The outside world offers nothing but danger!"
    courtier_1 "Our beloved pyeha and pyeha-sshi died because of those outside infidels!"
    courtier_2 "The gates of Kyeongjang must remain closed, Pyeha. We cannot let history repeat itself."

    captain_sunwoo "Silence! All of you!"
    ji_hye         "This is Pyeha's birthday. Let us focus on the celebration and leave those negative thoughts behind."

    "I rose slowly from my throne, my gaze sweeping over them—advisors, merchants, courtiers, and guards."

    chung_hee "The tragedy of Tianho is a lesson carved into history, one that I have not forgotten. The loss of our beloved pyeha and pyeha-sshi serves as a reminder of the dangers of trust misplaced and gates left unguarded. But hear me now."
    chung_hee "Kyeongjang is not Tianho. Their choices, their fate—it is not ours to share. We have moved past the mistakes of the past. We are stronger, wiser, and more unified than they ever were. We are self-sufficient. We do not need the outside world to prosper."

    "I saw the crowd listening as I continued."

    chung_hee "The past is in the past. We will not dwell in the shadows of fear or doubt. Under my reign, Kyeongjang will remain untouchable. Eternal. A beacon of strength and prosperity."
    chung_hee "We will never commune with outsiders. That is a promise."

    vendor     "You are right, Pyeha. Kyeongjang needs no one else. We are strong because of you."
    courtier_1 "To Pyeha, the unshakable ruler of Kyeongjang!"

    # PDF p154
    courtier_2 "The past is in the past! To our Emperor!"

    "I lifted my cup, keeping my gaze fixed on them."

    chung_hee "Raise your cups, my people. Let this day not only celebrate my birth but also the unwavering strength of our empire. Together, we move forward. Together, we endure. Together, we thrive."

    "I felt the hall erupting in cheers."

    captain_sunwoo "And now, we celebrate! Long live pyeha!"

    jump ch4_kyeongjang_night


# =============================================================================
# SECTION 7: LABEL CH4_KYEONGJANG_NIGHT — Chung-hee Retrieves the Amulet
# =============================================================================
# PDF pages 154-157.
# Chung-hee POV continues.
# =============================================================================

label ch4_kyeongjang_night:

    # PDF p154 — 10 hours later
    stop music fadeout 2.0
    stop audio fadeout 1.5

    # [COMMENT: bg_kyeongjang_room — dark storeroom, pale moonlight, shelves of scrolls]
    scene bg_kyeongjang_room with fade          # PLACEHOLDER — Kyeongjang dark room
    play music ost_kyeongjang_quiet fadein 2.0  # PLACEHOLDER — quiet melancholy theme

    "10 hours later…"

    "The festivities had passed in a blur of music, laughter, and endless praise. When the final toast was raised and the last firework faded into the obsidian sky, the grand hall grew silent, leaving only echoes of the revelry behind."
    "The empire slept. The clock struck ten."
    "It's time."

    "The room I entered was dark, lit only by the pale moonlight filtering through a small, barred window high above. Shelves lined the walls, filled with dusty tomes, crates of sealed scrolls. The air was heavy with the scent of aged parchment and old wood."
    "My steps were deliberate, echoing softly against the stone floor as I approached the center of the room. There it was—a chest, simple in design but bound with golden filigree that glimmered faintly in the moonlight."

    "I knelt before it, the cold seeping into my knees."

    chung_hee "…"

    "My hand hesitated over the latch for only a moment before I pushed it open. Inside lay one thing—the amulet."
    "I reached for it, my hand steady, and lifted it from its resting place. The emerald-green gem seemed almost alive, its surface impossibly smooth and gleaming as though it held its own pulse. Around the gem, intricate golden runes spiraled outward."

    play sound sfx_amulet_pulse                 # PLACEHOLDER — amulet pulse SFX

    "The moment it touched my hand, the amulet's glow intensified, casting an ethereal green light that bathed the room."
    "I held it before me, trapping my eyes with its green glow. I held it for a long time."

    chung_hee "Mother… Father…"

    # PDF p155
    "Then another thought, sharp and resolute, pierced through the haze of my mind."

    chung_hee "I know you're there."

    ji_hye "?!"

    "Her silhouette slowly emerged from the darkness. My royal advisor, Ya Ji-Hye."
    "Her face was pale in the moonlight. She clutched the folds of her robes tightly, her shoulders tense as though bracing herself."

    ji_hye    "P-Pyeha… forgive my intrusion. I… I cannot stop you, can I?"

    "I turned to face her fully, the amulet's light glinting off my robes."

    chung_hee "You cannot stop the Emperor Lord, Royal Advisor."

    "Her breath hitched, and I can see her composure faltering for the briefest of moments. But she steadied herself, bowing deeply."

    ji_hye    "Forgive me, Pyeha… but as your humble servant, I must plead with you to reconsider. This path you are walking—it will only lead to ruin."
    chung_hee "Kyeongjang calls for vengeance. King Gustav will fall."
    ji_hye    "Kyeongjang? Or is it just you, Pyeha? Is it your vengeance that drives you—not the empire's? Please… just leave the past behind! I beg you!"

    "Her hands continued to tremble."

    ji_hye    "As your Royal Advisor—"
    chung_hee "How dare you presume to order your Emperor Lord? Do you think your station grants you the right to defy me?"

    "Her knees buckled, and tears started falling down from her eyes. She dropped to the floor, her forehead nearly touching the cold stone."

    ji_hye    "Please, Chung! I beg you, not as your advisor but as your aunt. Please… don't do this!"

    "I saw her shoulders shake. Tears continued to fall down from her eyes."
    "I looked away, my jaw tightening as I clutched the amulet tighter."

    chung_hee "Do not make this harder than it already is, Aunt."

    "But she would not relent. She lifted her face to look at me, her eyes glistening with tears."

    ji_hye "Do you not remember what happened to our beloved Pyeha and Pyeha-sshi? They too sought answers in the outside realm, and it cost them their lives."
    ji_hye "Please, Chung… I don't want to lose another family member. Jong-hee—your little brother—would be heartbroken to hear of your death too."

    # PDF p156
    "I turned fully to her, my grip on the amulet loosening slightly."

    chung_hee "Please… do not bring my little brother into this, Aunt."

    "There was a brief silence in our thoughts."

    chung_hee "Speaking of Jong-hee… how is he? I didn't see him at the celebration earlier."
    ji_hye    "He's hospitalized since yesterday. The illness is taking over again."
    ji_hye    "All the more reason for you not to go. Please, Chung…"

    "Her tears stained the stone beneath her, and I could see her breaking—truly breaking before me. I knelt before her. The glow of the amulet painted the streaks of her tears in green."

    chung_hee "Aunt Ji-hye… I must do this. I must."
    ji_hye    "You and Jong-hee are all I have left, Chung. Please… please don't leave me too"

    "Her hands gripped the folds of her robe tighter. I reached out, placing a hand on her trembling shoulder."

    chung_hee "He must pay. You know that, Aunt."

    "I stood, lifting her gently to her feet, the amulet's unearthly light illuminating her tear-streaked face again."

    ji_hye    "Then… then at least speak with the captain, Pyeha. Perhaps he can offer a different perspective. Perhaps he can talk some sense into you."

    "My eyes narrowed slightly."

    chung_hee "Again, Aunt, you cannot stop me."

    "She hesitated, and then, a small, sad smile broke through her tears."

    ji_hye "You are just as hard-headed as Pyeha-sshi… your mother."

    "The air shifted, and then I felt something – another person's familiar thoughts."
    "Sunwoo's. I"

    chung_hee "Did you call Captain Sunwoo, Aunt?"

    "Her expression faltered, and she bowed her head."

    ji_hye "I… yes, Chung. I was worried. I thought perhaps he could change your mind."

    "A sigh escaped me."

    chung_hee "For the last time, Aunt, neither you nor he can stop me."

    # PDF p157
    "She surprised me then, wrapping her arms around me in an embrace."

    ji_hye    "Then I will stay. If I cannot stop you, at least let me see you off."

    "I rested a hand on her back for a short while."

    chung_hee "I intend to return, Aunt. I won't leave you or Jong-hee. I promise."

    "Her lips trembled, and I heard the unspoken thought she didn't dare voice aloud:"
    "\"That's what pyeha and pyeha-sshi said when they left for Tianho. Five years ago…\""

    "I reached out and placed a hand on her trembling shoulder."

    chung_hee "Please. Get up."

    "I help her get up, the amulet's glow casting its unearthly light upon both of us."

    ji_hye "I think it's important to let the captain speak with you. Perhaps he can offer a different perspective, talk some sense into you."
    chung_hee "Again, Aunt. You can't stop me."
    ji_hye "I know. You're just as hard headed like pyeha-sshi – your mother."

    "I heard another mind. Ji-Hye, it thought out. It was the captain."

    chung_hee "Did you call Captain Sunwoo, Aunt?"
    ji_hye    "I… yes, Chung. I was just worried. I thought maybe he can change your mind,"
    chung_hee "For the last time, Aunt. You or him can't stop me."

    "She hugs me."

    ji_hye    "Chung, I want to stay for a bit. I know I can't stop you, but I wish to see you go."
    chung_hee "I intend to return, Aunt. It's just for a day. I won't leave you and Jong-hee. I promise."

    "She opened her mouth, trying to say something. She hesitated, but I heard her thought – 'That's what pyeha and pyeha-sshi said when they went to Tianho. Five years ago…'"
    "The captain will be coming. I could sense that she really wanted me to stay, and it gave me pause. The captain could potentially cross paths with me if I stayed. He can't stop me, but it'll save me precious time by explaining myself."
    "I need to act fast. What should I do?"

    jump ch4_chunghee_qtc


# =============================================================================
# SECTION 8: LABEL CH4_CHUNGHEE_QTC — Timed Choice: What to do with Ji-hye
# =============================================================================
# PDF pages 157-163.
# Quick Timed Choice — 4 options. All lead to ch4_common_1 or ch4_common_2.
# =============================================================================

label ch4_chunghee_qtc:

    # PDF p157
    play sound sfx_amulet_pulse loop            # PLACEHOLDER — tension / amulet pulse

    menu:

        "Falter and do nothing.":
            # PDF p158 — choice 1 OR NO CHOICE

            stop sound

            "I stood there, the amulet pulsing faintly in my hand. Aunt Ji-hye continued sobbing, tugging at something deep within me. Strangely, I made no move."
            "I simply… stood there."

            ji_hye    "Chung… what are you doing? Are you… frozen? Have you reconsidered?"
            chung_hee "No, Aunt. I am merely… recalibrating my thoughts."
            ji_hye    "*crying*"
            chung_hee "…"
            ji_hye    "*crying*"
            chung_hee "…"

            jump ch4_common_1

        "Trick Aunt Ji-Hye.":
            # PDF p158 — choice 2

            stop sound

            "There's no time."
            "I focused, my mind reaching outward, weaving through the threads of energy. With deliberate precision, I channeled my power, bending the perception of those around me. Slowly, my form shimmered, then vanished completely."

            ji_hye "Chung?! Chung, where are you?!"

            "She stepped forward, her hands grasping at the empty air."

            ji_hye "No… no, no, no! He's gone… he's really gone!"

            "Her knees gave way, and she collapsed to the cold stone floor, sobbing."

            ji_hye "Why, Chung? Why couldn't you listen to me? Why couldn't you stay?!"

            "Her thoughts were a blur. Panic. Loss."
            "Captain Sunwoo stepped into the room, his sharp gaze immediately taking in Ji-Hye's crumpled form."

            captain_sunwoo "Ji-hye-nim, what's happened?"

            # PDF p159
            "She looked up at him, her face streaked with tears."

            ji_hye         "He's gone… He left us, Sunwoo! He's gone to the outside lands. I tried to stop him, but he wouldn't listen… and now he's gone, just like Pyeha and Pyeha-sshi…"

            "She cried, burying her face in her hands."
            "Sunwoo knelt beside her, his expression softening as he placed a steady hand on her shoulder."

            captain_sunwoo "Ji-hye-nim, I'm sorry. I should've arrived sooner… this isn't your fault. You did everything you could."
            ji_hye         "He's my nephew, Sunwoo. My family. And I couldn't save him. I couldn't save any of them!"

            "The Captain tightened his grip on her shoulder, his voice low and firm."

            ji_hye "What will I tell Jong-hee when he wakes up in the hospital? What will I say when he asks where his brother is? He would be…*crying*"

            "For a fleeting moment, I almost stepped forward, my body tense and my heart aching at the sight of her crumpled form. But then the amulet in my hand pulsed, its emerald glow casting its light over the dim room."
            "I have to finish this."

            captain_sunwoo "Pyeha is strong. He's stubborn, yes, but he's strong. We must trust that he knows what he's doing."
            captain_sunwoo "Come, Ji-Hye-nim. Let's get you out of here. It's late, but I know of a small vendor near the palace that serves steaming bowls of spicy kimchi jjigae."
            captain_sunwoo "A good meal might help calm your mind."
            ji_hye         "Kimchi jjigae? At this hour, Captain?"
            captain_sunwoo "It's Kyeongjang, Ji-hye-nim. There's always someone open. And I'm told this place also makes the best bindaetteok to pair with it."
            ji_hye         "*sniffling* You're persistent, Captain Sunwoo… but thank you. I… I appreciate it."

            "Sunwoo helped her to her feet, his arm steadying her as she wiped her face."

            captain_sunwoo "Let's go. You need warmth, and you won't find it here in this cold room."

            "They began to leave, walking away with Aunt holding his arm."
            "Left alone, I emerged from the shadows where I had been standing invisibly. My hands tightened around the glowing amulet."

            chung_hee "Aunt… I'm so sorry. Please forgive me."

            jump ch4_common_2

        "Do what she wants. Keep Aunt Ji-hye company.":
            # PDF p160 — choice 3

            stop sound

            "I sighed, letting my shoulders relax slightly."

            chung_hee "I'll keep you company for a while, Aunt."

            "Aunt Ji-hye's face lit up with gratitude."

            ji_hye "Thank you, Chung."

            "I clutched the amulet tighter in my hands, its glow pulsing softly like a heartbeat. Its light bathed us both in green."
            "Her mind was an open book to me—pages unfolding like petals of a flower, revealing memories that had been locked away in the recesses of her heart."
            "I didn't invade her thoughts intentionally, but her emotions made them pour out like a rushing river, impossible to ignore."
            "I saw her as a child, running hand in hand with my mother through the sunlit gardens of Kyeongjang. Their laughter was soft and carefree, playing simple games and playing with toys."
            "The memories shifted. I watched them grow older, their bond remaining unshaken. Family gatherings, late-night conversations under the stars, and quiet moments shared in the palace's library."
            "Another memory surfaced—a dazzling vision of Aunt Ji-hye dressed in the finest silks, the fabric shimmering in the light. It was my mother's wedding day. With my father. Aunt Ji-hye cried. She always does."
            "Then the memories darkened, I saw my mother standing before Aunt Ji-hye expressing her desire to venture to Tianho with my father. Aunt cried and begged her to reconsider."
            "The last memory was Aunt knowing of my father and mother's fate. Captain Sunwoo was there, comforting her. We were there too. Me and Jong-hee."

            chung_hee "Aunt…"

            "Aunt Ji-hye looked up at me, her eyes glistening with tears."

            ji_hye    "Chung, please… I've lost her once. Don't make me lose you too."

            "I swallowed hard, pushing down the emotions that threatened to rise. I had to remain strong. For her. For Jong-hee. For myself."

            chung_hee "Aunt, I promise. I'll return safely, and no harm will befall me."

            "She stepped forward and wrapped her arms around me, holding me tightly."
            "She didn't let go for a while. When she finally pulled back, her hands rested on my arms, her grip firm yet trembling."

            # PDF p161
            ji_hye "Do you remember the last time you, Jong-hee, and I ate outside together?"

            "I thought for a moment, the image of simpler days coming to mind."

            chung_hee "I believe it was three years ago, Aunt. At that little noodle shop in the marketplace. Jong-hee couldn't stop laughing at the way the broth splashed on your robes."
            ji_hye    "Yes… that's the one. You scolded him, but you were laughing too. I miss those days, Chung. I miss when it was just the three of us, before…. the weight of the empire fell on your shoulders."

            "I fell quiet. It's not my choice, Aunt. It's never been."

            ji_hye    "I hope we can have that again someday. Just one more day like that. Promise me, Chung. Promise me you'll come back, so we can laugh together again."

            "I placed a hand over hers, squeezing gently."

            chung_hee "I promise, Aunt. One day, we'll have that moment again."
            ji_hye    "I would love that, Chung—"

            jump ch4_common_1

        "Make Aunt Ji-hye go to sleep.":
            # PDF p161 — choice 4

            stop sound

            "I gazed at Aunt Ji-Hye, her trembling form clutching her robes."

            chung_hee "Aunt… I'm sorry. I cannot afford to falter. You leave me no choice."

            "Her eyes widened as she realized what I intended to do."

            ji_hye "Chung, no! Don't do this. Please, I'm begging you—"

            "Before she could finish, I closed my eyes, channeling my focus. My mind reached into hers, gently but firmly quieting her frantic thoughts."
            "A gentle focused thought. And I encouraged her to drift into a peaceful slumber."

            ji_hye "Oh… I - Yes. I feel sleepy…"
            ji_hye "So… sleepy…"

            "Aunt Ji-hye blinked a few times. Slowly, she sank to her knees, her eyelids fluttering closed as she succumbed to an unnatural, peaceful slumber."
            "I stepped forward, catching her before she could slump to the cold stone floor."

            ji_hye "Zzz…. Zzz…"

            "Carefully, I carried her to the spare sofa in the corner of the room."

            chung_hee "I'm sorry, Aunt. I promise… I will return."

            "As I straightened, I sensed him before I saw him."

            # PDF p162
            captain_sunwoo "Pyeha, it's Kang Sunwoo. May I enter?"

            "I turned, composing myself as the door opened. Captain Sunwoo stepped inside, his sharp gaze immediately noticing Ji-Hye's sleeping form. His brow furrowed, but he bowed deeply before me."

            captain_sunwoo "Pyeha, I see that the Royal Advisor is… resting. I hope I am not intruding."
            chung_hee      "You are not. She was overwhelmed and needed rest. I trust you will keep your voice low, Captain."

            "He straightened, his eyes flicking to the glowing amulet in my hand before returning to meet mine."

            captain_sunwoo "Pyeha, forgive me for my boldness, but I understand you intend to leave the palace tonight. I must implore you to reconsider."
            chung_hee      "Captain, I appreciate your concern, but my decision is final."
            captain_sunwoo "Then allow me to accompany you, Pyeha. If you insist on facing danger, I will not let you face it alone."
            chung_hee      "Your place is here, Sunwoo. Kyeongjang needs its captain, and I need you to protect what I leave behind. This is my burden to bear."

            "The amulet in my hand began to glow brighter, its golden runes spiraling outward as I prepared to activate it."

            captain_sunwoo "Pyeha—"
            chung_hee      "Take care of Aunt Ji-hye. And Jong-hee… tell him I will return."

            "Captain Sunwoo carried Aunt Ji-hye and left the room."

            jump ch4_common_2


# =============================================================================
# SECTION 9: LABEL CH4_COMMON_1 — Captain Sunwoo Arrives (Common 1)
# =============================================================================
# PDF pages 162-163.
# Reached from choices 1 and 3.
# =============================================================================

label ch4_common_1:

    # PDF p162
    "The heavy wooden door to the storage creaked open. A figure entered. It was Captain Sunwoo."
    "Upon entering, he bowed deeply, the moonlight glinting off the metal plates of his uniform."

    captain_sunwoo "Pyeha. Forgive my intrusion, but I have come at Ji-Hye's request. She feared for you."

    "I turned to face him fully."

    chung_hee      "Captain Sunwoo. You should know better than to interrupt the Emperor Lord's solitude."
    captain_sunwoo "Pyeha, I… I mean no disrespect. But if I may speak freely…"
    captain_sunwoo "Please don't do this… this path you are planning to choose is a perilous one."

    "I raised an eyebrow."

    chung_hee "You think I do not know that, Captain? You think I haven't considered the risks?"

    # PDF p163
    "He kept his head bowed earnestly. Aunt Ji-hye held my hand tightly."

    ji_hye         "Chung… Please… *crying*"
    captain_sunwoo "I do not doubt your wisdom, Pyeha. But the burden of vengeance is not yours to bear alone."
    captain_sunwoo "If it is vengeance you seek, then allow me to gather the most skilled soldiers of Kyeongjang. Let us march together, and I swear by my honor, Pyeha and Pyeha-sshi will be avenged."
    chung_hee      "This is something I must do on my own, Captain. Kyeongjang will not suffer more losses on my behalf."
    captain_sunwoo "Pyeha… please reconsider. Your safety is paramount. If you fall, the empire—"
    chung_hee      "The empire will endure. It has endured before. And I will not fall."

    "Sunwoo's gaze faltered. He bowed his head low."

    captain_sunwoo "Then may the Tetrad watch over you, Pyeha."

    "Both of them looked at each other and looked down."

    ji_hye "If you are truly set on this path, Chung, then all I can do is wish you safety. Please… come back to us. Come back to Jong-hee."
    chung_hee "I will return, Aunt. I swear it."

    "Her trembling hands touched my face, her eyes searching mine one last time before stepping back."

    ji_hye "Then I have nothing left to say except… goodbye, my Emperor Lord. May your journey be swift, and may justice be yours."

    "Captain Sunwoo stood up and approached Aunt Ji-hye."

    captain_sunwoo "Royal Advisor. Would you care to walk back with me?"
    ji_hye         "Yes, Captain Sunwoo. I appreciate your kind offer."

    "As they turned to leave, Aunt Ji-hye paused at the doorway, glancing back over her shoulder. Her lips trembled as though she wanted to speak, but she said nothing."
    "Instead, she gave me a small, bittersweet smile before disappearing into the shadows with Captain Sunwoo."

    "Love you Jong-hee. Aunt Ji-Hye. Please forgive me."

    jump ch4_common_2


# =============================================================================
# SECTION 10: LABEL CH4_COMMON_2 — Chung-hee Activates the Amulet
# =============================================================================
# PDF pages 163-164.
# Reached from choices 2, 4, and Common 1.
# =============================================================================

label ch4_common_2:

    # PDF p163
    "I clutched the amulet of teleportation in my hand. Its emerald glow pulsated with raw energy, illuminating the dark corners of the room."

    # PDF p164
    "Sparks of green light danced along its golden edges."
    "I took a deep breath, steadying my resolve. My heartbeat slowed, my focus narrowing to a single thought—the place I needed to be."

    play sound sfx_amulet_pulse                 # PLACEHOLDER — amulet pulse

    chung_hee "Almighty Renji, Keeper of the Void and Sovereign of Time and Space, I beseech your power. Let your authority guide me across this mortal plane."
    chung_hee "Deliver me to my destination, that I may fulfill what destiny demands."

    "The room seemed to hold its breath. For a moment, everything stilled. Then, the amulet pulsed violently, its glow intensifying. I felt its power surging through me, a searing heat that seemed to burn through my very essence, yet left no mark on my flesh."

    chung_hee "To Tianho…"

    "Then I vanished into the void."

    stop music fadeout 2.0
    stop sound

    jump ch4_tianho_dorian


# =============================================================================
# SECTION 11: LABEL CH4_TIANHO_DORIAN — Dorian's POV, 8 months later (Tianho)
# =============================================================================
# PDF pages 164-168.
# POV returns to Dorian.
# =============================================================================

label ch4_tianho_dorian:

    # PDF p164 — Tianho, Dorian's POV
    scene cg_black with fade                    # PLACEHOLDER — transition black

    pause 1.0

    "Tianho"

    # [COMMENT: bg_tianho_dorian_room — small house interior, warm, humble]
    scene bg_tianho_dorian_room with fade       # PLACEHOLDER — Dorian's Tianho room
    play music ost_tianho_memorial fadein 3.0   # PLACEHOLDER — gentle, quiet theme
    play audio amb_tianho_afternoon loop fadein 2.0  # PLACEHOLDER — Tianho afternoon ambient

    "It had been eight months since Elias and I came to Tianho. Yuxuan graciously gave us a small house for us to live in —not far from his grand manor."
    "Our house was a little far from the main city. The city itself was a shadow of what I remembered. Once bustling and grand, it was now quieter. What was where high buildings once was, were just small makeshift houses and delapidated structures."
    "Yuxuan's manor, however, was a different story. The sprawling estate stood like a testament to prosperity, its large halls and manicured gardens untouched by time. A faint scent of jasmine lingered everywhere, as if the very air itself had been perfumed."
    "Despite the grandeur, Yuxuan at some times, didn't sleep there. One of the maids mentioned it in passing, but she didn't elaborate on where he stayed instead, and I didn't pry."
    "He would often invite Elias and me over to his manor for meals, celebrations, or simply to spend the night in one of the many guest rooms."
    "Sometimes, he would find excuses to linger, sharing stories from his travels or discussing matters of the empire that I could tell he wished to unburden himself of."
    "Other times, he would vanish for days, leaving the manor unusually quiet. It was a routine I'd come to expect, though the unpredictability of it still caught me off guard."
    "In those eight months, life moved forward quietly. Elias, my little light in the darkness, would often dress in skirts and adorn himself with flowers to match Tedda. Whatever makes him happy, I suppose."
    "The amulet that Elias once had stopped glowing entirely. It's like the power inside had been all used up. Good riddance."

    # PDF p165
    "For me, I spent my time rebuilding—physically, mentally, emotionally. I was no longer the Dragon of Gale in the sense that I once was. My days were simpler now, filled with quiet reflection and attempts to find a purpose beyond the shadow of loss."
    "The Dragon of Gale is dead."
    "Yuxuan had invited me more than once to visit my family's graves. Each time, I declined. It wasn't that I didn't want to go—it was that I couldn't."
    "The thought of standing before their final resting place, of facing the reality of their absence, was something I couldn't bring myself to do."
    "Until now."
    "Tomorrow marks the fifth anniversary of the tragedy of Tianho. Five years since that fateful day when everything changed, when the world as I knew it was shattered."

    "I turned to Elias, who had been sitting on the rug, giggling as he carefully tied a chain of flowers around Tedda's neck."

    dorian "Elias… I think I'm ready."
    elias  "Ready for what, daddy?"

    "Before I could answer, Yuxuan stepped into the room, his robes sweeping softly against the wooden floor. He had been reading in the corner, but now his full attention was on me."

    yuxuan "For what, Dorian?"
    dorian "To visit their graves. maybe now is the time."

    "Yuxuan expression softened. He set the book aside and crossed the room, placing a reassuring hand on my shoulder."

    yuxuan "Praise the Prosperity Dragon. If you're ready, then I'll go with you."

    "I hesitated, glancing at the darkened sky outside the window. The thought of Empress Olympia lingered in the back of my mind—a ripple of unease that I couldn't shake."

    dorian "Do you think we could go now? I'd rather avoid running into the Empress of Gale if we can help it."

    "Yuxuan nodded without hesitation."

    yuxuan "Sure!"

    "Before I could respond, Elias sprang to his feet, clutching Tedda tightly to his chest."

    elias  "Ooh! Can me and Tedda come, daddy?"
    "Tedda: …"

    # PDF p166
    "Tedda remained silent, as always, but Elias made sure to shake the little toy, as if demanding my agreement."
    "I knelt in front of him, placing a gentle hand on his head."

    dorian "I don't think it's a good idea… This isn't the kind of trip for you."
    yuxuan "Oh, come now, Dorian. Let him come along. There are plenty of food stalls along the way. I'm sure Elias and Tedda would enjoy that, wouldn't you, Elias?"
    elias  "Food? Like dumplings? And candy sticks? Ooooh, Tedda loves candy sticks!"

    "He spun in a little circle, holding Tedda above his head."

    dorian "Alright, but you have to promise me you'll stay close. No running off, understand?"
    yuxuan "Alright. It's settled. I'll have the carriage waiting!"

    scene cg_black with dissolve               # PLACEHOLDER — black transition

    "The ride to the cemetery was quiet, save for the soft creak of the carriage wheels and the occasional chatter from Elias."
    "He sat in Yuxuan's lap, happily pointing out passing trees and the occasional bird. I stayed silent, lost in my thoughts, the weight of what lay ahead pressing down on me."

    jump ch4_cemetery


# =============================================================================
# SECTION 12: LABEL CH4_CEMETERY — Dorian Visits the Graves
# =============================================================================
# PDF pages 166-168.
# =============================================================================

label ch4_cemetery:

    # PDF p166
    # [COMMENT: bg_tianho_memorial_gate — cemetery entrance, modest, serene]
    scene bg_tianho_memorial_gate with fade     # PLACEHOLDER — Tianho memorial gate

    "It took thirty minutes to get there. The cemetery was modest yet serene, nestled on the outskirts of the city. A handful of people wandered among the gravestones, some kneeling in prayer, others buying food at small booths set up nearby."

    yuxuan "Take your time, Dorian. Elias and I will wander around for a bit."
    elias  "Tedda and I will wait for you, daddy!"
    dorian "Stay close to Yuxuan, alright?"

    # [COMMENT: bg_tianho_memorial — cemetery interior, soft afternoon light, gravestones]
    scene bg_tianho_memorial with dissolve      # PLACEHOLDER — Tianho memorial interior

    "And just like that, I was alone."
    "The morning wind whispered through the trees, carrying with it a faint chill that seeped into my bones. I took a deep breath and began to walk."
    "Yuxuan had given me directions before we arrived, and I followed the path he described. It felt endless, each step heavier than the last."

    # PDF p167
    "Then I saw them."
    "Their graves stood together in a quiet corner of the cemetery, the tombstones slightly weathered by time but still standing firm. The carvings were intricate, their names etched in flowing script that seemed to glisten under the morning light."
    "Elara Burnham. Daniel. Emily. Sarah. Lucas."
    "My family."

    "My breath caught in my throat as I stared at the names, each one a sharp reminder of what I had lost. My knees felt weak, and before I knew it, I had fallen to the ground in front of them."
    "I reached out, my fingers brushing against Elara's name. The cold stone beneath my hand was a stark contrast to the warmth she had always carried."

    # CG: Dorian kneeling before the five graves
    scene cg_dorian_family_graves with dissolve # PLACEHOLDER — cg_dorian_family_graves
    pause 2.0
    scene bg_tianho_memorial with dissolve

    # [# 23]
    dorian "My love, my heart..."

    "The words came out in a whisper, trembling with emotion."

    dorian "It's been years. I've missed you all so much."

    "I swallowed hard, my vision blurring as tears welled up in my eyes."

    dorian "I've been wandering for so long, trying to find my place in this world. But I never forgot you, and I never will."

    "My voice cracked as I choked back a sob."

    dorian "I'm so sorry for everything. I should have protected you. I should have been there with you all."

    "I stayed there, sitting in silence as the wind carried the soft rustle of leaves. My mind drifted back to memories of them—Elara's laugh, Daniel's courage, Emily's curiosity, Sarah's wisdom, and little Lucas's boundless energy."
    "Time seemed to slip away as I sat there, lost in thought. I didn't know how long it had been when I finally looked up, noticing more people arriving at the cemetery. The peaceful solitude was beginning to fade, and I realized it was time to leave."
    "I stood, brushing off the dirt from my knees, and looked down at the tombstones one last time."

    dorian "I wish I could stay longer, but I need to get a move on."

    "The words felt hollow as they left my lips."
    "I lingered for a moment longer, my fingers grazing Elara's name once more."

    dorian "See you in my dreams, I guess."

    "I turned and began walking back toward the entrance."

    # [COMMENT: bg_tianho_memorial_2 — wider cemetery view, afternoon]
    scene bg_tianho_memorial_2 with dissolve    # PLACEHOLDER — Tianho memorial 2

    # PDF p168
    "I couldn't find Yuxuan at his previous location. I scanned the area. Then I found Elias."

    # [# 24 – Until Dorian's line]
    "He was perched atop a gravestone, his little legs swinging back and forth as he cuddled Tedda close. A bouquet of wildflowers rested beside him."

    elias "Tedda, look at the pretty flowers. They're so colorful!"
    "Tedda: …"
    elias "This one's my favorite, Tedda. It's the same color as your nose!"
    "Tedda: …"
    elias "Hehe, I love you, Tedda!"
    "Tedda: …"

    "I couldn't help but sigh as I approached him."

    dorian "Elias, you're not supposed to sit on top of gravestones. Get down from there."

    "Elias instinctively looked up at me. He cuddled his teddy bear, Tedda, close. He jumped from his perch and walked up to me."

    elias  "Oh… Daddy, are you finished already?"
    dorian "Yeah. I'm done. Where's Yuxuan? Why aren't you guys at our agreed spot?"

    "I crouched down, brushing some dirt off his cheek."

    dorian "Yeah, I'm done. But Elias, this is a place of respect. We don't sit on gravestones, alright?"
    elias  "Oh… sorry, daddy."

    "I scanned the area, my gaze landing on Yuxuan a little distance away. He was deep in conversation, gesturing with his usual authority as he discussed something I couldn't quite hear at first."
    "I took Elias's hand, his tiny fingers wrapping tightly around mine as he skipped beside me, Tedda swinging from his other hand."
    "As we got closer, Yuxuan's voice became clear, his commanding tone filling the air."

    yuxuan "Gentlemen, I appreciate your insights on the new propulsion system. It's a promising concept, and I look forward to our continued collaboration."

    "He adjusted a sleek communication device on his wrist before continuing."

    yuxuan "But I need to make sure that the team will be performing properly. Can I count on that, Mr. Diagro? Meeting deadlines is not an unreasonable expectation."

    # PDF p169
    yuxuan "This new invention has the potential to make a positive impact, to improve lives. I believe it's our responsibility to share it with the world, to make a difference."
    yuxuan "The propulsion system needs to be launched next month. That's an order, Ms. Ara."

    "I glanced down at Elias, whose eyes were wide with curiosity, though I could tell he didn't understand half of what Yuxuan was saying."

    dorian "Elias, how long have you been separated from Yuxuan?"

    "Elias tilted his head, biting his lip as if deep in thought. He lifted his hand, struggling to count on his tiny fingers. He scrunched up his face, clearly losing track. He gave up and hugged Tedda."

    elias  "A lot, daddy. Mister Yuxuan was talking for a lot of minutes."
    dorian "I see. So, he's been at it for a while now."

    "Elias nodded enthusiastically, holding Tedda up as if the bear could confirm his statement."
    "I stood there for a moment, watching Yuxuan in his element. The conversation seemed intense, and I wondered how much longer it would take."
    "He had always told me to interrupt him if his discussions dragged on, but I didn't want to come across as rude—not when he was clearly dealing with something important."

    jump ch4_yuxuan_convo


# =============================================================================
# SECTION 13: LABEL CH4_YUXUAN_CONVO — Waiting for Yuxuan (Choices)
# =============================================================================
# PDF pages 169-172.
# D1: interrupt gives +yuxuan_affection
# =============================================================================

label ch4_yuxuan_convo:

    # PDF p169
    menu:

        "Continue to wait patiently.":
            # PDF p169 — choice 1 AND 2 share same text before waving
            $ ch4_yuxuan_interrupted = False

            "I can give him a few more minutes. It's not like we're in a rush. Elias seems content enough for now."

            yuxuan "Look, I understand your concerns, and they are VALID, but I firmly believe that the market is ready for this innovation. We can't afford to have any more delays."
            yuxuan "But nothing! Risks are inherent in any endeavor, but we've mitigated them to the best of our abilities. We owe it to ourselves and to Ena to move forward."
            yuxuan "Of course, of course. Yes. Ms. Jane, please prepare a detailed plan to be submitted at the end of your shift. Got it?"
            yuxuan "Overtime? But you're on the night shift and it's barely the end of the afternoon… You have plenty of time. Ugh. Okay fine, approved."

            # PDF p170
            yuxuan "But you better have the plan prepared or, I swear in the name of the Prosperity dragon, I'm gonna have to replace you! No, I mean it! I really mean—"

            "Seeing no other option, I waved at Yuxuan, trying to catch his attention. When he finally noticed me, his expression shifted from intense concentration to one of embarrassment, realizing that I had been waiting patiently."

            yuxuan "My apologies, I'll be back with you in just a moment. Ms. Ara, take the lead please."

            jump ch4_yuxuan_common

        "Try to get his attention by waving your hand.":
            # PDF p169-170 — same as choice 1
            $ ch4_yuxuan_interrupted = False

            "I can give him a few more minutes. It's not like we're in a rush. Elias seems content enough for now."

            yuxuan "Look, I understand your concerns, and they are VALID, but I firmly believe that the market is ready for this innovation. We can't afford to have any more delays."
            yuxuan "But nothing! Risks are inherent in any endeavor, but we've mitigated them to the best of our abilities. We owe it to ourselves and to Ena to move forward."
            yuxuan "Of course, of course. Yes. Ms. Jane, please prepare a detailed plan to be submitted at the end of your shift. Got it?"
            yuxuan "Overtime? But you're on the night shift and it's barely the end of the afternoon… You have plenty of time. Ugh. Okay fine, approved."

            yuxuan "But you better have the plan prepared or, I swear in the name of the Prosperity dragon, I'm gonna have to replace you! No, I mean it! I really mean—"

            "Seeing no other option, I waved at Yuxuan, trying to catch his attention. When he finally noticed me, his expression shifted from intense concentration to one of embarrassment, realizing that I had been waiting patiently."

            yuxuan "My apologies, I'll be back with you in just a moment. Ms. Ara, take the lead please."

            jump ch4_yuxuan_common

        "Ask Elias and Tedda for help.":
            # PDF p170 — choice 3
            $ ch4_yuxuan_interrupted = False

            "Elias could charm a mountain into moving. Maybe his enthusiasm can draw Yuxuan's attention."

            dorian "Elias, do you think you and Tedda can get Yuxuan to notice us?"

            "Elias's face immediately lit up, his eyes sparkling with excitement. He clutched Tedda to his chest, as if this was the most important mission he'd ever been given."

            elias "Okay, Daddy! Tedda and me can do it! Watch!"

            "He waved Tedda's little paw around wildly, its arms flailing like a windmill."

            elias  "Mister Yuxuan! See? Tedda's waving at you! She says hi really loud!"
            "Tedda: …"

            yuxuan "I already told you, Jane! Get it done by the end of your shift! Is that too much to ask? We can't afford to have another delay, I told you!"
            yuxuan "We need to get those propulsion systems on the market as soon as possible! You have a secretary, right? Go and ask her for help!"

            "Elias frowned."

            elias  "Daddy, Mister Yuxuan didn't see Tedda."

            "I pinched the bridge of my nose, trying not to laugh."

            dorian "It's okay, Elias. It's not your fault. He's busy."

            "But Elias wasn't about to give up so easily. His eyes lit up with a new idea, and he pointed toward a nearby gravestone adorned with beautiful flowers."

            elias "Daddy! Tedda and me will give him flowers! Pretty flowers! Look over there!"

            "Before I could say a word, Elias bolted toward the gravestone with his tiny feet pattering against the ground."
            "The tag on the flowers read: Rest in Peace, Mom."

            # PDF p171
            "I hurried after him, catching him just as he reached for the vibrant blooms. Gently, I took his little hand before he could pick any."

            dorian "Elias, no. We can't just pick flowers from a gravestone. That's bad."
            elias  "Oh… sorry, daddy. We'll just continue waving then."

            "Without a care in the world, he cheerfully continues to wave the toy's hands. Charming, but definitely not getting Yuxuan's attention. Why did I even ask for his help?"

            jump ch4_yuxuan_common

        "Interrupt Yuxuan yourself.":
            # PDF p171 — choice 4
            $ ch4_yuxuan_interrupted = True
            $ yuxuan_affection += 1             # +1 Yuxuan affection

            "He told me to step in when this happens. I might as well remind him that we're waiting."
            "Approaching Yuxuan, I waited for a brief pause in his conversation, and then I cleared my throat to ensure I had his attention."

            dorian "Yuxuan. Yuxuan?"
            yuxuan "Jane, I won't ask again. Get it done and send it to him. No excuses."
            dorian "Yuxuan. Hey, I'm finished."

            "As I interrupted Yuxuan, he felt relieved. His face lit up with a smile as he turned to his device."

            yuxuan "I must step away for a moment. Jane, I trust that you will take charge of the meeting… Huh? Of course it's you! Do you see any other Janes in there?"

            jump ch4_yuxuan_common


label ch4_yuxuan_common:

    # PDF p171-172 — Common after all four choices
    "Yuxuan hung up his communication device with a soft sigh, fiddling with it briefly before slipping it into his robe pocket. He gave me a sheepish smile."
    "I chuckled, shaking my head."

    yuxuan "Dorian, buddy, sorry for the spectacle. Are you finished? How was it?"
    dorian "Don't mention it, Yu. And… yeah, I'm done. It felt nice, actually. It's been a long time since I've been able to visit my family. Thank you for bringing us here."
    dorian "And I saw what you did with the flowers. It means a lot."
    dorian "You've already done so much for me. For us. And about the gravesite fees… I'll pay you back. If I can do chores, or help with anything—"

    "He waved a hand dismissively."

    # PDF p172
    yuxuan "No, no, no! Pleasure's all mine, Dorian. It's the least I can do since you've saved me during the tragedy."
    yuxuan "And… we're friends. It's an honor for me to be there for you."
    dorian "Th-Thank you, Yu. I appreciate it."
    yuxuan "Anyway, I think it's time for us to go. Before we leave, however, I suggest we try those treats from Hinami. Elias, do you like treats?"
    elias  "Treats?! Candies?"
    yuxuan "Well, treats, yes. But they're not candies. They're delectable treats from the Hinami booth here. They're fish treats- considering the ingredients—"

    "As Yuxuan continued speaking, I noticed a growing number of people entering the cemetery. They moved in coordinated lines, their armor gleaming in the sunlight and marked with the unmistakable emblem of the Mjoll kingdom."
    "What in Tetrad's name are they doing here? Are they here for me? For Elias?"

    yuxuan "Come, I'll show you where to booth is. Let's go. You'll love them!"
    dorian "Wait, Yu—"

    svante "Excuse me, civilians. You need to get away from this place as soon as possible. It's not safe here."

    "A strangely familiar young man approached us, his brushed-up hair was of the color violet, matching his armor."
    "Svante. An aldorith from Mjoll."
    "I instinctively turned Elias away, hoping Svante wouldn't recognize us. As he approached, his voice was firm but respectful."

    yuxuan "What? What do you mean it's not safe? This is a cemetery. Why would we need to leave?"
    svante "As I've said, sir. It's not safe. Please leave immediately."
    yuxuan "No. And who are YOU to tell us to leave? There better be a good reason for this!"
    svante "Sir, by the order of king Gustav, civilians must evacuate the premises as soon as possible. It's for your own safety."
    yuxuan "King Gustav? King Gustav has no jurisdiction here. This is Tianho! What in Ena's name are you talking about?"
    svante "Sir, please… this is for your own safety. We don't want you to get involved."

    "I kept my head bowed, tightening my grip on Elias's hand. His little fingers curled into mine as Tedda dangled limply in his grasp."

    # PDF p173
    dorian "Thank you for the warning. We'll heed your advice and leave immediately. Which exit should we take?"
    svante "Please exit through the main gate—the way you came. But hurry. There isn't much time."
    yuxuan "No, we're not going anywhere without those damned treats—"
    dorian "Yu, let's just go. Please. Come on. Elias."
    elias  "Oh… Okay, daddy."

    jump ch4_cemetery_exit


# =============================================================================
# SECTION 14: LABEL CH4_CEMETERY_EXIT — Memorial Gate Chaos
# =============================================================================
# PDF pages 173-178.
# The explosions begin. Mjoll soldiers. Niko and Tian Xun confrontations.
# =============================================================================

label ch4_cemetery_exit:

    # PDF p173
    # [COMMENT: bg_tianho_memorial_gate — people scrambling to leave, soldiers arriving]
    scene bg_tianho_memorial_gate with dissolve # PLACEHOLDER — memorial gate

    play music ost_cemetery_chaos fadein 0.5    # PLACEHOLDER — rising tension

    "We hurriedly made our way through the cemetery gates. We could see people doing the same – scrambling to get out."
    "We exited the gate, and Yuxuan is mad – furious, even."

    yuxuan "This is preposterous! I am Cheng Yuxuan, an inventor of great renown! I've contributed to the advancement of technology in countless kingdoms! And yet, here I am, herded out of a cemetery like some common criminal!"

    "I sighed, trying to keep my tone calm as I responded."

    dorian "We're not being treated like common criminals, Yu. Calm down."
    yuxuan "My work has changed lives, improved industries, and brought prosperity to this land! I've dedicated myself to progress, and now I'm being treated like some kind of threat? This is absolutely outrageous!"

    "Elias clung to my hand, his little giggles bubbling up despite the situation. He hugged Tedda close, whispering something to her while sneaking amused glances at Yuxuan."
    "I stepped closer, placing a firm hand on Yuxuan's shoulder to steady him. His rant came to an abrupt halt, and I noticed his cheeks flush an intense shade of crimson."

    yuxuan "…?!"

    "He looked at me, wide-eyed, almost frozen in place."

    dorian "Yu, calm yourself. We're going to be fine. Let's just go home."

    "Yuxuan blinked rapidly, his face growing even redder as he stumbled over his words."

    yuxuan "Ah. Um... Hehe, okay. T-Thank you, Dorian. I... Uh… appreciate your support. You always know how to, um, calm my nerves."
    dorian "Yu, are you okay? You seem... flustered."
    elias  "Mister Yuxuan, your face matches Tedda's color!"
    yuxuan "Wh-What?! No!!! I—"

    # PDF p174
    dorian "Come on. Let's keep moving."
    yuxuan "You're right. Let's go."

    # [COMMENT: bg_tianho_memorial — the cemetery itself, Niko and prophet being confronted]
    scene bg_tianho_memorial with dissolve      # PLACEHOLDER — back in memorial area

    niko    "You're kicking us out of here?! We have every right to be here!"
    svante  "Sir, please understand. This is for your safety. I must insist—"
    prophet "Safety? SAFETY?! We're here because we have brothers who died during the tragedy! This is sacred ground! How dare you kick us out?!"
    svante  "With all due respect, sir, this isn't my choice. These are orders. I assure you, this is for your own protection—"
    tian_xun "Protection? Bah! These fools don't deserve protection, Svante. If they won't leave willingly, I'll personally show them the consequences of disobedience!"
    svante   "S-Sir—"
    tian_xun "I could clear this whole area with one of my beauties, you know. One boom, and everyone's gone! It'd be a lesson in obedience, wouldn't it?"
    svante   "Sir Tian Xun. Please, that won't be necessary. Our goal was to—"
    tian_xun "Oh, but think of the possibilities, Svante! A controlled explosion right here and now—imagine it! One boom, and they'll scatter like frightened mice. Gustav would love it! BOOM! BOOM!"
    niko     "You've got to be kidding me. This lunatic works for Gustav? No wonder things are a mess."
    prophet  "Lunatic, indeed. You shame the name of Tianho, Tian Xun. I pity your parents. To see you now… what grief they must bear."
    tian_xun "Ashamed? HAHAHAHA! My parents were nobodies! Farmers!"
    tian_xun "What did they ever give me except poverty and a back-breaking life, old fool? Gustav gave me wealth, power, and the means to create. Go, my beauties! BOOM! BOOM!"
    tian_xun "They should be proud of me! But enough talk—get out before I decide to test my newest invention right here."
    tian_xun "GET OUT! OUT, OUT, OUT! BEFORE I GO BOOM!"
    niko     "Tsk…"
    prophet  "Come, brother Niko. There is no reasoning with this one. Let us go for now. But mark my words, this is far from over."
    svante   "I… I'm sorry."
    tian_xun "Run! Run, little lambs! HAHAHA!"

    # PDF p175
    tian_xun "Now come, Svante. We've got such lovely things to test today… Ooh!! I'm getting twitchy, temperamental, and itching to blow!"
    tian_xun "Hehehe~"

    # [COMMENT: bg_tianho_memorial_gate — Niko and prophet at the gate, aftermath]
    scene bg_tianho_memorial_gate with dissolve # PLACEHOLDER — memorial gate

    prophet "…"
    niko    "…"
    prophet "… Brother Niko?"
    niko    "Kaito… Please forgive me."
    prophet "Do not let this trouble you too deeply, brother Niko. Your brother's grave will still be here tomorrow. Nothing can take that away."
    niko    "I hope so."
    prophet "He knows, Niko. Kaito knows. The love you share transcends these fleeting moments. He understands far more than you give him credit for."

    elias   "Daddy, what about the treats?"
    dorian  "Let's get treats later when we get home. Come on."

    niko    "Hmm…"
    prophet "What is it, brother Niko?"
    niko    "Hmm… that toy… I remember…"
    niko    "Tedda… Wait, does that mean that the child is… Elias?"
    prophet "Elias? From Mjoll? Impossible. That boy was struck down by an arrow. We saw it with our own eyes!"
    niko    "Enoch probably intervened."
    niko    "And that means that man with the child… is Dorian."
    prophet "Dorian… Ex-paladin Dorian… By Enoch, you're right! I did not recognize him with that new hairstyle."
    niko    "The Dragon of Gale…"
    prophet "What are they doing here?"

    "The area was crowded with people—more and more of them rushing hurriedly away, their faces painted with unease."

    # PDF p176
    yuxuan "What is going on? Why is everyone acting like this?"
    dorian "Mjoll… What are they up to now?"

    "Yuxuan rolled his eyes, fiddling with his communication device."

    yuxuan "This is intolerable. I'm calling for our carriage. We're leaving this madhouse at once."

    girl_ald_soldier "WAIT! HE KNOWS!! HE'S GETTING AWAY!! AFTER HIM, NOW!!"
    tian_xun "What?! HE'S GETTING AWAY?! Bahaha, not on my watch! Fire the beauty—FIRE HER NOW!!"

    elias "Fire? What are they firing, daddy?"
    yuxuan "What are they talking about?"

    play sound sfx_explosion_boom               # PLACEHOLDER — explosion SFX

    "-EXPLOSION-"

    "Before any of us could comprehend what was happening, a deafening BOOM shattered the air. The shockwave hit us first, followed by the searing heat of the explosion."
    "The ground trembled violently beneath our feet as dirt and debris rained down from the blast."
    "Before any of us could comprehend what was happening, a deafening BOOM shattered the air. The shockwave hit us first, followed by the searing heat of the explosion."
    "The ground trembled violently beneath our feet as dirt and debris rained down from the blast."

    yuxuan "By the Prosperity Dragon! What was that?!"

    "Then… a voice boomed inside my head."

    chung_hee "People of Tianho! I have been tricked by Mjoll! They've ambushed me—please, I need aid!"

    yuxuan "Wait—I can hear it! I can hear his voice!"
    elias  "Daddy… can you hear it too? What's happening?"

    "I nodded grimly, gripping Elias's hand tighter."

    woman_1 "The man is asking for aid! But I can't stay here! I have children—I have to get home!"
    man_1   "Have you seen the number of soldiers here? I'm not risking my family for this!"
    man_2   "Not my fight! I'm sorry, but I'm not dying today!"

    "Despite the desperate plea ringing in our minds, the people around us fled without hesitation"

    # [COMMENT: bg_empty_battlefield — empty cemetery area, bodies beginning to fall]
    scene bg_empty_battlefield with dissolve    # PLACEHOLDER — empty battlefield

    # PDF p176-177 — Chung-hee's broadcast continues, battle begins
    chung_hee "Someone! Anyone! If you have honor, hear me! I seek only the king of Mjoll—this is my last warning. I do not wish to harm innocents!"
    aoi       "Such powerful mind channeling…"

    # PDF p177
    tian_xun  "Honor?! HAHAHA! Don't make me laugh! Someone like YOU, scot-free after MY masterpiece?!"
    tian_xun  "Impossible! A miscalculation like this… it's infuriating! You should've been a pile of ash by now! How did you survive, huh?!"
    tian_xun  "What you need is another! Another! BOOM! BOOM!"
    aoi       "Tian Xun, enough! The last thing we need is another one of your wasted bombs."
    tian_xun  "Grr…. You're no fun, Aoi."
    aoi       "Aldoriths, form up! His barriers won't last long. He's already at his limit."

    chung_hee "This is your last chance! I have no quarrel with you. I seek only your king. Stand aside, and no harm will come to you."

    mjoll_lars  "Your fight with our king is OUR fight, you fool. Do you think you can just waltz in and demand a duel?!"
    mjoll_helga "We've been waiting for a real fight. Your 'honor' doesn't scare us, Emperor. You'll die here like the rest of your kind."
    mjoll_pavel "You're outnumbered, outclassed, and out of luck. It's time you joined your ancestors."

    svante "…"
    boy_ald_soldier "Your blood will stain the land, Emperor! For Father!"
    svante "No… No, this isn't right."
    girl_ald_soldier "What?! What did you say?"
    svante "This man doesn't want to harm us! He's asking for a duel—he's giving us a chance to avoid more bloodshed! Please, don't let this end like this!"
    mjoll_lars "Are you… are you siding with him? You'd betray your own people?"
    svante "No! I'm trying to stop more deaths! This man hasn't done anything wrong!"
    svante "Father said that the Emperor is a dishonorable man who murders and kills innocents. Look at him! He's offering us peace! Will a dishonorable man do that?"
    aoi    "Bold of an aldorith to have an opinion. Your Father will know about this."
    boy_ald_soldier "You really want to end up like your sister Kristin, huh? Dead for nothing?"
    svante "All I'm saying is that this isn't the Emperor of Kyeongjang! He's far from him!"
    tian_xun "Oh, how touching! A traitor among the righteous. Let's see how your little 'peace talk' works against THIS!"
    aoi    "Tian Xun, stop! That's the last bomb we have!"

    play sound sfx_explosion_boom               # PLACEHOLDER — second explosion

    "-EXPLOSION-"

    # PDF p178
    tian_xun  "HAHAHAHA! BOOM! BOOM!"
    mjoll_helga "The barrier… it's still there!"
    chung_hee  "I didn't come here to spill blood. But if you force my hand…"
    aoi        "Tsk! We wasted the last bomb because of you, Tian Xun! Aldoriths—kill him!"
    tian_xun   "KILL BOTH OF THEM! LET BOTH OF THEIR HEADS BE MOUNTED ON A SPIKE!!"
    tian_xun   "CHARGE!! CHA- *coughs* CHARGE!!"
    svante     "Sir! What should we do?"
    chung_hee  "Run… Leave this place. You're not like them."

    scene bg_tianho_memorial_gate with dissolve # PLACEHOLDER — memorial gate

    "The ground trembled beneath us as the second explosion ripped through the air, sending debris flying in every direction. People screamed and scattered."
    "I grabbed Elias's hand tightly as we ran, Yuxuan leading the way with his communication device pressed against his ear."

    yuxuan "The carriage! It's here—it's at the front gate! But it can't get through!"

    "Elias stumbled."

    elias "Tedda! I dropped Tedda!"

    "He turned back, tears welling up in his eyes as he pointed toward the ground. There, a small stuffed bear lay in the dirt."

    elias  "We can't leave her! She's scared!"

    "I raised my hand. The ground shifted slightly as the earth responded to my will, lifting the bear from the dirt and bringing it quickly to my hand."

    dorian "There. Tedda's fine now. Let's go."

    "Then, we saw that the carriage was in sight—but so were they."
    "Three soldiers from Mjoll stood near the carriage, their armor gleaming in the afternoon sun. All of them were arguing with the driver."

    man_1           "We need this carriage. It's ours now. Get off!"
    carriage_driver "I don't care who you are—I was called to pick Master Yuxuan up! This is the property of Cheng Industries!"
    man_2           "Hey, buddy. We can do this the easy way, or we can do this the hard way. Your choice."

    # PDF p179
    female_guard    "Get out of there if you know what's good for you!"
    carriage_driver "Ahh!! Okay! Okay!"

    "The second soldier turned, spotting us as we approached. His hand shot to his weapon—a jagged blade that glinted in the light."

    female_guard "Looks like they're here."
    yuxuan       "Hey! Step away from the carriage! That's the property of Cheng Industries!"
    man_2        "If you're smart, you know better than to fight us. Find another way out."
    elias        "Daddy… They look scary…"
    dorian       "You're not taking this carriage. We have a child with us."
    female_guard "And? You think we care about your kid? This carriage belongs to King Gustav now."

    "I clenched my fists, feeling the familiar hum of power coursing through me. The ground beneath my feet shifted slightly, small cracks forming as my frustration grew."

    dorian "This carriage doesn't belong to you. Step down now, or you'll regret it"
    man_1  "A channeler, huh?"
    man_2  "You don't scare me, pal. Now beat it!"

    "The soldier in the driver's seat cursed, trying to pull the reins, but the carriage didn't budge. The horses, too petrified, didn't budge."

    female_guard "What?"

    dorian "Step aside. Now."

    "The second soldier stepped toward me, blade raised."

    man_2 "Why I oughta! Someone ought to teach you some manners!"

    play sound sfx_heartbeat loop               # PLACEHOLDER — tension

    # =========================================================================
    # D1 — Quick Timed Choice: Channel Earth or Do nothing / Yuxuan help
    # PDF p179-180
    # =========================================================================

    menu:

        "Channel Earth.":
            $ ch4_carriage_qtc1 = "earth"
            stop sound

            play sound sfx_earth_pillar         # PLACEHOLDER — earth pillar SFX

            "I stomped the ground. The earth buckled beneath the soldier's feet, a jagged pillar shooting up and knocking the blade from his hands."
            "His head hit the ground, knocking him unconscious."

            # PDF p180
            dorian "You were warned."

        "Do nothing. Yuxuan, help!":
            $ ch4_carriage_qtc1 = "sleep_powder"
            stop sound

            "I froze, panic gripping me as the soldier's blade gleamed dangerously close. My breath caught in my throat."
            "Before I could react, Yuxuan reached into his satchel and flung a small pouch at the soldier. It burst mid-air, releasing a fine, silvery powder."

            man_2  "Zzz… Zzz…"
            yuxuan "Sleep powder. Courtesy of Cheng Industries. I knew this would come in handy!"

    # D1 converge — PDF p180
    female_guard    "This one's trouble! Fall back!"
    man_1           "Grr…. Hurry! Pull the reins again! Let's get out of here!"

    "The soldiers scrambled onto the carriage, yanking the driver out of the seat. The female soldier grabbed the reins, cracking them hard, and the horses began to pull away."

    carriage_driver "You can't do that! No!"

    play sound sfx_heartbeat loop               # PLACEHOLDER — tension

    # =========================================================================
    # D2 — Quick Timed Choice: Stumble or Use wind
    # PDF p180-181
    # =========================================================================

    menu:

        "Stumble! Elias, help!":
            $ ch4_carriage_qtc2 = "stumble"
            stop sound

            "I tried to focus, summoning the energy to stop them—but my foot caught on a loose rock, and I fell flat on my face."

            yuxuan "Dorian!"
            elias  "Tedda! Protect us!"

            "Elias flung his stuffed bear with all his might. The toy hit the female soldier dead in the face as she was laughing, specifically her mouth."

            # PDF p181
            female_guard "Pfttt—Waahhh!! Eww!!"

            "She flailed, grabbing at the reins, but the sudden commotion startled the horses. They reared up, neighing loudly."
            "The male soldier shouted, pulling on the reins to regain control."

            man_1 "Stop! WHOA!"

            play sound sfx_carriage_crash       # PLACEHOLDER — carriage crash

            "The carriage lurched violently to the side, its wheels hitting a large rock. The entire thing tipped over, spilling the soldiers onto the ground in a cloud of dust and splinters, knocking them unconscious."

            elias  "Tedda! We did it!"
            dorian "Remind me never to underestimate that bear."

        "Use wind to knock them off!":
            $ ch4_carriage_qtc2 = "wind"
            stop sound

            play sound sfx_wind_blast           # PLACEHOLDER — wind SFX

            "I planted my feet firmly and reached deep, calling on the winds. They roared to life around me, whipping through the air like an invisible storm."
            "With a sharp motion of my arm, the wind blasted toward the carriage."
            "The gust struck the soldiers with brutal force, knocking them clean off the back. They landed on the ground, knocking them unconscious."

    # D2 converge — PDF p181
    carriage_driver "Please, get in!"

    scene cg_black with dissolve               # PLACEHOLDER — black screen transition

    "The three of us hurriedly got inside the carriage. The driver pulled on the reins and went on our way."
    "The carriage wheels rumbled beneath us, the city's chaos fading behind as we sped toward safety. I exhaled, the tension in my shoulders easing slightly, though my mind was still racing. Yuxuan sat across from me, as he held Elias close."

    elias  "Daddy… are we safe now?"

    "I reached over and gently ruffled his hair."

    dorian "Almost. We're getting out of here."

    jump ch4_battlefield


# =============================================================================
# SECTION 15: LABEL CH4_BATTLEFIELD — Dorian Finds Chung-hee
# =============================================================================
# PDF pages 182-184.
# =============================================================================

label ch4_battlefield:

    # PDF p182
    "But then, as we turned a corner, we saw it."
    "The area near the cemetery was littered with bodies—armored individuals sprawled across the ground, their blood staining the dirt. Some were barely moving, others entirely still. The once-sacred space now looked like a battlefield."
    "In the center of it all, a young man stood in the middle. His chest rose and fell unevenly, his breaths labored and ragged. His right hand clutched at his side, blood seeping through his fingers, and his left arm hung limply at his side."
    "His face was pale, slick with sweat and dirt, but what caught my attention most was his eye, which glowed faintly, pulsing with an unnatural light that flickered with each breath he took."

    "Then, a voice filled my head again."

    chung_hee "I beg… of you… Please… help… me…"

    "I froze, staring at him as the carriage slowed. He stumbled forward, his legs barely holding him up, and his eye flickered as if struggling to stay alight."

    chung_hee "Hurry… please. I've exhausted my powers… More of them… might come. I—"

    "Before he could finish, his knees buckled, and he crumpled to the ground. His body hit the blood-soaked dirt with a sickening thud, and for a moment, everything was still."

    dorian "He needs my help. I have to help him, Yu."
    yuxuan "What?! Don't even think about it. We have Elias to protect. He's not our problem. We shouldn't involve ourselves with them!"
    elias  "Daddy… he's hurt. Are we… are we going to help him?"
    dorian "I have to."

    carriage_driver "Sir, I don't think we should stop. More of those armored ones could show up any second."

    "I looked back at the young man lying in the dirt, his form so still now, as though even breathing was too much effort. His aura was faint, flickering like a dying ember, but it was still there, waiting."

    dorian "We can't just leave him."
    yuxuan "And risk our lives—and Elias's—for a stranger? Dorian, please!"
    dorian "Yu, if it was you or Elias there, I would do anything to help."
    yuxuan "Dorian…"
    dorian "Please, Yu. Take Elias to safety and stay out of harm's way. I'll do everything I can to ensure I'm not caught up in something dangerous."
    yuxuan "Fine. Meet me at my house, please. Just stay safe, Dorian. Promise me."

    # PDF p183
    dorian "I promise. Stay safe. You too, Elias."

    "Without another word, I opened the carriage door and jumped down."

    # [COMMENT: bg_empty_battlefield — scattered bodies, blood on dirt, burnt earth]
    scene bg_empty_battlefield with fade        # PLACEHOLDER — empty battlefield

    "As I hurriedly made my way over the scattered bodies in the aftermath of the confrontation, I walked over the bodies of the fallen. The bodies, clad in bloodied armored attire, lay scattered like fallen soldiers on a battlefield."
    "One… four… eight… twelve…"
    "The air was thick with the metallic tang of blood, mingled with the acrid stench of burnt earth. It was suffocating. It was familiar."

    # [COMMENT: bg_frostcradle_bloodied — same as ch3 bloodied frostcradle — memory flashback]
    scene bg_frostcradle_bloodied with dissolve # PLACEHOLDER — Frostcradle bloodied (memory)

    "Too familiar."
    "Memories came flooding back – horrible ones."

    boy_ald_soldier  "Mercy!! Enoch save me!! Ahhh!!"
    girl_ald_soldier "We're just obeying orders! Don't kill us!! Ahh!!"
    dorian           "…"

    "I clenched my fists, forcing myself to push the memories aside. I darted past the remaining bodies and reached the young man."

    # [COMMENT: bg_empty_battlefield — back to battlefield]
    scene bg_empty_battlefield with dissolve    # PLACEHOLDER — empty battlefield

    "His pale body was riddled with deep gashes and bruises, his torn clothes clinging to him in blood-soaked tatters. His chest rose and fell unevenly, each labored breath rasping."
    "I knelt beside him, my heart pounding in my chest as I reached out. His skin was icy cold to the touch, his face drenched in sweat. He was fading—fast."
    "Then I felt it."
    "A faint flicker of energy pulsed weakly from him, like the dying ember of a once-roaring flame. His aura was dim, fragile, and almost extinguished. Whatever power he once had was completely drained."

    dorian "This is bad… this is really bad…"

    "He needed a doctor. Now."

    # PDF p184
    dorian "Listen to me. The clinic—it's a little far from here, but I'll carry you. Just hold on, alright? I'll do what I can."

    "I slipped my arms beneath his frail, battered body, carefully lifting him. His head lolled limply against my chest, his weight alarmingly light."
    "As I straightened, preparing to run, a soft, barely audible voice reached my ears."
    "A whisper? No… it was something else."

    niko_raven "Does he have a pulse?"

    "I froze, my eyes darting around."

    dorian     "Who said that? Hello?"
    niko_raven "Hello, I'm here. Does he have a pulse? Please check his pulse."

    jump ch4_niko_raven


# =============================================================================
# SECTION 16: LABEL CH4_NIKO_RAVEN — Niko the Raven / Healing Chung-hee
# =============================================================================
# PDF pages 184-187.
# [# 25 – Until "I stumbled back…"]
# =============================================================================

label ch4_niko_raven:

    # PDF p184-185
    # [# 25 – Until "I stumbled back…"]
    "My gaze snapped to the source—a raven perched on a jagged piece of debris. Its jet-black feathers gleamed unnaturally under the faint light, and its beady eyes locked onto mine."
    "A talking raven? I blinked, rubbed my eyes, and looked again, half-convinced I was hallucinating from the stress."
    "The bird let out an exasperated sigh—an actual sigh."

    niko_raven "*sighs* Can you check his pulse now, please?"

    "Still doubting my sanity, I hesitated, then followed the raven's oddly calm advice. Gently, I pressed my fingers to the young man's wrist, feeling for the faint rhythm of life. His pulse was there—weak, erratic, but there."

    dorian     "He's still holding on. But if I don't get him to a doctor soon, he won't make it. The nearest clinic is—"
    niko_raven "Hold on a second. I'll help you."

    "Before I could react, the raven's feathers began to shimmer with an ethereal, silvery glow. Its form trembled and warped, the light intensifying with each passing second."
    "I stumbled back, clutching the young man tightly as the raven's body began to change. Feathers melted into skin, and wings elongated into arms."
    "Standing before me, where the raven once perched, was a tall, striking figure—a person."

    dorian "What the…"

    "He wasted no time, dropping to his knees beside the unconscious young man. His movements were fluid yet precise, every motion purposeful."

    # PDF p185
    "He pulled a small satchel from his side and opened it, revealing an assortment of seeds, dried herbs, and vials filled with mysterious liquids."

    niko "His pulse is weak, but he's still hanging on. Good. That gives me something to work with."

    "He plucked a few seeds from the satchel and cupped them in his hand. Closing his eyes, he took a deep breath, and I felt a strange energy ripple through the air."
    "The seeds began to sprout, tiny shoots unfurling as though sped up by years in mere seconds. Vines and leaves stretched forth, twisting around his fingers before blooming into vibrant, fragrant flowers."

    dorian "Nature channeling… I've never seen one channel nature before."

    "He snapped the petals from one flower and crushed them between his palms, creating a paste that glowed faintly green. Without hesitation, he applied it to the worst of the young man's wounds, smearing it into gashes and bruises with the deftness of someone who had done this countless times before."

    dorian "What… what are you doing?"
    niko   "He's losing blood too quickly. The paste will slow the bleeding and encourage his skin to knit itself back together."

    "He crushed another leaf, mixed it with water from a vial, and poured the liquid into the young man's mouth with careful precision."

    dorian "Is that safe? He can barely—"
    niko   "It's a tonic. It'll keep his organs from shutting down. If you're so worried, please help me keep his head steady."
    dorian "Got it."

    "I obeyed, holding the young man's head as Niko worked. His hands glowed faintly with energy, the aura spreading into the young man's wounds as he muttered soft words under his breath—spells? Prayers? I couldn't tell."

    niko "His channeling energy is still fragile. His body is trying to give up, but I'm not letting it. Not yet."

    "He reached for a final seed, planting it near the young man's head. It grew instantly into a flower with soft, golden petals. Niko plucked one and crushed it between his fingers, letting its essence drip onto the young man's mouth."
    "The glow seeped into his skin, and for a moment, the young man's breathing grew steadier. I could feel his aura growing a little stronger."

    dorian "Amazing…"
    niko   "This will stabilize him for now, but he needs real rest—immediately. If another fight breaks out, he won't survive it."
    dorian "Who are you? And did this man… did he talk to you too?"

    # PDF p186
    niko   "Yes, this man reached out to me. To everyone within the vicinity of Tianho cemetery, I believe. Very potent mind channeling, no doubt."
    dorian "And only the two of us came to his aid?"
    niko   "I'm afraid so, yes."
    niko   "He's from Kyeongjang. You won't find anyone else on Ena with a power like that."

    "He extended a hand, his expression softening slightly."

    niko   "I'm Niko. Niko Tsukumo. I'm in service to the death god, Enoch. It's a pleasure to finally meet you one-on-one, Paladin Dorian."

    "I shook his hand, his grip firm but warm."

    dorian "Niko… Have we met before?"
    niko   "We have. Five years ago. I was with my younger brother, Kaito. We crossed paths here in Tianho when you were with Paladin Cyrus."

    "His words startled me."

    dorian "I don't recall. I apologize."
    niko   "Don't apologize. It's been a long time."
    dorian "You're a nature channeler. I take it you're from Clan Ligaya?"
    niko   "Contrary to popular belief, not every nature channeler hails from Clan Ligaya. My mother is from Clan Kaibig—the sister clan to Ligaya—and my father is from Hamatame, the village of shadows."

    jump ch4_svante_capture


# =============================================================================
# SECTION 17: LABEL CH4_SVANTE_CAPTURE — Svante Caught / Yuxuan Returns
# =============================================================================
# PDF pages 186-189.
# =============================================================================

label ch4_svante_capture:

    # PDF p186
    "Then, a flicker of movement caught my eye. My instincts kicked in, and I turned sharply, spotting the same young man who had warned us to leave earlier."
    "The moment he noticed my gaze, his eyes widened in panic."

    svante "…!"

    "He turned on his heel and bolted."
    "I held my palm outward. The ground beneath us shifted and groaned in response to my will, rising up to form solid restraints that coiled around his legs like vines."
    "He stumbled, crashing to his knees as the earth held him in place."

    svante "Please! Let me go! I'm not here to hurt you!"

    "He writhed against the restraints, his voice trembling. But I didn't let up."
    "I strode toward him."

    dorian "You knew something was going to happen here. Start talking. Now."

    "His breath hitched, his wide eyes darting between me, Niko, and the unconscious man."

    # PDF p187
    svante "I... I don't know everything. They didn't tell me much, but—"
    niko   "But you were with that lunatic. You and your group tried to drive me and my fellow prophet away! Don't act innocent now."
    svante "It wasn't like that! I was trying to help you! Please, you have to believe me!"
    niko   "Help us? By threatening us? You're making this a lot harder for yourself, you know."
    svante "I wasn't threatening you! I was trying to save you! If you'd stayed, you'd be dead!"
    svante "They'll kill anyone who gets in their way. I… I didn't want to be part of this."
    niko   "Then why were you here at all? You could've walked away. Who are you anyway?"
    svante "M-My name's Svante, sir. Please don't hurt me. I s-surrender."
    svante "I-I wanted to help him… and you don't understand. I can't just walk away from them! They'd come after me! I—"

    elias  "Daddy!!"

    "To my utter surprise, Yuxuan and Elias came running towards me. Yuxuan was panting heavily, his hands on his knees as he struggled to catch his breath."
    "Elias crashed into me clinging to my leg as though his life depended on it. His small body trembled, and when I knelt to pull him into my arms, I could feel his rapid heartbeat against my chest. He was clutching Tedda in his one hand."

    dorian "Yuxuan?! What in Tetrad's name are you doing here?! You should be at the carriage!"

    "Yuxuan straightened, his face pale as he blurted out the words in a frantic rush."

    yuxuan "Dorian, we-we have a problem! There's an army—a whole battalion of Mjoll soldiers—heading this way! We're surrounded!"
    dorian "What?!"
    svante "I tried to warn you! You should've run when you had the chance! Now we're all going to die here!"
    yuxuan "Dorian, what are we supposed to do? We can't fight them all, but we can't stay here either! We're trapped!"
    dorian "You shouldn't have come back! You should've gotten the child out of here! What were you thinking?!"
    yuxuan "Dorian, we're not leaving you behind. We're in this together, no matter what."
    elias  "Daddy, I wanted to be with you! I won't leave you, daddy!"

    "I groaned and opened my mouth to answer, but the sound of distant boots—hundreds of them—marching in unison filled the cemetery air."

    # PDF p188
    niko   "Calm down. How many soldiers did you see?"
    yuxuan "I... I don't know. There were so many of them—it looked like an entire battalion! Maybe more!"
    niko   "We can't stay here. We have to move. Now."
    yuxuan "Move where?! I just told you! We're surrounded! Every path out of this cemetery is crawling with Mjoll soldiers!"

    man_1  "We have you surrounded! Surrender now and you might live to see another day. Resist, and you'll meet a swift end!"
    yuxuan "W-We surrender! Please! Don't hurt us!"

    "Before he could fully raise his hands, I grabbed his shoulder and yanked him back."

    dorian "Yu, no need to surrender."
    svante "He's right! If we surrender, we're as good as dead! They won't let us walk away, not after this. We have to fight or die!"

    man_2  "Come out with your hands up! All of you! We won't ask again!"

    "A commanding female voice cut through the voices of the soldiers like a blade."

    aoi    "Back-up has finally arrived, Tian Xun. As for you lot—what took you so long?"

    "The soldiers straightened up immediately, some even flinching at her tone."

    man_1     "S-Sorry, mam Aoi! It won't happen again!"
    tian_xun  "HAHHAHAHA! Oh, but it better not! Because if I have to wait one more agonizing second for a BOOM, I might just detonate myself for fun! My darlings were perfectly timed and they ruined it! THEY RUINED IT!!"
    tian_xun  "I want fireworks! I want limbs flying! I want screams and smoke!"

    "At the corner of my eye, I saw her. The woman was about Yuxuan's stature. Water circled faintly around her fingers, as if drawn to her by instinct."
    "A water channeler."

    female_guard "We were under the impression that the—"
    aoi          "Save your excuses. Kill the target."
    female_guard "What about the others, mam?"
    aoi          "I don't care for them. Just make sure that the target is dealt with. As for the others, dead or alive—it's up to you."
    tian_xun     "NO! KILL THEM! LEAVE NO SURVIVORS! THEY FOILED MY BEAUTIES!"
    tian_xun     "LEAVE NONE! NOT A SINGLE ONE!"

    # PDF p189
    "A man stormed into view, his movements erratic and exaggerated, his face twisted into an expression of obsessive rage."

    tian_xun "My cannons! My beautiful cannons! They ruined everything! Do you know how long it took me to design those? The fuses, the powder, the precision—ruined!"

    "He stomped his foot like a child throwing a tantrum, then pointed a trembling finger in our direction."

    tian_xun "ESPECIALLY THE TARGET!! HE WASTED MY BOMBS!"

    "The lady rolled her eyes. She glanced at him, her expression one of thinly veiled disdain."

    aoi      "Calm down, Tian Xun. For someone from Tianho, you're embarrassing yourself."
    tian_xun "Embarrassing?! You don't understand! The cannons were my masterpiece! My explosions! You can't just… replace art like that!"
    aoi      "You were the one who wasted your own bombs! Ugh!"
    aoi      "But enough. Focus on the task at hand. Your tantrum can wait."
    tian_xun "This is not a tantrum, Aoi! NOT A TANTRUM!!"

    "Tian Xun muttered something under his breath, his fingers twitching."

    tian_xun "I'M GONNA MAKE THEM BOOM… GONNA MAKE THEM ALL GO BOOM… HAHAHA…"

    "From our vantage point, I could see the soldiers shuffling nervously. Aoi's cold demeanor and Tian Xun's volatile nature were enough to unsettle even seasoned warriors."
    "I tightened my grip on Yuxuan's shoulder and glanced down at Elias, who clung to my leg."

    svante "They're going to shoot any minute now. Take cover!"

    "My chest tightened. The unconscious man, barely clinging to life, lay vulnerable on the ground. Thanks to Niko, his condition has improved, but any attack would almost certainly finish him."

    elias "D-Daddy!"

    "The lady raised her arm, her voice slicing through the tense air like a blade."

    aoi "Ready! Aim! Fire!"

    play sound sfx_arrow_volley                 # PLACEHOLDER — arrow volley SFX

    "In an instant, a volley of arrows darkened the sky, their deadly tips glinting like shards of ice in the pale light. The sound of bowstrings snapping echoed through the cemetery, followed by the sharp whistling of arrows slicing through the air."
    "Before anyone could react, Svante stepped forward, his arms raised as if commanding the battlefield itself. He furrowed his brow."

    svante "Everyone, get back!"

    # [# 27 Until "The ground shook"]
    # PDF p190
    play sound sfx_metal_barrier                # PLACEHOLDER — metal barrier SFX

    "A shimmering metallic sheen erupted from the ground around him, forming a barrier that expanded outward."
    "The arrows struck the gleaming shield with a series of sharp clangs, ricocheting off harmlessly. Sparks flew as the metal deflected each projectile with precision, bending and twisting under Svante's control."

    elias  "Daddy, get back! Get back!"

    "I pulled him behind me, my heart pounding as I watched Svante deflect every single arrow."

    yuxuan "By the Prosperity Dragon… I didn't think anyone could do that."
    niko   "A metal channeller, huh? Interesting…"

    "He tilted his head, studying Svante with a sharp gaze."

    niko "You don't see that very often around here in Ena."

    "I had heard stories of metal channelers — but I've never seen one before. It was a rare gift."
    "The soldiers and remaining aldoriths hesitated for a moment, stunned by the display of power, but their shock quickly gave way to fury."

    tian_xun     "GRRRR… THAT HANDSOME VIOLET-HAIRED BOY IS HELPING THEM!! CURSE YOU SVANTE!!"
    boy_ald_soldier "S-Svante's helping them!"
    man_1        "Grr…. You think you can defy us?"
    female_guard "He's helping them! That traitor! Father will be angry!"
    man_2        "Hmph. That means we have to take care of him, then. Second artillery units, ready… aim… fire!"

    "The ground shook as the soldiers prepared to launch a second wave of attacks. Meanwhile, the distinct clatter of hooves thundered in the distance, growing louder with every passing second."

    mjoll_helga "Arrow units! Continue to shoot! Keep firing! Overwhelm them!"

    "The lady raised her hand once more."

    aoi "Cavalry units! Advance! Run them down!"

    "The cavalry surged forward, a wall of armored soldiers mounted on warhorses, their lances glinting under the moonlight. The ground quaked beneath the thunder of hooves."

    tian_xun "YES! YES! ATTACK!"

    "As I prepared to act, readying my earth channeling to create a defense, Niko stepped forward. He knelt briefly, bowing his head and clasping his hands together as though in prayer. His voice was soft at first, almost a whisper, uttering words."

    # PDF p191
    niko "Kuroi yami no chikara… watashi no michibikite. Chikara o ataete… Enoch-sama no tame ni."

    "His words grew louder, and I can see pulses of dark energy surrounding him as he spoke."

    niko "Chikara o ataete… Enoch-sama no tame ni."

    # [# 26 Until Tian Xun says "YES!! YES!! HAHAHA"]
    play sound sfx_shadow_surge                 # PLACEHOLDER — shadow surge SFX

    "A pulse of shadow erupted from his body, snaking through the air like living tendrils. The shadows coiled and writhed, stretching toward the oncoming cavalry with an unnatural speed."
    "As the darkness reached them, it engulfed the soldiers and their horses, twisting around them like black flames."

    man_1        "What the?! Is that the power of the death god?! I don't want to die! I don't want to die!"
    mjoll_lars   "Get a grip, aldoriths! Father will remove all our heads if we return without results!"
    mjoll_helga  "But what should we do, brother?"

    "The horses reared back, their eyes wide with terror as the shadows wrapped around their legs. The soldiers, trapped in the suffocating darkness, screamed in fear, their weapons slipping from their hands."

    female_guard "Ahhh!! Tetrad save me!"
    mjoll_lars   "Ahhh!!"

    "The shadows seemed alive, hissing and whispering as they consumed the light around them."
    "Niko stood tall, his figure wreathed in a shroud of creeping shadows."

    aoi    "T-The death god?! So, they have a Death God's priest among them… No matter. Regroup and attack again!"

    "But her words fell on deaf ears. The soldiers and aldoriths stood frozen, their weapons shaking in trembling hands. Some dropped to their knees, bowing their heads in reverence, as if pleading for forgiveness."

    man_2        "Enoch, please forgive us! *cries* Have mercy on our souls!"
    female_guard "We're doomed! He's marked by the Death God Himself!"
    tian_xun     "WHAT?! What in the Prosperity Dragon's radiant name are all of you doing? Get up! Get up if you know what's good for you!"

    "The once-organized battalion had devolved into chaos, their fear tangible as they scrambled in disarray. Aoi's frustration boiled over, her composure unraveling as she clenched her fists."

    aoi "This is preposterous! What kind of power are we dealing with here?!"

    tian_xun "Preposterous? No, no, my dear Aoi. This is art! This… is genius! HAHAHA!"
    aoi      "Tian Xun, what are you doing?! We need to regroup, not stand around laughing like a madman!"

    # PDF p192
    tian_xun "Regroup? Oh no, no, no. This isn't the time to fall back, Aoi. This is the time to show them true power. It's time for my masterpiece!"
    aoi      "Wait… That's not…"
    tian_xun "YES!! YES!! HAHAHAHAHA!!"
    aoi      "You're insane! You can't use that here, Tian Xun! You'll destroy us all!"
    tian_xun "Destroy us? Oh, Aoi, don't be so dramatic. This. Is. Progress! This is the culmination of my Tianho roots, my art! Draconic fire, distilled into its purest, most destructive form!"

    "From beneath his robe, Tian Xun pulled out a small, ornate container. It was carved with intricate dragon motifs that seemed to writhe and twist as the light played over them. A faint, fiery glow seeped from its seams, pulsating like a heartbeat."

    aoi      "Are you daft?! Do you even understand what you're holding?!"
    tian_xun "Legends state that draconic fire can only be channeled by those who are direct descendants of the ancient dragons. The late King Long Shen possessed one… but my father took it before the tragedy. And now, it is mine."

    "He pressed his lips to the container, kissing it."

    tian_xun "A gift from the Prosperity Dragon itself… My eternal muse. My guiding light."
    aoi      "Tian Xun, stop this madness! You can't—"
    tian_xun "Madness?! Madness would be not using this! Do you comprehend what failure means, Aoi? Do you?!"
    aoi      "…"
    tian_xun "Failure means King Gustav will have our heads mounted on his throne like trophies! Would you want that?"
    aoi      "Fine… Fine. Do it. Use it."
    tian_xun "Oh, you'll see, Aoi. You'll all see. Prepare my final beauty—the crescendo of my genius! BOOM! BOOM! HAHAHA!"
    aoi      "I'll get the other battalion of soldiers. Make sure you don't miss this time, okay? You two! Come with me."
    mjoll_lars  "Mam!"
    mjoll_helga "Yes, mam."

    "Svante turned to us, his form trembling."

    # PDF p193
    svante "Tian Xun… He… He's preparing another bomb!"
    niko   "He's the lunatic who kicked us out of Tianho, isn't he? Everyone, stay close! The shadows will protect—"
    svante "No! This isn't just another bomb! He's using his best from his personal collection… it's made of draconic fire!"
    dorian "!?"
    niko   "Draconic fire?! Are they really that desperate to kill us?!"
    niko   "If they're not careful, they'll blow this entire place to ashes!"

    "I stepped forward, clutching Elias protectively to my side as my mind raced."
    "The air grew heavier, a stifling presence of dread pressing down on all of us as we watched Tian Xun. His figure stood atop a platform."
    "His voice rose in a demented crescendo, echoing through the field."

    tian_xun "Oh, Prosperity Dragon, hear me now, your loyal servant! I offer this moment, this explosion, as a symphony to your grandeur!"
    tian_xun "Let your draconic fire consume the unworthy! Burn for me, my deity! BURN FOR GLORY! BURN FOR ART! BOOM! BOOM! HAHAHAHA!"

    "Suddenly, the air around us shifted. A deafening roar erupted from the container as something massive was hurled into the sky. The glowing projectile screamed toward us with terrifying speed, trailing an inferno of searing light and heat."
    "The ground trembled beneath our feet, and the very air seemed to vibrate with the power of the draconic fire. It wasn't just a bomb—it was a living, breathing entity, roaring with ferocity as it descended toward us."

    tian_xun "BEHOLD! DRACONIC FIRE! A MASTERPIECE BORN FROM THE PROSPERITY DRAGON!"

    "The projectile grew closer, its heat searing even from afar."

    niko   "Argh… Everybody! Get down!"
    svante "Almighty Enoch… Please save me…"
    boy_ald_soldier "Let's see how your metal powers save you from this one, Svante, dear brother."
    female_guard    "Haha! Look at him! He's terrified! The traitor aldorith will die at last!"
    man_1           "He'll die like the snake that he is. Nothing can save him now."
    tian_xun        "DIE!! DIE!! DIE!! ALL FOR THE PROSPERITY DRAGON!!"

    jump ch4_prosperity_dragon


# =============================================================================
# SECTION 19: LABEL CH4_PROSPERITY_DRAGON — White Screen / Prosperity Dragon
# =============================================================================
# PDF pages 194-197.
# Quick Time Choice — only "Remember yourself" (choice 4) leads to the correct path.
# =============================================================================

label ch4_prosperity_dragon:

    # PDF p194
    scene cg_prosperity_dragon_white with fade  # PLACEHOLDER — white screen, dragon presence
    play music ost_prosperity_dragon fadein 0.5 # PLACEHOLDER — divine dragon theme

    "Suddenly, time seemed to stand still. Absolute silence."
    "I closed my eyes. Is this it?"

    prosperity_dragon "My child…"

    "My breath hitched. That voice—it was unmistakable."

    dorian            "…?"
    prosperity_dragon "It has been far too long since you last called upon me. On your own volition."
    dorian            "I…"
    prosperity_dragon "Tell me, child, what is it that you desire? What compels you to reach out to me after so long?"

    "I swallowed hard, my voice trembling as I replied."

    dorian "Please… You know what I need."
    prosperity_dragon "Speak it! Acknowledge what you seek. Do not make me drag it from your lips like a coward's confession."
    prosperity_dragon "I know all who carry my blood, all my offspring. I know what burns in your heart. But I will hear it from you, Dorian. Say it with conviction and do not dance around the truth!"

    "I clenched my fists, forcing myself to confront the desperation clawing at my soul."
    "Elias… Yuxuan… Those who I hold dear."
    "I want to protect them."

    dorian            "I… I need your power. Please… grant me your power again."
    prosperity_dragon "My power. How easily you forget, Dorian."
    prosperity_dragon "You have forgotten who you are! Ever since your family was torn from you… ever since the you've worked as a mercenary in Mjoll… you have turned away from what you were born to be."
    prosperity_dragon "You have forsaken your very essence. My power is your birthright, and yet you shun it!"

    "The air ignited around me. Small embers flickered to life, swirling in a growing storm of heat and light. They multiplied rapidly, transforming into a sea of flames that enveloped me."
    "The heat was blistering, but it didn't burn—it was familiar, like an old friend."
    "The flames danced in hues of crimson, gold, and orange coiled around my hand."
    "Just like before."
    "And then, a memory."

    # PDF p195
    "The yaoguai king's hand, stained with blood, holding Elara's severed head high like a trophy. The screams of my children echoed in my ears. The emptiness in their eyes as they lay lifeless before me."

    yk     "The Dragonkin... I've been searching for you. At last, I've found you."
    dorian "Elara… Daniel… Emily… Sarah… Lucas… My family…"

    "The flames around me surged. Tears blurred my vision."

    dorian            "If only… If only I had been strong enough…"
    prosperity_dragon "Enough!"
    prosperity_dragon "My blood runs in your veins. My power is your power. You are not weak. You are not broken. You are DRAGONKIN! You only need to accept it—to welcome it as you did before!"

    "My hands shook."
    "Elias… Yuxuan… The ones that I care about…"

    dorian "They might be put in danger because of me. I—"

    "I could feel the heat. The draconic fire."
    "The bomb. It was approaching."

    prosperity_dragon "The bomb… Channel your power, Dorian! Take control! Remember yourself. Remember your heritage. Remember who you are."
    prosperity_dragon "The bomb… Channel your power, Dorian. Remember yourself. Remember your power."

    dorian "I…"

    "The flames surrounding me grew brighter, hotter, more intense."
    "I close my eyes, my trembling hand hovering over the flames. All of my memories surge forward, each vying for my attention."

    $ ch4_draconic_choice = ""
    play sound sfx_heartbeat loop               # PLACEHOLDER — tension

    menu:

        "Remember the tragedy of Tianho.":
            $ ch4_draconic_choice = "tianho"
            stop sound

            # PDF p195-196
            "The tragedy of Tianho—the screams, the chaos, the flames engulfing the city as people cried out."
            "I saw their faces: desperate, terrified, looking to me as if I were a god who could fix everything. I wasn't. I was powerless. I failed them."
            "The fires consumed the city that day. My hands still carried the ash of that failure."

            dorian "I'm sorry… I'm so sorry…"

            jump ch4_bad_end_bomb

        "Remember your family.":
            $ ch4_draconic_choice = "family"
            stop sound

            # PDF p196 — choice 2 or Nothing
            "Their laughter echoed in my ears. Elara's warm smile as she held Lucas in her arms. Daniel teaching Emily how to channel her first flame, the two of them bickering playfully as Sarah tried to mediate."
            "I could see them all so clearly. Elara's hand brushing against my cheek, her voice soft as she whispered to me:"

            elara  "You've done enough, love. Just rest. Rest with us."
            dorian "Elara… I wasn't strong enough… I couldn't save you. I couldn't save any of you!"

            jump ch4_bad_end_bomb

        "Remember the people who died at Mjoll because of you.":
            $ ch4_draconic_choice = "mjoll"
            stop sound

            # PDF p196 — choice 3
            "Their faces haunted me too. The aldoriths of Mjoll and… how could I forget? Vasily."
            "My power unleashed recklessly. I only defended myself and Elias but…"

            vasily "My friend… How could you kill me?"
            dorian "Vasily… Friend, I… I didn't mean to! Forgive me…"

            jump ch4_bad_end_bomb

        "Remember yourself.":
            $ ch4_draconic_choice = "self"
            stop sound

            # PDF p196-197 — choice 4 — correct path
            "I closed my eyes, letting the voice of the Prosperity Dragon wash over me. The flames burned brighter."

            dorian "The Dragon of Gale…"

            "The memories surged like a tidal wave, crashing into me. The battlefield roared with the echoes of my past victories."
            "But that was before the tragedy. Before the yaoguai king. Before I failed my family. Before I let the weight of my grief smother my flames."

            # PDF p197
            prosperity_dragon "Rise up, child. Rise, and show them the might of your bloodline!"

            "The flames surged around me, growing wild and untamed, but I didn't flinch. My hands trembled as the memories of Elara and my children flashed before my eyes—their laughter, their warmth, their love."

            jump ch4_draconic_fire


# =============================================================================
# SECTION 20: LABEL CH4_BAD_END_BOMB — Bad End (Bomb)
# =============================================================================
# PDF pages 197-198.
# =============================================================================

label ch4_bad_end_bomb:

    # PDF p197
    "The heat was unbearable. But I felt nothing."

    prosperity_dragon "Child… You have forgotten yourself."

    "The voice rumbled through me, ancient and sorrowful."

    prosperity_dragon "For that, you are lost for eternity. This is where your journey ends. Farewell, Dorian."

    "His voice echoed faintly as the light engulfed me. The bomb's draconic fire was silent—beautiful, even—as it bloomed in the distance, consuming everything in its path."
    "I didn't fight it. There was warmth. Comfort. A gentle light that pulled me forward, away from the battlefield, away from my regrets."
    "And then I saw them."
    "Elara stood there, radiant as ever, her arms outstretched. Behind her were Daniel, Sarah, Emily, and little Lucas, all smiling at me with the same warmth I had longed to feel again."

    elara  "You've done enough, my heart. Come home now. Rest."

    "Tears streamed down my face as I reached for her, my heart swelling with relief, with love, with the peace I had craved for so long."

    dorian "I'm so sorry… but I'm here now. I'm home."

    scene cg_bomb_bad_end with fade             # PLACEHOLDER — cg_bomb_bad_end
    pause 2.0

    jump game_over


# =============================================================================
# SECTION 21: LABEL CH4_DRACONIC_FIRE — Draconic Fire Unleashed (Common)
# =============================================================================
# PDF pages 197-202.
# =============================================================================

label ch4_draconic_fire:

    # PDF p197-198 — Common
    stop music fadeout 0.5
    play music ost_prosperity_dragon fadein 0.2 # PLACEHOLDER — surge of draconic power

    "I opened my eyes. The bomb was coming quickly—a monstrous force of destruction hurtling toward us. The air around it distorted, waves of unbearable heat radiating outward. I could feel it—the core of draconic fire within. Pure energy, raw and chaotic."

    # [COMMENT: bg_empty_battlefield — back to battlefield, bomb incoming]
    scene bg_empty_battlefield with dissolve    # PLACEHOLDER — empty battlefield

    "I stepped forward, raising my hand toward the bomb."

    # [# 28 Until "The battlefield fell silent"]
    # PDF p198
    play sound sfx_draconic_fire                # PLACEHOLDER — draconic fire surge SFX

    "The flames roared, wild and feral, but I felt them bend to my will. My hands twisted, drawing the energy into a vortex. The blazing fire coiled and folded in on itself, condensing into a massive, searing sphere of power."

    dorian "Ryyaaahhhhhh!!!"

    "The energy roared in my hands, a feral, untamed beast. With a surge of power, I flung it toward him, the blazing sphere of draconic fire tearing through the air like a comet, leaving a trail of destruction in its wake."

    scene cg_draconic_fire_surge with shock_cut # PLACEHOLDER — cg_draconic_fire_surge
    pause 0.8
    scene bg_empty_battlefield with dissolve

    tian_xun "HAHAHAHA! YES! YES!!"
    tian_xun "Prosperity Dragon, witness this moment! Witness your loyal servant's ultimate sacrifice! Let my ashes be your offering! Let this field become your altar! THIS… IS TRUE ART!"
    tian_xun "PROSPERITY DRAGON! WITNESS ME! MY FINAL WORK! MY GLORIOUS END! BOOM! BOOM! HAHAHA—"

    "The bomb slammed into the ground where Tian Xun stood, detonating with a force that shook the heavens."
    "His laughter turned to a guttural scream as the fire engulfed him, the draconic energy tearing his body apart."

    niko   "Everyone, get behind my shadows!"
    yuxuan "O-Okay…"
    niko   "Dorian, you too."

    "Niko's shadows surged around us, forming a protective barrier. I quickly took cover, just in case."
    "The soldiers surrounding Tian Xun barely had time to scream. The heat hit them first, blistering their skin and igniting their armor. Their cries turned to guttural wails as the flames engulfed them, reducing them to ash in moments."

    mjoll_pavel  "No!! Impossible!! AHHHH!!!"
    man_2        "Ahh Ahhh Ahhhhh!!!! Curse you Svanteee!!!"

    "Some of them dropped their weapons, falling to their knees as if in prayer, their faces contorted in horror and despair."

    female_guard "Ahhhh!!! I don't want to die!! I don't want to—"
    man_1        "Enoch save meeeee!! AHHHH!!"

    "Her voice vanished as the flames swallowed her whole."

    # PDF p199
    "Others tried to run, but there was no escape."
    "The battlefield fell silent, save for the crackling of the flames. The once-proud soldiers of Tian Xun's forces were gone, their remains nothing more than ashes."

    stop music fadeout 2.0

    "I stood there, breathing heavily."

    yuxuan "Dorian…"
    svante "What the…"
    niko   "Merciful Enoch… what did you just do?"

    "I didn't answer. I… didn't know. How did I do it?"
    "Elias hugged me even more. Tedda hanging."

    elias "Daddy… is it over?"

    aoi   "Tian Xun!! No!!"

    "Her voice rang out, raw with fury and disbelief."

    aoi         "You monsters! You dare kill him?! That genius, that visionary! He was worth a thousand of you pathetic fools!"
    mjoll_helga "P-Pavel!! They killed Pavel! No!!"

    "Her eyes gleamed with an almost unhinged fury as she turned to her soldiers."

    aoi        "CHARGE! Kill them all! Leave no survivors! They will pay for what they've done!"
    mjoll_lars "Soldiers, kill them!! Kill them all!! Charge!!"

    "The ground shook as the battalion surged forward, a wall of soldiers armed with spears, swords, and shields."

    yuxuan "By the Prosperity Dragon! Another battalion?! Really?! How many soldiers do they even have?!"

    "I turned to Svante, who stood pale and trembling, sweat beading his brow."

    dorian "How many of you are here?"

    "He pointed at the unconscious man."

    svante "A lot, sir. My father didn't want to take any chances. He wanted this man— dead at all costs."
    svante "We can't fight them forever. We're outnumbered ten to one! We need to do something, and we need to do it now."

    "Niko stepped forward, shadows pooling at his feet."

    niko "I'll hold them off as long as I can with my shadows, but that won't be enough. They'll overwhelm us eventually."

    # PDF p200
    niko "Any ideas, Dorian? Surely, you've got something else up your sleeve."

    "The soldiers were closing in fast, their unified march like the rumble of a landslide. Aoi was at the front, water surrounding her."

    aoi    "You cannot escape! Not even the Prosperity Dragon will save you from my wrath!"
    dorian "Tsk…"

    "Yuxuan approached me."

    yuxuan "Dorian, listen. Seeing you creatively use your fire channeling abilities gave me an idea.\\"

    "He hesitated for only a second before continuing."

    yuxuan "I don't tell anyone this—like, ever—but I've got an underground lab nearby. It's hidden, secure, and there's no way anyone will find us there."
    yuxuan "If you can use your earth powers to dig us a path, I can guide us the rest of the way. Can you do that? Please tell me you can… Otherwise, I just told you my secret for nothing."

    "I arched a brow. Oh."

    dorian "Of course, I can."

    "I turned to Niko, who stood with his shadows coiling protectively around us, their dark tendrils shifting like living sentinels. He met my gaze and gave a curt nod."

    niko "If it keeps us alive, we go with his idea. But I'm covering us while we move. No one gets through my shadows."

    aoi        "Lars! Take care of those shadows! Push forward! Kill them all!"
    mjoll_lars "On it, mam! Charge, soldiers!"

    "The pounding of their boots grew louder, closer."
    "There wasn't much time."

    play sound sfx_earth_pillar                 # PLACEHOLDER — earth tunneling SFX

    "I took a deep breath, slamming my palms into the earth. The ground rumbled and groaned beneath us as I focused. a wide opening formed, a tunnel descending into the depths below."

    dorian "Everyone, jump in—now!"
    niko   "I'll be the last one to jump."

    "Yuxuan didn't hesitate. He leapt in first, already reaching up."

    yuxuan "Come on. I'll catch you."

    "Elias clutched his beloved stuffed animal, Tedda, to his chest as he stood at the edge of the opening."

    elias  "Tedda, don't let go!"
    "Tedda: …"

    # PDF p201
    "I moved to the edge, hefting the unconscious man over my shoulder. His weight was considerable, but I tightened my grip, refusing to falter."

    niko   "Be careful with him! He's barely hanging on as it is!"
    dorian "I know. I've got him. Just keep them off us!"

    "Svante lingered at the edge, uncertainty clouding his features. He hesitated, torn between the battle raging above and the unknown below."

    dorian "You too. Jump. Now. I'll jump after you."
    svante "I… are you sure— I'm an aldorith I might—"
    dorian "Dragon's bollocks! Just jump!"
    svante "O-Okay, sir!"

    "He jumped, vanishing into the tunnel's depths."
    "I tightened my hold on the unconscious man and followed, leaping into the darkness."

    yuxuan "That's everyone…You there! It's your turn!"
    niko   "Move over! Shadows, release!"

    play sound sfx_tunnel_seal                  # PLACEHOLDER — tunnel sealing SFX

    "As he jumped, the shadows recoiled, pulling away like a collapsing wave. I didn't waste a second—I slammed my hands into the dirt once more, sealing the tunnel shut above us."
    "The battlefield disappeared."
    "Darkness surrounded us. The only sounds were our ragged breaths and the distant echoes of the battle above, muffled by layers of earth."

    jump ch4_underground


# =============================================================================
# SECTION 22: LABEL CH4_UNDERGROUND — Underground / Chapter 5 Opening
# =============================================================================
# PDF pages 201-202.
# =============================================================================

label ch4_underground:

    # PDF p201
    scene cg_black with fade                    # PLACEHOLDER — darkness
    play music ost_underground_move fadein 2.0  # PLACEHOLDER — tense escape theme
    play audio amb_tunnel loop fadein 1.5       # PLACEHOLDER — tunnel ambient

    yuxuan "Is everyone alright?"
    niko   "Shh… Keep your voice down. They're still looking for us. I can feel them getting closer."

    "Above us, we can faintly hear the muffled voices of the soldiers. Elias was about to say something when Yuxuan covered the child's mouth."

    mjoll_lars   "Where did they go?! Dammit! They've used the amulet!"

    "A strangled sob."

    mjoll_helga  "Pavel… *cries* Lars, I'm scared…"
    mjoll_lars   "Calm down, Helga. We'll find them. Aldoriths, search the area for any clues!"
    man_2        "You heard him, aldoriths! Search every nook and cranny at the cemetery!"

    # PDF p202
    female_guard "Sir yes, sir!"

    "And then—"

    aoi "Ti… Tian Xun…"

    "A pause."
    "Then, a bloodcurdling scream."

    aoi "TIAN XUN!!"

    "And as if the heavens themselves mourned, the sky split open, unleashing a torrential downpour."
    "Raindrops hammered against the earth."

    svante "It's raining now."
    niko   "Good. That way they can't hear us moving."

    "I looked around. Darkness engulfed us, thick and suffocating. But then—"

    # [COMMENT: bg_tianho_underground_1 — natural cave tunnel, Elias's flashlight glowing]
    scene bg_tianho_underground_1 with dissolve # PLACEHOLDER — Tianho underground tunnel 1

    # [# 29 – Until "I took his hand"]
    "A soft glow flickered to life, illuminating Elias's small frame. He clutched a delicate, flower-shaped flashlight in his tiny hands—the one Yuxuan had given him."

    elias "Nice going, Tedda. The flashlight is helping."

    "He held the stuffed bear close, its one button eye reflecting the faint golden light."

    "I took his hand."

    dorian "Are you hurt? Injured?"

    "Elias smiled and shook his head. He hugged Tedda tight."

    elias  "We're fine, Daddy."
    svante "I-I really can't believe it… We made it. We actually made it. I thought that was the end."
    svante "Thank you… Thank you, sir! I could kiss your fee—"
    yuxuan "We're not out of danger yet. Everyone, stay close. Keep that light steady—we're moving now."

    scene cg_black with fade                    # PLACEHOLDER — fade to black
    stop music fadeout 2.0
    stop audio fadeout 1.5

    pause 2.0

    # Chapter title card — Chapter 5 header
    show screen chapter_title_screen(
        "5",
        "Cheng Industries",
        subtitle="Tianho — The Underground Lab",
        duration=3.0
    )
    pause 3.0

    jump chapter_5


# =============================================================================
# END OF CHAPTER 4
# =============================================================================