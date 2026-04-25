###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  FILE:  chapter_08.rpy
#  SCENE: CHAPTER 8 — Behind the Sealed Door
#
#  CONTENTS:
#    Section 1  — Character Definitions (new only)
#    Section 2  — Image Declarations
#    Section 3  — Audio Declarations
#    Section 4  — Game Variables
#    Section 5  — label chapter_8          (Ch7 bridge / lab door / tunnel walk)
#    Section 6  — label ch8_door_chamber   (Yuxuan reveal / Roboto glitch)
#    Section 7  — label ch8_impostor       (Chung-hee reveals Yuxuan is yaoguai)
#    Section 8  — label ch8_open_door      (How to open the door — 4 choices)
#    Section 9  — label ch8_inside_door    (Inside the sealed chamber / bridge)
#    Section 10 — label ch8_corpse         (Kyeongjang soldier / letter choice)
#    Section 11 — label ch8_letter_common  (Button / six paintings puzzle)
#    Section 12 — label ch8_paintings      (Six paintings + dialogue)
#    Section 13 — label ch8_painting_order (Touch order puzzle — 4 options)
#    Section 14 — label ch8_magnus_found   (Magnus in ice / freed / awakens)
#    Section 15 — label ch8_magnus_battle  (Battle QTCs: wing tracker)
#    Section 16 — label ch8_magnus_end     (IF wing < 3 = GAME OVER / IF >= 3 = proceed)
#    Section 17 — label ch8_magnus_peace   (Chung-hee breaks through / Magnus calms)
#    Section 18 — label ch8_walk_back      (Return to lab / Magnus collapses / sleep)
#
#  NAMING CONVENTIONS:
#    image tags      — bg_name, cg_name, character_name emotion
#    audio variables — audio.ost_name, audio.sfx_name, audio.amb_name
#    label names     — ch8_name (all lowercase, underscores only)
#
#  TRACKER SUMMARY:
#    wing_tracker : starts at 0; each correct battle QTC = +1 wing
#                   QTC lantern stands (+1) / dodge+counter (+1) / earth anchor (+1) / reason (+1)
#                   IF wing >= 3 → ch8_magnus_peace; IF wing < 3 → GAME OVER
#
#  AFFINITY TRACKERS (door opening choice):
#    niko_affection     : +1 Choice 1 (Niko's suggestion)
#    svante_affection   : +1 Choice 2 (Svante's suggestion)
#    yuxuan_affection   : +1 Choice 3 (Yuxuan's suggestion)
#    chunghee_affection : +1 Choice 4 (Chung-hee's suggestion)
#
#  PLACEHOLDER PATHS:
#    Search "# PLACEHOLDER" to find every line needing a real asset.
###############################################################################


# =============================================================================
# SECTION 1: CHARACTER DEFINITIONS
# =============================================================================
# moved to compiled file

# Note: magnus, yaoguai_king, feng, aoi, svante, niko, chung_hee, yuxuan, weng, tim, tedda,
#       roboto, gao, jiang, elias, dorian, vasily already defined in prior chapters.


# =============================================================================
# SECTION 2: IMAGE DECLARATIONS
# =============================================================================

image bg_underground_door       = "images/backgrounds/bg_underground_door.png"           # PLACEHOLDER
# (reused from ch5 — polished metal door, no handles, lab tunnel entrance)

image bg_tianho_underground_2   = "images/backgrounds/bg_tianho_underground_2.png"       # PLACEHOLDER
# (reused from ch5 — refined underground passage with electric lights)

image bg_underground_the_door   = "images/backgrounds/bg_underground_the_door.png"       # PLACEHOLDER
# Vast domed chamber — stone door with Prosperity Dragon carved in breathtaking detail

image bg_inside_sealed_door     = "images/backgrounds/bg_inside_sealed_door.png"         # PLACEHOLDER
# Vast cavern, bottomless chasm around perimeter, narrow stone bridge to central platform

image bg_cheng_bunker           = "images/backgrounds/bg_cheng_bunker.png"               # PLACEHOLDER
# (reused from ch7)

image bg_lab_bedroom_normal     = "images/backgrounds/bg_lab_bedroom_normal.png"         # PLACEHOLDER
# (reused from ch6)

# --- CGs ---
image cg_magnus_ice             = "images/cg/cg_magnus_ice.png"                          # PLACEHOLDER
# Magnus entombed in crystal-clear ice, great feathered wings curled around body, serene yet haunting

image cg_magnus_awakens         = "images/cg/cg_magnus_awakens.png"                      # PLACEHOLDER
# Magnus exploding free from ice, wings spread, white eyes blazing, golden veins of divine energy

image cg_magnus_rage            = "images/cg/cg_magnus_rage.png"                         # PLACEHOLDER
# Magnus hovering above platform, bathed in golden celestial light, wings at full span

image cg_painting_1             = "images/cg/cg_painting_1.png"                          # PLACEHOLDER
# The Loom's Whisper — celestial void, radiant hands sculpting a half-formed woman

image cg_painting_2             = "images/cg/cg_painting_2.png"                          # PLACEHOLDER
# Chains of Choice — divine woman stepping from throne, golden chains, man with candle

image cg_painting_3             = "images/cg/cg_painting_3.png"                          # PLACEHOLDER
# Thrones of the Eternal — four celestial beings on thrones, golden sun above

image cg_painting_4             = "images/cg/cg_painting_4.png"                          # PLACEHOLDER
# Wrath — woman on burning throne, single tear, golden banners torn

image cg_painting_5             = "images/cg/cg_painting_5.png"                          # PLACEHOLDER
# Tragedy — winged man with severed head, kneeling divine woman, stormy heavens

image cg_painting_6             = "images/cg/cg_painting_6.png"                          # PLACEHOLDER
# When the Stars Watched — bard plays lute, divine woman watches from garden edge


# =============================================================================
# SECTION 3: AUDIO DECLARATIONS
# =============================================================================

define audio.ost_ch8_tunnel     = "audio/music/ost_ch8_tunnel.ogg"         # PLACEHOLDER
define audio.ost_ch8_door       = "audio/music/ost_ch8_door.ogg"           # PLACEHOLDER
# Ancient, reverent — first sight of the carved door

define audio.ost_ch8_chamber    = "audio/music/ost_ch8_chamber.ogg"        # PLACEHOLDER
# Eerie, vast — inside the sealed chamber

define audio.ost_ch8_letter     = "audio/music/ost_ch8_letter.ogg"         # PLACEHOLDER
# Sorrowful, quiet — Hwan-sik's mind note

define audio.ost_ch8_paintings  = "audio/music/ost_ch8_paintings.ogg"      # PLACEHOLDER
# Mystical — the six paintings puzzle

define audio.ost_ch8_magnus     = "audio/music/ost_ch8_magnus.ogg"         # PLACEHOLDER
# Intense divine battle — Magnus awakens

define audio.ost_ch8_end        = "audio/music/ost_ch8_end.ogg"            # PLACEHOLDER
# Quiet relief — Magnus calms, walk back

define audio.sfx_door_unlock    = "audio/sfx/sfx_door_unlock.ogg"          # PLACEHOLDER
define audio.sfx_lightning_ch8  = "audio/sfx/sfx_lightning_ch8.ogg"        # PLACEHOLDER
define audio.sfx_ice_shatter    = "audio/sfx/sfx_ice_shatter.ogg"          # PLACEHOLDER
define audio.sfx_divine_pulse   = "audio/sfx/sfx_divine_pulse.ogg"         # PLACEHOLDER
define audio.sfx_metal_shards   = "audio/sfx/sfx_metal_shards.ogg"         # PLACEHOLDER
define audio.sfx_painting_glow  = "audio/sfx/sfx_painting_glow.ogg"        # PLACEHOLDER
define audio.amb_cavern_deep    = "audio/ambient/amb_cavern_deep.ogg"       # PLACEHOLDER


# =============================================================================
# SECTION 4: GAME VARIABLES
# =============================================================================

# default wing_tracker    = 0      # correct battle QTCs; >= 3 = proceed to peace
# default ch8_d1_choice   = ""    # door opening: "niko"/"svante"/"yuxuan"/"chunghee"
# default ch8_d2_choice   = ""    # "spearheads"/"lanterns"
# default ch8_d3_choice   = ""    # "stand"/"dodge"
# default ch8_d4_choice   = ""    # "fire_wind"/"earth_anchor"
# default ch8_d5_choice   = ""    # "fire_magnus"/"reason"
# default ch8_read_letter = False
# default ch8_puzzle_seen = False
# default ch8_puzzle_pass = False


# =============================================================================
# SECTION 5: LABEL CHAPTER_8 — Bridge from Ch7 / Lab Door / Tunnel Walk
# =============================================================================
# ch8 txt lines 1-121.
# =============================================================================

label chapter_8:
    $ save_name = "Chapter 9"
    # ch8 lines 1-13 — bridge from ch7 ending
    scene bg_cheng_bunker with fade             # PLACEHOLDER — bunker corridor
    play music ost_ch8_tunnel fadein 2.0        # PLACEHOLDER — tunnel theme

    "Then—a chuckle."
    "The flickering firelight cast shadows over his face as he leaned back slightly, tilting his bottle lazily toward me. He grinned."

    feng "Heh. Alright, alright. No need to be so serious."
    feng "You always did have a way of making things dramatic, old friend. But I get it."

    "He lifted the bottle in an easygoing mock toast."

    feng "See you tomorrow. Try not to get yourself killed before then, yeah?"

    "I gave him a nod before turning away, leading the others forward."
    "As we moved through the dimly lit corridors of the camp, I caught the faintest sound of Feng taking another long drink."

    aoi  "Another wine bottle, sir?"
    feng "Sure thing, Aoi."

    "CHAPTER 8"

    # ch8 lines 16-84
    # [COMMENT: bg_overlooking_tianho — night path back to Yuxuan's lab]
    scene bg_tianho_underground_2 with dissolve # PLACEHOLDER — tunnel / path

    "The journey to Yuxuan's lab was quiet, save for the occasional shuffle of boots against the dirt. Above us, the night stretched vast and endless, a deep indigo canvas speckled with stars, their cold glow barely enough to illuminate the path."
    "A hush had fallen over our group, the weight of the night pressing in, thick with unspoken thoughts."
    "I kept a watchful eye on our surroundings, my senses tuned to any shift in the air, but the night remained undisturbed. Meanwhile, Svante found a brief distraction, chatting softly with Tim, who clutched Weng's hand while balancing his plastic bags of Hinami flan."

    weng "By the stars, my back is starting to ache… Tim, are you sure you can finish all of that?"
    tim  "Positive, Miss Weng!"

    # ch8 lines 27-84
    # [COMMENT: bg_underground_door — polished metal door, lab entrance]
    scene bg_underground_door with dissolve     # PLACEHOLDER — lab entrance door

    "After a while, we reached the entrance of Yuxuan's lab. The same towering door of polished metal loomed before us. Like before, it spoke as we approached."

    "Door: Facial recognition is currently in progress. Please refrain from excessive movement."

    "A few moments later, the voice spoke again."

    "Door: Initiating secondary verification. Please present a valid voice signature."

    weng       "Cai Weng. Master Yuxuan's assistant."

    "Door: Processing… Please provide a biological confirmation."

    "Chung-hee exhaled sharply, folding his arms. His gaze flicked to Weng before trailing over the towering metal door."

    chung_hee  "Isn't this… excessive? Must a simple door be guarded like a royal vault?"

    "Niko raised a brow, glancing at him."

    niko       "They don't have security systems like this in Kyeongjang, huh?"

    chung_hee  "We have, but not this excessive."

    svante     "You have these in Kyeongjang too, Your Majesty?"

    "Chung-hee let out a quiet scoff, shaking his head."

    chung_hee  "Yes, but not even our palace gates demand so much proof of existence."
    chung_hee  "And again, Svante. Call me Chung."

    svante     "S-Sorry, Your Majesty. I mean Sir Chung."

    "The door let out a low beep, and the heavy locks shifted with a mechanical hiss."

    "Door: Identity confirmed. Welcome home, Miss Cai Weng. May the blessings of the Prosperity Dragon be with you this wonderful night."
    "Door: Here at Cheng's we bring change."
    "~Here at Cheng's we bring change.~"

    niko "Merciful Enoch, I can't seem to escape that damn jingle."

    "The seamless metal parted, revealing the pristine interior of the lab."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    "Roboto whirred forward. Its polished exterior reflected the glow of the overhead panels, giving it an almost ghostly sheen in the dim light."

    roboto "G-G-G-Good evening, Master Dorian. Master Yuxuan is t-t-taking a n-n-n-nap."
    roboto "He r-r-requested me to show you y-y-y-your d-d-destination."

    svante "Sir Yuxuan… naps?"

    niko "He's a human being. Of course he gets tired."

    "Weng turned to us, her gaze gentle but firm as she placed a guiding hand on Tim's back."

    weng "Are you sure about this, Sir Dorian? If so, this is where we part ways for now. Roboto will be leading you to the door in your dream."
    weng "Tim and I are already feeling tired. These old bones of mine aren't helping."

    tim  "N-No I'm not *yawns* I'm more than willing to- *yawn*"

    "Weng chuckled softly, shaking her head."

    weng "I apologize. If I were younger I would have *yawn*"

    "She yawned, covering her mouth as fatigue settled into her features."

    svante "Don't worry, miss Weng."

    "Tim pouted but gave a small wave."

    tim  "Aww… But take care, sirs! See you *yawns* tomorrow."

    chung_hee "We will, Tim."

    weng "I'll check on Elias and Tedda for you before we go to sleep, Sir Dorian. Take care."

    "I met her gaze and gave a slight nod."

    dorian "Thank you, Miss Weng. I appreciate it."

    "She gave me a knowing look before turning away, leading Tim inside. The metal door slid shut behind them with a quiet hiss."
    "Roboto whirred again, its headpiece swiveling slightly as it pivoted toward the darkened corridor ahead."

    roboto "F-F-Follow me, sirs. T-T-This way…"

    # ch8 lines 86-121
    # [COMMENT: bg_tianho_underground_2 — refined tunnel, faint etchings on walls]
    scene bg_tianho_underground_2 with dissolve # PLACEHOLDER — underground tunnel 2
    play audio amb_cavern_deep loop fadein 1.5   # PLACEHOLDER — deep cavern ambient

    "It pivoted forward, its legs gliding smoothly over the damp ground. The corridor stretched out before us—a vast, quiet expanse of reinforced tunnels lined with cold stone and compacted earth. The air was thick with the scent of damp earth and soil."
    "As we walked deeper into the tunnel, our footsteps echoed softly against the stone, swallowed by the dim, cavernous passage."
    "I let my gaze drift across the tunnel's edges, where faint etchings ran like veins along the surface—symbols and patterns I didn't recognize— worn, weathered, nearly erased by time, yet still clinging stubbornly to the walls surface."
    "I narrowed my eyes, reaching out to brush my fingertips against one of the engravings. The texture was uneven, the grooves shallow but deliberate."

    dorian "So, Roboto, do you have any background of how these tunnels came to be?"

    roboto "M-Master Yuxuan and his partners d-d-discovered these tunnels b-by accident."

    "Niko and Chung-hee exchanged a glance with me. The tunnels were older than Yuxuan?"

    roboto "The original creators are… u-u-unknown. However, some data suggest that they predate the c-c-current settlements"

    svante     "The creators might predate the current settlements? So that means…"

    chung_hee  "There is a distinct possibility these tunnels were built long ago, before any of our cities existed."

    "I turned my attention back to the etchings. There was something about them, something unsettlingly intricate. The longer I looked, the more I felt a strange sense of familiarity, like I had seen them before in a dream or in the remnants of some old myth."
    "The tunnel stretched endlessly before us, its ancient markings bathed in the cold, sterile glow of the fixed lights embedded in the walls. The artificial brightness clashed against the archaic surroundings, like two worlds trying to coexist."

    dorian "And where exactly in the tunnel are you taking us?"

    "Roboto whirred again, tilting its metallic headpiece slightly."

    roboto "T-To the end of the tunnels."

    "It hesitated for the briefest of moments, as if its internal systems were recalibrating its response. Then, it spoke again, its voice more certain this time."

    roboto "The m-m-massive d-d-door with the Prosperity Dragon illustration… It l-l-lies ahead. At the end of the tunnels."

    "The group fell into a heavier silence as we continued walking, the weight of Roboto's words settling over us. Each step forward felt like a step into something long buried, something not meant to be disturbed."

    jump ch8_door_chamber


# =============================================================================
# SECTION 6: LABEL CH8_DOOR_CHAMBER — The Dragon Door / Yuxuan Reveal
# =============================================================================
# ch8 txt lines 122-188.
# =============================================================================

label ch8_door_chamber:

    # ch8 lines 122-188
    # [COMMENT: bg_underground_the_door — vast domed chamber, door with Prosperity Dragon carving]
    scene bg_underground_the_door with fade     # PLACEHOLDER — domed chamber, the Dragon Door
    stop music fadeout 1.0
    play music ost_ch8_door fadein 2.0          # PLACEHOLDER — ancient reverent theme

    "Minutes later, the tunnel finally widened, revealing a vast, domed chamber. And there—standing at the farthest point—was the door."
    "There's no mistaking it. It was the same door in my dream. The Prosperity Dragon stretched across its surface in breathtaking detail. Its body coiling through storm-wracked clouds."
    "Then, out of the corner of my eye, I saw movement."
    "A hooded figure stood at the base of the door, partially concealed in the shadows. My muscles tensed, instinct kicking in. Then, in one fluid motion, the figure lifted their hand and pulled back the hood."
    "Yuxuan's face emerged from beneath the fabric, illuminated by the dim glow of the chamber."

    yuxuan "You're late, buddy."

    "For a moment, none of us moved."

    dorian     "Yu… you're here."
    chung_hee  "I hope you weren't waiting long."
    svante     "We—we thought you were sleeping!"
    niko       "Shouldn't you be in bed?"

    "Yuxuan, unbothered as ever, smirked. He shifted his weight onto one foot, crossing his arms."

    yuxuan "What can I say? The idea of you wandering through my tunnels unsupervised was more terrifying than losing a little sleep."

    "And then—Roboto twitched."
    "The bot, which had been standing dutifully beside us, suddenly jolted. A harsh electronic screech cut through the chamber, its optics flickering erratically."

    roboto "E-E-E-E-Error. E-E-E-E-Error. P-P-P-Para-d-d-d-d-d—"

    "With a sudden, jerky movement, it spun on its wheels and bolted down the corridor, its metallic limbs twitching as if something had taken hold of its systems."
    "We all turned, watching as it disappeared into the darkness, its garbled stuttering echoing until it was gone."
    "I glanced back at Yuxuan, half-expecting him to look concerned. But instead— he let out an exaggerated sigh, his smirk never faltering."

    yuxuan "Guess even my trashy machines can't handle the grandeur of my genius."

    "He waved a hand dismissively, as if Roboto's erratic malfunction was of no concern. Chung-hee furrowed his brow, arms crossed."

    chung_hee  "Oh, do they?"

    "Yuxuan's grin didn't waver, but his fingers twitched at his side before he threw up his hands in mock surrender."

    yuxuan "Of course, Your Majesty! I assure you, everything is perfectly under control."
    yuxuan "But enough about my poor, overworked machines. Let's turn our focus to the real star of the show, shall we?"

    "He gestured dramatically toward the massive door, its intricate carvings gleaming under the dim light."

    niko "Dorian, is this the same one that you saw on your dream?"

    "I stepped forward, my gaze tracing the magnificent structure. The closer I got, the more I could see the painstaking detail."
    "Its sinuous body in a mesmerizing display of movement, despite being frozen in metal. Every scale was meticulously sculpted, each ridge catching the dim light, making it seem as if the dragon were shifting in place."
    "Its eyes, inlaid with polished jade, gleamed with an eerie lifelike quality. Though unmoving, they seemed to watch us, reflecting the dim chamber light like distant stars in the void."

    svante "Incredible… I bet even the most skilled earth channelers would struggle to sculpt something this detailed."

    "His fingers twitched at his side, as if he were resisting the urge to reach out and confirm that the door was real—that something this perfect hadn't just been imagined into existence."

    yuxuan     "Amazing, right?"
    chung_hee  "A creation worthy of the Tetrad themselves. Not a single detail out of place. This was not simply built—it was bestowed."

    "Niko, hands clasped behind his back, studied the metalwork with a careful eye."

    niko "Whoever created this was clearly more than just a master craftsman… They were a devout worshiper of the Prosperity Dragon."
    niko "I highly doubt that a pagan or a mere artisan would dedicate their waking hours to crafting something this impossibly intricate. This isn't just an offering—it's a declaration."

    "He let his fingers trail over the carved ridges of the dragon's body, his tone growing contemplative."

    niko "This level of precision… the sheer reverence in the way each scale, each line, each curve has been etched—it's not just talent. It's faith."

    "The chamber was silent, save for the quiet hum of flickering lights and the faint, distant sound of shifting metal in the tunnels beyond."
    "Then, Svante hesitated before speaking, glancing at Chung-hee with curiosity."

    svante "You worship the Tetrad, right, Your Maj— I mean, Sir Chung? Do you have sculptures like this back in Kyeongjang?"

    chung_hee  "As a matter of fact, we do."
    chung_hee  "In the Imperial Capital, we have towering sculptures of each of the four Immortal Tetrads."
    chung_hee  "Adriana, the Immortal Tetrad of Emotion and Kindness, standing at the gates of the Celestial Palace of the Emperor Lord. A reminder for the Emperor Lord's responsibility to rule with kindness and mercy."
    chung_hee  "Meanwhile, in the great halls of justice, a solemn statue of Renji, the Immortal Tetrad of Justice and the Void."
    chung_hee  "The Grand Library of Kyeongjang houses a magnificent sculpture of Li Mengtia, the Immortal Tetrad of Knowledge and Wisdom. Visitors see his face each time they seek guidance in the pursuit of knowledge."
    chung_hee  "And in the heart of the imperial gardens, the most revered of them all—Saelara, the Immortal Tetrad of Creation, is immortalized in marble. Her outstretched hands hold an intricate celestial map, a reminder that creation itself is a gift to be cherished and honored."
    chung_hee  "These sculptures were all commissioned by my great great great grandfather, one of the late Emperors of Kyeongjang. He believed the Tetrad's presence should not only be felt but seen, woven into the very foundation of the empire."

    svante "Wow… what I wouldn't give to see them, sir."

    "A quiet chuckle broke through the solemn air."

    yuxuan "Hahaha! You hit the nail in the head there, Chung-hee. That's a theory I had when I first found this tunnel."

    "His gaze remained locked on the dragon-carved door, a glint of something unreadable in his sharp eyes. He lifted a hand, tracing the air just above the intricate engravings."

    yuxuan "My partners and I stumbled upon these tunnels completely by accident, and since then, I've been studying this door for years. Ever since the Tragedy of Tianho."

    "Then, with a smooth motion, he turned to face me and Chung-hee directly, holding out his palm."

    yuxuan "Now then. The amulets. Hand them over."

    "I stiffened. The amulets? My fingers instinctively curled around the cool metal resting in my pocket."
    "Slowly, I withdrew it—the amulet I had found on Elias when I first found him. Its surface gleamed under the dim tunnel light, an intricate pattern of old symbols carved into the metal."

    dorian "I have it, Yu. But why?"

    "He motioned toward the door, his fingers ghosting over the carvings of the Prosperity Dragon once more."

    yuxuan "This door is sealed. My theory is that it has been for far longer than any of us have walked this land."

    "He glanced at me and Chung-hee, his expression unreadable."

    yuxuan "Something is inside this. Something ancient."
    yuxuan "It won't open for just anyone. You can't break through it with brute force. We already tried."

    "Chung-hee crossed his arms, his tone cautious."

    chung_hee  "Then have you discovered what does open it?"

    "Yuxuan smiled faintly, as if pleased by the question."

    yuxuan "Draconic fire. Only a channeler of draconic fire is strong enough to awaken the engravings can unlock the seal. That, and… the two amulets."

    svante "D-Draconic fire? Are you sure, Master Yuxuan? You mean Sir Dorian…"

    "I exchanged a glance with Chung-hee, my grip tightening around the amulet."

    chung_hee  "And you're certain about this?"

    yuxuan "I wouldn't ask if I weren't."

    "Yuxuan huffed a quiet laugh, tilting his head slightly. Still, neither of us moved to hand them over."
    "Yuxuan, sensing our hesitation, took a step closer, his voice dipping into something softer—something personal."

    yuxuan "Dorian. You found that amulet on Elias, didn't you? That poor little child. That amulet was given to him by his mother—Queen Ekaterina. You were there when he lost everything. At that cave."

    "The mention of it made my jaw tighten. Snow. Darkness. The relentless howling wind. The way Elias had clung to that amulet like it was his last tether to the world."

    dorian "What are you getting at, Yu?"

    "Yuxuan exhaled, shaking his head slightly, as if he couldn't believe I had to ask."

    yuxuan "I'm saying… who helped you and little Elias when you were trapped in Frostcradle during the blizzard? When the cold was closing in and there was no way out?"

    "He took a step closer, tilting his head."

    yuxuan "It was me, wasn't it?"

    "My grip on the amulet tightened."

    yuxuan "You and Elias would've starved to death in that cave if I hadn't gotten you both out."

    dorian "Yes. I do, Yu. Always."

    "I smiled at Yuxuan and gave him the amulet."

    yuxuan "Thank you for your trust, Dorian."

    "He winked at me, a mischievous smile on his lips."

    "The familiar voice, vast as the sky and deep as the roots of the earth, roared in my head."
    "A blinding white light swallowed my vision."

    prosperity_dragon "YOU HAVE BEEN DECEIVED, CHILD!"

    "A sharp pain lanced through my skull. My breath caught."

    dorian "ARGH! What do you mean?"

    "The voice thundered again, rattling through my bones."

    prosperity_dragon "GET BACK THE AMULET, CHILD! OBEY!"

    "And then—silence. The light vanished."
    "I staggered, the room spinning as reality snapped back into place."
    "My heart pounded against my ribs like a war drum."

    niko "Dorian, are you alright?"

    dorian "I-I'm fine…"

    yuxuan "And what about you, Your Majesty?"
    yuxuan "You left Kyeongjang with a purpose, didn't you? And when you return home, Your Majesty, what will you say? What will your aunt think?"
    yuxuan "That you came all this way, held the key to something far greater, and did nothing."

    jump ch8_impostor


# =============================================================================
# SECTION 7: LABEL CH8_IMPOSTOR — Chung-hee Reveals Yuxuan Is a Yaoguai
# =============================================================================
# ch8 txt lines 279-386.
# =============================================================================

label ch8_impostor:

    # ch8 lines 279-386
    "The shift in Chung-hee was immediate. His entire demeanor darkened, his jaw tightening as his hands curled into fists at his sides."

    chung_hee  "Where did you get that?"

    yuxuan "Pardon, Your Majesty?"

    chung_hee  "Where did you find out about my aunt?"
    chung_hee  "I never told any of you about her. I never spoke of my family—any of them."

    "Silence hung between us, heavy and suffocating. My mind raced. Chung-hee had never once mentioned an aunt. All we knew was that his parents had perished in the Tragedy."
    "Yuxuan, unfazed, merely offered a small, knowing smile. He tilted his head, amusement flickering in his expression."

    yuxuan "I have my ways. I make it a point to know things. Call it… connections."

    niko "Connections? To Kyeongjang? With all due respect, you don't actually expect us to believe you have ties there, do you, Yuxuan?"

    svante "He does have a point, sir Yuxuan."

    "And then I felt it."
    "A pressure in the air, like static crawling beneath my skin. My body tensed instinctively."
    "Chung-hee exhaled slowly, closing his eyes for a fleeting moment before opening them again—sharper, burning with quiet fury. His fingers twitched at his sides, lightning crackling faintly along his knuckles."

    chung_hee  "…I apologize for this."

    "It was the only warning we got."

    # [# 40 — until Svante says "Sir Chung, what…"]
    play sound sfx_lightning_ch8               # PLACEHOLDER — lightning strike SFX

    "Before anyone could react, a surge of raw energy erupted from his fingertips. A bolt of lightning, blinding and furious, shot straight toward Yuxuan."

    svante "SIR—!"

    "The crackling energy illuminated the chamber in a violent flash."
    "The electricity struck Yuxuan dead-on, his body convulsing violently as arcs of energy danced across his frame. The smell of singed fabric filled the air, and for a single, agonizing moment, all I could hear was the crackling of lightning fading into silence."

    dorian "YU!! NO!!"

    "Panic surged through me as I rushed forward, heart pounding in my chest. The others weren't far behind, though they weren't running to help—no, they were turning on Chung-hee."

    svante "SIR CHUNG, WHAT DID YOU JUST DO?!"

    niko "Chung, are you insane?! That was completely uncalled for!"

    "Chung-hee didn't respond at first, his posture rigid, hands still crackling with fading electricity."

    chung_hee  "That was not Yuxuan."

    svante "Sir Chung! What in Enoch's name are you talking about?! He's right there, dying!"

    "A low, guttural sound filled the chamber. The body on the ground twitched, spasming unnaturally before its limbs jerked at odd angles. Bones cracked, skin rippled, and for one terrifying moment, its face melted into something grotesque."
    "A yaoguai."

    yaoguai "Ra-Ra-RAAAWWWRRR!!!"

    "My stomach twisted. Yuxuan had been a yaoguai this whole time?!"

    niko "Enoch above… What is going on here?!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto approaching SFX

    roboto "A-A-A-A-Alert. M-M-M-Master Yuxuan is here…"

    "We all whirled around just in time to see Roboto clanking down the tunnel. And beside him—"
    "Another Yuxuan."
    "This one was completely unharmed, holding a steaming cup of coffee with an irritable scowl on his face. His robes were slightly disheveled, his long hair loose over his shoulders like he'd just rolled out of bed."
    "He blinked blearily at us before groaning."

    yuxuan "What in the Prosperity Dragon's name is going on!!"

    "He took a long, frustrated sip of coffee before pointing an accusatory finger at Roboto."

    yuxuan "There better be a good reason for waking me up, Roboto!"

    dorian "Wait… Yu?"

    svante "…Umm. What just happened?"

    "The moment Yuxuan's gaze landed on the grotesque, convulsing form of the yaoguai, his entire body tensed. His eyes widened in sheer terror, and his grip on the coffee cup slackened."

    yuxuan "E-E-EEEKKKK!!!"

    "With an unceremonious yelp, he leaped backward, dropping his drink as his free hand flailed in panic. His breath came in sharp, ragged gasps as he pointed a trembling finger at the writhing creature."

    yuxuan "HOW DID IT GET IN HERE?! DORIAN!! HELP!!"

    niko "Oh brother…"

    dorian "It's already dead, Yu."

    "We quickly explained everything—how Chung-hee had sensed something was off, how he struck down the imposter, and how the yaoguai had been disguising itself as Yuxuan all along. As we spoke, Yuxuan's face shifted from horror to a mixture of understanding and lingering unease."

    yuxuan "Oh my… Did that really happen? How did you found out that the person wasn't really me?"

    "Chung-hee exhaled slowly, his gaze still locked onto the lifeless form of the yaoguai. His expression was unreadable—stoic, yet touched with something heavier."

    chung_hee  "I dug deep into its mind. I found out too late."
    chung_hee  "I don't do this. I don't invade minds unless absolutely necessary. It's a violation of trust, of privacy… But this thing was dangerous. It was deceiving us."
    chung_hee  "I swear on my honor—I will never turn my abilities against any of you unless it is a matter of life and death. That is my promise."

    "The weight of his words settled over us. I nodded, accepting his vow."

    svante "I trust you, sir Chung. After saving and not killing me, I technically owe you my life still. *nervous chuckle*"
    niko   "That works. You don't seem to be the type that breaks his promises."
    yuxuan "Well… oh, goodness! Well, it's a damn good thing Roboto woke me up."

    roboto "N-N-N-No worries, Master Yuxuan! Y-Y-Y-You can always count on Robotoooo~~"

    "It beeped and blinked its lights proudly."

    roboto "I w-w-w-was worried, so I hurried to wake Master Yuxuan up. I had help from Miss Tedda as well."
    roboto "Miss Tedda helped me w-w-w-wake Master Yuxuan up while I monitored the tunnels for further threats."

    "Then Roboto turned to the yaoguai's still form, its glowing optics flickering as it processed the situation. It tilted its head slightly, then spoke with a tone of programmed enthusiasm."

    roboto "I shall take care of this! P-p-proper disposal protocols will be followed!"

    # [# 41 — Until a collective breath seemed…]
    play sound sfx_roboto_beep                  # PLACEHOLDER

    "With a series of quick, mechanical movements, Roboto extended a set of slender, metallic arms. It latched onto the corpse, adjusting its grip before effortlessly hoisting the body upward. The weight didn't seem to strain it in the slightest."

    niko "Strong fella… who knew?"

    roboto "Now, now. Off to proper containment and disposal you go~"

    "The lifeless form dangled in its grasp as Roboto turned toward the tunnels. Just before departing, it spun back around and blinked at us cheerfully."

    roboto "S-S-See you at the lab, sirs!"

    svante "See you, Roboto!"

    "With that, the little machine whirred away, carrying the remains of the yaoguai as if it were no more than an inconvenient piece of trash."

    roboto "Robotooooo~"

    "A collective breath seemed to escape from all of us."
    "Finally, we turned to face the door once more. Its intricate carvings gleamed under the dim tunnel lights, the Prosperity Dragon's gaze seeming to watch us in quiet expectation."

    "Chung-hee studied it for a moment, then spoke."

    chung_hee  "Maybe… what the fake Yuxuan said was true."

    niko   "Even if it was lying about who it was, it might not have been lying about the door itself."

    yuxuan "From what the lot of you were saying, yes. Those are merely theories though."

    svante "It won't hurt to try, right? If this thing really does require the amulets and draconic fire to open, then…"

    "I tightened my grip around the amulet in my palm."

    dorian "I'm the only one who can open it."

    "Without a word, he reached into the folds of his coat and pulled out his amulet. The dim tunnel light caught the edges of the amulet as he extended it toward me."
    "I looked at him, searching his expression. There was no hesitation, no doubt."

    chung_hee  "If anyone can open it, it's you."

    "I took the amulet from his palm, feeling the cool weight of it settle into my hand alongside my own. A strange sensation passed through me—like an old whisper, a buried echo of something ancient stirring just beneath my skin."
    "I turned toward the towering door, exhaling slowly."

    dorian "Alright… I know I need to channel draconic fire to break the seal, but what do I do with the amulets? Hold them up? Place them on the door?"

    "I glanced at Yuxuan, hoping for some guidance."
    "He stared back at me."
    "Then blinked."
    "Then slowly folded his arms."

    yuxuan "…Did the winged man tell you what to do?"

    dorian "What?! Are you saying you don't know?"

    yuxuan "Buddy, you think I've done this before? I told you, I've spent years studying this door, not opening it."

    "I groaned, rolling my shoulders."

    dorian "Great. So what now?"

    svante "Maybe we can just… you know, guess. How hard could it be? It's just a pose right?"

    chung_hee  "I hardly think dramatic poses are necessary. We possess the amulets—surely that alone should be enough. Must we resort to theatrics?"

    niko "Think about it. Posture holds great significance in religious ceremonies, does it not? If this door is bound to something ancient—something sacred—then the way we present ourselves may matter more than we think."

    chung_hee  "I… highly doubt that."

    "Niko took a step forward, holding out his hands with the amulets, palms facing upward, as if offering them to an unseen deity."

    niko "Like this. This is how priests kneel before an altar, or how supplicants raise their hands in prayer. If this is a ritual, then our stance should reflect reverence—humility befitting an item of such significance."
    niko "Humility. Reflection. Devotion."

    chung_hee  "Isn't that a little excessive?"

    dorian "Chung's right, Niko. Any other ideas?"

    svante "Or—and hear me out—you point them at the door like twin weapons. Like—'BEHOLD MY POWER!'—and then blast the fire!"

    "He spread his arms dramatically, mimicking a grand gesture of divine invocation."

    svante "Like this, Sir Dorian!"

    chung_hee  "Not you too, Svante."

    yuxuan "Please. If we're going by theatrical inspiration, we should follow The Trials of the Silver Dragon."

    "Chung-hee raised an eyebrow, his expression one of mild curiosity."

    chung_hee  "The Trials of the Silver Dragon? I am unfamiliar with this Silver Dragon you speak of. Is this a deity of some significance?"

    yuxuan "It's an audio drama I listen to every morning! The protagonist stands before the sacred gate, arms crossed over his chest, an amulet in each hand, and recites a sacred vow before unleashing his divine energy."

    svante "You're into audio dramas too, sir Yuxuan?! My mom used to star in one! It's called—"

    "Chung-hee let out a long, suffering sigh, pinching the bridge of his nose as if physically pained by the discussion."

    chung_hee  "Or perhaps you simply place the amulets against the door, instead of engaging in wildly unnecessary pageantry."

    "I stared at them all."

    dorian "…These are my options?"

    "Niko looked proud, Svante gave me an encouraging thumbs-up, Yuxuan was practically vibrating with excitement over his audio drama fantasy, and Chung-hee… looked utterly done with this conversation."
    "They all looked far too pleased with themselves."
    "Still, I couldn't ignore that there was a logic to what they were saying. Rituals, reverence, power—whatever the answer was, it had to be something intentional."
    "I exhaled sharply, gripping the amulets tighter."

    jump ch8_open_door


# =============================================================================
# SECTION 8: LABEL CH8_OPEN_DOOR — Opening the Door (4 Choices)
# =============================================================================
# ch8 txt lines 461-554.
# All lead to the same common.
# =============================================================================

label ch8_open_door:

    menu:

        "Go with Niko's suggestion.":
            $ ch8_d1_choice = "niko"
            $ niko_affection += 1

            # ch8 lines 469-482
            "I took a deep breath and followed Niko's suggestion, raising the amulets with both hands, palms facing upward as if offering them to something divine. Niko stood close, his voice calm yet commanding."

            niko "That's it. Hold them up as an offering."
            niko "Feel the faith. Show humility. Devotion. Sincerity. Let go of all doubt."

            chung_hee  "You've chosen Niko's suggestion. A noble choice… I think. Let us see if the door deems it worthy."

            svante "Well, I suppose that makes some sense. Old temples and rituals usually had some kind of pose, right?"

            chung_hee  "Agreed. There is wisdom in tradition. Even if one does not fully grasp the meaning, the act itself can hold power."

            niko "Faith is power, Sir Chung. If you dismiss it, you dismiss what has moved entire civilizations, what has turned the tides of history."

            jump ch8_open_door_common

        "Go with Svante's suggestion.":
            $ ch8_d1_choice = "svante"
            $ svante_affection += 1

            # ch8 lines 484-502
            "I took a steadying breath, deciding to follow Svante's advice. If nothing else, it had flair. I guess."
            "Squaring my stance, I tightened my grip around the amulets, their cool metal warming under my touch."
            "A familiar heat coiled in my chest, waiting to be unleashed."

            svante "Like twin weapons, sir! Point them toward the door—let them know who's in charge!"

            "I exhaled sharply, raising both amulets before me like blades poised for battle. Energy crackled along my fingertips, sparks of draconic fire licking at the edges of my vision. The chamber seemed to hold its breath."

            dorian "BEHOLD MY POWER!"

            "The amulets flared to life, light exploding from their surfaces in a blinding display."

            "Svante & Yuxuan: PRAISE BE TO THE SILVER DRAGON!"

            niko "…"

            chung_hee  "... Silver Dragon? I assume this pertains to the fictional audio drama Sir Yuxuan insists on referencing?"

            niko "Merciful Enoch, grant me patience for I'm running out of it."

            svante "Now, sir Dorian—channel the draconic fire! Show the door your might!"

            jump ch8_open_door_common

        "Go with Yuxuan's suggestion.":
            $ ch8_d1_choice = "yuxuan"
            $ yuxuan_affection += 1

            # ch8 lines 504-520
            "After a moment of indecision, I sighed and turned to Yuxuan."

            dorian "Alright, Yuxuan, what was that ridiculous thing you mentioned?"

            "His face lit up with delight, as if he had been waiting for this moment his entire life."

            yuxuan "Ah, an excellent choice! There's this one scene from 'The Silver Dragon Chronicles'—Episode 37, mind you—"

            "He went into full detail. I didn't understand anything."

            svante "Sir Yuxuan! That's correct!"

            niko "...Do you actually listen to these programs or do they just manifest in your mind?"

            "Fine. I took a deep breath. struck a dramatic stance, raising my arms high. I made sure to follow what he said."

            dorian "BY THE WILL OF THE ANCIENT FLAME, I STAND AT THE PRECIPICE OF DESTINY! … Like that?"

            yuxuan "I love it! The INTENSITY! The EMOTION! Oh, the drama! It's perfect!"

            svante "Beautiful. Absolutely beautiful, sir Dorian. I felt moved! Bravo! Bravo!"

            chung_hee  "…"

            niko "…Merciful Enoch, please grant me patience for I'm running out of it."

            jump ch8_open_door_common

        "Go with Chung-hee's suggestion.":
            $ ch8_d1_choice = "chunghee"
            $ chunghee_affection += 1

            # ch8 lines 522-543
            "I exhaled slowly, pressing my fingers against my temple before turning to Chung-hee."
            "For once, I'm going to listen to the most reasonable person in the room."

            dorian "Chung, what was your idea?"

            "Chung-hee regarded me with a measured gaze, his expression calm and unwavering."

            chung_hee  "The amulets are keys—therefore, they must be used as such. Align them with the engravings and let the door recognize its rightful seal."

            niko "Sometimes the simple answer is the right one."

            svante "I suppose it does make the most sense… probably."

            yuxuan "No battle cry? No flair? That's sad."

            "I sighed, stepping forward until I was close enough to the door to see the fine details of its carvings."
            "Taking a breath, I pressed both amulets against the engravings, aligning them with the shapes etched into the stone."
            "A deep, resonant click echoed through the chamber."

            play sound sfx_door_unlock          # PLACEHOLDER — door unlock SFX

            svante "Oh! Did you hear that, Your sir Chung? It might have worked!"

            chung_hee  "Svante, I remind you—such sounds do not reach me for I am not of hearing. Please tell me what the sound was."

            svante "Right. Of course. My apologies, sir Chung."

            niko "It was a click, Chung. Like the unlocking of a mechanism or something."

            jump ch8_open_door_common


label ch8_open_door_common:

    # ch8 lines 545-554
    "The air around me thickened, charged with something unseen. The amulets pulsed against my skin, and a warmth coiled in my core—draconic fire."
    "I held firm. I did not break my stance."
    "Then, with a low, grinding groan, the door began to shift. Dust and debris rained down as the massive stone slab trembled and heaved. The very ground beneath us shuddered, and the deep, echoing sound of stone scraping against stone filled the air."
    "A gust of air rushed out from the darkness beyond, stale and putrid. It carried the suffocating weight of decay, dampness, and something acrid—like burnt metal and old, rotting blood."
    "The door fully parted, revealing a cavernous space beyond."

    jump ch8_inside_door


# =============================================================================
# SECTION 9: LABEL CH8_INSIDE_DOOR — Inside the Sealed Chamber / Bridge
# =============================================================================
# ch8 txt lines 556-620.
# =============================================================================

label ch8_inside_door:

    # [COMMENT: bg_inside_sealed_door — vast cavern, chasm, narrow stone bridge to central platform]
    scene bg_inside_sealed_door with fade       # PLACEHOLDER — sealed chamber interior
    stop music fadeout 1.0
    play music ost_ch8_chamber fadein 2.0       # PLACEHOLDER — eerie vast chamber theme
    play audio amb_cavern_deep loop fadein 1.0  # PLACEHOLDER — deep cavern ambient

    "The space beyond was vast, stretching beyond the reach of our light. The ceiling vanished into darkness, unseen, while a sheer, bottomless chasm yawned around the perimeter. The only solid footing was a narrow stone bridge, a precarious path leading to a massive circular platform at the center of the abyss."

    "I turned to Yuxuan, my voice laced with disbelief."

    dorian "Yu, do you mean to tell me you studied this door for years and never once suspected what was inside of it?"

    "Yuxuan held up both hands in defense, his eyes wide."

    yuxuan "I swear to you, I had no idea! We tried everything—earth channeling, brute force—but we could never break the seal. We assumed it was an empty chamber, or that it had collapsed long ago!"

    "With caution, we stepped forward, each footfall echoing across the vast emptiness."

    niko "Careful, everyone."

    chung_hee  "Watch your footing. The bridge is old."

    "The bridge rocked."

    svante "How deep is the pit?"

    yuxuan "Prosperity Dragon bless me! That is one deep pit!"

    "On the central platform, the remnants of something long-forgotten lay strewn about."
    "Broken tables, their once-sturdy legs snapped and rotting, were overturned in disarray. Glass apparatus, cracked and shattered, glinted faintly under the dim glow of embedded crystals pulsing weakly along the cavern walls."
    "Strange tools lay abandoned—rusted clamps, peculiar metal rods, and parchment so aged that it disintegrated at the slightest touch."
    "There were corpses littered in the central area. Niko crouched near one of the fallen figures, eyes narrowing as he examined the remains."

    niko "Odd. The decomposition suggests varying timelines. Some of these bodies have been here for centuries, reduced to skeletal remains. Others… are far more recent. Mummified, desiccated, yet eerily preserved by the cold, dry air."
    niko "It reminds me of the time I went to a remote village in the Hinami kingdom. The way corpses were left untouched after the famine, preserved not by time's mercy but by sheer desolation."

    "Svante swallowed hard, his face paling."

    svante "I-I think I'm going to be sick… *barfs*"

    yuxuan "C-Can I go back? Oh Prosperity Dragon… *barfs* *barfs*"

    dorian "Calm down, Yu."

    "Chung-hee wrinkled his nose in distaste, his voice as poised as ever despite the ghastly scene before us."

    chung_hee  "This stench is vile. A cloying, putrescent rot. Something terrible had happened here. And whatever it was… it had not been swift. Nor had it been merciful."

    "We moved cautiously, our footsteps echoing in the vast, forsaken chamber. Dust and debris covered the floor, mingling with shards of broken glass and rusted metal tools."

    svante "Merciful Enoch…"

    "We turned toward him and saw what had caught his attention."
    "A corpse lay sprawled across the floor, half-buried under fallen debris. Unlike the other remains, this one was in the process of decomposition. Its flesh had darkened and sagged, splitting in places where decay had eaten away at the muscle. The stench was nearly unbearable."

    "Chung-hee stepped forward, his sharp gaze scanning the corpse with unnerving precision. His expression remained unreadable, but there was something distant in his eyes."

    chung_hee  "That uniform… It is standard Kyeongjang military wear."

    dorian "A Kyeongjang soldier? Here?"

    "Chung-hee's eyes traced the insignia still faintly visible beneath layers of dust and decay. His lips pressed into a firm line."

    chung_hee  "No doubt about it. This is not just any soldier—this insignia belongs to the royal guard."

    yuxuan "The royal guard… You mean… they served the Emperor?"

    chung_hee  "Yes. My father's soldiers."

    niko "Judging by the decomposition, he's been here for at least four to five years. The cold air likely slowed the process, keeping him more preserved than he otherwise would be."

    "I saw something flicker in Chung-hee's expression—something almost unreadable. Disbelief? Concern?"
    "His gaze fell to the corpse's hands, which were stiff with rigor mortis. One was curled tightly around something."
    "Carefully, I stepped closer, mindful not to disturb the fragile remains. My eyes narrowed as I caught a group of glimmering parchment, aged and brittle, yet miraculously intact, clutched between the soldier's fingers."

    svante "A letter. Should we read it?"

    jump ch8_corpse


# =============================================================================
# SECTION 10: LABEL CH8_CORPSE — Read or Not Read the Letter
# =============================================================================
# ch8 txt lines 622-724.
# =============================================================================

label ch8_corpse:

    menu:

        "Read the note.":
            $ ch8_read_letter = True

            # ch8 lines 626-711
            "I reached out carefully, peeling the parchments from the cadaver's grip. As I did, the stiffened arm shifted slightly, causing the torso to slump. The movement dislodged something from beneath the folds of decayed fabric."
            "The parchments were not neatly stacked. They were haphazardly pressed together, their edges frayed and uneven. Some pieces were torn, others stained with something dark and long-dried."
            "Ink had faded, but the words remained—scrawled in uneven strokes, as if written with trembling hands."
            "A testament."

            svante "W-What does it say, sir?"

            "I took a steady breath. The moment my fingers brushed the parchment, a pulse of light flickered across its surface. The letters glowed. A low hum filled the air, like a whisper too faint to grasp—until it wasn't."
            "The words did not stay confined to the pages."

            play sound sfx_painting_glow        # PLACEHOLDER — mind note pulse SFX

            hwan_sik "Baek Hwan-sik, Kyeongjang Protector of Emperor Lord Hyon Min-joon"

            "They echoed in our minds."

            niko "Are all of you hearing this?"

            "A voice—hoarse, weak, filled with exhaustion and regret."

            chung_hee  "A mind note. Whoever wrote this… they channeled their very thoughts onto the parchment."

            # [LETTER — Until I exhaled…]
            play music ost_ch8_letter fadein 1.5 # PLACEHOLDER — sorrowful letter theme

            "Day 1"
            hwan_sik "I failed him. I failed my sworn duty. His Majesty, the Emperor Lord. Pyeha and pyeha-sshi was killed… Murdered in cold blood."
            hwan_sik "Pyeha and pyeha-sshi's body was dragged out by the aldoriths… Bastards that they are…"
            hwan_sik "I do not know if anyone will ever read this, but I must write. If only to keep my mind from slipping. If only to leave something behind when my body joins the others."
            hwan_sik "We came here for knowledge. That was what they told us. His Majesty was led by the rulers and scholars deep into this place. I was ordered to protect him, but I—"
            hwan_sik "I was struck down before I could even raise my blade. Now I am alone."
            hwan_sik "The door is sealed. I have pounded on it until my fists bled. No one is coming."
            hwan_sik "The pain is dulling, which should bring me relief, but it does not. The skin is turning dark. Swollen. I do not think I will last long."

            "Day 3"
            hwan_sik "I found something. A button —hidden beneath dust and debris."
            hwan_sik "It took a while for me to solve the puzzle, but I managed to follow her footsteps. I think I unlocked something."
            hwan_sik "But my hand trembles as I write. The infection is spreading. The veins in my arm are blackened. It hurts to breathe. I hope it gets better tomorrow."

            "Day 5"
            hwan_sik "My arm… the skin is splitting. Fever grips me like a vice. I tried to burn the infection out, but I could not hold the knife steady."
            hwan_sik "I keep hearing things. Scraping in the dark. Breathing. But I know I am alone."
            hwan_sik "Aren't I?"

            "Day 8"
            hwan_sik "The rations are gone. I can barely stand. My stomach feels like a hollow pit. My body is light—too light."
            hwan_sik "The dead are everywhere, but some of them… they should not be this well preserved."
            hwan_sik "Some of them have been here for decades. Maybe centuries. And yet, they have not rotted."
            hwan_sik "I found records. They were studying the dead. What were they trying to do?"
            hwan_sik "Why did they bring rulers, scholars—the Emperor Lord, pyeha, himself—into this cursed place?"

            "Day 13:"
            hwan_sik "I tried everything. Every switch. Every carving. Every prayer I can still remember."
            hwan_sik "I do not have the power to free him. But I know someone is inside that stupid ice. By Xianlun, I do not have the power to free myself."
            hwan_sik "My breath is shallow, my vision fading. The infection has reached my chest. I will not last much longer."
            hwan_sik "I found a container of syringes. A potent sleeping agent. A quiet way to go. There are two. I only need one."
            hwan_sik "But if anyone finds this… if you are reading, hearing these words— Know that Kyeongjang did not fall to cowards."
            hwan_sik "Xianlun, I draw near… Seok-jin, I love you. I'm sorry I couldn't fulfill my promise…"

            "The final lines trailed off, ink smudged and uneven. The last stroke faltered, as if his strength had failed him in his final moments."

            "I exhaled slowly, feeling the weight of the words settle deep in my chest. My fingers tightened around the parchments, the paper crackling slightly in my grip."

            yuxuan "By the Prosperity Dragon…"

            dorian "He knew he wasn't going to make it."

            svante "He… He wanted to be remembered."

            "Chung-hee clasped his hands together, as if in prayer."

            chung_hee  "And so he shall be. Soldier Baek Hwan-sik, Protector of the Emperor Lord…"
            chung_hee  "Your Emperor Lord thanks you. May Xianlun's gates open wide for you, and may you walk among the honored dead of Kyeongjang."

            niko "But why? Why bring the Emperor of Kyeongjang here? What purpose could this place have served?"

            chung_hee  "We will uncover the truth. And we will not leave this place until we do."

            jump ch8_letter_common

        "Don't read the note.":
            $ ch8_read_letter = False

            # ch8 lines 713-723
            "I hesitated. Something about that parchment felt wrong. The sight of the soldier's decaying hand, locked in an eternal grip, sent a chill through me."

            dorian "I don't want to touch that."

            "Chung-hee exhaled slowly, his gaze flicking to me before returning to the corpse."

            chung_hee  "Then I shall take it."
            chung_hee  "This man once swore fealty to the Imperial House of Kyeongjang. Even in death, he remains my subject. It is my obligation to bear witness to his final message."

            "With a careful hand, he pried the brittle parchment from the soldier's grasp. As he did, the stiffened arm shifted slightly, the dried sinew cracking under the pressure."

            jump ch8_letter_common


# =============================================================================
# SECTION 11: LABEL CH8_LETTER_COMMON — Button / Six Paintings Puzzle Setup
# =============================================================================
# ch8 txt lines 725-773.
# =============================================================================

label ch8_letter_common:

    stop music fadeout 1.5
    play music ost_ch8_chamber fadein 1.5

    # ch8 lines 725-773
    "A small object clattered against the stone floor, the faint sound echoing in the silence. Instinctively, I reached down and picked it up, brushing away the dust."

    yuxuan "What's that?"

    "At first glance, it appeared to be just a button—small, round, unassuming. But as the dim light of the cavern illuminated its surface, I realized it was anything but ordinary."
    "The button was exquisitely crafted, its golden frame polished to a mirror sheen despite the years of dust and decay surrounding it. Ornate filigree swirled around its edges, delicate patterns curling like vines embracing the central design."
    "Embedded within the metal was a miniature portrait, impossibly detailed. Even in the flickering glow, I could make out the fine brushstrokes—an artist's delicate hand immortalizing a man's face. But a crack marred the surface, obscuring his features."

    svante "That's a beautiful button… It's so well made. Just like the door earlier."

    "Yuxuan leaned in, frowning."

    yuxuan "Even for someone like me—who appreciates a fair bit of extravagance—this seems excessive. No one puts this much care into a simple button."

    svante "Or… maybe it's more than that! Maybe it's a piece of something greater."
    svante "Too bad we can't see his face, though."

    niko "Let's press it and see what happens."

    "I hesitated for only a breath, then pressed the button."

    play sound sfx_painting_glow                # PLACEHOLDER — painting summon SFX

    "A whisper curled through the air, a voice neither harsh nor gentle—something ancient, something knowing. It slithered around my mind like a serpent, threading through my thoughts with a tone both amused and expectant."

    spirit "If you seek the truth, lay your hand upon the echoes of devotion."

    "Before me, six paintings shimmered into existence, suspended in the darkness like windows to another time. Each one pulsed with an eerie, otherworldly glow—soft but insistent, waiting. Expecting."

    spirit "Touch them all, and only then shall my greatest treasure be revealed."

    "A heavy silence settled over us."

    svante "T-Touch them? Are you sure? All the paintings look beautiful!"

    "His voice cracked slightly, gaze darting between the glowing paintings and me."

    yuxuan "Oh my! These are all exquisite! Can't we all just take them? I'm sure they'd be a wonderful addition to my collection and—"

    dorian "I don't think that's a good idea, Yu."

    niko "It would be foolish to rush in blindly. We have no idea what these represent—or what consequences touching them might bring."

    dorian "It's obviously a trial of some sort. If they wanted us to just tap all six and be done with it, they wouldn't have gone through the trouble of making them appear like this."

    chung_hee  "Agreed. We must proceed with caution. Each one of these may hold a key to understanding what lies ahead."

    "I stepped closer, studying the nearest painting. The light within it flickered, almost as if it were breathing."

    dorian "We should examine them first—one by one. There's no telling what will happen if we touch them all at once."

    svante "R-Right. No reckless touching."

    "I turned my attention to the first painting."

    jump ch8_paintings


# =============================================================================
# SECTION 12: LABEL CH8_PAINTINGS — Six Paintings Examination
# =============================================================================
# ch8 txt lines 774-851.
# =============================================================================

label ch8_paintings:

    $ ch8_puzzle_seen = True

    play music ost_ch8_paintings fadein 1.5     # PLACEHOLDER — mystical paintings theme

    # --- Painting 1: The Loom's Whisper ---
    scene cg_painting_1 with dissolve           # PLACEHOLDER — painting 1 CG
    pause 1.0

    "PUZZLE"
    "The Loom's Whisper:"
    # [PUZZLE1 — Until end of dialogue]
    "A celestial void, vast and endless, swirls with cosmic threads of silver and gold. Radiant hands sculpt the form of a woman, her body emerging from celestial mist."
    "Her body is half-formed, her eyes closed in peaceful slumber, as if she has yet to awaken to the world."

    yuxuan    "The title of this painting is… The Loom's Whisper…"
    niko      "Remarkable. The art style is exquisite."
    svante    "It's kind of eerie, isn't it?"
    chung_hee "Sculpted not just by hands, but by will. By fate. By the Weaver."

    # --- Painting 2: Chains of Choice ---
    scene cg_painting_2 with dissolve           # PLACEHOLDER — painting 2 CG
    pause 1.0

    "Chains of Choice:"
    # [PUZZLE2 — Until end of dialogue]
    "A radiant figure of a woman steps down from a celestial throne, reaching for the hand of a man bathed in soft candlelight."
    "Their fingers intertwine, golden chains barely visible around the divine's wrists, as if binding them to something they are trying to leave behind."
    "In the background, unseen figures watch in silence, their expressions unreadable."

    niko "Galean symbology. Golden chains mean devotion. A vow. A promise you can't break. You were a citizen of Gale, Dorian. Is that true?"

    dorian "Yes. Elara and I were bound in golden chains when we were wed."

    niko "I see. I apologize for bringing that up."

    dorian "No need. The wedding was a fond memory… save for the catering. Elara said it was a disaster."

    # --- Painting 3: Thrones of the Eternal ---
    scene cg_painting_3 with dissolve           # PLACEHOLDER — painting 3 CG
    pause 1.0

    "Thrones of the Eternal:"
    # [PUZZLE3 — Until end of dialogue]
    "Four celestial beings sit upon towering thrones, their forms bathed in an ethereal glow. Time itself seems frozen in reverence, their robes shifting like flowing water despite the stillness. Above them, a golden sun watches, its unblinking gaze heavy with judgment."
    "One throne, covered in flowers, bore the sweet smile of the radiant woman."

    yuxuan "Hmm… her throne is different. Softer. As if she ruled with something the others did not."
    niko   "Flowers and smiles don't rule eternity. They decay. Enoch's throne is carved from obsidian and silence. Cold, clear. Eternal like death itself. That's power."
    yuxuan "\"tHat's pOwEr\"… Hmph!"
    niko   "Are you a child?"

    # --- Painting 4: Wrath ---
    scene cg_painting_4 with dissolve           # PLACEHOLDER — painting 4 CG
    pause 1.0

    "Wrath:"
    # [PUZZLE4 — Until end of dialogue]
    "A radiant figure of a woman sits upon a burning throne, fingers digging into the armrests as fire consumes the sky behind them. Her eyes burn with unrelenting fury, golden banners slashed and torn at their feet."
    "The last remnants of kindness stain her cheek—a single tear, gleaming in the firelight."

    chung_hee "Wrath. Pure and simple wrath."
    yuxuan    "The deadliest emotion."

    # --- Painting 5: Tragedy ---
    scene cg_painting_5 with dissolve           # PLACEHOLDER — painting 5 CG
    pause 1.0

    "Tragedy:"
    # [PUZZLE5 — Until end of dialogue]
    "A winged man looms over a battlefield, clutching the severed head of a fallen man. A radiant figure of a woman kneels in the distance, hands trembling, golden tears slipping down their cheeks. The heavens above are split open with storm clouds, the divine light struggling against the encroaching darkness."

    svante "Oh no… That's heartbreaking."
    niko   "Lord Enoch…"
    dorian "What?"
    niko   "That's him. Lord Enoch. The wings. The markings. The way he holds the severed head like a trophy."
    niko   "Why is he here? Why does he appear in these paintings?"

    # --- Painting 6: When the Stars Watched ---
    scene cg_painting_6 with dissolve           # PLACEHOLDER — painting 6 CG
    pause 1.0

    "When the Stars Watched:"
    # [PUZZLE6 — Until end of dialogue]
    "A bard plays his lute beneath a sky dusted with stars, unaware of the radiant figure of a woman watching him from the garden's edge."
    "Their eyes meet across a reflecting pool, the rippling water caught between two fates. The air hums with something unspoken—something fragile, dangerous, and inevitable."

    svante    "Ahh, a romance! This is the moment where everything changes, isn't it?"
    yuxuan    "*sighs* He must have been very beautiful…"
    chung_hee "Stars do not interfere with the lives of men. They only watch."

    scene bg_inside_sealed_door with dissolve   # Return to chamber bg

    spirit "Do you want to go through the paintings one more time?"

    menu:

        "Yes please.":
            spirit "Very well. Then you may look again. Pay close attention…"
            chung_hee "Let us examine each painting thoroughly, Dorian. Every detail might matter."
            jump ch8_paintings

        "No, I got everything.":
            spirit "Good. Then let us proceed."
            jump ch8_painting_order


# =============================================================================
# SECTION 13: LABEL CH8_PAINTING_ORDER — Touch Order Puzzle (4 Options)
# =============================================================================
# ch8 txt lines 868-907.
# Only option 2 is correct.
# =============================================================================

label ch8_painting_order:

    # ch8 lines 868-907
    spirit "You will touch each fragment with your own hands."

    "I swallowed and looked at my companions, their expressions reflecting the same uncertainty I felt. The paintings loomed before us, waiting."

    dorian "So… which one do we touch first?"

    menu:

        "The Loom's Whisper, Chains of Choice, Thrones of the Eternal, Tragedy, When the Stars Watched, Wrath":

            # ch8 lines 885-896 — WRONG
            "The moment our hands made contact with the final painting, a tremor coursed through the chamber. The air turned thick—almost suffocating—as the spirit's presence swelled, then cracked like fragile glass."
            "A mournful sigh echoed from the unseen depths, the sorrow in it raw and unbearable."

            spirit "No… That is not how it was… That is not how it should be…"

            yuxuan "What?! We were wrong?"

            spirit "I wanted you to see… to understand… but you do not see."

            svante "Unfortunate… Maybe we can try again, sir Dorian."

            niko "Perhaps the paintings show a story. Let's be sure to pay attention."

            jump ch8_paintings

        "The Loom's Whisper, Thrones of the Eternal, When the Stars Watched, Chains of Choice, Tragedy, Wrath":

            # ch8 lines 898-907 — CORRECT
            "As the final painting was touched, the chamber came alive. A golden glow spread from the images, weaving threads of light through the air like strands of fate itself. The very walls pulsed, as if breathing in unison with something ancient."

            spirit "Yes… yes, you see it now."

            "A warmth blossomed in my chest. The paintings shimmered, their colors deepening, details sharpening as if the story they told had never been clearer. The air hummed with power, heavy yet comforting."

            spirit "And so… Here is my greatest treasure."

            chung_hee "Finally. Great job, Dorian."

            jump ch8_painting_correct

        "Thrones of the Eternal, The Loom's Whisper, Tragedy, When the Stars Watched, Chains of Choice, Wrath":

            "The moment our hands made contact with the final painting, a tremor coursed through the chamber. The air turned thick—almost suffocating—as the spirit's presence swelled, then cracked like fragile glass."
            "A mournful sigh echoed from the unseen depths, the sorrow in it raw and unbearable."

            spirit "No… That is not how it was… That is not how it should be…"

            yuxuan "What?! We were wrong?"

            spirit "I wanted you to see… to understand… but you do not see."

            svante "Unfortunate… Maybe we can try again, sir Dorian."

            niko "Perhaps the paintings show a story. Let's be sure to pay attention."

            jump ch8_paintings

        "Thrones of the Eternal, When the Stars Watched, Chains of Choice, The Loom's Whisper, Wrath, Tragedy":

            "The moment our hands made contact with the final painting, a tremor coursed through the chamber. The air turned thick—almost suffocating—as the spirit's presence swelled, then cracked like fragile glass."
            "A mournful sigh echoed from the unseen depths, the sorrow in it raw and unbearable."

            spirit "No… That is not how it was… That is not how it should be…"

            yuxuan "What?! We were wrong?"

            spirit "I wanted you to see… to understand… but you do not see."

            svante "Unfortunate… Maybe we can try again, sir Dorian."

            niko "Perhaps the paintings show a story. Let's be sure to pay attention."

            jump ch8_paintings


label ch8_painting_correct:

    # ch8 lines 910-920 — Common after correct order
    play sound sfx_door_unlock                  # PLACEHOLDER — mechanism unlock SFX

    "Threads of golden light wove through the air, swirling around us like strands of fate finally aligning. The glow seeped into the very walls, making the entire cavern pulse like a living thing."
    "The temperature dropped in an instant. My breath turned to mist, and an unnatural chill settled in my bones."
    "Then, from the very center of the platform, the stone cracked apart. A deafening groan filled the chamber as something massive emerged—a monolith of ice, clear as crystal, towering and flawless."
    "Inside it—a man. A winged man."

    jump ch8_magnus_found


# =============================================================================
# SECTION 14: LABEL CH8_MAGNUS_FOUND — Magnus in Ice / Freed / Awakens
# =============================================================================
# ch8 txt lines 916-1001.
# =============================================================================

label ch8_magnus_found:

    # ch8 lines 916-1001
    # CG: Magnus entombed in crystal-clear ice
    scene cg_magnus_ice with dissolve           # PLACEHOLDER — cg_magnus_ice
    pause 2.0
    scene bg_inside_sealed_door with dissolve

    "His form was perfectly preserved, encased in shimmering frost. Great, feathered wings curled around his body, their tips barely visible through the ice. His face, serene yet hauntingly familiar, stirred something deep within me."
    "My heart pounded. It was him. Magnus."
    "My hands trembled as I reached forward, drawn by something I could not name."
    "Then, a voice—soft at first, but urgent—whispered into my mind."

    dorian "Magnus!"

    yuxuan "Wait… Hold on- That's Magnus?!"

    "Then, a voice—soft at first, but urgent—whispered into my mind."

    magnus "You have found me, Dorian!"

    "I staggered back. The voice wasn't just in my head—it was inside me, resonating through my very soul."

    magnus "Release me, Dorian! Please!!"

    "The plea sent a sharp, aching pang through my chest. This was no illusion. No mere fragment of the past."
    "He was here. He was alive."

    "Svante took a shaky step back, his eyes wide with disbelief."

    svante "D-Did we just unearth a person? This is insane!"

    yuxuan "Wait… is that him?! The winged man from the paintings?!"

    "Niko stepped forward, closer to the ice. His breath fogged the surface."

    niko "No, Yuxuan. The winged man from the paintings was Enoch."
    niko "Interesting… His body is perfectly intact. No decay, no deterioration. This isn't just preservation—this is suspension. He has not aged a single day since he was sealed."

    "The voice called out again, ringing inside my mind."

    magnus "Dorian! Release me, please! Only you can release me from this prison I'm in!"

    dorian "I can hear him. Inside my mind. He's calling my name, begging me to free him."

    chung_hee  "I hope you know what you're doing, Dorian."

    "I swallowed hard, my pulse roaring in my ears."
    "I raised my hands, and the chamber trembled in response. Draconic fire ignited in my palms, gold and crimson, burning with an intensity that set the air ablaze. It crackled and roared, a storm of embers swirling around me, hungry, desperate to be unleashed."

    dorian "Everyone, get back!"

    niko "Move back! Now! Unless you want to be reduced to ash!"

    "The others obeyed, retreating to the edges of the platform as my flames surged higher. I stepped closer, my heartbeat syncing with the pulsing energy coursing through me. This was not just fire. This was will. This was power."
    "I thrust my hands forward, and the fire struck the ice."

    play sound sfx_ice_shatter                  # PLACEHOLDER — ice shattering SFX

    "The ice hissed and cracked, steam curling into the air in thick, suffocating waves. The monolith that had imprisoned Magnus for centuries groaned under the heat, fractures spiderwebbing across its surface."

    spirit "What… WHAT HAVE YOU DONE?!"

    "Then, with a deafening shatter, the ice exploded."
    "Chunks of frozen crystal shot outward, skidding across the stone floor. A final burst of steam engulfed the chamber, obscuring everything in a thick, suffocating mist."
    "Magnus collapsed forward, landing on his hands and knees, his breath ragged, his body trembling. His wings, massive and drenched in melting frost, unfurled in violent spasms, feathers scattering across the floor. Water pooled beneath him, cascading from his skin like he had been submerged in an abyss."

    magnus "*coughing*"

    svante "He must be hurt!"

    "Svante lurched forward, but Niko was already moving. He dropped to one knee beside Magnus, his fingers ghosting over the man's soaked skin before pressing against his throat to check his pulse. His brow furrowed, concern tightening his features."

    niko "Can you hear me? You're breathing too fast—try to slow it down."
    niko "You must have been trapped for a long time. Hypothermia, dehydration—who knows what else."

    "His head hung low, silver hair plastered to his face. And then—"
    "His eyes snapped open."
    "They were white. Glowing, searing, burning with unearthly rage."
    "Then—his voice. A sound that carried the weight of a thousand storms."

    # CG: Magnus awakens, white eyes blazing
    scene cg_magnus_awakens with shock_cut      # PLACEHOLDER — cg_magnus_awakens
    pause 0.5
    scene bg_inside_sealed_door with dissolve

    magnus "YOU KILLED ADRIANA!"

    svante "What?!"
    niko   "?!"

    "His words struck like a hammer, reverberating through the chamber. The walls shook. The abyss itself seemed to tremble beneath us."
    "Before I could speak, before any of us could even breathe—he moved."
    "Lightning-fast, Magnus lunged, his wings snapping open with the force of a hurricane. The ground cracked beneath his takeoff."
    "Magnus soared upward, his entire body wreathed in raw celestial power. Golden veins of energy crackled along his arms, surging through his fingers like barely-contained lightning."

    play sound sfx_divine_pulse                 # PLACEHOLDER — divine energy pulse SFX

    magnus "MONSTERS! YOU'VE TORMENTED MY DREAMS FOR AN ETERNITY! I HAVE DROWNED IN YOUR LIES! BURNED IN YOUR DECEIT!"

    "I shuddered at the sight of him. The silhouette—his form, the eerie glow of his eyes—he looked just like…"
    "I swallowed hard. No. Not just like. It was the same as the death god in the Tragedy of Tianho."
    "A rush of memories crashed into me, merciless and overwhelming."
    "The castle of Tianho—reduced to rubble, its towering spires collapsing in plumes of smoke. The fires—raging, unstoppable, swallowing the city whole. The screams of the fallen, echoing endlessly."
    "Elara. My children. Paladin Cyrus."
    "For a moment, I stood frozen. The memory of the paintings, of Enoch looming over the battlefield, holding a severed head like a trophy—they overlapped. The past, the present. Reality twisted under the weight of it."
    "The chamber warped, the present fracturing under the weight of the past. My vision swam, flickering between now and then, between Magnus and the death god, between the living and the dead."

    dorian "No… No… No, get away! I-I won't let you! I—"

    yuxuan "Dorian! Dorian! You're shaking! Are you alright?"

    svante "Sir Dorian! We have to move! Hurry!"

    "I sucked in a breath, forcing my body to obey. My muscles screamed in protest, locked in the remnants of my memories, but Svante's grip was tough. He yanked me backward with all his strength."
    "A heartbeat later, lightning ripped through the space where I had stood."
    "The force of the blast detonated against the stone, sending white-hot shards flying in all directions. A deafening crack split the air, the floor trembling beneath us as waves of heat seared our skin. I hit the ground hard, the impact rattling through my bones, knocking the breath from my lungs."
    "I hit the ground hard, my breath leaving me in a ragged gasp."

    svante "That was close, sir Dorian."

    chung_hee  "His mind."

    "We turned to look at him."

    chung_hee  "It's being warped. There's something else at work here. I'll figure something out. Buy me some time."

    niko "Sure. But we can't last long if he's this powerful! We need to weaken him!"

    "Above us, Magnus hovered, golden energy writhing around him like a living thing. His breathing was ragged, but his eyes burned brighter than ever."

    niko "Kurayami ni hisomu mono… watashi no koe ni kotae yo, Enoch-sama."

    "The air shuddered. Niko rose to his feet. His usual calm was gone, replaced by a grim determination. His fingers flexed, dark energy coiling around them like tendrils of living shadow."
    "The torches lining the cavern walls flickered violently before being snuffed out—plunging us into darkness."
    "Magnus let out a snarl, his burning gaze snapping to Niko, sensing the shift in power. The golden energy surging around him flared in warning, his wings bristling."

    magnus "YOU DARE CALL UPON THE DARK IN MY PRESENCE?!"

    "The golden energy around him exploded, tearing through the shadows in a violent burst. The sheer force sent ripples through the chamber, scattering tendrils of darkness like smoke caught in a tempest."
    "Niko barely managed to twist away, ducking behind jagged stone as radiant arcs of energy lashed out, carving deep scars into the cavern walls. But even as he evaded, I could see him—still channeling. The shadows coiled around him, writhing, adapting, waiting for an opening."
    "Svante, Chung-hee, Yuxuan, and I huddled behind a jagged stone. The heat of Magnus's power was oppressive, the light burning through the mist of steam left behind by the shattered ice."
    "Chung-hee was deep in thought."

    dorian "What's the situation, Chung-hee?"

    "He didn't respond immediately. His eyes flickered with something unsteady—like he wasn't fully present. His breathing was uneven."

    chung_hee  "Something's very wrong. His mind is in chaos. Broken, fragmented—like shattered glass scattered across a storm. I can sense the echoes of his memories, but they are not whole."

    yuxuan "W-What do you mean? Can you fix it?"

    chung_hee  "It is a labyrinth of torn recollections—some forced upon him, some stolen, some warped beyond recognition. I need a moment to piece them together."

    dorian "Then do what you must, Chung. We'll hold the line."

    "A sudden pulse of divine energy sent tremors through the stone, and Svante turned to me, his breath shallow, eyes darting between Magnus and Niko. His fingers curled into fists."

    svante "Sir Niko needs help."

    "I could see it—the hesitation in his gaze, the silent question behind his words. He was waiting for guidance."
    "I exhaled sharply, mind racing. Svante's a metal channeler. If we were going to turn the tide, I needed Svante to focus his magic on something metallic."
    "Near the rubble, broken spearheads littered the ground—remnants of royal guards who had once stood here. They were crude, but they were large enough to act as a weapon."
    "Scattered all around us were the remains of ancient lantern stands, their metal frames cracked and bent. They weren't as large or sturdy as the spearheads, but their fragmented nature meant Svante could spread his power through them, striking from multiple angles at once. And with Magnus focused on Niko, he might not anticipate it."

    jump ch8_magnus_battle


# =============================================================================
# SECTION 15: LABEL CH8_MAGNUS_BATTLE — Battle QTCs (wing tracker)
# =============================================================================
# ch8 txt lines 1059-1320.
# =============================================================================

label ch8_magnus_battle:

    # [# 42 — Until end of Battle]
    "Quick Timed Choice:"

    menu:

        "Ask Svante to channel the fallen spearheads":
            $ ch8_d2_choice = "spearheads"
            # no wing gain

            # ch8 lines 1066-1082
            "I gripped Svante's shoulder, voice firm."

            dorian "Use the spearheads, Svante."

            "He gave a sharp nod, his eyes narrowing in focus. With a flick of his wrist, the broken spearheads trembled—then shot forward, streaking through the air like jagged bolts of metal, twisting and writhing as they hurtled toward Magnus."
            "At the last second, Magnus' wings snapped open, a radiant gust of golden energy surging outward. The spearheads met his divine aura with a violent clang, stopping mid-air as if colliding with an unseen force."
            "Sparks burst from the impact, the shadows flickering and twisting—but Magnus barely flinched."

            magnus "Pathetic."

            "Before we could react, he raised his hand—and with a single crushing motion, the pillar we were hiding behind detonated, sending shards of rock raining down around us."
            "I barely had time to throw up my arms as the blast sent us sprawling. Dust choked the air, and pain flared through my side as I hit the ground hard."

            svante "*coughs* S-Sorry. My bad…"
            yuxuan "*coughs* I… I think I'm going to be sick…"

            jump ch8_battle_qtc2

        "Ask Svante to channel the fallen lantern stands.":
            $ ch8_d2_choice = "lanterns"
            $ wing_tracker += 1                 # +1 wing

            # ch8 lines 1084-1101
            "I met Svante's eyes."

            dorian "Svante, see the lantern shards around us?"

            svante "Yes, sir Dorian. What do you want me to- Oh… got it."

            "Svante hesitated for only a second before nodding. His hands moved in sharp, precise motions, and the jagged shards of metal hurtled toward Magnus."

            play sound sfx_metal_shards         # PLACEHOLDER — metal shards SFX

            "The shards whistled through the air, moving unpredictably, weaving and darting. They struck Magnus from multiple angles, slashing across his arms, his chest—his wings."

            magnus "AHHH!!!"

            "His body recoiled mid-air, wings jerking as golden blood sprayed into the mist. He staggered backward, his form flickering with instability. For the first time, a look of genuine surprise crossed his face."
            "With a furious roar, Magnus threw out his arm. A burst of divine energy erupted from him like a tidal wave, and before we could react—"
            "The rock pillar we were hiding behind shattered."

            svante "*coughs* Did I do good?"

            jump ch8_battle_qtc2


label ch8_battle_qtc2:

    # ch8 lines 1103-1131
    "Magnus' golden eyes locked onto mine. Fury burned in their depths, raw and seething. His wings flared, sending waves of heat rolling through the cavern."

    magnus "You."

    "My breath hitched."

    magnus "You're the one who haunted my dreams. The tormentor. The deceiver."
    magnus "The VILLAIN."

    "My pulse pounded in my ears. Villain?"

    dorian "Villain? What in Tetrad's name are you talking about? You're the one—"

    magnus "YOU MUST DIE, MONSTER!"

    "Magnus lunged. I barely had a second to react before he closed the distance, his hand wreathed in blinding celestial fire."

    "Quick Timed Choice:"

    menu:

        "Stand my ground and try to block the attack":
            $ ch8_d3_choice = "stand"
            # no wing gain

            # ch8 lines 1119-1131
            "I planted my feet, raising my sword to brace against the impact. If I could just—"
            "Too late."
            "Magnus' strength was monstrous. The instant his strike connected, a shockwave of divine force blasted through me. Pain. White-hot, searing pain. My entire body jerked backward as I was sent flying, crashing against the cavern floor."

            dorian "*coughs* Dragon's bollocks."

            yuxuan "Dorian! Are you alright?!"

            dorian "I'm fine…"

            niko "He's too strong!"

            jump ch8_battle_qtc3

        "Dodge and counter":
            $ ch8_d3_choice = "dodge"
            $ wing_tracker += 1                 # +1 wing

            # ch8 lines 1133-1141
            "I moved."
            "Instinct screamed at me—don't block, don't take it head-on. At the last second, I twisted sharply, the heat of Magnus' strike grazing past my armor instead of slamming into me full force."
            "I used that instant. Draconic fire flared through my hand, and I punched his side. Magnus flinched and staggered."

            magnus "YOU MONSTER! I'LL KILL YOU!"

            niko "Great job!"

            jump ch8_battle_qtc3


label ch8_battle_qtc3:

    # ch8 lines 1143-1202
    "Magnus' wings exploded outward, their sheer size blotting out the dim cavern light. The golden energy rippling from his form turned violent—twisting, writhing, expanding in jagged arcs that scraped against the cavern walls. The sheer force of it sent a storm of dust and debris raining down."
    "Some of the dead bodies were moved and left falling off the central platform."

    dorian "Everyone, grab onto something!"

    yuxuan "Prosperity Dragon, save me!!"

    "Svante almost fell, but he got a knife and attached it to the ground to avoid him falling."

    svante "That was close…"

    "Magnus ascended."
    "The cavern trembled beneath his rise. His wings, drenched in divine radiance, tore through the air, leaving streaks of molten light in their wake. The heat was suffocating, like standing too close to the heart of a dying star."
    "His eyes glew as he spoke."

    magnus "You CANNOT escape me. The gates of Xianlun stand open. They shall welcome you into eternity."

    "And then he descended like a falling sun."

    yuxuan "AHHH!!"

    niko "Shadows, to me!! Kage no subete wa watashi no meirei ni shitagau."

    "Darkness surged from Niko's body, curling like living smoke, devouring the golden light that tried to consume it. His shadows thickened into jagged tendrils, writhing with power, anchoring themselves into the stone like black thorns."
    "The shadows wrapped around Magnus' legs, his arms—clinging, pulling. They thrashed like chains forged from the abyss, tightening with every flick of Niko's wrist."

    magnus "Argh!! Let go of me!"

    "Scattered across the battlefield, metal glinted in the dim light—broken spearheads, shattered lantern shards. Svante lifted a hand, and the pieces shook."

    play sound sfx_metal_shards                 # PLACEHOLDER — metal storm SFX

    "Like a storm of blades, the metal debris whipped through the air, honing in on Magnus with deadly precision. Svante's power magnified them, spinning them faster than any thrown weapon could ever reach."
    "One jagged piece tore across Magnus' wing."

    magnus "AHHHH!! YOU WILL PAY FOR THIS!!"

    "A roar of pain erupted from his throat, shaking the walls, sending dust cascading from the ceiling. His flight wavered, his balance lost for a fraction of a second."

    yuxuan "Who in the Prosperity Dragon's name is this guy?! Why is he this powerful?!"

    "Panic flared in his eyes, but it didn't stop him from acting. With the speed and confidence of a seasoned gambler betting it all, he unscrewed the cap of a flask, wound up his arm, and hurled it straight toward Magnus."
    "It sailed through the air—"
    "And smacked squarely into Chung-hee's shoulder. The impact made the sound of an unimpressively dull thunk."
    "Chung-hee, mid-focus, stiffened. For a brief, fleeting moment, his regal composure cracked, his lips pressing into a thin line as he slowly turned his head to inspect the object that had so rudely interrupted him."

    chung_hee  "Sir Yuxuan, I implore you—cease this senseless barrage immediately."

    yuxuan "S-Sorry! It was a good plan in my head, okay?!"

    "The wind howled. Magnus channeled air, and it responded to him like a vengeful god. The pressure in the chamber shifted violently, turning the space into a raging tempest."
    "A cyclone of sheer force erupted from Magnus' outstretched hand, aimed directly at us."
    "I felt my feet slipping. The ground beneath me vanished as the wind threatened to hurl us into the chasm below."

    svante "T-The wind?! What should we do?"

    "Quick Timed Choice:"

    menu:

        "Counter with fire, trying to burn through the wind.":
            $ ch8_d4_choice = "fire_wind"
            # no wing gain

            # ch8 lines 1204-1224
            "The air raged, trying to throw me into the abyss—but I wasn't going to let it."
            "I called upon my fire. Draconic fire."
            "The warmth ignited within me, coiling in my chest before bursting forth. A roaring pillar of flame surged from my palms, slamming against the wind like a dragon baring its fangs."
            "For a brief second, I thought it would work."
            "The fire and air clashed violently. Instead of overpowering the wind, my flames were swept up into the cyclone—twisting, twisting—turning into something volatile."

            niko "Dorian, STOP!"

            svante "No, no, no—!"

            "An explosion rocked the cavern. The force threw me backward. Agony flared through my arm as I slammed into the jagged stone. The smell of scorched fabric and burnt flesh filled the air."

            dorian "Ghkk—!"

            "Pain. My right arm throbbed, bleeding, burned. Smoke curled from my sleeve, and my vision blurred for a moment."

            magnus "You dare try to match my storms with fire?! You know nothing of loss! Nothing of PAIN!"

            "He lifted his hand again, the air thickening around us, preparing to strike once more."
            "I gritted my teeth. The injury was bad, but I could still fight."

            jump ch8_battle_qtc4

        "Anchor myself with earth channeling and grab onto my companions.":
            $ ch8_d4_choice = "earth_anchor"
            $ wing_tracker += 1                 # +1 wing

            # ch8 lines 1226-1244
            "I slammed my palm against the trembling stone beneath me, channeling earth. The ground answered my call. My energy surged downward, forcing jagged spikes of rock to burst upward, forming desperate footholds. A tether—something to keep us from being swallowed by the storm."
            "The wind still howled. I needed to hold on. I needed to pull the others back before it was too late."

            dorian "Come on! Grab my arm!"

            yuxuan "You're out of your damn mind if you think I'm letting go!"

            "Yuxuan reached first, his grip like iron. He dug his nails into my forearm, anchoring himself against the relentless force."

            svante "I-I can't—!"

            "He was slipping. His feet scraped against the stone, but the wind was too strong. His frame was being dragged straight for the abyss."

            svante "Sir Dorian! Sir Dorian, help please!! AHHH—"
            dorian "Svante!!"

            "A shadow tendril grabbed Svante's arm."

            niko "Are you alright?"

            svante "Yes, sir Niko. T-Thank you."

            "Chung-hee floated, his cape whipping around him like a storm-struck banner."

            chung_hee  "I'm getting the bigger picture of his mind. I'm close!"

            jump ch8_battle_qtc4


label ch8_battle_qtc4:

    # ch8 lines 1246-1282
    magnus "I see that you've wounded me. Villains. Righteousness will have its vengeance!"

    "Magnus exhaled slowly, closing his eyes. The faint scratches on his wings—remnants of our desperate struggle—began to disappear."

    niko "That's… that's not possible."

    svante "H-He just—! That should've taken time!"

    "Magnus' white eyes snapped open. The air shuddered with his presence."

    magnus "You think you can wound me? Me?!"

    "His voice sent a ripple through the chamber. The walls cracked under the sheer force of his rage."

    magnus "I have suffered an eternity of torment. And now, you dare to stand before me as if you are not the architects of my misery?"

    "He stepped forward. Each footfall sent a tremor through the stone."

    magnus "I should rip you apart. One by one. Slowly. Make you feel what I felt when she—"

    "His breath hitched. His fingers twitched."

    dorian "When she what, Magnus?"

    "His expression contorted. His hands clenched into fists."

    magnus "YOU TOOK HER FROM ME!"

    "Divine light ignited."

    niko "You're being unreasonable! We don't know what you're talking about!"

    magnus "LIES! ABSOLUTE LIES! YOU SHAN'T FOOL ME WITH YOUR DECEIT, VILLAIN!"

    "Divine light ignited."
    "It surged from within him—an overwhelming pillar of golden radiance, stretching to the heavens. The light twisted and burned, crackling with unholy power."

    yuxuan "W-What's going on?!"

    svante "He's channeling light… but—"

    "The very air seemed to bend. The cavern rumbled. I looked at Chung-hee, still concentrating on Magnus' mind."

    niko "Damn it! He's not just wielding power—he's devouring it! We're wasting our strength throwing everything at him!"

    "I need to do something."

    "Quick Timed Choice:"

    menu:

        "Counter with Draconic Fire":
            $ ch8_d5_choice = "fire_magnus"
            # no wing gain

            # ch8 lines 1283-1302
            "My instincts screamed at me. Fight back."
            "I channeled my fire, reaching deep within myself. My core burned, the draconic energy roaring to life."
            "The heat within me surged outward, twisting into a spiraling inferno."
            "And yet—It didn't work."
            "Magnus' light consumed my fire."

            dorian "Ghhkk—!"

            "I was thrown backward, my body crashing against the cavern wall. A sharp crack erupted through my arm, a searing pain spreading like wildfire. My vision blurred. Smoke curled from my skin."

            niko "DORIAN!"
            svante "SIR DORIAN!"

            "Their voices were distant, muffled beneath the ringing in my ears. I forced myself upright, my movements sluggish and pained. My fingers curled against my ribs. It hurts."
            "Above me, Magnus hovered, bathed in golden fury, his wings outstretched like a vengeful god descending upon the unworthy. His eyes burned with celestial wrath, locking onto me like I was nothing more than a blasphemer before his throne."

            magnus "You dare fight me? You dare compare your flame to the light of the divine?!"

            jump ch8_magnus_end

        "Reason with Magnus":
            $ ch8_d5_choice = "reason"
            $ wing_tracker += 1                 # +1 wing

            # ch8 lines 1304-1320
            "I clenched my fists, my body begging me to retaliate—but I forced myself to breathe. Think."
            "I looked at Magnus. He wasn't just furious. He was in agony. Grief."
            "I remembered losing Elara, my wife. How it felt."

            dorian "Magnus—stop!"

            magnus "You would dare speak to me?! After what you've done?!"

            dorian "I don't know what happened. But I know you're hurting. Tell me what happened."

            "His wings twitched. The divine light flickered—for just a moment."
            "I stepped forward."

            dorian "We didn't take her from you, Magnus. We don't even know who you mean."

            svante "You think we're your enemies, but we're not!"

            "Magnus staggered. His breath came uneven, his fists clenched so tightly his knuckles turned white. The divine glow around him wavered, like a candle caught in the wind."

            magnus "DECEIT! FOUL VILLAIN!"

            jump ch8_magnus_end


# =============================================================================
# SECTION 16: LABEL CH8_MAGNUS_END — Wing Check / Bad End or Proceed
# =============================================================================
# ch8 txt lines 1322-1381.
# =============================================================================

label ch8_magnus_end:

    # ch8 lines 1322-1381

    if wing_tracker < 3:

        # ch8 lines 1326-1380 — BAD ENDING
        "DIFFERENT OUTCOMES"

        magnus "You think you can deceive me? You think I cannot see the blood on your hands?"

        "And then—he moved."
        "Faster than thought. Faster than we could react."
        "Chung-hee staggered, a radiant blade of light impaled through his chest."
        "His lips parted, but no sound came. The divine energy devoured him from the inside, spreading like wildfire. His body disintegrated into golden dust before he could even scream."

        niko "CHUNG-HEE—!"
        svante "Sir Chung! NO!!"

        "Niko lunged forward, fury igniting in his eyes, shadow engulfing his body."
        "With a flick of his hand, a spear of golden fire erupted from the ground, spearing Niko clean through."
        "He gasped—his eyes wide, his mouth moving soundlessly—"

        niko "Urgh- Ah… Lord Enoch…"

        svante "No, no, no—!"

        "Svante tried to run—a mistake."
        "Magnus reached out."
        "An unseen force gripped Svante's body, lifting him off the ground. His limbs jerked, twisting at unnatural angles as if invisible hands were crushing him from the inside."

        svante "AHHH!!!"

        "His neck twisted violently to the side. His body dropped."

        dorian "Svante! No!"
        yuxuan "Svanteee!!!"

        "Magnus raised a hand. A single, effortless motion."
        "Yuxuan's body crumpled. His breath caught in her throat, his mouth open in a silent scream as his own bones crushed inward, collapsing under the weight of his will."

        yuxuan "D-Dorian… I—"
        dorian "No!! YU!!"

        "Magnus turned his head towards me, slow, deliberate. His wings unfurled, their brilliance unbearable, their presence suffocating."
        "His white eyes locked onto mine. For a fraction of a second, something wavered."

        magnus "Dorian…"

        "His voice—uncertain, shaken."

        magnus "Please! T-This isn't m—"

        "Then, like a blade through glass, the moment shattered. His face twisted, his body tensed—whatever glimpse of clarity had surfaced was drowned beneath raw, consuming fury."

        dorian "M-Magnus?!"

        magnus "DIE, VILLAIN!!"

        "A force wrapped around my throat."
        "I choked, my vision swimming. My body lifted off the ground, my feet dangling in the empty air."
        "My lungs burned. My fingers clawed uselessly at my throat, trying to pry away a force I could not touch."
        "Magnus brought me closer. Face to face."

        dorian "Magnus…*coughs*"

        "His expression was unreadable, but his eyes—those terrible, soulless white eyes—bored into me, stripping me down to my very core."

        magnus "You will feel what I felt."

        "Then suddenly, I saw him. A presence just beyond Magnus, just behind his flickering golden light. A figure watching with quiet amusement."
        "A crown of bone sat atop his head, the twisted remnants of something ancient and cruel."

        yk "Shame… I thought you had what it takes, dragonkin."

        "The last of my breath fled my body."
        "I gasped—a final, desperate sound."
        "And then everything went black."

        jump game_over

    else:

        jump ch8_magnus_peace


# =============================================================================
# SECTION 17: LABEL CH8_MAGNUS_PEACE — Chung-hee Breaks Through / Magnus Calms
# =============================================================================
# ch8 txt lines 1382-1443.
# =============================================================================

label ch8_magnus_peace:

    # ch8 lines 1382-1442
    play sound sfx_divine_pulse                 # PLACEHOLDER — divine light shudder SFX

    magnus "AHHHH!! MY HEAD!!"

    "Suddenly, the divine light around him shuddered before flickering violently, like a sun on the verge of exploding. His wings spasmed. His hands shot up to clutch his head, fingers digging into his skull."
    "His voice tore through the chamber like a dying star. The walls shook. The very ground beneath us quaked as his agony turned into a raw, unfiltered roar of fury."

    magnus "YOU KILLED ADRIANA!! MURDERER! VILLAIN!!"

    yuxuan "There's so much talk of this Adriana. Who is she? We don't even know who she is!"

    "The heat of his rage was scorching. Even as he clutched his head, golden veins of divine energy flared violently across his arms, surging out in wild, uncontrollable bursts. The air around him bent, warped, twisted like reality itself was struggling under his presence."
    "I took a step back, barely stopping myself from instinctively summoning my fire again."

    niko "We didn't kill her, Magnus!"

    magnus "DECEIVERS!"

    "Another pulse of power. A shockwave. Stones rained from above as the cavern cracked apart at the seams."
    "Through it all, Chung-hee stood firm."
    "He placed two fingers against his temple, eyes locked onto Magnus like a hunter sighting prey."

    chung_hee  "Your mind is in shambles, Magnus."

    "Magnus' whole body convulsed. His breathing was ragged, uneven. It was like something inside him was tearing apart—splitting him in two."

    magnus "*panting* I WON'T GIVE IN!! YOU WON'T TWIST ME LIKE HER!! I'LL KILL YOU ALL!"

    chung_hee  "You were frozen for centuries. You have no real memory, Magnus."

    "Magnus snarled. He fought against it."

    magnus "YOU LIE!"

    "He slammed a fist into the ground. The earth ruptured beneath him in a violent, golden explosion."
    "I staggered back, shielding my face as dust and debris erupted around us."
    "But Chung-hee didn't move."
    "His voice remained calm. Unyielding."

    chung_hee  "All your memories—they were implanted. Fabricated. Artificial."

    "I was in shock. Fabricated memories?"
    "Magnus' breath hitched."
    "For a second, the divine light around him faltered. But then—he roared again."

    magnus "NO! NO! I REMEMBER HER! I REMEMBER HER SMILE! I REMEMBER HER HAND IN MINE! YOU WON'T TAKE THAT FROM ME!"

    "Magnus' breath came in ragged, seething gasps. His body trembled—whether from pain or fury, I couldn't tell. His wings remained outstretched, the divine light flickering chaotically along the edges like an unstable flame."

    magnus "Y-You're trying to twist me. Trying to make me forget her."

    chung_hee  "Calm down, Magnus. We're just as confused as you are."

    "Magnus' wings twitched. His muscles tensed, but something in his expression… shifted."
    "Doubt."
    "Hesitation."

    chung_hee  "We aren't your enemies. We aren't here to hurt you."

    "Magnus' gaze snapped to me instantly, his entire body coiled like a predator ready to pounce."
    "I extended my hand."

    dorian "See? We're not out to get you."

    "His chest heaved. His wings twitched. But he didn't move."
    "I followed his line of sight—to the shattered ice. The ice that had once entombed him."

    dorian "We freed you, Magnus."

    "For a long, aching moment, Magnus just stared."
    "His fingers twitched. His lips parted. The divine light around him dimmed."
    "A choked breath escaped him."

    magnus "Everything I knew… everything I remembered… was a lie?"

    "Magnus' hand trembled as he stared at mine. His breath was shallow, unsteady. For a moment, I thought he would refuse—thought he would pull away, retreat into his fury."
    "But then—his fingers twitched."
    "His shoulders sagged, as if the weight of centuries was suddenly crushing him all at once."
    "And he took my hand."

    jump ch8_walk_back


# =============================================================================
# SECTION 18: LABEL CH8_WALK_BACK — Return to Lab / Magnus Collapses / Sleep
# =============================================================================
# ch8 txt lines 1445-1474.
# =============================================================================

label ch8_walk_back:

    # ch8 lines 1445-1473
    # [COMMENT: bg_tianho_underground_2 — walk back through refined tunnel]
    scene bg_tianho_underground_2 with fade     # PLACEHOLDER — underground tunnel 2
    stop music fadeout 2.0
    play music ost_ch8_end fadein 2.0           # PLACEHOLDER — quiet relief theme

    "--[ BG - Tianho Underground 2 – Normal ]"
    "The walk back to Yuxuan's hidden laboratory was uneventful. None of us spoke much—our minds still reeling from everything that had happened. The discovery of Magnus, the battle, the truth behind his memories… it was too much to process all at once."
    "Magnus barely made it halfway before his strength gave out. His body, once brimming with divine power, now seemed fragile—human. He collapsed, barely conscious, his breathing shallow but steady."
    "I caught him before he hit the ground, feeling the unnatural heat still lingering beneath his skin. His wings were dragging on the cave floor."

    # ch8 lines 1454-1474
    scene cg_black with fade                    # PLACEHOLDER — black screen

    stop music fadeout 1.0

    "When we finally reached the laboratory, Roboto was on edge. It seemed to sense the tension. It moved toward Magnus, scanning him with mechanical precision before giving a small nod."

    roboto "H-H-HHe requires rest. I have prepared a bed. Please f-f-follow me."

    "We did as it instructed, laying Magnus down on the softest mattress we could find. His face was pale, his breathing slow but even."
    "With that done, the rest of us barely managed to settle in before exhaustion dragged us under. The moment my head hit the pillow, I felt myself slipping into the depths of sleep."
    "The day had been long. Too long. And as my consciousness faded, I could only hope that tomorrow would bring more answers."

    "CHAPTER 9"

    # ch8 lines 1467-1473 — bridge to ch9
    # [COMMENT: bg_lab_bedroom_normal — soft light, comfortable bed, chapter 9 begins]
    scene bg_lab_bedroom_normal with fade       # PLACEHOLDER — lab bedroom, soft morning light

    "I woke to the softest, most comforting scent. The warm aroma of freshly laundered sheets mixed with something faintly sweet—like the lingering traces of vanilla and sun-dried cotton."
    "The fabric cradled me in its gentle embrace, and for a moment, I considered sinking deeper into its warmth. But then, the sound of soft munching reached my ears."
    "I blinked my eyes open, taking in the dim light of the fixtures."

    stop music fadeout 3.0
    stop audio fadeout 2.0

    pause 2.0

    show screen chapter_title_screen(
        "8",
        "Behind the Sealed Door",
        subtitle="END",
        duration=3.0
    )
    pause 3.0

    jump chapter_9


# =============================================================================
# END OF CHAPTER 8
# =============================================================================
