###############################################################################
#  Dragon's Heart: The Crimson Rebirth
###############################################################################

# =============================================================================
# SECTION 5: LABEL CHAPTER_6 — Lab Bedroom / Dorian Wakes
# =============================================================================

label chapter_6:
    if demo_mode:
        scene black with fade
        pause 1.0
        centered "Thank you for playing the demo\n\n Full version will include ch6-10"
        pause 2.0
        $ MainMenu(confirm=False)()
        
    $ save_name = "Chapter 6"
    # scene bg_lab_bedroom with fade              # PLACEHOLDER — lab bedroom, dim lamp in corner — use spare_room
    scene spare_room with fade

    # play music ost_lab_dim fadein 2.0           # PLACEHOLDER — quiet late lab theme
    # play audio amb_lab loop fadein 1.5          # PLACEHOLDER — lab hum ambient

    show screen chapter_title_screen(
        "6",
        "Beneath Tianho",
        # subtitle="Tianho — Underground Lab",
        duration=3.0
    )
    pause 3.0
    scene spare_room with fade


    show elias normal_neutral at right_char_kids with Dissolve(0.2)
    elias "Daddy! Daddy! Wake up!"

    "A small pair of hands shook my shoulders. My breath hitched as I jolted awake, a choked gasp escaping my throat."
    "Tears clung to my face. Damn it. I pressed my palms against my eyes, willing myself to steady."

    elias "Are you okay, Daddy?"

    "I swallowed, trying to push away the burning weight in my throat. My body still trembled, the dream lingering like a wound torn open."
    show dorian sad at left_char with Dissolve(0.2)
    dorian "N-n-no, buddy. It's nothing. Don't think about it."

    "A small pause. The fan hummed softly in the quiet room, blades cutting through the still air."
    "A single dim lamp was at the far corner of the room. It partially lightened up Elias' face."

    show elias normal_sad at right_char_kids
    elias "You were crying, Daddy."

    "His voice wavered, gentle, worried."

    elias "I was worried. Tedda went out to get water from kitchen."
    show dorian normal_alt_calm at left_char with Dissolve(0.2)
    "I exhaled, rubbing my face."

    show elias normal_neutral at right_char_kids
    elias "Tedda says bad dreams need water. She'll be back."

    show dorian neutral at left_char
    "He smiled and reached out, his tiny hand wrapping around mine."
    "I froze."
    "With my free hand, I wiped away the last of my tears, then gave his fingers a gentle squeeze."
    "He hesitated, then reached up with his other hand, his small arms barely making it to my face as he patted my head."

    show elias normal_happy at right_char_kids
    elias "I'm here, daddy. Okay? Don't cry. I love you."

    "I forced a chuckle, ruffling his messy curls."
    show dorian smile at left_char
    dorian "Come on, Elias. I'm not crying. But, thank you. I love you too, Elias."

    show elias normal_happy at right_char_kids
    "His eyes shone, full of childlike pride."

    elias "You always protect me, Daddy. I wanna protect you too."

    "I smirked, shaking my head."
    show dorian neutral at left_char
    dorian "But what happens if I got attacked by an ugly monster? Would you save me?"

    show elias normal_sad at right_char_kids
    "Elias gasped."
    "The worry on his face vanished—replaced with uncontainable excitement."
    show elias normal_happy at right_char_kids
    "He scrambled up on the bed, wiggling like a puppy, his whole body buzzing with energy."
    "Then—he struck a pose."
    show elias alt_joy at right_char_kids
    "One foot forward. One tiny fist raised."
    show elias normal_evil at right_char_kids
    elias "Hmph! I'll beat that ugly monster and his ass!"

    show dorian serious at left_char
    dorian "Elias—language."

    show elias normal_happy at right_char_kids
    "He froze."
    "Then, with wide, guilty eyes, he quickly corrected himself—talking even faster."

    elias "I mean, butt. Daddy. AND—AND THEN—!!! I'll do a super-duper spinny kick! WHOOSH!!!"

    show elias normal_happy at right_char_kids
    "He spun in a clumsy circle, nearly tumbling onto his face."
    "I wrapped my arms around him, holding him close."

    dorian "How long was I asleep, Elias?"
    elias  "I don't know, daddy. Mister Niko brought you here."
    elias  "After you fell asleep, Tim and I were played and colored. A… And—And… Tedda joined us!"
    elias  "And then… and then… hmm…"

    "He scrunched his nose, tapping his chin like he was deep in thought. I couldn't help but chuckle and play along with Elias's imagination."

    show dorian neutral at left_char
    dorian "Haha. Tedda joined you and Tim? Did she give you hugs?"
    show elias normal_happy at right_char_kids
    elias  "Yes, Daddy! Big big hugs! And I feel so happy. We're with other people now."
    show dorian smile at left_char
    dorian "Yeah. It's not just you, me and Yuxuan."
    show dorian neutral at left_char
    elias  "And Tedda!"

    show elias normal_happy at right_char_kids
    "He threw his arms up, bouncing slightly."

    dorian "And Tedda."

    "The fan continued to hum softly in the quiet room. Elias yawned and hugged me close back."

    jump ch6_elias_choices


# =============================================================================
# SECTION 6: LABEL CH6_ELIAS_CHOICES — D1: 4 Questions for Elias
# =============================================================================
# Single-select. Each choice awards +1 affection to a different character.
# All lead to ch6_elias_common.
# =============================================================================

label ch6_elias_choices:
    menu:
        "How's Yuxuan?":
            $ ch6_d1_elias_choice = "yuxuan"
            $ yuxuan_affection += 1             # +1 Yuxuan affection

            show dorian neutral at left_char
            dorian "How's Yuxuan? What happened during dinner?"
            show elias normal_lying at right_char_kids
            elias  "I think he go… to his office, daddy. I saw him getting… Grrr…"
            show dorian normal at left_char
            dorian "Like angry? That's him alright. Sounds like something that he'll do."
            show elias normal_neutral at right_char_kids
            elias  "But then he went inside office and it became quiet. Weaaaal quiet. He took Mister Roboto with him too."
            elias  "But he's reallyyyy nice, daddy. He gave me and Tim some candies a while ago! He even made you and me stay in a big room like this. Maybe we can live here forever! Hihi"
            show dorian neutral at left_char
            dorian "Well, not forever, Elias. I doubt a millionaire like him would want us to stay in his expensive home."
            show elias normal_happy at right_char_kids
            elias  "He wants us to, daddy! He told me that if we wanted to, we could stay here forever with him! You, me and him!"
            dorian "Huh? Wait, did he really say that?"
            show elias normal_happy at right_char_kids
            elias  "Yes, daddy! Tim even made fun of Mr. Yuxuan! He said that Mr. Yuxuan was… hmm, what was it… oh, a blushing mess! Tim said Mr. Yuxuan was a blushing mess when he said we can stay here forever!"
            elias  "*yawns* Hmm… Daddy, what does a blushing mess mean?"

            "He yawned, snuggling deeper into the blankets."

            show dorian neutral at left_char
            dorian "Uh, well... a blushing mess is when someone has their face all red and can't speak straight. Like when they're embarrassed or have a crush on someone."
            show elias normal_happy at right_char_kids
            elias  "Ohhh, like when Mr. Yuxuan talk to you, daddy! He always gets all red and acting weiwwd! Tim was right, daddy!"
            show dorian normal_alt_annoyed at left_char
            dorian "I-I'm not sure what you mean, Elias. Yuxuan is just a good friend, that's all."

            jump ch6_elias_common

        "What happened to the Emperor?":
            $ ch6_d1_elias_choice = "emperor"
            $ chunghee_affection += 1           # +1 Chung-hee affection

            show dorian neutral at left_char
            dorian "Do you remember the man we rescued? How is he doing?"
            show elias normal_neutral at right_char_kids
            elias  "Oh, the man with the cool arm, daddy?"

            show dorian serious at left_char
            "My thoughts went to the dream I had earlier."
            "If that was true then…"
            "I'm sorry, Chung."
            "Emperor Hyon Min-joon and his wife. So that's how they died."
            "Gustav Nordstrom…"
            show dorian angry at left_char
            "Just the thought of his name got my blood boiling. I tightened my fist."

            elias  "So, Mister Niko told him that he get more sleep and then- And- Daddy, are you listening?"
            show dorian neutral at left_char
            dorian "Oh, I'm sorry, buddy. I was just thinking about some stuff."
            show elias normal_sad at right_char_kids
            elias  "*yawns* Oh, okay. Um… I… I forgot, Daddy. What was I talking about?"

            "He yawned, snuggling deeper into the blankets."

            show elias normal_neutral at right_char_kids
            elias "Oh! We were talking about the Empewor… His name is Cheng or Chong. Chang-hai? Cheng-hai?"
            elias "Cheng, daddy. Or Chang. Maybe Tedda knows. You should ask her when she gets back, daddy. She knows a lot about Kyeongjang!"

            jump ch6_elias_common

        "How was the violet-haired man?":
            $ ch6_d1_elias_choice = "svante"
            $ svante_affection += 1             # +1 Svante affection

            show dorian neutral at left_char
            dorian "Do you remember the violet-haired guy with us? What happened to him when I passed out?"
            show elias normal_neutral at right_char_kids
            elias  "Hmm… The pink one, daddy? He helped Miss Weng clean."

            show dorian serious at left_char
            "Svante Nordstrom… The aldorith. He was one of the soldiers who were originally tasked to kill the mysterious man."
            "To my surprise, he joined us and helped us escape."
            "I must admit, it took a lot of courage and strength for him to just disobey his father like that."

            show elias normal_happy at right_char_kids
            elias  "He's from Mjoll. Right, Daddy? Mjoll is very very cold."

            "Elias cuddles even more, burying his tiny head at my chest."

            show dorian smile at left_char
            dorian "Yeah. You like the weather here more, Elias?"
            show elias normal_neutral at right_char_kids
            elias  "*yawns* Yes, Daddy. It isn't cold like the cave there. It's more… comfy here."
            show dorian neutral at left_char

            "He yawned, snuggling deeper into the blankets."

            show elias normal_happy at right_char_kids
            elias  "I hope we get to know the pink guy. I think he's so nice. He laughed when Tim made a joke."
            show dorian normal_alt_annoyed at left_char
            dorian "Pink is not violet, Elias."

            jump ch6_elias_common

        "How is the doctor?":
            $ ch6_d1_elias_choice = "niko"
            $ niko_affection += 1               # +1 Niko affection

            show dorian neutral at left_char
            dorian "I guess that the doctor helped me when I passed out, huh?"
            show elias normal_happy at right_char_kids
            elias  "Yes, Daddy! He was so cool! He waved his fingers and there were plants!"
            elias  "What do you call them, Daddy?"
            show dorian neutral at left_char
            dorian "Nature channelers, Elias. They're called nature channelers. They channel nature itself."
            dorian "You haven't seen one before, right?"

            show elias normal_neutral at right_char_kids
            "Elias shook his head."

            elias  "Then he carried you back here, Daddy. Mister Svante helped him."
            show dorian normal_alt_annoyed at left_char
            dorian "…I weigh more than two people combined."
            show elias normal_happy at right_char_kids
            elias  "He's really strong, Daddy! And he was so serious."
            show dorian neutral at left_char

            "He yawned, snuggling deeper into the blankets."

            elias  "*yawns* Very…. Amazing…"

            jump ch6_elias_common


# =============================================================================
# SECTION 7: LABEL CH6_ELIAS_COMMON — Elias Falls Asleep
# =============================================================================

label ch6_elias_common:
    show dorian neutral at left_char
    show elias normal_neutral at right_char_kids
    "Elias's breathing slowed, his tiny chest rising and falling in a steady rhythm. His fingers, still curled around my sleeve, loosened their grip as sleep took him."

    show dorian smile at left_char
    "I leaned down, pressing a gentle kiss to his forehead."

    dorian "Sleep well, buddy."
    show dorian neutral at left_char

    "Carefully, I tucked the blanket around him, making sure he was warm before standing."
    "The room was quiet, save for the soft hum of the fan."
    "I lingered for a moment, watching the peaceful rise and fall of his breath, then quietly made my way to the main area."

    jump ch6_briefing


# =============================================================================
# SECTION 8: LABEL CH6_BRIEFING — Lab Dim / Chung-hee and Tim
# =============================================================================
# Chung-hee explains: Tianho is under siege. Weng went above. Niko and Svante followed.
# =============================================================================

label ch6_briefing:

    scene lab_cave_off with dissolve

    "There, in the dim glow of the lanterns, Chung-hee sat with his back straight, a cup of tea cradled in his hands."
    "Beside him, Tim fidgeted anxiously, his little fingers drumming against the wooden table."
    "Chung-hee looked up as I entered, his sharp eyes studying me."

    scene lab_cave_on with dissolve
    show chunghee normal_neutral at right_char
    show dorian neutral at left_char
    with Dissolve(0.2)
    chung_hee "You're awake."
    dorian    "How long was I out?"
    chung_hee "Four hours, I believe."

    "He took a sip of his tea, setting the cup down with a quiet clink. Then, his expression hardened."

    show chunghee normal_angry at right_char
    chung_hee "We need to go. To Tianho."
    show dorian serious at left_char
    dorian    "Tianho? Why?"

    show chunghee normal_v2 at right_char
    "Chung-hee exhaled slowly, fingers curling around his cup."

    chung_hee "Tianho is under siege by monsters."
    show dorian angry at left_char
    dorian    "What?!"

    "Tim's face was pinched with worry, his small hands clenched into fists."
    show dorian serious at left_char

    show tim sad at center_char_kids with Dissolve(0.2)
    tim "Mister Dorian! Miss Weng—!"

    "He swallowed hard, looking up at me with wide, desperate eyes."

    tim "Tianho is under attack! Miss Weng went there to check on Master Yuxuan's main branch shortly after dinner, but then suddenly monsters attacked!"

    show chunghee normal_neutral at right_char
    chung_hee "Svante and Niko followed after her. I stayed behind because Niko ordered me to."
    chung_hee "He said I'm still recovering."

    tim "But they've been gone for so long…! What if—what if something happened to them?"

    "His voice cracked slightly, and he hugged his arms to his chest."

    dorian    "Where's Yuxuan?"

    "Chung-hee's brow furrowed slightly."

    chung_hee "He panicked the moment he heard, said something about the underground and locked himself in his study. He said it was important."
    show dorian serious at left_char
    dorian    "Important?"
    tim       "Yes, Mister. He said it was very important."
    show chunghee normal_sad at right_char
    chung_hee "I want to help. But I don't think I can do much with my situation."
    chung_hee "Will you accompany me, Dorian?"

    show dorian neutral at left_char
    show tim normal at center_char_kids
    "I glanced at him, noting the way his fingers lightly tapped against the side of his cup. I can tell that his unease."

    dorian    "Yeah, of course. But I can't leave Elias behind."
    show chunghee normal_neutral at right_char
    chung_hee "He has Tedda."

    show dorian normal_alt_annoyed at left_char
    "I nearly rolled my eyes."

    dorian    "Chung, you're an adult. You know Tedda's a stuffed animal doll, right?"
    hide chunghee

    jump ch6_tedda

# =============================================================================
# SECTION 9: LABEL CH6_tedda — Tedda is Alive / Roboto Update
# =============================================================================

label ch6_tedda:

    show tedda_human at right_char with Dissolve(0.2)
    tedda " A stuffed animal doll? Oh, Mister Dorian, I'm offended!"

    "I turned, and there she was, standing in the doorway with a dramatic pout."
    "She held a pitcher of water in both hands, her pink dress swishing as she swayed on her heels."
    "Stuffed toy ears, identical to the ones on Elias's doll, sat atop her head."

    show dorian normal_alt_tense at left_char
    dorian        "… T-Tedda?"
    tedda   "It's me, Mister Dorian! Hello!"
    show dorian neutral at left_char
    show tim alt_pumped at center_char_kids
    tim           "She's Tedda, Mister Dorian! Mister Chung made her alive with his mind channeling!"
    hide tedda_human
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    chung_hee     "Took you a while just to get water."
    show tim normal at center_char_kids

    "Tedda huffed, puffing up her cheeks."
    hide chunghee

    show tedda_human at right_char with Dissolve(0.2)
    tedda "I'll have you know, I got very sidetracked!"

    "She marched over and placed the pitcher down with exaggerated effort."

    tedda "First, the kitchen was too dark. Spooky! So I had to light a lantern."

    "She held up a finger."

    tedda "Then, I saw a spider. A very rude spider, mind you! And I had to ask it politely to leave before I could pass."

    "Another finger went up."

    tedda "And THEN, I got thirsty carrying the water back, so I had to drink a little myself. Can't deliver water if I pass out, you know?"

    "She flashed me an innocent smile, then picked up a cup and pressed it into my hands."

    tedda "Now, drink, Mister Dorian. You need it after having that bad dream of yours."

    show dorian neutral at left_char
    "I frowned but didn't argue. She wasn't going to let up until I did, anyway. I took a slow sip, the cool water soothing my dry throat."

    tedda "There, see? Lady Elias will be just fine with me."

    "I sighed, wiping my mouth with the back of my hand."

    show dorian normal_alt_annoyed at left_char
    dorian "Lady Elias?"
    show dorian neutral at left_char
    "Tedda only giggled, her eyes twinkling."

    tedda "Just a little nickname. It suits her, don't you think?"
    
    "Then, we heard whirring. Roboto approached us."
    hide tedda_human
    show roboto happy at right_robot with Dissolve(0.2)
    roboto "Apologies for me being late, M-M-M-Master Dorian."
    roboto "Me and Miss T-T-Tedda here will take care of Elias. Don't worry."

    "His arms whirred as he gave me a reassuring thumbs-up."

    roboto "You can count on Robotoooo~"

    hide roboto
    show tedda_human at right_char with Dissolve(0.2)
    tedda "See? You'll be leaving Lady Elias in the best hands. Now go and take care of yourselves!"

    show tim alt_nervous at center_char_kids
    "Tim, who had been fidgeting near the table, quickly stepped forward."
    tim "Mister Roboto, how's Master Yuxuan?"

    "Roboto's head tilted, gears clicking as he processed the question. His screen showed a smiling face."
    hide tedda_human
    show roboto happy at right_robot with Dissolve(0.2)
    roboto "Master Yuxuan is doing fine. I gave him some s-s-s-s-snackss!"
    roboto "He's currently monitoring the situation ab-b-b-b-bove ground and b-b-b-below ground from his room."

    show dorian serious at left_char
    dorian "And what about Svante and Niko? Any word from them?"

    show roboto bad_mood at right_robot
    roboto "Unfortunately, we were not able to contact t-t-t-t-them."

    show dorian normal_alt_calm at left_char
    roboto "If you wish to go there, now would b-b-b-b-b-b-b-b-b *crashes*"

    show dorian neutral at left_char
    show roboto error at right_robot
    "His head snapped back with a loud clunk before he slumped forward slightly, his voice cutting off entirely."
    
    hide roboto
    show tedda_human at right_char with Dissolve(0.2)

    tedda "Umm… Is Roboto alright?"
    show tim think at center_char_kids 
    tim "Oh, um… Hold on a second."

    "Tim hurried behind Roboto, his small hands fumbling as he reached into his pocket. He pulled out a well-worn screwdriver, its handle smoothed from years of use."
    "With careful hands, he opened a panel on Roboto's back, adjusting a few loose wires."

    tim "Okay… this one connects here, and that one—yeah, that should do it…"

    "A few moments later, Roboto jolted back to life."

    hide tedda_human
    show roboto happy at right_robot with Dissolve(0.2)
    roboto "Bzzt—Reboot sequence complete… r-r-r-r-recalibrating sensors…"
    roboto "Robotooo is ready to seerrveeee~ You can count on Robotoo~"

    tedda "Yay! Tim, you're amazing!"

    "Tim scratched the back of his neck, looking away with a sheepish smile."

    tim       "It's nothing, Tedda. Just a small fix."
    hide roboto

    show chunghee normal_neutral at right_char with Dissolve(0.2)
    "Chung-hee stepped back, shaking his head in disbelief."

    chung_hee "Are all kids here that smart?"
    show dorian neutral at left_char
    dorian    "No."

    hide tim
    show roboto happy at center_robot with Dissolve(0.2)
    roboto "Y-Y-You should depart now if you're planning to leave."
    dorian "Alright. Let's head out."

    jump ch6_depart

# =============================================================================
# SECTION 10: LABEL CH6_DEPART — Tim Insists / Group Leaves
# =============================================================================

label ch6_depart:

    "Tim's hands curled tighter. He inhaled deeply, then straightened up, determination flickering behind his nervous eyes."
    hide roboto
    show tim alt_pumped at center_char_kids with Dissolve(0.2)

    tim "I can show you the way to Tianho!"
    tim "I-I know all the fastest roads! I can help!"

    show chunghee normal_neutral at right_char
    chung_hee "Tim, it's too dangerous for you. You would be safer here with Tedda and Roboto."
    dorian    "Chung-hee's right, Tim. Even if you're smart, you're still 5 years old. If anything were to happen to you, Yuxuan would—"
    show tim sad at center_char_kids
    tim       "Please, Mister Dorian! I don't wanna just sit here and do nothing!"

    show dorian normal_alt_calm at left_char
    "I sighed."

    show dorian neutral at left_char
    dorian "Dragon's bollocks. Fine. But you stay close to us, alright? And when we tell you to run, you run. No arguments. Got it?"

    show tim happy at center_char_kids
    "Tim's eyes widened in shock. Then he grinned, nodding rapidly."

    tim       "Yes, sir."
    show chunghee normal_neutral at right_char
    chung_hee "Let's head out."

    show dorian neutral at left_char
    "I gave Tedda and Roboto one last look."
    hide chunghee
    hide tim
    show tedda_human at right_char
    show roboto happy at center_robot
    with Dissolve(0.2)
    dorian    "Take care of Elias, okay?"

    "Tedda beamed, placing a hand on her hip."

    tedda "Obviously! Now go before you miss all the fun!"
    roboto      "C-C-Come home safe!"

    jump ch6_elevator


# =============================================================================
# SECTION 11: LABEL CH6_ELEVATOR — Elevator to Surface
# =============================================================================

label ch6_elevator:

    scene black with fade               
    stop music fadeout 1.5

    "Tim led us through a dimly lit corridor, the soft hum of machinery whispering through the walls. At the end stood a small, unassuming elevator, its metal frame dull and scratched with age."
    "No buttons. No panels. Just a smooth reflective surface."
    "Without a word, Tim stepped forward. A soft blue light flickered to life, scanning his face with a faint beep."

    door_voice "Attention. Facial recognition is currently in progress."
    door_voice "Identity confirmed. Going above ground. Take care, Mister Tim."

    "The elevator jolted, then ascended so smoothly it felt like we weren't moving at all. A moment later, the doors slid open with a quiet hiss."

    jump ch6_overlooking


# =============================================================================
# SECTION 12: LABEL CH6_OVERLOOKING — Overlooking Tianho at Night
# =============================================================================

label ch6_overlooking:

    # scene bg_tianho_overlooking_night with fade # PLACEHOLDER — rocky outcrop, Tianho below — use bg_tianho_city_night
    scene bg_tianho_deng_night with fade

    # play music ost_tianho_night fadein 2.0      # PLACEHOLDER — tense quiet night theme
    # play audio amb_tianho_night loop fadein 1.5 # PLACEHOLDER — ruin-night ambient

    "We stepped out into what looked like a rocky outcrop, hidden beneath a thick canopy of gnarled trees."
    "The entrance behind us disappeared, concealed beneath layers of foliage and jagged stone. The air smelled of damp earth and moss, the ground uneven beneath my boots."
    "Tim moved ahead, brushing past thick vines and branches that had been carefully arranged to keep the entrance secret."
    "He pointed past the trees, toward a cluster of makeshift structures nestled in the valley below."
    show tim normal at right_char_kids 
    show dorian serious at left_char
    with Dissolve(0.2)
    tim "That's Tianho."

    show dorian sad at left_char with Dissolve(0.2)
    "I followed his gaze, my stomach twisting at the sight before me."
    "I couldn't help but compare it to before. Before the Tragedy."
    hide tim
    hide dorian
    with Dissolve(0.1)
    "Before the flames. Before the screams."
    "Before the Death God. Before the Emperor. Before the Yaoguai King."
    "Tianho—if you could even call it that anymore—looked nothing like the grand city it had once been."
    "Gone were the towering pagodas, the intricate wooden bridges that once spanned the rivers like delicate ribbons."
    "It was a makeshift village, hastily built upon the bones of the old Tianho."
    "Wooden scaffolding clung to the remnants of once-magnificent buildings, their broken walls patched with mismatched planks and scavenged stone."
    "Tim adjusted the straps of his satchel and glanced up at me."

    show tim normal at right_char_kids 
    show dorian serious at left_char
    with Dissolve(0.2)
    tim "We'll have to walk the rest of the way. It's not far—just a short walk."

    show dorian neutral at left_char
    "I nodded, then turned to Chung-hee."
    hide tim
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    dorian    "Chung… earlier, you were floating. Why aren't you doing that now?"

    "Chung-hee's voice echoed in my mind, the way it always did."

    chung_hee "Floating attracts attention. Also, why would waste energy floating when I could just walk?"

    hide chunghee
    hide dorian
    with Dissolve(0.1)
    "We pressed forward."

    pause 2.0

    show dorian serious at left_char 
    show tim alt_nervous at right_char_kids
    with Dissolve(0.2)
    dorian "Stay alert."

    "Tim nodded, his expression growing serious."

    dorian "And Tim—stay close. Don't wander off."
    show tim alt_nervous at right_char_kids with Dissolve(0.1)
    tim    "Y-Yes, sir."

    show dorian angry at left_char
    "Then, I felt it—a ripple in the air, a shift in the stillness that sent a chill up my spine."
    hide tim
    show chunghee normal_v2 at right_char with Dissolve(0.2)
    "Chung-hee tensed beside me. He felt it too."
    "Then—footsteps."
    "Fast. Heavy."

    scene bg_tianho_deng_night with shock_cut
    play music audio.ost_battle loop
    show yaoguai at center_yg with Dissolve(0.2)
    "Out of nowhere, three Yaoguai burst into view, tearing through the dust and haze with inhuman speed."
    "Their grotesque forms flickered in and out of sight—limbs too long, spines twisted at unnatural angles, glowing eyes burning with raw hunger."

    voice audio.yg_scream
    yg "Raaaaaaawwrrr!!! Craaawwrrr!!"

    show yaoguai at right_yg 
    show chunghee normal_angry at left_char
    with Dissolve(0.2)
    "Chung-hee reacted instantly."

    chung_hee "Get back!"

    # play sound sfx_lightning_crack              # PLACEHOLDER — lightning SFX
    show chunghee normal_power_up at left_char
    "He thrust a hand forward, and the air pulsed— a sudden, invisible force slammed into the nearest Yaoguai, halting it mid-lunge."
    voice audio.yg_screech
    "The creature shrieked in fury, its claws scraping wildly against an unseen barrier, but it was pinned in place."
    hide yaoguai with Dissolve(0.1)

    show chunghee normal_angry at left_char
    chung_hee "Dorian, behind you!"
    hide chunghee

    show dorian angry at left_char
    show yaoguai at right_yg 
    with Dissolve(0.2)
    "I spun around and the yaoguai was already upon me."

    voice audio.yg_scream
    yg "Raaaaaaawwrrr!!!" 

    "Its clawed hands stretched forward, its gaping maw snapping open, teeth like jagged shards of obsidian."
    $ renpy.save("quick-1")
    "Too close. Too fast."

    jump ch6_yaoguai_encounter

# =============================================================================
# SECTION 13: LABEL CH6_YAOGUAI_ENCOUNTER — Timed Choice D1 (Earth or Stumble)
# =============================================================================
# Stumble = +1 yaoguai_tracker. Tracker ≥ 2 checked at ch6_yaoguai_common.
# =============================================================================

label ch6_yaoguai_encounter:
    $ _choice_timeout = 5.0
    menu:
        "Channel earth!":
            $ _choice_timeout = 0
            $ ch6_first_qtc = "earth"

            play sound sfx_earth  # PLACEHOLDER — earth spike SFX

            show dorian dragon_eyes at left_char
            "My foot slammed into the ground, and a pulse of raw energy surged through my veins."
            "A burst of sharpened rock erupted from the ground, spearing upward like a wall of jagged teeth."
            voice audio.yg_screech
            "The Yaoguai screeched, twisting in midair to avoid the worst of it, but the stone still caught its leg—a sickening crunch."

            voice audio.yg_scream
            yg "GRAAAHHH!!!"

            voice audio.yg_screech
            "It crashed onto its side, hissing in fury."
            hide yaoguai with Dissolve(0.1) 

        "Stumble!":
            $ _choice_timeout = 0
            $ ch6_first_qtc = "stumble"
            $ ch6_yaoguai_tracker += 1          # +1 yaoguai tracker

            show dorian angry at left_char
            "My foot caught on a loose rock."
            "Shiii—"
            "I tripped, my arms flailing as the world tilted."
            "The Yaoguai pounced. Its claws raked across my side—pain exploded through me as I hit the ground hard. The impact knocked the breath from my lungs."
            hide dorian
            hide yaoguai
            with Dissolve(0.1)

            show tim alt_nervous at left_char_kids with Dissolve(0.2)
            tim "Mister Dorian!!"

            "I barely registered his voice—the Yaoguai loomed over me."

            show yaoguai at right_yg with Dissolve(0.2)
            voice audio.yg_scream
            yg "Graaaaaaawwrrr!!!"
            
            scene cg_blindinglight with shock_cut
            # TODO: lightning sfx
            "Then, a flash of light. A bolt of lightning hit the beast."
            "The Yaoguai was sent flying—its body crashed through a tree, splintering bark on impact."
            scene bg_tianho_deng_night with Dissolve(0.8)
            show chunghee normal_power_up at right_char with Dissolve(0.2)
            "Chung-hee stood over me, eyes narrowed, hand still raised."

            chung_hee "Are you alright?"
            show dorian serious at left_char with Dissolve(0.2)
            "I sucked in a shaky breath, pain flaring through my ribs."

            dorian "T-Thanks… Sorry."

    $ _choice_timeout = 0
    hide chunghee
    show tim alt_nervous at right_char_kids with Dissolve(0.2)
    "Tim's panicked scream split the air."

    tim "Mister! A-Another one!"
    show dorian angry at left_char
    "I turned just in time to see another Yaoguai sprinting toward us from the shadows, its grotesque form blurring with unnatural speed."

    tim "Mister! Make a barrier! Quick!"

    jump ch6_yaoguai_barrier


# =============================================================================
# SECTION 14: LABEL CH6_YAOGUAI_BARRIER — Timed Choice D2 (Earth or Wind barrier)
# =============================================================================
# Wind = +1 yaoguai_tracker (wrong). Both lead to ch6_yaoguai_common.
# =============================================================================

label ch6_yaoguai_barrier:
    $ _choice_timeout = 5.0
    menu:
        "Make a barrier made out of earth.":
            $ _choice_timeout = 0
            $ ch6_second_qtc = "earth"
            hide tim
            show yaoguai at right_yg 
            show dorian dragon_eyes at left_char
            with Dissolve(0.2)

            "I slammed my hands together, channeling my energy into the ground."
            "The earth rumbled." with hpunch
            play sound sfx_earth
            "A wall of solid rock erupted between us and the Yaoguai—thick, sturdy, unyielding. The creature crashed into it headfirst, letting out a choked snarl as the impact sent it sprawling."
            voice audio.yg_scream
            yg "GRAAAH—!!"

            hide yaoguai with Dissolve(0.1)
            # TODO: scratching sfx
            "I could hear it scratching, clawing, trying to scale the wall, but I had bought us time."
            show dorian serious at left_char

            show tim happy at right_char_kids with Dissolve(0.2)
            tim "You did it, sir Dorian!"

            show dorian normal_alt_confident at left_char
            "I exhaled sharply, wiping sweat from my brow."

        "Make a barrier made out of wind.":
            $ _choice_timeout = 0
            $ ch6_second_qtc = "wind"
            $ ch6_yaoguai_tracker += 1          # +1 yaoguai tracker
            hide tim
            show yaoguai at right_yg
            show dorian dragon_eyes at left_char
            with Dissolve(0.2)
            play sound audio.sfx_wind
            # TODO: scene cg_dorian_yg_fight_night with shock_cut
            "I thrust my hands forward, summoning the wind—a forceful gust howled to life, swirling between us and the oncoming Yaoguai."
            "For a split second, I thought it would be enough."
            show dorian angry at left_char
            "I was wrong."

            # TODO: snarling sfx
            "The Yaoguai snarled and dove straight through the whirlwind, using the momentum to propel itself faster."

            tim "M-Mister—!!"

            "I barely had time to react before it was on me."

            play sound audio.sfx_claw  
            "Sharp claws raked across my shoulder. Pain exploded through me as I staggered back."

            voice audio.yg_scream
            yg "RRRAAAAGH!!!"

            "It reared back for another strike—"
            "BOOM!"
            # TODO: force field sfx
            "An invisible force slammed into it, sending the creature flying into the dirt."
            stop sound fadeout 0.5
            hide yaoguai

            show chunghee normal_neutral at right_char with Dissolve(0.2)
            chung_hee "Dorian, take care."

            "I clutched my shoulder, my breath shaky."

            show dorian serious at left_char
            dorian "I thought the wind would stop it…"

    $ _choice_timeout = 0
    jump ch6_yaoguai_common


# =============================================================================
# SECTION 15: LABEL CH6_YAOGUAI_COMMON — Tracker Check / Game Over or Continue
# =============================================================================

label ch6_yaoguai_common:
    if ch6_yaoguai_tracker >= 2:
        # GAME OVER — blood loss
        stop sound
        stop music fadeout 2.0

        show dorian normal_alt_tense at left_char
        "Pain flared across my side. Warm, wet."
        "I pressed a hand to my ribs, and my fingers came away slick with blood."
        "Damn it. When did I—?"

        show tim alt_nervous at center_char_kids with Dissolve(0.2)
        tim "M-Mister Dorian! You're bleeding!"

        "I staggered, my vision swaying. Too much blood. Too fast."

        show chunghee normal_angry at right_char
        chung_hee "Dorian! We need to find Niko. Fast!"

        "But the ground tilted beneath me, my legs buckling. I hit my knees."
        scene black with fade                # PLACEHOLDER — black screen
        "Darkness…"
        "Please… Not now…"

        stop music fadeout 1.0
        stop audio
        pause 1.5   

        "Reload your last save and avoid taking hits from the Yaoguai."

        pause 1.0
        jump game_over

    else:
        show dorian serious at left_char
        "The remaining Yaoguai snarled, their bodies twitching, their eyes locked on us."

        dorian    "They're… a lot faster than I remember."
        hide tim
        show chunghee normal_neutral at right_char with Dissolve(0.2)
        chung_hee "We need to end this quickly."
        chung_hee "Stay close to me. I have this."

        show chunghee normal_power_up at right_char
        "His eyes flashed. He lifted his arms."
        "And then— Lightning."

        # play sound sfx_lightning_crack          # PLACEHOLDER — lightning SFX
        hide chunghee
        hide dorian
        show yaoguai at center_yg 
        with Dissolve(0.2)
        "A storm of raw electricity erupted from his fingertips, forking through the air."
        "The Yaoguai screeched as the bolts struck one, then another, then the last—lightning chaining them together in a web."

        voice audio.yg_scream
        yg "GRAAAHHHHH!"

        "Their bodies twisted, convulsing violently—"
        play sound audio.monster_death
        hide yaoguai with Dissolve(0.1)
        "Then they were gone. Soot."
    
        "Silence followed."

        "Chung-hee exhaled, lowering his hands. Tim clung to my side, still tense."
        "I let out a slow breath, my pulse still pounding."

        show dorian normal at left_char
        show chunghee normal_neutral at right_char
        with Dissolve(0.2)
        dorian    "…Remind me to never piss you off, Chung."
        chung_hee "…"

        "Chung-hee just gave me a knowing look."
        show dorian serious at left_char

        jump ch6_tianho_approach


# =============================================================================
# SECTION 16: LABEL CH6_TIANHO_APPROACH — Running to Tianho
# =============================================================================

label ch6_tianho_approach:

    "We ran—feet pounding against the rough earth, the wind howling past us."
    show tim normal at center_char_kids with Dissolve(0.2)
    "Tim clung to me, his small arms wrapped tightly around my neck as I carried him."

    tim "Go left! That way!"

    hide chunghee
    hide tim
    show yaoguai at right_yg 
    with Dissolve(0.2)
    "I barely had time to process his words before two more Yaoguai emerged from the shadows—twisted, snarling creatures with glowing, predatory eyes."
    "I didn't hesitate."

    play sound sfx_earth          # PLACEHOLDER — earth spike SFX

    show dorian dragon_eyes at left_char with Dissolve(0.2)
    "With a surge of power, I slammed my foot to the ground. The earth trembled beneath us—then rose."
    "Jagged spikes of stone erupted from the ground in a split second, impaling both creatures mid-leap."
    hide yaoguai
    
    voice audio.monster_death
    "A sickening crunch. A strangled howl."
    "Then—silence."
    stop music fadeout 2.0
    show dorian serious at left_char with Dissolve(0.1)
    "I exhaled sharply. No time to waste."
    "We pushed forward."

    # scene bg_tianho_post_tragedy_night with dissolve # PLACEHOLDER — Tianho ruins at night — use bg_tianho_city_on_fire
    scene tianho_food_stalls_destroyed with fade
    stop music fadeout 2.0
    stop sound

    "We reached Tianho."
    "It had been five years since the Tragedy of Tianho—five years since the city fell."
    "Now, it was a makeshift town, pieced together from the ruins. The skeleton of a place that once thrived."
    "But there were flickering business lights. Small lanterns swayed gently in the night breeze, their glow casting soft pools of light onto the cracked streets."
    "A few shops had reopened—noodle carts pushed against alley walls, tiny market stalls selling whatever goods they have to offer."
    "It was quiet. The air was heavy. Suffocating."
    "We walked down streets lined with Yaoguai corpses."
    "Twisted, grotesque bodies lay motionless in the dust, limbs contorted in unnatural angles."
    "Some had deep slashes, others looked like they had rotted from the inside out."
    show dorian serious at left_char 
    show tim alt_nervous at center_char_kids
    show chunghee normal_neutral at right_char
    with Dissolve(0.2)
    "I lowered Tim gently to the ground. He stumbled a bit, still shaken."
    "Chung-hee immediately pulled him close, his expression unreadable."

    chung_hee "Stay close to me."

    "Tim nodded, his small fingers clutching the hem of Chung-hee's sleeve."
    "Then… I've heard voices. A hushed whisper from the shadows."

    jump ch6_jiang_gao

# =============================================================================
# SECTION 17: LABEL CH6_JIANG_GAO — Cheng Industries Entrance / Jiang and Gao
# =============================================================================

label ch6_jiang_gao:
    scene bg_tianho_city_night with fade

    show soldier_gao at right_char
    show soldier_jiang at left_char
    with Dissolve(0.2)
    gao  "Gao, look! People!"
    jiang "Hmm… Wait, Jiang… Is that—"
    gao   "Paladin Dorian? In Li Mengtia's name! It's really you!"
    jiang "Hey! Hey! Over here, sir!"
    
    hide soldier_jiang
    show dorian neutral at left_char with Dissolve(0.2)
    "I turned toward the sound, heart pounding, and there they were—peering out from a ruined storefront, their bodies pressed into the shadows."
    "They weren't in armor. No swords at their hips. Instead, they wore Cheng Industries shirts—stained, but unmistakable."
    "Relief washed over me."

    show dorian smile at left_char
    dorian "Jiang! Gao!"

    "I barely held back the urge to grab them, to make sure they were real."
    "Gao smirked and pointed at his shirt."
    show dorian neutral at left_char

    gao  "We work for Cheng Industries now! Here at Cheng's, we make ch—"

    "Jiang rolled his eyes."

    hide soldier_gao
    show soldier_jiang at right_flip with Dissolve(0.2)
    jiang "Change. *Hums a tone* Yes, anyway…"

    "He cleared his throat."

    jiang "You must be looking for Miss Weng… She's with your friends."
    dorian "You know Miss Weng?"
    jiang "She's our supervisor… in a way."
    hide soldier_jiang
    show soldier_gao at right_char with Dissolve(0.2)
    gao   "She's with the doctor, and the guy with the pink hair."
    hide soldier_gao
    show soldier_jiang at right_flip with Dissolve(0.2)
    jiang "Idiot. It's not pink. It's violet."
    hide soldier_jiang
    show soldier_gao at right_char with Dissolve(0.2)
    gao   "Sir, it's been a while! How are—"

    hide soldier_gao
    show soldier_jiang at right_flip with Dissolve(0.2)
    jiang "Don't raise your voice too much, Gao. That thing might see us."
    show dorian serious at left_char

    dorian "He's right, Gao. Where are the others?"

    hide soldier_jiang
    show soldier_gao at right_char with Dissolve(0.2)
    gao   "H-Hiding, sir. Many are wounded. They're hiding inside this store."

    hide soldier_gao
    show soldier_jiang at right_flip with Dissolve(0.2)
    jiang "The doctor is trying to heal the injured."

    show chunghee normal_neutral at center_char with Dissolve(0.2)
    "Chung-hee's sharp gaze flicked between us."
    chung_hee "Do you know these people, Dorian?"

    show dorian neutral at left_char
    dorian    "Yeah, I've fought with them during the Tragedy of Tianho."

    "Tim's worry hadn't left his face."
    hide chunghee
    show tim alt_nervous at center_char_kids with Dissolve(0.2)
    tim "But… they're hiding from something… Shouldn't we hide too?"

    show dorian serious at left_char
    "I glanced at him. He's right. It's too dangerous for him to be out in the open. I gestured toward Jiang."

    jiang "Got it, Paladin. We'll make sure he's safe."

    "He approached Tim and extended his hand."

    jiang "Come with us, little one."
    tim   "Um… okay. Take care mister Dorian."

    "They took him to hide behind the storefront, their eyes still watching."
    "Then—"
    "The ground trembled." with hpunch

    jump ch6_hundun_appears


# =============================================================================
# SECTION 18: LABEL CH6_HUNDUN_APPEARS — The Hundun Emerges / Tim Explains
# =============================================================================

label ch6_hundun_appears:

    # scene bg_tianho_post_tragedy_night with dissolve # PLACEHOLDER — Tianho ruins — use bg_tianho_city_on_fire
    scene bg_tianho_city_night with dissolve

    # TODO: play sound fadein 0.5      # PLACEHOLDER — Hundun theme

    "A wet, gurgling sound slithered through the alleyways of Tianho."
    "It wasn't footsteps. It wasn't breathing."
    "It was something else."
    "A noise so unnatural it sent a shiver down my spine."

    show soldier_jiang at left_char
    show soldier_gao at right_char
    with Dissolve(0.2)   
    
    jiang "Li Mengtia, save us…"
    gao   "D-Don't you wanna hide with us, Paladin Dorian?"

    "And then I saw it."
    scene cg_hundun_attack with shock_cut
    # play sound sfx_hundun_whisper               # PLACEHOLDER — Hundun whisper SFX
    "A massive, shifting mass of flesh and darkness loomed above us, writhing and twisting in unnatural ways."
    "Its form was never still."
    "Limbs sprouted and folded, then vanished back into the mass."
    "Clawed fingers stretched, twitched, then melted away."
    "Jagged mouths appeared across its hide, filled with crooked, gnashing teeth."
    "The lanterns flickered erratically, the air warping around us."

    "Tim's voice was barely a whisper."

    tim "A… Hundun…"

    scene bg_tianho_city_night with dissolve
    show dorian serious at left_char
    show chunghee normal_neutral at right_char
    show tim alt_nervous at center_char_kids
    with Dissolve(0.2)
    "Chung-hee approached me, his gaze not leaving the monster's."

    chung_hee "I take it this isn't just another Yaoguai?"
    dorian    "Don't you have this creature in Kyeongjang?"
    chung_hee "No, I- I haven't read about this. This is foreign to me…"

    show tim think at center_char_kids
    tim       "Hundun… it means 'chaos.' It's not like the others. I've read about it. In Li Mengtia's bibliography page 237."
    dorian    "How so?"
    tim       "Chaos. Confusion. It moves in ways you can't predict. If you watch it too long, you'll start seeing things that aren't real."
    show tim alt_nervous at center_char_kids
    tim       "Hunduns confuse people and… they eat them."

    "Gao took an uneasy step back."
    hide chunghee
    hide tim
    show soldier_jiang at right_flip
    show soldier_gao at center_char
    with Dissolve(0.2)

    gao   "Holy… So that's why people have been hiding."
    jiang "Once people started seeing that thing, they're minds are all muddied."
    show dorian normal_alt_annoyed at left_char
    dorian "Tch. Just my lucky day."
    show dorian serious at left_char

    scene cg_hundun_attack with dissolve

    "The Hundun rippled."
    "Its many mouths opened at once."
    "And then—it spoke."
    "Not in words."
    "Not in a voice."
    "But in echoes."
    "Whispers."

    hundun "Mhmhmhmhmhm…"

    "The air itself warped, twisting like a heat mirage. The world wavered at the edges of my vision, everything doubling, then tripling—Chung-hee, Tim, Jiang, Gao, the Hundun."

    scene tianho_hundun_haze with Dissolve(0.4)
    show dorian angry at left_char
    show hundun at right_hd
    with Dissolve(0.2)
    dorian "W-What the…"

    "Too many."
    "My grip tightened into fists, my nails digging into my palms as I fought to keep my focus."
    "The monster's many mouths split open, but no sound came. Instead, the echoes surged through my mind, like a choir, curling around my thoughts, bleeding into them."

    hundun "Mhmhmhmhmhm…"

    "I blinked—once, twice—only to find that my own hands were shifting before my eyes, fingers elongating and twisting. The ground beneath me felt wrong—soft, then hard, then liquid."
    "Tianho itself flickered before my eyes."
    "No longer a struggling city in recovery, but a warped nightmare—buildings bending at impossible angles, their windows wide and dark like gaping mouths."
    "The sky above churned in a swirling abyss, the color of rotting ink."

    hide dorian
    hide hundun

    show soldier_jiang at left_char
    show soldier_gao at right_char
    with Dissolve(0.2)
    jiang "Come here, Paladin! Hahaha! We won't bite!"
    gao   "Hahahaha! Your blood will be perfect for our dinner!"
    hide soldier_jiang
    hide soldier_gao

    show dorian normal_alt_tense at left_char
    show hundun at right_hd
    with Dissolve(0.2)
    "My breath hitched."
    "All of a sudden, Chung-hee's voice echoed in my mind."

    chung_hee "Dorian. Listen to me."

    jump ch6_hundun_illusion_1


# =============================================================================
# SECTION 19: LABEL CH6_HUNDUN_ILLUSION_1 — Elara and Family Illusion
# =============================================================================

label ch6_hundun_illusion_1:

    scene bg_dorians_room with shock_cut # PLACEHOLDER — Dorian's Tianho room (illusion), no asset declared
    # play music ost_illusion_family fadein 0.5   # PLACEHOLDER — distorted warmth theme
    pause 1.5
    "It was sharp, cutting through the suffocating fog in my mind."

    chung_hee "What you're seeing is the Hundun. It's digging into your thoughts, warping your perception. You must trust me."

    show dorian serious at left_char with Dissolve(0.2)
    "I swallowed hard, clutching my head as another vision flickered before me—"
    show dorian sad at left_char
    show elara at right_char with Dissolve(0.2)
    "Elara."
    "She stood just ahead, her red hair flowing as she reached out to me. Behind her, Emily, Sarah, Daniel, and Lucas—small hands outstretched, eyes wide with tears."

    dorian "E-Elara?! What are you doing here—"

    show lucas at center_char_kids with Dissolve(0.2)
    lucas "Dad come back!"
    hide lucas
    show emily at center_char_kids with Dissolve(0.2)
    emily "We miss you!"
    hide emily
    show daniel at center_char_kids with Dissolve(0.2)
    daniel "We missed you so much!"
    hide daniel
    show sarah at center_char_kids with Dissolve(0.2)
    sarah "Come here, dad!"
    hide sarah with Dissolve(0.1)
    elara "Dorian."

    "She stepped forward, arms outstretched, a smile pulling at her lips."

    elara "Here. I missed you. Take one more step."

    "My entire body locked up."
    "My heart pounded."
    "I wanted to."
    "One step."
    "One step closer, and I could hold them again."
    "My breath shook."
    "My legs moved."
    "One step—"
    "NO."

    # scene bg_tianho_food_stalls_fire with shock_cut # PLACEHOLDER — food stalls on fire (nightmare) — use tianho_food_stalls_fire
    scene tianho_food_stalls_fire with shock_cut

    show dorian angry at left_char 
    show elara at right_char
    with Dissolve(0.2)

    "I clenched my jaw."
    "The illusions flickered."
    "The children's eyes darkened—turning black, hollow, hungry."
    show elara at distort_mild with Dissolve(0.2)
    "Elara's face twitched."
    "For a fraction of a second, the warmth in her smile cracked."

    elara "Dorian… I won't ask again."

    dorian "You're not Elara."

    "I slammed my fists together."


    show dorian dragon_eyes at left_char with Dissolve(0.1)
    "Flames erupted from my hands—bright, wild, furious."
    play sound audio.sfx_fire_explosion
    "I thrust my arms forward, sending a torrent of fire surging toward them."
    "The illusion shattered like glass."
    camera at bigshake(5.0, rate=0.020, time=0.09), shattered_glass_transform
    with shattered_glass_transition
    hide elara with Dissolve(0.1)
    "The warm, familiar faces of my loved ones morphed."
    camera

    "Elara's soft features melted into a grotesque, many-mouthed horror. The children's arms stretched into clawed appendages. Their eyes turned into endless, soulless pits."
    show hundun at silhouette_hd with Dissolve(0.8)
    # play sound sfx_illusion_shatter             # PLACEHOLDER — shatter SFX

    "Its true form coiled in the darkness—its many mouths stretched wide, jagged teeth gnashing in fury."
    "It screamed."
    show hundun at silhouette_reveal_hd with Dissolve(0.3)
    "Not one voice. Not two. A thousand voices."

    hundun "You. Reject. Us. Hmmmmrnmmmm…"

    "Its flesh blackened and split, its writhing limbs thrashing wildly."
    "Reality warped, twisted, fractured."

    hundun "Your fire will not cleanse. Your fire will not save. Your fire will not bring them back."
    hundun "Hrnnnrrnnn…"

    hide dorian
    jump ch6_vasily_room


# =============================================================================
# SECTION 20: LABEL CH6_VASILY_ROOM — Vasily Illusion / Mjoll Throne Room
# =============================================================================

label ch6_vasily_room:

    # scene bg_mjoll_palace_throne with shock_cut # PLACEHOLDER — Mjoll throne room (illusion) — use mjoll_palace_throne
    scene mjoll_palace_throne with shock_cut
    # play music ost_vasily fadein 0.3   # PLACEHOLDER — eerie familiarity theme

    "The world collapsed in on itself."
    "The ruined streets of Tianho vanished, replaced by a throne room. A lavish throne room in Mjoll. As I remembered it."

    show vasily alt_think at center_char with Dissolve(0.2)
    vasily "My, my. Dorian my friend. Still as temperamental as ever, I see."
    vasily "Do tell me, how's the Prince?"

    show vasily neutral at right_char 
    show dorian serious at left_char
    with Dissolve(0.2)
    dorian "Vasily…"

    "The words barely left my lips before he multiplied."
    show dorian angry at left_char
    show vasily alt_savage at right_char
    "One Vasily. Then two. Then four. Then dozens—standing at every corner of the throne room, each an exact copy, each watching me with those sharp, amused eyes."

    chung_hee "Be careful, Dorian… This is a trap."
    chung_hee "Don't be rash. Rely on what I say."

    "I could feel it. The pressure building around me."
    "Vasily was channeling light."
    scene vasily_attack with shock_cut
    "The illusions layered on top of each other, twisting, warping, shifting. The throne room flickered—too bright, too dark, too blinding."
    "My heartbeat pounded in my ears."

    vasily "What's the matter, old friend? Confused?"
    scene mjoll_palace_throne with shock_cut

    show dorian angry at left_char 
    show vasily alt_aggressive at right_char
    with Dissolve(0.2)
    $ renpy.save("quick-1")
    "I ground my teeth. I had to make a decision—fast."

    jump ch6_vasily_qtc


# =============================================================================
# SECTION 21: LABEL CH6_VASILY_QTC — Timed Choice D3 (HARD GATE)
# =============================================================================
# Choices 1 and 2 = GAME OVER. Choice 3 (close eyes) and 4 (fire room) = correct.
# =============================================================================

label ch6_vasily_qtc:
    $ _choice_timeout = 5.0
    menu:
        "Attack the Vasily who speaks the most.":
            $ _choice_timeout = 0
            $ ch6_vasily_qtc = "speak_most"

            show dorian dragon_eyes at left_char with Dissolve(0.1)
            "I struck first—but my hand went straight through the illusion."
            
            show dorian angry at left_char
            dorian "W-What?"

            show vasily alt_savage at right_char
            vasily "No hard feelings, old friend."

            scene cg_blindinglight with shock_cut
            "A blinding flash of bright light came. Light seared through my side, burning hot, ripping through flesh like molten steel."

            dorian "Ahhhh!!! F—"
            "I hit the ground hard, vision swimming, my nerves screaming in agony. Above me, Vasily loomed, smirking, his sharp eyes gleaming in the flickering light."

            vasily "It hurts. Doesn't it, old friend?"
            vasily "Call it karma. Or revenge."

            chung_hee "DORIAN, NO!"

            "And then darkness swallowed me whole."
            scene black with fade    
            stop music fadeout 1.0
            stop audio
            pause 1.5
            jump game_over

        "Attack the Vasily closest to you.":
            $ _choice_timeout = 0
            $ ch6_vasily_qtc = "closest"
            stop sound

            show dorian dragon_eyes at left_char with Dissolve(0.1)
            "I struck first—but my hand went straight through the illusion."
            
            show dorian angry at left_char
            dorian "W-What?"

            show vasily alt_savage at right_char
            vasily "No hard feelings, old friend."

            scene cg_blindinglight with shock_cut
            "A blinding flash of bright light came. Light seared through my side, burning hot, ripping through flesh like molten steel."

            dorian "Ahhhh!!! F—"
            "I hit the ground hard, vision swimming, my nerves screaming in agony. Above me, Vasily loomed, smirking, his sharp eyes gleaming in the flickering light."

            vasily "It hurts. Doesn't it, old friend?"
            vasily "Call it karma. Or revenge."

            chung_hee "DORIAN, NO!"

            "And then darkness swallowed me whole."
            scene black with fade            # PLACEHOLDER — black screen
            stop music fadeout 1.0
            stop audio
            pause 1.5
            jump game_over

        "Close your eyes and rely on Chung-hee's mind channeling.":
            $ _choice_timeout = 0
            $ ch6_vasily_qtc = "close_eyes"
            stop sound

            show dorian normal_alt_calm at left_char with Dissolve(0.1)
            "I shut my eyes, forcing myself to ignore the illusions."

            show vasily alt_aggressive at right_char
            vasily "What's the matter, old friend?"
            vasily "Open your eyes before you get yourself killed! Hrmmmmmnnnn…."

            "Then—a voice cut through the noise."

            chung_hee "Third person from the left."

            show dorian dragon_eyes at left_char with Dissolve(0.1)
            "I didn't hesitate."
            play sound audio.sfx_fire_explosion
            "I lunged—flames igniting along my fist."

            show vasily alt_mad at right_char
            vasily "Wha-?!"

            "The moment my fire struck him, the illusions shattered like glass, breaking into shards of twisted, flickering light."
            camera at bigshake(5.0, rate=0.020, time=0.09), shattered_glass_transform
            with shattered_glass_transition
            # play sound sfx_illusion_shatter     # PLACEHOLDER — shatter SFX

            vasily "AAHHH!!!"
            camera
            hide vasily
            show hundun at right_hd with Dissolve(0.2)
            hundun "AHHHHH!!! You!!"

        "Use fire channeling to light up the entire room.":
            $ _choice_timeout = 0
            $ ch6_vasily_qtc = "fire_room"
            stop sound

            # play sound audio.sfx_fire_explosion        # PLACEHOLDER — fire SFX

            show dorian dragon_eyes at left_char with Dissolve(0.1)
            "I threw my hands up, summoning fire from deep within."

            play sound audio.sfx_fire_explosion
            "The flames exploded outward, engulfing the entire room in a brilliant, raging inferno."

            show vasily alt_savage at right_char
            vasily "Graahhh!!"

            hide vasily
            show hundun at right_hd with Dissolve(0.2)
            "The Hundun howled, its monstrous form recoiling from the fire."

            hundun "NOOOOOO!!!"

    $ _choice_timeout = 0
    jump ch6_rulers_illusion


# =============================================================================
# SECTION 22: LABEL CH6_RULERS_ILLUSION — 4 Rulers Illusion
# =============================================================================
# Gustav, Olympia, Min-joon, Vasily. Chung-hee gives the strike order.
# =============================================================================

label ch6_rulers_illusion:

    # scene bg_mjoll_square_festive with shock_cut # PLACEHOLDER — Mjoll square (illusion) — use bg_mjoll_icelands
    scene bg_mjoll_icelands with shock_cut

    show vasily alt_savage at center_char
    "Vasily's grin widened, a slow, lazy smirk spreading across his face."

    vasily "Time for some friends from the upper society."
    
    show vasily neutral at center_char
    "He snapped his fingers."
    "The air twisted."

    show king_gustav at right_char
    show olympia at left_char
    with Dissolve(0.2)
    "King Gustav. Empress Olympia. Emperor Min-joon."
    "Their figures stood tall and regal. I took an instinctive step back, my chest tightening."
    "Their gazes bore into me, their expressions unreadable—but their intentions were clear. Destroy me."

    show vasily alt_aggressive at center_char
    vasily "Do you, by chance, remember them, old friend?"

    hide king_gustav
    hide olympia
    show vasily alt_aggressive at right_char
    show dorian angry at left_char
    with Dissolve(0.2)
    dorian "What kind of sick game is this?"

    hide vasily
    show king_gustav at right_char with Dissolve(0.2)
    gustav_illusion "DIE!"

    hide king_gustav
    show olympia at right_char with Dissolve(0.2)
    olympia_illusion "You burn everything you touch, Paladin."

    # TODO: add wind sfx
    "The winds around her howled, her presence distorting the air itself."

    olympia_illusion "You will die, you monster!"

    show dorian angry at left_char
    "I clenched my fists."

    hide olympia
    minjoon_illusion "Your head will be ours… It will look good on a pike."

    show vasily alt_savage at right_char with Dissolve(0.2)
    "My breath hitched."
    "My flames wavered—as if responding to my own doubt."
    show dorian normal_alt_tense at left_char with Dissolve(0.1)
    "I could feel their power pressing down on me."
    "Could see the unwavering conviction in their eyes."
    "Was this an illusion? Or was it something more?"
    "A cold wave of fear crept into my chest, tightening like a vice."

    $ renpy.save("quick-1")
    chung_hee "Dorian. Listen to me. I can feel your fear. You must let it go."

    show dorian normal_alt_calm at left_char
    "I sucked in a sharp breath."

    dorian "…*breathes deeply* Hrnnn…"

    chung_hee "Do not let your mind betray you. Those are merely illusions."
    chung_hee "Strike first at the Honorable Empress."
    chung_hee "And then the illusion of… pyeha."

    "For the briefest moment, his mind faltered—but it was gone in an instant."

    chung_hee "My father."
    chung_hee "Then, that venomous serpent of a king."
    chung_hee "And lastly, you shall strike down whoever is left."

    "The area shuddered as the rulers prepared their assault."
    show dorian serious at left_char with Dissolve(0.1)
    "I gritted my teeth, sweat beading down my temple. Even though I knew they weren't real, their presence was so overwhelming that doubt still clawed at the edges of my mind."
    hide dorian
    show king_gustav at right_char
    show vasily alt_savage at center_char 
    show olympia at left_char
    with Dissolve(0.2)
    "Their gazes pierced through me, judgment dripping from every word, every movement."
    "On the far left, Gustav stood unshaken, his broad form towering, his expression carved from stone."
    "Cracks spiderwebbed beneath his feet, the very earth groaning under the weight of his rage."

    gustav_illusion "Prepare to die, Dorian!"

    "To his right, Empress Olympia hovered mid-air, her robes billowing violently in a cyclone of shrieking wind."
    "A hurricane twisted around her, distorting the air itself, flickers of lightning threading through the storm."

    olympia_illusion "You will rue this day!"

    "At the center, Vasily stood, his form bathed in radiant light, his smirk so casual it sent chills down my spine. He raised his hand, and daggers of light formed at his fingertips, their edges pulsing with raw, celestial power."

    vasily "A pity it has to end this way, dear friend."

    "On the far right, Emperor Min-joon stood, but he did not move. His eyes gleamed an unnatural violet, swirling with shifting patterns."

    minjoon_illusion "Your family died because of you. Death will be too kind of a punishment for monsters such as yourself…"

    hide king_gustav
    hide olympia
    show dorian angry at left_char 
    show vasily alt_aggressive at right_char 
    with Dissolve(0.2)
    "I staggered, my breath hitching— My body felt disconnected."

    chung_hee "Wait for it, Dorian."

    "The four figures stepped forward, power building to a breaking point—"
    show dorian dragon_eyes at left_char
    "I tightened my fists. My flames surged."

    vasily "LIGHTS OUT!"

    scene black with shock_cut           

    "Then—pitch blackness."
    "The world vanished."
    "The ground beneath me disappeared into an abyss. I couldn't see. All I can see are shadows."

    chung_hee "NOW!! Hit them before they strike!"
    jump ch6_darkness_qtc


# =============================================================================
# SECTION 23: LABEL CH6_DARKNESS_QTC — Timed Choice D4 (Shadow Order — HARD GATE)
# =============================================================================
# Only choice 2 is correct:  2nd, 4th, 1st, 3rd  (Olympia → Min-joon → Gustav → Vasily).
# Choices 1, 3, 4 = GAME OVER.
# =============================================================================

label ch6_darkness_qtc:

    $ _choice_timeout = 5.0
    menu:
        "Hit the second shadow first, then the first, then the fourth, then the third.":
            $ _choice_timeout = 0
            $ ch6_darkness_qtc = "order_wrong_1"
            stop sound

            dorian "GRAAHHH!!"

            "My flames surged, my fists colliding with—nothing."

            dorian "W-What?! But how?!"

            olympia_illusion "Oh, Paladin. Did you think you could strike down the wind? The Dragon of Gale has lost his wits."
            gustav_illusion "Foolish. Utterly foolish."
            minjoon_illusion "How disappointing. How unworthy."
            vasily  "You always were predictable, dear friend."

            "A sudden pressure exploded in my chest—"
            "Then—searing, unbearable pain."

            dorian "AHHH!!"

            vasily "THIS is my revenge. Farewell, dear friend."
            chung_hee       "DORIAN! NO!"
            vasily "HAHAHAHAHAHA!!"

            pause 1.5
            "Reload your last save. Trust Chung-hee's instructions precisely."
            jump game_over

        "Hit the second shadow first, then the fourth, then the first, then the third.":
            $ _choice_timeout = 0
            $ ch6_darkness_qtc = "order_2"
            stop sound

            "I launched forward—my flames twisted in my palms, roaring to life."
            "Flames hit the targets. They shrieked as the fire engulfed them."

            # play sound sfx_illusion_shatter     # PLACEHOLDER — shatter SFX

            olympia_illusion "AHHH!!!"

            camera at bigshake(5.0, rate=0.020, time=0.09), shattered_glass_transform
            with shattered_glass_transition
            "Her form cracked, like glass under heat—then shattered."
            camera

            minjoon_illusion "AH! AH! AHHH!!!"

            "Emperor Min-joon vanished, his form dissolving like ash on the wind."

            gustav_illusion "Curse…. CURSE YOU!!!! I WON'T FALL TO FIRE!!"

            "His form shattered as he continued to mutter curses."

            hundun "Hmmmhmmmm….."

            "Vasily smirked."

        "Hit the fourth shadow first, then the first, then the second, then the third.":
            $ _choice_timeout = 0
            $ ch6_darkness_qtc = "order_wrong_3"
            stop sound
            dorian "GRAAHHH!!"

            "My flames surged, my fists colliding with—nothing."

            dorian "W-What?! But how?!"

            olympia_illusion "Oh, Paladin. Did you think you could strike down the wind? The Dragon of Gale has lost his wits."
            gustav_illusion "Foolish. Utterly foolish."
            minjoon_illusion "How disappointing. How unworthy."
            vasily  "You always were predictable, dear friend."

            "A sudden pressure exploded in my chest—"
            "Then—searing, unbearable pain."

            dorian "AHHH!!"

            vasily "THIS is my revenge. Farewell, dear friend."
            chung_hee       "DORIAN! NO!"
            vasily "HAHAHAHAHAHA!!"

            pause 1.5
            "Reload your last save. Trust Chung-hee's instructions precisely."
            jump game_over

        "Hit the fourth shadow first, then the second, then the first, then the third.":
            $ _choice_timeout = 0
            $ ch6_darkness_qtc = "order_wrong_4"
            stop sound

            dorian "GRAAHHH!!"

            "My flames surged, my fists colliding with—nothing."

            dorian "W-What?! But how?!"

            olympia_illusion "Oh, Paladin. Did you think you could strike down the wind? The Dragon of Gale has lost his wits."
            gustav_illusion "Foolish. Utterly foolish."
            minjoon_illusion "How disappointing. How unworthy."
            vasily  "You always were predictable, dear friend."

            "A sudden pressure exploded in my chest—"
            "Then—searing, unbearable pain."

            dorian "AHHH!!"

            vasily "THIS is my revenge. Farewell, dear friend."
            chung_hee       "DORIAN! NO!"
            vasily "HAHAHAHAHAHA!!"

            pause 1.5
            "Reload your last save. Trust Chung-hee's instructions precisely."
            jump game_over

    $ _choice_timeout = 0
    hide dorian
    hide vasily
    jump ch6_vasily_final


# =============================================================================
# SECTION 24: LABEL CH6_VASILY_FINAL — Vasily Final / Frostcradle
# =============================================================================

label ch6_vasily_final:

    vasily "Well done, old friend."

    "He clapped his hands together, and the world around us shattered."
    camera at bigshake(5.0, rate=0.020, time=0.09), shattered_glass_transform
    with shattered_glass_transition
    camera

    scene frostcradle_blizzard with shock_cut
    show snow_blizzard_1
    # play music ost_frostcradle fadein 0.5       # PLACEHOLDER — cold howling theme
    # play audio amb_blizzard loop fadein 1.0     # PLACEHOLDER — blizzard ambient

    "The warmth was ripped away in an instant, replaced by a howling blizzard."
    "The sky churned an eerie gray, thick snow pounding against my skin like frozen needles."
    "The air burned in my lungs, each breath coming out in a white gasp."
    "We stood on an endless stretch of ice, the frozen wasteland stretching in all directions. Jagged cliffs loomed in the distance, their edges sharp as broken glass."
    "Mjoll."

    show dorian serious at left_char
    show vasily alt_savage at right_char
    with Dissolve(0.2)
    "I clenched my fists, flames flickering to life at my fingertips. They sputtered, struggling against the cold."
    "Vasily stood across from me, unbothered, smirking. His coat billowed in the wind, the fur-lined edges pristine despite the storm."

    vasily "Feels familiar, doesn't it? How many battles did we fight here, Dorian? How many nights did we spend wading through snow, side by side…"

    dorian "Mjoll…"

    show vasily alt_aggressive at right_char
    vasily "Fitting, isn't it? Where it all started. Where we stood side by side—until you decided to betray it all."

    show dorian sad at left_char
    "I looked down."

    dorian "Look, you didn't give me a choice—"
    show dorian serious at left_char

    show vasily alt_savage at right_char
    "His eyes glowed with an unnatural radiance. Then—"
    show cg_blindinglight with shock_cut
    "A surge of blinding light."
    show vasily_attack with Dissolve(0.3)
    "It swirled around his hands before condensing into a searing white beam, crackling with raw power."


    vasily "Let's see if you still have the strength to stand against me, Dorian."  
    scene frostcradle_blizzard with shock_cut
    show snow_blizzard_1

    show dorian dragon_eyes at left_char
    show vasily alt_savage at right_char
    with Dissolve(0.2)
    "The very air shimmered with heat as the beam bore down on me, faster, sharper, deadlier."

    # play sound sfx_heartbeat loop               # PLACEHOLDER — tension heartbeat

    jump ch6_vasily_ice_qtc


# =============================================================================
# SECTION 25: LABEL CH6_VASILY_ICE_QTC — Timed Choice D5 (Earth or Fire)
# =============================================================================
# Both choices are valid — different outcomes, then converge.
# =============================================================================

label ch6_vasily_ice_qtc:

    $ _choice_timeout = 5.0
    menu:

        "Channel Earth.":
            $ _choice_timeout = 0
            $ ch6_ice_qtc = "earth"
            stop sound

            show dorian dragon_eyes at left_char
            play sound sfx_earth  # PLACEHOLDER — earth wall SFX
            "I slammed my foot into the ice. A wall of jagged stone and ice shot up in front of me just as Vasily's beam struck."
            "The impact was deafening."

            play sound audio.sfx_ice_explosion
            "Cracks spread through the barrier, light spilling through the fractures. The force of his attack shattered the wall, sending shards of rock and ice flying in all directions."
            show dorian angry at left_char with Dissolve(0.1)
            "I barely had time to brace before the explosion sent me skidding backward, boots scraping against the frozen ground."

            "Vasily laughed, his silhouette glowing against the snow."

            show vasily alt_savage at right_char
            vasily "Hiding behind walls now? That won't save you, Dorian."

            "I wiped blood from my lip."

        "Channel Fire.":
            $ _choice_timeout = 0
            $ ch6_ice_qtc = "fire"
            stop sound

            
            show dorian dragon_eyes at left_char
            play sound audio.sfx_fire_explosion        # PLACEHOLDER — fire clash SFX
            "I threw my hands forward, summoning the flames deep within me. Fire erupted, a roaring inferno colliding with Vasily's beam."

            # TODO: lava melting ice sfx
            "For a moment, the world burned white-hot—our powers clashing in a searing explosion. Ice melted in an instant, the snow beneath us turning to steam. I pushed forward, forcing the fire down the path of his light."

            "Vasily gritted his teeth, digging his heels into the ice."

            show vasily alt_mad at right_char 
            vasily "Tch—so you still have some fight in you!"

            show cg_blindinglight with shock_cut 
            "He flicked his wrist. The beam split in two—one part diverting around my flames, the other curving like a spear toward my side."
            scene frostcradle_blizzard with shock_cut
            show snow_blizzard_1

            show dorian angry at left_char
            show vasily alt_savage at right_char
            with Dissolve(0.2)

            "It grazed my ribs, a white-hot burn searing through my coat. I hissed in pain but stood my ground."

    $ _choice_timeout = 0
    show vasily alt_aggressive at right_char
    "He raised his hand. The air shifted."
    scene cg_vasily_clones with shock_cut
    "The ground beneath me trembled. Shadows stretched unnaturally, writhing, shifting—before bodies stepped out of them. A dozen. A hundred. A thousand."

    dorian "Tsk…"
    "The Vasily copies moved in unison, like reflections in a shattered mirror."

    vasily "You didn't think you'd get a fair fight, did you?"

    "A wall of Vasilys—perfect replicas—stared back at me. Their eyes glowed with the same ruthless cunning. Their smirks identical. A sickening, dizzying sight."
    "They stood in perfect formation, radiating a light so intense it swallowed the snowstorm in an ethereal glow. Each one moved in sync, eyes gleaming like suns."
    "Then—he laughed. A mocking, cruel sound that rang through the frozen battlefield."

    vasily "Hahaha! Farewell, old friend. I'll be meeting you in Xianlun."
    scene cg_blindinglight with shock_cut
    "And then, the world erupted in blinding white. A wave of pure white radiance surged forward, folding in on itself—expanding, swallowing everything in its path."

    "I clenched my fists, breath unsteady. My body tensed, my fire flaring to life. But before I could react—"
    "Everything stopped."
    scene frostcradle_blizzard with shock_cut

    show dorian serious at left_char
    show vasily alt_savage at right_char
    with Dissolve(0.2)
    "The snow, mid-air, froze in place. Individual flakes suspended in time, glimmering like tiny frozen stars."
    "The clones, mid-attack, halted. Their light dimmed, their movements severed."
    "Vasily froze, his hand still raised—expression unreadable."
    scene black with fade
    "And then—Mjoll disappeared."
    "The frozen battlefield vanished and the stench of burnt flesh filled the air."
    jump ch6_hundun_defeated


# =============================================================================
# SECTION 26: LABEL CH6_HUNDUN_DEFEATED — Return to Tianho / Hundun Fallen
# =============================================================================

label ch6_hundun_defeated:

    scene bg_tianho_city_night with dissolve
    stop audio fadeout 1.5
    # play music ost_tianho_night fadein 1.0      # PLACEHOLDER — night theme returns

    "I was standing in Tianho again."
    scene cg_chung_slay_hundun with shock_cut
    "The Hundun—the monstrous, shifting mass of darkness—lay on the scorched ground, its grotesque form twitching."
    "Its many mouths hung open, jagged teeth bared, its skin blackened and peeling, thick smoke curling from its half-burned body."
    "A pool of shimmering darkness seeped from its wounds, writhing, alive. Its whispers were no longer mocking, no longer deceptive. Only pained."

    hundun "Rrrrrnnnmmmrr…"
    
    "And standing over it—his coat still billowing slightly from the residual static—was Chung-hee."
    "Lightning crackled at his fingertips, bright and sharp against the ruined cityscape."
    "For a moment, he simply looked down at the creature, his face impassive, unreadable. Then, his sharp gaze shifted to me."
    scene bg_tianho_city_night with shock_cut
    show chunghee normal_neutral at right_char
    show dorian serious at left_char
    with Dissolve(0.2)
    chung_hee "Are you alright, Dorian?"
    
    "His voice rang through my mind, steady and clear."
    "I exhaled—only then realizing how tightly I had been clenching my fists. My fire flickered out, my breath escaping in a sharp, ragged sigh."

    dorian "I'm fine… thanks."

    show dorian sad at left_char
    "I flexed my fingers. I still felt the lingering heat of the illusory flames from Mjoll. The memory of Vasily's voice, the blinding light, the suffocating pressure—it had felt so real."
    show dorian serious at left_char

    show chunghee normal_neutral at right_char
    "Chung-hee tilted his head slightly, eyes narrowing as he studied me."

    chung_hee "I apologize for losing contact with you. The Hundun doubled down on me."

    "His fingers twitched, the last of the electricity fading from his hands. He wasn't looking at me. His gaze turned on the Hundun's charred body."

    chung_hee "This isn't how it's supposed to be. The old stories…"

    "Tiny footsteps pounded against the broken ground. Tim."

    show tim alt_pumped at center_char_kids with Dissolve(0.2)
    tim "I knew it! I-I knew it! This is just like the Pre-Enoch stories!"

    show dorian serious at left_char
    dorian "Pre-Enoch? This monster is Pre-Enoch?"

    show tim normal at center_char_kids with Dissolve(0.2)
    tim "Yes, sir Dorian! In Li Mengtia's bibliography, page 237, he wrote about creatures that existed before the time of the death god Enoch!"
    tim "Before he wiped them all out four hundred years ago!"

    scene bg_tianho_city_night with Dissolve(0.1)
    show soldier_gao at right_char
    show soldier_jiang at left_char 
    with Dissolve(0.2)
    "Soldier Gao and Soldier Jiang peeked out from behind their hiding spot, still half-crouched, looking just as stunned."

    gao   "Wait, wait, wait."
    jiang "Did that kid just say—four hundred years ago?"

    show tim alt_pumped at center_char_kids with Dissolve(0.2)
    "Tim nodded furiously."

    tim "Yes!"

    hide soldier_gao
    hide soldier_jiang
    show dorian neutral at left_char
    show chunghee normal_v2 at right_char
    with Dissolve(0.2)
    "Chung-hee's hands tightened into fists. The faintest flicker of electricity crackled at his fingertips before dying out."

    chung_hee "No… that doesn't make sense."
    dorian    "So this thing existed during Enoch's time, huh…"
    show chunghee normal_neutral at right_char
    chung_hee "Not just existed. These creatures…"
    chung_hee "They were hunted. Purged. Every last one of them."

    show dorian serious at left_char
    "I raised an eyebrow."

    chung_hee "That's what the records say. That's what we were taught. That's what we believed."
    tim       "That's what Li Mengtia wrote, too…"
    hide chunghee
    show soldier_jiang at right_char with Dissolve(0.2)
    jiang     "You really read those? But you're a toddler."

    show tim alt_annoyed at center_char_kids
    "Tim shot him an irritated glance but didn't stop."
    
    hide soldier_jiang
    show chunghee normal_v2 at right_char with Dissolve(0.2)
    chung_hee "I don't know much about the details. Maybe someone familiar with Enoch can tell us more. We—"

    play sound audio.yg_scream volume 0.8
    yg "Raaaaaaawwrrr!!!"

    show dorian angry at left_char
    show tim alt_nervous at center_char_kids
    "A guttural scream pierced the air. I stiffened, my instincts already sharpening."

    show dorian serious at left_char
    dorian    "Did you hear that?"
    show chunghee normal_neutral at right_char
    chung_hee "No. I'm still processing all your thoughts about what it is."

    hide dorian
    hide chunghee
    hide tim
    show soldier_gao at right_char
    show soldier_jiang at left_char
    with Dissolve(0.2)
    "Jiang gripped the hilt of his sheathed sword, his jaw clenched."

    jiang "Yaoguai."
    gao   "They must be enraged. They can't feel their leader anymore."

    voice audio.yg_scream
    yg "Raaaaaa!!!"

    jiang "Then that means… there might be a few left!"

    "He turned to me, his expression determined."

    jiang "Let us join you! We can help—"

    hide soldier_jiang
    hide soldier_gao
    show dorian serious at left_char 
    with Dissolve(0.2)
    "I took a closer look at their bodies. Jiang was limping on his right leg. I raised a hand, cutting him off."

    show dorian neutral at left_char 
    dorian "Stand down, soldier. We can handle this."

    "My gaze flicked to the bodies strewn across the ruined streets. The civilians who hadn't made it. The ones who didn't get the chance to hide."
    show soldier_jiang at right_flip with Dissolve(0.2)
    "Jiang followed my gaze. His mouth pressed into a firm line."

    jiang "But—"
    show dorian serious at left_char
    dorian "Orders are orders, soldier."
    hide soldier_jiang
    show soldier_gao at right_char with Dissolve(0.2)
    gao   "A-Affirmative, Paladin. Jiang, let's just follow his orders."
    gao   "Besides… you're already not in a position to fight."

    hide soldier_gao
    show soldier_jiang at right_flip with Dissolve(0.2)
    "Jiang exhaled sharply, frustration flashing across his face."

    jiang "Fine. But you better come back in one piece."
    show tim alt_pumped at center_char_kids with Dissolve(0.2)
    tim   "We will! Don't worry about us, sir soldiers! We'll be very careful!"
    show dorian normal_alt_annoyed at left_char
    dorian "Tim, you're not coming with us. Go with them."
    show tim sad at center_char_kids with Dissolve(0.1)

    "Tim flinched, his small hands clenching into fists."

    tim "But… but I can help!"

    hide soldier_jiang
    show dorian serious at left_char
    show chunghee normal_neutral at right_char
    with Dissolve(0.2)
    "Chung-hee stepped in."

    chung_hee "Tim… Listen to Dorian."

    "A silence stretched between us."
    "Tim bit his lip, his little shoulders trembling, but he finally nodded."

    tim "Okay…Fine…"

    hide chunghee
    show dorian neutral at left_char
    show soldier_gao at right_char with Dissolve(0.2)
    "Soldier Gao clapped a reassuring hand on his back."

    gao   "Come on, little fella. We'll bring you to Ma'am Weng."
    tim   "Is she alright, Mister?"
    hide soldier_gao
    show soldier_jiang at right_flip with Dissolve(0.2)
    jiang "Yes, she's with the doctor and the violet-haired guy. Tending to the wounded."

    show tim alt_nervous at center_char_kids
    "Tim hesitated for one last moment—then, with a final reluctant glance at the Hundun, me and Chung-hee, he followed them into the store."
    show tim normal at center_char_kids
    tim "Take care, Mister Dorian, okay? And Mister Chung."
    
    hide tim 
    hide soldier_jiang
    show chunghee normal_v2 at right_char
    show dorian serious at left_char
    with Dissolve(0.2)
    "The moment they disappeared, another howl rang through the night."
    "This time, closer."

    jump ch6_feng_appears


# =============================================================================
# SECTION 27: LABEL CH6_FENG_APPEARS — Feng and Aoi Arrive
# =============================================================================

label ch6_feng_appears:

    scene bg_tianho_city_night_sleeping with dissolve

    show dorian serious at left_char
    show chunghee normal_v2 at right_char 
    with Dissolve(0.2)
    play music audio.ost_battle
    "I rolled my shoulders, feeling the fire in my veins ignite."

    show chunghee normal_power_up at right_char with Dissolve(0.1)
    chung_hee "I can feel more of them coming. Prepare yourself, Dorian."

    "Another screech — a hideous, piercing sound that scraped against my skull like metal tearing through stone."
    hide chunghee
    show dorian angry at left_char
    show yaoguai at right_yg 
    with Dissolve(0.2)
    voice audio.yg_scream
    yg "RAAAAA!!!!"

    "Their grotesque forms twisted, eyes burning with a deep, unnatural rage. Clawed feet slammed against the ground as they charged."
    "Their attention flicked between us and the Hundun's smoldering corpse. They howled again, the sound rattling through the broken streets of Tianho."

    voice audio.yg_screech
    yg "SKREEEEEAAAAAAAAAAAARGHHH!!"

    show dorian dragon_eyes at left_char with Dissolve(0.1)
    scene cg_dorian_yg_fight_night with shock_cut
    play sound audio.sfx_wind
    "I stepped forward, thrusting my arms out. The wind howled with me."
    "A violent gust tore through the Yaoguai, sweeping them up like ragdolls. I twisted my fingers, and the currents snapped—spinning like a tornado, hurling the creatures into the crumbling walls of Tianho's ruins."
    play sound audio.monster_death
    "Bones cracked. Flesh splintered. They shrieked as they were flung into the air."
    
    voice audio.yg_scream
    yg "GRAAAAAA!!!"

    # play sound sfx_lightning_crack              # PLACEHOLDER — Chung-hee lightning SFX

    scene bg_tianho_city_night with dissolve
    show dorian dragon_eyes at left_char
    show chunghee normal_power_up at right_char
    with Dissolve(0.2)
    "Beside me, Chung-hee raised his hands, and a shimmering forcefield exploded outward. A Yaoguai leapt toward him—fangs bared, claws outstretched—only to slam into the forcefield."
    play sound audio.sfx_stone_break
    "The creature was thrown back so violently that it left a crater where it landed. Another tried, only for Chung-hee to flick his wrist."
    "The forcefield twisted and with a sickening crunch, the Yaoguai's body caved inward."

    voice audio.yg_scream
    yg "Raaaaaaa!!!!"

    hide yaoguai
    show dorian serious at left_char 
    show chunghee normal_v2 at right_char
    with Dissolve(0.2)
    "For a fleeting moment, I thought we had them."

    show dorian angry at left_char 
    show chunghee normal_angry at right_char
    with Dissolve(0.1)
    "Then—there were more."
    "Not just a handful. Dozens."
    hide dorian 
    hide chunghee
    show yaoguai at center_yg
    with Dissolve(0.2)
    "They emerged from the shadows, from the broken alleys, from the wreckage of some of the old buildings. Grotesque forms twisting. Glowing eyes flashing. Clawed fingers scraping against stone. They kept coming."
    "My pulse pounded in my ears. Chung-hee's voice echoed sharply in my mind."
    hide yaoguai
    show dorian serious at left_char
    show chunghee normal_angry at right_char
    chung_hee "Dorian, find a spot to hide. I'll—"
    dorian    "Don't be reckless, Chung."
    show chunghee normal_sad at right_char
    chung_hee "I—Fine…"

    show dorian dragon_eyes at left_char with Dissolve(0.1)
    "I readied myself—fists clenched, fire curling at my fingertips—when suddenly a brilliant blue light cut through the night."

    # play sound sfx_blue_fire
    "A wall of blue fire hurled towards the yaoguai. The Yaoguai screeched in agony as the blue flames swallowed them whole. Their blackened bodies twisted, shriveling, burning, turning to ash."

    "I turned sharply, and a figure stood atop the wreckage of a ruined merchant's stall. I knew that stance."
    "My eyes widened."
    "My mind reeled. What in Tetrad's was he doing here?"

    scene bg_tianho_city_night_sleeping with shock_cut

    show feng_suit at right_char
    show aoi_battle_suit at left_char
    with Dissolve(0.2)
    dorian "Feng?!"
    feng   "Watch out! Behind you!"
    aoi    "Stay sharp!"

    "Before I could even open my mouth—"
    scene cg_feng_aoi with shock_cut
    yg "Graaaawwrrrr!!!"

    # play sound sfx_water_spear                  # PLACEHOLDER — water spear SFX

    "A surge of water rushed through the streets, coiling unnaturally, moving like a living serpent. The liquid swirled with unnatural precision, snaking between us and slamming into the advancing monsters with crushing force."
    "The water pierced through them, shaping into sharp spears that skewered the creatures in mid-air."

    yg "Raaaaaaaaaahhh!! Graahh—"

    "Their bodies tensed—twitched—then dissolved into black mist."

    chung_hee "You—!"

    "Chung-hee's glare darkened, energy rippling in the air around him like a storm ready to break. Electricity cracked through the air."
    "I turned, and there she was. One of the Commandants of Mjoll. The woman who stood beside Tian Xun earlier. She stood where the last Yaoguai had fallen, calm. Unshaken."

    "Feng casually raised a hand."

    scene bg_tianho_city_night_sleeping with shock_cut
    show feng_suit at right_char
    show aoi_battle_suit at left_char
    with Dissolve(0.2)

    feng "Easy. She's on our side."

    "Aoi merely huffed, flicking her wrist."

    aoi "Hmph."

    hide feng_suit
    show yaoguai at right_yg with Dissolve(0.2)
    "A final tendril of water lashed out behind her, striking the last Yaoguai."
    hide yaoguai with Dissolve(0.1)
    "The creature didn't even have time to scream before it burst into dust."

    show dorian serious at right_flip with Dissolve(0.2)
    dorian "What…"

    hide dorian 
    show yaoguai at right_yg with Dissolve(0.2)
    voice audio.yg_scream
    yg "Graaaarrrrr!!"

    "Aoi's head snapped toward the sound, water already coiling at her fingertips, alive and restless. Her expression was unreadable, cold as ever."

    aoi "I'll handle it, Feng. This won't take long."

    hide aoi_battle_suit
    hide yaoguai
    with Dissolve(0.1)
    "She didn't wait for permission. With a swift movement, she vanished into the shadows, her figure weaving through the broken streets of Tianho."
    "But even as she disappeared, Chung-hee's glare followed her."
    "His entire body remained tense, his presence humming with quiet suspicion. Electricity crackled faintly at his fingertips."

    jump ch6_reunion


# =============================================================================
# SECTION 28: LABEL CH6_REUNION — Dorian and Feng Reunion
# =============================================================================

label ch6_reunion:

    # play music ost_reunion fadein 1.0           # PLACEHOLDER — warm bittersweet reunion theme
    "Feng exhaled before stepping forward, finally turning his attention to me."
    show feng_suit at right_char
    show chunghee normal_neutral at center_char 
    show dorian normal at left_char 
    with Dissolve(0.2)
    "He didn't say anything at first. His gaze lingered on Chung-hee. The ghost of a smirk pulled at his lips."
    feng "By the Prosperity Dragon, The Emperor of Kyeongjang in the flesh."

    "Chung-hee met his gaze, still stiff, still guarded."

    feng "You look different from your father, His Majesty Hyon Min-joon. But I see the resemblance."

    "Chung-hee didn't respond."

    feng "Should I kneel? Or perhaps I should summon an interpreter for a deaf-mute? I could arrange—"

    show chunghee normal_angry at center_char with Dissolve(0.1)
    "Chung-hee's voice slammed into our minds like a thunderclap."

    chung_hee "Does it look like I need an interpreter?"
    show chunghee normal_v2 at center_char with Dissolve(0.1)

    "Feng's smirk faltered—just slightly."
    "Feng."
    "My old friend. My old best friend."
    "He stood before me, still wearing that same confident stance, that same effortless composure—but something was different."
    "I remembered the Taotie. Its claws. Its shriek. The way it had nearly gouged out Feng's left eye."

    show dorian sad at left_char with Dissolve(0.1)
    "I opened my mouth, wanting to ask—wanting to know— but before I could—"

    dorian "Feng, what are you doing here?"

    show dorian serious at left_char with Dissolve(0.1)
    "I clenched my fists."

    dorian "Don't you know she's from Mjoll? They attacked—"

    "Feng cut me off with a single, casual shrug."

    feng "She's a mercenary of King Gustav. Her loyalty can always be bought."

    show chunghee normal_neutral at center_char
    chung_hee "Loyalty isn't something that can be bought."

    feng "Loyalty is a luxury, Your Majesty. Some of us don't have the privilege of being born into it."

    show dorian neutral at left_char
    dorian "As long as she's on our side, it doesn't matter anyway."

    "Feng only rolled his shoulders, exhaling lazily."

    feng "Look, I didn't come here to debate politics. I came because I heard some crazy rumors—"
    feng "So, there we were, interrogating the aldoriths that was with Aoi earlier—nothing unusual. Then they start babbling about a blond-haired demon who burned through an entire battalion. Fire, wind, earth, they said."
    feng "And I thought, 'Nah. That can't be my best friend. My best friend left Tianho years ago, and he sure as hell ain't going back...' Then—lo and behold."
    feng "How's it going, old friend? Miss me?"

    show dorian normal at left_char with Dissolve(0.1)
    dorian "Feng… It's been a while. I thought you were dead."
    feng   "Funny. I thought the same about you."

    show dorian neutral at left_char with Dissolve(0.1)
    "And then—without thinking—I stepped forward and pulled him into a hug."
    "Then, with a quiet chuckle, he patted my back—harder than necessary."

    feng "Alright, alright. Don't get all sentimental on me."

    show dorian smile at left_char
    "I huffed a laugh, pulling back just enough to look at him."

    dorian "Haha. Shut up, jackass."

    "Then I noticed it. The scars. A jagged mark running down the left side of his face—faint but unmistakable. And the red-tinted glasses. My stomach clenched."

    show dorian serious at left_char
    dorian "Your eye… How is it?"

    "Feng waved a hand dismissively."

    feng "It's fine. Healed up a long time ago."
    feng "The Empress' personal doctor patched me up. Had some fancy healing techniques. You know how they are in the Imperial City—spare no expense when they want you back in fighting shape."

    "He smirked, tapping his glasses."

    feng "Still, I keep these around. Gives me a little edge. Makes me look mysterious, don't you think?"

    show dorian normal_alt_annoyed at left_char with Dissolve(0.1)
    "I rolled my eyes."

    dorian "You always did think too highly of yourself."
    feng   "Hahaha. Damn right."
    show dorian neutral at left_char with Dissolve(0.1)

    "Feng slung an arm around my shoulders, his grin easy. He gestured toward the charred remains of the Hundun, its twisted form still crackling with lingering energy."

    feng "Tell you what—once we're done cleaning up this mess, let's catch up over a drink. I know a place."
    feng "Best liquor this side of Tianho."
    feng "My treat, of course. The Empress still pays us Paladins well."

    "Then, with an exaggerated wave, he turned his attention to Chung-hee, his smirk widening."

    feng "What about you, Your Majesty? Will the Emperor Lord grace us peasants with his presence?"

    show chunghee normal_v2 at center_char
    "Chung-hee stood with his arms crossed, with his brow twitched."

    chung_hee "Please. Calling you or Sir Dorian 'peasants' is beneath me."

    show dorian normal at left_char
    "I arched an eyebrow."

    dorian "So, that's a yes?"

    show chunghee alt_neutral at center_char with Dissolve(0.1)
    "Chung-hee's mouth opened—then closed. A faint wrinkle appeared between his brows, as if he were choosing his words carefully."

    chung_hee "I… suppose I can accompany you."
    show chunghee normal_neutral at center_char with Dissolve(0.1)

    feng "Oh? His Majesty drinks with commoners? I'm honored."

    jump ch6_end


# =============================================================================
# SECTION 29: LABEL CH6_END — Yaoguai Howl / Feng Departs / Chapter 7
# =============================================================================

label ch6_end:

    "But before I could reply, the air shattered—another piercing screech."

    yg "Grawwwrrrr!!!"

    show feng_suit at right_char
    "Feng's entire body went rigid. The easygoing playfulness vanished in an instant. His smirk faded, his stance shifting, shoulders squared."

    feng "See you later, buddy."

    "He cracked his knuckles, stepping forward as his blue flames reignited at his fingertips."

    feng "Don't worry. Me and the Paladins will handle this. Go to the hideout."

    show dorian serious at left_char
    "I frowned, feeling an unease settle in my gut."

    dorian "You sure?"
    feng   "Tianho is under the protection of the Imperial City of Gale. This is our job as Paladins. You should know this, buddy—you were one of us once."
    feng   "Besides, there are plenty of us. You sticking around would just be a waste of resources."
    
    show dorian normal_alt_calm at left_char with Dissolve(0.1)
    "He wasn't wrong. He looked at the charred body of the Hundun."
    show dorian serious at left_char with Dissolve(0.1)

    feng "And more importantly—the appearance of this… thing isn't normal. Whatever's happening, we need answers, not just bodies in the streets."
    feng "Fortunately, we have specialists from the city who will handle the investigation. Best you steer clear once they arrive."

    show chunghee normal_v2 at center_char with Dissolve(0.1)
    "Chung-hee nodded."

    chung_hee "He's right, Dorian."
    chung_hee "Then we go to the hideout beneath the Cheng Industries store."

    show dorian normal_alt_annoyed at left_char with Dissolve(0.1)
    dorian "Tch. Fine."
    feng   "Try not to miss me too much. See you later."

    "I rolled my eyes."

    show dorian normal at left_char with Dissolve(0.1)
    dorian "Try not to get bitten this time, dumbass."

    "Feng barked out a laugh—then disappeared into the shadows, his blue flames joining the lanterns in illuminating the area."

    scene black with fade                    # PLACEHOLDER — fade to black
    stop music fadeout 2.0
    stop audio fadeout 1.5

    pause 2.0

    show screen chapter_title_screen(
        "6",
        "Return to Tianho",
        subtitle="END",
        duration=3.0
    )
    pause 3.0
    jump chapter_7


# =============================================================================
# END OF CHAPTER 6
# =============================================================================