###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  FILE:  chapter_09_p2.rpy
#  SCENE: CHAPTER 9 PART 2 — Hot Spring to End of Chapter
#
#  CONTENTS:
#    Section 1  — Image Declarations (new for Part 2)
#    Section 2  — Audio Declarations (new for Part 2)
#    Section 3  — Game Variables (new for Part 2)
#    Section 4  — label chapter_09_p2        (Hot Spring — Magnus / Yuxuan entry)
#    Section 5  — label ch9_huli_jing        (Hot Spring — Huli Jing appears)
#    Section 6  — label ch9_judgment_mjoll   (Illusion: Mjoll — Fynn Hjorth trial)
#    Section 7  — label ch9_judgment_hinami  (Illusion: Hinami — Katashi Morita trial)
#    Section 8  — label ch9_judgment_kyeong  (Illusion: Kyeongjang — Seorin Im trial)
#    Section 9  — label ch9_judgments_back   (Common — back to hot spring)
#    Section 10 — label ch9_huli_reward_low  (IF approval < 3 — fox leaves without reward)
#    Section 11 — label ch9_huli_reward_high (IF approval >= 3 — fox grants question)
#    Section 12 — label ch9_huli_love        (Love route choice)
#    Section 13 — label ch9_huli_exit        (CommonCommonCommon — fox farewell / FWOOMP)
#    Section 14 — label ch9_stuffed_fox_exit (Common — darkness / toy / everyone pops out)
#    Section 15 — label ch9_kids_spring      (Hot Spring — kids POV / Tim / Huli Jing)
#    Section 16 — label ch9_fox_toy          (Elias opens fox toy)
#    Section 17 — label ch9_spring_end       (Common — untangled / bathing / hilltop prep)
#    Section 18 — label ch9_hilltop          (Hill — ceremony / Aoi / lanterns)
#    Section 19 — label ch9_lantern_kids     (Lantern release — Elias launches lantern)
#    Section 20 — label ch9_route_yuxuan     (ROUTE: Yuxuan lantern scene)
#    Section 21 — label ch9_route_chunghee   (ROUTE: Chung-hee lantern scene)
#    Section 22 — label ch9_route_svante     (ROUTE: Svante lantern scene)
#    Section 23 — label ch9_route_niko       (ROUTE: Niko lantern scene)
#    Section 24 — label ch9_route_magnus     (ROUTE: Magnus lantern scene)
#    Section 25 — label ch9_end              (Common ending — sparklers / going home)
#
#  NAMING CONVENTIONS:
#    image tags      — bg_name, cg_name, character_name emotion
#    audio variables — audio.ost_name, audio.sfx_name, audio.amb_name
#    label names     — ch9_name (all lowercase, underscores only)
#    NO SPACES in any tag, label, variable, or image name.
#
#  TRACKER SUMMARY:
#    huli_jing_approval : +1 per exile judgment (max 3) — gates reward
#    chunghee_affection : +1 ch9 flan question (choice 4 of reward)
#    love_route_locked  : set to "yuxuan" / "niko" / "svante" / "chunghee" / "magnus"
#    yuxuan_affection   : +++ Yuxuan / +1 "They'd be proud of you"
#    niko_affection     : +++ Niko
#    svante_affection   : +++ Svante
#    chunghee_affection : +++ Chung-hee
#    magnus_affection   : ++++ Magnus
#
#  PLACEHOLDER PATHS:
#    Search "# PLACEHOLDER" to find every line that needs a real asset.
###############################################################################


# =============================================================================
# SECTION 1: IMAGE DECLARATIONS
# =============================================================================

image bg_hot_spring              = "images/backgrounds/bg_hot_spring.png"                  # PLACEHOLDER
# Natural underground hot spring — glowing fungi, steam, lanterns on cavern walls

image bg_mjoll_town_square       = "images/backgrounds/bg_mjoll_town_square.png"           # PLACEHOLDER
# Mjoll town square — snow, stone buildings, iron gates, grey sky

image bg_hinami                  = "images/backgrounds/bg_hinami.png"                      # PLACEHOLDER
# Hinami cliffside — blue sky, crashing waves below, salt-laced wind

image bg_kyeongjang_palace       = "images/backgrounds/bg_kyeongjang_palace.png"           # (reuse from ch4)
# Kyeongjang palace courtyard — pagodas, gold leaf rooftops, pale sky

image bg_hill_memorial_night     = "images/backgrounds/bg_hill_memorial_night.png"         # PLACEHOLDER
# Hilltop overlooking Tianho Memorial — indigo sky, lanterns glowing below

image cg_huli_jing_spring        = "images/cg/cg_huli_jing_spring.png"                    # PLACEHOLDER
# Huli Jing perched on spring rock — nine tails spread, golden eyes, steam around her

image cg_elara_xianlun           = "images/cg/cg_elara_xianlun.png"                       # PLACEHOLDER
# Elara, Daniel, Emily, Sarah, Lucas beneath the golden gate of Xianlun

image cg_aoi_performance         = "images/cg/cg_aoi_performance.png"                     # PLACEHOLDER
# Aoi in indigo kimono, holographic sea and dragon rising behind her


# =============================================================================
# SECTION 2: AUDIO DECLARATIONS
# =============================================================================

define audio.ost_ch9_hotspring   = "audio/music/ost_ch9_hotspring.ogg"      # PLACEHOLDER
define audio.ost_huli_jing       = "audio/music/ost_huli_jing.ogg"          # PLACEHOLDER
define audio.ost_judgment_mjoll  = "audio/music/ost_judgment_mjoll.ogg"     # PLACEHOLDER
define audio.ost_judgment_hinami = "audio/music/ost_judgment_hinami.ogg"    # PLACEHOLDER
define audio.ost_judgment_kyeong = "audio/music/ost_judgment_kyeong.ogg"    # PLACEHOLDER
define audio.ost_ch9_ceremony    = "audio/music/ost_ch9_ceremony.ogg"       # PLACEHOLDER
define audio.ost_ch9_lanterns    = "audio/music/ost_ch9_lanterns.ogg"       # PLACEHOLDER
define audio.ost_ch9_fireworks   = "audio/music/ost_ch9_fireworks.ogg"      # PLACEHOLDER

define audio.sfx_huli_fwoomp     = "audio/sfx/sfx_huli_fwoomp.ogg"         # PLACEHOLDER
define audio.sfx_judgment_chains = "audio/sfx/sfx_judgment_chains.ogg"     # PLACEHOLDER
define audio.sfx_firework_boom   = "audio/sfx/sfx_firework_boom.ogg"       # PLACEHOLDER
define audio.sfx_sparklers       = "audio/sfx/sfx_sparklers.ogg"           # PLACEHOLDER
define audio.sfx_cheng_jingle    = "audio/sfx/sfx_cheng_jingle.ogg"        # PLACEHOLDER

define audio.amb_hot_spring      = "audio/ambient/amb_hot_spring.ogg"      # PLACEHOLDER
define audio.amb_hilltop_night   = "audio/ambient/amb_hilltop_night.ogg"   # PLACEHOLDER


# =============================================================================
# SECTION 3: GAME VARIABLES
# =============================================================================

# default huli_jing_approval  = 0     # +1 per exile judgment, max 3
# default love_route_locked   = ""    # "yuxuan" "niko" "svante" "chunghee" "magnus"


# =============================================================================
# SECTION 4: LABEL CHAPTER_09_P2 — Hot Spring
# =============================================================================

label chapter_09_p2:

    # [COMMENT: bg_hot_spring — natural cavern hot spring, lanterns, steam]
    scene bg_hot_spring with dissolve           # PLACEHOLDER — hot spring
    play music ost_ch9_hotspring fadein 2.0     # PLACEHOLDER — hot spring theme
    play audio amb_hot_spring loop fadein 1.5   # PLACEHOLDER — hot spring ambient

    "We reached the hot springs, and the moment we stepped inside, the warmth in the air wrapped around me like a comforting embrace."
    "The soft glow of lanterns flickered against the cavern walls, their light dancing over the steaming water. The air carried a faint floral scent, something soothing yet unfamiliar."
    "Roboto came to a stop and turned to me."

    roboto "Master Dorian, please undress b-b-b-before entering. Master Yuxuan has ensured the waters will provide optimal relaxation."
    dorian "Yeah, thanks for the reminder."

    "Roboto nodded, its eyes flickering."

    roboto "I have other matters to attend to. Please enjoy your time."
    roboto "M-M-Master Yuxuan will join you momentarily."

    "And with that, the metallic figure turned and departed, his whirring echoing as he disappeared down the stone hallway."
    "Left alone, I took a step forward, only to pause when I noticed a figure already standing by the water's edge."
    "Magnus."
    "He was dressed in a deep blue shirt with gold accents, a rare sight given that I saw him the entire day shirtless. But what stood out the most was the absence of his wings."
    "I furrowed my brows. Magnus without his wings?"
    "Magnus turned his head slightly, his expression calm."

    magnus "Dorian! Going to take a dip in the hot spring as well?"
    magnus "Look! I've made a discovery-an astonishing revelation, a truth hidden within my very being!"

    "I raised a brow."

    magnus "Apparently, I can make my wings appear and disappear at will! A most convenient ability, wouldn't you say?"
    dorian "Convenient. Saves fabric, I guess."
    magnus "Precisely. And, most importantly, it prevents... unfortunate accidents involving doorways and the backs of unsuspecting heads."
    magnus "Because I have, on numerous occasions, unintentionally struck Svante..."

    "He paused, rubbing his chin before continuing."

    magnus "And Yuxuan... And Chung-hee... And Niko... And Elias... And Tim... And Miss Weng... And Roboto... And Tedda..."
    dorian "So... everyone. You accidentally hit everyone with your wings."
    magnus "Yes, everyone... But you! Everyone but you. But you must understand, my dear Dorian!"
    magnus "It was never intentional! A cruel twist of fate, a betrayal of my own grand appendages!"

    "He placed a hand over his heart, looking entirely too pleased with himself."

    magnus "But alas! The heavens took pity on me. I merely wished for relief, and lo and behold-like the parting of storm clouds, the burden was lifted!"

    "He rolled his shoulders once more, as if reveling in his newfound control. I chuckled, nodding toward his attire."

    dorian "By the way, nice outfit. You clean up well."
    magnus "Ah, such high praise from the esteemed Dragon of Gale! I shall treasure this moment."

    "I asked him where did he get the outfit."

    magnus "Ah, a tale most unexpected! Tedda, our diligent little dolly, was cleaning out Yuxuan's closet when she stumbled upon this garment-folded, untouched, a relic of time."
    magnus "I tried it on and Miss Weng and sir Niko loved it! Oh, the applause!"
    magnus "But... it turned out that this was from one of Yuxuan's deceased old friend's clothes."

    "My eyes widened."

    dorian "Shouldn't you return it if that's the case? What would Yuxuan think?"
    magnus "I did show him. And he said, 'Better that you wear it than let it gather dust.'"
    magnus "So here I am, wearing a memory... but making it move again, making it breathe. Perhaps that is what clothes are meant to do-carry stories forward, instead of letting them fade into silence."

    "He took a sudden step back and struck a pose-one hand on his hip, the other extended outward as if he were about to take center stage in some grand performance."

    magnus "Tell me, Dorian-does this not suit me like the sky embraces the sun? Like the waves cradle the moon? This shade of blue-it was destined to grace my form, was it not?"
    magnus "Or, in more common terms-blue suits me, don't you think?"

    menu:

        "Yes, it does.":
            $ magnus_affection += 1             # +1 Magnus affection

            "Magnus gasped, his expression shifting into one of delighted triumph. He spun again, this time with even more flourish, letting the fabric billow as he moved."

            magnus "Ah! I knew you were a man of refined taste! You see it, don't you, Dorian? This hue, this elegance-it was made for me!"

            "He placed a hand on my shoulder, his eyes shining with genuine joy beneath all the dramatics."

            magnus "And to have such recognition from you... well, my dear friend, I shall cherish this moment until the stars themselves fade from the sky!"

            "He took a deep breath, straightening his posture before giving me a wink."

            magnus "Blue it is, then. A color worthy of a Gale-born soul such as mine."

        "No, it doesn't.":

            "Magnus froze, his expression caught somewhere between shock and absolute betrayal. His hand clutched at his chest as if I had struck him with an arrow."

            magnus "No? No?! Dorian, you wound me!"

            "He turned away dramatically, bringing a hand to his forehead as if the weight of my words was too much to bear."

            magnus "Then tell me, O Great Fashion Oracle, what shade would better suit my divine essence?"

            "He peered at me over his shoulder, awaiting my response. Whether I gave him an actual color or simply let him stew in his devastation, I knew one thing for certain-he wasn't going to let me forget this anytime soon."

    "Shaking my head, I reached for my belt and started undoing my clothes. Magnus followed suit, both of us stripping down to our undergarments before stepping into the water."
    "The moment I sank into the warmth, a deep sigh escaped me. The heat seeped into my muscles, melting away tension I hadn't realized I was carrying. Magnus settled in beside me, his gaze drifting over the glowing fungi, the sheer ambiance of the place."

    magnus "It's beautiful here. Almost... unreal."
    dorian "*sighs* This is the life..."
    magnus "*sighs* This is perfect..."

    "We both closed our eyes and let the gentle hum of water lapping against the stone take us into tranquility."

    magnus "..."
    magnus "A spring of warmth, a fleeting dream. Where silence hums and soft lights gleam."
    magnus "A breath of peace, a moment's grace, Lost within this sacred place."

    "A few minutes passed in peaceful silence before Magnus shifted slightly, tilting his head toward me."

    magnus "Dorian, my dear friend, can you do me a favor?"
    dorian "Depends."
    magnus "Can you scrub my back?"
    dorian "Really?"
    magnus "Miss Weng gave me something to help us scrub. I'll go get it."

    "Then, the door slid open."
    "Yuxuan entered, his usual composed expression relaxed into something softer, almost coy."
    "His eyes swept over the water, and he exhaled, the corner of his lips tugging into the smallest, knowing smirk."

    yuxuan "Ah, Dorian... Just the two of us, bathed in the glow of the springs..."
    dorian "Oh, Yu."

    "He took another step forward, slipping out of his robe in one fluid motion, revealing his body beneath the dim lighting."

    yuxuan "The heat is perfect, wouldn't you say? Almost as if it's drawing us in... together."

    "Yuxuan confidently stripped down to his undergarments, preparing to step in. His movements were slow, deliberate, like a man savoring the moment."
    "Then he saw Magnus."
    "For a moment, there was silence. Absolute. Stunned. Silence."
    "Yuxuan's eyes landed on Magnus, who-completely oblivious-smiled and raised his hands in delight."

    magnus "Yuxuan, my dear friend! Have you come to partake in the benefits of the hot-"
    yuxuan "W H A T."
    magnus "-springs?"
    yuxuan "DORIAN?! WHAT-WHAT IS HE DOING HERE?! I THOUGHT-"

    "His hands clutched his undergarments, suddenly realizing he had undressed in front of an audience. His composure crumbled like old parchment."

    dorian "Uh... bathing?"
    magnus "Nice undergarments, my dear friend! Thank you for lending me your friends' undergarments as well!"
    yuxuan "T-Thanks?!-Wait-NO-WHY-"
    magnus "Come join us, my dear friend!"

    "Yuxuan inhaled deeply, nostrils flaring. His fingers twitched, and for a second, I swore he was debating whether to murder Magnus on the spot or sink into the hot spring and pretend this never happened."
    "Instead, his eye twitched violently."

    dorian "Just come join us, Yu. The water's fine."

    "Still twitching, Yuxuan slipped into the water. The moment he did, Magnus spread his arms wide and pulled him into a suffocating hug."

    yuxuan "M-Magnus! H-hey! I'm getting strangled!"
    magnus "My dear friend, the water is amazing!"
    yuxuan "WHY ARE YOU EVEN HERE?!"
    magnus "What do you mean? You told me to join you."
    yuxuan "...What? I never-"

    "And then... the door slid open."
    "Niko. Svante. Chung-hee."
    "All three of them. In their undergarments."
    "They weren't even paying attention to us at first. They were deep in mid-conversation, voices echoing slightly against the cavern walls."

    niko      "Fasting is a form of discipline, Svante. A way to show devotion to Enoch. A test of the soul's resolve."
    svante    "But for that long? I don't think you can do it. How are you not hungry? I'd pass out."
    niko      "You rely on Enoch's words. And pray. One does not live by earthly sustenance, but by every word that-"
    niko      "Unless... Your faith isn't good enough."
    svante    "I... I-"
    chung_hee "He's being dramatic, Svante. You don't have to do it if you don't want to. Niko, stop it."

    "And then-finally-they looked up."
    "Magnus lifted his arms wide, water sloshing around him. His wings were still hidden, but it was as if he radiated an invisible aura of divinity."

    magnus "Dear friends!! Here we are!!"

    "He waved, as if this was the most natural gathering in the world. Chung-hee blinked, deadpan."

    chung_hee "Oh look. It's Magnus. Dorian's here too, along with Yuxuan."
    svante    "MAGNUS!! YOU'RE HERE!!"

    "Yuxuan, still submerged in the water, was visibly vibrating with rage. His fingers twitched as if they were itching to summon some kind of spell-maybe to drown Magnus, maybe to drown himself."

    yuxuan "WHY. IS. EVERYONE. HERE."
    chung_hee "What's gotten into him?"
    svante    "Didn't you invite us, Yuxuan?"
    niko      "Your invitation made me think it was going to be just the two of us here."
    chung_hee "Same. I thought you had some confidential information about the Divine Weapon, so I came here expecting something important. I was surprised to see these two, though."
    svante    "Yeah. You even called us your \"special guest\"."

    "Yuxuan's eye twitched so violently that for a second, I thought he might actually explode. He inhaled sharply, barely keeping himself from launching into a full-blown tantrum."
    "Then he snapped his head toward the entrance, his voice echoing through the chamber."

    yuxuan "Special?! ROBOTO! ROBOTO!"

    "A few moments passed."
    "The sound of mechanical whirring filled the air, followed by the faint clanking of metal against stone. And then-"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "Y-y-y-you called, Master Yuxuan? Roboto is h-h-h-here. At your service."
    yuxuan "I told you to bring our special guest here! I also told Tedda to take care of Elias so our special guest could come here! How in the name of the Prosperity Dragon did this-"

    "Roboto's sensors flickered again."

    roboto "M-M-Master Yuxuan, you said to bring the... special guest."

    "Roboto's mechanical eyes whirred as it scanned the room."

    roboto "The term 'special guest' was n-n-not explicitly defined. Given that Master Dorian, Sir Magnus, Sir Chung-hee, Sir Niko, and Sir Svante all hold unique statuses, it was l-l-l-logical to conclude that all of them qualified as... special guests."

    "Yuxuan let out a sound somewhere between a strangled groan and a defeated whimper."
    "His entire body trembled. His eye twitched again. He opened his mouth-closed it-opened it again-"
    "Then, with a slow, heavy inhale, he lowered himself deeper into the water until only his eyes were visible, like a man giving up on life itself."

    dorian "The water is nice, Yu. Might as well enjoy it."
    svante "Dorian! Let's explore that side with Magnus!"
    dorian "Sounds nice. Let's go."
    magnus "Then let us embark, my friends! Onward to the unknown! Chung, can you hold my hand as we walk?"
    chung_hee "I should've stayed in bed."
    niko      "Just Dorian, huh? Figures."
    yuxuan    "I will END you, Niko."
    niko      "That explains all of the rose petals in-"
    yuxuan    "Shhh!! Just shhh!!"
    niko      "Hey! How dare you splash water on me!"

    "Steam curled lazily through the air as we settled deeper into the hot springs. The warmth seeped into my muscles, unraveling tension I hadn't even realized I carried. For a moment-just a moment-it was peaceful."

    jump ch9_huli_jing


# =============================================================================
# SECTION 5: LABEL CH9_HULI_JING — Huli Jing Appears
# =============================================================================

label ch9_huli_jing:

    play music ost_huli_jing fadein 1.0         # PLACEHOLDER — Huli Jing ethereal theme

    huli_jing "Hihihihi~"

    niko      "Wait... Did you hear that?"
    chung_hee "No. For the hundredth time, no."
    magnus    "I heard it. I think it's... a laugh."
    huli_jing "Hihihihi~"
    yuxuan    "Eek! What was that?"

    "A whisper of laughter, high and melodic, like wind chimes swaying in a summer breeze. The air itself thickened, humming with unseen energy. A delicate floral scent, subtly sweet, curled into the steam rising from the springs."

    huli_jing "Ahh, what a luxurious sight! A gathering of warriors, scholars, and lost souls-all marinating like dumplings in a pot."

    "A faint tinkling of bells accompanied soft footsteps, the sound of water rippling as a figure gracefully stepped into view."
    "Perched atop a rock at the edge of the spring, half-shrouded by mist, was a fox."
    "Nine, impossibly long tails curled elegantly around her, their tips flicking idly, as if brushing away unseen dust motes of magic. Her golden eyes-slit-pupiled, like molten amber-watched us with quiet amusement."

    show cg_huli_jing_spring with dissolve      # PLACEHOLDER — cg_huli_jing_spring

    huli_jing "Oh, don't look so startled, my handsome bathers... You wouldn't deny a lonely fox the pleasure of a little conversation, would you?"

    "The being's laughter echoed through the mist, melodic yet uncanny, like a song sung in reverse. The steam curled tighter, shifting unnaturally, as if the very air around us was holding its breath."
    "A faint pressure settled in my chest-an instinctual warning, ancient and primal. Then I saw it."
    "Not just the nine flowing tails..."

    scene bg_hot_spring with dissolve           # PLACEHOLDER — hot spring

    svante "She's a fox spirit. A huli jing."
    svante "My mom told me and Kristin stories. Said they were born from moonlight and starlight. They've lived for centuries... maybe since the first breath of the world when the Weaver made the Tetrad."
    dorian "And what do they want?"
    svante "That's the thing. No one ever knows."

    "His voice lowered, nearly reverent."

    svante "Some are kind. Protectors. But most of them? They bring ruin with a smile. Trick kings into giving up empires. They love riddles, deals... They whisper and let you think you've won-until the price seeps in through the cracks you forgot were there."
    svante "They've whispered to emperors... to gods. Inspired love, betrayal, even genocide. And sometimes, they simply watched. Waiting."

    "The Huli Jing tilted her head, her smile curling wider, inhumanly so."

    huli_jing "Mmm... clever boy. A shame your mother never told you the most important part."
    huli_jing "We never knock twice."
    niko      "Yuxuan, you didn't say there'd be an ancient spirit here!"
    yuxuan    "But I... I always bathe here! Miss Weng too! Tim as well. We never-!"
    huli_jing "Of course not, my entrepreneurial little beetle. We don't come for the scent of soap, sweat, and money."

    "She tilted her head, and her nine tails unfurled behind her like a blooming chrysanthemum, each one stirring the steam with ethereal grace."

    huli_jing "I came because I smelled something rare..."
    huli_jing "Among your gathering... I scent the blood of an emperor. The son of a king. One who has been chosen by the death god. One... touched by a deity's longing. And one..."

    "She turned her gaze to me. And the air stilled."

    huli_jing "Praise the Prosperity Dragon indeed..."
    chung_hee "What do you want, spirit? Speak plainly."
    huli_jing "This spring... the mist that dances on its surface... the dreams that bloom when one sinks into its warmth-"
    huli_jing "These were once mine... before I was betrayed. Before I was slain mercilessly by the Death God Enoch himself."

    "Niko, lounging with a towel over his head, didn't even lift his gaze."

    niko "You creatures probably deserved it, given your kind's reputation."
    huli_jing "Understandable... for a lapdog to bark what it cannot comprehend. But I'll pretend I didn't hear that-your heart beats too loud with something else."

    "One tail coiled like a ribbon around her waist, the others slowly dancing in the air like smoke given form."

    huli_jing "Now, centuries later, you've stumbled in my spring. And I can smell it... all of you. You're tangled up in fate, in longing."

    "She looked at me again, that same unreadable expression."

    huli_jing "I am lonely. And I wish to play."
    huli_jing "If you agree to my game, I promise: I will never trouble you again. In return, I will answer one- and only one-question. From the spirit world. From the place where truths hide and mortals dare not look."

    "The mist pulsed once, as if alive."

    huli_jing "No tricks. No riddles. Just truth."

    "My heart quickened. One question."

    prosperity_dragon "The Huli Jing knows more than she speaks. The knowledge she carries lies coiled in riddles older than your bloodline."
    prosperity_dragon "She could speak answers that even the Tetrad have forgotten."
    huli_jing "But if you refuse..."
    chung_hee "Then what? You'll kill us?"
    yuxuan    "AH! Prosperity Dragon save me!"
    niko      "You're more than welcome to try."
    huli_jing "No, no. I don't spill blood. My fur is too good for that."
    huli_jing "I'll curse this spring for a thousand years. Every bather after you will think they've slipped into paradise, only to discover they're soaking in..."
    huli_jing "Fermented foot fungus stew."
    chung_hee "Pardon me?"
    magnus    "F-Fermented foot fungus stew?"
    yuxuan    "EWWW! I bathe here all the time!!"
    svante    "I... I think I'm gonna be sick... blarrrghhh!"
    huli_jing "Hahaha! Your guests will be smelling like the Tetrad's feet by the time they finish bathing!"
    niko      "*sighs*"
    huli_jing "So, my beautiful dumplings... Shall we play?"

    "I looked around the spring, its mist now feeling heavier somehow-less soothing, more watchful. My eyes met Svante's. He was looking around too, brow furrowed deep in thought."

    svante    "She said she can answer one question..."
    niko      "Don't be stupid, Svante."
    svante    "I'm not being stupid, Niko. I was just thinking that maybe we need it!"
    niko      "She said no tricks-but that's the trick. You said it yourself: spirits like her oftentimes never play fair. You'll think you're getting a straight answer and wind up cursed, or worse."
    chung_hee "Niko's right, Svante."
    chung_hee "Every version of this tale ends the same way. We had stories like that in Kyeongjang too. Not of the Huli Jing-but spirits with games, riddles and promises."
    chung_hee "An innocent hero. A ruined life. Don't be a storybook idiot, Svante."
    svante    "I... I hate to say it, but you may be right."
    magnus    "But... what if she's telling the truth? Not all spirits are malevolent."
    magnus    "One question. One truth. Think about what you could learn. Something no divine, no scholar, no channeler could tell us."
    magnus    "Isn't that worth a little risk?"
    yuxuan    "I want to do it!! We have to do it!!"
    chung_hee "But... why?"
    yuxuan    "I-I always bathe here! So does Miss Weng! And Tim! We come here every day! If she curses this spring, it'll smell like foot fungus for a thousand years!"
    yuxuan    "I can already imagine the smell! I have to do something!"
    yuxuan    "I AM CHENG YUXUAN, an inventor of great renown. And I will NOT BE SMELLING LIKE SOMEONE'S FOOT!"

    "He nearly slipped on the rocks trying to make his point."

    yuxuan "AHHH!!"
    dorian "Yu! Careful!"
    yuxuan "Do you know how expensive this place is?! I spent a lot of coin to refurbish this place!"
    niko   "How much would that be?"
    yuxuan "A LOT!!"

    huli_jing "Ahhh, the little beetle speaks sense~"

    "She cooed, lounging now on her side, chin propped up by one delicate hand."

    huli_jing "So? What will it be, dumpling?"

    "The mist curled around my fingertips. I didn't know what pushed me to speak, but the words came anyway."

    yuxuan    "Do it! Do it!"
    dorian    "I'll do it. I agree to the game."
    chung_hee "Fine. I trust you, Dorian."

    jump ch9_judgment_mjoll


# =============================================================================
# SECTION 6: LABEL CH9_JUDGMENT_MJOLL — Illusion: Mjoll / Fynn Hjorth Trial
# =============================================================================

label ch9_judgment_mjoll:

    # [COMMENT: bg_mjoll_town_square — snow, stone buildings, shackled man in center]
    scene bg_mjoll_town_square with flash       # PLACEHOLDER — Mjoll town square illusion
    stop music fadeout 0.5
    play music ost_judgment_mjoll fadein 0.5    # PLACEHOLDER — Mjoll judgment theme
    play sound sfx_judgment_chains              # PLACEHOLDER — chains SFX

    "The mist curled tighter the moment the words left my lips. It coiled like a serpent around my limbs-soft, almost warm-and then turned cold."
    "The springs vanished."
    "In their place, snow."
    "The world around us shimmered, then cracked like glass. Wind howled past us, biting at our skin, lifting flurries of snow into the air like ash. But I still felt the heat from the hot springs."

    magnus    "O-Oh. Oh no. We're still in our undergarments!"
    yuxuan    "AH! I can't be seen wondering around in my undergarments! Think of the bad publicity!"
    svante    "W-What?! This is Mjoll! This is my hometown!! I can't be here! Not like this!"

    "He wrapped his arms around his chest, cheeks blazing red."

    niko      "You're not used to your brothers seeing you in your undergarments?"
    chung_hee "It's not real. Look at the snow-doesn't melt when it hits your skin."

    "He held out a hand. True enough, the flakes dissolved before they touched him."

    dorian    "We can also feel the heat of the hot spring's waters."
    chung_hee "It's just an illusion. A trick. The spirit's game."

    "The snow parted. In the middle of the town stood a man, shackled and bare-kneed in the snow. Blood streaked the front of his torn tunic. Before him, crumpled in the red-stained snow, were two villagers-a woman and a child. Motionless."

    huli_jing "This man, Fynn Hjorth, is a follower of the death god."
    huli_jing "He killed his neighbor and her daughter in the dead of night. Stabbed them both. Took their coin. I'll leave you to it."

    "Fynn raised his head. His face was pale, eyes sunken and wild."

    fynn "Enoch told me to do it! He told me to cleanse them! To protect the town!"

    "She sat atop a stone throne of ice that hadn't been there before, tails draped like velvet across her lap."

    huli_jing "Now, as part of our little game... you will judge him."
    huli_jing "Death, exile, or forgiveness."

    "I stood frozen. Not from the cold, but from the sheer weight of it all."

    chung_hee "We were to judge a man's life. Such a burden to carry."

    "The wind grew louder. Or perhaps it was the breath of the spirits gathering to hear our verdict."

    huli_jing "Spirits, be our witness."
    huli_jing "Choose wisely, my dumplings. There is no appeal in this court. Your decision is FINAL."

    "I looked at the man in the eyes. A man broken, or a man twisted? A misguided zealot? A monster wearing a mask of devotion?"
    "But now... the judgment was mine to cast."

    menu:

        "Pass the judgment of Death.":

            "I closed my eyes. The cold air kissed my skin, but I felt nothing-only the weight of my decision. I raised my hand, flame flickering to life in my palm. Not a warm flame. A crimson one."

            dorian "He took two innocent lives. That cannot be forgiven. We sentence death."

            "A tremor rippled through the ground. The snow around Fynn shattered into sharp shards as the spirits surged up from beneath. He screamed-but it wasn't a scream of fear. It was something worse. A scream of belief."

            fynn   "I was chosen! I was doing Lord Enoch's work! You'll see!"
            svante "You murdered a mother cradling her child. You didn't cleanse anything. You just wanted to kill!"
            yuxuan "You deserve it! Degenerate!"

            "The mist devoured him. No blood. No remains. Only silence."

            huli_jing "Hmm... decisive."

            "Her voice was unreadable-neither impressed nor disappointed."
            "She tapped her heart. The snow continued to fall. I felt heavier."

        "Pass the judgment of Exile.":
            $ huli_jing_approval += 1           # +1 Huli Jing approval

            "I hesitated, staring into Fynn's frantic eyes. There was no remorse there-only delusion. But killing him would make me no better."
            "I extended my hand. A cold blue light bloomed in my palm."

            dorian "You'll not die here, Fynn. But you'll never walk these lands again."

            "The snow beneath him shifted violently, like it was trying to reject him."

            fynn "No... no, this is my home! I did what I had to! For the town! For Lord Enoch!"

            "The wind howled louder. His chains dissolved into frost, and something unseen dragged him backward into the mist-screaming, kicking, shouting for Enoch to save him."

            fynn "Lord Enoch! Lord Enoch your servant begs you! No!"

            chung_hee "Good. Take him far away from here. Should he ever return, death would await him."
            huli_jing "Hmm... merciful, but not weak."

            "Her voice was unreadable-neither impressed nor disappointed."

        "Pass the judgment of Forgiveness.":

            "The silence was unbearable."
            "Everyone waited. The spirits. The snow. The fox. I took a breath. My heart was hammering."

            dorian "He's broken. Not evil. If he can live with what he's done... let him. We grant forgiveness."
            fynn   "You... you're not killing me?"
            niko   "Yes. Continue walking in Enoch's path, brother."
            yuxuan "W-What?! Why are we letting him go? What is wrong with you, Dorian?!"
            chung_hee "Kindness or naiveness? I hope we aren't straying towards the latter."

            "Her voice was unreadable-neither impressed nor disappointed."

        "Investigate first and ask the others for their opinion.":

            huli_jing "Not ready to decide, dumpling?"

            "I took a breath and stepped forward. The wind bit at my skin, the illusion of snow somehow feeling far too real. I knelt in front of the man they called Fynn Hjorth. His eyes darted wildly."

            dorian "Tell me what happened. In your own words."

            "He looked up. Eyes-clouded, red-rimmed-twitched wildly in their sockets."

            fynn "They were touched by rot. The mother... I saw her. I heard her whispering at night, speaking to the dark, speaking to Saelara. She was offering prayers when she thought no one could hear."

            "The name landed like a stone in the snow. I felt more than heard a subtle shift in the mist."

            fynn "And the child. The child had silver eyes... the kind only a Tetrad follower would birth."
            fynn "Enoch sent me the vision. Clear as fire. Told me to cleanse them. To save this town."

            "He grabbed my wrist."

            fynn "I did it for Him. For Lord Enoch. His voice roared like a tempest! Oh, glorious, radiant death!"
            fynn "I felt His hand guide mine when I struck with the axe. I watched the life leave their heretic eyes, and I laughed, I laughed for Enoch!"

            "He broke into hysterical giggling. I pulled my hand away. I stood, heart a stone in my chest."

            chung_hee "Madness. I've heard stories like this in Kyeongjang. Men claiming divine voices told them to murder their own kin. It's never justice. It's bloodlust wrapped in prophecy."
            magnus    "But... is it really forbidden? Tetrad worship?"
            svante    "In Mjoll, yes. It's punishable by death. Especially Saelara... Her worship is considered the gravest blasphemy. Father says her name poisons the wind."
            svante    "But I rarely see Tetrad worshippers punished for it. Some keep their heads down. Live quietly. They're not hunted unless they cross a line."
            svante    "Still... my mother always told me: \"Too much mercy for the killer becomes cruelty to the dead.\""
            niko      "Maybe Fynn did see Enoch. You'd be surprised how often the divine walks among us, especially when desperation opens the door. You speak of madness-but what if he really was chosen?"
            yuxuan    "Are you joking? He murdered a mother and her child in the name of your rotting corpse deity! You defend this?"
            niko      "Only those who follow a sane god can understand the cost of divine obedience. Unlike others who would worship an overgrown lizard."
            yuxuan    "LIZARD?! HOW DARE YOU- The Prosperity Dragon ISN'T A LIZARD!"
            chung_hee "The two of you, calm down."

            "Magnus took a careful step toward Fynn, expression soft but troubled."

            magnus "You took two lives, Fynn. A mother and her child. Look at me."

            "Fynn raised his head, trembling."

            magnus "Do you feel it? The weight of what you've done? Do you... regret it?"

            "Fynn stared at him. For the briefest second, a flicker of uncertainty passed through his eyes-like a man waking from a terrible dream. Then his lips split into a smile."

            fynn "No. I was chosen. I'd do it again if my Lord commanded me to."
            fynn "ALL HAIL LORD ENOCH!"

            "The air turned still. Even the snow seemed to freeze in place."

            huli_jing "Ooooh... how deliciously complicated. Mortals and your morality. So-will you judge, dumplings?"

            jump ch9_judgment_mjoll

    jump ch9_judgment_hinami


# =============================================================================
# SECTION 7: LABEL CH9_JUDGMENT_HINAMI — Illusion: Hinami / Katashi Morita Trial
# =============================================================================

label ch9_judgment_hinami:

    # [COMMENT: bg_hinami — cliffside, blue sky, crashing waves below]
    scene bg_hinami with flash                  # PLACEHOLDER — Hinami cliffs illusion
    stop music fadeout 0.5
    play music ost_judgment_hinami fadein 0.5   # PLACEHOLDER — Hinami judgment theme

    "Then, the air shifted again."
    "The bitter cold of Mjoll vanished like melting frost. In its place came warmth-salt-laced and sun-kissed. The world opened into color and light."
    "Suddenly, we were standing atop windswept cliffs beneath a wide blue sky. The scent of the sea wrapped around us, briny and deep. Waves thundered against the rocks below, their rhythm steady."

    svante "W-We're not at Mjoll anymore."
    magnus "Really? Where are we now?"
    niko   "Hinami..."

    "He stepped forward, lifting his face to the wind."

    niko      "This ocean scent... It's unmistakable. It's from Hinami."
    chung_hee "That's right. You said you were from Hinami..."
    huli_jing "That's right! Welcome to Hinami, little dumplings! Ahhh... can you feel it?"
    huli_jing "The salt in your lungs, the sun on your cheeks? A perfect day for judgment."
    svante    "A-Another judgment?!"

    "She turned, fox tail swaying."

    huli_jing "Look behind you, dumplings."

    "We did."
    "Chained to the jagged cliff face was a man. Arms outstretched, his body crucified by salt and time. His skin was rough and sun-darkened, his clothes tattered and clinging to his frame. Bruises ringed his wrists where iron bit into flesh. The tide lapped at his ankles like a patient predator. With every swell, he shivered."
    "Below him, kneeling in the wet sand, was a woman. Her shoulders shook with sobs as she clutched a bundle of soaked cloth to her chest."

    emi "Please! Please, he didn't mean any harm!"

    "Her cries echoed across the shore. Even the seagulls were silent."

    huli_jing "This man is Katashi Morita. Once a fisherman. Now heralded as a thief."

    "She gestured to the girl, who clung to a soaked bundle of cloth."

    huli_jing "And that is Emi, his daughter. She's been crying since dawn."
    emi       "Please! Save my father. I beg you!"
    huli_jing "Ah, this game is divine. You know the rules, my dumplings. Like before-you judge."
    magnus    "Just like before... Justice is not a sword, but a wave. It wears you down. It erodes the soul. It asks you to stand in the storm and never flinch."
    huli_jing "Well said, pretty one."
    huli_jing "So, beloved judges... what now? This island's laws are clear. Theft is theft. And the punishment?"
    huli_jing "DEATH."
    yuxuan    "D-Death? Niko-tell me that's not true."
    niko      "It depends on what was stolen. On who it was stolen from. And why. Hinami's laws are old... and not always kind."
    huli_jing "But here, your judgment holds sway. What will your choice be?"

    "I looked at my companions. Magnus whispered, barely audible."

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

            huli_jing "Ah, cold justice... Spirits, let it be done."

            "There was a faint sound-like metal on stone-as the chains coiled tighter. The wind howled."
            "Then, the wave rose-taller than any before, unnaturally high, as if the sea itself was delivering judgment. It crashed forward."
            "And when the water receded... he was gone."

            emi "NO! FATHER! FATHER! PLEASE!"

            "The tide tugged gently at the hem of her dress, as if trying to comfort her. But there was no comfort here."

            svante    "I... I thought we were better than this."
            magnus    "I hope you're proud of yourself, Dorian."
            niko      "The law is not kindness, it is structure. And Katashi knew what he risked when he broke it."
            niko      "We cannot let emotion blind us. That is how justice becomes chaos. Dorian did what needed to be done, even when it hurt. That is the mark of a real judge."
            yuxuan    "\"wE cAnnOt lEt eMotIon bLind Us\" Hmph!"

            "Niko rolled his eyes."

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

            chung_hee "He will live. That, in itself, is a mercy most do not receive."
            niko      "This is mercy, by Hinami's standards. And mercy... is a rare, dangerous thing. Enoch, please forgive us..."
            yuxuan    "I don't care about Enoch's forgiveness."
            magnus    "Wherever the sea carries you-may it carry you to peace. I wish you both the best."

            "Huli Jing twirled one tail lazily."

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

            niko   "This will... upset the elders. Enoch, judge us gently. We have strayed from the letter of the law-but perhaps not its spirit."
            magnus "Let them be upset. If the law cannot bend for the starving, then it deserves to break."
            yuxuan "Yeah! What Magnus said!"
            svante "I hope the world is kinder to you from now on. I hope it gives you peace. You both deserve it."
            magnus "Justice without mercy is a sword that rusts in its own blood~ Let this tide wash away the weight-let love be understood~"

            "Katashi and Emi turned, bowing deeply. The shadows returned-silent escorts. But this time, they walked behind, not leading them like prisoners-but following them like guardians."

            huli_jing "...!"

            "Huli Jing smiled wide, teeth sharp but gleaming like polished pearls. Her silver tails flicked in satisfaction."

        "Investigate first and ask the others for their opinion.":

            dorian "Before we make any decisions... I want to speak to Katashi first."
            emi    "Please, sirs! I beg of you!"

            "Tears streamed down her face, her hands clutching the soaked hem of her robe."

            huli_jing "Don't worry, dumpling. Your father's fate will be spun soon enough."

            "She tapped her chin with a lacquered claw, eyes gleaming."

            magnus  "Kind sir... What do you have to say for yourself? Do you deny the charges laid upon you?"
            katashi "I do not deny it. I broke the law."
            katashi "But tell me-is it justice to watch your child starve? Is it noble to let your daughter bathe in saltwater while nobles hoard rose oils and perfumes? I am no saint. But I would steal again if it meant she could eat."
            chung_hee "Eat, you say? Then enlighten us, Katashi Morita. What prize did you deem worth breaking the King's law?"
            katashi "A loaf of bread. A sack of rice. A bar of soap. Two dried fish."

            "Svante looked like he'd been punched."

            svante  "T-That's it? Just food and soap?"
            emi     "We were starving! We hadn't eaten in days. Please... he didn't want to steal. I begged him not to... but-he did it for me!"
            dorian  "Where did you steal the food and soap?"
            katashi "... I stole from the home of Lord Nakai."
            niko    "Merciful En-... Lord Nakai?!"
            niko    "You've either got guts or a death wish. Might as well stroll into a yaoguai king's den and ask for a cup of tea."
            svante  "Who is Lord Nakai, Niko?"
            niko    "One of Hinami's high lords. Second only to King Tatsuya Fujiwara. He commands the military and answers to no one but the crown."
            niko    "The man would have you flayed for touching his wine cellar, let alone stealing from his kitchens."
            katashi "I knew the risk. But his servants throw away more food in a week than most villages see in a season. I couldn't watch her waste away. Not again."
            chung_hee "Again? What do you mean... 'not again'?"
            emi     "We had... a sister. Her name was Maru."
            emi     "She died last winter. Her belly swollen from hunger, her skin cracked and cold. We had no firewood. No rice. No medicine."
            katashi "Lord Nakai never paid us our wages. We toiled from dawn till night, patching nets and scrubbing floors. But when the season ended, his men said we were too late-too slow. No coin. No food. No justice."
            katashi "I swore I'd never lose another child."
            emi     "Please! I beg you-don't take him from me..."

            "She suddenly stumbled toward Chung-hee, dropping to her knees and clutching his bare ankles."

            emi "Please, your highness, your grace-anything! Take my life instead! I'll serve-I'll go in his place! Just let him go!"

            "She lowered her face, lips trembling, and pressed them against his foot. Svante blushed and shielded his face."

            svante    "N-No! Please don't do that, we're still in our undergarments!"
            chung_hee "H-Hey... that's-this is highly improper. Please rise. There is no need for... such a display."
            huli_jing "Hey! No touching the judges! That's against the rules!"
            yuxuan    "This is preposterous!"
            yuxuan    "I am Cheng Yuxuan, an inventor of great renown! I've contributed to the advancement of technology in countless kingdoms! And yet, here I am, in my undergarments in front of all to see!"
            yuxuan    "You could have at least gotten us some clothes before making us judges, you know!"
            huli_jing "And where's the fun in that?"
            emi       "Please! I'll scrub floors-I'll beg Lord Nakai himself-I'll cut off my hair, my hands, just please... don't let him die!"

            "Her words hung in the salt-heavy air, raw and aching."
            "I turned to the others, the wind pressing against my back like a tide urging me to speak."

            dorian    "You've heard him. Now I ask you-what do you think?"
            niko      "According to the teachings of Lord Enoch, the law is the spine of civilization. Harsh? Perhaps. But mercy without order is rot without bone."
            niko      "\"When one man steals with no consequence, a hundred more will follow. Then who feeds the honest?\" That's what Enoch teaches. The law must stand-or all things crumble."
            chung_hee "As the Emperor of Kyeongjang, I've had to pass judgments that weighed heavy on my heart."
            chung_hee "Aunt Ji - I mean, my royal advisor once told me, \"Compassion must walk behind law, not in front of it.\""
            chung_hee "Order is fragile. If the law bends for sympathy, how long until it breaks for greed?"
            yuxuan    "But what kind of justice punishes a starving man trying to save his daughter? Are we really protecting society?! Or just the pride of the rich?"
            niko      "You're one to talk. You're one of the rich yourself."
            yuxuan    "I try to feed as many as I can! I give what I have! I- I don't punish love with death! If we are going to punish him, at least don't kill him!"
            svante    "W-We should forgive him. Please. What kind of world punishes love like this?"
            svante    "A father's love... I..."

            "Then, Magnus stepped forward. His eyes were on Katashi, but his voice was lifted to the crashing sea."

            magnus "I don't care what the law says."
            magnus "Justice without compassion is cruelty dressed in gold. If the law demands we turn away from the hungry, then the law has already failed."
            magnus "Look at her. Look at him. Tell me-are these the faces of danger? Are these threats to the throne?"
            magnus "Break the chains. Feed them. Heal them. That is the kind of kingdom I would fight for."
            niko   "This isn't about threats, Magnus. It's about precedent. The moment the law yields, even once, every tyrant will find cause to twist it."
            chung_hee "As much as it pains me, I must agree. The law is not a feeling-it is a pillar. Without it, we drift."
            huli_jing "Mmm... such passion. Such division. Oh, my dumplings... what a delightful dilemma."
            huli_jing "Well then, Dragon of Gale... it falls to you."

            "I then turned to the Huli Jing."
            "I turned to look at them all-at Katashi, crucified by justice; at Emi, drowning in desperation; at the sea, endless and roaring. The world held its breath."

            jump ch9_judgment_hinami

    jump ch9_judgment_kyeong


# =============================================================================
# SECTION 8: LABEL CH9_JUDGMENT_KYEONG — Illusion: Kyeongjang / Seorin Im Trial
# =============================================================================

label ch9_judgment_kyeong:

    # [COMMENT: bg_kyeongjang_palace — palace courtyard, pagodas, marble platform]
    scene bg_kyeongjang_palace with flash       # PLACEHOLDER — Kyeongjang illusion
    stop music fadeout 0.5
    play music ost_judgment_kyeong fadein 0.5   # PLACEHOLDER — Kyeongjang judgment theme

    "The air shifted again-sharp and dry, like brittle parchment touched by flame. The scent of lotus blossoms and aged ink reached my nostrils, thick and heady. My feet met smooth stone, cold to the touch. I looked around slowly."
    "We were no longer near the sea."
    "Towering pagodas surrounded us, their curved rooftops gleaming with gold leaf beneath a pale sky. The very ground vibrated with power-a coiled pressure humming just beneath the surface."
    "I blinked, adjusting to the light that struck the stone courtyard like polished jade. And then-I saw her."
    "A woman knelt in the center of a marble platform, chains wrapped tight around her wrists. Her hanbok was torn, stained from travel or shame. Her long black hair hung in tangles, but even in ruin, she carried a strange grace."
    "She raised her head. Her hollow, desperate eyes locked onto one of us."

    seorin "Y-Your Majesty?"

    "Chung-hee was startled. His face flushed, and he shifted awkwardly, hand tugging at the edge of the towel slung over his shoulders. We were, after all, still in our undergarments."

    chung_hee "Seorin seonsaengnim?"

    "Huli Jing cooed from above, now reclined on a gilded parasol carried by an unseen force, her nine tails fanned out like a blooming chrysanthemum."

    huli_jing "Ahhh, so he does know her. Even better. The final judgment will cut closest to the heart."
    dorian    "Wait... You know her, Chung?"
    chung_hee "She was my past mentor. In alchemy. Before I ever wore the crown."

    "He narrowed his eyes at the ornate architecture."

    chung_hee "With this vision, I take it we stand in Kyeongjang?"
    huli_jing "Right you are, dumpling! Welcome back to the capital!"
    svante    "W-Wow... This is Kyeongjang? It's beautiful..."
    yuxuan    "PRAISE THE PROSPERITY DRAGON! KYEONGJANG! AT LAST!"
    yuxuan    "I have waited for this moment my entire life! My life's work has led me to this moment! Niko, pinch me! I must be dreaming!"
    niko      "This is still an illusion, Yuxuan. Part of the Huli Jing's game."
    magnus    "Beautiful, magnificent Kyeongjang! Oh, how noble your towers, how gleaming your-"
    dorian    "Magnus. Please. Save the ballad for later."

    chung_hee "Seonsaengnim. Explain yourself."
    seorin    "Y-Your Majesty! I didn't mean for any of it. I swear it, I didn't."

    "Her voice cracked as she tried to rise, but the chains held her fast."

    huli_jing "Seorin Im. Scholar. Once one of the most promising alchemists in the Empire. Tasked with crafting a powerful medicinal salve for the royal hospital-one that would heal plague, infection, and injury alike."
    huli_jing "But her alchemy was flawed. The ingredients, unstable. Instead of healing the sick..."
    huli_jing "...it poisoned them. Fifty-five souls. Gone. Thirty-seven imperial soldiers. Eighteen children. Every last one who drank the salve died within hours."

    magnus "Those... Those poor children..."
    dorian "Tetrad above..."
    niko   "Unforgivable. I've seen things like this in Hamatame. Villagers dosing the sick with faulty tinctures, hoping for miracles. It always ends in death. You don't gamble with lives-not as a healer. Not ever."
    seorin "I-I didn't know, Your Majesty! It was a mistake! Please, I beg you!"

    "She turned to Chung-hee, voice trembling, heart in her throat."

    seorin "You know me, Your Majesty... You know I would never do this deliberately."

    "Around the platform, ghostly silhouettes began to appear-spirits with soft blue eyes and pale robes, their hands clasped before them as if in mourning."

    huli_jing "So... my beautiful dumplings. For the last time. Death, exile, or forgiveness?"
    niko      "Last time? Great."
    huli_jing "The dead don't speak, but they remember. And they are watching."

    "She grinned, sharp as a blade."

    huli_jing "Judge wisely, Dragon of Gale. This one cuts to the bone..."

    menu:

        "Pass the judgment of Death.":

            "I closed my eyes. The weight of it all pressed down on my chest like iron."

            dorian "Seorin Im. By your own admission, your salve was unstable. Your negligence took the lives of children, soldiers... innocent people who trusted you."
            dorian "We pass the sentence of death to you, Seorin Im."
            seorin "No... Your Majesty-please! You know me-!"

            "But her voice broke as Chung-hee turned away."

            chung_hee "I did know you once."

            "The shadows moved without a sound. Like a tide, they rose-liquid, cold, inky-and swallowed her whole."

            seorin "No! No! Get away! NO!"

            "They enveloped her. And then- Silence. She was gone."
            "Yuxuan muttered a prayer under his breath."

            yuxuan    "By the Prosperity Dragon... may her spirit find peace."
            niko      "She made her choice long before this moment. Enoch teaches: mistakes may be human, but consequences are divine."
            chung_hee "I am sorry, Seorin seonsaengnim. I wish the stars had guided your path elsewhere."
            magnus    "...So many lives. So many lost. But in the end... it was her hand that made the poison."
            huli_jing "So cruel... and yet so just. Your judgment echoes through the heavens, dumpling."

        "Pass the judgment of Exile.":
            $ huli_jing_approval += 1           # +1 Huli Jing approval

            dorian "Your negligence caused suffering on a scale we can't ignore. You are exiled. You will never set foot on Kyeongjang soil again."

            "I turned to Chung-hee, who gave a solemn nod."

            chung_hee "I have no qualms with the judgment, Dorian."

            "Her voice cracked, but she did not argue."

            seorin "I... I understand. Thank you."
            chung_hee "Farewell, Seorin seonsaengnim. I wish the stars had guided your path elsewhere."

            "Chains dissolved into smoke. She crumpled to the ground, then rose, trembling. The spirits turned their backs on her as she was led away by shadowy guards."

            seorin "Farewell, Your Majesty."

            yuxuan    "That was fair. Harsh... but fair."
            niko      "She'll never escape the guilt. That's a heavier sentence than steel."
            huli_jing "A punishment without blood... elegant, in its own way."

        "Pass the judgment of Forgiveness.":

            dorian "Seorin Im. You made a mistake. One you'll carry the rest of your life. But we believe in redemption... and we believe you would give your life to take it all back."
            dorian "And for that, we pass the judgment of forgiveness to you, Seorin Im."
            seorin "A thousand thank yous would not suffice. I... I will not waste this chance."

            "Her wrists slackened as the chains uncoiled, shimmering into mist. She gasped, then clutched her own hands tightly, tears running freely."

            seorin "Thank you... Thank you..."

            "Chung-hee stood motionless, the wind ruffling the towel at his shoulders. His hand trembled slightly at his side. Then, with difficulty, he gave a single, solemn nod."
            "The shadows returned-not as hunters, but as silent escorts. They gathered around Seorin like quiet sentinels and began to lead her away."

            yuxuan "Dorian buddy, that was brave! I think you did the right thing."
            magnus "I wouldn't claim it was the right thing... But if justice can wear a gentler face, then let it be this one. My heart is at peace with the path we've chosen."
            niko   "You forgave her. And now she walks away. Just like that."
            niko   "I hope those fifty-five souls get to walk too. I hope the parents of those children get to wake up tomorrow without weeping. I hope the soldiers get their years back."
            niko   "But they won't. I hope you understand that."
            svante "I... I want to believe people deserve a second chance, but... I kind of agree with Niko. That many lives? It's hard to forgive fully."
            huli_jing "Oh, you tender little dumpling. Mercy is a delicious flavor."

        "Investigate first and ask the others for their opinion.":

            "I turned to Chung-hee and met his gaze. I gave a nod. He returned it, slower, and he stepped forward."

            chung_hee "Seonsaengnim. Start from the beginning. Tell us everything."
            seorin    "Yes, Your Majesty. I will."
            seorin    "I was tasked to create a salve powerful enough to heal plague, infection, burns... everything. I studied night and day."
            seorin    "I tested it thoroughly on rats, on plants, even small doses on myself. Every result was stable. As the Almighty Tetrad Immortal Renji is my witness."
            seorin    "But the supply-when it scaled to mass production... something changed. I swear I didn't alter the formula. I had no idea the ingredients had spoiled, or reacted differently in bulk..."
            niko      "You didn't realize it was poison after it was distributed?"
            seorin    "No-I didn't... I didn't even know until I heard the soldiers were dying. Then the children..."

            "She looked down."

            seorin "By then it was too late. I rushed to the lab, ran test after test. It was the main reagent-it had turned unstable in storage."
            seorin "But it was already in the hands of the sick. Already killing them."
            yuxuan "This is... this is a disaster. A total collapse of safety protocols. How was this even allowed to pass inspection?"
            yuxuan "Cheng Industries better not be cutting corners like this. I'll need to audit our entire healing division. This can't ever happen in Tianho."
            seorin "And then I was arrested and brought here..."
            seorin "Your Majesty, please... I beg you. I was careless, yes. But not cruel. I never meant for harm."

            "I turned to the others. My chest was tight with the gravity of what I had to ask."

            dorian "For the last time. Tell me... what do you all think?"
            niko   "Even if it's just a mistake, it's a crime. And crimes have consequences. If we let her walk free, we say their deaths meant nothing."
            niko   "Fifty-five lives, Dorian. Fifty-five."
            svante "Niko's right. Their lives can't go unanswered. Forgiveness doesn't erase the dead."
            yuxuan "I don't know. I... I see her remorse. But can we risk others thinking a mistake like this is acceptable?"
            magnus "She should not die. Death is final. She would learn nothing. Heal nothing. Let her live with the grief she caused-and do something with it. Make her rebuild what she destroyed."
            yuxuan "But letting her walk away unscathed... Would that be fair to the ones that died?"

            "I turned again to Chung-hee, but before I could speak, he raised a hand."

            dorian    "This is your empire, Chung. Your people. If you wish to render judgment, I will stand aside."
            chung_hee "No. You should be the one to deliver judgment, Dorian."
            chung_hee "I am the Emperor of Kyeongjang. And because of that-I cannot be the one to judge her. I knew Seorin once. Admired her even. That bond clouds my mind even now."
            huli_jing "Ohhh, I love this. Look at all of you, writhing on the hook of morality."
            seorin    "Please, Your Majesty!"
            huli_jing "So have we made a decision, dumpling?"

            jump ch9_judgment_kyeong

    jump ch9_judgments_back


# =============================================================================
# SECTION 9: LABEL CH9_JUDGMENTS_BACK — Common: Back to Hot Spring
# =============================================================================

label ch9_judgments_back:

    # [COMMENT: bg_hot_spring — back to hot spring]
    scene bg_hot_spring with flash              # PLACEHOLDER — hot spring return
    stop music fadeout 0.5
    play music ost_huli_jing fadein 0.5         # PLACEHOLDER — Huli Jing theme

    "The air shifted one final time."
    "The incense, the towers of Kyeongjang, the weight of our choices-all of it faded like breath on glass. The cold dissolved. The thunderous silence of the spirit realm gave way to something gentler."
    "Heat. Steam. The sound of water lapping gently at stone. We were back. In the hot springs."

    yuxuan    "By the Prosperity Dragon's blessed scales-we're back!!"
    niko      "That wasn't just illusion. That felt real. Too real."
    chung_hee "It was an illusion. I think. Tetrad above, I hope it was."

    "Magnus stretched dramatically, droplets flinging off his arms like golden ribbons."

    magnus "And yet... we're still in our undergarments. Perhaps now we can enjoy a proper bath without sentencing anyone to death."
    svante    "I don't think I'll ever look at justice the same way again..."
    huli_jing "Mmmm... Delicious, wasn't it? Judging mortals is no neat affair. It tangles the soul."
    huli_jing "Makes it chewy. Like good dumplings."

    if huli_jing_approval < 3:
        jump ch9_huli_reward_low
    else:
        jump ch9_huli_reward_high


# =============================================================================
# SECTION 10: LABEL CH9_HULI_REWARD_LOW — Fox Leaves Without Reward
# =============================================================================

label ch9_huli_reward_low:

    huli_jing "As for your judgments, my dear dumplings... I was a little underwhelmed. Mmm. Lukewarm, like reheated noodles."
    huli_jing "I gave you a game. A gift of truth. And you judged... mediocrely. Is that even a word?"
    dorian    "But you promised. You said you'd leave the springs."
    yuxuan    "Yes! You swore it on your tails, remember? We upheld our end."
    huli_jing "And a promise is a promise. I shall never again haunt these springs, nor return to soak my tails. You'll never see me here again. Pity... I was beginning to like you."
    magnus    "And we were starting to like you too, beloved fox!"
    magnus    "Farewell to the fox with the nine shining tails... To judgment and laughter where truth always sails...~"
    huli_jing "Wow! I love it, dumpling! I'm going to miss you!"
    niko      "Wait. You also promised one answer. One truth."
    huli_jing "Ah... but you failed the game. No answer for you. But I am not without gifts."

    "She snapped her claws-"

    play sound sfx_huli_fwoomp                  # PLACEHOLDER — FWOOMP SFX

    "FWOOMP."

    jump ch9_stuffed_fox_exit


# =============================================================================
# SECTION 11: LABEL CH9_HULI_REWARD_HIGH — Fox Grants Question
# =============================================================================

label ch9_huli_reward_high:

    huli_jing "As for your judgments, my dear dumplings..."
    huli_jing "I am beyond delighted. Compassion with justice, side by side... How refreshing."

    "A shimmer of foxfire circled her ankles as she floated down gracefully onto the steaming surface of the spring."

    niko "Well... that's reassuring. I was starting to question everything."

    "Chung-hee, ever the stoic, crossed his arms and gave the faintest, coolest nod."

    yuxuan "THANK YOU, PROSPERITY DRAGON! YESSS!!"
    magnus "I was sure I'd end up cursed. Or bald."

    "Huli Jing floated closer to me. The lavender steam coiled around her as if drawn by her warmth. Then her golden eyes narrowed, a glint of something ancient sparkling behind them."

    huli_jing "As a reward, I will grant something I haven't done in centuries, sweet dumpling. One question. Any question, and I will answer."

    "The air stilled. Even the steam seemed to hold its breath."

    svante "My mother used to tell stories about this... She said the Huli Jing only ever answered a single question as a reward before. Just once in all her lifetimes..."

    "My eyes widened. Is that true?"

    dorian "Really? Who did she answer?"
    svante "Li Mengtia. The Divine Tetrad of Knowledge and Wisdom. That was a thousand years ago."

    chung_hee "Dorian. Ask about the future of Ena. We need to know if the Divine Weapon still poses a threat."

    "My heartbeat slowed. The fox spirit smiled, nine tails curling gently around her."

    huli_jing "So, my dumpling... ask. One truth, one mystery, one thread in the grand weave of fate. I will answer. Just once."

    menu:

        "Ask about the future of Ena.":

            dorian "What's going to happen to Ena?"

            "The question hung in the steam like a thread pulled tight."
            "The Huli Jing paused, tilting her head. One tail slowly wrapped around her arm like a silken ribbon."

            huli_jing "Ahh... a noble and unselfish question. Very well, little dumpling. I will show you. But only for a moment. One breath. One heartbeat."

            "She lifted a single clawed finger to my forehead. Pain. Light. Fire."
            "A searing jolt ripped through me. My breath caught in my throat as visions burst behind my eyes."
            "Visions exploded in my mind- A crowned figure of fangs and molten eyes standing atop a throne of bones. Villages drowned in darkness. Temples burning under a red sky."

            huli_jing "He has awakened. The harmony of Ena breaks. But the tide has not yet turned..."

            "She leaned closer, her many tails coiling behind her like stormclouds."

            huli_jing "Dragonkin... Only you and your companions can stop him."

            "I swallowed hard, my hands still shaking. But she wasn't done."
            "Her voice dropped to a whisper that slid beneath my skin."

            huli_jing "He will come to you. Soon. He will make an offer. A deal. One that promises power... vengeance... salvation. He will make it tempting. He will make it feel right."
            huli_jing "Decline it. Do NOT give him the Divine Weapon. Do NOT give him Magnus. If you want Ena to survive, decline it without hesitation."
            huli_jing "Or Accept it... if you want to doom your world. Your choice, dumpling."
            huli_jing "But... since you passed my test with such heart, I doubt you will choose wrong."
            magnus "Someone's making you a deal? What kind of deal? Who is this bastard? When does this happen? What does it have to do with me?"
            chung_hee "Beware him, Dorian. Such creatures twist language like silk. They don't lie. But they do mislead. They'll offer you fairness... even justice. But beneath it, always: rot."
            dorian    "Thank you. For showing me."
            huli_jing "You can absolutely thank me by making the right choice, dumpling."

            "Her tail brushed my cheek like a whisper."

        "Ask how Elara and the kids are doing.":

            "I remembered them. Elara."
            "Daniel. Emily. Sarah. Lucas."
            "Their laughter. Their warmth. The sound of their feet running across the wooden floors of our home in Gale."
            "I felt the ache again. That terrible hollow ache I never dared to touch."

            dorian "How... how are my wife and the kids doing?"

            "The question slipped from me before I could stop it. My voice cracked."
            "The Huli Jing's smile faded. Her playful poise stilled. Her eyes, golden and ancient, turned solemn. There was a softness to her now-a reverence I hadn't seen before."

            huli_jing "Elara. That's your wife's name, isn't it, dumpling? Daniel, the eldest. Emily, so clever. Sarah, the dreamer. Lucas, your little star."

            "She gestured with a paw, and soft golden mist coiled from her tails as they lifted and coiled like ribbons of starlight, swirling into the air."
            "They stood beneath a warm, endless sky. Smiling. Whole. Unscarred by the world."
            "Elara's arm rested around Sarah's shoulder. Daniel stood tall, hand protectively over his younger siblings. Emily clutched a bundle of flowers. Lucas was... laughing. Running in circles like always."
            "Behind them loomed a great golden gate, etched with stars and music and language I couldn't read but felt in my heart."
            "And just beyond that- The Halls of Xianlun. Realm of the noble dead. The honored. The brave. The pure."

            show cg_elara_xianlun with dissolve  # PLACEHOLDER — cg_elara_xianlun
            pause 2.0
            scene bg_hot_spring with dissolve   # PLACEHOLDER — hot spring

            huli_jing "They walk where pain cannot touch them now, dumpling. Brave, every one of them. They knew courage. They knew love. And that was enough."

            "A melody I couldn't name filled the air-like lullabies sung."

            huli_jing "They rest in song, Dorian. You gave them your everything. And they carried your love with them."
            huli_jing "They want you to live your life. And live you shall."

            "My knees gave out. I fell."
            "Niko was there-quiet, steady-catching me before I hit the ground."

            niko   "Easy, Dorian. Breathe."
            yuxuan "They made it to Xianlun. That's all any of us could hope for."
            magnus "Xianlun... The great halls. Rest in peace."
            dorian "Thank you... for showing me. I needed this."
            huli_jing "You're welcome, dumpling. And when your time comes... they will be the first to greet you at the gate."

        "Ask about your future.":

            dorian "What's waiting for me in my future?"

            "The Huli Jing's ears twitched."

            huli_jing "Your path is a tangle, dumpling. Woven of heart and blade... but you wish to know who walks beside you in the end, hmm?"

            "She touched my forehead. Visions bloomed."
            "Not of battle, nor glory-but moments. Shared laughter. Late-night talks. Someone bandaging my wounds."
            "A hand reaching for mine under the stars. A voice calling my name as if it was the only name they ever knew."
            "My companions. One of them. But which one? The vision blurred-never showing their face. Just the feeling. Of being loved. Truly. Without weight or duty or fear."

            huli_jing "I will not name them. But your true love... is already beside you. All that's left-is for you to see them clearly."

            "The vision faded. I blinked, disoriented."

            chung_hee "Was that a prophecy or a romantic prank?"

            "Yuxuan blushed, refusing to look up."

            yuxuan "T-The possibility of... me and Dorian... I-I wasn't prepared for that."

            "Magnus smirked."

            magnus "Did she show you me? Come on, you can say it."
            niko   "Magnus, don't you have a woman?"
            svante "Niko, he's been frozen for Enoch knows how long. Odds are she's dust."
            huli_jing "You all chatter like baby sparrows. But here, Dorian, more truths for your heart-if you dare take them."
            huli_jing "There will come a moment when your future lover will be the one to rescue you. And when that moment arrives... you must trust them. Let them save you."

            "She flicked a tail, and for a heartbeat, I saw fire. Pain. Then- hands catching me before I fell."

            huli_jing "And-there is a child in your life. The most important soul to you right now. There will come a time when they will need you the most... At that instance, choose your child over spending time with your love, Dorian."
            huli_jing "Lastly... never betray your lover. No matter how cruel the world becomes. Or how tempting it may be. Be the man they believe you are."

            "I swallowed hard. Another lover. Even hearing the words felt like betrayal. Could I even love again? Did I want to?"
            "Part of me whispered no."
            "But another part... the part that had long been silent... trembled."

            dorian    "...Thank you. For showing me."
            huli_jing "You can thank me by honoring them when the time comes. Be faithful, dumpling. With all your heart."

        "Ask about the secret to Gao's perfect Tianho flan.":
            $ chunghee_affection += 1           # +1 Chung-hee affection

            dorian "Okay, real question: What's the secret to Gao's flan?!"

            "Silence."
            "A long, awkward beat of silence."

            niko "...Merciful Enoch."

            huli_jing "Gao? You mean the soldier?"
            yuxuan    "Dorian means Li Gao. He's a retail worker for Cheng Industries. And yes, he was a soldier before. He makes... I mean his mom makes insanely good flan."

            "Huli Jing's tails froze. Her eyes went wide."

            svante "Can you imagine being one of the only mortals in history to be granted a question from an ancient, reality-bending fox spirit-and you ask about flan?"
            yuxuan "Dorian buddy, umm... I literally own the company he works in. I could've just... bought the recipe."
            huli_jing "Ohhh, dumpling! I adore it! Li Mengtia asked me about the essence of knowledge. You ask about custard."
            huli_jing "You are an icon. You are a legend. And you are the moment."

            "She twirled midair, tails drawing shapes in the steam, and whispered."

            huli_jing "It's salt. Just a pinch. Right after pouring the custard, before it sets. It sharpens the sweet. A secret as old as war and love."

            chung_hee "I KNEW IT! I knew it! I knew there was a mystery in that flan!"

            "Everyone turned."

            magnus "Well well well... His Majesty's got a sweet tooth!"
            niko   "Not you too, Chung."

            "Chung-hee froze mid-celebration. His cheeks flushed a little pink. Then, in perfect imperial fashion, he straightened his spine, dusted his undergarments and tucked his arms behind his back."

            chung_hee "...I was merely confirming a culinary hypothesis. Nothing more. Carry on. And stop calling me His Majesty."
            magnus    "? O Flan Divine, fit for a throne, praised by the Emperor all on his own... ?"
            chung_hee "Stop."

    "Huli Jing: Just for you, Dragon of Gale. Another gift. One that is very handy."

    "Her eyes sparkled as she leaned forward."

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
            $ love_route_locked = "yuxuan"
            $ yuxuan_affection += 3             # +++ Yuxuan affection

            "Yuxuan straightened, hopeful."

            dorian "I choose Yu."

            "His whole face lit up like the midsummer lantern festivals in Lanliang."

            yuxuan    "Dorian~! I knew it! I knew this was destiny! Take that, Niko!"
            niko      "...What did I do?"
            huli_jing "Oooh! A inventor's heart, gilded in pride and glitter."

            "She twirled in the air, one tail looping into a perfect spiral before she carved a sigil of light in midair. She tapped my chest with one claw, and warmth flooded through me."
            "I felt an odd tingling sensation."

        "Niko.":
            $ love_route_locked = "niko"
            $ niko_affection += 3               # +++ Niko affection

            dorian "I choose Niko."

            "Niko arched an eyebrow, skeptical."

            niko "Choose me? Choose me for what, exactly?"
            huli_jing "Hmm... The doctor who walks with death. The prophet of Enoch. Steady as stone, cold as snow, yet tender underneath. Delicious."
            magnus    "? Oh Healer of mine come soothe thee. Thine path is mine and yours to- ?"
            niko      "Magnus, quiet. Besides, you got the lyrics all wrong."

            "The Huli Jing drew a sigil in the air with a claw and touched my heart. I felt an odd tingling sensation."

        "Svante.":
            $ love_route_locked = "svante"
            $ svante_affection += 3             # +++ Svante affection

            dorian "I choose Svante."

            "Svante flinched at the attention, cheeks red. His hands fidgeted."

            svante    "You... You really mean that, sir-I mean, Dorian? Choose me for what?"
            huli_jing "Awwww! My sweet dumpling! You chose the softest bun in the basket!"
            chung_hee "Sweetest? He was sent to assassinate me yesterday."
            svante    "I-I beg your forgiveness once more, Your Majest-!"
            chung_hee "Svante, I jest. A ruler who cannot laugh has already lost half his kingdom. And I already accepted your apology. I do not give those lightly."
            svante    "I... Thank you, Chung."

            "The Huli Jing danced in the air, and with a flick of a claw, etched a glowing sigil in the steam before pressing it gently to my heart."

        "Chung-hee.":
            $ love_route_locked = "chunghee"
            $ chunghee_affection += 3           # +++ Chung-hee affection

            dorian "I choose Chung-hee."

            "Chung-hee's expression faltered for a moment. Just a moment."

            chung_hee "You honor me, Dorian."
            huli_jing "The Emperor of Kyeongjang! Oh, I didn't know you were into royalty, dumpling. A scandal! A story! And-wait, he can read our minds! Everyone-think pure thoughts!"
            chung_hee "I'll pretend I didn't hear that."
            huli_jing "Teasing, your Majesty. Just teasing. You're a difficult one to crack."

            "The Huli Jing drew a sigil in the air with a claw and touched my heart. I felt an odd tingling sensation."

        "Magnus.":
            $ love_route_locked = "magnus"
            $ magnus_affection += 4             # ++++ Magnus affection

            dorian "I choose Magnus."

            "He gasped, both hands dramatically clasped over his chest."

            magnus    "I knew it! The stars were right! The harp sang to me last night!"
            niko      "Of course it did..."
            huli_jing "An unknown heart, bright and wild. He'll break it, you know. But he'll write you a song for every piece."
            magnus    "? Love's a fire, bright and bold-let it burn or leave you cold~ ?"
            huli_jing "You're lucky he's charming. Now hold still."

            "She painted the sigil with three tails at once-effervescent and glittering-before placing it on my chest. I felt an odd tingling sensation."

    jump ch9_huli_exit


# =============================================================================
# SECTION 13: LABEL CH9_HULI_EXIT — CommonCommonCommon: Fox Farewell / FWOOMP
# =============================================================================

label ch9_huli_exit:

    huli_jing "And a promise is a promise. I shall never again haunt these springs, nor return to soak my tails. You'll never see me here again."
    huli_jing "I will be in Xianlun. With my family. Pity... I was beginning to like you."
    magnus    "And we were starting to like you too, beloved fox!"
    magnus    "Farewell to the fox with the nine shining tails... To judgment and laughter where truth always sails...~"
    huli_jing "Wow! I love it, dumpling! I'm going to miss you!"
    huli_jing "Alas, this is farewell. But I have one last parting gift."

    "She snapped her claws-"

    play sound sfx_huli_fwoomp                  # PLACEHOLDER — FWOOMP SFX

    "FWOOMP."

    jump ch9_stuffed_fox_exit


# =============================================================================
# SECTION 14: LABEL CH9_STUFFED_FOX_EXIT — Darkness / Toy / Everyone Pops Out
# =============================================================================

label ch9_stuffed_fox_exit:

    # [COMMENT: cg_black — total darkness]
    scene cg_black with fade                    # PLACEHOLDER — black screen
    pause 0.5

    "In a blink, the warmth vanished. Steam gone. Stones vanished. Comfort obliterated. Suddenly-squish. Pressed in. Too close. Far too close."

    dorian "What in the name of the Tetrad-?!"

    "I was squished-stuffed, really-inside what looked like a giant toy Limbs tangled, faces mashed together, undergarments sticking uncomfortably."

    dorian "Why... why can't I move my legs-"
    yuxuan "Ahhh! Dorian~! Just you and me and-wait, wait, someone's chest is in my-"
    niko   "Grr... Yuxuan. That is my chest. Kindly remove your hand."
    yuxuan "AHH! I thought it was Dorian!! Magnus, your foot-!"
    magnus "I'm trying! I'm trying! This is not how I imagined group bonding."
    niko   "Unbelievable... Chung, stop pushing!"
    svante "Wait-I think I found a lever!"
    chung_hee "T-That is NOT a lever! P-Please-unhand me!"
    svante "AHH! I-I'm sorry, Your Maj-I mean, Chung!"
    dorian "Svante, for the love of the Tetrad, don't lift your arms. I can smell your armpits-"
    svante "AHH! Sorry! Oh-Enoch above, smite me now-"
    "Everyone: *struggling sounds*"

    magnus "Oh brothers of steam, of springs and of soap, Entangled in trials~"
    "Everyone: Magnus. Shut up."

    jump ch9_kids_spring


# =============================================================================
# SECTION 15: LABEL CH9_KIDS_SPRING — Kids POV / Tim / Huli Jing Gift
# =============================================================================

label ch9_kids_spring:

    # [COMMENT: bg_hot_spring — Tim and Elias in the springs, playing]
    scene bg_hot_spring with dissolve           # PLACEHOLDER — hot spring kids

    "Tim: Elias! Hey Elias!"
    "Elias: Yes, Tim?"
    tim   "Come here! The water's fine!"
    tim   "Given the thermal consistency of this geothermal spring and accounting for the elevation, I hypothesize that the temperature today hovers around seventy-eight degrees Celsius-perhaps just under the threshold to soft-boil an egg."
    tim   "We might even be able to cook noodles, Elias. Just imagine-hot spring ramen! Ambient-heated broth, mineral-rich. Quite possibly delicious."
    elias "Soup? We takin bath in soup?!"
    weng  "It's not soup, kids. It's spring water. Full of magic. And minerals. Good for the bones and even better for the soul."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto      "S-S-S-Springs detected. Temperature optimal. Steam density: fluffy."
    elias       "Ooh! It's so pretty! We swim together, Roboto!"
    roboto      "N-N-Negative... I may be waterproof, but my sensors are not human-safe. A power surge could shock the party. I will supervise from a safe distance."
    tedda_alive "Then it's just us! Come, Lady Elias!"
    weng        "Tedda, are you sure you don't want to wear swimwear?"
    tedda_alive "My clothes can't be removed, Miss Weng. I'm a toy, remember?"
    weng        "Oh, silly me. I forgot. Carry on, then."
    tedda_alive "Let's go, Lady Elias! Let's swim like noble queens in our glittery bath!"
    elias       "Yey!! Let's go, Tedda! Tim, let's go!"
    tim         "Hey! I'm a king! I'm not a queen!"

    tim   "So... Miss Weng told me a story once. About this very spring."
    elias "Ooooh. What story?"
    tim   "A tale of the Huli Jing. A legendary fox spirit said to dwell in these waters."
    elias "Hulee Jee?"
    tim   "Huli Jing. A fox spirit who once lived in this spring! Some say she played tricks, others say she gave blessings with kind and compassionate hearts! There was a legend of a game... a test of judgment... but most adults think it's just a myth."
    elias "Ooh! Can we see them?"
    tim   "Only those who are destined to do great things can see them!"
    weng  "Tim, enough of your stories. That's just Tianho folklore. Only the Tetrad Li Mengtia ever claimed to see and speak with one-and that was a thousand years ago."
    weng  "Now hurry up and focus on your baths. We have a ceremony later."
    elias "Miss Weng, what we do later?"
    weng  "We'll watch a special program and release lanterns into the sky, Elias dear."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "Unfortunately, t-t-the lantern releasing is only for adults."
    weng   "But don't worry, little ones. There will be plenty of delicious food afterward."
    roboto "Based on observed preparations from the Hinami delegation, there will also be a d-d-dragon presentation at the memorial grounds."
    tim    "No way! A DRAGON presentation?!"
    roboto "H-H-However, reports indicate the dragon will be a hologram. Please consume this information with a figurative grain of sodium chloride."
    tedda_alive "Wow! Did you hear that, Lady Elias?"
    tim         "And Miss Weng brought crayons for us! We get to color while we wait!"
    elias       "Yay! Color time!"
    tedda_alive "I already have so many ideas for what we can draw, Lady Elias!"

    "-BACK CRACK-"

    weng   "My back... If you'll excuse me, I'll have a cup of calming jasmine tea."
    roboto "M-M-Miss Weng, I highly suggest you don't drink tea while taking a bath in the springs."

    "-Weng and Roboto goes away-"

    elias "Hmm... Daddy told me to always believe in legends."
    tim   "Oh, Mister Dorian? He's so cool! He fought a Hundun in Tianho with Mister Chung, remember?"
    tim   "Oh I forgot. You weren't there. But he was so cool!"
    elias "Daddy's so cool! He's big and strong and wears underpants with dragons on them! He fight big monster!"
    tim   "Hey, Elias... Watch this."

    "-Tim extended his hands. A tiny glowing figure, like a dragon made of mist, forms between his palms, wriggling and coiling like it's alive.-"

    tedda_alive "It's a dragon!"
    tim         "A basic projection, stabilized by willpower and concentration. This one is better!"
    elias       "WOW! How you do dat, Tim? Magic cwayons?"
    tim         "Shhh. Don't tell Miss Weng! It's a secret ability of mine that I can do! You promise?"
    elias       "Um... okay. I promise. You have powers wike Daddy!"
    tim         "I'm... not entirely sure how I got them. They're just... there. That's why I want to ask Mister Chung if-"
    tedda_alive "Wait... something moved over there! The water moved!"
    tim         "Wait... D-Do you see what I'm seeing?"

    huli_jing "..."

    elias "Where? Oh! That's a cute fox! With fow tails!"
    tim   "Four? No! It's nine, Elias! One, two, three, four, five, six, seven, eight... nine! That's a real Huli Jing!"
    elias "It's so cute! Come here little foxie!"

    huli_jing "Hello little ones! What are your names?"

    tim         "My name is Tim! I'm the brains of the group! I'm also the leader!"
    elias       "And I'm Elias! Hewwo!"
    tedda_alive "Kids, are you talking to someone? I don't see anything... Should we tell Miss Weng? What if it's dangerous?"
    weng        "Hey, kids! Who are you talking to?"
    huli_jing "Here's a little gift for you... Goodbye little dumplings..."
    tim         "Wait... where did it go? Aww, it ran away!"
    tedda_alive "Look! Lady Elias! Look at the water! Pretty colors!"
    elias       "Red and yellow and green and pink! It's so pretty!"
    tim         "Chromatic auric distortion. A spontaneous display of spiritual color energy. Fascinating..."
    elias       "Do ya think it's from the fox?"
    tim         "I... don't know. Maybe?"
    tedda_alive "Lady Elias! Look! There's something floating over there-It's a FOX STUFFED TOY!"
    elias       "Oooooh!! Can I have it? Can I have it?!"
    tim         "The Huli Jing said it was a gift. So we should open it! Open it, Elias!"
    tedda_alive "Or!! Maybe you can give it a shake first! Maybe there's magic inside!"

    jump ch9_fox_toy


# =============================================================================
# SECTION 16: LABEL CH9_FOX_TOY — Elias Opens Fox Toy
# =============================================================================

label ch9_fox_toy:

    menu:

        "Shwake it!":

            elias       "Ooh! Okay! I'll shwake it!"
            tedda_alive "With emotion, Lady Elias! Let's goooo!!"
            tim         "Are... you sure shaking it is the best course of action?"
            elias       "Shwake! Shwake!"
            "Men: AHHHHH!!"
            tim         "Huh? What was that?"
            tedda_alive "That must be coming from inside, Lady Elias! Open it!"
            "-POP-"

        "Open it!":

            elias       "Let's open it first, Tedda!"
            tim         "Let's count to three first!"
            tedda_alive "On the count of three open it~ One! Two!"
            "-POP-"

    jump ch9_spring_end


# =============================================================================
# SECTION 17: LABEL CH9_SPRING_END — Untangled / Bathing / Hilltop Prep
# =============================================================================

label ch9_spring_end:

    scene bg_hot_spring with flash              # PLACEHOLDER — hot spring pop

    "I tumbled out."
    "Face-first. Right into someone's thigh."
    "Everything reeked of lavender, steam, and shame. We were all still in our undergarments, soaked, tangled like a bundle of wet spaghetti, sprawled out in the middle of the hot spring."

    chung_hee "This is completely indecent. I swear someone's cheek was on my-wait. Never mind. I don't want to know."
    svante    "I'm... I'm upside down. I can taste someone's foot."
    magnus    "I think my entire spine cracked. Also, someone's sitting on my hair."
    niko      "I apologize. I'll move now."
    elias     "DAAADDDYYY!! Why are you in the foxie?!"

    "Above us, I saw Weng, holding a teacup in her swimwear. She squinted at the mess."

    weng   "By the stars, Master Yuxuan? What happened to all of you?"
    yuxuan "W-We did it, Miss Weng! The spring won't smell like fermented feet stew!"
    weng   "W-What?"
    dorian "J-Just ignore him, Miss Weng."
    yuxuan "It's a long story involving a fox, judges and... moral philosophy."
    elias  "Daddy, you look siwwy! I'll help you."

    "Tiny hands grabbed mine. I looked up to see Elias, dripping and smiling."

    tedda_alive "That looks uncomfortable! I'll help you Lady Elias!"
    weng        "Do you need help? Roboto, hold this teacup."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "T-T-Transferring... hot liquid. Grip calibrated to teacup fragility."
    tim    "That was amazing. I deduce that the fox must've sealed them inside an extradimensional plush construct-"
    chung_hee "Tim. Please. Not now."
    tim    "S-Sorry, Mister Chung! Do you need some help?"

    "One by one, we were untangled-wet, dazed, and half-dressed, but alive. Tedda and Elias offered towels. Roboto beeped encouragingly. Magnus looked like he needed ten massages."
    "I groaned, dragging myself upright. My hair clung to my face. Water trickled down my back."

    roboto "S-S-Spatial anomaly resolved. Group integrity: 100%. Modesty: 4.143%."
    elias  "You okay now, Daddy?"

    "I looked at him and grinned, still catching my breath."

    dorian "Yeah, buddy. I'm okay now."

    "After we finished bathing, I gently scrubbed Elias for a while, until Tedda took over with gleeful determination, humming a tune while she made sure every inch of Elias was squeaky clean."
    "Weng, groaning a little, called out for help with Tim-her back giving out after all the excitement. I didn't know she had lots of back problems."
    "Yuxuan tried to step in, but quickly realized toddler bath time was not his calling. I ended up taking over, gently scrubbing Tim while he lectured me about soap composition."

    tim    "Interesting. I appear to be cleaner than the average imperial scroll... but less organized."
    tim    "This blend lacks proper alkali balance, Mister Dorian. My skin pH will be most offended. Roboto told me that."
    dorian "Tim, I wasn't able to understand half of what you just said. Now, raise your arm."

    "Once we were all dry and dressed, we changed into our Tianho ceremonial attire-layers of silk and charm, embroidered with celestial patterns. Yuxuan, beaming with excitement, led us to the special place he had mentioned."
    "We took an elevator hidden deep inside the library, and when the doors opened, we emerged onto a quiet hilltop."

    jump ch9_hilltop


# =============================================================================
# SECTION 18: LABEL CH9_HILLTOP — Hill / Ceremony / Aoi / Lanterns Setup
# =============================================================================

label ch9_hilltop:

    # [COMMENT: bg_hill_memorial_night — hilltop, indigo sky, Tianho Memorial glowing below]
    scene bg_hill_memorial_night with fade      # PLACEHOLDER — hill overlooking memorial
    stop music fadeout 2.0
    play music ost_ch9_ceremony fadein 2.0      # PLACEHOLDER — ceremony theme
    play audio amb_hilltop_night loop fadein 1.5 # PLACEHOLDER — hilltop night ambient

    "The warm breeze rolled over the hill as we all stood beneath the deepening indigo sky. The last rays of sunlight clung to the clouds like strands of gold silk, while the first stars blinked to life-gentle pearls scattered across a velvet sky."
    "From afar, the Tianho Memorial shimmered in the twilight, glowing faintly."
    "Elias and Tim were already running in small circles around the hill, chasing each other in their ceremonial robes."

    elias "You can't catch me, Professor Tim!"
    tim   "Incorrect, my student. My calculations suggest you have a 32.8% chance of tripping on your hem in the next five seconds."
    elias "Wha-AHH!"

    "Elias' foot caught on the edge of the robe, causing them to tumble onto the floor, giggling uncontrollably."
    "Weng was laying out a neat spread of food on a long silk blanket, adjusting each dish with practiced hands-though every so often, she winced and rubbed her lower back."

    weng "Kids, stop running around like little spirits. You're in ceremonial outfits. You'll tear the fabric and then what?"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "B-b-bento arrangement: c-c-c-complete. Humidity: 47%. Aesthetic symmetry: 93.44%... adjusting for toddler chaos."

    tedda_alive "Ooh! Look how cute these rice cakes are! They look like smiling bunnies!"

    "Yuxuan waved us over from the far side of the hill, dressed in his expensive looking golden ceremonial attire."

    yuxuan "Dorian! Over here, come on!"
    yuxuan "This is the place I wanted all of you to see. A hill above history. The calm before reverence."

    "We all gathered at the rise. The view was breathtaking. The Tianho Memorial stood distant yet dominant, a pale silhouette bathed in the twilight's soft glow."

    yuxuan "I had my people prepare this place for this very special night."

    "Magnus stood quietly to one side, his arms crossed, expression unreadable. He stared out at the fading horizon."

    magnus "It's a beautiful view... The kind that doesn't ask for words. Makes you feel small. But not in a bad way. Small like a star in a sky of stories."
    svante "Hard to believe that yesterday we were fighting right there."
    niko   "It was all just yesterday. A siege, bombs falling like fire. Now we're here."
    chung_hee "Indeed. To think King Gustav sent an entire battalion to destroy what he feared. I did not expect to survive the day. And yet-"
    chung_hee "All of you saved me. Thank you."

    "I scanned the land surrounding the Tianho Memorial. There was no trace of what had happened. No debris, no craters, no bloodstains. Just pristine grass, untouched stone, and soft lanterns beginning to glow in preparation for the evening's rites."

    dorian "They did well. There's not a single trace of the bombs."
    svante "Or my brothers and sisters... I can't believe so many of us died yesterday."
    yuxuan "They called in all the best Earth Channelers from across the Empire. Every stone replaced, every crack healed."
    roboto "For m-m-m-more information, even the Paladins from Gale lent their hands. According to my database, they all w-w-w-worked to make this moment possible."

    "-BACK CRACK-"

    weng        "Tetrad above... Should've called in a back healer too. These knees weren't built for bending this much."
    niko        "Miss Weng, do you want me to grab a chair?"
    weng        "Yes, please. Maybe we could use a table instead of a mat."
    tedda_alive "On it, Miss Weng! Spare table coming in hot!"

    "We all pitched in. Magnus levitated the spare table over with a grunt of wind magic. Svante rolled out fresh cushions."
    "Even Roboto carefully laid out ceramic cups and bundles of incense, his mechanical fingers trembling slightly with effort."
    "The breeze picked up, carrying with it the scent of steamed rice, plum wine, and jasmine. The horizon began to darken into cobalt and violet, and distant bells rang faintly across the hills. Lanterns along the path to the memorial flickered to life one by one."

    yuxuan "It's starting! Everyone, grab a seat."

    "All at once, the soft hum of conversation quieted."

    tim   "Elias, come sit with me!"
    elias "Coming! Daddy, sit with us!"

    "I smiled, lowering myself beside them as Elias eagerly curled into my side, his tiny fingers finding mine. His hair still smelled faintly of lavender from the hot spring. A rare, rare calmness washed over me as I rested my arm around him."

    elias  "Daddy look! Miss Weng gave us cwayons!"
    dorian "That's nice, Elias."

    "Then the lights dimmed."
    "The entire sky above the Tianho Memorial shimmered-and from the center of the clearing, a pulse of blue light burst upward."
    "The hill trembled softly as sound and vision merged. Water began to rise upward in brilliant strands of glowing liquid. The streams coiled and danced, forming an enormous spectral image."
    "A woman stepped into the projection. Her indigo kimono trailed behind her like flowing waves."

    svante "Lady Aoi..."

    "A gasp left my lips."
    "She stood alone in the image, graceful and dignified, as if she were standing on the ocean's surface itself. The holographic sea churned around her feet, and from the depths behind her, a massive, shimmering shape began to rise."

    "( PLAY VIDEO: Dragon of the Depths - ?? )"

    show cg_aoi_performance with dissolve       # PLACEHOLDER — cg_aoi_performance
    pause 3.0
    scene bg_hill_memorial_night with dissolve  # PLACEHOLDER — hill

    "As the last haunting note of the song faded into the wind, silence settled over the hill like a soft shroud."
    "None of us moved for several long seconds-no one dared disturb the weight of what we had just witnessed."
    "I turned, instinctively. Svante, normally so composed, had tears glistening at the corners of his eyes. Niko sat motionless; fists clenched tightly in his lap. Chung-hee stared ahead, jaw set, his expression regal-but his breathing had slowed, as if to anchor himself."
    "Yuxuan looked at me. His gaze met mine-quiet, knowing."
    "Even Elias and Tim were silent, their wide eyes fixed on the heavens above. Weng was busy wiping tears from her eyes."
    "Magnus let out a breath."

    magnus "Amazing. I could give it a go too. A little aria of my own-"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "W-W-Would you like some tea to calm you down, Sir Magnus?"
    magnus "...I suppose that's a no."

    "Then, as the water projection calmed into a mirror-like stillness once more, Lady Aoi reappeared-her image clear, standing tall at the center of the great pool of light."

    aoi "Tonight, beneath these stars and above these honored hills, we gather not as divided nations, but as a shared people-united by memory, by loss, and by hope."
    aoi "We remember the Tragedy of Tianho. A day not written in ink, but seared into our hearts."
    aoi "A thousand lives-fathers, mothers, children, heroes-lost to the fire, to the fear, to the fury. The ground may have healed, but their names live on in us."
    aoi "In every breath we take, in every song we sing, and in every vow we swear."
    aoi "We remember their courage. We honor their sacrifice. And in their memory, we promise: never again."

    aoi "We are graced by the presence of those who lead our world with dignity and strength."
    aoi "His Majesty, King Tatsuya Fujiwara of Hinami, whose wisdom and compassion have lit a path of healing for his people."
    aoi "King Gustav Nordstrom of Mjoll, whose fierce devotion to justice and peace remains unwavering even in times of grief."
    aoi "And Her Radiance, Empress Olympia Wyndham of Gale, who continues to lead with elegance, fortitude, and an unshakable will."
    aoi "To all rulers and leaders present-thank you for your presence, your compassion, and your courage to remember."
    aoi "This ceremony is not just for mourning. It is for resolve. That we-no matter the distance between us-will never forget."

    "The light dimmed once again. We sat in reverence."

    play sound sfx_cheng_jingle                 # PLACEHOLDER — Cheng jingle SFX

    door_voice "And tonight's ceremony has been proudly brought to you by Cheng Industries. Here at Cheng's... we bring change."

    "-Here at Cheng's, we bring change...  -"

    magnus      "Here at Cheng's, we bring change..."
    tedda_alive "Here at Cheng's, we bring change..."
    tim         "Here at Cheng's, we bring change..."
    elias       "*hums off tune*"

    "Yuxuan tried and failed to hide his smile."

    yuxuan "We absolutely smashed the marketing. Me and my friends at the Zhong Lotus Promenade once-"
    niko   "Tsk. Typical."

    "Chung-hee leaned toward me, brows arched."

    chung_hee "Can I ask what the sound was?"
    dorian    "It's a... commercial jingle. For Cheng Industries. Yuxuan's company."

    "Despite the interruption, the ceremony below continued, unbothered by the distant chorus of the people around me."
    "The ceremony continued from afar, the glow of the memorial casting long, gentle light over the gathering below. In the next phase, testimonies were shared-fragments of lives once lived, spoken aloud by their loved ones."
    "Some spoke of a baker who had just opened her first shop, her dreams rising like dough in the early morning sun."
    "Others remembered a teacher who stayed behind to guide frightened children to safety, his final words reassuring."
    "One woman recalled her twin sons, musicians who died with their instruments in hand, playing even as the ground crumbled."
    "We listened in stillness. While the children got bored and carried on coloring. And then came the Lantern Release."

    yuxuan "Miss Weng, the lanterns please!"

    "Weng stood, her hands carrying a lacquered box. She opened it gently and revealed lanterns, folded and decorated in the traditional style of Tianho, each one tied with a crimson ribbon."

    weng "Here it is, Master Yuxuan."

    yuxuan "One for each of us. The Prosperity Dragon will carry our prayers to the ones we've lost."
    weng   "You may write a message. A memory. A prayer. You can draw something if words are hard. Or add a token-something small. Something that meant something to you... or to them."
    niko   "Understood. Thank you."
    svante "Anything, huh..."
    yuxuan "Now. I know we all have someone to remember. Take your time. Go where you need. Be alone if you must. Speak quietly to the ones who can no longer answer."

    "We all nodded."
    "And then-without another word-we slowly began to scatter. Lanterns in hand."

    jump ch9_lantern_kids


# =============================================================================
# SECTION 19: LABEL CH9_LANTERN_KIDS — Elias Launches Lantern
# =============================================================================

label ch9_lantern_kids:

    play music ost_ch9_lanterns fadein 2.0      # PLACEHOLDER — lantern release theme

    "I walked away from the others, lantern in hand, toward a more remote edge of the hill where the moonlight draped the grass like silver thread. I wanted the moment to be quiet. Private. The wind was gentle here, and the stars looked like they were listening."
    "I knelt down beside a smooth stone and studied the blank canvas of the lantern."
    "Elara. Daniel. Emily. Sarah. Lucas."
    "It was only yesterday that I stood at their graves again, after five long years. It still didn't feel real. As if time had stretched and folded itself in strange ways, and grief had learned to hide in the folds."
    "I paused."
    "Would a message be too much? Too little? Would it even reach them?"
    "The pen felt clinical. Cold. It didn't match the weight of what I needed to say."
    "I reached for my satchel, fingers brushing past brushes and ink stones, when I heard it-"
    "There was a rustling behind me."
    "I turned slowly."
    "Behind me, moving in a suspicious little group like a squad of overly curious ducklings, were Elias, Tim, Tedda, and Roboto."

    dorian "What are all of you doing?"

    "Elias immediately perked up like I'd just invited him to a picnic."

    elias       "We want to help, daddy!"
    tim         "Affirmative, sir Dorian! We've elected to supervise your creative process."
    tedda_alive "I brought glitter! And googley eyes!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "O-O-OObservation mode: Active. Sentimental ritual detected. Emotional resonance: 73.3%."
    tim    "Miss Weng hurt her back setting up her lantern and said she's skipping the event. So I took command and assembled the child unit!"
    roboto "M-M-Master Yuxuan said he preferred to be alone. Emotional spike detected. Possible mourning protocol initiated."
    elias       "It's not mourning, Roboto! Siwwy Roboto! It's night time!"
    tedda_alive "I'm with Lady Elias!"

    "I sighed and scooted over."

    dorian "Fine. But be careful. And no glitter."
    elias  "Daddy? No gwitter?"

    "As I launched into a brief explanation of paper textures and ink flow with Tim-who, to his credit, had real thoughts about paper grain-Roboto began calibrating wind speed and \"optimal lantern-lift trajectory.\" Whatever that meant."
    "I didn't notice Elias had quietly dipped a brush into the ink. His tiny hands were already scribbling furiously across the side of my lantern."

    tedda_alive "Oh my! Lady Elias! Is that me?"
    elias       "Yup!! I wrote your name! Look!"

    "Elias, with the confidence of a master scribe, turned the lantern around to show us. In big, messy letters, it read: \"teDuH\""

    dorian "Elias... you're supposed to write names of the dead. Not the living."
    dorian "And also... that's not how you spell Tedda's name."
    tim    "Yeah, Elias! It's Tedda! T-E-D-D-A! Tedda! Not TeDUH!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "L-L-Literacy deviation detected. Spelling accuracy: 37%. Suggest enrolling Elias in supplementary language modules. Possibly... kindergarten."
    elias  "Kinnygarden?"

    "Before I could even confiscate the lantern-WHOOSH."
    "A gust of wind lifted the lantern right out of his tiny hands."
    "We all turned as it wobbled into the air-floating awkwardly, proudly, like a crooked duck with a mission."

    elias       "W-Wait!! Nooo!! I didn't mean to let go yet!"
    tedda_alive "Oh no! My name's flying away!!"
    tim         "Correction: a barely legible approximation of your name is flying away."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "L-Lantern has launched. Contents: ['teDuH']. Probability of proper sentiment delivery: 3.6%. Ascension trajectory: marginally passable."

    "I just... stared up at the sky. Elias reached out and grabbed my hand, his grip small and warm."

    elias  "Sowwy, Daddy. It was pretty though."
    dorian "It was... something. Don't worry, buddy."

    "We watched it vanish into the stars-an accidental, misspelled tribute, lovingly launched by sticky little fingers."

    elias "I love you, daddy."
    dorian "I love you too, Elias."

    weng  "Tim, Elias! I can see the glitter from here!"
    tim   "Hahaha! Retreat! We've been spotted!"
    weng  "Come here! Don't disturb the adults! Let's eat!"
    tedda_alive "Lady Elias, we must go! Miss Weng is summoning us!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "M-M-Miss Weng has entered Critical Hunger Mode. She is demanding all juniors report for dumpling consumption immediately."
    elias  "Dumprings!?"
    weng   "And lots of flan! Come here! I'm getting hungry!"

    "A wide, mischievous grin tugged at her lips. In her hands she cradled a large, round bamboo steamer basket, the wood darkened slightly from years of faithful use. Wisps of fragrant steam curled from beneath the woven lid."
    "With a dramatic flourish, she lifted the lid. Inside, nestled atop glistening green banana leaves, were dozens of plump dumplings. Tianho Xiang Xia Bao. Tianho Fragrant Shrimp Dumplings."
    "Each dumpling gleamed invitingly under the misty steam, their translucent skins slightly stretched over a generous filling of tender shrimp, minced Tianho forest mushrooms, and fragrant herbs."

    weng "There's more where this came from! Come here, kids!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "A-A-A-ALERT: DUMPLING DISPENSATION IN PROGRESS. MOBILIZE. MOBILIZE. L-L-Let's go, everyone!"

    "And just like that, they vanished-sprinting back with a flurry of giggles, robotic beeping, and a suspicious trail of glitter that they absolutely were not supposed to have."

    # Branch on love_route_locked
    if love_route_locked == "yuxuan":
        jump ch9_route_yuxuan
    elif love_route_locked == "chunghee":
        jump ch9_route_chunghee
    elif love_route_locked == "svante":
        jump ch9_route_svante
    elif love_route_locked == "niko":
        jump ch9_route_niko
    else:
        jump ch9_route_magnus


# =============================================================================
# SECTION 20: LABEL CH9_ROUTE_YUXUAN — Yuxuan Lantern Scene
# =============================================================================

label ch9_route_yuxuan:

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
    yuxuan "Ah-hah... yeah, well... I told Roboto that so... I could, uh... scout the area. Alone. For... strategic solitude. Yes."

    "He gave me a sheepish smile, clearly realizing how flimsy his excuse sounded."
    "We both chuckled softly. Without another word, I took the lantern he offered, our fingers brushing for a moment. He lingered in the touch longer than necessary. We didn't mention it."

    "We walked a little farther from the others, away from the gentle laughter of children and the distant sound of flutes playing down at the memorial."
    "The wind was gentler here. A quiet hill beneath the stars, just the two of us. The glow of the memorial in the distance made Yuxuan's silhouette shimmer like something caught in a dream."
    "He sat down slowly on the grass, patting the space beside him. I joined him."

    yuxuan "How have you been feeling... since Elara? Since the kids?"

    "He didn't look at me when he said it. His voice was soft, like he was afraid of pressing too hard."
    "I hesitated, staring out into the dark where Elias's lantern had floated. Somewhere above, it drifted still-misspelled and luminous."

    dorian "I'm... getting there. One day at a time."

    "The words sat in the air for a long moment. He nodded, understanding without needing the details. Then, I glanced at him."
    "He was touching the lantern. I noticed an entire line of names written on the lantern."

    dorian "Those names there. Did you... lose someone important in the tragedy?"

    "Yuxuan didn't respond right away. He traced a finger along the edge of the lantern, watching the way the candlelight flickered through the rice paper."

    yuxuan "Yeah. I did. A lot of someones, actually. Friends. Colleagues. People who... believed in me. Partners who were with me since the beginning. We all had this dream-building something that could help people. That could change lives."
    yuxuan "We met at the Xiangli Centre-back when none of us had money, barely enough to eat. We'd beg vendors for scraps, pool coins for dumplings. I was shocked how many inventors were there. All brilliant. All broke like me. Heh."

    "He paused, his voice thickening. He touched the names written in the lantern."

    yuxuan "They were there when Cheng Industries was just a wild idea on a napkin. We stayed up all night coding and designing and arguing over font choices. We believed in what we were building."
    yuxuan "I remember standing for hours at the Zhong Lotus Promenade, trying to convince passersby that our tech could change lives. And then... when Tianho fell..."
    yuxuan "They didn't make it... But I did."

    "He looked away."

    yuxuan "When you rescued me... I was grateful. So grateful to you. I was over the moon to have survived. But once I heard they didn't..."

    "His voice caught. He rubbed at his neck, eyes glinting with the shine of held-back tears."

    yuxuan "I couldn't breathe. I felt like I'd stolen their air just to keep myself going."
    yuxuan "I told myself I need to finish what we started. And I did. Cheng Industries... it's successful. It's helping people now. I just..."
    yuxuan "I just wish they were here to see it."

    "He gave a soft, shaky laugh and rubbed his neck."

    yuxuan "Sorry. That got heavy. I should've told you all this sooner."

    menu:

        "They'd be proud of you. I know I am.":
            $ yuxuan_affection += 1             # +1 Yuxuan affection

            dorian "No. It's okay. They'd be proud of you. I know I am."
            yuxuan "Thank you, Dorian. I really appreciate it."
            dorian "I'm glad you told me this."

        "Say nothing.":
            pass

    "He turned to look at me then, eyes glinting with something more vulnerable than usual. The breeze tugged gently at his hair."
    "I lowered my gaze to the lantern in our hands."
    "Elara. Daniel. Emily. Sarah. Lucas."
    "I wrote each name with slow, reverent strokes. His hand never left the side of the lantern, steady and warm beside mine."
    "Then... the call came."

    feng   "Honored guests, travelers, friends from every border-"
    yuxuan "Dorian... That man up front. Wait... Is that your best friend? He's-oh. He's the emcee?"
    dorian "I guess he is... That charismatic dog..."
    feng   "Tonight, our lanterns rise not just as tribute, but as light."
    feng   "May they find the ones we lost... and may the stars remember them always."
    feng   "On the count of three-One. Two. Three-Release!"

    "All around us, lanterns lifted."
    "One by one. Then by the dozens. Then by the hundreds."
    "A quiet gasp rippled through the crowd. It was as if the heavens themselves were exhaling."
    "Lanterns floated upward like glowing petals caught in an invisible tide, rising into the night sky. Red, gold, amber. Some danced lazily in the wind, others soared with sharp purpose."
    "Our lantern joined them-gentle, steady, the names glowing softly like a heartbeat. And then-"

    play sound sfx_firework_boom                # PLACEHOLDER — firework boom SFX
    play music ost_ch9_fireworks fadein 0.5     # PLACEHOLDER — fireworks theme

    "BOOM."

    "A firework lit the sky in brilliant pink."
    "Then another-crackling blue, gold, silver stars spinning across the clouds. One exploded into the shape of a dragon, another in the spiral of a flower."
    "It was breathtaking. Silent awe fell across the hilltop as the world above bloomed in light."

    tim   "ELIAS!! ELIAS!! LOOK!! It's amazing!"
    tedda_alive "OH MY GOODNESS! IT'S A FLOWER!"
    elias "A FROWER! A DWAGON!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "V-V-VISUAL SPECTACLE REGISTERED. SENSORY SYSTEMS OVERLOADING-IN A GOOD WAY! INITIATING JOY DANCE PROTOCOL!"

    "Roboto actually spun in a little circle, his mechanical arms lifted like wings, twinkling lights flashing from his chest panel like party lights at a tiny disco."

    dorian "Looks like they're having fun too."

    "I turned to Yuxuan, who hadn't moved. His eyes reflected every flare, every color, as if he were trying to memorize it all."

    yuxuan "Dorian... I... I want to say something"

    "I raised a brow, a smile tugging at my lips."

    yuxuan "But it's embarrassing. So you... um... you have to close your eyes first."

    "I smirked."

    dorian "Is this another Cheng Industries promotional stunt?"
    yuxuan "No! I mean-well, not unless you want a jingle."

    "I closed my eyes, amused."
    "A moment passed. Two. I felt his fingers brush against mine, almost trembling."
    "And then-soft."
    "A quick, fluttering kiss on my cheek."
    "So fast, it might've been imagined. But I felt it. Warm and real."
    "I opened my eyes. He was blushing, absolutely red, looking anywhere but at me."

    dorian "Yu..."
    yuxuan "I... just wanted to say I um... I... have fee-"

    play sound sfx_sparklers                    # PLACEHOLDER — sparklers SFX

    roboto "SPARKLER DISPERSION SYSTEM: ENGAGED!"
    tedda_alive "SPARKLERS!"
    elias "Ahh!! Tim!"
    tim   "I wanna hold two! Roboto!"
    niko  "You can, Tim. But make sure you practice caution. You don't know how many people die because of fireworks."
    magnus "Don't be such a spoilsport, Niko! You're scaring the kids!"

    "Weng appeared from behind a tree, holding her back like she just climbed a mountain."

    weng   "Tetrad save me-someone help me with this sparkler! Svante, could you be a dear and help me?"
    svante "I got you, Miss Weng!"

    "Yuxuan sighed beside me, face still red, voice almost sheepish."

    yuxuan "I guess the moment passed..."

    "I looked at him, smiled, and gently bumped my shoulder into his."

    dorian "Maybe. Or maybe it's just getting started."

    "He glanced at me then, lips parting as if to say something more-but a new firework lit the sky before he could."
    "A massive one-gold and white, shaped like a phoenix, wings spreading wide over the hilltop. We both looked up, quiet again."

    jump ch9_end


# =============================================================================
# SECTION 21: LABEL CH9_ROUTE_CHUNGHEE — Chung-hee Lantern Scene
# =============================================================================

label ch9_route_chunghee:

    chung_hee "Are you alright, Dorian?"

    "I turned around-and there stood Chung-hee, silent as always, holding his lantern with both hands like it was some sacred relic. His brows were slightly furrowed as he watched the crooked, ink-blotted \"teDuH\" lantern bobbing higher and higher into the night sky."
    "I gave him a tired smile, brushing a bit of glitter off my sleeve."

    dorian "Well, Elias just launched a lantern to the heavens with a misspelled tribute to a still-living plush girl."
    dorian "By the way, you never did tell me how you brought her to life."
    chung_hee "It's simple, really. Tedda's an animation of Elias' emotions. I just embedded a living crystal inside her body."
    dorian "A living crystal?"

    "He raised his right hand-the crystallized one. A prismatic gleam passed over the surface as moonlight kissed its edges."

    chung_hee "Standard practice in Kyeongjang."
    dorian    "...You say that like animating plush toys with living crystals is totally normal."

    "He let out a mental chuckle, soft as wind against silk."
    "Then his gaze drifted to his untouched lantern. Pristine. Perfect. Hesitating."

    chung_hee "I was going to ask Tim for help. But he ran off yelling something about dumplings and flan."
    chung_hee "With a mind that sharp, I keep forgetting he's the same age as Elias."

    "He looked back at me, holding out his lantern like it was some cryptic artifact."

    chung_hee "How does it work? Is there a button? Or... does one blow into it?"

    "I had to stifle a laugh."

    dorian    "No blowing required, Chung. It's not a balloon."
    chung_hee "Oh..."

    "I knelt beside him, brushing out the folds gently, pointing to the wax plate."

    dorian "You light this part here. The hot air lifts it up. Like this-"

    "A soft flame danced at my fingertips. As I moved to light it-"

    chung_hee "Wait."

    "He looked down at the lantern again, then up at me. His gaze was gentle. Inviting."

    chung_hee "Share it with me? Since yours... flew off early."

    "I nodded. He looked at me like I was more than a warrior, more than a companion. Like he needed me there."
    "He exhaled-quiet relief flowing from his shoulders as I sat beside him. He took the brush and dipped it slowly into the ink."
    "He didn't speak."
    "His hand trembled slightly as he pressed the bristles against the paper. And then-he paused. His eyes flicked toward the memorial down below. His breath caught."
    "He closed his eyes... and the brush slipped from his fingers. He bowed his head-and sobbed."

    chung_hee "Mom... Dad... I'm so sorry."

    "His body shook with each breathless cry, silent but raw, each tremor echoing louder in my chest than any scream could've."
    "I placed a hand on his back. He didn't pull away."
    "Moments passed. Maybe minutes. The soft rustling of wind, the flicker of firelight, the faint laughter of children far in the distance... and the sound of his crying."
    "Finally, he lifted his head and wiped at his face with the back of his sleeve."

    chung_hee "Forgive me... Such a display is unbecoming of an emperor."
    dorian    "Don't say that."

    "I turned to him."

    dorian "If I may ask, what happened?"

    "He hesitated... then let it out like a dam finally breaking."

    chung_hee "I love my parents with all my heart. But I never wanted the throne. I wanted to be a writer."
    chung_hee "I argued with my parents the day they left. They... wanted me to take the throne. I didn't want to. I said cruel things. Things I never meant."

    "He swallowed."

    chung_hee "I thought I had time to fix things. I thought I'd see them again. But they came to Tianho that day. And I..."

    "His voice faltered."

    chung_hee "I never got to apologize. It was too late."

    "He looked down. I leaned closer. I reached for his hand-his normal one-and held it firmly. He blushed."

    dorian "Then we'll make this one count. For them."

    "He nodded, his fingers curling softly around mine."

    dorian "What about your aunt? You mentioned her yesterday. Is she...?"

    "He lowered his eyes."

    chung_hee "I... suppose I can talk to you about her now. She's alive. She warned me about coming here. About King Gustav."
    chung_hee "She was right..."

    "With slow, reverent strokes, he wrote his parent's names on the lantern's side: Hyon Min-joon. Kim Seo-yeon."
    "I could feel the reverence in his hands-the way each letter was its own goodbye. Then, we rose together. Still holding hands."
    "He lit the base, and the lantern swelled gently, filling with warm air. Our arms brushed. Our eyes met again. Neither of us looked away."
    "Down below, Feng's voice carried across the fields, rich and resonant, echoing through the hush of the gathered crowd."

    feng      "Honored guests, travelers, friends from every border-"
    chung_hee "Paladin Feng. Your best friend. Hm. Let me guess... he's the master of ceremonies tonight, isn't he?"
    dorian    "I guess he is... That charismatic dog..."
    feng      "Tonight, our lanterns rise not just as tribute, but as light."
    feng      "May they find the ones we lost... and may the stars remember them always."
    feng      "On the count of three-One. Two. Three-Release!"

    "We let go together."
    "All around us, lanterns lifted."
    "One by one. Then by the dozens. Then by the hundreds."
    "A quiet gasp rippled through the crowd. It was as if the heavens themselves were exhaling."
    "Lanterns floated upward like glowing petals caught in an invisible tide, rising into the night sky. Red, gold, amber. Some danced lazily in the wind, others soared with sharp purpose."
    "Our lantern joined them-gentle, steady, the names glowing softly like a heartbeat. And then-"

    play sound sfx_firework_boom                # PLACEHOLDER — firework boom SFX
    play music ost_ch9_fireworks fadein 0.5     # PLACEHOLDER — fireworks theme

    "BOOM."

    "A firework lit the sky in brilliant pink."
    "Then another-crackling blue, gold, silver stars spinning across the clouds. One exploded into the shape of a dragon, another in the spiral of a flower."
    "It was breathtaking. Silent awe fell across the hilltop as the world above bloomed in light."

    tim         "ELIAS!! ELIAS!! LOOK!! It's amazing!"
    tedda_alive "OH MY GOODNESS! IT'S A FLOWER!"
    elias       "A FROWER! A DWAGON!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "V-V-VISUAL SPECTACLE REGISTERED. SENSORY SYSTEMS OVERLOADING-IN A GOOD WAY! INITIATING JOY DANCE PROTOCOL!"

    "Roboto actually spun in a little circle, his mechanical arms lifted like wings, twinkling lights flashing from his chest panel like party lights at a tiny disco."

    dorian    "Looks like they're having fun too."
    chung_hee "They sure are."

    "Chung-hee turned toward me, the firelight painting his face with soft, dancing shadows."

    chung_hee "Thank you... for staying with me."

    "I smiled, saying nothing. Just letting the warmth between us linger."
    "He glanced down, realizing our hands were still entwined. His eyes widened slightly. A faint blush crept up his neck, and he quickly-though reluctantly-let go."
    "Then, almost like flipping a switch, he straightened his posture, squared his shoulders, and cleared his throat."

    chung_hee "Ahem. I-apologize. I allowed emotion to... compromise my composure. Clearly, this moment has overwhelmed me."
    chung_hee "Thank you, Dorian."

    "He folded his arms, turning his head as if to reclaim his dignity. But the pink hue still burned on his cheeks."

    play sound sfx_sparklers                    # PLACEHOLDER — sparklers SFX

    roboto      "SPARKLER DISPERSION SYSTEM: ENGAGED!"
    tedda_alive "SPARKLERS!"
    elias       "Ahh!! Tim!"
    tim         "I wanna hold two! Roboto!"
    niko        "You can, Tim. But make sure you practice caution. You don't know how many people die because of fireworks."
    magnus      "Don't be such a spoilsport, Niko! You're scaring the kids!"
    yuxuan      "Niko, you're making it sound like they're juggling hand grenades like that Tian Xun guy."

    "Weng appeared from behind a tree, holding her back like she just climbed a mountain."

    weng   "Tetrad save me-someone help me with this sparkler! Svante, could you be a dear and help me?"
    svante "I got you, Miss Weng!"

    "Laughter and sparks filled the air as the kids darted between glowing trails of light, their joy casting little halos of warmth over the night."
    "Chung-hee and I stood together, quietly watching them."

    chung_hee "Do you think... Never mind..."
    dorian    "Should we join them?"
    chung_hee "Absolutely."

    jump ch9_end


# =============================================================================
# SECTION 22: LABEL CH9_ROUTE_SVANTE — Svante Lantern Scene
# =============================================================================

label ch9_route_svante:

    svante "Is... that your lantern, Dorian?"

    "I turned around, still shaking my head at the trail of glitter Elias left behind, and there he was-Svante."
    "He stood a few steps away, his arms awkwardly half-folded like he'd been trying to decide whether to approach me or not. His eyes drifted up to the sky where \"teDuH\" was still barely visible-wobbling, defiant, and doomed."

    dorian "It was. Emphasis on was. Courtesy of Elias."

    "His lips twitched like he was fighting the urge to stay serious. But then a warm, helpless chuckle escaped him."

    svante "Haha! Really? It had 'Elias was here' energy all over it."

    "He stepped closer, his shoulders still a little tense, like he wasn't sure if he was intruding."

    svante "So... uh, what are you doing now?"
    dorian "Now that my lantern's flying into the cosmos like a glitter-filled disaster? Probably will grab food with Elias. Why? Something wrong?"
    svante "N-No! Nothing's wrong. I just..."
    svante "I just... um... wanted to see how you were doing. Thought maybe... I don't know, you'd want some company."

    "There was something in the way he said it. A little nervous. A little hesitant. But it wasn't pity. It was care. Simple, honest care."
    "He held up the lantern in his hands-a modest one, folded neatly with the ribbon still untied."

    svante "I haven't written anything yet. I wasn't here during the tragedy. I didn't lost anyone in Tianho. But I figured... maybe you'd want to share one with me?"

    "I blinked, caught off guard for a moment. That softness in his voice-it made my chest ache a little. I nodded slowly."

    dorian "I think that's a nice idea."

    "He smiled shyly, scratching the back of his head."

    svante "You can write something, if you want. I... honestly don't know anyone I'd-"

    "He stopped himself, gently handing the lantern to me."
    "I took it in both hands. The paper was cool beneath my fingers, the inkbrush ready beside me. For a long, quiet breath, I just stared at it."
    "Then I spoke, softly."

    dorian "Kristin."
    svante "... Kristin..."

    "His voice caught on the name. His shoulders stiffened, just slightly. I saw the way his jaw clenched, how his breath hitched before he carefully smoothed it out again."

    dorian "I know she didn't die in Tianho. But... it still counts. Doesn't it?"

    "He didn't speak right away. But then he nodded, once. Firm. A bit shaky."

    svante "Yeah. Of course it does."

    "We sat down side by side on the grass, the cool hilltop quiet except for the distant laughter of kids and the soft hum of singing. Probably Magnus."
    "I passed him the ink and brush."
    "He held it in his fingers for a long time-trembling, like he wasn't sure he was ready. But then he looked at me, his mouth pressed into a line."

    svante "I don't think I ever apologized for what happened. Back at Mjoll."

    "I glanced at him. I didn't interrupt."

    svante "W-When Count Vasily came for Elias... and Kristin spoke out..."

    "He swallowed hard. His grip tightened slightly on the brush."

    svante "She was k-killed on the spot. Just for saying it was wrong. And I-"

    "His voice cracked. He stopped, closed his eyes, drew a slow breath."

    svante "I was so angry with you. With Elias. I blamed you both. I wanted someone to hurt as much as I did. And I hated myself for it. Because deep down, I knew..."
    svante "That was the first time I ever questioned my father. King Gustav. I want to know why he did what he did but..."

    "He looked down again, brushing the tip of the inkstick against the rim of the bowl."

    svante "I... I want to say I'm sorry, Dorian. For the resentment. You and Elias."

    "I reached over and gently rested a hand over his. He blushed."

    svante "D-Dorian..."
    dorian "Kristin gave you the courage to start questioning him. You don't have to be sorry for that."
    dorian "And if it wasn't for you, we never could've saved Chung-hee. You stood in the way of your father's plan. You risked everything."
    dorian "That was your sister's courage in you."
    svante "I... can't deny it. I was scared at first. Sir Tian Xun was... scary. Very much so."

    "For a long moment, neither of us said anything. The lantern paper between us was no longer blank. Svante had written her name in clean, careful strokes."
    "Kristin Nordstrom."
    "Below it, he added one more line:"
    "You still guide me."
    "He handed the brush back to me with a small, grateful nod. Together, we lit the lantern."
    "Then... the call came."

    feng   "Honored guests, travelers, friends from every border-"
    svante "That's Sir Feng... He's the one running the ceremonies?"
    dorian "I guess he is... That charismatic dog..."
    feng   "Tonight, our lanterns rise not just as tribute, but as light."
    feng   "May they find the ones we lost... and may the stars remember them always."
    feng   "On the count of three-One. Two. Three-Release!"

    "All around us, lanterns lifted."
    "One by one. Then by the dozens. Then by the hundreds."
    "A quiet gasp rippled through the crowd. It was as if the heavens themselves were exhaling."
    "Lanterns floated upward like glowing petals caught in an invisible tide, rising into the night sky. Red, gold, amber. Some danced lazily in the wind, others soared with sharp purpose."
    "Our lantern joined them-gentle, steady, the names glowing softly like a heartbeat. And then-"

    play sound sfx_firework_boom                # PLACEHOLDER — firework boom SFX
    play music ost_ch9_fireworks fadein 0.5     # PLACEHOLDER — fireworks theme

    "BOOM."

    "A firework lit the sky in brilliant pink."
    "Then another-crackling blue, gold, silver stars spinning across the clouds. One exploded into the shape of a dragon, another in the spiral of a flower."
    "It was breathtaking. Silent awe fell across the hilltop as the world above bloomed in light."

    tim         "ELIAS!! ELIAS!! LOOK!! It's amazing!"
    tedda_alive "OH MY GOODNESS! IT'S A FLOWER!"
    elias       "A FROWER! A DWAGON!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "V-V-VISUAL SPECTACLE REGISTERED. SENSORY SYSTEMS OVERLOADING-IN A GOOD WAY! INITIATING JOY DANCE PROTOCOL!"

    "Roboto actually spun in a little circle, his mechanical arms lifted like wings, twinkling lights flashing from his chest panel like party lights at a tiny disco."

    dorian "Looks like they're having fun too."
    svante "Haha yeah. They're having a lot of fun."

    "Elias was laughing so hard he had to hold onto Tedda, and Tim was pointing frantically at every firework like each one was a miracle."
    "Svante chuckled softly beside me. I turned to him just as another firework lit the sky-this time in shimmering gold, the shape of a phoenix unfurling its wings across the stars."
    "He was looking up, the warm glow flickering in his eyes. His lips were parted slightly, like he wanted to say something. But instead, he just... leaned."
    "Gently. Almost shyly."
    "His head came to rest on my shoulder."
    "I didn't move. Just let him stay there, quiet against me, as the fireworks continued to bloom like celestial flowers overhead."

    svante "I haven't... felt peace like this in a long time."

    "His voice was barely a whisper, like he wasn't even sure if he wanted to say it out loud. But I heard him."

    svante "These past few days... I wish it wouldn't end. I wish it would last."

    "And without thinking, I shifted slightly-just enough to lean my head lightly against his. Our temples touched. The space between us vanished."

    dorian "Then let it stay a little longer."

    "He closed his eyes for a moment, like he was memorizing the feeling. The lanterns above us drifted higher and higher, joining the stars. I could still see ours-Kristin's name glowing gently in the dark."

    play sound sfx_sparklers                    # PLACEHOLDER — sparklers SFX

    roboto      "SPARKLER DISPERSION SYSTEM: ENGAGED!"
    tedda_alive "SPARKLERS!"
    elias       "Ahh!! Tim!"
    tim         "I wanna hold two! Roboto!"
    niko        "You can, Tim. But make sure you practice caution. You don't know how many people die because of fireworks."
    magnus      "Don't be such a spoilsport, Niko! You're scaring the kids!"
    yuxuan      "Niko, you're making it sound like they're juggling hand grenades like that Tian Xun guy."

    "Weng appeared from behind a tree, holding her back like she just climbed a mountain."

    weng        "Finally, my back isn't hurting... Chung-hee, would you like a sparkler?"
    chung_hee   "Hmm... Perhaps I can try using one. For... recreational purposes."

    "Laughter and sparks filled the air as the kids darted between glowing trails of light, their joy casting little halos of warmth over the night. Roboto spun in place again, strobing pink and purple like some overexcited festival lantern."

    roboto "S-S-Safe sparkler mode initiated!"

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

    niko "...I told Miss Weng not to give the kids any brushes. Especially Elias."

    "I turned around-and there he was. Niko. Standing a few steps behind me with his arms crossed and that usual unreadable expression on his face, like the breeze didn't dare ruffle his robes without permission."
    "His eyes tracked the crooked lantern floating in the sky-\"teDuH\" proudly displayed for all the heavens to see."

    niko "I saw the kids beside you and figured your lantern was probably in trouble."

    "He glanced at the fading trail of glitter still lingering in the grass where Elias had bolted off."

    niko "Seems I was right."

    "I let out a low laugh despite myself. There was something comforting about his tone. Not mocking. Just... dry, matter-of-fact, like he wasn't surprised one bit."

    dorian "Heh. You got me."

    "He reached into his only sleeve and pulled out a lantern-immaculate, folded with that eerie precision he always had."

    niko "You can share mine, if you want."

    "I looked at him, eyebrows raised."

    dorian "Are you sure? You're a Prophet. Shouldn't this be between you and... you know. The death god?"
    niko   "This particular festival honors the Prosperity Dragon."
    niko   "I don't worship the Prosperity Dragon. Us Prophets obey Enoch's law word by word. Enoch himself proclaimed that dragons are just are overgrown lizards with complex delusions of grandeur."
    yuxuan "HEY! I HEARD THAT, NIKO!"
    niko   "I'm just doing the lantern release merely so I don't miss out so to speak."

    "He gave me a flat look, as if daring me to challenge him on his theology or his dragon takes. I just shook my head, grinning."

    dorian "Alright, fine. Let's share it."

    "He passed me a brush, the ink already prepared. We didn't speak right away. The night buzzed softly around us-Roboto's automated sounds, children laughing, and the sound of Magnus humming a melody."
    "Then, slowly, Niko pulled out a small container. He opened it carefully, reverently. Tianho flan."
    "And then... a book. Bound in dark leather, worn at the corners."

    dorian "I remember you mentioning that that's Kaito's favorite dessert, right?"

    "He didn't look up immediately. Just kept his eyes on the flan like it might vanish if he blinked."

    dorian "You never told me what happened. Not really."

    "For a moment, I didn't think he would answer. But then:"

    niko "...He died saving people at the tragedy."
    niko "During the Tragedy. There was an inn-Shenzhou. It caught fire. Most people ran. Kaito... ran in."
    niko "There were children. An elderly couple. A dog. Knowing Kaito, he probably went back for all of them."

    "He paused, hands tightening just a little around the book."

    niko "He always did that. Put himself last. I used to yell at him for it. All the time."
    niko "First Law of Enoch: 'To hinder death is to defy Him.' Us Prophets are told never to hinder death. It's not our place. Enoch teaches us-death is the final mercy. The embrace of rest."

    "He stared at the flan, the lantern, the sky."

    niko "But Kaito never followed that. He said... 'If you can hold someone back from that rest, even for a little while, maybe they'll find a reason to keep living.'"
    niko "That's why he wasn't accepted by the Prophets at first. They chose me instead. I obeyed. I understood the doctrine. I followed."
    niko "They only let him in because I bargained. I was receiving visions from Enoch. The others saw that. They knew I was... special and my devotion knew no limits."

    "I sat still, letting the silence stretch between us. The kind of silence that didn't need to be filled."

    dorian "He sounds like someone worth remembering."

    "Niko didn't look at me right away, but his expression softened."
    "Then-deliberately-he pulled out a second spoon from the container and held it toward me."

    niko "He hated sharing. But I think he'd make an exception for you."

    "I took the spoon. We shared the flan in silence, the stars above us and the glow of lanterns painting the world in amber and gold."
    "We weren't even halfway done when a pair of familiar voices piped up behind us."

    elias "Daddy, is that fwan?"
    tim   "We already finished ours. And that one smells superior. May I analyze it-er, I mean, may I have some?"

    "I turned to see them standing there, Elias wide-eyed with excitement and sticky hands, and Tim with his arms folded like a tiny scholar trying to be polite."

    niko "You two already finished your desserts?"
    elias "We're super good at eating dessert!"
    tim  "Yes. Our proficiency is unmatched. We request a second round."
    niko "Under one condition. More vegetables. Got it?"
    tim  "Acceptable terms."

    "They snatched the rest of the flan and ran off, shouting about carrots and cucumbers like they were ancient curses."

    dorian "You know... in a way, I thank Enoch for not taking Elias away from me."
    dorian "There was a time. In Mjoll. Elias was hit by an arrow. Mortally."
    dorian "It was chaos. I thought... I thought he was gone. I went berserk."

    "I looked down, remembering the blood on my hands, the way the blood pooled around Elias. The panic. The helplessness."

    dorian "Yuxuan told me someone stitched him up. No one knew who. But he said if it wasn't for those stitches... Elias would've died that night."
    niko   "...Hmm."

    "Niko didn't answer. He looked down at the book again. Then at the lantern."
    "And slowly, silently, he took the brush and dipped it in ink. Wrote, in clean, solemn strokes:"
    "Kaito Tsukumo. Rest in peace, beloved brother."

    niko "Well. Shall we, Dorian?"

    "I nodded. Together, we lit the lantern. Then... the call came."

    feng   "Honored guests, travelers, friends from every border-"
    niko   "Your best friend. He's the master of ceremonies, I take it."
    dorian "I guess he is... That charismatic dog..."
    feng   "Tonight, our lanterns rise not just as tribute, but as light."
    feng   "May they find the ones we lost... and may the stars remember them always."
    feng   "On the count of three-One. Two. Three-Release!"

    "All around us, lanterns lifted."
    "One by one. Then by the dozens. Then by the hundreds."
    "A quiet gasp rippled through the crowd. It was as if the heavens themselves were exhaling."
    "Lanterns floated upward like glowing petals caught in an invisible tide, rising into the night sky. Red, gold, amber. Some danced lazily in the wind, others soared with sharp purpose."
    "Our lantern joined them-gentle, steady, the names glowing softly like a heartbeat. And then-"

    play sound sfx_firework_boom                # PLACEHOLDER — firework boom SFX
    play music ost_ch9_fireworks fadein 0.5     # PLACEHOLDER — fireworks theme

    "BOOM."

    "A firework lit the sky in brilliant pink."
    "Then another-crackling blue, gold, silver stars spinning across the clouds. One exploded into the shape of a dragon, another in the spiral of a flower."
    "It was breathtaking. Silent awe fell across the hilltop as the world above bloomed in light."

    tim         "ELIAS!! ELIAS!! LOOK!! It's amazing!"
    tedda_alive "OH MY GOODNESS! IT'S A FLOWER!"
    elias       "A FROWER! A DWAGON!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "V-V-VISUAL SPECTACLE REGISTERED. SENSORY SYSTEMS OVERLOADING-IN A GOOD WAY! INITIATING JOY DANCE PROTOCOL!"

    "Roboto actually spun in a little circle, his mechanical arms lifted like wings, twinkling lights flashing from his chest panel like party lights at a tiny disco."

    dorian "Looks like they're having fun too."
    niko   "A lot of fun, actually."

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

    play sound sfx_sparklers                    # PLACEHOLDER — sparklers SFX

    roboto      "SPARKLER DISPERSION SYSTEM: ENGAGED!"
    tedda_alive "SPARKLERS!"
    elias       "Ahh!! Tim!"
    tim         "I wanna hold two! Roboto!"
    niko        "You can, Tim. But make sure you practice caution. You don't know how many people die because of fireworks."
    magnus      "Don't be such a spoilsport, Niko! You're scaring the kids!"
    yuxuan      "Niko, you're making it sound like they're juggling hand grenades like that Tian Xun guy."

    "Weng appeared from behind a tree, holding her back like she just climbed a mountain."

    weng   "Tetrad save me-someone help me with this sparkler! Svante, could you be a dear and help me?"
    svante "I got you, Miss Weng!"

    "Laughter and sparks filled the air as the kids darted between glowing trails of light, their joy casting little halos of warmth over the night. Roboto spun in place again, strobing pink and purple like some overexcited festival lantern."

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

    magnus "What a lovely made piece of artwork!"

    "I turned around, and there he was-Magnus. Standing a few paces away, hands in his ceremonial sleeves, eyes tilted upward toward the sky. His gaze followed the drifting lantern with \"teDuH\" scrawled proudly across its paper like it belonged in a museum of chaotic childhood art."

    magnus "A lone flame sails with crooked grace, a tribute born of sticky haste."
    magnus "The name misspelled; the ink still wet-but love was there. So, no regret."

    "I couldn't help but chuckle."
    "Magnus turned his head slightly, his usual cool expression softening into the faintest grin. He stepped closer, hands behind his back now."

    magnus "I just wanted to see you! Is that alright? I also wanted to ask if you played an instrument."

    "I shook my head a little."

    dorian "Not really. I mean, I've tried-kind of. I'm more of a... listener."
    magnus "Mm... I play the harp. Nothing fancy. Just enough to annoy my tutors when I was a boy... I remember that much, at least."
    magnus "I could play for you sometime. If you'd like."

    "Something about the way he said that made the night feel warmer. Then, after a small pause, he tilted his head toward me."

    magnus "Would you... like to share a lantern with me?"

    "He held one out, delicately folded, the red ribbon trailing from one end like a promise. One lantern."

    dorian "...Yeah. I'd like that, Magnus."

    "We stepped away from the others, just far enough that the noise faded into a soft background hum. The lantern flickered between us as we walked, swaying gently in the breeze."
    "After a while, Magnus spoke again-softly."

    magnus "I still don't remember everything. Not even most things. But... bits remain."
    dorian "Like what?"

    "He thought for a moment, fingers brushing the red ribbon."

    magnus "The taste of Galean persimmons. The sound of wind through temple bells. A song... Many songs... something about stars."
    magnus "But most vividly, I remember... love. I had a woman. Her name was Adriana."

    "I froze. The name hit like a dropped torch in the dark. He mentioned her before when we were fighting but I was too focused on surviving."

    dorian "Adriana? You mean the Adriana? One of the Immortal Tetrad?"
    magnus "Immortal? Hahaha! No, she was mortal. Human. She lived in a village near the coast... or maybe it was on the cliffs. I can't quite see it. But I remember her hands. Her voice."

    "His brow furrowed, eyes narrowing like he was reaching for something just beyond the veil."

    magnus "She was killed. I don't remember the man who did it. A villain with eyes like razors and a soul already given to ash."

    "I didn't know what to say. My heart tightened in my chest, caught between sympathy and something sharper-something I couldn't name yet."
    "But then, Magnus looked at me. And everything shifted."

    magnus "After she died, I began to dream. Not of her. Of... someone else."
    magnus "Of you, Dorian."

    "I stared at him, stunned into silence."

    magnus "I saw you-again and again. Calling out. In firelight, in snow, in the middle of shattered cities I'd never seen before. Calling for me. Begging me to wake up."

    "A cold thrill ran down my spine."

    dorian "No... that can't be right. I'm the one who dreamed of you."

    "The lantern between us flickered."
    "Magnus turned, slowly, fully, to face me."
    "We stood in silence, just for a moment, as the fireworks cracked again above us-silver now, fanning out in spirals like celestial wings."

    dorian "How long were you calling for me?"
    magnus "Long enough for me to believe I might never be found."
    magnus "But I was... by you and our companions. For that, I thank you."

    "I looked down at the lantern between us. We hadn't written anything yet. Without a word, I took up the brush."
    "Elara. Daniel. Sarah. Emily. Lucas."
    "I wrote each name with care, letting the memory settle into every stroke of ink. Magnus stood beside me, watching-not intruding, but present, solid."
    "We lit the lantern together. The flame inside flickered once, then glowed warm and steady. Then... the call came."

    feng   "Honored guests, travelers, friends from every border-"
    feng   "Tonight, our lanterns rise not just as tribute, but as light."
    feng   "May they find the ones we lost... and may the stars remember them always."
    feng   "On the count of three-One. Two. Three-Release!"

    "All around us, lanterns lifted."
    "One by one. Then by the dozens. Then by the hundreds."
    "A quiet gasp rippled through the crowd. It was as if the heavens themselves were exhaling."
    "Lanterns floated upward like glowing petals caught in an invisible tide, rising into the night sky. Red, gold, amber. Some danced lazily in the wind, others soared with sharp purpose."
    "Our lantern joined them-gentle, steady, the names glowing softly like a heartbeat. And then-"

    play sound sfx_firework_boom                # PLACEHOLDER — firework boom SFX
    play music ost_ch9_fireworks fadein 0.5     # PLACEHOLDER — fireworks theme

    "BOOM."

    "A firework lit the sky in brilliant pink."
    "Then another-crackling blue, gold, silver stars spinning across the clouds. One exploded into the shape of a dragon, another in the spiral of a flower."
    "It was breathtaking. Silent awe fell across the hilltop as the world above bloomed in light."

    tim         "ELIAS!! ELIAS!! LOOK!! It's amazing!"
    tedda_alive "OH MY GOODNESS! IT'S A FLOWER!"
    elias       "A FROWER! A DWAGON!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "V-V-VISUAL SPECTACLE REGISTERED. SENSORY SYSTEMS OVERLOADING-IN A GOOD WAY! INITIATING JOY DANCE PROTOCOL!"

    "Roboto actually spun in a little circle, his mechanical arms lifted like wings, twinkling lights flashing from his chest panel like party lights at a tiny disco."

    dorian "Looks like they're having fun too."
    magnus "Oh, how the young ones delight! Come, Dorian-we should join them. At least for a moment."

    "He offered me his hand - an invitation. I accepted it and we danced along with the kids."
    "Magnus lifted his voice in song-soft and smooth, a melody that felt older than the stars overhead. His voice wrapped around me like silk, and without thinking, I joined in."

    magnus "O stars that sail the velvet night, O winds that carry dreams in flight..."
    dorian "...If I must drift, let it be near, the one who makes the dark feel clear."

    "And then-"
    "BAM."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    roboto "U-U-U-UNINTENTIONAL TRAJECTORY DETECTED-IMPACT IMMINENT!"
    tedda_alive "Oh my! I'm so sorry!"

    "There was a blur of motion-a flailing arm and suddenly I tripped. Magnus tried to catch me, but his foot caught the edge of his robe, and we both went tumbling back."
    "I landed right on top of him."
    "The world went quiet for a moment-just the thud of hearts, the echo of laughter, the flicker of firelight dancing across Magnus' cheeks."
    "I stared down at him, and he stared up at me."
    "One of my hands was braced on his chest, the other still holding a piece of my robe from the fall. His hands had instinctively found my waist."

    magnus "You... have a beautiful voice."
    dorian "You too, Magnus. Sorry for landing on top of you."
    magnus "That may have been the highlight of my evening."

    "We didn't move. We could have. But neither of us wanted to."

    play sound sfx_sparklers                    # PLACEHOLDER — sparklers SFX

    roboto      "SPARKLER DISPERSION SYSTEM: ENGAGED!"
    tedda_alive "SPARKLERS!"
    elias       "Ahh!! Tim!"
    tim         "I wanna hold two! Roboto!"
    niko        "You can, Tim. But make sure you practice caution. You don't know how many people die because of fireworks."
    magnus      "Don't be such a spoilsport, Niko! You're scaring the kids!"
    yuxuan      "Niko, you're making it sound like they're juggling hand grenades like that Tian Xun guy."

    "Weng appeared from behind a tree, holding her back like she just climbed a mountain."

    weng   "Tetrad save me-someone help me with this sparkler! Svante, could you be a dear and help me?"
    svante "I got you, Miss Weng!"

    "Laughter and sparks filled the air as the kids darted between glowing trails of light, their joy casting little halos of warmth over the night. Roboto spun in place again, strobing pink and purple like some overexcited festival lantern."

    roboto "S-S-Safe sparkler mode initiated!"

    "We both burst into laughter as I finally rolled off Magnus-but not far. Just enough to still feel the warmth of him beside me, our arms brushing as we watched the sky blossom in fire."

    magnus "We'll finish that dance later."
    dorian "It's a promise."

    jump ch9_end


# =============================================================================
# SECTION 25: LABEL CH9_END — Common Ending / Sparklers / Going Home
# =============================================================================

label ch9_end:

    "The hilltop was glowing now, cast in soft hues of flame and magic. Lanterns floated steadily upward, their light flickering like heartbeat echoes. Sparklers twirled in tiny hands."
    "One by one, the firecrackers gave way to silence. The celebration slowly dissolved into the hush of night."
    "We returned to the lab in quiet procession. My steps felt heavier, but not from exhaustion-from the weight of everything I'd seen, heard, and felt."
    "I changed, climbed into bed, and let myself collapse into the softness. My heart was full. Maybe too full."

    scene cg_black with fade                    # PLACEHOLDER — fade to black
    stop music fadeout 3.0
    stop audio fadeout 2.0

    pause 2.0

    jump chapter_10


# =============================================================================
# END OF CHAPTER 9 PART 2
# =============================================================================
