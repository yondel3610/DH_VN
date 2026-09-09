###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  SCENE: CHAPTER 9 PART 2 — Hot Spring to End of Chapter
###############################################################################

# =============================================================================
# SECTION 1: IMAGE DECLARATIONS
# =============================================================================

# =============================================================================
# SECTION 2: AUDIO DECLARATIONS
# =============================================================================

# define audio.ost_ch9_hotspring   = "audio/music/ost_ch9_hotspring.ogg"      # PLACEHOLDER
# define audio.ost_huli_jing       = "audio/music/ost_huli_jing.ogg"          # PLACEHOLDER
# define audio.ost_judgment_mjoll  = "audio/music/ost_judgment_mjoll.ogg"     # PLACEHOLDER
# define audio.ost_judgment_hinami = "audio/music/ost_judgment_hinami.ogg"    # PLACEHOLDER
# define audio.ost_judgment_kyeong = "audio/music/ost_judgment_kyeong.ogg"    # PLACEHOLDER
# define audio.ost_ch9_ceremony    = "audio/music/ost_ch9_ceremony.ogg"       # PLACEHOLDER
# define audio.ost_ch9_lanterns    = "audio/music/ost_ch9_lanterns.ogg"       # PLACEHOLDER
# define audio.ost_ch9_fireworks   = "audio/music/ost_ch9_fireworks.ogg"      # PLACEHOLDER
# define audio.sfx_judgment_chains = "audio/sfx/sfx_judgment_chains.ogg"     # PLACEHOLDER
# define audio.audio.sfx_fireworks   = "audio/sfx/audio.sfx_fireworks.ogg"       # PLACEHOLDER
# define audio.sfx_sparklers       = "audio/sfx/sfx_sparklers.ogg"           # PLACEHOLDER
# define audio.sfx_cheng_jingle    = "audio/sfx/sfx_cheng_jingle.ogg"        # PLACEHOLDER
# define audio.amb_hot_spring      = "audio/ambient/amb_hot_spring.ogg"      # PLACEHOLDER
# define audio.amb_hilltop_night   = "audio/ambient/amb_hilltop_night.ogg"   # PLACEHOLDER

# =============================================================================
# SECTION 3: GAME VARIABLES
# =============================================================================

# =============================================================================
# SECTION 4: LABEL CHAPTER_09_P2 — Hot Spring
# =============================================================================

label chapter_09_p2:
    $ save_name = "Chapter 9"
    scene yuxuan_lab_hotspring with fade          # PLACEHOLDER — hot spring
    # play music ost_ch9_hotspring fadein 2.0     # PLACEHOLDER — hot spring theme
    # play audio amb_hot_spring loop fadein 1.5   # PLACEHOLDER — hot spring ambient

    "We reached the hot springs, and the moment we stepped inside, the warmth in the air wrapped around me like a comforting embrace."
    "The soft glow of lanterns flickered against the cavern walls, their light dancing over the steaming water."
    "The air carried a faint floral scent, something soothing yet unfamiliar."
    "Roboto came to a stop and turned to me."

    show dorian neutral at left_char
    show roboto happy at right_robot
    with Dissolve(0.2)

    roboto "Master Dorian, please undress b-b-b-before entering. Master Yuxuan has ensured the waters will provide optimal relaxation."
    voice audio.dorian_ch9_line93  # transcript: "Yeah, thanks for the reminder."
    dorian "Yeah, thanks for the reminder."

    "Roboto nodded, its eyes flickering."

    roboto "I have other matters to attend to. Please enjoy your time."
    roboto "M-M-Master Yuxuan will join you momentarily."

    # TODO: roboto motors
    hide roboto 
    hide dorian 
    with Dissolve(0.1)
    "And with that, the metallic figure turned and departed, his whirring echoing as he disappeared down the stone hallway."
    "Left alone, I took a step forward, only to pause when I noticed a figure already standing by the water's edge."
    "Magnus."

    show magnus clothed_wings at right_char
    show dorian neutral at left_char
    with Dissolve(0.2)
    "He was dressed in a deep blue shirt with gold accents, a rare sight given that I saw him the entire day shirtless. But what stood out the most was the absence of his wings."
    "I furrowed my brows. Magnus without his wings?"
    "Magnus turned his head slightly, his expression calm."

    voice audio.magnus_ch9_line41  # transcript: "Dorian, going to take a"
    magnus "Dorian! Going to take a dip in the hot spring as well?"
    voice audio.magnus_ch9_line42  # transcript: "Look, I've made a discovery!"
    magnus "Look! I've made a discovery-an astonishing revelation, a truth hidden within my very being!"

    "I raised a brow."

    show magnus clothed_no_wings at right_char with Dissolve(0.2)
    voice audio.magnus_ch9_line43  # transcript: "Apparently, I can make my"
    magnus "Apparently, I can make my wings appear and disappear at will! A most convenient ability, wouldn't you say?"
    voice audio.dorian_ch9_line94  # transcript: "Convenient, same fabric I guess."
    dorian "Convenient. Saves fabric, I guess."
    voice audio.magnus_ch9_line44  # transcript: "Precisely, and most importantly, it"
    magnus "Precisely. And, most importantly, it prevents... unfortunate accidents involving doorways and the backs of unsuspecting heads."
    voice audio.magnus_ch9_line45  # transcript: "because I have on numerous"
    magnus "Because I have, on numerous occasions, unintentionally struck Svante..."

    "He paused, rubbing his chin before continuing."
    voice audio.magnus_ch9_line46
    magnus "And Yuxuan... And Chung-hee... And Niko... And Elias... And Tim... And Miss Weng... And Roboto... And Tedda..."
    voice audio.dorian_ch9_line95  # transcript: "So, everyone, you accidentally had"
    dorian "So... everyone. You accidentally hit everyone with your wings."
    voice audio.magnus_ch9_line47  # transcript: "Yes, everyone. But you! Everyone"
    magnus "Yes, everyone... But you! Everyone but you. But you must understand, my dear Dorian!"
    voice audio.magnus_ch9_line48  # transcript: "It was never intentional! A"
    magnus "It was never intentional! A cruel twist of fate, a betrayal of my own grand appendages!"

    "He placed a hand over his heart, looking entirely too pleased with himself."

    voice audio.magnus_ch9_line49  # transcript: "But alas, the heavens took"
    magnus "But alas! The heavens took pity on me. I merely wished for relief, and lo and behold-like the parting of storm clouds, the burden was lifted!"

    "He rolled his shoulders once more, as if reveling in his newfound control. I chuckled, nodding toward his attire."
    show dorian normal at left_char with Dissolve(0.1)
    voice audio.dorian_ch9_line96  # transcript: "By the way, nice outfit."
    dorian "By the way, nice outfit. You clean up well."
    voice audio.magnus_ch9_line50
    magnus "Ah, such high praise from the esteemed Dragon of Gale! I shall treasure this moment."

    show dorian normal_alt_neutral at left_char with Dissolve(0.1)
    "I asked him where did he get the outfit."

    voice audio.magnus_ch9_line51  # transcript: "Ah, tail most unexpected! Teta,"
    magnus "Ah, a tale most unexpected! Tedda, our diligent little dolly, was cleaning out Yuxuan's closet when she stumbled upon this garment-folded, untouched, a relic of time."
    voice audio.magnus_ch9_line52  # transcript: "I tried it on, and"
    magnus "I tried it on and Miss Weng and sir Niko loved it! Oh, the applause!"
    voice audio.magnus_ch9_line53  # transcript: "But it turns out that"
    magnus "But... it turned out that this was from one of Yuxuan's deceased old friend's clothes."

    "My eyes widened."

    voice audio.dorian_ch9_line97  # transcript: "shouldn't you return it if"
    dorian "Shouldn't you return it if that's the case? What would Yuxuan think?"
    voice audio.magnus_ch9_line54  # transcript: "I did show him and"
    magnus "I did show him. And he said, 'Better that you wear it than let it gather dust.'"
    voice audio.magnus_ch9_line55  # transcript: "So here I am wearing"
    magnus "So here I am, wearing a memory... but making it move again, making it breathe. Perhaps that is what clothes are meant to do-carry stories forward, instead of letting them fade into silence."

    "He took a sudden step back and struck a pose-one hand on his hip, the other extended outward as if he were about to take center stage in some grand performance."

    voice audio.magnus_ch9_line56  # transcript: "Tell me Dorian, does this"
    magnus "Tell me, Dorian-does this not suit me like the sky embraces the sun? Like the waves cradle the moon? This shade of blue-it was destined to grace my form, was it not?"
    voice audio.magnus_ch9_line57
    magnus "Or, in more common terms-blue suits me, don't you think?"

    menu:
        "Yes, it does.":
            $ A5_magnus_affection += 1             # +1 Magnus affection
            show dorian smile at left_char with Dissolve(0.1)
            "Magnus gasped, his expression shifting into one of delighted triumph. He spun again, this time with even more flourish, letting the fabric billow as he moved."

            voice audio.magnus_ch9_line58  # transcript: "Haha, I knew you were"
            magnus "Ah! I knew you were a man of refined taste! You see it, don't you, Dorian? This hue, this elegance-it was made for me!"
            
            show dorian neutral at left_char with Dissolve(0.1)
            "He placed a hand on my shoulder, his eyes shining with genuine joy beneath all the dramatics."

            voice audio.magnus_ch9_line59  # transcript: "And to have such recognition"
            magnus "And to have such recognition from you... well, my dear friend, I shall cherish this moment until the stars themselves fade from the sky!"

            "He took a deep breath, straightening his posture before giving me a wink."
            voice audio.magnus_ch9_line60
            magnus "Blue it is, then. A color worthy of a Gale-born soul such as mine."

        "No, it doesn't.":
            show dorian normal_alt_annoyed at left_char with Dissolve(0.1)
            
            "Magnus froze, his expression caught somewhere between shock and absolute betrayal. His hand clutched at his chest as if I had struck him with an arrow."
            show dorian normal_alt_neutral at left_char with Dissolve(0.1)

            voice audio.magnus_ch9_line61  # transcript: "No. No! Dorian, you warned"
            magnus "No? No?! Dorian, you wound me!"

            "He turned away dramatically, bringing a hand to his forehead as if the weight of my words was too much to bear."

            voice audio.magnus_ch9_line62  # transcript: "Then tell me, oh great,"
            magnus "Then tell me, O Great Fashion Oracle, what shade would better suit my divine essence?"

            "He peered at me over his shoulder, awaiting my response."
            "Whether I gave him an actual color or simply let him stew in his devastation, I knew one thing for certain-he wasn't going to let me forget this anytime soon."

    scene yuxuan_lab_hotspring with Dissolve(0.75)          # PLACEHOLDER — hot spring
    "Shaking my head, I reached for my belt and started undoing my clothes. Magnus followed suit, both of us stripping down to our undergarments before stepping into the water."
    "The moment I sank into the warmth, a deep sigh escaped me. The heat seeped into my muscles, melting away tension I hadn't realized I was carrying."
    "Magnus settled in beside me, his gaze drifting over the glowing fungi, the sheer ambiance of the place."

    show dorian underwear_neutral at left_char
    show magnus underwear_base at right_char
    with Dissolve(0.2)
    voice audio.magnus_ch9_line63  # transcript: "It's beautiful here. Almost. Unreal."
    magnus "It's beautiful here. Almost... unreal."
    voice audio.dorian_ch9_line98  # transcript: "Ah, this is the life."
    dorian "*sighs* This is the life..."
    voice audio.magnus_ch9_line64  # transcript: "This is perfect."
    magnus "*sighs* This is perfect..."

    "We both closed our eyes and let the gentle hum of water lapping against the stone take us into tranquility."
    voice audio.magnus_ch9_line65
    magnus "..."
    voice audio.magnus_ch9_line66  # transcript: "A spring of warmth, a"
    magnus "A spring of warmth, a fleeting dream. Where silence hums and soft lights gleam."
    voice audio.magnus_ch9_line67  # transcript: "Breath of peace, a moment's"
    magnus "A breath of peace, a moment's grace, Lost within this sacred place."

    "A few minutes passed in peaceful silence before Magnus shifted slightly, tilting his head toward me."

    show  magnus underwear_serious at right_char with Dissolve(0.1)
    voice audio.magnus_ch9_line68
    magnus "Dorian, my dear friend, can you do me a favor?"
    show dorian underwear_normal at left_char with Dissolve(0.1)
    voice audio.dorian_ch9_line99  # transcript: "the pens."
    dorian "Depends."
    show magnus underwear_base at right_char with Dissolve(0.1)
    voice audio.magnus_ch9_line69  # transcript: "Can you scrub my back?"
    magnus "Can you scrub my back?"
    show dorian underwear_neutral at left_char with Dissolve(0.1)
    voice audio.dorian_ch9_line100  # transcript: "Really?"
    dorian "Really?"
    voice audio.magnus_ch9_line70  # transcript: "Miss Wang gave me something"
    magnus "Miss Weng gave me something to help us scrub. I'll go get it."

    hide magnus with Dissolve(0.1)
    "Then, the door slid open."
    "Yuxuan entered, his usual composed expression relaxed into something softer, almost coy."
    "His eyes swept over the water, and he exhaled, the corner of his lips tugging into the smallest, knowing smirk."

    show yuxuan normal_neutral at right_char with Dissolve(0.2)

    voice audio.yuxuan_ch9_line29  # transcript: "Ah, Dorian, just the two"
    yuxuan "Ah, Dorian... Just the two of us, bathed in the glow of the springs..."
    voice audio.dorian_ch9_line101  # transcript: "Oh, no."
    dorian "Oh, Yu."

    "He took another step forward, slipping out of his robe in one fluid motion, revealing his body beneath the dim lighting."

    voice audio.yuxuan_ch9_line30  # transcript: "The heat is perfect, wouldn't"
    yuxuan "The heat is perfect, wouldn't you say? Almost as if it's drawing us in... together."

    show yuxuan underwear_neutral at right_char with Dissolve(0.1)
    "Yuxuan confidently stripped down to his undergarments, preparing to step in. His movements were slow, deliberate, like a man savoring the moment."
    "Then he saw Magnus."
    "For a moment, there was silence. Absolute. Stunned. Silence."
    "Yuxuan's eyes landed on Magnus, who-completely oblivious-smiled and raised his hands in delight."

    show magnus underwear_base at center_char with Dissolve(0.2)

    magnus "Yuxuan, my dear friend! Have you come to partake in the benefits of the hot-"
    show yuxuan underwear_angry at right_char with Dissolve(0.1)
    voice audio.yuxuan_ch9_line31  # transcript: "What?"
    yuxuan "W H A T."
    show magnus underwear_ignore at center_char with Dissolve(0.1)
    voice audio.magnus_ch9_line72  # transcript: "Springs"
    magnus "-springs?"
    voice audio.yuxuan_ch9_line32  # transcript: "Dorian, what is he doing"
    yuxuan "DORIAN?! WHAT-WHAT IS HE DOING HERE?! I THOUGHT-"

    "His hands clutched his undergarments, suddenly realizing he had undressed in front of an audience. His composure crumbled like old parchment."

    show dorian underwear_serious at left_char with Dissolve(0.1)
    voice audio.dorian_ch9_line102  # transcript: "um... baving"
    dorian "Uh... bathing?"
    show dorian underwear_neutral at left_char with Dissolve(0.1)
    show magnus underwear_base at center_char
    with Dissolve(0.1)
    voice audio.magnus_ch9_line73  # transcript: "Nice undergarments, my dear friend."
    magnus "Nice undergarments, my dear friend! Thank you for lending me your friends' undergarments as well!"
    voice audio.yuxuan_ch9_line33  # transcript: "Thanks. Wait, no, why?"
    yuxuan "T-Thanks?!-Wait-NO-WHY-"
    voice audio.magnus_ch9_line74 
    magnus "Come join us, my dear friend!"

    show yuxuan underwear_normal at right_char with Dissolve(0.1)
    "Yuxuan inhaled deeply, nostrils flaring. His fingers twitched, and for a second, I swore he was debating whether to murder Magnus on the spot or sink into the hot spring and pretend this never happened."
    show yuxuan underwear_angry at right_char with Dissolve(0.1)
    "Instead, his eye twitched violently."

    voice audio.dorian_ch9_line103  # transcript: "Just come join us, you."
    dorian "Just come join us, Yu. The water's fine."

    show yuxuan underwear_normal at right_char with Dissolve(0.1)
    "Still twitching, Yuxuan slipped into the water. The moment he did, Magnus spread his arms wide and pulled him into a suffocating hug."

    show yuxuan underwear_angry at right_char with Dissolve(0.1)
    voice audio.yuxuan_ch9_line34  # transcript: "Magnus, hey, I'm getting strangled."
    yuxuan "M-Magnus! H-hey! I'm getting strangled!"
    voice audio.magnus_ch9_line75  # transcript: "My dear friend, the water"
    magnus "My dear friend, the water is amazing!"
    voice audio.yuxuan_ch9_line35  # transcript: "Why are you even here?"
    yuxuan "WHY ARE YOU EVEN HERE?!"
    voice audio.magnus_ch9_line76  # transcript: "What do you mean? You"
    magnus "What do you mean? You told me to join you."
    voice audio.yuxuan_ch9_line36  # transcript: "What? I never..."
    yuxuan "...What? I never-"

    "And then... the door slid open."
    "Niko. Svante. Chung-hee."
    "All three of them. In their undergarments."
    "They weren't even paying attention to us at first. They were deep in mid-conversation, voices echoing slightly against the cavern walls."

    hide magnus
    hide yuxuan
    hide dorian
    show niko underwear_base at left_char
    show svante underwear_base at center_char
    show chunghee underwear_neutral at right_char
    with Dissolve(0.2)

    voice audio.niko_ch9_line41  # transcript: "Fasting is a form of"
    niko "Fasting is a form of discipline, Svante. A way to show devotion to Enoch. A test of the soul's resolve."
    voice audio.svante_ch9_line49  # transcript: "But for that long, I"
    svante    "But for that long? I don't think you can do it. How are you not hungry? I'd pass out."
    voice audio.niko_ch9_line42  # transcript: "You rely on Enoch's words"
    niko "You rely on Enoch's words. And pray. One does not live by earthly sustenance, but by every word that-"
    voice audio.niko_ch9_line43  # transcript: "Unless your faith isn't good"
    niko "Unless... Your faith isn't good enough."
    voice audio.svante_ch9_line50  # transcript: "I... I..."
    svante    "I... I-"
    voice audio.chung_ch9_line22  # transcript: "He's being dramatic, Svante. You"
    chung_hee "He's being dramatic, Svante. You don't have to do it if you don't want to. Niko, stop it."

    "And then-finally-they looked up."
    "Magnus lifted his arms wide, water sloshing around him. His wings were still hidden, but it was as if he radiated an invisible aura of divinity."

    hide svante
    hide chunghee
    show magnus underwear_base at right_char
    with Dissolve(0.2)

    voice audio.magnus_ch9_line77  # transcript: "Dear friends, here we are!"
    magnus "Dear friends!! Here we are!!"

    "He waved, as if this was the most natural gathering in the world. Chung-hee blinked, deadpan."

    hide niko
    show chunghee underwear_happy at left_char
    show svante underwear_happy at center_char
    with Dissolve(0.2)
    voice audio.chung_ch9_line23  # transcript: "Oh look, it's Magnus. Dorian's"
    chung_hee "Oh look. It's Magnus. Dorian's here too, along with Yuxuan."
    voice audio.svante_ch9_line51  # transcript: "Magnus, you're here!"
    svante    "MAGNUS!! YOU'RE HERE!!"
    

    "Yuxuan, still submerged in the water, was visibly vibrating with rage. His fingers twitched as if they were itching to summon some kind of spell-maybe to drown Magnus, maybe to drown himself."
    hide chunghee
    hide svante
    hide magnus
    show yuxuan underwear_angry at center_char
    with Dissolve(0.2)
    voice audio.yuxuan_ch9_line37  # transcript: "Why is everyone here?"
    yuxuan "WHY. IS. EVERYONE. HERE."
    
    hide yuxuan
    show niko underwear_base at left_char
    show svante underwear_base at center_char
    show chunghee underwear_neutral at right_char
    with Dissolve(0.2)
    voice audio.chung_ch9_line25  # transcript: "what's gotten into him."
    chung_hee "What's gotten into him?"
    voice audio.svante_ch9_line52  # transcript: "Didn't you invite us, you"
    svante    "Didn't you invite us, Yuxuan?"
    voice audio.niko_ch9_line44  # transcript: "Your invitation made me think"
    niko "Your invitation made me think it was going to be just the two of us here."
    voice audio.chung_ch9_line26
    chung_hee "Same. I thought you had some confidential information about the Divine Weapon, so I came here expecting something important. I was surprised to see these two, though."
    voice audio.svante_ch9_line53  # transcript: "Yeah, you even call this"
    svante    "Yeah. You even called us your \"special guest\"."

    hide svante
    show yuxuan underwear_angry at center_char
    with Dissolve(0.1)
    "Yuxuan's eye twitched so violently that for a second, I thought he might actually explode. He inhaled sharply, barely keeping himself from launching into a full-blown tantrum."
    "Then he snapped his head toward the entrance, his voice echoing through the chamber."

    voice audio.yuxuan_ch9_line38  # transcript: "Special? Rebato? Rebato!"
    yuxuan "Special?! ROBOTO! ROBOTO!"
    hide yuxuan
    hide chunghee
    hide niko
    with Dissolve(0.1)
    "A few moments passed."
    "The sound of mechanical whirring filled the air, followed by the faint clanking of metal against stone. And then-"

    # play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    show yuxuan underwear_angry at left_char
    show roboto happy at right_robot 
    with Dissolve(0.2)

    roboto "Y-y-y-you called, Master Yuxuan? Roboto is h-h-h-here. At your service."
    voice audio.yuxuan_ch9_line39  # transcript: "I told you to bring"
    yuxuan "I told you to bring our special guest here! I also told Tedda to take care of Elias so our special guest could come here! How in the name of the Prosperity Dragon did this-"
    show roboto malfunction at right_robot with Dissolve(0.1)
    "Roboto's sensors flickered again."

    roboto "M-M-Master Yuxuan, you said to bring the... special guest."
    show roboto happy at right_robot with Dissolve(0.1)

    "Roboto's mechanical eyes whirred as it scanned the room."

    roboto "The term 'special guest' was n-n-not explicitly defined. Given that Master Dorian, Sir Magnus, Sir Chung-hee, Sir Niko, and Sir Svante all hold unique statuses, it was l-l-l-logical to conclude that all of them qualified as... special guests."

    show yuxuan underwear_sad at left_char with Dissolve(0.1)

    "Yuxuan let out a sound somewhere between a strangled groan and a defeated whimper."
    show yuxuan underwear_angry at left_char with Dissolve(0.1)

    "His entire body trembled. His eye twitched again. He opened his mouth-closed it-opened it again-"
    show yuxuan underwear_sad at left_char with Dissolve(0.1)

    "Then, with a slow, heavy inhale, he lowered himself deeper into the water until only his eyes were visible, like a man giving up on life itself."

    hide roboto
    show dorian underwear_normal at left_char
    show yuxuan underwear_sad at right_char 
    with Dissolve(0.1)

    voice audio.dorian_ch9_line104  # transcript: "The water is nice, you."
    dorian "The water is nice, Yu. Might as well enjoy it."
    show svante underwear_happy at center_char with Dissolve(0.2)
    voice audio.svante_ch9_line54  # transcript: "Dorian, let's explore that side"
    svante "Dorian! Let's explore that side with Magnus!"
    voice audio.dorian_ch9_line105  # transcript: "Let's go."
    dorian "Sounds nice. Let's go."

    hide svante
    show magnus underwear_base at center_char with Dissolve(0.2)
    voice audio.magnus_ch9_line78  # transcript: "Then let us embark my"
    magnus "Then let us embark, my friends! Onward to the unknown! Chung, can you hold my hand as we walk?"

    hide yuxuan
    show chunghee underwear_base at right_char with Dissolve(0.2)
    voice audio.chung_ch9_line27  # transcript: "I should have stayed in"
    chung_hee "I should've stayed in bed."

    hide magnus
    hide chunghee
    show niko underwear_smile at center_char 
    show yuxuan underwear_angry at right_char 
    with Dissolve(0.2)
    voice audio.niko_ch9_line45  # transcript: "Just Dorian, huh? Figures."
    niko "Just Dorian, huh? Figures."
    voice audio.yuxuan_ch9_line40  # transcript: "I will end you, Nico."
    yuxuan    "I will END you, Niko."
    voice audio.niko_ch9_line46  # transcript: "That explains all the rose"
    niko "That explains all of the rose petals in-"
    voice audio.yuxuan_ch9_line41  # transcript: "Shhh, just shhh."
    yuxuan    "Shhh!! Just shhh!!"

    show niko underwear_anger at center_char with Dissolve(0.1)
    voice audio.niko_ch9_line47  # transcript: "Hey, how dare you splash"
    niko "Hey! How dare you splash water on me!"
    scene yuxuan_lab_hotspring with Dissolve(0.75)          # PLACEHOLDER — hot spring
    "Steam curled lazily through the air as we settled deeper into the hot springs."
    "The warmth seeped into my muscles, unraveling tension I hadn't even realized I carried. For a moment-just a moment-it was peaceful."

    jump ch9_huli_jing


# =============================================================================
# SECTION 5: LABEL CH9_HULI_JING — Huli Jing Appears
# =============================================================================

label ch9_huli_jing:

    # play music ost_huli_jing fadein 1.0         # PLACEHOLDER — Huli Jing ethereal theme
    voice audio.hulijing_ch9_line1
    huli_jing "Hihihihi~"

    show niko underwear_serious at right_char
    show chunghee underwear_base at left_char
    show yuxuan underwear_lying at center_char
    with Dissolve(0.2)

    voice audio.niko_ch9_line48  # transcript: "Wait. Did you hear that?"
    niko "Wait... Did you hear that?"
    voice audio.chung_ch9_line28  # transcript: "No, for the hundredth time,"
    chung_hee "No. For the hundredth time, no."
    voice audio.magnus_ch9_line79  # transcript: "I heard it. I think"
    magnus "I heard it. I think it's... a laugh."

    voice audio.hulijing_ch9_line2
    huli_jing "Hihihihi~"
    voice audio.yuxuan_ch9_line42  # transcript: "E! What was that?"
    yuxuan    "Eek! What was that?"

    "A whisper of laughter, high and melodic, like wind chimes swaying in a summer breeze."
    "The air itself thickened, humming with unseen energy. A delicate floral scent, subtly sweet, curled into the steam rising from the springs."
    
    hide niko
    hide chunghee
    hide yuxuan
    show huli_jing at center_char 
    with Dissolve(0.2)
    voice audio.hulijing_ch9_line3  # transcript: "Ah, with a luxurious sight,"
    huli_jing "Ahh, what a luxurious sight! A gathering of warriors, scholars, and lost souls-all marinating like dumplings in a pot."

    "A faint tinkling of bells accompanied soft footsteps, the sound of water rippling as a figure gracefully stepped into view."
    "Perched atop a rock at the edge of the spring, half-shrouded by mist, was a fox."
    "Nine, impossibly long tails curled elegantly around her, their tips flicking idly, as if brushing away unseen dust motes of magic."
    "Her golden eyes-slit-pupiled, like molten amber-watched us with quiet amusement."
    voice audio.hulijing_ch9_line4  # transcript: "No, don't look so startled"
    huli_jing "Oh, don't look so startled, my handsome bathers... You wouldn't deny a lonely fox the pleasure of a little conversation, would you?"

    "The being's laughter echoed through the mist, melodic yet uncanny, like a song sung in reverse. The steam curled tighter, shifting unnaturally, as if the very air around us was holding its breath."
    "A faint pressure settled in my chest-an instinctual warning, ancient and primal. Then I saw it."
    "Not just the nine flowing tails..."

    show dorian underwear_neutral at left_char
    show svante underwear_neutral at right_char
    with Dissolve(0.1)
    voice audio.svante_ch9_line55  # transcript: "She's a fox spirit. A"
    svante "She's a fox spirit. A huli jing."
    voice audio.svante_ch9_line56  # transcript: "My mom told me in"
    svante "My mom told me and Kristin stories. Said they were born from moonlight and starlight. They've lived for centuries... maybe since the first breath of the world when the Weaver made the Tetrad."
    voice audio.dorian_ch9_line106  # transcript: "and what do they want?"
    dorian "And what do they want?"
    show svante underwear_base at right_char with Dissolve(0.1)
    voice audio.svante_ch9_line57  # transcript: "That's the thing. No one"
    svante "That's the thing. No one ever knows."

    "His voice lowered, nearly reverent."

    voice audio.svante_ch9_line58  # transcript: "Some are kind, protectors, but"
    svante "Some are kind. Protectors. But most of them? They bring ruin with a smile. Trick kings into giving up empires. They love riddles, deals... They whisper and let you think you've won-until the price seeps in through the cracks you forgot were there."
    voice audio.svante_ch9_line59  # transcript: "They've whispered to emperors, to"
    svante "They've whispered to emperors... to gods. Inspired love, betrayal, even genocide. And sometimes, they simply watched. Waiting."

    "The Huli Jing tilted her head, her smile curling wider, inhumanly so."

    voice audio.hulijing_ch9_line5  # transcript: "Mmm, clever boy. As shame"
    huli_jing "Mmm... clever boy. A shame your mother never told you the most important part."
    voice audio.hulijing_ch9_line6  # transcript: "We never knock twice."
    huli_jing "We never knock twice."
    hide svante
    show niko underwear_base at right_char with Dissolve(0.2)
    voice audio.niko_ch9_line49  # transcript: "You swan, you didn't say"
    niko "Yuxuan, you didn't say there'd be an ancient spirit here!"

    hide niko
    show yuxuan underwear_lying at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch9_line43  # transcript: "But I... I always bathe"
    yuxuan    "But I... I always bathe here! Miss Weng too! Tim as well. We never-!"
    voice audio.hulijing_ch9_line7  # transcript: "Of course not my entrepreneur,"
    huli_jing "Of course not, my entrepreneurial little beetle. We don't come for the scent of soap, sweat, and money."

    "She tilted her head, and her nine tails unfurled behind her like a blooming chrysanthemum, each one stirring the steam with ethereal grace."

    voice audio.hulijing_ch9_line8  # transcript: "I came because I snobbed"
    huli_jing "I came because I smelled something rare..."
    voice audio.hulijing_ch9_line9  # transcript: "Among your gathering, I sent"
    huli_jing "Among your gathering... I scent the blood of an emperor. The son of a king. One who has been chosen by the death god. One... touched by a deity's longing. And one..."

    show dorian underwear_serious at left_char with Dissolve(0.1)
    "She turned her gaze to me. And the air stilled."

    voice audio.hulijing_ch9_line10  # transcript: "Praise the prosperity dragon indeed."
    huli_jing "Praise the Prosperity Dragon indeed..."

    hide yuxuan 
    show chunghee underwear_neutral at right_char with Dissolve(0.2)
    voice audio.chung_ch9_line29  # transcript: "What do you want, Spirit?"
    chung_hee "What do you want, spirit? Speak plainly."
    voice audio.hulijing_ch9_line11  # transcript: "This spring, the mist that"
    huli_jing "This spring... the mist that dances on its surface... the dreams that bloom when one sinks into its warmth-"
    voice audio.hulijing_ch9_line12
    huli_jing "These were once mine... before I was betrayed. Before I was slain mercilessly by the Death God Enoch himself."

    "Niko, lounging with a towel over his head, didn't even lift his gaze."
    hide chunghee
    show niko underwear_serious at right_char with Dissolve(0.2)
    voice audio.niko_ch9_line50  # transcript: "You creatures probably deserved it,"
    niko "You creatures probably deserved it, given your kind's reputation."
    voice audio.hulijing_ch9_line13  # transcript: "Understandable? For a lapdog to"
    huli_jing "Understandable... for a lapdog to bark what it cannot comprehend. But I'll pretend I didn't hear that-your heart beats too loud with something else."

    "One tail coiled like a ribbon around her waist, the others slowly dancing in the air like smoke given form."

    voice audio.hulijing_ch9_line14  # transcript: "Now, centuries later, you've stumbled"
    huli_jing "Now, centuries later, you've stumbled in my spring. And I can smell it... all of you. You're tangled up in fate, in longing."

    "She looked at me again, that same unreadable expression."

    voice audio.hulijing_ch9_line15  # transcript: "I am lonely and I"
    huli_jing "I am lonely. And I wish to play."
    voice audio.hulijing_ch9_line16  # transcript: "If you agree to my"
    huli_jing "If you agree to my game, I promise: I will never trouble you again. In return, I will answer one- and only one-question. From the spirit world. From the place where truths hide and mortals dare not look."

    "The mist pulsed once, as if alive."

    voice audio.hulijing_ch9_line17  # transcript: "No tricks, no riddles, just"
    huli_jing "No tricks. No riddles. Just truth."

    "My heart quickened. One question."

    prosperity_dragon "The Huli Jing knows more than she speaks. The knowledge she carries lies coiled in riddles older than your bloodline."
    prosperity_dragon "She could speak answers that even the Tetrad have forgotten."

    voice audio.hulijing_ch9_line18
    huli_jing "But if you refuse..."
    hide niko
    show chunghee underwear_angry at right_char with Dissolve(0.2)
    voice audio.chung_ch9_line30  # transcript: "Then what? You'll kill us?"
    chung_hee "Then what? You'll kill us?"
    hide chunghee
    show yuxuan underwear_sad at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch9_line44  # transcript: "Ah, Prosperity Dragon saved me."
    yuxuan    "AH! Prosperity Dragon save me!"
    hide yuxuan
    show niko underwear_serious at right_char with Dissolve(0.2)
    voice audio.niko_ch9_line51  # transcript: "You're more than welcome to"
    niko "You're more than welcome to try."
    voice audio.hulijing_ch9_line19  # transcript: "No, no, I don't spill"
    huli_jing "No, no. I don't spill blood. My fur is too good for that."
    voice audio.hulijing_ch9_line20  # transcript: "I'll curse this spring for"
    huli_jing "I'll curse this spring for a thousand years. Every bather after you will think they've slipped into paradise, only to discover they're soaking in..."
    voice audio.hulijing_ch9_line21  # transcript: "fermented foot fungus stew."
    huli_jing "Fermented foot fungus stew."

    hide niko
    show chunghee underwear_neutral at right_char with Dissolve(0.2)
    voice audio.chung_ch9_line31  # transcript: "Pardon me."
    chung_hee "Pardon me?"

    hide chunghee
    show magnus underwear_sad at right_char with Dissolve(0.2)
    voice audio.magnus_ch9_line80  # transcript: "Ferment in footfongistu!"
    magnus "F-Fermented foot fungus stew?"
    hide magnus
    show yuxuan underwear_angry at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch9_line45  # transcript: "Eww! I bathed here all"
    yuxuan    "EWWW! I bathe here all the time!!"

    hide yuxuan
    show svante underwear_nervous at right_char with Dissolve(0.2)
    svante    "I... I think I'm gonna be sick... blarrrghhh!"
    voice audio.hulijing_ch9_line22  # transcript: "Your guests will be smelling"
    huli_jing "Hahaha! Your guests will be smelling like the Tetrad's feet by the time they finish bathing!"

    hide svante 
    show niko underwear_ignore at right_char with Dissolve(0.2)
    voice audio.niko_ch9_line52
    niko "*sighs*"
    voice audio.hulijing_ch9_line23  # transcript: "So, my beautiful dumplings, shall"
    huli_jing "So, my beautiful dumplings... Shall we play?"

    "I looked around the spring, its mist now feeling heavier somehow-less soothing, more watchful. My eyes met Svante's. He was looking around too, brow furrowed deep in thought."
    
    hide niko
    show svante underwear_neutral at right_char with Dissolve(0.2)
    voice audio.svante_ch9_line60  # transcript: "She said she can answer"
    svante "She said she can answer one question..."
    hide svante
    show niko underwear_ignore at right_char with Dissolve(0.2)
    voice audio.niko_ch9_line53  # transcript: "Don't be stupid, Sponte."
    niko "Don't be stupid, Svante."

    hide niko
    show svante underwear_neutral at right_char with Dissolve(0.2)
    voice audio.svante_ch9_line61  # transcript: "I'm not being stupid, Nico."
    svante "I'm not being stupid, Niko. I was just thinking that maybe we need it!"

    hide svante 
    show niko underwear_serious at right_char with Dissolve(0.2)
    voice audio.niko_ch9_line54  # transcript: "She said no tricks, but"
    niko "She said no tricks-but that's the trick. You said it yourself: spirits like her oftentimes never play fair. You'll think you're getting a straight answer and wind up cursed, or worse."

    hide niko
    show chunghee underwear_base at right_char with Dissolve(0.2)
    voice audio.chung_ch9_line32  # transcript: "Nico's right, Svante."
    chung_hee "Niko's right, Svante."
    voice audio.chung_ch9_line33  # transcript: "Every version of this tale"
    chung_hee "Every version of this tale ends the same way. We had stories like that in Kyeongjang too. Not of the Huli Jing-but spirits with games, riddles and promises."
    voice audio.chung_ch9_line34  # transcript: "An innocent hero, a ruined"
    chung_hee "An innocent hero. A ruined life. Don't be a storybook idiot, Svante."

    hide chunghee
    show svante underwear_neutral at right_char with Dissolve(0.2)
    voice audio.svante_ch9_line62  # transcript: "I hate to say it,"
    svante "I... I hate to say it, but you may be right."

    hide svante
    show magnus underwear_base at right_char with Dissolve(0.2)
    voice audio.magnus_ch9_line81  # transcript: "But what if she's telling"
    magnus "But... what if she's telling the truth? Not all spirits are malevolent."
    show magnus underwear_serious at right_char with Dissolve(0.1)
    voice audio.magnus_ch9_line83  # transcript: "One question, one truth. Think"
    magnus "One question. One truth. Think about what you could learn. Something no divine, no scholar, no channeler could tell us."
    voice audio.magnus_ch9_line82  # transcript: "Isn't that worth a little"
    magnus "Isn't that worth a little risk?"

    hide magnus
    show yuxuan underwear_normal at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch9_line46  # transcript: "I want to do it."
    yuxuan "I want to do it!! We have to do it!!"

    hide yuxuan 
    show chunghee underwear_base at right_char with Dissolve(0.2)
    voice audio.chung_ch9_line35  # transcript: "But why?"
    chung_hee "But... why?"

    hide chunghee
    show yuxuan underwear_sad at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch9_line47  # transcript: "I always bathe here. So"
    yuxuan "I-I always bathe here! So does Miss Weng! And Tim! We come here every day! If she curses this spring, it'll smell like foot fungus for a thousand years!"
    show yuxuan underwear_angry at right_char with Dissolve(0.1)
    voice audio.yuxuan_ch9_line48  # transcript: "I can already imagine the"
    yuxuan "I can already imagine the smell! I have to do something!"
    voice audio.yuxuan_ch9_line49
    yuxuan "I AM CHENG YUXUAN, an inventor of great renown. And I will NOT BE SMELLING LIKE SOMEONE'S FOOT!"
    show dorian underwear_neutral at left_char with Dissolve(0.1)

    "He nearly slipped on the rocks trying to make his point."

    show yuxuan underwear_sad at right_char with Dissolve(0.1)
    voice audio.yuxuan_ch9_line50
    yuxuan "AHHH!!"

    voice audio.dorian_ch9_line107  # transcript: "You careful!"
    dorian "Yu! Careful!"

    show yuxuan underwear_angry at right_char with Dissolve(0.1)
    voice audio.yuxuan_ch9_line51  # transcript: "Do you know how expensive"
    yuxuan "Do you know how expensive this place is?! I spent a lot of coin to refurbish this place!"

    hide yuxuan
    show niko underwear_smile at right_char with Dissolve(0.1)
    voice audio.niko_ch9_line55  # transcript: "How much would that be?"
    niko "How much would that be?"

    hide niko
    show yuxuan underwear_angry at right_char with Dissolve(0.1)
    voice audio.yuxuan_ch9_line52  # transcript: "A LOT!"
    yuxuan "A LOT!!"
    show yuxuan underwear_normal at right_char with Dissolve(0.1)

    voice audio.hulijing_ch9_line24
    huli_jing "Ahhh, the little beetle speaks sense~"

    "She cooed, lounging now on her side, chin propped up by one delicate hand."

    voice audio.hulijing_ch9_line25  # transcript: "So, what will it be,"
    huli_jing "So? What will it be, dumpling?"

    "The mist curled around my fingertips. I didn't know what pushed me to speak, but the words came anyway."

    show yuxuan underwear_angry at right_char with Dissolve(0.1)
    voice audio.yuxuan_ch9_line53  # transcript: "Do it! Do it!"
    yuxuan "Do it! Do it!"
    show dorian underwear_serious at left_char with Dissolve(0.1)
    voice audio.dorian_ch9_line108  # transcript: "I'll do it. I agree"
    dorian "I'll do it. I agree to the game."  

    hide yuxuan
    show chunghee underwear_base at right_char with Dissolve(0.2)
    voice audio.chung_ch9_line36  # transcript: "Fine, I trust you, Dorian."
    chung_hee "Fine. I trust you, Dorian."

    jump ch9_judgment_mjoll


# =============================================================================
# SECTION 6: LABEL CH9_JUDGMENT_MJOLL — Illusion: Mjoll / Fynn Hjorth Trial
# =============================================================================

label ch9_judgment_mjoll:

    # [COMMENT: bg_mjoll_town_square — snow, stone buildings, shackled man in center]
    scene bg_mjoll_icelands with flash       # PLACEHOLDER — Mjoll town square illusion
    show snow_blizzard_1

    stop music fadeout 0.5
    # TODO: add audio
    # play music ost_judgment_mjoll fadein 0.5    # PLACEHOLDER — Mjoll judgment theme
    # play sound sfx_judgment_chains              # PLACEHOLDER — chains SFX

    "The mist curled tighter the moment the words left my lips. It coiled like a serpent around my limbs-soft, almost warm-and then turned cold."
    "The springs vanished."
    "In their place, snow."
    "The world around us shimmered, then cracked like glass. Wind howled past us, biting at our skin, lifting flurries of snow into the air like ash. But I still felt the heat from the hot springs."

    show magnus underwear_angry at right_char 
    show dorian underwear_serious at left_char
    with Dissolve(0.1)
    voice audio.magnus_ch9_line85  # transcript: "Oh, oh no! We're stealing"
    magnus "O-Oh. Oh no. We're still in our undergarments!"

    hide magnus
    show yuxuan underwear_sad at right_char with Dissolve(0.1)
    voice audio.yuxuan_ch9_line54  # transcript: "Ugh! I can't be seen"
    yuxuan "AH! I can't be seen wondering around in my undergarments! Think of the bad publicity!"

    hide yuxuan
    show svante underwear_nervous at right_char with Dissolve(0.1)
    voice audio.svante_ch9_line63  # transcript: "What? This is B-O-L! This"
    svante "W-What?! This is Mjoll! This is my hometown!! I can't be here! Not like this!"

    "He wrapped his arms around his chest, cheeks blazing red."

    hide svante
    show niko underwear_serious at right_char with Dissolve(0.1)
    voice audio.niko_ch9_line56  # transcript: "You're not used to your"
    niko "You're not used to your brothers seeing you in your undergarments?"

    hide niko
    show chunghee underwear_base at right_char with Dissolve(0.1)
    voice audio.chung_ch9_line37  # transcript: "It's not real. Look at"
    chung_hee "It's not real. Look at the snow-doesn't melt when it hits your skin."

    "He held out a hand. True enough, the flakes dissolved before they touched him."

    voice audio.dorian_ch9_line109  # transcript: "We can also feel the"
    dorian "We can also feel the heat of the hot spring's waters."
    voice audio.chung_ch9_line38  # transcript: "It's just an illusion, a"
    chung_hee "It's just an illusion. A trick. The spirit's game."

    hide chunghee
    hide dorian
    with Dissolve(0.1)

    "The snow parted. In the middle of the town stood a man, shackled and bare-kneed in the snow. Blood streaked the front of his torn tunic."
    "Before him, crumpled in the red-stained snow, were two villagers-a woman and a child. Motionless."
    show huli_jing at center_char with Dissolve(0.2)
    voice audio.hulijing_ch9_line26  # transcript: "This man finned Earth as"
    huli_jing "This man, Fynn Hjorth, is a follower of the death god."
    voice audio.hulijing_ch9_line27  # transcript: "He killed his neighbor and"
    huli_jing "He killed his neighbor and her daughter in the dead of night. Stabbed them both. Took their coin. I'll leave you to it."

    "Fynn raised his head. His face was pale, eyes sunken and wild."

    voice audio.fynn_ch9_line1  # transcript: "He knocked told me to"
    fynn "Enoch told me to do it! He told me to cleanse them! To protect the town!"

    show huli_jing at center_char with Dissolve(0.2)

    "She sat atop a stone throne of ice that hadn't been there before, tails draped like velvet across her lap."

    voice audio.hulijing_ch9_line28  # transcript: "Now, as part of our"
    huli_jing "Now, as part of our little game... you will judge him."
    voice audio.hulijing_ch9_line29  # transcript: "Death, exile, or forgiveness."
    huli_jing "Death, exile, or forgiveness."

    jump choice_judgement_mjoll

label choice_judgement_mjoll:
    show dorian underwear_serious at left_char 
    show chunghee underwear_base at right_char 
    with Dissolve(0.2)
    "I stood frozen. Not from the cold, but from the sheer weight of it all."

    voice audio.chung_ch9_line39  # transcript: "We were the judge of"
    chung_hee "We were to judge a man's life. Such a burden to carry."

    "The wind grew louder. Or perhaps it was the breath of the spirits gathering to hear our verdict."

    voice audio.hulijing_ch9_line30  # transcript: "spirits be our witness"
    huli_jing "Spirits, be our witness."
    voice audio.hulijing_ch9_line31  # transcript: "Shoes wisely, my dumplings. There"
    huli_jing "Choose wisely, my dumplings. There is no appeal in this court. Your decision is FINAL."

    "I looked at the man in the eyes. A man broken, or a man twisted? A misguided zealot? A monster wearing a mask of devotion?"
    "But now... the judgment was mine to cast."


    menu:

        "Pass the judgment of Death.":
            
            "I closed my eyes. The cold air kissed my skin, but I felt nothing-only the weight of my decision. I raised my hand, flame flickering to life in my palm. Not a warm flame. A crimson one."

            voice audio.dorian_ch9_line110  # transcript: "He took two innocent lives."
            dorian "He took two innocent lives. That cannot be forgiven. We sentence death."

            # TODO: ice shard sfx
            "A tremor rippled through the ground. The snow around Fynn shattered into sharp shards as the spirits surged up from beneath."
            "He screamed-but it wasn't a scream of fear. It was something worse. A scream of belief."

            voice audio.fynn_ch9_line2  # transcript: "I was chosen! I was"
            fynn   "I was chosen! I was doing Lord Enoch's work! You'll see!"

            hide chunghee
            show svante underwear_angry at right_char with Dissolve(0.2)
            voice audio.svante_ch9_line64  # transcript: "You murdered a mother and"
            svante "You murdered a mother cradling her child. You didn't cleanse anything. You just wanted to kill!"

            hide svante
            show yuxuan underwear_angry at right_char with Dissolve(0.2)
            voice audio.yuxuan_ch9_line55  # transcript: "You deserve it, degenerate."
            yuxuan "You deserve it! Degenerate!"

            "The mist devoured him. No blood. No remains. Only silence."
            voice audio.hulijing_ch9_line32
            huli_jing "Hmm... decisive."

            "Her voice was unreadable-neither impressed nor disappointed."
            "She tapped her heart. The snow continued to fall. I felt heavier."

        "Pass the judgment of Exile.":
            $ huli_jing_approval += 1           # +1 Huli Jing approval

            "I hesitated, staring into Fynn's frantic eyes. There was no remorse there-only delusion. But killing him would make me no better."
            "I extended my hand. A cold blue light bloomed in my palm."

            dorian "You'll not die here, Fynn. But you'll never walk these lands again."

            "The snow beneath him shifted violently, like it was trying to reject him."

            voice audio.fynn_ch9_line3  # transcript: "No, no, this is my"
            fynn "No... no, this is my home! I did what I had to! For the town! For Lord Enoch!"

            # TODO: add sfx
            "The wind howled louder. His chains dissolved into frost, and something unseen dragged him backward into the mist-screaming, kicking, shouting for Enoch to save him."

            voice audio.fynn_ch9_line4  # transcript: "Lord Enoch! Lord Enoch your"
            fynn "Lord Enoch! Lord Enoch your servant begs you! No!"

            chung_hee "Good. Take him far away from here. Should he ever return, death would await him."
            voice audio.hulijing_ch9_line33  # transcript: "Hmm, merciful, but not weak."
            huli_jing "Hmm... merciful, but not weak."

            "Her voice was unreadable-neither impressed nor disappointed."

        "Pass the judgment of Forgiveness.":

            "The silence was unbearable."
            "Everyone waited. The spirits. The snow. The fox. I took a breath. My heart was hammering."
            show dorian underwear_sad at left_char with Dissolve(0.1)

            dorian "He's broken. Not evil. If he can live with what he's done... let him. We grant forgiveness."
            voice audio.fynn_ch9_line5  # transcript: "You... You're not killing me!"
            fynn   "You... you're not killing me?"

            hide chunghee
            show niko underwear_serious at right_char with Dissolve(0.2)
            voice audio.niko_ch9_line57  # transcript: "Yes, continue walking in Enoch's"
            niko "Yes. Continue walking in Enoch's path, brother."

            hide niko
            show yuxuan underwear_angry at right_char with Dissolve(0.2)
            yuxuan "W-What?! Why are we letting him go? What is wrong with you, Dorian?!"

            hide yuxuan
            show chunghee underwear_sad at right_char with Dissolve(0.2)
            chung_hee "Kindness or naiveness? I hope we aren't straying towards the latter."

            "Her voice was unreadable-neither impressed nor disappointed."

        "Investigate first and ask the others for their opinion.":

            voice audio.hulijing_ch9_line35  # transcript: "Not ready to decide, dumpling."
            huli_jing "Not ready to decide, dumpling?"

            "I took a breath and stepped forward. The wind bit at my skin, the illusion of snow somehow feeling far too real. I knelt in front of the man they called Fynn Hjorth. His eyes darted wildly."

            dorian "Tell me what happened. In your own words."

            "He looked up. Eyes-clouded, red-rimmed-twitched wildly in their sockets."

            voice audio.fynn_ch9_line6  # transcript: "They were touched by rot."
            fynn "They were touched by rot. The mother... I saw her. I heard her whispering at night, speaking to the dark, speaking to Saelara. She was offering prayers when she thought no one could hear."

            "The name landed like a stone in the snow. I felt more than heard a subtle shift in the mist."

            voice audio.fynn_ch9_line7  # transcript: "And the child. The child"
            fynn "And the child. The child had silver eyes... the kind only a Tetrad follower would birth."
            voice audio.fynn_ch9_line8
            fynn "Enoch sent me the vision. Clear as fire. Told me to cleanse them. To save this town."

            "He grabbed my wrist."

            voice audio.fynn_ch9_line9  # transcript: "I did it for him."
            fynn "I did it for Him. For Lord Enoch. His voice roared like a tempest! Oh, glorious, radiant death!"
            voice audio.fynn_ch9_line10  # transcript: "I felt his handguide bite"
            fynn "I felt His hand guide mine when I struck with the axe. I watched the life leave their heretic eyes, and I laughed, I laughed for Enoch!"

            "He broke into hysterical giggling. I pulled my hand away. I stood, heart a stone in my chest."

            show chunghee underwear_angry at right_char with Dissolve(0.1)
            chung_hee "Madness. I've heard stories like this in Kyeongjang. Men claiming divine voices told them to murder their own kin. It's never justice. It's bloodlust wrapped in prophecy."

            hide chunghee
            show magnus underwear_base at right_char with Dissolve(0.2)
            voice audio.magnus_ch9_line86  # transcript: "But is it really forbidden?"
            magnus "But... is it really forbidden? Tetrad worship?"

            hide magnus
            show svante underwear_neutral at right_char with Dissolve(0.2)
            svante "In Mjoll, yes. It's punishable by death. Especially Saelara... Her worship is considered the gravest blasphemy. Father says her name poisons the wind."
            svante "But I rarely see Tetrad worshippers punished for it. Some keep their heads down. Live quietly. They're not hunted unless they cross a line."
            svante "Still... my mother always told me: \"Too much mercy for the killer becomes cruelty to the dead.\""

            hide svante
            show niko underwear_serious at right_char with Dissolve(0.2)
            niko "Maybe Fynn did see Enoch. You'd be surprised how often the divine walks among us, especially when desperation opens the door. You speak of madness-but what if he really was chosen?"

            hide niko
            show yuxuan underwear_angry at right_char with Dissolve(0.2)
            yuxuan "Are you joking? He murdered a mother and her child in the name of your rotting corpse deity! You defend this?"

            hide yuxuan
            show niko underwear_meditate at right_char with Dissolve(0.2)
            niko "Only those who follow a sane god can understand the cost of divine obedience. Unlike others who would worship an overgrown lizard."

            hide niko
            show yuxuan underwear_angry at right_char with Dissolve(0.2)
            yuxuan "LIZARD?! HOW DARE YOU- The Prosperity Dragon ISN'T A LIZARD!"

            hide yuxuan
            show chunghee underwear_base at right_char with Dissolve(0.2)
            voice audio.chung_ch9_line61  # transcript: "The two of you calm"
            chung_hee "The two of you, calm down."

            hide chunghee
            show magnus underwear_serious at right_char with Dissolve(0.2)
            "Magnus took a careful step toward Fynn, expression soft but troubled."

            voice audio.magnus_ch9_line87  # transcript: "You took two lives, Finn."
            magnus "You took two lives, Fynn. A mother and her child. Look at me."

            "Fynn raised his head, trembling."

            voice audio.magnus_ch9_line88  # transcript: "Do you feel it? The"
            magnus "Do you feel it? The weight of what you've done? Do you... regret it?"

            "Fynn stared at him. For the briefest second, a flicker of uncertainty passed through his eyes-like a man waking from a terrible dream. Then his lips split into a smile."

            voice audio.fynn_ch9_line11  # transcript: "No. I was chosen. I'd"
            fynn "No. I was chosen. I'd do it again if my Lord commanded me to."
            voice audio.fynn_ch9_line12  # transcript: "Oh, Hail Lord Enoch!"
            fynn "ALL HAIL LORD ENOCH!"

            "The air turned still. Even the snow seemed to freeze in place."        
            voice audio.hulijing_ch9_line36  # transcript: "Oh, how deliciously complicated mortals"
            huli_jing "Ooooh... how deliciously complicated. Mortals and your morality. So-will you judge, dumplings?"

            scene bg_mjoll_icelands with Dissolve(0.1)
            show snow_blizzard_1

            jump choice_judgement_mjoll

    jump ch9_judgment_hinami


# =============================================================================
# SECTION 7: LABEL CH9_JUDGMENT_HINAMI — Illusion: Hinami / Katashi Morita Trial
# =============================================================================

label ch9_judgment_hinami:

    # [COMMENT: bg_hinami — cliffside, blue sky, crashing waves below]
    scene hinami_castle_morning with flash                  # PLACEHOLDER — Hinami cliffs illusion
    # stop music fadeout 0.5
    # play music ost_judgment_hinami fadein 0.5   # PLACEHOLDER — Hinami judgment theme

    "Then, the air shifted again."
    "The bitter cold of Mjoll vanished like melting frost. In its place came warmth-salt-laced and sun-kissed. The world opened into color and light."
    "Suddenly, we were standing atop windswept cliffs beneath a wide blue sky."
    "The scent of the sea wrapped around us, briny and deep. Waves thundered against the rocks below, their rhythm steady."

    show svante underwear_nervous at left_char
    show magnus underwear_base at center_char
    show niko underwear_serious at right_char
    with Dissolve(0.2) 

    svante "W-We're not at Mjoll anymore."
    voice audio.magnus_ch9_line89  # transcript: "Really? Where are we now?"
    magnus "Really? Where are we now?"
    niko "Hinami..."
    
    hide svante
    hide magnus
    hide niko
    show huli_jing at center_char
    show chunghee underwear_neutral at left_char 
    show niko underwear_meditate at right_char
    with Dissolve(0.2)
    "He stepped forward, lifting his face to the wind."

    show niko underwear_ignore at right_char with Dissolve(0.1)
    niko "This ocean scent... It's unmistakable. It's from Hinami."
    show niko underwear_serious at right_char with Dissolve(0.1)

    voice audio.chung_ch9_line62  # transcript: "That's right. You said you"
    chung_hee "That's right. You said you were from Hinami..."
    voice audio.hulijing_ch9_line37  # transcript: "That's right. Welcome to Hinami"
    huli_jing "That's right! Welcome to Hinami, little dumplings! Ahhh... can you feel it?"
    voice audio.hulijing_ch9_line38  # transcript: "A sout in your lungs,"
    huli_jing "The salt in your lungs, the sun on your cheeks? A perfect day for judgment."
    hide chunghee
    show svante underwear_nervous at left_char
    with Dissolve(0.2)
    svante    "A-Another judgment?!"

    "She turned, fox tail swaying."

    voice audio.hulijing_ch9_line39  # transcript: "Look behind you dumplings."
    huli_jing "Look behind you, dumplings."

    "We did."
    "Chained to the jagged cliff face was a man. Arms outstretched, his body crucified by salt and time. His skin was rough and sun-darkened, his clothes tattered and clinging to his frame."
    "Bruises ringed his wrists where iron bit into flesh. The tide lapped at his ankles like a patient predator. With every swell, he shivered."
    "Below him, kneeling in the wet sand, was a woman. Her shoulders shook with sobs as she clutched a bundle of soaked cloth to her chest."

    emi "Please! Please, he didn't mean any harm!"

    "Her cries echoed across the shore. Even the seagulls were silent."

    voice audio.hulijing_ch9_line40  # transcript: "Miss Mann is Katashima Rita."
    huli_jing "This man is Katashi Morita. Once a fisherman. Now heralded as a thief."

    "She gestured to the girl, who clung to a soaked bundle of cloth."

    voice audio.hulijing_ch9_line41  # transcript: "And that is Emmy, his"
    huli_jing "And that is Emi, his daughter. She's been crying since dawn."
    emi       "Please! Save my father. I beg you!"
    voice audio.hulijing_ch9_line42  # transcript: "This game is too fine."
    huli_jing "Ah, this game is divine. You know the rules, my dumplings. Like before-you judge."

    hide svante
    show magnus underwear_serious at left_char
    with Dissolve(0.2)
    voice audio.magnus_ch9_line90  # transcript: "Just like before Justice is"
    magnus "Just like before... Justice is not a sword, but a wave. It wears you down. It erodes the soul. It asks you to stand in the storm and never flinch."
    voice audio.hulijing_ch9_line43  # transcript: "Well said pretty one."
    huli_jing "Well said, pretty one."
    voice audio.hulijing_ch9_line44  # transcript: "So beloved judges, what now?"
    huli_jing "So, beloved judges... what now? This island's laws are clear. Theft is theft. And the punishment?"
    voice audio.hulijing_ch9_line45  # transcript: "and death."
    huli_jing "DEATH."
    hide magnus
    show yuxuan underwear_sad at left_char
    with Dissolve(0.2)
    yuxuan    "D-Death? Niko-tell me that's not true."
    niko "It depends on what was stolen. On who it was stolen from. And why. Hinami's laws are old... and not always kind."
    voice audio.hulijing_ch9_line47  # transcript: "But here, your judgment holds"
    huli_jing "But here, your judgment holds sway. What will your choice be?"


label choice_judgement_hinami:
    hide yuxuan
    hide niko
    show dorian underwear_serious at left_char 
    show magnus underwear_serious at right_char
    with Dissolve(0.2)

    "I looked at my companions. Magnus whispered, barely audible."

    voice audio.magnus_ch9_line91  # transcript: "The burden of choice, forced"
    magnus "The burden of choice falls to us."

    menu:

        "Pass the judgment of Death.":

            "I closed my eyes, the weight of the island pressing on my chest. When I opened them, I lifted my hand."

            dorian "Hinami's laws are cruel... but they are clear. And you, Katashi Morita, have broken them. I pass the judgment of death."

            "Emi's scream pierced the sky."

            emi "No-NO! You said the judges were kind! Please-no! He did it for me! It should've been me!"

            "She stumbled forward, crawling toward the shore as if she could reach him. Her voice cracked, desperation raw and bleeding."
            "Katashi didn't resist. His eyes were steady, weathered like driftwood."

            katashi "Then let the Tetrad see my blood... and judge them who made me choose between hunger and crime."

            "He turned his gaze to his daughter, voice soft now, almost inaudible against the crashing surf."

            katashi "Emi... my daughter... live. That's all I ever wanted for you. Please... live."
            emi     "Father! No! NO! *cries*"

            "The Huli Jing exhaled, slowly, her smirk dimming like a flame losing air."

            voice audio.hulijing_ch9_line48  # transcript: "Ah, cold justice. Spirits, let"
            huli_jing "Ah, cold justice... Spirits, let it be done."

            "There was a faint sound-like metal on stone-as the chains coiled tighter. The wind howled."
            "Then, the wave rose-taller than any before, unnaturally high, as if the sea itself was delivering judgment. It crashed forward."
            "And when the water receded... he was gone."

            emi "NO! FATHER! FATHER! PLEASE!"

            "The tide tugged gently at the hem of her dress, as if trying to comfort her. But there was no comfort here."
            hide magnus 
            show svante underwear_sad at right_char with Dissolve(0.2)
            svante    "I... I thought we were better than this."

            hide svante
            show magnus underwear_serious at right_char with Dissolve(0.2)
            voice audio.magnus_ch9_line92  # transcript: "I hope you're proud of"
            magnus "I hope you're proud of yourself, Dorian."

            hide magnus
            show niko underwear_serious at right_char with Dissolve(0.2)
            niko "The law is not kindness, it is structure. And Katashi knew what he risked when he broke it."
            niko "We cannot let emotion blind us. That is how justice becomes chaos. Dorian did what needed to be done, even when it hurt. That is the mark of a real judge."
            hide niko
            show yuxuan underwear_angry at right_char with Dissolve(0.2)
            yuxuan    "\"wE cAnnOt lEt eMotIon bLind Us\" Hmph!"

            "Niko rolled his eyes."

            voice audio.hulijing_ch9_line49  # transcript: "Hmm, so be it. One"
            huli_jing "Mmm. So be it. One life ends... another sorrow born."

        "Pass the judgment of Exile.":

            "I stepped forward, my voice cutting through the mist."

            dorian "Your crime cannot be ignored. But your reasons... I understand them. You will not die, Katashi. But you are banished. From Hinami. Forever."

            "Katashi looked down at his daughter, sorrow blooming across his weathered features."

            katashi "Exile is a quieter death... but it is a death I can meet on my feet. Thank you. For sparing me."
            emi     "Wait-what? No! Where will we go? We have no coin, no boat-how will we survive?"

            "Before the wind could carry her tears, the chains snapped. Not with violence-but with finality."
            "Dark shapes emerged from the rocks-shadows, cloaked and faceless-guiding the father and daughter away from the cliffs."

            katashi "We'll survive, Emi. We always have. One tide at a time."
            emi     "Yes, Father."

            hide magnus 
            show chunghee underwear_neutral at right_char with Dissolve(0.2)
            chung_hee "He will live. That, in itself, is a mercy most do not receive."
            hide chunghee
            show niko underwear_base at right_char with Dissolve(0.2)
            niko "This is mercy, by Hinami's standards. And mercy... is a rare, dangerous thing. Enoch, please forgive us..."

            hide niko
            show yuxuan underwear_lying at right_char with Dissolve(0.2)
            yuxuan    "I don't care about Enoch's forgiveness."
            
            hide yuxuan
            show magnus underwear_base at right_char with Dissolve(0.2)
            voice audio.magnus_ch9_line93  # transcript: "Wherever the sea carries you,"
            magnus "Wherever the sea carries you-may it carry you to peace. I wish you both the best."

            "Huli Jing twirled one tail lazily."

            voice audio.hulijing_ch9_line50  # transcript: "Hmm, a soft punishment wrapped"
            huli_jing "A soft punishment wrapped in thorns."

            "She tilted her head toward me, eyes narrowing playfully."

        "Pass the judgment of Forgiveness.":
            $ huli_jing_approval += 1           # +1 Huli Jing approval

            dorian "You stole-but not for greed. For love. For survival. You chose your daughter's life over obedience to a cruel system. And for that..."
            dorian "You will not die. You are forgiven."

            "A silence followed-still and wide as the sea itself. Even the wind paused."
            "Katashi's mouth parted, trembling. His knees buckled, but he caught himself. Tears began to spill freely, carving tracks through the grime on his cheeks. He lowered his head in reverence."

            katashi "You... you honor me more than this island ever has. I have no words, only gratitude. From the deepest part of me... thank you."

            "Beside him, Emi sobbed and threw herself around his waist, her arms locking tight around her father."

            emi "Thank you!! Thank you! You saved him-you saved us!"

            "With a sound like falling rain, the chains shattered, not broken by force-but by will. They fell into the surf, vanishing beneath the tide."

            hide magnus
            show niko underwear_serious at right_char with Dissolve(0.2)
            niko "This will... upset the elders. Enoch, judge us gently. We have strayed from the letter of the law-but perhaps not its spirit."
            hide niko
            show magnus underwear_base at right_char with Dissolve(0.2)
            voice audio.magnus_ch9_line94  # transcript: "Let them be upset. If"
            magnus "Let them be upset. If the law cannot bend for the starving, then it deserves to break."
            hide magnus
            show yuxuan underwear_happy at right_char with Dissolve(0.2)
            yuxuan "Yeah! What Magnus said!"
            hide yuxuan
            show svante underwear_neutral at right_char with Dissolve(0.2)
            svante "I hope the world is kinder to you from now on. I hope it gives you peace. You both deserve it."
            hide svante
            show magnus underwear_serious at right_char with Dissolve(0.2)
            voice audio.magnus_ch9_line95  # transcript: "Just as without mercy is"
            magnus "Justice without mercy is a sword that rusts in its own blood~ Let this tide wash away the weight-let love be understood~"

            "Katashi and Emi turned, bowing deeply. The shadows returned-silent escorts. But this time, they walked behind, not leading them like prisoners-but following them like guardians."

            huli_jing "...!"

            "Huli Jing smiled wide, teeth sharp but gleaming like polished pearls. Her silver tails flicked in satisfaction."

        "Investigate first and ask the others for their opinion.":

            dorian "Before we make any decisions... I want to speak to Katashi first."
            emi    "Please, sirs! I beg of you!"

            "Tears streamed down her face, her hands clutching the soaked hem of her robe."

            voice audio.hulijing_ch9_line51  # transcript: "Don't worry, Dumbling. Your father's"
            huli_jing "Don't worry, dumpling. Your father's fate will be spun soon enough."

            "She tapped her chin with a lacquered claw, eyes gleaming."

            voice audio.magnus_ch9_line96  # transcript: "What do you have to"
            magnus "Kind sir... What do you have to say for yourself? Do you deny the charges laid upon you?"
            katashi "I do not deny it. I broke the law."
            katashi "But tell me-is it justice to watch your child starve? Is it noble to let your daughter bathe in saltwater while nobles hoard rose oils and perfumes? I am no saint. But I would steal again if it meant she could eat."
            
            hide magnus 
            show chunghee underwear_neutral at right_char with Dissolve(0.2)
            chung_hee "Eat, you say? Then enlighten us, Katashi Morita. What prize did you deem worth breaking the King's law?"
            katashi "A loaf of bread. A sack of rice. A bar of soap. Two dried fish."

            "Svante looked like he'd been punched."
            hide chunghee
            show svante underwear_sad at right_char 
            show dorian underwear_sad at left_char
            with Dissolve(0.2)
            svante  "T-That's it? Just food and soap?"
            emi     "We were starving! We hadn't eaten in days. Please... he didn't want to steal. I begged him not to... but-he did it for me!"
            dorian  "Where did you steal the food and soap?"
            show dorian underwear_serious at left_char with Dissolve(0.1)
            katashi "... I stole from the home of Lord Nakai."
            hide svante
            show niko underwear_serious at right_char with Dissolve(0.2)
            niko "Merciful En-... Lord Nakai?!"
            niko "You've either got guts or a death wish. Might as well stroll into a yaoguai king's den and ask for a cup of tea."
            hide niko
            show svante underwear_base at right_char with Dissolve(0.2)
            svante  "Who is Lord Nakai, Niko?"
            hide svante
            show niko underwear_serious at right_char with Dissolve(0.2)
            niko "One of Hinami's high lords. Second only to King Tatsuya Fujiwara. He commands the military and answers to no one but the crown."
            niko "The man would have you flayed for touching his wine cellar, let alone stealing from his kitchens."
            katashi "I knew the risk. But his servants throw away more food in a week than most villages see in a season. I couldn't watch her waste away. Not again."
            hide niko
            show chunghee underwear_neutral at right_char with Dissolve(0.2)
            voice audio.chung_ch9_line63  # transcript: "again. What do you mean"
            chung_hee "Again? What do you mean... 'not again'?"
            emi     "We had... a sister. Her name was Maru."
            emi     "She died last winter. Her belly swollen from hunger, her skin cracked and cold. We had no firewood. No rice. No medicine."
            katashi "Lord Nakai never paid us our wages. We toiled from dawn till night, patching nets and scrubbing floors. But when the season ended, his men said we were too late-too slow. No coin. No food. No justice."
            katashi "I swore I'd never lose another child."
            emi     "Please! I beg you-don't take him from me..."

            "She suddenly stumbled toward Chung-hee, dropping to her knees and clutching his bare ankles."

            emi "Please, your highness, your grace-anything! Take my life instead! I'll serve-I'll go in his place! Just let him go!"

            "She lowered her face, lips trembling, and pressed them against his foot. Svante blushed and shielded his face."
            hide chunghee
            show svante underwear_nervous at right_char with Dissolve(0.2)
            svante    "N-No! Please don't do that, we're still in our undergarments!"
            hide svante
            show chunghee underwear_sad at right_char with Dissolve(0.2)
            chung_hee "H-Hey... that's-this is highly improper. Please rise. There is no need for... such a display."
            voice audio.hulijing_ch9_line52  # transcript: "Hey, no touching the judges,"
            huli_jing "Hey! No touching the judges! That's against the rules!"

            hide chunghee
            show yuxuan underwear_angry at right_char with Dissolve(0.2)
            yuxuan    "This is preposterous!"
            yuxuan    "I am Cheng Yuxuan, an inventor of great renown! I've contributed to the advancement of technology in countless kingdoms! And yet, here I am, in my undergarments in front of all to see!"
            yuxuan    "You could have at least gotten us some clothes before making us judges, you know!"
            voice audio.hulijing_ch9_line53  # transcript: "And where's the fun in"
            huli_jing "And where's the fun in that?"
            emi       "Please! I'll scrub floors-I'll beg Lord Nakai himself-I'll cut off my hair, my hands, just please... don't let him die!"

            "Her words hung in the salt-heavy air, raw and aching."
            "I turned to the others, the wind pressing against my back like a tide urging me to speak."

            dorian    "You've heard him. Now I ask you-what do you think?"
            hide yuxuan
            show niko underwear_meditate at right_char with Dissolve(0.2)
            niko "According to the teachings of Lord Enoch, the law is the spine of civilization. Harsh? Perhaps. But mercy without order is rot without bone."
            niko "\"When one man steals with no consequence, a hundred more will follow. Then who feeds the honest?\" That's what Enoch teaches. The law must stand-or all things crumble."
            hide niko
            show chunghee underwear_base at right_char with Dissolve(0.2)
            chung_hee "As the Emperor of Kyeongjang, I've had to pass judgments that weighed heavy on my heart."
            chung_hee "Aunt Ji - I mean, my royal advisor once told me, \"Compassion must walk behind law, not in front of it.\""
            chung_hee "Order is fragile. If the law bends for sympathy, how long until it breaks for greed?"
            hide chunghee
            show yuxuan underwear_sad at right_char with Dissolve(0.2)
            yuxuan    "But what kind of justice punishes a starving man trying to save his daughter? Are we really protecting society?! Or just the pride of the rich?"
            hide yuxuan
            show niko underwear_serious at right_char with Dissolve(0.2)
            niko "You're one to talk. You're one of the rich yourself."
            hide niko
            show yuxuan underwear_angry at right_char with Dissolve(0.2)
            yuxuan    "I try to feed as many as I can! I give what I have! I- I don't punish love with death! If we are going to punish him, at least don't kill him!"
            hide yuxuan
            show svante underwear_nervous at right_char with Dissolve(0.2)
            svante    "W-We should forgive him. Please. What kind of world punishes love like this?"
            svante    "A father's love... I..."

            "Then, Magnus stepped forward. His eyes were on Katashi, but his voice was lifted to the crashing sea."
            hide svante
            show magnus underwear_serious at right_char with Dissolve(0.2)
            voice audio.magnus_ch9_line97  # transcript: "I don't care what the"
            magnus "I don't care what the law says."
            magnus "Justice without compassion is cruelty dressed in gold. If the law demands we turn away from the hungry, then the law has already failed."
            show magnus underwear_base at right_char with Dissolve(0.1)
            voice audio.magnus_ch9_line98  # transcript: "Look at her, look at"
            magnus "Look at her. Look at him. Tell me-are these the faces of danger? Are these threats to the throne?"
            voice audio.magnus_ch9_line99  # transcript: "Break the chains. Feed them."
            magnus "Break the chains. Feed them. Heal them. That is the kind of kingdom I would fight for."
            hide magnus
            show niko underwear_serious at right_char with Dissolve(0.2)
            niko "This isn't about threats, Magnus. It's about precedent. The moment the law yields, even once, every tyrant will find cause to twist it."
            hide niko
            show chunghee underwear_base at right_char with Dissolve(0.2)
            chung_hee "As much as it pains me, I must agree. The law is not a feeling-it is a pillar. Without it, we drift."
            voice audio.hulijing_ch9_line54  # transcript: "Hmm, such passion, such division,"
            huli_jing "Mmm... such passion. Such division. Oh, my dumplings... what a delightful dilemma."
            voice audio.hulijing_ch9_line55  # transcript: "Well then, Dragon of Gail,"
            huli_jing "Well then, Dragon of Gale... it falls to you."

            "I then turned to the Huli Jing."
            "I turned to look at them all-at Katashi, crucified by justice; at Emi, drowning in desperation; at the sea, endless and roaring. The world held its breath."
            
            scene hinami_castle_morning with Dissolve(0.1)
            jump choice_judgement_hinami

    jump ch9_judgment_kyeong


# =============================================================================
# SECTION 8: LABEL CH9_JUDGMENT_KYEONG — Illusion: Kyeongjang / Seorin Im Trial
# =============================================================================

label ch9_judgment_kyeong:

    # [COMMENT: bg_kyeongjang_palace — palace courtyard, pagodas, marble platform]
    scene kyeonjang_palace with flash       # PLACEHOLDER — Kyeongjang illusion
    stop music fadeout 0.5
    play music ost_judgment_kyeong fadein 0.5   # PLACEHOLDER — Kyeongjang judgment theme

    "The air shifted again-sharp and dry, like brittle parchment touched by flame."
    "The scent of lotus blossoms and aged ink reached my nostrils, thick and heady. My feet met smooth stone, cold to the touch. I looked around slowly."
    "We were no longer near the sea."
    "Towering pagodas surrounded us, their curved rooftops gleaming with gold leaf beneath a pale sky. The very ground vibrated with power-a coiled pressure humming just beneath the surface."
    "I blinked, adjusting to the light that struck the stone courtyard like polished jade. And then-I saw her."
    "A woman knelt in the center of a marble platform, chains wrapped tight around her wrists. Her hanbok was torn, stained from travel or shame."
    "Her long black hair hung in tangles, but even in ruin, she carried a strange grace."
    "She raised her head. Her hollow, desperate eyes locked onto one of us."

    seorin "Y-Your Majesty?"

    show chunghee underwear_neutral at left_char with Dissolve(0.2)

    "Chung-hee was startled. His face flushed, and he shifted awkwardly, hand tugging at the edge of the towel slung over his shoulders. We were, after all, still in our undergarments."

    voice audio.chung_ch9_line64  # transcript: "Shorin Sun-Sing-Yim."
    chung_hee "Seorin seonsaengnim?"

    show huli_jing at right_char with Dissolve(0.2)

    "Huli Jing cooed from above, now reclined on a gilded parasol carried by an unseen force, her nine tails fanned out like a blooming chrysanthemum."
    voice audio.hulijing_ch9_line56
    huli_jing "Ahhh, so he does know her. Even better. The final judgment will cut closest to the heart."
    hide huli_jing 
    hide chunghee
    show huli_jing at center_char
    show chunghee underwear_sad at right_char   
    show dorian underwear_sad at left_char
    with Dissolve(0.2)
    dorian    "Wait... You know her, Chung?"
    chung_hee "She was my past mentor. In alchemy. Before I ever wore the crown."

    show dorian underwear_serious at left_char 
    show chunghee underwear_base at right_char   
    with Dissolve(0.1)
    "He narrowed his eyes at the ornate architecture."

    voice audio.chung_ch9_line65  # transcript: "with this vision I take"
    chung_hee "With this vision, I take it we stand in Kyeongjang?"

    voice audio.hulijing_ch9_line57  # transcript: "Right, you are dumpling. Welcome"
    huli_jing "Right you are, dumpling! Welcome back to the capital!"

    hide chunghee
    show svante underwear_neutral at right_char with Dissolve(0.2)
    svante "W-Wow... This is Kyeongjang? It's beautiful..."

    hide svante
    show yuxuan underwear_normal at right_char with Dissolve(0.2)
    yuxuan "PRAISE THE PROSPERITY DRAGON! KYEONGJANG! AT LAST!"
    yuxuan "I have waited for this moment my entire life! My life's work has led me to this moment! Niko, pinch me! I must be dreaming!"

    hide yuxuan
    show niko underwear_serious at right_char with Dissolve(0.2)
    niko "This is still an illusion, Yuxuan. Part of the Huli Jing's game."

    hide niko
    show magnus underwear_base at right_char with Dissolve(0.2)
    voice audio.magnus_ch9_line100  # transcript: "Beautiful Magnificent Kiongdong! Oh how"
    magnus "Beautiful, magnificent Kyeongjang! Oh, how noble your towers, how gleaming your-"

    
    show dorian underwear_normal at left_char with Dissolve(0.1)
    dorian "Magnus. Please. Save the ballad for later."
    show dorian underwear_neutral at left_char with Dissolve(0.1)
    hide magnus
    show chunghee underwear_base at right_char with Dissolve(0.2)
    voice audio.chung_ch9_line66  # transcript: "Sun Sang-gyin, explain yourself."
    chung_hee "Seonsaengnim. Explain yourself."

    seorin "Y-Your Majesty! I didn't mean for any of it. I swear it, I didn't."

    show dorian underwear_serious at left_char with Dissolve(0.1)
    "Her voice cracked as she tried to rise, but the chains held her fast."
    voice audio.hulijing_ch9_line58
    huli_jing "Seorin Im. Scholar. Once one of the most promising alchemists in the Empire. Tasked with crafting a powerful medicinal salve for the royal hospital-one that would heal plague, infection, and injury alike."
    voice audio.hulijing_ch9_line59  # transcript: "but her alchemy was flawed."
    huli_jing "But her alchemy was flawed. The ingredients, unstable. Instead of healing the sick..."
    voice audio.hulijing_ch9_line60
    huli_jing "...it poisoned them. Fifty-five souls. Gone. Thirty-seven imperial soldiers. Eighteen children. Every last one who drank the salve died within hours."

    hide chunghee
    show magnus underwear_base at right_char with Dissolve(0.2)
    voice audio.magnus_ch9_line101  # transcript: "Those poor children..."
    magnus "Those... Those poor children..."

    show dorian underwear_serious at left_char with Dissolve(0.2)
    dorian "Tetrad above..."

    hide magnus
    show niko underwear_meditate at right_char with Dissolve(0.2)
    niko "Unforgivable. I've seen things like this in Hamatame. Villagers dosing the sick with faulty tinctures, hoping for miracles. It always ends in death. You don't gamble with lives-not as a healer. Not ever."
    show niko underwear_serious at right_char with Dissolve(0.1)

    seorin "I-I didn't know, Your Majesty! It was a mistake! Please, I beg you!"

    "She turned to Chung-hee, voice trembling, heart in her throat."

    seorin "You know me, Your Majesty... You know I would never do this deliberately."

    "Around the platform, ghostly silhouettes began to appear-spirits with soft blue eyes and pale robes, their hands clasped before them as if in mourning."

    voice audio.hulijing_ch9_line61  # transcript: "So, my beautiful dumplings, for"
    huli_jing "So... my beautiful dumplings. For the last time. Death, exile, or forgiveness?"

    show niko underwear_ignore at right_char with Dissolve(0.1)
    niko "Last time? Great."

label choice_judgment_kyeong:
    show huli_jing at center_char
    show dorian underwear_serious at left_char
    show niko underwear_serious at right_char 
    with Dissolve(0.1)

    voice audio.hulijing_ch9_line62  # transcript: "The dead don't speak, but"
    huli_jing "The dead don't speak, but they remember. And they are watching."
    "She grinned, sharp as a blade."

    voice audio.hulijing_ch9_line63  # transcript: "Judge-wise, the dragon of Gail,"
    huli_jing "Judge wisely, Dragon of Gale. This one cuts to the bone..."

    menu:
        "Pass the judgment of Death.":

            "I closed my eyes. The weight of it all pressed down on my chest like iron."

            dorian "Seorin Im. By your own admission, your salve was unstable. Your negligence took the lives of children, soldiers... innocent people who trusted you."
            dorian "We pass the sentence of death to you, Seorin Im."
            seorin "No... Your Majesty-please! You know me-!"

            "But her voice broke as Chung-hee turned away."
            hide niko
            show chunghee underwear_sad at right_char with Dissolve(0.2)
            voice audio.chung_ch9_line67  # transcript: "I didn't know you once."
            chung_hee "I did know you once."

            "The shadows moved without a sound. Like a tide, they rose-liquid, cold, inky-and swallowed her whole."
            show dorian underwear_sad at left_char with Dissolve(0.1)
            seorin "No! No! Get away! NO!"

            "They enveloped her. And then- Silence. She was gone."
            "Yuxuan muttered a prayer under his breath."

            hide chunghee
            show yuxuan underwear_sad at right_char with Dissolve(0.2)
            yuxuan    "By the Prosperity Dragon... may her spirit find peace."
            hide yuxuan
            show niko underwear_serious at right_char with Dissolve(0.2)
            niko "She made her choice long before this moment. Enoch teaches: mistakes may be human, but consequences are divine."
            hide niko
            show chunghee underwear_sad at right_char with Dissolve(0.2)
            chung_hee "I am sorry, Seorin seonsaengnim. I wish the stars had guided your path elsewhere."
            hide chunghee
            show magnus underwear_serious at right_char with Dissolve(0.2)
            voice audio.magnus_ch9_line102  # transcript: "So many lives, so many"
            magnus "...So many lives. So many lost. But in the end... it was her hand that made the poison."
            voice audio.hulijing_ch9_line64  # transcript: "So cruel! And yet, so"
            huli_jing "So cruel... and yet so just. Your judgment echoes through the heavens, dumpling."

        "Pass the judgment of Exile.":
            $ huli_jing_approval += 1           # +1 Huli Jing approval

            dorian "Your negligence caused suffering on a scale we can't ignore. You are exiled. You will never set foot on Kyeongjang soil again."

            "I turned to Chung-hee, who gave a solemn nod."
            hide niko
            show chunghee underwear_sad at right_char with Dissolve(0.2)
            voice audio.chung_ch9_line77  # transcript: "I have no qualms with"
            chung_hee "I have no qualms with the judgment, Dorian."

            "Her voice cracked, but she did not argue."

            seorin "I... I understand. Thank you."
            chung_hee "Farewell, Seorin seonsaengnim. I wish the stars had guided your path elsewhere."

            "Chains dissolved into smoke. She crumpled to the ground, then rose, trembling. The spirits turned their backs on her as she was led away by shadowy guards."

            seorin "Farewell, Your Majesty."
            hide chunghee
            show yuxuan underwear_lying at right_char with Dissolve(0.2)
            yuxuan    "That was fair. Harsh... but fair."
            hide yuxuan
            show niko underwear_meditate at right_char with Dissolve(0.2) 
            niko "She'll never escape the guilt. That's a heavier sentence than steel."
            voice audio.hulijing_ch9_line65  # transcript: "A punishment without blunt. Elegant"
            huli_jing "A punishment without blood... elegant, in its own way."

        "Pass the judgment of Forgiveness.":

            dorian "Seorin Im. You made a mistake. One you'll carry the rest of your life. But we believe in redemption... and we believe you would give your life to take it all back."
            dorian "And for that, we pass the judgment of forgiveness to you, Seorin Im."
            seorin "A thousand thank yous would not suffice. I... I will not waste this chance."

            "Her wrists slackened as the chains uncoiled, shimmering into mist. She gasped, then clutched her own hands tightly, tears running freely."

            seorin "Thank you... Thank you..."

            "Chung-hee stood motionless, the wind ruffling the towel at his shoulders. His hand trembled slightly at his side. Then, with difficulty, he gave a single, solemn nod."
            "The shadows returned-not as hunters, but as silent escorts. They gathered around Seorin like quiet sentinels and began to lead her away."
            hide niko
            show yuxuan underwear_happy at right_char with Dissolve(0.2) 
            yuxuan "Dorian buddy, that was brave! I think you did the right thing."

            hide yuxuan
            show magnus underwear_base at right_char with Dissolve(0.2) 
            voice audio.magnus_ch9_line103  # transcript: "I would inclaim it was"
            magnus "I wouldn't claim it was the right thing... But if justice can wear a gentler face, then let it be this one. My heart is at peace with the path we've chosen."
            
            hide magnus
            show niko underwear_meditate at right_char with Dissolve(0.2) 
            niko "You forgave her. And now she walks away. Just like that."
            show niko underwear_serious at right_char with Dissolve(0.1) 

            niko "I hope those fifty-five souls get to walk too. I hope the parents of those children get to wake up tomorrow without weeping. I hope the soldiers get their years back."
            niko "But they won't. I hope you understand that."
            hide niko

            show svante underwear_base at right_char with Dissolve(0.2) 
            svante "I... I want to believe people deserve a second chance, but... I kind of agree with Niko. That many lives? It's hard to forgive fully."
            voice audio.hulijing_ch9_line66  # transcript: "Oh, you tend a little"
            huli_jing "Oh, you tender little dumpling. Mercy is a delicious flavor."

        "Investigate first and ask the others for their opinion.":

            "I turned to Chung-hee and met his gaze. I gave a nod. He returned it, slower, and he stepped forward."
            hide niko
            show chunghee underwear_base at right_char with Dissolve(0.2)
            voice audio.chung_ch9_line68  # transcript: "Sun-sang-yim, start from the beginning."
            chung_hee "Seonsaengnim. Start from the beginning. Tell us everything."
            seorin    "Yes, Your Majesty. I will."
            seorin    "I was tasked to create a salve powerful enough to heal plague, infection, burns... everything. I studied night and day."
            seorin    "I tested it thoroughly on rats, on plants, even small doses on myself. Every result was stable. As the Almighty Tetrad Immortal Renji is my witness."
            seorin    "But the supply-when it scaled to mass production... something changed. I swear I didn't alter the formula. I had no idea the ingredients had spoiled, or reacted differently in bulk..."
            
            hide chunghee
            show niko underwear_serious at right_char with Dissolve(0.2)
            niko "You didn't realize it was poison after it was distributed?"
            seorin    "No-I didn't... I didn't even know until I heard the soldiers were dying. Then the children..."

            "She looked down."
            seorin "By then it was too late. I rushed to the lab, ran test after test. It was the main reagent-it had turned unstable in storage."
            seorin "But it was already in the hands of the sick. Already killing them."
            hide niko
            show yuxuan underwear_sad at right_char with Dissolve(0.2) 
            yuxuan "This is... this is a disaster. A total collapse of safety protocols. How was this even allowed to pass inspection?"
            show yuxuan underwear_lying at right_char with Dissolve(0.1) 
            
            yuxuan "Cheng Industries better not be cutting corners like this. I'll need to audit our entire healing division. This can't ever happen in Tianho."
            seorin "And then I was arrested and brought here..."
            seorin "Your Majesty, please... I beg you. I was careless, yes. But not cruel. I never meant for harm."

            "I turned to the others. My chest was tight with the gravity of what I had to ask."

            dorian "For the last time. Tell me... what do you all think?"
            hide yuxuan
            show niko underwear_serious at right_char with Dissolve(0.2)
            niko "Even if it's just a mistake, it's a crime. And crimes have consequences. If we let her walk free, we say their deaths meant nothing."
            show niko underwear_ignore at right_char with Dissolve(0.2)
            niko "Fifty-five lives, Dorian. Fifty-five."
            hide niko
            show svante underwear_base at right_char with Dissolve(0.2) 
            svante "Niko's right. Their lives can't go unanswered. Forgiveness doesn't erase the dead."
            hide svante
            show yuxuan underwear_neutral at right_char with Dissolve(0.2) 
            yuxuan "I don't know. I... I see her remorse. But can we risk others thinking a mistake like this is acceptable?"
            hide yuxuan 
            show magnus underwear_serious at right_char with Dissolve(0.2) 
            voice audio.magnus_ch9_line104  # transcript: "She should not die. Death"
            magnus "She should not die. Death is final. She would learn nothing. Heal nothing. Let her live with the grief she caused-and do something with it. Make her rebuild what she destroyed."
            
            hide magnus
            show yuxuan underwear_neutral at right_char with Dissolve(0.2) 
            yuxuan "But letting her walk away unscathed... Would that be fair to the ones that died?"

            "I turned again to Chung-hee, but before I could speak, he raised a hand."
            hide yuxuan
            show chunghee underwear_base at right_char with Dissolve(0.2)
            dorian    "This is your empire, Chung. Your people. If you wish to render judgment, I will stand aside."
            show chunghee underwear_sad at right_char with Dissolve(0.1)
            voice audio.chung_ch9_line69  # transcript: "No, you should be the"
            chung_hee "No. You should be the one to deliver judgment, Dorian."
            chung_hee "I am the Emperor of Kyeongjang. And because of that-I cannot be the one to judge her. I knew Seorin once. Admired her even. That bond clouds my mind even now."
            voice audio.hulijing_ch9_line67  # transcript: "Oh, I love this! Look"
            huli_jing "Ohhh, I love this. Look at all of you, writhing on the hook of morality."
            seorin    "Please, Your Majesty!"
            voice audio.hulijing_ch9_line68  # transcript: "So, have we made a"
            huli_jing "So have we made a decision, dumpling?"
            
            scene kyeonjang_palace with Dissolve(0.1)
            jump choice_judgment_kyeong

    jump ch9_judgments_back


# =============================================================================
# SECTION 9: LABEL CH9_JUDGMENTS_BACK — Common: Back to Hot Spring
# =============================================================================

label ch9_judgments_back:

    # [COMMENT: bg_hot_spring — back to hot spring]
    scene yuxuan_lab_hotspring with flash              # PLACEHOLDER — hot spring return
    stop music fadeout 0.5
    play music ost_huli_jing fadein 0.5         # PLACEHOLDER — Huli Jing theme

    "The air shifted one final time."
    "The incense, the towers of Kyeongjang, the weight of our choices-all of it faded like breath on glass. The cold dissolved. The thunderous silence of the spirit realm gave way to something gentler."
    "Heat. Steam. The sound of water lapping gently at stone. We were back. In the hot springs."
    show yuxuan underwear_happy at center_char
    show chunghee underwear_base at right_char 
    show niko underwear_serious at left_char
    with Dissolve(0.2)

    yuxuan    "By the Prosperity Dragon's blessed scales-we're back!!"
    niko "That wasn't just illusion. That felt real. Too real."
    chung_hee "It was an illusion. I think. Tetrad above, I hope it was."

    "Magnus stretched dramatically, droplets flinging off his arms like golden ribbons."
    hide niko
    hide yuxuan
    hide chunghee
    show huli_jing at center_char
    show magnus underwear_base at right_char 
    show svante underwear_sad at left_char
    with Dissolve(0.1)
    voice audio.magnus_ch9_line105
    magnus "And yet... we're still in our undergarments. Perhaps now we can enjoy a proper bath without sentencing anyone to death."
    svante    "I don't think I'll ever look at justice the same way again..."
    show svante underwear_normal at left_char with Dissolve(0.1)
    voice audio.hulijing_ch9_line69  # transcript: "Mmm, delicious, wasn't it? Judging"
    huli_jing "Mmmm... Delicious, wasn't it? Judging mortals is no neat affair. It tangles the soul."
    voice audio.hulijing_ch9_line70  # transcript: "makes it chewy like good"
    huli_jing "Makes it chewy. Like good dumplings."

    if huli_jing_approval < 3:
        jump ch9_huli_reward_low
    else:
        jump ch9_huli_reward_high


# =============================================================================
# SECTION 10: LABEL CH9_HULI_REWARD_LOW — Fox Leaves Without Reward
# =============================================================================

label ch9_huli_reward_low:

    show huli_jing at center_char with Dissolve(0.2)
    voice audio.hulijing_ch9_line71
    huli_jing "As for your judgments, my dear dumplings... I was a little underwhelmed. Mmm. Lukewarm, like reheated noodles."
    voice audio.hulijing_ch9_line72  # transcript: "and give you a game,"
    huli_jing "I gave you a game. A gift of truth. And you judged... mediocrely. Is that even a word?"
    hide magnus
    hide svante
    show dorian underwear_serious at left_char
    show yuxuan underwear_angry at right_char
    with Dissolve(0.2)
    
    dorian    "But you promised. You said you'd leave the springs."
    yuxuan    "Yes! You swore it on your tails, remember? We upheld our end."
    show dorian underwear_neutral at left_char with Dissolve(0.1)
    voice audio.hulijing_ch9_line73
    huli_jing "And a promise is a promise. I shall never again haunt these springs, nor return to soak my tails. You'll never see me here again. Pity... I was beginning to like you."
    
    hide yuxuan
    show magnus underwear_ignore at right_char with Dissolve(0.2)
    voice audio.magnus_ch9_line106  # transcript: "And we were starting to"
    magnus "And we were starting to like you too, beloved fox!"
    show magnus underwear_base at right_char with Dissolve(0.2)
    voice audio.magnus_ch9_line107  # transcript: "Fare well to the fox"
    magnus "Farewell to the fox with the nine shining tails... To judgment and laughter where truth always sails...~"
    voice audio.hulijing_ch9_line74  # transcript: "Well, I love it dumpling,"
    huli_jing "Wow! I love it, dumpling! I'm going to miss you!"

    hide magnus
    show niko underwear_serious at right_char with Dissolve(0.2)
    niko "Wait. You also promised one answer. One truth."
    voice audio.hulijing_ch9_line75  # transcript: "Hmm, but you failed the"
    huli_jing "Ah... but you failed the game. No answer for you. But I am not without gifts."

    "She snapped her claws-"

    play sound audio.sfx_fwoop                 # PLACEHOLDER — FWOOMP SFX

    "FWOOMP."

    jump ch9_stuffed_fox_exit


# =============================================================================
# SECTION 11: LABEL CH9_HULI_REWARD_HIGH — Fox Grants Question
# =============================================================================

label ch9_huli_reward_high:

    show huli_jing at center_char
    voice audio.hulijing_ch9_line76
    huli_jing "As for your judgments, my dear dumplings..."
    voice audio.hulijing_ch9_line77  # transcript: "I am beyond delighted, compassion"
    huli_jing "I am beyond delighted. Compassion with justice, side by side... How refreshing."

    "A shimmer of foxfire circled her ankles as she floated down gracefully onto the steaming surface of the spring."
    hide magnus
    hide svante
    show niko underwear_smile at right_char
    show yuxuan underwear_happy at left_char
    with Dissolve(0.2)
    niko "Well... that's reassuring. I was starting to question everything."

    "Chung-hee, ever the stoic, crossed his arms and gave the faintest, coolest nod."

    yuxuan "THANK YOU, PROSPERITY DRAGON! YESSS!!"
    hide niko
    hide yuxuan
    show magnus underwear_base at left_char
    show svante underwear_neutral at right_char
    with Dissolve(0.2)
    voice audio.magnus_ch9_line108  # transcript: "I'm sure I'd end up"
    magnus "I was sure I'd end up cursed. Or bald."

    "Huli Jing floated closer to me. The lavender steam coiled around her as if drawn by her warmth."
    "Then her golden eyes narrowed, a glint of something ancient sparkling behind them."

    voice audio.hulijing_ch9_line78  # transcript: "As a reward, I'll grant"
    huli_jing "As a reward, I will grant something I haven't done in centuries, sweet dumpling. One question. Any question, and I will answer."

    "The air stilled. Even the steam seemed to hold its breath."

    svante "My mother used to tell stories about this... She said the Huli Jing only ever answered a single question as a reward before. Just once in all her lifetimes..."
    hide magnus
    show dorian underwear_serious at left_char with Dissolve(0.2)
    "My eyes widened. Is that true?"

    dorian "Really? Who did she answer?"
    svante "Li Mengtia. The Divine Tetrad of Knowledge and Wisdom. That was a thousand years ago."

    hide svante
    show chunghee underwear_base at right_char with Dissolve(0.2)
    chung_hee "Dorian. Ask about the future of Ena. We need to know if the Divine Weapon still poses a threat."

    "My heartbeat slowed. The fox spirit smiled, nine tails curling gently around her."

    voice audio.hulijing_ch9_line79  # transcript: "So, my dumpling, ask, one"
    huli_jing "So, my dumpling... ask. One truth, one mystery, one thread in the grand weave of fate. I will answer. Just once."

    menu:

        "Ask about the future of Ena.":

            dorian "What's going to happen to Ena?"

            "The question hung in the steam like a thread pulled tight."
            "The Huli Jing paused, tilting her head. One tail slowly wrapped around her arm like a silken ribbon."

            voice audio.hulijing_ch9_line80  # transcript: "Ah, a noble and unselfish"
            huli_jing "Ahh... a noble and unselfish question. Very well, little dumpling. I will show you. But only for a moment. One breath. One heartbeat."

            "She lifted a single clawed finger to my forehead. Pain. Light. Fire."
            "A searing jolt ripped through me. My breath caught in my throat as visions burst behind my eyes."
            "Visions exploded in my mind- A crowned figure of fangs and molten eyes standing atop a throne of bones. Villages drowned in darkness. Temples burning under a red sky."

            voice audio.hulijing_ch9_line81  # transcript: "He has awakened. The harmony"
            huli_jing "He has awakened. The harmony of Ena breaks. But the tide has not yet turned..."

            "She leaned closer, her many tails coiling behind her like stormclouds."

            voice audio.hulijing_ch9_line82  # transcript: "Dragonkin, only you and your"
            huli_jing "Dragonkin... Only you and your companions can stop him."

            "I swallowed hard, my hands still shaking. But she wasn't done."
            "Her voice dropped to a whisper that slid beneath my skin."

            voice audio.hulijing_ch9_line83  # transcript: "He will come to you."
            huli_jing "He will come to you. Soon. He will make an offer. A deal. One that promises power... vengeance... salvation. He will make it tempting. He will make it feel right."
            voice audio.hulijing_ch9_line84  # transcript: "The client, do not give"
            huli_jing "Decline it. Do NOT give him the Divine Weapon. Do NOT give him Magnus. If you want Ena to survive, decline it without hesitation."
            voice audio.hulijing_ch9_line85  # transcript: "or, except that, if you"
            huli_jing "Or Accept it... if you want to doom your world. Your choice, dumpling."
            voice audio.hulijing_ch9_line86  # transcript: "But, since you passed my"
            huli_jing "But... since you passed my test with such heart, I doubt you will choose wrong."

            hide chunghee
            show magnus underwear_serious at right_char with Dissolve(0.2)
            voice audio.magnus_ch9_line109  # transcript: "Someone's making you a deal."
            magnus "Someone's making you a deal? What kind of deal? Who is this bastard? When does this happen? What does it have to do with me?"
            hide magnus
            show chunghee underwear_neutral at right_char with Dissolve(0.2)
            chung_hee "Beware him, Dorian. Such creatures twist language like silk. They don't lie. But they do mislead. They'll offer you fairness... even justice. But beneath it, always: rot."
            dorian    "Thank you. For showing me."
            voice audio.hulijing_ch9_line87  # transcript: "You can absolutely think by"
            huli_jing "You can absolutely thank me by making the right choice, dumpling."

            "Her tail brushed my cheek like a whisper."
            hide chunghee with Dissolve(0.1)

        "Ask how Elara and the kids are doing.":

            "I remembered them. Elara."
            "Daniel. Emily. Sarah. Lucas."
            "Their laughter. Their warmth. The sound of their feet running across the wooden floors of our home in Gale."
            show dorian underwear_sad at left_char with Dissolve(0.1)
            "I felt the ache again. That terrible hollow ache I never dared to touch."

            dorian "How... how are my wife and the kids doing?"

            "The question slipped from me before I could stop it. My voice cracked."
            "The Huli Jing's smile faded. Her playful poise stilled. Her eyes, golden and ancient, turned solemn. There was a softness to her now-a reverence I hadn't seen before."
            show dorian underwear_serious at left_char with Dissolve(0.1)

            voice audio.hulijing_ch9_line88  # transcript: "Elara, that's your wife's name,"
            huli_jing "Elara. That's your wife's name, isn't it, dumpling? Daniel, the eldest. Emily, so clever. Sarah, the dreamer. Lucas, your little star."

            "She gestured with a paw, and soft golden mist coiled from her tails as they lifted and coiled like ribbons of starlight, swirling into the air."
            "They stood beneath a warm, endless sky. Smiling. Whole. Unscarred by the world."
            "Elara's arm rested around Sarah's shoulder. Daniel stood tall, hand protectively over his younger siblings. Emily clutched a bundle of flowers. Lucas was... laughing. Running in circles like always."
            "Behind them loomed a great golden gate, etched with stars and music and language I couldn't read but felt in my heart."
            "And just beyond that- The Halls of Xianlun. Realm of the noble dead. The honored. The brave. The pure."

            scene plain_white with dissolve
            show cg_family_into_light with dissolve  # PLACEHOLDER — cg_elara_xianlun
            pause 2.0
            scene yuxuan_lab_hotspring with dissolve   # PLACEHOLDER — hot spring
            show huli_jing at center_char

            voice audio.hulijing_ch9_line89  # transcript: "They well-cropain cannot touch them"
            huli_jing "They walk where pain cannot touch them now, dumpling. Brave, every one of them. They knew courage. They knew love. And that was enough."

            "A melody I couldn't name filled the air-like lullabies sung."

            voice audio.hulijing_ch9_line90  # transcript: "They rest in songdorian. They"
            huli_jing "They rest in song, Dorian. You gave them your everything. And they carried your love with them."
            voice audio.hulijing_ch9_line91  # transcript: "They want you to live"
            huli_jing "They want you to live your life. And live you shall."

            "My knees gave out. I fell."
            show dorian underwear_sad at left_char
            show niko underwear_serious at right_char
            with Dissolve(0.2)
            "Niko was there-quiet, steady-catching me before I hit the ground."

            niko "Easy, Dorian. Breathe."
            hide niko
            show yuxuan underwear_sad at right_char with Dissolve(0.2)
            yuxuan "They made it to Xianlun. That's all any of us could hope for."
            hide yuxuan
            show magnus underwear_sad at right_char with Dissolve(0.2)
            voice audio.magnus_ch9_line110  # transcript: "Shen, the great horse. Rest"
            magnus "Xianlun... The great halls. Rest in peace."
            show dorian underwear_serious at left_char with Dissolve(0.1)
            dorian "Thank you... for showing me. I needed this."
            voice audio.hulijing_ch9_line92  # transcript: "You're welcome, dumpling. And when"
            huli_jing "You're welcome, dumpling. And when your time comes... they will be the first to greet you at the gate."
            hide magnus 
            show dorian underwear_neutral at left_char
            with Dissolve(0.1)

        "Ask about your future.":

            dorian "What's waiting for me in my future?"

            "The Huli Jing's ears twitched."

            voice audio.hulijing_ch9_line93  # transcript: "Your path is a tangledumbling,"
            huli_jing "Your path is a tangle, dumpling. Woven of heart and blade... but you wish to know who walks beside you in the end, hmm?"

            "She touched my forehead. Visions bloomed."
            "Not of battle, nor glory-but moments. Shared laughter. Late-night talks. Someone bandaging my wounds."
            "A hand reaching for mine under the stars. A voice calling my name as if it was the only name they ever knew."
            "My companions. One of them. But which one? The vision blurred-never showing their face. Just the feeling. Of being loved. Truly. Without weight or duty or fear."

            voice audio.hulijing_ch9_line94  # transcript: "I will not name them,"
            huli_jing "I will not name them. But your true love... is already beside you. All that's left-is for you to see them clearly."

            "The vision faded. I blinked, disoriented."

            voice audio.chung_ch9_line70  # transcript: "Was that a prophecy or"
            chung_hee "Was that a prophecy or a romantic prank?"

            "Yuxuan blushed, refusing to look up."

            hide chunghee
            show yuxuan underwear_lying at right_char with Dissolve(0.2)
            yuxuan "T-The possibility of... me and Dorian... I-I wasn't prepared for that."

            "Magnus smirked."

            hide yuxuan
            show magnus underwear_ignore at right_char with Dissolve(0.2)
            voice audio.magnus_ch9_line111  # transcript: "Did she show you me?"
            magnus "Did she show you me? Come on, you can say it."
            hide magnus
            show niko underwear_smile at right_char with Dissolve(0.2)
            niko "Magnus, don't you have a woman?"
            hide niko
            show svante underwear_base at right_char with Dissolve(0.2)
            svante "Niko, he's been frozen for Enoch knows how long. Odds are she's dust."
            hide svante
            hide dorian
            with Dissolve(0.1)
            voice audio.hulijing_ch9_line95  # transcript: "You won't shatter like baby"
            huli_jing "You all chatter like baby sparrows. But here, Dorian, more truths for your heart-if you dare take them."
            voice audio.hulijing_ch9_line96  # transcript: "There will come a moment"
            huli_jing "There will come a moment when your future lover will be the one to rescue you. And when that moment arrives... you must trust them. Let them save you."

            "She flicked a tail, and for a heartbeat, I saw fire. Pain. Then- hands catching me before I fell."

            voice audio.hulijing_ch9_line97  # transcript: "And there is a child"
            huli_jing "And-there is a child in your life. The most important soul to you right now. There will come a time when they will need you the most... At that instance, choose your child over spending time with your love, Dorian."
            voice audio.hulijing_ch9_line98  # transcript: "Lastly, never betray your lover,"
            huli_jing "Lastly... never betray your lover. No matter how cruel the world becomes. Or how tempting it may be. Be the man they believe you are."

            "I swallowed hard. Another lover. Even hearing the words felt like betrayal. Could I even love again? Did I want to?"
            "Part of me whispered no."
            "But another part... the part that had long been silent... trembled."

            dorian    "...Thank you. For showing me."
            voice audio.hulijing_ch9_line99  # transcript: "You can thank me by"
            huli_jing "You can thank me by honoring them when the time comes. Be faithful, dumpling. With all your heart."

        "Ask about the secret to Gao's perfect Tianho flan.":
            $ A4_chunghee_affection += 1           # +1 Chung-hee affection

            show dorian underwear_normal at left_char with Dissolve(0.1)
            dorian "Okay, real question: What's the secret to Gao's flan?!"

            "Silence."
            "A long, awkward beat of silence."

            hide chunghee
            show niko underwear_ignore at right_char with Dissolve(0.2)
            niko "...Merciful Enoch."

            voice audio.hulijing_ch9_line100  # transcript: "Yeah, you mean the soundtrack?"
            huli_jing "Gao? You mean the soldier?"
            hide niko
            show yuxuan underwear_neutral at right_char with Dissolve(0.2)
            yuxuan    "Dorian means Li Gao. He's a retail worker for Cheng Industries. And yes, he was a soldier before. He makes... I mean his mom makes insanely good flan."

            "Huli Jing's tails froze. Her eyes went wide."

            hide yuxuan
            show svante underwear_angry at right_char with Dissolve(0.2)
            svante "Can you imagine being one of the only mortals in history to be granted a question from an ancient, reality-bending fox spirit-and you ask about flan?"
            hide svante
            show yuxuan underwear_lying at right_char with Dissolve(0.2)
            yuxuan "Dorian buddy, umm... I literally own the company he works in. I could've just... bought the recipe."
            voice audio.hulijing_ch9_line101  # transcript: "Oh, dumpling, I adore it!"
            huli_jing "Ohhh, dumpling! I adore it! Li Mengtia asked me about the essence of knowledge. You ask about custard."
            show dorian underwear_neutral at left_char with Dissolve(0.1)
            voice audio.hulijing_ch9_line102  # transcript: "You are an icon, you"
            huli_jing "You are an icon. You are a legend. And you are the moment."

            "She twirled midair, tails drawing shapes in the steam, and whispered."

            voice audio.hulijing_ch9_line103  # transcript: "It's salt, just a pinch."
            huli_jing "It's salt. Just a pinch. Right after pouring the custard, before it sets. It sharpens the sweet. A secret as old as war and love."

            hide yuxuan
            show chunghee underwear_happy at right_char with Dissolve(0.2)
            chung_hee "I KNEW IT! I knew it! I knew there was a mystery in that flan!"

            "Everyone turned."

            hide chunghee
            show magnus underwear_ignore at right_char with Dissolve(0.2)
            voice audio.magnus_ch9_line112  # transcript: "Well, well, well. His majesty's"
            magnus "Well well well... His Majesty's got a sweet tooth!"
            hide magnus
            show niko underwear_smile at right_char with Dissolve(0.2)
            niko "Not you too, Chung."

            "Chung-hee froze mid-celebration. His cheeks flushed a little pink. Then, in perfect imperial fashion, he straightened his spine, dusted his undergarments and tucked his arms behind his back."

            hide niko
            show chunghee underwear_base at right_char with Dissolve(0.2)
            voice audio.chung_ch9_line71  # transcript: "I was merely confirming a"
            chung_hee "...I was merely confirming a culinary hypothesis. Nothing more. Carry on. And stop calling me His Majesty."
            hide chunghee
            show magnus underwear_base at right_char with Dissolve(0.2)
            voice audio.magnus_ch9_line113  # transcript: "Oh, flat divine, fit for"
            magnus "? O Flan Divine, fit for a throne, praised by the Emperor all on his own... ?"
            hide magnus
            show chunghee underwear_angry at right_char with Dissolve(0.2)
            voice audio.chung_ch9_line72  # transcript: "Stop!"
            chung_hee "Stop."
            hide chunghee with Dissolve(0.1)


    voice audio.hulijing_ch9_line104  # transcript: "Just for you, Dragon of"
    huli_jing "Just for you, Dragon of Gale. Another gift. One that is very handy."

    "Her eyes sparkled as she leaned forward."

    voice audio.hulijing_ch9_line105  # transcript: "Choose one of these men."
    huli_jing "Choose one of these men."

    "The humid air from the hot springs clung to my skin, curling tendrils of steam around us. I could feel the heat rising not only from the water but from my own cheeks as well."
    "The Huli Jing's smile deepened as I leaned closer, my voice dropping into a low whisper, almost swallowed by the bubbling of the spring."

    jump ch9_huli_love


# =============================================================================
# SECTION 12: LABEL CH9_HULI_LOVE — Love Route Choice
# =============================================================================

label ch9_huli_love:
    menu:
        "Yuxuan.":
            $ A3_yuxuan_affection += 3             # +++ Yuxuan affection
            show dorian underwear_neutral at left_char
            show yuxuan underwear_lying at right_char 
            with Dissolve(0.1)
            "Yuxuan straightened, hopeful."

            dorian "I choose Yu."
            show yuxuan underwear_normal at right_char with Dissolve(0.1)

            "His whole face lit up like the midsummer lantern festivals in Lanliang."

            show yuxuan underwear_happy at right_char with Dissolve(0.1)
            yuxuan    "Dorian~! I knew it! I knew this was destiny! Take that, Niko!"
            hide yuxuan
            show niko underwear_ignore at right_char with Dissolve(0.2)
            niko "...What did I do?"
            hide niko with Dissolve(0.1)
            voice audio.hulijing_ch9_line106  # transcript: "Ooh, an inventor's heart, gilded"
            huli_jing "Oooh! A inventor's heart, gilded in pride and glitter."

            "She twirled in the air, one tail looping into a perfect spiral before she carved a sigil of light in midair."
            "She tapped my chest with one claw, and warmth flooded through me."
            show dorian underwear_serious at left_char with Dissolve(0.1)
            "I felt an odd tingling sensation."

        "Niko.":
            $ A1_niko_affection += 3               # +++ Niko affection

            show dorian underwear_neutral at left_char
            show niko underwear_base at right_char 
            with Dissolve(0.1)
            dorian "I choose Niko."

            show niko underwear_serious at right_char with Dissolve(0.1)
            "Niko arched an eyebrow, skeptical."

            niko "Choose me? Choose me for what, exactly?"
            show niko underwear_base at right_char with Dissolve(0.1)
            voice audio.hulijing_ch9_line107
            huli_jing "Hmm... The doctor who walks with death. The prophet of Enoch. Steady as stone, cold as snow, yet tender underneath. Delicious."
            hide niko
            show magnus underwear_base at right_char with Dissolve(0.2)
            voice audio.magnus_ch9_line114  # transcript: "O healer of mine comes"
            magnus "? Oh Healer of mine come soothe thee. Thine path is mine and yours to- ?"
            hide magnus
            show niko underwear_ignore at right_char with Dissolve(0.1)
            niko "Magnus, quiet. Besides, you got the lyrics all wrong."
            hide niko with Dissolve(0.1)

            "The Huli Jing drew a sigil in the air with a claw and touched my heart. I felt an odd tingling sensation."

        "Svante.":
            $ A2_svante_affection += 3             # +++ Svante affection

            show dorian underwear_neutral at left_char
            show svante underwear_nervous at right_char
            with Dissolve(0.2)

            dorian "I choose Svante."

            "Svante flinched at the attention, cheeks red. His hands fidgeted."

            svante    "You... You really mean that, sir-I mean, Dorian? Choose me for what?"
            voice audio.hulijing_ch9_line108  # transcript: "Aw, nice sweet dumpling! You"
            huli_jing "Awwww! My sweet dumpling! You chose the softest bun in the basket!"
            hide svante
            show chunghee underwear_base at right_char with Dissolve(0.2)
            voice audio.chung_ch9_line73  # transcript: "Sweetest, he was sent to"
            chung_hee "Sweetest? He was sent to assassinate me yesterday."
            hide chunghee
            show svante underwear_nervous at right_char with Dissolve(0.2)
            svante    "I-I beg your forgiveness once more, Your Majest-!"
            hide svante
            show chunghee underwear_base at right_char with Dissolve(0.2)
            voice audio.chung_ch9_line74  # transcript: "Savante I jest, a ruler"
            chung_hee "Svante, I jest. A ruler who cannot laugh has already lost half his kingdom. And I already accepted your apology. I do not give those lightly."
            hide chunghee
            show svante underwear_base at right_char with Dissolve(0.2)
            svante    "I... Thank you, Chung."
            hide svante with Dissolve(0.1)

            "The Huli Jing danced in the air, and with a flick of a claw, etched a glowing sigil in the steam before pressing it gently to my heart."

        "Chung-hee.":
            $ A4_chunghee_affection += 3           # +++ Chung-hee affection

            show dorian underwear_neutral at left_char
            show chunghee underwear_neutral at right_char
            with Dissolve(0.2)

            dorian "I choose Chung-hee."

            "Chung-hee's expression faltered for a moment. Just a moment."

            voice audio.chung_ch9_line75  # transcript: "honor me, Dorian."
            chung_hee "You honor me, Dorian."
            voice audio.hulijing_ch9_line109
            huli_jing "The Emperor of Kyeongjang! Oh, I didn't know you were into royalty, dumpling. A scandal! A story! And-wait, he can read our minds! Everyone-think pure thoughts!"
            show chunghee underwear_angry at right_char with Dissolve(0.1)
            voice audio.chung_ch9_line76  # transcript: "I'll pretend I didn't hear"
            chung_hee "I'll pretend I didn't hear that."
            show chunghee underwear_base at right_char with Dissolve(0.1)
            voice audio.hulijing_ch9_line110  # transcript: "Teasing your majesty just teasing"
            huli_jing "Teasing, your Majesty. Just teasing. You're a difficult one to crack."

            hide chunghee with Dissolve(0.1)
            "The Huli Jing drew a sigil in the air with a claw and touched my heart. I felt an odd tingling sensation."

        "Magnus.":
            $ A5_magnus_affection += 4             # ++++ Magnus affection

            show dorian underwear_neutral at left_char
            show magnus underwear_base at right_char
            with Dissolve(0.2)

            dorian "I choose Magnus."
            show magnus underwear_powered at right_char with Dissolve(0.1)

            "He gasped, both hands dramatically clasped over his chest."

            voice audio.magnus_ch9_line115  # transcript: "I knew it, the stars"
            magnus "I knew it! The stars were right! The harp sang to me last night!"
            hide magnus
            show niko underwear_ignore at right_char with Dissolve(0.2)
            niko "Of course it did..."
            hide niko
            show magnus underwear_base at right_char with Dissolve(0.2)
            voice audio.hulijing_ch9_line111  # transcript: "An unknown heart brightened wild."
            huli_jing "An unknown heart, bright and wild. He'll break it, you know. But he'll write you a song for every piece."
            voice audio.magnus_ch9_line116  # transcript: "Love's a fire bright in"
            magnus "? Love's a fire, bright and bold-let it burn or leave you cold~ ?"
            huli_jing "You're lucky he's charming. Now hold still."

            hide magnus with Dissolve(0.1)
            "She painted the sigil with three tails at once-effervescent and glittering-before placing it on my chest. I felt an odd tingling sensation."
    jump ch9_huli_exit


# =============================================================================
# SECTION 13: LABEL CH9_HULI_EXIT — CommonCommonCommon: Fox Farewell / FWOOMP
# =============================================================================

label ch9_huli_exit:

    huli_jing "And a promise is a promise. I shall never again haunt these springs, nor return to soak my tails. You'll never see me here again."
    huli_jing "I will be in Xianlun. With my family. Pity... I was beginning to like you."
    show magnus underwear_base at right_char with Dissolve(0.1)
    magnus "And we were starting to like you too, beloved fox!"
    magnus "Farewell to the fox with the nine shining tails... To judgment and laughter where truth always sails...~"
    huli_jing "Wow! I love it, dumpling! I'm going to miss you!"
    voice audio.hulijing_ch9_line112  # transcript: "Alas, this is for a"
    huli_jing "Alas, this is farewell. But I have one last parting gift."

    "She snapped her claws-"

    hide huli_jing with Dissolve(0.1)
    play sound audio.sfx_fwoop                 # PLACEHOLDER — FWOOMP SFX
    "FWOOMP."

    jump ch9_stuffed_fox_exit


# =============================================================================
# SECTION 14: LABEL CH9_STUFFED_FOX_EXIT — Darkness / Toy / Everyone Pops Out
# =============================================================================

label ch9_stuffed_fox_exit:

    # [COMMENT: cg_black — total darkness]
    scene black with fade                    # PLACEHOLDER — black screen
    pause 0.5

    "In a blink, the warmth vanished. Steam gone. Stones vanished. Comfort obliterated. Suddenly-squish. Pressed in. Too close. Far too close."

    dorian "What in the name of the Tetrad-?!"

    scene cg_men_trapped with dissolve
    "I was squished-stuffed, really-inside what looked like a giant toy Limbs tangled, faces mashed together, undergarments sticking uncomfortably."

    dorian "Why... why can't I move my legs-"
    yuxuan "Ahhh! Dorian~! Just you and me and-wait, wait, someone's chest is in my-"
    niko "Grr... Yuxuan. That is my chest. Kindly remove your hand."
    yuxuan "AHH! I thought it was Dorian!! Magnus, your foot-!"
    voice audio.magnus_ch9_line117  # transcript: "I'm trying, I'm trying! This"
    magnus "I'm trying! I'm trying! This is not how I imagined group bonding."
    niko "Unbelievable... Chung, stop pushing!"
    svante "Wait-I think I found a lever!"
    voice audio.chung_ch9_line78  # transcript: "That is not a lever."
    chung_hee "T-That is NOT a lever! P-Please-unhand me!"
    svante "AHH! I-I'm sorry, Your Maj-I mean, Chung!"
    dorian "Svante, for the love of the Tetrad, don't lift your arms. I can smell your armpits-"
    svante "AHH! Sorry! Oh-Enoch above, smite me now-"
    "Everyone: *struggling sounds*"

    voice audio.magnus_ch9_line118  # transcript: "A brother of steam of"
    magnus "Oh brothers of steam, of springs and of soap, Entangled in trials~"
    voice audio.chung_ch9_line79
    chung_hee "Magnus. Shut up."

    jump ch9_kids_spring


# =============================================================================
# SECTION 15: LABEL CH9_KIDS_SPRING — Kids POV / Tim / Huli Jing Gift
# =============================================================================

label ch9_kids_spring:

    # [COMMENT: bg_hot_spring — Tim and Elias in the springs, playing]
    scene yuxuan_lab_hotspring with fade           # PLACEHOLDER — hot spring kids

    show tim underwear_normal at left_char_kids
    show elias swimwear_neutral at right_char_kids 
    with Dissolve(0.2)

    voice audio.tim_ch9_line26  # transcript: "Elias, hey Elias!"
    tim "Elias! Hey Elias!"

    show elias swimwear_happy at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line30
    elias "Yes, Tim?"

    voice audio.tim_ch9_line27  # transcript: "Come here, the water's fine."
    tim "Come here! The water's fine!"
    show tim underwear_think at left_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line28  # transcript: "Given the thermal consistency of"
    tim "Given the thermal consistency of this geothermal spring and accounting for the elevation, I hypothesize that the temperature today hovers around seventy-eight degrees Celsius-perhaps just under the threshold to soft-boil an egg."
    show tim underwear_happy at left_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line29  # transcript: "We might even be able"
    tim "We might even be able to cook noodles, Elias. Just imagine-hot spring ramen! Ambient-heated broth, mineral-rich. Quite possibly delicious."

    show elias swimwear_lying at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line31  # transcript: "So we take in buttons"
    elias "Soup? We takin bath in soup?!"

    show weng bathwear at center_char with Dissolve(0.2)

    weng "It's not soup, kids. It's spring water. Full of magic. And minerals. Good for the bones and even better for the soul."

    play sound audio.sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    hide weng
    show roboto happy at center_robot with Dissolve(0.2)

    roboto "S-S-S-Springs detected. Temperature optimal. Steam density: fluffy."

    show elias swimwear_happy at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line32  # transcript: "Oh, it's so pretty! We're"
    elias "Ooh! It's so pretty! We swim together, Roboto!"
    roboto "N-N-Negative... I may be waterproof, but my sensors are not human-safe. A power surge could shock the party. I will supervise from a safe distance."
    tedda "Then it's just us! Come, Lady Elias!"

    hide roboto
    show weng bathwear at center_char with Dissolve(0.2)

    weng "Tedda, are you sure you don't want to wear swimwear?"
    hide weng
    show tedda_human at center_char with Dissolve(0.2)
    tedda "My clothes can't be removed, Miss Weng. I'm a toy, remember?"
    hide tedda_human
    show weng bathwear at center_char with Dissolve(0.2)
    weng "Oh, silly me. I forgot. Carry on, then."
    hide weng
    show tedda_human at center_char with Dissolve(0.2)
    tedda "Let's go, Lady Elias! Let's swim like noble queens in our glittery bath!"
    hide tedda_human with Dissolve(0.1)

    show elias swimwear_happy at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line33
    elias "Yey!! Let's go, Tedda! Tim, let's go!"

    show tim underwear_angry at left_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line30  # transcript: "Hey, I'm a king, I'm"
    tim "Hey! I'm a king! I'm not a queen!"

    show tim underwear_normal at left_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line31  # transcript: "So, Miss Wang told me"
    tim "So... Miss Weng told me a story once. About this very spring."

    show elias swimwear_cute at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line34  # transcript: "Ooh, what's the only?"
    elias "Ooooh. What story?"

    voice audio.tim_ch9_line32  # transcript: "A tale of the hoolie"
    tim "A tale of the Huli Jing. A legendary fox spirit said to dwell in these waters."

    show elias swimwear_cute at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line35
    elias "Hulee Jee?"

    voice audio.tim_ch9_line33  # transcript: "Hulee Jing, a fox spirit"
    tim "Huli Jing. A fox spirit who once lived in this spring! Some say she played tricks, others say she gave blessings with kind and compassionate hearts! There was a legend of a game... a test of judgment... but most adults think it's just a myth."

    show elias swimwear_happy at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line36
    elias "Ooh! Can we see them?"

    show tim underwear_think at left_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line34  # transcript: "Only those who are destined"
    tim "Only those who are destined to do great things can see them!"

    hide tedda_human
    show weng bathwear at center_char with Dissolve(0.2)

    weng "Tim, enough of your stories. That's just Tianho folklore. Only the Tetrad Li Mengtia ever claimed to see and speak with one-and that was a thousand years ago."
    weng "Now hurry up and focus on your baths. We have a ceremony later."

    show elias swimwear_neutral at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line37  # transcript: "This one, what do you"
    elias "Miss Weng, what we do later?"

    weng "We'll watch a special program and release lanterns into the sky, Elias dear."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    hide weng
    show roboto happy at center_robot with Dissolve(0.2)

    roboto "Unfortunately, t-t-the lantern releasing is only for adults."

    hide roboto
    show weng bathwear at center_char with Dissolve(0.2)

    weng "But don't worry, little ones. There will be plenty of delicious food afterward."

    hide weng
    show roboto happy at center_robot with Dissolve(0.2)

    roboto "Based on observed preparations from the Hinami delegation, there will also be a d-d-dragon presentation at the memorial grounds."

    show tim underwear_happy at left_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line35  # transcript: "No way! A dragon presentation?"
    tim "No way! A DRAGON presentation?!"

    roboto "H-H-However, reports indicate the dragon will be a hologram. Please consume this information with a figurative grain of sodium chloride."

    hide roboto
    show tedda_human at center_char with Dissolve(0.2)
    tedda "Wow! Did you hear that, Lady Elias?"
    voice audio.tim_ch9_line36  # transcript: "And Miss Wang broke crayons"
    tim "And Miss Weng brought crayons for us! We get to color while we wait!"

    show elias swimwear_happy at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line38  # transcript: "Yay! Cold time!"
    elias "Yay! Color time!"

    tedda "I already have so many ideas for what we can draw, Lady Elias!"

    play sound audio.sfx_back
    "-BACK CRACK-"

    hide roboto
    hide tedda_human
    show weng bathwear at center_char with Dissolve(0.2)

    weng "My back... If you'll excuse me, I'll have a cup of calming jasmine tea."

    hide weng
    show roboto happy at center_robot with Dissolve(0.2)

    roboto "M-M-Miss Weng, I highly suggest you don't drink tea while taking a bath in the springs."

    hide roboto
    show weng bathwear at center_char with Dissolve(0.2)

    show elias swimwear_neutral at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line39  # transcript: "Hmm... Daddy told me to"
    elias "Hmm... Daddy told me to always believe in legends."

    show tim underwear_happy at left_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line37  # transcript: "Oh, Mr. Dorian, he's so"
    tim "Oh, Mister Dorian? He's so cool! He fought a Hundun in Tianho with Mister Chung, remember?"

    show tim underwear_shy at left_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line38  # transcript: "Oh, I forgot, you weren't"
    tim "Oh I forgot. You weren't there. But he was so cool!"

    show elias swimwear_happy at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line40
    elias "Daddy's so cool! He's big and strong and wears underpants with dragons on them! He fight big monster!"

    show tim underwear_normal at left_char_kids with Dissolve(0.1)
    tim "Hey, Elias... Watch this."

    scene cg_tim_powers with Dissolve(0.6)
    "Tim extended his hands. A tiny glowing figure, like a dragon made of mist, forms between his palms, wriggling and coiling like it's alive."
    tedda "It's a dragon!"

    tim "A basic projection, stabilized by willpower and concentration. This one is better!"

    voice audio.elias_ch9_line41
    elias "WOW! How you do dat, Tim? Magic cwayons?"

    tim "Shhh. Don't tell Miss Weng! It's a secret ability of mine that I can do! You promise?"

    voice audio.elias_ch9_line42  # transcript: "Umm... Okay, I promise. You"
    elias "Um... okay. I promise. You have powers wike Daddy!"

    tim "I'm... not entirely sure how I got them. They're just... there. That's why I want to ask Mister Chung if-"
    scene yuxuan_lab_hotspring with Dissolve(0.5)
    show elias swimwear_happy at right_char_kids 
    show tim underwear_shy at left_char_kids 
    show tedda_human at center_char
    with Dissolve(0.1)
    tedda "Wait... something moved over there! The water moved!"
    voice audio.tim_ch9_line39  # transcript: "Wait, do you see what"
    tim "Wait... D-Do you see what I'm seeing?"
    huli_jing "..."

    show elias swimwear_cute at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line43  # transcript: "Oh, that's a cute fox!"
    elias "Where? Oh! That's a cute fox! With fow tails!"

    show tim underwear_think at left_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line40
    tim "Four? No! It's nine, Elias! One, two, three, four, five, six, seven, eight... nine! That's a real Huli Jing!"

    show elias swimwear_happy at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line44  # transcript: "It's so cute! Come here,"
    elias "It's so cute! Come here little foxie!"

    voice audio.hulijing_ch9_line113  # transcript: "Hello little ones, what are"
    huli_jing "Hello little ones! What are your names?"

    show tim underwear_happy at left_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line41  # transcript: "My name is Tim. I'm"
    tim "My name is Tim! I'm the brains of the group! I'm also the leader!"

    show elias swimwear_happy at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line45  # transcript: "And I'm a Ryan's Hegel!"
    elias "And I'm Elias! Hewwo!"

    tedda "Kids, are you talking to someone? I don't see anything... Should we tell Miss Weng? What if it's dangerous?"
    hide tedda_human
    show weng bathwear at center_char with Dissolve(0.1)
    weng "Hey, kids! Who are you talking to?"
    voice audio.hulijing_ch9_line114  # transcript: "Here's a little gift for"
    huli_jing "Here's a little gift for you... Goodbye little dumplings..."

    show tim underwear_sad at left_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line42  # transcript: "Wait, where did they go?"
    tim "Wait... where did it go? Aww, it ran away!"

    hide weng
    show tedda_human at center_char with Dissolve(0.2)
    tedda "Look! Lady Elias! Look at the water! Pretty colors!"

    show elias swimwear_cute at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line46
    elias "Red and yellow and green and pink! It's so pretty!"

    show tim underwear_think at left_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line43  # transcript: "Chromatic oric distortion, a spontaneous"
    tim "Chromatic auric distortion. A spontaneous display of spiritual color energy. Fascinating..."

    show elias swimwear_neutral at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line47  # transcript: "Do you think it's from"
    elias "Do ya think it's from the fox?"

    show tim underwear_shy at left_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line44  # transcript: "I don't know... maybe?"
    tim "I... don't know. Maybe?"

    scene cg_elias_release with shock_cut
    tedda "Lady Elias! Look! There's something floating over there-It's a FOX STUFFED TOY!"
    voice audio.elias_ch9_line48  # transcript: "Oh, can I have it?"
    elias "Oooooh!! Can I have it? Can I have it?!"
    voice audio.tim_ch9_line45  # transcript: "The hooly jang said it"
    tim "The Huli Jing said it was a gift. So we should open it! Open it, Elias!"
    tedda "Or!! Maybe you can give it a shake first! Maybe there's magic inside!"

    jump ch9_fox_toy

# =============================================================================
# SECTION 16: LABEL CH9_FOX_TOY — Elias Opens Fox Toy
# =============================================================================

label ch9_fox_toy:
    menu:
        "Shwake it!":

            voice audio.elias_ch9_line49  # transcript: "Oh, okay, how sweet it!"
            elias "Ooh! Okay! I'll shwake it!"
            tedda "With emotion, Lady Elias! Let's goooo!!"

            voice audio.tim_ch9_line46  # transcript: "Are you sure shaking it"
            tim "Are... you sure shaking it is the best course of action?"

            voice audio.elias_ch9_line50
            elias "Shwake! Shwake!"
            "AHHHHH!!"

            voice audio.tim_ch9_line47  # transcript: "Huh? What was that?"
            tim "Huh? What was that?"
            tedda "That must be coming from inside, Lady Elias! Open it!"
            
            play sound audio.sfx_pop
            "-POP-"

        "Open it!":
            voice audio.elias_ch9_line51
            elias "Let's open it first, Tedda!"

            voice audio.tim_ch9_line48  # transcript: "Let's count to three first."
            tim "Let's count to three first!"
            tedda "On the count of three open it~ One! Two!"

            play sound audio.sfx_pop
            "-POP-"

    jump ch9_spring_end


# =============================================================================
# SECTION 17: LABEL CH9_SPRING_END — Untangled / Bathing / Hilltop Prep
# =============================================================================

label ch9_spring_end:

    scene yuxuan_lab_hotspring with flash              # PLACEHOLDER — hot spring pop

    "I tumbled out."
    "Face-first. Right into someone's thigh."
    "Everything reeked of lavender, steam, and shame."
    "We were all still in our undergarments, soaked, tangled like a bundle of wet spaghetti, sprawled out in the middle of the hot spring."

    show chunghee underwear_neutral at left_char
    show svante underwear_base at center_char
    show magnus underwear_base at right_char 
    with Dissolve(0.2)

    voice audio.chung_ch9_line80  # transcript: "This is completely indecent. I"
    chung_hee "This is completely indecent. I swear someone's cheek was on my-wait. Never mind. I don't want to know."
    svante    "I'm... I'm upside down. I can taste someone's foot."
    voice audio.magnus_ch9_line119  # transcript: "I think my entire spine"
    magnus "I think my entire spine cracked. Also, someone's sitting on my hair."

    hide svante
    show niko underwear_serious at center_char with Dissolve(0.2)

    niko "I apologize. I'll move now."

    scene cg_elias_release_surprised with shock_cut 
    voice audio.elias_ch9_line52  # transcript: "Daddy, while you're in the"
    elias "DAAADDDYYY!! Why are you in the foxie?!"

    "Above us, I saw Weng, holding a teacup in her swimwear. She squinted at the mess."

    weng "By the stars, Master Yuxuan? What happened to all of you?"

    yuxuan "W-We did it, Miss Weng! The spring won't smell like fermented feet stew!"

    weng "W-What?"

    dorian "J-Just ignore him, Miss Weng."

    yuxuan "It's a long story involving a fox, judges and... moral philosophy."
    scene yuxuan_lab_hotspring with dissolve
    
    show dorian underwear_neutral at left_char
    show elias swimwear_happy at right_char_kids 
    with Dissolve(0.2)
    voice audio.elias_ch9_line53  # transcript: "Daddy, you're silly. I'll help"
    elias "Daddy, you look siwwy! I'll help you."

    "Tiny hands grabbed mine. I looked up to see Elias, dripping and smiling."

    show tedda_human at center_char with Dissolve(0.2)
    tedda "That looks uncomfortable! I'll help you Lady Elias!"
    hide elias
    show weng bathwear at right_flip with Dissolve(0.2)
    weng "Do you need help? Roboto, hold this teacup."

    hide weng
    show roboto happy at right_robot with Dissolve(0.2)

    roboto "T-T-Transferring... hot liquid. Grip calibrated to teacup fragility."

    hide tedda_human
    show tim underwear_think at center_char_kids with Dissolve(0.2)
    voice audio.tim_ch9_line49  # transcript: "That was amazing! I deduced"
    tim "That was amazing. I deduce that the fox must've sealed them inside an extradimensional plush construct-"

    hide roboto
    show chunghee underwear_neutral at right_char with Dissolve(0.2)
    voice audio.chung_ch9_line81  # transcript: "Tim, please not now."
    chung_hee "Tim. Please. Not now."

    show tim underwear_shy at center_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line50  # transcript: "Sorry, Mr. Chung. Do you"
    tim "S-Sorry, Mister Chung! Do you need some help?"

    scene yuxuan_lab_hotspring with Dissolve(0.7)
    "One by one, we were untangled-wet, dazed, and half-dressed, but alive. Tedda and Elias offered towels."
    "Roboto beeped encouragingly. Magnus looked like he needed ten massages."
    "I groaned, dragging myself upright. My hair clung to my face. Water trickled down my back."

    show roboto happy at center_robot with Dissolve(0.2)
    roboto "S-S-Spatial anomaly resolved. Group integrity: 100%%. Modesty: 4.143%%."
    hide roboto
    show dorian underwear_neutral at left_char
    show elias swimwear_neutral at right_char_kids
    with Dissolve(0.2)
    voice audio.elias_ch9_line54
    elias "You okay now, Daddy?"

    show dorian underwear_smile at left_char with Dissolve(0.1)

    "I looked at him and grinned, still catching my breath."

    dorian "Yeah, buddy. I'm okay now."

    scene yuxuan_lab_hotspring with Dissolve(0.7)
    "After we finished bathing, I gently scrubbed Elias for a while, until Tedda took over with gleeful determination, humming a tune while she made sure every inch of Elias was squeaky clean."
    "Weng, groaning a little, called out for help with Tim-her back giving out after all the excitement. I didn't know she had lots of back problems."
    "Yuxuan tried to step in, but quickly realized toddler bath time was not his calling. I ended up taking over, gently scrubbing Tim while he lectured me about soap composition."
    show dorian underwear_neutral at left_char
    show tim underwear_think at right_char_kids
    with Dissolve(0.2)
    voice audio.tim_ch9_line51  # transcript: "Interesting. I appear to be"
    tim "Interesting. I appear to be cleaner than the average imperial scroll... but less organized."
    voice audio.tim_ch9_line52  # transcript: "This blend lacks proper alkali"
    tim "This blend lacks proper alkali balance, Mister Dorian. My skin pH will be most offended. Roboto told me that."
    dorian "Tim, I wasn't able to understand half of what you just said. Now, raise your arm."

    scene yuxuan_lab_hotspring with Dissolve(0.4)
    "Once we were all dry and dressed, we changed into our Tianho ceremonial attire-layers of silk and charm, embroidered with celestial patterns."
    "Yuxuan, beaming with excitement, led us to the special place he had mentioned."
    "We took an elevator hidden deep inside the library, and when the doors opened, we emerged onto a quiet hilltop."

    jump ch9_hilltop

# =============================================================================
# SECTION 18: LABEL CH9_HILLTOP — Hill / Ceremony / Aoi / Lanterns Setup
# =============================================================================

label ch9_hilltop:

    # [COMMENT: bg_hill_memorial_night — hilltop, indigo sky, Tianho Memorial glowing below]
    scene bg_tianho_deng_night with fade      # PLACEHOLDER — hill overlooking memorial
    stop music fadeout 2.0
    # play music ost_ch9_ceremony fadein 2.0      # PLACEHOLDER — ceremony theme
    # play audio amb_hilltop_night loop fadein 1.5 # PLACEHOLDER — hilltop night ambient

    "The warm breeze rolled over the hill as we all stood beneath the deepening indigo sky. "
    "The last rays of sunlight clung to the clouds like strands of gold silk, while the first stars blinked to life-gentle pearls scattered across a velvet sky."
    scene bg_tianho_deng_blossom with dissolve
    "From afar, the Tianho Memorial shimmered in the twilight, glowing faintly."
    "Elias and Tim were already running in small circles around the hill, chasing each other in their ceremonial robes."

    show elias ceremonial_happy at left_char_kids
    show tim ceremonial_happy at right_char_kids
    with Dissolve(0.2)

    voice audio.elias_ch9_line55  # transcript: "You can catch me for"
    elias "You can't catch me, Professor Tim!"
    voice audio.tim_ch9_line53  # transcript: "Incorrect, my student. My calculation"
    tim "Incorrect, my student. My calculations suggest you have a 32.8%% chance of tripping on your hem in the next five seconds."
    voice audio.elias_ch9_line56
    elias "Wha-AHH!"

    hide elias
    hide tim
    with Dissolve(0.1)

    "Elias' foot caught on the edge of the robe, causing them to tumble onto the floor, giggling uncontrollably."
    "Weng was laying out a neat spread of food on a long silk blanket, adjusting each dish with practiced hands-though every so often, she winced and rubbed her lower back."

    show weng ceremonial at right_flip 
    show dorian ceremonial_neutral at left_char 
    with Dissolve(0.2)

    weng "Kids, stop running around like little spirits. You're in ceremonial outfits. You'll tear the fabric and then what?"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    show roboto happy at center_robot with Dissolve(0.2)

    roboto "B-b-bento arrangement: c-c-c-complete. Humidity: 47%%. Aesthetic symmetry: 93.44%%... adjusting for toddler chaos."

    hide weng
    show tedda_human at right_char with Dissolve(0.2)
    tedda "Ooh! Look how cute these rice cakes are! They look like smiling bunnies!"

    hide roboto
    hide tedda_human
    show yuxuan ceremonial_happy at right_char with Dissolve(0.2)

    "Yuxuan waved us over from the far side of the hill, dressed in his expensive looking golden ceremonial attire."

    yuxuan "Dorian! Over here, come on!"
    yuxuan "This is the place I wanted all of you to see. A hill above history. The calm before reverence."

    "We all gathered at the rise. The view was breathtaking. The Tianho Memorial stood distant yet dominant, a pale silhouette bathed in the twilight's soft glow."

    "Magnus stood quietly to one side, his arms crossed, expression unreadable. He stared out at the fading horizon."
    hide yuxuan
    show magnus ceremonial at right_char with Dissolve(0.2)
    voice audio.magnus_ch9_line120
    magnus "It's a beautiful view... The kind that doesn't ask for words. Makes you feel small. But not in a bad way. Small like a star in a sky of stories."
    show svante ceremonial_happy at center_char with Dissolve(0.2)
    svante "Hard to believe that yesterday we were fighting right there."
    hide magnus
    show niko ceremonial_smile at right_char with Dissolve(0.2)
    niko "It was all just yesterday. A siege, bombs falling like fire. Now we're here."
    hide svante
    show chunghee ceremonial_default at center_char with Dissolve(0.2)
    voice audio.chung_ch9_line82  # transcript: "Indeed, to think King Gustav"
    chung_hee "Indeed. To think King Gustav sent an entire battalion to destroy what he feared. I did not expect to survive the day. And yet-"
    voice audio.chung_ch9_line83  # transcript: "All of you saved me."
    chung_hee "All of you saved me. Thank you."

    "I scanned the land surrounding the Tianho Memorial. There was no trace of what had happened. No debris, no craters, no bloodstains."
    "Just pristine grass, untouched stone, and soft lanterns beginning to glow in preparation for the evening's rites."
    show dorian ceremonial_normal at left_char with Dissolve(0.1)
    dorian "They did well. There's not a single trace of the bombs."
    show dorian ceremonial_neutral at left_char with Dissolve(0.1)

    hide chunghee 
    show svante ceremonial_sad at center_char with Dissolve(0.2)
    svante "Or my brothers and sisters... I can't believe so many of us died yesterday."
    hide niko 
    show yuxuan ceremonial_neutral at right_char with Dissolve(0.2)
    yuxuan "They called in all the best Earth Channelers from across the Empire. Every stone replaced, every crack healed."

    hide svante
    show roboto happy at center_robot with Dissolve(0.2)

    roboto "For m-m-m-more information, even the Paladins from Gale lent their hands. According to my database, they all w-w-w-worked to make this moment possible."

    play sound audio.sfx_back
    "-BACK CRACK-"

    hide yuxuan
    show weng ceremonial at right_flip with Dissolve(0.2)

    weng "Tetrad above... Should've called in a back healer too. These knees weren't built for bending this much."
    hide roboto
    show niko ceremonial_base at center_char with Dissolve(0.2)
    niko "Miss Weng, do you want me to grab a chair?"
    weng "Yes, please. Maybe we could use a table instead of a mat."

    hide weng
    show tedda_human at right_char with Dissolve(0.2)
    tedda "On it, Miss Weng! Spare table coming in hot!"

    scene bg_tianho_deng_blossom with Dissolve(0.5)
    "We all pitched in. Magnus levitated the spare table over with a grunt of wind magic. Svante rolled out fresh cushions."
    "Even Roboto carefully laid out ceramic cups and bundles of incense, his mechanical fingers trembling slightly with effort."
    "The breeze picked up, carrying with it the scent of steamed rice, plum wine, and jasmine."
    "The horizon began to darken into cobalt and violet, and distant bells rang faintly across the hills. Lanterns along the path to the memorial flickered to life one by one."

    show yuxuan ceremonial_neutral at center_char with Dissolve(0.2)
    yuxuan "It's starting! Everyone, grab a seat."
    hide yuxuan with Dissolve(0.1)
    "All at once, the soft hum of conversation quieted."

    show elias ceremonial_happy at right_char_kids
    show tim ceremonial_happy at left_char_kids
    with Dissolve(0.2)
    voice audio.tim_ch9_line54  # transcript: "Elias, come sit with me."
    tim "Elias, come sit with me!"
    voice audio.elias_ch9_line57
    elias "Coming! Daddy, sit with us!"
    
    hide tim
    show dorian ceremonial_neutral at left_char
    show elias ceremonial_neutral at right_char_kids
    with Dissolve(0.2)

    "I smiled, lowering myself beside them as Elias eagerly curled into my side, his tiny fingers finding mine."
    "His hair still smelled faintly of lavender from the hot spring. A rare, rare calmness washed over me as I rested my arm around him."
    show elias ceremonial_happy at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line58
    elias "Daddy look! Miss Weng gave us cwayons!"
    show dorian ceremonial_smile at left_char with Dissolve(0.1)
    dorian "That's nice, Elias."

    scene bg_tianho_deng_blossom with Dissolve(0.5)
    "Then the lights dimmed."
    "The entire sky above the Tianho Memorial shimmered-and from the center of the clearing, a pulse of blue light burst upward."

    scene cg_aoi_singing with fade
    "The hill trembled softly as sound and vision merged. Water began to rise upward in brilliant strands of glowing liquid. The streams coiled and danced, forming an enormous spectral image."
    "A woman stepped into the projection. Her indigo kimono trailed behind her like flowing waves."

    svante "Lady Aoi..."

    "A gasp left my lips."
    "She stood alone in the image, graceful and dignified, as if she were standing on the ocean's surface itself."
    "The holographic sea churned around her feet, and from the depths behind her, a massive, shimmering shape began to rise."
    scene black with Dissolve(0.5)
    $ renpy.movie_cutscene("images/aoi.webm")

    scene bg_tianho_deng_blossom with Dissolve(0.5)

    "As the last haunting note of the song faded into the wind, silence settled over the hill like a soft shroud."
    "None of us moved for several long seconds-no one dared disturb the weight of what we had just witnessed."
    "I turned, instinctively. Svante, normally so composed, had tears glistening at the corners of his eyes."
    "Niko sat motionless; fists clenched tightly in his lap. Chung-hee stared ahead, jaw set, his expression regal-but his breathing had slowed, as if to anchor himself."
    "Yuxuan looked at me. His gaze met mine-quiet, knowing."
    "Even Elias and Tim were silent, their wide eyes fixed on the heavens above. Weng was busy wiping tears from her eyes."
    "Magnus let out a breath."
    
    show magnus ceremonial at right_char 
    show roboto happy at center_robot
    show dorian ceremonial_neutral at left_char 
    with Dissolve(0.2)
    voice audio.magnus_ch9_line121  # transcript: "Amazing. I could give it"
    magnus "Amazing. I could give it a go too. A little aria of my own-"

    roboto "W-W-Would you like some tea to calm you down, Sir Magnus?"
    voice audio.magnus_ch9_line122  # transcript: "I suppose that's a no."
    magnus "...I suppose that's a no."

    "Then, as the water projection calmed into a mirror-like stillness once more, Lady Aoi reappeared-her image clear, standing tall at the center of the great pool of light."
    
    scene cg_aoi_singing with fade
    voice audio.aoi_ch9_line44  # transcript: "Tonight beneath these stars and"
    aoi "Tonight, beneath these stars and above these honored hills, we gather not as divided nations, but as a shared people-united by memory, by loss, and by hope."
    voice audio.aoi_ch9_line45  # transcript: "We remember the tragedy of"
    aoi "We remember the Tragedy of Tianho. A day not written in ink, but seared into our hearts."
    voice audio.aoi_ch9_line46  # transcript: "A thousand lives, fathers, mothers,"
    aoi "A thousand lives-fathers, mothers, children, heroes-lost to the fire, to the fear, to the fury. The ground may have healed, but their names live on in us."
    voice audio.aoi_ch9_line47  # transcript: "In every breath we take,"
    aoi "In every breath we take, in every song we sing, and in every vow we swear."
    voice audio.aoi_ch9_line48  # transcript: "We remember their courage. We"
    aoi "We remember their courage. We honor their sacrifice. And in their memory, we promise: never again."

    voice audio.aoi_ch9_line49  # transcript: "We are graced by the"
    aoi "We are graced by the presence of those who lead our world with dignity and strength."
    aoi "His Majesty, King Tatsuya Fujiwara of Hinami, whose wisdom and compassion have lit a path of healing for his people."
    voice audio.aoi_ch9_line50  # transcript: "King Gustav Nordstrom of Moll,"
    aoi "King Gustav Nordstrom of Mjoll, whose fierce devotion to justice and peace remains unwavering even in times of grief."
    voice audio.aoi_ch9_line51  # transcript: "and her radiance, Empress Olympia"
    aoi "And Her Radiance, Empress Olympia Wyndham of Gale, who continues to lead with elegance, fortitude, and an unshakable will."
    voice audio.aoi_ch9_line52  # transcript: "to all rulers and leaders"
    aoi "To all rulers and leaders present-thank you for your presence, your compassion, and your courage to remember."
    voice audio.aoi_ch9_line53  # transcript: "This ceremony is not just"
    aoi "This ceremony is not just for mourning. It is for resolve. That we-no matter the distance between us-will never forget."

    scene bg_tianho_deng_blossom with Dissolve(0.5)
    "The light dimmed once again. We sat in reverence."

    # play sound sfx_cheng_jingle                 # PLACEHOLDER — Cheng jingle SFX

    door_voice "And tonight's ceremony has been proudly brought to you by Cheng Industries. Here at Cheng's... we bring change."

    "-Here at Cheng's, we bring change...  -"
    # TODO: play or overlap in unison
    voice audio.magnus_ch9_line123
    magnus "Here at Cheng's, we bring change..."
    tedda "Here at Cheng's, we bring change..."
    voice audio.tim_ch9_line55  # transcript: "Here at Changs, we bring"
    tim "Here at Cheng's, we bring change..."
    voice audio.elias_ch9_line59
    elias "*hums off tune*"

    show yuxuan ceremonial_happy at center_char 
    show dorian ceremonial_neutral at left_char 
    show niko ceremonial_base at right_char
    with Dissolve(0.2)
    "Yuxuan tried and failed to hide his smile."

    yuxuan "We absolutely smashed the marketing. Me and my friends at the Zhong Lotus Promenade once-"
    show niko ceremonial_meditate at right_char with Dissolve(0.1)
    niko "Tsk. Typical."

    hide yuxuan
    show chunghee ceremonial_default at center_char with Dissolve(0.2)
    "Chung-hee leaned toward me, brows arched."

    voice audio.chung_ch9_line84  # transcript: "Can I ask what the"
    chung_hee "Can I ask what the sound was?"   
    show niko ceremonial_base at right_char with Dissolve(0.1)
    dorian    "It's a... commercial jingle. For Cheng Industries. Yuxuan's company."

    scene bg_tianho_deng_blossom with Dissolve(0.5)
    "Despite the interruption, the ceremony below continued, unbothered by the distant chorus of the people around me."
    scene bg_tianho_fanrong_square with Dissolve(0.5)
    "The ceremony continued from afar, the glow of the memorial casting long, gentle light over the gathering below."
    "In the next phase, testimonies were shared-fragments of lives once lived, spoken aloud by their loved ones."
    "Some spoke of a baker who had just opened her first shop, her dreams rising like dough in the early morning sun."
    scene bg_tianho_xiangli_stalls with Dissolve(0.5)
    "Others remembered a teacher who stayed behind to guide frightened children to safety, his final words reassuring."
    "One woman recalled her twin sons, musicians who died with their instruments in hand, playing even as the ground crumbled."
    scene bg_tianho_deng_blossom with Dissolve(0.5)
    "We listened in stillness. While the children got bored and carried on coloring. And then came the Lantern Release."

    show yuxuan ceremonial_happy at center_char 
    show weng ceremonial at right_flip 
    show dorian ceremonial_neutral at left_char
    with Dissolve(0.2)
    yuxuan "Miss Weng, the lanterns please!"

    "Weng stood, her hands carrying a lacquered box. She opened it gently and revealed lanterns, folded and decorated in the traditional style of Tianho, each one tied with a crimson ribbon."

    show yuxuan ceremonial_normal at center_char with Dissolve(0.1)
    weng "Here it is, Master Yuxuan."

    yuxuan "One for each of us. The Prosperity Dragon will carry our prayers to the ones we've lost."
    weng "You may write a message. A memory. A prayer. You can draw something if words are hard. Or add a token-something small. Something that meant something to you... or to them."
    
    hide weng 
    show niko ceremonial_base at right_char with Dissolve(0.2)
    niko "Understood. Thank you."

    hide niko
    show svante ceremonial_base at right_char with Dissolve(0.2)
    svante "Anything, huh..."
    yuxuan "Now. I know we all have someone to remember. Take your time. Go where you need. Be alone if you must. Speak quietly to the ones who can no longer answer."

    scene bg_tianho_deng_blossom with Dissolve(0.3)   
    "We all nodded."
    "And then-without another word-we slowly began to scatter. Lanterns in hand."

    jump ch9_lantern_kids


# =============================================================================
# SECTION 19: LABEL CH9_LANTERN_KIDS — Elias Launches Lantern
# =============================================================================

label ch9_lantern_kids:

    # play music ost_ch9_lanterns fadein 2.0      # PLACEHOLDER — lantern release theme

    show dorian ceremonial_neutral at left_char with Dissolve(0.2)

    "I walked away from the others, lantern in hand, toward a more remote edge of the hill where the moonlight draped the grass like silver thread."
    "I wanted the moment to be quiet. Private. The wind was gentle here, and the stars looked like they were listening."
    "I knelt down beside a smooth stone and studied the blank canvas of the lantern."
    show dorian ceremonial_sad at left_char with Dissolve(0.2)
    "Elara. Daniel. Emily. Sarah. Lucas."
    "It was only yesterday that I stood at their graves again, after five long years."
    "It still didn't feel real. As if time had stretched and folded itself in strange ways, and grief had learned to hide in the folds."
    show dorian ceremonial_serious at left_char with Dissolve(0.2)

    "I paused."
    "Would a message be too much? Too little? Would it even reach them?"
    "The pen felt clinical. Cold. It didn't match the weight of what I needed to say."
    "I reached for my satchel, fingers brushing past brushes and ink stones, when I heard it-"
    show dorian ceremonial_neutral at left_char with Dissolve(0.2)
    "There was a rustling behind me."
    "I turned slowly."
    "Behind me, moving in a suspicious little group like a squad of overly curious ducklings, were Elias, Tim, Tedda, and Roboto."

    show dorian ceremonial_normal at left_char
    show elias ceremonial_cute at right_char_kids
    show tim ceremonial_think at center_char_kids
    with Dissolve(0.2)
    dorian "What are all of you doing?"

    show dorian ceremonial_neutral at left_char with Dissolve(0.1)
    "Elias immediately perked up like I'd just invited him to a picnic."

    voice audio.elias_ch9_line60
    elias "We want to help, daddy!"
    voice audio.tim_ch9_line56  # transcript: "Affirmative Sardorian, we've elected to"
    tim "Affirmative, sir Dorian! We've elected to supervise your creative process."
    hide tim
    show tedda_human at center_char with Dissolve(0.2)
    tedda "I brought glitter! And googley eyes!"

    hide elias
    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX
    show roboto happy at right_robot with Dissolve(0.2)
    roboto "O-O-OObservation mode: Active. Sentimental ritual detected. Emotional resonance: 73.3%%."

    hide tedda_human
    show tim ceremonial_think at center_char_kids with Dissolve(0.2)
    voice audio.tim_ch9_line57  # transcript: "Miss Wang hurt her back,"
    tim "Miss Weng hurt her back setting up her lantern and said she's skipping the event. So I took command and assembled the child unit!"
    roboto "M-M-Master Yuxuan said he preferred to be alone. Emotional spike detected. Possible mourning protocol initiated."
    hide roboto
    hide tim
    show elias ceremonial_happy at right_char_kids
    show tedda_human at center_char 
    with Dissolve(0.2)
    voice audio.elias_ch9_line61
    elias "It's not mourning, Roboto! Siwwy Roboto! It's night time!"
    tedda "I'm with Lady Elias!"

    "I sighed and scooted over."

    dorian "Fine. But be careful. And no glitter."
    show elias ceremonial_sad at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line62
    elias "Daddy? No gwitter?"
    show elias ceremonial_neutral at right_char_kids 
    show dorian ceremonial_normal at left_char
    with Dissolve(0.1)

    "As I launched into a brief explanation of paper textures and ink flow with Tim-who, to his credit, had real thoughts about paper grain-Roboto began calibrating wind speed and \"optimal lantern-lift trajectory.\""
    "Whatever that meant."
    "I didn't notice Elias had quietly dipped a brush into the ink. His tiny hands were already scribbling furiously across the side of my lantern."

    show dorian ceremonial_neutral at left_char with Dissolve(0.1)
    tedda "Oh my! Lady Elias! Is that me?"
    show elias ceremonial_happy at right_char_kids with Dissolve(0.1)

    voice audio.elias_ch9_line63  # transcript: "Yeah, I wrote your name!"
    elias "Yup!! I wrote your name! Look!"
    "Elias, with the confidence of a master scribe, turned the lantern around to show us. In big, messy letters, it read: \"teDuH\""

    dorian "Elias... you're supposed to write names of the dead. Not the living."
    dorian "And also... that's not how you spell Tedda's name."
    hide tedda_human
    show tim ceremonial_think at center_char_kids with Dissolve(0.2)
    voice audio.tim_ch9_line58  # transcript: "Yeah, Elias, it's Tether. T-E-D-D-A."
    tim "Yeah, Elias! It's Tedda! T-E-D-D-A! Tedda! Not TeDUH!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    hide tim
    show roboto happy at center_robot with Dissolve(0.2)

    roboto "L-L-Literacy deviation detected. Spelling accuracy: 37%%. Suggest enrolling Elias in supplementary language modules. Possibly... kindergarten."
    voice audio.elias_ch9_line64
    elias "Kinnygarden?"

    play audio audio.sfx_wind
    "Before I could even confiscate the lantern-WHOOSH."
    "A gust of wind lifted the lantern right out of his tiny hands."
    "We all turned as it wobbled into the air-floating awkwardly, proudly, like a crooked duck with a mission."

    show elias ceremonial_sad at right_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line65
    elias "W-Wait!! Nooo!! I didn't mean to let go yet!"
    hide roboto 
    hide elias
    show tedda_human at center_char 
    show tim ceremonial_think at right_char_kids
    with Dissolve(0.2)
    tedda "Oh no! My name's flying away!!"
    voice audio.tim_ch9_line59  # transcript: "Correction, a barely legible approximation"
    tim "Correction: a barely legible approximation of your name is flying away."

    hide tedda_human
    show roboto happy at center_robot with Dissolve(0.2)
    play sound sfx_roboto_beep              
    roboto "L-Lantern has launched. Contents: ['teDuH']. Probability of proper sentiment delivery: 3.6%%. Ascension trajectory: marginally passable."

    hide roboto
    hide tim
    with Dissolve(0.1)
    "I just... stared up at the sky. Elias reached out and grabbed my hand, his grip small and warm."

    show elias ceremonial_neutral at right_char_kids 
    with Dissolve(0.2)
    voice audio.elias_ch9_line66  # transcript: "Solid daddy, it was pretty"
    elias "Sowwy, Daddy. It was pretty though."
    dorian "It was... something. Don't worry, buddy."

    show elias ceremonial_happy at right_char_kids with Dissolve(0.1)
    "We watched it vanish into the stars-an accidental, misspelled tribute, lovingly launched by sticky little fingers."

    voice audio.elias_ch9_line67  # transcript: "I love you daddy!"
    elias "I love you, daddy."
    show dorian ceremonial_smile at left_char with Dissolve(0.1)
    voice audio.dorian_ch9_line9  # transcript: "Love you too, Alise. No."
    dorian "I love you too, Elias."
    show dorian ceremonial_neutral at left_char with Dissolve(0.1)

    hide elias
    show weng ceremonial at right_flip 
    show tim ceremonial_shy at center_char_kids
    with Dissolve(0.2)
    weng "Tim, Elias! I can see the glitter from here!"
    voice audio.tim_ch9_line60  # transcript: "Retreat! We've been spotted!"
    tim "Hahaha! Retreat! We've been spotted!"
    weng "Come here! Don't disturb the adults! Let's eat!"
    hide tim
    hide weng
    show tedda_human at right_char 
    show elias ceremonial_neutral at center_char_kids
    with Dissolve(0.2)
    tedda "Lady Elias, we must go! Miss Weng is summoning us!"

    hide tedda_human
    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX
    show roboto happy at right_robot with Dissolve(0.2)
    roboto "M-M-Miss Weng has entered Critical Hunger Mode. She is demanding all juniors report for dumpling consumption immediately."
    show elias ceremonial_happy at center_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line68
    elias "Dumprings!?"

    hide roboto
    show weng ceremonial at right_flip with Dissolve(0.2)
    weng "And lots of flan! Come here! I'm getting hungry!"

    # TODO: FOOD16
    "A wide, mischievous grin tugged at her lips. In her hands she cradled a large, round bamboo steamer basket, the wood darkened slightly from years of faithful use."
    "Wisps of fragrant steam curled from beneath the woven lid."
    "With a dramatic flourish, she lifted the lid. Inside, nestled atop glistening green banana leaves, were dozens of plump dumplings."
    "Tianho Xiang Xia Bao. Tianho Fragrant Shrimp Dumplings."
    "Each dumpling gleamed invitingly under the misty steam, their translucent skins slightly stretched over a generous filling of tender shrimp, minced Tianho forest mushrooms, and fragrant herbs."

    weng "There's more where this came from! Come here, kids!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX
    hide elias
    show roboto happy at center_robot with Dissolve(0.2)
    roboto "A-A-A-ALERT: DUMPLING DISPENSATION IN PROGRESS. MOBILIZE. MOBILIZE. L-L-Let's go, everyone!"

    hide weng
    hide roboto
    with Dissolve(0.1)
    "And just like that, they vanished-sprinting back with a flurry of giggles, robotic beeping, and a suspicious trail of glitter that they absolutely were not supposed to have."

    # jump ch9_route_magnus # check each label scene
    call check_affection_route

# =============================================================================
# SECTION 20: LABEL CH9_ROUTE_YUXUAN — Yuxuan Lantern Scene
# =============================================================================

label ch9_route_yuxuan:

    hide weng
    show yuxuan ceremonial_neutral at right_char with Dissolve(0.2)

    "As I turned around, I saw Yuxuan. He was standing there, wide-eyed, staring up at the wobbling lantern."

    yuxuan "Dorian, what was that?! That lantern just launched early! What if someone down there saw it?! It's glowing like a signal flare! It could give away our location! I told Miss Weng not to let the kids have brushes unsupervised-!"
    dorian "Yu, it said teDuH. I don't think anyone is gonna decode that and send battalions."
    yuxuan "...TeDuH?! Was that supposed to be Tedda?"

    "I nodded. I watched his shoulders slowly slump as the lantern disappeared over the ridge."
    "Then, he looked at the lantern in his own hands-perfectly folded, delicately painted with calligraphy and a small pressed flower at the base. Of course his looked like a museum piece."

    yuxuan "Wait. Don't tell me... was that your lantern?"

    "I nodded again. Slowly. Dramatically."

    yuxuan "Nooo... Here. We'll share mine."
    dorian "You sure? Roboto told me earlier you wanted to be alone."
    show yuxuan ceremonial_lying at right_char with Dissolve(0.1)
    yuxuan "Ah-hah... yeah, well... I told Roboto that so... I could, uh... scout the area. Alone. For... strategic solitude. Yes."
    
    show yuxuan ceremonial_happy at right_char 
    show dorian ceremonial_normal at left_char 
    with Dissolve(0.1)
    "He gave me a sheepish smile, clearly realizing how flimsy his excuse sounded."
    "We both chuckled softly. Without another word, I took the lantern he offered, our fingers brushing for a moment. He lingered in the touch longer than necessary. We didn't mention it."

    hide yuxuan
    hide dorian
    with Dissolve(0.1)
    "We walked a little farther from the others, away from the gentle laughter of children and the distant sound of flutes playing down at the memorial."
    "The wind was gentler here. A quiet hill beneath the stars, just the two of us. The glow of the memorial in the distance made Yuxuan's silhouette shimmer like something caught in a dream."
    "He sat down slowly on the grass, patting the space beside him. I joined him."

    show yuxuan ceremonial_normal at right_char
    show dorian ceremonial_neutral at left_char
    with Dissolve(0.2)
    yuxuan "How have you been feeling... since Elara? Since the kids?"

    "He didn't look at me when he said it. His voice was soft, like he was afraid of pressing too hard."
    "I hesitated, staring out into the dark where Elias's lantern had floated. Somewhere above, it drifted still-Misspelled and luminous."

    dorian "I'm... getting there. One day at a time."

    "The words sat in the air for a long moment. He nodded, understanding without needing the details. Then, I glanced at him."
    "He was touching the lantern. I noticed an entire line of names written on the lantern."

    show dorian ceremonial_sad at left_char with Dissolve(0.1)
    dorian "Those names there. Did you... lose someone important in the tragedy?"

    show yuxuan ceremonial_sad at right_char with Dissolve(0.1)
    "Yuxuan didn't respond right away. He traced a finger along the edge of the lantern, watching the way the candlelight flickered through the rice paper."
    yuxuan "Yeah. I did. A lot of someones, actually. Friends. Colleagues. People who... believed in me. Partners who were with me since the beginning. We all had this dream-building something that could help people. That could change lives."
    yuxuan "We met at the Xiangli Centre-back when none of us had money, barely enough to eat. We'd beg vendors for scraps, pool coins for dumplings. I was shocked how many inventors were there. All brilliant. All broke like me. Heh."

    "He paused, his voice thickening. He touched the names written in the lantern."
    show yuxuan ceremonial_normal at right_char
    show dorian ceremonial_neutral at left_char
    with Dissolve(0.2)
    yuxuan "They were there when Cheng Industries was just a wild idea on a napkin. We stayed up all night coding and designing and arguing over font choices. We believed in what we were building."
    show yuxuan ceremonial_sad at right_char with Dissolve(0.1)
    yuxuan "I remember standing for hours at the Zhong Lotus Promenade, trying to convince passersby that our tech could change lives. And then... when Tianho fell..."
    yuxuan "They didn't make it... But I did."

    "He looked away."

    show yuxuan ceremonial_normal at right_char with Dissolve(0.1)
    yuxuan "When you rescued me... I was grateful. So grateful to have survived. But once I heard they didn't..."

    "His voice caught. He rubbed at his neck, eyes glinting with the shine of held-back tears."

    yuxuan "I couldn't breathe. I felt like I'd stolen their air just to keep myself going."
    yuxuan "I told myself I need to finish what we started. And I did. Cheng Industries... it's successful. It's helping people now. I just..."
    yuxuan "I just wish they were here to see it."

    "He gave a soft, shaky laugh and rubbed his neck."

    show yuxuan ceremonial_happy at right_char with Dissolve(0.1)

    yuxuan "Sorry. That got heavy. I should've told you all this sooner."

    menu:

        "They'd be proud of you. I know I am.":
            $ A3_yuxuan_affection += 1             # +1 Yuxuan affection

            dorian "No. It's okay. They'd be proud of you. I know I am."
            yuxuan "Thank you, Dorian. I really appreciate it."
            dorian "I'm glad you told me this."

        "Say nothing.":
            pass
    
    show yuxuan ceremonial_neutral at right_char with Dissolve(0.1)
    "He turned to look at me then, eyes glinting with something more vulnerable than usual. The breeze tugged gently at his hair."
    "I lowered my gaze to the lantern in our hands."
    "Elara. Daniel. Emily. Sarah. Lucas."
    "I wrote each name with slow, reverent strokes. His hand never left the side of the lantern, steady and warm beside mine."
    "Then... the call came."

    hide dorian
    hide yuxuan
    show feng_suit at center_char
    with Dissolve(0.2)
    feng   "Honored guests, travelers, friends from every border-"
    hide feng_suit

    show yuxuan ceremonial_neutral at right_char
    show dorian ceremonial_normal at left_char
    with Dissolve(0.2)

    yuxuan "Dorian... That man up front. Wait... Is that your best friend? He's-oh. He's the emcee?"
    dorian "I guess he is... That charismatic dog..."

    hide dorian
    hide yuxuan
    show feng_suit at center_char
    with Dissolve(0.2)

    feng   "Tonight, our lanterns rise not just as tribute, but as light."
    feng   "May they find the ones we lost... and may the stars remember them always."
    feng   "On the count of three-One. Two. Three-Release!"
    
    hide feng_suit
    "All around us, lanterns lifted."
    "One by one. Then by the dozens. Then by the hundreds."
    "A quiet gasp rippled through the crowd. It was as if the heavens themselves were exhaling."
    "Lanterns floated upward like glowing petals caught in an invisible tide, rising into the night sky. Red, gold, amber. Some danced lazily in the wind, others soared with sharp purpose."
    "Our lantern joined them-gentle, steady, the names glowing softly like a heartbeat. And then-"

    play sound audio.sfx_fireworks                # PLACEHOLDER — firework boom SFX
    scene cg_festivities with shock_cut
    # play music ost_ch9_fireworks fadein 0.5     # PLACEHOLDER — fireworks theme
    "BOOM."
    
    "A firework lit the sky in brilliant pink."
    "Then another-crackling blue, gold, silver stars spinning across the clouds. One exploded into the shape of a dragon, another in the spiral of a flower."
    "It was breathtaking. Silent awe fell across the hilltop as the world above bloomed in light."

    voice audio.tim_ch9_line61  # transcript: "Elias Elias look it's amazing"
    tim "ELIAS!! ELIAS!! LOOK!! It's amazing!"
    tedda "OH MY GOODNESS! IT'S A FLOWER!"
    voice audio.elias_ch9_line69
    elias "A FROWER! A DWAGON!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX
    roboto "V-V-VISUAL SPECTACLE REGISTERED. SENSORY SYSTEMS OVERLOADING-IN A GOOD WAY! INITIATING JOY DANCE PROTOCOL!"
    scene bg_tianho_deng_blossom with Dissolve(0.2)

    "Roboto actually spun in a little circle, his mechanical arms lifted like wings, twinkling lights flashing from his chest panel like party lights at a tiny disco."
    
    show yuxuan ceremonial_neutral at right_char
    show dorian ceremonial_normal at left_char
    with Dissolve(0.2)
    dorian "Looks like they're having fun too."

    show dorian ceremonial_neutral at left_char with Dissolve(0.1)
    "I turned to Yuxuan, who hadn't moved. His eyes reflected every flare, every color, as if he were trying to memorize it all."

    yuxuan "Dorian... I... I want to say something"

    "I raised a brow, a smile tugging at my lips."

    yuxuan "But it's embarrassing. So you... um... you have to close your eyes first."

    show dorian ceremonial_normal at left_char with Dissolve(0.1)
    "I smirked."

    dorian "Is this another Cheng Industries promotional stunt?"
    show yuxuan ceremonial_lying at right_char with Dissolve(0.1)
    yuxuan "No! I mean-well, not unless you want a jingle."

    scene black with Dissolve(0.2)
    "I closed my eyes, amused."
    "A moment passed. Two. I felt his fingers brush against mine, almost trembling."
    scene cg_dorian_yuxian with dissolve
    "And then-soft."
    "A quick, fluttering kiss on my cheek."
    "So fast, it might've been imagined. But I felt it. Warm and real."
    "I opened my eyes. He was blushing, absolutely red, looking anywhere but at me."

    dorian "Yu..."
    yuxuan "I... just wanted to say I um... I... have fee-"

    scene bg_tianho_deng_blossom with shock_cut
    play sound sfx_sparklers                    # PLACEHOLDER — sparklers SFX

    show roboto happy at center_robot 
    show elias ceremonial_happy at right_char_kids
    show tim ceremonial_happy at left_char_kids
    with Dissolve(0.2)
    roboto "SPARKLER DISPERSION SYSTEM: ENGAGED!"

    hide roboto
    show tedda_human at center_char with Dissolve(0.2)
    tedda "SPARKLERS!"
    voice audio.elias_ch9_line70
    elias "Ahh!! Tim!"
    voice audio.tim_ch9_line62  # transcript: "I wanna hold two, Roberto!"
    tim "I wanna hold two! Roboto!"

    hide tedda_human
    show niko ceremonial_serious at center_char with Dissolve(0.2)
    niko "You can, Tim. But make sure you practice caution. You don't know how many people die because of fireworks."

    hide tim
    show magnus ceremonial at left_char with Dissolve(0.2)
    voice audio.magnus_ch9_line124  # transcript: "Don't be such a spoiled"
    magnus "Don't be such a spoilsport, Niko! You're scaring the kids!"

    "Weng appeared from behind a tree, holding her back like she just climbed a mountain."

    hide elias
    show weng ceremonial at right_flip with Dissolve(0.2)
    weng "Tetrad save me-someone help me with this sparkler! Svante, could you be a dear and help me?"

    hide niko
    show svante ceremonial_happy at center_char with Dissolve(0.2)
    voice audio.svante_ch9_line1  # transcript: "Oh, got it Miss Wang."
    svante "I got you, Miss Weng!"

    "Yuxuan sighed beside me, face still red, voice almost sheepish."

    hide weng
    hide magnus
    hide svante
    show yuxuan ceremonial_sad at right_char
    show dorian ceremonial_neutral at left_char
    with Dissolve(0.2)

    yuxuan "I guess the moment passed..."

    show yuxuan ceremonial_neutral at right_char with Dissolve(0.1)
    "I looked at him, smiled, and gently bumped my shoulder into his."

    show dorian ceremonial_smile at left_char with Dissolve(0.2)
    dorian "Maybe. Or maybe it's just getting started."

    "He glanced at me then, lips parting as if to say something more-but a new firework lit the sky before he could."
    "A massive one-gold and white, shaped like a phoenix, wings spreading wide over the hilltop. We both looked up, quiet again."
    jump ch9_end


# =============================================================================
# SECTION 21: LABEL CH9_ROUTE_CHUNGHEE — Chung-hee Lantern Scene
# =============================================================================

label ch9_route_chunghee:

    hide weng
    show chunghee ceremonial_neutral at right_char with Dissolve(0.2)

    voice audio.chung_ch9_line85  # transcript: "Are you alright, Dorian?"
    chung_hee "Are you alright, Dorian?"

    "I turned around-and there stood Chung-hee, silent as always, holding his lantern with both hands like it was some sacred relic."
    "His brows were slightly furrowed as he watched the crooked, ink-blotted \"teDuH\" lantern bobbing higher and higher into the night sky."
    "I gave him a tired smile, brushing a bit of glitter off my sleeve."

    show dorian ceremonial_normal at left_char with Dissolve(0.1)
    dorian "Well, Elias just launched a lantern to the heavens with a misspelled tribute to a still-living plush girl."
    show dorian ceremonial_neutral at left_char with Dissolve(0.1)
    dorian "By the way, you never did tell me how you brought her to life."
    show chunghee ceremonial_default at right_char with Dissolve(0.2)
    chung_hee "It's simple, really. Tedda's an animation of Elias' emotions. I just embedded a living crystal inside her body."
    dorian "A living crystal?"

    "He raised his right hand-the crystallized one. A prismatic gleam passed over the surface as moonlight kissed its edges."
    show chunghee ceremonial_neutral at right_char with Dissolve(0.1)

    chung_hee "Standard practice in Kyeongjang."
    dorian    "...You say that like animating plush toys with living crystals is totally normal."

    "He let out a mental chuckle, soft as wind against silk."
    "Then his gaze drifted to his untouched lantern. Pristine. Perfect. Hesitating."

    chung_hee "I was going to ask Tim for help. But he ran off yelling something about dumplings and flan."
    chung_hee "With a mind that sharp, I keep forgetting he's the same age as Elias."

    "He looked back at me, holding out his lantern like it was some cryptic artifact."

    chung_hee "How does it work? Is there a button? Or... does one blow into it?"

    "I had to stifle a laugh."
    show dorian ceremonial_smile at left_char with Dissolve(0.1)
    dorian "No blowing required, Chung. It's not a balloon."
    show dorian ceremonial_neutral at left_char with Dissolve(0.1)

    chung_hee "Oh..."

    "I knelt beside him, brushing out the folds gently, pointing to the wax plate."

    dorian "You light this part here. The hot air lifts it up. Like this-"

    chung_hee "Wait."

    show chunghee ceremonial_sad at right_char with Dissolve(0.1)

    "He looked down at the lantern again, then up at me. His gaze was gentle. Inviting."

    chung_hee "Share it with me? Since yours... flew off early."
    show chunghee ceremonial_neutral at right_char with Dissolve(0.1)

    "I nodded. He looked at me like I was more than a warrior, more than a companion. Like he needed me there."
    "He exhaled-quiet relief flowing from his shoulders as I sat beside him. He took the brush and dipped it slowly into the ink."
    "He didn't speak."
    "His hand trembled slightly as he pressed the bristles against the paper. And then-he paused. His eyes flicked toward the memorial down below. His breath caught."
    "He closed his eyes... and the brush slipped from his fingers. He bowed his head-and sobbed."
    show chunghee ceremonial_sad at right_char 
    show dorian ceremonial_sad at left_char
    with Dissolve(0.1)
    chung_hee "Mom... Dad... I'm so sorry."

    "His body shook with each breathless cry, silent but raw, each tremor echoing louder in my chest than any scream could've."
    "I placed a hand on his back. He didn't pull away."
    "Moments passed. Maybe minutes. The soft rustling of wind, the flicker of firelight, the faint laughter of children far in the distance... and the sound of his crying."
    "Finally, he lifted his head and wiped at his face with the back of his sleeve."

    chung_hee "Forgive me... Such a display is unbecoming of an emperor."
    dorian    "Don't say that."

    "I turned to him."
    show dorian ceremonial_neutral at left_char with Dissolve(0.1)

    dorian "If I may ask, what happened?"

    "He hesitated... then let it out like a dam finally breaking."
    show chunghee ceremonial_neutral at right_char with Dissolve(0.1)

    chung_hee "I love my parents with all my heart. But I never wanted the throne. I wanted to be a writer."
    chung_hee "I argued with my parents the day they left. They... wanted me to take the throne. I didn't want to. I said cruel things. Things I never meant."

    "He swallowed."
    show chunghee ceremonial_sad at right_char with Dissolve(0.1)

    chung_hee "I thought I had time to fix things. I thought I'd see them again. But they came to Tianho that day. And I..."

    "His voice faltered."

    chung_hee "I never got to apologize. It was too late."
    scene cg_dorian_chung with dissolve
    "He looked down. I leaned closer. I reached for his hand-his normal one-and held it firmly. He blushed."

    dorian "Then we'll make this one count. For them."


    "He nodded, his fingers curling softly around mine."

    dorian "What about your aunt? You mentioned her yesterday. Is she...?"


    "He lowered his eyes."

    chung_hee "I... suppose I can talk to you about her now. She's alive. She warned me about coming here. About King Gustav."
    chung_hee "She was right..."

    scene bg_tianho_deng_blossom with Dissolve(0.2)
    "With slow, reverent strokes, he wrote his parent's names on the lantern's side: Hyon Min-joon. Kim Seo-yeon."
    "I could feel the reverence in his hands-the way each letter was its own goodbye. Then, we rose together. Still holding hands."
    "He lit the base, and the lantern swelled gently, filling with warm air. Our arms brushed. Our eyes met again. Neither of us looked away."
    "Down below, Feng's voice carried across the fields, rich and resonant, echoing through the hush of the gathered crowd."

    show feng_suit at center_char with Dissolve(0.2)
    feng      "Honored guests, travelers, friends from every border-"

    hide feng_suit
    show chunghee ceremonial_neutral at right_char
    show dorian ceremonial_neutral at left_char 
    with Dissolve(0.2)
    
    chung_hee "Paladin Feng. Your best friend. Hm. Let me guess... he's the master of ceremonies tonight, isn't he?"
    show dorian ceremonial_normal at left_char with Dissolve(0.1)
    dorian    "I guess he is... That charismatic dog..."

    hide dorian
    hide chunghee
    show feng_suit at center_char 
    with Dissolve(0.2)
    feng      "Tonight, our lanterns rise not just as tribute, but as light."
    feng      "May they find the ones we lost... and may the stars remember them always."
    feng      "On the count of three-One. Two. Three-Release!"

    hide feng_suit with Dissolve(0.1)
    "We let go together."
    "All around us, lanterns lifted."
    "One by one. Then by the dozens. Then by the hundreds."
    "A quiet gasp rippled through the crowd. It was as if the heavens themselves were exhaling."
    "Lanterns floated upward like glowing petals caught in an invisible tide, rising into the night sky."
    "Red, gold, amber. Some danced lazily in the wind, others soared with sharp purpose."
    "Our lantern joined them-gentle, steady, the names glowing softly like a heartbeat. And then-"

    play sound audio.sfx_fireworks                # PLACEHOLDER — firework boom SFX
    # play music ost_ch9_fireworks fadein 0.5     # PLACEHOLDER — fireworks theme
    scene cg_festivities with shock_cut
    "BOOM."

    "A firework lit the sky in brilliant pink."
    "Then another-crackling blue, gold, silver stars spinning across the clouds. One exploded into the shape of a dragon, another in the spiral of a flower."
    "It was breathtaking. Silent awe fell across the hilltop as the world above bloomed in light."

    tim "ELIAS!! ELIAS!! LOOK!! It's amazing!"
    tedda "OH MY GOODNESS! IT'S A FLOWER!"
    elias "A FROWER! A DWAGON!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "V-V-VISUAL SPECTACLE REGISTERED. SENSORY SYSTEMS OVERLOADING-IN A GOOD WAY! INITIATING JOY DANCE PROTOCOL!"

    "Roboto actually spun in a little circle, his mechanical arms lifted like wings, twinkling lights flashing from his chest panel like party lights at a tiny disco."

    dorian    "Looks like they're having fun too."
    chung_hee "They sure are."
    scene bg_tianho_deng_blossom with dissolve

    show dorian ceremonial_neutral at left_char
    show chunghee ceremonial_neutral at right_char
    with Dissolve(0.2)
    "Chung-hee turned toward me, the firelight painting his face with soft, dancing shadows."

    chung_hee "Thank you... for staying with me."

    show dorian ceremonial_smile at left_char with Dissolve(0.2)
    "I smiled, saying nothing. Just letting the warmth between us linger."
    "He glanced down, realizing our hands were still entwined. His eyes widened slightly. A faint blush crept up his neck, and he quickly-though reluctantly-let go."
    "Then, almost like flipping a switch, he straightened his posture, squared his shoulders, and cleared his throat."

    show chunghee ceremonial_neutral at right_char

    chung_hee "Ahem. I-apologize. I allowed emotion to... compromise my composure. Clearly, this moment has overwhelmed me."
    voice audio.chung_ch9_line47  # transcript: "Thank you, Miss Wayne."
    chung_hee "Thank you, Dorian."

    "He folded his arms, turning his head as if to reclaim his dignity. But the pink hue still burned on his cheeks."

    play sound sfx_sparklers                    # PLACEHOLDER — sparklers SFX
    hide dorian
    hide chunghee
    show roboto happy at center_robot 
    show elias ceremonial_happy at right_char_kids
    show tim ceremonial_happy at left_char_kids
    with Dissolve(0.2)
    roboto "SPARKLER DISPERSION SYSTEM: ENGAGED!"

    hide roboto
    show tedda_human at center_char with Dissolve(0.2)
    tedda "SPARKLERS!"
    elias "Ahh!! Tim!"
    tim "I wanna hold two! Roboto!"
    stop sound fadeout 1.5

    hide tedda_human
    show niko ceremonial_serious at center_char with Dissolve(0.2)
    niko "You can, Tim. But make sure you practice caution. You don't know how many people die because of fireworks."

    hide tim
    show magnus ceremonial at left_char with Dissolve(0.2)
    magnus "Don't be such a spoilsport, Niko! You're scaring the kids!"

    "Weng appeared from behind a tree, holding her back like she just climbed a mountain."

    hide elias
    show weng ceremonial at right_flip with Dissolve(0.2)
    weng "Tetrad save me-someone help me with this sparkler! Svante, could you be a dear and help me?"

    hide niko
    show svante ceremonial_happy at center_char with Dissolve(0.2)
    svante "I got you, Miss Weng!"
    "Laughter and sparks filled the air as the kids darted between glowing trails of light, their joy casting little halos of warmth over the night."
    
    hide svante
    hide magnus
    hide weng
    show dorian ceremonial_neutral at left_char
    show chunghee ceremonial_neutral at right_char
    with Dissolve(0.2)
    "Chung-hee and I stood together, quietly watching them."

    chung_hee "Do you think... Never mind..."
    dorian    "Should we join them?"
    show chunghee ceremonial_happy at right_char with Dissolve(0.1)

    chung_hee "Absolutely."

    jump ch9_end


# =============================================================================
# SECTION 22: LABEL CH9_ROUTE_SVANTE — Svante Lantern Scene
# =============================================================================

label ch9_route_svante:

    hide weng
    show svante ceremonial_neutral at right_char with Dissolve(0.2)

    svante "Is... that your lantern, Dorian?"

    "I turned around, still shaking my head at the trail of glitter Elias left behind, and there he was-Svante."
    "He stood a few steps away, his arms awkwardly half-folded like he'd been trying to decide whether to approach me or not."
    "His eyes drifted up to the sky where \"teDuH\" was still barely visible-wobbling, defiant, and doomed."

    show dorian ceremonial_normal at left_char with Dissolve(0.1)
    dorian "It was. Emphasis on was. Courtesy of Elias."
    show dorian ceremonial_neutral at left_char with Dissolve(0.1)

    "His lips twitched like he was fighting the urge to stay serious. But then a warm, helpless chuckle escaped him."
    show svante ceremonial_happy at right_char with Dissolve(0.1)
    svante "Haha! Really? It had 'Elias was here' energy all over it."

    "He stepped closer, his shoulders still a little tense, like he wasn't sure if he was intruding."
    show svante ceremonial_base at right_char with Dissolve(0.1)
    svante "So... uh, what are you doing now?"
    dorian "Now that my lantern's flying into the cosmos like a glitter-filled disaster? Probably will grab food with Elias. Why? Something wrong?"
    show svante ceremonial_nervous at right_char with Dissolve(0.1)

    svante "N-No! Nothing's wrong. I just..."
    svante "I just... um... wanted to see how you were doing. Thought maybe... I don't know, you'd want some company."

    "There was something in the way he said it. A little nervous. A little hesitant. But it wasn't pity. It was care. Simple, honest care."
    "He held up the lantern in his hands-a modest one, folded neatly with the ribbon still untied."
    show svante ceremonial_neutral at right_char with Dissolve(0.1)

    svante "I haven't written anything yet. I wasn't here during the tragedy. I didn't lost anyone in Tianho. But I figured... maybe you'd want to share one with me?"

    "I blinked, caught off guard for a moment. That softness in his voice-it made my chest ache a little. I nodded slowly."

    dorian "I think that's a nice idea."

    show svante ceremonial_base at right_char

    "He smiled shyly, scratching the back of his head."

    svante "You can write something, if you want. I... honestly don't know anyone I'd-"

    "He stopped himself, gently handing the lantern to me."
    "I took it in both hands. The paper was cool beneath my fingers, the inkbrush ready beside me. For a long, quiet breath, I just stared at it."
    "Then I spoke, softly."

    dorian "Kristin."
    show svante ceremonial_sad at right_char with Dissolve(0.1)

    svante "... Kristin..."

    show dorian ceremonial_sad at left_char with Dissolve(0.1)
    "His voice caught on the name. His shoulders stiffened, just slightly. I saw the way his jaw clenched, how his breath hitched before he carefully smoothed it out again."
    show dorian ceremonial_neutral at left_char with Dissolve(0.1)
    
    dorian "I know she didn't die in Tianho. But... it still counts. Doesn't it?"
    show svante ceremonial_neutral at right_char with Dissolve(0.1)
    "He didn't speak right away. But then he nodded, once. Firm. A bit shaky."

    svante "Yeah. Of course it does."

    "We sat down side by side on the grass, the cool hilltop quiet except for the distant laughter of kids and the soft hum of singing. Probably Magnus."
    "I passed him the ink and brush."
    "He held it in his fingers for a long time-trembling, like he wasn't sure he was ready. But then he looked at me, his mouth pressed into a line."

    svante "I don't think I ever apologized for what happened. Back at Mjoll."

    "I glanced at him. I didn't interrupt."

    svante "W-When Count Vasily came for Elias... and Kristin spoke out..."

    show svante ceremonial_angry at right_char 
    show dorian ceremonial_serious at left_char
    with Dissolve(0.1)
    "He swallowed hard. His grip tightened slightly on the brush."

    svante "She was k-killed on the spot. Just for saying it was wrong. And I-"

    "His voice cracked. He stopped, closed his eyes, drew a slow breath."
    show svante ceremonial_neutral at right_char
    show dorian ceremonial_neutral at left_char
    with Dissolve(0.1)

    svante "I was so angry with you. With Elias. I blamed you both. I wanted someone to hurt as much as I did. And I hated myself for it. Because deep down, I knew..."
    svante "That was the first time I ever questioned my father. King Gustav. I want to know why he did what he did but..."

    "He looked down again, brushing the tip of the inkstick against the rim of the bowl."

    svante "I... I want to say I'm sorry, Dorian. For the resentment. You and Elias."

    "I reached over and gently rested a hand over his. He blushed."

    show svante ceremonial_nervous at right_char

    svante "D-Dorian..."
    dorian "Kristin gave you the courage to start questioning him. You don't have to be sorry for that."
    dorian "And if it wasn't for you, we never could've saved Chung-hee. You stood in the way of your father's plan. You risked everything."
    dorian "That was your sister's courage in you."
    svante "I... can't deny it. I was scared at first. Sir Tian Xun was... scary. Very much so."

    scene bg_tianho_deng_blossom with Dissolve(0.2)
    "For a long moment, neither of us said anything. The lantern paper between us was no longer blank. Svante had written her name in clean, careful strokes."
    "{i}Kristin Nordstrom.{/i}"
    "Below it, he added one more line:"
    "{i}You still guide me.{/i}"
    "He handed the brush back to me with a small, grateful nod. Together, we lit the lantern."
    "Then... the call came."

    show feng_suit at center_char with Dissolve(0.2)
    feng   "Honored guests, travelers, friends from every border-"
    hide feng_suit
    show svante ceremonial_neutral at right_char
    show dorian ceremonial_neutral at left_char
    with Dissolve(0.2)
    svante "That's Sir Feng... He's the one running the ceremonies?"
    show dorian ceremonial_normal at left_char with Dissolve(0.1)
    dorian "I guess he is... That charismatic dog..."\

    hide svante
    hide dorian
    show feng_suit at center_char 
    with Dissolve(0.2)

    feng   "Tonight, our lanterns rise not just as tribute, but as light."
    feng   "May they find the ones we lost... and may the stars remember them always."
    feng   "On the count of three-One. Two. Three-Release!"

    scene bg_tianho_deng_blossom with Dissolve(0.2)

    "All around us, lanterns lifted."
    "One by one. Then by the dozens. Then by the hundreds."
    "A quiet gasp rippled through the crowd. It was as if the heavens themselves were exhaling."
    "Lanterns floated upward like glowing petals caught in an invisible tide, rising into the night sky. Red, gold, amber. Some danced lazily in the wind, others soared with sharp purpose."
    "Our lantern joined them-gentle, steady, the names glowing softly like a heartbeat. And then-"
    scene cg_festivities with shock_cut
    play sound audio.sfx_fireworks                # PLACEHOLDER — firework boom SFX
    # play music ost_ch9_fireworks fadein 0.5     # PLACEHOLDER — fireworks theme

    "BOOM."

    "A firework lit the sky in brilliant pink."
    "Then another-crackling blue, gold, silver stars spinning across the clouds. One exploded into the shape of a dragon, another in the spiral of a flower."
    "It was breathtaking. Silent awe fell across the hilltop as the world above bloomed in light."

    tim "ELIAS!! ELIAS!! LOOK!! It's amazing!"
    tedda "OH MY GOODNESS! IT'S A FLOWER!"
    elias "A FROWER! A DWAGON!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "V-V-VISUAL SPECTACLE REGISTERED. SENSORY SYSTEMS OVERLOADING-IN A GOOD WAY! INITIATING JOY DANCE PROTOCOL!"

    "Roboto actually spun in a little circle, his mechanical arms lifted like wings, twinkling lights flashing from his chest panel like party lights at a tiny disco."

    dorian "Looks like they're having fun too."
    svante "Haha yeah. They're having a lot of fun."

    "Elias was laughing so hard he had to hold onto Tedda, and Tim was pointing frantically at every firework like each one was a miracle."
    scene bg_tianho_deng_blossom with Dissolve(0.2)
    
    "Svante chuckled softly beside me. I turned to him just as another firework lit the sky-this time in shimmering gold, the shape of a phoenix unfurling its wings across the stars."
    "He was looking up, the warm glow flickering in his eyes. His lips were parted slightly, like he wanted to say something. But instead, he just... leaned."
    scene cg_dorian_svante with shock_cut
    "Gently. Almost shyly."
    "His head came to rest on my shoulder."
    "I didn't move. Just let him stay there, quiet against me, as the fireworks continued to bloom like celestial flowers overhead."

    svante "I haven't... felt peace like this in a long time."

    "His voice was barely a whisper, like he wasn't even sure if he wanted to say it out loud. But I heard him."

    svante "These past few days... I wish it wouldn't end. I wish it would last."

    "And without thinking, I shifted slightly-just enough to lean my head lightly against his. Our temples touched. The space between us vanished."

    dorian "Then let it stay a little longer."

    "He closed his eyes for a moment, like he was memorizing the feeling."
    "The lanterns above us drifted higher and higher, joining the stars. I could still see ours-Kristin's name glowing gently in the dark."
    scene bg_tianho_deng_blossom with Dissolve(0.2)

    play sound sfx_sparklers                    # PLACEHOLDER — sparklers SFX
    hide dorian
    hide chunghee
    show roboto happy at center_robot 
    show elias ceremonial_happy at right_char_kids
    show tim ceremonial_happy at left_char_kids
    with Dissolve(0.2)
    roboto "SPARKLER DISPERSION SYSTEM: ENGAGED!"

    hide roboto
    show tedda_human at center_char with Dissolve(0.2)
    tedda "SPARKLERS!"
    elias "Ahh!! Tim!"
    tim "I wanna hold two! Roboto!"
    stop sound fadeout 1.5

    hide tedda_human
    show niko ceremonial_serious at center_char with Dissolve(0.2)
    niko "You can, Tim. But make sure you practice caution. You don't know how many people die because of fireworks."

    hide tim
    show magnus ceremonial at left_char with Dissolve(0.2)
    magnus "Don't be such a spoilsport, Niko! You're scaring the kids!"

    "Weng appeared from behind a tree, holding her back like she just climbed a mountain."

    hide elias
    show weng ceremonial at right_flip with Dissolve(0.1)
    weng "Finally, my back isn't hurting... Chung-hee, would you like a sparkler?"
    hide niko
    show chunghee ceremonial_neutral at center_char with Dissolve(0.2)
    chung_hee   "Hmm... Perhaps I can try using one. For... recreational purposes."

    "Laughter and sparks filled the air as the kids darted between glowing trails of light, their joy casting little halos of warmth over the night. Roboto spun in place again, strobing pink and purple like some overexcited festival lantern."
    hide chunghee
    show roboto happy at center_robot with Dissolve(0.2)
    roboto "S-S-Safe sparkler mode initiated!"

    scene bg_tianho_deng_blossom with Dissolve(0.2)
    "And still... we stayed seated, Svante and I. Side by side. Just watching. Breathing. Letting it all wash over us."

    svante "Dorian..."

    "I glanced at him. His face was turned to the stars again, but the softness in his voice pulled my eyes to him."

    svante "Thank you... for this peace. For giving me a chance. For everything."

    "He hesitated. Then, more quietly, as if afraid it might break the moment:"

    svante "Can you... stay awhile?"

    "The firelight played across his features. I reached over and gently, without words, took his hand. He smiled."
    "Above us, another firework burst across the sky-this time a brilliant ring of silver that shimmered like frost on a blade."

    jump ch9_end


# =============================================================================
# SECTION 23: LABEL CH9_ROUTE_NIKO — Niko Lantern Scene
# =============================================================================

label ch9_route_niko:
    # play music audio.niko_theme with fadein 2.0 loop
    hide weng
    show niko ceremonial_base at right_char with Dissolve(0.2)

    niko "...I told Miss Weng not to give the kids any brushes. Especially Elias."

    "I turned around-and there he was. Niko. Standing a few steps behind me with his arms crossed and that usual unreadable expression on his face, like the breeze didn't dare ruffle his robes without permission."
    "His eyes tracked the crooked lantern floating in the sky-\"teDuH\" proudly displayed for all the heavens to see."

    niko "I saw the kids beside you and figured your lantern was probably in trouble."

    "He glanced at the fading trail of glitter still lingering in the grass where Elias had bolted off."
    show niko ceremonial_smile at right_char with Dissolve(0.1)

    niko "Seems I was right."

    "I let out a low laugh despite myself. There was something comforting about his tone. Not mocking. Just... dry, matter-of-fact, like he wasn't surprised one bit."
    show niko ceremonial_base at right_char 
    show dorian ceremonial_normal at left_char
    with Dissolve(0.1)
    dorian "Heh. You got me."

    show dorian ceremonial_neutral at left_char with Dissolve(0.1)
    "He reached into his only sleeve and pulled out a lantern-immaculate, folded with that eerie precision he always had."

    niko "You can share mine, if you want."

    "I looked at him, eyebrows raised."
    show dorian ceremonial_serious at left_char with Dissolve(0.1)

    dorian "Are you sure? You're a Prophet. Shouldn't this be between you and... you know. The death god?"
    show niko ceremonial_base at right_char 
    show dorian ceremonial_neutral at left_char 
    with Dissolve(0.1)
    niko "This particular festival honors the Prosperity Dragon."
    niko "I don't worship the Prosperity Dragon. Us Prophets obey Enoch's law word by word. Enoch himself proclaimed that dragons are just are overgrown lizards with complex delusions of grandeur."
    yuxuan "HEY! I HEARD THAT, NIKO!"
    niko "I'm just doing the lantern release merely so I don't miss out so to speak."

    "He gave me a flat look, as if daring me to challenge him on his theology or his dragon takes. I just shook my head, grinning."

    dorian "Alright, fine. Let's share it."

    "He passed me a brush, the ink already prepared. We didn't speak right away."
    "The night buzzed softly around us-Roboto's automated sounds, children laughing, and the sound of Magnus humming a melody."
    "Then, slowly, Niko pulled out a small container. He opened it carefully, reverently. Tianho flan."
    "And then... a book. Bound in dark leather, worn at the corners."

    dorian "I remember you mentioning that that's Kaito's favorite dessert, right?"
    show niko ceremonial_meditate at right_char with Dissolve(0.1)

    "He didn't look up immediately. Just kept his eyes on the flan like it might vanish if he blinked."

    dorian "You never told me what happened. Not really."

    "For a moment, I didn't think he would answer. But then."
    show niko ceremonial_sad at right_char with Dissolve(0.1)

    niko "...He died saving people at the tragedy."
    niko "During the Tragedy. There was an inn-Shenzhou. It caught fire. Most people ran. Kaito... ran in."
    niko "There were children. An elderly couple. A dog. Knowing Kaito, he probably went back for all of them."

    "He paused, hands tightening just a little around the book."

    niko "He always did that. Put himself last. I used to yell at him for it. All the time."
    show niko ceremonial_meditate at right_char with Dissolve(0.1)

    niko "First Law of Enoch: 'To hinder death is to defy Him.' Us Prophets are told never to hinder death. It's not our place. Enoch teaches us-death is the final mercy. The embrace of rest."

    show niko ceremonial_serious at right_char with Dissolve(0.1)
    "He stared at the flan, the lantern, the sky."

    niko "But Kaito never followed that. He said... 'If you can hold someone back from that rest, even for a little while, maybe they'll find a reason to keep living.'"
    niko "That's why he wasn't accepted by the Prophets at first. They chose me instead. I obeyed. I understood the doctrine. I followed."
    niko "They only let him in because I bargained. I was receiving visions from Enoch. The others saw that. They knew I was... special and my devotion knew no limits."

    "I sat still, letting the silence stretch between us. The kind of silence that didn't need to be filled."

    dorian "He sounds like someone worth remembering."

    show niko ceremonial_base at right_char with Dissolve(0.1)

    "Niko didn't look at me right away, but his expression softened."
    "Then-deliberately-he pulled out a second spoon from the container and held it toward me."

    niko "He hated sharing. But I think he'd make an exception for you."

    "I took the spoon. We shared the flan in silence, the stars above us and the glow of lanterns painting the world in amber and gold."
    "We weren't even halfway done when a pair of familiar voices piped up behind us."

    show elias ceremonial_cute at center_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line71  # transcript: "Daddy is so fun!"
    elias "Daddy, is that fwan?"
    hide elias
    show tim ceremonial_shy at center_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line63  # transcript: "We already finished ours, and"
    tim "We already finished ours. And that one smells superior. May I analyze it-er, I mean, may I have some?"
    hide tim with Dissolve(0.1)

    "I turned to see them standing there, Elias wide-eyed with excitement and sticky hands, and Tim with his arms folded like a tiny scholar trying to be polite."

    niko "You two already finished your desserts?"
    show elias ceremonial_happy at center_char_kids with Dissolve(0.1)
    voice audio.elias_ch9_line72
    elias "We're super good at eating dessert!"
    hide elias
    show tim ceremonial_happy at center_char_kids with Dissolve(0.1)
    voice audio.tim_ch9_line64  # transcript: "Yes, our proficiency is unmatched."
    tim "Yes. Our proficiency is unmatched. We request a second round."
    show niko ceremonial_smile at right_char with Dissolve(0.1)
    niko "Under one condition. More vegetables. Got it?"
    voice audio.tim_ch9_line65  # transcript: "Acceptable terms."
    tim "Acceptable terms."

    hide tim with Dissolve(0.1)
    "They snatched the rest of the flan and ran off, shouting about carrots and cucumbers like they were ancient curses."

    dorian "You know... in a way, I thank Enoch for not taking Elias away from me."
    dorian "There was a time. In Mjoll. Elias was hit by an arrow. Mortally."
    dorian "It was chaos. I thought... I thought he was gone. I went berserk."

    "I looked down, remembering the blood on my hands, the way the blood pooled around Elias. The panic. The helplessness."
    show dorian ceremonial_normal at left_char with Dissolve(0.1)
    dorian "Yuxuan told me someone stitched him up. No one knew who. But he said if it wasn't for those stitches... Elias would've died that night."
    show dorian ceremonial_neutral at left_char with Dissolve(0.1)

    niko "...Hmm."

    show niko ceremonial_sad at right_char with Dissolve(0.1)

    "Niko didn't answer. He looked down at the book again. Then at the lantern."
    "And slowly, silently, he took the brush and dipped it in ink. Wrote, in clean, solemn strokes:"
    "Kaito Tsukumo. Rest in peace, beloved brother."

    show niko ceremonial_base at right_char with Dissolve(0.1)

    niko "Well. Shall we, Dorian?"

    hide niko
    hide dorian
    with Dissolve(0.1)
    "I nodded. Together, we lit the lantern. Then... the call came."

    show feng_suit at center_char with Dissolve(0.1) 
    feng   "Honored guests, travelers, friends from every border-"
    hide feng_suit
    show dorian ceremonial_neutral at left_char 
    show niko ceremonial_smile at right_char 
    with Dissolve(0.2)
    niko "Your best friend. He's the master of ceremonies, I take it."
    dorian "I guess he is... That charismatic dog..."
    hide niko
    hide dorian
    show feng_suit at center_char with Dissolve(0.2) 
    feng   "Tonight, our lanterns rise not just as tribute, but as light."
    feng   "May they find the ones we lost... and may the stars remember them always."
    feng   "On the count of three-One. Two. Three-Release!"
    hide feng_suit with Dissolve(0.1)
    "All around us, lanterns lifted."
    "One by one. Then by the dozens. Then by the hundreds."
    "A quiet gasp rippled through the crowd. It was as if the heavens themselves were exhaling."
    "Lanterns floated upward like glowing petals caught in an invisible tide, rising into the night sky."
    "Red, gold, amber. Some danced lazily in the wind, others soared with sharp purpose."
    "Our lantern joined them-gentle, steady, the names glowing softly like a heartbeat. And then-"

    # play sound audio.sfx_fireworks                # PLACEHOLDER — firework boom SFX
    # play music ost_ch9_fireworks fadein 0.5     # PLACEHOLDER — fireworks theme

    "BOOM."

    scene cg_festivities with dissolve
    "A firework lit the sky in brilliant pink."
    "Then another-crackling blue, gold, silver stars spinning across the clouds. One exploded into the shape of a dragon, another in the spiral of a flower."
    "It was breathtaking. Silent awe fell across the hilltop as the world above bloomed in light."

    tim "ELIAS!! ELIAS!! LOOK!! It's amazing!"
    tedda "OH MY GOODNESS! IT'S A FLOWER!"
    elias "A FROWER! A DWAGON!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "V-V-VISUAL SPECTACLE REGISTERED. SENSORY SYSTEMS OVERLOADING-IN A GOOD WAY! INITIATING JOY DANCE PROTOCOL!"

    "Roboto actually spun in a little circle, his mechanical arms lifted like wings, twinkling lights flashing from his chest panel like party lights at a tiny disco."

    dorian "Looks like they're having fun too."
    niko "A lot of fun, actually."

    scene cg_dorian_niko with dissolve

    "He reached into his pockets. His fingers curled around something small."
    "Then he held it out to me."
    "A tiny charm."
    "Shaped like a yellow flower. Pressed and lacquered, its petals still delicate, preserved perfectly in time. It shimmered faintly beneath the lantern light-sun-touched and a little worn, like it had been carried for a while."

    niko "It's... a star lily."

    "His voice was soft. Too soft for someone who usually spoke in clean, clipped words and divine edicts."

    niko "It only grows in the fields outside the Seventh Temple in Hamatame. They say it blooms at dawn. Even in winter."

    "He didn't meet my eyes. His gaze stayed fixed somewhere far off in the distance."

    niko "It reminded me of you."

    "There was a pause."
    "His jaw tightened."

    niko "Bright... and stubborn."

    "I stared at the charm, turning it gently in my hand."

    dorian "Niko..."

    "He cleared his throat, still avoiding my gaze."

    niko "You don't have to keep it. I just thought..."

    "He stopped himself."
    "I didn't say anything. Instead, I leaned just a little closer. Let my shoulder brush against his. He tensed-but didn't pull away."
    "The fireworks above us flared again-red, gold, a spiraling white bloom like a galaxy unfolding. A quiet gasp rippled through the crowd again."
    "And in the middle of all that noise and color, Niko glanced toward me-just once."
    "Tetrad above... is he... blushing?"
    "I tucked the charm carefully into my cloak pocket."

    scene bg_tianho_deng_blossom with fade
    play sound audio.sfx_sparklers                    # PLACEHOLDER — sparklers SFX


    show roboto happy at center_robot
    show tedda_human at right_char
    show elias ceremonial_happy at left_char_kids 
    with Dissolve(0.2)

    roboto "SPARKLER DISPERSION SYSTEM: ENGAGED!"
    tedda "SPARKLERS!"
    elias "Ahh!! Tim!"

    hide tedda_human
    show tim ceremonial_happy at right_char_kids with Dissolve(0.2)
    tim "I wanna hold two! Roboto!"
    stop sound fadeout 1.0
    hide tim 
    hide elias
    hide roboto
    show niko ceremonial_base at right_char 
    show magnus ceremonial at left_char
    show yuxuan ceremonial_happy at center_char
    with Dissolve(0.2)
    niko "You can, Tim. But make sure you practice caution. You don't know how many people die because of fireworks."

    magnus "Don't be such a spoilsport, Niko! You're scaring the kids!"

    yuxuan      "Niko, you're making it sound like they're juggling hand grenades like that Tian Xun guy."

    "Weng appeared from behind a tree, holding her back like she just climbed a mountain."

    hide niko
    show weng ceremonial at right_flip with Dissolve(0.2)
    weng "Tetrad save me-someone help me with this sparkler! Svante, could you be a dear and help me?"

    hide magnus
    show svante ceremonial_happy at left_char with Dissolve(0.2)
    svante "I got you, Miss Weng!"

    scene bg_tianho_deng_blossom with Dissolve(0.3)
    "Laughter and sparks filled the air as the kids darted between glowing trails of light, their joy casting little halos of warmth over the night."
    "Roboto spun in place again, strobing pink and purple like some overexcited festival lantern."

    roboto "S-S-Safe sparkler mode initiated!"

    "I looked at Niko again."
    "And before either of us spoke again, our fingers found each other."
    "No words. Just the quiet meeting of palms. His fingers curled gently into mine."

    niko "Thank you, Dorian."
    jump ch9_end


# =============================================================================
# SECTION 24: LABEL CH9_ROUTE_MAGNUS — Magnus Lantern Scene
# =============================================================================

label ch9_route_magnus:

    hide weng
    show magnus ceremonial at right_char with Dissolve(0.2)

    voice audio.magnus_ch9_line125  # transcript: "What a lovely made piece"
    magnus "What a lovely made piece of artwork!"

    "I turned around, and there he was-Magnus. Standing a few paces away, hands in his ceremonial sleeves, eyes tilted upward toward the sky."
    "His gaze followed the drifting lantern with \"teDuH\" scrawled proudly across its paper like it belonged in a museum of chaotic childhood art."

    voice audio.magnus_ch9_line126  # transcript: "A long flame sails with"
    magnus "A lone flame sails with crooked grace, a tribute born of sticky haste."
    voice audio.magnus_ch9_line127  # transcript: "The name is spelled, the"
    magnus "The name misspelled; the ink still wet-but love was there. So, no regret."

    show dorian ceremonial_normal at left_char with Dissolve(0.1)
    "I couldn't help but chuckle."
    "Magnus turned his head slightly, his usual cool expression softening into the faintest grin. He stepped closer, hands behind his back now."
    show dorian ceremonial_neutral at left_char with Dissolve(0.1)

    voice audio.magnus_ch9_line128  # transcript: "I just wanted to see"
    magnus "I just wanted to see you! Is that alright? I also wanted to ask if you played an instrument."

    "I shook my head a little."
    show dorian ceremonial_normal at left_char with Dissolve(0.1)
    dorian "Not really. I mean, I've tried-kind of. I'm more of a... listener."
    show dorian ceremonial_neutral at left_char with Dissolve(0.1)

    voice audio.magnus_ch9_line129  # transcript: "Mmm, I play the harp."
    magnus "Mm... I play the harp. Nothing fancy. Just enough to annoy my tutors when I was a boy... I remember that much, at least."
    voice audio.magnus_ch9_line130  # transcript: "I could play for you"
    magnus "I could play for you sometime. If you'd like."

    "Something about the way he said that made the night feel warmer. Then, after a small pause, he tilted his head toward me."

    voice audio.magnus_ch9_line131  # transcript: "Would you like to share"
    magnus "Would you... like to share a lantern with me?"

    "He held one out, delicately folded, the red ribbon trailing from one end like a promise. One lantern."

    dorian "...Yeah. I'd like that, Magnus."

    hide magnus
    hide dorian
    with Dissolve(0.1)
    "We stepped away from the others, just far enough that the noise faded into a soft background hum. The lantern flickered between us as we walked, swaying gently in the breeze."
    "After a while, Magnus spoke again-softly."

    show dorian ceremonial_neutral at left_char
    show magnus ceremonial at right_char 
    with Dissolve(0.2)

    voice audio.magnus_ch9_line132  # transcript: "I still don't remember everything."
    magnus "I still don't remember everything. Not even most things. But... bits remain."
    dorian "Like what?"

    "He thought for a moment, fingers brushing the red ribbon."

    voice audio.magnus_ch9_line133  # transcript: "the taste of gallium persimmons,"
    magnus "The taste of Galean persimmons. The sound of wind through temple bells. A song... Many songs... something about stars."
    voice audio.magnus_ch9_line134  # transcript: "But most vividly, remember, love."
    magnus "But most vividly, I remember... love. I had a woman. Her name was Adriana."

    show dorian ceremonial_serious at left_char with Dissolve(0.1)
    "I froze. The name hit like a dropped torch in the dark. He mentioned her before when we were fighting but I was too focused on surviving."

    dorian "Adriana? You mean the Adriana? One of the Immortal Tetrad?"
    show dorian ceremonial_neutral at left_char with Dissolve(0.1)

    voice audio.magnus_ch9_line135
    magnus "Immortal? Hahaha! No, she was mortal. Human. She lived in a village near the coast... or maybe it was on the cliffs. I can't quite see it. But I remember her hands. Her voice."

    "His brow furrowed, eyes narrowing like he was reaching for something just beyond the veil."

    voice audio.magnus_ch9_line136  # transcript: "She was killed. I don't"
    magnus "She was killed. I don't remember the man who did it. A villain with eyes like razors and a soul already given to ash."

    show dorian ceremonial_serious at left_char with Dissolve(0.1)
    "I didn't know what to say. My heart tightened in my chest, caught between sympathy and something sharper-something I couldn't name yet."
    "But then, Magnus looked at me. And everything shifted."
    show dorian ceremonial_neutral at left_char with Dissolve(0.1)

    voice audio.magnus_ch9_line137  # transcript: "After she died, I began"
    magnus "After she died, I began to dream. Not of her. Of... someone else."
    voice audio.magnus_ch9_line138  # transcript: "of you, Dorian."
    magnus "Of you, Dorian."

    "I stared at him, stunned into silence."

    voice audio.magnus_ch9_line139  # transcript: "I saw you again and"
    magnus "I saw you-again and again. Calling out. In firelight, in snow, in the middle of shattered cities I'd never seen before. Calling for me. Begging me to wake up."

    "A cold thrill ran down my spine."

    dorian "No... that can't be right. I'm the one who dreamed of you."

    "The lantern between us flickered."
    "Magnus turned, slowly, fully, to face me."
    "We stood in silence, just for a moment, as the fireworks cracked again above us-silver now, fanning out in spirals like celestial wings."

    dorian "How long were you calling for me?"
    voice audio.magnus_ch9_line140  # transcript: "long enough for me to"
    magnus "Long enough for me to believe I might never be found."
    voice audio.magnus_ch9_line141  # transcript: "But I was. By you"
    magnus "But I was... by you and our companions. For that, I thank you."

    hide magnus
    hide dorian
    with Dissolve(0.1)
    "I looked down at the lantern between us. We hadn't written anything yet. Without a word, I took up the brush."
    "Elara. Daniel. Sarah. Emily. Lucas."
    "I wrote each name with care, letting the memory settle into every stroke of ink. Magnus stood beside me, watching-not intruding, but present, solid."
    "We lit the lantern together. The flame inside flickered once, then glowed warm and steady. Then... the call came."

    show feng_suit at center_char with Dissolve(0.2)
    feng   "Honored guests, travelers, friends from every border-"
    feng   "Tonight, our lanterns rise not just as tribute, but as light."
    feng   "May they find the ones we lost... and may the stars remember them always."
    feng   "On the count of three-One. Two. Three-Release!"

    hide feng_suit with Dissolve(0.1)
    "All around us, lanterns lifted."
    "One by one. Then by the dozens. Then by the hundreds."
    "A quiet gasp rippled through the crowd. It was as if the heavens themselves were exhaling."
    "Lanterns floated upward like glowing petals caught in an invisible tide, rising into the night sky. Red, gold, amber. Some danced lazily in the wind, others soared with sharp purpose."
    "Our lantern joined them-gentle, steady, the names glowing softly like a heartbeat. And then-"

    scene cg_festivities with shock_cut
    play sound audio.sfx_fireworks                # PLACEHOLDER — firework boom SFX
    # play music ost_ch9_fireworks fadein 0.5     # PLACEHOLDER — fireworks theme

    "BOOM."

    "A firework lit the sky in brilliant pink."
    "Then another-crackling blue, gold, silver stars spinning across the clouds. One exploded into the shape of a dragon, another in the spiral of a flower."
    "It was breathtaking. Silent awe fell across the hilltop as the world above bloomed in light."

    tim "ELIAS!! ELIAS!! LOOK!! It's amazing!"
    tedda "OH MY GOODNESS! IT'S A FLOWER!"
    elias "A FROWER! A DWAGON!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "V-V-VISUAL SPECTACLE REGISTERED. SENSORY SYSTEMS OVERLOADING-IN A GOOD WAY! INITIATING JOY DANCE PROTOCOL!"

    "Roboto actually spun in a little circle, his mechanical arms lifted like wings, twinkling lights flashing from his chest panel like party lights at a tiny disco."

    dorian "Looks like they're having fun too."
    voice audio.magnus_ch9_line142  # transcript: "Oh, oh, the young ones"
    magnus "Oh, how the young ones delight! Come, Dorian-we should join them. At least for a moment."

    "He offered me his hand - an invitation. I accepted it and we danced along with the kids."
    "Magnus lifted his voice in song-soft and smooth, a melody that felt older than the stars overhead. His voice wrapped around me like silk, and without thinking, I joined in."

    voice audio.magnus_ch9_line143  # transcript: "O stars that sail the"
    magnus "O stars that sail the velvet night, O winds that carry dreams in flight..."
    dorian "...If I must drift, let it be near, the one who makes the dark feel clear."

    "And then-"
    scene cg_dorian_magnus with shock_cut
    "BAM."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "U-U-U-UNINTENTIONAL TRAJECTORY DETECTED-IMPACT IMMINENT!"
    tedda "Oh my! I'm so sorry!"

    "There was a blur of motion-a flailing arm and suddenly I tripped. Magnus tried to catch me, but his foot caught the edge of his robe, and we both went tumbling back."
    "I landed right on top of him."
    "The world went quiet for a moment-just the thud of hearts, the echo of laughter, the flicker of firelight dancing across Magnus' cheeks."
    "I stared down at him, and he stared up at me."
    "One of my hands was braced on his chest, the other still holding a piece of my robe from the fall. His hands had instinctively found my waist."

    voice audio.magnus_ch9_line144  # transcript: "You have a beautiful voice."
    magnus "You... have a beautiful voice."
    dorian "You too, Magnus. Sorry for landing on top of you."
    voice audio.magnus_ch9_line145  # transcript: "That may have been the"
    magnus "That may have been the highlight of my evening."

    "We didn't move. We could have. But neither of us wanted to."

    scene bg_tianho_deng_blossom with fade
    play sound sfx_sparklers                    # PLACEHOLDER — sparklers SFX

    show roboto happy at center_robot
    show tedda_human at right_char
    show elias ceremonial_happy at left_char_kids 
    with Dissolve(0.2)
    roboto "SPARKLER DISPERSION SYSTEM: ENGAGED!"
    tedda "SPARKLERS!"
    elias "Ahh!! Tim!"

    hide tedda_human
    show tim ceremonial_happy at right_char_kids with Dissolve(0.2)
    tim "I wanna hold two! Roboto!"
    stop sound fadeout 1.0

    hide tim 
    hide elias
    hide roboto
    show niko ceremonial_base at right_char 
    show magnus ceremonial at left_char
    show yuxuan ceremonial_happy at center_char
    with Dissolve(0.2)
    niko "You can, Tim. But make sure you practice caution. You don't know how many people die because of fireworks."

    magnus "Don't be such a spoilsport, Niko! You're scaring the kids!"

    yuxuan      "Niko, you're making it sound like they're juggling hand grenades like that Tian Xun guy."

    "Weng appeared from behind a tree, holding her back like she just climbed a mountain."

    hide niko
    show weng ceremonial at right_flip with Dissolve(0.2)
    weng "Tetrad save me-someone help me with this sparkler! Svante, could you be a dear and help me?"

    hide magnus
    show svante ceremonial_happy at left_char with Dissolve(0.2)
    svante "I got you, Miss Weng!"
    
    scene bg_tianho_deng_blossom with Dissolve(0.3)
    "Laughter and sparks filled the air as the kids darted between glowing trails of light, their joy casting little halos of warmth over the night."
    "Roboto spun in place again, strobing pink and purple like some overexcited festival lantern."

    roboto "S-S-Safe sparkler mode initiated!"

    "We both burst into laughter as I finally rolled off Magnus-but not far. Just enough to still feel the warmth of him beside me, our arms brushing as we watched the sky blossom in fire."

    voice audio.magnus_ch9_line146  # transcript: "We'll finish that dance later."
    magnus "We'll finish that dance later."
    dorian "It's a promise."

    jump ch9_end


# =============================================================================
# SECTION 25: LABEL CH9_END — Common Ending / Sparklers / Going Home
# =============================================================================

label ch9_end:

    "The hilltop was glowing now, cast in soft hues of flame and magic. Lanterns floated steadily upward, their light flickering like heartbeat echoes. Sparklers twirled in tiny hands."
    "One by one, the firecrackers gave way to silence. The celebration slowly dissolved into the hush of night."
    scene black with fade
    "We returned to the lab in quiet procession. My steps felt heavier, but not from exhaustion-from the weight of everything I'd seen, heard, and felt."
    "I changed, climbed into bed, and let myself collapse into the softness."
    "My heart was full."
    "Maybe too full."

    pause 2.0
    stop music fadeout 3.0
    stop audio fadeout 2.0
    show screen chapter_title_screen(
        "9",
        "Tianho Ceremony",
        subtitle="END",
        duration=3.0
    )
    pause 3.0

    jump chapter_10


# =============================================================================
# END OF CHAPTER 9 PART 2
# =============================================================================