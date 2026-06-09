###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  FILE:  chapter_05.rpy
#  SCENE: CHAPTER 5 — Cheng Industries
#
#  CONTENTS:
#    Section 1  — Character Definitions (NEW for Chapter 5)
#    Section 2  — Image Declarations
#    Section 3  — Audio Declarations
#    Section 4  — Game Variables
#    Section 5  — label chapter_5            (Underground — tunnel walk)
#    Section 6  — label ch5_lab_entrance     (Underground 2 — lab passage)
#    Section 7  — label ch5_yuxuan_lab       (Yuxuan's Laboratory — entry)
#    Section 8  — label ch5_spare_room       (Lab Bedroom — Chung-hee stabilized)
#    Section 9  — label ch5_niko_choices     (Choices: talking with Niko)
#    Section 10 — label ch5_niko_common      (Common — Niko faith / Tianho memory)
#    Section 11 — label ch5_living_room      (Lab Main Room — Elias and Tim)
#    Section 12 — label ch5_storage_room     (Storage Room — Svante interrogation)
#    Section 13 — label ch5_svante_choices   (Choices: questioning Svante)
#    Section 14 — label ch5_svante_common    (Common — Svante freed)
#    Section 15 — label ch5_dinner_setup     (Lab Main Room — dinner preparation)
#    Section 16 — label ch5_food_choice      (Choice: cuisine selection)
#    Section 17 — label ch5_nap              (Lab — Dorian naps, Weng intro)
#    Section 18 — label ch5_chung_wakes      (Kitchen — Chung-hee arrives at dinner)
#    Section 19 — label ch5_roboto_witness   (Choice: Roboto witness)
#    Section 20 — label ch5_food_moonlit     (IF Moonlit Noodles)
#    Section 21 — label ch5_food_truffle     (IF Imperial Truffle Roast)
#    Section 22 — label ch5_food_hotpot      (IF Fisherman's Hotpot)
#    Section 23 — label ch5_food_lamb        (IF Mjollian Mead-Braised Lamb)
#    Section 24 — label ch5_food_common      (Food common — Roboto dish for Chung-hee)
#    Section 25 — label ch5_dinner_talk      (Dinner — Gustav choice / Chung reveals plan)
#    Section 26 — label ch5_divine_weapon    (Chung reveals Divine Weapon / Cheonmyeong Gyeol)
#    Section 27 — label ch5_amulet_vision    (Dorian touches amulet — vision sequence)
#    Section 28 — label ch5_magnus_choices   (White screen — Magnus choices)
#    Section 29 — label ch5_magnus_common    (Magnus common — void breaks)
#    Section 30 — label ch5_nightmare        (Yaoguai King nightmare — end of chapter)
#
#  NAMING CONVENTIONS:
#    image tags      — bg_name, cg_name, character_name emotion
#    audio variables — audio.ost_name, audio.sfx_name, audio.amb_name
#    label names     — ch5_name (all lowercase, underscores only)
#    game variables  — chunghee_affection, yuxuan_affection, etc.
#    NO SPACES in any tag, label, variable, or image name.
#
#  POV NOTE:
#    All sections are Dorian's POV unless otherwise noted.
#
#  TRACKER SUMMARY:
#    yuxuan_affection   : +1 ch5 food choice Tianho / +1 Roboto choice 2 (No)
#    niko_affection     : +1 Roboto choice 1 (Yes) / +1 food choice Hinami
#    chunghee_affection : +1 ch5 D(Chung) inspiring choice / -1 naïve choice
#    svante_affection   : +1 food choice Mjoll
#
#  FOOD TRACKER:
#    ch5_food_choice : "tianho" "gale" "hinami" or "mjoll"
#    ch5_food_unlocked : name of dish added to journal
#
#  PLACEHOLDER PATHS:
#    Search "# PLACEHOLDER" to find every line that needs a real asset.
###############################################################################


# =============================================================================
# SECTION 1: CHARACTER DEFINITIONS (NEW FOR CHAPTER 5)
# =============================================================================

# compiled character definitions

# =============================================================================
# SECTION 2: IMAGE DECLARATIONS
# =============================================================================

# --- Backgrounds: Underground ---
image bg_tianho_underground_2    = "images/backgrounds/bg_tianho_underground_2.png"        # PLACEHOLDER
# Refined underground passage — electric lights on earthen walls, warm glow

image bg_underground_door        = "images/backgrounds/bg_underground_door.png"            # PLACEHOLDER
# Large polished metal door — no handles, no keyholes, gleaming under artificial light

# --- Backgrounds: Yuxuan's Lab ---
image bg_yuxuan_lab              = "images/backgrounds/bg_yuxuan_lab.png"                  # PLACEHOLDER
# Spacious lab interior — sleek furniture, shelves of books/blueprints, wall screens

image bg_yuxuan_lab_dim          = "images/backgrounds/bg_yuxuan_lab_dim.png"              # PLACEHOLDER
# Same as above but with dimmed warm lighting — evening atmosphere

image bg_lab_bedroom             = "images/backgrounds/bg_lab_bedroom.png"                 # PLACEHOLDER
# Well-furnished spare room — soft lighting, lone bed in corner, wooden chair beside it

image bg_lab_storage             = "images/backgrounds/bg_lab_storage.png"                 # PLACEHOLDER
# Dim storage room — single candle, cold stone floor, stale air

image bg_kitchen                 = "images/backgrounds/bg_kitchen.png"                     # PLACEHOLDER
# Lab kitchen and dining area — long table, warm light, Weng's cookpot on stove

# --- Backgrounds: Vision/Nightmare Sequences ---
image bg_white_screen            = "images/backgrounds/bg_white_screen.png"                # PLACEHOLDER
# Endless white void — no floor, no sky

image bg_sealed_door             = "images/backgrounds/bg_sealed_door.png"                 # PLACEHOLDER
# Underground chamber — crumbling stone, torchlight, blood on floor

image bg_tianho_on_fire          = "images/backgrounds/bg_tianho_on_fire.png"              # PLACEHOLDER
# Tianho city proper engulfed in flames — screaming crowds, smoke billowing

# --- CGs ---
image cg_dorian_amulet_vision    = "images/cg/cg_dorian_amulet_vision.png"                 # PLACEHOLDER
# Dorian convulsing as green amulet light engulfs him at the dinner table

image cg_magnus_void             = "images/cg/cg_magnus_void.png"                          # PLACEHOLDER
# Magnus in white void — wings spread, golden eyes urgent, reaching toward Dorian

image cg_minjoon_dying           = "images/cg/cg_minjoon_dying.png"                        # PLACEHOLDER
# Emperor Min-joon and Empress Seo-yeon dying together, amulet in hand, underground

image cg_yaoguai_nightmare       = "images/cg/cg_yaoguai_nightmare.png"                    # PLACEHOLDER
# Yaoguai King looming over chained Elara and children — Dorian restrained in foreground


# =============================================================================
# SECTION 3: AUDIO DECLARATIONS
# =============================================================================

# --- Music ---
define audio.ost_tunnel_move     = "audio/music/ost_tunnel_move.ogg"        # PLACEHOLDER
# Tense yet quiet — underground movement, dripping water

define audio.ost_cheng_lab       = "audio/music/ost_cheng_lab.ogg"          # PLACEHOLDER
# Warm, curious — inside Yuxuan's underground lab

define audio.ost_niko_faith      = "audio/music/ost_niko_faith.ogg"         # PLACEHOLDER
# Quiet and somber — Niko explaining Enoch and the Prophets

define audio.ost_svante_talk     = "audio/music/ost_svante_talk.ogg"        # PLACEHOLDER
# Low tension — Svante interrogation in storage room

define audio.ost_dinner_warm     = "audio/music/ost_dinner_warm.ogg"        # PLACEHOLDER
# Warm, light — dinner scene with the full group

define audio.ost_chung_reveal    = "audio/music/ost_chung_reveal.ogg"       # PLACEHOLDER
# Tense — Chung-hee's revelation about Gustav and the Divine Weapon

define audio.ost_amulet_vision   = "audio/music/ost_amulet_vision.ogg"      # PLACEHOLDER
# Ethereal — amulet contact, Dorian's vision

define audio.ost_magnus_void     = "audio/music/ost_magnus_void.ogg"        # PLACEHOLDER
# Strange, otherworldly — white void with Magnus

define audio.ost_minjoon_memory  = "audio/music/ost_minjoon_memory.ogg"     # PLACEHOLDER
# Tragic — Min-joon and Seo-yeon dying in the underground chamber

define audio.ost_nightmare       = "audio/music/ost_nightmare.ogg"          # PLACEHOLDER
# Horror — Yaoguai King nightmare sequence

# --- Sound Effects ---
define audio.sfx_earth_open      = "audio/sfx/sfx_earth_open.ogg"           # PLACEHOLDER
define audio.sfx_door_scan       = "audio/sfx/sfx_door_scan.ogg"            # PLACEHOLDER
define audio.sfx_door_chime      = "audio/sfx/sfx_door_chime.ogg"           # PLACEHOLDER
define audio.sfx_door_open       = "audio/sfx/sfx_door_open.ogg"            # PLACEHOLDER
define audio.sfx_roboto_beep     = "audio/sfx/sfx_roboto_beep.ogg"          # PLACEHOLDER
define audio.sfx_roboto_crash    = "audio/sfx/sfx_roboto_crash.ogg"         # PLACEHOLDER
define audio.sfx_amulet_vision   = "audio/sfx/sfx_amulet_vision.ogg"        # PLACEHOLDER
define audio.sfx_void_crack      = "audio/sfx/sfx_void_crack.ogg"           # PLACEHOLDER
define audio.sfx_chains          = "audio/sfx/sfx_chains.ogg"               # PLACEHOLDER
define audio.sfx_sleep_powder    = "audio/sfx/sfx_sleep_powder.ogg"         # PLACEHOLDER

# --- Ambient ---
define audio.amb_tunnel_drip     = "audio/ambient/amb_tunnel_drip.ogg"      # PLACEHOLDER
define audio.amb_lab_hum         = "audio/ambient/amb_lab_hum.ogg"          # PLACEHOLDER
define audio.amb_rain_muffled    = "audio/ambient/amb_rain_muffled.ogg"     # PLACEHOLDER
define audio.amb_kitchen         = "audio/ambient/amb_kitchen.ogg"          # PLACEHOLDER


# =============================================================================
# SECTION 4: GAME VARIABLES
# =============================================================================

# default niko_affection           = 0       # Niko trust tracker
# default svante_affection         = 0       # Svante trust tracker
# default ch5_food_choice          = ""      # "tianho" "gale" "hinami" or "mjoll"
# default ch5_roboto_witness       = ""      # "yes" or "no" (Roboto stumble testimony)
# default ch5_chunghee_speech      = ""      # "naive" or "inspiring"
# default ch5_magnus_q1            = False   # Asked Magnus about Min-joon vision
# default ch5_magnus_q2            = False   # Asked Magnus about Tragedy of Tianho
# default ch5_magnus_q3            = False   # Asked Magnus about this place
# default ch5_magnus_q4            = False   # Asked Magnus about the amulet


# =============================================================================
# SECTION 5: LABEL CHAPTER_5 — Underground Tunnel Walk
# =============================================================================
# Entry point — jumped to from chapter_04.rpy label ch4_underground.
# =============================================================================

label chapter_5:
    $ save_name = "Chapter 5"
    scene bg_tianho_underground_1 with fade     # PLACEHOLDER — natural cave tunnel
    play music ost_tunnel_move fadein 2.0       # PLACEHOLDER — tense tunnel theme
    play audio amb_tunnel_drip loop fadein 1.5  # PLACEHOLDER — dripping water ambient
    play audio amb_rain_muffled loop fadein 1.0 # PLACEHOLDER — muffled rain above

    "We pressed forward, the sound of rain muffled by the earth above."
    "The man I carried on my shoulder was heavier than I expected, his weight pressing down on me with every step."
    "I carried the unconscious young man on my shoulder, the scent of his unfamiliar perfume seemed to linger on my nose. Refined, yet foreign."
    "Behind me, Niko walked in silence, his sharp gaze fixed on the unconscious figure. He kept checking his pulse, brushing damp hair away from his face, as if making sure he was still breathing."

    niko   "Breathing. Good. Looks like the tonic is working."

    "Elias walked beside Yuxuan, his tiny fingers clutching Tedda. The glow from his flower-shaped flashlight cast flickering shadows on the walls, guiding our way."

    elias  "Are we there yet, Mister Yuxuan? Tedda's getting tired…"
    "Tedda: …"

    "Svante, the aldorith, walked near me, shifting anxiously. Every few steps, he would whisper yet another apology, his voice trembling slightly."

    svante "Forgive me for earlier. I'm sorry… I—"

    "Still, the rain poured outside. A distant rumble of thunder echoed above."

    yuxuan "Here we are… Just open it here. Perfect."

    jump ch5_lab_entrance


# =============================================================================
# SECTION 6: LABEL CH5_LAB_ENTRANCE — Refined Underground Passage
# =============================================================================

label ch5_lab_entrance:

    # [COMMENT: bg_tianho_underground_2 — refined passage with electric lights on walls]
    scene bg_tianho_underground_2 with fade     # PLACEHOLDER — refined underground passage

    play sound sfx_earth_open                   # PLACEHOLDER — earth opening SFX

    "I planted my feet firmly on the damp ground and extended my hand. The earth rumbled beneath my palm, shifting and parting at my command. A section of the tunnel wall crumbled away, revealing an entrance—more refined than the natural cave we had been trudging through."
    "Unlike the crude, damp tunnels of before, this place was structured—a carefully designed underground passage. Electric lights, neatly affixed to the earthen walls, illuminated the space with a warm, steady glow."

    svante "This is amazing… Spectacular, even. I… I had no idea tunnels like these existed in Tianho."
    yuxuan "These tunnels were built to facilitate the safe and discreet travel of my partnered merchants. They connect key points throughout the region, allowing for the transport of goods and valuable cargo—without attracting unwanted attention."
    dorian "Amazing. I wouldn't expect less from Cheng Yuxuan himself."
    niko   "…Wait a minute. Cheng Yuxuan? You're not just a Yuxuan. You're the Cheng Yuxuan? The renowned inventor?"
    yuxuan "The one and only. Pleasure to make your acquaintance."
    niko   "No wonder you have enough coin to facilitate the construction of all these tunnels. How much did it cost? It must have been a sizeable fortune."
    yuxuan "Haha. Thanks, but these tunnels have been here for a while now. Me and my partners just happened to stumble on it by accident."
    yuxuan "It would have been a waste if these tunnels just collected dirt. So, we at Cheng Industries decided to convert it to a passageway."

    "There was silence—then—"

    svante "CHENG INDUSTRIES?! YOU'RE THAT CHENG YUXUAN?!"

    "Svante was shrieking in excitement, his eyes sparkling. He grabbed Yuxuan's sleeve like an excited child."

    svante "This… This can't be real! You—you're the genius behind the delivery bots! The man who revolutionized steam-powered mechanisms from Mjoll! You— you saved me and my mom! I— I don't even know what to say! I—"

    "His words tumbled out in an excited, breathless mess, his face glowing with genuine admiration."

    svante "During the great blizzard… when our food ran out… the relief packages from Cheng Industries saved us. We were going to die, sir! But your shipments—your generosity—we lived because of you."

    "His hands clenched against his chest, his lip trembling as he blinked rapidly, clearly fighting back tears."

    elias  "Tedda, why is he crying?"
    "Tedda: …"

    "Yuxuan rubbed the back of his neck."

    yuxuan "…Uh. Right. Well. Glad to hear that. No need to make this weird."
    svante "B-But you're amazing—"
    niko   "Kid, breathe. The last thing I need is another patient."

    jump ch5_yuxuan_lab


# =============================================================================
# SECTION 7: LABEL CH5_YUXUAN_LAB — Entry into the Lab / Door Sequence
# =============================================================================

label ch5_yuxuan_lab:

    # [COMMENT: bg_underground_door — massive polished metal door, no handles]
    scene bg_underground_door with dissolve     # PLACEHOLDER — lab entrance door

    stop audio fadeout 1.0

    "We stopped at a massive door made out of polished metal, gleaming under the artificial lighting. It beared no handles or visible keyholes."
    "As we stepped closer, a sudden hum resonated from within. A thin, radiant crimson beam of light flickered to life, sweeping across Yuxuan's face with meticulous precision. Yuxuan remained perfectly still."
    "Then, the door spoke."

    play sound sfx_door_scan                    # PLACEHOLDER — door scan SFX

    door_voice "Attention. Facial recognition is currently in progress. Please be advised that excessive movement may disrupt this unit's sensors and may impact the accuracy of identity verification. Please refrain from doing so. Thank you for your understanding."

    "A pause. The crimson light pulsed. Then—"

    door_voice "Initiating secondary verification. Please present a valid voice signature."

    "Yuxuan exhaled sharply before speaking in a smooth, practiced tone."

    yuxuan     "Cheng Yuxuan. Authorizing entry."

    "The door whirred, but did not yet open."

    door_voice "Processing… Additional security measures activated. Please provide a biological confirmation."

    "Without hesitation, Yuxuan pressed his palm against the cold metal."

    door_voice "Analyzing genetic markers. Matching results with stored biological data."

    play sound sfx_door_chime                   # PLACEHOLDER — door chime SFX

    door_voice "Identity confirmed. Welcome home, Master Yuxuan. May the blessings of the Prosperity Dragon be with you today."
    door_voice "Here at Cheng's we bring change. As per your request, this unit will not play the Cheng Industries jingle."

    svante "Here at Cheng's, we bring change—"

    # [COMMENT: bg_yuxuan_lab — spacious lab, lived-in comfort, screens on walls]
    play sound sfx_door_open                    # PLACEHOLDER — door opening SFX
    scene bg_yuxuan_lab with dissolve           # PLACEHOLDER — Yuxuan's lab main room

    play music ost_cheng_lab fadein 2.0         # PLACEHOLDER — warm lab theme
    play audio amb_lab_hum loop fadein 1.5      # PLACEHOLDER — lab ambient hum

    "With a deep, mechanical thunk, the massive door finally split apart, revealing a sterile yet inviting interior. A rush of cool, crisp air greeted us as the passageway opened. The lighting inside was dimmed but warm, perfectly illuminating the space beyond."
    "We stepped inside, one by one."
    "It looked… comfortable."
    "The room was spacious, lined with sleek furniture, and had the distinct coziness of a lived-in space rather than the cold sterility of a scientific lab. A few shelves were stacked with books, blueprints, and small trinkets, while elegant screens displayed various data across the walls."

    yuxuan "There we are. Home sweet home."
    dorian "Where should we put him?"
    yuxuan "Roboto will escort you to the spare room. Roboto! Come here."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    "At his command, a small mechanical figure whirred to life from the corner of the room. With a series of cheerful beeps, a scrappy little robot wobbled its way toward us, its monitor-like face flickering before settling into a bright, pixelated smile."

    # line 1 (1)
    roboto "You called, Master Yuxuan? Roboto is here. At your service."
    yuxuan "Can you show these people to the spare room?"

    "Roboto's screen shifted, displaying a large question mark before flickering back to its usual expression."

    roboto "Which spare room, Master Yuxuan?"
    yuxuan "Any spare room, Roboto. Now. It's urgent."
    roboto "Certainly, Master Yuxuan."

    svante "A… A robot servant? A talking real-life robot servant? This is… AMAZING!!"
    elias  "Daddy, daddy, look! A robot!"

    "Roboto tilted its small head toward them, its screen displaying a cheerful expression."

    roboto "Precisely. I am a robot. I am Master Yuxuan's r-r-robot companion. I can be whatever he wants… A butler. A cleaner. Or even his own personal c-c-c-c…"
    roboto "…chef if need be."

    "Elias let out an excited squeal, making Tedda bounce in his grasp."

    elias  "Ooohhh, so cute! Mister Roboto, do you wanna play with me and Tedda?"

    "Roboto's head twitched slightly as it processed the request."
    
    # line 06 (1) end
    roboto "Certainly! My b-b-b-built-in intelligence allows me to play a wide v-v-variety of games. S-Seeing that you are a child, might I suggest a game of 'tag'?"
    dorian "Don't touch the robot, Elias. Take a seat and wait for us…"

    "Elias pouted but obeyed, hugging Tedda close."
    "Then—"

    svante "…Wait… W-Wait a minute…"

    "His excitement drained in an instant. His gaze sharpened."

    svante "Elias? Elias?!"

    "His eyes darted toward me, then back to the child. He took a shaky step backward."

    svante "Y-You're Elias Drakos?!"

    "Elias nodded his head and innocently nodded Tedda's head as well."

    elias  "That's me! And this is Tedda. We're best friends. And that's my Daddy right there."

    "Svante's face drained of all color. He suddenly looked sick. His entire body stiffened, his expression twisted with disbelief. His hand shot up, pointing straight at Elias."

    svante "What are you doing here?! Why are you dressed up like a girl?!"

    "His voice cracked as he turned his trembling hand toward me, realization crashing over him like a tidal wave."

    svante "I—I knew something was off when you channeled draconic fire!"
    svante "Y-You're the Massacrer of Mjoll!"
    svante "You… You murdered Count Vasily… My brothers… My sisters…."
    svante "K-Kristin…"

    "A hush fell over the room, heavy and suffocating."
    "Svante's chest rose and fell rapidly, his gaze darting wildly. Desperation clawed at his voice as he turned to the others."

    svante "Everyone, we're not safe here! This man—"

    play sound sfx_sleep_powder                 # PLACEHOLDER — sleep powder SFX

    "A swift movement—Yuxuan stepped forward and flicked a handful of shimmering powder straight into Svante's face."
    "The reaction was instant."
    "His words faltered, his body swaying. He blinked sluggishly."

    svante "Wh… What?"

    "His knees buckled. With a soft thud, he collapsed onto the floor."
    "A moment of silence."

    svante "Zzz… Zzz…."

    yuxuan "You can never have too much sleeping powder."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    "Roboto's screen flickered. A sleeping face with Zs on top."

    # line 01
    roboto "I detect sudden drowsiness. Should I-I-I activate tuck-in mode?"
    niko   "No. No, no, no. Right now, we need to get to the spare room. We have a man that needs treatment."
    roboto "Ah! Of course. Prioritizing medical emergency. Please follow me."

    "The little robot turned sharply and began leading the way down the corridor."
    "I adjusted the unconscious man in my arms and followed."
    "As we walked, Yuxuan grabbed Svante by the collar and dragged him effortlessly across the floor."

    yuxuan "I'll take this one to the storage room. I'll have to call Miss Weng first."

    "He shot me a knowing glance before disappearing into the shadows with Svante in tow."

    svante "Zzz… *mumbles something incoherent* Zzz…."

    jump ch5_spare_room


# =============================================================================
# SECTION 8: LABEL CH5_SPARE_ROOM — Chung-hee Stabilized
# =============================================================================

label ch5_spare_room:

    # [COMMENT: bg_lab_bedroom — warm spare room, lone bed, wooden chair]
    scene bg_lab_bedroom with dissolve          # PLACEHOLDER — lab spare bedroom

    "We entered the spare room, finding ourselves in yet another well-furnished and comfortable space. The lighting was soft, casting a warm glow over the neatly arranged furniture. A lone bed sat in the corner, its sheets crisp and clean, with a sturdy wooden chair positioned beside it."

    roboto "H-H-Here is guest r-room number one. P-Please make yourselves comfortable. If you need something, please don't hesitate to contact me."

    "I gently lowered the man onto the bed. His head lolled slightly before settling against the pillow."
    "Niko was at his side in an instant, fingers pressing against his wrist. He frowned in concentration, waiting, feeling."

    niko "He's alright. His pulse is steady. He just needs rest."

    "He pulled the blankets up to the young man's shoulders, tucking him in with practiced care. But there was a lingering uncertainty in Niko's expression—he wasn't satisfied just yet."
    "He looked at the little robot whirring around the room."

    niko   "Excuse me, what should we call you again?"
    roboto "R-R-Robotooo. Robot with an 'o'. Roboto."
    niko   "Do you have some water here?"

    "Roboto perked up, its monitor face flashing a bright question mark before flickering back to its usual cheerful expression."

    roboto "Warm… or… C-C-Cold? Does it need to be p-p-purified?"
    niko   "Warm water is fine. Can you put it in a pitcher and bring us some cups?"
    roboto "No problemooo!!! You can count on Roboto~"

    "With an excited little whirl of its gears, Roboto scurried out of the room, leaving me alone with Niko."
    "Niko exhaled and reached into the leather parcel slung across his chest. With a practiced motion, he unfastened it and pulled out a handful of small, round seeds. They rested in his palm, barely larger than pebbles, their dark shells smooth and unassuming."
    "The air in the room shifted ever so slightly, carrying the faint, fresh scent of damp earth and blooming leaves."
    "The seeds stirred in his palm."
    "Slowly, their shells cracked open, delicate green shoots emerging like tiny fingers reaching toward the sky. Within seconds, the fragile sprouts twisted and lengthened, their stems strengthening, their leaves unfurling."
    "Niko carefully placed them on the nightstand beside the bed, arranging them in a small clay dish that had been sitting unused."

    dorian "…You're using nature channeling again?"
    niko   "It's not enough that he's breathing. He needs to recover properly."

    "With another wave of his hand, the young plants continued to grow. They bloomed into delicate white blossoms, their petals trembling slightly as if breathing in the room's air."

    niko "These flowers release a mild healing essence. It should help his body recover faster, strengthen his energy flow, and ease any lingering strain on his energy."

    "He reached out and lightly pressed his fingers against the unconscious man's forehead. A soft green glow flickered at the tips of his fingers before dissipating into the young man's skin."
    "The young man shifted slightly, his expression relaxing as if a deep tension had left him. His breathing became more even."

    chung_hee "…"

    niko "Good. He's stabilizing."

    "He adjusted the blankets again, making sure the man was warm but not overheated. Then he sat back with a quiet sigh."

    dorian "You're really thorough with this."
    niko   "… Just being careful."

    "He looked at the man."

    niko "I've seen this before. People pushing themselves past their limits, burning through their energy until there's nothing left. Some never recover."

    "A brief silence stretched between us. Maybe now was a good time to talk to him."

    jump ch5_niko_choices


# =============================================================================
# SECTION 9: LABEL CH5_NIKO_CHOICES — Talking with Niko (Choices)
# =============================================================================

label ch5_niko_choices:

    menu:
        "Thank him for his assistance earlier.":

            dorian "You didn't have to help back there. But you did. So… thanks."
            niko   "Don't mention it. It's my duty."
            dorian "Your duty?"
            niko   "I was a doctor before."
            niko   "Trained for years under some of the best healers in my clan. Medicine was my life."

            "I blinked."

            dorian "A doctor? I figured you had medical experience, but I didn't think you were trained formally."

            "He let out a low chuckle."

            niko   "What, you thought I just had a natural talent for it?"
            dorian "With the way you worked? Yeah, I wouldn't have been surprised."
            niko   "Where I come from, healers aren't just people who stitch wounds and mix herbs. We had to know how to fight too."
            niko   "You can't save lives if you're dead, after all."

            "He smirked slightly. His gaze drifted to his hands."
            "His fingers flexed slightly, and for the first time, I got a clear look at the intricate symbols running along his arm. Runes—etched like ink, wrapping around. They weren't familiar. They weren't decorative."

            dorian "Those runes on your hands… I haven't seen them before."
            niko   "No. They're protective runes. A gift. Or maybe a curse. Depends on who you ask."

            "He turned his hand over, the runes catching the dim light of the room."

            niko "They help me control my shadows."

            "His voice trailed off, and for a brief second, I swore I saw something shift behind him. A flicker of darkness, barely noticeable, curling at the edges of his silhouette like something alive."
            "Then it was gone."

            dorian "Where did you get them?"
            niko   "Hamatame. A village deep in the mountains of the kingdom of Hinami. The Village of Shadows."
            dorian "I see. I haven't been to Hinami before."
            niko   "You should. The beaches are terrific this time of the year."
            dorian "Haha. Maybe. Thanks."

            jump ch5_niko_choices

        "Ask him how he turned into a raven.":

            "I shifted slightly, glancing at him."

            dorian "I've been meaning to ask you this… How—how did you turn into a raven?"

            "He smirked, clearly amused."

            niko   "Didn't I already tell you?"
            dorian "I've seen nature channelers before. Hell, I've fought against them. They can summon beasts, enhance their senses, even morph parts of their bodies. But none of them could fully transform."

            "I crossed my arms."

            dorian "I've seen nature channelers before. Hell, I've fought against them. But none of them could fully transform into animals. At most, they could summon beasts, and some could shift parts of their bodies."

            "I narrowed my eyes."

            dorian "You don't just shift. You become the animal. How?"

            "Niko leaned back, arms resting lazily behind his head."

            niko "It's part of my clan's bloodline ability. Clan Kaibig is… different. We don't just borrow nature's gifts—we embody them."
            niko "It's about becoming. We don't just take on the form. We take on the instincts. The senses. The mind."
            niko "Some in our clan dedicate their lives to mastering every single animal form – hundreds of them. They become the creatures they study, forsaking everything else."

            dorian "What about you?"

            "His smirk faded slightly. He glanced at the unconscious man, then back at me."

            niko "It's not my priority. I have a different calling."

            jump ch5_niko_choices

        "Ask him about our first meeting.":

            "I looked at him, searching his face for some kind of recognition."

            dorian "You said we've met before? Sorry… I don't remember."
            niko   "Tianho. You were with Paladin Cyrus. I was with my brother, Kaito."

            "I blinked. Tianho. That name carried echoes of fire and screaming, the weight of bodies hitting the ground before I could even process what was happening."
            "My mind clawed at the memories, but all I could grasp was the scent of burning flesh and the metallic tang of blood."
            "Elara. My family. Yuxuan. The Emperor of Kyeongjang. Paladin Cyrus. Vasily. Gao. Jiang. King Long Shen. Empress Olympia."
            "I don't recall meeting Niko. Or his brother."

            dorian "Tianho… That was years ago."
            niko   "Kaito wanted to be the translator for the Emperor of Kyeongjang's son. The deaf-mute son of the Emperor."

            "I frowned, trying to piece together the fragments."

            dorian "I'm very sorry. I still don't remember. But I do recall the auditions. Long lines. Hundreds of people waiting for a chance to serve."
            niko   "Yes. The line was massive. Even though we didn't get the chance."
            niko   "Paladin Cyrus had an issue with us. He has an issue with all followers of the Death God."

            "I hesitated before asking."

            dorian "So… Kaito. He's a follower of the Death God too?"

            "Niko's fingers twitched."

            niko   "Yes. But biologically speaking, he's also my brother."
            dorian "So… where is he now?"

            "Niko didn't answer immediately. Instead, he exhaled slowly through his nose. He tightened his fist and stared at the runes etched along his arm."

            niko   "He's with Enoch now. In Xianlun. Paradise."

            "I looked down. The air grew thick, like the room had suddenly shrunk."

            dorian "I'm sorry to hear that."
            niko   "Don't worry about it."

            "A long silence stretched between us. Then, slowly, Niko reached out, his fingers grazing the petals of the flowers surrounding the unconscious man."

            niko "The flowers seem to be working. He just needs rest, and he'll be okay."

            jump ch5_niko_choices

        "Ask him about his faith in the Death God.":
            
            dorian "You're a follower of the death god, right?"

            "Niko looked down at his half-robe."

            niko "Haven't I already told you? But yes. Yes, I am. It's no secret—I'm a member of the Prophets."

            "The moment he said it, my vision blurred. My breathing hitched."

            jump ch5_niko_common


# =============================================================================
# SECTION 10: LABEL CH5_NIKO_COMMON — Niko Faith / Tianho Memory
# =============================================================================

label ch5_niko_common:

    play music ost_niko_faith fadein 1.5        # PLACEHOLDER — somber faith theme

    # [COMMENT: bg_tianho_on_fire — Tianho burning, crowds screaming — memory flash]
    scene bg_tianho_on_fire with flash          # PLACEHOLDER — Tianho on fire (memory)

    "Darkness crept at the edges of my sight, twisting, curling."
    "Tianho."
    "I heard the screams before I saw the fire."

    woman_1 "No! It's the Death God!"
    man_1   "Run! Run for your lives!"

    "And above the burning city, hovering in the smoke-cloaked sky, it loomed. A figure with wings—the death god."

    # [COMMENT: bg_tianho_on_fire — Tianho city ruins, Paladin Cyrus moment]
    "I remember it destroying the castle of Tianho. I couldn't believe it."
    "And then—Paladin Cyrus."
    "I remembered his voice. I remembered the way he lifted his sword, and the way he ran towards the ruins. He had volunteered to face it alone."

    "Paladin Cyrus: Dorian, you evacuate the city. I'll deal with the winged monster."
    dorian  "Cyrus, you can't—"
    "Paladin Cyrus: Listen to me. This city still needs a future, and that future doesn't happen unless someone stops that thing."

    "Tetrad above. He was never seen again."

    # [COMMENT: bg_lab_bedroom — back to spare room]
    scene bg_lab_bedroom with fade              # PLACEHOLDER — lab bedroom

    "Niko took a step closer."

    niko "Are you alright, Dorian?"

    "I exhaled sharply, shaking my head, trying to push past the echoes clawing at my mind. My fists clenched."
    "I looked at him, my voice tight."

    dorian "Why? Why do you worship such a deity?"
    dorian "Surely you were there that night. The night of the tragedy. You saw what happened."

    "A beat of silence. Then another."
    "The flames still danced behind my eyes, the screams still clawed at my ears."

    dorian "Those people… They died because of your god."

    "Niko didn't speak right away. Instead, he stepped forward and placed a firm hand on my shoulder."

    niko "You might wanna sit down for this, Dorian."

    "I resisted at first. My blood still burned, my hands still trembled with the weight of old memories."
    "Reluctantly, I sank onto the chair."
    "He reached into a small folded pouch at his side and pulled out a worn pamphlet."

    dorian "These are… lovingly made. Did you make these?"
    niko   "No. These were drawn by the orphans we took in."
    niko   "Children who lost everything—their homes, their families, their past. Me, Kaito and a few other Prophets gave them shelter, a place to start again."
    niko   "Me and my fellow brothers in Enoch keep one of these just in case we have the opportunity to share our faith."

    "There's a certain purity and warmth in Niko's beliefs that is undeniably endearing. If only his faith were centered around a different deity, like the Tetrad for example, and not the one associated with the events in Tianho, I would have wholeheartedly embraced and admired his devotion."

    dorian "There are lots of drawings here. What's this have to do with the death god?"
    niko   "Well, as we all know, the death god is not a static entity but is reincarnated again and again, much like the cycle of life and death it oversees."

    "I ran a thumb over the painted pages, my chest still tight."

    dorian "So, you worship all of the reincarnations of the death gods. Not just Enoch?"
    niko   "Precisely. We worship the death god as an entity. However, the most prominent reincarnation of the death god is Enoch of Mjoll."
    niko   "Many historians agree that Enoch was the cause of the many changes in Ena: the downfall of the civilization of Kyeongjang, the fall of the tyrant king in Mjoll, the disappearance of the Tetrad gods and the immortal dragons, the abolishment of slavery in the Centennial Isles, and the list goes on."
    niko   "He shows the capacity of mankind. He may be a god, but he is also human. Both capable of doing good, and bad. Light and dark. Life and death."
    dorian "I appreciate your explanation about Enoch, but what does this have to do with the death god not being related to the incident in Tianho?"
    niko   "In Enoch's final moments, as he lay on his dying bed, he made a solemn vow to his best friend. He swore that in his next lives, he would do everything within his power to right the wrongs he had committed while he was alive."
    niko   "In response to Enoch's oath, his best friend swore a solemn promise of his own. He pledged to seek out the future incarnations of the death gods and guide them toward a path of greater benevolence and good."
    niko   "And thus, from those ancient promises, the Prophets of the Death God were founded. A dedicated group of individuals who have taken it upon themselves to seek out and guide the incarnations of the death god, nurturing their potential for benevolence and compassion."
    niko   "I am proud to be one of those people. This is my calling."
    dorian "Interesting. How many death gods were influenced by the prophets?"
    niko   "The first sighting we had was five years ago on Tianho. Our brothers tried to help him, but alas, he was already killed."

    "Five years ago?!"

    dorian "Five years ago? That's... surprising. I thought you said that the Prophets were founded four centuries ago. I would have expected the prophets to have encountered and influenced multiple death gods by now."
    niko   "We were. The Prophets have transitioned into a charity organization after the first century it was established. Many of us have already believed that death god's work is complete."
    niko   "So, you can imagine the excitement all of us prophets have when the sighting has been made five years ago."

    "I could imagine it, all right."
    "Four hundred years of waiting, of fading purpose—then suddenly, proof. A reason to move."

    dorian "And now you're investigating that sighting. Because you don't believe the creature that destroyed Tianho was the Death God."
    niko   "Exactly."
    dorian "Have you gotten any leads?"

    "Niko shook his head, frustration evident in the way his fingers curled slightly."

    niko "None. We've searched outside of Tianho. We scoured Gale, Hinami, the borderlands. But there's nothing. No traces. No patterns."
    niko "Something isn't right, Dorian. We're missing something. We just don't know what."

    "Before I could respond, a familiar whirring sound filled the room."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    "The little machine rolled in with a tray, a neat pitcher of warm water and a stack of cups balanced with near-perfect precision. Its screen flickered, displaying an animated image of water being poured."

    roboto "Beep-boop! R-r-r-Roboto has arrived with water delivery!"
    niko   "Roboto, lower your voice."

    "The robot's screen immediately switched to a large 'shhh' icon, accompanied by the sound of static mimicking a whisper."

    roboto "Activating silent mode… Shhhh…."

    "It turned back to us, its voice now hushed."

    roboto "H-H-Here is your water, sir. Warm, just as you've requested."
    niko   "Thank you. Just place it beside me, please."

    "It wobbled forward, carefully placing the tray on the small bedside table. The screen changed again, now showing a satisfied-looking pitcher giving a thumbs-up."

    roboto "Mission accomplished! Would you like Roboto to stay and provide additional hydration support?"
    dorian "Hydration support?"
    roboto "Roboto can monitor water levels! Fluff pillows! Tuck in patients! Or… or… tell a bedtime story!"
    dorian "Stories, huh? Interesting."

    "Niko yawned, stretching his arms."

    niko "You can stay if you want. Nothing else to do but keep watch."

    "Roboto's screen changed again, now displaying a small clock icon."

    roboto "Oh! Speaking of time—it's almost dinner! Master Yuxuan is currently looking for you in the living room, Sir Dorian."

    "I glanced at Niko, who was already sinking back into his chair, stretching his legs out with a quiet sigh."

    niko "Go ahead. I'll keep watch here."

    "I gave him a nod before stepping out, leaving Roboto standing beside the bed, its screen flickering between a neutral expression and a 'standby mode' prompt."

    roboto "Please g-g-g-g-go ahead and take a nap, sir Niko. If the patient exhibits irregular breathing patterns, Roboto shall alert you immediately!"
    roboto "Would you like me to turn off the lights?"
    niko   "Sure. Thanks."

    jump ch5_living_room


# =============================================================================
# SECTION 11: LABEL CH5_LIVING_ROOM — Elias and Tim
# =============================================================================

label ch5_living_room:

    # [COMMENT: bg_yuxuan_lab — lab main room, Elias and Tim running in circles]
    scene bg_yuxuan_lab with dissolve           # PLACEHOLDER — lab main room

    "As I stepped into the main area, the sound of playful giggles filled the air. Laughter bouncing off the walls like sunlight filtering through an open window."
    "Elias was running in circles, his little legs pumping as fast as they could carry him. Close behind, a small boy with messy green hair and oversized glasses was in hot pursuit."

    tim   "You know I'm gonna catch you, Elias!"

    "Elias let out an exaggerated gasp, clutching his stuffed bear, Tedda, against his chest."

    elias "Ahh! Haha! Hurry, Tedda! Tim might catch us!"
    "Tedda: …"

    "The kid pushed his glasses up the bridge of his nose."

    tim   "Hmm… If I analyze the velocity of his movements and factor in his diminishing stamina…"
    tim   "A-ha! I have predicted your trajectory!"

    "With sudden speed, Tim lunged, tapping Elias on the shoulder."

    elias "Hahaha! Aaaaahhh! He got me!"
    tim   "Mathematical precision. You stood no chance."

    "Elias tilted his head."

    elias "I dunno what that means, but that was fun!"
    tim   "Let's have a rematch! I shall implement new strategies to maintain my superior—"

    weng  "Tim? Tim! By the stars, Tim… I'm calling you."

    "An elderly woman in a crisp white uniform strode toward them, her silver-streaked hair pulled into a neat bun."
    "The little boy let out a small grunt, clearly reluctant to stop playing. He turned his head slightly, brows furrowed."

    tim  "But we're busy, Miss Weng…"
    weng "Tim, be careful. You might break something again! I don't want a repeat of your Roboto incident."

    "His shoulders slumped in defeat."

    tim "Yes, Miss Weng… Ugh…"

    "I glanced at Elias, who was still bouncing on his feet, too absorbed in the game to notice me watching. A small smile tugged at my lips."
    "It was rare—seeing him like this. Seeing him play with someone other than Tedda. Someone real. Someone his age."

    "I softened my voice."

    dorian "Elias, are you having fun?"

    "No response. He was too caught up in his play, bouncing excitedly on his feet."

    elias "Tim, should we continue playing tag?"
    tim   "Sorry, Elias. But Miss Weng doesn't want me to play tag anymore."
    elias "Aww… But… But—"
    tim   "That's okay! We can still tell stories!"
    elias "Oh… Okay!"
    tim   "I'll start! There's a huge library here! And my favorite story is the one about the kumiho and—"

    "Yuxuan approached me, his usual easygoing smirk in place. He gestured toward the green-haired kid."

    yuxuan "So that's Tim. The one playing with Elias."
    dorian "He and Elias are getting along well. I'm happy."
    yuxuan "It's good for him. Kids need company."

    "He then turned to the elderly woman, motioning toward me."

    yuxuan "Soooo, this is Cai Weng. Miss Weng, this is Dorian Burnham."
    yuxuan "Weng is a true gem. She's my personal assistant, my cook, my all-rounder here at this laboratory."
    weng   "Oh, you're too kind, Master Yuxuan. I'm just doing my job. It's a pleasure to be of service here. Is that right, Tim?"

    "Tim was still too focused on Elias. Elias giggles and waves Tedda around."

    weng "…*sighs* Kids…"

    "She turned to me with a polite nod."

    weng   "Pleasure to meet you, Sir Burnham."
    dorian "Likewise, Miss Weng."

    "I chuckled under my breath, watching Elias laugh as he exchanged stories with Tim."
    "Yuxuan told me that Svante, the aldorith who realized who I was, was placed in the storage room."
    "Isn't that dangerous? Svante's a metal channeler, as we've seen a while ago. He might turn on us."
    "Miss Weng tells me that Svante's been handcuffed with Jinyan steel which suppresses channeling."

    yuxuan "By the way, Svante—the Aldorith who figured out who you were? I had him placed in the storage room."

    "I turned to him sharply."

    dorian "Isn't that dangerous? He's a metal channeler. We saw what he could do earlier. He might turn on us."

    "Before Yuxuan could answer, Weng let out a small chuckle, shaking her head."

    weng "No need to worry, Sir Burnham. The aldorith's been properly restrained."

    "She gestured toward her wrist, mimicking the snap of cuffs."

    weng "We restrained him with Jinyan Steel—he shouldn't be a problem now."

    "That caught my attention. Jinyan Steel—extremely rare, ridiculously expensive. I'd only used it once before, back when I had to subdue a particularly powerful channeler. The material didn't just restrain—it completely suppressed channeling."
    "I'm not surprised Yuxuan has some here, given his wealth and influence."

    dorian "And he's just… sitting in there?"
    yuxuan "Fast asleep. Thanks to the Cheng Industries' Sleeping Powder."

    "Weng's gaze flickered toward the clock hanging on the wall."

    weng   "Speaking of sleep, it's already past dinner time… No wonder I'm feeling lightheaded."
    weng   "I need to hurry. You must be hungry, Master Yuxuan. Sir Burnham."
    dorian "Just a little."

    "Right on cue, my stomach growled. Loudly."
    "Yuxuan shot me a look of pure amusement."

    yuxuan "Don't worry, Dorian. We'll have you fed up in no time."

    "I sighed, rubbing the back of my neck."

    dorian "I almost forgot. I haven't eaten anything all day."

    "And then it hit me—Elias."
    "I glanced toward him, still caught up in his conversation with Tim. The two of them were huddled close, exchanging animated whispers about something I couldn't hear."

    dorian "Elias is probably starving too…"

    "Yuxuan waved a hand dismissively."

    yuxuan "Oh, don't worry about him. I made sure he was well-fed while you were off handling, you know… family matters at the memorial gravesite."
    dorian "Thanks, Yu. What did you feed him?"
    yuxuan "Umm… Tianho chocolates. Took him to a booth. It was owned by Cheng Industries so I told my employee to give him as much as he wanted."

    "I blinked."

    dorian "How many did he eat?"

    "I stared at him, and a sense of deep, immediate regret settled in."

    yuxuan "I… uh… got caught up. Associates called. Kinda lost track. *clears throat* Sorry?"

    "I sighed."

    dorian "Tetrad, help me."
    yuxuan "Hey, he liked it! Kept him happy while you were gone."

    "I looked back at Elias, who was still bouncing on his feet, chattering away with Tim, his energy seemingly endless."
    "So that's why he was so hyper."
    "I let out a slow breath, pinching the bridge of my nose. Yuxuan clapped a hand on my shoulder."

    yuxuan "Relax. He'll crash eventually. Maybe after dinner. Or maybe at midnight."

    "Weng approached us again, wiping her hands on her apron."

    weng "What do you want, sir?"

    "She took out a small notebook from her side pocket at her white dress."
    "I gave her a confused look. I look at Yuxuan, who smiled and put his arm around me."

    yuxuan "She's asking about our food, Dorian. You already know what I want, Miss Weng."
    weng   "Of course. I wouldn't want Master Yuxuan being denied his favorite dragonfire curry."
    dorian "Tianho's Dragonfire Curry?"
    yuxuan "Spicy, bold, and delicious!"
    weng   "Suiting an amazing inventor such as yourself, Master Yuxuan! You're truly incredible!"

    "I watched as she showered him with praise, her words flowing like an endless stream. I smiled awkwardly."

    yuxuan "Thank you so much, Miss Weng."
    weng   "A man of vision! An inspiration to the people of Tianho! The greatest inventor in the kingdom! The—"

    "Weng paused, looking at me."

    weng "Ah, apologies, Sir Burnham. I can make other things too, of course. I'm well-versed in the cuisines of all five kingdoms—Tianho, Gale, Hinami, Mjoll, and the Centennial Isles."
    weng "Just name any dish. If we have the ingredients, I'm sure I can cook it for you."
    weng "And if we don't have the ingredients, well I'll just buy it from the market at the Tianho city proper. I don't mind. It's directly up ground from here. There's still time before it closes."

    "I rubbed the back of my neck."
    "Honestly, I wasn't picky. I'd eat just about anything. But maybe I should choose a dish from one of the kingdoms."

    weng "Don't underestimate the power of food, Sir Burnham. They say you can visit a place just by tasting its dishes."

    "Her eyes gleamed with enthusiasm."

    weng "And I believe that's true."

    "She leaned forward slightly."

    weng "So, Sir Burnham, what cuisine are you in the mood for?"

    jump ch5_food_choice


# =============================================================================
# SECTION 12: LABEL CH5_STORAGE_ROOM — Svante Interrogation
# =============================================================================

label ch5_storage_room:
    stop music fadeout 1.5
    # [COMMENT: bg_lab_storage — dim storage room, single candle, cold stone]
    scene bg_lab_storage with dissolve          # PLACEHOLDER — lab storage room

    play music ost_svante_talk fadein 1.5       # PLACEHOLDER — low tension theme

    "I stepped into the storage room, my movements silent against the cold stone floor. The dim flicker of a single candle cast long shadows across the walls, stretching and shifting with the flame's uncertain dance."
    "Unlike the other rooms, the air was stale, thick with dust and the faint scent of damp stone."
    "Then I heard it."
    "A voice—low, trembling—whispering desperate words into the dark."

    svante "Mighty Enoch… Please… *tears* Your servant is afraid…"

    "I stood still, just inside the doorway. He hadn't noticed me. Not yet."

    svante "I know I have strayed, I know I have sinned... I never meant to question Father. I never meant to doubt him."

    "He paused, sniffling."

    svante "I— I betrayed our sacred law. I know I should never have doubted Father... I know my place. But… Kristin…"
    svante "But… what if…"
    svante "What if Kristin was right all along?"

    "He swallowed hard, his words now coming in ragged, pleading bursts."

    svante "My Lord Enoch, please... *crying* Please don't abandon me. Not now, not when the monster is near."
    svante "My mother needs me… She's the only family I have left, my Lord. Please help me…"
    svante "I… I don't know what to do anymore. I'm so sorry. I feel so lost and broken. Please, mighty Enoch, show me mercy."

    "His fingers twitched uselessly, bound and helpless against the wall. The sheen of Jinshen steel caught the dim candlelight, the cuffs glinting like an executioner's blade. I recognized them instantly."
    "Good. That way, I wouldn't have to worry about his channeling."
    "I took a single step forward."
    "His breath hitched. His head snapped up so fast I thought he'd hurt himself."

    svante "No… No, no, no… Please—please, no…"
    dorian "Calm down. I just want to ask you a few things."
    svante "Sir… I beg you. Please let me go! *crying* I have a mother! She's sick. She's the only family that I have left!"
    svante "No… No, no, no… Don't hurt me! I beg you! Please—please, no—"

    "I heard his stomach rumble."

    dorian "You must be starving. Here, I just need to—"
    svante "I… Is that it, sir? I-If you wish to spare me, Please, you don't have to feed me."
    svante "Please. I'll eat morsels from the garbage if I have to. Just please let me live!"

    "I rolled my eyes."

    dorian "ARE YOU GOING TO CALM DOWN OR NOT?!"

    "Silence. He stopped struggling. But I can see him trembling a bit."

    svante "*crying*"
    dorian "No one needs to die today. I just need to ask you a few questions. Calm down."
    svante "Y-Yes, sir…"

    "I took a deep breath."

    dorian "Let's start with the obvious. Why does Mjoll want the man that we saved dead?"

    "Svante hesitated, his fingers twitching against the cuffs. His gaze flickered toward the floor, avoiding mine."

    svante "I—I don't know everything, sir. I swear it. But..."
    svante "Father said that the man we were supposed to kill… cursed him."
    dorian "Cursed him?"

    "My eyes widened."

    svante "That's what he told us. That the man— he was some kind of heretic and is an enemy of Mjoll."
    dorian "And you believe him?"

    "A brief silence erupted between us."

    svante "No… I think he's… lying…"
    svante "Because he's lied before… with the Elias incident. He told everyone that it was Elias who killed his own mother."
    svante "My sister Kristin… she accompanied the two prophets as they examined Queen Ekaterina's body."
    svante "The fingerprints on the knife belonged to Father himself. But still, he tried to pin the blame on Elias..."
    svante "I was the only person my sister talked to about this. At first, I got mad at her for doubting Father but after her death, I… I started to wonder."
    svante "What if she was right?"
    dorian "So you think the man you were sent to kill today… was innocent?"
    svante "Y-Yes, sir."

    "I nodded. That was brave of him to say. For an aldorith, it would have been a death sentence."

    svante "Do you have any more questions, sir?"

    jump ch5_svante_choices


# =============================================================================
# SECTION 13: LABEL CH5_SVANTE_CHOICES — Questioning Svante
# =============================================================================

label ch5_svante_choices:

    menu:

        "Why were you the only aldorith spared by this man?":

            dorian "When I saw the battlefield, the bodies of your brothers and sisters were scattered around him. Yet, you… you were still alive."
            dorian "How did he know you were on his side?"
            svante "I… defended him. He saw it, surely."
            svante "I tried to explain to our commanders Tian Xun, to Lady Aoi… to all of them… I told them that something felt wrong. That I wasn't sure this man deserved to die."
            svante "But Tian Xun and Lady Aoi called me a traitor."
            svante "Then… he attacked. Almost everyone who came close to him died. They didn't expect him to be that powerful. No one did."

            "I studied him carefully. He wasn't lying. The tremor in his voice, the way his body tensed at the memory—it was all genuine."

            dorian "What about your commanders? Tell me about them."
            svante "Oh them? Tian Xun was um…"

            "Svante shifted, adjusting his wrists against the cuffs. He winced slightly."

            svante "Sorry. A little bit itchy."
            svante "Tian Xun was a loose cannon. He's obsessed with bombs. They say he grew up in Tianho in an impoverished family, even though his father worked for the King."
            dorian "You mean King Long Shen, the late king of Tianho?"

            "Svante frowned a little bit."

            svante "I think so. Sorry, sir. I'm not familiar with the other kings. I only know Father."
            dorian "And the last one? Lady Aoi?"
            svante "Oh! Believe it or not, Lady Aoi used to be a songstress from Hinami."
            dorian "That's not what I asked."

            "Svante flinched."

            svante "O-Oh! Sorry, sir! She—uh—she's a powerful water channeler from Hinami. She just… showed up at the palace one day, gave a demonstration of her power."
            svante "Father was impressed. So impressed that he made her commander of an entire battalion of Aldoriths."
            dorian "You don't sound convinced."
            svante "Just between you and me, sir… word among my brothers is that Father only sees Queen Ekaterina in her."
            dorian "Yeah…. I can see that."

            jump ch5_svante_choices

        "Who are you?":

            dorian "What's your name?"

            "Svante blinked at me, looking genuinely confused—almost as if the question was unnecessary."

            svante "Svante, sir. Svante Nordstrom."

            "I tilted my head slightly."

            dorian "Nordstrom. As in Gustav Nordstrom. You took on the king's last name. I'm surprised he even let you do that."
            svante "You're not wrong, sir. Usually, us aldoriths carry the last name of their mothers."
            svante "M-Mother received special permission from Father, sir."
            dorian "Really? How come?"
            svante "Mother was at the top of her career when she gave birth to me. She was a songstress. Father was really into her back then."
            dorian "What about your sister?"
            svante "Kristin…"

            "He paused, his hands twitching against the cuffs."

            svante "She only carried my mother's name."

            jump ch5_svante_choices

        "How do you know me?":

            dorian "How did you recognize me?"

            "He shifted slightly, as if trying to find the right words."

            svante "I… I actually didn't at first, sir."
            dorian "How come?"

            "Svante's gaze flickered towards me. At my hair, my clothes, everything."

            svante "Well, your hair, sir. It's different. And your clothes."

            "He bit his lip, hesitating."

            svante "Elias was also wearing girl's clothes so I didn't recognize him."
            dorian "But then you figured it out."
            svante "It wasn't until I heard you call Elias' name that I put all the pieces together."
            dorian "You called me a different name as well. Why?"
            svante "The Massacrer of Mjoll. They named you that after you… you—"

            "His breathing quickened, and his eyes darted toward mine—fearful, desperate. A long silence erupted."

            dorian "I won't hurt you. I promise."
            svante "O-Okay, sir."

            jump ch5_svante_choices

        "That's all for now.":

            dorian "That's all. I don't have any more questions for you."

            "I exhaled, stepping back, watching him in the dim light. His breathing had steadied, but his posture remained rigid, his body still caught between fear and exhaustion."

            svante "Sir Dorian…"
            svante "What would you have done? If you were me?"

            "I narrowed my eyes."

            dorian "If I were you?"

            "He nodded. His violet eyes met mine, pleading, uncertain. No malice. No scheming. Just a hurt and tormented man."

            dorian "I wouldn't let doubt rule me. I would decide. I'd choose a side. And stick with it."

            "He swallowed, nodding slowly."

            jump ch5_svante_common


# =============================================================================
# SECTION 14: LABEL CH5_SVANTE_COMMON — Svante Freed
# =============================================================================

label ch5_svante_common:

    "A pause. I studied him. The way his shoulders slumped in exhaustion, the way his fingers twitched, the way he spoke—like a man who had already lost everything and was now only waiting for the final blow."
    "I'd seen men like him before. Broken. But not beyond repair."
    "I felt that he wasn't a threat. Not now."
    "I reached into my pocket, fingers brushing over the cold metal key Weng had given me."

    dorian "Can I trust you?"

    "His head shot up."

    svante "Trust me with what?"

    "I held the key up between us, letting it glint in the dim light."

    dorian "Swear to me—by your god—that you will never harm my family."
    svante "I… I wasn't planning to, but…. I swear by Enoch that I will never harm you or your family."

    "Then, without breaking eye contact, I stepped forward and reached for his cuffs."
    "The metal was cool beneath my fingers as I slid the key into the lock. A sharp click echoed in the small room."
    "The heavy Jinshen steel fell away from his wrists."
    "Svante inhaled sharply, his arms dropping limply to his sides. He stared at his freed hands for a moment."

    dorian "Don't make me regret this."
    svante "I won't, sir."

    jump ch5_dinner_setup


# =============================================================================
# SECTION 15: LABEL CH5_DINNER_SETUP — Before Dinner / Tim and Elias
# =============================================================================

label ch5_dinner_setup:

    # [COMMENT: bg_yuxuan_lab — lab main room]
    scene bg_yuxuan_lab with dissolve           # PLACEHOLDER — lab main room

    "As Svante and I stepped into the main room, the warm scent of spices and simmering broth filled the air. The rich aroma of slow-cooked meats and fragrant herbs curled through the space."
    "Weng was still by the stove, stirring a pot with practiced ease. The moment her gaze landed on Svante, she set down her spoon and wiped her hands on her apron, stepping forward with a welcoming smile."

    weng "Ah, you're awake! That's good to see. You must be starving."
    weng "Proper introductions are in order. I'm Cai Weng, Master Yuxuan's assistant. It's a pleasure to meet you, young man."

    "He blinked, as if taken aback by the kindness in her voice. He looked at me, and then back to her."

    svante "I… Yes. Thank you, m-mam. My name's Svante. Svante Nordstrom. I-I'm so glad to meet you."
    weng   "Dinner is ready. Please have a seat, gentlemen and I'll be serving you up the food."
    weng   "I hope you like haugensoppa. I made it just for you."
    svante "Haugensoppa? You… know Mjoll cuisine?"
    weng   "Oh, I've had my fair share of travelers from the North. You lot love your root vegetable stews."

    "Svante opened his mouth, perhaps to ask more, but before he could reply—"
    "A sudden burst of tiny, hurried footsteps came from the hallway."

    tim   "Elias, you're going too slow! Dinner's about to start!"
    elias "I'm carrying Tedda and my book! It's a little heavy!"

    "Tim marched into the room first, his small arms wrapped around a thick, leather-bound book far too large for someone his age. The title was embossed in gold: 'Tianho's Ancient Dynasties.'"
    "Elias followed closely behind, but instead of a weighty tome, he proudly clutched a children's coloring book, its cover splashed with bright rainbows and smiling animals. Perched lazily on top was Tedda."
    "Tim sighed dramatically, adjusting his glasses."

    tim   "Elias, I told you to pick something educational."
    elias "This one had colors, Tim! It's got wainbows! They're edumecational."
    tim   "Rainbows are not educational, Elias."

    "Elias gasped as he spotted Svante. His eyes widened with delight."

    elias "Look! It's the pink haired guy! He's awake!"
    tim   "Huh? He's not pink haired, Elias! It's violet!"
    elias "Tim, pink and violet are the same. Right, Tedda?"
    "Tedda: …"
    tim   "What?! They're completely different colors. Right, Miss Weng?"
    svante "Actually… my hair is violet. It's not really pink."
    tim   "HA! It's violet! See, Elias? See? I win! HAHA—"
    weng  "Tim, quit it. You're embarrassing me in front of Sir Burnham and Sir Nordstrom. Now be a good boy and help me serve dinner."

    "Tim huffed but did as he was told, setting his book down carefully before moving to grab a stack of bowls."

    jump ch5_nap


# =============================================================================
# SECTION 16: LABEL CH5_FOOD_CHOICE — Cuisine Selection
# =============================================================================
# This section is reached earlier in ch5_living_room.
# It jumps back here before the nap section.
# =============================================================================

label ch5_food_choice:

    play music ost_cheng_lab fadein 1.0         # PLACEHOLDER — warm lab theme

    menu:

        "A dish from Tianho.":
            $ ch5_food_choice = "tianho"
            $ yuxuan_affection += 1             # +1 Yuxuan affection

            "Tianho."
            "I remembered when Elara and I took the kids there—before everything. Before the tragedy."
            "It was beautiful once. Its people, its culture, its heart."
            "And then there was Yuxuan."
            "He always told me he'd never forget that I saved him that day, but I don't remember a thing. Maybe I didn't want to. Tianho was a place I tried to forget."
            "But Yuxuan… he's always been there for me."

            "I turned to him, offering a small smile."

            dorian "Thank you."

            "A faint blush dusted Yuxuan's face."

            yuxuan "H-huh?"

            "I glanced back at Weng."

            dorian "I'll go with something from Tianho, Miss Weng."

            "She clapped her hands together, eyes lighting up."

            weng "A fine choice, sir Burnham! I know just the thing!"

            "She jotted something down on her notepad, nodding to herself."

            weng "I'll make sure it captures the beauty of Tianho."

        "A dish from Gale.":
            $ ch5_food_choice = "gale"
            $ chunghee_affection += 1           # +1 Chung-hee interest (Gale / Kyeongjang curiosity)

            "Gale. My home."
            "The Empire of Gale was a land of plenty, its cuisine just as vast and rich."
            "I hadn't had a proper Galean meal since—since Elara and I took the kids to that banquet."
            "It was extravagant, hosted by Empress Olympia herself. That night, she made a grand announcement—the Emperor of Kyeongjang would be visiting."
            "The people had erupted with joy."
            "Kyeongjang."
            "And now, the unconscious man we had just saved… he was from Kyeongjang."
            "His mind channeling, his appearance… everything."
            "Something about him. Just made me very curious."
            "I shook the thought away. No use overthinking. Once he wakes up, we'll hopefully get to know him."

            dorian "I'll have something from Gale. My homeland."

            "Weng's eyes widened."

            weng "You're from the Empire of Gale, Sir Burnham?"

            "I nodded. She practically gushed."

            weng "Oh, I've been to Gale before! With my lover! The sights—oh, the sights!"

            "She twirled her pen between her fingers, a nostalgic smile crossing her lips."

            weng "Ah… then you'll need something fit for a nobleman. I have just the thing, Sir Burnham!"

        "A dish from Hinami.":
            $ ch5_food_choice = "hinami"
            $ niko_affection += 1               # +1 Niko affection

            "Hinami. The Kingdom of Water and Shadow Channelers."
            "I had plenty of friends from Hinami. When I was a Paladin for the Empress of Gale, I had the honor of meeting King Tatsuya Fujiwara during his state visit."
            "Familiar—yet, I'd never actually been."
            "Niko came to mind. Hinami was his home."
            "Hamatame Village, specifically."
            "The way he moved, the way he carried himself—his grace, his skill. Watching him heal the unconscious man had been nothing short of mesmerizing."
            "How he used his shadows to protect us from the Mjoll soldiers earlier."

            dorian "I think I'll have something from Hinami."

            "Weng's eyes gleamed with excitement."

            weng "The Island Kingdom of Hinami—oh! Such beautiful beaches!"

            "She tapped her notepad, thinking."

            weng "The fish there? Top notch. There's even an elusive species called Aokibane—very rare!"

            "She chuckled to herself."

            weng "And of course, there's the famous Ganderbilt—an exquisite delicacy."

            "She snapped her fingers."

            weng "Great choice, Sir Burnham. Something warm and comforting, then."

        "A dish from Mjoll.":
            $ ch5_food_choice = "mjoll"
            $ svante_affection += 1             # +1 Svante affection

            "Mjoll."
            "Elara's hometown. I lived there for—what? Four, five years? I'd lost count."
            "King Gustav. Queen Ekaterina. Elias. Vasily."
            "Tetrad above, Vasily."
            "I can't believe I killed him. Vasily. My friend."
            "Not only him. But an entire battalion of aldoriths and soldiers. It was a blur. But I can hear the aldoriths cries and screams."
            "Not just him. An entire battalion of Aldoriths and soldiers. It was a blur, but I could still hear it."
            "The screams."
            "And now… Svante."
            "I'd seen the way he looked at me. He was afraid. I don't want him to be. I—"

            weng "Sir Dorian? Are you having trouble choosing?"

            "I blinked, shaking the memories away."

            dorian "Oh, uh. Sorry. I'd like something from Mjoll."

            "She tilted her head slightly, observing me."

            weng "The snowy kingdom. I see…"

            yuxuan "I remember you telling me that you've been there before, Miss Weng."

            "A brief silence. She looked down, her fingers tightening around her pen."

            weng "Yes… yes, I have."

            "Then, just as quickly, she smiled and scribbled on her notepad."

            weng "A hearty meal, then. Something warm, something rich."

            "She glanced at me, her smile reassuring."

            weng "Something that will keep the cold away."

    jump ch5_common

# =============================================================================
# SECTION 16B: LABEL CH5_COMMON — Weng, Tim & Elias Dinner Scene
# =============================================================================
label ch5_common:
    # [COMMENT: bg_yuxuan_kitchen or bg_yuxuan_lab — Weng approaches the toddlers]
    scene bg_yuxuan_lab with dissolve           # PLACEHOLDER — lab/common area

    "Weng then approached the two toddlers, smoothing out the wrinkles in her apron."

    weng "Alright, little ones. What would you like for dinner?"

    "Tim adjusted his tiny glasses, crossing his arms."

    tim "Braised Tianho fish with fermented black beans. Steamed tofu with ginger. And a side of sautéed bok choy with garlic."

    "I blinked."

    dorian "What kind of five-year-old asks for that?"
    yuxuan "Hahaha! That's Tim. He has quite the refined palate, just like me and Weng."
    "Tim pushed his glasses up the bridge of his nose, utterly serious."
    tim "Proper nutrition is essential for cognitive development of toddlers like myself. My brain requires high-quality fuel."
    "Meanwhile, Elias was bouncing on his heels, practically vibrating with excitement."
    elias "Ooh! I want choco—"
    "I cut him off before he could even finish."
    dorian "Chicken. Rice. Soup. And lots of vegetables. He'll have that."
    "Elias's little face scrunched up into a dramatic pout, his lower lip jutting out."
    elias "But daddy—"
    "I gave him The Look."
    dorian "No, Elias. You already ate enough chocolate today. You need your vitamins."
    "Elias squirmed. His little hands clutched Tedda, his stuffed bear, like the poor toy could somehow convince me to change my mind."
    
    tim "Vegetables are good for you, Elias."
    elias "No, they're not… They're icky!"
    tim "Yes, they are. They contain essential vitamins and minerals that help you grow stronger and support brain function. You want to be smart like me, don't you?"
    elias "Fiiineeee…"
    weng "Alright then, why don't you two go play while I prepare dinner?"
    tim "Master Yuxuan, can Elias and I go to the library?"
    yuxuan "Always, Tim. Keep on reading, green-haired buddy."

    "Tim's face lit up. He turned to Elias, taking his hand like a tiny professor guiding his student."

    tim "Come with me. I'll show you the library."

    "Elias blinked, surprised."

    tim "I'll show you my favorite books! Let's read together! Oh, you're gonna love the legend of the kumiho!"
    elias "Let's go! Ooh! Do they have pictures and flowers there?"
    weng "Tim… Make sure to be back once dinner is finished, okay? It's a challenge to get you away from those books once you start. Be mindful of little Elias with you."

    "Yuxuan and I watched them go, both of us shaking our heads in amusement."

    yuxuan "They make quite the pair huh, Dorian? They just met and they're acting like they've known each other for a long time!"
    dorian "No kidding."

    "Weng chuckled as she headed toward the kitchen."

    weng "You two, just sit tight and wait. Dinner will be ready soon."

    jump ch5_nap

# =============================================================================
# SECTION 17: LABEL CH5_NAP — Dorian Naps Before Dinner
# =============================================================================
label ch5_nap:

    # [COMMENT: bg_yuxuan_lab_dim — lab with dimmed lights]
    scene bg_yuxuan_lab_dim with dissolve       # PLACEHOLDER — lab dimmed lights

    "I nodded, stretching out on the sofa."

    yuxuan "Gonna take a nap?"
    dorian "Just for a bit."

    "As soon as my head hit the cushion, exhaustion washed over me. It's been a long day. I put a pillow on top of my face."
    "And within moments, I was out."

    "I must have slept for an hour or two."
    "I stretched, still groggy from my nap, the muffled sound of rain aboveground blending with the quiet hum of Yuxuan's underground laboratory."
    "The dim lighting cast long shadows, and the scent of something rich and savory filled the air."
    "My stomach rumbled."

    weng "Sir Burnham? You woke up early. Thought you'd sleep until dinner was ready."

    "She stood near the stove, stirring a pot, the warmth from the fire flickering across her face."

    dorian "Did I?"

    "I could still feel the weight of sleep clinging to me."

    weng   "Master Yuxuan's in his study. Said he had work to do."

    "I nodded, rubbing the back of my neck as the scent of the stew—something hearty and rich—filled my nostrils."

    dorian "Smells good, Miss Weng."
    weng   "You're too kind, Sir Burnham. You'll get your share soon enough. But—"

    "She wiped her hands on her apron and approached me, lowering her voice slightly."

    weng "Remember the Aldorith? Svante?"
    dorian "Yeah. What about him?"

    "She glanced toward the hallway leading to the storage room."

    weng "I took the liberty of preparing something from Mjoll for him. His food's almost ready. No use letting him starve."

    "She reached into her pocket and pulled out a small, cold iron key, pressing it into my palm."

    weng "You're the one who he has a problem with. I was thinking you should be the one to check on him. See if he's woken up. Maybe talk to him."

    "I looked down at the key. It was simple but sturdy, and heavier than I expected."

    dorian "Is he even awake?"
    weng   "Hard to say. He's been out for a while, but knowing sleeping powder, its effects should have worn off about now."
    dorian "And if he's a threat?"

    "Weng wiped her hands on her apron again."

    weng "Then you'll know what to do, sir Burnham."

    "I nodded. A test. A chance. If Svante didn't prove to be a threat, I could unlock his cuffs. But if he did…"
    "I clenched my jaw and stood up, pocketing the key."

    dorian "I'll see where he stands."

    "Weng nodded in approval before turning back to the stove, resuming her work."

    jump ch5_interrogation

# =============================================================================
# SECTION 17A: LABEL ch5_storage_room interrogation
# =============================================================================
label ch5_interrogation:
    scene bg_lab_storage with dissolve          # PLACEHOLDER — lab storage room
    play music ost_svante_talk fadein 1.5       # PLACEHOLDER — low tension theme
    "I stepped into the storage room, my movements silent against the cold stone floor. The dim flicker of a single candle cast long shadows across the walls, stretching and shifting with the flame's uncertain dance."
    "Unlike the other rooms, the air was stale, thick with dust and the faint scent of damp stone."
    "Then I heard it."
    "A voice—low, trembling—whispering desperate words into the dark."

    svante "Mighty Enoch… Please… {i}*tears*{/i} Your servant is afraid…"

    "I stood still, just inside the doorway. He hadn't noticed me. Not yet."

    svante "I know I have strayed, I know I have sinned... I never meant to question Father. I never meant to doubt him."

    "He paused, sniffling."

    svante "I— I betrayed our sacred law. I know I should never have doubted Father... I know my place. But… Kristin…"
    svante "But… what if…"
    svante "What if Kristin was right all along?"

    "He swallowed hard, his words now coming in ragged, pleading bursts."

    svante "My Lord Enoch, please... {i}*crying*{/i} Please don't abandon me. Not now, not when the monster is near."
    svante "My mother needs me… She's the only family I have left, my Lord. Please help me…"
    svante "I… I don't know what to do anymore. I'm so sorry. I feel so lost and broken. Please, mighty Enoch, show me mercy."

    "His fingers twitched uselessly, bound and helpless against the wall. The sheen of Jinshen steel caught the dim candlelight, the cuffs glinting like an executioner's blade. I recognized them instantly."
    "Good. That way, I wouldn't have to worry about his channeling."
    "I took a single step forward."
    "His breath hitched. His head snapped up so fast I thought he'd hurt himself."

    svante "No… No, no, no… Please—please, no…"
    dorian "Calm down. I just want to ask you a few things."
    svante "Sir… I beg you. Please let me go! {i}*crying*{/i} I have a mother! She's sick. She's the only family that I have left!"
    svante "No… No, no, no… Don't hurt me! I beg you! Please—please, no—"

    "I heard his stomach rumble."
    dorian "You must be starving. Here, I just need to—"
    svante "I… Is that it, sir? I-If you wish to spare me, Please, you don't have to feed me."
    svante "Please. I'll eat morsels from the garbage if I have to. Just please let me live!"

    "I rolled my eyes."

    dorian "ARE YOU GOING TO CALM DOWN OR NOT?!"

    "Silence. He stopped struggling. But I could see him trembling."

    svante "{i}*crying*{/i}"
    dorian "No one needs to die today. I just need to ask you a few questions. Calm down."
    svante "Y-Yes, sir…"

    "I took a deep breath."

    dorian "Let's start with the obvious. Why does Mjoll want the man that we saved dead?"

    "Svante hesitated, his fingers twitching against the cuffs. His gaze flickered toward the floor, avoiding mine."

    svante "I—I don't know everything, sir. I swear it. But..."
    svante "Father said that the man we were supposed to kill… cursed him."
    dorian "Cursed him?"

    "My eyes widened."
    svante "That's what he told us. That the man— he was some kind of heretic and is an enemy of Mjoll."
    dorian "And you believe him?"

    "A brief silence erupted between us."

    svante "No… I think he's… lying…"
    svante "Because he's lied before… with the Elias incident. He told everyone that it was Elias who killed his own mother."
    svante "My sister Kristin… she accompanied the two prophets as they examined Queen Ekaterina's body."
    svante "The fingerprints on the knife belonged to Father himself. But still, he tried to pin the blame on Elias..."
    svante "I was the only person my sister talked to about this. At first, I got mad at her for doubting Father but after her death, I… I started to wonder."
    svante "What if she was right?"
    dorian "So you think the man you were sent to kill today… was innocent?"

    svante "Y-Yes, sir."
    "I nodded. That was brave of him to say. For an aldorith, it would have been a death sentence."
    svante "Do you have any more questions, sir?"

# =============================================================================
# SECTION 17B: INTERROGATION CHOICE MENU
# =============================================================================
label ch5_interrogation_menu:
    menu:
        "Why were you the only aldorith spared by this man?":
            jump ch5_interro_q1
        "Who are you?":
            jump ch5_interro_q2
        "How do you know me?":
            jump ch5_interro_q3
        "That's all for now.":
            jump ch5_interro_q4

# --- Q1 ---
label ch5_interro_q1:
    dorian "When I saw the battlefield, the bodies of your brothers and sisters were scattered around him. Yet, you… you were still alive."
    dorian "How did he know you were on his side?"
    svante "I… defended him. He saw it, surely."
    svante "I tried to explain to our commanders Tian Xun, to Lady Aoi… to all of them… I told them that something felt wrong. That I wasn't sure this man deserved to die."
    svante "But Tian Xun and Lady Aoi called me a traitor."
    svante "Then… he attacked. Almost everyone who came close to him died. They didn't expect him to be that powerful. No one did."

    "I studied him carefully. He wasn't lying. The tremor in his voice, the way his body tensed at the memory—it was all genuine."

    dorian "What about your commanders? Tell me about them."
    svante "Oh them? Tian Xun was um…"

    "Svante shifted, adjusting his wrists against the cuffs. He winced slightly."

    svante "Sorry. A little bit itchy."
    svante "Tian Xun was a loose cannon. He's obsessed with bombs. They say he grew up in Tianho in an impoverished family, even though his father worked for the King."
    dorian "You mean King Long Shen, the late king of Tianho?"

    "Svante frowned a little."

    svante "I think so. Sorry, sir. I'm not familiar with the other kings. I only know Father."
    dorian "And the last one? Lady Aoi?"
    svante "Oh! Believe it or not, Lady Aoi used to be a songstress from Hinami."
    dorian "That's not what I asked."

    "Svante flinched."

    svante "O-Oh! Sorry, sir! She—uh—she's a powerful water channeler from Hinami. She just… showed up at the palace one day, gave a demonstration of her power."
    svante "Father was impressed. So impressed that he made her commander of an entire battalion of Aldoriths."
    dorian "You don't sound convinced."
    svante "Just between you and me, sir… word among my brothers is that Father only sees Queen Ekaterina in her."
    dorian "Yeah…. I can see that."

    jump ch5_interrogation_menu

# --- Q2 ---
label ch5_interro_q2:
    dorian "What's your name?"

    "Svante blinked at me, looking genuinely confused—almost as if the question was unnecessary."

    svante "Svante, sir. Svante Nordstrom."

    "I tilted my head slightly."

    dorian "Nordstrom. As in Gustav Nordstrom. You took on the king's last name. I'm surprised he even let you do that."

    svante "You're not wrong, sir. Usually, us aldoriths carry the last name of their mothers."

    svante "M-Mother received special permission from Father, sir."
    dorian "Really? How come?"
    svante "Mother was at the top of her career when she gave birth to me. She was a songstress. Father was really into her back then."
    dorian "What about your sister?"
    svante "Kristin…"

    "He paused, his hands twitching against the cuffs."

    svante "She only carried my mother's name."

    jump ch5_interrogation_menu

# --- Q3 ---
label ch5_interro_q3:
    dorian "How did you recognize me?"
    "He shifted slightly, as if trying to find the right words."

    svante "I… I actually didn't at first, sir."
    dorian "How come?"
    
    "Svante's gaze flickered toward me. At my hair, my clothes, everything."
    svante "Well, your hair, sir. It's different. And your clothes."
    "He bit his lip, hesitating."
    svante "Elias was also wearing girl's clothes so I didn't recognize him."

    dorian "But then you figured it out."
    svante "It wasn't until I heard you call Elias' name that I put all the pieces together."
    dorian "You called me a different name as well. Why?"
    svante "The Massacrer of Mjoll. They named you that after you… you—"

    "His breathing quickened, and his eyes darted toward mine—fearful, desperate. A long silence erupted."

    dorian "I won't hurt you. I promise."
    svante "O-Okay, sir."

    jump ch5_interrogation_menu

# --- Q4 ---
label ch5_interro_q4:
    dorian "That's all. I don't have any more questions for you."
    "I exhaled, stepping back, watching him in the dim light. His breathing had steadied, but his posture remained rigid, his body still caught between fear and exhaustion."
    svante "Sir Dorian…"
    svante "What would you have done? If you were me?"

    "I narrowed my eyes."

    dorian "If I were you?"

    "He nodded. His violet eyes met mine, pleading, uncertain. No malice. No scheming. Just a hurt and tormented man."

    dorian "I wouldn't let doubt rule me. I would decide. I'd choose a side. And stick with it."

    "He swallowed, nodding slowly."

# =============================================================================
# SECTION 17C: INTERROGATION COMMON — Svante Released
# =============================================================================
label ch5_interro_common:
    "A pause. I studied him. The way his shoulders slumped in exhaustion, the way his fingers twitched, the way he spoke—like a man who had already lost everything and was now only waiting for the final blow."
    "I'd seen men like him before. Broken. But not beyond repair."
    "I felt that he wasn't a threat. Not now."
    "I reached into my pocket, fingers brushing over the cold metal key Weng had given me."

    dorian "Can I trust you?"

    "His head shot up."

    svante "Trust me with what?"

    "I held the key up between us, letting it glint in the dim light."

    dorian "Swear to me—by your god—that you will never harm my family."
    svante "I… I wasn't planning to, but…. I swear by Enoch that I will never harm you or your family."

    "Then, without breaking eye contact, I stepped forward and reached for his cuffs."
    "The metal was cool beneath my fingers as I slid the key into the lock. A sharp click echoed in the small room."
    "The heavy Jinshen steel fell away from his wrists."
    "Svante inhaled sharply, his arms dropping limply to his sides. He stared at his freed hands for a moment."

    dorian "Don't make me regret this."
    svante "I won't, sir."

# =============================================================================
# SECTION 17D: RETURN TO LAB — Dinner Begins
# =============================================================================
label ch5_return_to_lab:
    scene bg_yuxuan_lab with dissolve           # PLACEHOLDER — lab main room, warm light
    play music ost_dinner_warm fadein 2.0       # PLACEHOLDER — warm dinner theme
    play audio amb_kitchen loop fadein 1.5      # PLACEHOLDER — kitchen ambient

    "As Svante and I stepped into the main room, the warm scent of spices and simmering broth filled the air. The rich aroma of slow-cooked meats and fragrant herbs curled through the space."
    "Weng was still by the stove, stirring a pot with practiced ease. The moment her gaze landed on Svante, she set down her spoon and wiped her hands on her apron, stepping forward with a welcoming smile."

    weng "Ah, you're awake! That's good to see. You must be starving."
    weng "Proper introductions are in order. I'm Cai Weng, Master Yuxuan's assistant. It's a pleasure to meet you, young man."

    "He blinked, as if taken aback by the kindness in her voice. He looked at me, and then back to her."

    svante "I… Yes. Thank you, m-mam. My name's Svante. Svante Nordstrom. I-I'm so glad to meet you."
    weng "Dinner is ready. Please have a seat, gentlemen and I'll be serving you up the food."
    weng "I hope you like haugensoppa. I made it just for you."
    svante "Haugensoppa? You… know Mjoll cuisine?"
    weng "Oh, I've had my fair share of travelers from the North. You lot love your root vegetable stews."

    "Svante opened his mouth, perhaps to ask more, but before he could reply—"
    "A sudden burst of tiny, hurried footsteps came from the hallway."

    tim "Elias, you're going too slow! Dinner's about to start!"
    elias "I'm carrying Tedda and my book! It's a little heavy!"

    "Tim marched into the room first, his small arms wrapped around a thick, leather-bound book far too large for someone his age. The title was embossed in gold: {i}Tianho's Ancient Dynasties.{/i}"
    "Elias followed closely behind, but instead of a weighty tome, he proudly clutched a children's coloring book, its cover splashed with bright rainbows and smiling animals. Perched lazily on top was Tedda."
    "Tim sighed dramatically, adjusting his glasses."

    tim "Elias, I told you to pick something educational."
    elias "This one had colors, Tim! It's got rainbows! They're educational."
    tim "Rainbows are not educational, Elias."

    "Elias gasped as he spotted Svante. His eyes widened with delight."

    elias "Look! It's the pink haired guy! He's awake!"
    tim "Huh? He's not pink haired, Elias! It's violet!"
    elias "Tim, pink and violet are the same. Right, Tedda?"
    tim "What?! They're completely different colors. Right, Miss Weng?"
    svante "Actually… my hair is violet. It's not really pink."
    tim "HA! It's violet! See, Elias? See? I win! HAHA—"
    weng "Tim, quit it. You're embarrassing me in front of Sir Burnham and Sir Nordstrom. Now be a good boy and help me serve dinner."

    "Tim huffed but did as he was told, setting his book down carefully before moving to grab a stack of bowls."

    jump ch5_chung_wakes
# =============================================================================
# SECTION 18: LABEL CH5_CHUNG_WAKES — Chung-hee Arrives at Dinner
# =============================================================================
label ch5_chung_wakes:
    # [COMMENT: bg_kitchen — long dining table, warm light, Weng cooking]
    scene bg_kitchen with dissolve              # PLACEHOLDER — kitchen / dining area

    play music ost_dinner_warm fadein 2.0       # PLACEHOLDER — warm dinner theme
    play audio amb_kitchen loop fadein 1.5      # PLACEHOLDER — kitchen ambient

    dorian "Elias, why did you even bring all of those—"

    "I felt something. A shift in the air."
    "A presence."
    "Slowly, I turned."
    "The once-unconscious man was now floating. His feet hovered barely above the ground, the air around him rippling like disturbed water."
    "Then, his head bowed slightly. A voice entered our minds."

    chung_hee "You must be the ones who rescued me. Thank you."

    "The room fell into an eerie silence."

    "We were all seated at the long table—me, Yuxuan, Niko, Svante, and the once-unconscious man. Roboto hummed softly as it moved around the table, methodically placing glasses of water in front of each of us."

    roboto "One for you… One for you…"
    roboto "Would you prefer ice cold or lukewarm, Sir Niko?"
    niko   "Ice cold. Thanks."

    "Then—the voice returned. Not spoken aloud, but entering our minds like a gentle ripple through still water."

    chung_hee "Once again, I wish to express my deepest gratitude. Words alone cannot convey how much I owe you."
    chung_hee "If not for you, I would have met a terrible fate."
    dorian    "Don't mention it."
    niko      "And you don't need to be so formal. You don't have to use mind channeling all the time—we can understand you just fine if you speak normally."

    "There was a pause."

    chung_hee "Forgive me. I can only communicate through mind channeling. I hope it is not of any inconvenience to you."
    yuxuan    "Really? Why not?"
    chung_hee "I was born unable to speak. Nor hear. This is the only way I can make myself understood."
    niko      "So you're a deaf-mute… and you're using your channeling abilities to expand your senses. That's impressive."
    dorian    "I respect that."
    niko      "I actually know a little bit of sign language. My brother and I studied it so we can translate for the Emperor of Kyeongjang's son—he's also a deaf-mute."
    svante    "The son of the Emperor of Kyeongjang's a deaf-mute? Poor guy."
    chung_hee "You know my father?"
    niko      "Father?"
    chung_hee "Yes, you've heard correctly. My name is Hyon Chung-hee. Son of Emperor Hyon Min-joon. And the Emperor of Kyeongjang."

    "Silence."
    "For a moment, none of us reacted."

    dorian    "?!"
    niko      "?!"
    svante    "?!"

    "Niko inhaled sharply, his eyes darting toward me as if to confirm that we had all heard the same thing."
    "Svante's entire body tensed, his expression a mixture of disbelief and caution. Even Weng, who had spent the past hour focused solely on her cooking, froze mid-motion."
    "Tim, who had been carefully placing spoons on the table, accidentally dropped one. The clatter was deafening in the silence."
    "Only Elias remained blissfully unaware, still coloring, his small voice humming a made-up tune."

    elias "La la la la..."
    "Tedda: …"

    yuxuan "T-The Emperor?!"
    weng   "By the stars…"

    "I leaned back slightly, watching the man—the Emperor—carefully."
    "His expression did not waver. He did not fidget, nor did he show any trace of uncertainty."

    dorian    "You must be joking. The Emperor of Kyeongjang is dead."
    chung_hee "Yes, my Father, Emperor Min-joon and my mother passed away during their time in Tianho."
    chung_hee "In the wake of their passing, I was named their successor. I am the Emperor now."

    "He exhaled slowly."

    chung_hee "But as for me. I am alive and well. Thanks to all of your combined efforts."

    "I blinked."
    "Silence stretched across the room, thick and suffocating. No one spoke. No one moved."
    "Then—"
    "Yuxuan burst out laughing."

    yuxuan "HAHAHAHAHAHA!"
    yuxuan "Pfft—alright, that's it. I've officially lost my mind because of that damn propulsion system. This is a dream. A really weird, stress-induced dream."

    "He waved a hand in front of his face dramatically."

    yuxuan "I mean, let's think about this logically. What are the odds that the actual Emperor of Kyeongjang would be sitting at my dinner table, in my secret underground lab, eating my food?"

    "He turned to Weng, looking utterly amused."

    yuxuan "Come on, Miss Weng. Pinch me. Maybe I'll wake up in my office, face-first in a pile of paperwork."

    "Weng let out a long, suffering sigh, pressing her fingers against her temples."

    weng "Master Yuxuan… Are you sure?"

    "Niko chuckled, shaking his head."

    niko "Well, I didn't exactly expect to be dining with the owner of Cheng Industries at his 'secret laboratory' either, let alone with an elderly lady as his personal maid… but here we are."
    niko "On top of that, let's look at our dinner party for a second, shall we?"
    niko "First up, we have a former Paladin who can channel earth, wind, and fire. Let's also not forget the spectacle with the draconic fire earlier."

    "He flicked a glance at me."

    niko "Next we have an aldorith with violet hair who switched sides and can manipulate metal at will, an affinity that less than one percent of the population can even dream of."

    "At that, Svante visibly tensed, his fingers curling ever so slightly on the table. But he smiled and said nothing."

    niko "A talking robot with a mind of its own. And—"

    play sound sfx_roboto_crash                 # PLACEHOLDER — Roboto crash SFX

    roboto "R-R-R-R-R-R-R-ooooooo- *crashes*"
    niko "Right. Moving on."
    niko "A green-haired toddler who, for some reason, spends his free time reading damn bibliographies instead of playing with toys."

    "Tim blinked up at him from behind his book, entirely unfazed. Then, as if on cue, he calmly turned a page in his heavy tome—Tianho's Ancient Dynasties."

    tim "Hnn…"
    niko "A crossdressing toddler who just so happens to be the crown Prince of Mjoll and carries around a smelly ragdoll named 'Tedda.'"

    "Elias suddenly giggled, completely unaware of the tension in the air. He held up his coloring book, showing it off proudly."

    elias "Look! Wainbow, daddy!"
    tim   "Not now, Elias. The grown-ups are talking."
    niko  "And you have me. A Prophet of the death god, Enoch, who happens to be his Chosen."

    "Niko shot Yuxuan a slow, knowing smirk."

    niko "So tell me, Yuxuan—are you really that surprised that the man sitting with us is the Emperor of Kyeongjang?"

    "Yuxuan stared at him for a moment, then exhaled, shaking his head."

    yuxuan "You make a fair point."
    weng   "You're such an open-minded and understanding person, Master Yuxuan. The pinnacle of open-mindedness!"
    yuxuan "Aww thank you, Miss Weng! Well, I am a veryyyyy understanding man, so—"

    "I buried my face in my palms."

    chung_hee "I see. You are all… quite the interesting group."

    "Chung-hee's expression remained unreadable. Svante suddenly spoke up, his voice quiet but firm."

    svante "If I may… I believe His Majesty is telling the truth."

    "A hush settled over the group. Svante's eyes were downcast."

    svante "Father said the Emperor of Kyeongjang was going to be the next target. He told us the Emperor was a sick, twisted, dishonorable person."

    "His hands clenched into fists."

    svante "And I believed him at first. I had no reason to but I believed him."
    svante "But… when I met you, Your Majesty, you were kind. You spoke to us with dignity. You offered us peace."
    svante "I didn't believe you could be the Emperor because you weren't the monster I was taught to fear."
    svante "But looking at it now, he must have been lying. Not that you weren't the Emperor but the part where you were a sick, twisted person."

    "Chung-hee regarded him for a long moment, expression unreadable."
    "Then—he gave a small, approving nod."

    chung_hee "Thank you."

    "The Emperor of Kyeongjang… No, Emperor Min-joon's son."
    "A thousand questions swirled in my mind. Questions about the past. About the Tragedy of Tianho. About why he was targeted. About why he was here."
    "But before I could voice a single thought—"
    "Weng sat the first dish down."

    "Her voice was warm and full of praise as she placed a steaming bowl in front of Yuxuan."

    weng "Dragonfire curry for the incredibly intelligent, devilishly handsome, and world-renowned genius that is Master Yuxuan."

    "Yuxuan lit up like a child on his birthday."

    yuxuan "Miss Weng! You shouldn't have! My precious dragonfire curry! Oh, how I've missed you!"

    "He clasped his hands together dramatically."
    "Meanwhile, Roboto whirred into view, carefully balancing trays of food."

    roboto "Robotoooo is ready to s-s-s-serve~ F-f-food is ready~"
    niko   "The robot shouldn't be allowed to serve food. It might crash again."
    yuxuan "You're the only one who thinks that, Niko. Roboto is a technological marvel and- IT. DOES. NOT. CRASH."

    "Niko's eyes blinked."

    niko   "Yuxuan, I mean no disrespect to Roboto. It's amazing. But a while ago it almost crashed and brought down a jar filled with water in it."
    yuxuan "Why I never!"
    niko   "Dorian was there. He'll be our witness. Dorian, it's true right?"

    jump ch5_roboto_witness


# =============================================================================
# SECTION 19: LABEL CH5_ROBOTO_WITNESS — Roboto Stumble Testimony
# =============================================================================

label ch5_roboto_witness:

    menu:
        "Yes. Roboto almost tripped.":
            $ ch5_roboto_witness = "yes"
            $ niko_affection += 1               # +1 Niko affection

            dorian "Yeah… Roboto did almost trip. But Niko caught it in time, so I don't think it matters much."
            niko   "There you have it."

            play sound sfx_roboto_beep          # PLACEHOLDER — Roboto beep SFX

            roboto "M-m-m-master Dorian is c-c-correct! I was transporting water, but my sensors momentarily overloaded. Sir Niko was able to assist me."
            yuxuan "Oh… Maybe some recalibration is in order. Can't have my masterpiece faltering under pressure."

            "Roboto blinked rapidly, its mechanical eyes adjusting."

            roboto "C-c-confirmed! Roboto will undergo recalibration!"

            "Yuxuan sighed, adjusting his glasses."

            yuxuan "Great. Now I feel guilty. Roboto, remind me to run diagnostics later."

            play sound sfx_roboto_beep          # PLACEHOLDER — Roboto beep SFX

            roboto "Reminder set! Diagnostics will begin at 20:00 hours!"

        "No. Roboto had it all under control.":
            $ ch5_roboto_witness = "no"
            $ yuxuan_affection += 1             # +1 Yuxuan affection

            "I shook my head, folding my arms."

            dorian "No, Roboto had it under control."

            play sound sfx_roboto_beep          # PLACEHOLDER — Roboto beep SFX

            roboto "D-d-data inconclusive. Roboto must recalibrate!!"

            "Yuxuan's expression brightened, and he gave me a satisfied nod."

            yuxuan "Thank you, Dorian. At least someone here has good judgment."

            "Niko pinched the bridge of his nose."

            niko   "Oh, for the love of—"
            yuxuan "Let this be a lesson, Niko. One should never question the technological marvel that is Roboto."

    "Roboto whirred smoothly across the room, carefully placing each dish in front of us."

    roboto "Here is your f-f-f-food, Your Majesty. We lack information on Kyeongjang cuisine, but we have prepared a special dish from Gale."

    "As Roboto spoke, its small monitor flickered to life, displaying a video of hand signs."

    roboto "T-T-This is called mountain herb stew along with a plate of sautéed highland greens."
    roboto "Cooked with garlic and a drizzle of fragrant mountain oil. Enjoy, Your Highness!"

    "Chung-hee's expression softened slightly. He raised his hands and responded with hand signs of his own."
    "Roboto paused for a moment before beeping happily."

    roboto "A-A-A-Affirmative! I will not call you Your Majesty. T-t-thank you, Sir Chung-hee!"

    "Niko and Yuxuan paused, exchanging glances."

    niko   "Roboto knows sign language?"
    yuxuan "I programmed Roboto to recognize multiple languages, but I don't remember programming sign language. Fascinating…"
    weng   "As is expected from our amazing and very talented inventor, Master Yuxuan!"
    yuxuan "Aww thank you, Miss Weng!"
    niko   "Oh brother."

    "Niko rolled his eyes, picked up his chopsticks and started eating."
    "Chung-hee picked up his chopsticks, taking a bite of the stew. For the first time since arriving, he looked almost… at ease."

    # Branch on food choice
    if ch5_food_choice == "tianho":
        jump ch5_food_moonlit
    elif ch5_food_choice == "gale":
        jump ch5_food_truffle
    elif ch5_food_choice == "hinami":
        jump ch5_food_hotpot
    elif ch5_food_choice == "mjoll":
        jump ch5_food_lamb
    else:
        jump ch5_food_common


# =============================================================================
# SECTION 20: LABEL CH5_FOOD_MOONLIT — IF Moonlit Noodles (Tianho)
# =============================================================================

label ch5_food_moonlit:

    "Roboto whirred in again, humming softly as it approached me with a steaming bowl. The rich, savory aroma of black garlic and star anise filled the air, mingling with the sharper spice of Yuxuan's dragonfire curry."

    roboto "Here are your Moonlit Noodles, M-M-Master D-D-Dorian!"

    "The little machine's voice stuttered slightly, but its movements were careful and precise as it placed the bowl before me. The deep, dark broth gleamed under the dim light, the noodles glistening as they curled beneath the surface."
    "Resting atop them were thin slices of braised beef, their edges caramelized to perfection, and a single soft-boiled tea egg, its yolk just barely runny."

    "Yuxuan leaned over with interest, his eyes lighting up."

    yuxuan "Hey Dorian, do you know why the dish is called Moonlit noodles?"

    menu:

        "Is it because of the egg?":
            $ yuxuan_affection += 1             # +1 Yuxuan affection

            "I looked at the egg and it vaguely looked like the moon."

            dorian "Is it because of the egg?"

            "Yuxuan looked at the bowl."

            yuxuan "Oh you're right. I haven't thought of it that way."
            dorian "You mean you didn't know, Yu?"
            yuxuan "I don't know. That's why I'm asking."

        "I don't know.":

            dorian "No. Why are they called that?"
            yuxuan "I don't know. That's why I'm asking you."
            dorian "This is my first time eating these, Yu. Why would I know that?"
            yuxuan "… Oh…"
            yuxuan "Well, yeah. Figures. You don't really look like someone who dabbles in fine cuisine."

            "I raised an eyebrow."

            dorian "What's that supposed to mean?"

            "Yuxuan waved his hand vaguely."

            yuxuan "No, no, no. I didn't mean it in a bad way. I meant that you can eat almost anything and still be happy! Not many people are like you, Dorian."
            dorian "I'll take that as a compliment. Thanks, Yu."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "M-m-m-master Dorian is a man of culture! M-m-my sensors detect a 92.3% probability that he will e-e-e-enjoy this meal!"
    yuxuan "But what happens if Dorian doesn't like it?"

    "There was a brief pause. Then—"

    roboto "E-e-e-error! Scenario not calculated! Rebooting crisis protocol… Processing…"

    "I sighed."

    dorian "Yu, stop messing with Roboto."
    yuxuan "It's just part of his crisis protocol subroutine, Dorian. He can handle it."

    "He leaned back, arms crossed, a knowing smirk tugging at his lips."

    yuxuan "Here, I'll show you. Roboto, give me a compliment."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "A c-c-c-compliment? Certainly!"

    "The little machine beeped twice before its voice rang out."

    roboto "M-M-Master Yuxuan, you are the greatest inventor Ena has ever known! Your intelligence will put the Almighty Tetrad Li Mengtia to shame!"
    yuxuan "Awww Roboto, you really know how to make a guy feel special."
    roboto "I-I-I'm glad you like it, Master Y-Y-Yuxuan! I-I-I try my b-b-best!"

    "I let out a slow breath, stirring my noodles with my chopsticks. The warmth from the broth seeped into my fingers."

    chung_hee "You should be proud of yourself, Sir Yuxuan."

    "Yuxuan blinked, his smirk brightening into a smile as he turned to the Emperor."

    yuxuan "Really, Your Majesty?"

    "Chung-hee nodded, setting his chopsticks down neatly beside his bowl."

    chung_hee "Roboto is a marvel. Not only functional but adaptable. Few inventors create something with the ability to learn, let alone something with such… personality."
    chung_hee "In Kyeongjang, our automatons do not use sign language. They do not adapt to individual needs. I appreciate what Roboto did."

    jump ch5_food_common


# =============================================================================
# SECTION 21: LABEL CH5_FOOD_TRUFFLE — IF Imperial Truffle Roast (Gale)
# =============================================================================

label ch5_food_truffle:

    roboto "Here it is! A meal fit for a conqueror—Master D-D-Dorian's Imperial Truffle Roast!"
    roboto "Slow-roasted venison, glazed with truffles and wine reduction, served with buttered root vegetables, all arranged to p-p-please even the most discerning p-p-p-p-p-p-p~"
    dorian "Palate. Thanks, Roboto."

    "It placed the dish before me with an exaggerated flourish, its screen blinking in what I could only assume was enthusiasm. The scent of roasted venison and truffle filled the air, rich and mouthwatering."
    "I eyed the venison, the glaze shimmering. Chung-hee leaned forward slightly, his sharp eyes scanning my plate with interest."

    chung_hee "Fascinating…"
    dorian    "Something wrong?"

    "He studied the dish as if committing every detail to memory."

    chung_hee "Kyeongjang is familiar with many foreign dishes, but an Imperial Truffle Roast is a rarity among our people."
    chung_hee "Truffles themselves are difficult to acquire within our lands… and venison, though not unheard of, is not often prepared in this manner."

    "Tim, who had been quietly flipping through the pages of his latest book, had dropped it onto the table. He blinked up at Chung-hee, adjusting his glasses."

    tim "Your Majesty, I've read that ancient Kyeongjang dishes were once served on lacquered stone platters infused with medicinal resins."

    "The table fell silent."
    "I turned to Tim, half-expecting him to be making things up. But no—his expression was as serious as ever."

    "Chung-hee stiffened. Just barely, but enough for me to notice. His gaze, so often cool and composed, flickered with something else. A sharp glint of recognition."

    chung_hee "...That practice fell out of use centuries ago."

    "His fingers tapped once against the table."

    chung_hee "Few even remember it."

    "Tim tilted his head."

    tim "It was abandoned before the time of the Death God Enoch, correct?"

    "Chung-hee's head turned toward the boy fully now, shocked."

    tim "I read it from a pre-Enoch book. Very few literature from that time period are preserved. Luckily Master Yuxuan keeps a few in his big library."

    "He spread his tiny arms wide to emphasize just how massive Yuxuan's collection was."

    "Chung-hee studied him with the same scrutiny he had given my meal moments before."

    chung_hee "How old are you?"

    "Tim adjusted his glasses."

    tim   "Five."

    "I blinked."
    "Chung-hee blinked."
    "The two of us stared at him."

    dorian "Are you sure?"
    tim    "Yes, I'm sure, sir Dorian."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "R-R-Roboto confirms! Tim is 100% five years old!"

    yuxuan "Ahaha… don't mind Tim. He's just... Well, we call him a little genius here."

    chung_hee "A five-year-old… quoting lost histories and the fall of divine ages..."
    chung_hee "In Kyeongjang, wisdom is not measured by years, but by the depth of one's spirit. And yours, young scholar, is fathomless."

    "Tim beamed proudly, pushing up his glasses with both hands."

    tim "Anyway, thank you for confirming it, Your Majesty. I was just curious."

    jump ch5_food_common


# =============================================================================
# SECTION 22: LABEL CH5_FOOD_HOTPOT — IF Fisherman's Hotpot (Hinami)
# =============================================================================

label ch5_food_hotpot:

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "A dish fit for a traveler of tides and a seeker of shadows! Presenting your Fisherman's Hotpot, M-M-Master D-D-Dorian—crafted with the heart of the sea and the soul of the island itself!"

    dorian "Thank you, Roboto. It looks delicious."

    "As I took the first sip of the miso broth, the rich umami flavor spread over my tongue, warming me instantly. The fresh seafood, barely touched by the heat, still had that ocean-bright taste, balanced perfectly with the mild tofu and tender greens."
    "Beside me, Niko had his head bowed, hands loosely clasped."

    niko "Bless us O mighty Enoch and these thy gifts, which we are about to receive."
    niko "May this food restore our strength, giving new energy to tired limbs and bodies."

    "He finished his prayer and glanced at my bowl."

    niko   "Delicious, huh?"
    dorian "Yeah. The miso broth with the seafood is a great combination."
    niko   "It does. Used to have that all the time when I stopped by Hinami Port for fish and supplies."

    "I raised a brow."

    dorian "Didn't peg you as the type to sit around a fire with a bunch of fishermen."
    niko   "Well, when you're a doctor in a small village in Hamatame, you take what you can get. They'd trade me fresh seafood, supplies for herbs and organic medicine."
    niko   "Oftentimes I'd end up sharing a meal with them."

    "He stirred his spoon through the broth, a hint of nostalgia flickering across his face."

    niko "Hinami isn't as wealthy as Mjoll or Gale, but the sea is generous. The people there take care of each other. No one eats alone after a long day at sea."

    dorian "I take it you miss your home nation?"
    niko   "You could say that. They say that Hinami will be hosting the Tragedy of Tianho's anniversary tomorrow. Perhaps I'll—"

    "A small commotion at the other end of the table pulled my attention away."

    tim   "Elias, you need to eat your chicken. And your rice. And your vegetables."

    "Elias shook his head and clutched Tedda like a shield."

    elias "No!"

    "Tim sighed, pinching the bridge of his nose."

    tim "Elias, you can't just eat chocolate and sweets all the time!"

    "Niko chuckled."

    niko "What seems to be the problem?"
    tim  "Elias won't eat his vegetables!"

    dorian "Elias. We talked about this. You need to eat your vegetables."
    tim    "Listen to your father, Elias."
    elias  "But daddy…"
    niko   "Alright, kiddo. How about this—if you eat your chicken, rice, and veggies, I'll read you a bedtime story tonight. How's that sound?"

    "Elias's eyes lit up."

    elias "A story?! Okay!"

    "Elias glanced at his plate, then back at Niko. He picked up his spoon and carefully scooped up a piece of chicken. After a moment's hesitation, he popped it into his mouth."
    "Then he beamed again."

    elias "I eat!"
    tim   "(muttering) Manipulated by bedtime stories…"

    "After a pause, he fidgeted slightly before speaking up."

    tim  "I… I'm included too, Sir Niko, right? I can join the storytime… if you want…"

    "Niko grinned."

    niko "Sure, but only if you eat your food too."
    tim  "Okay. Let's eat, Elias."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "C-c-cognitive reinforcement successful! Reward-based motivation confirmed as eff-eff-effective!"

    "I glanced at Niko, offering a nod of thanks."

    dorian "Thanks for your help with Elias. Didn't know you were good with kids."

    "Niko shrugged, a small smile tugging at his lips."

    niko "You're welcome, Dorian."

    "I watched as Tim and Elias, now fully focused on their plates, quietly ate their food."
    "Across the table, Chung-hee had been quietly observing."

    chung_hee "Fascinating… You should be proud of yourself, Sir Niko."
    niko      "I used to have a lot of kid patients back in Hamatame. You learn a few tricks when you're treating scared little ones, Your Majesty."

    jump ch5_food_common


# =============================================================================
# SECTION 23: LABEL CH5_FOOD_LAMB — IF Mjollian Mead-Braised Lamb (Mjoll)
# =============================================================================

label ch5_food_lamb:

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "Behold! A meal fit for a warrior! A dish crafted for the strong and the steadfast—M-M-Master D-D-Dorian, your Mjollian Mead-Braised Lamb awaits!"

    "I stared down at the plate in front of me. Thick, spiced mead sauce clung to the slow-braised lamb shank, its aroma warm and heady. Beside it, a dense slice of black rye bread and a small dish of herbed butter sat neatly on the tray."
    "It looked rich—very rich. Heavy. Nothing like the plain food I usually ate."

    svante "Have you eaten that before, Sir Dorian? Back in Mjoll?"
    dorian "I… don't remember eating this. I usually just made something easy—stews, boiled potatoes, whatever was quick."
    svante "Did Father's cooks serve you food when you were working under him as a mercenary?"
    dorian "No, I always refused. Dishes like this are too fancy for my taste back then."

    "I glanced at him, then back at the food."

    "Svante hesitated before exhaling softly, a sad smile ghosting his lips."

    svante "My mother used to love that dish. Before she got sick… back when she was still— back when people still talked about her."
    dorian "Your mother?"
    svante "I doubt you'd know her sir Dorian. She was a songstress—a famous one, once. Back in Tianho, before she got sick."
    svante "Her voice used to be everywhere—on the radio, in the theaters. People adored her."

    "He stared down at the dish, a flicker of something bittersweet in his eyes."

    svante "She used to call that dish 'the taste of home.' Said it reminded her of the time before… everything changed."

    "I looked down at the dish again. To me, it was just another meal—fuel to keep going, nothing more. But to him? It was a memory."
    "I nudged the plate slightly in his direction."

    dorian "You can have it if you want. I really don't mind. I'll just ask for something else—"

    "Svante's eyes widened slightly."

    svante "What? No, I— I appreciate it, sir, but you should eat. It's a warrior's meal, after all. My mom would have liked that, though."
    svante "You should eat it, sir Dorian. Who knows? Maybe you'll grow to like something other than stale bread and ration bars, sir."

    "I rolled my eyes."

    dorian "You're making it sound like that's all I eat."
    svante "No, no, no! I apologize, sir, I—"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "M-m-m-my sensors indicate that M-M-Master Dorian is just fooling around."
    svante "Oh, um… S-Sorry…"

    "I shrugged, took my chopsticks, and went to eating."

    "A few minutes after I started eating, Weng approached, setting down another dish with practiced ease."

    weng "Here are some Tianho dumplings I prepared. Extra portions."
    tim  "Yay! Elias, you need to try these!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "Tianho dumplings—suitable for any occasion!"

    "She then placed a fresh pot of tea in the center of the table, steam curling elegantly from its spout."

    weng   "And some tea. Freshly brewed from tea leaves from Tianho. I hope you like it."
    yuxuan "The teacup looks beautiful, Miss Weng!"
    tim    "We got it yesterday from a bargain store, Master Yuxuan!"
    weng   "Now, everyone grab a cup and I'll pour you some."

    jump ch5_food_common


# =============================================================================
# SECTION 24: LABEL CH5_FOOD_COMMON — Food Common (Roboto serves Chung-hee)
# =============================================================================

label ch5_food_common:

    "Weng then approached the two toddlers, smoothing out the wrinkles in her apron."

    weng "Alright, little ones. What would you like for dinner?"

    "Tim adjusted his tiny glasses, crossing his arms."

    tim "Braised Tianho fish with fermented black beans. Steamed tofu with ginger. And a side of sautéed bok choy with garlic."

    "I blinked."
    "Weng just smiled and jotted the words down on the notepad."

    dorian "What kind of five-year-old asks for that?"
    yuxuan "Hahaha! That's Tim. He has quite the refined palate, just like me and Weng."

    "Tim pushed his glasses up the bridge of his nose, utterly serious."

    tim "Proper nutrition is essential for cognitive development of toddlers like myself. My brain requires high-quality fuel."

    "Meanwhile, Elias was bouncing on his heels, practically vibrating with excitement."

    elias "Ooh! I want choco—"

    "I cut him off before he could even finish."

    dorian "Chicken. Rice. Soup. And lots of vegetables. He'll have that."

    "Elias's little face scrunched up into a dramatic pout, his lower lip jutting out."

    elias "But daddy—"

    "I gave him The Look."

    dorian "No, Elias. You already ate enough chocolate today. You need your vitamins."

    "Elias squirmed. His little hands clutched Tedda, his stuffed bear, like the poor toy could somehow convince me to change my mind."

    tim   "Vegetables are good for you, Elias."
    elias "No, they're not… They're icky!"
    tim   "Yes, they are. They contain essential vitamins and minerals that help you grow stronger and support brain function. You want to be smart like me, don't you?"
    elias "Fiiineeee…"
    weng  "Alright then, why don't you two go play while I prepare dinner?"
    tim   "Master Yuxuan, can Elias and I go to the library?"
    yuxuan "Always, Tim. Keep on reading, green-haired buddy."

    "Tim's face lit up. He turned to Elias, taking his hand like a tiny professor guiding his student."

    tim   "Come with me. I'll show you the library."

    "Elias blinked, surprised."

    tim   "I'll show you my favorite books! Let's read together! Oh, you're gonna love the legend of the kumiho!"
    elias "Let's go! Ooh! Do they have pictures and flowers there?"
    weng  "Tim… Make sure to be back once dinner is finished, okay? It's a challenge to get you away from those books once you start. Be mindful of little Elias with you."

    "Yuxuan and I watched them go, both of us shaking our heads in amusement."

    yuxuan "They make quite the pair huh, Dorian? They just met and they're acting like they've known each other for a long time!"
    dorian "No kidding."

    "Weng chuckled as she headed toward the kitchen."

    weng "You two, just sit tight and wait. Dinner will be ready soon."

    jump ch5_chung_wakes


# =============================================================================
# SECTION 25: LABEL CH5_DINNER_TALK — Gustav Choice / Dinner Conversation
# =============================================================================

label ch5_dinner_talk:

    "We continued eating."
    "I focused on finishing my plate first—I was hungry."
    "The dishes were nothing short of perfection. Weng was a damn good cook."
    "Across from me, Elias had already devoured half of his plate, looking both satisfied and slightly overwhelmed."
    "I glanced around. Once everyone had eaten their fill, I set down my chopsticks and spoke up."

    dorian "So, Chung. Any idea why the kingdom of Mjoll wanted you killed?"

    "The light-hearted atmosphere dimmed instantly. Chung-hee's expression darkened."
    "He met my gaze. Then, calmly, with the weight of finality, he spoke."

    chung_hee "I will end the life of King Gustav Nordstrom."

    "The entire table went silent."
    "I felt my grip tighten around my cup. The room had grown heavy, like a storm rolling in. Across from me, Svante's entire body went rigid, his fingers barely twitching against the table."

    svante "?!"

    "Niko leaned forward, brows furrowing."

    niko  "…What?"

    "Weng set her teacup down slowly, her voice barely above a whisper."

    weng "By the stars…"

    "Chung-hee remained composed, his gaze unwavering."

    chung_hee "King Gustav seeks to claim the Divine Weapon. He wishes to rule over all nations of Ena."
    niko      "Divine Weapon? What are you talking about?"

    "Chung-hee didn't blink. He met our gazes."

    chung_hee "Five years ago, King Long Shen spoke to my father about a weapon unlike any other. A relic forged to defy the laws of life and death itself."
    chung_hee "A weapon meant to raise the dead. To bring back entire armies."

    "A weighted silence followed. I had never heard of such a thing. And judging by the expressions around the room, neither had they."

    "Tim shook his head, pushing his glasses up the bridge of his nose."

    tim "…I… don't think I've ever read about anything like that, Sir Chung."
    yuxuan "Hmm… That doesn't sound good. If Tim hasn't read about it, it probably doesn't exist."
    weng "That is true, Master Yuxuan."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    "Roboto's glowing eyes flickered. The whir of his internal mechanisms filled the room as he processed the information."

    roboto "Checking… C-C-C-Checking library r-r-r-records…"
    roboto "Search concluded! N-N-No records in the library about a so-called 'DIVINE WEAPON.'"

    svante "Legends speak of weapons blessed—or cursed— but none have ever mentioned such a thing as a weapon bringing back people to life."
    niko   "I've read all of Enoch's chronicles. Every single one. Not one of them mentions a Divine Weapon."

    "He leaned forward, gaze sharp."

    niko "Do you even know where this thing is?"
    chung_hee "No. Only that it is somewhere in Tianho."
    chung_hee "The fact remains. It must never fall into King Gustav's hands."
    chung_hee "I will end him before that happens."

    "Yuxuan let out a sharp breath, leaning back in his chair."

    yuxuan "I was not expecting that with my tea."

    "Svante's fingers trembled against the table. His voice was unsteady."

    svante    "Kill… Father? A-Are you sure of this, sir Chung?"
    chung_hee "I would not speak of such things lightly."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    "Roboto, usually cheerful, gave a low whirring sound."

    roboto "D-d-d-danger level escalating. Adjusting threat parameters… I-I-I strongly advise against making dangerous statements out loud!"

    "Niko exhaled sharply, rubbing his temples."

    niko "You're talking about regicide, Chung."
    chung_hee "If he succeeds, countless lives will be lost. I will not allow it."

    "Svante's hands curled into fists. He hesitated before speaking, voice shaking just slightly."

    svante "If I may, how do you intend to k-kill Father, sir Chung?"

    "Chung-hee lowered his gaze for a moment."

    chung_hee "Cheonmyeong Gyeol…"

    "Svante blinked, confused."

    svante "Huh? Chanmong…"
    chung_hee "Cheonmyeong Gyeol… A duel between two rulers to the death."

    "The words seemed to echo through our minds."
    "For a moment, nobody spoke. Then, from the far end of the table—"
    "Tim straightened, his eyes widening with recognition."

    tim "Wait… you mean the ancient trials of Kyeongjang? The ones that determined a kingdom's fate with a single battle?"
    tim "I've read that before! In pre-Enoch books!"

    "Chung-hee gave a single nod."

    chung_hee "Yes. It is an ancient tradition, one older than any war on record."
    chung_hee "Long ago, the rulers of old would stake their lives in battle rather than sacrifice their people to war. A single duel—no armies, no bloodshed beyond their own. The winner would decide the fate of nations. It was a trial of honor, strength, and destiny."
    dorian    "I've never heard of that before."
    niko      "Me neither. I don't think those are present in any of the Death God's scriptures."

    "Tim's expression glowed with excitement."

    tim   "I knew it! The texts said the greatest rulers of the old dynasties fought like this! Right, Elias?"
    elias "Hehe. Tedda says I love you, Tim!"
    "Tedda: …"
    tim   "Umm… never mind."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "Tim's knowledge is accurate. The Cheonmyeong Gyeol was considered the ultimate test of kingship. Only the worthy could survive."
    yuxuan "That's Tim for you. Always knowing the old stories."

    chung_hee "I challenged Gustav months ago. He only recently accepted."

    "Yuxuan leaned back in his chair, one brow arching in curiosity."

    yuxuan "Then tell me, Chung—if King Gustav agreed to the duel, why did he send a battalion of soldiers and Aldoriths after you?"

    "A shadow passed over Chung-hee's face."
    "I turned to Svante."

    dorian "Svante, do you know anything about this?"

    "Svante looked down, his hands tightening into fists. He swallowed hard before shaking his head."

    svante "N-no. I… We were only told by Father that Chung would be there. He didn't tell us anything else."

    "Niko scoffed. He leaned back, arms crossed, his expression dark with disgust."

    niko "What a coward."

    "Weng approached the table with practiced grace, a porcelain teapot cradled gently in her hands."

    weng   "Perhaps a calming tea is just what you boys need. Should I pour some more?"
    svante "Yes, please. Thank you, miss."
    niko   "Yeah…. Thanks."

    "Beside them, Tim reached across the table, cheerfully nudging a plate forward."

    tim   "Here, have some more crumpets sirs! They go well along with the tea."

    "Svante took one, though his hands still trembled slightly as he brought it to his plate."

    svante "T-Thank you."

    "Across the table, Chung-hee inhaled deeply, his hands resting flat against the polished wood."

    chung_hee "I was honestly surprised… A king should be… strong, just, honorable…"

    "Yuxuan snorted. Then he laughed."

    yuxuan "Hahaha! King Gustav? Honorable? Hah! That's the best joke I've heard all day!"

    "I exhaled sharply, shaking my head."

    menu:

        "Don't be naïve, Chung.":
            $ ch5_chunghee_speech = "naive"
            $ chunghee_affection -= 1           # -1 Chung-hee affection

            dorian "You're being naïve, Chung."

            "Chung-hee frowned."

            chung_hee "Those in power need to have honor. They won't be sitting in their thrones otherwise. People follow them for a reason. They—"
            dorian    "Honor doesn't rule kingdoms. Power does. And those who don't accept that? They get crushed beneath those who do."

            "For the first time, doubt flickered in Chung-hee's eyes. But it was quickly buried under quiet defiance."

            chung_hee "I..."
            chung_hee "You're wrong, Dorian."

            "He turned his gaze away, staring at the table."

        "It's inspiring how you still believe in that.":
            $ ch5_chunghee_speech = "inspiring"
            $ chunghee_affection += 1           # +1 Chung-hee affection

            "I sighed, rubbing the back of my neck."

            dorian "I don't know if I agree with you, Chung… but it's inspiring how you still believe in that."

            "Chung-hee blinked, caught off guard. Then, slowly, a small, grateful smile crossed his face."

            chung_hee "You… You think so?"

            "I nodded."

            dorian "Maybe I've seen too much of the world to believe in nobility anymore… but it's not a bad thing to hold onto."

            "Chung-hee's shoulders eased, some of the tension melting away."

            chung_hee "Then I will prove to you that nobility isn't dead, Dorian."

    jump ch5_divine_weapon


# =============================================================================
# SECTION 26: LABEL CH5_DIVINE_WEAPON — Chung Reveals More / Tea Scene
# =============================================================================

label ch5_divine_weapon:

    "Yuxuan leaned forward, swirling the tea in his cup before raising an eyebrow."

    yuxuan "Chung, if I may ask—why are you alone? Don't Emperors get, like… I don't know, guards or something?"

    "He gestured vaguely with his free hand."

    yuxuan "I remember when the previous Emperor of Kyeongjang visited Tianho. He was flanked by an entire regiment of soldiers."

    "Chung-hee nodded, his gaze distant, as if recalling the memory himself."

    chung_hee "Yes… my father and my mother went to Tianho with an honor guard. His visit was meant to be a grand affair—fanfare, ceremony. His presence symbolized Kyeongjang standing as one with Ena."

    "He let out a quiet breath, then shook his head."

    chung_hee "But I never sought such treatment. King Gustav and I agreed to a Cheonmyeong Gyeol."

    "He paused, glancing at Svante for the briefest moment before looking away."

    chung_hee "So I believed…"

    "His fingers brushed against the table's surface, contemplative."

    chung_hee "I saw no need to march with banners or soldiers. I came alone, as an Emperor of Kyeongjang should in a duel to the death. But Gustav…"

    "His jaw tightened."

    chung_hee "King Gustav did not honor our agreement. He sent his army. His Aldoriths. His soldiers. Assassins."

    "A cold silence settled over the table."

    svante    "I apologize again. Please forgive me, sir. I—"
    chung_hee "No need to apologize. It's the ruler who makes the decisions."
    dorian    "And it led you to us."
    yuxuan    "By the goodness of the Prosperity Dragon, you're still alive. Praise be!"
    niko      "That bastard Gustav. Can you imagine travelling thousands of miles for a duel just for you to be the target of assassination?"

    "Chung-hee reached into the folds of his robes and pulled out a small, ornate object—an amulet, its surface shimmering with emerald green light."

    chung_hee "I didn't travel. If not for this, I would not be here."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "Powerful device detected. Anomaly class: High-tier. Likelihood of survival increase: 89.4%. E-E-E-E-Errr-r-r-r-r-r—"

    play sound sfx_roboto_crash                 # PLACEHOLDER — Roboto crash SFX

    roboto "*crashes*"

    "Yuxuan whistled, leaning in."

    yuxuan "Wow!"
    chung_hee "This was the last thing found on my parents' bodies. Tianho gave to us after the day of the tragedy."
    weng "That's too sad. I'm so sorry Sir Chung."

    "I stared at the amulet, my gaze locked onto its swirling green glow. There was something about it—something calling to me."
    "And then, as if a switch flipped in my mind, I remembered something. The amulet Elias wore back in Mjoll."
    "My breath hitched. Could it be—? Could this have the same power?"
    "No, it couldn't."
    "Yuxuan, of course, was already leaning in, his eyes gleaming with barely contained excitement."

    yuxuan "Chung, is it okay if I touch it?"

    "I rolled my eyes."

    dorian "Yu!"
    weng   "Please forgive my master, Sir Chung."

    "Yuxuan threw up his hands."

    yuxuan "What? I was just asking a question!"

    "Tim suddenly perked up, his small hands clapping together."

    tim   "Can I touch it too, Mister Chung? I promise I'll take good care of it!"
    elias "Me too! And Tedda!"
    tim   "Hey I was first, Elias!"
    weng  "Tim, let the adults talk."

    "Chung-hee blinked, clearly caught off guard by all the attention. He hesitated for a moment before finally nodding."

    chung_hee "Please… be my guest?"

    "Niko raised a brow, folding his arms."

    niko "Your Majest—Chung. You don't have to let him touch your amulet. We know it's sacred."

    "Chung-hee offered a small smile."

    chung_hee "Don't worry, Sir Niko. You all proved that I can trust you with my life. What's a small amulet compared to that?"

    "Yuxuan immediately whooped, fist-pumping the air."

    yuxuan "Yes! Woohoo! Roboto, engage study mode!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "O-o-on it, Master Y-Y-Yuxuan! Engaging scanning proc-proc-process—ERROR! Unstable energy detected! I r-r-recommend caution!"

    "Before Roboto could finish his analysis, Yuxuan had already reached out, his fingertips brushing the amulet's cool, engraved surface."
    "A deep hum pulsed through the air. The sound wasn't just audible—it was something I could feel in my chest, like the distant vibration of a temple bell."
    "Yuxuan's eyes lit up with childlike wonder. He giggled, completely ignoring Roboto's warning."

    yuxuan "Ooooh! This thing is buzzing! You feel that? Dorian! Come! Touch!"
    svante "S-Sir Yuxuan! Are you sure you can touch it like that?"
    yuxuan "Of course! Come on! Touch it, Svante! You too, Niko!"
    niko   "Not interested…"
    tim    "I'm interested!"
    weng   "No, Tim. No."

    "I sighed, pinching the bridge of my nose."

    dorian "Yu, you are way too excited about this."
    yuxuan "Come on, Dorian! Touch it! What's the worst that could happen?"

    "Reluctantly, I reached forward."
    "The moment my fingers made contact—"

    jump ch5_amulet_vision

# =============================================================================
# SECTION 27: LABEL CH5_AMULET_VISION — Dorian Touches the Amulet
# =============================================================================

label ch5_amulet_vision:

    play sound sfx_amulet_vision                # PLACEHOLDER — amulet vision SFX

    dorian "ARRGHHHH!!!"
    niko   "Dorian!"

    # [COMMENT: bg_white_screen — total white, void, endless]
    scene bg_white_screen with flash            # PLACEHOLDER — white screen flash
    stop music fadeout 0.5
    play music ost_amulet_vision fadein 0.5     # PLACEHOLDER — amulet vision theme

    "A shockwave of raw energy erupted through me."
    "A tidal wave of power slammed into my very soul, knocking the breath from my lungs. My vision fractured—splintering like broken glass. My knees buckled."
    "Darkness. Total Darkness."
    "Then, I heard voices. Echoes."
    "A half-naked man with wings."
    "His golden eyes burned with urgency. Feathers glistened under an unseen light, his presence radiant yet commanding."

    magnus "Dragonkin!! We don't have much time!"

    "I staggered backward."

    magnus "They know you're here! Come to me!"

    "His wings flared wide, winds surging from nowhere. The world around me warped, twisted—"
    "Then—"

    # [COMMENT: bg_sealed_door — underground chamber, blood, torchlight — Min-joon's death]
    scene bg_sealed_door with dissolve          # PLACEHOLDER — sealed underground chamber
    stop music fadeout 0.5
    play music ost_minjoon_memory fadein 0.5    # PLACEHOLDER — Min-joon memory theme

    "Blood. Darkness. Betrayal."
    "I saw him."
    "A man, regal yet crumbling—his robes once pristine, now soaked in his own blood."
    "Emperor Min-joon."
    "He was on his knees, gasping, one hand clutching a fatal wound at his side. His breath came in ragged, uneven bursts."
    "Before him—King Gustav."
    "A towering shadow, eyes wild with fury."

    emperor_minjoon "Heh. *coughs*"
    king_gustav     "You… You TOOK AWAY MY ONE CHANCE!"

    "He raised his blade, its tip glistening with Min-joon's blood."

    king_gustav     "You, Olympia, and that damned Long Shen…"
    emperor_minjoon "You… will never… lay your hands… on the Divine Weapon."

    "Gustav's face contorted with unbridled fury. He gripped the hilt of his sword tighter. It glew with a radiant light."

    emperor_minjoon "We… *coughs* made sure that it will… never go to… someone like you…"

    "The underground chamber trembled. Cracks splintered across the stone ceiling."
    "The entire structure was collapsing."
    "Gustav growled, his blade trembling from restraint. The light flickered."

    king_gustav "Tsk… I need to take care of Long Shen first. In the meantime…"

    "He stepped back. He gave a curtsy."

    king_gustav "Enjoy Xianlun, Your Majesty."

    "Min-joon collapsed to the ground, gasping. Blood pooled beneath him, his strength fading."
    "Beside him, a frail, trembling hand reached out."
    "His wife."
    "Tears streamed down her face, but she said nothing—only grasped his hand, smiling. Her grip was weak as blood spilled around her."

    seo_yeon        "I love you, Min-joon."
    emperor_minjoon "Seo-yeon… my love… I'm sorry…"
    seo_yeon        "We'll… be together… in Xianlun…"

    "Min-joon touched the amulet around his neck with his other hand."

    emperor_minjoon "Chung-hee… Jong-hee… I… I hope this gets to you."
    seo_yeon        "Chung… Jong… my precious loves."
    emperor_minjoon "Kyeo… *coughs* The Empire of Kyeongjang is in your hands now, Chung-hee…"
    emperor_minjoon "I'm… sorry… to place this burden on you at such a young age but… *coughs*"
    seo_yeon        "Min-joon my love…"

    "Min-joon's breath hitched."

    emperor_minjoon "I'm sorry…"
    seo_yeon        "We're sorry that we have to leave you both…"
    seo_yeon        "Mom and Dad… will…"
    emperor_minjoon "We… won't be there anymore… Stay strong… For… For Kyeongjang…"
    seo_yeon        "We…"
    emperor_minjoon "We love—"

    "The sound of rubble crashing."
    "Darkness."

    # [COMMENT: bg_white_screen — white void returns]
    scene bg_white_screen with fade             # PLACEHOLDER — white void
    stop music fadeout 0.5
    play music ost_magnus_void fadein 0.5       # PLACEHOLDER — Magnus void theme

    "For a moment, there was nothing—just darkness, emptiness, weightlessness."
    "A blinding white light swallowed everything."
    "Then, slowly, a figure emerged."
    "I could finally see him clearly."
    "The man calling out to me. He took a sharp step forward."

    magnus "Dragonkin! You're alright."

    "I blinked, disoriented."
    "Everything around us was an endless white void. There was no floor, no sky—just vast nothingness."
    "But Magnus—he was real."
    "I tried to steady my breathing."

    dorian "What… just happened? Where am I?"

    "He didn't answer. His golden eyes flickered to something behind me. His wings tensed."

    magnus "It's coming."

    "A shiver crawled down my spine."

    dorian "What is?"

    "Magnus took another step forward, his movements sharp, urgent."

    magnus "No time. You have to find me."
    dorian "Find you? You're right here."

    "His jaw tightened. He turned his head again, scanning the empty space around us."
    "I followed his gaze but saw nothing."

    dorian "Who are you?"
    magnus "I…"

    "For the briefest second, he hesitated."
    "Then, his golden eyes flicked back to mine."

    magnus "Magnus…"
    dorian "Magnus?"
    magnus "Yes… Magnus…It's been a while since anyone called me that…"
    magnus "Time… There's no time…"
    magnus "If you have some questions, please. I'll answer them. Hurry… there isn't enough time."

    jump ch5_magnus_choices


# =============================================================================
# SECTION 28: LABEL CH5_MAGNUS_CHOICES — White Screen: Choices with Magnus
# =============================================================================

label ch5_magnus_choices:

    menu:

        "I saw the vision of the late Kyeongjang Emperor and his wife. Why did I see it?" if not ch5_magnus_q1:
            $ ch5_magnus_q1 = True

            "His expression darkened."
            "A flicker of sorrow crossed his face—but then, just as quickly, he looked away."
            "His wings shifted restlessly."

            magnus "That past is written in blood. I cannot change it."
            magnus "And neither can you, Dragonkin…"
            dorian "Why did I see the vision? Did they send it?"

            "He kept quiet. He does not know."
            "His hands twitched—fingers tightening, as if trying to grasp something unseen."

            magnus "Come find me, Dorian. Before the past claims another soul."
            magnus "Beneath Tianho."

            jump ch5_magnus_choices

        "Do you know what happened during the Tragedy of Tianho?" if not ch5_magnus_q2:
            $ ch5_magnus_q2 = True

            "Magnus flinched."
            "His golden eyes widened—but then, just as quickly, he squeezed them shut, shaking his head."

            magnus "Tianho… You need to find me…"

            "He inhaled sharply, as if the very words burned his throat."

            magnus "No, no… there's no time for this."

            "He spun around, scanning the white abyss. His breath quickened."

            magnus "They're coming… they're trying to get in…"

            "His wings shuddered."
            "Then, he turned back to me, his voice a mere whisper of fire."

            magnus "Come find me, Dorian. Beneath Tianho."

            jump ch5_magnus_choices

        "What is this place?" if not ch5_magnus_q3:
            $ ch5_magnus_q3 = True

            "His movements slowed. His breathing evened."
            "Magnus looked directly at me."

            magnus "This… is your mind."

            "A quiet pause."

            magnus "I speak to you from my place. I cannot leave it."
            magnus "I… I wish I could leave and—"

            "His golden gaze softened—just for a second."
            "Then, suddenly— his body tensed again. The paranoia returned. His wings trembled."

            magnus "No, no, no. There's no time—!"
            magnus "They might get in…. No!"

            "His head snapped toward the unseen horizon, eyes wild."

            magnus "Find me, Dorian! Find me! Beneath Tianho."

            jump ch5_magnus_choices

        "I touched this amulet. What did it do to me?":
            $ ch5_magnus_q4 = True

            "Magnus looked around. He clenched his fists tight."

            magnus "No… There's not enough time…"

            "His voice shook."

            magnus "It's too soon."
            magnus "Come find me, Dorian. Beneath Tianho! Please!"

            jump ch5_magnus_common


# =============================================================================
# SECTION 29: LABEL CH5_MAGNUS_COMMON — Magnus Common / Void Breaks
# =============================================================================

label ch5_magnus_common:

    play sound sfx_void_crack loop              # PLACEHOLDER — void cracking SFX

    "The world quaked around us."
    "A low, guttural rumble crawled through the white void, rising—building—like a storm about to break."
    "Magnus lunged forward, grabbing my wrist with a grip like iron."

    magnus "Please, Dragonkin—Dorian—!"

    "His voice trembled, a raw edge of fear in his tone. His golden eyes were wide, frantic. He squeezed my hand tighter."

    magnus "You're nearer than you think! You must—"

    "The ground lurched. The white space around us fractured, cracks splintering through reality itself."
    "There was a distant thunderous BOOM."
    "The rumbling grew louder—deafening."
    "Magnus' wings flared wide, his breath ragged. He yanked me closer, his nails digging into my skin."

    magnus "HURRY!"

    "Another shuddering crash."
    "The void itself was breaking apart."

    magnus "DO—NOT—FORGET—BENEATH TIANHO—"

    "A final, ear-splitting ROAR."

    jump ch5_nightmare


# =============================================================================
# SECTION 30: LABEL CH5_NIGHTMARE — Yaoguai King Nightmare / End of Chapter
# =============================================================================

label ch5_nightmare:

    # [COMMENT: bg_tianho_on_fire — Tianho burning, nightmare sequence]
    scene bg_tianho_on_fire with flash          # PLACEHOLDER — Tianho on fire
    stop music fadeout 0.5
    play music ost_nightmare fadein 0.3         # PLACEHOLDER — nightmare horror theme

    "Then— the world shattered."
    "Darkness. Cold. Suffocating."
    "Then, there was laughter."
    "A deep, inhuman cackle slithered through the black, curling like smoke."
    "It echoed inside my skull."

    yk "Hahahaha… Dragonkin… don't interfere."

    "The darkness shifted."
    "I saw flashes—distorted, broken images—a nightmare burned into my soul."
    "Blood. Fire. Chains."
    "A towering silhouette loomed before me."
    "The Yaoguai King."
    "His twisted horns curled like a crown, glowing embers crackling beneath his skin. His veins—molten gold—and pulsing."
    "His jagged teeth gleamed as he grinned."

    yk "Do you remember what I took from you last time?"

    "I gasped—choking, drowning—memories crashing over me."

    elara "Dorian! No!"

    "I turned—her face."
    "Terror."
    "Tears in her eyes."

    play sound sfx_chains                       # PLACEHOLDER — chains SFX

    dorian "Elara?! Elara! No!!"

    elara "Dorian! Please don't come! Whatever you do—!"

    "The chains around her wrists tightened."
    "A cry—small, fragile."

    lucas "Daddy! Daddy! Save us!"

    "A surge of fire roared in my veins."
    "I lunged forward—only for chains to slam around my limbs, dragging me down."

    dorian "I… I will! No! No!! Let them go, please! I'll do anything!"

    yk "Hahahaha!"

    "His laughter warped—a monstrous, guttural sound ripping through the void."
    "A shriek—Emily."

    emily "Ahhh!! Daddy!"

    "I thrashed."
    "Chains dug into my flesh."
    "Fire erupted—coursing through my bones—but I couldn't reach them."

    dorian "NO!!! NO!!! AHHHH!!! I'LL KILL YOU!"

    "A chorus of cries—my children."

    "Emily, Sarah, Daniel, Lucas: Daddy! Daddy! Daddy!"

    "Their voices faded."
    "Ripped from my grasp."
    "I screamed."

    scene cg_yaoguai_nightmare with fade        # PLACEHOLDER — cg_yaoguai_nightmare
    pause 2.0

    scene cg_black with fade                    # PLACEHOLDER — black screen
    stop music fadeout 2.0
    stop audio fadeout 1.5

    pause 2.0

    show screen chapter_title_screen(
        "5",
        "Cheng Industries",
        subtitle="END",
        duration=3.0
    )
    pause 3.0

    jump chapter_6


# =============================================================================
# END OF CHAPTER 5
# =============================================================================
