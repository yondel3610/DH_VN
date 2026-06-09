###############################################################################
#  Dragon's Heart: The Crimson Rebirth
###############################################################################

# =============================================================================
# SECTION 1-4: DEFINITIONS, DECLARATIONS, AUDIO, VARIABLES
# =============================================================================

# =============================================================================
# SECTION 2: IMAGE DECLARATIONS
# =============================================================================

# --- Backgrounds: Mjoll Palace ---
# (already declared in chapter_02.rpy)

# --- Backgrounds: Kyeongjang ---
# image bg_kyeongjang_palace       = "images/backgrounds/bg_kyeongjang_palace.png"          # PLACEHOLDER
# image bg_kyeongjang_room         = "images/backgrounds/bg_kyeongjang_room.png"            # PLACEHOLDER

# --- Backgrounds: Tianho ---
# image bg_tianho_dorian_room      = "images/backgrounds/bg_tianho_dorian_room.png"         # PLACEHOLDER
# image bg_tianho_memorial_gate    = "images/backgrounds/bg_tianho_memorial_gate.png"       # PLACEHOLDER
# image bg_tianho_memorial         = "images/backgrounds/bg_tianho_memorial.png"            # PLACEHOLDER
# image bg_tianho_memorial_2       = "images/backgrounds/bg_tianho_memorial_2.png"          # PLACEHOLDER
# image bg_empty_battlefield       = "images/backgrounds/bg_empty_battlefield.png"          # PLACEHOLDER
# image bg_frostcradle_bloodied    = "images/backgrounds/bg_frostcradle_bloodied.png"       # PLACEHOLDER
# image bg_tianho_underground_1    = "images/backgrounds/bg_tianho_underground_1.png"       # PLACEHOLDER

# --- CGs ---
# image cg_dorian_family_graves    = "images/cg/cg_dorian_family_graves.png"                # PLACEHOLDER
# image cg_chung_hee_amulet        = "images/cg/cg_chung_hee_amulet.png"                   # PLACEHOLDER
# image cg_prosperity_dragon_white = "images/cg/cg_prosperity_dragon_white.png"            # PLACEHOLDER
# image cg_bomb_bad_end            = "images/cg/cg_bomb_bad_end.png"                       # PLACEHOLDER
# image cg_draconic_fire_surge     = "images/cg/cg_draconic_fire_surge.png"                # PLACEHOLDER

# =============================================================================
# SECTION 3: AUDIO DECLARATIONS
# =============================================================================

# define audio.ost_mjoll_aftermath  = "audio/music/ost_mjoll_aftermath.ogg"       # PLACEHOLDER
# define audio.ost_kyeongjang_celeb = "audio/music/ost_kyeongjang_celeb.ogg"      # PLACEHOLDER
# define audio.ost_kyeongjang_quiet = "audio/music/ost_kyeongjang_quiet.ogg"      # PLACEHOLDER
# define audio.ost_tianho_memorial  = "audio/music/ost_tianho_memorial.ogg"       # PLACEHOLDER
# define audio.ost_cemetery_chaos   = "audio/music/ost_cemetery_chaos.ogg"        # PLACEHOLDER
# define audio.ost_prosperity_dragon= "audio/music/ost_prosperity_dragon.ogg"     # PLACEHOLDER
# define audio.ost_underground_move = "audio/music/ost_underground_move.ogg"      # PLACEHOLDER
# define audio.sfx_explosion_boom   = "audio/sfx/sfx_explosion_boom.ogg"          # PLACEHOLDER
# define audio.sfx_arrow_volley     = "audio/sfx/sfx_arrow_volley.ogg"            # PLACEHOLDER
# define audio.sfx_earth_pillar     = "audio/sfx/sfx_earth_pillar.ogg"            # PLACEHOLDER
# define audio.sfx_carriage_crash   = "audio/sfx/sfx_carriage_crash.ogg"          # PLACEHOLDER
# define audio.sfx_metal_barrier    = "audio/sfx/sfx_metal_barrier.ogg"           # PLACEHOLDER
# define audio.sfx_shadow_surge     = "audio/sfx/sfx_shadow_surge.ogg"            # PLACEHOLDER
# define audio.sfx_draconic_fire    = "audio/sfx/sfx_draconic_fire.ogg"           # PLACEHOLDER
# define audio.sfx_tunnel_seal      = "audio/sfx/sfx_tunnel_seal.ogg"             # PLACEHOLDER
# define audio.sfx_amulet_pulse     = "audio/sfx/sfx_amulet_pulse.ogg"            # PLACEHOLDER
# define audio.amb_kyeongjang_feast = "audio/ambient/amb_kyeongjang_feast.ogg"    # PLACEHOLDER
# define audio.amb_cemetery         = "audio/ambient/amb_cemetery.ogg"            # PLACEHOLDER
# define audio.amb_tianho_afternoon = "audio/ambient/amb_tianho_afternoon.ogg"    # PLACEHOLDER
# define audio.amb_rain_heavy       = "audio/ambient/amb_rain_heavy.ogg"          # PLACEHOLDER
# define audio.amb_tunnel           = "audio/ambient/amb_tunnel.ogg"              # PLACEHOLDER

# =============================================================================
# SECTION 4: GAME VARIABLES
# =============================================================================

# default chunghee_affection     = 0
# default ch4_yuxuan_interrupted = False
# default ch4_chunghee_choice    = ""
# default ch4_carriage_qtc1      = ""
# default ch4_carriage_qtc2      = ""
# default ch4_draconic_choice    = ""


# =============================================================================
# SECTION 5: label chapter_4
# =============================================================================

label chapter_4:
    $ save_name = "Chapter 4"

    scene cg_black with fade
    # play music ost_mjoll_aftermath fadein 2.0      # PLACEHOLDER

    show screen chapter_title_screen(
        "4",
        "The Massacrer of Mjoll",
        subtitle="Mjoll / Kyeongjang / Tianho",
        duration=3.0
    )
    pause 3.0

    # scene bg_mjoll_palace_throne with fade         # PLACEHOLDER

    show king_gustav at right_char with Dissolve(0.2)
    king_gustav "Count Vasily… dead."
    king_gustav "My right hand man… I… I can't believe this."
    king_gustav "And the amulet? Tell me you at least retrieved the damn amulet!"
    # show mjoll_lars at left_char               # PLACEHOLDER — no sprite declared
    mjoll_lars  "N-No, Your Majesty. We searched the site thoroughly, but it… it's gone."
    # show mjoll_helga at left_char              # PLACEHOLDER — no sprite declared
    mjoll_helga "We believe… we believe sir Dor – I mean, Dorian took it."
    king_gustav "That traitorous snake! After everything I gave him—after all my trust!"
    king_gustav "How many? How many died?"
    mjoll_lars  "Nearly all, Your Majesty. We lost nearly the entire battalion."
    king_gustav "By Enoch… Nearly all…"

    # show mjoll_pavel at left_char              # PLACEHOLDER — no sprite declared
    mjoll_pavel "Your Majesty… We have the two survivors with us. They're outside."
    king_gustav "Send them in."

    # show girl_ald_soldier at left_char         # PLACEHOLDER — no sprite declared
    girl_ald_soldier "It… *crying* It wasn't human… He wasn't human…"
    mjoll_lars       "Miss, please. Take a breath. Tell us what happened."
    girl_ald_soldier "Flames… everywhere… He burned them… He burned them all alive!"
    girl_ald_soldier "If I hadn't run… I would have… I would have— I would hav—burned with them! *weeping*"

    mjoll_pavel "And we have Svante, Your Majesty."

    hide king_gustav
    show svante normal_sad at right_char with Dissolve(0.2)
    svante "He's a monster… A massacrer… He… he killed them all…"
    svante "Count Vasily… Kristin… My brothers… sisters… Everyone… gone… It was a massacre… *weeping*"

    show king_gustav at left_char with Dissolve(0.2)
    king_gustav "I am sorry, my son."
    svante      "F-Father…"

    king_gustav "I've heard troubling whispers. Whispers of your sister—TAINTED by the Prince's lies, doubting me."
    show svante normal_nervous at right_char
    svante      "Kristin, she—"
    king_gustav "She deserved her fate. Her death was just. Her betrayal brought shame to you and your ailing mother. Surely it must have pleased you to see her cut down for my name."
    svante      "I—"
    king_gustav "You are loyal, my son, and for that, you will be rewarded. But I see the grief in your eyes—the weight of Count Vasily and the others lost."
    svante      "The man… he was surrounded by fire, Father. It was like… it was part of him. He burned everything. Everyone. I barely escaped."

    king_gustav "A massacre…"
    girl_ald_soldier "Massacrer… He's a massacrer! *weeping*"
    mjoll_helga "Miss, please calm down."

    king_gustav "Dorian the Dragon of Gale… Now the Massacrer of Mjoll."
    king_gustav "I want him hunted down. I don't care how many Aldoriths it takes or how long. Find him. Kill him. He is an enemy of this land. Do you hear me?"
    "Aldoriths: Yes, Father!"
    show svante normal_nervous at right_char
    svante      "Y-Yes, Father…"

    # show messenger at left_char                # PLACEHOLDER — no sprite declared
    messenger   "A letter from the Emperor of Kyeongjang, Your Majesty."

    mjoll_pavel "K-Kyeongjang, Your Majesty?"
    king_gustav "Hmm… Fascinating…"
    mjoll_pavel "…"
    mjoll_helga "…"
    mjoll_lars  "…"
    svante      "…"

    king_gustav "Forget Dorian. We have a new target."
    king_gustav "Aldoriths. Our sights are now set on the Emperor of Kyeongjang."
    "Aldoriths: Yes, Father!!"
    mjoll_lars  "Yes, Your Highness!"
    show svante normal_nervous at right_char
    svante      "The Emperor of Kyeongjang…"

    hide king_gustav
    hide svante
    jump ch4_kyeongjang


# =============================================================================
# SECTION 6: label ch4_kyeongjang (Chung-hee POV)
# =============================================================================

label ch4_kyeongjang:

    scene cg_black with fade
    pause 1.0

    "8 months later"
    "Somewhere in the Kyeongjang Empire"

    # scene bg_kyeongjang_palace with fade           # PLACEHOLDER
    # play music ost_kyeongjang_celeb fadein 2.0     # PLACEHOLDER
    # play audio amb_kyeongjang_feast loop fadein 2.0 # PLACEHOLDER

    show chunghee normal_neutral at left_char with Dissolve(0.2)
    "Hyon Chung-hee's POV"

    "The grand hall was alive with celebration today."
    "Though I could not hear the cacophony of cheers or the music of the orchestra, I could feel the energy pulsing through the room. I can hear their thoughts."
    "They were as clear as if spoken aloud."

    servant     "Happy birthday, Pyeha. May your days be long and prosperous."
    woman_1     "Pyeha's birthday… what can we possibly gift someone so divine?"
    man_1       "Just focus on your singing. Don't falter. Not today."

    "I sat upon the throne of Kyeongjang, looking at the scrumptious feast laid before me."

    show captain_kang at right_char with Dissolve(0.2)
    "Captain Kang Sunwoo, clad in the pristine silver and navy uniform of the Imperial Guard, bowed low before the throne, his posture respectful and precise."

    captain_sunwoo "Pyeha, I humbly wish you a most joyous birthday. May your reign continue to bring light and prosperity to Kyeongjang for many decades to come."
    show chunghee normal_neutral at left_char
    chung_hee      "Captain Sunwoo, I appreciate your words. Please, enjoy the feast. It is as much for you as it is for me."

    "He hesitated for a moment, his sharp eyes flickering."

    captain_sunwoo "Pyeha, forgive me for addressing you on such a day of celebration, but I must say this—things are looking brighter for Kyeongjang."
    captain_sunwoo "Trade has flourished within our borders, and our crops yield twice what they did last year. Under your divine hand, the people see you as their protector, their guiding light."
    captain_sunwoo "The Tetrad themselves could not have chosen a better ruler."

    "Before I could respond, another figure stepped forward—Ya Ji-hye, my royal advisor."

    hide captain_kang
    show ya_ji_hye at right_char with Dissolve(0.2)
    ji_hye "Pyeha, on this most auspicious day, I offer my humblest and most heartfelt birthday wishes. May your reign be eternal, and may Kyeongjang continue to prosper under your divine leadership."
    ji_hye "You are the pillar of this empire, the sun that shines upon its people."

    "I inclined my head, granting her silent permission to continue. Satisfied, she bowed once more and retreated into the crowd."

    hide ya_ji_hye
    "Next, Park Dae-hyun, Head of Infrastructure, approached."

    # show dae_hyun at right_char                # PLACEHOLDER — no sprite declared
    dae_hyun "Pyeha, I too wish you the happiest of birthdays. May your wisdom guide Kyeongjang for generations to come."

    "Beyond my advisors, I felt the pulse of the celebration itself."

    courtier_1 "To Pyeha, the living embodiment of Kyeongjang's strength!"
    courtier_2 "The Emperor's wisdom surpasses all. He is untouchable. Eternal."

    "And as is tradition, a song filled the hall."
    "You are untouchable. Eternal. A god among men."

    show captain_kang at right_char with Dissolve(0.2)
    captain_sunwoo "Pyeha, the people adore you. Kyeongjang grows stronger with each passing day under your rule. You are their guiding star"
    hide captain_kang
    show ya_ji_hye at right_char with Dissolve(0.2)
    ji_hye         "Pyeha has done what other kingdoms could not. Kyeongjang is self-made, unshaken by the tragedy of Tianho."

    "Upon the mention of the tragedy of Tianho, I could see the unease in their thoughts."

    hide ya_ji_hye
    woman_1  "The tragedy of Tianho… it all began when they tried to reconnect with the world. Look where it led them."
    man_1    "(thinking): Kyeongjang cannot make the same mistake. Pyeha must keep us strong and protected."
    man_2    "(thinking): The world beyond Kyeongjang brought only ruin to Tianho. Our Lord Emperor won't let that happen to us."
    vendor   "Your Majesty, Tianho was mighty, but their trust in outsiders doomed them. Let us not follow their folly. Kyeongjang is strong because we are self-sufficient. The outside world offers nothing but danger!"
    courtier_1 "Our beloved pyeha and pyeha-sshi died because of those outside infidels!"
    courtier_2 "The gates of Kyeongjang must remain closed, Pyeha. We cannot let history repeat itself."

    show captain_kang at right_char with Dissolve(0.2)
    captain_sunwoo "Silence! All of you!"
    hide captain_kang
    show ya_ji_hye at right_char with Dissolve(0.2)
    ji_hye         "This is Pyeha's birthday. Let us focus on the celebration and leave those negative thoughts behind."
    hide ya_ji_hye

    "I rose slowly from my throne, my gaze sweeping over them."

    show chunghee normal_neutral at left_char
    chung_hee "The tragedy of Tianho is a lesson carved into history, one that I have not forgotten. The loss of our beloved pyeha and pyeha-sshi serves as a reminder of the dangers of trust misplaced and gates left unguarded. But hear me now."
    chung_hee "Kyeongjang is not Tianho. Their choices, their fate—it is not ours to share. We have moved past the mistakes of the past. We are stronger, wiser, and more unified than they ever were. We are self-sufficient. We do not need the outside world to prosper."

    chung_hee "The past is in the past. We will not dwell in the shadows of fear or doubt. Under my reign, Kyeongjang will remain untouchable. Eternal. A beacon of strength and prosperity."
    chung_hee "We will never commune with outsiders. That is a promise."

    vendor     "You are right, Pyeha. Kyeongjang needs no one else. We are strong because of you."
    courtier_1 "To Pyeha, the unshakable ruler of Kyeongjang!"
    courtier_2 "The past is in the past! To our Emperor!"

    "I lifted my cup, keeping my gaze fixed on them."

    chung_hee "Raise your cups, my people. Let this day not only celebrate my birth but also the unwavering strength of our empire. Together, we move forward. Together, we endure. Together, we thrive."

    show captain_kang at right_char with Dissolve(0.2)
    "I felt the hall erupting in cheers."

    captain_sunwoo "And now, we celebrate! Long live pyeha!"

    hide captain_kang
    hide chunghee
    jump ch4_kyeongjang_night


# =============================================================================
# SECTION 7: label ch4_kyeongjang_night
# =============================================================================

label ch4_kyeongjang_night:

    # stop music fadeout 2.0
    # stop audio fadeout 1.5

    # scene bg_kyeongjang_room with fade             # PLACEHOLDER
    # play music ost_kyeongjang_quiet fadein 2.0     # PLACEHOLDER

    "10 hours later…"

    "The festivities had passed in a blur of music, laughter, and endless praise."
    "The empire slept. The clock struck ten."
    "It's time."

    "The room I entered was dark, lit only by the pale moonlight filtering through a small, barred window high above."
    "My steps were deliberate, echoing softly against the stone floor as I approached the center of the room. There it was—a chest, simple in design but bound with golden filigree that glimmered faintly in the moonlight."

    show chunghee normal_neutral at left_char with Dissolve(0.2)
    "I knelt before it, the cold seeping into my knees."

    chung_hee "…"

    "My hand hesitated over the latch for only a moment before I pushed it open. Inside lay one thing—the amulet."
    "I reached for it, my hand steady, and lifted it from its resting place."

    # play sound sfx_amulet_pulse                    # PLACEHOLDER

    # scene cg_chung_hee_amulet with dissolve        # PLACEHOLDER
    # pause 1.5
    # scene bg_kyeongjang_room with dissolve

    "The moment it touched my hand, the amulet's glow intensified, casting an ethereal green light that bathed the room."
    "I held it before me, trapping my eyes with its green glow. I held it for a long time."

    show chunghee normal_sad at left_char
    chung_hee "Mother… Father…"

    "Then another thought, sharp and resolute, pierced through the haze of my mind."

    show chunghee normal_neutral at left_char
    chung_hee "I know you're there."

    show ya_ji_hye at right_char with Dissolve(0.2)
    ji_hye    "?!"

    "Her silhouette slowly emerged from the darkness."
    "Her face was pale in the moonlight. She clutched the folds of her robes tightly, her shoulders tense."

    ji_hye    "P-Pyeha… forgive my intrusion. I… I cannot stop you, can I?"

    show chunghee normal_neutral at left_char
    "I turned to face her fully, the amulet's light glinting off my robes."

    chung_hee "You cannot stop the Emperor Lord, Royal Advisor."

    "Her breath hitched."

    ji_hye    "Forgive me, Pyeha… but as your humble servant, I must plead with you to reconsider. This path you are walking—it will only lead to ruin."
    show chunghee normal_angry at left_char
    chung_hee "Kyeongjang calls for vengeance. King Gustav will fall."
    ji_hye    "Kyeongjang? Or is it just you, Pyeha? Is it your vengeance that drives you—not the empire's? Please… just leave the past behind! I beg you!"

    "Her hands continued to tremble."

    ji_hye    "As your Royal Advisor—"
    show chunghee normal_angry at left_char
    chung_hee "How dare you presume to order your Emperor Lord? Do you think your station grants you the right to defy me?"

    "Her knees buckled, and tears started falling down from her eyes. She dropped to the floor."

    ji_hye    "Please, Chung! I beg you, not as your advisor but as your aunt. Please… don't do this!"

    "I saw her shoulders shake. Tears continued to fall down from her eyes."

    show chunghee normal_neutral at left_char
    "I looked away, my jaw tightening as I clutched the amulet tighter."

    chung_hee "Do not make this harder than it already is, Aunt."

    "She lifted her face to look at me, her eyes glistening with tears."

    ji_hye "Do you not remember what happened to our beloved Pyeha and Pyeha-sshi? They too sought answers in the outside realm, and it cost them their lives."
    ji_hye "Please, Chung… I don't want to lose another family member. Jong-hee—your little brother—would be heartbroken to hear of your death too."

    "I turned fully to her, my grip on the amulet loosening slightly."

    show chunghee normal_sad at left_char
    chung_hee "Please… do not bring my little brother into this, Aunt."

    "There was a brief silence in our thoughts."

    show chunghee normal_neutral at left_char
    chung_hee "Speaking of Jong-hee… how is he? I didn't see him at the celebration earlier."
    ji_hye    "He's hospitalized since yesterday. The illness is taking over again."
    ji_hye    "All the more reason for you not to go. Please, Chung…"

    "Her tears stained the stone beneath her. I knelt before her."

    show chunghee normal_sad at left_char
    chung_hee "Aunt Ji-hye… I must do this. I must."
    ji_hye    "You and Jong-hee are all I have left, Chung. Please… please don't leave me too"

    "Her hands gripped the folds of her robe tighter. I reached out, placing a hand on her trembling shoulder."

    show chunghee normal_neutral at left_char
    chung_hee "He must pay. You know that, Aunt."

    "I stood, lifting her gently to her feet."

    ji_hye    "Then… then at least speak with the captain, Pyeha. Perhaps he can offer a different perspective."

    chung_hee "Again, Aunt, you cannot stop me."

    "She hesitated, and then, a small, sad smile broke through her tears."

    ji_hye "You are just as hard-headed as Pyeha-sshi… your mother."

    "The air shifted, and then I felt something—another person's familiar thoughts. Sunwoo's."

    show chunghee normal_neutral at left_char
    chung_hee "Did you call Captain Sunwoo, Aunt?"

    ji_hye "I… yes, Chung. I was worried. I thought perhaps he could change your mind."

    "A sigh escaped me."

    chung_hee "For the last time, Aunt, neither you nor he can stop me."

    "She surprised me then, wrapping her arms around me in an embrace."

    ji_hye    "Then I will stay. If I cannot stop you, at least let me see you off."

    show chunghee normal_sad at left_char
    "I rested a hand on her back for a short while."

    chung_hee "I intend to return, Aunt. I won't leave you or Jong-hee. I promise."

    "Her lips trembled, and I heard the unspoken thought she didn't dare voice aloud:"
    "'That's what pyeha and pyeha-sshi said when they left for Tianho. Five years ago…'"

    show chunghee normal_neutral at left_char
    "I reached out and placed a hand on her trembling shoulder."

    chung_hee "Please. Get up."

    ji_hye "I think it's important to let the captain speak with you. Perhaps he can offer a different perspective, talk some sense into you."
    chung_hee "Again, Aunt. You can't stop me."
    ji_hye "I know. You're just as hard headed like pyeha-sshi – your mother."

    "I heard another mind. Ji-Hye, it thought out. It was the captain."

    chung_hee "Did you call Captain Sunwoo, Aunt?"
    ji_hye    "I… yes, Chung. I was just worried. I thought maybe he can change your mind,"
    chung_hee "For the last time, Aunt. You or him can't stop me."

    "She hugs me."

    ji_hye    "Chung, I want to stay for a bit. I know I can't stop you, but I wish to see you go."
    show chunghee normal_sad at left_char
    chung_hee "I intend to return, Aunt. It's just for a day. I won't leave you and Jong-hee. I promise."

    "She opened her mouth, trying to say something. She hesitated, but I heard her thought."
    "'That's what pyeha and pyeha-sshi said when they went to Tianho. Five years ago…'"

    "The captain will be coming. I need to act fast. What should I do?"

    hide ya_ji_hye
    hide chunghee
    jump ch4_chunghee_qtc


# =============================================================================
# SECTION 8: label ch4_chunghee_qtc
# =============================================================================

label ch4_chunghee_qtc:

    # play sound sfx_amulet_pulse loop               # PLACEHOLDER

    show chunghee normal_neutral at left_char with Dissolve(0.2)
    show ya_ji_hye at right_char with Dissolve(0.2)

    menu:

        "Falter and do nothing.":
            stop sound

            "I stood there, the amulet pulsing faintly in my hand. Aunt Ji-hye continued sobbing."
            "I simply… stood there."

            ji_hye    "Chung… what are you doing? Are you… frozen? Have you reconsidered?"
            show chunghee normal_neutral at left_char
            chung_hee "No, Aunt. I am merely… recalibrating my thoughts."
            ji_hye    "*crying*"
            chung_hee "…"
            ji_hye    "*crying*"
            chung_hee "…"

            jump ch4_common_1

        "Trick Aunt Ji-Hye.":
            stop sound

            show chunghee alt_smirk at left_char
            "There's no time."
            "I focused, my mind reaching outward, weaving through the threads of energy. With deliberate precision, I channeled my power, bending the perception of those around me. Slowly, my form shimmered, then vanished completely."

            hide chunghee
            ji_hye "Chung?! Chung, where are you?!"

            "She stepped forward, her hands grasping at the empty air."

            ji_hye "No… no, no, no! He's gone… he's really gone!"

            "Her knees gave way, and she collapsed to the cold stone floor, sobbing."

            ji_hye "Why, Chung? Why couldn't you listen to me? Why couldn't you stay?!"

            show captain_kang at left_char with Dissolve(0.2)
            "Captain Sunwoo stepped into the room."

            captain_sunwoo "Ji-hye-nim, what's happened?"

            ji_hye         "He's gone… He left us, Sunwoo! He's gone to the outside lands. I tried to stop him, but he wouldn't listen… and now he's gone, just like Pyeha and Pyeha-sshi…"

            "She cried, burying her face in her hands."
            "Sunwoo knelt beside her, his expression softening as he placed a steady hand on her shoulder."

            captain_sunwoo "Ji-hye-nim, I'm sorry. I should've arrived sooner… this isn't your fault. You did everything you could."
            ji_hye         "He's my nephew, Sunwoo. My family. And I couldn't save him. I couldn't save any of them!"

            ji_hye "What will I tell Jong-hee when he wakes up in the hospital? *crying*"

            captain_sunwoo "Pyeha is strong. He's stubborn, yes, but he's strong. We must trust that he knows what he's doing."
            captain_sunwoo "Come, Ji-Hye-nim. Let's get you out of here. It's late, but I know of a small vendor near the palace that serves steaming bowls of spicy kimchi jjigae."
            captain_sunwoo "A good meal might help calm your mind."
            ji_hye         "Kimchi jjigae? At this hour, Captain?"
            captain_sunwoo "It's Kyeongjang, Ji-hye-nim. There's always someone open. And I'm told this place also makes the best bindaetteok to pair with it."
            ji_hye         "*sniffling* You're persistent, Captain Sunwoo… but thank you. I… I appreciate it."

            "Sunwoo helped her to her feet."

            captain_sunwoo "Let's go. You need warmth, and you won't find it here in this cold room."

            "They began to leave."
            "Left alone, I emerged from the shadows where I had been standing invisibly."

            show chunghee normal_sad at left_char with Dissolve(0.2)
            hide captain_kang
            hide ya_ji_hye
            chung_hee "Aunt… I'm so sorry. Please forgive me."

            jump ch4_common_2

        "Do what she wants. Keep Aunt Ji-hye company.":
            stop sound

            show chunghee normal_neutral at left_char
            "I sighed, letting my shoulders relax slightly."

            chung_hee "I'll keep you company for a while, Aunt."

            show ya_ji_hye at right_char
            "Aunt Ji-hye's face lit up with gratitude."

            ji_hye "Thank you, Chung."

            "I clutched the amulet tighter in my hands. Her mind was an open book to me."
            "I saw her as a child, running hand in hand with my mother through the sunlit gardens of Kyeongjang."
            "The memories shifted — family gatherings, late-night conversations under the stars."
            "Then the memories darkened. I saw my mother standing before Aunt Ji-hye expressing her desire to venture to Tianho."
            "The last memory was Aunt knowing of my father and mother's fate. Captain Sunwoo was there, comforting her."

            show chunghee normal_sad at left_char
            chung_hee "Aunt…"

            ji_hye    "Chung, please… I've lost her once. Don't make me lose you too."

            show chunghee normal_neutral at left_char
            "I swallowed hard, pushing down the emotions that threatened to rise."

            chung_hee "Aunt, I promise. I'll return safely, and no harm will befall me."

            "She stepped forward and wrapped her arms around me."

            ji_hye "Do you remember the last time you, Jong-hee, and I ate outside together?"

            chung_hee "I believe it was three years ago, Aunt. At that little noodle shop in the marketplace. Jong-hee couldn't stop laughing at the way the broth splashed on your robes."
            ji_hye    "Yes… that's the one. You scolded him, but you were laughing too. I miss those days, Chung."

            show chunghee normal_sad at left_char
            "I fell quiet. It's not my choice, Aunt. It's never been."

            ji_hye    "I hope we can have that again someday. Promise me, Chung. Promise me you'll come back, so we can laugh together again."

            show chunghee normal_neutral at left_char
            "I placed a hand over hers, squeezing gently."

            chung_hee "I promise, Aunt. One day, we'll have that moment again."
            ji_hye    "I would love that, Chung—"

            jump ch4_common_1

        "Make Aunt Ji-hye go to sleep.":
            stop sound

            show chunghee normal_neutral at left_char
            "I gazed at Aunt Ji-Hye, her trembling form clutching her robes."

            chung_hee "Aunt… I'm sorry. I cannot afford to falter. You leave me no choice."

            show ya_ji_hye at right_char
            "Her eyes widened as she realized what I intended to do."

            ji_hye "Chung, no! Don't do this. Please, I'm begging you—"

            show chunghee alt_neutral at left_char
            "Before she could finish, I closed my eyes, channeling my focus. My mind reached into hers, gently but firmly quieting her frantic thoughts."

            ji_hye "Oh… I - Yes. I feel sleepy…"
            ji_hye "So… sleepy…"

            hide ya_ji_hye
            "Aunt Ji-hye blinked a few times. Slowly, she sank to her knees, her eyelids fluttering closed."
            "Carefully, I carried her to the spare sofa in the corner of the room."

            show chunghee normal_sad at left_char
            chung_hee "I'm sorry, Aunt. I promise… I will return."

            show captain_kang at right_char with Dissolve(0.2)
            "As I straightened, I sensed him before I saw him."

            captain_sunwoo "Pyeha, it's Kang Sunwoo. May I enter?"

            show chunghee normal_neutral at left_char
            "I turned, composing myself as the door opened."

            captain_sunwoo "Pyeha, I see that the Royal Advisor is… resting. I hope I am not intruding."
            chung_hee      "You are not. She was overwhelmed and needed rest. I trust you will keep your voice low, Captain."

            captain_sunwoo "Pyeha, forgive me for my boldness, but I understand you intend to leave the palace tonight. I must implore you to reconsider."
            chung_hee      "Captain, I appreciate your concern, but my decision is final."
            captain_sunwoo "Then allow me to accompany you, Pyeha. If you insist on facing danger, I will not let you face it alone."
            chung_hee      "Your place is here, Sunwoo. Kyeongjang needs its captain, and I need you to protect what I leave behind. This is my burden to bear."

            show chunghee alt_tense at left_char
            "The amulet in my hand began to glow brighter, its golden runes spiraling outward as I prepared to activate it."

            captain_sunwoo "Pyeha—"
            show chunghee normal_neutral at left_char
            chung_hee      "Take care of Aunt Ji-hye. And Jong-hee… tell him I will return."

            hide captain_kang
            "Captain Sunwoo carried Aunt Ji-hye and left the room."

            jump ch4_common_2


# =============================================================================
# SECTION 9: label ch4_common_1
# =============================================================================

label ch4_common_1:

    show captain_kang at right_char with Dissolve(0.2)
    show chunghee normal_neutral at left_char with Dissolve(0.2)
    "The heavy wooden door to the storage creaked open. A figure entered. It was Captain Sunwoo."
    "Upon entering, he bowed deeply."

    captain_sunwoo "Pyeha. Forgive my intrusion, but I have come at Ji-Hye's request. She feared for you."

    show chunghee normal_angry at left_char
    chung_hee      "Captain Sunwoo. You should know better than to interrupt the Emperor Lord's solitude."
    captain_sunwoo "Pyeha, I… I mean no disrespect. But if I may speak freely…"
    captain_sunwoo "Please don't do this… this path you are planning to choose is a perilous one."

    show chunghee normal_neutral at left_char
    "I raised an eyebrow."

    chung_hee "You think I do not know that, Captain? You think I haven't considered the risks?"

    show ya_ji_hye at right_char with Dissolve(0.2)
    "He kept his head bowed earnestly. Aunt Ji-hye held my hand tightly."

    ji_hye         "Chung… Please… *crying*"
    hide captain_kang
    show captain_kang at right_char with Dissolve(0.2)
    captain_sunwoo "I do not doubt your wisdom, Pyeha. But the burden of vengeance is not yours to bear alone."
    captain_sunwoo "If it is vengeance you seek, then allow me to gather the most skilled soldiers of Kyeongjang."
    show chunghee normal_neutral at left_char
    chung_hee      "This is something I must do on my own, Captain. Kyeongjang will not suffer more losses on my behalf."
    captain_sunwoo "Pyeha… please reconsider. Your safety is paramount. If you fall, the empire—"
    chung_hee      "The empire will endure. It has endured before. And I will not fall."

    "Sunwoo's gaze faltered. He bowed his head low."

    captain_sunwoo "Then may the Tetrad watch over you, Pyeha."

    "Both of them looked at each other and looked down."

    ji_hye "If you are truly set on this path, Chung, then all I can do is wish you safety. Please… come back to us. Come back to Jong-hee."
    show chunghee normal_sad at left_char
    chung_hee "I will return, Aunt. I swear it."

    "Her trembling hands touched my face, her eyes searching mine one last time before stepping back."

    ji_hye "Then I have nothing left to say except… goodbye, my Emperor Lord. May your journey be swift, and may justice be yours."

    captain_sunwoo "Royal Advisor. Would you care to walk back with me?"
    ji_hye         "Yes, Captain Sunwoo. I appreciate your kind offer."

    hide ya_ji_hye
    hide captain_kang
    "As they turned to leave, Aunt Ji-hye paused at the doorway."
    "Instead, she gave me a small, bittersweet smile before disappearing into the shadows with Captain Sunwoo."

    "Love you Jong-hee. Aunt Ji-Hye. Please forgive me."

    jump ch4_common_2


# =============================================================================
# SECTION 10: label ch4_common_2
# =============================================================================

label ch4_common_2:

    show chunghee alt_tense at left_char with Dissolve(0.2)
    "I clutched the amulet of teleportation in my hand. Its emerald glow pulsated with raw energy."

    "Sparks of green light danced along its golden edges."
    "I took a deep breath, steadying my resolve. My heartbeat slowed, my focus narrowing to a single thought—the place I needed to be."

    # play sound sfx_amulet_pulse                    # PLACEHOLDER

    show chunghee alt_charging at left_char
    chung_hee "Almighty Renji, Keeper of the Void and Sovereign of Time and Space, I beseech your power. Let your authority guide me across this mortal plane."
    chung_hee "Deliver me to my destination, that I may fulfill what destiny demands."

    "The room seemed to hold its breath. For a moment, everything stilled. Then, the amulet pulsed violently."

    chung_hee "To Tianho…"

    hide chunghee
    "Then I vanished into the void."

    # stop music fadeout 2.0
    stop sound

    jump ch4_tianho_dorian


# =============================================================================
# SECTION 11: label ch4_tianho_dorian (Dorian POV returns)
# =============================================================================

label ch4_tianho_dorian:

    scene cg_black with fade
    pause 1.0

    "Tianho"

    # scene bg_tianho_dorian_room with fade           # PLACEHOLDER
    # play music ost_tianho_memorial fadein 3.0       # PLACEHOLDER
    # play audio amb_tianho_afternoon loop fadein 2.0 # PLACEHOLDER

    show dorian neutral at left_char with Dissolve(0.2)
    "It had been eight months since Elias and I came to Tianho. Yuxuan graciously gave us a small house for us to live in."
    "Our house was a little far from the main city. The city itself was a shadow of what I remembered."
    "Yuxuan's manor, however, was a different story. The sprawling estate stood like a testament to prosperity."
    "In those eight months, life moved forward quietly. Elias, my little light in the darkness, would often dress in skirts and adorn himself with flowers to match Tedda."
    "The amulet that Elias once had stopped glowing entirely. Good riddance."

    "For me, I spent my time rebuilding—physically, mentally, emotionally."
    "The Dragon of Gale is dead."
    "Yuxuan had invited me more than once to visit my family's graves. Each time, I declined."
    "Until now."
    "Tomorrow marks the fifth anniversary of the tragedy of Tianho."

    "I turned to Elias, who had been sitting on the rug, giggling as he carefully tied a chain of flowers around Tedda's neck."

    show elias first_meet_happy at right_char_kids with Dissolve(0.2)
    show dorian neutral at left_char
    dorian "Elias… I think I'm ready."
    elias  "Ready for what, daddy?"

    show yuxuan normal_neutral at left_char with Dissolve(0.2)
    "Before I could answer, Yuxuan stepped into the room."

    yuxuan "For what, Dorian?"
    hide dorian
    show dorian neutral at right_char with Dissolve(0.2)
    dorian "To visit their graves. maybe now is the time."

    show yuxuan normal_happy at left_char
    "Yuxuan's expression softened."

    yuxuan "Praise the Prosperity Dragon. If you're ready, then I'll go with you."

    show dorian sad at right_char
    "I hesitated, glancing at the darkened sky outside the window."

    dorian "Do you think we could go now? I'd rather avoid running into the Empress of Gale if we can help it."

    show yuxuan normal_happy at left_char
    yuxuan "Sure!"

    show elias first_meet_happy at right_char_kids
    "Before I could respond, Elias sprang to his feet, clutching Tedda tightly to his chest."

    elias  "Ooh! Can me and Tedda come, daddy?"
    "Tedda: …"

    show dorian neutral at right_char
    "I knelt in front of him, placing a gentle hand on his head."

    dorian "I don't think it's a good idea… This isn't the kind of trip for you."
    show yuxuan alt_smile at left_char
    yuxuan "Oh, come now, Dorian. Let him come along. There are plenty of food stalls along the way. I'm sure Elias and Tedda would enjoy that, wouldn't you, Elias?"
    show elias first_meet_happy at right_char_kids
    elias  "Food? Like dumplings? And candy sticks? Ooooh, Tedda loves candy sticks!"

    "He spun in a little circle, holding Tedda above his head."

    show dorian neutral at right_char
    dorian "Alright, but you have to promise me you'll stay close. No running off, understand?"
    show yuxuan normal_happy at left_char
    yuxuan "Alright. It's settled. I'll have the carriage waiting!"

    hide dorian
    hide yuxuan
    hide elias
    scene cg_black with dissolve

    "The ride to the cemetery was quiet, save for the soft creak of the carriage wheels and the occasional chatter from Elias."

    jump ch4_cemetery


# =============================================================================
# SECTION 12: label ch4_cemetery
# =============================================================================

label ch4_cemetery:

    # scene bg_tianho_memorial_gate with fade         # PLACEHOLDER
    # play music ost_tianho_memorial fadein 2.0       # PLACEHOLDER (if not already playing)
    # play audio amb_cemetery loop fadein 2.0         # PLACEHOLDER

    show yuxuan normal_neutral at left_char with Dissolve(0.2)
    show dorian neutral at right_char with Dissolve(0.2)
    "It took thirty minutes to get there. The cemetery was modest yet serene."

    yuxuan "Take your time, Dorian. Elias and I will wander around for a bit."
    show elias first_meet_happy at right_char_kids with Dissolve(0.2)
    elias  "Tedda and I will wait for you, daddy!"
    show dorian neutral at right_char
    dorian "Stay close to Yuxuan, alright?"

    # scene bg_tianho_memorial with dissolve          # PLACEHOLDER

    hide yuxuan
    hide elias
    hide dorian
    show dorian sad at left_char with Dissolve(0.2)
    "And just like that, I was alone."
    "The morning wind whispered through the trees. I took a deep breath and began to walk."

    "Then I saw them."
    "Their graves stood together in a quiet corner of the cemetery."
    "Elara Burnham. Daniel. Emily. Sarah. Lucas."
    "My family."

    "My breath caught in my throat. My knees felt weak, and before I knew it, I had fallen to the ground in front of them."

    hide dorian
    # scene cg_dorian_family_graves with dissolve     # PLACEHOLDER
    # pause 2.0
    # scene bg_tianho_memorial with dissolve

    show dorian sad at left_char with Dissolve(0.2)
    dorian "My love, my heart..."

    dorian "It's been years. I've missed you all so much."
    dorian "I've been wandering for so long, trying to find my place in this world. But I never forgot you, and I never will."
    dorian "I'm so sorry for everything. I should have protected you. I should have been there with you all."

    "I stayed there, sitting in silence as the wind carried the soft rustle of leaves."
    "Time seemed to slip away. I finally looked up, noticing more people arriving."

    dorian "I wish I could stay longer, but I need to get a move on."

    "The words felt hollow as they left my lips."

    dorian "See you in my dreams, I guess."

    "I turned and began walking back toward the entrance."

    # scene bg_tianho_memorial_2 with dissolve        # PLACEHOLDER

    hide dorian
    show elias first_meet_happy at right_char_kids with Dissolve(0.2)
    "I couldn't find Yuxuan at his previous location. I scanned the area. Then I found Elias."
    "He was perched atop a gravestone, his little legs swinging back and forth as he cuddled Tedda close."

    elias "Tedda, look at the pretty flowers. They're so colorful!"
    "Tedda: …"
    elias "This one's my favorite, Tedda. It's the same color as your nose!"
    "Tedda: …"
    elias "Hehe, I love you, Tedda!"
    "Tedda: …"

    show dorian neutral at left_char with Dissolve(0.2)
    "I couldn't help but sigh as I approached him."

    dorian "Elias, you're not supposed to sit on top of gravestones. Get down from there."

    show elias first_meet_neutral at right_char_kids
    "Elias instinctively looked up at me. He jumped from his perch and walked up to me."

    elias  "Oh… Daddy, are you finished already?"
    show dorian neutral at left_char
    dorian "Yeah. I'm done. Where's Yuxuan? Why aren't you guys at our agreed spot?"

    show dorian neutral at left_char
    "I crouched down, brushing some dirt off his cheek."

    dorian "But Elias, this is a place of respect. We don't sit on gravestones, alright?"
    show elias first_meet_sad at right_char_kids
    elias  "Oh… sorry, daddy."

    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    "I scanned the area, my gaze landing on Yuxuan a little distance away. He was deep in conversation."

    yuxuan "Gentlemen, I appreciate your insights on the new propulsion system. It's a promising concept."

    "He adjusted a sleek communication device on his wrist."

    yuxuan "But I need to make sure that the team will be performing properly. Can I count on that, Mr. Diagro?"

    show elias first_meet_happy at right_char_kids
    "I glanced down at Elias, whose eyes were wide with curiosity."

    show dorian neutral at left_char with Dissolve(0.2)
    dorian "Elias, how long have you been separated from Yuxuan?"

    show elias first_meet_neutral at right_char_kids
    "Elias tilted his head, biting his lip as if deep in thought. He scrunched up his face, clearly losing track. He gave up and hugged Tedda."

    elias  "A lot, daddy. Mister Yuxuan was talking for a lot of minutes."
    show dorian neutral at left_char
    dorian "I see. So, he's been at it for a while now."

    "Elias nodded enthusiastically."
    "I stood there for a moment, watching Yuxuan in his element."

    jump ch4_yuxuan_convo


# =============================================================================
# SECTION 13: label ch4_yuxuan_convo
# =============================================================================

label ch4_yuxuan_convo:

    menu:

        "Continue to wait patiently.":
            $ ch4_yuxuan_interrupted = False

            show dorian neutral at left_char
            "I can give him a few more minutes."

            show yuxuan normal_neutral at right_char
            yuxuan "Look, I understand your concerns, and they are VALID, but I firmly believe that the market is ready for this innovation."
            yuxuan "But nothing! Risks are inherent in any endeavor, but we've mitigated them to the best of our abilities."
            yuxuan "Of course, of course. Yes. Ms. Jane, please prepare a detailed plan to be submitted at the end of your shift. Got it?"
            yuxuan "Overtime? But you're on the night shift and it's barely the end of the afternoon… Ugh. Okay fine, approved."
            show yuxuan normal_angry at right_char
            yuxuan "But you better have the plan prepared or, I swear in the name of the Prosperity dragon, I'm gonna have to replace you! No, I mean it! I really mean—"

            show dorian normal_alt_neutral at left_char
            "Seeing no other option, I waved at Yuxuan."
            show yuxuan normal_neutral at right_char
            "When he finally noticed me, his expression shifted from intense concentration to embarrassment."

            yuxuan "My apologies, I'll be back with you in just a moment. Ms. Ara, take the lead please."

            jump ch4_yuxuan_common

        "Try to get his attention by waving your hand.":
            $ ch4_yuxuan_interrupted = False

            show dorian normal_alt_neutral at left_char
            "I can give him a few more minutes."

            show yuxuan normal_neutral at right_char
            yuxuan "Look, I understand your concerns, and they are VALID, but I firmly believe that the market is ready for this innovation."
            yuxuan "But nothing! Risks are inherent in any endeavor, but we've mitigated them to the best of our abilities."
            yuxuan "Of course, of course. Yes. Ms. Jane, please prepare a detailed plan to be submitted at the end of your shift. Got it?"
            yuxuan "Overtime? But you're on the night shift and it's barely the end of the afternoon… Ugh. Okay fine, approved."
            show yuxuan normal_angry at right_char
            yuxuan "But you better have the plan prepared or, I swear in the name of the Prosperity dragon, I'm gonna have to replace you! No, I mean it! I really mean—"

            show dorian normal_alt_neutral at left_char
            "Seeing no other option, I waved at Yuxuan."
            show yuxuan normal_neutral at right_char
            yuxuan "My apologies, I'll be back with you in just a moment. Ms. Ara, take the lead please."

            jump ch4_yuxuan_common

        "Ask Elias and Tedda for help.":
            $ ch4_yuxuan_interrupted = False

            show dorian normal_alt_neutral at left_char
            "Elias could charm a mountain into moving."

            dorian "Elias, do you think you and Tedda can get Yuxuan to notice us?"

            show elias first_meet_happy at right_char_kids
            "Elias's face immediately lit up."

            elias "Okay, Daddy! Tedda and me can do it! Watch!"

            "He waved Tedda's little paw around wildly."

            elias  "Mister Yuxuan! See? Tedda's waving at you! She says hi really loud!"
            "Tedda: …"

            show yuxuan normal_angry at right_char with Dissolve(0.2)
            yuxuan "I already told you, Jane! Get it done by the end of your shift!"

            show elias first_meet_sad at right_char_kids
            elias  "Daddy, Mister Yuxuan didn't see Tedda."

            show dorian neutral at left_char
            "I pinched the bridge of my nose, trying not to laugh."

            dorian "It's okay, Elias. It's not your fault. He's busy."

            show elias first_meet_happy at right_char_kids
            "But Elias wasn't about to give up so easily."

            elias "Daddy! Tedda and me will give him flowers! Pretty flowers! Look over there!"

            hide elias
            show dorian serious at left_char
            "Before I could say a word, Elias bolted. I hurried after him, catching him just as he reached the gravestone."

            dorian "Elias, no. We can't just pick flowers from a gravestone. That's bad."
            show elias first_meet_sad at right_char_kids with Dissolve(0.2)
            elias  "Oh… sorry, daddy. We'll just continue waving then."

            show elias first_meet_happy at right_char_kids
            "Without a care in the world, he cheerfully continues to wave the toy's hands."

            jump ch4_yuxuan_common

        "Interrupt Yuxuan yourself.":
            $ ch4_yuxuan_interrupted = True
            $ yuxuan_affection += 1

            show dorian normal_alt_neutral at left_char
            "He told me to step in when this happens."

            show yuxuan normal_neutral at right_char with Dissolve(0.2)
            dorian "Yuxuan. Yuxuan?"
            yuxuan "Jane, I won't ask again. Get it done and send it to him. No excuses."
            dorian "Yuxuan. Hey, I'm finished."

            show yuxuan normal_happy at right_char
            "As I interrupted Yuxuan, he felt relieved."

            yuxuan "I must step away for a moment. Jane, I trust that you will take charge of the meeting… Huh? Of course it's you! Do you see any other Janes in there?"

            jump ch4_yuxuan_common


label ch4_yuxuan_common:

    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    show dorian neutral at left_char with Dissolve(0.2)
    "Yuxuan hung up his communication device with a soft sigh."
    "I chuckled, shaking my head."

    show yuxuan normal_happy at right_char
    yuxuan "Dorian, buddy, sorry for the spectacle. Are you finished? How was it?"
    show dorian neutral at left_char
    dorian "Don't mention it, Yu. And… yeah, I'm done. It felt nice, actually. Thank you for bringing us here."
    dorian "And I saw what you did with the flowers. It means a lot."
    dorian "You've already done so much for me. For us. And about the gravesite fees… I'll pay you back."

    "He waved a hand dismissively."

    show yuxuan normal_happy at right_char
    yuxuan "No, no, no! Pleasure's all mine, Dorian. It's the least I can do since you've saved me during the tragedy."
    yuxuan "And… we're friends. It's an honor for me to be there for you."
    show dorian smile at left_char
    dorian "Th-Thank you, Yu. I appreciate it."
    show yuxuan alt_smile at right_char
    yuxuan "Anyway, I think it's time for us to go. Before we leave, however, I suggest we try those treats from Hinami. Elias, do you like treats?"
    show elias first_meet_happy at right_char_kids with Dissolve(0.2)
    elias  "Treats?! Candies?"
    show yuxuan normal_neutral at right_char
    yuxuan "Well, treats, yes. But they're not candies. They're delectable treats from the Hinami booth here."

    "As Yuxuan continued speaking, I noticed a growing number of people entering the cemetery. Mjoll soldiers."

    show dorian serious at left_char
    "What in Tetrad's name are they doing here? Are they here for me? For Elias?"

    yuxuan "Come, I'll show you where the booth is. Let's go. You'll love them!"
    show dorian serious at left_char
    dorian "Wait, Yu—"

    show svante normal_nervous at left_char with Dissolve(0.2)
    svante "Excuse me, civilians. You need to get away from this place as soon as possible. It's not safe here."

    show dorian normal_alt_neutral at left_char
    "A strangely familiar young man approached us."
    "Svante. An aldorith from Mjoll."

    show yuxuan normal_angry at right_char with Dissolve(0.2)
    yuxuan "What? What do you mean it's not safe? This is a cemetery. Why would we need to leave?"
    svante "As I've said, sir. It's not safe. Please leave immediately."
    yuxuan "No. And who are YOU to tell us to leave?"
    svante "Sir, by the order of king Gustav, civilians must evacuate the premises as soon as possible."
    yuxuan "King Gustav? King Gustav has no jurisdiction here. This is Tianho!"
    svante "Sir, please… this is for your own safety."

    show dorian normal_alt_calm at left_char
    "I kept my head bowed, tightening my grip on Elias's hand."

    dorian "Thank you for the warning. We'll heed your advice and leave immediately. Which exit should we take?"
    show svante normal_nervous at left_char
    svante "Please exit through the main gate—the way you came. But hurry. There isn't much time."
    show yuxuan normal_angry at right_char
    yuxuan "No, we're not going anywhere without those damned treats—"
    show dorian serious at left_char
    dorian "Yu, let's just go. Please. Come on. Elias."
    show elias first_meet_neutral at right_char_kids
    elias  "Oh… Okay, daddy."

    hide svante
    hide yuxuan
    hide elias
    hide dorian
    jump ch4_cemetery_exit


# =============================================================================
# SECTION 14: label ch4_cemetery_exit
# =============================================================================

label ch4_cemetery_exit:

    # scene bg_tianho_memorial_gate with dissolve     # PLACEHOLDER
    # play music ost_cemetery_chaos fadein 0.5        # PLACEHOLDER

    show yuxuan normal_angry at right_char with Dissolve(0.2)
    show dorian neutral at left_char with Dissolve(0.2)
    "We hurriedly made our way through the cemetery gates."

    yuxuan "This is preposterous! I am Cheng Yuxuan, an inventor of great renown! And yet, here I am, herded out of a cemetery like some common criminal!"

    show dorian normal_alt_calm at left_char
    dorian "We're not being treated like common criminals, Yu. Calm down."
    show yuxuan normal_angry at right_char
    yuxuan "My work has changed lives! And now I'm being treated like some kind of threat? This is absolutely outrageous!"

    show elias first_meet_happy at right_char_kids with Dissolve(0.2)
    "Elias clung to my hand, his little giggles bubbling up despite the situation."

    show dorian normal_alt_neutral at left_char
    "I stepped closer, placing a firm hand on Yuxuan's shoulder to steady him. His rant came to an abrupt halt."

    show yuxuan normal_neutral at right_char
    yuxuan "…?!"

    "He looked at me, wide-eyed, almost frozen in place."

    show dorian neutral at left_char
    dorian "Yu, calm yourself. We're going to be fine. Let's just go home."

    show yuxuan normal_neutral at right_char
    "Yuxuan blinked rapidly, his face growing red."

    yuxuan "Ah. Um... Hehe, okay. T-Thank you, Dorian. I... Uh… appreciate your support."
    show dorian neutral at left_char
    dorian "Yu, are you okay? You seem... flustered."
    show elias first_meet_happy at right_char_kids
    elias  "Mister Yuxuan, your face matches Tedda's color!"
    show yuxuan normal_angry at right_char
    yuxuan "Wh-What?! No!!! I—"

    show dorian neutral at left_char
    dorian "Come on. Let's keep moving."
    show yuxuan normal_neutral at right_char
    yuxuan "You're right. Let's go."

    # scene bg_tianho_memorial with dissolve          # PLACEHOLDER

    hide yuxuan
    hide dorian
    hide elias

    show niko normal_base at left_char with Dissolve(0.2)
    show svante normal_nervous at right_char with Dissolve(0.2)
    niko    "You're kicking us out of here?! We have every right to be here!"
    svante  "Sir, please understand. This is for your safety."
    # show prophet at left_char                  # PLACEHOLDER — no sprite declared
    prophet "Safety? SAFETY?! We're here because we have brothers who died during the tragedy!"
    svante  "With all due respect, sir, this isn't my choice."
    show tian_xun at center_char with Dissolve(0.2)
    tian_xun "Protection? Bah! These fools don't deserve protection, Svante."
    svante   "S-Sir—"
    tian_xun "I could clear this whole area with one of my beauties, you know. One boom, and everyone's gone!"
    svante   "Sir Tian Xun. Please, that won't be necessary."
    tian_xun "Oh, but think of the possibilities, Svante! One boom, and they'll scatter like frightened mice. Gustav would love it! BOOM! BOOM!"
    show niko alt_annoyed at left_char
    niko     "You've got to be kidding me. This lunatic works for Gustav?"
    prophet  "Lunatic, indeed. You shame the name of Tianho, Tian Xun."
    tian_xun "Ashamed? HAHAHAHA! My parents were nobodies! Farmers!"
    tian_xun "GET OUT! OUT, OUT, OUT! BEFORE I GO BOOM!"
    show niko normal_ignore at left_char
    niko     "Tsk…"
    prophet  "Come, brother Niko. There is no reasoning with this one."
    show svante normal_sad at right_char
    svante   "I… I'm sorry."
    tian_xun "Run! Run, little lambs! HAHAHA!"

    tian_xun "Now come, Svante. We've got such lovely things to test today… Ooh!! I'm getting twitchy, temperamental, and itching to blow!"
    tian_xun "Hehehe~"

    # scene bg_tianho_memorial_gate with dissolve     # PLACEHOLDER

    hide tian_xun
    hide svante
    show niko normal_base at left_char with Dissolve(0.2)
    prophet "…"
    niko    "…"
    prophet "… Brother Niko?"
    niko    "Kaito… Please forgive me."
    prophet "Do not let this trouble you too deeply, brother Niko."
    niko    "I hope so."
    prophet "He knows, Niko. Kaito knows."

    show elias first_meet_happy at right_char_kids with Dissolve(0.2)
    elias   "Daddy, what about the treats?"
    show dorian neutral at left_char with Dissolve(0.2)
    dorian  "Let's get treats later when we get home. Come on."

    show niko alt_tense at left_char
    niko    "Hmm…"
    prophet "What is it, brother Niko?"
    niko    "Hmm… that toy… I remember…"
    niko    "Tedda… Wait, does that mean that the child is… Elias?"
    prophet "Elias? From Mjoll? Impossible. That boy was struck down by an arrow."
    niko    "Enoch probably intervened."
    niko    "And that means that man with the child… is Dorian."
    show niko normal_base at left_char
    prophet "Dorian… Ex-paladin Dorian… By Enoch, you're right!"
    niko    "The Dragon of Gale…"
    prophet "What are they doing here?"

    hide niko
    show dorian serious at left_char with Dissolve(0.2)
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    "The area was crowded with people rushing hurriedly away."

    yuxuan "What is going on? Why is everyone acting like this?"
    dorian "Mjoll… What are they up to now?"

    show yuxuan normal_angry at right_char
    yuxuan "This is intolerable. I'm calling for our carriage. We're leaving this madhouse at once."

    girl_ald_soldier "WAIT! HE KNOWS!! HE'S GETTING AWAY!! AFTER HIM, NOW!!"
    show tian_xun at center_char with Dissolve(0.2)
    tian_xun "What?! HE'S GETTING AWAY?! Bahaha, not on my watch! Fire the beauty—FIRE HER NOW!!"

    show elias first_meet_neutral at right_char_kids
    elias "Fire? What are they firing, daddy?"
    show yuxuan normal_neutral at right_char
    yuxuan "What are they talking about?"

    # play sound sfx_explosion_boom                  # PLACEHOLDER

    "-EXPLOSION-"

    hide tian_xun
    show yuxuan normal_sad at right_char
    "Before any of us could comprehend what was happening, a deafening BOOM shattered the air."
    "The ground trembled violently beneath our feet as dirt and debris rained down."

    yuxuan "By the Prosperity Dragon! What was that?!"

    "Then… a voice boomed inside my head."

    chung_hee "People of Tianho! I have been tricked by Mjoll! They've ambushed me—please, I need aid!"

    show yuxuan normal_neutral at right_char
    yuxuan "Wait—I can hear it! I can hear his voice!"
    show elias first_meet_neutral at right_char_kids
    elias  "Daddy… can you hear it too? What's happening?"

    show dorian serious at left_char
    "I nodded grimly, gripping Elias's hand tighter."

    woman_1 "The man is asking for aid! But I can't stay here! I have children!"
    man_1   "Have you seen the number of soldiers here? I'm not risking my family for this!"
    man_2   "Not my fight! I'm sorry, but I'm not dying today!"

    # scene bg_empty_battlefield with dissolve        # PLACEHOLDER

    hide yuxuan
    hide elias
    hide dorian
    chung_hee "Someone! Anyone! If you have honor, hear me! I seek only the king of Mjoll—this is my last warning."
    # show aoi at right_char                     # PLACEHOLDER — use aoi_base
    show aoi_base at right_char with Dissolve(0.2)
    aoi       "Such powerful mind channeling…"

    show tian_xun at center_char with Dissolve(0.2)
    tian_xun  "Honor?! HAHAHA! Don't make me laugh! You should've been a pile of ash by now!"
    tian_xun  "What you need is another! Another! BOOM! BOOM!"
    show aoi_base at right_char
    aoi       "Tian Xun, enough! The last thing we need is another one of your wasted bombs."
    tian_xun  "Grr…. You're no fun, Aoi."
    aoi       "Aldoriths, form up!"

    chung_hee "This is your last chance! I have no quarrel with you."

    mjoll_lars  "Your fight with our king is OUR fight, you fool!"
    mjoll_helga "We've been waiting for a real fight."
    mjoll_pavel "You're outnumbered, outclassed, and out of luck."

    show svante normal_nervous at left_char with Dissolve(0.2)
    svante "…"
    boy_ald_soldier "Your blood will stain the land, Emperor! For Father!"
    show svante normal_sad at left_char
    svante "No… No, this isn't right."
    girl_ald_soldier "What?! What did you say?"
    show svante normal_base at left_char
    svante "This man doesn't want to harm us! He's asking for a duel—he's giving us a chance to avoid more bloodshed!"
    mjoll_lars "Are you… are you siding with him? You'd betray your own people?"
    svante "No! I'm trying to stop more deaths! This man hasn't done anything wrong!"
    svante "Father said that the Emperor is a dishonorable man who murders and kills innocents. Look at him! He's offering us peace!"
    show aoi_base at right_char
    aoi    "Bold of an aldorith to have an opinion. Your Father will know about this."
    boy_ald_soldier "You really want to end up like your sister Kristin, huh? Dead for nothing?"
    show svante normal_base at left_char
    svante "All I'm saying is that this isn't the Emperor of Kyeongjang! He's far from him!"
    show tian_xun at center_char
    tian_xun "Oh, how touching! A traitor among the righteous. Let's see how your little 'peace talk' works against THIS!"
    show aoi_base at right_char
    aoi      "Tian Xun, stop! That's the last bomb we have!"

    # play sound sfx_explosion_boom                  # PLACEHOLDER

    "-EXPLOSION-"

    tian_xun  "HAHAHAHA! BOOM! BOOM!"
    mjoll_helga "The barrier… it's still there!"
    chung_hee  "I didn't come here to spill blood. But if you force my hand…"
    show aoi_battle_suit at right_char
    aoi        "Tsk! We wasted the last bomb because of you, Tian Xun! Aldoriths—kill him!"
    tian_xun   "KILL BOTH OF THEM! LET BOTH OF THEIR HEADS BE MOUNTED ON A SPIKE!!"
    tian_xun   "CHARGE!! CHA- *coughs* CHARGE!!"
    show svante normal_nervous at left_char
    svante     "Sir! What should we do?"
    chung_hee  "Run… Leave this place. You're not like them."

    # scene bg_tianho_memorial_gate with dissolve     # PLACEHOLDER

    hide tian_xun
    hide svante
    hide aoi_battle_suit
    show dorian neutral at left_char with Dissolve(0.2)
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    "The ground trembled beneath us as the second explosion ripped through the air."

    yuxuan "The carriage! It's here—it's at the front gate! But it can't get through!"

    show elias first_meet_crying at right_char_kids with Dissolve(0.2)
    "Elias stumbled."

    elias "Tedda! I dropped Tedda!"

    "He turned back, tears welling up in his eyes."

    elias  "We can't leave her! She's scared!"

    show dorian normal_alt_confident at left_char
    "I raised my hand. The ground shifted slightly as the earth responded to my will."

    dorian "There. Tedda's fine now. Let's go."

    "Then, we saw that the carriage was in sight—but so were they."
    "Three soldiers from Mjoll stood near the carriage."

    # show man_1 at right_char                   # PLACEHOLDER — no sprite declared
    man_1           "We need this carriage. It's ours now. Get off!"
    carriage_driver "I don't care who you are—I was called to pick Master Yuxuan up!"
    man_2           "Hey, buddy. We can do this the easy way, or we can do this the hard way."
    female_guard    "Get out of there if you know what's good for you!"
    carriage_driver "Ahh!! Okay! Okay!"

    show elias first_meet_neutral at right_char_kids
    "The second soldier turned, spotting us."

    show yuxuan normal_angry at right_char
    yuxuan       "Hey! Step away from the carriage! That's the property of Cheng Industries!"
    man_2        "If you're smart, you know better than to fight us."
    show elias first_meet_neutral at right_char_kids
    elias        "Daddy… They look scary…"
    show dorian serious at left_char
    dorian       "You're not taking this carriage. We have a child with us."
    female_guard "And? You think we care about your kid?"
    dorian       "This carriage doesn't belong to you. Step down now, or you'll regret it"
    man_1        "A channeler, huh?"
    man_2        "You don't scare me, pal. Now beat it!"

    "The soldier in the driver's seat cursed."

    female_guard "What?"

    show dorian dragon_eyes at left_char
    dorian "Step aside. Now."

    man_2 "Why I oughta! Someone ought to teach you some manners!"

    # play sound sfx_heartbeat loop                  # PLACEHOLDER

    $ _choice_timeout = 5.0
    menu:

        "Channel Earth.":
            $ ch4_carriage_qtc1 = "earth"
            $ _choice_timeout = 0
            stop sound

            # play sound sfx_earth_pillar             # PLACEHOLDER

            show dorian normal_alt_confident at left_char
            "I stomped the ground. The earth buckled beneath the soldier's feet, a jagged pillar shooting up and knocking the blade from his hands."
            "His head hit the ground, knocking him unconscious."

            dorian "You were warned."

        "Do nothing. Yuxuan, help!":
            $ ch4_carriage_qtc1 = "sleep_powder"
            $ _choice_timeout = 0
            stop sound

            show dorian sad at left_char
            "I froze, panic gripping me as the soldier's blade gleamed dangerously close."
            "Before I could react, Yuxuan reached into his satchel and flung a small pouch at the soldier."

            man_2  "Zzz… Zzz…"
            show yuxuan normal_happy at right_char
            yuxuan "Sleep powder. Courtesy of Cheng Industries. I knew this would come in handy!"

    # D1 converge
    female_guard    "This one's trouble! Fall back!"
    man_1           "Grr…. Hurry! Pull the reins again! Let's get out of here!"

    "The soldiers scrambled onto the carriage, yanking the driver out of the seat."

    carriage_driver "You can't do that! No!"

    # play sound sfx_heartbeat loop                  # PLACEHOLDER

    $ _choice_timeout = 5.0
    menu:

        "Stumble! Elias, help!":
            $ ch4_carriage_qtc2 = "stumble"
            $ _choice_timeout = 0
            stop sound

            show dorian sad at left_char
            "I tried to focus—but my foot caught on a loose rock, and I fell flat on my face."

            show yuxuan normal_sad at right_char
            yuxuan "Dorian!"
            show elias first_meet_happy at right_char_kids
            elias  "Tedda! Protect us!"

            "Elias flung his stuffed bear with all his might. The toy hit the female soldier dead in the face."

            female_guard "Pfttt—Waahhh!! Eww!!"

            "She flailed, grabbing at the reins, but the sudden commotion startled the horses."

            man_1 "Stop! WHOA!"

            # play sound sfx_carriage_crash             # PLACEHOLDER

            "The carriage lurched violently to the side. The entire thing tipped over."

            show elias first_meet_happy at right_char_kids
            elias  "Tedda! We did it!"
            show dorian neutral at left_char with Dissolve(0.2)
            dorian "Remind me never to underestimate that bear."

        "Use wind to knock them off!":
            $ ch4_carriage_qtc2 = "wind"
            $ _choice_timeout = 0
            stop sound

            # play sound sfx_wind_blast                # PLACEHOLDER

            show dorian normal_alt_confident at left_char
            "I planted my feet firmly and reached deep, calling on the winds."
            "With a sharp motion of my arm, the wind blasted toward the carriage."
            "The gust struck the soldiers with brutal force, knocking them clean off the back."

    # D2 converge
    carriage_driver "Please, get in!"

    hide dorian
    hide yuxuan
    hide elias
    scene cg_black with dissolve

    show dorian neutral at left_char with Dissolve(0.2)
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    show elias first_meet_neutral at right_char_kids with Dissolve(0.2)
    "The three of us hurriedly got inside the carriage."
    "Yuxuan sat across from me, as he held Elias close."

    show elias first_meet_neutral at right_char_kids
    elias  "Daddy… are we safe now?"

    show dorian neutral at left_char
    "I reached over and gently ruffled his hair."

    dorian "Almost. We're getting out of here."

    hide dorian
    hide yuxuan
    hide elias
    jump ch4_battlefield


# =============================================================================
# SECTION 15: label ch4_battlefield
# =============================================================================

label ch4_battlefield:

    "But then, as we turned a corner, we saw it."
    "The area near the cemetery was littered with bodies."
    "In the center of it all, a young man stood. His chest rose and fell unevenly."
    "His face was pale, slick with sweat and dirt, and his eye glowed faintly."

    "Then, a voice filled my head again."

    chung_hee "I beg… of you… Please… help… me…"

    show dorian serious at left_char with Dissolve(0.2)
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    "I froze, staring at him as the carriage slowed."

    chung_hee "Hurry… please. I've exhausted my powers… More of them… might come."

    "Before he could finish, his knees buckled, and he crumpled to the ground."

    dorian "He needs my help. I have to help him, Yu."
    show yuxuan normal_angry at right_char
    yuxuan "What?! Don't even think about it. We have Elias to protect."
    show elias first_meet_neutral at right_char_kids with Dissolve(0.2)
    elias  "Daddy… he's hurt. Are we… are we going to help him?"
    show dorian serious at left_char
    dorian "I have to."

    carriage_driver "Sir, I don't think we should stop."

    show dorian neutral at left_char
    dorian "We can't just leave him."
    show yuxuan normal_angry at right_char
    yuxuan "And risk our lives—and Elias's—for a stranger? Dorian, please!"
    show dorian neutral at left_char
    dorian "Yu, if it was you or Elias there, I would do anything to help."
    show yuxuan normal_sad at right_char
    yuxuan "Dorian…"
    show dorian neutral at left_char
    dorian "Please, Yu. Take Elias to safety and stay out of harm's way. I'll do everything I can."
    show yuxuan normal_neutral at right_char
    yuxuan "Fine. Meet me at my house, please. Just stay safe, Dorian. Promise me."

    dorian "I promise. Stay safe. You too, Elias."

    show elias first_meet_neutral at right_char_kids
    "Without another word, I opened the carriage door and jumped down."

    hide dorian
    hide yuxuan
    hide elias

    # scene bg_empty_battlefield with fade            # PLACEHOLDER

    show dorian serious at left_char with Dissolve(0.2)
    "As I hurriedly made my way over the scattered bodies."
    "One… four… eight… twelve…"
    "The air was thick with the metallic tang of blood, mingled with the acrid stench of burnt earth."

    # scene bg_frostcradle_bloodied with dissolve     # PLACEHOLDER — memory flashback

    show dorian sad at left_char
    "Too familiar."
    "Memories came flooding back – horrible ones."

    boy_ald_soldier  "Mercy!! Enoch save me!! Ahhh!!"
    girl_ald_soldier "We're just obeying orders! Don't kill us!! Ahh!!"
    dorian           "…"

    # scene bg_empty_battlefield with dissolve        # PLACEHOLDER

    "I clenched my fists, forcing myself to push the memories aside."

    "His pale body was riddled with deep gashes and bruises. His chest rose and fell unevenly."
    "I knelt beside him, my heart pounding."

    show dorian serious at left_char
    dorian "This is bad… this is really bad…"

    dorian "Listen to me. The clinic—I'll carry you. Just hold on, alright?"

    "I slipped my arms beneath his frail, battered body, carefully lifting him."
    "As I straightened, a soft, barely audible voice reached my ears."

    niko_raven "Does he have a pulse?"

    show dorian normal_alt_neutral at left_char
    "I froze, my eyes darting around."

    dorian     "Who said that? Hello?"
    niko_raven "Hello, I'm here. Does he have a pulse? Please check his pulse."

    jump ch4_niko_raven


# =============================================================================
# SECTION 16: label ch4_niko_raven
# =============================================================================

label ch4_niko_raven:

    show dorian neutral at left_char with Dissolve(0.2)
    "My gaze snapped to the source—a raven perched on a jagged piece of debris."
    "The bird let out an exasperated sigh—an actual sigh."

    niko_raven "*sighs* Can you check his pulse now, please?"

    "Still doubting my sanity, I pressed my fingers to the young man's wrist."

    dorian     "He's still holding on. But if I don't get him to a doctor soon, he won't make it."
    niko_raven "Hold on a second. I'll help you."

    "Before I could react, the raven's feathers began to shimmer with an ethereal, silvery glow."
    "Standing before me, where the raven once perched, was a tall, striking figure."

    show dorian normal_alt_neutral at left_char
    dorian "What the…"

    show niko normal_base at right_char with Dissolve(0.2)
    "He wasted no time, dropping to his knees beside the unconscious young man."
    "He pulled a small satchel from his side and opened it."

    niko "His pulse is weak, but he's still hanging on. Good. That gives me something to work with."

    "The seeds began to sprout, tiny shoots unfurling. Vines and leaves stretched forth."

    show dorian normal_alt_neutral at left_char
    dorian "Nature channeling… I've never seen one channel nature before."

    niko "He's losing blood too quickly. The paste will slow the bleeding."

    dorian "What… what are you doing?"
    niko   "He's losing blood too quickly. The paste will slow the bleeding and encourage his skin to knit itself back together."
    dorian "Is that safe? He can barely—"
    niko   "It's a tonic. It'll keep his organs from shutting down. If you're so worried, please help me keep his head steady."
    dorian "Got it."

    show niko normal_meditate at right_char
    "He muttered soft words under his breath."

    niko "His channeling energy is still fragile. His body is trying to give up, but I'm not letting it. Not yet."

    "The glow seeped into the young man's skin, and his breathing grew steadier."

    show dorian neutral at left_char
    dorian "Amazing…"
    show niko normal_base at right_char
    niko   "This will stabilize him for now, but he needs real rest—immediately."
    dorian "Who are you? And did this man… did he talk to you too?"

    niko   "Yes, this man reached out to me. Very potent mind channeling, no doubt."
    dorian "And only the two of us came to his aid?"
    niko   "I'm afraid so, yes."
    niko   "He's from Kyeongjang."

    show niko normal_smile at right_char
    "He extended a hand, his expression softening slightly."

    niko   "I'm Niko. Niko Tsukumo. I'm in service to the death god, Enoch. It's a pleasure to finally meet you one-on-one, Paladin Dorian."

    "I shook his hand."

    show dorian neutral at left_char
    dorian "Niko… Have we met before?"
    show niko normal_base at right_char
    niko   "We have. Five years ago. I was with my younger brother, Kaito. We crossed paths here in Tianho when you were with Paladin Cyrus."

    show dorian neutral at left_char
    dorian "I don't recall. I apologize."
    show niko normal_base at right_char
    niko   "Don't apologize. It's been a long time."
    dorian "You're a nature channeler. I take it you're from Clan Ligaya?"
    niko   "Contrary to popular belief, not every nature channeler hails from Clan Ligaya. My mother is from Clan Kaibig—the sister clan to Ligaya—and my father is from Hamatame, the village of shadows."

    jump ch4_svante_capture


# =============================================================================
# SECTION 17: label ch4_svante_capture
# =============================================================================

label ch4_svante_capture:

    show svante normal_nervous at left_char with Dissolve(0.2)
    show dorian serious at right_char with Dissolve(0.2)
    "Then, a flicker of movement caught my eye."
    "The moment he noticed my gaze, his eyes widened in panic."

    svante "…!"

    "He turned on his heel and bolted."
    "I held my palm outward. The ground beneath him rose to form restraints."

    svante "Please! Let me go! I'm not here to hurt you!"

    show dorian serious at right_char
    "I strode toward him."

    dorian "You knew something was going to happen here. Start talking. Now."

    show niko normal_serious at left_char with Dissolve(0.2)
    svante "I... I don't know everything. They didn't tell me much, but—"
    niko   "But you were with that lunatic. Don't act innocent now."
    svante "It wasn't like that! I was trying to help you! Please, you have to believe me!"
    niko   "Help us? By threatening us?"
    svante "I wasn't threatening you! I was trying to save you!"
    svante "They'll kill anyone who gets in their way. I… I didn't want to be part of this."
    niko   "Then why were you here at all? Who are you anyway?"
    show svante normal_nervous at right_char with Dissolve(0.2)
    svante "M-My name's Svante, sir. Please don't hurt me. I s-surrender."
    svante "I-I wanted to help him… I can't just walk away from them! They'd come after me!"

    show elias first_meet_happy at right_char_kids with Dissolve(0.2)
    elias  "Daddy!!"

    hide svante
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    "To my utter surprise, Yuxuan and Elias came running towards me."

    show dorian normal_alt_annoyed at left_char with Dissolve(0.2)
    dorian "Yuxuan?! What in Tetrad's name are you doing here?! You should be at the carriage!"

    show yuxuan normal_sad at right_char
    yuxuan "Dorian, we-we have a problem! There's an army—a whole battalion of Mjoll soldiers—heading this way! We're surrounded!"
    show svante normal_nervous at left_char with Dissolve(0.2)
    dorian "What?!"
    svante "I tried to warn you! You should've run when you had the chance! Now we're all going to die here!"
    show yuxuan normal_sad at right_char
    yuxuan "Dorian, what are we supposed to do? We can't fight them all!"
    show dorian normal_alt_annoyed at left_char
    dorian "You shouldn't have come back! You should've gotten the child out of here!"
    show yuxuan normal_neutral at right_char
    yuxuan "Dorian, we're not leaving you behind. We're in this together."
    show elias first_meet_neutral at right_char_kids
    elias  "Daddy, I wanted to be with you! I won't leave you, daddy!"

    "I groaned and opened my mouth to answer, but the sound of distant boots filled the cemetery air."

    show niko normal_serious at left_char with Dissolve(0.2)
    niko   "Calm down. How many soldiers did you see?"
    show yuxuan normal_sad at right_char
    yuxuan "I... I don't know. There were so many of them!"
    show niko normal_serious at left_char
    niko   "We can't stay here. We have to move. Now."
    show yuxuan normal_angry at right_char
    yuxuan "Move where?! We're surrounded!"

    man_1  "We have you surrounded! Surrender now and you might live to see another day!"
    show yuxuan normal_sad at right_char
    yuxuan "W-We surrender! Please! Don't hurt us!"

    show dorian serious at left_char
    "Before he could fully raise his hands, I grabbed his shoulder."

    dorian "Yu, no need to surrender."
    show svante normal_nervous at left_char with Dissolve(0.2)
    svante "He's right! If we surrender, we're as good as dead!"

    man_2  "Come out with your hands up! All of you! We won't ask again!"

    show aoi_battle_suit at right_char with Dissolve(0.2)
    aoi    "Back-up has finally arrived, Tian Xun."

    man_1     "S-Sorry, mam Aoi! It won't happen again!"
    show tian_xun at center_char with Dissolve(0.2)
    tian_xun  "HAHHAHAHA! Oh, but it better not! My darlings were perfectly timed and they ruined it! THEY RUINED IT!!"
    tian_xun  "I want fireworks! I want limbs flying! I want screams and smoke!"

    show aoi_battle_suit at right_char
    female_guard "We were under the impression that the—"
    aoi          "Save your excuses. Kill the target."
    female_guard "What about the others, mam?"
    aoi          "I don't care for them. Just make sure that the target is dealt with."
    tian_xun     "NO! KILL THEM! LEAVE NO SURVIVORS! THEY FOILED MY BEAUTIES!"
    tian_xun     "LEAVE NONE! NOT A SINGLE ONE!"

    show tian_xun at center_char
    "A man stormed into view, his movements erratic and exaggerated."

    tian_xun "My cannons! My beautiful cannons! They ruined everything!"
    tian_xun "ESPECIALLY THE TARGET!! HE WASTED MY BOMBS!"

    show aoi_battle_suit at right_char
    "The lady rolled her eyes."

    aoi      "Calm down, Tian Xun. For someone from Tianho, you're embarrassing yourself."
    tian_xun "Embarrassing?! You don't understand! The cannons were my masterpiece!"
    aoi      "You were the one who wasted your own bombs! Ugh!"
    aoi      "But enough. Focus on the task at hand."
    tian_xun "This is not a tantrum, Aoi! NOT A TANTRUM!!"
    tian_xun "I'M GONNA MAKE THEM BOOM… GONNA MAKE THEM ALL GO BOOM… HAHAHA…"

    show svante normal_nervous at left_char
    svante "They're going to shoot any minute now. Take cover!"

    show dorian serious at left_char with Dissolve(0.2)
    "My chest tightened."

    show elias first_meet_crying at right_char_kids
    elias "D-Daddy!"

    show aoi_battle_suit at right_char
    aoi "Ready! Aim! Fire!"

    # play sound sfx_arrow_volley                    # PLACEHOLDER

    "In an instant, a volley of arrows darkened the sky."
    "Before anyone could react, Svante stepped forward."

    show svante normal_base at left_char
    svante "Everyone, get back!"

    # play sound sfx_metal_barrier                   # PLACEHOLDER

    "A shimmering metallic sheen erupted from the ground around him."
    "The arrows struck the gleaming shield with a series of sharp clangs."

    show elias first_meet_crying at right_char_kids
    elias  "Daddy, get back! Get back!"

    show dorian serious at left_char
    "I pulled him behind me."

    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "By the Prosperity Dragon… I didn't think anyone could do that."
    show niko normal_base at left_char with Dissolve(0.2)
    niko   "A metal channeller, huh? Interesting…"

    "He tilted his head, studying Svante."

    niko "You don't see that very often around here in Ena."

    tian_xun     "GRRRR… THAT HANDSOME VIOLET-HAIRED BOY IS HELPING THEM!! CURSE YOU SVANTE!!"
    boy_ald_soldier "S-Svante's helping them!"
    man_1        "Grr…. You think you can defy us?"
    female_guard "He's helping them! That traitor!"
    man_2        "That means we have to take care of him, then. Second artillery units, ready… aim… fire!"

    # show mjoll_helga at right_char             # PLACEHOLDER — no sprite declared
    mjoll_helga "Arrow units! Continue to shoot!"
    show aoi_battle_suit at right_char with Dissolve(0.2)
    aoi "Cavalry units! Advance! Run them down!"
    tian_xun "YES! YES! ATTACK!"

    show niko normal_meditate at left_char with Dissolve(0.2)
    "As I prepared to act, Niko stepped forward. He knelt briefly, bowing his head."

    niko "Kuroi yami no chikara… watashi no michibikite. Chikara o ataete… Enoch-sama no tame ni."

    # play sound sfx_shadow_surge                    # PLACEHOLDER

    "A pulse of shadow erupted from his body, snaking through the air like living tendrils."

    man_1        "What the?! Is that the power of the death god?! I don't want to die!"
    mjoll_lars   "Get a grip, aldoriths!"
    mjoll_helga  "But what should we do, brother?"

    "The horses reared back, their eyes wide with terror."

    female_guard "Ahhh!! Tetrad save me!"
    mjoll_lars   "Ahhh!!"

    show niko normal_serious at left_char
    "Niko stood tall, his figure wreathed in a shroud of creeping shadows."

    show aoi_battle_suit at right_char
    aoi    "T-The death god?! So, they have a Death God's priest among them… No matter. Regroup and attack again!"

    "But her words fell on deaf ears."

    man_2        "Enoch, please forgive us! *cries* Have mercy on our souls!"
    female_guard "We're doomed! He's marked by the Death God Himself!"
    tian_xun     "WHAT?! What in the Prosperity Dragon's radiant name are all of you doing? Get up!"

    show aoi_battle_suit at right_char
    aoi "This is preposterous! What kind of power are we dealing with here?!"

    show tian_xun at center_char
    tian_xun "Preposterous? No, no, my dear Aoi. This is art! This… is genius! HAHAHA!"
    show aoi_battle_suit at right_char
    aoi      "Tian Xun, what are you doing?! We need to regroup!"
    tian_xun "Regroup? Oh no, no, no. This isn't the time to fall back, Aoi. It's time for my masterpiece!"
    aoi      "Wait… That's not…"
    tian_xun "YES!! YES!! HAHAHAHAHA!!"
    aoi      "You're insane! You can't use that here, Tian Xun! You'll destroy us all!"
    tian_xun "Destroy us? Oh, Aoi, don't be so dramatic. This. Is. Progress!"

    "From beneath his robe, Tian Xun pulled out a small, ornate container carved with intricate dragon motifs."

    show aoi_battle_suit at right_char
    aoi      "Are you daft?! Do you even understand what you're holding?!"
    tian_xun "Legends state that draconic fire can only be channeled by those who are direct descendants of the ancient dragons."
    tian_xun "A gift from the Prosperity Dragon itself… My eternal muse."

    "He pressed his lips to the container, kissing it."

    aoi      "Tian Xun, stop this madness!"
    tian_xun "Madness?! Madness would be not using this!"
    aoi      "…"
    tian_xun "Failure means King Gustav will have our heads mounted on his throne like trophies!"
    aoi      "Fine… Fine. Do it. Use it."
    tian_xun "Oh, you'll see, Aoi. Prepare my final beauty—the crescendo of my genius! BOOM! BOOM! HAHAHA!"
    show aoi_battle_suit at right_char
    aoi      "I'll get the other battalion of soldiers."
    # show mjoll_lars at left_char               # PLACEHOLDER
    mjoll_lars  "Mam!"
    # show mjoll_helga at left_char              # PLACEHOLDER
    mjoll_helga "Yes, mam."

    hide aoi_battle_suit
    show svante normal_nervous at left_char with Dissolve(0.2)
    "Svante turned to us, his form trembling."

    svante "Tian Xun… He… He's preparing another bomb!"
    show niko normal_serious at left_char with Dissolve(0.2)
    niko   "He's the lunatic who kicked us out of Tianho, isn't he? Everyone, stay close!"
    show svante normal_nervous at left_char
    svante "No! This isn't just another bomb! He's using his best from his personal collection… it's made of draconic fire!"
    show dorian serious at left_char with Dissolve(0.2)
    dorian "!?"
    show niko normal_serious at left_char
    niko   "Draconic fire?! Are they really that desperate to kill us?!"
    niko   "If they're not careful, they'll blow this entire place to ashes!"

    show dorian serious at left_char
    "I stepped forward, clutching Elias protectively to my side."

    show tian_xun at center_char
    "Tian Xun's voice rose in a demented crescendo."

    tian_xun "Oh, Prosperity Dragon, hear me now, your loyal servant!"
    tian_xun "Let your draconic fire consume the unworthy! Burn for me, my deity! BURN FOR GLORY! BURN FOR ART! BOOM! BOOM! HAHAHAHA!"

    hide tian_xun
    "Suddenly, the air around us shifted. A deafening roar erupted from the container."
    "The glowing projectile screamed toward us with terrifying speed."

    tian_xun "BEHOLD! DRACONIC FIRE! A MASTERPIECE BORN FROM THE PROSPERITY DRAGON!"

    show niko normal_serious at left_char
    niko   "Argh… Everybody! Get down!"
    show svante normal_nervous at left_char with Dissolve(0.2)
    svante "Almighty Enoch… Please save me…"
    boy_ald_soldier "Let's see how your metal powers save you from this one, Svante, dear brother."
    female_guard    "Haha! Look at him! He's terrified! The traitor aldorith will die at last!"
    man_1           "He'll die like the snake that he is."
    tian_xun        "DIE!! DIE!! DIE!! ALL FOR THE PROSPERITY DRAGON!!"

    hide niko
    hide svante
    hide dorian
    jump ch4_prosperity_dragon


# =============================================================================
# SECTION 19: label ch4_prosperity_dragon
# =============================================================================

label ch4_prosperity_dragon:

    # scene cg_prosperity_dragon_white with fade     # PLACEHOLDER
    # play music ost_prosperity_dragon fadein 0.5    # PLACEHOLDER

    "Suddenly, time seemed to stand still. Absolute silence."
    "I closed my eyes. Is this it?"

    # show prosperity_dragon at center_char      # PLACEHOLDER — no sprite declared
    prosperity_dragon "My child…"

    show dorian neutral at left_char with Dissolve(0.2)
    "My breath hitched."

    prosperity_dragon "It has been far too long since you last called upon me."
    show dorian neutral at left_char
    dorian            "…?"
    prosperity_dragon "Tell me, child, what is it that you desire?"

    "I swallowed hard."

    show dorian sad at left_char
    dorian "Please… You know what I need."
    prosperity_dragon "Speak it! Acknowledge what you seek."
    prosperity_dragon "I know what burns in your heart. But I will hear it from you, Dorian."

    "I clenched my fists."

    show dorian neutral at left_char
    dorian            "I… I need your power. Please… grant me your power again."
    prosperity_dragon "My power. How easily you forget, Dorian."
    prosperity_dragon "You have forgotten who you are! You have forsaken your very essence."

    "The air ignited around me. Small embers flickered to life."

    prosperity_dragon "And then, a memory."

    show dorian sad at left_char
    "The yaoguai king's hand, stained with blood, holding Elara's severed head high."

    yk     "The Dragonkin... I've been searching for you."
    dorian "Elara… Daniel… Emily… Sarah… Lucas… My family…"

    "The flames around me surged. Tears blurred my vision."

    show dorian sad at left_char
    dorian            "If only… If only I had been strong enough…"
    prosperity_dragon "Enough!"
    prosperity_dragon "My blood runs in your veins. You are DRAGONKIN! You only need to accept it!"

    "My hands shook."

    dorian "They might be put in danger because of me. I—"

    prosperity_dragon "The bomb… Channel your power, Dorian! Remember yourself. Remember your heritage."
    prosperity_dragon "Remember who you are."

    show dorian neutral at left_char
    dorian "I…"

    "The flames surrounding me grew brighter."

    $ ch4_draconic_choice = ""
    # play sound sfx_heartbeat loop                 # PLACEHOLDER

    $ _choice_timeout = 5.0
    menu:

        "Remember the tragedy of Tianho.":
            $ ch4_draconic_choice = "tianho"
            $ _choice_timeout = 0
            stop sound

            show dorian sad at left_char
            "The tragedy of Tianho—the screams, the chaos, the flames engulfing the city."
            "I saw their faces: desperate, terrified, looking to me as if I were a god who could fix everything."
            "The fires consumed the city that day. My hands still carried the ash of that failure."

            dorian "I'm sorry… I'm so sorry…"

            jump ch4_bad_end_bomb

        "Remember your family.":
            $ ch4_draconic_choice = "family"
            $ _choice_timeout = 0
            stop sound

            show dorian sad at left_char
            "Their laughter echoed in my ears. Elara's warm smile as she held Lucas in her arms."

            elara  "You've done enough, love. Just rest. Rest with us."
            dorian "Elara… I wasn't strong enough… I couldn't save you."

            jump ch4_bad_end_bomb

        "Remember the people who died at Mjoll because of you.":
            $ ch4_draconic_choice = "mjoll"
            $ _choice_timeout = 0
            stop sound

            show dorian sad at left_char
            "Their faces haunted me too. The aldoriths of Mjoll and… how could I forget? Vasily."

            vasily "My friend… How could you kill me?"
            dorian "Vasily… Friend, I… I didn't mean to! Forgive me…"

            jump ch4_bad_end_bomb

        "Remember yourself.":
            $ ch4_draconic_choice = "self"
            $ _choice_timeout = 0
            stop sound

            show dorian neutral at left_char
            "I closed my eyes, letting the voice of the Prosperity Dragon wash over me."

            dorian "The Dragon of Gale…"

            "The memories surged like a tidal wave."
            "But that was before the tragedy."

            prosperity_dragon "Rise up, child. Rise, and show them the might of your bloodline!"

            show dorian dragon_eyes at left_char
            "The flames surged around me, growing wild and untamed."

            jump ch4_draconic_fire


# =============================================================================
# SECTION 20: label ch4_bad_end_bomb
# =============================================================================

label ch4_bad_end_bomb:

    show dorian sad at left_char
    "The heat was unbearable. But I felt nothing."

    prosperity_dragon "Child… You have forgotten yourself."
    prosperity_dragon "For that, you are lost for eternity. This is where your journey ends. Farewell, Dorian."

    "His voice echoed faintly as the light engulfed me."
    "And then I saw them."
    "Elara stood there, radiant as ever, her arms outstretched."

    hide dorian
    elara  "You've done enough, my heart. Come home now. Rest."

    show dorian sad at left_char with Dissolve(0.2)
    "Tears streamed down my face as I reached for her."

    dorian "I'm so sorry… but I'm here now. I'm home."

    hide dorian
    # scene cg_bomb_bad_end with fade                # PLACEHOLDER
    # pause 2.0

    jump game_over


# =============================================================================
# SECTION 21: label ch4_draconic_fire
# =============================================================================

label ch4_draconic_fire:

    # stop music fadeout 0.5
    # play music ost_prosperity_dragon fadein 0.2    # PLACEHOLDER

    show dorian dragon_eyes at left_char with Dissolve(0.2)
    "I opened my eyes. The bomb was coming quickly."
    "I stepped forward, raising my hand toward the bomb."

    # scene bg_empty_battlefield with dissolve       # PLACEHOLDER

    # play sound sfx_draconic_fire                   # PLACEHOLDER

    "The flames roared, wild and feral, but I felt them bend to my will."

    dorian "Ryyaaahhhhhh!!!"

    hide dorian
    # scene cg_draconic_fire_surge with shock_cut    # PLACEHOLDER
    # pause 0.8
    # scene bg_empty_battlefield with dissolve

    show tian_xun at center_char with Dissolve(0.2)
    tian_xun "HAHAHAHA! YES! YES!!"
    tian_xun "Prosperity Dragon, witness this moment!"
    tian_xun "PROSPERITY DRAGON! WITNESS ME! MY FINAL WORK! BOOM! BOOM! HAHAHA—"

    hide tian_xun
    "The bomb slammed into the ground where Tian Xun stood, detonating with a force that shook the heavens."
    "His laughter turned to a guttural scream as the fire engulfed him."

    show niko normal_serious at left_char with Dissolve(0.2)
    vasily           "Ahhh!! Ahhhh!!!"
    girl_ald_soldier "What in the name of Enoch—"

    "The ground beneath her erupted, jagged pillars of molten rock spearing upward."

    boy_ald_soldier "C-Charge! Charge!"

    niko "Everyone, get behind my shadows!"
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "O-Okay…"
    niko   "Dorian, you too."

    hide niko
    hide yuxuan
    "They came at me in waves. But I killed them."

    mjoll_pavel  "No!! Impossible!! AHHHH!!!"
    man_2        "Ahh Ahhh Ahhhhh!!!! Curse you Svanteee!!!"
    female_guard "Ahhhh!!! I don't want to die!!"
    man_1        "Enoch save meeeee!! AHHHH!!"

    # stop music fadeout 2.0

    show dorian serious at left_char with Dissolve(0.2)
    "I stood there, breathing heavily."

    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "Dorian…"
    show svante normal_nervous at left_char with Dissolve(0.2)
    svante "What the…"
    show niko normal_base at left_char with Dissolve(0.2)
    niko   "Merciful Enoch… what did you just do?"

    show dorian neutral at right_char
    "I didn't answer. I… didn't know."

    show elias first_meet_neutral at right_char_kids with Dissolve(0.2)
    "Elias hugged me even more. Tedda hanging."

    elias "Daddy… is it over?"

    show aoi_battle_suit at right_char with Dissolve(0.2)
    aoi   "Tian Xun!! No!!"

    hide elias
    "Her voice rang out, raw with fury and disbelief."

    aoi         "You monsters! You dare kill him?! That genius, that visionary!"
    mjoll_helga "P-Pavel!! They killed Pavel! No!!"

    show aoi_battle_suit at right_char
    aoi        "CHARGE! Kill them all! Leave no survivors!"
    mjoll_lars "Soldiers, kill them!! Kill them all!! Charge!!"

    "The ground shook as the battalion surged forward."

    show yuxuan normal_angry at right_char with Dissolve(0.2)
    yuxuan "By the Prosperity Dragon! Another battalion?! Really?! How many soldiers do they even have?!"

    show dorian serious at left_char with Dissolve(0.2)
    "I turned to Svante."

    dorian "How many of you are here?"

    show svante normal_nervous at left_char
    "He pointed at the unconscious man."

    svante "A lot, sir. My father didn't want to take any chances."
    svante "We can't fight them forever. We're outnumbered ten to one!"

    show niko normal_serious at left_char with Dissolve(0.2)
    niko "I'll hold them off as long as I can with my shadows."
    niko "Any ideas, Dorian? Surely, you've got something else up your sleeve."

    show aoi_battle_suit at right_char
    aoi    "You cannot escape! Not even the Prosperity Dragon will save you from my wrath!"
    show dorian normal_alt_annoyed at left_char
    dorian "Tsk…"

    show yuxuan alt_think at right_char with Dissolve(0.2)
    "Yuxuan approached me."

    yuxuan "Dorian, listen. Seeing you creatively use your fire channeling abilities gave me an idea."
    yuxuan "I don't tell anyone this—like, ever—but I've got an underground lab nearby. It's hidden, secure."
    yuxuan "If you can use your earth powers to dig us a path, I can guide us the rest of the way."

    show dorian neutral at left_char
    "I arched a brow."

    dorian "Of course, I can."

    show niko normal_serious at left_char with Dissolve(0.2)
    "I turned to Niko."

    niko "If it keeps us alive, we go with his idea. But I'm covering us while we move."

    show aoi_battle_suit at right_char
    aoi        "Lars! Take care of those shadows! Push forward! Kill them all!"
    mjoll_lars "On it, mam! Charge, soldiers!"

    "The pounding of their boots grew louder, closer."

    # play sound sfx_earth_pillar                    # PLACEHOLDER

    show dorian normal_alt_confident at left_char
    "I took a deep breath, slamming my palms into the earth. The ground rumbled and groaned."

    dorian "Everyone, jump in—now!"
    show niko normal_base at left_char
    niko   "I'll be the last one to jump."

    hide aoi_battle_suit
    show yuxuan normal_happy at right_char with Dissolve(0.2)
    "Yuxuan didn't hesitate. He leapt in first."

    yuxuan "Come on. I'll catch you."

    show elias first_meet_neutral at right_char_kids with Dissolve(0.2)
    "Elias clutched Tedda to his chest."

    elias  "Tedda, don't let go!"
    "Tedda: …"

    show dorian serious at left_char with Dissolve(0.2)
    "I moved to the edge, hefting the unconscious man over my shoulder."

    show niko normal_base at left_char with Dissolve(0.2)
    niko   "Be careful with him! He's barely hanging on as it is!"
    show dorian serious at left_char
    dorian "I know. I've got him. Just keep them off us!"

    show svante normal_nervous at left_char with Dissolve(0.2)
    "Svante lingered at the edge, uncertainty clouding his features."

    dorian "You too. Jump. Now. I'll jump after you."
    svante "I… are you sure— I'm an aldorith I might—"
    show dorian normal_alt_annoyed at left_char
    dorian "Dragon's bollocks! Just jump!"
    svante "O-Okay, sir!"

    hide svante
    "He jumped, vanishing into the tunnel's depths."

    hide dorian
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    "I tightened my hold on the unconscious man and followed."

    yuxuan "That's everyone…You there! It's your turn!"
    show niko normal_base at left_char with Dissolve(0.2)
    niko   "Move over! Shadows, release!"

    # play sound sfx_tunnel_seal                     # PLACEHOLDER

    hide niko
    hide yuxuan
    "As he jumped, the shadows recoiled. I didn't waste a second—I slammed my hands into the dirt, sealing the tunnel shut above us."
    "The battlefield disappeared."
    "Darkness surrounded us."

    jump ch4_underground


# =============================================================================
# SECTION 22: label ch4_underground
# =============================================================================

label ch4_underground:

    scene cg_black with fade
    # play music ost_underground_move fadein 2.0     # PLACEHOLDER
    # play audio amb_tunnel loop fadein 1.5          # PLACEHOLDER

    show yuxuan normal_neutral at left_char with Dissolve(0.2)
    show niko normal_base at right_char with Dissolve(0.2)
    yuxuan "Is everyone alright?"
    niko   "Shh… Keep your voice down. They're still looking for us."

    show elias first_meet_neutral at right_char_kids with Dissolve(0.2)
    "Above us, we can faintly hear the muffled voices of the soldiers. Elias was about to say something when Yuxuan covered the child's mouth."

    mjoll_lars   "Where did they go?! Dammit! They've used the amulet!"
    mjoll_helga  "Pavel… *cries* Lars, I'm scared…"
    mjoll_lars   "Calm down, Helga. Aldoriths, search the area for any clues!"
    man_2        "You heard him, aldoriths! Search every nook and cranny at the cemetery!"
    female_guard "Sir yes, sir!"

    "And then—"

    show aoi_battle_suit at right_char with Dissolve(0.2)
    aoi "Ti… Tian Xun…"

    hide aoi_battle_suit
    "A pause."
    "Then, a bloodcurdling scream."

    aoi "TIAN XUN!!"

    show svante normal_nervous at left_char with Dissolve(0.2)
    show niko normal_base at right_char with Dissolve(0.2)
    "And as if the heavens themselves mourned, the sky split open, unleashing a torrential downpour."

    svante "It's raining now."
    niko   "Good. That way they can't hear us moving."

    hide svante
    hide niko
    hide yuxuan
    hide elias
    "I looked around. Darkness engulfed us, thick and suffocating. But then—"

    # scene bg_tianho_underground_1 with dissolve    # PLACEHOLDER

    show elias first_meet_happy at right_char_kids with Dissolve(0.2)
    "A soft glow flickered to life, illuminating Elias's small frame. He clutched a delicate, flower-shaped flashlight in his tiny hands."

    elias "Nice going, Tedda. The flashlight is helping."

    show dorian neutral at left_char with Dissolve(0.2)
    "I took his hand."

    dorian "Are you hurt? Injured?"

    show elias first_meet_happy at right_char_kids
    "Elias smiled and shook his head."

    elias  "We're fine, Daddy."

    show svante normal_nervous at left_char with Dissolve(0.2)
    svante "I-I really can't believe it… We made it. We actually made it."
    svante "Thank you… Thank you, sir! I could kiss your fee—"

    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    yuxuan "We're not out of danger yet. Everyone, stay close. Keep that light steady—we're moving now."

    hide dorian
    hide yuxuan
    hide svante
    hide elias
    scene cg_black with fade
    # stop music fadeout 2.0
    # stop audio fadeout 1.5

    pause 2.0

    show screen chapter_title_screen(
        "5",
        "Cheng Industries",
        subtitle="Tianho — The Underground Lab",
        duration=3.0
    )
    pause 3.0

    jump chapter_5

# =============================================================================
# END OF CHAPTER 4
# =============================================================================