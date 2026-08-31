###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  SCENE: CHAPTER 5 — Cheng Industries
###############################################################################

# =============================================================================
# SECTION 1: CHARACTER DEFINITIONS (NEW FOR CHAPTER 5)
# =============================================================================

# compiled character definitions

# =============================================================================
# SECTION 2: IMAGE DECLARATIONS
# =============================================================================

# compiled bg and cg definitions

# =============================================================================
# SECTION 3: AUDIO DECLARATIONS
# =============================================================================

# --- Music ---
# define audio.ost_tunnel_move     = "audio/music/ost_tunnel_move.ogg"        # PLACEHOLDER
# define audio.ost_cheng_lab       = "audio/music/ost_cheng_lab.ogg"          # PLACEHOLDER
# define audio.ost_niko_faith      = "audio/music/ost_niko_faith.ogg"         # PLACEHOLDER
# define audio.ost_svante_talk     = "audio/music/ost_svante_talk.ogg"        # PLACEHOLDER
# define audio.ost_dinner_warm     = "audio/music/ost_dinner_warm.ogg"        # PLACEHOLDER
# define audio.ost_chung_reveal    = "audio/music/ost_chung_reveal.ogg"       # PLACEHOLDER
# define audio.ost_amulet_vision   = "audio/music/ost_amulet_vision.ogg"      # PLACEHOLDER
# define audio.ost_minjoon_memory  = "audio/music/ost_minjoon_memory.ogg"     # PLACEHOLDER
# define audio.ost_nightmare       = "audio/music/ost_nightmare.ogg"          # PLACEHOLDER

# --- Sound Effects ---
# define audio.sfx_earth_open      = "audio/sfx/sfx_earth_open.ogg"           # PLACEHOLDER
# define audio.sfx_door_scan       = "audio/sfx/sfx_door_scan.ogg"            # PLACEHOLDER
# define audio.sfx_door_chime      = "audio/sfx/sfx_door_chime.ogg"           # PLACEHOLDER
# define audio.sfx_door_open       = "audio/sfx/sfx_door_open.ogg"            # PLACEHOLDER
# define audio.sfx_roboto_beep     = "audio/sfx/sfx_roboto_beep.ogg"          # PLACEHOLDER
# define audio.sfx_roboto_crash    = "audio/sfx/sfx_roboto_crash.ogg"         # PLACEHOLDER
# define audio.sfx_amulet_vision   = "audio/sfx/sfx_amulet_vision.ogg"        # PLACEHOLDER
# define audio.sfx_void_crack      = "audio/sfx/sfx_void_crack.ogg"           # PLACEHOLDER
# define audio.sfx_chains          = "audio/sfx/sfx_chains.ogg"               # PLACEHOLDER
# define audio.sfx_sleep_powder    = "audio/sfx/sfx_sleep_powder.ogg"         # PLACEHOLDER

# # --- Ambient ---
# define audio.amb_tunnel_drip     = "audio/ambient/amb_tunnel_drip.ogg"      # PLACEHOLDER
# define audio.amb_lab_hum         = "audio/ambient/amb_lab_hum.ogg"          # PLACEHOLDER
# define audio.amb_rain_muffled    = "audio/ambient/amb_rain_muffled.ogg"     # PLACEHOLDER
# define audio.amb_kitchen         = "audio/ambient/amb_kitchen.ogg"          # PLACEHOLDER

# =============================================================================
# SECTION 4: GAME VARIABLES
# =============================================================================

# =============================================================================
# SECTION 5: LABEL CHAPTER_5 — Underground Tunnel Walk
# =============================================================================

label chapter_5:
    $ save_name = "Chapter 5"
    play sound audio.amb_underground volume 0.4
    "We pressed forward, the sound of rain muffled by the earth above."
    "The man I carried on my shoulder was heavier than I expected, his weight pressing down on me with every step."
    "I carried the unconscious young man on my shoulder, the scent of his unfamiliar perfume seemed to linger on my nose. Refined, yet foreign."
    "Behind me, Niko walked in silence, his sharp gaze fixed on the unconscious figure. He kept checking his pulse, brushing damp hair away from his face, as if making sure he was still breathing."
    scene bg_underground_dim with Dissolve(2.0)
    show niko normal_base at right_char 
    show dorian neutral at left_char
    with Dissolve(0.2)
    voice audio.niko_ch5_line1
    niko   "Breathing. Good. Looks like the tonic is working."

    "Elias walked beside Yuxuan, his tiny fingers clutching Tedda. The glow from his flower-shaped flashlight cast flickering shadows on the walls, guiding our way."
    hide niko 
    show elias normal_lying at right_char_kids with Dissolve(0.2)
    voice audio.elias_ch5_line1
    elias "Are we there yet, Mister Yuxuan? Tedda's getting tired…"
    tedda "…"

    "Svante, the aldorith, walked near me, shifting anxiously. Every few steps, he would whisper yet another apology, his voice trembling slightly."

    hide elias
    show svante normal_nervous at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line1
    svante "Forgive me for earlier. I'm sorry… I—"

    "Still, the rain poured outside. A distant rumble of thunder echoed above."
    hide svante
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line1
    yuxuan "Here we are… Just open it here. Perfect."

    jump ch5_lab_entrance


# =============================================================================
# SECTION 6: LABEL CH5_LAB_ENTRANCE — Refined Underground Passage
# =============================================================================

label ch5_lab_entrance:
    play sound sfx_earth
    show dorian dragon_eyes at left_char
    "I planted my feet firmly on the damp ground and extended my hand."
    "The earth rumbled beneath my palm, shifting and parting at my command." with vpunch
    scene bg_underground_lit with fade 
    "A section of the tunnel wall crumbled away, revealing an entrance—more refined than the natural cave we had been trudging through."
    "Unlike the crude, damp tunnels of before, this place was structured—a carefully designed underground passage."
    "Electric lights, neatly affixed to the earthen walls, illuminated the space with a warm, steady glow."

    show svante normal_neutral at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line2
    svante "This is amazing… Spectacular, even. I… I had no idea tunnels like these existed in Tianho."

    show yuxuan normal_happy at center_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line2
    yuxuan "These tunnels were built to facilitate the safe and discreet travel of my partnered merchants. They connect key points throughout the region, allowing for the transport of goods and valuable cargo—without attracting unwanted attention."

    show dorian normal_alt_neutral at left_char with Dissolve(0.2)
    voice audio.dorian_ch5_line1
    dorian "Amazing. I wouldn't expect less from Cheng Yuxuan himself."
    hide svante
    show niko normal_base at right_char with Dissolve(0.2)
    voice audio.niko_ch5_line2
    niko   "…Wait a minute. Cheng Yuxuan? You're not just a Yuxuan. You're the Cheng Yuxuan? The renowned inventor?"

    show yuxuan alt_smile at center_char
    voice audio.yuxuan_ch5_line3
    yuxuan "The one and only. Pleasure to make your acquaintance."

    show niko normal_smile at right_char
    voice audio.niko_ch5_line3
    niko   "No wonder you have enough coin to facilitate the construction of all these tunnels. How much did it cost? It must have been a sizeable fortune."

    show yuxuan normal_happy at center_char
    voice audio.yuxuan_ch5_line4
    yuxuan "Haha. Thanks, but these tunnels have been here for a while now. Me and my partners just happened to stumble on it by accident."
    voice audio.yuxuan_ch5_line5
    yuxuan "It would have been a waste if these tunnels just collected dirt. So, we at Cheng Industries decided to convert it to a passageway."

    "There was silence—then—"

    hide niko
    show svante normal_happy at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line3
    svante "CHENG INDUSTRIES?! YOU'RE THAT CHENG YUXUAN?!"

    "Svante was shrieking in excitement, his eyes sparkling. He grabbed Yuxuan's sleeve like an excited child."
    voice audio.svante_ch5_line4
    svante "This… This can't be real! You—you're the genius behind the delivery bots! The man who revolutionized steam-powered mechanisms from Mjoll! You— you saved me and my mother! I— I don't even know what to say! I—"

    "His words tumbled out in an excited, breathless mess, his face glowing with genuine admiration."
    show svante alt_base at right_char
    voice audio.svante_ch5_line5
    svante "During the great blizzard… when our food ran out… the relief packages from Cheng Industries saved us. We were going to die, sir! But your shipments—your generosity—we lived because of you."

    "His hands clenched against his chest, his lip trembling as he blinked rapidly, clearly fighting back tears."
    hide svante
    show elias normal_neutral at right_char_kids with Dissolve(0.2)
    voice audio.elias_ch5_line2
    elias "Tedda, why is he crying?"
    tedda "..."
    hide elias

    show yuxuan normal_neutral at center_char
    show svante normal_happy at right_char with Dissolve(0.2)
    "Yuxuan rubbed the back of his neck."

    voice audio.yuxuan_ch5_line6
    yuxuan "…Uh. Right. Well. Glad to hear that. No need to make this weird."
    voice audio.svante_ch5_line6
    svante "B-But you're amazing—"
    hide svante
    show niko normal_base at right_char with Dissolve(0.2)
    voice audio.niko_ch5_line4
    niko   "Kid, breathe. The last thing I need is another patient."

    jump ch5_yuxuan_lab


# =============================================================================
# SECTION 7: LABEL CH5_YUXUAN_LAB — Entry into the Lab / Door Sequence
# =============================================================================

label ch5_yuxuan_lab:

    # [COMMENT: bg_underground_door — massive polished metal door, no handles]
    # scene bg_underground_door with dissolve     # PLACEHOLDER — lab entrance door

    stop audio fadeout 1.0
    scene underground_door with fade
    "We stopped at a massive door made out of polished metal, gleaming under the artificial lighting. It beared no handles or visible keyholes."
    "As we stepped closer, a sudden hum resonated from within. A thin, radiant crimson beam of light flickered to life, sweeping across Yuxuan's face with meticulous precision. Yuxuan remained perfectly still."
    "Then, the door spoke."

    # play sound sfx_door_scan                    # PLACEHOLDER — door scan SFX

    voice audio.door_ch5_line1
    door_voice "Attention. Facial recognition is currently in progress. Please be advised that excessive movement may disrupt this unit's sensors and may impact the accuracy of identity verification. Please refrain from doing so. Thank you for your understanding."
    show underground_door_scan with dissolve
    "A pause. The crimson light pulsed. Then—"
    voice audio.door_ch5_line2
    door_voice "Initiating secondary verification. Please present a valid voice signature."
    "Yuxuan exhaled sharply before speaking in a smooth, practiced tone."
    hide underground_door_scan with dissolve
    show yuxuan normal_neutral at center_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line7
    yuxuan     "Cheng Yuxuan. Authorizing entry."

    "The door whirred, but did not yet open."

    voice audio.door_ch5_line3
    door_voice "Processing… Additional security measures activated. Please provide a biological confirmation."

    "Without hesitation, Yuxuan pressed his palm against the cold metal."

    voice audio.door_ch5_line4
    door_voice "Analyzing genetic markers. Matching results with stored biological data."

    # play sound sfx_door_chime                   # PLACEHOLDER — door chime SFX

    voice audio.door_ch5_line5
    door_voice "Identity confirmed. Welcome home, Master Yuxuan. May the blessings of the Prosperity Dragon be with you today."
    voice audio.door_ch5_line6
    door_voice "Here at Cheng's we bring change. As per your request, this unit will not play the Cheng Industries jingle."

    show svante normal_happy at right_char with Dissolve(0.2)
    svante "Here at Cheng's, we bring change—"

    # [COMMENT: bg_yuxuan_lab — spacious lab, lived-in comfort, screens on walls]
    # play sound sfx_door_open                    # PLACEHOLDER — door opening SFX
    # scene bg_yuxuan_lab with dissolve           # PLACEHOLDER — Yuxuan's lab main room

    # play music ost_cheng_lab fadein 2.0         # PLACEHOLDER — warm lab theme
    # play audio amb_lab_hum loop fadein 1.5      # PLACEHOLDER — lab ambient hum
    
    "With a deep, mechanical thunk, the massive door finally split apart, revealing a sterile yet inviting interior."
    scene lab_cave_off with fade
    "A rush of cool, crisp air greeted us as the passageway opened. The lighting inside was dimmed but warm, perfectly illuminating the space beyond."
    "We stepped inside, one by one."
    "It looked… comfortable."
    "The room was spacious, lined with sleek furniture, and had the distinct coziness of a lived-in space rather than the cold sterility of a scientific lab."
    "A few shelves were stacked with books, blueprints, and small trinkets, while elegant screens displayed various data across the walls."
    scene lab_cave_on with dissolve
    show yuxuan normal_happy at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line8
    yuxuan "There we are. Home sweet home."

    show dorian normal_alt_neutral at left_char with Dissolve(0.2)
    voice audio.dorian_ch5_line2
    dorian "Where should we put him?"

    show yuxuan normal_neutral at right_char
    voice audio.yuxuan_ch5_line9
    yuxuan "Roboto will escort you to the spare room. Roboto! Come here."

    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    "At his command, a small mechanical figure whirred to life from the corner of the room."
    "With a series of cheerful beeps, a scrappy little robot wobbled its way toward us, its monitor-like face flickering before settling into a bright, pixelated smile."

    show roboto happy at center_robot with Dissolve(0.2)
    # line 1 (1)
    voice audio.roboto1_ch5_line1
    roboto "You called, Master Yuxuan? Roboto is here. At your service."

    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line10
    yuxuan "Can you show these people to the spare room?"

    "Roboto's screen shifted, displaying a large question mark before flickering back to its usual expression."

    show roboto bad_mood at center_robot
    voice audio.roboto1_ch5_line2
    roboto "Which spare room, Master Yuxuan?"
    show yuxuan normal_neutral at right_char
    voice audio.yuxuan_ch5_line11
    yuxuan "Any spare room, Roboto. Now. It's urgent."
    show roboto happy at center_robot
    voice audio.roboto1_ch5_line3
    roboto "Certainly, Master Yuxuan."
    hide roboto
    hide yuxuan
    show svante normal_happy at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line7
    svante "A… A robot servant? A talking real-life robot servant? This is… AMAZING!!"
    hide svante
    show elias normal_happy at right_char_kids with Dissolve(0.2)
    voice audio.elias_ch5_line3
    elias "Daddy, daddy, look! A robot!"
    show roboto happy at center_robot with Dissolve(0.2)
    "Roboto tilted its small head toward them, its screen displaying a cheerful expression."

    voice audio.roboto1_ch5_line4
    roboto "Precisely. I am a robot. I am Master Yuxuan's r-r-robot companion. I can be whatever he wants… A butler. A cleaner. Or even his own personal c-c-c-c…"
    voice audio.roboto1_ch5_line5
    roboto "…chef if need be."

    show elias alt_joy at right_char_kids
    "Elias let out an excited squeal, making Tedda bounce in his grasp."
    voice audio.elias_ch5_line4
    elias "Ooohhh, so cute! Mister Roboto, do you wanna play with me and Tedda?"

    "Roboto's head twitched slightly as it processed the request."

    # line 06 (1) end
    show roboto happy at center_robot
    voice audio.roboto1_ch5_line6
    roboto "Certainly! My b-b-b-built-in intelligence allows me to play a wide v-v-variety of games. S-Seeing that you are a child, might I suggest a game of 'tag'?"

    show dorian normal_alt_neutral at left_char with Dissolve(0.2)
    voice audio.dorian_ch5_line3
    dorian "Don't touch the robot, Elias. Take a seat and wait for us…"

    show elias normal_sad at right_char_kids
    "Elias pouted but obeyed, hugging Tedda close."
    hide elias 
    hide roboto
    with Dissolve(0.1)
    "Then—"

    show svante normal_neutral at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line8
    svante "…Wait… W-Wait a minute…"

    "His excitement drained in an instant. His gaze sharpened."

    show svante normal_nervous at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line9
    svante "Elias? Elias?!"

    "His eyes darted toward me, then back to the child. He took a shaky step backward."

    show svante normal_angry at right_char
    voice audio.svante_ch5_line10
    svante "Y-You're Elias Drakos?!"

    "Elias nodded his head and innocently nodded Tedda's head as well."
    hide svante
    show elias normal_happy at right_char_kids with Dissolve(0.2)
    voice audio.elias_ch5_line5
    elias "That's me! And this is Tedda. We're best friends. And that's my Daddy right there."

    "Svante's face drained of all color. He suddenly looked sick. His entire body stiffened, his expression twisted with disbelief. His hand shot up, pointing straight at Elias."
    hide elias 
    show svante normal_angry at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line11
    svante "What are you doing here?! Why are you dressed up like a girl?!"

    "His voice cracked as he turned his trembling hand toward me, realization crashing over him like a tidal wave."

    voice audio.svante_ch5_line12
    svante "I—I knew something was off when you channeled draconic fire!"
    voice audio.svante_ch5_line13
    svante "Y-You're the Massacrer of Mjoll!"
    voice audio.svante_ch5_line14
    svante "You… You murdered Count Vasily… My brothers… My sisters…."
    voice audio.svante_ch5_line15
    svante "K-Kristin…"

    "A hush fell over the room, heavy and suffocating."
    "Svante's chest rose and fell rapidly, his gaze darting wildly. Desperation clawed at his voice as he turned to the others."
    voice audio.svante_ch5_line16
    svante "Everyone, we're not safe here! This man—"

    # play sound sfx_sleep_powder                 # PLACEHOLDER — sleep powder SFX

    "A swift movement—Yuxuan stepped forward and flicked a handful of shimmering powder straight into Svante's face."
    "The reaction was instant."
    "His words faltered, his body swaying. He blinked sluggishly."

    show svante normal_sad at right_char
    voice audio.svante_ch5_line17
    svante "Wh… What?"

    "His knees buckled. With a soft thud, he collapsed onto the floor."
    "A moment of silence."

    hide svante
    voice audio.svante_ch5_line18
    svante "Zzz… Zzz…."

    show yuxuan alt_smile at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line12
    yuxuan "You can never have too much sleeping powder."

    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    "Roboto's screen flickered. A sleeping face with Zs on top."

    show roboto bad_mood at center_robot 
    # line 01
    voice audio.roboto_ch5_line1
    roboto "I detect sudden drowsiness. Should I-I-I activate tuck-in mode?"
    hide yuxuan
    show niko normal_base at right_char with Dissolve(0.2)
    voice audio.niko_ch5_line5
    niko   "No. No, no, no. Right now, we need to get to the spare room. We have a man that needs treatment."

    show roboto happy at center_robot
    voice audio.roboto_ch5_line2
    roboto "Ah! Of course. Prioritizing medical emergency. Please follow me."

    "The little robot turned sharply and began leading the way down the corridor."
    "I adjusted the unconscious man in my arms and followed."
    "As we walked, Yuxuan grabbed Svante by the collar and dragged him effortlessly across the floor."
    hide roboto
    show yuxuan normal_neutral at center_char
    voice audio.yuxuan_ch5_line13
    yuxuan "I'll take this one to the storage room. I'll have to call Miss Weng first."

    "He shot me a knowing glance before disappearing into the shadows with Svante in tow."
    voice audio.svante_ch5_line19
    svante "Zzz… *mumbles something incoherent* Zzz…."

    jump ch5_spare_room


# =============================================================================
# SECTION 8: LABEL CH5_SPARE_ROOM — Chung-hee Stabilized
# =============================================================================

label ch5_spare_room:

    # [COMMENT: bg_lab_bedroom — warm spare room, lone bed, wooden chair]
    # scene bg_lab_bedroom with dissolve          # PLACEHOLDER — lab spare bedroom
    scene spare_room_off with fade
    "We entered the spare room, finding ourselves in yet another well-furnished and comfortable space. The lighting was soft, casting a warm glow over the neatly arranged furniture."
    "A lone bed sat in the corner, its sheets crisp and clean, with a sturdy wooden chair positioned beside it."
    scene spare_room with dissolve

    show roboto happy at center_robot with Dissolve(0.2)
    voice audio.roboto_ch5_line3
    roboto "H-H-Here is guest r-room number one. P-Please make yourselves comfortable. If you need something, please don't hesitate to contact me."

    "I gently lowered the man onto the bed. His head lolled slightly before settling against the pillow."

    show niko normal_base at right_char 
    show dorian neutral at left_char
    with Dissolve(0.2)
    "Niko was at his side in an instant, fingers pressing against his wrist. He frowned in concentration, waiting, feeling."

    voice audio.niko_ch5_line6
    niko "He's alright. His pulse is steady. He just needs rest."

    "He pulled the blankets up to the young man's shoulders, tucking him in with practiced care. But there was a lingering uncertainty in Niko's expression—he wasn't satisfied just yet."
    "He looked at the little robot whirring around the room."

    show niko normal_base at right_char
    voice audio.niko_ch5_line7
    niko   "Excuse me, what should we call you again?"

    show roboto happy at center_robot
    voice audio.roboto_ch5_line4
    roboto "R-R-Robotooo. Robot with an 'o'. Roboto."

    voice audio.niko_ch5_line8
    niko   "Do you have some water here?"

    "Roboto perked up, its monitor face flashing a bright question mark before flickering back to its usual cheerful expression."

    show roboto malfunction at center_robot
    voice audio.roboto_ch5_line5
    roboto "Warm… or… C-C-Cold? Does it need to be p-p-purified?"

    show niko alt_base at right_char
    voice audio.niko_ch5_line9
    niko   "Warm water is fine. Can you put it in a pitcher and bring us some cups?"

    show roboto happy at center_robot
    voice audio.roboto_ch5_line6
    roboto "No problemooo!!! You can count on Roboto~"

    "With an excited little whirl of its gears, Roboto scurried out of the room, leaving me alone with Niko."
    hide roboto with Dissolve(0.2)

    "Niko exhaled and reached into the leather parcel slung across his chest. With a practiced motion, he unfastened it and pulled out a handful of small, round seeds."
    "They rested in his palm, barely larger than pebbles, their dark shells smooth and unassuming."
    "The air in the room shifted ever so slightly, carrying the faint, fresh scent of damp earth and blooming leaves."
    "The seeds stirred in his palm."
    "Slowly, their shells cracked open, delicate green shoots emerging like tiny fingers reaching toward the sky."
    "Within seconds, the fragile sprouts twisted and lengthened, their stems strengthening, their leaves unfurling."
    "Niko carefully placed them on the nightstand beside the bed, arranging them in a small clay dish that had been sitting unused."

    show dorian neutral at left_char with Dissolve(0.2)
    voice audio.dorian_ch5_line4
    dorian "…You're using nature channeling again?"
    show niko normal_serious at right_char
    voice audio.niko_ch5_line10
    niko   "It's not enough that he's breathing. He needs to recover properly."

    "With another wave of his hand, the young plants continued to grow. They bloomed into delicate white blossoms, their petals trembling slightly as if breathing in the room's air."

    show niko normal_base at right_char
    voice audio.niko_ch5_line11
    niko "These flowers release a mild healing essence. It should help his body recover faster, strengthen his energy flow, and ease any lingering strain on his energy."

    "He reached out and lightly pressed his fingers against the unconscious man's forehead. A soft green glow flickered at the tips of his fingers before dissipating into the young man's skin."
    "The young man shifted slightly, his expression relaxing as if a deep tension had left him. His breathing became more even."

    chung_hee "…"

    show niko normal_smile at right_char
    voice audio.niko_ch5_line12
    niko "Good. He's stabilizing."

    "He adjusted the blankets again, making sure the man was warm but not overheated. Then he sat back with a quiet sigh."

    show dorian neutral at left_char
    voice audio.dorian_ch5_line5
    dorian "You're really thorough with this."
    show niko normal_base at right_char
    voice audio.niko_ch5_line13
    niko   "… Just being careful."

    "He looked at the man."

    show niko normal_sad at right_char
    voice audio.niko_ch5_line14
    niko "I've seen this before. People pushing themselves past their limits, burning through their energy until there's nothing left. Some never recover."

    "A brief silence stretched between us. Maybe now was a good time to talk to him."

    show niko normal_base at right_char
    jump ch5_niko_choices


# =============================================================================
# SECTION 9: LABEL CH5_NIKO_CHOICES — Talking with Niko (Choices)
# =============================================================================

default niko_assistance = False
default niko_raven      = False
default niko_meeting    = False

label ch5_niko_choices:

    menu:
        "Thank him for his assistance earlier." if not niko_assistance:
            $ niko_assistance = True
            show dorian normal_alt_neutral at left_char
            dorian "You didn't have to help back there. But you did. So… thanks."
            show niko normal_base at right_char
            voice audio.niko_ch5_line15
            niko   "Don't mention it. It's my duty."
            dorian "Your duty?"
            voice audio.niko_ch5_line16
            niko   "I was a doctor before."
            voice audio.niko_ch5_line17
            niko   "Trained for years under some of the best healers in my clan. Medicine was my life."
            show dorian normal_alt_calm at left_char
            "I blinked."

            show dorian neutral at left_char
            voice audio.dorian_ch5_line6
            dorian "A doctor? I figured you had medical experience, but I didn't think you were trained formally."

            "He let out a low chuckle."

            show niko normal_smile at right_char
            voice audio.niko_ch5_line18
            niko   "What, you thought I just had a natural talent for it?"
            show dorian neutral at left_char
            voice audio.dorian_ch5_line7
            dorian "With the way you worked? Yeah, I wouldn't have been surprised."
            show niko normal_base at right_char
            voice audio.niko_ch5_line19
            niko   "Where I come from, healers aren't just people who stitch wounds and mix herbs. We had to know how to fight too."
            voice audio.niko_ch5_line20
            niko   "You can't save lives if you're dead, after all."

            "He smirked slightly. His gaze drifted to his hands."
            "His fingers flexed slightly, and for the first time, I got a clear look at the intricate symbols running along his arm. Runes—etched like ink, wrapping around. They weren't familiar. They weren't decorative."

            show dorian normal_alt_neutral at left_char
            voice audio.dorian_ch5_line8
            dorian "Those runes on your hands… I haven't seen them before."
            show niko normal_serious at right_char
            voice audio.niko_ch5_line21
            niko   "No. They're protective runes. A gift. Or maybe a curse. Depends on who you ask."

            "He turned his hand over, the runes catching the dim light of the room."

            show niko alt_base at right_char
            voice audio.niko_ch5_line22
            niko "They help me control my shadows."

            "His voice trailed off, and for a brief second, I swore I saw something shift behind him. A flicker of darkness, barely noticeable, curling at the edges of his silhouette like something alive."
            "Then it was gone."

            show dorian normal_alt_neutral at left_char
            voice audio.dorian_ch5_line9
            dorian "Where did you get them?"
            show niko normal_base at right_char
            voice audio.niko_ch5_line23
            niko   "Hamatame. A village deep in the mountains of the kingdom of Hinami. The Village of Shadows."
            show dorian neutral at left_char
            voice audio.dorian_ch5_line10
            dorian "I see. I haven't been to Hinami before."
            show niko normal_smile at right_char
            voice audio.niko_ch5_line24
            niko   "You should. The beaches are terrific this time of the year."
            show dorian smile at left_char
            voice audio.dorian_ch5_line11
            dorian "Haha. Maybe. Thanks."

            jump ch5_niko_choices

        "Ask him how he turned into a raven." if not niko_raven:
            $ niko_raven = True
            "I shifted slightly, glancing at him."

            show dorian normal_alt_neutral at left_char
            voice audio.dorian_ch5_line12
            dorian "I've been meaning to ask you this… How—how did you turn into a raven?"

            show niko normal_smile at right_char
            "He smirked, clearly amused."

            voice audio.niko_ch5_line25
            niko   "Didn't I already tell you?"
            show dorian normal_alt_calm at left_char
            
            "I crossed my arms."

            voice audio.dorian_ch5_line13
            dorian "I've seen nature channelers before. Hell, I've fought against them. They can summon beasts, enhance their senses, even morph parts of their bodies. But none of them could fully transform."
            show dorian serious at left_char
            "I narrowed my eyes."
            show dorian neutral at left_char
            voice audio.dorian_ch5_line15
            dorian "You don't just shift. You become the animal. How?"

            "Niko leaned back, arms resting lazily behind his head."

            show niko alt_base at right_char
            voice audio.niko_ch5_line26
            niko "It's part of my clan's bloodline ability. Clan Kaibig is… different. We don't just borrow nature's gifts—we embody them."
            voice audio.niko_ch5_line27
            niko "It's about becoming. We don't just take on the form. We take on the instincts. The senses. The mind."
            voice audio.niko_ch5_line28
            niko "Some in our clan dedicate their lives to mastering every single animal form - hundreds of them. They become the creatures they study, forsaking everything else."

            show dorian neutral at left_char
            voice audio.dorian_ch5_line16
            dorian "What about you?"

            show niko normal_sad at right_char
            "His smirk faded slightly. He glanced at the unconscious man, then back at me."

            voice audio.niko_ch5_line29
            niko "It's not my priority. I have a different calling."

            jump ch5_niko_choices

        "Ask him about our first meeting."if not niko_meeting:
            $ niko_meeting = True
            "I looked at him, searching his face for some kind of recognition."

            show dorian normal_alt_neutral at left_char
            voice audio.dorian_ch5_line17
            dorian "You said we've met before? Sorry… I don't remember."
            show niko normal_base at right_char
            voice audio.niko_ch5_line30
            niko   "Tianho. You were with Paladin Cyrus. I was with my brother, Kaito."
            show dorian normal_alt_calm at left_char
            "I blinked. Tianho. That name carried echoes of fire and screaming, the weight of bodies hitting the ground before I could even process what was happening."
            "My mind clawed at the memories, but all I could grasp was the scent of burning flesh and the metallic tang of blood."
            "Elara. My family. Yuxuan. The Emperor of Kyeongjang. Paladin Cyrus. Vasily. Gao. Jiang. King Long Shen. Empress Olympia."
            "I don't recall meeting Niko. Or his brother."

            show dorian sad at left_char
            voice audio.dorian_ch5_line18
            dorian "Tianho… That was years ago."
            show niko normal_base at right_char
            voice audio.niko_ch5_line31
            niko   "Kaito wanted to be the translator for the Emperor of Kyeongjang's son. The deaf-mute son of the Emperor."

            "I frowned, trying to piece together the fragments."

            show dorian serious at left_char
            voice audio.dorian_ch5_line19
            dorian "I'm very sorry. I still don't remember. But I do recall the auditions. Long lines. Hundreds of people waiting for a chance to serve."
            show niko normal_base at right_char
            voice audio.niko_ch5_line32
            niko   "Yes. The line was massive. Even though we didn't get the chance."
            voice audio.niko_ch5_line33
            niko   "Paladin Cyrus had an issue with us. He has an issue with all followers of the Death God."

            "I hesitated before asking."

            show dorian neutral at left_char
            voice audio.dorian_ch5_line20
            dorian "So… Kaito. He's a follower of the Death God too?"

            show niko normal_serious at right_char
            "Niko's fingers twitched."

            voice audio.niko_ch5_line34
            niko   "Yes. But biologically speaking, he's also my brother."
            show dorian neutral at left_char
            voice audio.dorian_ch5_line21
            dorian "So… where is he now?"

            show niko normal_sad at right_char
            "Niko didn't answer immediately. Instead, he exhaled slowly through his nose. He tightened his fist and stared at the runes etched along his arm."

            voice audio.niko_ch5_line35
            niko   "He's with Enoch now. In Xianlun. Paradise."

            "I looked down. The air grew thick, like the room had suddenly shrunk."

            show dorian sad at left_char
            voice audio.dorian_ch5_line22
            dorian "I'm sorry to hear that."
            show niko normal_base at right_char
            voice audio.niko_ch5_line36
            niko   "Don't worry about it."

            "A long silence stretched between us. Then, slowly, Niko reached out, his fingers grazing the petals of the flowers surrounding the unconscious man."

            voice audio.niko_ch5_line37
            niko "The flowers seem to be working. He just needs rest, and he'll be okay."

            jump ch5_niko_choices

        "Ask him about his faith in the Death God.":

            show dorian normal_alt_neutral at left_char
            voice audio.dorian_ch5_line23
            dorian "You're a follower of the death god, right?"

            show niko normal_base at right_char
            "Niko looked down at his half-robe."

            voice audio.niko_ch5_line38
            niko "Haven't I already told you? But yes. Yes, I am. It's no secret—I'm a member of the Prophets."

            "The moment he said it, my vision blurred. My breathing hitched."

            jump ch5_niko_common


# =============================================================================
# SECTION 10: LABEL CH5_NIKO_COMMON — Niko Faith / Tianho Memory
# =============================================================================

label ch5_niko_common:

    # play music ost_niko_faith fadein 1.5        # PLACEHOLDER — somber faith theme

    # [COMMENT: bg_tianho_on_fire — Tianho burning, crowds screaming — memory flash]
    # scene bg_tianho_on_fire with flash          # PLACEHOLDER — Tianho on fire (memory)
    scene bg_tianho_city_on_fire at flashback_filter_enter
    with flash

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
    voice audio.cyrus_ch5_line1
    cyrus"Dorian, you evacuate the city. I'll deal with the winged monster."
    voice audio.dorian_ch5_line24
    dorian  "Cyrus, you can't—"
    voice audio.cyrus_ch5_line2
    cyrus "Listen to me. This city still needs a future, and that future doesn't happen unless someone stops that thing."

    "Tetrad above. He was never seen again."

    # [COMMENT: bg_lab_bedroom — back to spare room]
    scene spare_room with fade              # PLACEHOLDER — lab bedroom

    show niko normal_base at right_char
    show dorian serious at left_char
    with Dissolve(0.2)
    "Niko took a step closer."

    voice audio.niko_ch5_line39
    niko "Are you alright, Dorian?"

    "I exhaled sharply, shaking my head, trying to push past the echoes clawing at my mind. My fists clenched."
    "I looked at him, my voice tight."

    show dorian angry at left_char
    voice audio.dorian_ch5_line25
    dorian "Why? Why do you worship such a deity?"
    voice audio.dorian_ch5_line26
    dorian "Surely you were there that night. The night of the tragedy. You saw what happened."

    "A beat of silence. Then another."
    "The flames still danced behind my eyes, the screams still clawed at my ears."

    voice audio.dorian_ch5_line27
    dorian "Those people… They died because of your god."

    "Niko didn't speak right away. Instead, he stepped forward and placed a firm hand on my shoulder."

    show niko normal_serious at right_char
    voice audio.niko_ch5_line40
    niko "You might wanna sit down for this, Dorian."

    "I resisted at first. My blood still burned, my hands still trembled with the weight of old memories."
    "Reluctantly, I sank onto the chair."

    show dorian serious at left_char
    "He reached into a small folded pouch at his side and pulled out a worn pamphlet."
    hide dorian
    hide niko
    with Dissolve(0.2)

    show floating_note at note_pop with Dissolve(0.3)
    ""
    hide floating_note with Dissolve(0.1)

    show dorian neutral at left_char with Dissolve(0.2)
    voice audio.dorian_ch5_line28
    dorian "These are… lovingly made. Did you make these?"
    show niko normal_base at right_char with Dissolve(0.2)
    voice audio.niko_ch5_line41
    niko   "No. These were drawn by the orphans we took in."
    voice audio.niko_ch5_line42
    niko   "Children who lost everything—their homes, their families, their past. Me, Kaito and a few other Prophets gave them shelter, a place to start again."
    voice audio.niko_ch5_line43
    niko   "Me and my fellow brothers in Enoch keep one of these just in case we have the opportunity to share our faith."

    "There's a certain purity and warmth in Niko's beliefs that is undeniably endearing."
    "If only his faith were centered around a different deity, like the Tetrad for example, and not the one associated with the events in Tianho, I would have wholeheartedly embraced and admired his devotion."

    show dorian neutral at left_char
    voice audio.dorian_ch5_line29
    dorian "There are lots of drawings here. What's this have to do with the death god?"
    show niko normal_base at right_char
    voice audio.niko_ch5_line44
    niko   "Well, as we all know, the death god is not a static entity but is reincarnated again and again, much like the cycle of life and death it oversees."

    "I ran a thumb over the painted pages, my chest still tight."

    show dorian neutral at left_char
    voice audio.dorian_ch5_line30
    dorian "So, you worship all of the reincarnations of the death gods. Not just Enoch?"
    show niko alt_base at right_char
    voice audio.niko_ch5_line45
    niko   "Precisely. We worship the death god as an entity. However, the most prominent reincarnation of the death god is Enoch of Mjoll."
    voice audio.niko_ch5_line46
    niko   "Many historians agree that Enoch was the cause of the many changes in Ena: the downfall of the civilization of Kyeongjang, the fall of the tyrant king in Mjoll, the disappearance of the Tetrad gods and the immortal dragons, the abolishment of slavery in the Centennial Isles, and the list goes on."
    voice audio.niko_ch5_line47
    niko   "He shows the capacity of mankind. He may be a god, but he is also human. Both capable of doing good, and bad. Light and dark. Life and death."
    show dorian neutral at left_char
    voice audio.dorian_ch5_line31
    dorian "I appreciate your explanation about Enoch, but what does this have to do with the death god not being related to the incident in Tianho?"
    show niko normal_base at right_char
    voice audio.niko_ch5_line48
    niko   "In Enoch's final moments, as he lay on his dying bed, he made a solemn vow to his best friend. He swore that in his next lives, he would do everything within his power to right the wrongs he had committed while he was alive."
    voice audio.niko_ch5_line49
    niko   "In response to Enoch's oath, his best friend swore a solemn promise of his own. He pledged to seek out the future incarnations of the death gods and guide them toward a path of greater benevolence and good."
    voice audio.niko_ch5_line50
    niko   "And thus, from those ancient promises, the Prophets of the Death God were founded. A dedicated group of individuals who have taken it upon themselves to seek out and guide the incarnations of the death god, nurturing their potential for benevolence and compassion."
    voice audio.niko_ch5_line51
    niko   "I am proud to be one of those people. This is my calling."
    show dorian neutral at left_char
    voice audio.dorian_ch5_line32
    dorian "Interesting. How many death gods were influenced by the prophets?"
    show niko normal_base at right_char
    voice audio.niko_ch5_line52
    niko   "The first sighting we had was five years ago on Tianho. Our brothers tried to help him, but alas, he was already killed."

    "Five years ago?!"

    show dorian serious at left_char
    voice audio.dorian_ch5_line33
    dorian "Five years ago? That's... surprising. I thought you said that the Prophets were founded four centuries ago. I would have expected the prophets to have encountered and influenced multiple death gods by now."
    show niko normal_base at right_char
    voice audio.niko_ch5_line53
    niko   "We were. The Prophets have transitioned into a charity organization after the first century it was established. Many of us have already believed that death god's work is complete."
    voice audio.niko_ch5_line54
    niko   "So, you can imagine the excitement all of us prophets have when the sighting has been made five years ago."

    "I could imagine it, all right."
    "Four hundred years of waiting, of fading purpose—then suddenly, proof. A reason to move."

    show dorian neutral at left_char
    voice audio.dorian_ch5_line34
    dorian "And now you're investigating that sighting. Because you don't believe the creature that destroyed Tianho was the Death God."
    show niko alt_tense at right_char
    voice audio.niko_ch5_line55
    niko   "Exactly."
    show dorian neutral at left_char
    voice audio.dorian_ch5_line35
    dorian "Have you gotten any leads?"

    show niko alt_disappointed at right_char
    "Niko shook his head, frustration evident in the way his fingers curled slightly."

    voice audio.niko_ch5_line56
    niko "None. We've searched outside of Tianho. We scoured Gale, Hinami, the borderlands. But there's nothing. No traces. No patterns."
    voice audio.niko_ch5_line57
    niko "Something isn't right, Dorian. We're missing something. We just don't know what."

    "Before I could respond, a familiar whirring sound filled the room."

    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    "The little machine rolled in with a tray, a neat pitcher of warm water and a stack of cups balanced with near-perfect precision. Its screen flickered, displaying an animated image of water being poured."

    show roboto happy at center_robot with Dissolve(0.2)
    voice audio.roboto_ch5_line7
    roboto "Beep-boop! R-r-r-Roboto has arrived with water delivery!"
    show niko normal_base at right_char
    voice audio.niko_ch5_line58
    niko   "Roboto, lower your voice."

    "The robot's screen immediately switched to a large 'shhh' icon, accompanied by the sound of static mimicking a whisper."

    show roboto bad_mood at center_robot
    voice audio.roboto_ch5_line8
    roboto "Activating silent mode… Shhhh…."

    "It turned back to us, its voice now hushed."

    show roboto happy at center_robot
    voice audio.roboto_ch5_line9
    roboto "H-H-Here is your water, sir. Warm, just as you've requested."
    show niko normal_base at right_char
    voice audio.niko_ch5_line59
    niko   "Thank you. Just place it beside me, please."

    "It wobbled forward, carefully placing the tray on the small bedside table. The screen changed again, now showing a satisfied-looking pitcher giving a thumbs-up."

    show roboto happy at center_robot
    voice audio.roboto_ch5_line10
    roboto "Mission accomplished! Would you like Roboto to stay and provide additional hydration support?"
    show dorian neutral at left_char
    voice audio.dorian_ch5_line36
    dorian "Hydration support?"
    show roboto happy at center_robot
    voice audio.roboto_ch5_line11
    roboto "Roboto can monitor water levels! Fluff pillows! Tuck in patients! Or… or… tell a bedtime story!"
    show dorian neutral at left_char
    voice audio.dorian_ch5_line37
    dorian "Stories, huh? Interesting."

    show niko normal_base at right_char
    "Niko yawned, stretching his arms."

    voice audio.niko_ch5_line60
    niko "You can stay if you want. Nothing else to do but keep watch."

    "Roboto's screen changed again, now displaying a small clock icon."

    show roboto happy at center_robot
    voice audio.roboto_ch5_line12
    roboto "Oh! Speaking of time—it's almost dinner! Master Yuxuan is currently looking for you in the living room, Sir Dorian."

    "I glanced at Niko, who was already sinking back into his chair, stretching his legs out with a quiet sigh."

    show niko normal_base at right_char
    voice audio.niko_ch5_line61
    niko "Go ahead. I'll keep watch here."

    "I gave him a nod before stepping out, leaving Roboto standing beside the bed, its screen flickering between a neutral expression and a 'standby mode' prompt."

    show roboto happy at center_robot
    voice audio.roboto_ch5_line13
    roboto "Please g-g-g-g-go ahead and take a nap, sir Niko. If the patient exhibits irregular breathing patterns, Roboto shall alert you immediately!"
    voice audio.roboto_ch5_line14
    roboto "Would you like me to turn off the lights?"
    show niko normal_base at right_char
    voice audio.niko_ch5_line62
    niko   "Sure. Thanks."
    scene spare_room_off with Dissolve(0.3)

    jump ch5_living_room


# =============================================================================
# SECTION 11: LABEL CH5_LIVING_ROOM — Elias and Tim
# =============================================================================

label ch5_living_room:

    # [COMMENT: bg_yuxuan_lab — lab main room, Elias and Tim running in circles]
    # scene bg_yuxuan_lab with dissolve           # PLACEHOLDER — lab main room
    scene lab_cave_on with fade
    "As I stepped into the main area, the sound of playful giggles filled the air. Laughter bouncing off the walls like sunlight filtering through an open window."
    scene cg_tim_and_elias with Dissolve(0.4)
    "Elias was running in circles, his little legs pumping as fast as they could carry him. Close behind, a small boy with messy green hair and oversized glasses was in hot pursuit."

    voice audio.tim_ch5_line1
    tim   "You know I'm gonna catch you, Elias!"

    "Elias let out an exaggerated gasp, clutching his stuffed bear, Tedda, against his chest."

    voice audio.elias_ch5_line6
    elias "Ahh! Haha! Hurry, Tedda! Tim might catch us!"
    tedda "..."

    "The kid pushed his glasses up the bridge of his nose."

    voice audio.tim_ch5_line2
    tim   "Hmm… If I analyze the velocity of his movements and factor in his diminishing stamina…"
    voice audio.tim_ch5_line3
    tim   "A-ha! I have predicted your trajectory!"

    "With sudden speed, Tim lunged, tapping Elias on the shoulder."

    voice audio.elias_ch5_line7
    elias "Hahaha! Aaaaahhh! He got me!"
    voice audio.tim_ch5_line4
    tim   "Mathematical precision. You stood no chance."

    "Elias tilted his head."

    voice audio.elias_ch5_line8
    elias "I dunno what that means, but that was fun!"
    voice audio.tim_ch5_line5
    tim   "Let's have a rematch! I shall implement new strategies to maintain my superior—"

    weng  "Tim? Tim! By the stars, Tim… I'm calling you."
    scene lab_cave_on with fade

    show weng normal at right_flip
    show tim normal at left_char_kids
    with Dissolve(0.2)
    "An elderly woman in a crisp white uniform strode toward them, her silver-streaked hair pulled into a neat bun."
    "The little boy let out a small grunt, clearly reluctant to stop playing. He turned his head slightly, brows furrowed."

    show tim sad at left_char_kids
    voice audio.tim_ch5_line6
    tim  "But we're busy, Miss Weng…"
    weng "Tim, be careful. You might break something again! I don't want a repeat of your Roboto incident."

    "His shoulders slumped in defeat."

    voice audio.tim_ch5_line7
    tim "Yes, Miss Weng… Ugh…"
    hide tim
    hide weng

    show dorian neutral at left_char
    show elias normal_neutral at right_char_kids
    with Dissolve(0.2)
    "I glanced at Elias, who was still bouncing on his feet, too absorbed in the game to notice me watching. A small smile tugged at my lips."
    "It was rare—seeing him like this. Seeing him play with someone other than Tedda. Someone real. Someone his age."

    show dorian smile at left_char
    "I softened my voice."

    voice audio.dorian_ch5_line38
    dorian "Elias, are you having fun?"
    show dorian neutral at left_char
    "No response. He was too caught up in his play, bouncing excitedly on his feet."

    show elias normal_happy at right_char_kids with Dissolve(0.2)
    voice audio.elias_ch5_line9
    elias "Tim, should we continue playing tag?"
    hide elias
    show tim sad at right_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line8
    tim   "Sorry, Elias. But Miss Weng doesn't want me to play tag anymore."
    hide tim
    show elias normal_sad at right_char_kids with Dissolve(0.2)
    voice audio.elias_ch5_line10
    elias "Aww… But… But—"
    hide elias
    show tim happy at right_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line9
    tim   "That's okay! We can still tell stories!"
    hide tim
    show elias normal_happy at right_char_kids with Dissolve(0.2)
    voice audio.elias_ch5_line11
    elias "Oh… Okay!"
    hide elias
    show tim happy at right_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line10
    tim   "I'll start! There's a huge library here! And my favorite story is the one about the kumiho and—"
    hide tim

    "Yuxuan approached me, his usual easygoing smirk in place. He gestured toward the green-haired kid."

    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line14
    yuxuan "So that's Tim. The one playing with Elias."
    show dorian normal_alt_neutral at left_char
    voice audio.dorian_ch5_line39
    dorian "He and Elias are getting along well. I'm happy."
    voice audio.yuxuan_ch5_line15
    yuxuan "It's good for him. Kids need company."
    
    show yuxuan normal_happy at center_char
    show weng normal at right_flip
    with Dissolve(0.2)
    "He then turned to the elderly woman, motioning toward me."

    voice audio.yuxuan_ch5_line16
    yuxuan "Soooo, this is Cai Weng. Miss Weng, this is Dorian Burnham."
    voice audio.yuxuan_ch5_line17
    yuxuan "Weng is a true gem. She's my personal assistant, my cook, my all-rounder here at this laboratory."
    show weng happy at right_flip
    weng   "Oh, you're too kind, Master Yuxuan. I'm just doing my job. It's a pleasure to be of service here. Is that right, Tim?"

    "Tim was still too focused on Elias. Elias giggles and waves Tedda around."
    show weng sad at right_flip
    weng "…*sighs* Kids…"   

    "She turned to me with a polite nod."
    show weng normal at right_flip
    weng   "Pleasure to meet you, Sir Burnham."
    show dorian normal_alt_neutral at left_char
    voice audio.dorian_ch5_line40
    dorian "Likewise, Miss Weng."

    "I chuckled under my breath, watching Elias laugh as he exchanged stories with Tim."
    "Yuxuan told me that Svante, the aldorith who realized who I was, was placed in the storage room."
    show dorian normal_alt_calm at left_char
    "Isn't that dangerous? Svante's a metal channeler, as we've seen a while ago. He might turn on us."
    show dorian normal_alt_neutral at left_char
    "Miss Weng tells me that Svante's been handcuffed with Jinyan steel which suppresses channeling."
    "Yuxuan crossed his arms as he looked at me."
    show yuxuan alt_think at center_char
    voice audio.yuxuan_ch5_line18
    yuxuan "By the way, Svante—the Aldorith who figured out who you were? I had him placed in the storage room."

    "I turned to him sharply."

    show dorian serious at left_char
    voice audio.dorian_ch5_line41
    dorian "Isn't that dangerous? He's a metal channeler. We saw what he could do earlier. He might turn on us."

    "Before Yuxuan could answer, Weng let out a small chuckle, shaking her head."
    show weng happy at right_flip
    weng "No need to worry, Sir Burnham. The aldorith's been properly restrained."

    "She gestured toward her wrist, mimicking the snap of cuffs."
    show weng happy at right_flip
    weng "We restrained him with Jinyan Steel—he shouldn't be a problem now."

    "That caught my attention. Jinyan Steel—extremely rare, ridiculously expensive. I'd only used it once before, back when I had to subdue a particularly powerful channeler."
    "The material didn't just restrain—it completely suppressed channeling."
    "I'm not surprised Yuxuan has some here, given his wealth and influence."
    show weng normal at right_flip

    show dorian neutral at left_char
    voice audio.dorian_ch5_line42
    dorian "And he's just… sitting in there?"
    show yuxuan alt_smile at center_char
    voice audio.yuxuan_ch5_line19
    yuxuan "Fast asleep. Thanks to the Cheng Industries' Sleeping Powder."

    "Weng's gaze flickered toward the clock hanging on the wall."

    weng   "Speaking of sleep, it's already past dinner time… No wonder I'm feeling lightheaded."
    weng   "I need to hurry. You must be hungry, Master Yuxuan. Sir Burnham."
    show dorian neutral at left_char
    voice audio.dorian_ch5_line43
    dorian "Just a little."

    "Right on cue, my stomach growled. Loudly."

    show yuxuan alt_smile at center_char
    "Yuxuan shot me a look of pure amusement."

    show yuxuan normal_happy at center_char
    voice audio.yuxuan_ch5_line20
    yuxuan "Don't worry, Dorian. We'll have you fed up in no time."

    show dorian normal_alt_neutral at left_char
    "I sighed, rubbing the back of my neck."

    voice audio.dorian_ch5_line44
    dorian "I almost forgot. I haven't eaten anything all day."

    "And then it hit me—Elias."
    "I glanced toward him, still caught up in his conversation with Tim. The two of them were huddled close, exchanging animated whispers about something I couldn't hear."

    show dorian neutral at left_char
    voice audio.dorian_ch5_line45
    dorian "Elias is probably starving too…"

    show yuxuan normal_neutral at center_char
    "Yuxuan waved a hand dismissively."

    voice audio.yuxuan_ch5_line21
    yuxuan "Oh, don't worry about him. I made sure he was well-fed while you were off handling, you know… family matters at the memorial gravesite."
    show dorian neutral at left_char
    voice audio.dorian_ch5_line46
    dorian "Thanks, Yu. What did you feed him?"
    show yuxuan alt_smile at center_char
    voice audio.yuxuan_ch5_line22
    yuxuan "Umm… Tianho chocolates. Took him to a booth. It was owned by Cheng Industries so I told my employee to give him as much as he wanted."

    "I blinked."

    show dorian serious at left_char
    voice audio.dorian_ch5_line47
    dorian "How many did he eat?"

    "I stared at him, and a sense of deep, immediate regret settled in."

    show yuxuan normal_lying at center_char
    voice audio.yuxuan_ch5_line23
    yuxuan "I… uh… got caught up. Associates called. Kinda lost track. *clears throat* Sorry?"

    show dorian neutral at left_char
    "I sighed."

    voice audio.dorian_ch5_line48
    dorian "Tetrad, help me."
    show yuxuan normal_happy at center_char
    voice audio.yuxuan_ch5_line24
    yuxuan "Hey, he liked it! Kept him happy while you were gone."

    "I looked back at Elias, who was still bouncing on his feet, chattering away with Tim, his energy seemingly endless."
    "So that's why he was so hyper."

    show dorian normal_alt_neutral at left_char
    "I let out a slow breath, pinching the bridge of my nose. Yuxuan clapped a hand on my shoulder."

    show yuxuan normal_neutral at center_char
    voice audio.yuxuan_ch5_line25
    yuxuan "Relax. He'll crash eventually. Maybe after dinner. Or maybe at midnight."

    "Weng approached us again, wiping her hands on her apron."

    weng "What do you want, sir?"

    "She took out a small notebook from her side pocket at her white dress."
    "I gave her a confused look. I look at Yuxuan, who smiled and put his arm around me."

    voice audio.yuxuan_ch5_line26
    yuxuan "She's asking about our food, Dorian. You already know what I want, Miss Weng."
    weng   "Of course. I wouldn't want Master Yuxuan being denied his favorite dragonfire curry."
    show dorian neutral at left_char
    voice audio.dorian_ch5_line49
    dorian "Tianho's Dragonfire Curry?"
    show yuxuan normal_happy at center_char
    voice audio.yuxuan_ch5_line27
    yuxuan "Spicy, bold, and delicious!"
    weng   "Suiting an amazing inventor such as yourself, Master Yuxuan! You're truly incredible!"

    "I watched as she showered him with praise, her words flowing like an endless stream. I smiled awkwardly."

    show yuxuan alt_smile at center_char
    voice audio.yuxuan_ch5_line28
    yuxuan "Thank you so much, Miss Weng."
    show weng alt_base at right_flip
    weng   "A man of vision! An inspiration to the people of Tianho! The greatest inventor in the kingdom! The—"
    show yuxuan normal_neutral at center_char
    "Weng paused, looking at me."

    weng "Ah, apologies, Sir Burnham. I can make other things too, of course. I'm well-versed in the cuisines of all five kingdoms—Tianho, Gale, Hinami, Mjoll, and the Centennial Isles."
    weng "Just name any dish. If we have the ingredients, I'm sure I can cook it for you."
    weng "And if we don't have the ingredients, well I'll just buy it from the market at the Tianho city proper. I don't mind. It's directly up ground from here. There's still time before it closes."

    show dorian neutral at left_char
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

# =============================================================================
# SECTION 13: LABEL CH5_SVANTE_CHOICES — Questioning Svante
# =============================================================================

label ch5_svante_choices:
    menu:
        "Why were you the only aldorith spared by this man?":

            show dorian neutral at left_char
            dorian "When I saw the battlefield, the bodies of your brothers and sisters were scattered around him. Yet, you… you were still alive."
            dorian "How did he know you were on his side?"
            show svante normal_nervous at right_char
            svante "I… defended him. He saw it, surely."
            svante "I tried to explain to our commanders Tian Xun, to Lady Aoi… to all of them… I told them that something felt wrong. That I wasn't sure this man deserved to die."
            svante "But Tian Xun and Lady Aoi called me a traitor."
            svante "Then… he attacked. Almost everyone who came close to him died. They didn't expect him to be that powerful. No one did."

            "I studied him carefully. He wasn't lying. The tremor in his voice, the way his body tensed at the memory—it was all genuine."

            show dorian neutral at left_char
            dorian "What about your commanders? Tell me about them."
            show svante normal_nervous at right_char
            svante "Oh them? Tian Xun was um…"

            "Svante shifted, adjusting his wrists against the cuffs. He winced slightly."

            svante "Sorry. A little bit itchy."
            svante "Tian Xun was a loose cannon. He's obsessed with bombs. They say he grew up in Tianho in an impoverished family, even though his father worked for the King."
            show dorian neutral at left_char
            dorian "You mean King Long Shen, the late king of Tianho?"

            "Svante frowned a little bit."

            show svante normal_nervous at right_char
            svante "I think so. Sorry, sir. I'm not familiar with the other kings. I only know Father."
            show dorian neutral at left_char
            dorian "And the last one? Lady Aoi?"
            show svante normal_happy at right_char
            svante "Oh! Believe it or not, Lady Aoi used to be a songstress from Hinami."
            show dorian normal_alt_annoyed at left_char
            dorian "That's not what I asked."

            "Svante flinched."

            show svante normal_nervous at right_char
            svante "O-Oh! Sorry, sir! She—uh—she's a powerful water channeler from Hinami. She just… showed up at the palace one day, gave a demonstration of her power."
            svante "Father was impressed. So impressed that he made her commander of an entire battalion of Aldoriths."
            show dorian neutral at left_char
            dorian "You don't sound convinced."
            show svante normal_nervous at right_char
            svante "Just between you and me, sir… word among my brothers is that Father only sees Queen Ekaterina in her."
            show dorian neutral at left_char
            dorian "Yeah…. I can see that."

            jump ch5_svante_choices

        "Who are you?":

            show dorian neutral at left_char
            dorian "What's your name?"

            "Svante blinked at me, looking genuinely confused—almost as if the question was unnecessary."

            show svante normal_neutral at right_char
            svante "Svante, sir. Svante Nordstrom."

            "I tilted my head slightly."

            show dorian neutral at left_char
            dorian "Nordstrom. As in Gustav Nordstrom. You took on the king's last name. I'm surprised he even let you do that."
            show svante normal_nervous at right_char
            svante "You're not wrong, sir. Usually, us aldoriths carry the last name of their mothers."
            svante "M-Mother received special permission from Father, sir."
            show dorian neutral at left_char
            dorian "Really? How come?"
            show svante normal_neutral at right_char
            svante "Mother was at the top of her career when she gave birth to me. She was a songstress. Father was really into her back then."
            show dorian neutral at left_char
            dorian "What about your sister?"
            show svante normal_sad at right_char
            svante "Kristin…"

            "He paused, his hands twitching against the cuffs."

            svante "She only carried my mother's name."

            jump ch5_svante_choices

        "How do you know me?":

            show dorian neutral at left_char
            dorian "How did you recognize me?"

            "He shifted slightly, as if trying to find the right words."

            show svante normal_nervous at right_char
            svante "I… I actually didn't at first, sir."
            show dorian neutral at left_char
            dorian "How come?"

            "Svante's gaze flickered toward me. At my hair, my clothes, everything."

            show svante normal_nervous at right_char
            svante "Well, your hair, sir. It's different. And your clothes."

            "He bit his lip, hesitating."

            svante "Elias was also wearing girl's clothes so I didn't recognize him."
            show dorian neutral at left_char
            dorian "But then you figured it out."
            show svante normal_nervous at right_char
            svante "It wasn't until I heard you call Elias' name that I put all the pieces together."
            show dorian neutral at left_char
            dorian "You called me a different name as well. Why?"
            show svante normal_sad at right_char
            svante "The Massacrer of Mjoll. They named you that after you… you—"

            "His breathing quickened, and his eyes darted toward mine—fearful, desperate. A long silence erupted."

            show dorian neutral at left_char
            dorian "I won't hurt you. I promise."
            show svante normal_nervous at right_char
            svante "O-Okay, sir."

            jump ch5_svante_choices

        "That's all for now.":

            show dorian neutral at left_char
            dorian "That's all. I don't have any more questions for you."

            "I exhaled, stepping back, watching him in the dim light. His breathing had steadied, but his posture remained rigid, his body still caught between fear and exhaustion."

            show svante normal_sad at right_char
            svante "Sir Dorian…"
            svante "What would you have done? If you were me?"

            "I narrowed my eyes."

            show dorian serious at left_char
            dorian "If I were you?"

            "He nodded. His violet eyes met mine, pleading, uncertain. No malice. No scheming. Just a hurt and tormented man."

            show dorian neutral at left_char
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

    show dorian neutral at left_char
    dorian "Can I trust you?"

    "His head shot up."

    show svante normal_nervous at right_char
    svante "Trust me with what?"

    "I held the key up between us, letting it glint in the dim light."

    show dorian serious at left_char
    dorian "Swear to me—by your god—that you will never harm my family."
    show svante normal_neutral at right_char
    svante "I… I wasn't planning to, but…. I swear by Enoch that I will never harm you or your family."

    "Then, without breaking eye contact, I stepped forward and reached for his cuffs."
    "The metal was cool beneath my fingers as I slid the key into the lock. A sharp click echoed in the small room."
    "The heavy Jinshen steel fell away from his wrists."
    "Svante inhaled sharply, his arms dropping limply to his sides. He stared at his freed hands for a moment."

    show dorian neutral at left_char
    dorian "Don't make me regret this."
    show svante normal_neutral at right_char
    svante "I won't, sir."

    hide svante
    hide dorian
    jump ch5_dinner_setup


# =============================================================================
# SECTION 15: LABEL CH5_DINNER_SETUP — Before Dinner / Tim and Elias
# =============================================================================
# OMITTED

# =============================================================================
# SECTION 16: LABEL CH5_FOOD_CHOICE — Cuisine Selection
# =============================================================================
label ch5_food_choice:
    # play music ost_cheng_lab fadein 1.0         # PLACEHOLDER — warm lab theme
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

            show dorian smile at left_char
            voice audio.dorian_ch5_line50
            dorian "Thank you."

            show yuxuan normal_neutral at center_char
            "A faint blush dusted Yuxuan's face."

            voice audio.yuxuan_ch5_line29
            yuxuan "H-huh?"

            "I glanced back at Weng."

            show dorian neutral at left_char
            voice audio.dorian_ch5_line51
            dorian "I'll go with something from Tianho, Miss Weng."

            "She clapped her hands together, eyes lighting up."
            show weng alt_calm at right_flip
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

            show dorian neutral at left_char
            voice audio.dorian_ch5_line52
            dorian "I'll have something from Gale. My homeland."

            "Weng's eyes widened."
            show weng alt_base at right_flip
            weng "You're from the Empire of Gale, Sir Burnham?"

            "I nodded. She practically gushed."
            show weng alt_close_eyes at right_flip
            weng "Oh, I've been to Gale before! With my lover! The sights—oh, the sights!"

            "She twirled her pen between her fingers, a nostalgic smile crossing her lips."
            show weng normal at right_flip
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

            show dorian neutral at left_char
            voice audio.dorian_ch5_line53
            dorian "I think I'll have something from Hinami."

            "Weng's eyes gleamed with excitement."

            weng "The Island Kingdom of Hinami—oh! Such beautiful beaches!"

            "She tapped her notepad, thinking."
            show weng thinking at right_flip
            weng "The fish there? Top notch. There's even an elusive species called Aokibane—very rare!"

            "She chuckled to herself."

            weng "And of course, there's the famous Ganderbilt—an exquisite delicacy."
            show weng happy at right_flip
            "She snapped her fingers."
            show weng alt_base at right_flip 
            weng "Great choice, Sir Burnham. Something warm and comforting, then."

        "A dish from Mjoll.":
            $ ch5_food_choice = "mjoll"
            $ svante_affection += 1             # +1 Svante affection

            "Mjoll."
            "Elara's hometown. I lived there for—what? Four, five years? I'd lost count."
            "King Gustav. Queen Ekaterina. Elias. Vasily."
            "Tetrad above, Vasily."
            show dorian sad at left_char
            "I can't believe I killed him. Vasily. My friend."
            "Not only him. But an entire battalion of aldoriths and soldiers. It was a blur. But I can hear the aldoriths cries and screams."
            "Not just him. An entire battalion of Aldoriths and soldiers. It was a blur, but I could still hear it."
            "The screams."
            "And now… Svante."
            "I'd seen the way he looked at me. He was afraid. I don't want him to be. I—"

            weng "Sir Dorian? Are you having trouble choosing?"

            show dorian normal_alt_calm at left_char
            "I blinked, shaking the memories away."
            show dorian neutral at left_char
            voice audio.dorian_ch5_line54
            dorian "Oh, uh. Sorry. I'd like something from Mjoll."

            "She tilted her head slightly, observing me."
            show weng sad at right_flip
            weng "The snowy kingdom. I see…"

            show yuxuan normal_neutral at center_char
            voice audio.yuxuan_ch5_line30
            yuxuan "I remember you telling me that you've been there before, Miss Weng."

            "A brief silence. She looked down, her fingers tightening around her pen."
            show weng alt_close_eyes at right_flip
            weng "Yes… yes, I have."
            show weng alt_base at right_flip
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
    scene lab_cave_on with dissolve           # PLACEHOLDER — lab/common area

    "Weng then approached the two toddlers, smoothing out the wrinkles in her apron."
    show weng normal at left_char with Dissolve(0.2)
    weng "Alright, little ones. What would you like for dinner?"

    "Tim adjusted his tiny glasses, crossing his arms."
    show tim alt_pumped at right_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line11
    tim "Braised Tianho fish with fermented black beans. Steamed tofu with ginger. And a side of sautéed bok choy with garlic."
    hide tim 
    hide weng
    show dorian neutral at left_char with Dissolve(0.2)
    "I blinked."

    voice audio.dorian_ch5_line55
    dorian "What kind of five-year-old asks for that?"
    show yuxuan normal_happy at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line31
    yuxuan "Hahaha! That's Tim. He has quite the refined palate, just like me and Weng."
    hide yuxuan
    show tim alt_pumped at right_char_kids with Dissolve(0.2)
    "Tim pushed his glasses up the bridge of his nose, utterly serious."
    voice audio.tim_ch5_line12
    tim "Proper nutrition is essential for cognitive development of toddlers like myself. My brain requires high-quality fuel."
    hide tim
    show elias normal_happy at right_char_kids with Dissolve(0.2)
    "Meanwhile, Elias was bouncing on his heels, practically vibrating with excitement."

    voice audio.elias_ch5_line12
    elias "Ooh! I want choco—"
    show dorian normal_alt_annoyed at left_char
    "I cut him off before he could even finish."
    voice audio.dorian_ch5_line56
    dorian "Chicken. Rice. Soup. And lots of vegetables. He'll have that."
    show elias normal_sad at right_char_kids
    "Elias's little face scrunched up into a dramatic pout, his lower lip jutting out."
    voice audio.elias_ch5_line13
    elias "But daddy—"
    show dorian normal_alt_annoyed at left_char
    "I gave him The Look."
    voice audio.dorian_ch5_line57
    dorian "No, Elias. You already ate enough chocolate today. You need your vitamins."
    show elias normal_sad at right_char_kids
    show dorian neutral at left_char
    "Elias squirmed. His little hands clutched Tedda, his stuffed bear, like the poor toy could somehow convince me to change my mind."
    hide elias
    show tim alt_serious at right_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line13
    tim "Vegetables are good for you, Elias."
    hide tim
    show elias alt_doubt at right_char_kids with Dissolve(0.2)
    voice audio.elias_ch5_line14
    elias "No, they're not… They're icky!"
    hide elias
    show tim alt_normal at right_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line14
    tim "Yes, they are. They contain essential vitamins and minerals that help you grow stronger and support brain function. You want to be smart like me, don't you?"
    hide tim
    show elias normal_neutral at right_char_kids with Dissolve(0.2)
    voice audio.elias_ch5_line15
    elias "Fiiineeee…"
    hide elias
    show weng normal at right_flip with Dissolve(0.2)
    weng "Alright then, why don't you two go play while I prepare dinner?"
    hide weng
    show tim alt_normal at right_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line15
    tim "Master Yuxuan, can Elias and I go to the library?"
    show yuxuan normal_happy at center_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line32
    yuxuan "Always, Tim. Keep on reading, green-haired buddy."
    show tim happy at right_char_kids

    "Tim's face lit up. He turned to Elias, taking his hand like a tiny professor guiding his student."

    voice audio.tim_ch5_line16
    tim "Come with me. I'll show you the library."
    "Elias blinked, surprised."

    voice audio.tim_ch5_line17
    tim "I'll show you my favorite books! Let's read together! Oh, you're gonna love the legend of the kumiho!"
    hide tim
    show elias normal_happy at right_char_kids with Dissolve(0.2)
    voice audio.elias_ch5_line16
    elias "Let's go! Ooh! Do they have pictures and flowers there?"
    hide elias
    show weng alt_calm at right_flip with Dissolve(0.2)
    weng "Tim… Make sure to be back once dinner is finished, okay? It's a challenge to get you away from those books once you start. Be mindful of little Elias with you."

    show yuxuan normal_neutral at center_char
    "Yuxuan and I watched them go, both of us shaking our heads in amusement."

    voice audio.yuxuan_ch5_line33
    yuxuan "They make quite the pair huh, Dorian? They just met and they're acting like they've known each other for a long time!"
    show dorian neutral at left_char
    voice audio.dorian_ch5_line58
    dorian "No kidding."

    "Weng chuckled as she headed toward the kitchen."

    weng "You two, just sit tight and wait. Dinner will be ready soon."
    "I nodded, stretching out on the sofa."
    jump ch5_nap

# =============================================================================
# SECTION 17: LABEL CH5_NAP — Dorian Naps Before Dinner
# =============================================================================
label ch5_nap:

    # [COMMENT: bg_yuxuan_lab_dim — lab with dimmed lights]
    scene lab_cave_on with dissolve       # PLACEHOLDER — lab dimmed lights

    show dorian neutral at left_char
    show yuxuan normal_neutral at right_char
    with Dissolve(0.2)
    voice audio.yuxuan_ch5_line34
    yuxuan "Gonna take a nap?"
    show dorian neutral at left_char
    voice audio.dorian_ch5_line59
    dorian "Just for a bit."

    hide yuxuan
    hide dorian
    with Dissolve(0.1)
    "As soon as my head hit the cushion, exhaustion washed over me. It's been a long day. I put a pillow on top of my face."
    "And within moments, I was out."
    pause 1.0
    scene lab_cave_off with dissolve
    pause 1.0
    "I must have slept for an hour or two."
    "I stretched, still groggy from my nap, the muffled sound of rain aboveground blending with the quiet hum of Yuxuan's underground laboratory."
    "The dim lighting cast long shadows, and the scent of something rich and savory filled the air."
    "My stomach rumbled."
    scene cg_weng_cooking with fade
    weng "Sir Burnham? You woke up early. Thought you'd sleep until dinner was ready."

    "She stood near the stove, stirring a pot, the warmth from the fire flickering across her face."

    voice audio.dorian_ch5_line60
    dorian "Did I?"

    "I could still feel the weight of sleep clinging to me."

    weng   "Master Yuxuan's in his study. Said he had work to do."

    "I nodded, rubbing the back of my neck as the scent of the stew—something hearty and rich—filled my nostrils."

    voice audio.dorian_ch5_line61
    dorian "Smells good, Miss Weng."
    voice audio.weng_ch5_line39
    weng   "You're too kind, Sir Burnham. You'll get your share soon enough. But—"

    "She wiped her hands on her apron and approached me, lowering her voice slightly."

    scene lab_cave_on with fade
    show weng normal at right_flip
    show dorian neutral at left_char
    with Dissolve(0.2)
    voice audio.weng_ch5_line40
    weng "Remember the Aldorith? Svante?"
    voice audio.dorian_ch5_line62
    dorian "Yeah. What about him?"

    "She glanced toward the hallway leading to the storage room."
    show weng alt_calm at right_flip
    voice audio.weng_ch5_line41
    weng "I took the liberty of preparing something from Mjoll for him. His food's almost ready. No use letting him starve."

    "She reached into her pocket and pulled out a small, cold iron key, pressing it into my palm."
    show weng alt_close_eyes at right_flip
    voice audio.weng_ch5_line42
    weng "You're the one who he has a problem with. I was thinking you should be the one to check on him. See if he's woken up. Maybe talk to him."
    show weng normal at right_flip
    "I looked down at the key. It was simple but sturdy, and heavier than I expected."

    show dorian serious at left_char
    voice audio.dorian_ch5_line63
    dorian "Is he even awake?"
    show weng alt_base at right_flip
    voice audio.weng_ch5_line43
    weng   "Hard to say. He's been out for a while, but knowing sleeping powder, its effects should have worn off about now."
    voice audio.dorian_ch5_line64
    dorian "And if he's a threat?"

    "Weng wiped her hands on her apron again."
    show weng serious at right_flip
    voice audio.weng_ch5_line44
    weng "Then you'll know what to do, sir Burnham."

    show dorian normal_alt_calm at left_char
    "I nodded. A test. A chance. If Svante didn't prove to be a threat, I could unlock his cuffs. But if he did…"
    "I clenched my jaw and stood up, pocketing the key."

    show dorian serious at left_char
    voice audio.dorian_ch5_line65
    dorian "I'll see where he stands."

    "Weng nodded in approval before turning back to the stove, resuming her work."

    jump ch5_interrogation

# =============================================================================
# SECTION 17A: LABEL ch5_storage_room interrogation
# =============================================================================
label ch5_interrogation:
    scene storage_room_off with fade          # PLACEHOLDER — lab storage room
    # play music ost_svante_talk fadein 1.5       # PLACEHOLDER — low tension theme
    "I stepped into the storage room, my movements silent against the cold stone floor. The dim flicker of a single candle cast long shadows across the walls, stretching and shifting with the flame's uncertain dance."
    "Unlike the other rooms, the air was stale, thick with dust and the faint scent of damp stone."
    "Then I heard it."
    "A voice—low, trembling—whispering desperate words into the dark."
    scene storage_room with dissolve

    show svante normal_sad at center_char
    voice audio.svante_ch5_line20
    svante "Mighty Enoch… Please… {i}*tears*{/i} Your servant is afraid…"

    "I stood still, just inside the doorway. He hadn't noticed me. Not yet."

    voice audio.svante_ch5_line21
    svante "I know I have strayed, I know I have sinned... I never meant to question Father. I never meant to doubt him."

    "He paused, sniffling."

    voice audio.svante_ch5_line22
    svante "I— I betrayed our sacred law. I know I should never have doubted Father... I know my place. But… Kristin…"
    voice audio.svante_ch5_line23
    svante "But… what if… What if Kristin was right all along?"

    "He swallowed hard, his words now coming in ragged, pleading bursts."

    voice audio.svante_ch5_line24
    svante "My Lord Enoch, please... {i}*crying*{/i} Please don't abandon me. Not now, not when the monster is near."
    voice audio.svante_ch5_line25
    svante "My mother needs me… She's the only family I have left, my Lord. Please help me…"
    voice audio.svante_ch5_line26
    svante "I… I don't know what to do anymore. I'm so sorry. I feel so lost and broken. Please, mighty Enoch, show me mercy."

    "His fingers twitched uselessly, bound and helpless against the wall. The sheen of Jinshen steel caught the dim candlelight, the cuffs glinting like an executioner's blade. I recognized them instantly."
    "Good. That way, I wouldn't have to worry about his channeling."
    "I took a single step forward."
    "His breath hitched. His head snapped up so fast I thought he'd hurt himself."

    show svante normal_nervous at right_char 
    show dorian normal_alt_neutral at left_char
    with Dissolve(0.2)
    voice audio.svante_ch5_line27
    svante "No… No, no, no… Please—please, no…"
    voice audio.dorian_ch5_line66
    dorian "Calm down. I just want to ask you a few things."
    show svante normal_sad at right_char
    voice audio.svante_ch5_line28
    svante "Sir… I beg you. Please let me go! {i}*crying*{/i} I have a mother! She's sick. She's the only family that I have left!"
    show svante normal_nervous at right_char 
    svante "No… No, no, no… Don't hurt me! I beg you! Please—please, no—"

    "I heard his stomach rumble."
    show dorian neutral at left_char
    voice audio.dorian_ch5_line67
    dorian "You must be starving. Here, I just need to—"
    show svante normal_nervous at right_char
    voice audio.svante_ch5_line29
    svante "I… Is that it, sir? I-If you wish to spare me, Please, you don't have to feed me."
    voice audio.svante_ch5_line30
    svante "Please. I'll eat morsels from the garbage if I have to. Just please let me live!"

    "I rolled my eyes."

    show dorian normal_alt_annoyed at left_char
    voice audio.dorian_ch5_line68
    dorian "ARE YOU GOING TO CALM DOWN OR NOT?!"

    "Silence. He stopped struggling. But I could see him trembling."

    show svante normal_sad at right_char
    voice audio.svante_ch5_line31
    svante "{i}*crying*{/i}"
    show dorian serious at left_char
    voice audio.dorian_ch5_line69
    dorian "No one needs to die today. I just need to ask you a few questions. Calm down."
    show svante normal_nervous at right_char
    voice audio.svante_ch5_line32
    svante "Y-Yes, sir…"

    "I took a deep breath."

    show dorian serious at left_char
    voice audio.dorian_ch5_line70
    dorian "Let's start with the obvious. Why does Mjoll want the man that we saved dead?"

    "Svante hesitated, his fingers twitching against the cuffs. His gaze flickered toward the floor, avoiding mine."

    show svante normal_nervous at right_char
    voice audio.svante_ch5_line33
    svante "I—I don't know everything, sir. I swear it. But..."
    voice audio.svante_ch5_line34
    svante "Father said that the man we were supposed to kill… cursed him."
    show dorian serious at left_char
    voice audio.dorian_ch5_line71
    dorian "Cursed him?"

    "My eyes widened."
    show svante alt_guilty at right_char
    voice audio.svante_ch5_line35
    svante "That's what he told us. That the man— he was some kind of heretic and is an enemy of Mjoll."
    show dorian serious at left_char
    voice audio.dorian_ch5_line72
    dorian "And you believe him?"

    "A brief silence erupted between us."

    show svante normal_sad at right_char
    voice audio.svante_ch5_line36
    svante "No… I think he's… lying…"
    voice audio.svante_ch5_line37
    svante "Because he's lied before… with the Elias incident. He told everyone that it was Elias who killed his own mother."
    voice audio.svante_ch5_line38
    svante "My sister Kristin… she accompanied the two prophets as they examined Queen Ekaterina's body."
    voice audio.svante_ch5_line39
    svante "The fingerprints on the knife belonged to Father himself. But still, he tried to pin the blame on Elias..."
    voice audio.svante_ch5_line40
    svante "I was the only person my sister talked to about this. At first, I got mad at her for doubting Father but after her death, I… I started to wonder."
    voice audio.svante_ch5_line41
    svante "What if she was right?"
    show dorian neutral at left_char
    voice audio.dorian_ch5_line73
    dorian "So you think the man you were sent to kill today… was innocent?"

    show svante normal_nervous at right_char
    voice audio.svante_ch5_line42
    svante "Y-Yes, sir."
    show dorian normal_alt_calm at left_char
    "I nodded. That was brave of him to say. For an aldorith, it would have been a death sentence."
    show svante normal_neutral at right_char
    voice audio.svante_ch5_line43
    svante "Do you have any more questions, sir?"

# =============================================================================
# SECTION 17B: INTERROGATION CHOICE MENU
# =============================================================================

default ch5_interro_q1 = False
default ch5_interro_q2 = False
default ch5_interro_q3 = False

label ch5_interrogation_menu:
    menu:
        "Why were you the only aldorith spared by this man?" if not ch5_interro_q1:
            $ ch5_interro_q1 = True
            jump ch5_interro_q1
        "Who are you?" if not ch5_interro_q2:
            $ ch5_interro_q2 = True
            jump ch5_interro_q2
        "How do you know me?" if not ch5_interro_q3:
            $ ch5_interro_q3 = True
            jump ch5_interro_q3
        "That's all for now.":
            jump ch5_interro_q4

# --- Q1 ---
label ch5_interro_q1:
    show dorian serious at left_char
    voice audio.dorian_ch5_line74
    dorian "When I saw the battlefield, the bodies of your brothers and sisters were scattered around him. Yet, you… you were still alive."
    voice audio.dorian_ch5_line75
    dorian "How did he know you were on his side?"
    show svante normal_nervous at right_char
    voice audio.svante_ch5_line44
    svante "I… defended him. He saw it, surely."
    voice audio.svante_ch5_line45
    svante "I tried to explain to our commanders Tian Xun, to Lady Aoi… to all of them… I told them that something felt wrong. That I wasn't sure this man deserved to die."
    voice audio.svante_ch5_line46
    svante "But Tian Xun and Lady Aoi called me a traitor."
    voice audio.svante_ch5_line47
    svante "Then… he attacked. Almost everyone who came close to him died. They didn't expect him to be that powerful. No one did."

    "I studied him carefully. He wasn't lying. The tremor in his voice, the way his body tensed at the memory—it was all genuine."

    show dorian normal_alt_neutral at left_char
    voice audio.dorian_ch5_line76
    dorian "What about your commanders? Tell me about them."
    
    show svante normal_nervous at right_char
    voice audio.svante_ch5_line48
    svante "Oh them? Tian Xun was um…"

    "Svante shifted, adjusting his wrists against the cuffs. He winced slightly."
    
    show svante alt_guilty at right_char
    voice audio.svante_ch5_line49
    svante "Sorry. A little bit itchy."
    voice audio.svante_ch5_line50
    svante "Tian Xun was a loose cannon. He's obsessed with bombs. They say he grew up in Tianho in an impoverished family, even though his father worked for the King."
    show dorian serious at left_char
    voice audio.dorian_ch5_line77
    dorian "You mean King Long Shen, the late king of Tianho?"
    show svante normal_nervous at right_char
    "Svante frowned a little."

    voice audio.svante_ch5_line51
    svante "I think so. Sorry, sir. I'm not familiar with the other kings. I only know Father."
    show dorian neutral at left_char
    voice audio.dorian_ch5_line78
    dorian "And the last one? Lady Aoi?"
    show svante normal_happy at right_char
    voice audio.svante_ch5_line52
    svante "Oh! Believe it or not, Lady Aoi used to be a songstress from Hinami."
    show dorian normal_alt_annoyed at left_char
    voice audio.dorian_ch5_line79
    dorian "That's not what I asked."
    show svante normal_nervous at right_char
    "Svante flinched."

    voice audio.svante_ch5_line53
    svante "O-Oh! Sorry, sir! She—uh—she's a powerful water channeler from Hinami. She just… showed up at the palace one day, gave a demonstration of her power."
    voice audio.svante_ch5_line54
    svante "Father was impressed. So impressed that he made her commander of an entire battalion of Aldoriths."
    show dorian neutral at left_char
    voice audio.dorian_ch5_line80
    dorian "You don't sound convinced."
    show svante normal_neutral at right_char
    voice audio.svante_ch5_line55
    svante "Just between you and me, sir… word among my brothers is that Father only sees Queen Ekaterina in her."
    show dorian neutral at left_char
    voice audio.dorian_ch5_line81
    dorian "Yeah…. I can see that."

    jump ch5_interrogation_menu

# --- Q2 ---
label ch5_interro_q2:
    show dorian serious at left_char
    voice audio.dorian_ch5_line82
    dorian "What's your name?"

    "Svante blinked at me, looking genuinely confused—almost as if the question was unnecessary."

    show svante normal_neutral at right_char
    voice audio.svante_ch5_line56
    svante "Svante, sir. Svante Nordstrom."

    "I tilted my head slightly."

    show dorian neutral at left_char
    voice audio.dorian_ch5_line83
    dorian "Nordstrom. As in Gustav Nordstrom. You took on the king's last name. I'm surprised he even let you do that."

    voice audio.svante_ch5_line57
    svante "You're not wrong, sir. Usually, us aldoriths carry the last name of their mothers."
    show svante normal_nervous at right_char
    voice audio.svante_ch5_line58
    svante "M-Mother received special permission from Father, sir."
    show dorian serious at left_char
    voice audio.dorian_ch5_line4
    dorian "Really? How come?"
    show svante normal_neutral at right_char
    voice audio.svante_ch5_line59
    svante "Mother was at the top of her career when she gave birth to me. She was a songstress. Father was really into her back then."
    show dorian serious at left_char
    voice audio.dorian_ch5_line85
    dorian "What about your sister?"
    show svante normal_sad at right_char
    voice audio.svante_ch5_line60
    svante "Kristin… She only carried my mother's name."

    "He paused, his hands twitching against the cuffs."

    jump ch5_interrogation_menu

# --- Q3 ---
label ch5_interro_q3:
    show dorian neutral at left_char
    voice audio.dorian_ch5_line86
    dorian "How did you recognize me?"
    "He shifted slightly, as if trying to find the right words."

    show svante normal_nervous at right_char
    voice audio.svante_ch5_line61
    svante "I… I actually didn't at first, sir."
    show dorian serious at left_char
    voice audio.dorian_ch5_line87
    dorian "How come?"

    "Svante's gaze flickered toward me. At my hair, my clothes, everything."
    show svante normal_nervous at right_char
    voice audio.svante_ch5_line62
    svante "Well, your hair, sir. It's different. And your clothes."
    "He bit his lip, hesitating."
    voice audio.svante_ch5_line63
    svante "Elias was also wearing girl's clothes so I didn't recognize him."

    show dorian neutral at left_char
    voice audio.dorian_ch5_line88
    dorian "But then you figured it out."
    show svante normal_nervous at right_char
    voice audio.svante_ch5_line64
    svante "It wasn't until I heard you call Elias' name that I put all the pieces together."
    show dorian neutral at left_char
    voice audio.dorian_ch5_line89
    dorian "You called me a different name as well. Why?"
    show svante normal_sad at right_char
    voice audio.svante_ch5_line65
    svante "The Massacrer of Mjoll. They named you that after you… you—"

    "His breathing quickened, and his eyes darted toward mine—fearful, desperate. A long silence erupted."

    show dorian neutral at left_char
    voice audio.dorian_ch5_line90
    dorian "I won't hurt you. I promise."
    show svante normal_nervous at right_char
    voice audio.svante_ch5_line66
    svante "O-Okay, sir."

    jump ch5_interrogation_menu

# --- Q4 ---
label ch5_interro_q4:
    show dorian neutral at left_char
    voice audio.dorian_ch5_line91
    dorian "That's all. I don't have any more questions for you."
    "I exhaled, stepping back, watching him in the dim light. His breathing had steadied, but his posture remained rigid, his body still caught between fear and exhaustion."
    show svante normal_sad at right_char
    voice audio.svante_ch5_line67
    svante "Sir Dorian…"
    voice audio.svante_ch5_line68
    svante "What would you have done? If you were me?"

    "I narrowed my eyes."

    show dorian serious at left_char
    voice audio.dorian_ch5_line92
    dorian "If I were you?"

    "He nodded. His violet eyes met mine, pleading, uncertain. No malice. No scheming. Just a hurt and tormented man."

    show dorian neutral at left_char
    voice audio.dorian_ch5_line93
    dorian "I wouldn't let doubt rule me. I would decide. I'd choose a side. And stick with it."

    show svante normal_neutral at right_char
    "He swallowed, nodding slowly."

# =============================================================================
# SECTION 17C: INTERROGATION COMMON — Svante Released
# =============================================================================
label ch5_interro_common:
    "A pause. I studied him. The way his shoulders slumped in exhaustion, the way his fingers twitched, the way he spoke—like a man who had already lost everything and was now only waiting for the final blow."
    "I'd seen men like him before. Broken. But not beyond repair."
    "I felt that he wasn't a threat. Not now."
    "I reached into my pocket, fingers brushing over the cold metal key Weng had given me."

    show dorian neutral at left_char
    voice audio.dorian_ch5_line94
    dorian "Can I trust you?"

    "His head shot up."

    show svante normal_nervous at right_char
    voice audio.svante_ch5_line69
    svante "Trust me with what?"

    "I held the key up between us, letting it glint in the dim light."

    show dorian serious at left_char
    voice audio.dorian_ch5_line95
    dorian "Swear to me—by your god—that you will never harm my family."
    show svante normal_neutral at right_char
    voice audio.svante_ch5_line70
    svante "I… I wasn't planning to, but…. I swear by Enoch that I will never harm you or your family."

    "Then, without breaking eye contact, I stepped forward and reached for his cuffs."
    "The metal was cool beneath my fingers as I slid the key into the lock. A sharp click echoed in the small room."
    "The heavy Jinshen steel fell away from his wrists."
    "Svante inhaled sharply, his arms dropping limply to his sides. He stared at his freed hands for a moment."

    show dorian neutral at left_char
    voice audio.dorian_ch5_line96
    dorian "Don't make me regret this."
    show svante normal_neutral at right_char
    voice audio.svante_ch5_line71
    svante "I won't, sir."

    jump ch5_return_to_lab

# =============================================================================
# SECTION 17D: RETURN TO LAB — Dinner Begins
# =============================================================================
label ch5_return_to_lab:
    scene lab_cave_off with fade           # PLACEHOLDER — lab main room, warm light
    # play music ost_dinner_warm fadein 2.0       # PLACEHOLDER — warm dinner theme
    # play audio amb_kitchen loop fadein 1.5      # PLACEHOLDER — kitchen ambient

    "As Svante and I stepped into the main room, the warm scent of spices and simmering broth filled the air. The rich aroma of slow-cooked meats and fragrant herbs curled through the space."
    "Weng was still by the stove, stirring a pot with practiced ease. The moment her gaze landed on Svante, she set down her spoon and wiped her hands on her apron, stepping forward with a welcoming smile."
    scene lab_cave_on with dissolve

    show weng happy at right_flip 
    show svante normal_neutral at left_char
    with Dissolve(0.2)
    voice audio.weng_ch5_line45
    weng "Ah, you're awake! That's good to see. You must be starving."
    voice audio.weng_ch5_line46
    weng "Proper introductions are in order. I'm Cai Weng, Master Yuxuan's assistant. It's a pleasure to meet you, young man."

    show svante normal_sad at left_char
    "He blinked, as if taken aback by the kindness in her voice. He looked at me, and then back to her."

    show svante normal_neutral at left_char with Dissolve(0.2)
    voice audio.svante_ch5_line72
    svante "I… Yes. Thank you, m-mam. My name's Svante. Svante Nordstrom. I-I'm so glad to meet you."

    show weng normal at right_flip
    voice audio.weng_ch5_line47
    weng "Dinner is ready. Please have a seat, gentlemen and I'll be serving you up the food."
    voice audio.weng_ch5_line48
    weng "I hope you like haugensoppa. I made it just for you."
    show svante normal_happy at left_char
    voice audio.svante_ch5_line73
    svante "Haugensoppa? You… know Mjoll cuisine?"
    voice audio.weng_ch5_line49
    weng "Oh, I've had my fair share of travelers from the North. You lot love your root vegetable stews."

    "Svante opened his mouth, perhaps to ask more, but before he could reply—"
    "A sudden burst of tiny, hurried footsteps came from the hallway."
    scene cg_tim_and_elias with fade
    voice audio.tim_ch5_line18
    tim "Elias, you're going too slow! Dinner's about to start!"
    voice audio.elias_ch5_line17
    elias "I'm carrying Tedda and my book! It's a little heavy!"

    "Tim marched into the room first, his small arms wrapped around a thick, leather-bound book far too large for someone his age. The title was embossed in gold: {i}Tianho's Ancient Dynasties.{/i}"
    "Elias followed closely behind, but instead of a weighty tome, he proudly clutched a children's coloring book, its cover splashed with bright rainbows and smiling animals. Perched lazily on top was Tedda."
    "Tim sighed dramatically, adjusting his glasses."
    scene lab_cave_on with fade

    show tim alt_pumped at left_char_kids 
    show elias normal_happy at right_char_kids
    with Dissolve(0.2)
    voice audio.tim_ch5_line19
    tim "Elias, I told you to pick something educational."
    voice audio.elias_ch5_line18
    elias "This one had colors, Tim! It's got rainbows! They're educational."
    voice audio.tim_ch5_line20
    tim "Rainbows are not educational, Elias."

    "Elias gasped as he spotted Svante. His eyes widened with delight."
    show elias normal_lying at right_char_kids
    voice audio.elias_ch5_line19
    elias "Look! It's the pink haired guy! He's awake!"
    show tim alt_normal at left_char_kids
    voice audio.tim_ch5_line21
    tim "Huh? He's not pink haired, Elias! It's violet!"
    show elias normal_evil at right_char_kids
    voice audio.elias_ch5_line20
    elias "Tim, pink and violet are the same. Right, Tedda?"
    show tim alt_annoyed at left_char_kids
    voice audio.tim_ch5_line22
    tim "What?! They're completely different colors. Right, Miss Weng?"
    show svante normal_base at center_char with Dissolve(0.2)
    voice audio.svante_ch5_line74
    svante "Actually… my hair is violet. It's not really pink."
    voice audio.tim_ch5_line23
    tim "HA! It's violet! See, Elias? See? I win! HAHA—"
    voice audio.weng_ch5_line50
    weng "Tim, quit it. You're embarrassing me in front of Sir Burnham and Sir Nordstrom. Now be a good boy and help me serve dinner."

    show tim shy at left_char_kids
    "Tim huffed but did as he was told, setting his book down carefully before moving to grab a stack of bowls."
    hide svante
    hide tim
    hide elias
    with Dissolve(0.1)
    jump ch5_chung_wakes


# =============================================================================
# SECTION 18: LABEL CH5_CHUNG_WAKES — Chung-hee Arrives at Dinner
# =============================================================================
label ch5_chung_wakes:
    # [COMMENT: bg_kitchen — long dining table, warm light, Weng cooking]
    # scene bg_kitchen with dissolve              # PLACEHOLDER — kitchen / dining area

    # play music ost_dinner_warm fadein 2.0       # PLACEHOLDER — warm dinner theme
    # play audio amb_kitchen loop fadein 1.5      # PLACEHOLDER — kitchen ambient

    show dorian neutral at left_char with Dissolve(0.2)
    voice audio.dorian_ch5_line97
    dorian "Elias, why did you even bring all of those—"
    show dorian serious at left_char

    "I felt something. A shift in the air."
    "A presence."
    "Slowly, I turned."
    "The once-unconscious man was now floating. His feet hovered barely above the ground, the air around him rippling like disturbed water."
    "Then, his head bowed slightly. A voice entered our minds."

    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee "You must be the ones who rescued me. Thank you."

    "The room fell into an eerie silence."
    "We were all seated at the long table—me, Yuxuan, Niko, Svante, and the once-unconscious man. Roboto hummed softly as it moved around the table, methodically placing glasses of water in front of each of us."

    show roboto happy at center_robot with Dissolve(0.2)
    voice audio.roboto_ch5_line15
    roboto "One for you… One for you…"
    voice audio.roboto_ch5_line16
    roboto "Would you prefer ice cold or lukewarm, Sir Niko?"
    hide chunghee
    show niko normal_base at right_char with Dissolve(0.2)
    voice audio.niko_ch5_line63
    niko   "Ice cold. Thanks."

    "Then—the voice returned. Not spoken aloud, but entering our minds like a gentle ripple through still water."
    hide niko
    hide roboto
    show niko normal_base at right_char
    show chunghee normal_neutral at center_char
    with Dissolve(0.2)
    chung_hee "Once again, I wish to express my deepest gratitude. Words alone cannot convey how much I owe you."
    chung_hee "If not for you, I would have met a terrible fate."
    show dorian neutral at left_char
    voice audio.dorian_ch5_line98
    dorian    "Don't mention it."
    voice audio.niko_ch5_line64
    niko      "And you don't need to be so formal. You don't have to use mind channeling all the time—we can understand you just fine if you speak normally."

    "There was a pause."

    show chunghee normal_neutral at center_char
    chung_hee "Forgive me. I can only communicate through mind channeling. I hope it is not of any inconvenience to you."
    hide niko
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line35
    yuxuan    "Really? Why not?"
    show chunghee normal_neutral at center_char
    chung_hee "I was born unable to speak. Nor hear. This is the only way I can make myself understood."
    hide yuxuan
    show niko normal_base at right_char with Dissolve(0.2)
    voice audio.niko_ch5_line65
    niko      "So you're a deaf-mute… and you're using your channeling abilities to expand your senses. That's impressive."
    show dorian neutral at left_char
    voice audio.dorian_ch5_line99
    dorian    "I respect that."
    show niko normal_smile at right_char
    voice audio.niko_ch5_line66
    niko      "I actually know a little bit of sign language. My brother and I studied it so we can translate for the Emperor of Kyeongjang's son—he's also a deaf-mute."
    hide niko
    show svante normal_neutral at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line75
    svante    "The son of the Emperor of Kyeongjang's a deaf-mute? Poor guy."
    show chunghee normal_neutral at center_char
    chung_hee "You know my father?"
    hide svante
    show niko normal_serious at right_char with Dissolve(0.2)
    voice audio.niko_ch5_line67
    niko      "Father?"
    show chunghee normal_neutral at center_char
    chung_hee "Yes, you've heard correctly. My name is Hyon Chung-hee. Son of Emperor Hyon Min-joon. And the Emperor of Kyeongjang."

    "Silence."
    "For a moment, none of us reacted."

    show dorian serious at left_char
    dorian    "?!"
    show niko normal_base at right_char
    voice audio.niko_ch5_line68
    niko      "?!"
    hide niko
    show svante normal_nervous at right_char
    svante    "?!"

    "Niko inhaled sharply, his eyes darting toward me as if to confirm that we had all heard the same thing."
    "Svante's entire body tensed, his expression a mixture of disbelief and caution. Even Weng, who had spent the past hour focused solely on her cooking, froze mid-motion."
    "Tim, who had been carefully placing spoons on the table, accidentally dropped one. The clatter was deafening in the silence."
    hide chunghee
    hide svante
    show elias normal_happy at right_char_kids with Dissolve(0.2)
    "Only Elias remained blissfully unaware, still coloring, his small voice humming a made-up tune."

    voice audio.elias_ch5_line21
    elias "La la la la..."
    tedda "..."
    hide elias

    show yuxuan normal_lying at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line36
    yuxuan "T-The Emperor?!"
    hide yuxuan 
    show weng alt_nervous at right_flip with Dissolve(0.2)
    voice audio.weng_ch5_line51
    weng   "By the stars…"
    hide weng 
    show yuxuan normal_normal at right_char with Dissolve(0.2)


    "I leaned back slightly, watching the man—the Emperor—carefully."
    show chunghee alt_neutral at center_char with Dissolve(0.2)
    "His expression did not waver. He did not fidget, nor did he show any trace of uncertainty."

    show dorian serious at left_char
    dorian    "You must be joking. The Emperor of Kyeongjang is dead."
    show chunghee alt_neutral at center_char
    chung_hee "Yes, my Father, Emperor Min-joon and my mother passed away during their time in Tianho."
    chung_hee "In the wake of their passing, I was named their successor. I am the Emperor now."
    
    show chunghee normal_sad at center_char
    "He exhaled slowly."

    show chunghee alt_neutral at center_char
    chung_hee "But as for me. I am alive and well. Thanks to all of your combined efforts."

    show dorian normal_alt_calm at left_char
    "I blinked."
    "Silence stretched across the room, thick and suffocating. No one spoke. No one moved."
    "Then—"

    show yuxuan normal_happy at right_char
    show dorian serious at left_char
    "Yuxuan burst out laughing."

    yuxuan "HAHAHAHAHAHA!"
    show yuxuan alt_smile at right_char
    voice audio.yuxuan_ch5_line37
    yuxuan "Pfft—alright, that's it. I've officially lost my mind because of that damn propulsion system. This is a dream. A really weird, stress-induced dream."
    "He waved a hand in front of his face dramatically."
    voice audio.yuxuan_ch5_line38
    yuxuan "I mean, let's think about this logically. What are the odds that the actual Emperor of Kyeongjang would be sitting at my dinner table, in my secret underground lab, eating my food?"

    "He turned to Weng, looking utterly amused."

    voice audio.yuxuan_ch5_line39
    yuxuan "Come on, Miss Weng. Pinch me. Maybe I'll wake up in my office, face-first in a pile of paperwork."
    hide yuxuan
    show weng alt_close_eyes_nervous at right_flip with Dissolve(0.2)
    voice audio.weng_ch5_line52
    "Weng let out a long, suffering sigh, pressing her fingers against her temples."

    voice audio.weng_ch5_line53
    weng "Master Yuxuan… Are you sure?"
    hide weng
    show niko normal_smile at right_char with Dissolve(0.2)
    "Niko chuckled, shaking his head."

    voice audio.niko_ch5_line69
    niko "Well, I didn't exactly expect to be dining with the owner of Cheng Industries at his 'secret laboratory' either, let alone with an elderly lady as his personal maid… but here we are."
    voice audio.niko_ch5_line70
    niko "On top of that, let's look at our dinner party for a second, shall we?"
    show niko normal_base at right_char
    voice audio.niko_ch5_line71
    niko "First up, we have a former Paladin who can channel earth, wind, and fire. Let's also not forget the spectacle with the draconic fire earlier."

    "He flicked a glance at me."

    voice audio.niko_ch5_line72
    niko "Next we have an aldorith with violet hair who switched sides and can manipulate metal at will, an affinity that less than one percent of the population can even dream of."

    voice audio.svante_ch5_line76
    "At that, Svante visibly tensed, his fingers curling ever so slightly on the table. But he smiled and said nothing."

    voice audio.niko_ch5_line73
    niko "A talking robot with a mind of its own. And—"

    # play sound sfx_roboto_crash                 # PLACEHOLDER — Roboto crash SFX
    hide chunghee
    show roboto error at center_robot with Dissolve(0.2)
    voice audio.roboto_ch5_line17
    roboto "R-R-R-R-R-R-R-ooooooo- *crashes*"
    hide roboto
    show chunghee alt_neutral at center_char with Dissolve(0.2)
    show niko normal_ignore at right_char
    voice audio.niko_ch5_line74
    niko "Right. Moving on."
    voice audio.niko_ch5_line75
    niko "A green-haired toddler who, for some reason, spends his free time reading damn bibliographies instead of playing with toys."
    hide chunghee
    show tim shy at center_char_kids with Dissolve(0.2)
    "Tim blinked up at him from behind his book, entirely unfazed. Then, as if on cue, he calmly turned a page in his heavy tome—Tianho's Ancient Dynasties."

    tim "Hnn…"
    hide tim with Dissolve(0.1)
    voice audio.niko_ch5_line76
    niko "A crossdressing toddler who just so happens to be the crown Prince of Mjoll and carries around a smelly ragdoll named 'Tedda.'"
    show elias normal_happy at center_char_kids with Dissolve(0.2)
    "Elias suddenly giggled, completely unaware of the tension in the air. He held up his coloring book, showing it off proudly."
    voice audio.elias_ch5_line22
    elias "Look! Wainbow, daddy!"
    hide elias
    show tim alt_nervous at center_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line24
    tim   "Not now, Elias. The grown-ups are talking."
    hide tim with Dissolve(0.1)
    show niko normal_base at right_char
    voice audio.niko_ch5_line77
    niko  "And you have me. A Prophet of the death god, Enoch, who happens to be his Chosen."

    "Niko shot Yuxuan a slow, knowing smirk."

    show niko normal_serious at right_char

    niko "So tell me, Yuxuan—are you really that surprised that the man sitting with us is the Emperor of Kyeongjang?"
    voice audio.niko_ch5_line78
    "Yuxuan stared at him for a moment, then exhaled, shaking his head."
    hide niko
    show yuxuan alt_think at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line40
    yuxuan "You make a fair point."
    hide yuxuan
    show weng alt_base at right_flip with Dissolve(0.2)
    voice audio.weng_ch5_line54
    weng   "You're such an open-minded and understanding person, Master Yuxuan. The pinnacle of open-mindedness!"
    hide weng
    show yuxuan alt_smile at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line41
    yuxuan "Aww thank you, Miss Weng! Well, I am a veryyyyy understanding man, so—"
    show yuxuan normal_neutral at right_char

    show dorian normal_alt_calm at left_char # with Dissolve(0.2)
    "I buried my face in my palms."
    show dorian serious at left_char
    show chunghee normal_neutral at center_char with Dissolve(0.2)
    chung_hee "I see. You are all… quite the interesting group."

    "Chung-hee's expression remained unreadable. Svante suddenly spoke up, his voice quiet but firm."
    hide yuxuan
    show svante normal_neutral at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line77
    svante "If I may… I believe His Majesty is telling the truth."

    "A hush settled over the group. Svante's eyes were downcast."

    voice audio.svante_ch5_line78
    svante "Father said the Emperor of Kyeongjang was going to be the next target. He told us the Emperor was a sick, twisted, dishonorable person."

    "His hands clenched into fists."
    show svante normal_angry at right_char
    voice audio.svante_ch5_line79
    svante "And I believed him at first. I had no reason to but I believed him."
    voice audio.svante_ch5_line80
    svante "But… when I met you, Your Majesty, you were kind. You spoke to us with dignity. You offered us peace."
    voice audio.svante_ch5_line81
    svante "I didn't believe you could be the Emperor because you weren't the monster I was taught to fear."
    voice audio.svante_ch5_line82
    svante "But looking at it now, he must have been lying. Not that you weren't the Emperor but the part where you were a sick, twisted person."

    show chunghee normal_neutral at center_char
    "Chung-hee regarded him for a long moment, expression unreadable."
    "Then—he gave a small, approving nod."
    show chunghee alt_wink at center_char
    chung_hee "Thank you."
    show chunghee alt_neutral at center_char
    "The Emperor of Kyeongjang… No, Emperor Min-joon's son."
    "A thousand questions swirled in my mind. Questions about the past. About the Tragedy of Tianho. About why he was targeted. About why he was here."
    "But before I could voice a single thought—"
    "Weng sat the first dish down."

    "Her voice was warm and full of praise as she placed a steaming bowl in front of Yuxuan."
    hide svante
    hide chunghee
    show weng normal at right_flip
    with Dissolve(0.2)
    voice audio.weng_ch5_line55
    weng "Dragonfire curry for the incredibly intelligent, devilishly handsome, and world-renowned genius that is Master Yuxuan."
    # TODO: FOOD10
    "Yuxuan lit up like a child on his birthday."
    show dorian neutral at left_char
    show yuxuan normal_happy at center_char with Dissolve(0.2)
    yuxuan "Miss Weng! You shouldn't have! My precious dragonfire curry! Oh, how I've missed you!"

    "He clasped his hands together dramatically."
    "Meanwhile, Roboto whirred into view, carefully balancing trays of food."
    hide weng
    # end food 10

    show roboto happy at right_robot with Dissolve(0.2)
    voice audio.roboto_ch5_line18
    roboto "Robotoooo is ready to s-s-s-serve~ F-f-food is ready~"
    hide roboto
    show niko normal_base at right_char with Dissolve(0.2)
    voice audio.niko_ch5_line79
    niko   "The robot shouldn't be allowed to serve food. It might crash again."
    show yuxuan normal_angry at center_char
    voice audio.yuxuan_ch5_line42
    yuxuan "You're the only one who thinks that, Niko. Roboto is a technological marvel and- IT. DOES. NOT. CRASH."

    "Niko's eyes blinked."
    show niko normal_ignore at right_char 
    voice audio.niko_ch5_line80
    niko   "Yuxuan, I mean no disrespect to Roboto. It's amazing. But a while ago it almost crashed and brought down a jar filled with water in it."
    show yuxuan normal_lying at center_char
    voice audio.yuxuan_ch5_line43
    yuxuan "Why I never!"
    show niko normal_base at right_char
    voice audio.niko_ch5_line81
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

            show dorian neutral at left_char
            dorian "Yeah… Roboto did almost trip. But Niko caught it in time, so I don't think it matters much."
            show niko normal_base at right_char
            voice audio.niko_ch5_line82
            niko   "There you have it."

            # play sound sfx_roboto_beep          # PLACEHOLDER — Roboto beep SFX
            hide yuxuan
            show roboto bad_mood at center_robot with Dissolve(0.2)
            voice audio.roboto_ch5_line19
            roboto "M-m-m-master Dorian is c-c-correct! I was transporting water, but my sensors momentarily overloaded. Sir Niko was able to assist me."
            hide roboto
            show yuxuan alt_think at center_char with Dissolve(0.2)
            voice audio.yuxuan_ch5_line44
            yuxuan "Oh… Maybe some recalibration is in order. Can't have my masterpiece faltering under pressure."
            "Roboto blinked rapidly, its mechanical eyes adjusting."
            hide yuxuan
            show roboto happy at center_robot
            voice audio.roboto_ch5_line20
            roboto "C-c-confirmed! Roboto will undergo recalibration!"
            hide roboto
            show yuxuan normal_neutral at center_char with Dissolve(0.2)
            "Yuxuan sighed, adjusting his glasses."

            voice audio.yuxuan_ch5_line45
            yuxuan "Great. Now I feel guilty. Roboto, remind me to run diagnostics later."

            # play sound sfx_roboto_beep          # PLACEHOLDER — Roboto beep SFX
            voice audio.roboto_ch5_line21
            roboto "Reminder set! Diagnostics will begin at 20:00 hours!"

        "No. Roboto had it all under control.":
            $ ch5_roboto_witness = "no"
            $ yuxuan_affection += 1             # +1 Yuxuan affection

            "I shook my head, folding my arms."

            show dorian neutral at left_char
            dorian "No, Roboto had it under control."

            # play sound sfx_roboto_beep          # PLACEHOLDER — Roboto beep SFX
            hide yuxuan
            show roboto happy at center_robot with Dissolve(0.2)
            voice audio.roboto_ch5_line22
            roboto "D-d-data inconclusive. Roboto must recalibrate!!"
            hide roboto
            show yuxuan normal_happy at center_char with Dissolve(0.2)
            "Yuxuan's expression brightened, and he gave me a satisfied nod."

            voice audio.yuxuan_ch5_line46
            yuxuan "Thank you, Dorian. At least someone here has good judgment."

            show niko normal_ignore at right_char
            "Niko pinched the bridge of his nose."

            voice audio.niko_ch5_line83
            niko   "Oh, for the love of—"
            show yuxuan alt_smile at center_char
            voice audio.yuxuan_ch5_line47
            yuxuan "Let this be a lesson, Niko. One should never question the technological marvel that is Roboto."
    hide dorian
    hide yuxuan
    hide niko
    with Dissolve(0.1)
    "Roboto whirred smoothly across the room, carefully placing each dish in front of us."
    show roboto happy at center_robot with Dissolve(0.2)
    voice audio.roboto_ch5_line23
    roboto "Here is your f-f-f-food, Your Majesty. We lack information on Kyeongjang cuisine, but we have prepared a special dish from Gale."

    "As Roboto spoke, its small monitor flickered to life, displaying a video of hand signs."

    show roboto happy at center_robot
    voice audio.roboto_ch5_line24
    roboto "T-T-This is called mountain herb stew along with a plate of sautéed highland greens."
    voice audio.roboto_ch5_line25
    roboto "Cooked with garlic and a drizzle of fragrant mountain oil. Enjoy, Your Highness!"

    show chunghee normal_neutral at right_char 
    show dorian neutral at left_char
    with Dissolve(0.2)
    "Chung-hee's expression softened slightly. He raised his hands and responded with hand signs of his own."
    "Roboto paused for a moment before beeping happily."

    show roboto happy at center_robot
    voice audio.roboto_ch5_line26
    roboto "A-A-A-Affirmative! I will not call you Your Majesty. T-t-thank you, Sir Chung-hee!"
    hide chunghee
    show niko alt_tense at right_char with Dissolve(0.2)
    "Niko and Yuxuan paused, exchanging glances."

    voice audio.niko_ch5_line84
    niko   "Roboto knows sign language?"
    hide roboto
    show yuxuan normal_neutral at center_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line48
    yuxuan "I programmed Roboto to recognize multiple languages, but I don't remember programming sign language. Fascinating…"
    voice audio.weng_ch5_line56
    weng   "As is expected from our amazing and very talented inventor, Master Yuxuan!"
    show yuxuan alt_smile at center_char
    voice audio.yuxuan_ch5_line49
    yuxuan "Aww thank you, Miss Weng!"
    show niko normal_ignore at right_char
    voice audio.niko_ch5_line85
    niko   "Oh brother."

    show niko alt_irritate at right_char
    "Niko rolled his eyes, picked up his chopsticks and started eating."
    hide yuxuan

    show chunghee normal_neutral at center_char with Dissolve(0.2)
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
    
    scene lab_cave_on with Dissolve(0.1)
    show roboto happy at right_robot 
    show dorian neutral at left_char
    with Dissolve(0.2)
    "Roboto whirred in again, humming softly as it approached me with a steaming bowl."
    "The rich, savory aroma of black garlic and star anise filled the air, mingling with the sharper spice of Yuxuan's dragonfire curry."

    voice audio.roboto_ch5_line27
    roboto "Here are your Moonlit Noodles, M-M-Master D-D-Dorian!"
    # TODO: FOOD14

    "The little machine's voice stuttered slightly, but its movements were careful and precise as it placed the bowl before me. "
    "The deep, dark broth gleamed under the dim light, the noodles glistening as they curled beneath the surface."
    "Resting atop them were thin slices of braised beef, their edges caramelized to perfection, and a single soft-boiled tea egg, its yolk just barely runny."

    show yuxuan normal_happy at center_char with Dissolve(0.2)
    "Yuxuan leaned over with interest, his eyes lighting up."

    voice audio.yuxuan_ch5_line50
    yuxuan "Hey Dorian, do you know why the dish is called Moonlit noodles?"

    menu:
        "Is it because of the egg?":
            $ yuxuan_affection += 1             # +1 Yuxuan affection

            show dorian neutral at left_char
            "I looked at the egg and it vaguely looked like the moon."

            dorian "Is it because of the egg?"

            show yuxuan normal_neutral at center_char
            "Yuxuan looked at the bowl."

            voice audio.yuxuan_ch5_line51
            yuxuan "Oh you're right. I haven't thought of it that way."
            show dorian neutral at left_char
            dorian "You mean you didn't know, Yu?"
            show yuxuan normal_neutral at center_char
            voice audio.yuxuan_ch5_line52
            yuxuan "I don't know. That's why I'm asking."

        "I don't know.":

            show dorian neutral at left_char
            dorian "No. Why are they called that?"
            show yuxuan normal_neutral at center_char
            voice audio.yuxuan_ch5_line53
            yuxuan "I don't know. That's why I'm asking you."
            show dorian normal_alt_annoyed at left_char
            dorian "This is my first time eating these, Yu. Why would I know that?"
            show yuxuan normal_lying at center_char
            yuxuan "… Oh…"
            voice audio.yuxuan_ch5_line54
            yuxuan "Well, yeah. Figures. You don't really look like someone who dabbles in fine cuisine."

            "I raised an eyebrow."

            show dorian neutral at left_char
            dorian "What's that supposed to mean?"

            "Yuxuan waved his hand vaguely."

            show yuxuan normal_neutral at center_char
            voice audio.yuxuan_ch5_line55
            yuxuan "No, no, no. I didn't mean it in a bad way. I meant that you can eat almost anything and still be happy! Not many people are like you, Dorian."
            show dorian neutral at left_char
            dorian "I'll take that as a compliment. Thanks, Yu."

    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    show roboto happy at right_robot
    voice audio.roboto_ch5_line28
    roboto "M-m-m-master Dorian is a man of culture! M-m-my sensors detect a 92.3%% probability that he will e-e-e-enjoy this meal!"
    show yuxuan normal_neutral at center_char
    voice audio.yuxuan_ch5_line56
    yuxuan "But what happens if Dorian doesn't like it?"

    "There was a brief pause. Then—"

    show roboto error at right_robot
    voice audio.roboto_ch5_line29
    roboto "E-e-e-error! Scenario not calculated! Rebooting crisis protocol… Processing…"

    show dorian neutral at left_char
    "I sighed."

    dorian "Yu, stop messing with Roboto."
    show yuxuan alt_smile at center_char
    voice audio.yuxuan_ch5_line57
    yuxuan "It's just part of his crisis protocol subroutine, Dorian. He can handle it."

    "He leaned back, arms crossed, a knowing smirk tugging at his lips."

    voice audio.yuxuan_ch5_line58
    yuxuan "Here, I'll show you. Roboto, give me a compliment."

    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    show roboto happy at right_robot
    voice audio.roboto_ch5_line30
    roboto "A c-c-c-compliment? Certainly!"

    "The little machine beeped twice before its voice rang out."

    voice audio.roboto_ch5_line31
    roboto "M-M-Master Yuxuan, you are the greatest inventor Ena has ever known! Your intelligence will put the Almighty Tetrad Li Mengtia to shame!"
    show yuxuan alt_smile at center_char
    voice audio.yuxuan_ch5_line59
    yuxuan "Awww Roboto, you really know how to make a guy feel special."
    show roboto happy at right_robot
    voice audio.roboto_ch5_line32
    roboto "I-I-I'm glad you like it, Master Y-Y-Yuxuan! I-I-I try my b-b-best!"

    show dorian neutral at left_char
    "I let out a slow breath, stirring my noodles with my chopsticks. The warmth from the broth seeped into my fingers."
    hide roboto
    show chunghee normal_v2 at right_char with Dissolve(0.2)
    chung_hee "You should be proud of yourself, Sir Yuxuan."

    show yuxuan normal_happy at center_char
    "Yuxuan blinked, his smirk brightening into a smile as he turned to the Emperor."

    voice audio.yuxuan_ch5_line60
    yuxuan "Really, Your Majesty?"
    "Chung-hee nodded, setting his chopsticks down neatly beside his bowl."
    show chunghee alt_neutral at right_char
    chung_hee "Roboto is a marvel. Not only functional but adaptable. Few inventors create something with the ability to learn, let alone something with such… personality."
    chung_hee "In Kyeongjang, our automatons do not use sign language. They do not adapt to individual needs. I appreciate what Roboto did."

    jump ch5_dinner_talk

# =============================================================================
# SECTION 21: LABEL CH5_FOOD_TRUFFLE — IF Imperial Truffle Roast (Gale)
# =============================================================================

label ch5_food_truffle:
    scene lab_cave_on with dissolve
    show dorian neutral at left_char
    show roboto happy at right_robot
    with Dissolve(0.2)
    voice audio.roboto_ch5_line33
    roboto "Here it is! A meal fit for a conqueror—Master D-D-Dorian's Imperial Truffle Roast!"
    voice audio.roboto_ch5_line34
    roboto "Slow-roasted venison, glazed with truffles and wine reduction, served with buttered root vegetables, all arranged to p-p-please even the most discerning p-p-p-p-p-p-p~"
    dorian "Palate. Thanks, Roboto."

    # TODO: FOOD13
    "It placed the dish before me with an exaggerated flourish, its screen blinking in what I could only assume was enthusiasm."
    "The scent of roasted venison and truffle filled the air, rich and mouthwatering."

    show chunghee normal_neutral at center_char with Dissolve(0.2)
    "I eyed the venison, the glaze shimmering. Chung-hee leaned forward slightly, his sharp eyes scanning my plate with interest."

    chung_hee "Fascinating…"
    show dorian neutral at left_char
    dorian    "Something wrong?"

    show chunghee alt_smirk at center_char
    "He studied the dish as if committing every detail to memory."

    chung_hee "Kyeongjang is familiar with many foreign dishes, but an Imperial Truffle Roast is a rarity among our people."
    chung_hee "Truffles themselves are difficult to acquire within our lands… and venison, though not unheard of, is not often prepared in this manner."
    hide roboto
    show tim think at right_char_kids with Dissolve(0.2)
    "Tim, who had been quietly flipping through the pages of his latest book, had dropped it onto the table. He blinked up at Chung-hee, adjusting his glasses."

    voice audio.tim_ch5_line25
    tim "Your Majesty, I've read that ancient Kyeongjang dishes were once served on lacquered stone platters infused with medicinal resins."

    "The table fell silent."
    "I turned to Tim, half-expecting him to be making things up. But no—his expression was as serious as ever."

    show chunghee alt_tense at center_char
    "Chung-hee stiffened. Just barely, but enough for me to notice. His gaze, so often cool and composed, flickered with something else. A sharp glint of recognition."

    chung_hee "...That practice fell out of use centuries ago."

    "His fingers tapped once against the table."

    chung_hee "Few even remember it."

    "Tim tilted his head."
    show tim alt_normal at right_char_kids
    voice audio.tim_ch5_line26
    tim "It was abandoned before the time of the Death God Enoch, correct?"

    show chunghee normal_neutral at center_char
    "Chung-hee's head turned toward the boy fully now, shocked."

    voice audio.tim_ch5_line27
    tim "I read it from a pre-Enoch book. Very few literature from that time period are preserved. Luckily Master Yuxuan keeps a few in his big library."

    "He spread his tiny arms wide to emphasize just how massive Yuxuan's collection was."

    show chunghee normal_neutral at center_char
    "Chung-hee studied him with the same scrutiny he had given my meal moments before."

    chung_hee "How old are you?"

    "Tim adjusted his glasses."
    show tim alt_serious at right_char_kids
    voice audio.tim_ch5_line28
    tim   "Five."

    show dorian normal_alt_calm at left_char
    show chunghee alt_wink at center_char
    "I blinked."
    "Chung-hee blinked."
    "The two of us stared at him."
    show chunghee alt_neutral at center_char
    show dorian neutral at left_char
    dorian "Are you sure?"
    show tim alt_normal at right_char_kids
    voice audio.tim_ch5_line29
    tim    "Yes, I'm sure, sir Dorian."

    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX
    hide chunghee
    show roboto happy at center_robot with Dissolve(0.2)
    voice audio.roboto_ch5_line35
    roboto "R-R-Roboto confirms! Tim is 100%% five years old!"

    hide roboto
    show yuxuan normal_happy at center_char with Dissolve(0.2)
    yuxuan "Ahaha… don't mind Tim. He's just... Well, we call him a little genius here."
    hide yuxuan
    show chunghee normal_neutral at center_char with Dissolve(0.2)
    chung_hee "A five-year-old… quoting lost histories and the fall of divine ages..."
    show chunghee alt_smirk at center_char
    chung_hee "In Kyeongjang, wisdom is not measured by years, but by the depth of one's spirit. And yours, young scholar, is fathomless."

    show tim alt_pumped at right_char_kids
    "Tim beamed proudly, pushing up his glasses with both hands."
    voice audio.tim_ch5_line30
    tim "Anyway, thank you for confirming it, Your Majesty. I was just curious."

    jump ch5_dinner_talk

# =============================================================================
# SECTION 22: LABEL CH5_FOOD_HOTPOT — IF Fisherman's Hotpot (Hinami)
# =============================================================================

label ch5_food_hotpot:
    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX
    hide niko
    hide chunghee
    show roboto happy at right_robot
    with Dissolve(0.2)
    voice audio.roboto_ch5_line36
    roboto "A dish fit for a traveler of tides and a seeker of shadows! Presenting your Fisherman's Hotpot, M-M-Master D-D-Dorian—crafted with the heart of the sea and the soul of the island itself!"

    # TODO: FOOD15
    show dorian neutral at left_char
    dorian "Thank you, Roboto. It looks delicious."
    hide roboto
    show niko normal_base at right_char with Dissolve(0.2)
    "As I took the first sip of the miso broth, the rich umami flavor spread over my tongue, warming me instantly."
    "The fresh seafood, barely touched by the heat, still had that ocean-bright taste, balanced perfectly with the mild tofu and tender greens."
    "Beside me, Niko had his head bowed, hands loosely clasped."

    voice audio.niko_ch5_line86
    niko "Bless us O mighty Enoch and these thy gifts, which we are about to receive."
    voice audio.niko_ch5_line87
    niko "May this food restore our strength, giving new energy to tired limbs and bodies."

    "He finished his prayer and glanced at my bowl."

    show niko normal_smile at right_char
    voice audio.niko_ch5_line88
    niko   "Delicious, huh?"
    show dorian neutral at left_char
    dorian "Yeah. The miso broth with the seafood is a great combination."
    show niko normal_base at right_char
    voice audio.niko_ch5_line89
    niko   "It does. Used to have that all the time when I stopped by Hinami Port for fish and supplies."
    show dorian normal_alt_annoyed at left_char
    "I raised a brow."

    show dorian neutral at left_char
    dorian "Didn't peg you as the type to sit around a fire with a bunch of fishermen."
    show niko normal_smile at right_char
    voice audio.niko_ch5_line90
    niko   "Well, when you're a doctor in a small village in Hamatame, you take what you can get. They'd trade me fresh seafood, supplies for herbs and organic medicine."
    voice audio.niko_ch5_line91
    niko   "Oftentimes I'd end up sharing a meal with them."

    show niko normal_base at right_char
    "He stirred his spoon through the broth, a hint of nostalgia flickering across his face."

    voice audio.niko_ch5_line92
    niko "Hinami isn't as wealthy as Mjoll or Gale, but the sea is generous. The people there take care of each other. No one eats alone after a long day at sea."

    show dorian neutral at left_char
    dorian "I take it you miss your home nation?"
    show niko normal_base at right_char
    voice audio.niko_ch5_line93
    niko   "You could say that. They say that Hinami will be hosting the Tragedy of Tianho's anniversary tomorrow. Perhaps I'll—"

    "A small commotion at the other end of the table pulled my attention away."
    hide niko
    hide dorian
    show elias normal_mad at right_char_kids
    show tim alt_annoyed at left_char_kids
    with Dissolve(0.2)
    voice audio.tim_ch5_line31
    tim   "Elias, you need to eat your chicken. And your rice. And your vegetables."

    "Elias shook her head and clutched Tedda like a shield."

    voice audio.elias_ch5_line23
    elias "No!"

    "Tim sighed, pinching the bridge of his nose."

    voice audio.tim_ch5_line32
    tim "Elias, you can't just eat chocolate and sweets all the time!"

    show niko normal_smile at center_char with Dissolve(0.2)
    "Niko chuckled."

    voice audio.niko_ch5_line94
    niko "What seems to be the problem?"
    voice audio.tim_ch5_line33
    tim  "Elias won't eat his vegetables!"
    hide tim

    show dorian serious at left_char with Dissolve(0.2)
    dorian "Elias. We talked about this. You need to eat your vegetables."
    hide dorian
    show tim normal at left_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line34
    tim    "Listen to your father, Elias."
    show elias normal_sad at right_char_kids
    voice audio.elias_ch5_line24
    elias "But daddy…"
    show niko normal_smile at center_char
    voice audio.niko_ch5_line95
    niko   "Alright, kiddo. How about this—if you eat your chicken, rice, and veggies, I'll read you a bedtime story tonight. How's that sound?"

    show elias normal_happy at right_char_kids
    "Elias's eyes lit up."

    elias "A story?! Okay!"

    "Elias glanced at his plate, then back at Niko. He picked up his spoon and carefully scooped up a piece of chicken. After a moment's hesitation, he popped it into his mouth."

    show elias normal_happy at right_char_kids
    "Then he beamed again."

    voice audio.elias_ch5_line26
    elias "I eat!"
    voice audio.tim_ch5_line35
    tim   "(muttering) Manipulated by bedtime stories…"

    "After a pause, he fidgeted slightly before speaking up."
    show tim alt_nervous at left_char_kids
    voice audio.tim_ch5_line36
    tim  "I… I'm included too, Sir Niko, right? I can join the storytime… if you want…"

    show niko normal_smile at center_char
    "Niko grinned."
    show niko alt_base at center_char
    voice audio.niko_ch5_line96
    niko "Sure, but only if you eat your food too."
    voice audio.tim_ch5_line37
    tim  "Okay. Let's eat, Elias."

    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX
    hide tim
    hide elias
    hide niko
    show roboto happy at right_robot
    show dorian neutral at left_char
    with Dissolve(0.2)
    voice audio.roboto_ch5_line37
    roboto "C-c-cognitive reinforcement successful! Reward-based motivation confirmed as eff-eff-effective!"

    "I glanced at Niko, offering a nod of thanks."
    hide roboto
    show niko normal_base at right_char with Dissolve(0.2)
    dorian "Thanks for your help with Elias. Didn't know you were good with kids."

    "Niko shrugged, a small smile tugging at his lips."

    voice audio.niko_ch5_line97
    niko "You're welcome, Dorian."

    "I watched as Tim and Elias, now fully focused on their plates, quietly ate their food."

    show chunghee normal_neutral at center_char with Dissolve(0.2)
    "Across the table, Chung-hee had been quietly observing."

    chung_hee "Fascinating… You should be proud of yourself, Sir Niko."
    show niko normal_smile at right_char
    voice audio.niko_ch5_line98
    niko      "I used to have a lot of kid patients back in Hamatame. You learn a few tricks when you're treating scared little ones, Your Majesty."

    jump ch5_dinner_talk

# =============================================================================
# SECTION 23: LABEL CH5_FOOD_LAMB — IF Mjollian Mead-Braised Lamb (Mjoll)
# =============================================================================
label ch5_food_lamb:
    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX
    hide niko
    hide chunghee
    show roboto happy at right_robot
    with Dissolve(0.2)
    voice audio.roboto_ch5_line38
    roboto "Behold! A meal fit for a warrior! A dish crafted for the strong and the steadfast—M-M-Master D-D-Dorian, your Mjollian Mead-Braised Lamb awaits!"
    # TODO: FOOD11
    "I stared down at the plate in front of me. Thick, spiced mead sauce clung to the slow-braised lamb shank, its aroma warm and heady."
    "Beside it, a dense slice of black rye bread and a small dish of herbed butter sat neatly on the tray."
    "It looked rich—very rich. Heavy. Nothing like the plain food I usually ate."
    hide roboto
    show svante normal_neutral at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line83
    svante "Have you eaten that before, Sir Dorian? Back in Mjoll?"
    show dorian neutral at left_char
    dorian "I… don't remember eating this. I usually just made something easy—stews, boiled potatoes, whatever was quick."
    show svante normal_neutral at right_char
    voice audio.svante_ch5_line84
    svante "Did Father's cooks serve you food when you were working under him as a mercenary?"
    show dorian neutral at left_char
    dorian "No, I always refused. Dishes like this are too fancy for my taste back then."

    "I glanced at him, then back at the food."

    show svante normal_sad at right_char
    "Svante hesitated before exhaling softly, a sad smile ghosting his lips."

    voice audio.svante_ch5_line85
    svante "My mother used to love that dish. Before she got sick… back when she was still— back when people still talked about her."
    show dorian neutral at left_char
    dorian "Your mother?"
    show svante normal_sad at right_char
    voice audio.svante_ch5_line86
    svante "I doubt you'd know her sir Dorian. She was a songstress—a famous one, once. Back in Tianho, before she got sick."
    voice audio.svante_ch5_line87
    svante "Her voice used to be everywhere—on the radio, in the theaters. People adored her."

    "He stared down at the dish, a flicker of something bittersweet in his eyes."

    voice audio.svante_ch5_line88
    svante "She used to call that dish 'the taste of home.' Said it reminded her of the time before… everything changed."

    "I looked down at the dish again. To me, it was just another meal—fuel to keep going, nothing more. But to him? It was a memory."
    "I nudged the plate slightly in his direction."

    show dorian neutral at left_char
    dorian "You can have it if you want. I really don't mind. I'll just ask for something else—"

    show svante normal_nervous at right_char
    "Svante's eyes widened slightly."

    voice audio.svante_ch5_line89
    svante "What? No, I— I appreciate it, sir, but you should eat. It's a warrior's meal, after all. My mom would have liked that, though."
    voice audio.svante_ch5_line90
    svante "You should eat it, sir Dorian. Who knows? Maybe you'll grow to like something other than stale bread and ration bars, sir."

    show dorian normal_alt_annoyed at left_char
    "I rolled my eyes."

    dorian "You're making it sound like that's all I eat."
    show svante normal_nervous at right_char
    voice audio.svante_ch5_line91
    svante "No, no, no! I apologize, sir, I—"

    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX
    show roboto happy at center_robot with Dissolve(0.2)
    voice audio.roboto_ch5_line39
    roboto "M-m-m-my sensors indicate that M-M-Master Dorian is just fooling around."
    show svante normal_nervous at right_char
    voice audio.svante_ch5_line92
    svante "Oh, um… S-Sorry…"

    show dorian neutral at left_char
    "I shrugged, took my chopsticks, and went to eating."

    "A few minutes after I started eating, Weng approached, setting down another dish with practiced ease."
    hide svante
    hide dorian
    hide roboto
    show weng normal at right_flip
    show tim happy at left_char_kids
    with Dissolve(0.2)

    weng "Here are some Tianho dumplings I prepared. Extra portions."
    voice audio.tim_ch5_line38
    tim  "Yay! Elias, you need to try these!"

    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    show roboto happy at center_robot with Dissolve(0.2)
    voice audio.roboto_ch5_line40
    roboto "Tianho dumplings—suitable for any occasion!"

    "She then placed a fresh pot of tea in the center of the table, steam curling elegantly from its spout."

    show weng normal at right_flip with Dissolve(0.2)
    weng "And some tea. Freshly brewed from tea leaves from Tianho. I hope you like it."

    hide roboto
    show yuxuan normal_happy at center_char with Dissolve(0.2)
    yuxuan "The teacup looks beautiful, Miss Weng!"

    show tim normal at left_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line39
    tim "We got it yesterday from a bargain store, Master Yuxuan!"

    show weng normal at right_flip
    weng "Now, everyone grab a cup and I'll pour you some."
    hide yuxuan
    hide tim
    show svante normal_neutral at left_char
    with Dissolve(0.2)
    "Svante glanced at her, a thoughtful expression crossing his face."
    voice audio.svante_ch5_line93
    svante "Miss Weng, you're from Tianho, right?"

    show weng alt_close_eyes at right_flip
    "Weng's hands paused, just for a fraction of a second, as she poured the tea."

    show weng normal at right_flip
    weng "Sharp observation, young man. Yes, I'm from Tianho."

    show svante normal_neutral at left_char
    "Svante nodded, not noticing the way her expression shifted—gentle, almost… nostalgic."

    voice audio.svante_ch5_line94
    svante "My mother always spoke about someone she loved there. Said she left part of her heart in Tianho."

    show weng alt_close_eyes at right_flip
    "For the briefest moment, Weng's fingers stilled. A flicker of something passed through her eyes—too fleeting to name."
    "Then, just as quickly, she was smiling again, her face unreadable."

    show weng normal at right_flip
    weng "Did she, now?"

    show svante normal_sad at left_char
    voice audio.svante_ch5_line95
    svante "She said he made the best Moonlit Noodles she ever had. She used to say that if life had been different, maybe she would've—"

    "He stopped, shaking his head."
    show svante normal_base at left_char
    voice audio.svante_ch5_line96
    svante "Never mind, Miss. Sorry. It's just something she used to say."

    show weng happy at right_flip
    weng "The lover must have been quite the woman to make such an impression."

    show svante normal_neutral at left_char
    voice audio.svante_ch5_line97
    svante "Oh, that's right… She never told me if it was a man or a woman. Sorry, I assumed…"

    show weng normal at right_flip
    weng "Don't worry about it, Svante. You think too much. Eat up. You too, Sir Burnham."
    hide svante
    show dorian neutral at left_char with Dissolve(0.2)
    dorian "Thanks, Miss Weng."

    show roboto happy at center_robot with Dissolve(0.2)
    voice audio.roboto_ch5_line41
    roboto "Would you like more Tianho dumplings?"
    hide roboto
    show tim normal at center_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line40
    tim "I'd love more please!"
    hide dorian
    hide tim
    show niko normal_smile at left_char with Dissolve(0.2)
    voice audio.niko_ch5_line99
    niko "This tea is amazing. I'd love to get some seeds so I can brew this."

    show weng happy at right_flip
    weng "Please, have some more, sir Niko."
    
    show yuxuan normal_neutral at center_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line61
    yuxuan "By the way, Hinami would be hosting the Tragedy of Tianho's anniversary tomorrow. Miss Weng, please don't forget to buy some more fish."

    show weng alt_calm at right_flip
    weng "I'll take care of it, Master Yuxuan."
    hide niko
    hide yuxuan
    show svante normal_happy at left_char with Dissolve(0.2)
    voice audio.svante_ch5_line98
    svante "Hinami's hosting this year? That's great! Maybe they brought some of their tropical fish to sell. Mom didn't eat seafood that often but she loved ganderbilt."

    show weng normal at right_flip
    weng "I think they will, sir Svante. Hinami's trade ships arrived this morning—I saw the sails near the eastern docks."

    show svante normal_happy at left_char
    voice audio.svante_ch5_line99
    svante "They're already here?! Wow…"

    "Weng poured tea for our other companions. Then, she handed Svante a teacup, her fingers brushing his just for a second."

    show weng alt_calm at right_flip
    weng "By the way, you have your mother's eyes, Svante."

    show svante normal_nervous at left_char
    "Svante blinked."

    voice audio.svante_ch5_line100
    svante "Th-Thanks, Miss Weng. Wait, how did you kn—"

    show chunghee normal_neutral at center_char with Dissolve(0.2)
    chung_hee "I hope your mother is doing well, Svante."

    show svante normal_neutral at left_char
    "Svante swallowed, his expression carefully neutral."

    voice audio.svante_ch5_line101
    svante "Thank you, Your Majesty. I can only hope."

    jump ch5_dinner_talk

# =============================================================================
# SECTION 24: LABEL CH5_FOOD_COMMON — OMMITTED
# =============================================================================

# =============================================================================
# SECTION 25: LABEL CH5_DINNER_TALK — Gustav Choice / Dinner Conversation
# =============================================================================

label ch5_dinner_talk:
    scene lab_cave_on with dissolve

    show chunghee normal_neutral at center_char with Dissolve(0.2)
    chung_hee "And please, don't call me Your Majesty. I'm no Emperor here. You all saved my life."
    chung_hee "I told Roboto this before, but I'll say it again—"
    chung_hee "Please. Call me Chung."

    "A brief silence followed. Then, I nodded."

    show dorian neutral at left_char with Dissolve(0.2)
    dorian "Chung's alright."

    show yuxuan normal_happy at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line62
    yuxuan "It's a great name!"

    show chunghee alt_smirk at center_char
    chung_hee "Thank you."
    hide yuxuan

    show weng happy at right_flip with Dissolve(0.2)
    weng "It's a wonderful name for a wonderful gentleman such as yourself, Sir Chung."

    "She smiled and raised the teapot."

    weng "Would you like more tea, sir Chung?"

    show chunghee normal_neutral at center_char
    chung_hee "I would love some more."
    hide chunghee
    hide dorian
    hide weng
    show roboto happy at center_robot
    show niko normal_base at right_char
    show svante normal_happy at left_char 
    with Dissolve(0.2)
    voice audio.roboto_ch5_line42
    roboto "Want another dumpling, sir Niko? Sir Svante?"
    voice audio.niko_ch5_line100
    niko "Another please. Thanks."
    svante "Don't mind if I do! Thanks a lot!"
    hide niko
    hide svante
    show tim normal at left_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line41
    tim "Elias, want some tea?"

    show elias normal_neutral at right_char_kids with Dissolve(0.2)
    voice audio.elias_ch5_line27
    elias "Mmm… Just water please!"

    show roboto happy at center_robot
    voice audio.roboto_ch5_line43
    roboto "C-c-c-coming right up!"

    hide roboto
    hide elias
    hide tim
    with Dissolve(0.1)
    "We continued eating."
    "I focused on finishing my plate first—I was hungry."
    "The dishes were nothing short of perfection. Weng was a damn good cook."

    show dorian neutral at left_char
    show elias normal_happy at right_char_kids 
    with Dissolve(0.2)
    "Across from me, Elias had already devoured half of his plate, looking both satisfied and slightly overwhelmed."
    hide elias with Dissolve(0.1)
    "I glanced around. Once everyone had eaten their fill, I set down my chopsticks and spoke up."
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    dorian "So, Chung. Any idea why the kingdom of Mjoll wanted you killed?"
    show chunghee alt_tense at right_char
    show dorian serious at left_char
    "The light-hearted atmosphere dimmed instantly. Chung-hee's expression darkened."
    "He met my gaze. Then, calmly, with the weight of finality, he spoke."

    chung_hee "I will end the life of King Gustav Nordstrom."

    "The entire table went silent."

    show dorian serious at left_char
    "I felt my grip tighten around my cup. The room had grown heavy, like a storm rolling in. Across from me, Svante's entire body went rigid, his fingers barely twitching against the table."
    hide chunghee
    show svante normal_nervous at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line102
    svante "?!"
    hide svante
    show niko alt_tense at right_char with Dissolve(0.2)
    "Niko leaned forward, brows furrowing."
    voice audio.niko_ch5_line101
    niko  "…What?"
    hide niko with Dissolve(0.1)
    "Weng set her teacup down slowly, her voice barely above a whisper."
    show weng alt_nervous at right_flip with Dissolve(0.2)
    weng "By the stars…"

    show chunghee normal_neutral at center_char
    "Chung-hee remained composed, his gaze unwavering."

    chung_hee "King Gustav seeks to claim the Divine Weapon. He wishes to rule over all nations of Ena."
    hide weng
    show niko normal_base at right_char
    voice audio.niko_ch5_line102
    niko      "Divine Weapon? What are you talking about?"

    show chunghee normal_v2 at center_char with Dissolve(0.2)
    "Chung-hee didn't blink. He met our gazes."
    show chunghee normal_neutral at center_char
    chung_hee "Five years ago, King Long Shen spoke to my father about a weapon unlike any other. A relic forged to defy the laws of life and death itself."
    show chunghee alt_neutral at center_char
    chung_hee "A weapon meant to raise the dead. To bring back entire armies."

    "A weighted silence followed. I had never heard of such a thing. And judging by the expressions around the room, neither had they."
    "Tim shook his head, pushing his glasses up the bridge of his nose."
    hide niko
    show tim alt_nervous at right_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line42
    tim "…I… don't think I've ever read about anything like that, Sir Chung."
    hide tim
    show yuxuan alt_think at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line63
    yuxuan "Hmm… That doesn't sound good. If Tim hasn't read about it, it probably doesn't exist."
    hide yuxuan
    show weng alt_close_eyes_nervous at right_flip with Dissolve(0.2)
    weng "That is true, Master Yuxuan."

    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    "Roboto's glowing eyes flickered. The whir of his internal mechanisms filled the room as he processed the information."
    hide weng
    show roboto bad_mood at right_robot with Dissolve(0.2)
    voice audio.roboto_ch5_line44
    roboto "Checking… C-C-C-Checking library r-r-r-records…"
    show roboto happy at right_robot
    voice audio.roboto_ch5_line45
    roboto "Search concluded! N-N-No records in the library about a so-called 'DIVINE WEAPON.'"
    hide roboto
    show svante normal_neutral at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line103
    svante "Legends speak of weapons blessed—or cursed— but none have ever mentioned such a thing as a weapon bringing back people to life."
    hide svante
    show niko normal_base at right_char with Dissolve(0.2)
    voice audio.niko_ch5_line103
    niko   "I've read all of Enoch's chronicles. Every single one. Not one of them mentions a Divine Weapon."
    show niko alt_tense at right_char
    "He leaned forward, gaze sharp."
    voice audio.niko_ch5_line104
    niko "Do you even know where this thing is?"
    show chunghee normal_neutral at center_char
    chung_hee "No. Only that it is somewhere in Tianho."
    chung_hee "The fact remains. It must never fall into King Gustav's hands."
    chung_hee "I will end him before that happens."

    hide niko
    show yuxuan normal_sad at right_char with Dissolve(0.2)
    "Yuxuan let out a sharp breath, leaning back in his chair."
    voice audio.yuxuan_ch5_line64
    yuxuan "I was not expecting that with my tea."
    hide yuxuan
    show svante normal_nervous at right_char with Dissolve(0.2)
    "Svante's fingers trembled against the table. His voice was unsteady."
    voice audio.svante_ch5_line104
    svante    "Kill… Father? A-Are you sure of this, sir Chung?"
    show chunghee normal_neutral at center_char
    chung_hee "I would not speak of such things lightly."

    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    "Roboto, usually cheerful, gave a low whirring sound."
    hide svante
    show roboto bad_mood at right_robot with Dissolve(0.2)
    voice audio.roboto_ch5_line46
    roboto "D-d-d-danger level escalating. Adjusting threat parameters… I-I-I strongly advise against making dangerous statements out loud!"

    hide roboto
    show niko normal_ignore at right_char with Dissolve(0.2)
    "Niko exhaled sharply, rubbing his temples."
    voice audio.niko_ch5_line105
    niko "You're talking about regicide, Chung."
    show chunghee normal_v2 at center_char
    chung_hee "If he succeeds, countless lives will be lost. I will not allow it."
    hide niko
    show svante normal_angry at right_char with Dissolve(0.2)
    "Svante's hands curled into fists. He hesitated before speaking, voice shaking just slightly."
    voice audio.svante_ch5_line105
    svante "If I may, how do you intend to k-kill Father, sir Chung?"

    show chunghee alt_neutral at center_char
    "Chung-hee lowered his gaze for a moment."

    chung_hee "Cheonmyeong Gyeol…"

    show svante normal_nervous at right_char
    "Svante blinked, confused."

    voice audio.svante_ch5_line106
    svante "Huh? Chanmong…"
    show chunghee normal_neutral at center_char
    chung_hee "Cheonmyeong Gyeol… A duel between two rulers to the death."

    "The words seemed to echo through our minds."
    "For a moment, nobody spoke. Then, from the far end of the table—"

    hide svante

    show tim alt_nervous at right_char_kids with Dissolve(0.2)
    "Tim straightened, his eyes widening with recognition."
    voice audio.tim_ch5_line43
    tim "Wait… you mean the ancient trials of Kyeongjang? The ones that determined a kingdom's fate with a single battle?"
    voice audio.tim_ch5_line44
    tim "I've read that before! In pre-Enoch books!"

    show chunghee normal_neutral at center_char
    "Chung-hee gave a single nod."

    chung_hee "Yes. It is an ancient tradition, one older than any war on record."
    chung_hee "Long ago, the rulers of old would stake their lives in battle rather than sacrifice their people to war. A single duel—no armies, no bloodshed beyond their own. The winner would decide the fate of nations. It was a trial of honor, strength, and destiny."
    show dorian neutral at left_char
    dorian    "I've never heard of that before."
    hide tim
    show niko normal_base at right_char with Dissolve(0.2)
    voice audio.niko_ch5_line106
    niko      "Me neither. I don't think those are present in any of the Death God's scriptures."
    hide niko
    "Tim's expression glowed with excitement."

    show tim happy at right_char_kids with Dissolve(0.2) 
    voice audio.tim_ch5_line45
    tim   "I knew it! The texts said the greatest rulers of the old dynasties fought like this! Right, Elias?"
    hide tim
    show elias alt_joy at right_char_kids with Dissolve(0.2)
    voice audio.elias_ch5_line28
    elias "Hehe. Tedda says I love you, Tim!"
    tedda "..."
    hide elias
    show tim alt_annoyed at right_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line46
    tim   "Umm… never mind."
    hide tim
    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    show roboto happy at right_robot with Dissolve(0.2)
    voice audio.roboto_ch5_line47
    roboto "Tim's knowledge is accurate. The Cheonmyeong Gyeol was considered the ultimate test of kingship. Only the worthy could survive."
    hide roboto 
    show yuxuan alt_smile at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line65
    yuxuan "That's Tim for you. Always knowing the old stories."
    show yuxuan alt_neutral at right_char

    show chunghee normal_neutral at center_char
    chung_hee "I challenged Gustav months ago. He only recently accepted."

    show yuxuan normal_neutral at right_char
    "Yuxuan leaned back in his chair, one brow arching in curiosity."

    voice audio.yuxuan_ch5_line66
    yuxuan "Then tell me, Chung—if King Gustav agreed to the duel, why did he send a battalion of soldiers and Aldoriths after you?"

    show chunghee normal_neutral at center_char
    "A shadow passed over Chung-hee's face."

    hide yuxuan
    show svante normal_sad at right_char with Dissolve(0.2)
    "I turned to Svante."

    dorian "Svante, do you know anything about this?"

    show svante normal_sad at right_char
    "Svante looked down, his hands tightening into fists. He swallowed hard before shaking his head."

    voice audio.svante_ch5_line107
    svante "N-no. I… We were only told by Father that Chung would be there. He didn't tell us anything else."
    hide svante 
    show niko normal_ignore at right_char with Dissolve(0.2)
    "Niko scoffed. He leaned back, arms crossed, his expression dark with disgust."
    voice audio.niko_ch5_line107
    niko "What a coward."
    "Weng approached the table with practiced grace, a porcelain teapot cradled gently in her hands."

    hide niko
    show weng normal at right_flip with Dissolve(0.2)
    weng   "Perhaps a calming tea is just what you boys need. Should I pour some more?"
    hide weng
    show svante normal_neutral at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line108
    svante "Yes, please. Thank you, miss."
    hide svante
    show niko normal_base at right_char with Dissolve(0.2)
    voice audio.niko_ch5_line108
    niko   "Yeah…. Thanks."

    "Beside them, Tim reached across the table, cheerfully nudging a plate forward."
    hide niko
    show tim happy at right_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line47
    tim   "Here, have some more crumpets sirs! They go well along with the tea."
    hide tim
    show svante normal_neutral at right_char with Dissolve(0.2)
    "Svante took one, though his hands still trembled slightly as he brought it to his plate."
    voice audio.svante_ch5_line109
    svante "T-Thank you."

    show chunghee normal_neutral at center_char
    "Across the table, Chung-hee inhaled deeply, his hands resting flat against the polished wood."

    chung_hee "I was honestly surprised… A king should be… strong, just, honorable…"
    hide svante
    show yuxuan alt_smile at right_char with Dissolve(0.2)
    "Yuxuan snorted. Then he laughed."
    voice audio.yuxuan_ch5_line67
    yuxuan "Hahaha! King Gustav? Honorable? Hah! That's the best joke I've heard all day!"

    show dorian normal_alt_calm at left_char
    "I exhaled sharply, shaking my head."

    menu:
        "Don't be naïve, Chung.":
            $ ch5_chunghee_speech = "naive"
            $ chunghee_affection -= 1           # -1 Chung-hee affection
            hide yuxuan
            show chunghee normal_neutral at right_char
            show dorian serious at left_char
            with Dissolve(0.2) 
            dorian "You're being naïve, Chung."

            show chunghee normal_sad at right_char
            "Chung-hee frowned."

            show chunghee normal_angry at right_char
            chung_hee "Those in power need to have honor. They won't be sitting in their thrones otherwise. People follow them for a reason. They—"
            show dorian angry at left_char
            dorian    "Honor doesn't rule kingdoms. Power does. And those who don't accept that? They get crushed beneath those who do."
            show dorian serious at left_char
            show chunghee normal_sad at right_char
            "For the first time, doubt flickered in Chung-hee's eyes. But it was quickly buried under quiet defiance."

            chung_hee "I..."
            chung_hee "You're wrong, Dorian."
            show chunghee alt_tense at right_char
            "He turned his gaze away, staring at the table."

        "It's inspiring how you still believe in that.":
            $ ch5_chunghee_speech = "inspiring"
            $ chunghee_affection += 1           # +1 Chung-hee affection
            hide yuxuan
            show chunghee normal_neutral at right_char
            show dorian neutral at left_char 
            with Dissolve(0.2)
            "I sighed, rubbing the back of my neck."
            show chunghee alt_wink at right_char
            dorian "I don't know if I agree with you, Chung… but it's inspiring how you still believe in that."
            "Chung-hee blinked, caught off guard. Then, slowly, a small, grateful smile crossed his face."
            chung_hee "You… You think so?"

            show dorian normal_alt_neutral at left_char
            "I nodded."

            dorian "Maybe I've seen too much of the world to believe in nobility anymore… but it's not a bad thing to hold onto."

            show chunghee normal_neutral at right_char
            "Chung-hee's shoulders eased, some of the tension melting away."

            chung_hee "Then I will prove to you that nobility isn't dead, Dorian."

    jump ch5_divine_weapon


# =============================================================================
# SECTION 26: LABEL CH5_DIVINE_WEAPON — Chung Reveals More / Tea Scene
# =============================================================================

label ch5_divine_weapon:
    scene lab_cave_on with dissolve
    show dorian neutral at left_char
    show chunghee normal_neutral at center_char
    show yuxuan normal_neutral at right_char
    with Dissolve(0.2)
    "Yuxuan leaned forward, swirling the tea in his cup before raising an eyebrow."

    voice audio.yuxuan_ch5_line68
    yuxuan "Chung, if I may ask—why are you alone? Don't Emperors get, like… I don't know, guards or something?"

    "He gestured vaguely with his free hand."
    show yuxuan alt_mid_close_eyes at right_char
    voice audio.yuxuan_ch5_line69
    yuxuan "I remember when the previous Emperor of Kyeongjang visited Tianho. He was flanked by an entire regiment of soldiers."

    show chunghee normal_v2 at center_char
    "Chung-hee nodded, his gaze distant, as if recalling the memory himself."

    show yuxuan normal_normal at right_char
    chung_hee "Yes… my father and my mother went to Tianho with an honor guard. His visit was meant to be a grand affair—fanfare, ceremony. His presence symbolized Kyeongjang standing as one with Ena."

    "He let out a quiet breath, then shook his head."

    chung_hee "But I never sought such treatment. King Gustav and I agreed to a Cheonmyeong Gyeol."
 
    "He paused, glancing at Svante for the briefest moment before looking away."

    show chunghee alt_neutral at center_char
    chung_hee "So I believed…"

    "His fingers brushed against the table's surface, contemplative."

    chung_hee "I saw no need to march with banners or soldiers. I came alone, as an Emperor of Kyeongjang should in a duel to the death. But Gustav…"

    show dorian serious at left_char
    "His jaw tightened."

    show chunghee normal_angry at center_char
    chung_hee "King Gustav did not honor our agreement. He sent his army. His Aldoriths. His soldiers. Assassins."

    "A cold silence settled over the table."
    hide yuxuan
    show svante normal_sad at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line110
    svante    "I apologize again. Please forgive me, sir. I—"
    show chunghee alt_neutral at center_char
    chung_hee "No need to apologize. It's the ruler who makes the decisions."
    show dorian neutral at left_char
    dorian    "And it led you to us."
    hide svante
    show yuxuan normal_happy at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line70
    yuxuan    "By the goodness of the Prosperity Dragon, you're still alive. Praise be!"
    hide yuxuan
    show niko normal_base at right_char with Dissolve(0.2)
    voice audio.niko_ch5_line109
    niko      "That bastard Gustav. Can you imagine travelling thousands of miles for a duel just for you to be the target of assassination?"

    show chunghee normal_neutral at center_char
    "Chung-hee reached into the folds of his robes and pulled out a small, ornate object—an amulet, its surface shimmering with emerald green light."

    chung_hee "I didn't travel. If not for this, I would not be here."

    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX
    hide niko
    show roboto bad_mood at right_robot with Dissolve(0.2)
    voice audio.roboto_ch5_line48
    roboto "Powerful device detected. Anomaly class: High-tier. Likelihood of survival increase: 89.4%%. E-E-E-E-Errr-r-r-r-r-r—"

    # play sound sfx_roboto_crash                 # PLACEHOLDER — Roboto crash SFX

    show roboto error at right_robot
    roboto "*crashes*"

    hide roboto
    show yuxuan normal_happy at right_char with Dissolve(0.2)
    "Yuxuan whistled, leaning in."

    voice audio.yuxuan_ch5_line71
    yuxuan "Wow!"
    show yuxuan normal_normal at right_char
    show chunghee normal_neutral at center_char
    chung_hee "This was the last thing found on my parents' bodies. Tianho gave to us after the day of the tragedy."
    hide yuxuan
    show weng sad at right_flip with Dissolve(0.2)
    weng "That's too sad. I'm so sorry Sir Chung."

    show dorian serious at left_char
    "I stared at the amulet, my gaze locked onto its swirling green glow. There was something about it—something calling to me."
    "And then, as if a switch flipped in my mind, I remembered something. The amulet Elias wore back in Mjoll."
    "My breath hitched. Could it be—? Could this have the same power?"
    "No, it couldn't."

    hide weng
    show yuxuan normal_happy at right_char with Dissolve(0.2)
    "Yuxuan, of course, was already leaning in, his eyes gleaming with barely contained excitement."

    voice audio.yuxuan_ch5_line72
    yuxuan "Chung, is it okay if I touch it?"

    show dorian normal_alt_annoyed at left_char
    "I rolled my eyes."

    dorian "Yu!"
    show dorian serious at left_char
    hide yuxuan 
    show weng alt_base at right_flip with Dissolve(0.2)
    weng   "Please forgive my master, Sir Chung."
    hide weng
    show yuxuan alt_neutral at right_char with Dissolve(0.2)
    "Yuxuan threw up his hands."
    voice audio.yuxuan_ch5_line73
    yuxuan "What? I was just asking a question!"
    hide yuxuan
    hide chunghee
    show elias normal_happy at right_char_kids 
    show tim alt_pumped at center_char_kids
    with Dissolve(0.2)
    "Tim suddenly perked up, his small hands clapping together."   

    voice audio.tim_ch5_line48
    tim   "Can I touch it too, Mister Chung? I promise I'll take good care of it!"
    voice audio.elias_ch5_line29
    elias "Me too! And Tedda!"
    show tim alt_annoyed at center_char_kids
    voice audio.tim_ch5_line49
    tim   "Hey I was first, Elias!"
    hide tim
    hide elias
    show weng alt_close_eyes at right_flip with Dissolve(0.2)
    weng  "Tim, let the adults talk."
    hide weng

    show chunghee normal_neutral at center_char
    show niko normal_base at right_char
    with Dissolve(0.2)
    "Chung-hee blinked, clearly caught off guard by all the attention. He hesitated for a moment before finally nodding."

    chung_hee "Please… be my guest?"

    show niko alt_tense at right_char
    "Niko raised a brow, folding his arms."

    voice audio.niko_ch5_line110
    niko "Your Majest—Chung. You don't have to let him touch your amulet. We know it's sacred."

    show chunghee alt_smirk at center_char
    "Chung-hee offered a small smile."

    chung_hee "Don't worry, Sir Niko. You all proved that I can trust you with my life. What's a small amulet compared to that?"
    show chunghee normal_neutral at center_char

    hide niko
    hide chunghee
    show yuxuan normal_happy at right_char 
    show roboto happy at center_robot
    with Dissolve(0.2)
    "Yuxuan immediately whooped, fist-pumping the air."

    voice audio.yuxuan_ch5_line74
    yuxuan "Yes! Woohoo! Roboto, engage study mode!"

    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX
    voice audio.roboto_ch5_line49
    roboto "O-o-on it, Master Y-Y-Yuxuan! Engaging scanning proc-proc-process—ERROR! Unstable energy detected! I r-r-recommend caution!"

    show yuxuan normal_normal at right_char
    "Before Roboto could finish his analysis, Yuxuan had already reached out, his fingertips brushing the amulet's cool, engraved surface."
    show yuxuan alt_mid_close_eyes at right_char
    "A deep hum pulsed through the air. The sound wasn't just audible—it was something I could feel in my chest, like the distant vibration of a temple bell."
    "Yuxuan's eyes lit up with childlike wonder. He giggled, completely ignoring Roboto's warning."

    show yuxuan normal_happy at right_char
    voice audio.yuxuan_ch5_line75
    yuxuan "Ooooh! This thing is buzzing! You feel that? Dorian! Come! Touch!"
    hide yuxuan
    show svante normal_nervous at right_char with Dissolve(0.2)
    voice audio.svante_ch5_line111
    svante "S-Sir Yuxuan! Are you sure you can touch it like that?"
    hide svante
    show yuxuan normal_happy at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch5_line76
    yuxuan "Of course! Come on! Touch it, Svante! You too, Niko!"
    hide yuxuan
    show niko normal_ignore at right_char with Dissolve(0.2)
    voice audio.niko_ch5_line111
    niko   "Not interested…"
    hide niko
    show tim happy at right_char_kids with Dissolve(0.2)
    voice audio.tim_ch5_line50
    tim    "I'm interested!"
    hide tim 
    show weng serious at right_flip with Dissolve(0.2)
    weng   "No, Tim. No."
    hide weng
    show yuxuan normal_happy at right_char with Dissolve(0.2)

    show dorian normal_alt_calm at left_char
    "I sighed, pinching the bridge of my nose."

    show dorian normal_alt_neutral at left_char
    dorian "Yu, you are way too excited about this."
    show yuxuan normal_happy at right_char
    voice audio.yuxuan_ch5_line77
    yuxuan "Come on, Dorian! Touch it! What's the worst that could happen?"

    show dorian normal_alt_neutral at left_char
    "Reluctantly, I reached forward."
    "The moment my fingers made contact—"

    jump ch5_amulet_vision


# =============================================================================
# SECTION 27: LABEL CH5_AMULET_VISION — Dorian Touches the Amulet
# =============================================================================

label ch5_amulet_vision:

    # play sound sfx_amulet_vision                # PLACEHOLDER — amulet vision SFX
    show dorian normal_alt_tense at left_char
    dorian "ARRGHHHH!!!"
    hide roboto
    hide yuxuan
    show niko normal_anger at right_char with Dissolve(0.2)
    voice audio.niko_ch5_line112
    niko   "Dorian!"

    # [COMMENT: bg_white_screen — total white, void, endless]
    scene plain_white with flash            # PLACEHOLDER — white screen flash
    # stop music fadeout 0.5
    # play music ost_amulet_vision fadein 0.5     # PLACEHOLDER — amulet vision theme

    "A shockwave of raw energy erupted through me."
    "A tidal wave of power slammed into my very soul, knocking the breath from my lungs. My vision fractured—splintering like broken glass. My knees buckled."
    scene black with dissolve
    "Darkness. Total Darkness."
    "Then, I heard voices. Echoes."
    "A half-naked man with wings."
    "His golden eyes burned with urgency. Feathers glistened under an unseen light, his presence radiant yet commanding."

    show magnus alt_shocked at center_char, dream_haze
    voice audio.magnus_ch5_line1
    magnus "Dragonkin!! We don't have much time!"

    "I staggered backward."

    voice audio.magnus_ch5_line2
    magnus "They know you're here! Come to me!"

    "His wings flared wide, winds surging from nowhere. The world around me warped, twisted—"
    "Then—"

    hide magnus
    # [COMMENT: bg_sealed_door — underground chamber, blood, torchlight — Min-joon's death]
    # scene bg_sealed_door with dissolve          # PLACEHOLDER — sealed underground chamber
    # stop music fadeout 0.5
    # play music ost_minjoon_memory fadein 0.5    # PLACEHOLDER — Min-joon memory theme

    scene kyeonjang_palace with Dissolve(0.9)

    "Blood. Darkness. Betrayal."
    "I saw him."
    show king_gustav at right_char 
    with Dissolve(0.2)
    "A man, regal yet crumbling—his robes once pristine, now soaked in his own blood."
    "Emperor Min-joon."
    "He was on his knees, gasping, one hand clutching a fatal wound at his side. His breath came in ragged, uneven bursts."
    "Before him—King Gustav."
    "A towering shadow, eyes wild with fury."

    # TODO: minjoon sprite
    voice audio.minjoon_ch5_line1
    emperor_minjoon "Heh. *coughs*"
    king_gustav     "You… You TOOK AWAY MY ONE CHANCE!"

    "He raised his blade, its tip glistening with Min-joon's blood."

    king_gustav     "You, Olympia, and that damned Long Shen…"
    voice audio.minjoon_ch5_line2
    emperor_minjoon "You… will never… lay your hands… on the Divine Weapon."

    "Gustav's face contorted with unbridled fury. He gripped the hilt of his sword tighter. It glew with a radiant light."

    voice audio.minjoon_ch5_line3
    emperor_minjoon "We… *coughs* made sure that it will… never go to… someone like you…"

    "The underground chamber trembled. Cracks splintered across the stone ceiling." with hpunch
    # TODO: ground effects
    "The entire structure was collapsing."

    "Gustav growled, his blade trembling from restraint. The light flickered."

    king_gustav "Tsk… I need to take care of Long Shen first. In the meantime…"

    "He stepped back. He gave a curtsy."

    king_gustav "Enjoy Xianlun, Your Majesty."

    "Min-joon collapsed to the ground, gasping. Blood pooled beneath him, his strength fading."
    hide king_gustav
    with Dissolve(0.1)
    "Beside him, a frail, trembling hand reached out."
    "His wife."
    "Tears streamed down her face, but she said nothing—only grasped his hand, smiling. Her grip was weak as blood spilled around her."

    seo_yeon        "I love you, Min-joon."
    voice audio.minjoon_ch5_line4
    emperor_minjoon "Seo-yeon… my love… I'm sorry…"
    seo_yeon        "We'll… be together… in Xianlun…"

    "Min-joon touched the amulet around his neck with his other hand."

    voice audio.minjoon_ch5_line5
    emperor_minjoon "Chung-hee… Jong-hee… I… I hope this gets to you."
    seo_yeon        "Chung… Jong… my precious loves."
    voice audio.minjoon_ch5_line6
    emperor_minjoon "Kyeo… *coughs* The Empire of Kyeongjang is in your hands now, Chung-hee…"
    voice audio.minjoon_ch5_line7
    emperor_minjoon "I'm… sorry… to place this burden on you at such a young age but… *coughs*"
    seo_yeon        "Min-joon my love…"

    "Min-joon's breath hitched."

    voice audio.minjoon_ch5_line8
    emperor_minjoon "I'm sorry…"
    seo_yeon        "We're sorry that we have to leave you both…"
    seo_yeon        "Mom and Dad… will…"
    voice audio.minjoon_ch5_line9
    emperor_minjoon "We… won't be there anymore… Stay strong… For… For Kyeongjang…"
    seo_yeon        "We…"
    voice audio.minjoon_ch5_line10
    emperor_minjoon "We love—"

    play sound sfx_stone_break
    "The sound of rubble crashing."
    
    scene black with dissolve
    "Darkness."

    "For a moment, there was nothing—just darkness, emptiness, weightlessness."
    scene plain_white with flash
    "A blinding white light swallowed everything."
    "Then, slowly, a figure emerged."
    "I could finally see him clearly."
    "The man calling out to me. He took a sharp step forward."

    show magnus normal at right_char, dream_haze_in 
    show dorian serious at left_char, dream_haze_in 
    voice audio.magnus_ch5_line3
    magnus "Dragonkin! You're alright."

    "I blinked, disoriented."
    "Everything around us was an endless white void. There was no floor, no sky—just vast nothingness."
    "But Magnus—he was real."
    "I tried to steady my breathing."

    dorian "What… just happened? Where am I?"

    show magnus alt_shocked at right_char
    "He didn't answer. His golden eyes flickered to something behind me. His wings tensed."

    voice audio.magnus_ch5_line4
    magnus "It's coming."

    "A shiver crawled down my spine."

    dorian "What is?"   

    show magnus alt_anger at right_char
    "Magnus took another step forward, his movements sharp, urgent."

    voice audio.magnus_ch5_line5
    magnus "No time. You have to find me."
    dorian "Find you? You're right here."

    "His jaw tightened. He turned his head again, scanning the empty space around us."
    "I followed his gaze but saw nothing."

    dorian "Who are you?"
    show magnus alt_newpose at right_char
    voice audio.magnus_ch5_line6
    magnus "I…"

    "For the briefest second, he hesitated."
    "Then, his golden eyes flicked back to mine."

    show magnus alt_newpose at right_char
    voice audio.magnus_ch5_line7
    magnus "Magnus…"
    dorian "Magnus?"
    voice audio.magnus_ch5_line8
    magnus "Yes… Magnus…It's been a while since anyone called me that…"
    show magnus alt_evil_eye at right_char
    voice audio.magnus_ch5_line9
    magnus "Time… There's no time…"
    voice audio.magnus_ch5_line10
    magnus "If you have some questions, please. I'll answer them. Hurry… there isn't enough time."

    jump ch5_magnus_choices


# =============================================================================
# SECTION 28: LABEL CH5_MAGNUS_CHOICES — White Screen: Choices with Magnus
# =============================================================================

label ch5_magnus_choices:
    menu:
        "I saw the vision of the late Kyeongjang Emperor and his wife. Why did I see it?" if not ch5_magnus_q1:
            $ ch5_magnus_q1 = True

            show magnus alt_close at right_char
            "His expression darkened."
            "A flicker of sorrow crossed his face—but then, just as quickly, he looked away."
            "His wings shifted restlessly."

            voice audio.magnus_ch5_line11
            magnus "That past is written in blood. I cannot change it."
            voice audio.magnus_ch5_line12
            magnus "And neither can you, Dragonkin…"
            show dorian normal_alt_calm at left_char
            dorian "Why did I see the vision? Did they send it?"

            show magnus alt_shocked at right_char
            "He kept quiet. He does not know."
            "His hands twitched—fingers tightening, as if trying to grasp something unseen."
            show dorian serious at left_char
            voice audio.magnus_ch5_line13
            magnus "Come find me, Dorian. Before the past claims another soul."
            voice audio.magnus_ch5_line14
            magnus "Beneath Tianho."
            

            jump ch5_magnus_choices

        "Do you know what happened during the Tragedy of Tianho?" if not ch5_magnus_q2:
            $ ch5_magnus_q2 = True

            show magnus alt_shocked at right_char
            voice audio.magnus_ch5_line15
            "Magnus flinched."
            "His golden eyes widened—but then, just as quickly, he squeezed them shut, shaking his head."

            voice audio.magnus_ch5_line16
            magnus "Tianho… You need to find me…"

            show magnus alt_evil_eye at right_char
            "He inhaled sharply, as if the very words burned his throat."

            voice audio.magnus_ch5_line17
            magnus "No, no… there's no time for this."

            "He spun around, scanning the white abyss. His breath quickened."

            voice audio.magnus_ch5_line18
            magnus "They're coming… they're trying to get in…"

            show magnus alt_anger at right_char
            "His wings shuddered."
            "Then, he turned back to me, his voice a mere whisper of fire."

            voice audio.magnus_ch5_line19
            magnus "Come find me, Dorian. Beneath Tianho."
            show dorian serious at left_char

            jump ch5_magnus_choices

        "What is this place?" if not ch5_magnus_q3:
            $ ch5_magnus_q3 = True

            show magnus alt_newpose at right_char
            "His movements slowed. His breathing evened."
            "Magnus looked directly at me."

            voice audio.magnus_ch5_line20
            magnus "This… is your mind."

            "A quiet pause."

            voice audio.magnus_ch5_line21
            magnus "I speak to you from my place. I cannot leave it."
            voice audio.magnus_ch5_line22
            magnus "I… I wish I could leave and—"

            show magnus alt_close at right_char
            "His golden gaze softened—just for a second."
            "Then, suddenly— his body tensed again. The paranoia returned. His wings trembled."

            show magnus alt_shocked at right_char
            voice audio.magnus_ch5_line23
            magnus "No, no, no. There's no time—!"
            voice audio.magnus_ch5_line24
            magnus "They might get in…. No!"

            show magnus alt_anger at right_char
            "His head snapped toward the unseen horizon, eyes wild."

            voice audio.magnus_ch5_line25
            magnus "Find me, Dorian! Find me! Beneath Tianho."

            jump ch5_magnus_choices

        "I touched this amulet. What did it do to me?":
            $ ch5_magnus_q4 = True

            show magnus alt_evil_eye at right_char
            "Magnus looked around. He clenched his fists tight."

            voice audio.magnus_ch5_line26
            magnus "No… There's not enough time…"

            show magnus alt_anger at right_char
            "His voice shook."

            magnus "It's too soon."
            voice audio.magnus_ch5_line27
            magnus "Come find me, Dorian. Beneath Tianho! Please!"

            jump ch5_magnus_common

# =============================================================================
# SECTION 29: LABEL CH5_MAGNUS_COMMON — Magnus Common / Void Breaks
# =============================================================================

label ch5_magnus_common:
    # play sound sfx_void_crack loop              # PLACEHOLDER — void cracking SFX

    show magnus alt_anger at right_char
    "The world quaked around us."
    "A low, guttural rumble crawled through the white void, rising—building—like a storm about to break." with hpunch
    "Magnus lunged forward, grabbing my wrist with a grip like iron."

    voice audio.magnus_ch5_line28
    magnus "Please, Dragonkin—Dorian—!"

    "His voice trembled, a raw edge of fear in his tone. His golden eyes were wide, frantic. He squeezed my hand tighter."

    voice audio.magnus_ch5_line29
    magnus "You're nearer than you think! You must—"

    show magnus alt_shocked at right_char
    "The ground lurched. The white space around us fractured, cracks splintering through reality itself."
    "There was a distant thunderous BOOM."
    show dorian normal_alt_tense at left_char
    "The rumbling grew louder—deafening."
    "Magnus' wings flared wide, his breath ragged. He yanked me closer, his nails digging into my skin."

    show magnus alt_anger at right_char
    voice audio.magnus_ch5_line30
    magnus "HURRY!"

    "Another shuddering crash."
    "The void itself was breaking apart."

    camera at bigshake(5.0, rate=0.020, time=0.09), shattered_glass_transform
    with shattered_glass_transition

    voice audio.magnus_ch5_line31
    magnus "DO—NOT—FORGET—BENEATH TIANHO—"

    # TODO: add boom sfx
    "A final, ear-splitting ROAR."

    hide magnus
    camera
    jump ch5_nightmare


# =============================================================================
# SECTION 30: LABEL CH5_NIGHTMARE — Yaoguai King Nightmare / End of Chapter
# =============================================================================

label ch5_nightmare:

    # [COMMENT: bg_tianho_on_fire — Tianho burning, nightmare sequence]
    # scene bg_tianho_on_fire with flash          # PLACEHOLDER — Tianho on fire
    scene bg_tianho_city_on_fire with flash
    # stop music fadeout 0.5
    # play music ost_nightmare fadein 0.3         # PLACEHOLDER — nightmare horror theme

    "Then— the world shattered."
    "Darkness. Cold. Suffocating."
    "Then, there was laughter."
    "A deep, inhuman cackle slithered through the black, curling like smoke."
    "It echoed inside my skull."

    voice audio.yk_ch5_line1
    yk "Hahahaha… Dragonkin… don't interfere."

    "The darkness shifted."
    "I saw flashes—distorted, broken images—a nightmare burned into my soul."
    "Blood. Fire. Chains."
    show yk at left_char, silhouette with Dissolve(1.5)
    "A towering silhouette loomed before me."
    "The Yaoguai King."
    "His twisted horns curled like a crown, glowing embers crackling beneath his skin. His veins—molten gold—and pulsing."
    show yk at left_char, silhouette_reveal with Dissolve(0.75)
    "His jagged teeth gleamed as he grinned."

    scene cg_elara_children_death with fade
    voice audio.yk_ch5_line2
    yk "Do you remember what I took from you last time?"

    "I gasped—choking, drowning—memories crashing over me."

    voice audio.elara_ch5_line1
    elara "Dorian! No!"

    "I turned—her face."
    "Terror."
    "Tears in her eyes."

    # play sound sfx_chains                       # PLACEHOLDER — chains SFX

    dorian "Elara?! Elara! No!!"

    voice audio.elara_ch5_line2
    elara "Dorian! Please don't come! Whatever you do—!"

    scene bg_tianho_city_on_fire with flash
    show dorian angry at left_char
    show yk at right_char
    with Dissolve(0.2)
    "The chains around her wrists tightened."
    "A cry—small, fragile."

    lucas "Daddy! Daddy! Save us!"

    show screen draconic_rage 
    show dorian dragon_eyes at left_char
    
    with Dissolve(0.2)
    "A surge of fire roared in my veins."
    "I lunged forward—only for chains to slam around my limbs, dragging me down."

    dorian "I… I will! No! No!! Let them go, please! I'll do anything!"

    voice audio.yk_ch5_line3
    yk "Hahahaha!"

    "His laughter warped—a monstrous, guttural sound ripping through the void."
    "A shriek—Emily."

    emily "Ahhh!! Daddy!"

    "I thrashed."
    "Chains dug into my flesh."
    "Fire erupted—coursing through my bones—but I couldn't reach them."
    hide screen draconic_rage

    show dorian angry at left_char with Dissolve(0.1)
    dorian "NO!!! NO!!! AHHHH!!! I'LL KILL YOU!"

    "A chorus of cries—my children."

    "Emily, Sarah, Daniel, Lucas: Daddy! Daddy! Daddy!"

    "Their voices faded."
    "Ripped from my grasp."
    "I screamed."

    # scene cg_yaoguai_nightmare with fade        # PLACEHOLDER — cg_yaoguai_nightmare
    # pause 2.0

    scene black with fade                    # PLACEHOLDER — black screen
    # stop music fadeout 2.0
    # stop audio fadeout 1.5

    pause 2.0

    show screen chapter_title_screen(
        "5",
        "Cheng Industries",
        subtitle="END",
        duration=3.0
    )
    pause 3.0
    # jump demo
    jump chapter_6


# =============================================================================
# END OF CHAPTER 5
# =============================================================================

label demo:
    scene black with fade
    pause 1.0
    centered "Thank you for playing the demo\n\n Full version will include ch6-10 \n\n and major gui updates"
    pause 2.0
    $ MainMenu(confirm=False)()

