###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  FILE:  chapter_09_p1.rpy
#  SCENE: CHAPTER 9 PART 1 — Morning to Pre-Hot Spring
#
#  CONTENTS:
#    Section 1  — Character Definitions (NEW for Chapter 9)
#    Section 2  — Image Declarations
#    Section 3  — Audio Declarations
#    Section 4  — Game Variables
#    Section 5  — label chapter_9            (Lab Bedroom — morning wake)
#    Section 6  — label ch9_elias_choice     (Choice: Stay with Elias or check Magnus)
#    Section 7  — label ch9_common           (Common — lab hallway / kitchen)
#    Section 8  — label ch9_lab_choices      (Lab living room — four activity choices)
#    Section 9  — label ch9_library          (Library — Chung-hee reading / Chung choices)
#    Section 10 — label ch9_library_common   (Library CommonCommon — poem / Weng visit)
#    Section 11 — label ch9_bedroom_yuxuan   (Bedroom — Yuxuan visit / snacks)
#    Section 12 — label ch9_tavern           (Tianho tavern — Niko / Aoi encounter)
#    Section 13 — label ch9_kitchen_help     (Kitchen — help with cooking / Magnus/Svante)
#    Section 14 — label ch9_kitchen_common   (Kitchen CommonCommon — after cooking)
#    Section 15 — label ch9_outfit_gather    (Lab — everyone gathers for outfits)
#    Section 16 — label ch9_pre_hotspring    (End of Part 1 — Roboto leads to hot spring)
#
#  NAMING CONVENTIONS:
#    image tags      — bg_name, cg_name, character_name emotion
#    audio variables — audio.ost_name, audio.sfx_name, audio.amb_name
#    label names     — ch9_name (all lowercase, underscores only)
#    game variables  — yuxuan_affection, niko_affection, etc.
#    NO SPACES in any tag, label, variable, or image name.
#
#  POV NOTE:
#    All sections are Dorian's POV.
#
#  TRACKER SUMMARY:
#    chunghee_affection : +1 library (let him be) / -1 press further
#    yuxuan_affection   : +1 bedroom choice 1 (eat with Yuxuan)
#    niko_affection     : +1 eat with Niko
#    svante_affection   : +1 ask about woman in photo
#    magnus_affection   : +1 join singing / +1 story yes
#
#  PLACEHOLDER PATHS:
#    Search "# PLACEHOLDER" to find every line that needs a real asset.
###############################################################################


# =============================================================================
# SECTION 1: CHARACTER DEFINITIONS (NEW FOR CHAPTER 9)
# =============================================================================

# define huli_jing   = Character("Huli Jing",    color="#f0c040")  # Amber gold — nine-tailed fox spirit
# define fynn        = Character("Fynn",          color="#cd5c5c")  # Muted red — the zealot, Mjoll
# define katashi     = Character("Katashi",       color="#8b7355")  # Earth brown — the fisherman, Hinami
# define emi         = Character("Emi",           color="#f9a8d4")  # Soft pink — Katashi's daughter
# define seorin      = Character("Seorin",        color="#a8d8ea")  # Pale blue — the alchemist, Kyeongjang
# define feng        = Character("Paladin Feng",  color="#ff8c00")  # Orange — Dorian's best friend, emcee
# define soldier_gao = Character("Soldier Gao",   color="#a0a0a0")  # Grey — Dorian's old soldier

# Characters in use this chapter (already defined in earlier chapters):
# dorian, elias, magnus, yuxuan, niko, svante, chung_hee, weng, tim, tedda_alive, roboto
# door_voice, vendor, man_1, man_2, woman_1, woman_2, aoi, prosperity_dragon, elara


# =============================================================================
# SECTION 2: IMAGE DECLARATIONS
# =============================================================================

image bg_tianho_food_stalls_day  = "images/backgrounds/bg_tianho_food_stalls_day.png"      # PLACEHOLDER
# Tianho food stall row — daytime, colorful vendor carts, festival crowds

image bg_library                 = "images/backgrounds/bg_library.png"                     # PLACEHOLDER
# Yuxuan's vast underground library — mahogany shelves, floating lanterns, giant hourglass

image bg_tianho_post_tragedy_day = "images/backgrounds/bg_tianho_post_tragedy_day.png"     # PLACEHOLDER
# Tianho streets — daytime, anniversary festival crowds, vendor stalls


# =============================================================================
# SECTION 3: AUDIO DECLARATIONS
# =============================================================================

define audio.ost_ch9_morning     = "audio/music/ost_ch9_morning.ogg"        # PLACEHOLDER
# Gentle, warm — morning wake-up in the lab bedroom

define audio.ost_ch9_kitchen     = "audio/music/ost_ch9_kitchen.ogg"        # PLACEHOLDER
# Lively, homey — kitchen prep with Magnus and Svante

define audio.ost_ch9_library     = "audio/music/ost_ch9_library.ogg"        # PLACEHOLDER
# Quiet, contemplative — Yuxuan's library atmosphere

define audio.ost_ch9_tavern      = "audio/music/ost_ch9_tavern.ogg"         # PLACEHOLDER
# Tianho street festival atmosphere — distant drums, flutes

define audio.sfx_cheng_jingle    = "audio/sfx/sfx_cheng_jingle.ogg"        # PLACEHOLDER

define audio.amb_tianho_festival = "audio/ambient/amb_tianho_festival.ogg"  # PLACEHOLDER
define audio.amb_library         = "audio/ambient/amb_library.ogg"          # PLACEHOLDER


# =============================================================================
# SECTION 4: GAME VARIABLES
# =============================================================================

# default ch9_elias_choice   = ""      # "stay" or "rush"
# default ch9_lab_choice     = ""      # "library" "bedroom" "tavern" or "kitchen"
# default ch9_chung_pressed  = False
# default ch9_yuxuan_ate     = False
# default ch9_niko_ate       = False
# default ch9_svante_photo   = False
# default ch9_magnus_song    = False
# default ch9_story_promised = False


# =============================================================================
# SECTION 5: LABEL CHAPTER_9 — Lab Bedroom Morning Wake
# =============================================================================

label chapter_9:

    # [COMMENT: bg_lab_bedroom — warm spare room, Elias on bed with chocolate]
    scene bg_lab_bedroom with fade              # PLACEHOLDER — lab bedroom
    play music ost_ch9_morning fadein 2.0       # PLACEHOLDER — gentle morning theme

    show screen chapter_title_screen(
        "9",
        "The Fifth Anniversary",
        subtitle="Tianho — The Underground Lab",
        duration=3.0
    )
    pause 3.0

    "I woke to the softest, most comforting scent. The warm aroma of freshly laundered sheets mixed with something faintly sweet-like the lingering traces of vanilla and sun-dried cotton."
    "The fabric cradled me in its gentle embrace, and for a moment, I considered sinking deeper into its warmth. But then, the sound of soft munching reached my ears."
    "I blinked my eyes open, taking in the dim light of the fixtures."

    "Beside me, Elias sat cross-legged on the bed, happily chewing on a Hinami chocolate bar. His tiny hands were smudged with bits of melted chocolate, and his bright eyes lit up the moment he saw me stir."

    elias "Daddy! You're awake!"

    "Before I could even process what was happening, he launched himself at me, wrapping his little arms around my torso. I let out a breathless chuckle, ruffling his soft hair as he clung to me. He was warm, his small body buzzing with energy."

    dorian "Elias, you have chocolate all over your hands. And I told you to not eat on the bed."

    "He pulled back, grinning sheepishly. With a tiny huff, he hopped off the mattress and settled onto a chair beside the bed, still clutching his half-eaten chocolate bar like it was the most precious thing in the world."

    dorian "Have you eaten breakfast yet?"
    elias  "Yes, daddy! I'm eating my late lunch now."

    "Late lunch? So it was already afternoon? I had overslept."
    "I looked down at his hands, still clutching the half-eaten chocolate bar. Late lunch?"

    dorian "Elias, how many times have I told you? Eat your vegetables."

    "Elias immediately scrunched up his nose, his face contorting into the most dramatic expression of disgust."

    elias "I did, daddy! Miss Weng made me eat! Yucky veggies! Ew!"

    "I sighed, massaging my temples. Miss Weng was a miracle worker; I had to give her that. Getting Elias to eat vegetables was no small feat."
    "Come to think of it, everything's happening so fast."
    "In just a single day, I met Chung-hee, the Emperor of Kyeongjang; Niko, a prophet of the death god; and Svante, an aldorith who had switched sides. I had met Miss Weng, Yuxuan's trusted helper, Roboto, Yuxuan's automaton, and Tim, the brilliant toddler who somehow always knew more than he should."
    "I had reconnected with Paladin Feng, an old friend from my past, and met with Lady Aoi, the mercenary who had been trying to kill Chung-hee."
    "And we met and fought Magnus. The man from my dreams. What happened to him? Why had he been sealed in ice for centuries? And what memories had been implanted into his mind, twisting him into something even he didn't recognize?"
    "I barely had time to process any of it before Elias' small hand slipped into mine. I looked down at him."

    elias  "Me an' Tim gonna play later after my nap, Daddy! You wanna play too?"
    dorian "Sorry buddy. Daddy's busy."

    "Elias pouted and took another bite of the chocolate. After a few bites, he set down the chocolate and yawned."

    elias "Mmm... I'm real, real sleepy, Daddy. Can you pat my back so I can... um... nap better?"

    "He swayed a little in his seat, blinking drowsily, fighting sleep the way all kids his age did. I knew from experience that Elias never fell asleep quickly. If I helped him, maybe he'd drift off sooner."
    "But at the same time, I haven't checked up on Magnus yet. Who knew what was happening in his mind? If he woke up confused-or worse, hostile again-he could be a danger to everyone."
    "Elias wiped his hands on a paper towel until they were clean and jumped to the bed next to me."

    elias "Daddy... can you pat my back?"

    jump ch9_elias_choice


# =============================================================================
# SECTION 6: LABEL CH9_ELIAS_CHOICE
# =============================================================================

label ch9_elias_choice:

    menu:

        "Stay with Elias and help him sleep.":
            $ ch9_elias_choice = "stay"
            $ magnus_affection += 1             # +1 Magnus affection

            "I sighed, glancing at the reinforced door before finally relenting. Magnus could wait."
            "I shifted onto the bed beside Elias, resting on my side as he curled up next to me, his warmth pressing into my chest."
            "As I began to pat his back, his body relaxed, melting into me with a soft, contented sigh."

            elias "Miss Weng told me I hafta eat veggies, Daddy... but I dun' wanna."

            "I let out a quiet chuckle, my hand continuing its steady rhythm against his back."

            dorian "Miss Weng is right. You need to be healthy. When you grow old, you'll... get diseases. It's awful, trust me. You need those veggies."
            elias  "Blegh... but Tim says if you eat too many veggies you turn into a broccoli. Ew!"

            "I huffed out a small laugh, shaking my head."

            dorian "I doubt someone as smart as Tim would say anything like that, Elias."
            elias  "Roboto says it's gonna do something exciting later! Tedda told me so! An' Yuxuan was talkin' to someone real loud today, but I dunno who!"
            dorian "Yuxuan? Maybe it's someone important."
            elias  "Tedda said it's the iven owganizwer! I don't know what that means!"

            "I processed his words for a moment. Did he mean event organizer?"
            "For what?"
            "I stowed it away in my mind as something to check on later, still patting his back."
            "Elias let out another tiny yawn, his body going even softer against mine. Then, without warning, he nuzzled closer, his small fingers clutching my sleeve with just enough pressure to make my chest tighten."

            elias "Daddy... I hope you had fun when you visited your family at the grave..."

            "My breath caught."
            "I remembered. I visited their graves just yesterday with Yuxuan and Elias. Names carved in stone. Voices long gone, yet still whispering in the back of my mind. I inhaled sharply, my grip on Elias instinctively tightening."
            "Elara. Daniel. Sarah. Emily. Lucas."
            "I hope you're all doing alright in Xianlun."

            dorian "It was... enlightening. I wouldn't call it fun, Elias. But I hope you had fun eating all those chocolate at the memorial."

            "His only response was a sleepy hum, his fingers slowly loosening from my sleeve."

            elias  "I love you, Daddy."
            dorian "Love you too, Elias. Now, go to sleep."

            "Minutes passed. Five. Ten. Twenty? I lost count as I continued to pat his back, staring at his peaceful face, watching his eyelashes flutter ever so slightly."
            "The dim, flickering lights overhead cast long shadows across the sterile walls, their hum the only sound accompanying the rhythmic rise and fall of Elias' tiny chest."
            "His breathing evened out. His tiny body, pressed against me, sank deeper into sleep. I stayed until I could peel myself away, tuck the blankets around him as I left."

        "Rush to check on Magnus.":
            $ ch9_elias_choice = "rush"

            "I hesitated only for a moment before rising from the bed."

            dorian "Sorry buddy. I need to get this done immediately. Get some rest. I'll be back later."

            "Elias yawned but didn't argue."

            elias "Okay, daddy. I'll just pretend this piyow is you."

            "He hugged a tight pillow around him."
            "I stepped out of the room."

    jump ch9_common


# =============================================================================
# SECTION 7: LABEL CH9_COMMON — Lab Hallway / Kitchen
# =============================================================================

label ch9_common:

    # [COMMENT: bg_yuxuan_lab — lab hallway, savory scent drifting]
    scene bg_yuxuan_lab with dissolve           # PLACEHOLDER — lab main area

    "As soon as I stepped into the hallway, a wave of rich, savory aromas enveloped me. The air was thick with the scent of sizzling garlic, ginger, and scallions dancing in hot oil."
    "My stomach rumbled."

    # [COMMENT: bg_kitchen — kitchen, Magnus chopping, Weng watching Svante]
    scene bg_kitchen with dissolve              # PLACEHOLDER — kitchen
    play music ost_ch9_kitchen fadein 2.0       # PLACEHOLDER — lively kitchen theme

    "Drawn by curiosity, I followed the scent down the corridor, the rhythmic clatter of knives against wooden boards guiding me toward the kitchen. When I stepped inside, I stopped in my tracks."
    "There, hunched over the chopping board, was Magnus. Magnus?"
    "For a moment, my brain struggled to reconcile what I was seeing. Yesterday, he was a vengeful force of divine fury, light exploding from his body like an avenging god. But now?"
    "Now, he was cutting vegetables. Enthusiastically."
    "And still shirtless, his wings shifting slightly as he worked. I blinked. Had I hit my head?"
    "Weng stood at the counter, hands on her hips, watching over Svante, who was fumbling with a knife and a rather unfortunate daikon radish."

    weng "No, no! Not like that, Svante! Watch me."

    "She took the daikon from his hands and, with precise, elegant movements, she pressed the blade against the radish's smooth surface. With a flick of her wrist, she glided through the vegetable with effortless grace, each slice falling into uniform half-moons. Thin, translucent, perfect."

    svante "Oh... got it, Miss Weng! Thank you for teaching me!"

    "And then there was Magnus."
    "He wasn't just chopping vegetables-he was conducting a symphony. Every stroke of his knife was a masterful flourish. His brown hair shimmered under the kitchen lights, swaying with every precise movement as he diced, sliced, and minced."

    magnus "The essence of life is within the humble vegetable. See how it bends to the will of the blade, how it surrenders yet does not break!"

    "With a flick of his wrist, a daikon radish twirled elegantly into crescent moons, scattering across the cutting board like fallen petals."

    magnus "Behold, the radish-a pearl of the earth, carved by fate's hand into fragile crescents! Each slice, a whisper of nature's delicate song!"

    "Svante looked at him as if he had grown a second head."

    svante "Uh... Sir Magnus, would you mind cutting the daikon for me? I think I'll just stick to tomatoes."
    magnus "Ah! Fear not, dear Svante! While you engage in divine companionship with the tomatoes, the daikon and I shall embark upon a journey most divine!"
    svante "Y-Yes! Thank you, sir Magnus!"

    "I took a cautious step forward."

    dorian "...Magnus?"

    "He spun toward me with such bubbly energy that I instinctively tensed, half-expecting an attack. But instead, his eyes sparkled with pure joy."

    magnus "Ah! Dorian! At last, you awaken! You have entered the hallowed temple of culinary enlightenment! Have you come to witness the transcendence of mortal ingredients?!"

    "He held up a single radish slice between his fingers, as if he had just plucked the moon from the heavens. Weng turned toward me, her brow furrowing."

    weng "Sir Dorian, are you alright? Goodness, you must still be exhausted from yesterday."
    weng "You're always welcome to sleep some more, sir. I can leave some food-"

    "I wasn't sure how to answer that. Was I alright? After everything that had happened yesterday? After waking up to a completely different Magnus-bubbly, shirtless, and eagerly chopping vegetables while delivering poetic monologues about radishes?"

    dorian "I'm perfectly fine, Miss Weng. Thanks."

    "I glanced at Svante, who was grinning at my bewilderment."

    svante "Sir Dorian, turns out Magnus is actually a nice guy! When he saw I volunteered to help with the vegetables, he wanted to join in too!"
    svante "You should've seen him! Did I mention he's great at poetry as well? He was so excited about chopping vegetables, he started reciting poetry about them."

    "My eyes flickered back to Magnus. He was still cutting daikons by the numbers, his brown hair falling slightly over his face as he worked."
    "Magnus noticed my stare and flashed me a small, contented smile."

    magnus "Cooking is an art, Dorian. One must respect the ingredients. Handle them with care, as one would a delicate soul."

    "This was the same man who, less than a day ago, had sworn to rip me apart with divine fury. I ran a hand down my face, my gaze wandering absently around the kitchen."
    "That's when I noticed it. The sheer amount of food."
    "Sacks upon sacks of garlic and onions were piled near the counters, their papery skins rustling faintly in the warm air."
    "A tower of neatly stacked meat-fish, chicken, beef-rested by the sink, waiting to be prepared. Bowls of freshly washed vegetables lined the tables, their colors vibrant under the lantern light."
    "I blinked. When did all of this get here? The sheer abundance of supplies looked as if a small army was preparing for a feast."
    "Just as I was about to ask, the door swung open."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    "Tedda and Roboto entered, lugging even more sacks of food, their arms full of supplies. Tedda, struggling under the weight, huffed as she set her load down with a loud thump. Roboto placed its sacks down neatly before dusting off his metallic hands."

    tedda_alive "Ta-daaaa!! One more sack of tomatoes for chopping!"
    svante      "Here, Tedda. I'll help you, hold on-"
    tedda_alive "Aww, Mister Svante! Thank you! You're such a handsome gentleman teehee~"
    roboto      "M-M-Miss Tedda, may I remind you that you are a child's stuffed toy?"
    tedda_alive "Woops! Sorry!"

    "Roboto glitched slightly before turning towards Weng."

    roboto "M-M-Miss Weng. Here is the last sack of Hinami c-c-c-crabs."

    "Weng, elbows deep in washing a bundle of greens, nodded without looking up."

    weng        "Thank you, Roboto and Tedda. I'll handle the rest. I'll call for you if I need anything else."
    roboto      "No problem, Miss Weng. Y-Y-You can always count on Robotoooo~"

    "Its glowing eyes flickered as he turned toward me."

    roboto      "Oh Master D-D-D-Dorian! You're awake!"
    tedda_alive "Ooh Mister Dorian is awake! Hello Mister Dorian! Is Lady Elias sleeping now?"
    dorian      "Yes, he is."
    tedda_alive "Perfect! That means Mister Roboto and I can help with chopping vegetables!"
    weng        "That's always welcome, dear. The more hands, the better."

    "Magnus, completely unbothered, glanced at Weng."

    magnus "How many more daikon do we need?"

    "Weng, busy washing a bundle of greens, responded without looking up."

    weng   "We still need one sack more, Sir Magnus."
    dorian "...What is all of this for, Miss Weng?"
    weng   "Today is the Fifth Anniversary of the Tragedy of Tianho, sir Dorian. Aside from our group, I'll be cooking for the employees and their families as well."
    weng   "Far be it from Master Yuxuan to let his staff, Gao, Jiang, and their families, observe the day without delicious food on the table."

    "The words struck me like a fist to the chest. My breath hitched. That's right."
    "How could I have forgotten?"

    "Weng wiped her hands on a towel, her voice calm yet thoughtful."

    weng "Master Yuxuan left earlier to meet with the representatives from the Hinami Kingdom. Hinami will be hosting today's program."

    "That made sense. Hinami was always the first to extend a hand in times of remembrance."

    dorian "I'm not surprised. Their customs place great value on honoring the dead-especially their burial rites."

    "Svante leaned forward slightly, holding a tomato, curiosity flickering in his violet eyes."

    svante "What kind of customs, sir? Sorry, I'm not too familiar with Hinami's traditions. Father forbade us from stepping outside of Mjoll."
    magnus "I must admit, I too am unfamiliar. Can you enlighten us, Dorian?"
    dorian "For starters, they sink their dead to the bottom of the ocean. To them, the ocean isn't just a body of water-it's an eternal resting place, where souls drift into the embrace of the Dragon of the Depths."
    svante "...Wait. They just-sink them?"
    weng   "Indeed. I've read many accounts of their reverence for the Dragon of the Depths."
    weng   "They believe the sea carries their ancestors' spirits, guiding them to where they belong. It's a deeply sacred ritual."

    "Magnus paused, turning to face me with a contemplative frown."

    magnus "But if the dead are scattered across the ocean, how do the living visit their loved ones? Graves, shrines-these are markers, places of remembrance."
    magnus "How does one pay respects when the resting place is... endless?"
    weng   "That's a good point. Do they have any traditions to compensate for that?"
    dorian "Honestly? I don't know."
    roboto "The e-e-e-entire ocean. Whenever they s-s-s-see the ocean, they remember them. Their memory is not confined to a single place."
    svante "Really? That's amazing."

    tedda_alive "Leave it to Mister Roboto to give a quick answer!!"

    "Roboto blinked, its glowing eyes whirring slightly."

    roboto "Y-Y-Y-You can always count on Robotooooo, sir Svanteee~~"

    "Magnus, intrigued, tapped a finger against his chin."

    magnus "A profound perspective. To be remembered not by stone, but by the endless tides. Hm..."
    svante "Have you ever been to Hinami, sir Dorian?"

    "I shook my head."

    dorian "No. Hinami's an island. And as you can imagine, fire and water don't exactly mix. Besides, it's a long boat ride from here."

    "Svante chuckled."

    svante "Yeah, sir Dorian, I can see how that'd be a problem."

    "Magnus, still deep in thought, finally returned to his daikon slicing."
    "Weng picked up another bundle of greens, smiling softly. She chopped them into thin slices within seconds."

    weng "By the way, Sir Niko left early this morning. He went to Tianho to meet with his fellow prophets of the Death God."

    tedda_alive "Oh! I saw him at the tavern in Tianho while Mister Roboto and I were picking up the sacks of food!"

    "I frowned, scanning the room and noticing for the first time that someone else was missing."

    dorian "What about Chung-hee? Have you seen him?"
    roboto "I s-saw Sir Chung-hee at Master Yuxuan's library before he left for Tianho with M-M-Miss Tedda."
    roboto "He was intent on reading and I d-didn't want to disturb him."

    "I glanced at Tedda, who nodded in confirmation. So both Niko and Chung-hee were in Tianho. That didn't sit right with me."

    tedda_alive "Mister Chung-hee looked serious! Too serious oh my!"

    "Weng clapped her hands together, the sharp sound cutting through the chatter like a knife through soft dough."

    weng "Alright, everyone. Enough chit-chat. We need to start frying the fish."
    weng "Things are about to get very busy in here. We have many mouths to feed later, so let's stay focused."
    svante "Yes, Miss Weng!"
    magnus "Ah! The noble sizzle of flesh meeting flame! The symphony of heat and oil, of golden crisp and fragrant spice!"
    magnus "A humble fish, once a dweller of the deep, now ascends to its final form-a feast for the weary, a balm for the soul!"

    "Svante shot him a side glance, suppressing a laugh."

    svante "Pft- Hahahaha!"
    magnus "W-Why are you laughing?!"

    "I, on the other hand, found my gaze drifting to the overwhelming amount of food stacked up around the kitchen. Sacks of garlic and onions rustled softly where they were piled high. Slabs of freshly butchered meat lay in careful rows."
    "The sheer volume of it all made my stomach tighten. I wondered. How many people were they going to feed?"

    # [COMMENT: bg_yuxuan_lab — living room, Roboto follows Dorian out]
    scene bg_yuxuan_lab with dissolve           # PLACEHOLDER — lab living room

    "I decided not to linger and get in their way. Stepping out of the kitchen, I made my way toward the living room, lost in my own thoughts."
    "But just as I settled onto a chair, Roboto followed me, his servos whirring softly."

    roboto "Master Dorian, all of us will be busy for the time being. There's p-p-plenty to do. You can h-help, rest, or d-do whatever you like."
    dorian "Thanks, Roboto."
    roboto "No worries, master Dorian! You can always count on R-R-Robotooo~"

    "With that, Roboto whirred back towards the kitchen."
    "I exhaled, running a hand through my hair. Whatever I liked, huh?"

    jump ch9_lab_choices


# =============================================================================
# SECTION 8: LABEL CH9_LAB_CHOICES — Four Activity Choices
# =============================================================================

label ch9_lab_choices:

    menu:

        "Spend time at Yuxuan's library.":
            $ ch9_lab_choice = "library"
            $ chunghee_affection += 1           # +1 Chung-hee affection
            jump ch9_library

        "Go back to the bedroom and check on Elias.":
            $ ch9_lab_choice = "bedroom"
            $ yuxuan_affection += 1             # +1 Yuxuan affection
            jump ch9_bedroom_yuxuan

        "Have a drink at Tianho's tavern.":
            $ ch9_lab_choice = "tavern"
            jump ch9_tavern

        "Help with the kitchen.":
            $ ch9_lab_choice = "kitchen"
            jump ch9_kitchen_help


# =============================================================================
# SECTION 9: LABEL CH9_LIBRARY — Chung-hee Reading / Chung Choices
# =============================================================================

label ch9_library:

    # [COMMENT: bg_library — vast underground library, mahogany shelves, floating lanterns]
    scene bg_library with dissolve              # PLACEHOLDER — Yuxuan's library
    play music ost_ch9_library fadein 2.0       # PLACEHOLDER — quiet library theme
    play audio amb_library loop fadein 1.5      # PLACEHOLDER — library ambient

    "I decided to visit Yuxuan's library, hoping to clear my head. The weight of the day pressed against my shoulders, and I needed a moment to breathe, to escape into something else-anything else."
    "I had never actually been to his library before. I had heard about it in passing, mentioned in Yuxuan's half-hearted grumbles about keeping track of rare texts, and Tim and Elias going there on my first day inside Yuxuan's underground library."
    "As I walked down the stone hallway, my thoughts drifted. When was the last time I even read a book?"
    "I remembered my time as a Paladin in the service of Empress Olympia. We had a special library, a grand hall dedicated solely to the knowledge that Paladins were meant to wield. Not just books on war strategy and elemental channeling, but history, philosophy, even works of art."
    "I recalled the way we used to tease Feng for his love of romance novels. He never hid it-on the contrary, he would often sit with a book in one hand and his sword in the other, completely engrossed in some dramatic tale of love and tragedy."
    "I smirked to myself. Far be it from me to read romantic novels. Or maybe..."
    "Maybe I could read some poetry. There was a poet from Hinami whose works I had once admired."
    "I reached the door and pushed it open. A gust of cool air met me, carrying the scent of aged parchment, ink, and ancient wood."
    "It was unlike anything I had ever seen."
    "Mahogany bookshelves stretched as far as the eye could see, their golden inlays shimmering under the glow of soft, floating lanterns. The ceiling loomed far above me, at least forty feet high, with delicate metal bridges connecting the upper floors."
    "Everywhere I turned, books, books, books-stories waiting to be unraveled, secrets of the past preserved in brittle pages."
    "At the far end of the library, a massive hourglass stood on a pedestal, its grains of sand moving slowly, almost as if time itself was sluggish within this place."
    "Seated at one of the long tables in the center, surrounded by open books and scattered notes, was Chung-hee."
    "Chung-hee didn't even glance up when I approached. His eyes remained fixed on the pages before him, scanning each line with sharp, unwavering focus. His brow furrowed slightly, his lips pressed together in concentration."
    "The only indication that he even registered my presence was a small flick of his fingers, wordlessly gesturing for me to sit-as if I were just another book settling into place in the grand archive."
    "I took a seat across from him, watching as he turned a page with the kind of delicate precision one would use when handling something ancient and fragile."
    "The silence stretched. I cleared my throat."

    dorian "Hey, Chung. What are you reading?"

    "Nothing."
    "I tilted my head, glancing at the book in front of him. I couldn't make out all of the text, but I recognized diagrams of ancient seals, detailed notes about ice and-was that a passage about divine imprisonment?"
    "He turned another page, his expression unreadable."

    dorian    "Chung?"
    chung_hee "Hm? Sorry..."

    "A pause. His fingers hovered over the text, hesitating just for a second, as if debating whether my question warranted an answer. Then, with an air of finality, he set his hand down."

    chung_hee "I'm reading about Magnus. The Divine Weapon."
    dorian    "Divine Weapon? You think Magnus is the Divine Weapon King Gustav was after?"

    "Before I could press him further, he flipped back a few pages, cross-referencing something in the text. His fingers began tapping against the wooden table, a nervous habit I had come to recognize-his mind was racing, processing faster than he could communicate."
    "Then, his thoughts came through, the words sharper, more fragmented than usual."

    chung_hee "Yes... and no."

    "I could feel the strain in the voice inside my head. His composure, usually steady and unwavering, cracked ever so slightly."

    chung_hee "Look, I remain unconvinced that the Divine Weapon is merely a fully-grown man with wings."

    "His thoughts pressed into mine with force."

    chung_hee "On top of that, I searched his mind thoroughly, there was NOTHING about his memories connected with being a Divine Weapon. None!"
    dorian    "You did say that most of his memories weren't there. Does that mean... he lost them? Like amnesia or something?"
    chung_hee "I'm afraid it is far stranger than that."
    chung_hee "He did not lose memories, Dorian. Nothing is forgotten by him. It's just as if nothing was there in the first place."
    chung_hee "Only select memories were there. I-"

    "His grip on the book tightened."

    chung_hee "I must uncover the truth. If my lead was mistaken, then what have I been chasing? Have I erred? What would my aunt think? I-"

    "I blinked."

    dorian "Your aunt?"

    "The moment the words left my mouth, his entire presence changed."

    dorian "Yesterday, the false Yuxuan mentioned that you had an aunt in Kyeongjang. Was that true?"

    "The rhythmic tapping of his fingers against the wood ceased. His eyes, which had been darting between pages, now remained fixed, unreadable."

    chung_hee "It is of no consequence. Forget it."

    "I studied him."

    dorian    "Chung-"
    chung_hee "Please drop the subject. I must concentrate."

    "And just like that, he retreated into his book. Focused."

    menu:

        "Press further for more details about his aunt.":
            $ ch9_chung_pressed = True
            $ chunghee_affection -= 1           # -1 Chung-hee affection

            "I didn't want to let it go. Not this time."
            "Maybe it was the way he shut down the moment I mentioned his aunt. The way his unshakable presence wavered, if only for a breath."

            dorian "Chung, I need to know. Who is your aunt?"
            dorian "Tell me more, do you have any other family in-"

            "But before I could even finish, he closed his book with a deliberate, measured thud."
            "He turned to face me, his eyes gleaming like polished metal, sharp and unreadable. The weight of his presence settled over me like an invisible force."
            "Then, in my mind, his voice cut through with the precision of a blade."

            chung_hee "Dorian. You saved my life. For that, I will always be thankful."
            chung_hee "But you must understand something. You and I met only yesterday."
            chung_hee "I hope you don't mistake shared battlefields for shared burdens."

            "The pressure lifted as quickly as it came, but the silence it left in its wake was suffocating. He was right. I had known him for only a day and a half."
            "Chung-hee adjusted his sleeve, returning his gaze to his book."

            chung_hee "You will always have my gratitude, but you must learn your place."

        "Let him be and read a book.":
            $ chunghee_affection += 1           # +1 Chung-hee affection

            "I didn't press further."
            "If he wasn't ready to talk, then pushing him wouldn't change that. I knew what it was like to have parts of your past locked away, too painful or complicated to bring to light."
            "Honestly, I might even be pissed if anyone pressed me about Elara or about my kids..."

            dorian "Alright."

    jump ch9_library_common


# =============================================================================
# SECTION 10: LABEL CH9_LIBRARY_COMMON — Poem / Weng Visit
# =============================================================================

label ch9_library_common:

    "I turned my attention to the shelves around me. There were books upon books-some old, some new, some nearly crumbling with age."
    "I ran my fingers over the spines before pulling out one with an ornate cover. Poetry from the Hinami era. Maybe something lighthearted would help clear my mind."
    "Beside me, Chung-hee returned to his reading, his focus unshaken. I opened the book of poems."

    "\" Farmer Oda - Takayori Sogen"
    "\""
    "\"Beneath the moon's pale, mournful gaze, Where silver waves in sorrow wane,"
    "\"A father knelt on weary knees,"
    "\"His heart weighed down with silent pain."
    "\"The rice fields sang of autumn's end,"
    "\"Yet no small hands would reap the grain. No laughter danced among the reeds, Only the echo of his name."
    "\"He held his child, so cold, so still, A blossom lost before its spring."
    "\"No breath remained to warm her lips, No voice to hear, no song to sing."
    "\"And so he turned to sea's embrace, Where all prayers drift and call,"
    "\"Where Dragon waits in endless depths, To cradle those who slip and fall."
    "\"He wove her name in whispered pleas, And cast his grief upon the tide."
    "\"The ocean opened, vast and deep, And drew his love to rest inside."
    "\"'O Dragon, keeper of the lost, Let not my child drift alone."
    "\"Within your depths, may she be free, Where seafoam sings and spirits roam.'"
    "\"The tide replied, a hush, a sigh, A touch of salt, a breath, a tear."
    "\"And in the waves, he swore he saw"
    "\"Her shadow flicker-bright, then clear."
    "\"No footprints lingered on the shore, The farmer turned, his sorrow vast."
    "\"Yet every time he faced the sea,"
    "\"He knew her soul had found its past."
    "\"For in the waves, she danced anew, A child of light, a child of blue."
    "\"No grave to mark, no stone to see- The ocean held her endlessly. \""

    "I closed the book. Lovely poem."
    "A father's sorrow. It hits close to home. Too close."
    "I ran a hand through my hair, trying to shake the heaviness from my chest, when the sound of footsteps broke the silence."

    "Miss Weng stepped into the library, carrying a few bottles of water."

    weng "I figured you two would be parched after reading so much."

    "She handed one to me, another to Chung-hee. He took it with a polite nod."

    chung_hee "Thank you, Miss Weng."

    "I twisted the cap open, taking a long sip of water, letting its coolness settle in my throat."

    dorian "How's the cooking coming along?"

    "Weng wiped her hands on her apron, her expression warm but a little tired."

    weng "We're still roasting the chicken and cooking the beef. It's taking a while, so I thought I'd check up on you both. Make sure you're not already starving."
    weng "Magnus is a lot of help, by the way. He's very optimistic about helping. Prepping ingredients take a lot of work, you know."

    "I noticed the slightest twitch in Chung-hee's brow. His fingers, which had been resting idly on his book, curled just a little tighter."

    weng "Anyway, if you're feeling hungry already, just let me know, okay?"

    "She left soon after, her footsteps fading into the distance. I turned to Chung-hee."

    dorian "Calm down, Chung. You're letting this whole Magnus business get into you."

    "His shoulders, drawn taut like a bowstring, loosened ever so slightly. He let out a slow breath, rubbing his temple before replying."

    chung_hee "Apologies. I am... on edge."

    "Minutes passed in quiet. The library remained hushed, save for the occasional soft rustle of pages turning. I kept reading, but my focus wavered, my mind drifting between the words on the page and the thoughts circling my head."
    "Then, out of the corner of my eye, I saw him."
    "His head had dipped forward, his arms crossed on the table, his breathing slow and even. Asleep."
    "I huffed a quiet chuckle. The library was dim, quiet, safe. I let my eyes close, surrendering to the pull of rest."
    "When we woke up, we decided to go back to our rooms."

    jump ch9_outfit_gather


# =============================================================================
# SECTION 11: LABEL CH9_BEDROOM_YUXUAN — Yuxuan Visit / Snacks
# =============================================================================

label ch9_bedroom_yuxuan:

    # [COMMENT: bg_lab_bedroom — cool, quiet bedroom, Elias asleep]
    scene bg_lab_bedroom with dissolve          # PLACEHOLDER — lab bedroom

    "The air inside the room was cool, the quiet hum of the air conditioning blending with the soft, steady rhythm of Elias' breathing."
    "I shut the door behind me, letting out a deep breath. Yesterday had taken a toll on me. My body ached from the strain of battle, my mind even more so."
    "I stood by the bedside, watching Elias sleep. His small body was curled up, his face relaxed in peaceful slumber. His chest rose and fell in a steady rhythm, his tiny fingers clutching at the blanket. Safe. Warm. Untroubled."
    "I ran a hand over my face, rubbing the back of my neck. Maybe some reading would help clear my head."
    "As I turned toward the small bookshelf, a memory surfaced-one of the past, of old comrades, of moments stolen between duty and war."
    "Paladin Feng."
    "We used to tease him for his love of romance novels."

    "Paladin Cyrus: Feng, are you seriously reading that in the middle of camp?"
    feng "Buzz off, Cyrus! I need my daily romance!"

    "But he never cared. He would sit with a book in one hand completely engrossed in some dramatic tale of love and tragedy, nodding along as if it were the most natural thing in the world."
    "I smirked to myself. Romance novels and battlefield strategies-Feng balanced both with equal enthusiasm."

    "The bookshelf was small, its wooden frame slightly worn from years of use. I scanned the titles-manuals on channeling, old Tianho folklore, and philosophical texts from the East and West."
    "Something about the channeling manuals made me pause. Why does Yuxuan have these? He's not a channeler."
    "My gaze drifted to another book-a collection of poetry by Takayori Sogen, the renowned poet from Hinami."
    "I ran my fingers along the spine of the book. Takayori Sogen. A famous poet from Hinami. Once a water channeler in the service of the Hinami King Tatsuya Fujiwara."
    "The king took note of his work and decided to help publish Takayori's work, making him famous. I could almost hear her voice-bright, teasing, full of conviction. She was crazy about this man."

    elara "I want to marry Takayori Sogen!"

    "I exhaled sharply, shaking my head. Elara. You crazy woman."
    "She had adored his poetry. So much so that if he had been alive in our time, she might have gone through with it-marrying the poet of longing himself."
    "With a sigh, I pulled it free, flipping through its delicate pages."

    "\" Farmer Oda - Takayori Sogen"
    "\""
    "\"Beneath the moon's pale, mournful gaze, Where silver waves in sorrow wane,"
    "\"A father knelt on weary knees,"
    "\"His heart weighed down with silent pain."
    "\"The rice fields sang of autumn's end,"
    "\"Yet no small hands would reap the grain. No laughter danced among the reeds, Only the echo of his name."
    "\"He held his child, so cold, so still, A blossom lost before its spring."
    "\"No breath remained to warm her lips, No voice to hear, no song to sing."
    "\"And so he turned to sea's embrace, Where all prayers drift and call,"
    "\"Where Dragon waits in endless depths, To cradle those who slip and fall."
    "\""
    "\"He wove her name in whispered pleas, And cast his grief upon the tide."
    "\"The ocean opened, vast and deep, And drew his love to rest inside."
    "\"'O Dragon, keeper of the lost, Let not my child drift alone."
    "\"Within your depths, may she be free, Where seafoam sings and spirits roam.'"
    "\"The tide replied, a hush, a sigh, A touch of salt, a breath, a tear."
    "\"And in the waves, he swore he saw"
    "\"Her shadow flicker-bright, then clear."
    "\"No footprints lingered on the shore, The farmer turned, his sorrow vast. Yet every time he faced the sea,"
    "\"He knew her soul had found its past."
    "\"For in the waves, she danced anew, A child of light, a child of blue."
    "\"No grave to mark, no stone to see- The ocean held her endlessly. \""

    "Just as I was about to place the book back, the door suddenly opened."

    "Yuxuan stepped inside, holding a plastic bag filled with treats. His silver hair was slightly tousled, and his long robes rustled as he moved. His eyes lit up when he saw me awake."

    yuxuan "Ah, Dorian! You're up-"

    "He cut himself off, glancing toward the bed. His excited expression immediately shifted to one of guilt when he saw Elias still fast asleep."

    yuxuan "...Oops."

    "I smirked, closing the book in my hands."

    dorian "You forgot it was Elias' nap time?"

    "He winced, treading carefully."

    dorian "How was the meeting with the representatives from Hinami?"

    "He sighed."

    yuxuan "By the Prosperity Dragon, they have so much planned! But they wouldn't tell me a single thing!"
    yuxuan "\"It's a surprise, Lord Cheng.\" They said. Pft! As if I enjoy surprises!"

    "I chuckled, leaning back against the couch."

    dorian "Is the King of Hinami already here with his royal entourage?"
    yuxuan "Yes, Dorian. All the royals are here in Tianho as we speak. Tianho, Gale, Hinami, Mjoll, and the Centennial Isles... and Kyeongjang... if you count Chung-hee."
    yuxuan "Technically he is the Emperor of Kyeongjang so..."
    yuxuan "By the way, I brought some freshly made fish treats from Hinami. Figured he'd like them. And maybe you would too."

    "I raised a brow. Fish treats?"

    yuxuan "I was supposed to bring the two of you there yesterday when... well... there was a bomb... and the whole situation with Chung-hee happened."

    "He placed the bag on the low table between us, and immediately, a rich, savory scent wafted through the air-crispy, golden batter infused with the deep umami of Hinami spices."
    "I glanced at Elias. Yeah. He wasn't going to eat that."

    dorian "Did you really just bring these for Elias, or were you hoping I'd be the one eating them?"
    yuxuan "Umm... Both? What can I say? You always look like you forget to eat."

    "Before I could argue, my stomach betrayed me with a low, unmistakable growl. Yuxuan crossed his arms, looking far too smug."

    menu:

        "Eat with Yuxuan.":
            $ ch9_yuxuan_ate = True
            $ yuxuan_affection += 1             # +1 Yuxuan affection

            "I sighed, defeated, and reached for the bag."

            dorian "...Fine."

            "Yuxuan laughed, then motioned to another bag."

            yuxuan "I also got some Tianho sweets. Figured I'd make up for yesterday."

            "The faint scent of sweet red bean paste and toasted sesame drifted from the package."
            "I opened it, finding an assortment of soft pastries, perfectly golden rice cakes, and delicate buns dusted with just a touch of sugar."

            yuxuan "Let's eat!!"

            "I picked up a crispy fish treat, the heat still lingering on its surface. As I took a bite, the flavors melted onto my tongue-a delicate balance of salt, spice, and the natural sweetness of the fish."

            yuxuan "Tianho always makes the best sweets. There's this one stall near the east district-"

            tedda_alive "Master Yuxuan, I saw you with sweets!"

            "We both turned as Tedda stepped in, carrying a small stack of water bottles in her arms. She shot Yuxuan a pointed look."

            tedda_alive "Well, I saw you carrying sweets, so I figured they were for my Lady Elias. I barely had time to react before she continued."
            tedda_alive "And since sweets can be a choking hazard, I took it upon myself to bring water for all of you. Because unlike some stuffed toys, I am a responsible caretaker!"

            "I covered my mouth, still chewing, and reached for one of the bottles. She plopped it down beside me with an exaggerated sigh, looking incredibly proud of herself."

            tedda_alive "What do you think, sir Dorian? Am I a responsible caretaker of Lady Elias?"

            "Unfortunately, I was still chewing."
            "Yuxuan, ever the opportunist, saw his chance."
            "He sat up straighter, then flashed the most ridiculous, salesman-like grin I had ever seen."

            yuxuan "He says yes, Tedda. But more importantly-!"

            "He turned toward an invisible audience, gesturing dramatically with the half-eaten pastry in his hand."

            yuxuan "Nothing pairs better with the delicious, time-honored taste of Cheng Industries' Tianho Sweets than a refreshing bottle of water!"

            "I stared at him, completely deadpan."

            tedda_alive "Even the fish treats, Master Yuxuan?"
            yuxuan      "No... Not the fish treats though. Those are from the Hinami booth."

            "Tedda grinned and reached for a fish treat."

            tedda_alive "They look delicious! I wanna try some! Yummy yummy fishy treat!"

            "I sighed, reaching for a sesame rice cake."

        "Don't eat with Yuxuan.":

            "If I decided not to eat the treats, Yuxuan's smile faltered-just for a second. It was subtle, barely noticeable, but I caught the way his expression dimmed."

            yuxuan "Oh... well, that's fine. More for Elias, I guess."

            "He shrugged it off, forcing an easygoing tone, but I knew him well enough to see the flicker of disappointment in his eyes."

            yuxuan "A-Anyway! That's not the only reason I came by. So you won't believe what my Operations Manager said to me-"

    "Yuxuan and I continued talking about nothing and everything-old stories, absurd rumors, his company. The conversation ebbed and flowed with ease."
    "Time slipped away unnoticed, and before I knew it, Yuxuan glanced at the clock and straightened with a start."

    yuxuan "Oh, wait! I have to go. I need to check up on Miss Weng. I need to see if she finished cooking the meals!"

    "He stood, brushing the crumbs from his ornate robes."

    dorian "Don't worry. I'll be here. I'll be up in a bit."

    "Yuxuan shot me a knowing look."

    yuxuan "Try not to fall asleep where you sit."

    "I waved him off with a lazy flick of my hand as he strode out the door, disappearing into the dimly lit hallway."

    "A small rustling from the bed caught my attention. I turned just in time to see Elias stirring, his tiny fists rubbing at his tired eyes. His hair was a tousled mess, and he blinked up at me in a sleepy daze."

    elias "Hello, Daddy."

    "His voice was soft, still laced with drowsiness. Then, his gaze shifted to the table, and the moment his half-lidded eyes landed on the neatly arranged pastries and treats, they snapped fully open."

    elias "Ooh! Treats!"

    "A sleepy grin spread across his face as he sat up, suddenly far more awake than he had been mere seconds ago."
    "I chuckled, shaking my head."

    dorian "Those are from Yuxuan."

    "I reached over, lifting Elias effortlessly from the bed and settling him onto the couch. He wiggled in place, already reaching for one of the sweet red bean pastries with eager fingers."

    dorian "Enjoy, buddy."

    "Elias took a big bite, his cheeks puffing out as he chewed. His eyes lit up, his entire face brightening with pure delight."

    elias  "Mmm! 'S yummy, Daddy!"
    elias  "Mister Yuxuan's always so nice! He's a biiiig heart!"

    "I smiled."

    dorian "He sure is, Elias. He sure is."

    jump ch9_outfit_gather


# =============================================================================
# SECTION 12: LABEL CH9_TAVERN — Tianho Tavern / Niko / Aoi
# =============================================================================

label ch9_tavern:

    # [COMMENT: bg_underground_door — lab exit, door greeting Dorian]
    scene bg_underground_door with dissolve     # PLACEHOLDER — lab exit

    play sound sfx_door_chime                   # PLACEHOLDER — door chime

    door_voice "Good afternoon, Master Dorian. A reminder: Today marks the Fifth Anniversary of the Tragedy of Tianho. A day of remembrance for those we lost."
    dorian     "You already know my name? I just came here yesterday."
    door_voice "I keep a record of all the guests through Roboto, Master Dorian."
    door_voice "Events will be held throughout the entire day and will conclude late into the night. Might I suggest visiting the Tianho Memorial? Or perhaps lighting an offering at the shrine?"
    door_voice "And for the most anticipated event of the evening-don't miss the grand Lantern Release tonight! Let your loved ones' spirits dance among the stars!"
    door_voice "Buy our exclusive Cheng Industries Lantern, now featuring: red weather-resistant paper, ensuring a smooth ascent even in the wind!"
    door_voice "Here at Cheng's, we bring change!"

    play sound sfx_cheng_jingle                 # PLACEHOLDER — Cheng jingle SFX

    "-Here at Cheng's, we bring change...  -"

    "A familiar odd jingle filled the area, the cheerful tone feeling almost out of place."

    dorian     "Lantern release? What's that?"
    door_voice "The Lantern Release is an age-old tradition in the kingdom of Tianho. Participants write the name of their departed loved ones on the lantern, along with a message from their heart."
    door_voice "Then, as the night deepens, they release the lanterns into the sky together, creating a breathtaking sea of light that drifts into the heavens."
    door_voice "Legend says that the Prosperity Dragon sees the lanterns and their messages. Moved by the love and longing of those left behind, the Prosperity Dragon intercedes on their behalf to the Dragon of the Depths."
    door_voice "And in turn, the Dragon of the Depths carries those messages to the dead."

    "The thought lingered in my mind longer than I expected."

    dorian     "I'll... think about it. Thank you for reminding me."
    door_voice "You're welcome. Have a wonderful day, Master Dorian!"

    # [COMMENT: bg_tianho_post_tragedy_day — Tianho streets, anniversary festival crowd]
    scene bg_tianho_post_tragedy_day with dissolve # PLACEHOLDER — Tianho streets, daytime
    play music ost_ch9_tavern fadein 2.0        # PLACEHOLDER — festival street theme
    play audio amb_tianho_festival loop fadein 1.5 # PLACEHOLDER — festival ambient

    "The walk to Tianho was uneventful, but as soon as I got close, the energy of the city hit me like a wave. The streets were alive with movement-vendors calling out their wares, children weaving through the crowds with paper lanterns, and musicians playing soft, somber tunes on guqins and flutes."
    "Something else caught my attention-almost no guards patrolled the streets. From Gale, I spotted a few soldiers, their posture rigid as they observed the proceedings. But from Mjoll? Almost none."
    "I exhaled, slipping past the solemn crowd, heading toward my destination-The Tavern of the Jade Serpent."
    "The moment I reached it, I hesitated. I had planned on grabbing a drink, maybe taking a quiet moment to gather my thoughts. But instead, my gaze swept over the people inside, and my instincts flared."
    "Mjoll soldiers."
    "A group of them, already deep into their cups, laughing raucously. Their uniforms were loosened, some were already shirtless, their posture sloppy, the distinct stink of cheap liquor wafting out onto the street."

    man_1 "Bottoms up! Haha!"
    man_2 "Hey! No fair, you cheating swine! My cup's barely half-full!"

    "Immediately, my body tensed. I had spent too many years fighting with Mjoll soldiers to be comfortable standing this close to them. If one of them recognized me..."

    niko "Tsk. Those Mjoll soldiers... You'd think they'd have better things to do than getting drunk in broad daylight."

    "I turned, finding him standing just behind me, arms crossed, his eyes flicking toward the soldiers."

    niko   "What are you doing here? Did you follow me?"
    dorian "Follow you? Hardly. I heard you were meeting your fellow prophets in a tavern. Thought I'd grab a drink myself."

    "Niko's gaze drifted back to the Mjoll soldiers. His smirk faded, replaced with a quiet look of distaste."

    niko "Change of plans. We ate at a local eatery nearby instead. Seeing all those Mjoll soldiers... well, let's just say it killed my appetite."

    "He exhaled, rubbing his temples before glancing back at me."

    niko "But if you're still planning on eating, maybe I'll join you. We didn't eat that much, and I could use something sweet."

    menu:

        "Eat with Niko.":
            $ ch9_niko_ate = True
            $ niko_affection += 1               # +1 Niko affection

            # [COMMENT: bg_tianho_food_stalls_day — food stall row, vendor with clay pot]
            scene bg_tianho_food_stalls_day with dissolve # PLACEHOLDER — Tianho food stalls

            "As we stepped away from the tavern, the scent of something rich and fragrant drifted through the air. I followed my nose to a nearby food stall, where a vendor worked over a sizzling clay pot, stirring a deep, amber-colored broth bubbling with spices."

            vendor "Fresh bowls of Cabbage Head Hotpot! Good for the soul on this solemn day!"

            "I peered into the pot-large, tender meatballs bobbed in the bubbling broth, their juices blending with softened napa cabbage and delicate glass noodles, all soaking in that rich, umami-laden depth of flavor."

            dorian "Ever had this before? It's called Cabbage Head Hotpot. A Tianho classic."
            niko   "Can't say I have. Looks pretty hearty. But sure, go ahead."

            "I ordered two bowls, and we settled onto a wooden bench nearby, the warmth of the simmering broth already curling into the crisp air."

            vendor "Two orders, sir? Coming right up! Thank you for your patronage!"

            "With practiced ease, he ladled the broth into heavy ceramic bowls, filling them to the brim before handing them over."

            vendor "Here you go, sirs! Two piping hot bowls of Cabbage Head Hotpot-perfect for a day like this."
            niko   "Ah- Merciful Enoch!"

            "He recoiled slightly, nearly dropping his bowl as the heat seared through the ceramic."

            vendor "Careful, sir! That bowl is fresh off the fire!"

            "The first spoonful was nothing short of perfection-the meatballs were impossibly tender, each bite infused with the warmth of ginger, garlic, and a whisper of five-spice."
            "The broth, thick and deeply savory, carried just the right balance of richness, clinging to the softened strands of cabbage."
            "Niko hummed in approval, his chopsticks plucking up a bundle of glistening noodles."

            niko "Alright, I'll admit-it's damn good. The cabbage soaks up all the flavor. Reminds me of the dishes we had back at the seacoast of Hinami."

            "As he leaned back, tapping his chopsticks against the rim of his bowl, curiosity flickered across his face."

            niko "Kind sir, this is excellent. Would you mind parting with the recipe?"

            "The vendor let out a hearty chuckle, shaking his head."

            vendor "Ah, I must apologize, sir. This recipe has been passed down through generations. Can't just go giving away family secrets."

            "He grinned, tipping his ladle toward us."

            vendor "But I'm honored by your praise."

            "I tilted my head toward Niko."

            dorian "Would you like seconds? I could go for another round."
            niko   "Maybe just an extra serving of noodles. Not the broth-I can feel it settling in my bones already."
            vendor "Coming right up, sir! Again, thank you for your patronage!"

            "As the vendor prepared another portion, Niko shot me an amused glance."

            niko "You eat more than I expected, Dorian. Guess it's fair, considering the last thing we had was dinner, and we're well past lunch now."

            "I only shrugged, savoring the last sip of broth on my bowl."

            "The vendor set our bowls down with a warm smile, steam curling up from the broth."

            vendor "Here you are, sirs. A second serving. I added extra meatballs to your bowl-on the house, in honor of the festivities."
            vendor "And also, I heard about what you did yesterday. Thank you for clearing the town from those damn yaoguai. Consider this my way of saying thanks."
            dorian "How generous. Thank you."
            vendor "You're most welcome, sir. If my daughter were still here, she'd have me giving out an extra meatball to anyone who so much as complimented the cooking. She had a kind heart like that."
            vendor "She was taken during the Tragedy... five years ago today. Our family was being chased by a yaoguai and... you know."

            "Niko set his chopsticks down, his gaze shifting, solemn."

            niko "I'm very sorry to hear that."

            "The vendor waved a hand, a wistful but resolute smile tugging at his lips."

            vendor "Don't worry yourselves, sirs. She wouldn't have wanted grief. Today, we honor the fallen, not with sorrow, but with life. And so, we cook, we eat, and we carry forward."

            "We ate the rest of our meal in a more reflective silence, letting the warmth of the broth settle in. Delicious."
            "Just as we finished, Niko's attention drifted elsewhere, his gaze sharpening."

            niko "...Now that looks interesting."

            "I followed his line of sight to a man pulling a wooden cart down the street, its wheels creaking softly over the stone path. A rich, caramelized aroma wafted from it-sweet, creamy, with just the faintest hint of toasted sugar."
            "Something about the man seemed familiar. Then it clicked."

            dorian "Wait... Gao? Is that you?"

            "The man looked up sharply, then broke into a broad grin."

            soldier_gao "Paladin Dorian! You're here!"
            niko        "Gao? The soldier yesterday? What are you doing here?"
            soldier_gao "Oh, Doctor Niko! Well, I'm selling! Care to buy some delicious Tianho flan? Fresh from my mother's kitchen."

            "He patted the side of the cart with pride, the lids of several ceramic dishes clinking faintly against one another."

            soldier_gao "You'd best grab them now, sirs. I'm heading to the memorial soon, and we sell out quickly."

            "Niko stepped forward, peering at the cart's contents with mild interest."

            niko        "How much?"
            soldier_gao "Five coins per flan, sir. It'll be worth every coin. I promise!"

            "Without hesitation, Niko reached into his pouch and pulled out several coins, stacking them in Gao's palm."

            niko "I'll take five."

            soldier_gao "Thank you, sir! I'll wrap those up for you!"

            "I blinked."

            dorian "Five, Niko?"
            niko   "One for you. One for me. One for Elias. One for Tim."
            dorian "...And the fifth?"

            "Niko hesitated, just for a moment. Then he exhaled through his nose, taking the wrapped flans from Gao with careful hands."

            soldier_gao "Here you are, sirs! Five Hinami flans!"
            soldier_gao "Anyway I have to get going. People in the memorial are a little impatient. See you, Paladin! Doctor!"
            dorian "Thank you, Gao! Stay safe, okay?"

            "Niko looked at me."

            niko "The fifth is for Kaito."

            "My breath caught in my throat. Kaito. Niko's younger brother."

            dorian "Well, I know for a fact that he'd love whatever you give him."
            niko   "I know. But he really loved sweets so I figured he'd definitely want this."

            "I didn't press. Instead, I simply nodded."

        "Pass the eating. Go home with Niko.":

            "I shook my head."

            dorian "I'm not really hungry, Niko."

            "Niko shot me a sideways glance but didn't push the matter."

            niko "Suit yourself. Let's get out of here."

    # CommonCommon — Niko/Aoi street encounter
    scene bg_tianho_post_tragedy_day with dissolve # PLACEHOLDER — Tianho streets

    "The steady beat of drums and the lilting notes of flutes filled the streets as we wove through the growing crowd. The air buzzed with conversation, laughter, and the occasional call of a vendor hawking their wares."

    woman_2 "Moonlit noodles! Especially hot for the occasion!"
    man_2   "Come get your Cheng Industries Lanterns here! Now featuring: red weather-resistant paper, ensuring a smooth ascent even in the wind!"
    woman_2 "Here at Cheng's, we bring change! Do you want your loved ones to feel extra loved? Try our new and improved-"

    "Then, through the throng of people, a familiar figure emerged."
    "A woman in a flowing indigo kimono, her posture as poised as ever, her expression unreadable."

    "Lady Aoi."
    "One of the commanders who had led the attack on Chung-hee."

    niko   "Keep your guard up, Dorian."
    dorian "You don't have to tell me twice."

    "Aoi's sharp eyes flicked to us, her gaze lingering just long enough to let us know she had seen us long before we noticed her. She tilted her head slightly, the faintest ghost of a smirk tugging at her lips."

    aoi "Sir Dorian. Doctor Niko. A pleasure."

    "We didn't return the greeting. Our stares were cold, unyielding. She rolled her eyes."

    aoi    "Why are you looking at me like that?"
    dorian "Oh, I don't know. Maybe because the last time we met, you tried to kill us?"
    niko   "Or because we have no idea if you're still working for King Gustav?"
    niko   "For all we know, you might still be getting coin from him."

    "She let out a slow, exaggerated sigh before raising her hands-not in surrender, but with an air of casual indifference."

    aoi "Oh, for the love of Tetrad. I'm not after the Emperor anymore. I know when I'm beaten."

    "She met our stares head-on, her voice cool and steady."

    aoi "Look, I'll be honest with you. Yes, I was in it for the money. I always am. But I'm not an idiot."
    aoi "The last mercenary who failed King Gustav's orders? He was executed. Him and his wife."

    "The words hung in the air like a blade over our heads."

    aoi "Xianlun knows I'm not going back there."

    "She fixed her hair with her fingers."

    aoi "I took the coin he gave me. And I deserted."

    dorian "So that's why you took the job from Feng."

    "Aoi gave a small shrug."

    aoi    "Pretty much. But that's not why I'm here right now."
    dorian "Speaking of which, where is Feng?"
    aoi    "With the Empress at the Tianho Memorial, I've heard. He told me that he's on guard duty and won't leave her side."

    "Before I could say anything, a woman approached, balancing a tray with a delicate porcelain cup. The faint aroma of herbs and citrus drifted through the air."

    woman_2 "Here it is, madam. Your Lóngyan Tea-brewed with fresh Xingcao leaves, just as you requested."

    "I frowned. Xingcao? The name was unfamiliar to me. Niko, however, arched a brow."

    niko "Longyan Tea? That tea's used by singers to clear their voices."

    "Aoi lifted the cup gracefully, inhaling the steam before taking a careful sip."

    aoi "Yes. I'll be singing tonight, Doctor."

    "She glanced up at us, watching our reactions with quiet amusement."

    aoi "Why the faces? Haven't you heard? Hinami is hosting the Anniversary this year."

    "Aoi took a small sip of her tea before answering."

    aoi "His Majesty King Tatsuya Fujiwara of Hinami specifically requested me for a song, and who am I to refuse?"

    dorian "Svante has mentioned that you were a songstress before."

    "Aoi let out a soft chuckle."

    aoi  "Oh, I was never anything grand. Just a woman with a voice, singing songs that spoke to my homeland."
    niko "Wait... you're the Mistress of Flowing Verses. You performed for King Tatsuya while channeling rain."

    "Aoi smirked slightly, swirling the tea in her cup."

    aoi "I see my reputation precedes me. But I'm no more than a normal person."

    "Niko leaned forward."

    niko "King Gustav is surely going to be at the Tianho Memorial for the ceremony. If you're singing, he'll see you. He might order your capture."
    aoi  "Let him try."

    "With that, she pointed to the small pin on her robe-a delicate emblem of Hinami's royal crest, unmistakable in its craftsmanship."

    aoi  "He'll be inviting war with the kingdom of Hinami. The royal singer is protected by His Majesty, King Tatsuya Fujiwara."
    niko "Good point."

    menu:

        "Encourage Aoi.":

            dorian "You must be an incredible singer if you performed for the King of Hinami himself. Channeling rain while singing... I can't even imagine the level of control that takes."

            "Aoi raised a delicate brow, her fingers brushing against the porcelain cup of tea. A small smirk curled on her lips."

            aoi "\"Famous\" is a strong word. I was simply... appreciated. People liked what I did. I didn't just sing-I told stories. I gave people something to believe in."

            "She placed her cup down and lifted a single hand, her fingers elegantly tracing the air. A cool breeze stirred around us, and suddenly, droplets of water formed in the air."
            "The moisture wove together into shimmering threads, swirling like mist before gathering into a delicate ribbon of liquid."
            "The ribbon of water coiled around her wrist like a living ornament before dispersing into the air in a fine mist. She exhaled slowly, as if lost in the memory."

            aoi    "The stage was my battlefield before I ever picked up a blade."
            dorian "I'm curious. I'd like to see you perform."
            aoi    "Then watch closely tonight. Who knows? Maybe I'll dedicate a verse to you."

        "Don't say anything.":

            "Aoi stood there, silent, her fingers resting lightly against the rim of her teacup. She exhaled softly, her gaze shifting away from me, scanning the crowd."

    "Aoi's gaze lingered on a family sitting nearby-an elderly woman pouring tea with careful, practiced hands, serving two younger figures. Their expressions were solemn, their movements slow and deliberate, as if honoring something unseen."
    "She exhaled softly, her fingers brushing against the silk of her kimono sleeve."

    aoi "I used to think music was just for beauty. For fleeting moments of admiration."

    "Her voice was quieter now, almost lost beneath the hum of the festival."
    "Then, just as quickly as the moment arrived, she straightened."

    aoi  "Anyway, I must bid you gentlemen farewell. I need to rest my voice for my performance later."
    niko "We wish you luck in your performance, Lady Aoi. Make Hinami proud."

    "She inclined her head slightly, her gaze sharp."

    aoi "I'll do my best. Take care, Sir Dorian. Doctor Niko."

    "With that, she turned and disappeared into the crowd, the faint scent of tea and jasmine lingering in her wake."
    "I let out a slow breath, shaking my head slightly before glancing at Niko."

    niko "Well... at least we have one less person who has a target on our backs."

    "Just then, out of the corner of my vision, a small figure came into view-marching toward us with determined little steps. Tim."
    "The tiny genius clutched a plate precariously balanced in his little hands. On it were three perfectly arranged slices of Tianho flan."

    niko "Tim? What in Enoch's name are you doing here alone?"
    tim  "S-Sir Niko? Sir Dorian? What are you doing here?"

    dorian "Adult stuff. Now back to you. What are you doing all by yourself here?"
    niko   "Miss Weng might be worried sick."
    tim    "I always go out by myself. I'm a big boy!"

    "Niko and I exchanged glances."

    tim "I went out of the lab and bought flan for all of us! I did the math. Three flan. One for me, one for Elias, and one we can share for the occasion! Perfectly balanced."

    "Niko, however, smirked and lifted a small paper bag, shaking it lightly."

    niko "I already bought five, kid. We have more than enough."

    "Tim froze. His eyes darted from the bag to his own plate. Then back to the bag. Then to the plate again."

    tim "Five, sir Niko?"
    niko "Five."

    "Another pause. A deep frown creased Tim's brow. He looked at his three flan. Then at Niko's five. Then back at his own."

    tim "...My calculations are wrong... Rookie mistake."
    tim "Numbers don't matter if you control the pace of the battlefield."
    niko "Well, it's better to have an abundance than a shortage. Let's just go back."

    "We looked at the number of people. It's getting larger."

    tim    "You're right, Sir Niko."
    dorian "Come on. Let's head back."

    jump ch9_outfit_gather


# =============================================================================
# SECTION 13: LABEL CH9_KITCHEN_HELP — Help with Cooking
# =============================================================================

label ch9_kitchen_help:

    # [COMMENT: bg_kitchen — kitchen, Svante chopping, Magnus with daikon]
    scene bg_kitchen with dissolve              # PLACEHOLDER — kitchen

    "Deciding to lend a hand with the cooking, I stepped back into the kitchen, where the rich aroma of sizzling oil, fresh herbs, and simmering broth filled the air."
    "At the counter, Svante was still hunched over a cutting board, his brows furrowed in concentration as he meticulously chopped green onions."
    "Magnus held the radish up to the light, turning it this way and that as though contemplating its very essence. Then, with a dramatic flourish, he brought his knife down, slicing cleanly through it."

    magnus "Ah! The crisp snap of a fresh daikon beneath my blade! It sings, a melody of earth and harvest, a tale whispered by the soil itself-"
    svante "It's just a vegetable, Magnus."
    magnus "A vegetable that has lived, Svante. A humble root, torn from its slumber beneath the earth, now meeting its noble fate in the fires of culinary creation."
    svante "Magnus, please just cut the daikon."

    "I smirked, folding my arms as I leaned against the counter."

    dorian "Where's Miss Weng? Shouldn't she be making sure Magnus doesn't turn dinner into a sonnet?"
    svante "Oh, sir Dorian! You're here! You decided want to help us?"

    "Magnus, still handling his daikon with far too much ceremony, gestured vaguely toward the back of the kitchen."

    magnus "Miss Weng has retreated to the sacred domain of baking."

    "Svante nodded, finally glancing up."

    svante "She took Tedda with her. Baking is a long and arduous process, and Mjoll cuisine requires a lot of it."
    dorian "Makes sense. I imagine it's easier with an extra pair of hands."
    magnus "Then we must prepare our stomachs! For a true feast is on the horizon!"

    "I sighed, stepping forward and turning my attention to Svante."

    dorian "Anything you need me to do?"

    "Svante stiffened slightly, his knife pausing mid-air for just a fraction of a second. His face turned the faintest shade of pink before he quickly gestured toward a small basket of onions beside him."

    svante "Ah-yes! The onions. We need more of them chopped."

    "I nodded and grabbed a knife, setting to work beside him. The sharp scent of onions filled the air, stinging my eyes slightly as I worked in quiet rhythm next to him."
    "Svante, still a little flustered, focused entirely on his own chopping, glancing at me every so often before quickly looking away."
    "After a moment, he cleared his throat."

    svante "So, um... Sir Dorian. You were with the Paladins before, right? With Paladin Feng?"

    "I nodded and continued chopping."

    svante "Is it true you were best friends?"

    "I paused briefly, considering my answer, before resuming my work."

    dorian "We were close, yes. In a way, you could say we were."
    svante "Oh... I see..."

    "My thoughts drifted to Feng. He was my closest friend during my time with the Paladins."
    "I remembered the countless times we sparred together, both of us fire channelers, pushing each other to our limits."
    "Neither of us held back-Feng never allowed it. He fought with relentless precision, his movements sharp and calculated, like a blade honed to perfection. But outside of battle? He was my closest friend."
    "I huffed a quiet laugh."
    "For all his discipline in combat, he had a habit of skipping training entirely-just so he could sit under a tree with a romance novel in hand, utterly engrossed in tales of star-crossed lovers and grand declarations of devotion."

    dorian "Why do you ask?"
    svante "Oh-um. Nothing, sir."

    "I sighed, shaking my head."

    dorian "There it is again. What's with the 'sir'? I thought I told you to just call me Dorian."

    "Svante stiffened slightly, his ears turning red as he immediately tried to correct himself."

    svante "Oh, s-sorry, s-Dorian! I meant Dorian-Sorry, sir. I mean-"

    "He cut himself off, flustered, then exhaled sharply before returning to his onions with renewed determination."
    "We continued cutting, the rhythmic thud of our knives filling the kitchen as the pile of onions gradually shrank. The sharp scent burned my eyes slightly, but I pushed through, matching Svante's steady pace."
    "As I reached for another onion, something on the counter caught my eye-a photograph, slightly worn at the edges but well-kept."
    "The image was of a woman frozen mid-motion, caught in the flow of a dance-her arms elegantly extended, her silken sleeves billowing like waves."
    "The pose was familiar."

    menu:

        "Keep quiet.":

            "I decided to keep quiet. It wasn't my place to pry."
            "Svante glanced at the counter, and his eyes widened slightly when he noticed the photograph still sitting there. His cheeks flushed, and with quick, almost clumsy movements, he scooped it up and slipped it into his pocket."

            svante "S-Sorry, Sir Dorian. I must have left it."

            "I offered a small, reassuring smile."

            dorian "Don't worry. I didn't see anything."

            "Svante nodded stiffly, though his fingers lingered over his pocket for a moment before he returned to his task."
            "Before the silence could settle for too long, a soft whirring sound cut through the air."
            "Roboto rolled toward us, its metal joints clicking faintly as it maneuvered across the kitchen. In one hand, it clutched a spatula-though whether it actually intended to cook or was simply mimicking us, I wasn't sure."

            roboto "Sir S-S-S-Svante, how are you holding up? You and S-S-Sir Magnus have been working a lot. Would you prefer to have a quick rest?"

            "Magnus scoffed, tossing his brown hair over his shoulder with unnecessary flair."

            magnus "Rest? Me? Real men power through all of this!"

            "Svante chuckled, shaking his head as he wiped his hands on a cloth."

            svante "Don't worry, Roboto. I've done harder tasks during my time at Mjoll with Father."
            magnus "That's the spirit! A true warrior of the kitchen!"

        "Ask about the woman in the picture.":
            $ ch9_svante_photo = True
            $ svante_affection += 1             # +1 Svante affection

            dorian "This dance... It's budao weng, right?"

            "A dance performed in Tianho by women and, at times, crossdressing men-known for its fluid movements that mimicked the rolling of waves and the shifting of the wind."
            "Beside me, Svante's knife stilled. His gaze flickered toward the photograph, and for a moment, something unreadable crossed his face. Then, with slightly pinkened cheeks, he quickly took the picture back, slipping it into his pocket."

            svante "S-Sorry, sir. That's just my mom."
            dorian "Oh, that's right. You mentioned before-your mother was a songstress in Tianho."
            svante "Yes, sir. This photo was taken during one of her performances when I was younger. She would perform the budao weng while singing."

            "There was an unmistakable fondness in his tone."

            dorian "She looks graceful."
            svante "She was, sir."

            "A small, almost shy smile crossed Svante's lips before he nodded."

            svante "You see... the budao weng requires precise balance. The movements are fluid, but they need to be controlled."
            svante "My mother would wear metal cufflinks on her ankles-thin, but heavy enough to ground her movements."
            svante "She asked me to reinforce them since I can channel metal. To ensure she wouldn't slip or stumble."
            svante "She taught me a lot about performance. About music, dance... even metal channeling."
            dorian "Metal channeling? Is she a metal channeler?"

            "Svante shook his head."

            svante "No, sir. My mother is a fire channeler."
            svante "But... she studied it. She read books, talked to scholars from Tianho, Mjoll, Gale-did everything she could to understand what I could do. She didn't know how to channel metal herself, but she still coached me."
            svante "She helped me refine my control, made sure I didn't strain myself, even though there was barely any information out there."

            "A soft whirring sound interrupted us."
            "Roboto rolled toward us, still clutching a spatula in its metal hand."

            roboto "Resources about metal channeling are scarce, so it's a-a-a-amazing how she managed to teach you something."

            "Svante turned toward Roboto with bright eyes."

            svante "Thank you, Roboto."
            roboto "Anyway, d-d-d-d-do you dance and sing, sir Svante?"
            svante "D-Dance? Where did you get that?"
            roboto "Y-Y-You said that you mom taught you a lot about performance. About music, dance. S-S-So I assumed that she taught you how to dance and sing."
            svante "I... I know how, but I'm not really good at it. Not as good as Magnus here."
            magnus "*belting a high note* Ahhhh!"
            svante "See?! I can't compare to that!"

    jump ch9_kitchen_common


# =============================================================================
# SECTION 14: LABEL CH9_KITCHEN_COMMON — After Cooking CommonCommon
# =============================================================================

label ch9_kitchen_common:

    "Then, as if realizing something, he let out a small chuckle, rubbing the back of his neck."

    svante "Sorry. I'm just so happy! It's just... I've never had a conversation with a real-life robot before."

    "Magnus suddenly clapped his hands together, his brown hair catching the light as he grinned."

    magnus "Me too! And now, I feel the poetic urge to compose a song in honor of our beloved robotic companion!"

    "Magnus took a deep breath and, with the dramatic flair only he could muster, began to sing in an exaggerated operatic tone."

    magnus "Oh, noble steel and gears divine! ~"
    magnus "With spatula in hand, a chef most grand! Oh, dear Roboto, guide our pan! ~"

    "I exchanged glances with Svante, suppressing a chuckle. Is this the man who almost killed us?"

    svante "He's been like that since early morning."

    "Roboto, however, didn't seem the least bit fazed by Magnus' impromptu serenade. The little automaton simply adjusted its grip on the spatula before addressing Svante again."

    roboto "We have a lot of delivery a-a-a-autobots in Mjoll, Sir Svante. Are you sure you haven't spoken to any of them before?"

    "Svante shook his head."

    svante "The Cheng Industries delivery bots don't really talk, Roboto."
    svante "Me and Kristin tried talking to one once, but all they do is sing a jingle."

    "Roboto whirred again, processing the information."

    roboto "I u-u-understand. You mean the Cheng Industries Jingle! Delivery autoboots are programmed to register the Cheng Industries Jingle as their automated response for any query."
    roboto "H-H-H-Here at Cheng's, we bring change."
    magnus "HERE AT CHENG'S, WE BRING CHANGE!!!~"
    dorian "Dragon's bollocks, Magnus! You surprised me!"

    "Roboto, still clutching the spatula, simply beeped in satisfaction."
    "Magnus, emboldened by his successful performance, placed a hand over his chest as if addressing an invisible audience."

    magnus "A glorious melody, etched into the hearts of many! A song of commerce! Of unapologetic capitalism! Of-"
    roboto "W-W-W-Would you like some help in cutting the daikon, sir Magnus?"

    "Magnus sighed dramatically, shaking his head as if he had just been gravely wronged."

    magnus "I don't need help, Roboto. A thousand thanks though."

    "After a solid hour of work, we had finally finished all the preparations. Svante, Magnus and I handled the chopping-onions, scallions, daikon, and an assortment of other vegetables."
    "Magnus, despite his flair for dramatics, proved surprisingly efficient at peeling and slicing. Roboto assisted where it could, handing us ingredients and even stirring a few mixtures under supervision."
    "By the time Weng and Tedda returned, the counters were neatly arranged with trays of prepped vegetables, cleaned fish, and marinated meats. Weng smiled in approval before effortlessly taking over the more delicate cooking-frying, broiling, and adjusting flavors with practiced ease."

    # [COMMENT: bg_yuxuan_lab_dim — lab living room, dimmed lights, post-cooking rest]
    scene bg_yuxuan_lab_dim with dissolve       # PLACEHOLDER — lab dimmed living room

    "Svante yawned, rubbing his eyes before mumbling a quick goodnight and retreating to his room."
    "I sank into the sofa with a sigh, exhaustion settling deep in my limbs. The warmth of the kitchen still clung to me-the scent of spices, the lingering crackle of oil."
    "Beside me, Magnus flopped down with little grace, his wings shifting as he got comfortable. The soft rustle of feathers filled the quiet space between us."

    magnus "Woo! I can't believe we finished all of that! My hands are still sore from the chopping."

    "He wiggled his fingers for emphasis, then flexed them dramatically as if they had endured some great battle."

    magnus "Oh, the toil of mortal labor! The weary hands of a soldier turned humble servant of the kitchen! Is this the fate I have been reduced to? From the clash of steel to the gentle kiss of a kitchen knife against daikon?"
    dorian "Magnus, are you seriously comparing chopping ingredients to fighting a war?"

    "Magnus grinned, folding his arms."

    magnus "Precisely! And I-I, the valiant warrior-have emerged victorious once again!"

    "His wings fluttered slightly as he leaned back, letting out an exaggerated sigh of satisfaction. I watched him quietly, my thoughts beginning to drift."
    "It was only last night that we rescued Magnus. The memory of it still clung to the corners of my mind-the rush of the wind, his wings outstretched like some celestial figure, the sheer relief of being alive."
    "I debated whether to bring it up. Would it even be appropriate? Would he shrug it off with that same careless charm, or would he acknowledge the weight of what he had done?"
    "But before I could decide, he began to hum. A familiar melody."
    "I turned my head slightly, listening as his deep, rich voice filled the space between us. The song was unmistakable-a traditional Galean ballad, one I hadn't heard in years."

    dorian "That song..."

    "Magnus smiled, eyes half-lidded in contentment."

    magnus "Ah, you know it? Of course you do. It is the Song of Longing. A tale as old as the gales themselves."

    "He sang softly, the words carrying an old sorrow, a quiet yearning."

    magnus "O sky above, how cruel you are, to gift me wings yet keep me far..."

    "I watched him as he sang, the way his fingers tapped idly against his knee in time with the rhythm."

    menu:

        "Keep on listening.":

            "I didn't join in. Instead, I simply leaned back against the sofa, letting Magnus' voice fill the room. The melody curled around me like the wind itself-soft, wistful, full of yearning."
            "Magnus' eyes were half-closed as he sang, completely lost in the music. His fingers tapped lightly against his knee, keeping time with a rhythm only he could hear. There was something unguarded about him in this moment, something raw beneath the usual bravado."
            "When he finished, he exhaled, smiling to himself."

            magnus "A beautiful song, isn't it?"

            "I nodded, reclining further into the sofa."
            "Magnus stretched his arms above his head, wings fluttering slightly as he relaxed further into the sofa as well."

            magnus "Ah, but enough of that. I mustn't let my heart grow too sentimental. We have a feast ahead, after all!"

        "Join him in singing.":
            $ ch9_magnus_song = True
            $ magnus_affection += 1             # +1 Magnus affection

            dorian "O gentle breeze, please let me fly, so I may reach where heavens lie..."

            "Magnus' voice faltered for just a second, as if surprised, but then he grinned, adjusting his pitch to harmonize with mine. His voice was richer, seasoned with experience, while mine was steadier, more grounded."
            "When we finished, Magnus laughed softly, a genuine warmth in his expression."

            magnus "Well, well. Not bad at all, Dorian. You've got the soul of a Galean troubadour hidden beneath all that paladin steel."
            dorian "Don't get used to it."
            magnus "Oh, but now that I know you can sing, how could I not?"
            magnus "You sang the song well, Dorian. You may not have wings, but your voice knows the wind."

            "His wings fluttered slightly, a sign of amusement. There was a pleased glint in his eye, and though he said nothing more, I could tell-he was genuinely happy."

    jump ch9_outfit_gather


# =============================================================================
# SECTION 15: LABEL CH9_OUTFIT_GATHER — Everyone Gathers for Outfits
# =============================================================================

label ch9_outfit_gather:

    # [COMMENT: bg_yuxuan_lab — lab main room, Yuxuan entering with crimson robes]
    scene bg_yuxuan_lab with dissolve           # PLACEHOLDER — lab main room

    "Hours passed, and as the evening settled in, Yuxuan called for all of us to gather in the living room."
    "He entered with his usual air of effortless grace, his long crimson robes flowing like mist over water. His presence alone was enough to quiet the room."
    "Weng followed closely behind him, her arms stacked with neatly folded garments, each one shimmering under the lantern light. The delicate embroidery caught my eye immediately-fine, intricate threads woven into mesmerizing patterns."

    yuxuan "Everyone, it is time to dress for the occasion."

    "He gestured to Weng, who carefully laid the outfits out for all to see."

    weng "They've been tailored to fit each of you perfectly."

    "Her voice was brimming with pride as she smoothed the fabric with careful hands."

    yuxuan "The colors were chosen with intention."

    "He let his gaze sweep over us, taking in each reaction."

    yuxuan "They speak of who you are. They reflect your spirit. Wear them, and you will command not just attention, but respect."
    tim    "But it is unfortunate to say that Roboto and Tedda won't be getting any garments."

    "Before I could step forward to examine them closer, a small, mechanical whir filled the air."

    roboto "It is understandable since I do not require g-g-g-garments."

    "Its tone was matter-of-fact, entirely devoid of complaint."

    roboto      "Nor does Miss Tedda. I am a machine, and Tedda is-"
    tedda_alive "Awwww!!! But I wanna dress up tooooo!!"
    elias       "*cries* It's unfwair!"

    "Elias cried and hugged Tedda. His small fists clenched as he pouted up at me."

    dorian "Elias, it's not the end of the world."
    niko   "They'll survive."
    tim    "Hmm. Come to think of it, the outfits look like what we wore last time, Miss Weng."

    "Despite his deliberately dry tone, his eyes lingered on the stitching, a clear sign that he approved of the craftsmanship."
    "Then there was Magnus."
    "He stepped forward, his gaze sweeping over the garments as though he were staring at something divine. Slowly, he reached out, barely brushing his fingertips against the fabric."

    magnus "These outfits look... STELLAR!"
    magnus "Oh, look how the threads of fate are woven into cloth! The artisans who stitched these must have whispered to the very stars, coaxing light and shadow to dance upon silk and thread!"
    tim    "I firmly agree, sir Magnus!"
    niko   "Yuxuan, you do realize we can't go to the Tianho Memorial, right?"

    "Weng paused. Even Elias' previous pouting seemed to freeze."

    svante "Sir Yuxuan... you said Father would be there, right?"
    svante "I... I don't want to be seen."
    magnus "Svante, you have a father? You did not mention this to me earlier. Do you two share a strained bond-"
    svante "I... I'll tell you later, Magnus."

    "Chung-hee's arms were crossed, his expression unreadable."

    chung_hee "Svante's right. As much as I'd love to challenge King Gustav right then and there, I doubt he'll fight fair."
    elias     "Daddy, does that mean we don't get to eat Hinami fwan?"
    dorian    "We're just not going to the memorial, Elias. You can still have some. Hey, stop tugging my sleeve."
    elias     "Oh... okay. I really wanted some fwan."
    tim       "Elias, I bought one for you! We'll still eat Hinami flan!"
    elias     "Yeyy!!"
    tedda_alive "Aww, but we still won't see the festivities!"
    niko      "It's for the best. We don't want to risk getting seen by King Gustav."
    yuxuan    "Who said anything about being seen?"

    "He stepped forward, his gaze sweeping over us like he was savoring the moment."

    yuxuan "There is a place-one where we can watch everything unfold without a single soul noticing us."
    roboto "Master Yuxuan has m-m-m-made a place available so all of us can participate in the festivities. We will have a magnificent view of the memorial!"
    weng   "Not only magnificent. But also romantic!"

    "I narrowed my eyes."

    dorian "And where exactly is this place, Yu?"

    "Yuxuan merely chuckled. His voice was like silk, smooth and unreadable."

    yuxuan "Patience, Dorian... You'll see."

    "Magnus, of course, immediately seized the moment, launching into song with a dramatic flourish."

    magnus "Oh, secrets held in moonlit air, unseen eyes in silent stare-"
    magnus "But seriously. Where?"
    niko   "Agreed. I apologize for the bluntness, but I don't care if this place has a 'magnificent view.' What I care about is our safety."
    svante "We need to be safe. I'm sorry. I'm just... very anxious. I don't want to see Father."

    "Yuxuan only smiled wider, tilting his head in amusement."

    yuxuan "It's a surpriseeeee~"

    "Niko groaned, rubbing his temple. Tedda, still pouting, looked up at Chung-hee with wide, pleading eyes."

    niko      "I hate surprises. Can't you just read Yuxuan's mind, Chung?"
    chung_hee "Do you consent to having your mind read, Yuxuan?"
    yuxuan    "WHAT?! By the Prosperity Dragon's name, NO!"
    chung_hee "Well, there. You have your answer."
    tedda_alive "Awww!!"
    niko      "But aren't you already reading our minds?"
    chung_hee "I read minds, yes. But as much as possible, I don't delve deep to look for secrets. Especially those I have a relationship with... or am trying to have a relationship with."
    svante    "Hahahaha!"

    "Yuxuan arched a brow, crossing his arms as he turned his gaze back to Chung-hee with playful intrigue."

    yuxuan    "Trying, are we?"
    chung_hee "..."

    "Chung-hee didn't respond and walked away."

    niko "Sighs Leave the man alone, Yuxuan."

    # [COMMENT: bg_lab_bedroom — Elias and Dorian heading to room]
    scene bg_lab_bedroom with dissolve          # PLACEHOLDER — lab bedroom

    "Elias and I made our way back to our room, his small hand gripping mine tightly. Just as I pushed the door open, hurried footsteps padded behind us."
    "Tim trailed in, carefully balancing a plate stacked with glistening slices of Hinami flan."

    tim "Elias! Elias! Look what I got!"

    "The caramelized tops shimmered under the lantern light, their rich, golden hue promising nothing short of perfection."
    "Elias wasted no time, eagerly grabbing a piece and taking a bite. The moment the soft custard melted on his tongue, his entire face lit up in pure joy."

    elias "It's so sweet! I LOVE IT! I LOVE FWAN!"

    "Tim beamed, arms crossed as if he had just proven a great point."

    tim    "See, Sir Dorian? I told you Elias would love it!"
    tim    "We have so much food for the festivities! Miss Weng cooked a lot! You'd be happy!"
    dorian "We do have a lot of food."
    elias  "Like... a mountain of food!"

    "His excitement was contagious, his legs kicking under the table as he stuffed another spoonful into his mouth."

    tim   "A whole kingdom's worth of food! An entire feast!"
    tim   "And mooncakes! And those soft, fluffy steamed cakes! And grilled skewers with that amazing sauce!"
    elias "The sauce! The sauce!"

    "They both burst into giggles, their shared enthusiasm making even me hungry."

    tim  "Oh! Sir Dorian-Sir Niko told me that you're a great storyteller!"
    elias "Ooh! Yes, Daddy is a great storyteller!"
    tim   "Really? Is that true? Sir Dorian, can you tell us a story sometime?"

    "The two of them looked up at me with wide, hopeful eyes."

    menu:

        "I'm too busy.":

            "I sighed, rubbing my temples."

            dorian "Not tonight. I have too much on my plate."

            "Elias' face fell, his excitement dimming like a candle in the wind. He looked down at his half-eaten flan, suddenly less enthusiastic."

            elias "Oh... okay."

            "Tim frowned but nodded in understanding."

            tim "I get it! You're busy. Maybe another time, Sir Dorian?"

            "Elias didn't respond right away. He simply shoved another bite of flan into his mouth, quieter than before."

        "Sure. Maybe once I'm available.":
            $ ch9_story_promised = True
            $ magnus_affection += 1             # +1 Magnus affection

            "I smiled, ruffling Elias' hair before nodding."

            dorian "Maybe once I'm free. I'll tell you both a story then."

            "Tim grinned, clasping his hands together."

            tim   "Ooh, I can't wait! Please tell me something I haven't read before! Please!"

            "My eyes widened. I doubt I have something Tim hasn't read before."

            tim    "Magnus also said he wanted to tell me and Elias some stories too!"
            dorian "Magnus? Really?"
            tim    "Yes! He said he'll tell us some old Galean ballads. Something about heroes and destiny and whatnot."
            dorian "I'll tell the two of you a story soon. But for now, we need to get ready."

            "Tim and Elias high-fived each other, their excitement renewed."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep SFX

    "A gentle but firm knock echoed from the door. I sighed, setting aside my cup as I got up to answer. The moment I pulled the door open, I found myself face-to-face with Roboto, its metallic figure standing stiffly in the hallway."

    roboto "Master Yuxuan requests your presence, Special Guest."

    "I raised an eyebrow."

    dorian "Special guest?"
    roboto "Yes. You are invited to b-b-bathe with him in the underground hot springs. This is for preparation in wearing the special outfits you will don for the Anniversary."
    dorian "Hot springs? I didn't know Yu had a hot spring here."

    "From inside the room, Tim piped up between bites of flan."

    tim    "Oh, yeah! Master Yuxuan has a hot spring here. It's natural!"
    elias  "Oh weally? Ish it nice?"
    dorian "Elias, don't talk when your mouth is full... Roboto, how exactly does a hot spring exist here?"

    "Roboto's eyes flickered for a moment before launching into an explanation."

    roboto "The underground hot s-s-springs are a result of geothermal activity. Heated groundwater rises from deep within the earth due to volcanic activity beneath Tianho's b-b-bedrock."
    roboto "The mineral-rich waters are known for their r-r-rejuvenating properties."
    elias  "Whoa... What's a geo-thermical?"
    tim    "It means the ground makes the water hot!"

    "I chuckled, shaking my head."

    dorian "Sounds luxurious, Roboto, but I need to bathe Elias first so he can get dressed in the outfit Yuxuan gave him."

    "Roboto tilted its head slightly."

    roboto "Don't worry, sir Dorian. Miss Tedda will see to it."

    "From the corner of the room, Tedda-Elias's ever-loyal stuffed bear-let out an indignant little squeak."

    tedda_alive "Aww! But I wanted to relax too! I never get to do anything fun!"
    elias "It's okay, daddy. Tim and I will be hewe."
    tim   "Yeah! Go enjoy your bath, Sir Dorian! I'll make sure Elias doesn't eat all the flan before you get back."
    tedda_alive "Hey! Lady Elias deserves to eat ALL the flan!"
    dorian "Tedda, we talked about this..."

    "Roboto took a step back, motioning for me to follow."

    roboto "Come follow me, m-m-master Dorian... The hot springs await..."

    "I exhaled, casting one last glance at the two troublemakers... and Tim before stepping into the hallway."

    tedda_alive "Ooh Lady Elias! Your outfit is so pretty!"
    tim         "Look at mine! Don't I look handsome? Hehe."

    jump ch9_p2


# =============================================================================
# SECTION 16: LABEL CH9_PRE_HOTSPRING — End of Part 1
# =============================================================================
# ch9_p2 is defined in chapter_09_p2.rpy and begins at [ BG - Hot Spring ].
# =============================================================================

label ch9_p2:

    jump chapter_09_p2


# =============================================================================
# END OF CHAPTER 9 PART 1
# =============================================================================
