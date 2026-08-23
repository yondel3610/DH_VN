###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  SCENE: CHAPTER 7 — The Seal and the Winged Man
###############################################################################

# =============================================================================
# SECTION 1: CHARACTER DEFINITIONS
# =============================================================================

# compiled character definitions

# =============================================================================
# SECTION 2: IMAGE DECLARATIONS
# =============================================================================

# =============================================================================
# SECTION 3: AUDIO DECLARATIONS
# =============================================================================
# define audio.ost_ch7_dream     = "audio/music/ost_ch7_dream.ogg"         # PLACEHOLDER
# define audio.ost_ch7_bunker    = "audio/music/ost_ch7_bunker.ogg"         # PLACEHOLDER
# define audio.ost_ch7_warm      = "audio/music/ost_ch7_warm.ogg"           # PLACEHOLDER
# define audio.ost_ch7_feng_clash = "audio/music/ost_ch7_feng_clash.ogg"    # PLACEHOLDER
# define audio.ost_ch7_drink     = "audio/music/ost_ch7_drink.ogg"          # PLACEHOLDER
# define audio.sfx_blue_flames   = "audio/sfx/sfx_blue_flames.ogg"          # PLACEHOLDER
# define audio.sfx_wine_pop      = "audio/sfx/sfx_wine_pop.ogg"             # PLACEHOLDER
# define audio.amb_bunker        = "audio/ambient/amb_bunker.ogg"            # PLACEHOLDER


# =============================================================================
# SECTION 4: GAME VARIABLES
# =============================================================================

# =============================================================================
# SECTION 5: LABEL CHAPTER_7 — White Void / Magnus Dream / Wake Up
# =============================================================================

label chapter_7:
    $ save_name = "Chapter 7"

    scene black with fade             # PLACEHOLDER — white void
    show screen chapter_title_screen(
        "7",
        "Cheng Industries",
        # subtitle="Tianho — Underground Lab",
        duration=3.0
    )
    pause 3.0
    scene plain_white with fade
    pause 1.5
    # play music ost_ch7_dream fadein 1.0         # PLACEHOLDER — urgent dream theme

    show magnus normal at center_char, dream_haze_in  # PLACEHOLDER — no magnus sprite declared
    magnus "DRAGONKIN…. DRAGONKIN!!"

    "I gasped, my breath sharp and ragged as I jolted awake. There he was—the winged man again."
    camera at bigshake(5.0, rate=0.020, time=0.09), shattered_glass_transform
    with shattered_glass_transition
    "The blinding white void collapsed like fragile glass, breaking inward, dissolving into wisps of fading light."
    camera
    scene underground_magnus with Dissolve(0.5)
    "The air hit me like a wave—thick, humid, ancient. It reeked of damp moss, of something metallic and bitter, of rot buried deep within the earth."
    "A cavern stretched before me, vast and endless. Stalagmites jutted from the ground like jagged teeth, and the walls shimmered faintly."
    "But it was the door that held me still. It loomed before me—massive, stretching high into the abyss, forged of simple stone yet impossibly ancient."
    "The carvings on its surface were impossibly delicate, intricate to the point of madness—a magnificent dragon, its body coiling through storm-wracked clouds. The Prosperity Dragon."
    "Magnus' fingers dug into my shoulders, desperate, clawing."
    "His golden eyes burned with an unnatural glow, his large white wings twitching, restless, afraid. Cracks spiderwebbed through his feathers, glowing faintly at the edges."

    show dorian serious at left_char
    show magnus alt_anger at right_char
    with Dissolve(0.2)
    magnus "They're here… Dragonkin. Help me! Please!"

    "And then—I felt it. Something watching. Something waiting."
    "A presence, slow and hungry, like a massive, slumbering beast curling in its den, exhaling long, rattling breaths through jagged fangs."

    show dorian angry at left_char 
    dorian "Magnus!"

    magnus "You have to hurry—no, no, no, listen to me, Dorian! This isn't a warning anymore—IT'S HERE!"

    "The cracks in his feathers deepened. The cavern trembled. Stone dust rained down from above." with hpunch
    "The air was heavier now—thick with something unseen, something pressing against my ribs, my throat, my skull."

    yk "Dragonkin… Dragonkin…"

    "It was low. Hungry. Smiling. Like it knew I was there. Like it knew my name."
    "I felt my blood turn to ice."

    show dorian serious at left_char
    dorian "Magnus! What in Tetrad's name is happening? What's behind that door?!"

    "Then Magnus became quiet."

    show magnus normal at right_char with Dissolve(0.1)
    magnus "There's no time. The seal—it's WEAKENING. I don't know how, but something—someone—has started to undo it!"
    show magnus alt_shocked at right_char with Dissolve(0.1)
    magnus "If it breaks—if it breaks, Dorian, I… I—"

    "The stone splintered. Something on the other side moved."

    show magnus alt_anger at right_char with Dissolve(0.1)

    magnus "PLEASE! HURRY! I don't think I can last much longer—Please—!!"

    show dorian normal_alt_tense at left_char with Dissolve(0.1)
    "Then, I felt pain."
    "Magnus screamed. His entire body convulsed as unseen forces ripped at him, as if his very essence was being torn apart."
    "His wings, so brilliant and white before, fractured, black veins crawling along his feathers like spreading rot."

    magnus "AHHHH!!!"

    show dorian angry at left_char with Dissolve(0.1)
    dorian "MAGNUS!!"

    "He reached for me, and I reached out for him. But before I could grasp him, he was yanked away."
    "The world around me shattered." with hpunch

    # =============================================================================
    # WAKE UP — Cheng Industries Bunker
    # =============================================================================

    scene cheng_industries_bunk with fade             # PLACEHOLDER — Cheng Industries bunker
    stop music fadeout 1.0
    # play music ost_ch7_bunker fadein 2.0        # PLACEHOLDER — quiet tense bunker theme
    # play audio amb_bunker loop fadein 1.5       # PLACEHOLDER — bunker ambient

    "I woke up gasping."
    "Cold sweat clung to my skin, my breath coming in short, uneven bursts. My body was tense, hands clenched like I had tried to hold onto something."
    "A soft whirring sound broke the silence."
    "I turned my head sharply, still disoriented, and was immediately greeted by the glow of a blue-tinted screen."
    "A small hovering delivery bot floated beside me, its screen flickering before revealing a familiar face."

    show supply_robot normal at right_supply
    show dorian serious at left_char
    with Dissolve(0.2)
    yuxuan "Had another dream, Dorian buddy?"

    "His usual teasing tone was there, but the way his brows furrowed told me he already knew the answer."
    "I blinked, my thoughts sluggish. I rubbed my palms against my face."
    show supply_robot normal at center_supply
    show weng normal at right_flip 
    with Dissolve(0.2)
    weng "Here Master Dorian, drink this."

    "I barely registered her presence before a warm ceramic cup was pressed into my hands. The scent of bitter herbs and a whiff of honey drifted into my nose."
    "We were deep within the hidden bunker beneath Cheng Industries, a makeshift sanctuary carved into the underbelly of Tianho. The space was dimly lit, filled with the quiet sounds of the wounded."
    "Scattered around the room, soldiers and civilians alike lay on makeshift beds, some wrapped in bloodied bandages, others slumped in exhaustion."

    "I took the teacup that Weng held out to me."

    show dorian neutral at left_char with Dissolve(0.1)
    dorian "Thank you, Miss Weng."

    show weng happy at right_flip with Dissolve(0.1)
    weng "You must be parched from the battle earlier. I really have to thank you for being concerned about an old woman like me."

    yuxuan "Weng told me about the Hundun. And when I heard, well—by the Prosperity Dragon, I was mortified! What in the world was an extinct creature doing here?!"

    show weng normal at right_flip with Dissolve(0.1)
    weng "His Majesty told Sir Niko, Sir Svante, and me. At first, we didn't believe him. Until Tim backed him up."
    weng "And then we went outside and saw the body."

    show dorian serious at left_char
    dorian "Yu, how's Elias?"

    "Yuxuan opened his mouth to respond, but before he could—"

    hide weng
    hide supply_robot
    show tedda_human at right_char 
    show roboto happy at center_robot
    with Dissolve(0.2)
    tedda "Master Doriaaaann! Lady Elias is sleeping soundly! You have nothing to worry about! She is—"
    roboto "Miss Tedda, please lower your voice."
    tedda "Oh… Sorry, Roboto. Whoopsiee…"

    hide tedda_human
    hide roboto
    show supply_robot base at right_supply 
    with Dissolve(0.2)
    "Yuxuan sighed, but a smirk tugged at the corner of his lips."

    yuxuan "Well, you heard it, buddy. Elias is fine."

    show dorian neutral at left_char
    "I nodded but barely acknowledged their words. My mind was still back in the dream. The cavern. The door."

    jump ch7_dream_debrief


# =============================================================================
# SECTION 6: LABEL CH7_DREAM_DEBRIEF — Bunker Dream Debrief with Group
# =============================================================================

label ch7_dream_debrief:

    show dorian serious at left_char 
    show supply_robot lied at right_supply 
    with Dissolve(0.1)
    dorian "Yu… I have to tell you something."

    "The room hushed slightly. I took a breath and told them everything."
    "I told them how the white void cracked apart, breaking like shattered glass until I stood in an ancient underground cavern."
    "I told them about the winged man - Magnus. How his white wings streaked with cracks of light. How he would always call me every now and then."
    "How he had grabbed me, shook me, and yelled my name in desperation. He told me that the seal was weakening. That someone—or something—was undoing it."
    "When I finished speaking, a heavy silence settled over between the three of us."

    show supply_robot lied at center_supply 
    show weng normal at right_flip with Dissolve(0.2)
    weng "By the stars… Is that what happened in your dream?"

    yuxuan "A winged man? Preposterous. We—"

    hide weng
    show niko normal_base at right_char with Dissolve(0.2)
    niko "A winged man, you said?"

    "I turned just in time to see him striding over, his coat slightly disheveled from tending to the injured."
    "In one gloved hand, he held a scalpel, the blade still stained with antiseptic, while his other hand balanced a tray of rolled bandages and a mortar filled with crushed medicinal herbs."

    hide niko
    show svante normal_neutral at right_char with Dissolve(0.2)
    svante "Sir Dorian, you're awake."

    "The violet-haired Aldorith lifted his head. He set down the cloth and stood, striding toward us."

    svante "Me and Sir Niko hurried to get here when we learned that the monsters attacked Tianho."

    show supply_robot normal at center_supply with Dissolve(0.1)
    yuxuan "If it wasn't for them, almost half of the wounded here might have died."

    hide svante
    show weng normal at right_flip with Dissolve(0.2)
    weng "Such amazing gentlemen. I appreciate your help."

    "Weng looked at Svante and Niko. But Niko's gaze locked onto me, sharp and unyielding."

    hide weng
    show niko normal_serious at right_char with Dissolve(0.2)
    niko "Describe the winged man to me. Every detail."

    "I hesitated. Something about the intensity in his voice—like he wasn't just curious, but searching for something."
    show dorian normal_alt_calm at left_char with Dissolve(0.1)
    "I told him. About Magnus' white wings. Brown hair. His golden eyes. The cracks of light streaking through them. His panic. His urgency. The cavern, and the growl beneath it."
    show dorian serious at left_char 
    show niko alt_tense at right_char
    with Dissolve(0.1)
    "Niko listened in silence. He didn't even blink. Then, his grip on the scalpel tightened."
    "Svante's brows twitched slightly."

    hide niko
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "But… That can't be."

    hide svante
    show niko normal_serious at right_char with Dissolve(0.2)
    niko "Are you certain that wasn't a premonition of the Death God?"
    niko "It must be a sign from Enoch himself! I implore you, tell me more about this dream! Is it telling you to go somewhere? I will follow you, Dorian!"

    "I opened my mouth to respond, but before I could—"

    show supply_robot base at center_supply 
    yuxuan "Oh, here we go…"
    yuxuan "Niko, I think you'd love any excuse to bring up Enoch."

    show niko normal_ignore at right_char with Dissolve(0.1)
    niko "…"

    show dorian neutral at left_char
    "Niko shot him a glare but turned back to me, the intensity in his expression unwavering."

    show niko normal_serious at right_char
    niko "You described a man with wings. The golden eyes is a dead giveaway."

    show supply_robot sad at center_supply with Dissolve(0.1)
    yuxuan "Oh, come on. You're reading into this a little too much. Not everything is about your Death God, Niko. Dreams happen all the time!"

    "Yuxuan's image flickered with animation."
    
    show supply_robot lied at center_supply with Dissolve(0.1)
    yuxuan "Why, just last week, I dreamt that I had only eaten one piece of chocolate, but when I turned around—bam!—I was surrounded by an entire mountain of Hinami treats! And naturally, I ate all of them."

    hide niko
    show weng happy at right_flip with Dissolve(0.2)
    weng "That's such a lovely dream, Master Yuxuan. You are incomparable and you are such a visionary!"

    show supply_robot base at center_supply with Dissolve(0.1)
    yuxuan "Awww thank you so much, Miss Weng!"

    hide weng
    show niko normal_ignore at right_char with Dissolve(0.2)
    niko "*groans* Ugh…"

    yuxuan "Now tell me, Niko. Should I be preparing for an avalanche of delectable confections from Hinami to be given to me by the magnificent Prosperity Dragon? Because, if so, I need to grab my finest fork and plate!"

    show niko alt_annoyed at right_char with Dissolve(0.1)
    niko "What? That's just ridiculous, Yuxuan."

    hide niko
    show svante normal_happy at right_char with Dissolve(0.2)
    svante "Now that you mention it, that sounds like a wonderful dream, Sir Yuxuan." 
    show svante alt_funny at right_char with Dissolve(0.1)
    svante "I once dreamt that I stood in a field of violet flowers! I was barefoot, and the earth beneath me was warm! And for the first time, I felt… light."

    show supply_robot normal at center_supply with Dissolve(0.1)
    yuxuan "See?! Dreams are harmless!"

    hide svante
    show niko normal_anger at right_char with Dissolve(0.2)
    niko "That's not what I'm talking about, Yuxu—"

    hide niko
    show weng normal at right_flip with Dissolve(0.2)
    weng "I remember dreaming of stirring a lovely kettle and the entire city of Tianho gathered around—each of them drinking from it."

    hide weng
    show svante normal_happy at right_char with Dissolve(0.2)
    svante "Wow… That really fits you, Miss Weng."

    hide svante
    show niko normal_ignore at right_char with Dissolve(0.2)
    niko "You're all missing the point… Enoch, help me."

    show dorian serious at left_char with Dissolve(0.1)
    dorian "I… I need to find him. Magnus said he's in Tianho—but I have no damn clue where."

    show niko normal_serious at right_char with Dissolve(0.2)
    "Niko straightened, nodding. I blinked."

    show dorian neutral at left_char
    dorian "You sure?"

    show niko normal_serious at right_char
    niko "I believe this isn't just some cryptic dream, Dorian. Something is happening."

    "I ran a hand through my hair, taking a slow breath."

    niko "Tell me—was there anything else in your dream? Something distinct?"

    show dorian normal_alt_calm at left_char with Dissolve(0.1)
    "I closed my eyes for a moment, trying to recall every detail. Think, Dorian, think. Then, it hit me."

    show dorian neutral at left_char with Dissolve(0.1)
    dorian "There was a massive door. It was made of simple stone… but it bore an amazing illustration of the Prosperity Dragon. The details were immaculate, almost like I was looking at the dragon himself."

    show supply_robot lied at center_supply with Dissolve(0.1)
    yuxuan "A massive door… Intricate illustration of the Prosperity Dragon…"

    "I turned to the delivery bot as Yuxuan's face flickered on the screen. His usual playfulness was gone, replaced with a calculating look."

    show supply_robot base at center_supply with Dissolve(0.1)
    yuxuan "I think I know where that is."

    show dorian serious at left_char
    "My breath hitched."

    dorian "You do?"

    yuxuan "I'm not completely sure yet. But if my guess is right, there's only one place in Tianho that fits that description."

    show niko alt_tense at right_char with Dissolve(0.1)
    niko "Isn't the Prosperity Dragon the main deity of Tianho? Surely there are hundreds of places with illustrations of it."

    hide niko
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "Huh? The main deity? I was certain I saw a shrine for the Tetrad here in Tianho a while ago."

    hide svante
    show weng alt_close_eyes at right_flip with Dissolve(0.2)
    weng "Those are for the tourists that will be coming for the Tragedy's fifth anniversary tomorrow."

    hide weng
    show svante normal_neutral at right_char with Dissolve(0.2)
    svante "Oh… That makes a lot of sense, mam."

    yuxuan "Trust me. I'll explain. Get back to the lab. I'll lead you there once you arrive."

    hide svante
    show niko normal_base at right_char with Dissolve(0.2)
    niko "Fine."

    show dorian neutral at left_char
    "I nodded, already feeling the adrenaline creeping back in."

    hide niko
    show svante normal_happy at right_char with Dissolve(0.2)
    svante "If it's not a bother. I'd love to join if Sir Niko's coming."

    show dorian neutral at left_char with Dissolve(0.1)
    dorian "You sure? You don't have to come."

    show svante normal_neutral at right_char with Dissolve(0.1)
    svante "If you're heading toward danger, I would like to help, sir. It's the least I can do."

    hide svante
    show niko normal_ignore at right_char with Dissolve(0.2)
    niko "*sighs* Knock yourself out."

    show niko normal_base at right_char with Dissolve(0.1)
    "Niko wiped his hands on a clean cloth before turning toward the injured."

    niko "Give me a few minutes, Dorian. I need to finish treating the wounded first."

    hide niko
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "I… I'll help too, Sir Niko. W-Wait!"

    hide svante
    show niko normal_base at right_char with Dissolve(0.2)
    niko "Hurry up."

    hide niko
    show weng normal at right_flip with Dissolve(0.2)
    yuxuan "Miss Weng, how's medical supply stock? How are the wounded?"

    weng "We have plenty in reserve, Master Yuxuan. Right this way."

    hide weng
    hide supply_robot

    show dorian serious at left_char with Dissolve(0.1)
    "As the others scurried along, I was left alone with my thoughts."
    "The weight of the dream still clung to me, even now. Magnus' voice, the panic in it—it hadn't been just a dream."
    show dorian normal_alt_calm at left_char with Dissolve(0.1)
    "I crossed my arms, shifting my weight."
    "For now, all I could do was wait."
    scene cheng_industries_bunk with fade
    pause 2.0 
    show dorian normal_alt_tense at left_char with Dissolve(0.1)
    "…But after a few minutes, I was getting restless."
    show dorian neutral at left_char with Dissolve(0.1)
    "Maybe I could spend some time with someone. But who?"

    jump ch7_waiting


# =============================================================================
# SECTION 7: LABEL CH7_WAITING — Choices: Spend Time While Waiting
# =============================================================================

label ch7_waiting:
    # play music ost_ch7_warm fadein 1.5          # PLACEHOLDER — warm subdued theme

    menu:

        "Spend time with Svante.":
            $ ch7_d1_choice = "svante"
            $ svante_affection += 2
            jump ch7_svante_time

        "Help Niko with the patients.":
            $ ch7_d1_choice = "niko"
            $ niko_affection += 2
            jump ch7_niko_time

        "Look for Chung-hee.":
            $ ch7_d1_choice = "chunghee"
            $ chunghee_affection += 2
            jump ch7_chunghee_time

        "Check the remaining supplies with Yuxuan.":
            $ ch7_d1_choice = "yuxuan"
            $ yuxuan_affection += 2
            jump ch7_yuxuan_time


# =============================================================================
# SECTION 8: LABEL CH7_SVANTE_TIME — Spend Time with Svante
# =============================================================================

label ch7_svante_time:

    scene cheng_industries_bunk with dissolve         # PLACEHOLDER — bunker interior

    show svante normal_nervous at right_char with Dissolve(0.2)
    "I entered the room to my left. My gaze flickered to Svante—he was struggling."
    "The violet-haired Aldorith stood by a table of medical tools, his expression utterly lost."
    "His long fingers hovered over a scalpel, then a syringe, then a roll of bandages—clearly unsure what to do with any of them."
    "I sighed, stepping over."

    show dorian neutral at left_char with Dissolve(0.2)
    dorian "You look like you're about to perform a heart surgery, Svante."

    "He jumped slightly, nearly knocking over a jar of ointment."

    show svante normal_sad at right_char with Dissolve(0.1)
    svante "N-No, sir! I w-wouldn't dream of it!"

    "He quickly straightened, holding up a small glass bottle filled with clear liquid. His brows furrowed as he inspected the label like it might hold a hidden trap."

    svante "There's this little girl who was wounded by a yaoguai, and I'm trying to look for something that can clean the wound."

    show svante normal_neutral at right_char  with Dissolve(0.1)
    svante "This says, 'antiseptic'. But I don't know what it does."

    show dorian neutral at left_char with Dissolve(0.1)
    dorian "It's fine. Antiseptic cleans wounds. Prevents infection, that sort of thing."

    show svante normal_happy at right_char with Dissolve(0.1)
    svante "Really, sir?"

    "Relief flooded his features. Then, just as quickly, he frowned again."

    show svante normal_neutral at right_char with Dissolve(0.1)
    svante "I was worried that it might be poison. I don't want anyone's flesh dissolving on my watch."

    "I choked on a laugh."

    show dorian smile at left_char with Dissolve(0.1)
    dorian "Who would mix poison with medical supplies?"

    show svante normal_nervous at right_char with Dissolve(0.1)
    svante "Y-You never know, sir! Back in Mjoll, I don't have much experience with all this medical stuff."

    show dorian neutral at left_char with Dissolve(0.1)
    "He waved a hand vaguely at the shelves filled with neatly arranged vials and bandages."

    svante "Us guy Aldoriths tend to stick to the battlefield."

    show dorian normal_alt_annoyed at left_char with Dissolve(0.1)
    "That part didn't surprise me. Aldorith warriors were known for their resilience in combat, their strict traditions. If you weren't patching up wounds in the middle of a war zone, you probably weren't learning medicine at all."
    show dorian normal at left_char with Dissolve(0.1)

    dorian "Then why are you helping Niko?"

    show svante alt_guilty at right_char with Dissolve(0.1)
    "Svante rubbed the back of his neck, looking sheepish."
    svante "He needed an assistant, sir. And... I figured, since I'm a metal channeler, I could be useful somehow."

    "He hesitated, then raised his hand. A soft hum filled the air as faint metallic glimmers flickered along his fingertips."

    show svante alt_base at right_char with Dissolve(0.1)
    svante "See, I can use my metal channeling to bend surgical tools into shape if they break or dull too fast."

    show dorian neutral at left_char with Dissolve(0.1)
    "To demonstrate, he picked up a pair of tweezers that had a slightly bent tip. With a careful touch, he straightened them out, the metal shifting smoothly beneath his fingertips."

    svante "I can also clean instruments really well. Niko told me that sterilization is important, so..."

    "He gestured toward a tray of scalpels and forceps, all gleaming under the lantern light."
    "He must have used his ability to strip them of any impurities, making them practically spotless."

    "I raised a brow."

    dorian "That's actually really useful."

    show svante alt_weird at right_char with Dissolve(0.1)
    svante "Y-You think so?"

    "His ears burned red, and he fidgeted with the antiseptic bottle."

    show svante normal_sad at right_char
    svante "I was just trying to be helpful. My sister Kristin was the real healer in the family. She always patched me up whenever I got hurt when we were kids."

    "His voice softened at the mention of her, his eyes growing distant."

    show dorian normal_alt_neutral at left_char with Dissolve(0.1)
    dorian "She sounds like she was good at what she did."

    show svante normal_sad at right_char
    svante "She was amazing. Mom and I loved her."
    svante "I remember one time during my birthday, she made me a snow-violet cake."

    show dorian neutral at left_char with Dissolve(0.1)
    "I raised a brow."

    dorian "Oh, so she's a baker?"

    show svante alt_funny at right_char with Dissolve(0.1)
    svante "Haha. No, sir. Not even close. But she did her best."
    svante "She made it so she and I could celebrate with Mom. Even if it was a little lopsided and too sweet, it was the best cake I ever had."

    show dorian smile at left_char with Dissolve(0.1)
    dorian "You're right. She does sound amazing."
    show dorian neutral at left_char with Dissolve(0.1)

    show svante normal_sad at right_char with Dissolve(0.1)
    svante "Kristin… Mom…"

    "For a moment, he lingered in the memory, and a small nostalgic smile played at his lips but then he caught himself, clearing his throat."

    show svante normal_nervous at right_char with Dissolve(0.1)
    svante "M-Merciful Enoch… Look at me rambling."

    "He straightened, gripping the bottle a little tighter."

    svante "A-Anyway, I should probably bring this to Sir Niko before I waste more time."

    "He turned to go but then hesitated, glancing back at me."

    show svante normal_happy at right_char with Dissolve(0.1)
    svante "T-Thank you, sir Dorian. I would've overthought this for another ten minutes if you hadn't come in."

    show dorian normal at left_char with Dissolve(0.1)
    "I smirked."

    dorian "Not a problem. But are you sure you want to come with me and Niko to search for Magnus? You don't have to."
    show dorian normal_alt_neutral at left_char with Dissolve(0.1)

    svante "Y-Yes, sir! I really do want to help. I—"

    show niko normal_base at center_char with Dissolve(0.2)
    niko "Svante, did you get the antiseptic for the yaoguai bite?"

    show svante normal_nervous at right_char with Dissolve(0.1)
    svante "S-Sir Niko! C-Coming!"

    show svante normal_base at right_char with Dissolve(0.1)
    svante "See you later, sir Dorian."

    hide svante
    hide niko 
    with Dissolve(0.1)
    "He gave a firm nod, then hurried off, the antiseptic bottle clutched tightly in his hands."

    jump ch7_waiting_common

# =============================================================================
# SECTION 9: LABEL CH7_NIKO_TIME — Help Niko With the Patients
# =============================================================================

label ch7_niko_time:

    scene cheng_industries_bunk with dissolve         # PLACEHOLDER — bunker medical station

    "I stepped toward the heart of the medical station, where soldiers lay on makeshift cots beneath the dim warm glow of lanterns."
    "The air was thick with the scent of antiseptic, fresh herbs, and the underlying metallic tang of blood."
    "It was busier than I'd expected—soldiers and volunteers lay on cots or sat against crates, some wrapped in bloodied bandages, others groaning as healers worked tirelessly."

    show soldier_jiang at right_flip
    show dorian normal_alt_neutral at left_char
    with Dissolve(0.2)
    "I spotted Jiang, crouching beside a soldier with a deep gash on his leg. He looked up as I approached and gave me a quick wave."

    jiang "Paladin Dorian. You're safe. Thank the Prosperity Dragon."

    "His gaze flicked over my clothes, as if checking for wounds."

    jiang "You don't seem to be wounded. I take it you're here to help?"

    show dorian neutral at left_char with Dissolve(0.1)
    dorian "Yeah. You look like you could use a few extra hands. Where's Gao and Tim?"

    jiang "Gao's outside, patrolling the entrance. Tim's with Miss Weng, helping with supplies."

    "A pained voice interrupted us—a woman, her voice barely above a whisper."

    woman_2 "S-Sir! P-Please… It hurts…"
    woman_2 "I was hurt by a caught by a yaoguai when… Ughhh…"

    show soldier_jiang at right_flip
    jiang "On it, miss! See you later, Paladin."

    hide soldier_jiang with Dissolve(0.1)
    "I gave a brief nod, then scanned the room."

    show niko normal_base at right_char with Dissolve(0.2)
    "Niko was at the center of it all, hands steady as he stitched a deep wound on a soldier's arm."
    "Around him, vibrant green medicinal plants flourished in patches of soil—his nature channeling at work."
    "Leaves rustled, and fresh herbs sprouted as if responding to his focus, their natural properties easing pain and hastening recovery."

    "Niko barely glanced up as I approached."
    show niko normal_serious at right_char with Dissolve(0.1)
    niko "If you're here to help, take a pair of gloves from that crate and get to work."
    niko "And watch your step. There are vines near your feet—I'd rather not have a patient and a Paladin to heal tonight."

    "I grabbed a pair and pulled them on, stepping toward the injured soldier."

    dorian "What do you need, Niko?"

    show niko normal_base at right_char with Dissolve(0.1)
    niko "Keep pressure on this wound while I stitch it up."

    "The soldier winced as I applied pressure. He was a young man—early twenties, maybe—with dark hair matted to his forehead."

    male_soldier_ch7 "T-Thank you, sir..."

    show dorian normal_alt_neutral at left_char with Dissolve(0.1)
    dorian "Hang in there."

    male_soldier_ch7 "I knew it'd be tough, but I didn't think it'd be this bad…"

    show niko normal_base at right_char with Dissolve(0.1)
    niko "The wound will heal soon. Don't worry, sir."
    niko "Now, please relax and stay still."

    "With a flick of his wrist, he reached for a vial of clear liquid—one of Cheng Industries' medical innovations."
    "He uncorked it, allowing a single drop to land on the wound. The liquid shimmered for a moment before seeping into the soldier's skin."
    "A reaction followed instantly. The raw, gaping tear knit itself together at an unnatural speed, reducing to a red scar within seconds."
    "The soldier's breathing steadied, his pain lessening as Niko's nature channeling took over."

    show niko alt_base at right_char with Dissolve(0.1)
    niko "Feeling any pain, sir?"

    male_soldier_ch7 "N-no, sir."

    niko "Good. Please continue to relax."

    "The medicinal plants growing around them responded to his call. A cluster of leaves twitched before unfurling, releasing a faint, sweet aroma."
    "The air changed—thick with the scent of crushed herbs and damp earth. The soldier's body relaxed, the natural anesthetic properties dulling his agony."

    male_soldier_ch7 "That's… incredible."
    
    show niko alt_base at right_char with Dissolve(0.1)
    niko "Side effects may include dizziness. So don't be surprised if you're seeing stars now."

    male_soldier_ch7 "My father was a jeweler before this…"

    show niko normal_smile at right_char with Dissolve(0.1)
    niko "That's great to hear. Jewelry is a profitable trade here in Tianho."
    show niko alt_base at right_char with Dissolve(0.1)

    show dorian neutral at left_char with Dissolve(0.1)
    dorian "Where is he now?"

    male_soldier_ch7 "The… The tragedy of Tianho happened. We lost everything."

    show niko normal_sad at right_char with Dissolve(0.1)
    niko "I'm sorry to hear that."

    "The soldier's voice hardened, and his fingers curled into fists."

    male_soldier_ch7 "Damn that wretched Death God and his rotten followers. They deserve worse than death."

    show niko alt_annoyed at right_char with Dissolve(0.1)
    niko "…"
    show dorian serious at left_char with Dissolve(0.1)
    dorian "…"

    "I saw it—the subtle shift in Niko's expression. It was quick, barely perceptible, but it was there."
    "His shoulders tensed just slightly before relaxing again. His jaw clenched, his focus dropping back to his work."

    male_soldier_ch7 "Damn lunatics… They're the reason our city was destroyed."
    male_soldier_ch7 "If I ever see one of those damned prophets… By the Prosperity Dragon's name, I don't know what I'll do."

    show niko normal_base at right_char
    "Niko remained silent, his expression unreadable as he tied off the bandage with practiced precision."
    "When he finally spoke, his voice was carefully measured."

    niko "There. You should be good now."

    "He adjusted the bandage one last time, ensuring it was snug but not restrictive."

    niko "Your bandages are secure. We closed the wound, but still, try not to move too much."

    "With a quiet, deliberate motion, he reached for a cloth and gently placed it over the soldier's eyes."

    niko "I want you to rest. Your body needs time to recover from closing the wound."

    "The soldier's breath slowed. Within moments, he was out."
    "Niko straightened, rolling his shoulders as he scanned the room. Jiang approached, carrying a box filled with ointments."

    hide dorian
    show soldier_jiang at left_char with Dissolve(0.2)
    jiang "Doctor Niko, my men and I can take over from here. The Paladins have arrived. We'll handle the rest."

    show niko normal_base at right_char with Dissolve(0.2)
    niko "Make sure they stay hydrated. Even with the medicine, their bodies need strength to heal."
    niko "And most importantly—don't let them push themselves. I don't care how much better they say they feel."

    hide soldier_jiang 
    show dorian normal_alt_neutral at left_char 
    show niko alt_disappointed at right_char
    with Dissolve(0.2)
    "Niko exhaled quietly. Then, without another word, he turned and walked toward the far end of the hideout, slipping into a small, solitary room."
    "I followed."
    "The moment he stepped inside, his shoulders sagged slightly, the tension bleeding out of him as he approached a wooden table."
    "I leaned against it, watching him."

    show dorian neutral at left_char
    dorian "…I was surprised you didn't say anything, Niko."

    show niko normal_ignore at right_char with Dissolve(0.1)
    niko "I doubt it would have changed anything, Dorian."
    show niko normal_base at right_char with Dissolve(0.1)
    niko "Besides, if you're in my profession you'll need to grow a thick skin."

    "He didn't look at me, but I could see it in the way his hands curled into loose fists, the tension in his jaw, the flicker of something unreadable in his eyes."
    "A doctor's duty was to heal, not to pass judgment. But that didn't mean he wasn't affected."
    "Outside, muffled voices drifted in from the infirmary."
    "The low murmur of people speaking in hushed tones, the occasional rustling of bandages, the soft scrape of boots against the wooden floor."
    "Through the half-open door, I caught a glimpse of the makeshift ward—rows of injured soldiers quietly lying on worn cots, some resting, others grimacing as volunteers carefully wrapped fresh bandages around their wounds."

    show dorian serious at left_char with Dissolve(0.1)
    dorian "Damn those yaoguai…"

    show niko alt_base at right_char with Dissolve(0.1)
    niko "We're still on later, right? I apologize for making you wait."

    show dorian neutral at left_char
    dorian "Yes, we're still on."

    pause 1.5 

    "A pause. I glanced toward the doorway again, watching as a young volunteer carefully adjusted a soldier's sling, murmuring reassurances as she worked."
    "Others bustled around, distributing water, tending to wounds, keeping the place running."

    dorian "Take your time. You did well today."

    show niko alt_base at right_char with Dissolve(0.1)
    niko "Thank you. This won't be long. We've already patched up most of them."

    "I studied him for a moment, debating whether to press further."

    show dorian neutral at left_char with Dissolve(0.1)
    dorian "Want me to help?"

    show niko normal_smile at right_char with Dissolve(0.1)
    niko "No need. *chuckle* Though if you can, maybe fill that pitcher with water."

    "His voice was lighter now, a flicker of warmth cutting through the exhaustion."
    "I pushed off the table, grabbing the empty pitcher from a nearby shelf."

    niko "Thanks Dorian."

    hide niko 
    show dorian normal_alt_neutral at left_char 
    with Dissolve(0.2)
    "I nodded and turned to leave. As I stepped out, I glanced back one last time. "
    "Niko stood there, his head bowed slightly, his hands still resting against the table."

    jump ch7_waiting_common


# =============================================================================
# SECTION 10: LABEL CH7_CHUNGHEE_TIME — Look for Chung-hee
# =============================================================================

label ch7_chunghee_time:

    scene cheng_industries_bunk with dissolve  # PLACEHOLDER — bunker entrance area

    "Restlessness gnawed at me, so I stood and wandered through the area, searching for someone to pass the time with."
    "Dim lanterns flickered along the uneven stone walls, casting elongated shadows that stretched and shrunk as soldiers and volunteers moved about."
    "The scent of damp earth mixed with burning oil and faint traces of medicinal herbs."
    "Near the entrance, I spotted Chung-hee, standing stiffly with his arms crossed, his usual unreadable expression firmly in place"
    "Beside him, Soldier Gao animatedly gestured with both hands, practically vibrating with excitement."
    "Tim, perched atop a wooden crate, swung his legs back and forth while nibbling on something that smelled suspiciously sweet."
    "I approached just in time to hear Gao yelling."

    show chunghee normal_neutral at left_char
    show soldier_gao at right_char 
    with Dissolve(0.2)
    gao "I still can't believe I actually met the Emperor of Kyeongjang! Do you know how rare that is? This is historic!"

    "He clapped his hands together, eyes gleaming."

    gao "I—I'm gushing! Someone pinch me! I must be dreaming!"

    show chunghee normal_neutral at left_char with Dissolve(0.2)
    chung_hee "You're overreacting, Sir Gao. Calm down."

    show dorian normal_alt_neutral at left_char
    show chunghee normal_neutral at center_char 
    with Dissolve(0.2)

    dorian "Chung's right, Gao. Keep your voice down. There are injured people resting."


    "Tim, without looking up from his snack, licked caramel off his fingers and chimed in."
    hide soldier_gao
    show chunghee normal_neutral at right_char 
    show tim normal at center_char_kids
    with Dissolve(0.2)
    tim "Technically speaking, it's not unprecedented."

    hide tim
    show soldier_gao at center_char with Dissolve(0.2)
    "Gao turned to him, eyes wide."

    gao "See?! Even Tim thinks it's a big deal!"

    hide soldier_gao
    show tim normal at center_char_kids with Dissolve(0.2)
    "Tim swallowed his last bite and wiped his mouth, his expression completely serious."

    tim "I never said it was a big deal, mister. I simply stated that, historically, rulers do occasionally engage in interactions with their subordinates."
    tim "However, the context and frequency of these occurrences would determine whether this situation qualifies as 'rare.'"

    hide tim
    show soldier_gao at center_char with Dissolve(0.2)
    "Gao blinked at him."

    gao "That… I didn't understand that…"

    "I stepped closer, and Gao immediately perked up, beaming."

    gao "Sir Dorian! That's right! You haven't tasted this one yet!"

    show dorian normal_alt_annoyed at left_char with Dissolve(0.1)
    "I raised an eyebrow."

    dorian "Taste what?"
    show dorian normal_alt_neutral at left_char with Dissolve(0.1)

    "Grinning, he held up a small, round clay dish filled with something golden, glossy, and smooth. It looked like flan—caramelized on top, thick and creamy—but the scent was richer, deeper."
    "A subtle hint of spice lingered in the air, something I didn't usually associate with a simple dessert."
    
    # TODO: check for food in assets
    gao "Tianho flan! My mom packed these for me before I left home. This one's still fresh. You gotta try it."

    show dorian neutral at left_char with Dissolve(0.1)
    dorian "Oh… How thoughtful…"

    hide soldier_gao
    show tim happy at center_char_kids with Dissolve(0.2)
    "Tim, having already finished his portion, wiped his mouth and grinned."

    tim "Mister Chung!! This is so delicious!"

    "He held up his tiny hands as if presenting an invisible award."

    tim "Acceptable texture! Balanced sweetness! The cinnamon infusion is an amazing addition!"

    hide tim 
    show soldier_gao at center_char with Dissolve(0.2)
    gao "You heard that? It's Tim-approved, Your Majesty! That means it's gotta be top-tier!"

    show chunghee alt_tense at right_char with Dissolve(0.1)
    "Chung-hee hesitated, his gaze shifting between the flan and Gao. He looked... almost wary."

    chung_hee "Well, um… If you're referring to the physical act of hearing what he said, kind sir, I haven't, since I'm deaf."
    chung_hee "But if you're referring to the understanding of what someone meant, then yes, I 'heard' him."

    "Chung-hee paused."
    
    show chunghee alt_neutral at right_char with Dissolve(0.1)
    chung_hee "…Does that make sense?"

    show soldier_gao at center_char with Dissolve(0.2)
    "Gao nodded rapidly, flustered."

    gao "Oh… Um… Right?"

    "Quickly recovering, Gao cleared his throat."

    gao "My mom makes the best desserts in Tianho, Your Majesty! You should visit her stall tomorrow at the anniversary—she sells out before the ceremony even starts every time!"

    show chunghee normal_neutral at right_char with Dissolve(0.1)
    chung_hee "That would be the anniversary of the Tragedy of Tianho, correct?"

    gao "Yes, sir! A lot of people buy them to leave at the graves of their families and loved ones. I'm sure they'd appreciate it! It's a small but sweet way to remember them."

    show chunghee normal_sad at right_char with Dissolve(0.1)
    "Chung-hee's gaze lowered slightly, fingers tightening around the small dish in his hands."

    chung_hee "Something for Father… Mother…"

    show dorian serious at left_char with Dissolve(0.1)
    "I studied him, sensing the shift in his mood like the dimming of a flame."

    dorian "Is something the matter, Chung?"

    show chunghee normal_neutral at right_char 
    show dorian neutral at left_char
    with Dissolve(0.1)
    chung_hee "Well… it's nothing, sir Dorian."

    hide soldier_gao 
    show tim happy at center_char_kids with Dissolve(0.2)
    "Tim perked up again, eyes sparkling."

    tim "I should tell Elias about this! That way, the two of us can eat—"

    show dorian serious at left_char with Dissolve(0.1)
    "I cut in sharply."

    dorian "(In Tetrad's name, please don't.)"

    show dorian neutral at left_char with Dissolve(0.1)
    "If Elias got involved, my money would vanish faster than a spark in the wind."
    "I took a bite of the flan Gao handed me. The caramel glaze melted smoothly, giving way to a thick, velvety center, subtly laced with cinnamon."
    show dorian normal_alt_confident at left_char with Dissolve(0.1)
    "It was richer than I expected—warm, sweet, and spiced just enough to make me take another slow bite."

    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "Meanwhile, Chung-hee still hadn't taken a bite."

    show dorian neutral at left_char with Dissolve(0.1)
    "He was holding his portion as if it were something fragile, staring at it like he expected it to bite him instead."

    hide tim
    show soldier_gao at center_char with Dissolve(0.2)
    gao "Pinch me, I must be dreaming! His Majesty will be eating my mother's flan!! AHHH!!"

    "There was a long, drawn-out silence."


    chung_hee "…"
    dorian    "…"
    tim       "…"
    chung_hee "…"

    show dorian neutral at left_char
    "I gave him a pointed look."

    dorian "You're supposed to eat it, you know."

    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "Chung-hee's shoulders tensed slightly."

    chung_hee "I… know that, Sir Dorian."

    hide soldier_gao
    show tim think at center_char_kids with Dissolve(0.2)
    "Tim tapped a tiny finger against his chin, studying him."

    tim "Mister Chung, you might be overthinking the consumption process."

    show chunghee normal_v2 at right_char with Dissolve(0.2)
    "Chung-hee finally took an exaggeratedly slow bite, chewing with stiff awkwardness. The moment stretched. "
    "His expression remained unreadable as ever, but he didn't immediately spit it out, which was a good sign."
    "After a moment, he swallowed and nodded slightly."

    show chunghee normal_happy at right_char with Dissolve(0.1)
    chung_hee "…It's amazing, actually."

    hide tim
    show soldier_gao at center_char with Dissolve(0.2)
    "Gao let out a victorious cheer."

    gao "HA! I KNEW IT!"

    hide soldier_gao
    show tim happy at center_char_kids with Dissolve(0.2)
    "Tim clapped his hands."

    tim "Sensory approval has been achieved!"

    hide tim happy
    show dorian smile at left_char
    with Dissolve(0.1)
    "I smiled at Chung-hee, and after a beat, he smiled back."

    scene bg_tianho_city_night with fade
    "We stood together at the entrance, the quiet hum of the camp surrounding us."

    show dorian neutral at left_char
    show chunghee alt_neutral at right_char
    with Dissolve(0.2)
    "Lantern light flickered against the stone, shadows stretching and shrinking with each movement."
    "The warmth of the flan lingered on my tongue, and for a while, the weight in the air felt just a little lighter."

    jump ch7_waiting_common

# =============================================================================
# SECTION 11: LABEL CH7_YUXUAN_TIME — Check Supplies with Yuxuan
# =============================================================================

label ch7_yuxuan_time:

    scene cheng_industries_bunk with dissolve         # PLACEHOLDER — bunker supply area

    "The area was a little quieter now, the sounds of groaning wounded and hurried footsteps fading into a dull hum."
    "I made my way past rows of flickering lanterns toward the supply area, where Weng—her white dress pristine despite the chaos—was meticulously arranging bottles of medicine."
    "She glanced up when she saw me."
    show weng normal at right_flip 
    show dorian neutral at left_char
    with Dissolve(0.2)

    weng "Ah, Sir Dorian. How are you faring?"

    dorian "Just came to help, Miss Weng. What's the situation? Where's Yu?"

    show weng alt_base at right_flip with Dissolve(0.1)
    weng "Master Yuxuan's probably taking care of something in the lab right now. He asked me to take stock of the supplies."

    "She gestured toward a crate stacked high with neatly labeled boxes, all bearing the crest of Cheng Industries."
    "Their sleek packaging stood out against the more standard medical kits. The name was printed in bold lettering:"
    "\"Cheng Industries\""
    "There were rolls of self-adhesive bandages, burn ointments that absorbed instantly, and even auto-suture kits for rapid wound closure."
    "Expensive, cutting-edge supplies, leagues beyond the rough linen and herbal pastes most medics had to work with."

    dorian "This is all from Cheng Industries?"

    show weng thinking at right_flip with Dissolve(0.1)
    weng "Indeed, sir Dorian. While Sir Niko's salves and organic supplies have helped tremendously, more than half of our treatments tonight have relied on supplies from Cheng Industries."
    # TODO: check for line changes
    weng "The automated injectors for pain relief from yaoguai bites, the clotting agents for deep wounds, even the regenerative salves for burns—it's all Cheng Industries. If we didn't have them, we'd be in a much worse position."

    show dorian serious at left_char with Dissolve(0.1)
    "I frowned slightly. That meant a huge amount of their stock had already been used. That also meant…"

    show weng normal at right_flip with Dissolve(0.1)
    weng "Like I said, Master Yuxuan is very busy. He's waiting for a report, but he's not responding to any of my voice messages."
    show weng happy at right_flip with Dissolve(0.1)

    weng "But you're free to leave a voice message, Sir Dorian."

    show dorian normal at left_char with Dissolve(0.1)
    dorian "Might as well."

    show weng normal at right_flip with Dissolve(0.1)
    "She pressed a button on the delivery drone hovering beside her. She motioned me to speak."

    show dorian neutral at left_char with Dissolve(0.1)
    dorian "Hey Yu. While I'm waiting on Niko to finish with his duties here, I—"

    show supply_robot base at center_supply with Dissolve(0.2)
    "I wasn't able to finish my sentence when the machine projected a hologram—and in the shimmering blue light, Yuxuan appeared."
    "His hair was a little messy and he pushed books out of the way."

    "Yuxuan's image flickered into view—slightly disheveled, a mess of books and equipment surrounding him."
    "His normally sleek hair had a few stray strands sticking out, and there was ink smudged on his fingers."

    show supply_robot normal at center_supply with Dissolve(0.1)
    yuxuan "Dorian, buddy! How are you? S-Sorry for the mess. I didn't know you would be calling me."

    "He waved a hand at the air, flustered, as if trying to push the scattered notes and tools off-screen."
    "I raised an eyebrow."

    show dorian normal_alt_neutral at left_char with Dissolve(0.1)
    dorian "I'm sorry, Yu. Do you need a moment?"

    show supply_robot lied at center_supply with Dissolve(0.1)
    yuxuan "NO— I mean YES— I mean—"

    "He sucked in a sharp breath, then smoothed a hand down his robe in a poor attempt to compose himself."

    dorian "Are you sure? You look busy. I can just—"

    yuxuan "I don't look busy! I take offense to that!"

    show dorian smile at left_char with Dissolve(0.1)
    "I let out a quiet chuckle. Weng sighed."

    show weng sad at right_char with Dissolve(0.1)
    weng "Master Yuxuan hasn't rested since the attack. He was at the front lines aiding the wounded, negotiating with the local relief groups, overseeing Cheng Industries' contributions, and distributing emergency rations—"

    yuxuan "Miss Weng, I told you. I'm fine. I don't need rest. There's a lot I need to do."

    show weng normal at right_char with Dissolve(0.1)
    weng "My apologies, Master Yuxuan."

    show dorian neutral at left_char with Dissolve(0.1)
    "I took a closer look at him. Even in a flickering hologram, I could see the exhaustion clinging to him. The dim circles under his sharp eyes. The way his shoulders drooped ever so slightly."

    dorian "Yu. You look like you could use some sleep. Can you sleep?"

    show supply_robot base at center_supply with Dissolve(0.1)
    yuxuan "Dorian buddy, I'm going to be escorting you to the area you dreamed about, remember? I need to finish this before I can lead the rest of you there. I—"

    dorian "I appreciate that, Yu. Really, I do. It means a lot. But you really do look tired. I don't want you to overexert yourself."

    "For a moment, he looked like he wanted to argue. To brush it off. But instead, he sighed, running a hand through his hair. His voice dropped slightly, softer now."

    yuxuan "It's not just that."

    dorian "Then what?"

    "Yuxuan hesitated. He shifted, glancing away, as if gathering his thoughts. Finally, he exhaled, his tone unusually vulnerable."
    show supply_robot sad at center_supply
    show weng sad at right_flip
    with Dissolve(0.1)
    yuxuan "Tomorrow… It's the fifth anniversary of the Tragedy of Tianho."

    "A weight settled between us."
    "Even though the kingdom of Hinami would be hosting the memorial this year, it didn't change the fact that Tianho would be in focus."
    "And for Cheng Industries, the most powerful corporations in Tianho, that meant every move Yuxuan made would be under a magnifying lens."

    yuxuan "Cheng Industries will still be scrutinized. Every action, every donation, every word I say—there are people just waiting for me to slip up."
    yuxuan "Some people still believe we didn't do enough. Others think we did too much. And I know that no matter what I do tomorrow, someone will find a reason to be upset. A reason to call us vultures. Or opportunists. Or worse."

    show dorian neutral at left_char 
    show weng normal at right_flip
    with Dissolve(0.1)
    dorian "And that's why you're not resting?"

    show supply_robot base at center_supply with Dissolve(0.1)
    "Yuxuan let out a quiet, almost bitter laugh."

    show supply_robot normal at center_supply with Dissolve(0.1)
    yuxuan "I wouldn't be able to sleep even if I tried."

    show weng normal at right_flip with Dissolve(0.1)
    weng "Master Yuxuan, you're not just carrying your own worries. You're carrying the expectations of an entire nation, the legacy of your family."
    
    show weng normal at right_flip with Dissolve(0.1)
    weng "I know you feel like you can't afford to rest. That you have to keep pushing forward. But running on fumes isn't going to help anyone, least of all yourself."

    "The dim hum of the underground camp surrounded us—the distant murmur of the injured, the occasional beeping of medical devices."
    "Then I sighed."

    show dorian normal_alt_calm at left_char with Dissolve(0.1)
    dorian "Come here."

    yuxuan "W-what?"

    show dorian normal at left_char with Dissolve(0.1)
    dorian "I said come here…"

    "His hologram flickered slightly as he shifted in place."

    yuxuan "Dorian, I am literally a projection right now, what do you mean come here?"

    show weng normal at right_flip with Dissolve(0.1)
    weng "Master Yuxuan, just do it, please."

    "Hesitantly, he took a step forward. It didn't matter that his body wasn't physically here—just the gesture alone made something in his expression soften."
    "I lifted my hand, hovering it right where his shoulder would be if he were standing in front of me."

    show dorian neutral at left_char with Dissolve(0.1)
    dorian "I want you to rest, okay?"

    show supply_robot base at center_supply with Dissolve(0.1)
    yuxuan "D-Dorian…"

    "Yuxuan opened his mouth as if to protest, but then hesitated. His image wavered."

    yuxuan "But what about later? You still need me to show you the place from your dream…"
    yuxuan "Or, I don't know. Hmm… maybe Roboto can do it for you—"

    "He blinked at me, then scoffed, rubbing the back of his neck."

    yuxuan "I mean, technically, he could. Wait. In fact, Roboto can. Why in the Prosperity Dragon's name didn't I think of that?"

    "Yuxuan sucked in a breath, eyes widening just slightly. I took a step closer to his hologram, the faint blue light casting a soft glow over my face."

    dorian "If there's anything I can do to help you rest, just say the word."

    "There was a long pause."
    "Yuxuan seemed at a complete loss for words. He stared at me, opened his mouth, closed it again, then finally muttered, almost inaudibly—"

    yuxuan "Maybe if you were here…"

    "I blinked."
    "His eyes went wide as he realized what he had just said, his entire face turning red."

    yuxuan "D-Dorian! F-Forget it! I didn't—I mean—I was just—ugh!"

    "He ran both hands through his already-messy hair, looking like he wanted to crawl into a hole."

    show weng happy at right_char
    weng "Master Yuxuan, you really are bad at this."

    yuxuan "Ugh. Weng! Not now!"

    show dorian smile at left_char
    dorian "I'll be there soon, Yu. But for now… just try to get some rest."

    show dorian neutral at left_char
    show supply_robot base at center_supply 
    with Dissolve(0.1)


    yuxuan "Fine… But only because you asked."

    "The flickering blue light of his hologram made his expression hard to read, but there was something else in his gaze now—something softer. Warmer."
    "Then, he huffed dramatically, shifting back into his usual bravado."

    yuxuan "Fine. I'll send Roboto before I head to bed. Happy?"

    "I rolled my eyes and didn't reply. Before the connection could cut, another voice suddenly rang through the hologram."
    
    tedda "Mister Yuxuan! Mister Yuxuan! Here's your water!"

    yuxuan "Oh Tedda! Since you're here, can you do a hand massage? I need one so I can get to sleep."

    tedda "Ooh! I can do that, Mister Yuxuan!"
    tedda "Wait, oh my! Look at your hair! You do need to get some sleep!"
    tedda "Maybe a back massage is better! Hold on, let me—"

    "The hologram abruptly cut off."
    hide supply_robot with Dissolve(0.2)
    "The supply drone beside Weng beeped, returning to its idle state."

    show weng happy at right_flip with Dissolve(0.1)
    "Weng smiled, clearly amused, then gave me a nod of gratitude."
    show weng normal at right_flip with Dissolve(0.1)
    weng "Thank you, Sir Dorian."

    hide weng with Dissolve(0.2)

    "She excused herself, slipping back into her work, carefully organizing the medical supplies."
    "I exhaled and glanced around. The injured soldiers were still getting some rest. The air felt calmer now, the tension of earlier easing just a little."
    "Finding a quiet spot, I sat down and waited for Niko and the others to finish."

    jump ch7_waiting_common


# =============================================================================
# SECTION 12: LABEL CH7_WAITING_COMMON — More Wounded Arrive / Feng Returns
# =============================================================================

label ch7_waiting_common:

    scene cheng_industries_bunk_off with dissolve         # PLACEHOLDER — bunker main area
    stop music fadeout 1.5

    "I waited."
    "For what felt like an hour, I remained in place, arms folded as I watched the underground camp shift and stir around me."
    scene cheng_industries_bunk with dissolve

    "The dim glow of lanterns flickered against the stone walls, casting wavering shadows that danced with every passing movement."
    "The scent of medicinal herbs, sweat, and lingering blood filled the air."
    "Then, suddenly—chaos."
    "A fresh wave of wounded stumbled in through the entrance, the sound of hurried footsteps and pained groans breaking the temporary peace."

    show niko normal_anger at right_char with Dissolve(0.2)
    niko  "More? Get them here! Quickly!"

    show svante normal_nervous at left_char with Dissolve(0.2)
    svante "On it, sir!"

    hide svante
    hide niko
    with Dissolve(0.1)
    "Niko's voice rang through the camp as he and his assistants rushed forward, guiding the injured toward the makeshift medical beds."
    "Some paladins were already on the move, rolling out more bandages and preparing antiseptics."
    "Weng, despite her age, moved with sharp precision, directing volunteers where they were needed most."
    "A man groaned in agony as a deep gash along his side was quickly wrapped."
    "Another warrior, his face pale from blood loss, was lowered onto a cot while Niko pressed firm hands over his wound, muttering a prayer."
    "Through it all, Svante worked quietly, his hands trembling slightly as he sorted through gauze, ointments, and stitches."
    "He wasn't trained for this, but he was doing what he could—meticulously arranging supplies, refilling water basins, anything to help keep the system flowing."
    "Then—just as suddenly as it began—it was over."
    "The injured were patched up, their pain dulled by medicine and exhaustion. Some had already passed out, their bodies succumbing to much-needed rest."
    "Then, the paladins arrived."
    "They moved in slower than the others, their silver-plated armor scuffed and dirtied, some of them limping as they entered."

    show feng_suit at right_char with Dissolve(0.2)
    feng "Finally!"

    "At his side, he held the hand of what looked to be an injured fellow paladin—a younger man whose breathing was shallow but steady."
    "Feng's grip was firm, as if anchoring him in place."

    feng "You'll be alright. Just breathe."

    "The younger paladin barely managed a nod before being led away for treatment."
    "Feng lingered for a moment, watching until he was sure the healers had him in good hands. He turned and spotted me."
    "His expression brightened."

    show dorian neutral at left_char with Dissolve(0.2)
    feng "Old buddy! There you are!"

    "I stepped forward, scanning him for any serious injuries."

    dorian "How's the situation?"

    show feng_suit at right_char
    "Feng rolled his shoulders with a tired stretch. He dusted off his gauntlets, exhaling sharply."

    feng "Taken care of. By the Prosperity Dragon, we handled the yaoguai. Before heading back, we swept the perimeter, just to be sure."

    "I watched as he leaned against a stone pillar, the dim lantern light catching on his armor's scuffs and dents."

    feng "Turns out there were still a few lurking. But we already took care of them too."

    show niko normal_base at center_char with Dissolve(0.2)
    niko "How sure are you? There might still be some yaoguai lurking."

    show feng_suit at right_char with Dissolve(0.2)
    feng "Nah. We did everything we could. We checked the ruins, scouted the paths, even made sure there were no lingering traces of their aura. If there were any left, they'd have come crawling out by now."
    feng "I got Aoi fetch us some booze. I told that woman to lighten up but Dragon's bollocks was she as rigid as a dead ganderbilt."

    hide niko
    show svante normal_sad at center_char with Dissolve(0.2)
    "Svante, who had been silently organizing supplies nearby, hesitated before speaking."

    svante "Lady Aoi… Hmm…"
    svante "I just… I just hope nobody else gets hurt. Seeing all these people injured makes me worry."

    show feng_suit at right_char with Dissolve(0.2)
    "Feng waved a hand dismissively."
    show svante normal_neutral at center_char with Dissolve(0.2)

    feng "Meh. Relax, aldorith kid. We've got it under control. They don't call us paladins for nothing, eh, Dorian?"

    show dorian normal_alt_annoyed at left_char with Dissolve(0.1)
    "I rolled my eyes."

    dorian "Right."

    "Feng grinned, a deep, boisterous laugh escaping his throat."
    show dorian neutral at left_char with Dissolve(0.1)

    feng "Hahaha! Just like old times, huh, buddy?"

    show svante alt_base at center_char with Dissolve(0.2)
    "Svante's head tilted slightly, curiosity flickering in his eyes."

    svante "Pardon me, sir. Y-You and Sir Dorian know each other?"

    show dorian normal at left_char with Dissolve(0.1)
    dorian "You could say that."
    show dorian neutral at left_char with Dissolve(0.1)

    show feng_suit at right_char with Dissolve(0.2)
    "Feng scoffed and clapped a hand against my shoulder, shaking his head."

    feng "You could say that?! Dorian and I were best friends!"

    hide svante
    show niko alt_annoyed at center_char with Dissolve(0.2)
    "Niko, who had been quietly observing, finally spoke up."

    niko "Yeah. The two of you. And that Cyrus fellow."

    show feng_suit at right_char with Dissolve(0.2)
    "A flicker of recognition crossed Feng's face. His gaze drifted toward Niko, his brow furrowing slightly as he looked him over."
    show niko alt_base at center_char with Dissolve(0.1)

    feng "Oh… I remember you."

    "A beat passed. His expression changed—his features sharpening into something colder, edged with disdain."

    feng "You're that Death God prophet who had a brother with the audacity to try out for the interpreter for the son of the Emperor of Kyeongjang."

    show niko normal_serious at center_char 
    show dorian serious at left_char
    with Dissolve(0.1)
    "Niko's fingers curled slightly against his arms, his expression unreadable."

    niko "Yes… I was."

    show feng_suit at right_char with Dissolve(0.2)
    feng "Hmph. We should have arrested you in the first place."

    jump ch7_feng_niko_clash


# =============================================================================
# SECTION 13: LABEL CH7_FENG_NIKO_CLASH — Feng vs Niko / Aoi Arrives
# =============================================================================

label ch7_feng_niko_clash:

    # play music ost_ch7_feng_clash fadein 0.5    # PLACEHOLDER — tense confrontation theme

    "The air grew heavier."

    feng "Maybe if we had, things would have turned out differently. No Tianho Tragedy. No need for underground camps, no need for wounded paladins bleeding out on stone floors."

    show niko normal_serious at center_char with Dissolve(0.2)
    niko "Maybe if the paladins had spent less time polishing their pride, they'd still be standing."

    show feng_suit at right_char with Dissolve(0.2)
    feng "Right. Because listening to the Death God's lapdog always leads to prosperity."

    show niko normal_ignore at center_char with Dissolve(0.2)
    niko "Hmph."

    "He gestured vaguely toward the injured, his smirk thin and humorless."

    feng "Your death god caused this, idiot."
    feng "Do you ever wonder if your god watched and did nothing? Or do you already know the answer to that?"

    show niko normal_base at center_char with Dissolve(0.2)
    "Niko's expression didn't change, but something in his shoulders stiffened."

    niko "…"

    hide niko
    show svante normal_nervous at center_char with Dissolve(0.2)
    "Svante shifted uncomfortably, his gaze darting between them."

    svante "S-Sir, that's really not necessary, we're just—"

    feng "You're not off the hook either, aldorith."
    feng "Your Mjollians worship Enoch, don't they? A god of order, of righteous judgment? Tell me, where was that divine justice when Tianho burned?"

    show dorian serious at left_char with Dissolve(0.2)
    dorian "Feng, enough."

    "His eyes snapped to mine, still burning, but I didn't waver."

    "Feng exhaled sharply through his nose, his fists clenching at his sides."
    hide svante
    show niko alt_base at center_char with Dissolve(0.2)
    "Niko, still expressionless, simply turned away, resuming his work as if the conversation had already been beneath him. But I knew better."
    "Feng let out a low, humorless chuckle, shaking his head."

    feng "Tch. Whatever."

    "He locked eyes with Niko and gave him the finger."

    feng "Yeah. That's what I thought. Typical Enoch bootlicker."

    "His boots scraped against the stone floor as he stepped closer to Niko. With slow deliberation, he spat on the ground near Niko's feet."

    feng "Cyrus would still be alive if it wasn't for you lot."

    show dorian angry at left_char with Dissolve(0.1)
    dorian "Feng!"

    feng "Didn't have much love for the guy, but at least he didn't sit back and let the world burn while preaching about 'balance' and 'divine order.' At least he fought for something real."

    show feng_suit at right_char with Dissolve(0.1)
    show screen feng_blue_fire

    "A slow, smoldering heat began to radiate from his form. The temperature in the air shifted."
    "Blue flames erupted from Feng's arms, curling like living serpents around his fists. His eyes gleamed an otherworldly blue, flickering with restrained fury. The glow cast sharp shadows across his face."

    # TODO: play sound sfx_blue_flames               # PLACEHOLDER — blue fire SFX

    "He flexed his fingers, and the fire coiled and twisted with the motion, waiting—hungry."

    feng "How about a duel, huh?"

    "The challenge rang through the air like a war drum."

    hide feng_suit
    hide screen feng_blue_fire
    
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "S-Sir! Please! You can't be serious!"

    hide svante
    show feng_suit at right_char with Dissolve(0.2)
    show screen feng_blue_fire

    feng "Oh, I'm dead serious. Enoch bootlickers need to be taught a lesson."

    show niko normal_base at center_char with Dissolve(0.1)
    "Niko didn't flinch. He continued examining the medical equipment."

    niko "Sir Feng, you are exhausted. Your core temperature has risen by approximately three degrees, your muscles are visibly tense, and you're favoring your left side."
    niko "Your challenge is tempting but I'd much rather focus on treating our actual patients."

    feng "Why you arrogant son of a—"

    show niko normal_serious at center_char with Dissolve(0.1)
    niko "There are wounded here. Tell me, Sir Feng—how many people will suffer tonight because you chose to satisfy your pride instead of helping them?"

    feng "Die, you mother—"

    show dorian serious at left_char with Dissolve(0.1)
    "I had seen enough."
    "I stepped forward, shoving a firm hand against Feng's shoulder and forcing him back toward a nearby seat."
    "His flames flickered in protest but didn't lash out."

    show dorian angry at left_char with Dissolve(0.1)
    dorian "That's enough, Feng."

    "His eyes snapped to mine, still burning, but I didn't waver."

    show dorian serious at left_char with Dissolve(0.1)
    dorian "What's gotten into you? Lay off. Now. I won't ask again."

    show feng_suit at right_char
    "For a long, tense moment, Feng's fists remained clenched, his fire refusing to die down."

    feng "Tch. Whatever."
    hide screen feng_blue_fire with Dissolve(0.5)

    "He locked eyes with Niko and gave him the finger."

    scene cheng_industries_bunk with dissolve
    "A faint ripple echoed through the air before a crate of wine floated smoothly into the room, suspended in shimmering tendrils of water."
    "The liquid curled around it like a serpent, carrying it effortlessly before setting it down with an elegant, weightless grace."

    show dorian serious at left_char
    show aoi_battle_suit at right_flip
    with Dissolve(0.2)
    "Aoi stepped in behind it, her expression as unreadable as ever."
    "The air in the room seemed to shift."
    "She barely spared a glance at the others before flicking her wrist, dispersing the water with a snap of her fingers, leaving only the faintest mist behind. Not a single drop had been spilled."

    show svante normal_nervous at center_char with Dissolve(0.2)
    "Svante stiffened immediately."
    "His hands, which had just been sorting through medical supplies, froze mid-motion. His back straightened, and his face turned an even paler shade than before."

    svante "L-Lady Aoi…"

    show aoi_battle_suit at right_flip with Dissolve(0.2)
    "Aoi's cold gaze flickered toward him, her expression unwavering."
    "For a moment, there was silence."
    "Then, with all the enthusiasm of a stone wall, she gave him the slightest nod of acknowledgment."

    aoi "Svante."

    "Svante swallowed hard, his fingers fumbling slightly as he hastily resumed sorting the medical supplies."
    hide svante with Dissolve(0.1)
    "I almost felt nervous for him at first, expecting some kind of sharp remark from Aoi—but she didn't seem to care much about his presence."

    show dorian normal_alt_calm at left_char with Dissolve(0.1)
    "Feng, on the other hand, grinned widely, already reaching into the crate. With zero hesitation, he plucked a wine bottle from the stash, his fingers deftly undoing the seal with an easy familiarity."
    show dorian neutral at left_char with Dissolve(0.1)
    "With a triumphant pop, he shoved it into Aoi's hands."

    # play sound sfx_wine_pop                  # PLACEHOLDER — wine pop SFX

    hide aoi_battle_suit
    show feng_suit at right_char with Dissolve(0.2)
    feng "Cheers to old friends!"

    "He grabbed another bottle for himself, lifting it in an exaggerated toast before taking a hearty swig straight from the neck."

    feng "Now this is what I call a proper end to a fight!"

    hide feng_suit
    show aoi_battle_suit at right_flip with Dissolve(0.2)
    "Aoi, without missing a beat, put the wine bottle down and crossed her arms."

    aoi "You're supposed to ration these."

    show feng_suit at center_char with Dissolve(0.2)
    "Feng shrugged, tilting the bottle toward her in offering."

    feng "C'mon, Aoi. Live a little. Even you can't tell me you don't need a drink after today."

    "Aoi gave him a long, slow blink."

    aoi "I don't drink on duty, sir. I'm your mercenary, remember?"

    "Feng snorted, nudging me with his elbow."

    feng "She says that, but I swear I've seen her drink a whole bottle before. Right, Dorian?"

    "Aoi exhaled through her nose."

    aoi "That never happened. *sighs*"

    feng "See? That's what a guilty person would say."

    "She didn't dignify him with a response, but the sharpness in her gaze was enough to make most men reconsider their choices. Feng, however, was not most men."
    "With a dramatic sigh, he leaned against the crate, glancing between me and Aoi before making a lazy gesture."

    feng "Aoi, get my boy here a wine bottle."

    "For a second, she didn't move. Then, with slow, deliberate precision, she reached into the crate, grabbed a bottle, and turned toward me."
    "She held it out, her grip firm, but her tone was flatter than a deadpan joke."

    aoi "By the orders of Sir Feng, I am required to provide you with this beverage."

    "Her eyes flicked toward me, unreadable but clearly unimpressed."

    aoi "*dryly* Drink responsibly, sir."

    "Feng let out a bark of laughter."

    feng "Hahahaha! Aoi, you make it sound like I'm corrupting him!"

    aoi "Aren't you, sir?"

    feng "Hahahaha! Cheeky lady! I love it!"

    aoi "Ugh… Men…"

    "The firelight flickered against the rough stone walls, casting long, wavering shadows across the underground camp."

    "Feng leaned back, looking, his grin remained ever-present, his fingers curled around the neck of his bottle like it was a prize won in battle."
    "Aoi stood beside us, arms crossed, her watchful gaze scanning the camp even as Feng casually popped open another bottle."
    "I glanced at the bottle in my hand, feeling its cool weight against my palm."
    "The liquid inside sloshed gently as I tilted it, the deep amber catching the glow of the lanterns."
    "Feng, watching me closely, smirked."

    feng "Well? What's it gonna be, old buddy?"

    jump ch7_drink_choice

# =============================================================================
# SECTION 14: LABEL CH7_DRINK_CHOICE — D: Drink or Refuse
# =============================================================================

label ch7_drink_choice:
    # play music ost_ch7_drink fadein 1.0         # PLACEHOLDER — relaxed post-battle theme
    menu:

        "Drink with Feng.":
            $ ch7_drink_choice = "drink"
            $ svante_affection += 1
            $ feng_affection   += 1
            $ aoi_affection    += 1

            show dorian normal at left_char with Dissolve(0.1)
            "I let out a breath, then smirked. It's been a while since I drank with him. Feng whooped, throwing an arm around my shoulder."

            feng "That's my boy! Thought you got too serious for a good drink!"
            show dorian neutral at left_char with Dissolve(0.1)
            "I took a long sip, the burn of the wine spreading warmth through my chest. The tension from the day—the injured, the yaoguai attacks, the exhaustion—eased just a little."

            hide aoi_battle_suit
            show svante normal_happy at right_char with Dissolve(0.2)
            "Svante, who had been watching nervously, immediately perked up."

            svante "Ah… T-that's good, Sir Dorian! You should relax a little…"

            "He smiled, clearly relieved. Is he… worried about me?"
            "But then, I heard Niko sigh."

            hide svante
            show niko alt_disappointed at right_char with Dissolve(0.2)
            niko "Really, Dorian? At this time?"

            "I turned to him, catching the way his arms were crossed. He wasn't fuming, but there was disapproval in his gaze."

            show dorian sad at left_char with Dissolve(0.1)
            "I frowned, feeling a slight twinge of guilt. Niko had always been the responsible one, the one who thought ahead."
            "He had seen the worst of people when they let themselves go. Maybe, to him, drinking right now—after everything—was reckless."
            "Before I could say anything, Feng scoffed and waved a hand dismissively."
            show dorian neutral at left_char with Dissolve(0.1)

            hide niko
            show feng_suit at right_char with Dissolve(0.2)
            feng "Ignore the bootlicker, buddy."

            "He raised his bottle, clinking it against mine with an exaggerated wink."

            feng "Tonight, we drink to survival. To kicking ass. To another battle won. And to you not losing your damn mind under all that responsibility."

            show dorian smile at left_char with Dissolve(0.1)
            "I huffed a quiet laugh despite myself."
            show dorian neutral at left_char with Dissolve(0.1)

            dorian "Yeah, yeah. Just don't make me regret this."

            feng "No promises."

            "Then, he turned toward Aoi, lifting his bottle in her direction."

            feng "Aoi, join us, would you?"

            hide feng_suit
            show aoi_battle_suit at right_flip with Dissolve(0.2)
            "She rolled her eyes, arms still crossed."

            aoi "I don't drink on duty."

            hide aoi_battle_suit
            show feng_suit at right_char with Dissolve(0.2)
            feng "Oh, please. You're still getting paid, aren't you? It's not like I'm asking you to down the whole bottle and start singing folk songs. Just one drink."

            hide feng_suit
            show aoi_battle_suit at right_flip with Dissolve(0.2)
            "Aoi arched a brow at him. Then, with a dramatic sigh, she plucked a bottle from the stash."

            aoi "Fine. Since you're still paying me, basically."

            hide aoi_battle_suit
            show feng_suit at right_char with Dissolve(0.2)
            "Feng whooped again as we clinked our bottles together."

            feng "CHEERS, YOU BASTARDS! TO THE PROSPERITY DRAGON AND TO US!!"
            feng "MAY OUR COINS NEVER FAIL, OUR STOMACHS NEVER EMPTY, AND OUR CUPS NEVER RUN DRY!"

            "CHEERS!"

            jump ch7_drink_common

        "Refuse to drink with Feng.":
            $ ch7_drink_choice = "refuse"
            $ niko_affection += 1
            $ aoi_affection  += 1

            "I turned the bottle in my hands, watching the liquid swirl, before shaking my head."

            dorian "Not tonight."

            "Feng blinked, caught off guard. For a split second, he looked almost disappointed—before he threw his head back with an exaggerated groan and dramatically slumped against a crate."

            feng "Ugh, you really have changed."

            show dorian smile at left_char with Dissolve(0.1)
            "I chuckled, shoving the bottle back toward him."

            dorian "Someone has to stay sharp."
            show dorian normal_alt_neutral at left_char with Dissolve(0.1)

            feng "Pft… Boring Dorian. That's what you are now. Boring. Dorian."

            aoi "You could learn from him, sir."

            feng "Don't chastise me, Aoi. I get enough of that from my commanding officers, thanks."

            hide feng_suit
            hide aoi_battle_suit
            show niko alt_base at right_char with Dissolve(0.2)
            "Out of the corner of my eye, Niko's expression softened. He didn't say much—he never did when he was pleased—but I caught the slight nod of approval."

            niko "…Good."

            "I understood. To Niko, discipline meant survival. He had seen firsthand what happened when people got careless, when they let themselves indulge too much."
            show dorian normal_alt_confident at left_char with Dissolve(0.1)
            "Maybe, in his mind, I had just proven I wasn't like the rest."
            show dorian normal_alt_neutral at left_char with Dissolve(0.1)
            "But then, a quiet fidgeting caught my attention. I turned to see Svante, shifting from foot to foot, his expression unsure."

            hide niko
            show svante normal_nervous at right_char with Dissolve(0.2)
            svante "…Sir Dorian, it's just one drink. You can afford to relax, can't you?"

            "I glanced at him. Was he worried about me? Maybe, in his eyes, refusing to drink meant I was still carrying too much."

            show feng_suit at center_char with Dissolve(0.2)
            "Feng, of course, just shrugged and took another swig, completely unbothered."

            feng "Suit yourself. More for me."

            "He raised his bottle in a mock toast, then grinned."

            feng "Come on, Aoi. More for us."

            hide svante
            show aoi_battle_suit at right_flip with Dissolve(0.2)
            "Aoi pinched the bridge of her nose, but eventually sighed in resignation, grabbing another bottle."

            aoi "*sigh* Fine. Just one, alright?"

            feng "Fine."

            "Then, without missing a beat, he turned his attention to the nearby soldiers."

            feng "Hey you!"
            hide dorian
            hide aoi_battle_suit
            show soldier_jiang at left_char
            show soldier_gao at right_char
            with Dissolve(0.2)
            jiang "Yes, Paladin?"

            gao "Y-yes, sir?"

            "Feng grinned, waving his bottle."

            feng "Join us! Now!"

            "Jiang and Gao exchanged nervous glances."

            hide soldier_gao
            show aoi_battle_suit at right_flip with Dissolve(0.2)
            aoi "Really, sir? *sighs* You really are something, huh?"

            hide aoi_battle_suit
            show soldier_gao at right_char with Dissolve(0.2)

            feng "The more the merrier! This is a celebration—we survived another damn battle, didn't we?"

            "Jiang hesitated, but Gao—after a brief moment of uncertainty—grabbed a bottle and took a small sip. He coughed, sputtering slightly."

            gao "*coughs* Oh by the Dragon… *coughs* That's strong! *coughs*"

            show soldier_jiang at left_char with Dissolve(0.2)
            jiang "Ugh… Gao, get a grip."

            hide soldier_gao
            show aoi_battle_suit at right_flip with Dissolve(0.2)
            aoi "Hey, are you alright?"

            hide soldier_jiang
            show dorian neutral at left_char with Dissolve(0.1)
            dorian "Gao, don't push yourself, please."

            feng "That's the spirit! See? This guy gets it! Your turn, other guy! PARTY!!"

            aoi "Sir, calm yourself down."

            show dorian normal at left_char with Dissolve(0.1)
            "Jiang, looking increasingly uncomfortable, gave me a quick, searching glance. I simply shook my head, amused."

            hide soldier_jiang
            jump ch7_drink_common


# =============================================================================
# SECTION 15: LABEL CH7_DRINK_COMMON — Weng + Tim Arrive / Depart
# =============================================================================

label ch7_drink_common:

    scene cheng_industries_bunk with fade

    show dorian normal_alt_neutral at left_char
    show tim alt_normal at center_char_kids
    show weng alt_base at right_flip
    with Dissolve(0.2)
    "Weng walked toward us, her white dress pristine despite the long hours of work. Beside her, little Tim toddled along, his small fingers clutching her hand."
    "The toddler's other hand held a plastic bag filled with containers, each stacked neatly. Through the transparent material, I caught a glimpse of their contents—golden, jiggling Hinami flan."
    "Trailing slightly behind them was Chung-hee, his usual unreadable expression in place. His posture was relaxed, but his sharp eyes flicked over the camp, always assessing."
    "Always watching."
    show tim happy at center_char_kids with Dissolve(0.1)
    "Tim looked at Gao, who flashed a thumbs up at the kid. Tim smiled widely at him."
    "When Weng reached us, she clapped her hands together, nodding with finality."

    weng "It's time. We're leaving. Sorry we took too long, Sir Niko. Master Dorian."
    
    show dorian serious at left_char with Dissolve(0.1)
    "Finally. My thoughts turned to Magnus and the dream. And the mysterious door. I hope Yuxuan's lead is correct."
    show dorian normal_alt_neutral at left_char with Dissolve(0.1)
    "Niko was already finishing up, securing the last of his medical supplies. Svante, after lingering for a few seconds, finally sighed and stepped away from his task as well."
    
    hide weng
    show niko normal_base at right_char with Dissolve(0.2)
    niko  "No need to apologize, ma'am. I took too long as well. Come on, Svante."

    hide tim
    show svante normal_neutral at center_char with Dissolve(0.2)
    svante "Yes, sir Niko."

    hide svante
    hide niko
    show feng_suit at right_char with Dissolve(0.2)

    "I rolled my shoulders, turning to Feng, who was still nursing his bottle of wine, his usual cocky smirk firmly in place."

    dorian "We're heading out."

    feng "Where are you going?! The night's still young, buddy! Tomorrow is the anniversary! We have so many stuff to catch up on!"
    feng "You still haven't told me all about your time in the kingdom of Mjoll! Or did the cold finally get to your funny bone, huh? Hahaha!"

    show dorian serious at left_char with Dissolve(0.1)
    "I hesitated. I could feel his eyes on me—sharp, questioning."
    "But there was no time to waste. I had already lingered too long."

    dorian "Sorry, buddy. But we need to move. Now. It's urgent."

    hide feng_suit
    show chunghee alt_neutral at right_char with Dissolve(0.2)
    "I didn't raise my voice, but the weight behind my words made it clear—this wasn't something I could delay."
    "Chung-hee and I exchanged a glance. Niko exhaled sharply, adjusting the bandages on his arms."
    "He didn't need to ask why—I could tell by the look in his eyes that he already had a sense of it. Svante, after a brief moment of hesitation, hurried after us, his steps quick."
    hide chunghee
    show feng_suit at right_char with Dissolve(0.2)
    feng "Hmm…"

    "Behind me, I could feel Feng's stare lingering. A breath. A pause."
    "Then—a chuckle."
    "The flickering firelight cast shadows over his face as he leaned back slightly, tilting his bottle lazily toward me. He grinned."

    feng "Heh. Alright, alright. No need to be so serious."
    feng "You always did have a way of making things dramatic, old friend. But I get it."

    "He lifted the bottle in an easygoing mock toast."

    feng "See you tomorrow. Try not to get yourself killed before then, yeah?"

    show dorian neutral at left_char with Dissolve(0.2)
    "I gave him a nod before turning away, leading the others forward."
    "As we moved through the dimly lit corridors of the camp, I caught the faintest sound of Feng taking another long drink."

    hide dorian
    show aoi_battle_suit at left_char with Dissolve(0.2)
    aoi  "Another wine bottle, sir?"

    feng "Sure thing, Aoi."
    
    scene black with fade
    stop music fadeout 3.0
    stop audio fadeout 2.0

    pause 1.0

    show screen chapter_title_screen(
        "7",
        "Cheng Industries",
        subtitle="END",
        duration=3.0
    )
    pause 3.0

    jump chapter_8


# =============================================================================
# END OF CHAPTER 7
# =============================================================================
