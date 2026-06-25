###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  FILE:  chapter_08.rpy
#  SCENE: CHAPTER 8 — Behind the Sealed Door
###############################################################################

# =============================================================================
# SECTION 1: CHARACTER DEFINITIONS
# =============================================================================
# moved to compiled file

# =============================================================================
# SECTION 2: IMAGE DECLARATIONS
# =============================================================================
# moved to compiled file

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

    scene bg_cheng_bunker with fade
    play music ost_ch8_tunnel fadein 2.0        # PLACEHOLDER — tunnel theme

    show feng_suit at right_char with Dissolve(0.2)
    "Then—a chuckle."
    "The flickering firelight cast shadows over his face as he leaned back slightly, tilting his bottle lazily toward me. He grinned."

    feng "Heh. Alright, alright. No need to be so serious."
    feng "You always did have a way of making things dramatic, old friend. But I get it."

    "He lifted the bottle in an easygoing mock toast."

    feng "See you tomorrow. Try not to get yourself killed before then, yeah?"

    hide feng_suit
    show dorian neutral at left_char with Dissolve(0.2)
    "I gave him a nod before turning away, leading the others forward."
    "As we moved through the dimly lit corridors of the camp, I caught the faintest sound of Feng taking another long drink."

    show aoi_battle_suit at right_char with Dissolve(0.2)
    aoi  "Another wine bottle, sir?"

    hide aoi_battle_suit
    show feng_suit at right_char with Dissolve(0.2)
    feng "Sure thing, Aoi."

    hide feng_suit
    hide dorian

    "CHAPTER 8"

    scene bg_tianho_underground_2 with dissolve  # PLACEHOLDER — tunnel / path

    show weng normal at right_char with Dissolve(0.2)
    show tim normal at right_char_kids with Dissolve(0.2)
    "The journey to Yuxuan's lab was quiet, save for the occasional shuffle of boots against the dirt. Above us, the night stretched vast and endless, a deep indigo canvas speckled with stars, their cold glow barely enough to illuminate the path."
    "A hush had fallen over our group, the weight of the night pressing in, thick with unspoken thoughts."
    "I kept a watchful eye on our surroundings, my senses tuned to any shift in the air, but the night remained undisturbed. Meanwhile, Svante found a brief distraction, chatting softly with Tim, who clutched Weng's hand while balancing his plastic bags of Hinami flan."

    weng "By the stars, my back is starting to ache… Tim, are you sure you can finish all of that?"

    show tim happy at right_char_kids
    tim  "Positive, Miss Weng!"

    hide weng
    hide tim happy

    scene bg_underground_door with dissolve     # PLACEHOLDER — lab entrance door

    "After a while, we reached the entrance of Yuxuan's lab. The same towering door of polished metal loomed before us. Like before, it spoke as we approached."

    "Door: Facial recognition is currently in progress. Please refrain from excessive movement."
    "Door: Initiating secondary verification. Please present a valid voice signature."

    show weng normal at right_char with Dissolve(0.2)
    weng "Cai Weng. Master Yuxuan's assistant."

    "Door: Processing… Please provide a biological confirmation."

    hide weng
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "Chung-hee exhaled sharply, folding his arms. His gaze flicked to Weng before trailing over the towering metal door."

    chung_hee "Isn't this… excessive? Must a simple door be guarded like a royal vault?"

    hide chunghee normal_neutral
    show niko normal_base at right_char with Dissolve(0.2)
    "Niko raised a brow, glancing at him."

    niko "They don't have security systems like this in Kyeongjang, huh?"

    hide niko
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "We have, but not this excessive."

    hide chunghee normal_neutral
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "You have these in Kyeongjang too, Your Majesty?"

    hide svante
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "Chung-hee let out a quiet scoff, shaking his head."

    chung_hee "Yes, but not even our palace gates demand so much proof of existence."
    chung_hee "And again, Svante. Call me Chung."

    hide chunghee normal_neutral
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "S-Sorry, Your Majesty. I mean Sir Chung."

    hide svante
    "The door let out a low beep, and the heavy locks shifted with a mechanical hiss."

    "Door: Identity confirmed. Welcome home, Miss Cai Weng. May the blessings of the Prosperity Dragon be with you this wonderful night."
    "Door: Here at Cheng's we bring change."
    "~Here at Cheng's we bring change.~"

    show niko normal_ignore at right_char with Dissolve(0.2)
    niko "Merciful Enoch, I can't seem to escape that damn jingle."

    hide niko
    "The seamless metal parted, revealing the pristine interior of the lab."

    # play sound sfx_roboto_beep               # PLACEHOLDER — not declared

    show roboto happy at right_robot with Dissolve(0.2)
    "Roboto whirred forward. Its polished exterior reflected the glow of the overhead panels, giving it an almost ghostly sheen in the dim light."

    roboto "G-G-G-Good evening, Master Dorian. Master Yuxuan is t-t-taking a n-n-n-nap."
    roboto "He r-r-requested me to show you y-y-y-your d-d-destination."

    hide roboto
    show svante normal_neutral at right_char with Dissolve(0.2)
    svante "Sir Yuxuan… naps?"

    hide svante
    show niko normal_base at right_char with Dissolve(0.2)
    niko "He's a human being. Of course he gets tired."

    hide niko
    show weng normal at right_char with Dissolve(0.2)
    "Weng turned to us, her gaze gentle but firm as she placed a guiding hand on Tim's back."

    weng "Are you sure about this, Sir Dorian? If so, this is where we part ways for now. Roboto will be leading you to the door in your dream."
    weng "Tim and I are already feeling tired. These old bones of mine aren't helping."

    show tim normal at right_char_kids with Dissolve(0.2)
    tim  "N-No I'm not *yawns* I'm more than willing to- *yawn*"

    show weng happy at right_char
    "Weng chuckled softly, shaking her head."

    weng "I apologize. If I were younger I would have *yawn*"

    "She yawned, covering her mouth as fatigue settled into her features."

    hide weng
    show svante normal_happy at right_char with Dissolve(0.2)
    svante "Don't worry, miss Weng."

    hide svante
    show tim sad at right_char_kids with Dissolve(0.2)
    "Tim pouted but gave a small wave."

    tim  "Aww… But take care, sirs! See you *yawns* tomorrow."

    hide tim sad
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "We will, Tim."

    hide chunghee normal_neutral
    show weng normal at right_char with Dissolve(0.2)
    weng "I'll check on Elias and Tedda for you before we go to sleep, Sir Dorian. Take care."

    show dorian neutral at left_char with Dissolve(0.2)
    "I met her gaze and gave a slight nod."

    dorian "Thank you, Miss Weng. I appreciate it."

    hide weng
    "She gave me a knowing look before turning away, leading Tim inside. The metal door slid shut behind them with a quiet hiss."

    show roboto happy at right_robot with Dissolve(0.2)
    "Roboto whirred again, its headpiece swiveling slightly as it pivoted toward the darkened corridor ahead."

    roboto "F-F-Follow me, sirs. T-T-This way…"

    hide roboto

    scene bg_tianho_underground_2 with dissolve # PLACEHOLDER — underground tunnel 2
    play audio amb_cavern_deep loop fadein 1.5   # PLACEHOLDER — deep cavern ambient

    show dorian neutral at left_char with Dissolve(0.2)
    "It pivoted forward, its legs gliding smoothly over the damp ground. The corridor stretched out before us—a vast, quiet expanse of reinforced tunnels lined with cold stone and compacted earth. The air was thick with the scent of damp earth and soil."
    "As we walked deeper into the tunnel, our footsteps echoed softly against the stone, swallowed by the dim, cavernous passage."
    "I let my gaze drift across the tunnel's edges, where faint etchings ran like veins along the surface—symbols and patterns I didn't recognize—worn, weathered, nearly erased by time, yet still clinging stubbornly to the walls surface."
    "I narrowed my eyes, reaching out to brush my fingertips against one of the engravings. The texture was uneven, the grooves shallow but deliberate."

    dorian "So, Roboto, do you have any background of how these tunnels came to be?"

    show roboto happy at right_robot with Dissolve(0.2)
    roboto "M-Master Yuxuan and his partners d-d-discovered these tunnels b-by accident."

    hide roboto
    show niko normal_base at right_char with Dissolve(0.2)
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    hide niko
    "Niko and Chung-hee exchanged a glance with me. The tunnels were older than Yuxuan?"

    show roboto happy at right_robot with Dissolve(0.2)
    roboto "The original creators are… u-u-unknown. However, some data suggest that they predate the c-c-current settlements"

    hide roboto
    show svante normal_neutral at right_char with Dissolve(0.2)
    svante "The creators might predate the current settlements? So that means…"

    hide svante
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "There is a distinct possibility these tunnels were built long ago, before any of our cities existed."

    hide chunghee normal_neutral
    "I turned my attention back to the etchings. There was something about them, something unsettlingly intricate. The longer I looked, the more I felt a strange sense of familiarity, like I had seen them before in a dream or in the remnants of some old myth."
    "The tunnel stretched endlessly before us, its ancient markings bathed in the cold, sterile glow of the fixed lights embedded in the walls. The artificial brightness clashed against the archaic surroundings, like two worlds trying to coexist."

    show dorian neutral at left_char
    dorian "And where exactly in the tunnel are you taking us?"

    show roboto happy at right_robot with Dissolve(0.2)
    "Roboto whirred again, tilting its metallic headpiece slightly."

    roboto "T-To the end of the tunnels."

    "It hesitated for the briefest of moments, as if its internal systems were recalibrating its response. Then, it spoke again, its voice more certain this time."

    roboto "The m-m-massive d-d-door with the Prosperity Dragon illustration… It l-l-lies ahead. At the end of the tunnels."

    hide roboto
    "The group fell into a heavier silence as we continued walking, the weight of Roboto's words settling over us. Each step forward felt like a step into something long buried, something not meant to be disturbed."

    jump ch8_door_chamber


# =============================================================================
# SECTION 6: LABEL CH8_DOOR_CHAMBER — The Dragon Door / Yuxuan Reveal
# =============================================================================

label ch8_door_chamber:

    scene bg_underground_the_door with fade     # PLACEHOLDER — domed chamber, the Dragon Door
    stop music fadeout 1.0
    play music ost_ch8_door fadein 2.0          # PLACEHOLDER — ancient reverent theme

    hide dorian
    "Minutes later, the tunnel finally widened, revealing a vast, domed chamber. And there—standing at the farthest point—was the door."
    "There's no mistaking it. It was the same door in my dream. The Prosperity Dragon stretched across its surface in breathtaking detail. Its body coiling through storm-wracked clouds."
    "Then, out of the corner of my eye, I saw movement."
    "A hooded figure stood at the base of the door, partially concealed in the shadows. My muscles tensed, instinct kicking in. Then, in one fluid motion, the figure lifted their hand and pulled back the hood."
    "Yuxuan's face emerged from beneath the fabric, illuminated by the dim glow of the chamber."

    show yuxuan alt_smirk at right_char with Dissolve(0.2)
    yuxuan "You're late, buddy."

    "For a moment, none of us moved."

    show dorian neutral at left_char with Dissolve(0.2)
    dorian "Yu… you're here."

    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "I hope you weren't waiting long."

    hide chunghee normal_neutral
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "We—we thought you were sleeping!"

    hide svante
    show niko normal_base at right_char with Dissolve(0.2)
    niko "Shouldn't you be in bed?"

    hide niko
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    "Yuxuan, unbothered as ever, smirked. He shifted his weight onto one foot, crossing his arms."

    yuxuan "What can I say? The idea of you wandering through my tunnels unsupervised was more terrifying than losing a little sleep."

    "And then—Roboto twitched."
    "The bot, which had been standing dutifully beside us, suddenly jolted. A harsh electronic screech cut through the chamber, its optics flickering erratically."

    show roboto malfunction at right_robot with Dissolve(0.2)
    roboto "E-E-E-E-Error. E-E-E-E-Error. P-P-P-Para-d-d-d-d-d—"

    hide roboto
    "With a sudden, jerky movement, it spun on its wheels and bolted down the corridor, its metallic limbs twitching as if something had taken hold of its systems."
    "We all turned, watching as it disappeared into the darkness, its garbled stuttering echoing until it was gone."
    "I glanced back at Yuxuan, half-expecting him to look concerned. But instead— he let out an exaggerated sigh, his smirk never faltering."

    show yuxuan alt_smile at right_char with Dissolve(0.2)
    yuxuan "Guess even my trashy machines can't handle the grandeur of my genius."

    hide yuxuan
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "He waved a hand dismissively, as if Roboto's erratic malfunction was of no concern. Chung-hee furrowed his brow, arms crossed."

    chung_hee "Oh, do they?"

    hide chunghee normal_neutral
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    "Yuxuan's grin didn't waver, but his fingers twitched at his side before he threw up his hands in mock surrender."

    yuxuan "Of course, Your Majesty! I assure you, everything is perfectly under control."
    yuxuan "But enough about my poor, overworked machines. Let's turn our focus to the real star of the show, shall we?"

    "He gestured dramatically toward the massive door, its intricate carvings gleaming under the dim light."

    hide yuxuan
    show niko normal_base at right_char with Dissolve(0.2)
    niko "Dorian, is this the same one that you saw on your dream?"

    hide niko
    show dorian neutral at left_char
    "I stepped forward, my gaze tracing the magnificent structure. The closer I got, the more I could see the painstaking detail."
    "Its sinuous body in a mesmerizing display of movement, despite being frozen in metal. Every scale was meticulously sculpted, each ridge catching the dim light, making it seem as if the dragon were shifting in place."
    "Its eyes, inlaid with polished jade, gleamed with an eerie lifelike quality. Though unmoving, they seemed to watch us, reflecting the dim chamber light like distant stars in the void."

    show svante normal_happy at right_char with Dissolve(0.2)
    svante "Incredible… I bet even the most skilled earth channelers would struggle to sculpt something this detailed."

    "His fingers twitched at his side, as if he were resisting the urge to reach out and confirm that the door was real—that something this perfect hadn't just been imagined into existence."

    hide svante
    show yuxuan normal_happy at right_char with Dissolve(0.2)
    yuxuan "Amazing, right?"

    hide yuxuan
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "A creation worthy of the Tetrad themselves. Not a single detail out of place. This was not simply built—it was bestowed."

    hide chunghee normal_neutral
    show niko normal_serious at right_char with Dissolve(0.2)
    "Niko, hands clasped behind his back, studied the metalwork with a careful eye."

    niko "Whoever created this was clearly more than just a master craftsman… They were a devout worshiper of the Prosperity Dragon."
    niko "I highly doubt that a pagan or a mere artisan would dedicate their waking hours to crafting something this impossibly intricate. This isn't just an offering—it's a declaration."

    "He let his fingers trail over the carved ridges of the dragon's body, his tone growing contemplative."

    niko "This level of precision… the sheer reverence in the way each scale, each line, each curve has been etched—it's not just talent. It's faith."

    hide niko
    "The chamber was silent, save for the quiet hum of flickering lights and the faint, distant sound of shifting metal in the tunnels beyond."
    "Then, Svante hesitated before speaking, glancing at Chung-hee with curiosity."

    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "You worship the Tetrad, right, Your Maj— I mean, Sir Chung? Do you have sculptures like this back in Kyeongjang?"

    hide svante
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "As a matter of fact, we do."
    chung_hee "In the Imperial Capital, we have towering sculptures of each of the four Immortal Tetrads."
    chung_hee "Adriana, the Immortal Tetrad of Emotion and Kindness, standing at the gates of the Celestial Palace of the Emperor Lord. A reminder for the Emperor Lord's responsibility to rule with kindness and mercy."
    chung_hee "Meanwhile, in the great halls of justice, a solemn statue of Renji, the Immortal Tetrad of Justice and the Void."
    chung_hee "The Grand Library of Kyeongjang houses a magnificent sculpture of Li Mengtia, the Immortal Tetrad of Knowledge and Wisdom. Visitors see his face each time they seek guidance in the pursuit of knowledge."
    chung_hee "And in the heart of the imperial gardens, the most revered of them all—Saelara, the Immortal Tetrad of Creation, is immortalized in marble. Her outstretched hands hold an intricate celestial map, a reminder that creation itself is a gift to be cherished and honored."
    chung_hee "These sculptures were all commissioned by my great great great grandfather, one of the late Emperors of Kyeongjang. He believed the Tetrad's presence should not only be felt but seen, woven into the very foundation of the empire."

    hide chunghee normal_neutral
    show svante normal_happy at right_char with Dissolve(0.2)
    svante "Wow… what I wouldn't give to see them, sir."

    hide svante
    show yuxuan normal_happy at right_char with Dissolve(0.2)
    "A quiet chuckle broke through the solemn air."

    yuxuan "Hahaha! You hit the nail in the head there, Chung-hee. That's a theory I had when I first found this tunnel."

    "His gaze remained locked on the dragon-carved door, a glint of something unreadable in his sharp eyes. He lifted a hand, tracing the air just above the intricate engravings."

    show yuxuan normal_neutral at right_char
    yuxuan "My partners and I stumbled upon these tunnels completely by accident, and since then, I've been studying this door for years. Ever since the Tragedy of Tianho."

    "Then, with a smooth motion, he turned to face me and Chung-hee directly, holding out his palm."

    yuxuan "Now then. The amulets. Hand them over."

    show dorian serious at left_char
    "I stiffened. The amulets? My fingers instinctively curled around the cool metal resting in my pocket."
    "Slowly, I withdrew it—the amulet I had found on Elias when I first found him. Its surface gleamed under the dim tunnel light, an intricate pattern of old symbols carved into the metal."

    dorian "I have it, Yu. But why?"

    show yuxuan normal_neutral at right_char
    "He motioned toward the door, his fingers ghosting over the carvings of the Prosperity Dragon once more."

    yuxuan "This door is sealed. My theory is that it has been for far longer than any of us have walked this land."

    "He glanced at me and Chung-hee, his expression unreadable."

    yuxuan "Something is inside this. Something ancient."
    yuxuan "It won't open for just anyone. You can't break through it with brute force. We already tried."

    hide yuxuan
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "Chung-hee crossed his arms, his tone cautious."

    chung_hee "Then have you discovered what does open it?"

    hide chunghee normal_neutral
    show yuxuan alt_think at right_char with Dissolve(0.2)
    "Yuxuan smiled faintly, as if pleased by the question."

    yuxuan "Draconic fire. Only a channeler of draconic fire is strong enough to awaken the engravings can unlock the seal. That, and… the two amulets."

    hide yuxuan
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "D-Draconic fire? Are you sure, Master Yuxuan? You mean Sir Dorian…"

    hide svante
    show dorian neutral at left_char
    "I exchanged a glance with Chung-hee, my grip tightening around the amulet."

    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "And you're certain about this?"

    hide chunghee normal_neutral
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "I wouldn't ask if I weren't."

    "Yuxuan huffed a quiet laugh, tilting his head slightly. Still, neither of us moved to hand them over."
    "Yuxuan, sensing our hesitation, took a step closer, his voice dipping into something softer—something personal."

    yuxuan "Dorian. You found that amulet on Elias, didn't you? That poor little child. That amulet was given to him by his mother—Queen Ekaterina. You were there when he lost everything. At that cave."

    show dorian serious at left_char
    "The mention of it made my jaw tighten. Snow. Darkness. The relentless howling wind. The way Elias had clung to that amulet like it was his last tether to the world."

    dorian "What are you getting at, Yu?"

    show yuxuan normal_neutral at right_char
    "Yuxuan exhaled, shaking his head slightly, as if he couldn't believe I had to ask."

    yuxuan "I'm saying… who helped you and little Elias when you were trapped in Frostcradle during the blizzard? When the cold was closing in and there was no way out?"

    "He took a step closer, tilting his head."

    yuxuan "It was me, wasn't it?"

    show dorian neutral at left_char
    "My grip on the amulet tightened."

    show yuxuan normal_neutral at right_char
    yuxuan "You and Elias would've starved to death in that cave if I hadn't gotten you both out."

    show dorian smile at left_char
    dorian "Yes. I do, Yu. Always."

    "I smiled at Yuxuan and gave him the amulet."

    show yuxuan normal_happy at right_char
    yuxuan "Thank you for your trust, Dorian."

    "He winked at me, a mischievous smile on his lips."

    hide yuxuan
    hide dorian
    "The familiar voice, vast as the sky and deep as the roots of the earth, roared in my head."
    "A blinding white light swallowed my vision."

    # prosperity_dragon — voice only, no sprite declared
    prosperity_dragon "YOU HAVE BEEN DECEIVED, CHILD!"

    show dorian angry at left_char with Dissolve(0.2)
    "A sharp pain lanced through my skull. My breath caught."

    dorian "ARGH! What do you mean?"

    prosperity_dragon "GET BACK THE AMULET, CHILD! OBEY!"

    "And then—silence. The light vanished."
    "I staggered, the room spinning as reality snapped back into place."
    "My heart pounded against my ribs like a war drum."

    show niko normal_serious at right_char with Dissolve(0.2)
    niko "Dorian, are you alright?"

    show dorian neutral at left_char
    dorian "I-I'm fine…"

    hide niko
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "And what about you, Your Majesty?"
    yuxuan "You left Kyeongjang with a purpose, didn't you? And when you return home, Your Majesty, what will you say? What will your aunt think?"
    yuxuan "That you came all this way, held the key to something far greater, and did nothing."

    jump ch8_impostor


# =============================================================================
# SECTION 7: LABEL CH8_IMPOSTOR — Chung-hee Reveals Yuxuan Is a Yaoguai
# =============================================================================

label ch8_impostor:

    hide yuxuan
    show chunghee alt_tense at right_char with Dissolve(0.2)
    "The shift in Chung-hee was immediate. His entire demeanor darkened, his jaw tightening as his hands curled into fists at his sides."

    chung_hee "Where did you get that?"

    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "Pardon, Your Majesty?"

    hide yuxuan
    show chunghee alt_tense at right_char with Dissolve(0.2)
    chung_hee "Where did you find out about my aunt?"
    chung_hee "I never told any of you about her. I never spoke of my family—any of them."

    hide chunghee alt_tense
    "Silence hung between us, heavy and suffocating. My mind raced. Chung-hee had never once mentioned an aunt. All we knew was that his parents had perished in the Tragedy."

    show yuxuan alt_smirk at right_char with Dissolve(0.2)
    "Yuxuan, unfazed, merely offered a small, knowing smile. He tilted his head, amusement flickering in his expression."

    yuxuan "I have my ways. I make it a point to know things. Call it… connections."

    hide yuxuan
    show niko normal_serious at right_char with Dissolve(0.2)
    niko "Connections? To Kyeongjang? With all due respect, you don't actually expect us to believe you have ties there, do you, Yuxuan?"

    hide niko
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "He does have a point, sir Yuxuan."

    hide svante
    "And then I felt it."
    "A pressure in the air, like static crawling beneath my skin. My body tensed instinctively."

    show chunghee alt_charging at right_char with Dissolve(0.2)
    "Chung-hee exhaled slowly, closing his eyes for a fleeting moment before opening them again—sharper, burning with quiet fury. His fingers twitched at his sides, lightning crackling faintly along his knuckles."

    chung_hee "…I apologize for this."

    "It was the only warning we got."

    # play sound sfx_lightning_ch8             # PLACEHOLDER — lightning SFX

    hide chunghee alt_charging
    "Before anyone could react, a surge of raw energy erupted from his fingertips. A bolt of lightning, blinding and furious, shot straight toward Yuxuan."

    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "SIR—!"

    hide svante
    "The crackling energy illuminated the chamber in a violent flash."
    "The electricity struck Yuxuan dead-on, his body convulsing violently as arcs of energy danced across his frame. The smell of singed fabric filled the air, and for a single, agonizing moment, all I could hear was the crackling of lightning fading into silence."

    show dorian angry at left_char with Dissolve(0.2)
    dorian "YU!! NO!!"

    "Panic surged through me as I rushed forward, heart pounding in my chest. The others weren't far behind, though they weren't running to help—no, they were turning on Chung-hee."

    show svante normal_angry at right_char with Dissolve(0.2)
    svante "SIR CHUNG, WHAT DID YOU JUST DO?!"

    hide svante
    show niko normal_anger at right_char with Dissolve(0.2)
    niko "Chung, are you insane?! That was completely uncalled for!"

    hide niko
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "Chung-hee didn't respond at first, his posture rigid, hands still crackling with fading electricity."

    chung_hee "That was not Yuxuan."

    hide chunghee normal_neutral
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "Sir Chung! What in Enoch's name are you talking about?! He's right there, dying!"

    hide svante
    "A low, guttural sound filled the chamber. The body on the ground twitched, spasming unnaturally before its limbs jerked at odd angles. Bones cracked, skin rippled, and for one terrifying moment, its face melted into something grotesque."
    "A yaoguai."

    # yaoguai — no standard sprite declared, voice-only
    yaoguai "Ra-Ra-RAAAWWWRRR!!!"

    show niko normal_serious at right_char with Dissolve(0.2)
    "My stomach twisted. Yuxuan had been a yaoguai this whole time?!"

    niko "Enoch above… What is going on here?!"

    # play sound sfx_roboto_beep               # PLACEHOLDER — not declared

    show roboto happy at right_robot with Dissolve(0.2)
    roboto "A-A-A-A-Alert. M-M-M-Master Yuxuan is here…"

    hide roboto
    "We all whirled around just in time to see Roboto clanking down the tunnel. And beside him—"
    "Another Yuxuan."

    show yuxuan normal_angry at right_char with Dissolve(0.2)
    "This one was completely unharmed, holding a steaming cup of coffee with an irritable scowl on his face. His robes were slightly disheveled, his long hair loose over his shoulders like he'd just rolled out of bed."
    "He blinked blearily at us before groaning."

    yuxuan "What in the Prosperity Dragon's name is going on!!"

    "He took a long, frustrated sip of coffee before pointing an accusatory finger at Roboto."

    yuxuan "There better be a good reason for waking me up, Roboto!"

    show dorian neutral at left_char
    dorian "Wait… Yu?"

    hide yuxuan
    show svante normal_neutral at right_char with Dissolve(0.2)
    svante "…Umm. What just happened?"

    hide svante
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    "The moment Yuxuan's gaze landed on the grotesque, convulsing form of the yaoguai, his entire body tensed. His eyes widened in sheer terror, and his grip on the coffee cup slackened."

    yuxuan "E-E-EEEKKKK!!!"

    "With an unceremonious yelp, he leaped backward, dropping his drink as his free hand flailed in panic. His breath came in sharp, ragged gasps as he pointed a trembling finger at the writhing creature."

    yuxuan "HOW DID IT GET IN HERE?! DORIAN!! HELP!!"

    hide yuxuan
    show niko normal_ignore at right_char with Dissolve(0.2)
    niko "Oh brother…"

    hide niko
    show dorian neutral at left_char
    dorian "It's already dead, Yu."

    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    "We quickly explained everything—how Chung-hee had sensed something was off, how he struck down the imposter, and how the yaoguai had been disguising itself as Yuxuan all along. As we spoke, Yuxuan's face shifted from horror to a mixture of understanding and lingering unease."

    yuxuan "Oh my… Did that really happen? How did you found out that the person wasn't really me?"

    hide yuxuan
    show chunghee normal_sad at right_char with Dissolve(0.2)
    "Chung-hee exhaled slowly, his gaze still locked onto the lifeless form of the yaoguai. His expression was unreadable—stoic, yet touched with something heavier."

    chung_hee "I dug deep into its mind. I found out too late."
    chung_hee "I don't do this. I don't invade minds unless absolutely necessary. It's a violation of trust, of privacy… But this thing was dangerous. It was deceiving us."
    chung_hee "I swear on my honor—I will never turn my abilities against any of you unless it is a matter of life and death. That is my promise."

    hide chunghee normal_sad
    "The weight of his words settled over us. I nodded, accepting his vow."

    show svante alt_funny at right_char with Dissolve(0.2)
    svante "I trust you, sir Chung. After saving and not killing me, I technically owe you my life still. *nervous chuckle*"

    hide svante
    show niko normal_base at right_char with Dissolve(0.2)
    niko "That works. You don't seem to be the type that breaks his promises."

    hide niko
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "Well… oh, goodness! Well, it's a damn good thing Roboto woke me up."

    show roboto happy at right_robot with Dissolve(0.2)
    roboto "N-N-N-No worries, Master Yuxuan! Y-Y-Y-You can always count on Robotoooo~~"

    "It beeped and blinked its lights proudly."

    roboto "I w-w-w-was worried, so I hurried to wake Master Yuxuan up. I had help from Miss Tedda as well."
    roboto "Miss Tedda helped me w-w-w-wake Master Yuxuan up while I monitored the tunnels for further threats."

    "Then Roboto turned to the yaoguai's still form, its glowing optics flickering as it processed the situation. It tilted its head slightly, then spoke with a tone of programmed enthusiasm."

    show roboto fin at right_robot
    roboto "I shall take care of this! P-p-proper disposal protocols will be followed!"

    # play sound sfx_roboto_beep               # PLACEHOLDER — not declared

    hide roboto
    show niko normal_base at right_char with Dissolve(0.2)
    "With a series of quick, mechanical movements, Roboto extended a set of slender, metallic arms. It latched onto the corpse, adjusting its grip before effortlessly hoisting the body upward. The weight didn't seem to strain it in the slightest."

    niko "Strong fella… who knew?"

    show roboto happy at right_robot with Dissolve(0.2)
    roboto "Now, now. Off to proper containment and disposal you go~"

    "The lifeless form dangled in its grasp as Roboto turned toward the tunnels. Just before departing, it spun back around and blinked at us cheerfully."

    roboto "S-S-See you at the lab, sirs!"

    hide roboto
    show svante normal_happy at right_char with Dissolve(0.2)
    svante "See you, Roboto!"

    hide svante
    roboto "Robotooooo~"

    "A collective breath seemed to escape from all of us."
    "Finally, we turned to face the door once more. Its intricate carvings gleamed under the dim tunnel lights, the Prosperity Dragon's gaze seeming to watch us in quiet expectation."

    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "Chung-hee studied it for a moment, then spoke."

    chung_hee "Maybe… what the fake Yuxuan said was true."

    hide chunghee normal_neutral
    show niko normal_serious at right_char with Dissolve(0.2)
    niko "Even if it was lying about who it was, it might not have been lying about the door itself."

    hide niko
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "From what the lot of you were saying, yes. Those are merely theories though."

    hide yuxuan
    show svante normal_neutral at right_char with Dissolve(0.2)
    svante "It won't hurt to try, right? If this thing really does require the amulets and draconic fire to open, then…"

    hide svante
    show dorian serious at left_char
    "I tightened my grip around the amulet in my palm."

    dorian "I'm the only one who can open it."

    hide dorian
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "Without a word, he reached into the folds of his coat and pulled out his amulet. The dim tunnel light caught the edges of the amulet as he extended it toward me."
    "I looked at him, searching his expression. There was no hesitation, no doubt."

    chung_hee "If anyone can open it, it's you."

    show dorian neutral at left_char with Dissolve(0.2)
    "I took the amulet from his palm, feeling the cool weight of it settle into my hand alongside my own. A strange sensation passed through me—like an old whisper, a buried echo of something ancient stirring just beneath my skin."
    "I turned toward the towering door, exhaling slowly."

    dorian "Alright… I know I need to channel draconic fire to break the seal, but what do I do with the amulets? Hold them up? Place them on the door?"

    "I glanced at Yuxuan, hoping for some guidance."
    "He stared back at me."
    "Then blinked."
    "Then slowly folded his arms."

    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "…Did the winged man tell you what to do?"

    show dorian serious at left_char
    dorian "What?! Are you saying you don't know?"

    show yuxuan normal_neutral at right_char
    yuxuan "Buddy, you think I've done this before? I told you, I've spent years studying this door, not opening it."

    show dorian neutral at left_char
    "I groaned, rolling my shoulders."

    dorian "Great. So what now?"

    hide yuxuan
    show svante normal_neutral at right_char with Dissolve(0.2)
    svante "Maybe we can just… you know, guess. How hard could it be? It's just a pose right?"

    hide svante
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "I hardly think dramatic poses are necessary. We possess the amulets—surely that alone should be enough. Must we resort to theatrics?"

    hide chunghee normal_neutral
    show niko normal_serious at right_char with Dissolve(0.2)
    niko "Think about it. Posture holds great significance in religious ceremonies, does it not? If this door is bound to something ancient—something sacred—then the way we present ourselves may matter more than we think."

    "He let his fingers trail over the carved ridges of the dragon's body, his tone growing contemplative."

    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "I… highly doubt that."

    hide chunghee normal_neutral
    show niko normal_meditate at right_char with Dissolve(0.2)
    "Niko took a step forward, holding out his hands with the amulets, palms facing upward, as if offering them to an unseen deity."

    niko "Like this. This is how priests kneel before an altar, or how supplicants raise their hands in prayer. If this is a ritual, then our stance should reflect reverence—humility befitting an item of such significance."
    niko "Humility. Reflection. Devotion."

    hide niko
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "Isn't that a little excessive?"

    hide chunghee normal_neutral
    show dorian neutral at left_char
    dorian "Chung's right, Niko. Any other ideas?"

    hide dorian
    show svante alt_base at right_char with Dissolve(0.2)
    "Svante spread his arms dramatically, mimicking a grand gesture of divine invocation."

    svante "Or—and hear me out—you point them at the door like twin weapons. Like—'BEHOLD MY POWER!'—and then blast the fire!"
    svante "Like this, Sir Dorian!"

    hide svante
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "Not you too, Svante."

    hide chunghee normal_neutral
    show yuxuan alt_think at right_char with Dissolve(0.2)
    yuxuan "Please. If we're going by theatrical inspiration, we should follow The Trials of the Silver Dragon."

    hide yuxuan
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "Chung-hee raised an eyebrow, his expression one of mild curiosity."

    chung_hee "The Trials of the Silver Dragon? I am unfamiliar with this Silver Dragon you speak of. Is this a deity of some significance?"

    hide chunghee normal_neutral
    show yuxuan normal_happy at right_char with Dissolve(0.2)
    yuxuan "It's an audio drama I listen to every morning! The protagonist stands before the sacred gate, arms crossed over his chest, an amulet in each hand, and recites a sacred vow before unleashing his divine energy."

    hide yuxuan
    show svante normal_happy at right_char with Dissolve(0.2)
    svante "You're into audio dramas too, sir Yuxuan?! My mom used to star in one! It's called—"

    hide svante
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "Chung-hee let out a long, suffering sigh, pinching the bridge of his nose as if physically pained by the discussion."

    chung_hee "Or perhaps you simply place the amulets against the door, instead of engaging in wildly unnecessary pageantry."

    show dorian neutral at left_char with Dissolve(0.2)
    "I stared at them all."

    dorian "…These are my options?"

    hide chunghee normal_neutral
    show niko normal_base at right_char with Dissolve(0.2)
    show svante normal_happy at right_char with Dissolve(0.2)
    hide niko
    show yuxuan normal_happy at right_char with Dissolve(0.2)
    hide svante
    hide yuxuan
    "Niko looked proud, Svante gave me an encouraging thumbs-up, Yuxuan was practically vibrating with excitement over his audio drama fantasy, and Chung-hee… looked utterly done with this conversation."
    "They all looked far too pleased with themselves."
    "Still, I couldn't ignore that there was a logic to what they were saying. Rituals, reverence, power—whatever the answer was, it had to be something intentional."
    "I exhaled sharply, gripping the amulets tighter."

    jump ch8_open_door


# =============================================================================
# SECTION 8: LABEL CH8_OPEN_DOOR — Opening the Door (4 Choices)
# =============================================================================

label ch8_open_door:

    menu:

        "Go with Niko's suggestion.":
            $ ch8_d1_choice = "niko"
            $ niko_affection += 1

            show dorian neutral at left_char
            "I took a deep breath and followed Niko's suggestion, raising the amulets with both hands, palms facing upward as if offering them to something divine. Niko stood close, his voice calm yet commanding."

            show niko normal_meditate at right_char with Dissolve(0.2)
            niko "That's it. Hold them up as an offering."
            niko "Feel the faith. Show humility. Devotion. Sincerity. Let go of all doubt."

            hide niko
            show chunghee normal_neutral at right_char with Dissolve(0.2)
            chung_hee "You've chosen Niko's suggestion. A noble choice… I think. Let us see if the door deems it worthy."

            hide chunghee normal_neutral
            show svante normal_neutral at right_char with Dissolve(0.2)
            svante "Well, I suppose that makes some sense. Old temples and rituals usually had some kind of pose, right?"

            hide svante
            show chunghee normal_neutral at right_char with Dissolve(0.2)
            chung_hee "Agreed. There is wisdom in tradition. Even if one does not fully grasp the meaning, the act itself can hold power."

            hide chunghee normal_neutral
            show niko normal_serious at right_char with Dissolve(0.2)
            niko "Faith is power, Sir Chung. If you dismiss it, you dismiss what has moved entire civilizations, what has turned the tides of history."

            hide niko
            jump ch8_open_door_common

        "Go with Svante's suggestion.":
            $ ch8_d1_choice = "svante"
            $ svante_affection += 1

            show dorian serious at left_char
            "I took a steadying breath, deciding to follow Svante's advice. If nothing else, it had flair. I guess."
            "Squaring my stance, I tightened my grip around the amulets, their cool metal warming under my touch."
            "A familiar heat coiled in my chest, waiting to be unleashed."

            show svante alt_base at right_char with Dissolve(0.2)
            svante "Like twin weapons, sir! Point them toward the door—let them know who's in charge!"

            hide svante
            show dorian dragon_eyes at left_char
            "I exhaled sharply, raising both amulets before me like blades poised for battle. Energy crackled along my fingertips, sparks of draconic fire licking at the edges of my vision. The chamber seemed to hold its breath."

            dorian "BEHOLD MY POWER!"

            "The amulets flared to life, light exploding from their surfaces in a blinding display."

            show svante alt_funny at right_char with Dissolve(0.2)
            show yuxuan normal_happy at right_char with Dissolve(0.2)
            hide svante
            "Svante & Yuxuan: PRAISE BE TO THE SILVER DRAGON!"

            hide yuxuan
            show niko normal_ignore at right_char with Dissolve(0.2)
            niko "…"

            hide niko
            show chunghee normal_neutral at right_char with Dissolve(0.2)
            chung_hee "... Silver Dragon? I assume this pertains to the fictional audio drama Sir Yuxuan insists on referencing?"

            hide chunghee normal_neutral
            show niko normal_ignore at right_char with Dissolve(0.2)
            niko "Merciful Enoch, grant me patience for I'm running out of it."

            hide niko
            show svante alt_base at right_char with Dissolve(0.2)
            svante "Now, sir Dorian—channel the draconic fire! Show the door your might!"

            hide svante
            jump ch8_open_door_common

        "Go with Yuxuan's suggestion.":
            $ ch8_d1_choice = "yuxuan"
            $ yuxuan_affection += 1

            show dorian neutral at left_char
            "After a moment of indecision, I sighed and turned to Yuxuan."

            dorian "Alright, Yuxuan, what was that ridiculous thing you mentioned?"

            show yuxuan normal_happy at right_char with Dissolve(0.2)
            "His face lit up with delight, as if he had been waiting for this moment his entire life."

            yuxuan "Ah, an excellent choice! There's this one scene from 'The Silver Dragon Chronicles'—Episode 37, mind you—"

            "He went into full detail. I didn't understand anything."

            hide yuxuan
            show svante normal_happy at right_char with Dissolve(0.2)
            svante "Sir Yuxuan! That's correct!"

            hide svante
            show niko normal_ignore at right_char with Dissolve(0.2)
            niko "...Do you actually listen to these programs or do they just manifest in your mind?"

            hide niko
            show dorian dragon_eyes at left_char
            "Fine. I took a deep breath. struck a dramatic stance, raising my arms high. I made sure to follow what he said."

            dorian "BY THE WILL OF THE ANCIENT FLAME, I STAND AT THE PRECIPICE OF DESTINY! … Like that?"

            show yuxuan normal_happy at right_char with Dissolve(0.2)
            yuxuan "I love it! The INTENSITY! The EMOTION! Oh, the drama! It's perfect!"

            hide yuxuan
            show svante normal_happy at right_char with Dissolve(0.2)
            svante "Beautiful. Absolutely beautiful, sir Dorian. I felt moved! Bravo! Bravo!"

            hide svante
            show chunghee normal_neutral at right_char with Dissolve(0.2)
            chung_hee "…"

            hide chunghee normal_neutral
            show niko normal_ignore at right_char with Dissolve(0.2)
            niko "…Merciful Enoch, please grant me patience for I'm running out of it."

            hide niko
            jump ch8_open_door_common

        "Go with Chung-hee's suggestion.":
            $ ch8_d1_choice = "chunghee"
            $ chunghee_affection += 1

            show dorian neutral at left_char
            "I exhaled slowly, pressing my fingers against my temple before turning to Chung-hee."
            "For once, I'm going to listen to the most reasonable person in the room."

            dorian "Chung, what was your idea?"

            show chunghee normal_neutral at right_char with Dissolve(0.2)
            "Chung-hee regarded me with a measured gaze, his expression calm and unwavering."

            chung_hee "The amulets are keys—therefore, they must be used as such. Align them with the engravings and let the door recognize its rightful seal."

            hide chunghee normal_neutral
            show niko normal_base at right_char with Dissolve(0.2)
            niko "Sometimes the simple answer is the right one."

            hide niko
            show svante normal_neutral at right_char with Dissolve(0.2)
            svante "I suppose it does make the most sense… probably."

            hide svante
            show yuxuan normal_sad at right_char with Dissolve(0.2)
            yuxuan "No battle cry? No flair? That's sad."

            hide yuxuan
            show dorian neutral at left_char
            "I sighed, stepping forward until I was close enough to the door to see the fine details of its carvings."
            "Taking a breath, I pressed both amulets against the engravings, aligning them with the shapes etched into the stone."
            "A deep, resonant click echoed through the chamber."

            # play sound sfx_door_unlock       # PLACEHOLDER

            show svante normal_happy at right_char with Dissolve(0.2)
            svante "Oh! Did you hear that, Your sir Chung? It might have worked!"

            hide svante
            show chunghee normal_neutral at right_char with Dissolve(0.2)
            chung_hee "Svante, I remind you—such sounds do not reach me for I am not of hearing. Please tell me what the sound was."

            hide chunghee normal_neutral
            show svante normal_nervous at right_char with Dissolve(0.2)
            svante "Right. Of course. My apologies, sir Chung."

            hide svante
            show niko normal_base at right_char with Dissolve(0.2)
            niko "It was a click, Chung. Like the unlocking of a mechanism or something."

            hide niko
            jump ch8_open_door_common


label ch8_open_door_common:

    show dorian dragon_eyes at left_char with Dissolve(0.2)
    "The air around me thickened, charged with something unseen. The amulets pulsed against my skin, and a warmth coiled in my core—draconic fire."
    "I held firm. I did not break my stance."
    "Then, with a low, grinding groan, the door began to shift. Dust and debris rained down as the massive stone slab trembled and heaved. The very ground beneath us shuddered, and the deep, echoing sound of stone scraping against stone filled the air."
    "A gust of air rushed out from the darkness beyond, stale and putrid. It carried the suffocating weight of decay, dampness, and something acrid—like burnt metal and old, rotting blood."
    "The door fully parted, revealing a cavernous space beyond."

    jump ch8_inside_door


# =============================================================================
# SECTION 9: LABEL CH8_INSIDE_DOOR — Inside the Sealed Chamber / Bridge
# =============================================================================

label ch8_inside_door:

    scene bg_inside_sealed_door with fade       # PLACEHOLDER — sealed chamber interior
    stop music fadeout 1.0
    play music ost_ch8_chamber fadein 2.0       # PLACEHOLDER — eerie vast chamber theme
    play audio amb_cavern_deep loop fadein 1.0  # PLACEHOLDER — deep cavern ambient

    hide dorian
    "The space beyond was vast, stretching beyond the reach of our light. The ceiling vanished into darkness, unseen, while a sheer, bottomless chasm yawned around the perimeter. The only solid footing was a narrow stone bridge, a precarious path leading to a massive circular platform at the center of the abyss."

    show dorian neutral at left_char with Dissolve(0.2)
    "I turned to Yuxuan, my voice laced with disbelief."

    dorian "Yu, do you mean to tell me you studied this door for years and never once suspected what was inside of it?"

    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    "Yuxuan held up both hands in defense, his eyes wide."

    yuxuan "I swear to you, I had no idea! We tried everything—earth channeling, brute force—but we could never break the seal. We assumed it was an empty chamber, or that it had collapsed long ago!"

    hide yuxuan
    show dorian neutral at left_char
    "With caution, we stepped forward, each footfall echoing across the vast emptiness."

    show niko normal_serious at right_char with Dissolve(0.2)
    niko "Careful, everyone."

    hide niko
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "Watch your footing. The bridge is old."

    hide chunghee normal_neutral
    "The bridge rocked."

    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "How deep is the pit?"

    hide svante
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "Prosperity Dragon bless me! That is one deep pit!"

    hide yuxuan
    "On the central platform, the remnants of something long-forgotten lay strewn about."
    "Broken tables, their once-sturdy legs snapped and rotting, were overturned in disarray. Glass apparatus, cracked and shattered, glinted faintly under the dim glow of embedded crystals pulsing weakly along the cavern walls."
    "Strange tools lay abandoned—rusted clamps, peculiar metal rods, and parchment so aged that it disintegrated at the slightest touch."
    "There were corpses littered in the central area. Niko crouched near one of the fallen figures, eyes narrowing as he examined the remains."

    show niko normal_serious at right_char with Dissolve(0.2)
    niko "Odd. The decomposition suggests varying timelines. Some of these bodies have been here for centuries, reduced to skeletal remains. Others… are far more recent. Mummified, desiccated, yet eerily preserved by the cold, dry air."
    niko "It reminds me of the time I went to a remote village in the Hinami kingdom. The way corpses were left untouched after the famine, preserved not by time's mercy but by sheer desolation."

    hide niko
    show svante normal_nervous at right_char with Dissolve(0.2)
    "Svante swallowed hard, his face paling."

    svante "I-I think I'm going to be sick… *barfs*"

    hide svante
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "C-Can I go back? Oh Prosperity Dragon… *barfs* *barfs*"

    hide yuxuan
    show dorian neutral at left_char
    dorian "Calm down, Yu."

    hide dorian
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "Chung-hee wrinkled his nose in distaste, his voice as poised as ever despite the ghastly scene before us."

    chung_hee "This stench is vile. A cloying, putrescent rot. Something terrible had happened here. And whatever it was… it had not been swift. Nor had it been merciful."

    hide chunghee normal_neutral
    "We moved cautiously, our footsteps echoing in the vast, forsaken chamber. Dust and debris covered the floor, mingling with shards of broken glass and rusted metal tools."

    show svante normal_neutral at right_char with Dissolve(0.2)
    svante "Merciful Enoch…"

    "We turned toward him and saw what had caught his attention."
    "A corpse lay sprawled across the floor, half-buried under fallen debris. Unlike the other remains, this one was in the process of decomposition. Its flesh had darkened and sagged, splitting in places where decay had eaten away at the muscle. The stench was nearly unbearable."

    hide svante
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "Chung-hee stepped forward, his sharp gaze scanning the corpse with unnerving precision. His expression remained unreadable, but there was something distant in his eyes."

    chung_hee "That uniform… It is standard Kyeongjang military wear."

    show dorian neutral at left_char with Dissolve(0.2)
    dorian "A Kyeongjang soldier? Here?"

    show chunghee normal_sad at right_char with Dissolve(0.2)
    "Chung-hee's eyes traced the insignia still faintly visible beneath layers of dust and decay. His lips pressed into a firm line."

    chung_hee "No doubt about it. This is not just any soldier—this insignia belongs to the royal guard."

    hide chunghee normal_sad
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "The royal guard… You mean… they served the Emperor?"

    hide yuxuan
    show chunghee normal_sad at right_char with Dissolve(0.2)
    chung_hee "Yes. My father's soldiers."

    hide chunghee normal_sad
    show niko normal_serious at right_char with Dissolve(0.2)
    niko "Judging by the decomposition, he's been here for at least four to five years. The cold air likely slowed the process, keeping him more preserved than he otherwise would be."

    hide niko
    show dorian neutral at left_char
    "I saw something flicker in Chung-hee's expression—something almost unreadable. Disbelief? Concern?"
    "His gaze fell to the corpse's hands, which were stiff with rigor mortis. One was curled tightly around something."
    "Carefully, I stepped closer, mindful not to disturb the fragile remains. My eyes narrowed as I caught a group of glimmering parchment, aged and brittle, yet miraculously intact, clutched between the soldier's fingers."

    show svante normal_neutral at right_char with Dissolve(0.2)
    svante "A letter. Should we read it?"

    hide svante
    jump ch8_corpse


# =============================================================================
# SECTION 10: LABEL CH8_CORPSE — Read or Not Read the Letter
# =============================================================================

label ch8_corpse:

    menu:

        "Read the note.":
            $ ch8_read_letter = True

            show dorian neutral at left_char
            "I reached out carefully, peeling the parchments from the cadaver's grip. As I did, the stiffened arm shifted slightly, causing the torso to slump. The movement dislodged something from beneath the folds of decayed fabric."
            "The parchments were not neatly stacked. They were haphazardly pressed together, their edges frayed and uneven. Some pieces were torn, others stained with something dark and long-dried."
            "Ink had faded, but the words remained—scrawled in uneven strokes, as if written with trembling hands."
            "A testament."

            show svante normal_nervous at right_char with Dissolve(0.2)
            svante "W-What does it say, sir?"

            hide svante
            show dorian neutral at left_char
            "I took a steady breath. The moment my fingers brushed the parchment, a pulse of light flickered across its surface. The letters glowed. A low hum filled the air, like a whisper too faint to grasp—until it wasn't."
            "The words did not stay confined to the pages."

            # play sound sfx_painting_glow     # PLACEHOLDER

            # hwan_sik — voice only, no sprite declared
            hwan_sik "Baek Hwan-sik, Kyeongjang Protector of Emperor Lord Hyon Min-joon"

            "They echoed in our minds."

            show niko normal_serious at right_char with Dissolve(0.2)
            niko "Are all of you hearing this?"

            hide niko
            show chunghee normal_sad at right_char with Dissolve(0.2)
            "A voice—hoarse, weak, filled with exhaustion and regret."

            chung_hee "A mind note. Whoever wrote this… they channeled their very thoughts onto the parchment."

            hide chunghee normal_sad
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

            show dorian sad at left_char with Dissolve(0.2)
            "I exhaled slowly, feeling the weight of the words settle deep in my chest. My fingers tightened around the parchments, the paper crackling slightly in my grip."

            show yuxuan normal_sad at right_char with Dissolve(0.2)
            yuxuan "By the Prosperity Dragon…"

            hide yuxuan
            show dorian sad at left_char
            dorian "He knew he wasn't going to make it."

            hide dorian
            show svante normal_sad at right_char with Dissolve(0.2)
            svante "He… He wanted to be remembered."

            hide svante
            show chunghee normal_sad at right_char with Dissolve(0.2)
            "Chung-hee clasped his hands together, as if in prayer."

            chung_hee "And so he shall be. Soldier Baek Hwan-sik, Protector of the Emperor Lord…"
            chung_hee "Your Emperor Lord thanks you. May Xianlun's gates open wide for you, and may you walk among the honored dead of Kyeongjang."

            hide chunghee normal_sad
            show niko normal_serious at right_char with Dissolve(0.2)
            niko "But why? Why bring the Emperor of Kyeongjang here? What purpose could this place have served?"

            hide niko
            show chunghee normal_neutral at right_char with Dissolve(0.2)
            chung_hee "We will uncover the truth. And we will not leave this place until we do."

            hide chunghee normal_neutral
            jump ch8_letter_common

        "Don't read the note.":
            $ ch8_read_letter = False

            show dorian neutral at left_char
            "I hesitated. Something about that parchment felt wrong. The sight of the soldier's decaying hand, locked in an eternal grip, sent a chill through me."

            dorian "I don't want to touch that."

            hide dorian
            show chunghee normal_sad at right_char with Dissolve(0.2)
            "Chung-hee exhaled slowly, his gaze flicking to me before returning to the corpse."

            chung_hee "Then I shall take it."
            chung_hee "This man once swore fealty to the Imperial House of Kyeongjang. Even in death, he remains my subject. It is my obligation to bear witness to his final message."

            "With a careful hand, he pried the brittle parchment from the soldier's grasp. As he did, the stiffened arm shifted slightly, the dried sinew cracking under the pressure."

            hide chunghee normal_sad
            jump ch8_letter_common


# =============================================================================
# SECTION 11: LABEL CH8_LETTER_COMMON — Button / Six Paintings Puzzle Setup
# =============================================================================

label ch8_letter_common:

    stop music fadeout 1.5
    play music ost_ch8_chamber fadein 1.5

    show dorian neutral at left_char with Dissolve(0.2)
    "A small object clattered against the stone floor, the faint sound echoing in the silence. Instinctively, I reached down and picked it up, brushing away the dust."

    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "What's that?"

    hide yuxuan
    show dorian neutral at left_char
    "At first glance, it appeared to be just a button—small, round, unassuming. But as the dim light of the cavern illuminated its surface, I realized it was anything but ordinary."
    "The button was exquisitely crafted, its golden frame polished to a mirror sheen despite the years of dust and decay surrounding it. Ornate filigree swirled around its edges, delicate patterns curling like vines embracing the central design."
    "Embedded within the metal was a miniature portrait, impossibly detailed. Even in the flickering glow, I could make out the fine brushstrokes—an artist's delicate hand immortalizing a man's face. But a crack marred the surface, obscuring his features."

    show svante normal_happy at right_char with Dissolve(0.2)
    svante "That's a beautiful button… It's so well made. Just like the door earlier."

    hide svante
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    "Yuxuan leaned in, frowning."

    yuxuan "Even for someone like me—who appreciates a fair bit of extravagance—this seems excessive. No one puts this much care into a simple button."

    hide yuxuan
    show svante normal_neutral at right_char with Dissolve(0.2)
    svante "Or… maybe it's more than that! Maybe it's a piece of something greater."
    svante "Too bad we can't see his face, though."

    hide svante
    show niko normal_base at right_char with Dissolve(0.2)
    niko "Let's press it and see what happens."

    hide niko
    show dorian neutral at left_char
    "I hesitated for only a breath, then pressed the button."

    # play sound sfx_painting_glow             # PLACEHOLDER

    hide dorian
    "A whisper curled through the air, a voice neither harsh nor gentle—something ancient, something knowing. It slithered around my mind like a serpent, threading through my thoughts with a tone both amused and expectant."

    # spirit — voice only, no sprite declared
    spirit "If you seek the truth, lay your hand upon the echoes of devotion."

    "Before me, six paintings shimmered into existence, suspended in the darkness like windows to another time. Each one pulsed with an eerie, otherworldly glow—soft but insistent, waiting. Expecting."

    spirit "Touch them all, and only then shall my greatest treasure be revealed."

    "A heavy silence settled over us."

    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "T-Touch them? Are you sure? All the paintings look beautiful!"

    "His voice cracked slightly, gaze darting between the glowing paintings and me."

    hide svante
    show yuxuan normal_happy at right_char with Dissolve(0.2)
    yuxuan "Oh my! These are all exquisite! Can't we all just take them? I'm sure they'd be a wonderful addition to my collection and—"

    hide yuxuan
    show dorian neutral at left_char with Dissolve(0.2)
    dorian "I don't think that's a good idea, Yu."

    hide dorian
    show niko normal_serious at right_char with Dissolve(0.2)
    niko "It would be foolish to rush in blindly. We have no idea what these represent—or what consequences touching them might bring."

    show dorian neutral at left_char with Dissolve(0.2)
    dorian "It's obviously a trial of some sort. If they wanted us to just tap all six and be done with it, they wouldn't have gone through the trouble of making them appear like this."

    hide niko
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "Agreed. We must proceed with caution. Each one of these may hold a key to understanding what lies ahead."

    hide chunghee normal_neutral
    show dorian neutral at left_char
    "I stepped closer, studying the nearest painting. The light within it flickered, almost as if it were breathing."

    dorian "We should examine them first—one by one. There's no telling what will happen if we touch them all at once."

    hide dorian
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "R-Right. No reckless touching."

    hide svante
    "I turned my attention to the first painting."

    jump ch8_paintings


# =============================================================================
# SECTION 12: LABEL CH8_PAINTINGS — Six Paintings Examination
# =============================================================================

label ch8_paintings:

    $ ch8_puzzle_seen = True

    play music ost_ch8_paintings fadein 1.5     # PLACEHOLDER — mystical paintings theme

    # --- Painting 1 ---
    scene cg_painting_1 with dissolve           # PLACEHOLDER — The Loom's Whisper
    pause 1.0

    "PUZZLE"
    "The Loom's Whisper:"
    "A celestial void, vast and endless, swirls with cosmic threads of silver and gold. Radiant hands sculpt the form of a woman, her body emerging from celestial mist."
    "Her body is half-formed, her eyes closed in peaceful slumber, as if she has yet to awaken to the world."

    yuxuan    "The title of this painting is… The Loom's Whisper…"
    niko      "Remarkable. The art style is exquisite."
    svante    "It's kind of eerie, isn't it?"
    chung_hee "Sculpted not just by hands, but by will. By fate. By the Weaver."

    # --- Painting 2 ---
    scene cg_painting_2 with dissolve           # PLACEHOLDER — Chains of Choice
    pause 1.0

    "Chains of Choice:"
    "A radiant figure of a woman steps down from a celestial throne, reaching for the hand of a man bathed in soft candlelight."
    "Their fingers intertwine, golden chains barely visible around the divine's wrists, as if binding them to something they are trying to leave behind."
    "In the background, unseen figures watch in silence, their expressions unreadable."

    niko "Galean symbology. Golden chains mean devotion. A vow. A promise you can't break. You were a citizen of Gale, Dorian. Is that true?"

    dorian "Yes. Elara and I were bound in golden chains when we were wed."

    niko "I see. I apologize for bringing that up."

    dorian "No need. The wedding was a fond memory… save for the catering. Elara said it was a disaster."

    # --- Painting 3 ---
    scene cg_painting_3 with dissolve           # PLACEHOLDER — Thrones of the Eternal
    pause 1.0

    "Thrones of the Eternal:"
    "Four celestial beings sit upon towering thrones, their forms bathed in an ethereal glow. Time itself seems frozen in reverence, their robes shifting like flowing water despite the stillness. Above them, a golden sun watches, its unblinking gaze heavy with judgment."
    "One throne, covered in flowers, bore the sweet smile of the radiant woman."

    yuxuan "Hmm… her throne is different. Softer. As if she ruled with something the others did not."
    niko   "Flowers and smiles don't rule eternity. They decay. Enoch's throne is carved from obsidian and silence. Cold, clear. Eternal like death itself. That's power."
    yuxuan "\"tHat's pOwEr\"… Hmph!"
    niko   "Are you a child?"

    # --- Painting 4 ---
    scene cg_painting_4 with dissolve           # PLACEHOLDER — Wrath
    pause 1.0

    "Wrath:"
    "A radiant figure of a woman sits upon a burning throne, fingers digging into the armrests as fire consumes the sky behind them. Her eyes burn with unrelenting fury, golden banners slashed and torn at their feet."
    "The last remnants of kindness stain her cheek—a single tear, gleaming in the firelight."

    chung_hee "Wrath. Pure and simple wrath."
    yuxuan    "The deadliest emotion."

    # --- Painting 5 ---
    scene cg_painting_5 with dissolve           # PLACEHOLDER — Tragedy
    pause 1.0

    "Tragedy:"
    "A winged man looms over a battlefield, clutching the severed head of a fallen man. A radiant figure of a woman kneels in the distance, hands trembling, golden tears slipping down their cheeks. The heavens above are split open with storm clouds, the divine light struggling against the encroaching darkness."

    svante "Oh no… That's heartbreaking."
    niko   "Lord Enoch…"
    dorian "What?"
    niko   "That's him. Lord Enoch. The wings. The markings. The way he holds the severed head like a trophy."
    niko   "Why is he here? Why does he appear in these paintings?"

    # --- Painting 6 ---
    scene cg_painting_6 with dissolve           # PLACEHOLDER — When the Stars Watched
    pause 1.0

    "When the Stars Watched:"
    "A bard plays his lute beneath a sky dusted with stars, unaware of the radiant figure of a woman watching him from the garden's edge."
    "Their eyes meet across a reflecting pool, the rippling water caught between two fates. The air hums with something unspoken—something fragile, dangerous, and inevitable."

    svante    "Ahh, a romance! This is the moment where everything changes, isn't it?"
    yuxuan    "*sighs* He must have been very beautiful…"
    chung_hee "Stars do not interfere with the lives of men. They only watch."

    scene bg_inside_sealed_door with dissolve

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

label ch8_painting_order:

    spirit "You will touch each fragment with your own hands."

    show dorian neutral at left_char with Dissolve(0.2)
    "I swallowed and looked at my companions, their expressions reflecting the same uncertainty I felt. The paintings loomed before us, waiting."

    dorian "So… which one do we touch first?"

    menu:

        "The Loom's Whisper, Chains of Choice, Thrones of the Eternal, Tragedy, When the Stars Watched, Wrath":

            hide dorian
            "The moment our hands made contact with the final painting, a tremor coursed through the chamber. The air turned thick—almost suffocating—as the spirit's presence swelled, then cracked like fragile glass."
            "A mournful sigh echoed from the unseen depths, the sorrow in it raw and unbearable."

            spirit "No… That is not how it was… That is not how it should be…"

            show yuxuan normal_neutral at right_char with Dissolve(0.2)
            yuxuan "What?! We were wrong?"

            spirit "I wanted you to see… to understand… but you do not see."

            hide yuxuan
            show svante normal_sad at right_char with Dissolve(0.2)
            svante "Unfortunate… Maybe we can try again, sir Dorian."

            hide svante
            show niko normal_serious at right_char with Dissolve(0.2)
            niko "Perhaps the paintings show a story. Let's be sure to pay attention."

            hide niko
            jump ch8_paintings

        "The Loom's Whisper, Thrones of the Eternal, When the Stars Watched, Chains of Choice, Tragedy, Wrath":

            hide dorian
            "As the final painting was touched, the chamber came alive. A golden glow spread from the images, weaving threads of light through the air like strands of fate itself. The very walls pulsed, as if breathing in unison with something ancient."

            spirit "Yes… yes, you see it now."

            "A warmth blossomed in my chest. The paintings shimmered, their colors deepening, details sharpening as if the story they told had never been clearer. The air hummed with power, heavy yet comforting."

            spirit "And so… Here is my greatest treasure."

            show chunghee normal_happy at right_char with Dissolve(0.2)
            chung_hee "Finally. Great job, Dorian."

            hide chunghee normal_happy
            jump ch8_painting_correct

        "Thrones of the Eternal, The Loom's Whisper, Tragedy, When the Stars Watched, Chains of Choice, Wrath":

            hide dorian
            "The moment our hands made contact with the final painting, a tremor coursed through the chamber. The air turned thick—almost suffocating—as the spirit's presence swelled, then cracked like fragile glass."
            "A mournful sigh echoed from the unseen depths, the sorrow in it raw and unbearable."

            spirit "No… That is not how it was… That is not how it should be…"

            show yuxuan normal_neutral at right_char with Dissolve(0.2)
            yuxuan "What?! We were wrong?"

            spirit "I wanted you to see… to understand… but you do not see."

            hide yuxuan
            show svante normal_sad at right_char with Dissolve(0.2)
            svante "Unfortunate… Maybe we can try again, sir Dorian."

            hide svante
            show niko normal_serious at right_char with Dissolve(0.2)
            niko "Perhaps the paintings show a story. Let's be sure to pay attention."

            hide niko
            jump ch8_paintings

        "Thrones of the Eternal, When the Stars Watched, Chains of Choice, The Loom's Whisper, Wrath, Tragedy":

            hide dorian
            "The moment our hands made contact with the final painting, a tremor coursed through the chamber. The air turned thick—almost suffocating—as the spirit's presence swelled, then cracked like fragile glass."
            "A mournful sigh echoed from the unseen depths, the sorrow in it raw and unbearable."

            spirit "No… That is not how it was… That is not how it should be…"

            show yuxuan normal_neutral at right_char with Dissolve(0.2)
            yuxuan "What?! We were wrong?"

            spirit "I wanted you to see… to understand… but you do not see."

            hide yuxuan
            show svante normal_sad at right_char with Dissolve(0.2)
            svante "Unfortunate… Maybe we can try again, sir Dorian."

            hide svante
            show niko normal_serious at right_char with Dissolve(0.2)
            niko "Perhaps the paintings show a story. Let's be sure to pay attention."

            hide niko
            jump ch8_paintings


label ch8_painting_correct:

    # play sound sfx_door_unlock               # PLACEHOLDER

    "Threads of golden light wove through the air, swirling around us like strands of fate finally aligning. The glow seeped into the very walls, making the entire cavern pulse like a living thing."
    "The temperature dropped in an instant. My breath turned to mist, and an unnatural chill settled in my bones."
    "Then, from the very center of the platform, the stone cracked apart. A deafening groan filled the chamber as something massive emerged—a monolith of ice, clear as crystal, towering and flawless."
    "Inside it—a man. A winged man."

    jump ch8_magnus_found


# =============================================================================
# SECTION 14: LABEL CH8_MAGNUS_FOUND — Magnus in Ice / Freed / Awakens
# =============================================================================

label ch8_magnus_found:

    scene cg_magnus_ice with dissolve           # PLACEHOLDER — cg_magnus_ice
    pause 2.0
    scene bg_inside_sealed_door with dissolve

    show dorian neutral at left_char with Dissolve(0.2)
    "His form was perfectly preserved, encased in shimmering frost. Great, feathered wings curled around his body, their tips barely visible through the ice. His face, serene yet hauntingly familiar, stirred something deep within me."
    "My heart pounded. It was him. Magnus."
    "My hands trembled as I reached forward, drawn by something I could not name."

    dorian "Magnus!"

    hide dorian
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "Wait… Hold on- That's Magnus?!"

    hide yuxuan
    "Then, a voice—soft at first, but urgent—whispered into my mind."

    # magnus — voice in mind, no sprite yet
    magnus "You have found me, Dorian!"

    show dorian serious at left_char with Dissolve(0.2)
    "I staggered back. The voice wasn't just in my head—it was inside me, resonating through my very soul."

    magnus "Release me, Dorian! Please!!"

    "The plea sent a sharp, aching pang through my chest. This was no illusion. No mere fragment of the past."
    "He was here. He was alive."

    hide dorian
    show svante normal_nervous at right_char with Dissolve(0.2)
    "Svante took a shaky step back, his eyes wide with disbelief."

    svante "D-Did we just unearth a person? This is insane!"

    hide svante
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "Wait… is that him?! The winged man from the paintings?!"

    hide yuxuan
    show niko normal_serious at right_char with Dissolve(0.2)
    "Niko stepped forward, closer to the ice. His breath fogged the surface."

    niko "No, Yuxuan. The winged man from the paintings was Enoch."
    niko "Interesting… His body is perfectly intact. No decay, no deterioration. This isn't just preservation—this is suspension. He has not aged a single day since he was sealed."

    hide niko
    magnus "Dorian! Release me, please! Only you can release me from this prison I'm in!"

    show dorian serious at left_char with Dissolve(0.2)
    dorian "I can hear him. Inside my mind. He's calling my name, begging me to free him."

    hide dorian
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "I hope you know what you're doing, Dorian."

    hide chunghee normal_neutral
    show dorian dragon_eyes at left_char with Dissolve(0.2)
    "I swallowed hard, my pulse roaring in my ears."
    "I raised my hands, and the chamber trembled in response. Draconic fire ignited in my palms, gold and crimson, burning with an intensity that set the air ablaze. It crackled and roared, a storm of embers swirling around me, hungry, desperate to be unleashed."

    dorian "Everyone, get back!"

    show niko normal_serious at right_char with Dissolve(0.2)
    niko "Move back! Now! Unless you want to be reduced to ash!"

    hide niko
    hide dorian
    "The others obeyed, retreating to the edges of the platform as my flames surged higher. I stepped closer, my heartbeat syncing with the pulsing energy coursing through me. This was not just fire. This was will. This was power."
    "I thrust my hands forward, and the fire struck the ice."

    # play sound sfx_ice_shatter               # PLACEHOLDER

    "The ice hissed and cracked, steam curling into the air in thick, suffocating waves. The monolith that had imprisoned Magnus for centuries groaned under the heat, fractures spiderwebbing across its surface."

    spirit "What… WHAT HAVE YOU DONE?!"

    "Then, with a deafening shatter, the ice exploded."
    "Chunks of frozen crystal shot outward, skidding across the stone floor. A final burst of steam engulfed the chamber, obscuring everything in a thick, suffocating mist."

    show magnus normal at right_char with Dissolve(0.2)
    "Magnus collapsed forward, landing on his hands and knees, his breath ragged, his body trembling. His wings, massive and drenched in melting frost, unfurled in violent spasms, feathers scattering across the floor. Water pooled beneath him, cascading from his skin like he had been submerged in an abyss."

    magnus "*coughing*"

    hide magnus
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "He must be hurt!"

    hide svante
    show niko normal_serious at right_char with Dissolve(0.2)
    "Svante lurched forward, but Niko was already moving. He dropped to one knee beside Magnus, his fingers ghosting over the man's soaked skin before pressing against his throat to check his pulse. His brow furrowed, concern tightening his features."

    niko "Can you hear me? You're breathing too fast—try to slow it down."
    niko "You must have been trapped for a long time. Hypothermia, dehydration—who knows what else."

    hide niko
    show magnus normal at right_char with Dissolve(0.2)
    "His head hung low, silver hair plastered to his face. And then—"
    "His eyes snapped open."
    "They were white. Glowing, searing, burning with unearthly rage."
    "Then—his voice. A sound that carried the weight of a thousand storms."

    hide magnus
    scene cg_magnus_awakens with shock_cut      # PLACEHOLDER — cg_magnus_awakens
    pause 0.5
    scene bg_inside_sealed_door with dissolve

    show magnus alt_anger at right_char with Dissolve(0.2)
    magnus "YOU KILLED ADRIANA!"

    hide magnus
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "What?!"

    hide svante
    show niko normal_serious at right_char with Dissolve(0.2)
    niko "?!"

    hide niko
    show magnus alt_anger at right_char with Dissolve(0.2)
    "His words struck like a hammer, reverberating through the chamber. The walls shook. The abyss itself seemed to tremble beneath us."
    "Before I could speak, before any of us could even breathe—he moved."
    "Lightning-fast, Magnus lunged, his wings snapping open with the force of a hurricane. The ground cracked beneath his takeoff."
    "Magnus soared upward, his entire body wreathed in raw celestial power. Golden veins of energy crackled along his arms, surging through his fingers like barely-contained lightning."

    # play sound sfx_divine_pulse              # PLACEHOLDER

    magnus "MONSTERS! YOU'VE TORMENTED MY DREAMS FOR AN ETERNITY! I HAVE DROWNED IN YOUR LIES! BURNED IN YOUR DECEIT!"

    hide magnus
    show dorian serious at left_char with Dissolve(0.2)
    "I shuddered at the sight of him. The silhouette—his form, the eerie glow of his eyes—he looked just like…"
    "I swallowed hard. No. Not just like. It was the same as the death god in the Tragedy of Tianho."
    "A rush of memories crashed into me, merciless and overwhelming."
    "The castle of Tianho—reduced to rubble, its towering spires collapsing in plumes of smoke. The fires—raging, unstoppable, swallowing the city whole. The screams of the fallen, echoing endlessly."
    "Elara. My children. Paladin Cyrus."
    "For a moment, I stood frozen. The memory of the paintings, of Enoch looming over the battlefield, holding a severed head like a trophy—they overlapped. The past, the present. Reality twisted under the weight of it."
    "The chamber warped, the present fracturing under the weight of the past. My vision swam, flickering between now and then, between Magnus and the death god, between the living and the dead."

    show dorian angry at left_char
    dorian "No… No… No, get away! I-I won't let you! I—"

    hide dorian
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "Dorian! Dorian! You're shaking! Are you alright?"

    hide yuxuan
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "Sir Dorian! We have to move! Hurry!"

    hide svante
    show dorian neutral at left_char with Dissolve(0.2)
    "I sucked in a breath, forcing my body to obey. My muscles screamed in protest, locked in the remnants of my memories, but Svante's grip was tough. He yanked me backward with all his strength."
    "A heartbeat later, lightning ripped through the space where I had stood."
    "The force of the blast detonated against the stone, sending white-hot shards flying in all directions. A deafening crack split the air, the floor trembling beneath us as waves of heat seared our skin. I hit the ground hard, the impact rattling through my bones, knocking the breath from my lungs."

    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "That was close, sir Dorian."

    hide svante
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "His mind."

    "We turned to look at him."

    chung_hee "It's being warped. There's something else at work here. I'll figure something out. Buy me some time."

    hide chunghee normal_neutral
    show niko normal_serious at right_char with Dissolve(0.2)
    niko "Sure. But we can't last long if he's this powerful! We need to weaken him!"

    hide niko
    show magnus alt_evil_eye at right_char with Dissolve(0.2)
    "Above us, Magnus hovered, golden energy writhing around him like a living thing. His breathing was ragged, but his eyes burned brighter than ever."

    hide magnus
    show niko normal_meditate at right_char with Dissolve(0.2)
    niko "Kurayami ni hisomu mono… watashi no koe ni kotae yo, Enoch-sama."

    "The air shuddered. Niko rose to his feet. His usual calm was gone, replaced by a grim determination. His fingers flexed, dark energy coiling around them like tendrils of living shadow."
    "The torches lining the cavern walls flickered violently before being snuffed out—plunging us into darkness."

    hide niko
    show magnus alt_anger at right_char with Dissolve(0.2)
    magnus "YOU DARE CALL UPON THE DARK IN MY PRESENCE?!"

    "The golden energy around him exploded, tearing through the shadows in a violent burst. The sheer force sent ripples through the chamber, scattering tendrils of darkness like smoke caught in a tempest."

    hide magnus
    show niko normal_serious at right_char with Dissolve(0.2)
    "Niko barely managed to twist away, ducking behind jagged stone as radiant arcs of energy lashed out, carving deep scars into the cavern walls. But even as he evaded, I could see him—still channeling. The shadows coiled around him, writhing, adapting, waiting for an opening."

    hide niko
    "Svante, Chung-hee, Yuxuan, and I huddled behind a jagged stone. The heat of Magnus's power was oppressive, the light burning through the mist of steam left behind by the shattered ice."
    "Chung-hee was deep in thought."

    show dorian neutral at left_char with Dissolve(0.2)
    dorian "What's the situation, Chung-hee?"

    hide dorian
    show chunghee alt_tense at right_char with Dissolve(0.2)
    "He didn't respond immediately. His eyes flickered with something unsteady—like he wasn't fully present. His breathing was uneven."

    chung_hee "Something's very wrong. His mind is in chaos. Broken, fragmented—like shattered glass scattered across a storm. I can sense the echoes of his memories, but they are not whole."

    hide chunghee alt_tense
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "W-What do you mean? Can you fix it?"

    hide yuxuan
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "It is a labyrinth of torn recollections—some forced upon him, some stolen, some warped beyond recognition. I need a moment to piece them together."

    hide chunghee normal_neutral
    show dorian serious at left_char with Dissolve(0.2)
    dorian "Then do what you must, Chung. We'll hold the line."

    hide dorian
    show svante normal_nervous at right_char with Dissolve(0.2)
    "A sudden pulse of divine energy sent tremors through the stone, and Svante turned to me, his breath shallow, eyes darting between Magnus and Niko. His fingers curled into fists."

    svante "Sir Niko needs help."

    hide svante
    show dorian neutral at left_char with Dissolve(0.2)
    "I could see it—the hesitation in his gaze, the silent question behind his words. He was waiting for guidance."
    "I exhaled sharply, mind racing. Svante's a metal channeler. If we were going to turn the tide, I needed Svante to focus his magic on something metallic."
    "Near the rubble, broken spearheads littered the ground—remnants of royal guards who had once stood here. They were crude, but they were large enough to act as a weapon."
    "Scattered all around us were the remains of ancient lantern stands, their metal frames cracked and bent. They weren't as large or sturdy as the spearheads, but their fragmented nature meant Svante could spread his power through them, striking from multiple angles at once. And with Magnus focused on Niko, he might not anticipate it."

    jump ch8_magnus_battle


# =============================================================================
# SECTION 15: LABEL CH8_MAGNUS_BATTLE — Battle QTCs (wing tracker)
# =============================================================================

label ch8_magnus_battle:

    play music ost_ch8_magnus fadein 0.5        # PLACEHOLDER — intense divine battle theme

    "Quick Timed Choice:"

    menu:

        "Ask Svante to channel the fallen spearheads":
            $ ch8_d2_choice = "spearheads"

            show dorian serious at left_char
            "I gripped Svante's shoulder, voice firm."

            dorian "Use the spearheads, Svante."

            hide dorian
            show svante alt_base at right_char with Dissolve(0.2)
            "He gave a sharp nod, his eyes narrowing in focus. With a flick of his wrist, the broken spearheads trembled—then shot forward, streaking through the air like jagged bolts of metal, twisting and writhing as they hurtled toward Magnus."
            "At the last second, Magnus' wings snapped open, a radiant gust of golden energy surging outward. The spearheads met his divine aura with a violent clang, stopping mid-air as if colliding with an unseen force."
            "Sparks burst from the impact, the shadows flickering and twisting—but Magnus barely flinched."

            show magnus alt_anger at right_char with Dissolve(0.2)
            magnus "Pathetic."

            hide magnus
            hide svante
            "Before we could react, he raised his hand—and with a single crushing motion, the pillar we were hiding behind detonated, sending shards of rock raining down around us."
            "I barely had time to throw up my arms as the blast sent us sprawling. Dust choked the air, and pain flared through my side as I hit the ground hard."

            show svante normal_neutral at right_char with Dissolve(0.2)
            svante "*coughs* S-Sorry. My bad…"

            hide svante
            show yuxuan normal_neutral at right_char with Dissolve(0.2)
            yuxuan "*coughs* I… I think I'm going to be sick…"

            hide yuxuan
            jump ch8_battle_qtc2

        "Ask Svante to channel the fallen lantern stands.":
            $ ch8_d2_choice = "lanterns"
            $ wing_tracker += 1

            show dorian neutral at left_char
            "I met Svante's eyes."

            dorian "Svante, see the lantern shards around us?"

            hide dorian
            show svante normal_neutral at right_char with Dissolve(0.2)
            svante "Yes, sir Dorian. What do you want me to- Oh… got it."

            "Svante hesitated for only a second before nodding. His hands moved in sharp, precise motions, and the jagged shards of metal hurtled toward Magnus."

            # play sound sfx_metal_shards      # PLACEHOLDER

            hide svante
            show magnus alt_shocked at right_char with Dissolve(0.2)
            "The shards whistled through the air, moving unpredictably, weaving and darting. They struck Magnus from multiple angles, slashing across his arms, his chest—his wings."

            magnus "AHHH!!!"

            "His body recoiled mid-air, wings jerking as golden blood sprayed into the mist. He staggered backward, his form flickering with instability. For the first time, a look of genuine surprise crossed his face."
            "With a furious roar, Magnus threw out his arm. A burst of divine energy erupted from him like a tidal wave, and before we could react—"
            "The rock pillar we were hiding behind shattered."

            hide magnus
            show svante normal_nervous at right_char with Dissolve(0.2)
            svante "*coughs* Did I do good?"

            hide svante
            jump ch8_battle_qtc2


label ch8_battle_qtc2:

    show magnus alt_evil_eye at right_char with Dissolve(0.2)
    "Magnus' golden eyes locked onto mine. Fury burned in their depths, raw and seething. His wings flared, sending waves of heat rolling through the cavern."

    magnus "You."

    show dorian serious at left_char with Dissolve(0.2)
    "My breath hitched."

    show magnus alt_anger at right_char
    magnus "You're the one who haunted my dreams. The tormentor. The deceiver."
    magnus "The VILLAIN."

    show dorian neutral at left_char
    "My pulse pounded in my ears. Villain?"

    dorian "Villain? What in Tetrad's name are you talking about? You're the one—"

    show magnus alt_anger at right_char
    magnus "YOU MUST DIE, MONSTER!"

    hide magnus
    hide dorian
    "Magnus lunged. I barely had a second to react before he closed the distance, his hand wreathed in blinding celestial fire."

    "Quick Timed Choice:"

    menu:

        "Stand my ground and try to block the attack":
            $ ch8_d3_choice = "stand"

            show dorian serious at left_char with Dissolve(0.2)
            "I planted my feet, raising my sword to brace against the impact. If I could just—"
            "Too late."
            "Magnus' strength was monstrous. The instant his strike connected, a shockwave of divine force blasted through me. Pain. White-hot, searing pain. My entire body jerked backward as I was sent flying, crashing against the cavern floor."

            show dorian neutral at left_char
            dorian "*coughs* Dragon's bollocks."

            hide dorian
            show yuxuan normal_neutral at right_char with Dissolve(0.2)
            yuxuan "Dorian! Are you alright?!"

            show dorian neutral at left_char with Dissolve(0.2)
            dorian "I'm fine…"

            hide dorian
            hide yuxuan
            show niko normal_serious at right_char with Dissolve(0.2)
            niko "He's too strong!"

            hide niko
            jump ch8_battle_qtc3

        "Dodge and counter":
            $ ch8_d3_choice = "dodge"
            $ wing_tracker += 1

            show dorian dragon_eyes at left_char with Dissolve(0.2)
            "I moved."
            "Instinct screamed at me—don't block, don't take it head-on. At the last second, I twisted sharply, the heat of Magnus' strike grazing past my armor instead of slamming into me full force."
            "I used that instant. Draconic fire flared through my hand, and I punched his side. Magnus flinched and staggered."

            show magnus alt_shocked at right_char with Dissolve(0.2)
            magnus "YOU MONSTER! I'LL KILL YOU!"

            hide magnus
            show niko normal_smile at right_char with Dissolve(0.2)
            niko "Great job!"

            hide niko
            jump ch8_battle_qtc3


label ch8_battle_qtc3:

    show magnus alt_anger at right_char with Dissolve(0.2)
    "Magnus' wings exploded outward, their sheer size blotting out the dim cavern light. The golden energy rippling from his form turned violent—twisting, writhing, expanding in jagged arcs that scraped against the cavern walls. The sheer force of it sent a storm of dust and debris raining down."
    "Some of the dead bodies were moved and left falling off the central platform."

    hide magnus
    show dorian serious at left_char with Dissolve(0.2)
    dorian "Everyone, grab onto something!"

    hide dorian
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "Prosperity Dragon, save me!!"

    hide yuxuan
    show svante normal_nervous at right_char with Dissolve(0.2)
    "Svante almost fell, but he got a knife and attached it to the ground to avoid him falling."

    svante "That was close…"

    hide svante
    show magnus alt_evil_eye at right_char with Dissolve(0.2)
    "Magnus ascended."
    "The cavern trembled beneath his rise. His wings, drenched in divine radiance, tore through the air, leaving streaks of molten light in their wake. The heat was suffocating, like standing too close to the heart of a dying star."
    "His eyes glew as he spoke."

    magnus "You CANNOT escape me. The gates of Xianlun stand open. They shall welcome you into eternity."

    hide magnus
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    "And then he descended like a falling sun."

    yuxuan "AHHH!!"

    hide yuxuan
    show niko normal_meditate at right_char with Dissolve(0.2)
    niko "Shadows, to me!! Kage no subete wa watashi no meirei ni shitagau."

    "Darkness surged from Niko's body, curling like living smoke, devouring the golden light that tried to consume it. His shadows thickened into jagged tendrils, writhing with power, anchoring themselves into the stone like black thorns."
    "The shadows wrapped around Magnus' legs, his arms—clinging, pulling. They thrashed like chains forged from the abyss, tightening with every flick of Niko's wrist."

    show magnus alt_anger at right_char with Dissolve(0.2)
    magnus "Argh!! Let go of me!"

    hide magnus
    show svante alt_base at right_char with Dissolve(0.2)
    "Scattered across the battlefield, metal glinted in the dim light—broken spearheads, shattered lantern shards. Svante lifted a hand, and the pieces shook."

    # play sound sfx_metal_shards              # PLACEHOLDER

    "Like a storm of blades, the metal debris whipped through the air, honing in on Magnus with deadly precision. Svante's power magnified them, spinning them faster than any thrown weapon could ever reach."
    "One jagged piece tore across Magnus' wing."

    hide svante
    show magnus alt_anger at right_char with Dissolve(0.2)
    magnus "AHHHH!! YOU WILL PAY FOR THIS!!"

    "A roar of pain erupted from his throat, shaking the walls, sending dust cascading from the ceiling. His flight wavered, his balance lost for a fraction of a second."

    hide magnus
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "Who in the Prosperity Dragon's name is this guy?! Why is he this powerful?!"

    "Panic flared in his eyes, but it didn't stop him from acting. With the speed and confidence of a seasoned gambler betting it all, he unscrewed the cap of a flask, wound up his arm, and hurled it straight toward Magnus."
    "It sailed through the air—"
    "And smacked squarely into Chung-hee's shoulder. The impact made the sound of an unimpressively dull thunk."

    hide yuxuan
    show chunghee alt_tense at right_char with Dissolve(0.2)
    "Chung-hee, mid-focus, stiffened. For a brief, fleeting moment, his regal composure cracked, his lips pressing into a thin line as he slowly turned his head to inspect the object that had so rudely interrupted him."

    chung_hee "Sir Yuxuan, I implore you—cease this senseless barrage immediately."

    hide chunghee alt_tense
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "S-Sorry! It was a good plan in my head, okay?!"

    hide yuxuan
    show magnus alt_anger at right_char with Dissolve(0.2)
    "The wind howled. Magnus channeled air, and it responded to him like a vengeful god. The pressure in the chamber shifted violently, turning the space into a raging tempest."
    "A cyclone of sheer force erupted from Magnus' outstretched hand, aimed directly at us."

    hide magnus
    show svante normal_nervous at right_char with Dissolve(0.2)
    "I felt my feet slipping. The ground beneath me vanished as the wind threatened to hurl us into the chasm below."

    svante "T-The wind?! What should we do?"

    hide svante

    "Quick Timed Choice:"

    menu:

        "Counter with fire, trying to burn through the wind.":
            $ ch8_d4_choice = "fire_wind"

            show dorian dragon_eyes at left_char with Dissolve(0.2)
            "The air raged, trying to throw me into the abyss—but I wasn't going to let it."
            "I called upon my fire. Draconic fire."
            "The warmth ignited within me, coiling in my chest before bursting forth. A roaring pillar of flame surged from my palms, slamming against the wind like a dragon baring its fangs."
            "For a brief second, I thought it would work."
            "The fire and air clashed violently. Instead of overpowering the wind, my flames were swept up into the cyclone—twisting, twisting—turning into something volatile."

            show niko normal_anger at right_char with Dissolve(0.2)
            niko "Dorian, STOP!"

            hide niko
            show svante normal_nervous at right_char with Dissolve(0.2)
            svante "No, no, no—!"

            hide svante
            show dorian angry at left_char with Dissolve(0.2)
            "An explosion rocked the cavern. The force threw me backward. Agony flared through my arm as I slammed into the jagged stone. The smell of scorched fabric and burnt flesh filled the air."

            dorian "Ghkk—!"

            show dorian serious at left_char
            "Pain. My right arm throbbed, bleeding, burned. Smoke curled from my sleeve, and my vision blurred for a moment."

            show magnus alt_anger at right_char with Dissolve(0.2)
            magnus "You dare try to match my storms with fire?! You know nothing of loss! Nothing of PAIN!"

            "He lifted his hand again, the air thickening around us, preparing to strike once more."

            hide magnus
            show dorian serious at left_char
            "I gritted my teeth. The injury was bad, but I could still fight."

            jump ch8_battle_qtc4

        "Anchor myself with earth channeling and grab onto my companions.":
            $ ch8_d4_choice = "earth_anchor"
            $ wing_tracker += 1

            show dorian dragon_eyes at left_char with Dissolve(0.2)
            "I slammed my palm against the trembling stone beneath me, channeling earth. The ground answered my call. My energy surged downward, forcing jagged spikes of rock to burst upward, forming desperate footholds. A tether—something to keep us from being swallowed by the storm."
            "The wind still howled. I needed to hold on. I needed to pull the others back before it was too late."

            dorian "Come on! Grab my arm!"

            hide dorian
            show yuxuan normal_neutral at right_char with Dissolve(0.2)
            yuxuan "You're out of your damn mind if you think I'm letting go!"

            "Yuxuan reached first, his grip like iron. He dug his nails into my forearm, anchoring himself against the relentless force."

            hide yuxuan
            show svante normal_nervous at right_char with Dissolve(0.2)
            svante "I-I can't—!"

            "He was slipping. His feet scraped against the stone, but the wind was too strong. His frame was being dragged straight for the abyss."

            svante "Sir Dorian! Sir Dorian, help please!! AHHH—"

            show dorian serious at left_char with Dissolve(0.2)
            dorian "Svante!!"

            hide dorian
            hide svante
            show niko normal_serious at right_char with Dissolve(0.2)
            "A shadow tendril grabbed Svante's arm."

            niko "Are you alright?"

            hide niko
            show svante normal_nervous at right_char with Dissolve(0.2)
            svante "Yes, sir Niko. T-Thank you."

            hide svante
            show chunghee alt_charging at right_char with Dissolve(0.2)
            "Chung-hee floated, his cape whipping around him like a storm-struck banner."

            chung_hee "I'm getting the bigger picture of his mind. I'm close!"

            hide chunghee alt_charging
            jump ch8_battle_qtc4


label ch8_battle_qtc4:

    show magnus alt_anger at right_char with Dissolve(0.2)
    magnus "I see that you've wounded me. Villains. Righteousness will have its vengeance!"

    "Magnus exhaled slowly, closing his eyes. The faint scratches on his wings—remnants of our desperate struggle—began to disappear."

    hide magnus
    show niko normal_serious at right_char with Dissolve(0.2)
    niko "That's… that's not possible."

    hide niko
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "H-He just—! That should've taken time!"

    hide svante
    show magnus alt_evil_eye at right_char with Dissolve(0.2)
    "Magnus' white eyes snapped open. The air shuddered with his presence."

    magnus "You think you can wound me? Me?!"

    "His voice sent a ripple through the chamber. The walls cracked under the sheer force of his rage."

    magnus "I have suffered an eternity of torment. And now, you dare to stand before me as if you are not the architects of my misery?"

    "He stepped forward. Each footfall sent a tremor through the stone."

    magnus "I should rip you apart. One by one. Slowly. Make you feel what I felt when she—"

    "His breath hitched. His fingers twitched."

    hide magnus
    show dorian neutral at left_char with Dissolve(0.2)
    dorian "When she what, Magnus?"

    show magnus alt_anger at right_char with Dissolve(0.2)
    "His expression contorted. His hands clenched into fists."

    magnus "YOU TOOK HER FROM ME!"

    hide magnus
    show niko normal_anger at right_char with Dissolve(0.2)
    niko "You're being unreasonable! We don't know what you're talking about!"

    hide niko
    show magnus alt_anger at right_char with Dissolve(0.2)
    magnus "LIES! ABSOLUTE LIES! YOU SHAN'T FOOL ME WITH YOUR DECEIT, VILLAIN!"

    "Divine light ignited."
    "It surged from within him—an overwhelming pillar of golden radiance, stretching to the heavens. The light twisted and burned, crackling with unholy power."

    hide magnus
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "W-What's going on?!"

    hide yuxuan
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "He's channeling light… but—"

    hide svante
    show chunghee alt_charging at right_char with Dissolve(0.2)
    "The very air seemed to bend. The cavern rumbled. I looked at Chung-hee, still concentrating on Magnus' mind."

    hide chunghee alt_charging
    show niko normal_serious at right_char with Dissolve(0.2)
    niko "Damn it! He's not just wielding power—he's devouring it! We're wasting our strength throwing everything at him!"

    hide niko
    show dorian serious at left_char
    "I need to do something."

    "Quick Timed Choice:"

    menu:

        "Counter with Draconic Fire":
            $ ch8_d5_choice = "fire_magnus"

            show dorian dragon_eyes at left_char
            "My instincts screamed at me. Fight back."
            "I channeled my fire, reaching deep within myself. My core burned, the draconic energy roaring to life."
            "The heat within me surged outward, twisting into a spiraling inferno."
            "And yet—It didn't work."
            "Magnus' light consumed my fire."

            show dorian angry at left_char
            dorian "Ghhkk—!"

            hide dorian
            "I was thrown backward, my body crashing against the cavern wall. A sharp crack erupted through my arm, a searing pain spreading like wildfire. My vision blurred. Smoke curled from my skin."

            show niko normal_anger at right_char with Dissolve(0.2)
            niko "DORIAN!"

            hide niko
            show svante normal_nervous at right_char with Dissolve(0.2)
            svante "SIR DORIAN!"

            hide svante
            show dorian serious at left_char with Dissolve(0.2)
            "Their voices were distant, muffled beneath the ringing in my ears. I forced myself upright, my movements sluggish and pained. My fingers curled against my ribs. It hurts."

            show magnus alt_anger at right_char with Dissolve(0.2)
            "Above me, Magnus hovered, bathed in golden fury, his wings outstretched like a vengeful god descending upon the unworthy. His eyes burned with celestial wrath, locking onto me like I was nothing more than a blasphemer before his throne."

            magnus "You dare fight me? You dare compare your flame to the light of the divine?!"

            hide magnus
            jump ch8_magnus_end

        "Reason with Magnus":
            $ ch8_d5_choice = "reason"
            $ wing_tracker += 1

            show dorian neutral at left_char
            "I clenched my fists, my body begging me to retaliate—but I forced myself to breathe. Think."
            "I looked at Magnus. He wasn't just furious. He was in agony. Grief."
            "I remembered losing Elara, my wife. How it felt."

            dorian "Magnus—stop!"

            show magnus alt_anger at right_char with Dissolve(0.2)
            magnus "You would dare speak to me?! After what you've done?!"

            hide magnus
            show dorian neutral at left_char
            dorian "I don't know what happened. But I know you're hurting. Tell me what happened."

            show magnus alt_close at right_char with Dissolve(0.2)
            "His wings twitched. The divine light flickered—for just a moment."
            "I stepped forward."

            hide magnus
            show dorian neutral at left_char
            dorian "We didn't take her from you, Magnus. We don't even know who you mean."

            hide dorian
            show svante normal_neutral at right_char with Dissolve(0.2)
            svante "You think we're your enemies, but we're not!"

            hide svante
            show magnus alt_close at right_char with Dissolve(0.2)
            "Magnus staggered. His breath came uneven, his fists clenched so tightly his knuckles turned white. The divine glow around him wavered, like a candle caught in the wind."

            magnus "DECEIT! FOUL VILLAIN!"

            hide magnus
            jump ch8_magnus_end


# =============================================================================
# SECTION 16: LABEL CH8_MAGNUS_END — Wing Check / Bad End or Proceed
# =============================================================================

label ch8_magnus_end:

    if wing_tracker < 3:

        "DIFFERENT OUTCOMES"

        show magnus alt_anger at right_char with Dissolve(0.2)
        magnus "You think you can deceive me? You think I cannot see the blood on your hands?"

        "And then—he moved."
        "Faster than thought. Faster than we could react."

        hide magnus
        show chunghee normal_neutral at right_char with Dissolve(0.2)
        "Chung-hee staggered, a radiant blade of light impaled through his chest."
        "His lips parted, but no sound came. The divine energy devoured him from the inside, spreading like wildfire. His body disintegrated into golden dust before he could even scream."

        hide chunghee normal_neutral
        show niko normal_anger at right_char with Dissolve(0.2)
        niko "CHUNG-HEE—!"

        hide niko
        show svante normal_nervous at right_char with Dissolve(0.2)
        svante "Sir Chung! NO!!"

        "Niko lunged forward, fury igniting in his eyes, shadow engulfing his body."
        "With a flick of his hand, a spear of golden fire erupted from the ground, spearing Niko clean through."

        hide svante
        show niko normal_sad at right_char with Dissolve(0.2)
        "He gasped—his eyes wide, his mouth moving soundlessly—"

        niko "Urgh- Ah… Lord Enoch…"

        hide niko
        show svante normal_nervous at right_char with Dissolve(0.2)
        svante "No, no, no—!"

        "Svante tried to run—a mistake."
        "Magnus reached out."
        "An unseen force gripped Svante's body, lifting him off the ground. His limbs jerked, twisting at unnatural angles as if invisible hands were crushing him from the inside."

        show svante normal_angry at right_char
        svante "AHHH!!!"

        hide svante
        show dorian angry at left_char with Dissolve(0.2)
        "His neck twisted violently to the side. His body dropped."

        dorian "Svante! No!"

        hide dorian
        show yuxuan normal_neutral at right_char with Dissolve(0.2)
        yuxuan "Svanteee!!!"

        "Magnus raised a hand. A single, effortless motion."
        "Yuxuan's body crumpled. His breath caught in his throat, his mouth open in a silent scream as his own bones crushed inward, collapsing under the weight of his will."

        yuxuan "D-Dorian… I—"

        hide yuxuan
        show dorian angry at left_char with Dissolve(0.2)
        dorian "No!! YU!!"

        hide dorian
        show magnus alt_evil_eye at right_char with Dissolve(0.2)
        "Magnus turned his head towards me, slow, deliberate. His wings unfurled, their brilliance unbearable, their presence suffocating."
        "His white eyes locked onto mine. For a fraction of a second, something wavered."

        magnus "Dorian…"

        "His voice—uncertain, shaken."

        magnus "Please! T-This isn't m—"

        show magnus alt_anger at right_char
        "Then, like a blade through glass, the moment shattered. His face twisted, his body tensed—whatever glimpse of clarity had surfaced was drowned beneath raw, consuming fury."

        hide magnus
        show dorian serious at left_char with Dissolve(0.2)
        dorian "M-Magnus?!"

        show magnus alt_anger at right_char with Dissolve(0.2)
        magnus "DIE, VILLAIN!!"

        hide magnus
        show dorian angry at left_char with Dissolve(0.2)
        "A force wrapped around my throat."
        "I choked, my vision swimming. My body lifted off the ground, my feet dangling in the empty air."
        "My lungs burned. My fingers clawed uselessly at my throat, trying to pry away a force I could not touch."
        "Magnus brought me closer. Face to face."

        show dorian sad at left_char
        dorian "Magnus…*coughs*"

        hide dorian
        show magnus alt_evil_eye at right_char with Dissolve(0.2)
        "His expression was unreadable, but his eyes—those terrible, soulless white eyes—bored into me, stripping me down to my very core."

        magnus "You will feel what I felt."

        hide magnus
        show yk at center_yg with Dissolve(0.2)
        "Then suddenly, I saw him. A presence just beyond Magnus, just behind his flickering golden light. A figure watching with quiet amusement."
        "A crown of bone sat atop his head, the twisted remnants of something ancient and cruel."

        yk "Shame… I thought you had what it takes, dragonkin."

        hide yk
        show dorian sad at left_char with Dissolve(0.2)
        "The last of my breath fled my body."
        "I gasped—a final, desperate sound."
        "And then everything went black."

        hide dorian
        jump game_over

    else:

        jump ch8_magnus_peace


# =============================================================================
# SECTION 17: LABEL CH8_MAGNUS_PEACE — Chung-hee Breaks Through / Magnus Calms
# =============================================================================

label ch8_magnus_peace:

    # play sound sfx_divine_pulse              # PLACEHOLDER

    show magnus alt_anger at right_char with Dissolve(0.2)
    magnus "AHHHH!! MY HEAD!!"

    "Suddenly, the divine light around him shuddered before flickering violently, like a sun on the verge of exploding. His wings spasmed. His hands shot up to clutch his head, fingers digging into his skull."
    "His voice tore through the chamber like a dying star. The walls shook. The very ground beneath us quaked as his agony turned into a raw, unfiltered roar of fury."

    magnus "YOU KILLED ADRIANA!! MURDERER! VILLAIN!!"

    hide magnus
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "There's so much talk of this Adriana. Who is she? We don't even know who she is!"

    hide yuxuan
    show magnus alt_anger at right_char with Dissolve(0.2)
    "The heat of his rage was scorching. Even as he clutched his head, golden veins of divine energy flared violently across his arms, surging out in wild, uncontrollable bursts. The air around him bent, warped, twisted like reality itself was struggling under his presence."
    "I took a step back, barely stopping myself from instinctively summoning my fire again."

    hide magnus
    show niko normal_serious at right_char with Dissolve(0.2)
    niko "We didn't kill her, Magnus!"

    hide niko
    show magnus alt_anger at right_char with Dissolve(0.2)
    magnus "DECEIVERS!"

    hide magnus
    show chunghee alt_charging at right_char with Dissolve(0.2)
    "Another pulse of power. A shockwave. Stones rained from above as the cavern cracked apart at the seams."
    "Through it all, Chung-hee stood firm."
    "He placed two fingers against his temple, eyes locked onto Magnus like a hunter sighting prey."

    chung_hee "Your mind is in shambles, Magnus."

    hide chunghee alt_charging
    show magnus alt_close at right_char with Dissolve(0.2)
    "Magnus' whole body convulsed. His breathing was ragged, uneven. It was like something inside him was tearing apart—splitting him in two."

    magnus "*panting* I WON'T GIVE IN!! YOU WON'T TWIST ME LIKE HER!! I'LL KILL YOU ALL!"

    hide magnus
    show chunghee alt_tense at right_char with Dissolve(0.2)
    chung_hee "You were frozen for centuries. You have no real memory, Magnus."

    hide chunghee alt_tense
    show magnus alt_anger at right_char with Dissolve(0.2)
    magnus "YOU LIE!"

    "He slammed a fist into the ground. The earth ruptured beneath him in a violent, golden explosion."
    "I staggered back, shielding my face as dust and debris erupted around us."

    hide magnus
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "But Chung-hee didn't move."
    "His voice remained calm. Unyielding."

    chung_hee "All your memories—they were implanted. Fabricated. Artificial."

    hide chunghee normal_neutral
    show dorian neutral at left_char with Dissolve(0.2)
    "I was in shock. Fabricated memories?"

    hide dorian
    show magnus alt_close at right_char with Dissolve(0.2)
    "Magnus' breath hitched."
    "For a second, the divine light around him faltered. But then—he roared again."

    magnus "NO! NO! I REMEMBER HER! I REMEMBER HER SMILE! I REMEMBER HER HAND IN MINE! YOU WON'T TAKE THAT FROM ME!"

    "Magnus' breath came in ragged, seething gasps. His body trembled—whether from pain or fury, I couldn't tell. His wings remained outstretched, the divine light flickering chaotically along the edges like an unstable flame."

    magnus "Y-You're trying to twist me. Trying to make me forget her."

    hide magnus
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "Calm down, Magnus. We're just as confused as you are."

    hide chunghee normal_neutral
    show magnus alt_close at right_char with Dissolve(0.2)
    "Magnus' wings twitched. His muscles tensed, but something in his expression… shifted."
    "Doubt."
    "Hesitation."

    hide magnus
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "We aren't your enemies. We aren't here to hurt you."

    hide chunghee normal_neutral
    show magnus alt_close at right_char with Dissolve(0.2)
    "Magnus' gaze snapped to me instantly, his entire body coiled like a predator ready to pounce."

    hide magnus
    show dorian neutral at left_char with Dissolve(0.2)
    "I extended my hand."

    dorian "See? We're not out to get you."

    show magnus alt_close at right_char with Dissolve(0.2)
    "His chest heaved. His wings twitched. But he didn't move."
    "I followed his line of sight—to the shattered ice. The ice that had once entombed him."

    hide magnus
    show dorian neutral at left_char
    dorian "We freed you, Magnus."

    show magnus alt_newpose at right_char with Dissolve(0.2)
    "For a long, aching moment, Magnus just stared."
    "His fingers twitched. His lips parted. The divine light around him dimmed."
    "A choked breath escaped him."

    magnus "Everything I knew… everything I remembered… was a lie?"

    "Magnus' hand trembled as he stared at mine. His breath was shallow, unsteady. For a moment, I thought he would refuse—thought he would pull away, retreat into his fury."
    "But then—his fingers twitched."
    "His shoulders sagged, as if the weight of centuries was suddenly crushing him all at once."
    "And he took my hand."

    hide magnus
    jump ch8_walk_back


# =============================================================================
# SECTION 18: LABEL CH8_WALK_BACK — Return to Lab / Magnus Collapses / Sleep
# =============================================================================

label ch8_walk_back:

    scene bg_tianho_underground_2 with fade     # PLACEHOLDER — underground tunnel 2
    stop music fadeout 2.0
    play music ost_ch8_end fadein 2.0           # PLACEHOLDER — quiet relief theme

    show dorian neutral at left_char with Dissolve(0.2)
    show magnus normal at right_char with Dissolve(0.2)
    "The walk back to Yuxuan's hidden laboratory was uneventful. None of us spoke much—our minds still reeling from everything that had happened. The discovery of Magnus, the battle, the truth behind his memories… it was too much to process all at once."
    "Magnus barely made it halfway before his strength gave out. His body, once brimming with divine power, now seemed fragile—human. He collapsed, barely conscious, his breathing shallow but steady."
    "I caught him before he hit the ground, feeling the unnatural heat still lingering beneath his skin. His wings were dragging on the cave floor."

    hide dorian
    hide magnus

    scene cg_black with fade                    # PLACEHOLDER — black screen
    stop music fadeout 1.0

    show roboto happy at right_robot with Dissolve(0.2)
    "When we finally reached the laboratory, Roboto was on edge. It seemed to sense the tension. It moved toward Magnus, scanning him with mechanical precision before giving a small nod."

    roboto "H-H-HHe requires rest. I have prepared a bed. Please f-f-follow me."

    hide roboto
    show magnus normal at right_char with Dissolve(0.2)
    "We did as it instructed, laying Magnus down on the softest mattress we could find. His face was pale, his breathing slow but even."
    "With that done, the rest of us barely managed to settle in before exhaustion dragged us under. The moment my head hit the pillow, I felt myself slipping into the depths of sleep."
    "The day had been long. Too long. And as my consciousness faded, I could only hope that tomorrow would bring more answers."

    hide magnus
    "CHAPTER 9"

    scene bg_lab_bedroom_normal with fade       # PLACEHOLDER — lab bedroom, soft morning light

    show dorian sleepware_neutral at left_char with Dissolve(0.2)
    "I woke to the softest, most comforting scent. The warm aroma of freshly laundered sheets mixed with something faintly sweet—like the lingering traces of vanilla and sun-dried cotton."
    "The fabric cradled me in its gentle embrace, and for a moment, I considered sinking deeper into its warmth. But then, the sound of soft munching reached my ears."
    "I blinked my eyes open, taking in the dim light of the fixtures."

    hide dorian

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
