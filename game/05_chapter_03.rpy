###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  FILE:  chapter_03.rpy
#  SCENE: CHAPTER 3 — Frostcradle: The Child in the Ice
#
#  CONTENTS:
#    Section 1  — Character Definitions
#    Section 2  — Image Declarations  (backgrounds, CGs, sprites)
#    Section 3  — Audio Declarations  (music, SFX, ambient)
#    Section 4  — Game Variables      (trackers, flags, choice records)
#    Section 5  — label chapter_3     (opening — journey to Frostcradle)
#    Section 6  — label ch3_mine      (entering the mine / bodies)
#    Section 7  — label ch3_yuki_boss (Yuki-onna boss fight — D1–D4 QTCs)
#    Section 8  — label ch3_truth     (Elias found / Ekaterina's ghost)
#    Section 9  — label ch3_elias_questions (D — optional questions to Elias)
#    Section 10 — label ch3_blizzard_trapped (blizzard days begin)
#    Section 11 — label ch3_yuxuan_arrives   (supply bot / hologram scene)
#    Section 12 — label ch3_mushroom  (D6 — mushroom invitation with Yuxuan)
#    Section 13 — label ch3_breakfast (D7 — 4-option cooking choice)
#    Section 14 — label ch3_vasily_arrives   (Vasily battalion + Kristin death)
#    Section 15 — label ch3_critical_fork    (D5 — give or protect Elias)
#    Section 16 — label ch3_bad_end          (BAD ENDING — give Elias)
#    Section 17 — label ch3_fight_back       (GOOD PATH — draconic fire awakens)
#    Section 18 — label ch3_escape           (escape with Yuxuan; chapter end)
#
#  NAMING CONVENTIONS (enforced throughout):
#    image tags      — bg_name, cg_name, character_name emotion
#    audio variables — audio.ost_name, audio.sfx_name, audio.amb_name
#    label names     — ch3_name (all lowercase, underscores only)
#    game variables  — yuki_tracker, svante_affection, yuxuan_affection, etc.
#    NO SPACES in any tag, label, variable, or image name.
#
#  TRACKER SUMMARY:
#    yuki_tracker      : accumulates in D1–D4; ≥2 = GAME OVER after D4
#    svante_affection  : +1 if D5 = Refuse and fight
#    yuxuan_affection  : +2 if D6 = Join Yuxuan; -1 if D6 = Don't join
#    D7 (cooking)      : 4 soft-branch options; no stat effect
#
#  HARD GATES:
#    D4 wrong answer (dodge instead of fire blast) = GAME OVER
#    D4 correct but yuki_tracker >= 2 = GAME OVER (frost overwhelm)
#    D5 = Give Elias → BAD ENDING branch (irreversible)
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


# =============================================================================
# SECTION 3: AUDIO DECLARATIONS
# =============================================================================

# --- Music ---
# TODO: royalty free music with the vibes of the game

# --- SFX ---
# TODO: find and add sfx

# --- Ambient ---
# TODO: find and add ambient sounds
# cold wind, blizzard, fire crackles, carriage wheels

# =============================================================================
# SECTION 4: GAME VARIABLES
# =============================================================================

# yuki_tracker already declared in chapter_01.rpy — not redeclared here

# --- Chapter 3 choice records ---
# default ch3_d1    = ""   # "fire_circle" or "smash"
# default ch3_d2    = ""   # "lure" or "stand"
# default ch3_d3    = ""   # "fire_wall" or "dodge_burst"
# default ch3_d4    = ""   # "dodge" (game over) or "fire_blast"
# default ch3_d5    = ""   # "gave" or "refused"
# default ch3_d6    = ""   # "joined" or "skipped"
# default ch3_d7    = ""   # "omelette" / "soup" / "fried" / "rice"

# default ch3_asked_mom       = False
# default ch3_asked_amulet    = False
# default ch3_asked_bodies    = False


# =============================================================================
# SECTION 5: LABEL CHAPTER_3 — Opening (Journey to Frostcradle)
# =============================================================================
# Entry point — jumped to from chapter_02.rpy via 'jump chapter_3'.
# Dorian sets out alone into the blizzard toward Frostcradle.
# His family's ghost-voices accompany him as comfort.
# =============================================================================

# =============================================================================
# SECTION 9: LABEL CH3_ELIAS_QUESTIONS — Optional Questions to Elias
# =============================================================================
# Dorian recovers. He and Elias eat. Player can ask Elias optional questions.
# All paths converge on the blizzard scene.
# ACTUAL START OF CHAPTER 3
# =============================================================================
label ch3_elias_questions:
    
    $ save_name = "Chapter 3"

    scene cg_black with fade                            # PLACEHOLDER — carry from ch2 end
    pause 1.0

    show screen chapter_title_screen(
        "3",
        "Frostcradle",
        subtitle="The Child in the Ice",
        duration=3.0
    )
    pause 3.0

    scene frostcradle_cabin_on with fade
    "The cold floor bit into my cheek as I stirred awake. The roar of the blizzard echoed through the mining cave like a living beast."
    "When I opened my eyes, I was greeted by the dim light of the shack. Elias was in the corner, fumbling with what appeared to be a jar."
    "His tiny hands struggled against the lid, his face scrunched up in determination."

    show dorian neutral at left_char with Dissolve(0.2)
    dorian "What are you doing?"

    show elias first_meet_neutral at right_elias with Dissolve(0.2)
    elias "Ahhh!"

    show dorian normal_alt_calm at left_char
    dorian "Hey. I'm not going to hurt you."

    "Elias clutched the edge of a blanket like it was a shield, his gaze flickering between me and the jar."
    "I noticed it more clearly. Old and scratched — a preserve jar. Fruits, most likely. His little hands had been trying to open it."

    show dorian normal_alt_neutral at left_char
    dorian "You were trying to get this open, right?"

    "I reached for the jar slowly, watching as he tensed. His lips quivered, but he didn't say anything, just stared at me with those wide, frightened eyes. "
    "I took the jar and gave the lid a firm twist. It popped open with ease, the faint, sweet aroma of preserved fruits wafting into the air."
    "I set it back on the ground and slid it toward him."

    dorian "There. All yours."

    show elias first_meet_happy at right_elias with Dissolve(0.2)
    "He hesitated, then inched forward cautiously, still clutching the blanket. His tiny hands darted out to grab the jar, pulling it close. He buried his face in it and began to eat."

    show dorian neutral at left_char
    dorian "You need to wipe your face. Hold on."

    "I knelt and opened my pack. My hands brushed against something familiar. Emily's ribbon. Lucas's slingshot. Daniel's carved wooden horse. Elara's scarf. And Tedda — the knit doll with the missing eye."

    show dorian sad at left_char
    dorian "How did these get here?"
    show dorian neutral at left_char
    show elias first_meet_neutral at right_elias
    "I turned back to Elias, who was licking his fingers, his small face sticky with syrup. I offered him the cloth."

    dorian "Alright. Hold still."

    "I wiped his face gently, the cloth coming away sticky and stained. He squirmed a little but didn't resist."

    dorian "How old are you?"

    "Elias hesitated, then held up three fingers."

    show elias first_meet_happy at right_elias
    elias "Fow."
    show elias first_meet_neutral at right_elias

    show dorian smile at left_char
    dorian "Four, huh? You sure about that?"

    "He nodded, with a serious expression on his face."
    "I watched as Elias went right back to eating, his tiny hands sticky again with syrup. I sighed, shaking my head. I had just cleaned him up."
    "Sitting back against the creaky shack wall, I decided to try asking him a few questions."

    show dorian neutral at left_char
    dorian "Alright. I have some questions."
    "Elias didn't look up, too focused on scooping out the last bit of syrup from the jar with his fingers."

    jump ch3_question_menu


label ch3_question_menu:

    menu:

        "Did your mom bring you here?" if not ch3_asked_mom:
            $ ch3_asked_mom = True
            "I remember Ekaterina telling me that she brought Elias here as the spirit. I'm curious. How did she bring him here?"

            show dorian normal_alt_neutral at left_char with Dissolve(0.2)
            dorian "Did your mom bring you here?"

            show elias first_meet_neutral at right_elias with Dissolve(0.2)
            "Elias paused, his cheeks stuffed like a chipmunk's. He swallowed loudly before mumbling."

            elias "Uh-huh. Mommy say... um... stay here, an'... an' don't open da door... 'cause... 'cause bad mans come in an'—"

            "He stuffed another piece of fruit into his mouth mid-sentence, mumbling through it"

            show elias first_meet_sad at right_elias
            elias "An' Mama say... no cry, 'cause... 'cause Mommy's gonna be back. But she not..."

            "His little face scrunched up in thought, and he trailed off, licking his fingers again."

            show dorian normal_alt_neutral at left_char
            dorian "Well… I'm not getting any answers from you, am I?"
            show elias first_meet_neutral at right_elias
            elias  "Um… Huh?"

            jump ch3_question_menu

        "What's that amulet you're wearing?" if not ch3_asked_amulet:
            $ ch3_asked_amulet = True

            show dorian normal_alt_neutral at left_char
            dorian "What's that amulet you're wearing?"

            show elias first_meet_neutral at right_elias
            "At this, Elias froze. His sticky hands darted to the amulet, clutching it protectively."

            elias "This? They Mommy say... uh... um... Mommy say, don't give it! Don't give it to bad guys. No, no, no!"

            "He shook his head so hard his hair flopped around."

            elias "She say... it's... uh... it's super 'portant! Like... magic, or somethin'…"

            "He blinked at me, then tilted his head."

            show elias first_meet_sad at right_elias
            elias  "Are you a bad guy, mister?"
            show dorian smile at left_char
            dorian "What do you think? I opened the jar for you, didn't I?"

            "Elias squinted at me suspiciously before shoving another chunk of fruit into his mouth."

            show elias first_meet_happy at right_elias
            elias "Okay. I believe you, mister."

            jump ch3_question_menu

        "Who are those people frozen at the entrance?" if not ch3_asked_bodies:
            $ ch3_asked_bodies = True

            show dorian neutral at left_char
            "I gestured toward the cave entrance, where the bodies I had seen earlier were frozen."

            dorian "Who are those guys? The ones outside?"

            show elias first_meet_neutral at right_elias
            "Elias glanced toward the entrance, his expression scrunching up."

            elias "The bad guys… and they make Mommy go WHOOSH!"

            "He threw his arms up, making a dramatic gusting sound."

            show elias first_meet_happy at right_elias
            elias "And they go... um... like statues. Mommy say, 'Leave!' An' dey didn't... so, um, they go 'brrrrrrrrrr!'"

            "He shivered for emphasis, then giggled, poking at the jar."

            elias  "They're not scary, mister. Mommy's scarier!"
            show dorian neutral at left_char
            dorian "I can imagine."

            jump ch3_question_menu

        "I'm done asking questions for now.":

            show elias first_meet_happy at right_elias with Dissolve(0.2)
            elias "Okay! You ask lotsa stuffs, mister. I like da fruit. Got more?"

            show dorian neutral at left_char
            "I sighed, grabbing the cloth again."

            dorian "First, let's clean you up — again."

            hide elias
            jump ch3_blizzard_trapped


# =============================================================================
# SECTION 10: LABEL CH3_BLIZZARD_TRAPPED — Blizzard Days in the Shack
# =============================================================================
# Days pass. Dorian refuses to bond with Elias — until the Tedda moment breaks him.
# The family farewell dream. Elias calls Dorian "daddy" for the first time.
# =============================================================================
label ch3_blizzard_trapped:
    scene frostcradle_cabin_on with fade
    show dorian neutral at left_char with Dissolve(0.2)
    "The roar of the blizzard outside echoed loudly through the mining cave."
    "I wiped his face gently again, making his tiny face and little fingers spotless."

    "Then my stomach growled — how long it had been since my last meal? Hours? Half a day. I was starving."

    dorian "Kid, is there any food in here?"
    show elias first_meet_neutral at right_elias with Dissolve(0.2)
    "The toddler looked up from where he was fiddling with the now-empty jar. He pointed a finger toward the corner."

    elias "Uhhh... um... fishies over there, mister! An' veggies... Mommy say dey for soup. But I don't know how."
    hide elias
    hide dorian

    "I followed his gesture and found what he meant."
    "A pile of provisions—ice-cold fish wrapped in rough parchment, some frozen vegetables that looked like they'd been pulled straight from the fields, and a sack of rice."
    "I knelt down, inspecting the fish. They were Tianho white-scaled fish, a staple back in Tianho."
    "Small, delicate, with soft, flaky flesh that absorbed flavor well."
    "My mother used to cook these when I was a kid. I'd picked up the recipe and made it my own over the years."
    "I gathered the ingredients, setting them near the small cooking pit in the shack. The fire was low but steady, enough to get the job done"
    "Elias trailed behind me as I walk around the shack, clutching the edge of his blanket like a cape."
    "I began to chop the ingredients but I noticed his eyes not leaving me. I glanced back at him"

    show dorian normal_alt_neutral at left_char with Dissolve(0.2)
    dorian "*sighs* I'm going to cook some stew. Want some?"

    show elias first_meet_happy at right_elias with Dissolve(0.2)
    "Elias's face lit up, and he nodded eagerly."
    elias "Y-Yes. I'm hungry too, mister!"

    "I glanced at the empty fruit jar he'd polished off minutes ago and sighed, shaking my head."
    "Elias plopped down near the fire, watching intently as I worked. His eyes followed every movement as I gutted the fish with practiced ease, scaling it and slicing the flesh into even chunks."
    "I tossed the fish bones into a pot of water to make a light stock, adding a handful of the frozen vegetables. As the pot warmed, the delicate aroma of the white-scaled fish started to fill the shack."
    "I rinsed some rice and added it to the stew, letting it thicken as it simmered. A few pinches of salt and a small pouch of dried Tianho herbs from the provisions completed the dish."
    "Elias inched closer, his eyes wide and curious."

    show elias first_meet_happy at right_elias with Dissolve(0.2)
    elias "It smells soooo good. Like... um... like happy smells!"

    show dorian normal_alt_neutral at left_char with Dissolve(0.2)
    dorian "Happy smells?"

    "He nodded, his hair flopping over his forehead."

    elias "Uh-huh! Mommy makes somethin' like dat sometimes. But this smells better... I think."

    show dorian normal_alt_calm at left_char
    dorian "You haven't even tasted it yet. Sit tight—it'll be ready soon."

    "I smirked, ladling the finished stew into a couple of old wooden bowls I'd found among the shack's scattered supplies."
    "The fish had cooked perfectly, tender and flaky, the broth rich with the sweetness of the vegetables and the faint, salty tang of the kelp."

    show dorian normal_alt_neutral at left_char
    dorian "Here. Don't spill it."

    show elias first_meet_happy at right_elias
    "I handed him a bowl, and he cradled it carefully, blowing on it."
    "Elias took a cautious sip, then let out a happy hum, his legs kicking excitedly."

    elias "Mmm! It's hot... but it's yummy! You're a good cooker!"

    show dorian smile at left_char
    dorian "It's cook, not cooker."

    "I rolled my eyes, taking a sip of my own bowl. The stew was simple, hearty, and exactly what I needed."
    "Elias slurped his stew loudly, swinging his legs as he ate."
    "I finished my bowl quickly, setting it down as I glanced at Elias. He was still swinging his legs and slurping away at the stew."
    "I stood up."

    show dorian neutral at left_char
    dorian "Stay here, kid. I'll be right back."

    hide elias
    hide dorian

    "Elias barely acknowledged me, too absorbed in savoring every bite of his stew. I shook my head and stepped toward the entrance of the shack, the sound of the blizzard growing louder with every step."

    scene frostcradle_blizzard with dissolve
    show snow_blizzard_1

    "Pushing open the rough wooden door, I made my way to the mining entrance. The icy wind hit me like a wall, cutting through my cloak and stinging my face."
    "Snow swirled violently, making it impossible to see more than a few feet ahead."
    "I stepped out into the biting cold, my cloak whipping behind me, and the snow biting at my exposed skin."
    "The blizzard wasn't letting up anytime soon, and the queen was right about one thing: it was nearly impassable."
    "For a normal person that is."
    "I sighed, staring into the swirling mass of white. If I didn't get Elias out of here soon, we'd be stuck here for who knows how long."
    "The sooner I could get him to King Gustav, the better."

    elara "You know what Gustav will do to that child."

    show dorian normal_alt_annoyed at left_char with Dissolve(0.2)
    "I clenched my fists, my jaw tightening."

    show dorian serious at left_char
    dorian "It's a bounty, my heart. You know how bounties work."

    elara "Well then, why did you accept it?"
    dorian "Nobody told me that the target was a toddler. How in Tetrad's name was I supposed to know?"
    elara "You've seen Mjoll. You've seen how they treat the aldoriths. You know what Gustav will do to that child if he gets a hold of him."

    show dorian normal_alt_calm at left_char
    dorian "It's not my decision. It's not my place. The task was to kill him, Elara. I didn't... I couldn't. So maybe bringing him to Gustav is the compromise."

    "Even as I said the words, they tasted bitter."
    show dorian serious at left_char

    elara "A compromise? You think handing a defenseless child over to that monster is a compromise? You've seen what he does to people, Dorian. To innocents. What makes you think this boy will be any different?"

    show dorian sad at left_char
    dorian "I'm not a savior, Elara. I never was. I… wasn't strong enough to save you… and the kids."
    dorian "I'm a mercenary now. I've killed, I've followed orders, and I've done what needed to be done. This isn't—"
    elara "This isn't who you are. I know you've buried the man you used to be under all that guilt, but I know he's still there. And you know it too, or that boy would already be dead."

    show dorian serious at left_char
    dorian "Once the blizzard stops, I'm giving the boy to King Gustav. I'm a man of my word. I'm paid to do so."

    "The wind hit me with a sharp gust, biting through my cloak and sending a shiver down my spine."

    elara "*sigh* I understand, my heart."

    "I stood there for a long moment, the blizzard howling in my ears. If I didn't bring Elias to Gustav, where would I take him? What could I do for him?"
    "I was a mercenary. I did jobs. And I was paid to do this one."
    "I turned back, the blizzard still raging, and saw Elias standing behind me. He was wrapped in a blanket, his small form barely visible through the snow and cold."

    show elias first_meet_neutral at right_elias with Dissolve(0.2)

    elias "Hello, mister. Who are you talking to?"

    show dorian neutral at left_char
    "I blinked, momentarily caught off guard by his question."

    dorian "What are you doing here? I thought I told you to stay put."

    "I let out a long breath and turned back toward the shack, trying to push the weight of my thoughts aside."

    dorian "Come on. Let's head back, Elias."

    hide dorian
    hide elias

    scene frostcradle_cabin_on with dissolve

    "A couple of days passed. The blizzard showed no sign of letting up. The storm had trapped us here, together."
    "I didn't speak to Elias. Not once."
    "He tried, of course. In his small, curious voice, he'd ask questions. 'Why is it so cold?' or 'What's your favorite food?'"
    "I ignored them all. It was easier that way."
    "I cooked for him—simple meals of dried meats and whatever else I could scrape together—but I never sat with him."
    "Never looked at him longer than I had to. I told myself it was better this way. No attachments. No guilt."
    "When the storm passed, I would take him to King Gustav, collect my bounty, and move on."
    "That's how it had to be."
    "Until the morning I woke up to the sound of soft giggles."

    show elias first_meet_happy at right_elias with Dissolve(0.2)

    "I blinked groggily, the cold air biting at my face as I sat up. My eyes landed on Elias, sitting cross-legged on the floor with something clutched tightly in his hands."
    "It took me a second to realize what it was."
    "Tedda."

    show dorian sad at left_char with Dissolve(0.2)
    "My chest tightened. That was my gift for Sarah for her birthday. And now another child is holding it."
    show dorian serious at left_char
    dorian "That's for Sarah. Put that down."

    show elias first_meet_crying at right_elias
    "Elias froze, his wide eyes looking up at me, startled and afraid. He clutched Tedda tighter, his little fingers curling around the bear as if it might protect him."

    elias "I… I'm sorry, mister. I-I—"

    show dorian angry at left_char
    dorian "I said put it down."

    hide elias
    "He flinched at the harshness of my tone, his bottom lip trembling. Slowly, he placed the teddy bear on the floor and backed away, his small frame shrinking under my glare."
    "I bent down, picking up Tedda. My hands brushed off invisible dust as if I could somehow erase the fact that someone else had touched it. My fingers trembled, and I hated that they did."
    "Behind me, I heard the faint sound of a sniffle."

    show elias first_meet_sad at right_elias with Dissolve(0.2)

    elias "I'm sorry, mister. I didn't mean to make you mad."

    show dorian sad at left_char
    "I stood there, staring down at the bear in my hands."

    dorian "This bear's name is Tedda. This was for Sarah. My daughter."

    "There was a long silence. I wasn't sure why I said it. Maybe I thought it would make him understand. Maybe I just needed to say her name."

    dorian "She's not here anymore. I'm her dad… and everything I do is to protect her."

    show elias first_meet_sad at right_elias
    "Elias looked down at his lap, his small hands fiddling with the edge of his blanket."

    elias "I… I wish I had a daddy…"

    show dorian serious at left_char
    "His words hit me like a blow. I stared at him, stunned, as he looked away, his shoulders trembling."

    show elias first_meet_crying at right_elias
    elias "*sniffling* My daddy doesn't love me. He… he wants me dead."

    "I was shocked. I didn't know that he knew King Gustav wanted him dead."

    elias "Mommy saved me… from him. She kept me safe. But now she's…"

    "His voice cracked, and tears spilled down his cheeks."

    elias "…gone too."

    hide elias with Dissolve(0.2)
    "He buried his face in the blanket, his small body shaking with silent sobs. I stood there, frozen, clutching Tedda in my hands."
    "I stood there for a moment, staring down at Elias as he cried softly into his blanket. My grip on Tedda loosened, and before I could stop myself, I knelt beside him, holding out the bear."

    show dorian neutral at left_char
    dorian "Here."

    show elias first_meet_neutral at right_elias with Dissolve(0.2)
    "Elias peeked up at me, his tear-streaked face glowing with surprise. His small hands hesitated for a moment before gently taking Tedda from me."
    "He hugged the bear tightly, his tiny fingers curling into its soft fabric."

    show dorian smile at left_char
    dorian "If Tedda will make you happy, you can have her."
    show dorian normal at left_char

    show elias first_meet_happy at right_elias
    elias "T-Thank you, mister."

    "I thought that would be it. That maybe he'd cry himself to sleep, curled around Tedda the way she used to. But then Elias reached out with both arms and threw them around my neck."
    hide elias
    hide dorian
    scene cg_dorian_hug_elias with fade
    "He hugged me."
    "His small arms clung to me with all the strength in his tiny body, desperate and shaking, like he was afraid I'd vanish if he let go."

    elias "Mommy told me in a dweam. She's gone… She won't be come back…"

    "I didn't answer."
    "Didn't have the words."
    "So I just held him."
    "He didn't speak again. Neither did I."
    "Only the sound of the blizzard filled the silence—soft and endless."
    "And for a long time, we stayed like that."

    elias "Thank you, mister."

    "I opened my mouth to respond, but before I could, a faint whirring sound cut through the silence. It grew louder, and I turned toward the noise."
    "Then I saw it—something rolling toward the shack's entrance, its small frame navigating the uneven ground with mechanical precision."

    scene frostcradle_cabin_on with fade
    show dorian neutral at left_char
    show elias first_meet_neutral at right_elias
    with Dissolve(0.2)
    "A bot - a little taller than a man, metallic and polished, with a rectangular chest and mechanical arms designed to lift heavy objects."
    jump ch3_yuxuan_arrives

# =============================================================================
# SECTION 11: LABEL CH3_YUXUAN_ARRIVES — Supply Bot / Hologram Scene
# =============================================================================
# The Cheng Industries supply bot rolls in. Yuxuan's hologram activates.
# Dorian tells Yuxuan everything about Ekaterina and Elias.
# Magnus vision interrupts — Dorian collapses. Elias saves him.
# The family farewell dream.
# =============================================================================
label ch3_yuxuan_arrives:
    "Elias gasped, clutching Tedda tighter as he broke our hug and moved closer to get a look."

    show elias first_meet_sad at right_elias 
    elias "What's that? Is it alive?"
    show dorian normal_alt_neutral at left_char
    dorian "No, it's not alive. It's a supply bot. Made by Cheng Industries."
    show elias first_meet_neutral at right_elias
    elias "A suh-ply bot?"
    "The bot's sensors glowed softly as it paused."
    show supply_robot normal at center_supply with Dissolve(0.2)
    # play music ost_supply_bot_jingle fadein 0.5       # PLACEHOLDER

    "- Here at Cheng's, we bring change…"

    # stop music fadeout 1.5
    "An oddly soothing, yet out of tune jingle filled the cave over and over again. I grimaced, resisting the urge to roll my eyes."
    "Elias, on the other hand, was utterly entranced. His wide eyes followed the bot's every movement as it rolled to a stop in front of us. He hugged Tedda."

    show elias first_meet_happy at right_elias
    elias "It sings, mister! It's so cute!"

    "As the jingle faded, a soft hum emanated from the bot. A hologram flickered to life above its chest."
    # show yuxuan hologram at left_char          # PLACEHOLDER — Yuxuan hologram sprite
    show supply_robot base at center_supply 
    yuxuan "Praise the Prosperity Dragon! Dorian, I'm so happy to see you again!"

    show dorian normal_alt_neutral at left_char
    "I blinked, caught off guard. I awkwardly forced a smile, though I didn't remember his face at all. I only remembered writing him a letter."

    dorian "Nice to meet you again, Yuxuan."
    "He didn't seem to notice my hesitation as he continued, his voice bright and enthusiastic."
    show supply_robot normal at center_supply 
    yuxuan "I got your letter! The messenger you gave it to dropped it off at the post office, and thankfully we had a bot there! So I read it from the comfort of my home. Hehe, I wasn't expecting you to reach out, but I'm glad you did!"
    yuxuan "So, I hijacked one of our bots already en route to Mjoll and had it rerouted here."
    "The bot turned around and opened a compartment on its chest to reveal a neatly organized cache of goods: dried meats, vegetables, warm blankets, fire-starting kits, and even a few luxury items like hot drink packets and a sealed tin of sweets."

    yuxuan "The blizzard's getting worse, so I thought you'd appreciate a little extra help. Everything in here is yours — no charge, of course."
    "Elias' eyes widened, his eyes sparkled as he stared at the supplies"

    show elias first_meet_happy at right_elias
    elias "Mister, look! It's got food! And bwankets! And… and CANDIES!"

    "He tugged at my sleeve eagerly, practically bouncing on the spot."

    dorian "T-Thanks, Yuxuan. You didn't have to go out of your way."

    "Yuxuan waves a hand dismissively."
    show supply_robot base at center_supply
    yuxuan "Nonsense! You saved my hide back in Tianho, remember? Consider this payback."

    show elias first_meet_happy at right_elias
    elias "Wow, there's so many TWEATS! Tedda, look! Tweats just for us!"

    "Elias practically squealed as he reached for the tin of sweets, clutching Tedda in one arm while fumbling to open the packaging with the other."
    "Before I could stop him, he scurried off to a corner of the shack, clutching the tin and laughing gleefully."
    hide elias
    show supply_robot base at right_supply
    with Dissolve(0.2)

    show dorian normal_alt_annoyed at left_char
    dorian "Hey — we haven't had a proper meal, first!"

    "I groaned inwardly as Yuxuan chuckled through the hologram."

    yuxuan "Wait… Who's Tedda? Is there another person here? I can hijack another bot to make sure we get enough supplies-"
    show dorian neutral at left_char
    dorian "That's just the knit doll with the missing eye."
    show supply_robot normal at right_supply
    yuxuan "Oh… I thought it was another person. Anyway, Dorian…"
    yuxuan "I-I'm sorry if this seems abrupt, but it's so good to finally meet you. Well, not really 'meet.' More like… uh… see your face. Not face-to-face, but face-to-bot? I mean, I see your face, but you can't see mine. Heh."
    show dorian normal_alt_annoyed at left_char
    "I raised an eyebrow, unsure how to respond."
    show dorian normal_alt_neutral at left_char
    dorian "Um… thanks, Yuxuan. I'm happy to see you too. I really appreciate all of this."
    yuxuan "Ahem! Right, so… Have you, uh… handled the situation yet?"
    show supply_robot lied at right_supply
    dorian "What situation?"
    yuxuan "Have you killed the Prince? The one who murdered the Queen. You know, to stop the blizzard? The people in Mjoll are going haywire. They're barely surviving out there."
    yuxuan "King Gustav upped the bounty. He already tripled it."

    "The question hung heavily in the air. I took a deep breath and pointed to the corner."

    show dorian serious at left_char
    dorian "You're looking at him."

    "Yuxuan's holographic face froze mid-smile, his mouth dropping open as his gaze followed my hand to Elias."
    "The toddler was sitting cross-legged, happily stuffing candies into his mouth while making Tedda 'dance' beside him."

    elias "*giggling* Tedda says, 'Candy is the best thing ever!' Right, Tedda?"
    tedda "..."
    show supply_robot sad at right_supply
    yuxuan "W-WHAT?! That's… that's the Prince?!"
    show supply_robot normal at right_supply
    
    show dorian normal_alt_neutral at left_char
    "I crossed my arms and nodded."

    yuxuan "I… I'm confused. By the way they described what he did, I thought the Prince would be… older. At least of age! Not…"
    "He gestured toward Elias, who was now attempting to stack candies into a precarious little tower on Tedda's lap."

    show dorian sad at left_char
    "I sighed, the weight of everything pressing on my chest. Yuxuan might not have the full picture, but he deserved to know."
    "Elara and the kids were the ones who pushed me to write to him, after all. If they trusted him, maybe I should too."
    show dorian serious at left_char
    "Taking a deep breath, I leaned closer to the hologram."
    "I told Yuxuan everything. How Queen Ekaterina became the frost spirit Yuki-onna and that she's the one who caused the blizzard, not Elias."

    "Yuxuan's expression softened with horror and sympathy as he absorbed the information."
    show supply_robot sad at right_supply
    yuxuan "Heavens. Prosperity Dragon save Her Majesty's soul. That's too tragic!"
    yuxuan "And even King Gustav and Count Vasily want him dead…"
    "I nodded grimly, my jaw tightening."
    
    show dorian neutral at left_char
    dorian "Yeah. Kid's got it rough."
    "Yuxuan looked down for a moment, shaking his head."
    show supply_robot normal at right_supply
    yuxuan "But… what do you plan to do, Dorian? You can't exactly just…"

    "I stiffened. His words trailed off, leaving the question lingering in the air. What was I going to do?"
    show dorian sad at left_char
    dorian "I don't know…"

    "Yuxuan tilted his head, his brows furrowed with concern, but I quickly straightened."
    hide supply_robot
    show elias first_meet_happy at right_elias
    with Dissolve(0.2)
    
    show dorian normal_alt_neutral at left_char
    dorian "C'mon, Elias. I'll cook you up something proper before you finish half of that candy."
    "Elias perked up, his face lighting up as he scrambled to his feet, clutching Tedda with one hand and the candy tin with the other."
    elias "Okay, mister."
    hide elias
    show dorian normal_alt_tense at left_char 
    "I started toward the makeshift cooking area, but before I could take another step, a sharp pain pierced through my head like a hot blade."
    "My knees buckled, and the room tilted. My vision blurred."

    # -------------------------------------------------------------------------
    # MAGNUS VISION INTERRUPTS
    # -------------------------------------------------------------------------

    scene plain_white with shock_cut
    # play sound sfx_amulet_surge                       # PLACEHOLDER

    show magnus normal at center_char, dream_haze
    magnus "Come to Tianho, Dragonkin…"
    "His words echoed in my mind."
    magnus "My power flows through you now. Only you can open the…"
    "The vision flickered, the figure growing hazy, as if struggling to maintain form. His voice cracked, filled with desperation."

    magnus "Hurry… please…"

    scene black with shock_cut
    
    "And then, darkness."
    "I hit the ground hard, my body trembling as icy tendrils of pain radiated through my chest."
    "I vaguely heard Elias scream, his voice high-pitched and panicked."

    scene frostcradle_cabin_on with fade
    show supply_robot lied at left_supply 
    show elias first_meet_crying at right_elias
    with Dissolve(0.2)
    elias "Mister! Mister, wake up! What's wrong?"

    yuxuan "Dorian?! What happened?!"

    "I barely managed to lift my head, my breaths shallow and labored"
    dorian "I… don't know…"
    "My vision swam, and I felt myself slipping again. My power surged uncontrollably, the air around me flickering with faint embers."

    yuxuan "Elias, listen to me! You have to help him. The bot can't administer aid—it's not designed for that. Only you can do this!"
    elias "Umm… okay. But I don't know how!"

    scene black with dissolve
    "Everything went black."

    yuxuan "Stay calm! First, you… um… need to… You need to… Prosperity Dragon save us… Where's a doctor when you need him?"

    "Elias sniffled, crawling closer to me as I lay slumped against the wall. I felt his tiny hands on my face, shaking me gently."

    elias "Mister? Please wake up! Please don't leave me!"
    yuxuan "Elias, tilt - I mean move his head back a little—yes, like that. Good. Is he breathing?"
    yuxuan "Alright. Now, look at his chest. Do you see the sparks? That's his power. It's surging out of control. You need to calm him down."
    elias "H-How?"

    yuxuan "Hold his hand. Talk to him. Sometimes, power responds to emotion. Tell him he's safe, that you're here. It might help ground him."
    "I felt Elias' small hand trembling as he reached for mine. His fingers wrapped around mine tightly, and he pressed his forehead against my arm."
    elias "Mister… please don't leave. I'll be good, I promise. I'll share all my candies with you and Tedda! Just… don't go."
    "His voice broke into soft sobs as he clung to me."
    
    yuxuan "Elias, the necklace! It's reacting to him. Take it off and give it to him—quickly!"
    elias "O-Okay..."

    "I felt the weight of the amulet as Elias placed it on my chest. The energy around me shifted immediately, the chaotic sparks focusing, centering. The overwhelming heat dimmed."
    "A familiar voice echoed in my mind, low and resonant."

    magnus "Yes… Yes…"

    "And then everything went black."

    # -------------------------------------------------------------------------
    # FAMILY FAREWELL DREAM
    # -------------------------------------------------------------------------

    scene plain_white with fade

    elara  "Dorian… my heart."

    "I turned to see her, standing with Daniel, Sarah, Emily, and Lucas. They smiled at me, their faces serene."

    scene cg_family_into_light with Dissolve (0.9)
    daniel "Goodbye, Dad. It's time for us to go."
    sarah  "You don't need us anymore, Dad. You're strong now."
    emily  "We'll always be with you, in your heart."
    lucas  "Until we meet again, Dad."

    "Tears blurred my vision, but I couldn't bring myself to move or speak."

    dorian "D-Don't go…"

    "Elara stayed behind as the children faded into the light. She walked toward me, her hand brushing against my cheek."

    elara "I'll miss you, my heart. But Ena needs you. Our mission here is done."
    "Needs me? What?"
    "Her eyes shimmered with unshed tears, but her smile was soft, accepting."
    elara "Go, my heart. Ena is counting on you."
    elara "Until we meet again."

    "The warmth of her touch lingered as she, too, faded into the golden light."

    scene cg_blindinglight with Dissolve(0.5)

    dorian "No!!"

    scene frostcradle_cabin_on with fade

    "I woke with tears streaming down my face, my body trembling."
    "The faint glow of the fire in the corner cast long shadows across the walls."
    "Then I felt it — a small, warm body pressed tightly against mine."
    "Elias was curled up beside me, his tiny arms wrapped around my torso, clutching me. Tedda was squished between us."
    "As I wept silently, trying to hold in the sobs that threatened to escape, Elias stirred, mumbling softly in his sleep"

    show elias first_meet_neutral at right_elias with Dissolve(0.2)
    "As I wept silently, Elias stirred, mumbling softly in his sleep."

    elias "Please don't take Daddy away…"

    show dorian sad at left_char with Dissolve(0.2)
    "My heart broke all over again. His words cut deeper than any blade ever could, and before I knew it, I found myself holding him close, resting my chin on his soft hair."
    "The quiet hum of the bot had ceased—Yuxuan must have powered it down to give us peace."
    "The only sounds were the crackling of the fire and Elias' soft breathing"

    dorian "*crying*"
    "And as the firelight flickered, I held onto him."

    hide dorian
    hide elias

    scene black with fade
    pause 2.0

    jump ch3_mushroom


# =============================================================================
# SECTION 12: LABEL CH3_MUSHROOM — D6: Yuxuan Mushroom Invitation
# =============================================================================
# Morning after the dream. Yuxuan spots Blisscap mushrooms nearby.
# D6: Join Yuxuan (++yuxuan_affection) or Don't Join (-yuxuan_affection).
# Both paths converge on D7 the cooking choice.
# =============================================================================
label ch3_mushroom:
    # play music ost_blizzard_days fadein 2.0           # PLACEHOLDER
    scene frostcradle_cabin_on with Dissolve(0.9)

    show dorian neutral at left_char with Dissolve(0.2)

    "The next morning, I woke up early."
    "The fire had burned low, casting faint embers onto the cold stone floor. Elias was still asleep, his small body curled tightly around Tedda, his face peaceful in the glow of the dying flames."
    "Despite the relentless blizzard outside, the small space inside the cave—our sanctuary—felt surprisingly cozy. I could hear the faint howl of the wind echoing beyond the cave walls."
    "The blizzard was still there - howling louder than ever."

    "I found that I was wearing the amulet Elias was previously wearing. Oddly enough, it stopped glowing. I stood up, removed it and placed it on a small table."
    "A soft whirring sound made me glance toward the corner where Yuxuan's bot had been powered down."
    "For some reason, it's still here. It came to life with a low hum, the hologram of Yuxuan flickering into existence above it."

    show supply_robot base at right_supply with Dissolve(0.2)
    yuxuan "Good morning, Dorian!"

    show dorian normal_alt_neutral at left_char
    dorian "Morning, Yuxuan. You're up early."

    show supply_robot normal at right_supply with Dissolve(0.2)
    yuxuan "I never really sleep much. Or even eat. Too many projects to think about, you know? But… that's not what I called."
    yuxuan "You're not going to believe this, but there's a rare mushroom growing just outside the shack! I spotted it on the bot's scanners earlier."
    yuxuan "It's called a Blisscap. They only grow here in Mjoll, and their taste? Oh, it's incredible — earthy, with just a hint of sweetness. It'd be perfect for breakfast."

    "I raised an eyebrow."

    dorian "Really? Is it edible?"
    yuxuan "Completely! Trust me, I wouldn't suggest it if it weren't."

    "I paused, glancing at the pot and then toward Elias."
    "The thought of fresh ingredients was tempting, but the idea of going out there, given that I just fainted lately, even just to the edge of the shack, wasn't particularly appealing."
    
    show supply_robot base at right_supply with Dissolve(0.2)
    yuxuan "It's just outside, Dorian. Still inside the cave, so the blizzard won't get in the way. I could guide you to it, you know, if you're up for it. Please?"
    
    "His smile lingered a little longer than it needed to, and for a moment, I found myself considering it—not just the mushroom, but the chance to step out of the shack with him, even if only for a moment."

    menu:

        "Join Yuxuan.":
            $ ch3_d6 = "joined"
            $ yuxuan_affection += 1
            
            "I stood, brushing off my hands."

            show dorian neutral at left_char
            dorian "Alright, Yuxuan. Show me where it is."

            "His holographic face lit up with delight."

            yuxuan "Great! Follow the bot, and I'll guide you."
            "The bot whirred to life, leading the way to the edge of the shack."

            scene bg_frostcradle_cave with fade 

            "As I stepped outside, the air in the cave was cooler, but it wasn't unbearable."
            "The sound of the blizzard was muffled, leaving only the soft echoes of our footsteps and the hum of the bot."
            "Yuxuan's hologram flickered as he pointed toward a faint patch of glowing blue mushrooms near the cave wall."

            show supply_robot base at right_supply
            show dorian neutral at left_char
            with Dissolve(0.2)
            yuxuan "There. Aren't they beautiful? The glow is caused by a natural compound in their spores. It's harmless, I promise."
            "I crouched down, gently plucking a few of the mushrooms."

            yuxuan "You know… seeing you here, alive, after everything in Tianho — it's, um… it's really nice. I never got to say thank you. For what you did."
            "I glanced at his hologram, caught off guard by the sincerity in his tone."

            show dorian neutral at left_char
            dorian "You don't owe me anything, Yuxuan."

            show supply_robot normal at right_supply
            yuxuan "Maybe not. But that doesn't mean I'm not grateful. You didn't have to save me back then, but you did. And… it meant a lot."
            yuxuan "I… I'm just so happy I finally get to meet you again. You were my hero, you know? Still are."
            show supply_robot base at right_supply

            "He paused, his holographic image flickering faintly."

            yuxuan "Paladin Dorian Burnham. The Dragon of Gale. I never forgot your name."

            show dorian sad at left_char
            "The title felt foreign now, like it belonged to someone else entirely. I looked down, the faint glow of the mushrooms catching the edge of my hand."
            "Paladin Dorian. The Dragon of Gale. Am I even worth that title anymore?"
            dorian "I'm just a mercenary now, Yuxuan. I'm not a paladin anymore. I resigned years ago. That man you remember? I apologize. But he's gone."


            "The silence that followed was almost unbearable."

            yuxuan "Maybe you've changed. Maybe you've been through things that I can't even imagine. But you're still the man who saved me. You're still him."

            "There was a pause, the air between us heavy with unspoken words. I didn't know what to say, so I just nodded, turning back to the mushrooms."
            "When I stood, the bot handed me a small container to carry them in. I placed the glowing mushrooms inside, sealing it."
            
            yuxuan "Thanks for humoring me. I, uh… I hope breakfast turns out great."
            "For a moment, his hologram lingered, his gaze soft, almost hesitant."

            show dorian neutral at left_char
            dorian "It will. Thanks to you, Yuxuan."

            # back to shack

        "Don't join.":
            $ ch3_d6 = "skipped"
            $ yuxuan_affection -= 1

            "I shook my head, turning back to the pot."

            show dorian normal_alt_annoyed at left_char
            dorian "Thanks, but I'll pass. I've already got breakfast going."

            "Yuxuan's hologram faltered slightly, but he recovered quickly."
            show supply_robot sad at right_supply
            yuxuan "Of course. No problem. I just thought… well, never mind. If you change your mind, the bot will be here."

            show dorian neutral at left_char
            "He gave a faint smile."
            dorian "Appreciate it, Yuxuan. But I think I'll stick with what we've got for now."
            
            yuxuan "Understood. Well, if you need anything else, just let me know."

            "With that, the hologram flickered off."
            hide supply_robot
            "A few minutes later, Yuxuan's bot returned, its mechanical arms extending to offer me a small container filled with glowing Blisscap mushrooms."

            show supply_robot base at right_supply
            yuxuan "Here you go. Breakfast is on me. Well, technically on the cave, but you get the idea."

            show dorian neutral at left_char
            dorian "Thank you, Yuxuan."

    hide yuxuan
    hide supply_robot
    jump ch3_breakfast

# =============================================================================
# SECTION 13: LABEL CH3_BREAKFAST — D7: Cooking Choice (4 Soft Branches)
# =============================================================================
# Four breakfast options. No stat effect — purely flavour.
# All converge on Elias waking up and calling Dorian "daddy" for the first time.
# =============================================================================
label ch3_breakfast:

    show dorian normal_alt_neutral at left_char with Dissolve(0.2)
    "I moved to the fireplace, spreading the ingredients out on a makeshift wooden counter."
    "My hands hovered over the modest selection: a couple of golden fish, a white-scaled fish fillet, some string beans, a handful of other vegetables, and the glowing Blisscaps."
    
    dorian "Alright. Let's see what we can do with this."
    "The bot hovered near me, its singular lens observing as I deliberated."
    menu:

        "Golden Fish Omelette.":
            $ ch3_d7 = "omelette"

            "I decided to make a Golden Fish Omelette for us."
            "I cracked the eggs into a bowl, whisking them with a pinch of salt and a sprinkle of dried herbs Yuxuan swore wouldn't kill us."
            "I sliced thin pieces of golden fish and added them to the mix, along with a small handful of finely chopped Blisscaps for flavor."
            "The bot chimed in as I poured the mixture into the pan."

            show supply_robot normal at right_supply with Dissolve(0.2)
            yuxuan "C-Careful, Dorian! Don't let it stick to the pan. Maybe a bit more oil?"
            show dorian normal_alt_annoyed at left_char
            dorian "I know how to cook, you know."
            show dorian normal_alt_neutral at left_char

            "I frowned, adding a touch more oil as the edges began to crisp."
            "I folded the omelet in half, the golden fish glinting faintly against the soft yellow of the eggs."
            # TODO: show food 6
            "The result was decent—it looked nice! Yuxuan made me add a little herbs. “For garnishing”, he said."

        "Hearty White-Scaled Fish and Vegetable Soup.":
            $ ch3_d7 = "soup"

            "I decided to make soup with vegetables and some white-scaled fish."
            "I tossed the white-scaled fish into a pot of water, letting it simmer as I added diced vegetables-carrots, onions, and string beans. Healthy for growing little kids like Elias."
            show supply_robot normal at right_supply with Dissolve(0.2)
            yuxuan "Uh… maybe add some salt? It looks a little bland."

            show dorian normal_alt_neutral at left_char
            "I sprinkled in a pinch, tasting the broth with a wooden spoon."
            "It wasn't bad, but it lacked something."

            dorian "Maybe some dried herbs…"
            # TODO: show food 7
            "The bot handed me a small pouch of spices, and I added a pinch of dried basil. The soup took on a richer aroma, the fish's natural oils blending with the vegetables."


        "Pan-Fried Golden Fish with Scrambled Blisscaps and Veggies.":
            $ ch3_d7 = "fried"

            "I decided to just pan-fry the Golden Fish and some vegetables."
            "I seasoned the golden fish with salt and pepper, frying it in a pan until the skin was crispy and golden brown."
            "Meanwhile, I sautéed the Blisscaps and vegetables in a separate pan, their earthy aroma mixing with the fish."

            show supply_robot normal at right_supply with Dissolve(0.2)
            
            yuxuan "D-Dorian! You're burning the veggies!"
            show dorian neutral at left_char
            dorian "Dragon's bollocks! *grumbling*"
            # TODO: show food 8

            "The bot beeped. I plated the fish on a bed of the sautéed Blisscaps and veggies, adding a small garnish of string bean slices for color."

        "String-Bean and White-Scaled Fish Fried Rice.":
            $ ch3_d7 = "rice"

            "I decided to make some fried rice with some string beans and white-scaled fish."
            "I chopped the white-scaled fish into small pieces, stir-frying it with cooked rice, chopped string beans, and a handful of diced vegetables. The Blisscaps added a faint glow as I mixed them in."

            show supply_robot normal at right_supply with Dissolve(0.2)
            yuxuan "A little soy sauce might help."
            show dorian normal_alt_neutral at left_char
            dorian "We… don't have soy sauce. Oh — sorry. We have some."

            "I splashed in a small amount, the rice taking on a richer, darker hue."
            "The bot handed me a spoon to taste, its lens watching expectantly."
            "Not bad."

            # TODO: add food 9

            "I plated the fried rice, sprinkling a pinch of dried herbs on top for good measure."
    
    hide supply_robot
    show elias first_meet_happy at right_elias with Dissolve(0.2)
    "Elias woke up and toddled over, rubbing his eyes."

    elias "Good morning, da— I mean, mister!"

    show dorian smile at left_char
    "I smiled, kneeling to his level to hug him."

    dorian "Morning, Elias. Hungry?"

    "He nodded enthusiastically as I gestured to the food. He hugged Tedda tightly."

    show dorian normal_alt_neutral at left_char
    dorian "Dig in!"

    show elias first_meet_neutral at right_elias
    "Elias sat cross-legged on the floor, the warm meal before him."

    hide elias
    show supply_robot base at right_supply with Dissolve(0.2)
    yuxuan "If I had a mouth, I'd eat every bite. My compliments, Chef Burnham."

    "Somewhere in the background, I could faintly hear an old woman's voice."

    weng  "Master Yuxuan, you must eat something. You've been working so hard."
    "Yuxuan's expression flickered briefly, but he said nothing, his gaze shifting away."

    show dorian neutral at left_char
    dorian "Who's that, Yuxuan?"
    show supply_robot lied at right_supply
    yuxuan "Oh just no one… Just my chef. I'm going to eat, Miss Weng! Just wait!"

    "The sound of the raging blizzard outside filled the brief silence. I stirred the pot absently"
    hide supply_robot
    show elias first_meet_neutral at right_elias
    elias "Mister…"
    "I turned to him."
    dorian "Yes, Elias?"

    show elias first_meet_neutral at right_elias
    "He hesitated, fiddling with Tedda's paw."

    elias "Is… is it okay if I call you daddy?"

    "The question hit me harder than I expected. My chest tightened, but I quickly ruffled his messy hair with a soft smile."
    show dorian smile at left_char
    dorian "Whatever makes you happy."

    show elias first_meet_happy at right_elias
    "Elias beamed, his face lighting up with pure joy as he hugged Tedda tightly."

    elias "Okay, daddy."

    # play audio amb_blizzard_howl loop fadein 2.0      # PLACEHOLDER

    "The blizzard raged on for several long, frigid days."
    show black with dissolve

    pause 1.5

    scene cg_trio_in_frostcradle with fade 

    "Yuxuan kept us company through his bot most of the time. Every now and then, his hologram would flicker to life, filling the space with his lively chatter."
    "He talked about everything from the weather in Mjoll to his latest technological breakthroughs, often rambling about his innovations."
    yuxuan "Dorian! This bot is powered by solar cells I designed myself. They're ten times more efficient than the industry standard. Did you know—"
    yuxuan "Dorian, are you even listening? You're not, are you?"

    "I'd glance up from whatever I was doing—whether sharpening my weapons or staring into the fire—and offer a half-smile."

    dorian "I'm listening, Yuxuan. Solar cells. Revolutionary. Got it."
    "He'd huff, but his grin always returned as he continued explaining how his “innovations would save the world.”"
    "Elias, in his own way, was the heart of those dreary days. His laughter echoed through the shack as he spent hours creating grand adventures for Tedda. "
    "His little voice brought warmth to the cold as he made the bear “fight” monsters or embark on daring rescues."
    "When he wasn't playing with Tedda, Elias would draw with crayons Yuxuan had included in the supply bot."

    "His little hands worked diligently, and when he was done, he'd proudly show me his creations—crude, colorful scribbles that strangely resemble me."

    elias "This is you, Daddy. See? You're big and strong! And this is me, and this is Tedda. Oh! And this is Mister Yuxuan."
    "He pointed at the lopsided figures, each with big, exaggerated smiles."
    dorian "You're quite the artist, Elias. I'll make sure to hang these somewhere special."
    "He beamed at the praise, clutching Tedda tightly as if the bear shared his pride."

    "As for me, I spent most of my time working out, trying to stay strong in case the worst came. The storm outside felt endless, and I needed to be ready for whatever waited when it finally broke."
    "Elias would climb into my lap or press against my side, his small body seeking comfort."
    "He'd hold onto Tedda with one arm and wrap the other around me. His soft breathing as he drifted off to sleep reminded me of nights long gone."
    "I thought of Elara. Of Daniel, Sarah, Emily, and Lucas. I couldn't talk to them anymore. I couldn't feel their touch or hear their laughter."
    "Then I thought of Elias."
    "What if this was all over? What if we survived the blizzard? What then?"
    "Would I give him back to King Gustav? The man who wanted him dead? Could I even bring myself to do it?"
    "I glanced at Elias, curled against me, his little face serene and innocent."
    "I didn't know what the right choice was. I wasn't sure I ever would."
    "Should I just give him back to King Gustav? I… I don't really know."

    scene frostcradle_cabin_on with fade

    show elias first_meet_neutral at right_elias
    show dorian neutral at left_char
    with Dissolve(0.2)
    elias "Good night, Daddy."
    dorian "Good night, Elias."

    hide elias
    show supply_robot base at right_supply with Dissolve(0.2)
    yuxuan "Good night to both of you. May the howling blizzard only make our little shack feel warmer."
    
    scene frostcradle_cabin with fade

    "The next day, I woke up to an eerie silence."
    "No howling winds."
    "No biting cold seeping through the cracks of the shack."
    "For a moment, I lay still, straining my ears for any sign of the blizzard."
    "But there was nothing."
    "Only silence."
    "Heart pounding, I scrambled to my feet, careful not to wake Elias, who was still curled up with Tedda by the fire. Moving swiftly, I made my way to the cave entrance."

    scene frostcradle_no_blizzard with fade
    show snow_blizzard_1
    "Snow stretched endlessly in every direction. But the storm—after what felt like an eternity—had finally stopped."
    "I could see the surroundings again: jagged rocks, distant trees buried under layers of frost, and the faint outline of mountains in the far distance."
    "Relief washed over me, and I turned, ready to hurry back to the shack and tell Elias the good news. But as I stepped forward, a voice stopped me in my tracks."

    jump ch3_vasily_arrives


# =============================================================================
# SECTION 14: LABEL CH3_VASILY_ARRIVES — Vasily's Battalion + Kristin's Death
# =============================================================================
# Vasily emerges with a full battalion demanding Elias's death.
# Niko briefly challenges the narrative — is dismissed.
# Kristin speaks out — and is immediately killed.
# Svante's grief is weaponised by Vasily to turn him against Elias.
# =============================================================================

label ch3_vasily_arrives:
    # play music ost_vasily_arrives fadein 1.0          # PLACEHOLDER

    show vasily alt_normal at right_char with Dissolve(0.2)
    vasily "Hello, friend. Took you quite some time to finish the mission."

    show dorian serious at left_char with Dissolve(0.2)
    "I froze. The voice was calm, almost casual. Slowly, I turned around."
    "My throat tightened. It was Vasily"

    dorian "V-Vasily... What brings you here?"

    show vasily alt_think at right_char
    "He stepped closer, his boots crunching softly against the cave floor."

    vasily "Oh, you know. Just passing through. Thought I'd check on an old friend."
    "His eyes flicked past me, scanning the interior of the cave before landing back on me. A smile tugged at his lips, but it was sharp, calculated, and far from friendly."
    show vasily neutral at right_char
    vasily "Imagine my surprise when I heard rumors. A seasoned mercenary hiding in a cave. Abandoning his mission. It's... disappointing, Dorian."
    "He tilted his head slightly, his gaze narrowing."
    vasily "What else am I here for, friend? We're here for the contract."

    "My chest tightened."
    dorian "We?"

    "Vasily didn't respond. Instead, he snapped his fingers."
    "The sound echoed through the cave, and within moments, the faint crunch of snow turned into a thunderous rhythm as soldiers began marching into view."
    "An entire battalion, their armor gleaming even in the dim light, filed into position behind Vasily."
    "My breath caught in my throat. Each soldier bore the insignia of King Gustav's forces."

    show vasily alt_aggressive at right_char
    vasily "Under orders from His Majesty, the Prince is to be executed. Immediately."

    "His eyes locked onto mine, and for a moment, the only sound was the faint crackle of the fire from the shack behind me."

    vasily "So tell me, friend. Have you killed the Prince yet?"
    show dorian normal_alt_annoyed at left_char
    dorian "You… didn't tell me the Prince was a toddler, Vasily."

    show vasily alt_aggressive at right_char
    vasily "Does it matter? The contract was clear. Elias Drakos is to be eliminated. His age doesn't change what he's done… or what's at stake."

    show dorian normal_alt_calm at left_char
    dorian "Look, I-I'll give you the money back. Every coin. I'll pay you back and walk away from this."

    show vasily alt_savage at right_char
    "Vasily barked out a laugh."

    vasily "The prided mercenary of Mjoll, reduced to bargaining over coin? You, who once stared down entire armies without flinching, now trembling over a child?"
    vasily "I'll even double your pay. Triple it, if that's what it takes. You've saved my hide more times than I can count, and I consider you a friend. That's why I'm offering you this chance."
    show vasily neutral at right_char
    "He paused, his tone softening just slightly, but his eyes remained cold and calculating"
    vasily "Just give us the Prince, and we'll call it even. No hard feelings."

    show dorian serious at left_char
    "A small part of me wanted to believe him, to trust that he'd keep his word."
    "But the image of Elias—his laughter, his warmth, the way he hugged Tedda so tightly—flashed through my mind. Could I really hand him over?"
    "Before I could answer, a guttural cry broke the silence."

    hide vasily
    show svante normal_angry at right_char with Dissolve(0.2)
    svante "That snake of a prince deserves to die!"

    "I turned toward the source of the voice and saw the violet haired-aldorith storming forward, his sword already drawn. His eyes were bloodshot, and his voice cracked with anguish."

    svante "Hundreds of innocent people were killed because of the blizzard! Dozens of my brothers and sisters died because of him!"

    "Tears streaked his face as he pointed his blade toward me."

    svante "Kill the Prince! Show no mercy!"
    hide svante
    show boy_ald_normal at right_flip with Dissolve(0.2)         # PLACEHOLDER
    boy_ald_soldier "My brother is right! He killed our family through this blizzard! He deserves to die!"

    "The crowd of soldiers stirred, murmurs of agreement spreading through their ranks. The tension was rising, and I could feel the tide turning against me."
    hide boy_ald_normal
    "A man with striking blue hair stepped forward from the shadows — Niko, in a hooded robe."

    show niko normal_base at right_char with Dissolve(0.2)
    niko "Hey… is it true?"
    "His voice was measured, intelligent. He turned to Vasily, his gaze sharp."
    niko "The Prince… is he really just a toddler?"
    hide niko
    
    show vasily alt_aggressive at right_char with Dissolve(0.2)
    vasily "What of it, Prophet?"
    hide vasily

    show niko normal_serious at right_char with Dissolve(0.2)
    niko  "It just doesn't add up. I no longer sense the death god's energy here. The presence that once lingered is gone."
    niko  "A toddler committing murder? The Queen's death? I examined her body. The wound — it's surgical. Precise. A toddler didn't do this."

    "Another man in a hooded robe rushed forward, grabbing Niko's arm and pulling him back. This one wore an ingratiating smile, his voice light and appeasing."

    hide niko
    show prophet_1 at right_char with Dissolve(0.2)
    prophet_1 "Hehe, forgive my fellow brother in Enoch, Count. He tends to let his curiosity get the better of him."
    prophet_1 "Please, pay him no mind."
    hide prophet_1

    show niko alt_irritate at right_char with Dissolve(0.2)
    niko "No. I'm serious. Something doesn't make sense, and—"

    "Without a word, Vasily reached into a pouch at his belt and pulled out a heavy bag of coins, tossing it at the man's feet with a dull thud"
    hide niko

    show vasily alt_think at right_char with Dissolve(0.2)
    vasily "Here. Your payment. The services of the death god's Prophets are no longer required."
    hide vasily
    show niko alt_annoyed at right_char with Dissolve(0.2)
    niko   "Tsk."

    "The other prophet scooped up the coins and bowed deeply."
    "The blue haired prophet hesitated, glancing between the bag and Vasily's steely gaze. The other prophet quickly scooped up the coins and bowed deeply."

    prophet_2 "Thank you, Count. May Enoch's blessings be with you. We will trouble you no further. Come, Niko."
    show niko alt_tense at right_char
    niko   "But brother—"
    prophet_2 "You know the First Law of Enoch: 'To hinder death is to defy Him.' We are not to interfere. Not even if death comes unjustly. Not even if the innocent must suffer."
    prophet_2 "Death is the final mercy, the stillness beyond pain. If the Prince is marked by fate, we must not stand in its way."
    show niko alt_disappointed at right_char
    niko   "I understand, brother. Praise be to His Word."
    prophet_2 "Praise be. Now come. Let us leave this place."
    hide niko
    hide dorian
    with Dissolve(0.1)

    "He dragged the blue-haired prophet away, but the he shot me one last look, before disappearing over the crowd."
    "The murmurs among the soldiers grew louder. An aldorith with silver hair stepped forward, her voice trembling but resolute."

    show kristin_normal at right_char with Dissolve(0.2)           
    kristin "Count Vasily… maybe they have a point. If the pieces don't fit, we have a duty to—"

    show svante normal_nervous at left_char with Dissolve(0.2)
    svante "What are you doing, Kristin?"
    kristin "Thinking, Svante, dear brother. For myself. You should try it sometime."

    show svante normal_angry at left_char
    svante "Shut it, Kristin! You dare question King Gustav? Our Father?"
    kristin "Brother, you used to think for yourself. What happened to you? Since when did you let blind faith replace reason?"
    kristin "I was there, Svante. I saw the Queen's body with the prophets. The wound didn't match the story of Father. Don't you see? This isn't right!"
    kristin "Brother, please believe me."
    svante "I… I…"
    hide kristin_normal

    show vasily alt_aggressive at right_char with Dissolve(0.2)
    "The air grew colder as Vasily stepped forward, his expression dark."

    vasily  "Enough."

    "He snapped his fingers. Kristin turned to him, her eyes wide with fear."
    hide vasily
    show kristin_normal at right_char with Dissolve(0.2)
    kristin "Count, please. I'm just—"

    scene cg_kristin_death with shock_cut

    "The blade struck her before she could finish. She crumpled to the ground, her blood pooling in the snow."

    scene frostcradle_no_blizzard with fade
    show snow_blizzard_1
    boy_ald_soldier "Done, sir."
    show vasily alt_aggressive at right_char with Dissolve(0.2)
    vasily          "Any more aldoriths willing to share their dissenting opinion?"
    vasily          "Hmph. Your Father never tolerates treason. Remember that."

    "The soldiers stiffened, their faces a mix of shock and fear. Svante dropped to his knees beside Kristin's lifeless body, his cries piercing the silence."

    show svante normal_sad at left_char with Dissolve(0.2)
    "Svante dropped to his knees beside Kristin's lifeless body, his cries piercing the silence."

    svante  "K-Kristin… No…"
    kristin "B-Brother… I'm sorry… Tell mother I—"
    show svante normal_angry at left_char
    svante  "Kristin! KRISTIN!"

    show vasily alt_think at right_char
    "Vasily turned to him, his voice cold."

    vasily "It's the Prince's fault, Svante. His crime is sowing doubt on Kristin."
    show svante normal_sad at left_char
    svante "K… K-Kristin *cries*"
    vasily "If it weren't for him, Kristin would still be alive. King Gustav is right."

    show svante normal_angry at left_char
    "Svante's tear-streaked face twisted into a mask of rage."

    svante "E-Elias… that boy… he's the reason…"

    hide svante with Dissolve(0.1)

    show vasily alt_normal at right_char
    show dorian serious at left_char 
    with Dissolve(0.2)
    
    "Vasily turned back to me, his expression softening."
    "I looked at Vasily. He wasn't here to mock me or humiliate me—he truly thought he was helping. A friend. Someone I trusted, someone who had my back through countless battles."

    vasily "Dorian, think about it. Don't throw everything away for this child. You know how this ends if you don't do the right thing."

    show vasily alt_think at right_char
    "He placed a hand on my shoulder, firm yet gentle."

    vasily "His Majesty hated that you took too long, you know… "
    vasily "But I'll make sure King Gustav knows what you've done for him. A fresh start, Dorian. You'll be back in his good graces. Back to doing what you do best—hunting, taking on missions, living the life you've earned."
    "He paused, leaning in slightly."

    vasily "A mansion, Dorian. Wealth. Comfort. You don't have to keep running, keep hiding. You've saved me countless times, and I'm here to save you."
    vasily "I mean it, Dorian. You're my friend. Don't ruin everything for one child. Let me help you."
    $ renpy.save("quick-1") # retry/quick save
    vasily "Well, Dorian? What's it going to be?"

    jump ch3_critical_fork


# =============================================================================
# SECTION 15: LABEL CH3_CRITICAL_FORK — D5: Give or Refuse Elias
# =============================================================================
# THE pivotal decision of the chapter. Irreversible.
# Give Elias → ch3_bad_end (BAD ENDING branch — years later suicide).
# Refuse     → ch3_fight_back (GOOD PATH — draconic fire awakening).
# =============================================================================

label ch3_critical_fork:
    # play music ost_critical_fork fadein 1.0           # PLACEHOLDER

    menu:

        "Give Elias to Vasily.":
            $ ch3_d5 = "gave"
            stop sound
            # stop music fadeout 1.0

            show dorian sad at left_char with Dissolve(0.2)
            "A long silence."

            dorian "Go ahead. The kid's inside the shack."

            show vasily alt_savage at right_char with Dissolve(0.2)
            "Vasily smiled."

            vasily "Aldoriths, go inside and kill the prince. Now."
            hide vasily
            show boy_ald_normal at right_flip with Dissolve(0.2)
            boy_ald_soldier "What? That's it? You're not going to punish this traitor for—"
            hide boy_ald_normal
            show vasily alt_aggressive at right_char with Dissolve(0.2)
            vasily "Do it. Now."
            "The boy faltered, swallowed hard, and then nodded."
            hide vasily
            show boy_ald_normal at right_flip with Dissolve(0.2)
            boy_ald_soldier "Yes, sir."
            hide boy_ald_normal
            show girl_ald_normal at right_char with Dissolve(0.2)
            girl_ald_soldier "On it, sir!"
            hide girl_ald_normal

            show svante normal_angry at right_char with Dissolve(0.2) 
            svante "Leave the prince to me. Kristin… sister… you'll be avenged."
            hide svante

            show vasily alt_normal at right_char
            "Vasily turned to me, his eyes soft."

            vasily "You made the right choice, friend. Now let us take care of business. I'm sure you'd rather… not see how the prince will be dealt with."
            "I didn't respond. I couldn't. Vasily sighed, draping a heavy jacket over my shoulders."
            vasily "You must be cold. Come on. I had some aldoriths brew you up some tea."

            show dorian sad at left_char
            dorian "Thanks, Vasily."

            hide vasily
            hide dorian
            jump ch3_bad_end

        "Refuse. Protect Elias.":
            $ ch3_d5 = "refused"
            $ svante_affection += 1
            stop sound
            jump ch3_fight_back

# =============================================================================
# SECTION 16: LABEL CH3_BAD_END — BAD ENDING (Give Elias)
# =============================================================================
# Elias is killed offscreen. Years pass.
# Dorian lives in hollow luxury, avoids Yuxuan, loses everything inside.
# Ends at the cliffside: Dorian's suicide. BAD END / CREDITS.
# =============================================================================

label ch3_bad_end:

    scene bg_mjoll_icelands with fade
    show snow_blizzard_1
    # play music ost_bad_end_luxury fadein 3.0          # PLACEHOLDER

    "Years passed."
    "Mjoll welcomed me back like a long-lost hero."
    "Vasily was true to his word—he always was. The mansion he promised became mine, a grand, sprawling estate with lush gardens, gilded halls, and guards at every gate."
    "Wealth flowed endlessly, and with it came the comforts I'd once dreamed of during those cold, lonely nights in the field."
    "The missions resumed soon enough. Vasily handpicked each one, ensuring my success and cementing my place as one of King Gustav's most trusted assets."
    scene mjoll_palace_throne with dissolve       
    "Vasily visited often. He'd stroll through the gardens with a glass of wine in hand, talking about politics, conquests, or whatever lavish party he was planning next. "
    "He'd laugh, slap me on the back, and call me his old friend."
    
    show dorian serious at left_char
    show vasily neutral at right_char 
    with Dissolve(0.2)
    vasily "You've done well for yourself, my friend. Look at you now. Comfortable, respected… untouchable."

    woman_3 "You sure know how to throw a party, sir Dorian!"
    woman_1 "Maybe you'd like some… company later? *blushes*"
    dorian "Thanks. See you at the next party."

    vasily "Ladies, calm down. This is Dorian, the legendary mercenary of Mjoll you're speaking to!"

    woman_3 "Of course, Count. We know that. That's why we want to be with him."

    "But his words rang hollow, like the clinking of glasses in empty halls."
    "I never saw Elias again."
    "It wasn't hard to imagine where he might've ended up—locked away in some tower or paraded around as a trophy of Gustav's power."
    "I stopped asking questions. Stopped wondering. Wondering only made the nights longer."
    "As for Yuxuan? I avoided him entirely."
    "The thought of facing him, of seeing the disappointment or anger in his eyes, was unbearable."
    "He didn't deserve an explanation."
    "Not from me."
    "And Elara…"
    "Would she be proud of me?"
    "I already knew the answer."

    "The parties became a regular occurrence, each one more extravagant than the last."
    "Nobles from across the kingdoms gathered in glittering halls, their laughter echoing off marble walls."
    "I attended them all, silent and distant, a shadow in the midst of their revelry."

    vasily "Another grand event next week, my friend. King Gustav will be there. You'll come, won't you?"
    dorian "Of course, Vasily."
    woman_3 "Ooh sir Dorian! If you wanna have a good time, I know where it's at!"

    hide vasily
    hide dorian
    scene frostcradle_blizzard with fade                # PLACEHOLDER
    show snow_blizzard_1
    # stop music fadeout 3.0

    show dorian sad at left_char with Dissolve(0.2)
    "One evening, I left the party early."
    "The wind was bitter, cutting through my coat as I stood at the edge of the cliff."
    "Below, the snow stretched endlessly, a vast, frozen wasteland illuminated by the pale light of the moon."
    "I stared out at the expanse, my mind swirling with memories I could no longer suppress. Elias's innocent smile. Yuxuan's sarcastic quips."
    "And Elara. Always Elara."
    "I could almost hear her voice, soft and loving, like it used to be when she whispered my name."
    "The snow beneath my boots crunched softly as I took a step closer to the edge."

    scene black with fade
    dorian "Elara, I'll see you soon."

    "For a moment, everything was silent. The world seemed to hold its breath, waiting."
    "And then I let go."
    # stop audio

    pause 3.0

    "GAME OVER — BAD END"

    pause 1.0

    jump game_over

# =============================================================================
# SECTION 17: LABEL CH3_FIGHT_BACK — GOOD PATH: Draconic Fire Awakens
# =============================================================================
# Elias is shot by an arrow — Dorian's draconic fire erupts for the first time.
# The entire battalion is destroyed.
# Niko (in raven form) heals Elias in the background.
# Only Svante survives — he falls through crumbling ground.
# Dorian collapses. Yuxuan finds them.
# =============================================================================
label ch3_fight_back:

    # play music ost_vasily_arrives fadein 0.5          # PLACEHOLDER
    "I shook my head, stepping back from Vasily's grip, my voice firm but calm as I raised a hand in a gesture of negotiation."

    show dorian serious at left_char
    show vasily alt_aggressive at right_char 
    with Dissolve(0.2)

    dorian "No, Vasily. I can't do this. I beg you just… take the coin."
    dorian "I'll return every piece the King gave me for this mission. No harm, no foul. We can both walk away from this."
    show vasily neutral at right_char
    "Vasily sighed, shaking his head slowly."
    vasily "You don't get it, do you? This isn't about the coin, Dorian. It's about loyalty. It's about trust. The King doesn't just want his money's worth—he wants proof that his men are still willing to do what's necessary."
    vasily "The prince needs to die."
    "He took a step closer, his voice dropping to a near whisper."

    vasily "You're putting me in a bad spot, old friend. I vouched for you. I said you'd get the job done, no questions asked. Do you know what happens to me if you fail?"

    "Behind him, the violet haired aldorith let out a sharp, choked sob, his rage boiling over into words."

    hide vasily 
    show svante normal_angry at right_char with Dissolve(0.2)
    svante "That boy—that prince—is the reason my sister is dead! You're protecting a murderer! You're as guilty as he is!"
    "I kept my stance firm, meeting Vasily's gaze."

    dorian "Look. I beg you. Just take the money. We all can-"
    hide svante
    show elias first_meet_neutral at right_elias with Dissolve(0.2) 
    elias "Daddy?"
    hide elias

    show dorian normal_alt_tense at left_char
    "My heart dropped. I spun around, and there he was—Elias—standing at the entrance of the shack, clutching Tedda tightly to his chest."
    "His small face was pale, his wide eyes flicking between me and the soldiers."

    show dorian angry at left_char
    "I reached out, panic surging through me."
    dorian "Elias! Get back inside! Now!"
    
    show vasily alt_savage at right_char with Dissolve(0.2)
    "I turned back to Vasily, my hand instinctively moving to the hilt of my blade."

    dorian "You see? He's just a child, Vasily. Look at him. Does he look like a killer to you?"

    show vasily alt_mad at right_char
    "Vasily's expression hardened, his eyes narrowing as he studied Elias."
    vasily "The prince needs to die. My loyalty stands with the king. If the king says he murdered the Queen, then I would swear by Enoch's name that he did it."
    
    "Long live King Gustav!"
    hide vasily

    show svante normal_angry at right_char with Dissolve(0.2)
    svante "L-Long live King Gustav!"
    hide svante

    dorian "Enough!"
    "My shout echoed through the cave, silencing the crowd. I stepped forward, placing myself between Elias and the soldiers."

    show dorian normal_alt_annoyed at left_char
    dorian "If you want him, you'll have to go through me."
    show vasily alt_mad at right_char with Dissolve(0.2)
    "Vasily's eyes narrowed."
    vasily "Don't do this, old friend. You're throwing your life away for a child who doesn't even belong to you. Is it even worth it?"

    show dorian serious at left_char
    dorian "Yes. Yes, he is."

    show vasily neutral at right_char
    "Vasily's hands glew with light. He scoffed."
    vasily "So be it."

    scene vasily_attack with shock_cut
    "Vasily raised his hand, an orb of light forming in his palm. He hurled it toward Elias with a flick of his wrist, the sphere roaring through the cave like a comet."
    "I slammed my hands into the ground, the earth trembling beneath my feet as an earthen wall erupted from the cave floor." with hpunch
    "The light ball struck it with a deafening explosion, the impact sending shards of rock flying in every direction."
    scene frostcradle_no_blizzard with Dissolve(0.4)
    show snow_blizzard_1
    "Before I could catch my breath, pain tore through my leg as an arrow sank deep into my thigh."
    show dorian dragon_eyes at left_char
    show vasily alt_savage at right_char
    with Dissolve(0.2)
    dorian "ARGH!!!"
    "I stumbled, my balance faltering, blood pouring from the wound. Gritting my teeth, I tore the arrow free, the pain white-hot and blinding."
    "But before I could recover, another arrow whistled through the air."
    "Time seemed to slow as I saw it—its sharp tip gleaming, its deadly path aimed directly at Elias."

    scene cg_elias_arrow with shock_cut
    "The arrow struck him."

    elias "AH!!"

    "He crumpled to the ground, his small body going limp, blood pooling beneath him."

    scene frostcradle_no_blizzard with Dissolve(0.3)
    show snow_blizzard_1
    show boy_ald_normal at left_char
    show girl_ald_normal at right_char
    with Dissolve(0.2)

    boy_ald "He's hit! The bastard prince is down!"
    girl_ald "Praise be to Enoch! Someone check if he's dead!"
    boy_ald "Positive! The wound is grave—straight through the gut!"

    hide boy_ald_normal
    hide girl_ald_normal
    show dorian angry at left_char
    with Dissolve(0.2)

    dorian "No! Elias! No!"
    "A ragged scream tore from my throat as I staggered toward him. Vasily's smirk widened as he approached the boy, his hand glowing with that same deadly light."
    
    show vasily neutral at right_char with Dissolve(0.2)
    vasily "Such is the fate of all who goes against His Highness' wishes."

    dorian "Elias!! Elias!!"
    "I stared at Elias lying there—innocent, bloodied, and helpless."
    dorian "Elias!! Please!!"

    "He didn't respond. His eyes fluttered shut, and the world around me seemed to fade. All I could hear was the pounding of my heart and Vasily's laughter, cold and mocking."
    "My vision blurred, tears streaming down my face."
    "And then, I heard it."

    scene black with fade
    "A voice. Familiar. Deep. Ancient. Unstoppable."
    prosperity_dragon "Never shall it be said that my children are weak. Rise up, Dorian!"
    prosperity_dragon "Do not mourn. Fight!"

    show screen rage_power
    with dissolve
    "The air around me shifted. Heat radiated outward from my body, intense and suffocating. My hands, still trembling, began to glow, flames flickering to life on my fingertips."
    "I looked down at Elias, tears streaking my face, and something inside me shattered. The grief twisted, transformed into something raw and feral."
    "Rage."
    "They wanted Elias… and they were going to have to pay for it in blood."
    hide screen rage_power
    with dissolve

    scene frostcradle_no_blizzard
    show screen draconic_rage 
    show dorian dragon_eyes at left_char
    with Dissolve(0.2)

    dorian "You'll pay for this, Vasily… You'll pay for this."
    "Vasily's smirk faltered. He took a step back, his hand lowering as the fire around me grew, its heat warping the air."
    
    show vasily alt_mad at right_char with Dissolve(0.2)
    vasily "D… Draconic fire?! In Enoch's name…"
    vasily "Friend… wait… we can talk about this—"
    "I didn't let him finish."
    "With a roar that shook the cave, I raised my hands, fire erupting in a torrent that roared like a beast unleashed."
    "It surged toward him, engulfing him completely. His screams were drowned out by the crackling inferno."

    vasily "Ahhh!! Ahhhh!!!"
    hide vasily with Dissolve(0.3)

    show girl_ald_normal at right_char with Dissolve(0.2)
    girl_ald "What in the name of Enoch—"
    "The ground beneath her erupted, jagged pillars of molten rock spearing upward. The heat melted the steel of her armor, her body incinerated before she could even cry out."
    hide girl_ald_normal
    hide screen draconic_rage
    hide dorian

    scene cg_mjoll_massacre with fade
    # TODO: add intense fight music (massacre)
    boy_ald "C-Charge! Charge!"
    "They came at me in waves, arrows flying, swords raised."
    "But I killed them."
    "I raised one hand, and the earth quaked. Chasms opened beneath their feet, swallowing them whole."
    "With the other, I sent firestorms spiraling into their ranks, their screams echoing as they burned alive."

    female_soldier_1 "No!! Ahhh!!!!"
    male_soldier_1 "Ahhhh!!!"
    boy_ald "Mercy!! Enoch save me!! Ahhh!!"
    girl_ald "We're just obeying orders! Don't kill us!! Ahh!!"
    dorian "..."

    scene black with fade
    "A raven approached Elias."
    elias "D-Daddy… I-It hurts… it hurts! *cries*"
    niko "Shh… hey, hey. Little one. Are you alright?"
    elias "N-No! G-Get away! Don't hurt me! *cries*"
    niko "Hey, hey. Look at me. See? Just a bird. A talking, friendly bird."
    elias "A… A bird?"
    niko "Yes. Talking, friendly, very handsome bird. Came just for you."
    elias "It… it hurts… I'm scared… I don't wanna die… *cries*"
    niko "Now where does it hurt?"
    elias "M-My tummy… I-It's cold… it's so cold…"
    niko "Then hold this. One of my feathers. See? Strong. Safe."
    niko "Big bird's going to help you. It might tickle, might sting—but I promise, you'll feel better soon. Bird's honor."
    elias "*crying*"
    niko "Wait—what's this? Is this your friend?"
    elias "T-Tedda… Her name is Tedda. She's… friend."
    niko "Tedda, huh? A brave guardian. Good. You hold her tight. You've got her… and now you've got me."
    elias "I… I don't wanna die… like Mommy *cries*"
    niko "Not today. Not while the wind still moves and the roots still breathe. I'm going to patch you up, little prince. I promise. Just breathe with me."
    elias "O…Okay."

    scene black with fade

    # Back to Dorian's massacre aftermath
    scene frostcradle_no_blizzard with Dissolve(0.6)
    show snow_blizzard_1
    "One by one, they fell, their bodies consumed by the flames or crushed beneath the earth's fury. The snow outside melted, turning to steam that hissed and billowed around the cave."
    "Then… the violet haired aldorith was the only one left."

    show svante normal_sad at right_char
    show dorian normal_alt_annoyed at left_char 
    with Dissolve(0.2)
    "He fell to his knees, tears streaming down his face, his sword clattering to the ground."
    show svante normal_nervous at right_char
    svante "P-Please! Mercy! I-I didn't mean for this! It wasn't supposed to happen like this! Kristin—she's dead, and now—"
    "His words dissolved into incoherent sobs as he clutched at the hem of my cloak."
    "I raised a hand, fire flickering at my fingertips."
    dorian "…"

    svante "Please! I believed my sister! But you saw what they did to her! I don't— *crying*"
    svante "I'm sorry! I'm sorry! Please, sir! I—"

    show dorian serious at left_char 
    "The fire in my hand flared, my rage begging for release. I took a step forward, the heat forcing him to crawl backward."
    "And then his foot slipped."

    svante "AHHHH!!!"
    scene black with shock_cut
    "The ground beneath him crumbled. He screamed as he fell, his voice cutting off abruptly."
    "Silence."

    scene bg_frostcradle_cave with Dissolve(0.9)
    "The cave was still, save for the hiss of steam and the crackle of dying flames."
    show dorian sad at center_char with Dissolve(0.2)
    "I clenched my fists, the flames flickering out, leaving behind only the charred remains of what had been a battalion of soldiers."
    "I staggered, the heat around me dying down as exhaustion took hold. My legs gave out beneath me, and I crumpled to the ground. My vision blurred, darkness creeping in at the edges."

    dorian "Elias…"
    dorian "I'm sorry… I'm so sorry..."
    "The last of my strength slipped away, and the world around me faded into darkness."
    scene black with fade
    jump ch3_escape


# =============================================================================
# SECTION 18: LABEL CH3_ESCAPE — Yuxuan Finds Them / Escape to Tianho
# =============================================================================
# Yuxuan's bot finds Dorian. They escape in a carriage.
# Dorian wakes to find Elias alive beside him.
# Chapter ends with 'jump chapter_4'.
# =============================================================================
label ch3_escape:
    scene black
    pause 1.5
    "A faint whirring sound pulled me from the void. It was mechanical, distant, but growing louder."
    # TODO: add robot motor sounds (small motors)
    "My body felt heavy, as though I were sinking into the earth itself."
    # stop sound
    "Then I heard a voice, sharp and familiar, cutting through the haze."

    scene bg_frostcradle_cave with Dissolve(0.5)
    show supply_robot sad at left_supply with Dissolve(0.2)
    yuxuan "Dorian! Goodness, what happened here?!"

    "I forced my eyes open, just for a moment. A faint hologram flickered before me — Yuxuan's face, distorted by static, but unmistakably horrified."

    yuxuan "Prosperity Dragon bless me. I need to get you to safety…. Miss Weng! Call the—"

    hide supply_robot
    "The bot hovered closer, scanning the scene. I wanted to respond, to explain, but my body betrayed me."
    "My head lolled to the side, and everything went dark again."

    scene black with fade
    "The next time I stirred, the world felt different. Softer. Warmer."
    "I wasn't on the frozen ground anymore. Instead, I was lying in something cushioned, wrapped in thick blankets."
    "I blinked against the light filtering through the carriage windows, the soft sway of motion beneath me lulling but unfamiliar."
    "My head throbbed with a dull ache, and when I tried to sit up, a sharp pain shot through my leg, forcing a groan past my lips."
    dorian "Elias…"
    "Panic surged through me until I looked to my side and saw him."

    scene yuxuan_carriage with Dissolve(0.5)
    show elias first_meet_neutral at right_elias with Dissolve(0.2)
    "He was there, curled up on the bench across from me, Tedda clutched tightly in his arms. His chest rose and fell with shallow but steady breaths."
    elias  "Daddy…"

    show dorian neutral at left_char with Dissolve(0.2)
    dorian "I'm here, Elias. I'm right here. We're going to be okay."

    "I reached out, brushing his hair from his face. Tears welled up in my eyes."

    "A voice spoke from outside the carriage."
    hide elias
    show yuxuan normal_happy at right_char with Dissolve(0.2)
    yuxuan "Dorian! You're awake! Praise the Prosperity Dragon!"

    "The door creaked open, and Yuxuan stepped inside. For the first time, it wasn't just his hologram from a supply bot. It was him. In the flesh."
    "His smile was as warm and earnest as I remembered from the hologram, but seeing him here, in person, was something else entirely."
    "His robes shimmered with an opulent sheen. Deep crimson fabric. The stitching alone probably cost more than I'd made in the last decade."
    hide yuxuan

    show elias first_meet_happy at right_elias with Dissolve(0.2)
    elias "Daddy, it's him! Mister Yuxuan!"

    hide elias
    show yuxuan normal_sad at right_char with Dissolve(0.2)
    yuxuan "Thank the Prosperity Dragon I decided to check in. If I hadn't sent the bot when I did…"
    show yuxuan alt_mid_close_eyes at right_char
    "He trailed off, shaking his head."
    show yuxuan normal_neutral at right_char

    dorian "Y-Yuxuan."
    show dorian smile at left_char
    "My voice cracked, my throat dry as sandpaper."
    dorian "Good to see you in person."
    show dorian normal_alt_neutral at left_char
    "Yuxuan's grin widened."
    show yuxuan normal_happy at right_char
    yuxuan "The pleasure's all mine, Dorian! I'm so happy to finally meet you again!"

    show yuxuan alt_neutral at right_char
    "He stepped aside, glancing toward the driver."
    "One of the guards—an older man with silver streaks in his hair—replied without hesitation."

    man_2 "A few hours, Master Yuxuan"

    show dorian sad at left_char
    "At the mention of Tianho, something stirred in me. It had been years since I'd set foot there. Elara and my family. It's been a while."
    
    yuxuan "We're taking you both to Tianho. We'll be hiding there."
    show yuxuan normal_neutral at right_char
    show dorian serious at left_char
    "I tried to respond, but my throat was dry, and the words caught. Instead, I nodded, leaning back against the cushions."
    
    hide yuxuan 
    show elias first_meet_happy at right_elias
    "Elias stirred on the bench, his eyelids fluttering open. His gaze met mine, his small hand reaching out."
    elias "Daddy… I'm happy you're alright."

    show dorian neutral at left_char
    "I took his hand, squeezing it gently."

    dorian "I promise, Elias. We'll be okay. I'll protect you. No matter what."
    "The carriage rocked gently as it moved, the muffled sound of hooves against the road."
    "We were alive. We were together."
    scene black with fade

    "And for the moment, that was enough."
    # stop music fadeout 2.0
    # stop audio fadeout 1.5

    pause 2.0

    show screen chapter_title_screen(
        "4",
        "The Massacrer of Mjoll",
        subtitle="Kingdom of Mjoll — Aftermath",
        duration=3.0
    )
    pause 3.0

    jump chapter_4
    
# =============================================================================
# END OF CHAPTER 3
# =============================================================================
