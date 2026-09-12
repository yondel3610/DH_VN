###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  SCENE: CHAPTER 10 — The Yaoguai King's Deal

###############################################################################


# =============================================================================
# SECTION 1: IMAGE DECLARATIONS
# =============================================================================

# =============================================================================
# SECTION 2: AUDIO DECLARATIONS
# =============================================================================

# define audio.ost_ch10_dream      = "audio/music/ost_ch10_dream.ogg"         # PLACEHOLDER
# define audio.ost_ch10_yaoguai_deal = "audio/music/ost_ch10_yaoguai_deal.ogg" # PLACEHOLDER
# define audio.ost_ch10_bad_end    = "audio/music/ost_ch10_bad_end.ogg"       # PLACEHOLDER
# define audio.ost_ch10_alert      = "audio/music/ost_ch10_alert.ogg"         # PLACEHOLDER
# define audio.ost_ch10_boss       = "audio/music/ost_ch10_boss.ogg"          # PLACEHOLDER
# define audio.ost_ch10_rescue     = "audio/music/ost_ch10_rescue.ogg"        # PLACEHOLDER
# define audio.ost_ch10_aftermath  = "audio/music/ost_ch10_aftermath.ogg"     # PLACEHOLDER
# define audio.ost_ch10_credits    = "audio/music/ost_ch10_credits.ogg"       # PLACEHOLDER
# define audio.sfx_electric_net    = "audio/sfx/sfx_electric_net.ogg"         # PLACEHOLDER
# define audio.sfx_megaboom        = "audio/sfx/sfx_megaboom.ogg"             # PLACEHOLDER
# define audio.sfx_psychic_chains  = "audio/sfx/sfx_psychic_chains.ogg"       # PLACEHOLDER
# define audio.sfx_metal_blades    = "audio/sfx/sfx_metal_blades.ogg"         # PLACEHOLDER
# define audio.sfx_shadow_burst    = "audio/sfx/sfx_shadow_burst.ogg"         # PLACEHOLDER
# define audio.sfx_divine_lance    = "audio/sfx/sfx_divine_lance.ogg"         # PLACEHOLDER
# define audio.sfx_yaoguai_roar    = "audio/sfx/sfx_yaoguai_roar.ogg"        # PLACEHOLDER
# define audio.sfx_draconic_fire   = "audio/sfx/sfx_draconic_fire.ogg"        # PLACEHOLDER
# define audio.sfx_claw          = "audio/sfx/sfx_claws.ogg"                # PLACEHOLDER
# define audio.sfx_carriage_rumble = "audio/sfx/sfx_carriage_rumble.ogg"      # PLACEHOLDER
# define audio.sfx_cheng_jingle    = "audio/sfx/sfx_cheng_jingle.ogg"         # PLACEHOLDER (reuse)

# =============================================================================
# SECTION 3: GAME VARIABLES
# =============================================================================

# =============================================================================
# SECTION 4: LABEL CHAPTER_10 — Dream: Prosperity Dragon / Yaoguai King Deal
# =============================================================================

label chapter_10:
    $ save_name = "Chapter 10"
    # play music ost_ch10_dream fadein 2.0        # PLACEHOLDER — dream theme
    scene cg_black with fade
    
    show screen chapter_title_screen(
        "10",
        "The Deal",
        subtitle="Tianho",
        duration=3.0
    )
    pause 3.0
    scene plain_white with fade
    "A warm light shimmered behind my eyelids."
    "Then a voice-familiar, gentle, ancient, and layered with celestial resonance-whispered through the void."

    prosperity_dragon "Child... Listen to me..."
    prosperity_dragon "My child..."

    "But just as I reached toward her-"
    scene black with shock_cut
    "Darkness."
    play music audio.yaoguai_theme volume 0.8 fadein 1.5
    "The warmth was ripped away, swallowed by the cold. The world twisted into shadows. A heavy footstep echoed."
    "The air turned acrid."
    show dorian angry at left_char 
    show yk at right_char
    with Dissolve(0.2)
    voice audio.yk_ch10_line1  # transcript: "Dragon King."
    yk "Dragonkin..."

    "I spun around."

    voice audio.yk_ch10_line2  # transcript: "They sleep exhausted, vulnerable, that"
    yk "They sleep. Exhausted. Vulnerable. That ridiculous ceremony drained them. Their warriors lie scattered, half-drunk on memory. Tianho is wide open."

    "He raised a clawed hand, and behind him, silhouettes moved-legions of yaoguai hidden in the folds of night. Waiting."

    voice audio.yk_ch10_line3  # transcript: "Before dawn we strike at"
    yk "Before dawn, we strike. At their armies... at their soul. Their schools. Their homes. Their children."
    voice audio.yk_ch10_line4  # transcript: "Let them warn again. Let"
    yk "Let them mourn again. Let them remember anew."
    voice audio.dorian_ch10_line1  # transcript: "You monster, what do you"
    dorian "You monster!! What do you want?!"

    "He tilted his head, lips curling."

    voice audio.yk_ch10_line5  # transcript: "A deal, and a cream"
    yk "A deal. An agreement."
    voice audio.yk_ch10_line6  # transcript: "Give me Magnus. Give me"
    yk "Give me Magnus. Give me the winged man's unconscious body."
    voice audio.yk_ch10_line7  # transcript: "Do that, and TNO lives."
    yk "Do that... and Tianho lives. No blood. No fire. No screams. Just peace."
    yk "Refuse..."
    yk "And mark my words-Tianho will be ash before the sun rises."
    voice audio.dorian_ch10_line2  # transcript: "You wouldn't dare."
    dorian "You wouldn't dare-"

    "The Yaoguai King's eyes glinted-then he raised one jagged claw."

    voice audio.yk_ch10_line8  # transcript: "You doubt me? Fine. See"
    yk "You doubt me? Fine. See for yourself."

    show visions_ch10 with shock_cut
    "He snapped his fingers."
    "Visions flooded my mind, like a dam had burst inside my skull. Horrifyingly vivid:"
    "Yaoguai tearing through Tianho's sleeping streets-claws raking silk robes, teeth sinking into flesh. "
    "Fire against moonlight. Screams. A mother trying to shield her baby with trembling hands before her head ripped apart."
    "A soldier barely awake before teeth pierced his side. Children trampled in panic. Houses ablaze. Memorial lanterns crushed. I felt the people's agony."
    "The pain was unbearable."
    scene black with shock_cut
    show dorian normal_alt_tense at left_char 
    show yk at right_char
    with Dissolve(0.2)
    "When the vision snapped away, I nearly collapsed."

    voice audio.yk_ch10_line9  # transcript: "Now you understand make your"
    yk "Now you understand. Make your decision, dragonkin..."

    show dorian serious at left_char with Dissolve(0.1) 
    "I steadied myself, heart pounding like a war drum."

    voice audio.dorian_ch10_line3  # transcript: "I... I need time to"
    dorian "I... I need time. To think."
    voice audio.yk_ch10_line10  # transcript: "You will choose here and"
    yk "There is no time. You will choose here and now. The second you say no... they move."

    "My mind whirled-and then, I heard the familiar voice again."
    prosperity_dragon "I sense him... He's getting desperate. Impatient. His armies WILL attack Tianho."

    show dorian angry at left_char with Dissolve(0.1) 
    "My blood burned."
    "Rage-bitter, ancient-surged up. This monster."
    "He killed Elara."
    "He killed my children."
    "Their faces-gone too soon, smiling in dreams I could never have again. And now he wanted more?"
    "And then I heard it."
    "Elias' voice, giggling under fireworks. Tim spinning in the lanternlight. Weng's laugh. Yuxuan's smile. The people-my people."
    $ renpy.save("quick-1")

    prosperity_dragon "Breathe, my child... I am with you. Let not vengeance cloud your judgment."
    prosperity_dragon "The Yaoguai King... does not know what Magnus truly is and neither do you. To surrender him would be to surrender the unknown."
    prosperity_dragon "But if you refuse... the people of Tianho, weary from celebration, still dressed in joy, will awaken to carnage."

    jump ch10_deal_choice


# =============================================================================
# SECTION 5: LABEL CH10_DEAL_CHOICE
# =============================================================================

label ch10_deal_choice:

    menu:

        "Accept.":
            jump ch10_bad_end_accept

        "Do not accept.":
            jump ch10_refuse

        "Consult the Prosperity Dragon.":
            jump ch10_consult


# =============================================================================
# SECTION 6: LABEL CH10_BAD_END_ACCEPT — BAD ENDING: Accepted the Deal
# =============================================================================

label ch10_bad_end_accept:

    show dorian sad at left_char with Dissolve(0.1)
    voice audio.yk_ch10_line11  # transcript: "I knew you were always"
    yk "I knew you were always going to say yes."

    "The Yaoguai King's lips twisted into a crooked smile-satisfied, smug, victorious. He raised a hand, and the shadows behind him dispersed like vapor. The threat was withdrawn."

    scene black with fade

    # play music ost_ch10_bad_end fadein 1.0      # PLACEHOLDER — bad ending theme

    "Tianho would wake to another quiet morning. The streets would remain unburnt. Children would still laugh in the courtyards. No one would know how close they came to death."
    "But the cost..."
    "Magnus was taken, unconscious and bound in chains. I wasn't allowed to see his face. Not a word, not a goodbye."
    "The Prosperity Dragon's voice fell into silence. It did not return. It left me completely. Even its warmth was gone from my dreams. Its presence-snuffed out like a candle in deep water."
    "Days passed. Then weeks. Then-the world began to crumble. We heard the whispers first."

    scene bg_mjoll_destroyed with dissolve
    show snow_blizzard_1
    "Mjoll, the northern realm of snow and light, was the first to fall."
    "They said the mountains cracked open, that black mist spilled from the earth, and creatures with no mouths and too many eyes swept through the villages. The screams were swallowed. The snow ran red."
    "Hinami, Gale, the Centennial Isles, all of them destroyed by yaoguai."
    
    scene bg_tianho_city_night with fade
    "But Tianho... Tianho remained untouched. Exactly as he promised. Perfectly, horrifically untouched."
    "We had no contact with other nations. Not that we had a choice. There was no one left to contact. People began to leave. Not to run... just to fade."
    "Chung-hee left one night and never came back. No farewells. No goodbyes. We never heard from him or the empire of Kyeongjang."
    "Kyeongjang... Now, lost to time."

    scene black with dissolve

    "Niko joined the Prophets of Enoch, walking westward in silence. He told us, as the chosen of the Death God, that the world would be remade in its image. He smiled when he left. He didn't say goodbye."
    "Svante went home-to ash and broken stone. He said he needed to make peace with his brothers and sisters."
    "His dead brothers and sisters. We never heard from him again."
    "As for Yuxuan, Cheng Industries crumbled. The deals stopped. The trade dried. The joy left his voice, then the light left his eyes."
    "We found him one day, staring blankly into a broken screen, an empty bottle in his hand. In the end, it was just me and Elias."
    "We wandered through ashen fields where golden rice once swayed. We crossed rivers that now reeked of rot."
    "The towns were corpses-hollowed buildings with doors swinging open like mouths frozen in screams. There was no sun. Only smoke."
    "Elias held my hand tighter each day. He didn't cry anymore. He was learning what silence meant."
    "But the silence... didn't last. The Yaoguai followed."
    "I saw them."
    "Dozens. Then hundreds. Their claws gleamed like obsidian glass. Their eyes glowed with hunger. They walked without sound, without breath, without mercy."
    "They had waited. And now... they came for us."
    "The last thing I remember was the sound of him screaming my name-and then the light went out."

    jump ch10_bad_end_credits


# =============================================================================
# SECTION 7: LABEL CH10_REFUSE — Choice 2: Refuse / Wake Up
# =============================================================================

label ch10_refuse:

    show dorian angry at left_char with Dissolve(0.1)
    voice audio.dorian_ch10_line4  # transcript: "Never."
    dorian "Never."

    "The word left my mouth like thunder-final and resolute."
    "The Yaoguai King's expression shifted. No longer smug. No longer amused."
    "It twisted-wrath incarnate, as though my defiance was the deepest betrayal he'd ever known."
    "A thick silence bloomed between us. It pulsed like a second heartbeat, dense and waiting."

    voice audio.yk_ch10_line12  # transcript: "Then so be it. Let"
    yk "Then so be it. Let them drown in fire."

    "He took a step forward, face inches from mine, his breath a rot of ash and centuries."

    voice audio.yk_ch10_line13  # transcript: "Remember this night. It will"
    yk "Remember this night. It will become legend. And the blood spilled will be on your hands, dragonkin."
    voice audio.yk_ch10_line14  # transcript: "But should you change your"
    yk "But should you change your mind-and you will-you can find me where you saw Magnus. I'll be waiting..."

    "He's talking about the room with the sealed door."
    "Then, without another word, his body turned to black smoke-hissing as it evaporated-and the shadows surged behind him, spreading like a plague across the horizon."
    "They vanished into the winds. But I felt them still."
    "And then I heard his voice."

    prosperity_dragon "Child! Wake-wake now!"
    prosperity_dragon "They march now. They will strike from the southern hills."
    prosperity_dragon "Rally the Paladins. Gather every ally you can get. Help fortify the defenses. Set the alarm bells alight-yes, light them. The sound will not carry fast enough."
    prosperity_dragon "AWAKE! NOW!"

    "My eyes flew open."

    jump ch10_common_wake


# =============================================================================
# SECTION 8: LABEL CH10_CONSULT — Choice 3: Consult Dragon
# =============================================================================

label ch10_consult:

    show dorian normal_alt_tense at left_char with Dissolve(0.1)
    "I closed my eyes, my hands shaking."
    show dorian normal_alt_calm at left_char with Dissolve(0.1)

    voice audio.dorian_ch10_line5  # transcript: "Please, I don't know what"
    dorian "...Please. I don't know what to do."
    scene black with dissolve
    prosperity_dragon "Then listen, child... Let me tell you a story. As old as flame and wind..."
    prosperity_dragon "Long time ago before Enoch, there was once a prince named Zhan. Keeper of Li Mengtia's Endless Garden."
    prosperity_dragon "The Endless Garden was a place of miracles. Flowers that bloomed through winter's frost. Laughter that echoed across rivers clear as glass. His people adored him. The prosperity of his land knows no bounds."
    prosperity_dragon "At the center of it all... was a strange stone. Smooth, humming faintly. Zhan didn't know what it was. Just that it had always been there."
    prosperity_dragon "Seasons passed. The Garden grew richer. Zhan became the wealthiest of rulers. The most prosperous of them all."
    prosperity_dragon "But Zhan grew afraid. A conqueror came from the west. One who promised to spare the Garden if Zhan gave up the strange stone in the middle of the garden."
    prosperity_dragon "Zhan, afraid to lose everything, agreed. And true to his word... the conqueror spared the Garden."
    prosperity_dragon "But days passed, Zhan returned to find the trees wilting. The soil rotting. The laughter gone. The stone had not just fed the land... it was the land."
    prosperity_dragon "And the conqueror? He used the stone to build a fortress of shadows. And from it, he conquered ten other kingdoms. He slaughtered their men. Enslaved their women and children."
    prosperity_dragon "And Zhan, once beloved, stood in the ruins of what he had traded. He wept, of what thought he gave up a stone... but he had given away everything."
    prosperity_dragon "It is not my choice to make. I trust you to make the right decision, child."

    show dorian serious at left_char
    show yk at right_char
    with Dissolve(0.2)
    "I opened my eyes."
    "The Yaoguai King awaits for my decision."

    jump ch10_deal_choice


# =============================================================================
# SECTION 9: LABEL CH10_COMMON_WAKE — Wake Up / Storage Room Cameo / Alert
# =============================================================================

label ch10_common_wake:

    scene spare_room with flash

    "My body was drenched in sweat. The room was trembling. No-not the room. The ground."

    prosperity_dragon "Dorian! Listen to me! There is no room for hesitation now."

    "Elias was still sleeping near me. I touched his hair gently."
    "Then I quickly got dressed. There was no time for questions. No time for doubt."

    scene storage_room with dissolve
    voice audio.chace_ch10_line1
    "Chace: But... love, come on! I barely know him!"
    "Isagani: You said he just turned fourteen a few days ago, love. Fourteen. And his mother just died trying to keep him from being deported. Don't you care what happens to Yevhen?"
    voice audio.chace_ch10_line2
    "Chace: Of course I care! It's just-I don't know how to be anything to him. He's just a half-sibling. I didn't even know my dad had another kid until days ago."
    "Isagani: Funny. That didn't stop you with Maja."
    voice audio.chace_ch10_line3
    "Chace: Don't bring her into this, love. She's different."
    "Isagani: How? Because she was already in your life? Because loving her didn't feel like a risk?"
    voice audio.chace_ch10_line4
    "Chace: Yevhen's just a kid. A scared, angry kid who definitely doesn't want anything to do with me."
    "Isagani: Then be the first person who doesn't walk away. Love, if you turn your back on him now... that's not the man I said yes to."
    "Storyteller: Find out what happens next... in the explosive sequel to-A Tropical-"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep

    show yuxuan normal_neutral at left_char
    show niko normal_base at right_char
    show roboto happy at center_robot
    with Dissolve(0.2)

    voice audio.roboto_ch10_line1  # transcript: "A-A-A-A-O-Drama Pawsed by Mimment Master"
    roboto "A-A-Audiodrama paused by M-M-Master Yuxuan."
    voice audio.yuxuan_ch10_line1  # transcript: "So, thoughts? Come on, I"
    yuxuan "So... thoughts? Come on, I want honest feedback here!"
    voice audio.niko_ch10_line1  # transcript: "For starters, I love the"
    niko   "For starters, I love the acting. The guy who played Chace was perfect for the role."
    hide roboto
    show svante normal_base at center_char with Dissolve(0.2)
    voice audio.svante_ch10_line1  # transcript: "I... I agree! Even his"
    svante "I-I agree! Even his younger voice! The way he cried... it brought tears to my eyes!"

    hide niko
    show magnus clothed_no_wings at right_char with Dissolve(0.2)
    voice audio.magnus_ch10_line1  # transcript: "No well's voice was heaven"
    magnus "~Noel's voice... was heaven-sent... like silk, like rain, like sweet lament~"
    voice audio.yuxuan_ch10_line2  # transcript: "Yes, Roboto take note of"
    yuxuan "YES!! Roboto, take note of that. Praise from Magnus is a sign we're about to break the market!"

    hide svante
    show roboto happy at center_robot with Dissolve(0.2)
    voice audio.roboto_ch10_line2
    roboto "N-N-Noted. Cheng Industries... preparing hit tracker update. Logging Magnus endorsem-m-ment."

    hide magnus
    show niko alt_annoyed at right_char with Dissolve(0.2)
    voice audio.niko_ch10_line2
    niko   "Great. *yawns* Are we done here? I'm late for prayer."
    voice audio.yuxuan_ch10_line3  # transcript: "Honestly, I think his agani's"
    yuxuan "Honestly, I think Isagani's voice is underrated too. So grounded. So real. But enough about my tastes, I-"

    scene storage_room with Dissolve(0.2)
    "And then... I stepped into the room, the weight of urgency pressing on my shoulders."

    show dorian normal_alt_tense at left_char
    show magnus clothed_no_wings at right_char
    with Dissolve(0.2)

    voice audio.dorian_ch10_line6  # transcript: "They're coming."
    dorian "They're coming."
    voice audio.magnus_ch10_line2  # transcript: "Who?"
    magnus "Who?"

    "The room stilled. Every eye turned to me."

    voice audio.dorian_ch10_line7  # transcript: "The Yuguai King has made"
    dorian "The Yaoguai King has made his move. The attack has begun."
    show yuxuan normal_lying at center_char with Dissolve(0.2)
    voice audio.yuxuan_ch10_line4  # transcript: "Wait, but what?"
    yuxuan "Wait... w-what?"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep

    hide yuxuan
    show roboto malfunction at center_robot with Dissolve(0.2)

    voice audio.roboto_ch10_line3  # transcript: "incoming threat, but please reconfer."
    roboto "I-I-Incoming threat? P-Please reconfirm?"
    voice audio.dorian_ch10_line8  # transcript: "There's no time. Tion will"
    dorian "There's no time. Tianho will be attacked under an hour."

    jump ch10_departure


# =============================================================================
# SECTION 10: LABEL CH10_DEPARTURE — Underground Door / Goodbye to Kids
# =============================================================================

label ch10_departure:

    scene spare_room with fade

    "We woke up everyone inside the underground lab-Chung-hee, Miss Weng, and the kids. Tedda quietly gathered Elias and Tim and led them into a single room, locking the door behind her to keep them safe."

    show dorian serious at left_char
    show tedda_human at right_char
    with Dissolve(0.2)

    voice audio.dorian_ch10_line9  # transcript: "Please take care of Elias"
    dorian      "Please... take care of Elias, Tedda."
    tedda       "Don't worry, Sir Dorian. I'll make sure Elias and Tim are safe. I'll lock the door."

    "They slept together in a pile of pillows."
    scene spare_room with Dissolve(0.2)
    "The rest of us-me, Niko, Yuxuan, Chung-hee, Svante, Magnus, Miss Weng, and Roboto-hurried to the living room for a quick, urgent meeting."

    scene lab_cave_on with dissolve

    show chunghee normal_neutral at left_char
    show magnus clothed_no_wings at right_char
    show yuxuan normal_neutral at center_char
    with Dissolve(0.2)

    voice audio.chung_ch10_line1  # transcript: "Are you certain this is"
    chung_hee "Are you certain this is happening?"
    voice audio.magnus_ch10_line3  # transcript: "I trust Dorian. That's enough"
    magnus    "I trust Dorian. That's enough for me."
    show yuxuan normal_angry at center_char with Dissolve(0.1)
    voice audio.yuxuan_ch10_line5  # transcript: "It has to be that"
    yuxuan "It has to be that damned Yaoguai King. Probably the one who sent a doppelgänger to impersonate me! For all we know, anyone here could be fake!"
    voice audio.chung_ch10_line2  # transcript: "You won't worry. I saw"
    chung_hee "Yuxuan, don't worry. I saw through each of your minds. We're all safe."
    show yuxuan normal_lying at center_char with Dissolve(0.1)
    voice audio.yuxuan_ch10_line6  # transcript: "Oh, thank the prosperity dragon."
    yuxuan "Oh... thank the Prosperity Dragon."

    hide chunghee
    show dorian serious at left_char with Dissolve(0.2)
    voice audio.dorian_ch10_line10  # transcript: "You, can you send a"
    dorian    "Yu, can you send a message to Gao and Jiang immediately? We need to reach Paladin Feng. If he's still at Tianho at this hour, he might be able to mobilize the other paladins in time."
    show yuxuan normal_neutral at center_char with Dissolve(0.1)
    "Paladin Feng... My old friend. Once my closest ally. If he's still there, he'll act. He has to act."

    hide magnus
    hide yuxuan
    show svante normal_base at center_char
    show niko normal_base at right_char
    with Dissolve(0.2)

    voice audio.svante_ch10_line2  # transcript: "What about Lady Aui? She's"
    svante "What about Lady Aoi? She's an incredible water channeler. She could make a huge difference."
    voice audio.niko_ch10_line3  # transcript: "That is, if she's still"
    niko   "That is, if she's still in Tianho."
    voice audio.svante_ch10_line3  # transcript: "She sang during the festivities,"
    svante "She sang during the festivities, right? That means she might still be nearby. Though... she might ask for compensation."

    hide niko
    show weng happy at right_flip with Dissolve(0.2)
    weng   "Her song was beautiful! What a lovely young woman."

    hide weng
    show magnus clothed_no_wings at right_char with Dissolve(0.2)
    voice audio.magnus_ch10_line4  # transcript: "Wait, she's the one who"
    magnus "Wait... she's the one who sang at the festival? AND she's an incredible water channeler?"

    voice audio.svante_ch10_line4  # transcript: "Yes, that's why Father hired"
    svante "Yes! That's why Father hired her as a mercenary after Dorian. She deserted when Paladin Feng made a better offer."

    hide magnus
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    voice audio.chung_ch10_line3  # transcript: "She deserted when she and"
    chung_hee "She deserted when she and Tian Xun failed to eliminate me. Anyway, let's just hope she's still working with Feng. If she is, we might have a fighting chance."

    hide chunghee
    show yuxuan normal_neutral at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch10_line7  # transcript: "Roboto, establish connection with Lig"
    yuxuan "Roboto, establish connection with Li Gao and Sun Jiang immediately!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep

    hide svante
    show roboto happy at center_robot with Dissolve(0.2)
    voice audio.roboto_ch10_line4
    roboto "G-G-Got it, Master Yuxuan. Establishing connection in 3...2...1..."

    "The device crackled. A hologram shimmered to life-a flickering image of Jiang in his Cheng Industries uniform."

    voice audio.jiang_ch10_line1  # transcript: "Good evening Sir Yushuan, we're"
    jiang  "Good evening, sir Yuxuan. We're receiving your transmission. What's going on?"

    voice audio.yuxuan_ch10_line8
    yuxuan "Yes, Jiang. This is a full-scale alert. Patch in Gao-now."
    voice audio.jiang_ch10_line2  # transcript: "right away sir"
    jiang  "Right away, sir."
    voice audio.yuxuan_ch10_line9  # transcript: "Listen closely, there is no"
    yuxuan "Listen closely. There is no time for pleasantries. The Yaoguai are coming."

    voice audio.gao_ch10_line1  # transcript: "Y-Yell guy, what are they"
    gao    "Y-Yaoguai? What are they doing here?"
    voice audio.jiang_ch10_line3  # transcript: "Gal, Paladin Fang is still"
    jiang  "Gao, Paladin Feng is still here. I'm telling this to him now."
    voice audio.jiang_ch10_line4  # transcript: "Anything else, Master Yushuan?"
    jiang  "Anything else, Master Yuxuan?"
    voice audio.yuxuan_ch10_line10  # transcript: "Nothing else, please just tell"
    yuxuan "Nothing else. Please, just tell Paladin Feng."
    voice audio.jiang_ch10_line5  # transcript: "Let's get going gal. Hurry!"
    jiang  "Yes, sir. Let's get to it, Gao. Hurry!"

    "The screen blinked out."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep
    show roboto malfunction at center_robot with Dissolve(0.1)
    voice audio.roboto_ch10_line5  # transcript: "The connection terminated Master Yushuan."
    roboto "C-C-Connection terminated, Master Yuxuan."

    # $ feng_score += 1                           # +1 Feng alerted

    scene lab_cave_off with dissolve

    show dorian normal_alt_tense at left_char
    show chunghee normal_neutral at right_char
    with Dissolve(0.2)

    "I exhaled, realizing I'd been holding my breath. The lab felt heavier now-like the walls themselves could sense what was coming."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep
    show roboto error at center_char
    show dorian serious at left_char
    with Dissolve(0.2)
    voice audio.roboto_ch10_line6
    roboto    "F-F-Fear levels in the room are fluctuating at 63%%. Suggesting calming ambient music-"
    voice audio.chung_ch10_line4  # transcript: "If this happens tonight, we"
    chung_hee "If this happens tonight, we don't have long. We leave for Tianho now."

    hide roboto
    show svante normal_base at center_char with Dissolve(0.2)
    voice audio.svante_ch10_line5  # transcript: "We can set up a"
    svante "We can set up a makeshift command post there. An hour's not enough for full defense-but we have to try."

    hide svante
    show niko normal_base at center_char with Dissolve(0.2)
    voice audio.niko_ch10_line4  # transcript: "No more waiting. We move"
    niko "No more waiting. We move. Now."

    hide niko
    show magnus clothed_no_wings at center_char with Dissolve(0.2)
    voice audio.magnus_ch10_line5  # transcript: "Four hundred years. I slept"
    magnus    "Four hundred years, I slept in ice, and this is the week I wake to? Part of me thinks... maybe I was waiting for this."

    hide magnus
    show weng normal at center_char with Dissolve(0.2)
    weng      "Roboto and I will stay behind to protect the kids. This lab's shielded, reinforced. It'll hold."

    "She snapped her fingers. A flame sparked in her palm, steady and sharp."

    show weng serious at center_char with Dissolve(0.2)
    weng      "Any yaoguai stupid enough to get through that door? I'll make sure they burn to ash."

    play audio audio.sfx_back volume 0.7
    "A loud crack echoed from her spine as she stretched."

    hide chunghee
    show magnus clothed_no_wings at right_char with Dissolve(0.2)
    voice audio.magnus_ch10_line6  # transcript: "Such fire from a woman"
    magnus    "Such fire from a woman of iron and ember. But bones do not lie, Miss Weng."

    show weng normal at center_char with Dissolve(0.2)
    weng      "Oh shush, Magnus. Believe me, I've felled more enemies than I could count when I was your age."
    weng      "By the stars-getting old is not for the weak. Still... I trust the door holds. It always has."
    weng      "Roboto, be a dear and brew me a cup of tea, will you?"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep
    hide weng
    show roboto happy at center_robot with Dissolve(0.2)
    voice audio.roboto_ch10_line7  # transcript: "To-to-take care masters, please stay"
    roboto "T-T-Take care, Masters! Please stay alive!"
    voice audio.roboto_ch10_line8  # transcript: "I'll make you a quick"
    roboto "I'll make you a quick cup of tea, Miss W-W-Weng."

    scene underground_door with dissolve

    show magnus clothed_no_wings at right_char
    show niko normal_base at left_char
    show yuxuan normal_neutral at center_char
    with Dissolve(0.2)

    "We exited the door. The big metallic door for the underground laboratory closed."

    voice audio.door_ch10_line1  # transcript: "Good evening, Master Yushuang. A"
    door_voice "Good evening, Master Yuxuan. A reminder: Tonight is still the Fifth Anniversary of the Tragedy of Tianho. A day of remembrance for those we lost."
    voice audio.door_ch10_line2  # transcript: "Current city events include an"
    door_voice "Current city events include an afterparty at the Tavern of the Jade Serpent. Please drink responsibly."
    voice audio.magnus_ch10_line7  # transcript: "I'm talking door!"
    magnus "A... talking door!"
    voice audio.niko_ch10_line5  # transcript: "The city's partying not that"
    niko   "The city's partying... Not that I can blame them. But there's going to be a yaoguai attack. Soon."
    voice audio.yuxuan_ch10_line11  # transcript: "Double the security protocols. We"
    yuxuan "Double the security protocols. We cannot allow anyone unauthorized to go inside."

    # play sound sfx_door_chime                   # PLACEHOLDER — door chime

    voice audio.door_ch10_line3  # transcript: "Security and enhancement confirmed. Initiating"
    door_voice "Security enhancement confirmed. Initiating Protocol Lockdown: JIN-SHIELD. All channeling frequencies-nullified."
    voice audio.door_ch10_line4  # transcript: "perimeter defenses active. An authorized"
    door_voice "Perimeter defenses active. Unauthorized entry will result in automated defense response."
    voice audio.door_ch10_line5  # transcript: "Now unauthorized beam shall pass."
    door_voice "No unauthorized being shall pass."
    voice audio.niko_ch10_line6  # transcript: "Are you sure this thing"
    niko   "Are you sure this thing can hold, Yuxuan?"
    voice audio.door_ch10_line6  # transcript: "I am forced from genuine"
    door_voice "I am forged from Jinyan steel, tempered in the magma-forges of Yonghai. I do not buckle. I do not burn. I do not break."

    hide magnus
    hide niko
    show svante normal_base at left_char
    show chunghee normal_neutral at right_char
    with Dissolve(0.2)

    "Svante lifted his hand, trying to channel the metal. It won't budge."
    voice audio.svante_ch10_line6  # transcript: "It's right, my energy's getting"
    svante "It's right. My energy's getting dampened. Can't push even a breeze through it."
    voice audio.door_ch10_line8  # transcript: "Thank you for your feedback."
    door_voice "Thank you for your feedback. Here at Cheng Industries, we bring change. And yes, we take custom orders."

    hide svante
    show dorian serious at left_char with Dissolve(0.2)
    voice audio.dorian_ch10_line11  # transcript: "We're counting on you to"
    dorian "We're counting on you to protect them. The children... Weng... everyone inside."
    voice audio.door_ch10_line9  # transcript: "Affirmative. As per Mr. Yushuan's"
    door_voice "Affirmative. As per Master Yuxuan's settings, this unit will not play the Cheng Industries jingle unless he is 10 meters away."

    "The door's lights flickered once, then faded, locking into silent vigilance."
    "Everyone stood in a circle-Yuxuan's eyes scanning a datapad, Niko gripping his prayer beads, Svante nervously adjusting his gloves. "
    "Magnus, tapping his foot impatiently. Chung-hee, arms crossed, his brows drawn low."
    "All their attention was on Tianho."

    voice audio.yuxuan_ch10_line12  # transcript: "We'll head straight to the"
    yuxuan "We'll head straight to the eastern gate. We can set up defenses there."

    hide chunghee
    show niko normal_base at right_char with Dissolve(0.2)
    voice audio.niko_ch10_line7  # transcript: "We need to get people"
    niko "We need to get people to safety first."

    hide yuxuan
    show svante normal_sad at center_char with Dissolve(0.2)
    voice audio.svante_ch10_line7  # transcript: "I really hope Lady Owies"
    svante "I really hope Lady Aoi is still there. We'll need her..."

    hide niko
    show chunghee normal_neutral at right_char with Dissolve(0.2)
    voice audio.chung_ch10_line5  # transcript: "We only have 40 minutes."
    chung_hee "We only have 40 minutes. We need to hurry. I can use the amulet of teleportation to-"

    show dorian serious at left_char with Dissolve(0.1)
    voice audio.dorian_ch10_line12  # transcript: "Everyone, I'm not coming with"
    dorian    "Everyone, I'm not coming with you."

    "Heads turned. Silence fell like a blade."

    hide svante
    show magnus clothed_no_wings at center_char with Dissolve(0.2)
    voice audio.magnus_ch10_line8  # transcript: "What? No Dorian! We need"
    magnus "What? No, Dorian, we need every fighter we can get-"

    show dorian normal_alt_calm at left_char with Dissolve(0.1)
    voice audio.dorian_ch10_line13  # transcript: "You need to go, all"
    dorian "You need to go. All of you. Tianho needs you. You're stronger together-and you'll be able to set up defenses faster without me slowing you down."
    show dorian serious at left_char with Dissolve(0.1)

    voice audio.chung_ch10_line6  # transcript: "You're thinking of facing the"
    chung_hee "You're thinking of facing the Yaoguai King alone?"

    "I nodded once. My throat tightened."

    show dorian sad at left_char with Dissolve(0.2)
    voice audio.dorian_ch10_line14  # transcript: "Elora Sarah Daniel Emily Lucas"
    dorian "Elara. Sarah. Daniel. Emily... Lucas."

    "Their names cut into me like glass."

    voice audio.dorian_ch10_line15  # transcript: "He took everything. Burned it"
    dorian "He took everything. Burned it all. And I... I can't walk forward without facing him. This isn't just battle for me. It's blood. It's grief. It's personal."

    "The wind swallowed their responses, if any came. Behind me, I could feel their stares lingering. But my path was set."
    "Tonight, I would face the monster who tore my world apart. And either I would return..."
    "...or I would die with fire in my fists, and my family's names on my lips."

    jump ch10_route_farewell


# =============================================================================
# SECTION 11: LABEL CH10_ROUTE_FAREWELL — Route-Specific Farewells
# =============================================================================

label ch10_route_farewell:

    scene bg_tianho_underground_2 with dissolve

    # play music ost_ch10_alert fadein 1.0        # PLACEHOLDER — urgent alert theme

    if highest_character == "yuxuan":

        show dorian normal_alt_tense at left_char with Dissolve(0.2)

        "I kept walking."
        "Each step carried the weight of ghosts I could no longer protect. My fists clenched. My jaw tightened. I had to do this. Alone."
        "Then I heard it-footsteps pounding fast behind me."

        voice audio.yuxuan_ch10_line19  # transcript: "Dorian in"
        yuxuan "DORIAN!"
        show dorian serious at left_char with Dissolve(0.1)

        "I stopped. His voice cut through the silence like a blade. Urgent. Cracked. Furious."

        show yuxuan normal_angry at right_char with Dissolve(0.2)

        voice audio.yuxuan_ch10_line26  # transcript: "What in the Prosperity Dragon's"
        yuxuan "What in the Prosperity Dragon's name are you doing!?"

        "I turned halfway. There he was-panting."

        voice audio.dorian_ch10_line50  # transcript: "You please go back go"
        dorian "Yu, please. Go back. Go to Tianho."
        voice audio.yuxuan_ch10_line27  # transcript: "No, no, no, no. You"
        yuxuan "No. No, no, no-you don't get to play hero right now. This is suicide, Dorian! You know what the Yaoguai King can do! You really think you can take him alone?"
        voice audio.dorian_ch10_line26  # transcript: "I have to do this."
        dorian "I have to do this."
        voice audio.yuxuan_ch10_line28  # transcript: "No, you don't. You could"
        yuxuan "No, you don't! You could help us! You could protect more people! Why throw yourself away for revenge? It's selfish."
        voice audio.yuxuan_ch10_line29  # transcript: "I thought we were past"
        yuxuan "I thought we were past this. I thought we were a team. I... I thought we were family ever since the blizzard at Frostcradle. I..."

        "His voice broke."

        show yuxuan normal_sad at right_char with Dissolve(0.1)

        voice audio.yuxuan_ch10_line30  # transcript: "I don't want to lose"
        yuxuan "I don't want to lose you, Dorian..."
        voice audio.dorian_ch10_line52  # transcript: "I don't plan on dying,"
        dorian "I don't plan on dying, Yu."
        voice audio.yuxuan_ch10_line31  # transcript: "Well neither did your wife"
        yuxuan "Well, neither did your wife. Nor your kids. Nor Count Vasily. Nor my friends. Nor-"
        voice audio.yuxuan_ch10_line32  # transcript: "You know what? Fine."
        yuxuan "You know what? Fine."

        "His hands shook. His eyes shimmered from the underground lights, unshed tears."

        voice audio.yuxuan_ch10_line33  # transcript: "Do what you want. Be"
        yuxuan "Do what you want. Be the tragic Paladin. Die a noble death if that's what helps you sleep."
        
        hide yuxuan with Dissolve(0.1)
        "He turned, robe whipping behind him as he ran. His footsteps faded behind me."
        show dorian sad at left_char with Dissolve(0.1)
        "And I kept walking. Toward the dark. Toward him."
        show dorian serious at left_char with Dissolve(0.1)
        "I'm so sorry, Yu."

    elif highest_character == "chunghee":

        show dorian normal_alt_tense at left_char with Dissolve(0.2)

        "I kept walking."
        "Each step carried the weight of ghosts I could no longer protect. My fists clenched. My jaw tightened. I had to do this. Alone."
        "Then a voice thundered inside my head, not spoken aloud but pulsing through my chest like a divine decree."

        voice audio.chung_ch10_line16  # transcript: "Dorian, what do you think"
        chung_hee "Dorian. What do you think you are doing?"

        "Footsteps followed, fast, heavy, resolute. Chung-hee was behind me-his presence unmistakable."
        show dorian serious at left_char 
        show chunghee normal_angry at right_char
        with Dissolve(0.2)

        voice audio.dorian_ch10_line21  # transcript: "Go to Tion O. They"
        dorian    "Go to Tianho. They need you more than I do."
        voice audio.chung_ch10_line17  # transcript: "The Yagwai King isn't some"
        chung_hee "The Yaoguai King isn't some warlord you can stab through the heart. He's not a man-he's a force. A storm. You'll be throwing yourself into a hurricane fueled by rot and fury."
        voice audio.chung_ch10_line18  # transcript: "You'll die for Vengeance story"
        chung_hee "You'll die for vengeance, Dorian. And it won't bring them back."
        voice audio.dorian_ch10_line22  # transcript: "This is personal, Chong."
        dorian    "This is personal, Chung."
        voice audio.chung_ch10_line19  # transcript: "Personal. You think you're the"
        chung_hee "Personal? You think you're the only one who's ever lost someone? You're not the only man dragging corpses through the dark, Dorian."

        "I froze. Just for a second."
        show chunghee normal_v2 at right_char with Dissolve(0.1)
        voice audio.chung_ch10_line20  # transcript: "I once told Aunt Ye"
        chung_hee "I once told Aunt Ji-hye I had to face King Gustav alone. Said no one else could understand. That no one else could carry my war. I thought I was being noble. Brave."
        voice audio.chung_ch10_line21  # transcript: "I was wrong. I stood"
        chung_hee "I was wrong. I stood there in the battleground. Like a fool. Begging for mercy for anyone who would come by."
        voice audio.chung_ch10_line22  # transcript: "Then you and the others"
        chung_hee "Then you and the others came along. You, Niko, Svante, Yuxuan and Elias. You nursed me back to health."
        voice audio.chung_ch10_line23  # transcript: "and I realized I had"
        chung_hee "Then I realized I made a mistake. A mistake that nearly cost me my life. I would've died there if you-if all of you-hadn't been there."
        voice audio.dorian_ch10_line23  # transcript: "This is different. You don't"
        dorian    "This is different. You don't know what he took from me, Chung. I can't even hear his voice without seeing my family's faces-burning, screaming, gone."
        voice audio.chung_ch10_line24  # transcript: "You think I don't know"
        chung_hee "You think I don't know what that feels like?"
        voice audio.chung_ch10_line25  # transcript: "Every night I lie awake"
        chung_hee "Every night, I lie awake imagining how my mother and father must have died. Whether they were afraid. Whether they suffered. Whether they called for me before dying at Tianho."

        "He stepped closer, and the air thickened."
        show chunghee normal_sad at right_char with Dissolve(0.1)
        voice audio.chung_ch10_line26  # transcript: "Their deaths hang on me"
        chung_hee "Their deaths hang on me like chains, Dorian. But I bear them. And I'm telling you-don't add your name to the dead by going alone. I'm begging you-don't do this."
        show dorian sad at left_char 
        hide chunghee
        with Dissolve(0.1) 
        "I stared at him for a moment. And I turned. Started walking again. Behind me, I heard nothing. No words. No movement. Only silence."
        show dorian serious at left_char with Dissolve(0.1) 

        "...I'm sorry, Chung."

    elif highest_character == "svante":

        show dorian normal_alt_tense at left_char with Dissolve(0.2)

        "I kept walking."
        "Each step carried the weight of ghosts I could no longer protect. My fists clenched. My jaw tightened. I had to do this. Alone."
        "Then I heard it-footsteps pounding fast behind me."

        voice audio.svante_ch10_line8  # transcript: "Dorian"
        svante "Dorian!"

        "It was Svante. Breathless. His face flushed, eyes wide with panic and frustration as he caught up beside me."

        show svante normal_angry at right_char
        show dorian serious at left_char
        with Dissolve(0.2)

        voice audio.svante_ch10_line9  # transcript: "You can't go alone! The"
        svante "You can't go alone! The Yaoguai King-he's not just some monster. He's old, Dorian. Too powerful. Please, come back. Come with us to Tianho."
        voice audio.svante_ch10_line10  # transcript: "You shwants worried sick? I'm"
        svante "Yuxuan's worried sick. I'm worried sick. We need to-"
        voice audio.dorian_ch10_line44  # transcript: "Sponte, go back. I have"
        dorian "Svante, go back. I have to do this alone."
        voice audio.svante_ch10_line11  # transcript: "What? Why? Why does it"
        svante "W-What? Why?! Why does it have to be you, and why does it have to be alone?"
        voice audio.dorian_ch10_line45  # transcript: "It's personal."
        dorian "It... It's personal."

        "He grabbed my arm-his grip trembling."

        show svante normal_sad at right_char

        voice audio.svante_ch10_line12  # transcript: "You're being selfish. What about"
        svante "You're being selfish. What about Elias? You're all he has. He lost Queen Ekaterina, his mother-don't make him lose you, too!"

        "I looked at him, my heart twisting."

        voice audio.dorian_ch10_line39  # transcript: "I'm not planning to die."
        dorian "I'm not planning to die."

        "Svante looked down."

        voice audio.svante_ch10_line13  # transcript: "Neither did Kristen when she"
        svante "Neither did Kristin when she stood up to Count Vasily."
        voice audio.svante_ch10_line14  # transcript: "You were there, Dorian. You"
        svante "You were there, Dorian. You saw what they did to her. And then I blamed you and Elias."
        voice audio.svante_ch10_line15  # transcript: "So don't lie to me"
        svante "So don't lie to me now. Don't say you'll survive just because you want to."

        "Silence."
        show dorian sad at left_char with Dissolve(0.1) 
        voice audio.dorian_ch10_line38  # transcript: "I have to do this,"
        dorian "I have to do this."

        "He stared at me, breath ragged, anger and sorrow warring on his face. And then-He let go."
        "He turned away, shoulders slumped. But just before he walked back to the others, he looked over his shoulder. His eyes-violet-met mine."

        voice audio.svante_ch10_line16  # transcript: "I know we only met"
        svante "I know we only met a few days ago but..."
        voice audio.svante_ch10_line17  # transcript: "Please don't make me more"
        svante "...Please don't make me mourn you too."
        hide svante with Dissolve(0.1)
        "I watched him disappear into the shadows, his silhouette swallowed by the dim underground lights. I stood there for a moment longer, the ache in my chest heavier than before."
        show dorian serious at left_char with Dissolve(0.1)
        "I'm sorry, Svante."

    elif highest_character == "niko":

        show dorian normal_alt_tense at left_char with Dissolve(0.2)

        "I kept walking."
        "Each step carried the weight of ghosts I could no longer protect. My fists clenched. My jaw tightened. I had to do this. Alone."
        "Then I heard it-footsteps pounding fast behind me."
        
        voice audio.niko_ch10_line19
        niko "Dorian."

        "I stopped, but didn't turn. The sound of his footsteps caught up with mine."

        show niko normal_anger at right_char 
        show dorian serious at left_char 
        with Dissolve(0.2)

        voice audio.niko_ch10_line20  # transcript: "Forget me, forget about the"
        niko "Forget me. Forget about the others. But what about Elias?"

        "I flinched."

        voice audio.niko_ch10_line21  # transcript: "You know the Yalgui King"
        niko "You know the Yaoguai King isn't just some monster in the dark. You've seen what he is. What he does."
        voice audio.niko_ch10_line22  # transcript: "You're not invincible Dorian. Please,"
        niko "You're not invincible, Dorian. Please... come back to Tianho. Maybe we can-"
        voice audio.dorian_ch10_line51  # transcript: "I have to do this."
        dorian "I have to do this, Niko."
        voice audio.niko_ch10_line23  # transcript: "Then I'm coming with you."
        niko "Then I'm coming with you. You shouldn't-"

        show dorian normal_alt_calm at left_char with Dissolve(0.1)
        "I shook my head and raised my hand. And he stopped. Stilled. His expression twisted, somewhere between pleading and fury."
        show dorian serious at left_char
        show niko normal_sad at right_char
        with Dissolve(0.1)

        voice audio.niko_ch10_line24  # transcript: "Are you really willing to"
        niko "Are you really willing to leave Elias behind? Leave him fatherless? To chase a death you know is coming?"
        voice audio.dorian_ch10_line46  # transcript: "I'm not planning to die."
        dorian "I'm not planning to die."
        voice audio.niko_ch10_line25  # transcript: "Well neither did Kaito."
        niko "Well, neither did Kaito."
        voice audio.niko_ch10_line26  # transcript: "He thought he could save"
        niko "He thought he could save everyone in that burning building. Thought strength would be enough. Now he's in Xianlun."

        "I turned slightly. Just enough to look at him from the corner of my eye."
        voice audio.dorian_ch10_line40
        dorian "You, of all people-Enoch's chosen and a Prophet of the Death God-should understand. Death is natural. Normal. I'm choosing this. That's the Law of Enoch, right?"
        
        voice audio.dorian_ch10_line41  # transcript: "Don't deny someone their death."
        dorian "Don't deny someone their death."

        "That silenced him. For a beat. Then-he stepped back, something breaking behind his eyes."
        show niko alt_disappointed at right_char with Dissolve(0.1)
        voice audio.niko_ch10_line27  # transcript: "Fine"
        niko "Fine."
        
        voice audio.niko_ch10_line28  # transcript: "Then may the death god,"
        niko "Then may the Death God, Lord Enoch, greet your sacrifice with open arms and empty hands."
        hide niko with Dissolve(0.1)
        
        "He turned without another word and began walking away."
        "I turned, too and walked forward. I didn't look back."
        "Forgive me, Niko."

    else:

        show dorian normal_alt_tense at left_char with Dissolve(0.2)

        "I kept walking."
        "Each step carried the weight of ghosts I could no longer protect. My fists clenched at my sides. My jaw tightened. My breath came steady, but heavy-measured like the silence between thunder."
        "I had to do this. Alone."

        voice audio.magnus_ch10_line18  # transcript: "Wait, Dorian, wait!"
        magnus "Wait, Dorian! Wait!"

        "I didn't stop."
        show dorian serious at left_char
        show magnus clothed_no_wings at right_char
        with Dissolve(0.2)

        voice audio.magnus_ch10_line19  # transcript: "Heavens, you walk like you're"
        magnus "Heavens, you walk like you're marching into hell-...which, okay, fair, you kind of are, but still."

        "He stepped in front of me, arms stretched out like a wall I didn't ask for."

        voice audio.magnus_ch10_line20  # transcript: "Hey, hey, look at me"
        magnus "Hey. Hey. Look at me for a second, yeah? Just... listen."
        voice audio.magnus_ch10_line21  # transcript: "I... I don't know how"
        magnus "I-uh... I don't know how to do the whole \"pep talk\" thing. So... I'm gonna do the only thing I do know."

        "He cleared his throat dramatically."

        voice audio.magnus_ch10_line22  # transcript: "Don't throw yourself into doom,"
        magnus "Don't throw yourself into doom, my friend, The world still needs your flame to mend..."
        voice audio.magnus_ch10_line23  # transcript: "We've fought, we've cried, we've"
        magnus "We've fought, we've cried, we've bled, we've burned, But some of us still need you returned..."

        "He trailed off. He shrugged sheepishly."

        voice audio.magnus_ch10_line24  # transcript: "Uh... Okay, that was terrible."
        magnus "Okay, that was terrible. I know. But the message is clear, right?"
        voice audio.magnus_ch10_line25  # transcript: "The Yagwai King is powerful,"
        magnus "The Yaoguai King is powerful, Dorian. You know that. You're not stupid. If he wants you to come alone. He wants you to die."
        voice audio.magnus_ch10_line26  # transcript: "Why give him what he"
        magnus "Why give him what he wants? Just... come with us to Tianho. Ignore him. Help save lives there."
        voice audio.dorian_ch10_line47  # transcript: "I have to do this."
        dorian "I have to do this."

        "Magnus flinched."

        voice audio.magnus_ch10_line27  # transcript: "Why? Because of vengeance? Because"
        magnus "Why? Because of vengeance? Because of pride? You think you're doing this for your family-but what about the ones still here?"
        voice audio.magnus_ch10_line28  # transcript: "I'm talking about Elias. You"
        magnus "I'm talking about Elias. You know, the one that dresses up like a girl?"

        "I turned to look at him."
        voice audio.magnus_ch10_line29
        magnus "Yuxuan told me. I didn't know until now that he's your son. He's alive, Dorian. He still needs you."

        "A long silence. I shook my head."
        "Magnus looked at me like I had just slapped him."

        voice audio.magnus_ch10_line30  # transcript: "You're being selfish."
        magnus "You're being selfish."

        "He turned, started to walk away... but then stopped. Glanced back over his shoulder."

        voice audio.magnus_ch10_line31  # transcript: "I remember that my lover"
        magnus "I... I remembered that my lover once said to me."
        voice audio.magnus_ch10_line32  # transcript: "I don't intend on dying."
        magnus "\"I don't intend on dying.\" That was the last thing she ever said. And now that's... one of the only memories I have of her."

        "His voice dropped to a whisper."

        voice audio.magnus_ch10_line33  # transcript: "Please, let me come with"
        magnus "Please... let me come with you."

        "I looked at him. The pain in his eyes. The history in his voice."
        "But I shook my head. The Yaoguai King is after him. I can't risk it."

        "Magnus stepped back. Wounded. Silent."

        voice audio.magnus_ch10_line34  # transcript: "Fine."
        magnus "Fine."

        hide magnus with Dissolve(0.1)
        "And I walked away-toward the dark, toward the fire, toward the one thing that had taken everything from me."
        "Behind me, Magnus didn't follow."
        "I'm sorry, Magnus..."

    jump ch10_sealed_door


# =============================================================================
# SECTION 12: LABEL CH10_SEALED_DOOR — Sealed Door / Yaoguai King
# =============================================================================

label ch10_sealed_door:

    scene underground_magnus with fade

    "After minutes of walking, I reached the place where we had found Magnus."
    "A bottomless chasm wrapped around the edge, and a single narrow bridge stretching towards the center."

    # play music ost_ch10_boss fadein 1.0         # PLACEHOLDER — boss theme

    "Two yaoguai hunched over mangled bodies-unrecognizable, barely even bones now. The sound-"

    play sound audio.sfx_back loop
    "MUNCH. CRUNCH."
    stop sound fadeout 1.0
    "-echoed across the stone. One of them slurped something wet and vile, then burped loudly, its bloated belly sagging against the ground."

    show yaoguai_1 at left_yg_flip with Dissolve(0.2)

    yg "Mmmh... That one tasted like fear. My favorite seasoning."
    show yaoguai at right_yg with Dissolve(0.2)
    yg "You always say that. I think this one tasted like despair. Much richer. Earthier. You wouldn't know taste if it chewed you."
    yg "Bah. Give me fear with a side of broken dreams any day."
    yg "We already ate all of them, Your Majesty. Nothing but bones left!"
    voice audio.yk_ch10_line15  # transcript: "You're spoiling your appetite, boys."
    yk "You're spoiling your appetites, boys. The main course has arrived."

    scene underground_magnus with Dissolve(0.2)

    "At the center stood the Yaoguai King."
    "He was crouched low, fingers trailing along the broken ice where Magnus had once been entombed."
    show yk at right_char 
    show dorian serious at left_char
    with Dissolve(0.2)
    voice audio.yk_ch10_line16  # transcript: "This is where he slept"
    yk "This was where he slept. Four centuries in silence... and still, his presence lingers, dragonkin."
    voice audio.dorian_ch10_line27  # transcript: "I didn't know I was"
    dorian "Hmph. I didn't know I was expected."
    voice audio.yk_ch10_line17  # transcript: "Oh, you were always expected,"
    yk "Oh, you were always expected, dragonkin. Ever since your wife screamed my name with her dying breath."

    "I didn't flinch. Not on the outside."

    show yk at center_char
    show yaoguai at right_yg
    with Dissolve(0.2)

    yg "The dragonkin smells like righteous fury. I love when they're angry. It makes the blood sweeter."
    yg "Do you think we can have a taste before the king breaks him?"
    show dorian normal_alt_annoyed at left_char with Dissolve(0.1)
    voice audio.dorian_ch10_line28  # transcript: "Tell me what happened. And"
    dorian "Tell me what happened. And maybe I'll make this quick."
    show dorian serious at left_char with Dissolve(0.1)
    yg "Ohh, he wants answers now. How precious. Maybe if you ask real nice, we'll write it on your tombstone."
    yg "He's burning up! Let's bite him now! Hot blood's the sweetest!"
    voice audio.yk_ch10_line18  # transcript: "Hush boys, let the dragon"
    yk "Hush, boys... Let the dragonkin grieve with context."
    voice audio.yk_ch10_line19  # transcript: "Very well. This will be"
    yk "Very well. This will be fun. I suppose you've earned a peek behind the curtain. After all, you have played your part well, dragonkin."

    hide yaoguai
    show yk at right_char with Dissolve(0.1)

    "He circled slowly, claws clicking against the cracked ice where Magnus once hung, suspended in frost. His grin widened, revealing fangs too long for his face."

    voice audio.yk_ch10_line20  # transcript: "Magnus is a clone. A"
    yk "Magnus is... a clone. A clone of the death god."

    "My breath caught. My pulse thundered in my ears. A clone?"

    voice audio.yk_ch10_line21
    yk "Yes. A clone. Of the Death God's reincarnation."
    show dorian normal_alt_tense at left_char with Dissolve(0.1)
    "I said nothing. Not from fear-but disbelief. He watched me closely, savoring the silence like wine."
    show dorian angry at left_char with Dissolve(0.1)
    voice audio.yk_ch10_line22  # transcript: "You should have seen your"
    yk "You should've seen your face just now. Delicious..."

    yg "Delicious! Delicious! Good enough to eat!"

    show dorian serious at left_char with Dissolve(0.1)
    "He tapped the icy platform with a clawed foot, sending tiny shards skittering."

    voice audio.yk_ch10_line23  # transcript: "I over heard it all,"
    yk "I overheard it all, you know. A whispered little meeting between King Long Shen of Tianho and King Tatsuya Fujiwara of Hinami."
    voice audio.yk_ch10_line24  # transcript: "Did you know they met"
    yk "Did you know they meet in secret? So many secrets among old men with too much power."

    "He leaned closer, voice dropping to a conspiratorial murmur."

    voice audio.yk_ch10_line25  # transcript: "They spoke of rebirth. Said"
    yk "They spoke of the Rebirth. Said the Death God always reincarnates. Again and again and again. Death, reborn to die once more. Beautiful, isn't it? The god of endings trapped in an eternal loop."
    voice audio.yk_ch10_line26  # transcript: "When Enoch died, a new"
    yk "When Enoch died, a new vessel emerged. But they caught him. Froze him in true ice. Buried him deep beneath Tianho like a shameful relic."

    "My heart pounded. Four centuries. No sign of the Death God. And now I knew why."

    voice audio.yk_ch10_line27  # transcript: "From that vessel they made"
    yk "From that vessel, they made the clone. It took centuries. Science, sorcery, desperation. But they did it."
    voice audio.dorian_ch10_line29  # transcript: "Why? Why make a clone?"
    dorian "Why? Why make a clone?"
    voice audio.yk_ch10_line28  # transcript: "I don't care. Let the"
    yk "I don't care. Let the royals cling to their reasons. All that matters is the truth: the Death God's body still exists. And even without will... it is still a weapon."
    voice audio.yk_ch10_line29  # transcript: "Boom forged in divinity, blood"
    yk "Bone forged in divinity. Blood soaked in finality. Imagine it-an army raised from his marrow. Corpses that do not rot. Channelers who wield death as birthright. The dead, reborn to kill."

    "The Divine Weapon... is Magnus? This can't be..."

    voice audio.yk_ch10_line30  # transcript: "The original body, the one"
    yk "The original body-the one that brought the Tragedy of Tianho-was destroyed. That meddling paladin, Cyrus, actually managed to kill him and destroyed the body."
    voice audio.yk_ch10_line31  # transcript: "But Magnus still intact, still"
    yk "But Magnus? Still intact. Still potent. Was supposed to be mine."
    voice audio.yk_ch10_line32  # transcript: "I had everything. I was"
    yk "I had everything. I was so close. If not for that ridiculous spectacle with the rulers..."

    show dorian angry at left_char with Dissolve(0.1)
    "The Yaoguai King raised his claw. Shadows coiled around my head."
    "And I saw a vision..."

    jump ch10_vision_rulers


# =============================================================================
# SECTION 13: LABEL CH10_VISION_RULERS — Vision: Rulers' Meeting 5 Years Ago
# =============================================================================

label ch10_vision_rulers:

    scene underground_magnus with shock_cut

    "We were in this very hall, though the memory shimmered like heat rising from frost."

    show king_gustav at center_char
    show king_long_shen at left_char
    show olympia at right_char
    with Dissolve(0.2)

    voice audio.gustav_ch10_line1  # transcript: "Unhand me this instant, or"
    king_gustav "UNHAND ME this instant, or I will order every soldier in my empire to raze this palace to ash!"
    voice audio.shen_ch10_line1  # transcript: "You butchered my family, Gustav."
    long_shen   "You butchered my family, Gustav! You sent your aldorith assassins in the dead of night! My wife and my two sons-you knew what you were doing!"
    voice audio.gustav_ch10_line2  # transcript: "Do you have proof, Shen,"
    king_gustav "Pft. Do you have proof? Do you have proof, Shen? Or just grief and wild accusations?"

    "Silence fell. It was thick with outrage."

    voice audio.shen_ch10_line2  # transcript: "Any objections?"
    long_shen         "Any objections?"
    emperor_minjoon   "None. Then let it be known: if this is the way Ena kings govern, Kyeongjang disavows your alliance entirely."
    emperor_minjoon   "I should never have brought my wife here."
    seo_yeon          "You couldn't have known, love. But now we do."
    voice audio.olympia_ch10_line1
    olympia "Min-joon... Seo-yeon, I apologize on behalf of our alliance. Gustav will be punished. I swear it."
    emperor_minjoon   "You brought Jin-haeng back. You brought our son back from the dead... That is the only reason I still stand in this room."
    seo_yeon          "I would have torn apart time itself for that miracle. You gave me back my son... when my own body could not."
    voice audio.olympia_ch10_line2
    olympia "You have my thanks. It is my pleasure to give you your infant son back."
    voice audio.shen_ch10_line3  # transcript: "Death isn't enough for him!"
    long_shen         "DEATH ISN'T ENOUGH FOR HIM!"
    emperor_minjoon   "I cannot imagine your grief, Shen. And I do not intend to stand idle through it. Gustav must be killed."
    voice audio.olympia_ch10_line3
    olympia "We can't. We would risk the project getting known."
    voice audio.olympia_ch10_line4
    olympia "First-we reseal the chamber. That weapon must never be touched again."
    voice audio.olympia_ch10_line5
    olympia "I'll take the Amulet of Frost. I will guard it with my life. And I swear-Gustav will never hold power over the key again."
    voice audio.gustav_ch10_line3  # transcript: "That's mine. I hold the"
    king_gustav       "That's mine! I hold the third key to the door! Not you!"
    emperor_minjoon   "One of the keys is draconic fire, and only Tianho's royal blood can channel it. You knew that. That's why you murdered Long Shen's family-to ensure no one could ever seal the door again."
    voice audio.shen_ch10_line4  # transcript: "You killed my family? Because"
    long_shen         "YOU KILLED MY FAMILY because they could channel draconic fire!"

    voice audio.gustav_ch10_line4
    king_gustav       "GIVE ME THE AMULET OF FROST! YOU ARE VIOLATING THE AGREEMENT!"
    voice audio.olympia_ch10_line6
    olympia "The gall of you to even make demands!!"
    emperor_minjoon   "Your right to that amulet died with Shen's family. You forfeited your claim the moment you became a murderer."
    voice audio.shen_ch10_line5  # transcript: "Then execute his wife too"
    long_shen         "THEN EXECUTE HIS WIFE TOO! STRIKE HER DOWN AND EVEN THE SCORE!"
    voice audio.olympia_ch10_line7
    olympia "Shen. Calm down."
    voice audio.shen_ch10_line6  # transcript: "They were my family, Olympia!"
    long_shen         "THEY WERE MY FAMILY, OLYMPIA! My sons... my wife... They were the last heirs to the Prosperity Dragon's bloodline!"
    voice audio.olympia_ch10_line8
    olympia "I know, Shen... *softly* And I would've died in their place if it meant undoing this. But we have to think clearly now."
    emperor_minjoon   "I will guard the Amulet of Teleportation-the second key. I will make sure that it's safe in Kyeongjang."
    voice audio.shen_ch10_line7  # transcript: "By the prosperity dragon!"
    long_shen         "By the Prosperity Dragon-"
    voice audio.gustav_ch10_line5  # transcript: "Thank you long enough."
    king_gustav       "TOOK YOU LONG ENOUGH!"

    hide olympia 
    hide king_long_shen
    show boy_ald_normal at left_char
    show girl_ald_normal at right_char 
    with Dissolve(0.2)

    boy_ald   "They have Father! Destroy them!"
    voice audio.girl_ald_ch10_line1
    girl_ald  "YAHHHH!!"

    scene underground_magnus with Dissolve(0.2)
    "The doors exploded inward as Gustav's hidden soldiers stormed in, blades drawn and channeling elements." with hpunch

    emperor_minjoon "Gustav, you dare wage war in the heart of peace?"
    voice audio.shen_ch10_line8  # transcript: "You'll burn for this."
    long_shen       "You'll burn for this!"

    play sound audio.sfx_stone_break
    "A spire of earth struck Empress Olympia across the side, sending her tumbling. But even as blood trickled down her brow, she rose." with hpunch
    stop sound fadeout 1.0
    voice audio.shen_ch10_line9  # transcript: "Olympia! Are you alright?"
    long_shen       "OLYMPIA! ARE YOU ALRIGHT?"

    voice audio.olympia_ch10_line9 
    olympia "I'm fine, Shen."
    voice audio.gustav_ch10_line6  # transcript: "You will give me the"
    king_gustav     "Heh. You will give me the amulet of frost, skank!"
    voice audio.olympia_ch10_line10
    olympia "You want the weapon, Gustav? Then come and take it!"

    scene underground_door with dissolve

    "The vision shifted-like flame caught in a gust."
    "Screams. Roars. Metal clashing. The ground trembled beneath the weight of monsters unleashed."
    "And I stood before them. King Gustav lay broken on the blood-soaked ground, battered and heaving, his armor cracked, his face streaked with ash and blood."
    "Standing over him was King Long Shen, surrounded by scorched earth and a seething aura of draconic power."

    show king_gustav at right_char
    show king_long_shen at left_char
    with Dissolve(0.2)
    voice audio.gustav_ch10_line7
    king_gustav "Do it... Kill me..."

    "King Long Shen's voice thundered."

    voice audio.shen_ch10_line10  # transcript: "You release the death god"
    long_shen   "You released the Death God onto Tianho! What madness took root in your soul, Gustav?!"
    voice audio.gustav_ch10_line8  # transcript: "I have everything under control."
    king_gustav "I... I had everything under control. It was an accident!"
    voice audio.gustav_ch10_line9  # transcript: "If you and me other"
    king_gustav "If you and the other rulers hadn't fought me-none of this would've happened! If you would have just given me the divine weapon like I asked-"

    "I felt the ground shaking harder. A beast screamed in the distance." with hpunch
    show screen draconic_rage_shen
    "King Long Shen's eyes blazed gold-his veins glowing faintly with draconic fire."

    voice audio.shen_ch10_line11  # transcript: "You insufferable wretch! Your ambition"
    long_shen "You insufferable wretch. Your ambition knows no end!"

    "He stepped forward and thrust his palm toward the door."

    voice audio.shen_ch10_line12  # transcript: "By frost and flame. By"
    long_shen "By frost and flame, by blood made pure, the weapon be sealed behind this door. Three keys shall break what now I bind-Frost and flight, and fire combined."

    "A burst of pure fire channeled from his chest to the seal. The door screeched shut, etchings flaring with molten gold as the door locked."

    voice audio.gustav_ch10_line10  # transcript: "No! NOOOOO!"
    king_gustav "NO!! NOOOOO!!"
    voice audio.shen_ch10_line13  # transcript: "You will never open it"
    long_shen   "You will never open it again. Ena will be safer without you. The Amulet of Teleportation-Min-joon already sent it to Kyeongjang."
    voice audio.shen_ch10_line14  # transcript: "You'll never see it again."
    long_shen   "You'll never see it again."

    "He held up the second amulet-the Amulet of Frost, gleaming with icy light."

    voice audio.shen_ch10_line15  # transcript: "As for this, it stays"
    long_shen   "As for this? It stays with me."

    "King Gustav snarled."

    voice audio.gustav_ch10_line11  # transcript: "I swear as long as"
    king_gustav "I swear, as long as I draw breath, I will-"

    # TODO: searing audio
    "A scream tore from his throat as Long Shen slammed a flaming fist into his ribs, the heat searing armor and flesh. Gustav collapsed, choking on pain."
    voice audio.gustav_ch10_line12
    king_gustav "AAHHHHH!!!!"

    "King Long Shen took a knife from his pouch."

    voice audio.shen_ch10_line16  # transcript: "This is for my sons,"
    long_shen "This is for my sons. For my wife. For every soul you damned."

    "But then-"
    hide screen draconic_rage_shen
    scene vasily_attack with flash
    voice audio.vasily_ch10_line1  # transcript: "Your Majesty!"
    vasily "YOUR MAJESTY!!"


    "A beam of divine light tore through the haze. Count Vasily, brilliant and fast as lightning, surged in. In one blinding motion, he drove a knife through Long Shen's back."
    scene bg_tianho_underground_2 with fade

    show king_gustav at right_char
    show king_long_shen at left_char
    show vasily neutral at center_char
    with Dissolve(0.2)
    voice audio.shen_ch10_line17
    long_shen   "N.... No..."

    "The fire in his eyes flickered out. He crumpled, lifeless."
    voice audio.gustav_ch10_line13
    king_gustav "Vasily... what have you done? We needed him alive! We needed that seal!"

    "Count Vasily's eyes were hard."
    show vasily alt_savage at center_char with Dissolve(0.1)
    voice audio.vasily_ch10_line2  # transcript: "It would have killed you,"
    vasily "He would've killed you, Your Majesty."
    voice audio.vasily_ch10_line3  # transcript: "The all-quire are overrunning the"
    vasily "The yaoguai are overrunning the palace. Tianho is a ruin. We have to move-now."
    voice audio.vasily_ch10_line4  # transcript: "Are you listening to me"
    vasily "Are you listening to me, Your Majesty? Your Majesty!"

    "King Gustav roared."

    voice audio.gustav_ch10_line14  # transcript: "We'll never access the Divine"
    king_gustav "We'll never access the Divine Weapon now! You FOOL! You-BELLIGERENT, SANCTIMONIOUS-"

    "Count Vasily slapped him."

    show vasily alt_normal at center_char with Dissolve(0.1)
    voice audio.gustav_ch10_line15
    king_gustav "?!"
    voice audio.vasily_ch10_line5  # transcript: "Forgive me your majesty, but"
    vasily "Forgive me, Your Majesty. But Mjoll needs you alive. The death god is laying waste to everything."

    "He reached down, gripping Gustav's arm and hoisting him up with surprising gentleness."

    voice audio.vasily_ch10_line6  # transcript: "We have a carriage waiting."
    vasily "We have a carriage waiting. We're evacuating through the hidden passage beneath the north wing. Can you walk?"
    voice audio.gustav_ch10_line16  # transcript: "Of course."
    king_gustav "O... Of course."
    voice audio.vasily_ch10_line7  # transcript: "Then let me help you."
    vasily "Then let me help you. We must hurry."

    scene underground_magnus with fade

    "The vision ended yet I stood frozen. The echo of the vision still burned in my mind-the roar of fire, the flash of betrayal, the final breath of a king."
    "Count Vasily was the one who saved Gustav. That loyal dog."
    "King Gustav was the reason for the death god's release in his ice prison."
    "And in that chaos... King Long Shen-the last known wielder of draconic fire-was killed."

    show yk at right_char 
    show dorian angry at left_char
    with Dissolve(0.2)

    "The Yaoguai King let out a low, satisfied hum behind me, as if relishing my silence."

    voice audio.yk_ch10_line33  # transcript: "Now you understand, the Divine"
    yk "Now you understand... The divine seal needs something more than brute strength or blood. It needs fire. Not the mortal kind. Draconic fire."

    "I turned toward him, my fists clenched."

    voice audio.dorian_ch10_line30  # transcript: "You need it someone of"
    dorian "You needed someone of Tianho royal blood."

    "The King's smile split wider, showing rows of jagged, gleaming teeth."

    voice audio.yk_ch10_line34  # transcript: "Precisely. I could scour the"
    yk "Precisely. I could scour the continents for the two amulets. But it would be meaningless without a soul the seal would answer to. And then I saw you."
    voice audio.yk_ch10_line35  # transcript: "You, Dragonkin, speaking to the"
    yk "You, dragonkin... Speaking to the Prosperity Dragon as if it were an old friend. Whispering. Smiling. Laughing. Like it was nothing."

    "His voice grew quieter, darker-deadly."

    voice audio.yk_ch10_line36  # transcript: "Even kings and queens of"
    yk "Even kings and queens of Tianho have waited lifetimes to hear a whisper from that spirit. Some died without ever glimpsing it. The Prosperity Dragon has remained silent for generations..."
    voice audio.yk_ch10_line37  # transcript: "Yet it spoke to you"
    yk "Yet it spoke to you for some reason. Very casually."

    "My heart pounded."

    voice audio.yk_ch10_line38  # transcript: "That's when I knew. You"
    yk "That's when I knew. You are not just a warrior. You are the key. A flame born to break open what Long Shen sealed."
    voice audio.yk_ch10_line39  # transcript: "And I was right."
    yk "And I was right..."

    "He tilted his head, his tone mocking."

    voice audio.yk_ch10_line40  # transcript: "and whether you want to"
    yk "And whether you want to or not... I will have your flames."
    voice audio.dorian_ch10_line31  # transcript: "Then why kill Alora and"
    dorian "THEN WHY KILL ELARA AND MY CHILDREN?! THEY DIDN'T HAVE TO DIE FOR THIS!"

    "The words ripped from my chest-raw and seething."
    "It all came running back to me. How he disrespected Elara, the kids."

    voice audio.yk_ch10_line41  # transcript: "Because I needed you broken."
    yk "Because I needed you broken. The legends say draconic fire awakens only through sheer desperation. When your heart is torn apart and all that remains... is rage."

    "Then came the voices-those cursed, laughing mouths beside him."

    yg "And they were yummy! Yummy delicious!"
    yg "That woman- what a skank! Hahaha! And the little ones-"

    show dorian dragon_eyes at left_char with Dissolve(0.1)
    "They didn't finish. I didn't let them."
    scene cg_taotie_fight with shock_cut
    "My rage ignited. Draconic fire erupted around me like a storm-blazing gold and crimson, heat warping the air in violent waves."
    "I thrust both hands forward and unleashed a roaring inferno across the platform."
    play sound sfx_fire_explosion                # PLACEHOLDER — draconic fire SFX
    "The flames consumed the two yaoguai instantly, their screams shrill and choking as fire melted flesh from bone and turned the stone beneath them black."
    
    # voice audio.yg_scream
    yg "AAAAAGHHH-!!"
    yg "NO! STOP-GRRAHHHH!!"

    "Ash and smoke whirled in the air."
    "The Yaoguai King didn't move as the flames engulfed him-but his grin was gone."

    scene underground_magnus with shock_cut
    show yk at right_char
    show dorian dragon_eyes at left_char
    with Dissolve(0.2)

    voice audio.yk_ch10_line42  # transcript: "How dare you! After I"
    yk "HOW DARE YOU! AFTER I JUST TOLD YOU EVERYTHING! I could have given you power. Dominion. Revenge. I was going to make you a god, Dragonkin!"

    "My flames blazed brighter, the fire pulsing from my chest like a heartbeat."
    show screen draconic_rage
    voice audio.dorian_ch10_line32  # transcript: "This is for a Laura."
    dorian "This is for Elara. This is for my children. Daniel. Emily. Sarah. Lucas."

    "The King bared his jagged teeth."

    voice audio.yk_ch10_line43  # transcript: "Such power, such glorious fire,"
    yk "SUCH POWER! SUCH GLORIOUS FIRE! But how foolish! YOU WILL RUE THE DAY YOU FACE ME!"

    "He raised his claws, darkness gathering behind him in a wave of corrupted energy."

    voice audio.yk_ch10_line44  # transcript: "Come, Dragonkin, I burn you"
    yk "Come, dragonkin... I'LL BURN YOU TO ASHES!"

    "The Yaoguai King roared-a sound that cracked stone and shook the platform beneath our feet. Shadows curled around him like tendrils, twisting into monstrous limbs. His claws-longer than swords-gleamed."

    voice audio.yk_ch10_line45  # transcript: "Let's see if the trachonic"
    yk "Let's see if that draconic fire still burns as bright... when you're bleeding."

    "Then... a voice called out to me. It called out to me again."

    prosperity_dragon "Child..."

    "The world slowed."
    $ renpy.save("quick-1")
    prosperity_dragon "He is old. Two centuries of strength. Unmatched. Unrelenting."
    prosperity_dragon "You are new. You are fast. Heed my advice. Don't meet force with force."
    prosperity_dragon "Wait and slip past the storm. I trust you, child. Do not let this monstrosity get the better of you."

    "The world resumed its pace. The king lunged. Fast. Too fast. His claw came down like a guillotine, aiming to cleave me in half."
    play music audio.ost_battle volume 0.8 loop
    jump ch10_boss_fight_1


# =============================================================================
# SECTION 14: LABEL CH10_BOSS_FIGHT_1 — Boss Fight Round 1
# =============================================================================
label ch10_boss_fight_1:
    $ _choice_timeout = 5.0
    menu:

        "Dodge to the side and counter with a burst of flame.":
            $ yking_score += 1                  # +1 YKing score
            $ _choice_timeout = 0

            "I ducked low and rolled to the left."
            play sound audio.sfx_claw 
            play sound audio.sfx_yaoguai_burst
            "His claw slammed into the ground where I'd been standing, splintering the stone with a deafening crack."
            stop sound fadeout 1.0
            play sound sfx_fire_explosion
            "Mid-roll, I threw my hand forward and unleashed a torrent of fire straight at his side."
            "The flames roared against his ribs, and I caught the scent of scorched rot as bits of his corrupted armor blackened and burned."

            voice audio.yk_ch10_line46  # transcript: "Not bad. But not enough."
            yk "Not bad... but not enough."

        "Block the strike with a crossed-arm guard reinforced with draconic fire.":
            $ _choice_timeout = 0

            "I braced my arms in front of me, channeling draconic fire as a shield."
            play sound audio.sfx_claw 
            "His claw tore through it like paper. Pain exploded through my shoulder as his strike connected, slashing flesh and armor alike."

            voice audio.yk_ch10_line47
            yk "WATCH HOW MY CLAWS TEAR YOUR FLESH LIKE PAPER!"

            "I choked out, staggering back as blood streamed down my arm. But I stayed standing. I had to."

    "The Yaoguai King stepped back, dark eyes gleaming with menace."

    voice audio.yk_ch10_line48  # transcript: "You'll be joining your family"
    yk "You'll be joining your family soon..."

    "He spread his arms. The air warped and twisted. A cyclone of corrupted wind and shadow coiled above us, rising higher and higher into the sky like a black storm."

    jump ch10_boss_fight_2


# =============================================================================
# SECTION 15: LABEL CH10_BOSS_FIGHT_2 — Boss Fight Round 2: Spirits Wave
# =============================================================================

label ch10_boss_fight_2:
    $ _choice_timeout = 4.0
    menu:

        "Stay grounded and summon a shield of fire around you to brace for impact.":
            $ _choice_timeout = 0

            "I stood my ground and summoned a dome of fire around me."
            play sound audio.sfx_claw 
            "The cyclone hit with the force of a hurricane, blades of shadow slicing through the flames. The shield held-then shattered."
            "The impact hurled me across the arena."
            
            "I crashed hard, pain tearing through my side."

            voice audio.yk_ch10_line49  # transcript: "What's wrong, Dragonkin? Had enough?"
            yk "What's wrong, dragonkin? Had enough?"

            "I groaned, coughing up blood, but pushed myself to my knees. I wasn't done yet."

        "Leap into the air, aiming to slam down with a draconic flame punch.":
            $ yking_score += 1                  # +1 YKing score
            $ _choice_timeout = 0
            play sound sfx_fire_explosion
            "I clenched my fists and launched into the air, draconic fire roaring beneath my feet."
            play sound audio.sfx_eruption 
            "I plummeted from above, fist wreathed in flame, and slammed it into his chest like a meteor."
            stop sound fadeout 1.5
            "The impact cracked the ground and sent him skidding back, trails of fire left in my wake." with hpunch

            voice audio.yk_ch10_line50  # transcript: "Gah, screw you, dragonkin!"
            yk "Ghhh-! Screw you dragonkin!"

    "The arena smoldered. The ground cracked beneath us. My shoulder ached, my ribs screamed, but the fire in my heart wouldn't die." with hpunch
    "The Yaoguai King stood tall, smoke rising off his hide. His smile widened."

    voice audio.yk_ch10_line51  # transcript: "You're still alive. Good. That"
    yk "You're still alive? Good. That means I can keep breaking you-piece by piece."

    "My draconic fire flickered across the cracked stone, and I could feel the pulse of the Prosperity Dragon burning in my veins."
    "But the Yaoguai King was far from done."
    "With a snarl, he spread his arms wide. Black mist gushed from his body, and behind him rose the silhouettes of twisted spirits-dead yaoguai, their wailing souls clawing for release."

    voice audio.dorian_ch10_line33  # transcript: "Impossible! The Spirits!"
    dorian "Impossible... The spirits?"
    hide yk
    show yaoguai at right_yg with Dissolve(0.2)
    voice audio.yg_scream
    yg "Raaaaaaawwrrr!!! Grrraaawwwrrr!! Rawwwrrr!!"
    voice audio.yk_ch10_line52  # transcript: "The hatred will be my"
    yk "Their hatred will be my shield. Their screams, my chorus."

    "He hurled them toward me in a wave of screaming shadow."

    jump ch10_boss_fight_3


# =============================================================================
# SECTION 16: LABEL CH10_BOSS_FIGHT_3 — Boss Fight Round 3: Cyclone
# =============================================================================

label ch10_boss_fight_3:
    $ _choice_timeout = 3.0
    menu:

        "Channel wind to slice through the spirits before they could touch you.":
            $ yking_score += 1                  # +1 YKing score
            $ _choice_timeout = 0

            play sound audio.sfx_wind
            "I need to slice through them before they could touch me. I closed my eyes and inhaled-then roared."
            "A surge of wind erupted from my core, sharp as blades and fast as thunder. The spirits shrieked as the gust shredded through them, dissipating their forms into wailing mist."

            voice audio.yg_scream         # PLACEHOLDER — yaoguai roar
            yg "Raaaaaaawwrrr!!! AAHHHH!!"

        "Cover yourself in fire and charge through.":
            $ _choice_timeout = 0

            "I cloaked myself in fire and tried to power through."
            "The spirits screamed louder as they tore at my flame, phasing into me like knives. Cold dread flooded my mind as ghostly claws scraped at my soul."

            voice audio.yg_scream         # PLACEHOLDER — yaoguai roar

            yg "Gwaaaaarrrrr!!"

            "I stumbled, gasping."
            "They faded-but not before leaving my skin ice-cold and raw."

            voice audio.yk_ch10_line53  # transcript: "That's Stingdreggankin. Ha ha ha"
            yk "That sting, Dragonkin? Hahaha!"

    jump ch10_boss_outcome


# =============================================================================
# SECTION 17: LABEL CH10_BOSS_OUTCOME — Good or Bad Ending Gate
# =============================================================================

label ch10_boss_outcome:
    hide yaoguai
    show yk at right_char with Dissolve(0.2)

    voice audio.yk_ch10_line54  # transcript: "The halls of Shen Lunowate"
    yk "The halls of Xianlun await you... you'll see your kin again... Aren't you excited?"

    "He sneered."

    voice audio.yk_ch10_line55  # transcript: "Foolish boy. This ends now."
    yk "Foolish boy. This ends now."

    "And then he moved."
    "Faster than before. A blur of darkness and bone."
    "One claw arced high, slicing down like a falling guillotine. The other swept low, fast and vicious."

    $ _choice_timeout = 3.0
    menu:

        "Stand your ground and counter.":
            $ _choice_timeout = 0
            play sound sfx_claw
            "His lower claw slammed into me mid-motion, slicing across my hip."
            play sound audio.sfx_body_thud 
            "I howled and hit the ground hard, blood soaking into the dirt."
            "Still, I forced myself to rise."

            voice audio.yk_ch10_line56  # transcript: "This is what you get"
            yk "Futile, dragonkin. This is what you get for challenging me."

            "I was running out of time."

        "Duck between the claws and twist behind him.":
            $ yking_score += 1                  # +1 YKing score
            $ _choice_timeout = 0
            "I took one sharp breath and dove between his incoming arms. The wind of his swipe grazed my skin, but I twisted my torso mid-dodge and rolled behind him in one smooth motion."
            "The King spun, eyes wild. Too late."
            "I had flames blazing in both fists. I brought them down on his back."
            play sound audio.sfx_fire_explosion
            yk "GGGRRAAAAAAAAAGHHH!!!"

            "His howl tore the room. Fire scorched his corrupted back, searing deep. Smoke rose from his shoulders as he stumbled forward."

    if yking_score < 3:
        jump ch10_bad_end_fight
    else:
        jump ch10_boss_good
    # jump ch10_bad_end_fight


# =============================================================================
# SECTION 18: LABEL CH10_BAD_END_FIGHT — BAD END: YKing < 3
# =============================================================================

label ch10_bad_end_fight:
    stop music fadeout 1.5
    hide screen draconic_rage
    show dorian normal_alt_tense at left_char with Dissolve(0.1)
    "The Yaoguai King snarled-scorched, bleeding, but very much alive."
    "His charred skin peeled at the edges, smoke curling from every wound... and still, he laughed."

    play music audio.ost_tragedy fadein 1.5
    voice audio.yk_ch10_line58  # transcript: "Pathetic. I expected more from"
    yk "Pathetic. I expected more from the Dragon of Gale."

    "I could barely move. My limbs were trembling, my vision was swimming."
    "The King straightened, his body still crackling from the flames I had left on him."

    voice audio.yk_ch10_line59  # transcript: "You're wasting my time."
    yk "You're wasting my time."

    "In the space between heartbeats, he vanished."
    "A blinding pain tore across my chest. Cold flooded my lungs. I fell to my knees as warmth spilled from the open wound. My blood."

    voice audio.dorian_ch10_line34  # transcript: "GAAAHHHHH!"
    dorian "GAHHH!!"

    "The world began to tilt."
    "He stepped before me-towering, monstrous, victorious."

    voice audio.yk_ch10_line60  # transcript: "You tried little dragonkin, you"
    yk "You tried, little dragonkin. You really did."
    voice audio.yk_ch10_line61  # transcript: "Look on the bright side."
    yk "Look on the bright side. At least you'll get to be with your family now. Elani or whats-her-name... those tasty children of yours... I'm sure they've been waiting."

    play sound audio.sfx_body_thud   
    "I fell forward. My face hit the cold stone. My fingers twitched, reaching for fire that would never come."
    
    "Behind me, I heard the jeering laughter of his minions. The Yaoguai. Loud. Cruel. Victorious."
    "Darkness crept in-but before I faded completely, I heard the King speak again."
    "A promise."
    "A curse."

    voice audio.yk_ch10_line62  # transcript: "Ena will fall. Just as"
    yk "Ena will fall. Just as Tianho will. I will raze it to the roots. Their temples, their thrones... Once the Divine Weapon is mine..."
    scene black with dissolve
    "And then.. Darkness."

    jump ch10_bad_end_credits


# =============================================================================
# SECTION 19: LABEL CH10_BOSS_GOOD — YKing >= 3: Illusion of Elara / Rescue
# =============================================================================

label ch10_boss_good:
    stop music fadeout 2.0
    hide screen draconic_rage
    show dorian angry at left_char with Dissolve(0.1)
    "I dropped low and slammed my hand into the ground."
    play sound audio.sfx_earth 
    "A jagged spike of stone shot up and slammed into his jaw."
    play sound audio.sfx_back
    "It snapped his head back in a brutal crunch."
    # TODO: add searing sfx
    "Smoke curled from his wounds. His charred, half-melted body hissed and crackled like dying coals. But he didn't fall. Not yet."

    show yk at right_char with Dissolve(0.2)

    voice audio.yk_ch10_line63  # transcript: "You... You've gotten strong. Too"
    yk "You... You've gotten strong. Too strong."

    "His voice was trembling-not from fear, but fury. There was rage in his eyes now. Genuine. Feral. I had wounded his pride."
    "I stood tall, even as my body ached to collapse. Flames continued to swirl around me. The shadows behind him rippled."
    "And from them... she stepped forward."

    scene cg_elara_children_death with shock_cut

    voice audio.elara_ch10_line1  # transcript: "Torian, you did it. You're"
    elara "Dorian... you did it. You're safe now. Come home."

    "My knees nearly buckled. Her eyes. Her smile. Her soft, glowing skin. She reached toward me with trembling fingers."
    "But then I saw it. Just a flicker. The smirk behind the eyes. The hunger behind the tears. The way her shadow curved wrong against the floor."
    "Too late."

    scene underground_magnus with flash

    "Something sharp, searing, punched through my gut. My hands trembled."
    "The illusion melted away. Elara vanished like mist in the sun. And standing there, face twisted in delight, was the Yaoguai King."

    show yk at center_char with Dissolve(0.2)

    voice audio.yk_ch10_line64  # transcript: "Still so gullible. That's what"
    yk "Still so gullible. That's what makes you fun."

    "He lifted me by the throat. My legs kicked uselessly beneath me, blood dripping down his arm. The fire around me sputtered-waning."
    "He pulled me close, face inches from mine. I could smell the rot of his breath."

    yk "Watching you break, watching you cling to the fantasy that you could win? That's ART."

    "The Yaoguai King leaned in, claws poised to rip the last of my life away."

    voice audio.yk_ch10_line65  # transcript: "I was supposed to give"
    yk "I was supposed to give you power once I get my hands on that Magnus and take his power."
    voice audio.yk_ch10_line66  # transcript: "Hashim, but at least you"
    yk "A shame. But at least you'll join your wife. Your little ones. Perhaps they'll still recognize what's left of you."

    voice audio.dorian_ch10_line35
    dorian "D... Do it..."

    scene black with dissolve
    "I closed my eyes, accepting my fate."

    voice audio.yk_ch10_line67
    yk "This is farewell, dragonkin. DIE-"

    # jump ch10_rescue_magnus
    # # Branch on love route for rescue
    if highest_character == "yuxuan":
        jump ch10_rescue_yuxuan
    elif highest_character == "chunghee":
        jump ch10_rescue_chunghee
    elif highest_character == "svante":
        jump ch10_rescue_svante
    elif highest_character == "niko":
        jump ch10_rescue_niko
    else:
        jump ch10_rescue_magnus


# =============================================================================
# SECTION 20: LABEL CH10_RESCUE_YUXUAN — Yuxuan Rescues Dorian
# =============================================================================

label ch10_rescue_yuxuan:

    # play sound sfx_cheng_jingle                 # PLACEHOLDER — Cheng jingle SFX

    "\"HERE AT CHENG'S, WE BRING CHANGE!\""

    "The jingle blared through the chamber-loud, off-key, and utterly ridiculous. It echoed off the walls like a commercial from a forgotten dream."
    "The Yaoguai King froze mid-strike, his claws still around my neck."

    yk "Hmm?"

    "FWOMP!"

    play sound sfx_electric_net                 # PLACEHOLDER — electric net SFX

    "A massive net dropped from the ceiling-crackling with electricity. It slammed down on him like a divine trap, snapping around his limbs and torso with violent force."

    voice audio.yk_ch10_line95  # transcript: "What is this?"
    yk "WHAT IS THIS?!"

    "He thrashed, roaring in disbelief as sparks shot through his body. The net pulsed again, chaining him down like a wild beast caught in a god's snare."
    voice audio.supplybot_ch10_line1
    supply_robot "Electric net protocol engaged."

    "I looked up-barely conscious, my body trembling."
    voice audio.dorian_ch10_line53
    dorian "Y-Yuxuan?"
    play music audio.yuxuan_theme fadein 2.0
    scene cg_yuxuan_saves_dorian with shock_cut

    "Smoke billowed from the shattered archway above, and through it walked a figure wielding an absolutely massive cannon strapped to a rig of copper coils and glowing tubes."
    "It was Yuxuan. A supply bot rolled behind him, wheels screeching slightly as it dragged what looked like an absurdly overloaded battery."

    voice audio.yuxuan_ch10_line34  # transcript: "Presenting Chang Industries New Prototype"
    yuxuan "PRESENTING CHENG INDUSTRIES' NEW PROTOTYPE WEAPON! You like this, beastie?"
    voice audio.yk_ch10_line96  # transcript: "Who? Who does?"
    yk "WHO?! WHO DARES-"

    "A voice rang out-calm, powerful, ancient."

    prosperity_dragon "The renowned inventor, Cheng Yuxuan. CEO of Cheng Industries. A beacon of ingenuity... and a symbol of hope for all of Tianho."

    voice audio.yk_ch10_line71  # transcript: "The... The Prosperity Dragon?"
    yk "The... the Prosperity Dragon...?!"

    "The net pulsed again, blindingly bright."

    voice audio.yuxuan_ch10_line35  # transcript: "Oh, you're really screwed now."
    yuxuan "Oh, you're really screwed now. These tunnels? These are my turf, freak."

    play sound audio.sfx_beam_charge 
    "He flicked a switch. The cannon began to hum, and the coils down its barrel lit up like lightning in a bottle."

    voice audio.yuxuan_ch10_line36  # transcript: "Voltisch check."
    yuxuan "Voltage check?"
    voice audio.supplybot_ch10_line2
    supply_robot "CALIBRATION COMPLETE. VOLTAGE: 100,000%%. MEGABOOM PROTOCOL READY."

    "The air vibrated. The cannon whined, glowing dangerously." with hpunch

    voice audio.yk_ch10_line98  # transcript: "You insinant insignificant."
    yk "You insolent, insignificant-!"
    voice audio.yuxuan_ch10_line37  # transcript: "I'm not insignificant. I'm an"
    yuxuan "I'm not insignificant. I'm an icon."
    voice audio.yuxuan_ch10_line25  # transcript: "Dorian!"
    yuxuan "DORIAN, MOVE!"

    "He slammed his palm down on a button. With the last ounce of strength I had, I rolled out of the way."
    voice audio.supplybot_ch10_line3
    supply_robot "ENGAGING MEGABOOM. GOODBYE, YAOGUAI KING. COURTESY OF CHENG INDUSTRIES."
    voice audio.yuxuan_ch10_line39  # transcript: "This is Forty-Anneho, you overgrown"
    yuxuan "THIS IS FOR TIANHO, YOU OVERGROWN MONSTROSITY!!"
    play sound sfx_megaboom                     # PLACEHOLDER — megaboom SFX
    "BOOOOOOM."

    "The chamber erupted in light."
    play sound sfx_electric_net                 # PLACEHOLDER — electric net SFX
    "The beam of pure energy tore through the air like divine judgment-slamming into the Yaoguai King with the wrath of thunder, fire, and raw voltage."
    "His body convulsed, twisted, and screamed."
    "Shadows shattered like glass around him. His form burned-scales cracking, bones breaking, magic unraveling."

    voice audio.yk_ch10_line99
    yk "AAAAAGHHHHH-!! NO!!! NOO!!!"

    "Then silence."
    "Smoke curled from the ruin where he stood."
    scene underground_magnus with fade
    stop music fadeout 3.0
    "I collapsed to my knees, gasping. My vision blurred, but I was alive-scorched, bleeding, trembling... but alive."
    "Yuxuan was already sprinting toward me, cannon clattering to the ground."

    show yuxuan normal_sad at right_char 
    show dorian neutral at left_char
    with Dissolve(0.2)

    voice audio.yuxuan_ch10_line40  # transcript: "Torian! No, no! You okay?"
    yuxuan "DORIAN! NO!! NO!! Are you okay?! Say something!"

    "I looked up at him weakly."

    voice audio.dorian_ch10_line54
    dorian "Yu, y-you... saved me..."

    "He dropped beside me, grabbing my shoulders gently. The supply bot whirred to my side, scanning my injuries."
    voice audio.supplybot_ch10_line4
    supply_robot "Emergency assistance activated. Checking for serious injuries."
    voice audio.supplybot_ch10_line5
    supply_robot "CRITICAL DAMAGE DETECTED. WRAPPING BANDAGES. ADMINISTERING SALINE. HOLD STILL, MASTER DORIAN."

    "It clumsily began wrapping my arm in gauze."

    voice audio.yuxuan_ch10_line41  # transcript: "Don't worry, I've got you."
    yuxuan "Don't worry. I've got you. You're okay. You're okay now..."

    "I tried to speak. To thank him again. But the world spun."
    scene black with Dissolve(0.5)
    "And then... the world faded to black..."

    jump ch10_tianho_battle


# =============================================================================
# SECTION 21: LABEL CH10_RESCUE_CHUNGHEE — Chung-hee Rescues Dorian
# =============================================================================

label ch10_rescue_chunghee:

    play music audio.chunghee_theme fadein 2.0
    "A voice boomed through the area-not from lips, but from deep within our minds, rattling the very bones beneath our skin."

    voice audio.chung_ch10_line27  # transcript: "Unhand him."
    chung_hee "UNHAND HIM."
    play sound audio.chain_cast
    "The Yaoguai King froze."
    play sound audio.sfx_psychic_chains 
    "His claws still gripped my throat. Blood still dripped from my wound. But something changed in the air."
    "The pressure shifted. The shadows that danced eagerly behind the Yaoguai King suddenly recoiled, like frightened beasts sensing something far worse."

    "I gasped, barely clinging to consciousness."
    voice audio.dorian_ch10_line24
    dorian "C...Chung?"


    "My vision was fading, but I saw the flicker of his silhouette-elegant cape whipping in the wind. A flicker of white and silver."
    "Chung-hee."
    "And though his lips didn't move, his voice cracked like thunder in my mind again."

    voice audio.chung_ch10_line28  # transcript: "You will not lay another"
    chung_hee "You will not lay another finger on him."

    "The Yaoguai King snarled, baring his jagged teeth."

    voice audio.yk_ch10_line68  # transcript: "Another past... You... Dare... Threaten..."
    yk "Another pest? You dare threaten-"
    
    scene cg_chung_saves_dorian with shock_cut

    "Before he could finish, Chung-hee raised both hands, and the air around him rippled. With a sudden, sharp crack, ethereal chains-woven from pure mind energy-snapped into existence and lashed out."
    "They coiled around the Yaoguai King like living serpents, binding his arms, his legs, his neck. He thrashed, howled, clawed at them-but the psychic chains only tightened."

    voice audio.yk_ch10_line69  # transcript: "What? What the-"
    yk "W-What?! WHAT THE?!"

    "The chains tightened."

    voice audio.yk_ch10_line70
    yk "Nnnghh-What are you?!"

    "A voice rang out-calm, powerful, ancient."

    prosperity_dragon "The Kyeongjang Emperor, Hyon Chung-hee... The eldest son of Hyon Min-joon. The strongest mind channeler to ever walk the lands of Kyeongjang."
    voice audio.yk_ch10_line80  # transcript: "The... The Prosperity Dragon?"
    yk "The... the Prosperity Dragon...?!"

    "The Yaoguai King's pupils dilated."

    voice audio.yk_ch10_line72  # transcript: "No, no, no, no."
    yk "No... no, no-"

    "But Chung-hee stepped forward, eyes narrowing. And then-his mind reached out."
    "From the shadows beyond, the Yaoguai spirits-twisted remnants once bound to the King-hesitated, confused by the power now overwhelming their master."
    "He... He's... controlling them telepathically."

    voice audio.chung_ch10_line29  # transcript: "I'm casting off his control."
    chung_hee "I'm casting off his control. Obey your true nature."
    voice audio.chung_ch10_line30  # transcript: "The Yalguai King is Dorian."
    chung_hee "The Yaoguai King is Dorian. Feed to your hearts content."
    voice audio.yk_ch10_line73  # transcript: "What? No! I am your"
    yk "WHAT? NO! I AM YOUR MASTER! YOU-"
    yg "Yummy... Must feed!"

    "And they obeyed."
    "One by one, the once-writhing yaoguai spirits turned on their former master."
    voice audio.yg_scream 
    play sound audio.yg_screech 
    "They surged toward him, screeching, weeping, screaming like ghosts freed from torment-and they devoured him."

    voice audio.yk_ch10_line74  # transcript: "Huh, no, not like this."
    yk "AHHH!!! NOOOO!!! NOT LIKE THIS!!!"

    "The psychic chains constricted one final time-a brilliant flash of silver and white light-and then, with an agonizing shriek, the Yaoguai King erupted into dust."
    "Silence fell."
    "Warm hands caught me before I hit the ground. I collapsed against him, gasping for air. My chest ached, my vision flickered. But I felt his arms around me-strong, trembling just slightly."
    scene underground_magnus with fade
    stop music fadeout 3.0
    show chunghee normal_neutral at right_char
    show dorian neutral at left_char
    with Dissolve(0.2)

    voice audio.chung_ch10_line31  # transcript: "Dorian, are you alright?"
    chung_hee "Dorian, are you alright?"

    "He stared down at me, expression unreadable-but his voice was gentle in my mind, a whisper of moonlight and wind."
    voice audio.dorian_ch10_line25
    dorian "Chung..."

    "He nodded slowly, brushing the blood from my cheek with care."

    voice audio.chung_ch10_line32  # transcript: "It's alright now. You're safe."
    chung_hee "It's alright now. You're safe. I've got you."

    "The weight of everything caught up to me. The battle. Elara. The children. My soul was fraying at the edges."
    "But Chung-hee held me close, shielding me from the cold. He came for me."

    voice audio.chung_ch10_line33  # transcript: "Everything's going to be alright."
    chung_hee "Everything's going to be alright. I'll try to-"

    "A soft whirring sound echoed in the distance."

    show supply_robot base at center_supply with Dissolve(0.2)
    voice audio.supplybot_ch10_line6
    supply_robot "Emergency assistance activated. Master Yuxuan suspected that Sir Chung-hee and Master Dorian might need assistance."
    voice audio.supplybot_ch10_line7
    supply_robot "He was, as always, correct."

    voice audio.chung_ch10_line34  # transcript: "a supply bot. Think RengiaBov"
    chung_hee "A supply bot. Thank Renji above for Yuxuan and his intellect."

    "The small metal drone hovered into view, arms outstretched with medkits and healing supplies."
    voice audio.supplybot_ch10_line8
    supply_robot "Analyzing injuries. Administering emergency stabilization. Please hold Master Dorian's hand. Studies show physical contact aids recovery."

    voice audio.chung_ch10_line35  # transcript: "Everything's under control, Dorian, aye?"
    chung_hee "Everything's under control, Dorian. I-"

    show dorian normal_alt_tense at left_char with Dissolve(0.2)
    "My eyelids felt heavy..."

    scene black with fade
    "And then... the world faded to black..."

    jump ch10_tianho_battle


# =============================================================================
# SECTION 22: LABEL CH10_RESCUE_SVANTE — Svante Rescues Dorian
# =============================================================================

label ch10_rescue_svante:
    play sound sfx_metal_blades  
    "The air shrieked as something whipped past my ear-razor-sharp, blindingly fast."
    play sound audio.sfx_blade
    "CLANG!"

    "The Yaoguai King's arm was knocked aside by a gleaming dagger of steel. A flash of silver. A howl of pain."
    "Its arm exploded in a spray of black ichor."
    voice audio.yk_ch10_line89
    yk "GAHHHH-WHAT?!"

    play music audio.svante_theme volume 0.8 loop
    "Violet hair, eyes burning with fury. Violet armor slick with battle light."

    voice audio.dorian_ch10_line48
    dorian "S... Svante?"
    
    scene cg_svante_saves_dorian with shock_cut
    "He didn't look at me. His gaze was locked on the monster in front of him."

    voice audio.svante_ch10_line18  # transcript: "Step away from him."
    svante "Step. Away. From him."
    voice audio.yk_ch10_line90  # transcript: "You insolent little"
    yk "You insolent little-"

    play sound audio.sfx_blade
    "Another blade sliced into the King's shoulder, spraying more blood. Svante raised a single hand."
    "One. Two. Then hundreds of blades shimmered into view-floating, circling him like metal constellations. Long swords. Needles. Daggers. Cleavers. All forged with deadly precision, glinting like judgment."

    voice audio.svante_ch10_line19  # transcript: "I won't ask again."
    svante "I won't ask again."
    yk "Nnnghh-What... what are you?!"

    "A voice rang out-calm, powerful, ancient."

    prosperity_dragon "Svante Nordström. Illegitimate son of King Gustav of Mjoll. A heart forged not from royal blood, but from undying loyalty and courage."
    voice audio.yk_ch10_line84  # transcript: "The... The Prosperity Dragon."
    yk "The... the Prosperity Dragon...?!"
    voice audio.yg_scream
    "The Yaoguai King roared, furious, his claws curling as he summoned the shadows."
    voice audio.yg_screech  
    "The yaoguai spirits surrounding the Yaoguai King sprang forth-wailing specters of the dead, cloaked in fire and grief. They screeched, lunging toward Svante with blazing teeth and blade-like limbs."

    voice audio.svante_ch10_line20  # transcript: "Merciful enough."
    svante "M-Merciful Enoch..."

    hide yg

    "Svante ran as the swarm of spirits surged toward him. Then, he leapt in midair, meeting the spirits."
    "The pieces of metal surrounding him whirled like a hurricane, cutting through the spectral horde with blinding speed."
    play sound sfx_metal_blades  
    voice audio.sfx_blade
    "Spirits were pierced, severed, disintegrated by in flashes of light. Svante advanced with purpose-not one step wasted."
    play sound audio.sfx_blade
    "He reached the Yaoguai King and pierced his leg, then his shoulder-his jaw shattered beneath a whirling disk of steel."
    voice audio.yg_screech
    "The Yaoguai King shrieked, flailing, but every attempt at retaliation was met by a storm of blades that tore through flesh and armor alike."
    "Blood. Smoke. Steel. Svante was unrelenting."
    "The King staggered, fell to one knee, face twisted in pain and disbelief."
    play sound audio.sfx_blade
    "Svante took a sword and stabbed the King, tore through the Yaoguai King's chest, straight through heart and spine. The monster arched back, screaming, black flames pouring from his mouth."

    yk "AAAAAGHHHHH-!! NO!!! NOOOOO!!!"

    "The shadows writhed. And then, with one final gasp..."
    play sound audio.sfx_body_thud
    "The Yaoguai King collapsed in a heap of soot and shadow, disintegrating into the earth. Silence."
    "A deafening, holy silence."
    stop music fadeout 2.0
    scene underground_magnus with fade
    "I stumbled, vision blurring. My legs gave out. I fell, but strong arms caught me."

    show svante normal_nervous at right_char
    show dorian neutral at left_char 
    with Dissolve(0.2)
    voice audio.svante_ch10_line21  # transcript: "Dorian!"
    svante "DORIAN!"

    "He pulled me close, clutching me as though I might disappear."
    voice audio.svante_ch10_line22
    svante "Hey-hey. Look at me. Eyes open, alright? You're not dying on me. Not now. Not ever. Please..."

    "I gave a weak breath, blood trailing from my lips."

    voice audio.dorian_ch10_line49  # transcript: "You... You saved me."
    dorian "You... You saved me..."
    voice audio.svante_ch10_line23  # transcript: "I guess so. Dorian, I"
    svante "I guess so... D-Dorian, I was so scared. I thought I was too late. I thought I lost you."

    show dorian normal_alt_tense at left_char with Dissolve(0.1)
    "I tried to say his name again, to tell him I was still here-but the darkness came too fast, too heavy."

    voice audio.svante_ch10_line24
    svante "No-no, no, no. Stay with me. Dorian-stay with me!"

    "He looked up, desperation in his eyes."

    voice audio.svante_ch10_line25  # transcript: "Help! Please! Anyone!"
    svante "HELP! PLEASE! ANYONE!"

    "A soft whirring sound echoed in the distance."

    show supply_robot base at center_supply with Dissolve(0.2)
    voice audio.supplybot_ch10_line9
    supply_robot "Emergency assistance activated. Master Yuxuan suspected Master Dorian might be reckless. He was, in fact, correct."

    "The small metal drone hovered into view, arms outstretched with medkits and healing supplies."

    voice audio.svante_ch10_line26  # transcript: "Please! He needs help now!"
    svante "Please! He needs help-now!"
    voice audio.supplybot_ch10_line8
    supply_robot "Analyzing injuries. Administering emergency stabilization. Please hold Master Dorian's hand. Studies show physical contact aids recovery."

    voice audio.svante_ch10_line27  # transcript: "Hold on tight, Dorian. Everything"
    svante "Hold on tight, Dorian. Everything-"

    "His voice trailed off. I closed my eyes."
    scene black with dissolve
    "And then-darkness."

    jump ch10_tianho_battle


# =============================================================================
# SECTION 23: LABEL CH10_RESCUE_NIKO — Niko Rescues Dorian
# =============================================================================

label ch10_rescue_niko:
    "A sudden howl tore through the shadows."

    play sound sfx_shadow_burst                 # PLACEHOLDER — shadow burst SFX
    "A wind unlike any other ripped through the chamber-freezing cold, black as the void, alive with wrath. The Yaoguai King froze."
    play sound audio.sfx_stone_break 
    "And then, he was slammed off his feet-hurled across the chamber as a tidal wave of darkness crashed into him." with hpunch
    stop sound fadeout 1.5
    
    voice audio.yk_ch10_line83  # transcript: "Shadows, I was supposed to"
    yk "Shadows?! I was supposed to be your master! I-!"
    
    play sound audio.sfx_shadows
    "The shadows screamed."
    play music audio.niko_theme volume 0.8 fadein 1.5
    "And from the heart of them stepped a figure."

    voice audio.dorian_ch10_line42
    dorian "N... Niko?"
    
    scene cg_niko_saves_dorian with shock_cut
    "His face was cold, twisted in rage. Shadows flowed like blood from his fingertips, surpassing the Yaoguai King's."
    
    play sound sfx_shadow_burst
    "They coiled and snarled like starving wolves, eager to devour."
    "The Yaoguai King lunged from the rubble, claws raised. But Niko didn't flinch."

    yk "You insolent-"
    play sound sfx_shadow_burst
    voice sfx_shadows
    "With a single flick of Niko's wrist, spears of shadow launched forward-howling through the air like a chorus of executioners. They skewered the Yaoguai King's arm, nailing it to the wall."
    
    voice audio.yg_scream
    "He screamed, shadows biting into him like venom."

    voice audio.yk_ch10_line91  # transcript: "What? What are you?"
    yk "What-what are you?!"

    prosperity_dragon "Niko Tsukumo. Chosen Champion of the Death God Enoch. Former Healer in the village of Hamatame."
    voice audio.yk_ch10_line92  # transcript: "The... The Prosperity Dragon."
    yk "The... the Prosperity Dragon...?!"

    "The Yaoguai King's eyes widened in horror."

    voice audio.yk_ch10_line81  # transcript: "You were chosen. The dragon"
    yk   "You were chosen?! The Dragon talks to you?! But how?! I don't-"
    voice audio.niko_ch10_line29  # transcript: "You hurt him. You dare"
    niko "You hurt him. You dared to pretend to be her. You mocked his pain."


    "He raised both hands, and an enormous ring of shadow erupted around them."
    play sound sfx_shadows
    voice audio.niko_ch10_line30  # transcript: "Your death won't be quick."
    niko "Your death won't be quick. I want you to remember what fear tastes like."
    voice audio.yk_ch10_line86  # transcript: "The shadows. Mercy. I didn't"
    yk   "T-These shadows... M-Mercy! I didn't mean to insult the death god! I thought he wasn't supposed to intrude with my killing!"
    voice audio.niko_ch10_line31  # transcript: "I'll tear your soul apart."
    niko "I'll tear your soul apart piece by piece."
    voice audio.yk_ch10_line87  # transcript: "Mercy, please, please!"
    yk   "Mercy! Please-PLEASE!"

    voice audio.yk_ch10_line93
    play sound audio.sfx_shadow_burst
    "The Yaoguai King screamed as the shadows surged forward-latching onto his limbs, face, chest."
    "His flesh began to burn with a fire blacker than night."
    play sound audio.sfx_back
    "His bones cracked. His blood evaporated into mist."

    voice audio.yk_ch10_line88
    yk "AHHHHHH-!! NO-NO!! STOP! I BEG-PLEASE-AAAGHHH!!"

    "His skin peeled back. His eyeballs shriveled and popped, leaking black tears. His spine bent backwards as his legs twisted in unnatural angles."
    "The shadows clawed deeper-not just through body, but soul. Memory. Identity. Existence. He was undone."
    "Every lie. Every cruelty. Every scream he'd ever silenced-torn back into the world and used to shred him."
    "He shrank. Withered. Turned to ash. Until there was nothing left."
    "Nothing but soot."
    "Niko remained still. Unblinking. Merciless."
    "The air went still-eerily silent-as if the world itself dared not speak."
    "I felt my legs give out. My body couldn't take it anymore. I collapsed. But strong arms caught me."
    stop music fadeout 2.0
    scene underground_magnus with fade

    show niko alt_tense at right_char
    show dorian normal_alt_tense at left_char
    with Dissolve(0.2)

    voice audio.niko_ch10_line32  # transcript: "Dorian!"
    niko "DORIAN!"

    "He knelt, cradling me with shaking hands. My vision was fractured-blurry outlines, streaks of red. I tasted iron."
    voice audio.niko_ch10_line33
    niko "No-no no no. Look at me. Look at me."

    show dorian neutral at left_char with Dissolve(0.1)
    "He pulled me into his arms. His shaking hands cupped my face, his breath frantic."

    show niko normal_sad at right_char with Dissolve(0.1)
    voice audio.niko_ch10_line34  # transcript: "I got you. I got"
    niko "I got you. I got you, okay? You're safe now."

    "His voice cracked."
    "He ripped open his pouch and quickly crushed a handful of dried herbs, shoving the bitter powder into my mouth, followed by a flask of water."
    
    show niko normal_serious at right_char with Dissolve(0.1)

    voice audio.niko_ch10_line35  # transcript: "swallow that's it come on"
    niko "Swallow. That's it. Come on. Stay awake."
    voice audio.dorian_ch10_line43
    dorian "N... Niko... You saved me..."

    "My vision dimmed. I could barely see his face anymore."

    show niko normal_base at right_char with Dissolve(0.1)
    voice audio.niko_ch10_line36  # transcript: "You won't die. First I"
    niko "You won't die. First, I need to get you to-"

    "A soft whirring sound echoed in the distance."

    show supply_robot base at center_supply with Dissolve(0.2)
    voice audio.supplybot_ch10_line10
    supply_robot "Sir Niko detected. Emergency assistance activated. Master Yuxuan suspected Master Dorian might be reckless. He was, in fact, correct."

    "The small metal drone hovered into view, arms outstretched with medkits and healing supplies."
    show niko normal_anger at right_char with Dissolve(0.1)
    voice audio.niko_ch10_line37  # transcript: "Hey, over here! Help him,"
    niko "Hey! Over here! HELP HIM-NOW!"
    voice audio.supplybot_ch10_line11
    supply_robot "On it, sir Niko. Hastening services for emergency. Administering trauma-grade stabilizers. Please remain still, Master Dorian."
    show niko normal_base at right_char with Dissolve(0.1)

    voice audio.niko_ch10_line38  # transcript: "Everything will be alright, Door."
    niko "Everything will be alright, Dori-"

    "His voice trailed off. I closed my eyes."
    scene black with fade
    "And then-darkness."

    jump ch10_tianho_battle


# =============================================================================
# SECTION 24: LABEL CH10_RESCUE_MAGNUS — Magnus Rescues Dorian
# =============================================================================

label ch10_rescue_magnus:
    scene underground_magnus with dissolve

    voice audio.magnus_ch10_line35  # transcript: "Really? You really want me?"
    magnus "Really? You really want me?"

    "A voice, bright and thundering, cut through the suffocating dark like a blade of sunlight cleaving stormclouds."
    play music audio.ost_magnus_battle loop volume 0.75 fadein 3.0
    voice audio.magnus_ch10_line36  # transcript: "Well, I'm absolutely positively flattered."
    magnus "Well, I am absolutely and positively flattered!"
    show magnus clothed_no_wings at left_char
    show yk at right_char 
    with Dissolve(0.2)
    "From the smoke and ruin, he stepped forward. His golden eyes were ablaze, full of fury. Sweat clung to his face. His chest rose and fell, breath ragged."

    voice audio.magnus_ch10_line37  # transcript: "Then come face me, Demon."
    magnus "Then come and face me, demon. Here I am."

    voice audio.dorian_ch10_line36
    dorian "M... Magnus? No... I-"
    play sound audio.sfx_ice_explosion
    show magnus alt_evil_eye at left_char with flash
    "He ripped off his shirt in one sharp motion, his body glowing with sacred marks. Wings erupted from his back."

    voice audio.magnus_ch10_line38  # transcript: "Touch him again and I'll"
    magnus "Touch him again and I'll rip your cursed throat out."
    voice audio.yk_ch10_line75  # transcript: "Had lost the divine weapon."
    yk "At last. The Divine Weapon."

    play sound audio.sfx_body_thud
    "The Yaoguai King hissed and flung me aside like a discarded toy. I hit the ground, groaning weakly. I could barely keep my eyes open."
    "The Yaoguai King laughed manically."

    voice audio.yk_ch10_line76
    yk "HAHAHAHAHA!! AT LAST! AT LONG LAST! THE DIVINE WEAPON IS FINALLY MINE!!"
    voice audio.yk_ch10_line77  # transcript: "Now drop to your knees."
    yk "Now drop to your knees. I want to see you-"

    "He never finished."
    scene cg_magnus_saves_dorian with flash
    
    voice audio.yk_ch10_line78
    yk "Ughhh-ack..."

    play sound audio.sfx_ice_explosion
    "Magnus reappeared behind him, a golden lance piercing straight through the king's chest. Light surged. The Yaoguai King convulsed."
    play sound audio.sfx_body_thud
    voice audio.yk_ch10_line79
    yk "ARGHHH! What... What are you doing?!"

    prosperity_dragon "Magnus Wyndham. The so-called Divine Weapon. A new man."
    voice audio.yk_ch10_line97  # transcript: "The... the prosperity dragon?"
    yk "The... the Prosperity Dragon...?!"

    "The Yaoguai King's eyes widened in horror."

    voice audio.yk_ch10_line85  # transcript: "You were chosen. The dragon"
    yk "You were chosen?! The Dragon talks to you?! But how?! I don't-"
    voice audio.magnus_ch10_line39  # transcript: "Oh, you're too kind, Dragon."
    magnus "Aww you're too kind, Dragon. Now if you'll excuse me."

    "He launched skyward, dragging the king with him, wings leaving a burning wake. Then-"

    "BOOM."
    play sound audio.sfx_yaoguai_burst volume 0.75
    voice audio.yg_scream
    "A blazing sigil erupted across the underground rooftop, ancient and divine. The king screamed as the flames consumed him-white-hot fire pouring from his eyes and mouth."

    yk "GRAHHH!! NOOO!!! AHHHH!!!"
    voice audio.magnus_ch10_line40  # transcript: "You shall never touch him"
    magnus "YOU. SHALL. NEVER. TOUCH HIM. AGAIN!"

    "The Yaoguai King exploded in a storm of ash and shadow. The light swallowed it all. And then-Silence."
    "Magnus landed hard beside me, stumbling, dropping to his knees at my side."
    stop music fadeout 3.0
    scene underground_magnus with fade
    show magnus alt_shocked at right_char
    show dorian normal_alt_tense at left_char
    with Dissolve(0.2)
    voice audio.magnus_ch10_line41
    magnus "Dorian? Dorian! Hey-no, no, no, stay with me. Please."
    voice audio.dorian_ch10_line37  # transcript: "Magnus, you came..."
    dorian "M.. Magnus... You... came..."

    "His hands were trembling as he gathered me in his arms, pressing his forehead to mine."

    voice audio.magnus_ch10_line42  # transcript: "You're okay. You're okay. I"
    magnus "You're okay. You're okay. I've got you. Just breathe... You idiot..."
    voice audio.magnus_ch10_line43  # transcript: "Weaver's Bothex, why'd you fight"
    magnus "Weaver's bollocks, why'd you fight him alone...?"

    "I tried to say his name again, to tell him I was still here-but the darkness came too fast, too heavy."

    voice audio.magnus_ch10_line44  # transcript: "No. No."
    magnus "No... No..."
    voice audio.magnus_ch10_line45  # transcript: "Please, someone help! Is there"
    magnus "PLEASE! SOMEONE HELP! IS THERE ANYONE HERE?!"

    play sound audio.sfx_roboto_motor
    "A soft whirring sound echoed in the distance."
    show supply_robot base at center_supply with Dissolve(0.2)
    voice audio.supplybot_ch10_line12
    supply_robot "Sir Magnus detected. Emergency medical protocol online. Master Yuxuan suspected Master Dorian might be reckless. He was, in fact, correct."

    "The small metal drone hovered into view, arms outstretched with medkits and healing supplies."
    show magnus alt_newpose at right_char with Dissolve(0.1)
    voice audio.magnus_ch10_line46  # transcript: "What? You shone sent you?"
    magnus "Wh-what? Yuxuan sent you?"
    voice audio.supplybot_ch10_line13
    supply_robot "Affirmative. Master Yuxuan stated, quote: 'If Magnus goes after Dorian, which he absolutely will, bring everything and prepare for melodrama.'"

    show magnus alt_shocked at right_char with Dissolve(0.1)
    voice audio.magnus_ch10_line47  # transcript: "Hello, drama. I never mind."
    magnus "Melodrama? I-Never mind, help Dorian!"
    voice audio.supplybot_ch10_line14
    supply_robot "Vital signs stabilizing. Continue holding his hand. Data suggests you refusing to let go improves patient survival by 6.8%%"

    "Magnus cradled me close. Then, softly-tenderly-he began to hum."

    show magnus alt_newpose at right_char with Dissolve(0.1)
    voice audio.magnus_ch10_line49  # transcript: "I'll follow you through fire"
    magnus "I'll follow you through fire and flame... Wherever you go, I'll bear your name..."
    voice audio.supplybot_ch10_line15
    supply_robot "Please be advised that Master Yuxuan advises songs should be reserved until after stabilization."

    show magnus alt_smirk at right_char with Dissolve(0.1)
    voice audio.magnus_ch10_line50  # transcript: "Oh, sorry, robot sir. Please"
    magnus "O-Oh! S-Sorry, robot sir. Please-carry on!"
    voice audio.supplybot_ch10_line16
    supply_robot "Affirmative."

    show magnus alt_newpose at right_char with Dissolve(0.1)
    voice audio.magnus_ch10_line51  # transcript: "Everything will be"
    magnus "Everything will be-"   

    scene black with fade
    "His voice trailed off. I closed my eyes. And then-darkness."

    jump ch10_tianho_battle


# =============================================================================
# SECTION 25: LABEL CH10_TIANHO_BATTLE — Tianho / Gao / Jiang / Feng Gate
# =============================================================================

label ch10_tianho_battle:

    play music audio.ost_battle fadein 1.0 loop     # PLACEHOLDER — battle theme

    scene bg_tianho_city_night with flash

    show soldier_jiang at left_char
    show soldier_gao at right_char
    with Dissolve(0.2)

    voice audio.jiang_ch10_line6  # transcript: "Everyone fall back! Get inside"
    jiang "Everyone, fall back! Get inside your homes, now! Barricade the doors!"
    voice audio.gao_ch10_line2  # transcript: "GO! Don't look back! Get"
    gao   "GO! Don't look back! Get to Cheng Industries!"
    voice audio.yg_scream
    scene bg_tianho_city_night 
    show yaoguai at center_yg 
    with Dissolve(0.2)
    yg    "GRAWWRR!!!"

    hide yaoguai
    show soldier_jiang at left_char
    show soldier_gao at right_char
    with Dissolve(0.2)

    voice audio.jiang_ch10_line7  # transcript: "GAL! We've got incoming! Let's"
    jiang "GAO! We've got incoming! Left flank!"
    play sound audio.sfx_blade
    voice audio.gao_ch10_line3  # transcript: "I see it!"
    gao   "I see it!"
    voice audio.jiang_ch10_line8  # transcript: "Nice! You hit it!"
    jiang "Nice! You hit it!"

    if highest_character == "chunghee":
        
        hide yaoguai
        # scene bg_tianho_city_night with Dissolve(0.2)
        show yuxuan normal_angry at center_char with Dissolve(0.2)

        voice audio.yuxuan_ch10_line22  # transcript: "Yang, Gao, don't do anything"
        yuxuan "Jiang! Gao! Don't do anything reckless! Please-stay sharp, stay alive. My companions will handle the front."
        voice audio.jiang_ch10_line9  # transcript: "Understood, Master Yushuan. We'll hold"
        jiang  "Understood, Master Yuxuan. We'll hold the line. You can count on us."
        voice audio.gao_ch10_line4  # transcript: "Wouldn't be the first time"
        gao    "Wouldn't be the first time we've danced with monsters."

        hide soldier_gao
        hide soldier_jiang
        show svante normal_base at left_char 
        show magnus alt_newpose at right_char
        show yuxuan normal_neutral at center_char
        with Dissolve(0.2)

        voice audio.svante_ch10_line28  # transcript: "Leave the heavy lifting to"
        svante "Leave the heavy lifting to us. We'll make sure nothing gets past."
        voice audio.yuxuan_ch10_line23  # transcript: "Alright, we're trusting you. All"
        yuxuan "Alright... We're trusting you. All of you. Make it count."
        voice audio.magnus_ch10_line17  # transcript: "I shall scout up in"
        magnus "I shall scout up in the air. I shall see if there are more yaoguai."
        yuxuan "Oh that's actually a very good idea, Magnus."

        hide svante
        show niko normal_serious at left_char with Dissolve(0.2)

        voice audio.niko_ch10_line18  # transcript: "Everyone in position! No mistakes."
        niko   "Everyone! In position! No mistakes. We hold the gate or we die trying."
        show yuxuan normal_sad at center_char with Dissolve(0.1)
        voice audio.yuxuan_ch10_line24  # transcript: "Come on Dorian, wherever you"
        yuxuan "Come on, Dorian... wherever you are. Don't die on us now."

    else:
        hide yaoguai
        show chunghee normal_neutral at center_char with Dissolve(0.2)

        voice audio.chung_ch10_line7  # transcript: "Jing, Gao, do not act"
        chung_hee "Jiang. Gao. Do not act without thought. Stay sharp. Stay alive. My companions will handle the front."
        voice audio.jiang_ch10_line10  # transcript: "Understood, sir, Chonghi. We'll hold"
        jiang  "Understood, sir Chung-hee. We'll hold the line. You can count on us."
        gao    "Wouldn't be the first time we've danced with monsters."
        female_soldier_1 "We'll fight to our last breath to protect Tianho, my lord!"
        male_soldier_1 "I can't believe the Emperor of Kyeongjang is fighting with us! For our children... for every home still standing. For Tianho!"
        show chunghee normal_angry at center_char with Dissolve(0.1)
        voice audio.chung_ch10_line8
        chung_hee "To arms! Let the Yaoguai learn that Tianho's spirit does not break. Not now. Not ever."
        show chunghee normal_power_up at center_char with Dissolve(0.1)
        voice audio.chung_ch10_line9  # transcript: "Let no y'all guise survive!"
        chung_hee "Let no yaoguai survive!"
        show chunghee normal_neutral at center_char with Dissolve(0.1)

        voice audio.chung_ch10_line10  # transcript: "Dorian, wherever you are, you"
        chung_hee "Dorian... Wherever you are, you have to survive."

    scene bg_tianho_city_night
    show soldier_jiang at left_char
    show soldier_gao at right_char
    with Dissolve(0.2)

    man_1 "HELP! SOMEONE, PLEASE-AHHH!!!"
    voice audio.yg_scream     
    yg    "Graawwwr!!"
    voice audio.jiang_ch10_line11  # transcript: "I'll help you, sir. Gow,"
    jiang "I'll help you, sir! Gao, cover me!"
    voice audio.gao_ch10_line5  # transcript: "Honnets, y'ang!"
    gao   "On it, Jiang!"

    hide soldier_jiang
    hide soldier_gao
    show yaoguai at center_yg with Dissolve(0.2)
    voice audio.yg_scream     
    yg    "Graawwwr!!"

    if feng_score < 2:
        hide yaoguai
        show soldier_jiang at left_char
        show soldier_gao at right_char 
        with Dissolve(0.2)
        "Jiang managed to reach the man, shielding him—but it's too late."
        voice audio.yg_scream     
        yg "Graawwwr!!"
        
        voice audio.jiang_ch10_line12
        jiang "Get behind me! Go!"

        man_1 " AHHH!!!"
        voice audio.yg_scream     
        yg "GRAAAAAAAR!!"
        play sound audio.sfx_claw
        

        voice audio.jiang_ch10_line13
        jiang "NOO!!! DAMMIT! WE FAILED, GAO! I-"
        voice audio.gao_ch10_line6  # transcript: "G-ing! Look behind you!"
        gao   "JIANG!! LOOK BEHIND YOU!"
        voice audio.jiang_ch10_line14  # transcript: "What the-"
        jiang "What the-"

        show yaoguai at center_yg with Dissolve(0.2)
        voice audio.yg_scream     
        yg "GRAAAAAAARRR!!"

        play sound sfx_claw                   # PLACEHOLDER — claws SFX
        voice audio.jiang_ch10_line15
        jiang "ARGHH!!!"
        voice audio.gao_ch10_line7  # transcript: "She ain't no! Please get"
        gao   "JIANG!! NO!! PLEASE!! GET UP!!"
        voice audio.yg_scream     
        yg    "GWAAARR!!"
        voice audio.gao_ch10_line8  # transcript: "No! Please! No! Not me!"
        gao   "No... Please!! No! Not me!! AHHH!!"

        play sound sfx_claw                   # PLACEHOLDER — claws SFX

        hide soldier_gao
        hide soldier_jiang
        with Dissolve(0.1)

        yg "GWAAARR!"

        if highest_character == "yuxuan":
            voice audio.niko_ch10_line39  # transcript: "He knockup of go JANG!"
            niko "ENOCH ABOVE!! GAO!! JIANG!! NO!!"
        else:
            voice audio.yuxuan_ch10_line13
            yuxuan "NO!! GAO!! JIANG!! *cries*"

    else:
        hide yaoguai
        show soldier_jiang at left_char
        show soldier_gao at right_char
        with Dissolve(0.2)

        gao   "JIANG!! LOOK BEHIND YOU!"
        voice audio.jiang_ch10_line16  # transcript: "What the-"
        jiang "What the-"
        show feng_suit at center_char with Dissolve(0.2)
        feng  "GET BACK!"
        voice audio.gao_ch10_line9  # transcript: "Wait, paladin fang!"
        gao   "Wait... PALADIN FENG!!"
        feng  "Stay low. You're not dying today."

        voice audio.jiang_ch10_line17
        jiang "F-Feng?! P-Paladin! SIR!"
        feng  "I've seen too many good people fall today. I won't lose you two. Not tonight."
        hide soldier_jiang
        hide soldier_gao
        show feng_suit at left_char 
        show yaoguai at right_yg
        with Dissolve(0.2)
        voice audio.yg_screech
        yg    "GWAAARR!!"
        feng  "HYAAAA!!"
        hide yaoguai
        show feng_suit at center_char
        show soldier_gao at right_char
        show soldier_jiang at left_char
        with Dissolve(0.2)
        voice audio.gao_ch10_line10  # transcript: "So cool!"
        gao   "S... So cool...."
        feng  "Heh. Five years of working together and you're crushing on me now, Gao? I'm touched."
        man_1 "Th-thank you! May the Prosperity Dragon bless you!"
        feng  "Get inside. And lock all the damn doors. And for the love of, we told you to get inside!"
        man_1 "Y-Yes, sir!!"
    
        voice audio.jiang_ch10_line18  # transcript: "Let's move everyone! Let's move!"
        jiang "Let's move, everyone! Let's move!"

        hide soldier_jiang
        hide soldier_gao
        show feng_suit at left_char 
        with Dissolve(0.1)

        if highest_character == "yuxuan":
            show niko alt_base at right_char with Dissolve(0.2)
            niko "Paladin Feng... Seems we'll need to put our differences aside. We're grateful for your help."
        else:
            show yuxuan normal_neutral at right_char with Dissolve(0.2)
            yuxuan "Paladin Feng!! Oh!! Thank the Prosperity Dragon you're still here..."

        feng "Heh. You're lucky my best friend still owes me a drink. Now-how about we roast some yaoguai? My blue flame's just getting warmed up."
    stop music fadeout 2.0
    jump ch10_tianho_aoi


# =============================================================================
# SECTION 26: LABEL CH10_TIANHO_AOI — Babala / Aoi Gate
# =============================================================================

label ch10_tianho_aoi:

    scene tianho_food_stalls_fire with fade
    play music audio.ost_battle fadein 1.0 loop
    show babala at left_char with Dissolve(0.2)
    voice audio.babala_ch10_line1  # transcript: "Damn, Tweaver! I... I can't"
    babala "Damned Weaver... I-I can't for the life of me... My arms... they won't respond. I can't channel... not like I used to..."
    male_guard "We already told you to stay inside your homes! Why won't you listen?!"
    female_guard "Mam, please! We have to move-now!"
    voice audio.babala_ch10_line2  # transcript: "I'm trying!"
    babala "I'm trying!"
    voice audio.babala_ch10_line3  # transcript: "I shouldn't have come here."
    babala "I shouldn't have come here. These old bones were never meant for battle. This was foolish..."

    show yaoguai at right_yg with Dissolve(0.2)
    voice audio.yg_scream                 # PLACEHOLDER — yaoguai roar
    yg     "GRAWWWRR!!"
    voice audio.babala_ch10_line4  # transcript: "Help! Someone please!"
    babala "HELP! Someone-please!"

    if aoi_score < 2:

        female_guard "It's right behind us-AAHHH!!!"
        voice audio.yg_scream
        yg "GRAWWRRRRR!!!"

        voice audio.babala_ch10_line5
        babala "ARGHHH!!"
        male_guard "NO! NO!! AHH!!"

    else:
        $ aoi_score += 1
        female_guard "No!! No!!"
        male_guard "Get behind me, mam!"
        stop music fadeout 2.0
        voice audio.yg_scream
        yg  "GRAWWRRRRR!!!"
        hide babala

        play music audio.aoi_theme fadein 2.0 volume 0.75
        show aoi_battle_suit at left_char with Dissolve(0.2)
        voice audio.aoi_ch10_line1  # transcript: "Not today"
        aoi "Not today."

        voice audio.yg_screech
        yg  "GYAAAAA!!!"
        hide yaoguai
        show babala at right_char with Dissolve(0.2)
        voice audio.babala_ch10_line6  # transcript: "Evans, what is stunning young"
        babala "Heavens! What a stunning young woman! Thank the Weaver, you-"
        voice audio.aoi_ch10_line2  # transcript: "Save the flattery, more coming."
        aoi "Save the flattery. More are coming. Why are you even out here? We told you to evacuate!"
        voice audio.babala_ch10_line7  # transcript: "Alright alright, no need to"
        babala "Alright, alright! No need to shout!"
        voice audio.aoi_ch10_line3  # transcript: "What was that?"
        aoi "What was that?"
        voice audio.babala_ch10_line8  # transcript: "Nothing. Just grateful as all."
        babala "Nothing! Just grateful, is all. Pft."
        male_guard "That was incredible water channeling... Wait... Aren't you the songstress who performed earlier?"
        voice audio.aoi_ch10_line4  # transcript: "Yes, I'm Owie. Owie Mizuhara,"
        aoi "Yes. I'm Aoi. Aoi Mizuhara. Pleasure to meet you."
        voice audio.aoi_ch10_line5  # transcript: "You come with me. We"
        aoi "You-come with me. We don't have time to waste."
        voice audio.aoi_ch10_line6  # transcript: "They're more in this sector."
        aoi "There are more in this sector. I won't let a single one of them leave unscathed. They'll learn what it means to challenge a mistress of water."
        female_guard "Mam!"

        if feng_score >= 2 and aoi_score >= 1:
            hide babala
            show feng_suit at right_char with Dissolve(0.2)

            feng "Well, well... You wear the battlefield well, Lady Aoi. Quite the vision outside your kimono. Long hair really does suit you."
            voice audio.aoi_ch10_line7  # transcript: "Really thing, save the charm"
            aoi  "Ugh. Really, Feng? Save the charm for after we've cleaned up this mess. Now move-we're not done yet."

            show yaoguai at center_yg with Dissolve(0.2)
            voice audio.yg_screech
            yg   "GRAWWRRRRR!!!"
            hide yaoguai with Dissolve(0.1)
            voice audio.aoi_ch10_line8  # transcript: "to think they've learned from"
            aoi  "To think... they've learned from their attack yesterday."
            feng "Heh. More fun for us. Let's do it. I'll even give you a nice bonus if we survive."
            voice audio.aoi_ch10_line9  # transcript: "Agreed, you're on. It would"
            aoi  "Agreed. You're on. It would be an opportunity to go all out with my water channeling."
            feng "And me with my blue fire."
            feng "Side by side, you and me? These yaoguai won't know what hit them."
            feng "They will be sorry they messed with Tianho."

    jump ch10_epilogue


# =============================================================================
# SECTION 27: LABEL CH10_EPILOGUE — Prosperity Dragon Narration / Kitchen / Sail
# =============================================================================

label ch10_epilogue:
    scene black with dissolve
    scene bg_tianho_city_morning with fade
    stop music fadeout 2.0
    # play music ost_ch10_aftermath fadein 2.0    # PLACEHOLDER — aftermath / hopeful theme
    pause 3.0
    
    prosperity_dragon "And so, the attack on Tianho was repelled. The fires of war were extinguished not by luck, but by the bravery of those who stood unwavering in the face of despair."
    prosperity_dragon "Among them... one still rests."
    play music audio.dorian_theme fadein 2.5 loop
    prosperity_dragon "Dorian-the Dragon of Gale, bearer of grief, fire, and unyielding will-now lies in recovery, his body battered, but his soul no longer burdened by vengeance."
    prosperity_dragon "When he awoke, it was not to battle horns or the roar of flame, but to a familiar warmth. A small hand in his own. A voice, soft and sweet."

    show elias normal_happy at right_char_kids
    show dorian neutral at left_char
    show supply_robot normal at center_supply
    with Dissolve(0.2)
    voice audio.elias_ch10_line1  # transcript: "Daddy, you're weak!"
    elias "Daddy! You're awake!"
    voice audio.supplybot_ch10_line17
    supply_robot "Vitals stable. Blood pressure within optimal range. Neural activity increasing... Welcome back, Master Dorian."

    prosperity_dragon "The weight that had pressed on his heart for so long finally lifted in that moment. For the first time in what felt like lifetimes... he breathed without ache."
    prosperity_dragon "And beside him, the one who had saved him-the partner who stood between him and death-remained close."
    prosperity_dragon "To him, Dorian knew only gratitude. And perhaps, something deeper."
    prosperity_dragon "The Yaoguai King was no more. Justice-delayed, but never denied-was finally delivered. His family could rest. And so, too, could he."
    prosperity_dragon "The flames of revenge no longer consumed him. In their place... new embers flickered. Softer ones. Hopeful ones."
    prosperity_dragon "Dorian now stands at the edge of a new chapter. Not written in blood or fury-but perhaps... in love."
    stop music fadeout 1.5
    prosperity_dragon "As for our tale... it is not yet over."

    scene lab_cave_on with fade 
    play music audio.ost_yuxuan_lab fadein 1.5 loop volume 0.5
    show magnus alt_newpose at center_char
    show yuxuan normal_neutral at left_char
    show weng normal at right_flip
    with Dissolve(0.2)

    "I gathered everyone in the kitchen. I told them everything. About Magnus. About the Yaoguai King. About the Divine Weapon."

    voice audio.yuxuan_ch10_line14  # transcript: "Wait, so let me get"
    yuxuan "Wait... so let me get this straight. Magnus is a clone of the Death God?!"
    weng   "By the stars... I can't believe it. The Death God..."
    show magnus alt_shocked at center_char with Dissolve(0.2)
    "Magnus sat off to the side, silent, his brows furrowed in confusion. I didn't blame him."

    voice audio.magnus_ch10_line9  # transcript: "I don't really feel like"
    magnus "I... don't really feel like a clone. I don't even know what that means. I have memories. Feelings. I've laughed, cried, bled. How do you explain that?"

    hide weng
    show svante normal_base at right_char with Dissolve(0.2)

    voice audio.svante_ch10_line29  # transcript: "I'm with Magnus. I haven't"
    svante "I'm with Magnus. I haven't seen clones before. But I know he's not one. He's real to me. Maybe the Yaoguai King was just trying to mess with your head."

    hide yuxuan
    show niko normal_base at left_char with Dissolve(0.2)

    voice audio.niko_ch10_line9  # transcript: "I highly doubt that. Normally"
    niko   "I highly doubt that. Normally, I'd call it blasphemy outright. But considering that the Prosperity Dragon is involved with this... it aligns. All too well."

    hide svante
    show chunghee normal_neutral at right_char with Dissolve(0.2)

    voice audio.chung_ch10_line11  # transcript: "If what you're saying is"
    chung_hee "If what you're saying is true, I can take Magnus back to Kyeongjang with me. If he really is the Divine Weapon, we can't risk him falling into King Gustav's hands."
    hide chunghee
    show svante normal_base at right_char with Dissolve(0.2)
    voice audio.svante_ch10_line30  # transcript: "My father would never harm"
    svante "My father would never harm Magnus. He has merciful and kind tendencies! I don't think he'll want to doom us all."

    scene lab_cave_on 
    show elias normal_happy at left_char_kids 
    show tedda_human at center_char
    show tim happy at right_char_kids
    with Dissolve(0.2)

    voice audio.elias_ch10_line2
    elias  "Ooh! Can I come? I wanna go to Kongjong!"
    voice audio.tim_ch10_line1  # transcript: "I'd be honored to visit"
    tim    "I'd be honored to visit Kyeongjang!"
    tedda  "ME THREE! I WANNA GO TOOOO!"
    hide tedda_human
    hide tim
    hide elias
    show weng normal at right_flip 
    show roboto happy at left_robot
    with Dissolve(0.2)
    weng   "Kids, hush now. Don't interrupt the adults. Roboto, could you get them some snacks before they break my back and my nerves?"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep
    voice audio.roboto_ch10_line9  # transcript: "Right away, Miss Wayne! Snacks"
    roboto "R-R-R-Right away, Miss Weng. Snacks incoming."

    scene lab_cave_on 
    show dorian serious at left_char
    show niko alt_base at right_char
    show yuxuan normal_neutral at center_char
    with Dissolve(0.2)

    voice audio.dorian_ch10_line16  # transcript: "We need answers first, Chong."
    dorian "We need answers first, Chung. We need to know why the Divine Weapon was created. What its purpose is. Who it was meant to destroy-or protect."
    voice audio.niko_ch10_line10  # transcript: "to think they caged the"
    niko   "To think they caged the reincarnation of the Death God for four hundred years. Encased in some wretched contraption like a tool, a thing!"
    show niko normal_anger at right_char with Dissolve(0.1)
    voice audio.niko_ch10_line11  # transcript: "Have the great kings of"
    niko   "Have the great kings of Ena know no shame? Enoch weeps for what they've done! Heresy! Apostasy! No amount of gilded temples will cleanse that sin!"
    show yuxuan alt_think at center_char with Dissolve(0.1)
    voice audio.yuxuan_ch10_line15  # transcript: "Calm down Nico Calm down"
    yuxuan "Calm down, Niko. Calm down."
    voice audio.dorian_ch10_line17  # transcript: "The Yaguay King said he"
    dorian "The Yaoguai King said... he overheard two rulers speaking about it. King Long Shen of Tianho. And King Tatsuya Fujiwara of Hinami."

    hide niko
    show roboto happy at right_robot with Dissolve(0.2)
    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep
    voice audio.roboto_ch10_line10
    roboto "U-Unfortunately, K-K-King Long Shen has long been deceased. No further logs are available on his activities."

    voice audio.yuxuan_ch10_line16  # transcript: "Then we turn to the"
    yuxuan "Then we turn to the other. King Tatsuya of Hinami."

    "I looked down, my fists tight."
    
    show dorian neutral at left_char with Dissolve(0.2)

    voice audio.dorian_ch10_line18  # transcript: "I need to go. But..."
    dorian "I need to go. But... after everything that's happened, I don't think I want to go alone. Will some of you come with me?"

    "Chung-hee placed a hand on my shoulder."
    hide roboto
    show chunghee normal_neutral at right_char 
    show yuxuan normal_neutral at center_char
    with Dissolve(0.2)
    
    voice audio.chung_ch10_line12  # transcript: "You have me, Dorian. I'd"
    chung_hee "You have me, Dorian. I'd use the Amulet of Teleportation, but it's only stable for one person at a time. We'll need another route."

    show tim happy at right_char_kids with Dissolve(0.2)
    voice audio.tim_ch10_line2  # transcript: "I volunteer. I may be"
    tim   "I volunteer! I may be small, but I can catalog everything! Diplomats always bring scholars."

    show elias normal_happy at left_char_kids with Dissolve(0.2)
    voice audio.elias_ch10_line3  # transcript: "Daddy, I wanna come too!"
    elias "Daddy I wanna come too! I wanna go swimmwing!"

    "I winced. The thought of them anywhere near danger twisted in my gut like a blade."

    voice audio.dorian_ch10_line19  # transcript: "Elias, Tim, I'm sorry. It's"
    dorian "Elias... Tim... I'm sorry. It's too dangerous. You'll have to stay here where it's safe."

    hide chunghee
    hide tim
    hide elias
    show weng normal at right_flip with Dissolve(0.2)
    weng   "That's final. Listen to the adults, little ones. Tim, you stay here and play with Elias. There's plenty of adventure in stories and sweets."

    hide weng
    show tim sad at right_char_kids with Dissolve(0.1)
    voice audio.tim_ch10_line3  # transcript: "What? But I wanted to"
    tim    "WHAAAT?! But I wanted to wear my sailor hat!!"

    show yuxuan normal_happy at center_char with Dissolve(0.1)
    voice audio.yuxuan_ch10_line17  # transcript: "Luckily for all of us,"
    yuxuan "Luckily for all of us-I have just the thing. A luxury boat, custom-built, smooth as silk and fast as wind. Enough beds for everyone, even Tedda. And the kitchen makes warm bao buns on demand."

    hide tim
    show tedda_human at right_char with Dissolve(0.2)
    tedda  "Yeyyy!! Does that mean I'll be coming along?"

    hide tedda_human
    show roboto happy at right_robot with Dissolve(0.2)
    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep
    voice audio.roboto_ch10_line11  # transcript: "No, Miss Detta! You'll stay"
    roboto "No, Miss Tedda. You'll stay in the lab and c-c-c-clean up after Lady Elias. And maybe assist in kitchen duties if you don't burn rice again."

    hide roboto
    show tedda_human at right_char with Dissolve(0.1)
    tedda  "Aww boo..."

    hide tedda_human
    show niko normal_base at right_char with Dissolve(0.2)
    voice audio.niko_ch10_line12  # transcript: "Dorian, you'll need someone who"
    niko   "Dorian, you'll need someone who knows the island. I'll go. For Enoch. And for the truth they've long buried."

    hide yuxuan
    show magnus normal at center_char with Dissolve(0.2)

    "Magnus looked up from where he sat-his carefree demeanor dimmed. His eyes serious now, thoughtful."

    voice audio.magnus_ch10_line10  # transcript: "I... I'll go. I need"
    magnus "I... I'll go. I need to know who I really am. I need to understand what this 'Divine Weapon' means."

    hide niko
    show svante normal_base at right_char with Dissolve(0.2)
    voice audio.svante_ch10_line31  # transcript: "I'm happy for you Magnus."
    svante "I'm happy for you, Magnus. This will be a step in knowing who you actually are."
    voice audio.magnus_ch10_line11  # transcript: "Thank you, Swant."
    magnus "Thank you, Svante."
    voice audio.svante_ch10_line32  # transcript: "I'm also in. I've never"
    svante "I'm also in. I've never been to Hinami before, and honestly? I wanna see the beaches."
    voice audio.magnus_ch10_line12  # transcript: "Wait, beaches?"
    magnus "Wait... beaches?"

    hide svante
    show roboto happy at right_char with Dissolve(0.2)
    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep
    voice audio.roboto_ch10_line12  # transcript: "Yes, Hinami's coastal line is"
    roboto "Yes. Hinami's coastal line is considered one of the most breathtaking in all Ena. T-T-Turquoise waters. Shimmering white sand."
    voice audio.roboto_ch10_line13  # transcript: "Crystal clear coves and the"
    roboto "Crystal-clear coves. And the sunsets? Like fire melting into the sea. P-P-P-People write poetry about it. Some even propose there."

    show magnus alt_shocked at center_char with Dissolve(0.1)
    voice audio.magnus_ch10_line13  # transcript: "Woohoo! Beach trip! Let's go"
    magnus "WOOHOO!!! BEACH TRIP!!! Let's go swimming!!"

    hide roboto
    show niko normal_base at right_char with Dissolve(0.1)
    voice audio.niko_ch10_line13  # transcript: "Oh, brother!"
    niko   "Oh brother."

    show magnus normal at center_char with Dissolve(0.1)
    voice audio.magnus_ch10_line14  # transcript: "Spawned, let's go swimming once"
    magnus "Svante! Let's go swimming once we're there!"

    hide niko
    show svante normal_happy at right_char with Dissolve(0.1)
    voice audio.svante_ch10_line33  # transcript: "Of course! We probably deserve"
    svante "Of course! We probably deserve a little sun! I remember me and my fellow aldoriths bathing in the waterfall in Mjoll! I can't imagine swimming in a beach! It must be fun!"

    hide magnus
    show yuxuan normal_lying at center_char with Dissolve(0.1)
    voice audio.yuxuan_ch10_line18  # transcript: "Everyone please, this isn't vacation"
    yuxuan "Everyone, please! This isn't vacation time, we-"

    "Magnus leaned over and whispered something."

    yuxuan "D-D-Dorian in... "
    voice audio.magnus_ch10_line15
    magnus "Absolutely..."
    show yuxuan normal_happy at center_char with Dissolve(0.1)
    voice yuxuan_ch10_line20
    yuxuan "I-I-I CHANGE MY MIND! Everyone pack your swimwear!!"

    hide svante
    show niko normal_smile at right_char with Dissolve(0.1)
    voice audio.niko_ch10_line14  # transcript: "Well, if the opportunity arises,"
    niko   "Well, if the opportunity arises, I suppose a little dip wouldn't hurt. Hinami does have quite a few resorts, after all."

    hide dorian
    show svante normal_happy at left_char with Dissolve(0.1)
    voice audio.svante_ch10_line34  # transcript: "A white sandy beach. Is"
    svante "A white sandy beach... Is it really that beautiful?"

    voice audio.niko_ch10_line15
    niko   "As someone born there... yes. The beaches of Hinami are magic made real. Waters that glow under moonlight. Tide pools with starfish that shimmer."
    voice audio.niko_ch10_line16  # transcript: "They don't exaggerate, it is"
    niko   "They don't exaggerate. It is beautiful. And the castle of Hinami? It floats upon the sea itself."
    voice audio.yuxuan_ch10_line21  # transcript: "What? How do they do"
    yuxuan "What? How do they do that?"
    voice audio.niko_ch10_line17  # transcript: "Water-channlers, probably empowered by the"
    niko   "Water channelers. Probably empowered by the Dragon of the Depths... or some ancient art lost to time. Nobody really knows."

    hide niko
    show magnus normal at right_char with Dissolve(0.1)
    voice audio.magnus_ch10_line16  # transcript: "I can't wait. Nami, here"
    magnus "I can't wait! Hinami, here we come!"

    hide magnus
    hide svante
    show tim think at right_char_kids
    show elias normal_mad at left_char_kids
    with Dissolve(0.1)
    voice audio.elias_ch10_line4  # transcript: "No fly daddy! Huh! That's"
    elias  "No faiw!! Daddy!! That's so unfaiw!!"

    voice audio.tim_ch10_line4  # transcript: "Elias, maybe it's time for"
    tim    "Elias... maybe it's time for Operation: Sneak-Aboard. Listen carefully. Here's the plan-"
    "Chung-hee approached me, rubbing his temples."

    scene lab_cave_on
    show dorian neutral at left_char
    show chunghee normal_neutral at right_char
    with Dissolve(0.2)

    voice audio.chung_ch10_line13  # transcript: "Well, these people sure are"
    chung_hee "Well... these people sure are excited."
    voice audio.dorian_ch10_line20  # transcript: "Tell me about it."
    dorian    "Tell me about it..."

    hide yuxuan
    show weng normal at center_char with Dissolve(0.2)
    weng      "Don't worry, Sir Dorian. I'll take care of Elias. He'll be safe here-with Tim, Tedda, and Roboto. He'll be happy."
    voice audio.chung_ch10_line14  # transcript: "I'm sorry you're not feeling"
    chung_hee "I'm sorry you're not feeling well enough to join us, Miss Weng."
    weng      "It's alright, sir Chung. I'll be fine here with the little ones. A good cup of tea and some poetry by Takayori Sogen will keep me company."
    voice audio.chung_ch10_line15  # transcript: "That's it everyone. We leave"
    chung_hee "That's it, everyone. We leave at first light. Prepare yourselves."
    scene lab_cave_on with Dissolve(0.2)
    "And just like that, the decision was made."
    "Tomorrow-we set sail. "
    "To Hinami."

    scene black with fade
    stop music fadeout 1.0
    stop sound 
    pause 3.0
    jump credit_roll


# =============================================================================
# SECTION 28: LABEL CH10_CREDITS_SCENE — End Credits Scene: Gustav / Cyrus
# =============================================================================

label ch10_credits_scene:

    scene black with fade
    stop music fadeout 2.0
    pause 2.0

    scene destroyed_land with fade
    pause 3.0
    # play music ost_ch10_credits fadein 2.0      # PLACEHOLDER — ominous credits theme
    # play sound sfx_carriage_rumble              # PLACEHOLDER — carriage rumble SFX
    scene yuxuan_carriage
    show king_gustav at left_char
    show cyrus at right_char
    with Dissolve(0.75)

    "The imperial carriage rumbled down the muddy trail, wheels slick with rainwater."    
    play sound audio.sfx_eruption 
    "Thunder cracked in the distance, the sky bruised with approaching storm."

    voice audio.gustav_ch10_line17
    king_gustav "Damn that Yaoguai attack. Everything has to fall apart the moment I take a detour."
    voice audio.cyrus_ch10_line1  # transcript: "You seem surprised, Gustav. Monsters"
    cyrus "You seem surprised, Gustav. Monsters rarely wait their turn."
    voice audio.cyrus_ch10_line2  # transcript: "Besides, you'll be inside the"
    cyrus "Besides, you'll be inside the comfort of your castle soon."

    "The carriage lurched slightly. A knock sounded. The door creaked open to reveal three kneeling figures-hooded Aldoriths, rain dripping from their cloaks."

    show boy_ald_normal at center_char with Dissolve(0.2)

    boy_ald "Father... we are humbly asking for your permission to-"
    voice audio.cyrus_ch10_line3  # transcript: "Can't you see he is"
    cyrus   "CAN'T YOU SEE HE IS TALKING TO ME?!"
    boy_ald "F-Forgive us..."
    voice audio.gustav_ch10_line18  # transcript: "Cyrus, calm yourself. It's alright."
    king_gustav "Cyrus. Calm yourself. It's alright... My children, speak."
    boy_ald "Thank you Father. I appreciate your kindness."

    hide boy_ald_normal
    show girl_ald_normal at center_char with Dissolve(0.2)
    voice audio.girl_ald_ch10_line2
    girl_ald "Father, forgive the intrusion. We bring urgent news."

    hide girl_ald_normal
    show boy_ald_normal at center_char with Dissolve(0.2)
    boy_ald "We found him. Our brother... Svante. He lives."

    "King Gustav's eyes narrowed, tension rising in his shoulders."

    hide boy_ald_normal
    show girl_ald_normal at center_char with Dissolve(0.2)
    voice audio.girl_ald_ch10_line3
    girl_ald "We wished to bring him to you... but..."

    voice audio.gustav_ch10_line19  # transcript: "But what?"
    king_gustav "But what?"

    voice audio.girl_ald_ch10_line4
    girl_ald "He is not alone. He travels with others. A man named Dorian... and others whose names we don't know."
    voice audio.gustav_ch10_line20  # transcript: "Durian, what?"
    king_gustav "Dorian?! What?!"

    hide girl_ald_normal
    show boy_ald_normal at center_char with Dissolve(0.2)
    boy_ald "There is also one who is called Magnus."

    voice audio.gustav_ch10_line21  # transcript: "Magnus."
    king_gustav "Magnus?"

    boy_ald "Yes, Father. He has wings. And he burns with light."

    hide boy_ald_normal
    show mjoll_soldier_1 at center_char with Dissolve(0.2)
    mjoll_lars "We compared your past descriptions, Father. The signs match."

    hide mjoll_soldier_1
    show mjoll_soldier_female_1 at center_char with Dissolve(0.2)
    voice audio.helga_ch10_line1
    mjoll_helga "According to your descriptions, we believe he's the Divine Weapon."

    voice audio.cyrus_ch10_line4  # transcript: "And? Are you certain of"
    cyrus "And? Are you certain of this information? We don't tolerate false information."
    voice audio.helga_ch10_line2
    mjoll_helga "As certain as breath and bone, Paladin Cyrus."

    hide mjoll_soldier_female_1
    show mjoll_soldier_1 at center_char with Dissolve(0.2)
    mjoll_lars "We also inspected the sealed chamber, as you taught us. The seal was ultimately broken."
    mjoll_lars "The area was in utter disarray. Scorched stone. Scattered feathers. A battle, by all signs."

    voice audio.cyrus_ch10_line5  # transcript: "Torian and Magnus. Interesting."
    cyrus "Dorian and Magnus... Interesting."

    voice audio.gustav_ch10_line22
    king_gustav "Enoch above... The Divine Weapon."

    "A long silence fell, punctuated only by the rolling wheels and distant thunder."

    hide mjoll_soldier_1
    show girl_ald_normal at center_char with Dissolve(0.2)
    voice audio.girl_ald_ch10_line5
    girl_ald "Our agents in Tianho saw them together... just yesterday."

    voice audio.gustav_ch10_line23  # transcript: "Insolence! You took too long"
    king_gustav "INSOLENCE! You took too long to report this! TURN THE DAMN CARRIAGE AROUND! I want to-"
    voice audio.cyrus_ch10_line6  # transcript: "Back to Tionhu. Don't bother."
    cyrus "Back to Tianho? Don't bother. You'll only be wasting your time, Gustav."
    voice audio.gustav_ch10_line24  # transcript: "You think there's nothing to"
    king_gustav "You think they're not in Tianho anymore?"
    voice audio.cyrus_ch10_line7  # transcript: "No, they're not. I feel"
    cyrus "No, they're not. I feel it. A pull in my blood. In my bones."
    voice audio.cyrus_ch10_line8  # transcript: "They're either headed towards the"
    cyrus "They're either headed towards the Empire of Gale or the Island of Hinami."
    voice audio.cyrus_ch10_line9  # transcript: "But if I were to"
    cyrus "But if I were to bet my coin, I'd place it on Hinami."

    hide girl_ald_normal
    show mjoll_soldier_female_1 at center_char with Dissolve(0.2)
    voice audio.helga_ch10_line3
    mjoll_helga "But... Paladin. Forgive me-but the ferries bound for Hinami are booked solid because of the festivities of the anniversary of the tragedy."

    hide mjoll_soldier_female_1
    show mjoll_soldier_1 at center_char with Dissolve(0.2)
    mjoll_lars  "Helga, stop questioning the Paladin."

    hide mjoll_soldier_1
    show mjoll_soldier_female_1 at center_char with Dissolve(0.2)
    voice audio.helga_ch10_line4
    mjoll_helga "I'm not, Lars! But there's no passage left for them to go to the Kingdom of Hinami! We-"

    voice audio.cyrus_ch10_line10  # transcript: "Then that narrows it down."
    cyrus "Then that narrows it down. Who in Tianho is powerful or influential enough to reach the Island of Hinami without needing a ferry?"

    "He leaned forward slightly."

    voice audio.cyrus_ch10_line11  # transcript: "Tell me, Gustav, which king"
    cyrus "Tell me, Gustav. Which king failed to attend the rulers' meeting during the Tragedy of Tianho?"

    voice audio.gustav_ch10_line25
    king_gustav "Tatsuya..."

    "King Gustav froze."

    voice audio.gustav_ch10_line26
    king_gustav "Hinami..."

    scene black with fade
    stop music fadeout 3.0
    pause 5.0

    "Back up this save before finishing. Thank you for playing."

    $ MainMenu(confirm=False)()
    return


# =============================================================================
# SECTION 29: LABEL CH10_BAD_END_CREDITS — GAME OVER / BAD END Credits
# =============================================================================

label ch10_bad_end_credits:

    stop music fadeout 1.0
    play music audio.ost_tragedy fadein 1.0      # PLACEHOLDER — bad end music

    prosperity_dragon "The savior is gone. The one who could have rescued Ena lies dead."

    "The dragon's massive head lowered, smoke billowing from its nostrils as it turned its gaze to the horizon, where darkness gathered like a storm."

    prosperity_dragon "And now... who will save them?"

    "The land of Ena lay silent, its fate uncertain. The savior-its last hope-was gone."

    jump game_over
    stop music fadeout 3.0
    pause 2.0

    return


# =============================================================================
# END OF CHAPTER 10
# =============================================================================


# ============================================================
# CH10 CREDITS ROLL — unskippable except via Space
# ============================================================

# ============================================================
# CH10 CREDITS ROLL — unskippable except via Space
# ============================================================

# init python:
#     CREDITS_SCROLL_DURATION = 35.0  # TODO: tune to match how long your credit list takes to read comfortably

# transform credits_scroll_up:
#     yanchor 1.0       # Anchor the text box by its bottom edge
#     ypos 0.5          # The target destination is the center of the screen
#     yoffset 2500      # Start pushed 2500 pixels down (completely hidden off the bottom of the screen)
#     linear CREDITS_SCROLL_DURATION yoffset 0  # Scroll upwards until yoffset is 0 (stops at center)

# screen credits_roll():
#     modal True
#     zorder 200

#     # solid black background
#     add Solid("#000000")

#     # ---------------- input locking ----------------
#     # block every normal way of advancing/exiting a screen
#     key "game_menu" action NullAction()
#     key "hide_windows" action NullAction()
#     key "rollback" action NullAction()
#     key "rollforward" action NullAction()
#     key "skip" action NullAction()

#     # the only way out - press Space
#     key "K_SPACE" action [Hide("credits_roll", transition=Dissolve(1.5)), Jump("ch10_credits_scene")]

#     # invisible fullscreen button - swallows every click so nothing
#     # underneath can be triggered and the screen itself can't be
#     # dismissed by clicking
#     button:
#         xfill True
#         yfill True
#         background None
#         action NullAction()

#     # ---------------- scrolling credit text ----------------
#     vbox:
#         at credits_scroll_up
#         xalign 0.5
#         spacing 40

#         # TODO: placeholder - swap for the real logo asset path/size
#         add "dh_logo":
#             xalign 0.5
#             zoom 0.8
#         text " " size 60

#         text "DRAGON'S HEART: Crimson Rebirth" size 70 color "#ffffff" xalign 0.5 text_align 0.5 bold True
#         text "by Temers Studio" size 40 xalign 0.5 text_align 0.5
#         text " " size 60

#         text "Written & Directed by" size 30 color "#999999" xalign 0.5 text_align 0.5
#         text "ICO" size 42 color "#ffffff" xalign 0.5 text_align 0.5
#         # text " " size 40

#         text "Sprite Artists" size 30 color "#999999" xalign 0.5 text_align 0.5
#         text "----------" size 42 color "#ffffff" xalign 0.5 text_align 0.5
#         # text " " size 40

#         text "Background Artists" size 30 color "#999999" xalign 0.5 text_align 0.5
#         text "----------" size 42 color "#ffffff" xalign 0.5 text_align 0.5
#         text " " size 40

#         text "Music & Composition" size 30 color "#999999" xalign 0.5 text_align 0.5
#         text "---------- " size 42 color "#ffffff" xalign 0.5 text_align 0.5
#         text " " size 40

#         text "Programming" size 30 color "#999999" xalign 0.5 text_align 0.5
#         text "yondel__" size 42 color "#ffffff" xalign 0.5 text_align 0.5
#         text " " size 40

#         text "Character VAs" size 30 color "#999999" xalign 0.5 text_align 0.5
#         text "----------" size 42 color "#ffffff" xalign 0.5 text_align 0.5
#         text " " size 40
#         # text " " size 40
#         # text "Character Name" size 42 color "#ffffff" xalign 0.5 text_align 0.5
#         # text "*insert va" size 40 color "#ffffff" xalign 0.5 text_align 0.5 # TODO: VA LIST

#         # ── Assets Used ──
#         text "Assets Used" size 30 color "#999999" xalign 0.5 text_align 0.5
#         text "Tavern art by Maethavee.Kay'E on ArtStation" size 38 color "#ffffff" xalign 0.5 text_align 0.5
#         text "Library by Vui Huynh" size 38 color "#ffffff" xalign 0.5 text_align 0.5
#         text "Ice Monster art by Kvasir501 on Twitter" size 38 color "#ffffff" xalign 0.5 text_align 0.5
#         text "Tianho Throne room by Background Kit (Webtoon blanks)" size 38 color "#ffffff" xalign 0.5 text_align 0.5
#         text " " size 40

#         # ── Modules & Plugins ──
#         text "Modules & Plugins" size 30 color "#999999" xalign 0.5 text_align 0.5
#         text "Kinetic Text Tags by Daniel Westfall/@sodara9 on Twitter" size 38 color "#ffffff" xalign 0.5 text_align 0.5
#         text "Wave Shader Ren'Py Module 2022 by Daniel Westfall" size 38 color "#ffffff" xalign 0.5 text_align 0.5
#         text "Shattered Glass by Maurimo" size 38 color "#ffffff" xalign 0.5 text_align 0.5
#         text "Easy Renpy GUI by Feniks" size 38 color "#ffffff" xalign 0.5 text_align 0.5
#         text "Immersive Particles by Feniks" size 38 color "#ffffff" xalign 0.5 text_align 0.5
#         text " " size 40
        
#         text "Special Thanks" size 30 color "#999999" xalign 0.5 text_align 0.5
#         text "----------" size 42 color "#ffffff" xalign 0.5 text_align 0.5
#         text " " size 100
#         text "And most importantly, to you our dear player.\nIt was because of you who made this possible. " size 36 color "#e8d9b0" xalign 0.5 text_align 0.5
#         text "Thank you for playing Dragon's Heart and supporting Temers Studio. \nIt has been an honor making this game and we hope for your \ncontinued support on the studio's future endevours.\n.\n.\n\." size 36 color "#e8d9b0" xalign 0.5 text_align 0.5
#         text "\n---------- " size 42 xalign 0.5 text_align 0.5
#         text "\n----------" size 42 xalign 0.5 text_align 0.5
#         text "\n----------" size 42 xalign 0.5 text_align 0.5

#     # small skip hint, tucked in the corner, always visible
#     text "Press SPACE to skip":
#         xpos 30
#         ypos 1050
#         size 22
#         color "#777777"

#     # auto-continue once the scroll finishes on its own + 3 seconds of pause
#     timer (CREDITS_SCROLL_DURATION + 3.0) action [Hide("credits_roll", transition=Dissolve(1.5)), Jump("ch10_credits_scene")]


# label credit_roll:
#     play music audio.main_theme fadein 0.5
#     show screen credits_roll
#     with Dissolve(1.5)
#     $ ui.interact()

#     return

# ============================================================
# CH10 CREDITS ROLL — unskippable except via Space
# ============================================================

init python:
    CREDITS_SCROLL_DURATION = 75.0  # TODO: tune to match how long your credit list takes to read comfortably

transform credits_scroll_up:
    yanchor 0.0
    ypos 1.0
    linear CREDITS_SCROLL_DURATION ypos -3.0

screen credits_roll():
    modal True
    zorder 200

    # solid black background
    add Solid("#000000")

    # ---------------- input locking ----------------
    # block every normal way of advancing/exiting a screen
    key "game_menu" action NullAction()
    key "hide_windows" action NullAction()
    key "rollback" action NullAction()
    key "rollforward" action NullAction()
    key "skip" action NullAction()

    # the only way out - press Space
    key "K_SPACE" action [Hide("credits_roll", transition=Dissolve(1.5)), Jump("ch10_credits_scene")]

    # invisible fullscreen button - swallows every click so nothing
    # underneath can be triggered and the screen itself can't be
    # dismissed by clicking
    button:
        xfill True
        yfill True
        background None
        action NullAction()

    # ---------------- scrolling credit text ----------------
    vbox:
        at credits_scroll_up
        xalign 0.5
        spacing 40

        # TODO: placeholder - swap for the real logo asset path/size
        add "dh_logo":
            xalign 0.5
            zoom 0.8
        text " " size 60

        text "DRAGON'S HEART: Crimson Rebirth" size 70 color "#ffffff" xalign 0.5 text_align 0.5 bold True
        text "by Temers Studio" size 40 xalign 0.5 text_align 0.5
        text " " size 60

        text "Written & Directed by" size 30 color "#999999" xalign 0.5 text_align 0.5
        text "ICO" size 42 color "#ffffff" xalign 0.5 text_align 0.5
        # text " " size 40

        text "Sprite Artists" size 30 color "#999999" xalign 0.5 text_align 0.5
        text "----------" size 42 color "#ffffff" xalign 0.5 text_align 0.5
        # text " " size 40

        text "Background Artists" size 30 color "#999999" xalign 0.5 text_align 0.5
        text "----------" size 42 color "#ffffff" xalign 0.5 text_align 0.5
        text " " size 40

        text "Music & Composition" size 30 color "#999999" xalign 0.5 text_align 0.5
        text "---------- " size 42 color "#ffffff" xalign 0.5 text_align 0.5
        text " " size 40

        text "Programming" size 30 color "#999999" xalign 0.5 text_align 0.5
        text "yondel__" size 42 color "#ffffff" xalign 0.5 text_align 0.5
        text " " size 40

        text "Character VAs" size 30 color "#999999" xalign 0.5 text_align 0.5
        text "----------" size 42 color "#ffffff" xalign 0.5 text_align 0.5
        text " " size 40
        # text " " size 40
        # text "Character Name" size 42 color "#ffffff" xalign 0.5 text_align 0.5
        # text "*insert va" size 40 color "#ffffff" xalign 0.5 text_align 0.5 # TODO: VA LIST

        # ── Assets Used ──
        text "Assets Used" size 30 color "#999999" xalign 0.5 text_align 0.5
        text "Tavern art by Maethavee.Kay'E on ArtStation" size 38 color "#ffffff" xalign 0.5 text_align 0.5
        text "Library by Vui Huynh" size 38 color "#ffffff" xalign 0.5 text_align 0.5
        text "Ice Monster art by Kvasir501 on Twitter" size 38 color "#ffffff" xalign 0.5 text_align 0.5
        text "Tianho Throne room by Background Kit (Webtoon blanks)" size 38 color "#ffffff" xalign 0.5 text_align 0.5
        text " " size 40

        # ── Modules & Plugins ──
        text "Modules & Plugins" size 30 color "#999999" xalign 0.5 text_align 0.5
        text "Kinetic Text Tags by Daniel Westfall/@sodara9 on Twitter" size 38 color "#ffffff" xalign 0.5 text_align 0.5
        text "Wave Shader Ren'Py Module 2022 by Daniel Westfall" size 38 color "#ffffff" xalign 0.5 text_align 0.5
        text "Shattered Glass by Maurimo" size 38 color "#ffffff" xalign 0.5 text_align 0.5
        text "Easy Renpy GUI by Feniks" size 38 color "#ffffff" xalign 0.5 text_align 0.5
        text "Immersive Particles by Feniks" size 38 color "#ffffff" xalign 0.5 text_align 0.5
        text " " size 40
        
        text "Special Thanks" size 30 color "#999999" xalign 0.5 text_align 0.5
        text "----------" size 42 color "#ffffff" xalign 0.5 text_align 0.5
        text " " size 100
        text "And most importantly, to you our dear player.\nIt was because of you who made this possible. " size 36 color "#e8d9b0" xalign 0.5 text_align 0.5
        text "Thank you for playing Dragon's Heart and supporting Temers Studio. \nIt has been an honor making this game and we hope for your \ncontinued support on the studio's future endevours.\n.\n.\n\." size 36 color "#e8d9b0" xalign 0.5 text_align 0.5
        text "\n---------- " size 42
        text "\n----------" size 42
        text "\n----------" size 42
    # small skip hint, tucked in the corner, always visible
    text "Press SPACE to skip":
        xpos 30
        ypos 1050
        size 22
        color "#777777"

    # auto-continue once the scroll finishes on its own, in case the
    # player never presses Space
    timer CREDITS_SCROLL_DURATION action [Hide("credits_roll", transition=Dissolve(1.5)), Jump("ch10_credits_scene")]


label credit_roll:
    play music audio.main_theme fadein 0.5
    show screen credits_roll
    with Dissolve(1.5)
    $ ui.interact()

    return