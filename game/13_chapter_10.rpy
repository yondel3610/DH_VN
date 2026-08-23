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
# define audio.sfx_claws           = "audio/sfx/sfx_claws.ogg"                # PLACEHOLDER
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
    scene plain_white with fade
    play music ost_ch10_dream fadein 2.0        # PLACEHOLDER — dream theme

    show screen chapter_title_screen(
        "10",
        "The Yaoguai King's Deal",
        subtitle="Tianho — The Sealed Chamber",
        duration=3.0
    )
    pause 3.0

    "A warm light shimmered behind my eyelids."
    "Then a voice-familiar, gentle, ancient, and layered with celestial resonance-whispered through the void."

    prosperity_dragon "Child... Listen to me..."
    prosperity_dragon "My child..."

    "But just as I reached toward her-"
    "Darkness."
    "The warmth was ripped away, swallowed by the cold. The world twisted into shadows. A heavy footstep echoed."
    "The air turned acrid."

    yk "Dragonkin..."

    "I spun around."

    play music ost_ch10_yaoguai_deal fadein 0.5 # PLACEHOLDER — Yaoguai King theme

    show yk at center_char with Dissolve(0.2)

    yk "They sleep. Exhausted. Vulnerable. That ridiculous ceremony drained them. Their warriors lie scattered, half-drunk on memory. Tianho is wide open."

    "He raised a clawed hand, and behind him, silhouettes moved-legions of yaoguai hidden in the folds of night. Waiting."

    yk "Before dawn, we strike. At their armies... at their soul. Their schools. Their homes. Their children."
    yk "Let them mourn again. Let them remember anew."
    dorian "You monster!! What do you want?!"

    "He tilted his head, lips curling."

    yk "A deal. An agreement."
    yk "Give me Magnus. Give me the winged man's unconscious body."
    yk "Do that... and Tianho lives. No blood. No fire. No screams. Just peace."
    yk "Refuse..."
    yk "And mark my words-Tianho will be ash before the sun rises."
    dorian "You wouldn't dare-"

    "The Yaoguai King's eyes glinted-then he raised one jagged claw."

    yk "You doubt me? Fine. See for yourself."

    "He snapped his fingers."
    "Visions flooded my mind, like a dam had burst inside my skull. Horrifyingly vivid:"
    "Yaoguai tearing through Tianho's sleeping streets-claws raking silk robes, teeth sinking into flesh. Fire against moonlight. Screams. A mother trying to shield her baby with trembling hands before her head ripped apart."
    "A soldier barely awake before teeth pierced his side. Children trampled in panic. Houses ablaze. Memorial lanterns crushed. I felt the people's agony."
    "The pain was unbearable."
    "When the vision snapped away, I nearly collapsed."

    yk "Now you understand. Make your decision, dragonkin..."

    "I steadied myself, heart pounding like a war drum."

    dorian "I... I need time. To think."
    yk "There is no time. You will choose here and now. The second you say no... they move."

    "My mind whirled-and then, I heard the familiar voice again."

    prosperity_dragon "I sense him... He's getting desperate. Impatient. His armies WILL attack Tianho."

    "My blood burned."
    "Rage-bitter, ancient-surged up. This monster."
    "He killed Elara."
    "He killed my children."
    "Their faces-gone too soon, smiling in dreams I could never have again. And now he wanted more?"
    "And then I heard it."
    "Elias' voice, giggling under fireworks. Tim spinning in the lanternlight. Weng's laugh. Yuxuan's smile. The people-my people."

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

    yk "I knew you were always going to say yes."

    "The Yaoguai King's lips twisted into a crooked smile-satisfied, smug, victorious. He raised a hand, and the shadows behind him dispersed like vapor. The threat was withdrawn."

    scene black with fade
    play music ost_ch10_bad_end fadein 1.0      # PLACEHOLDER — bad ending theme

    "Tianho would wake to another quiet morning. The streets would remain unburnt. Children would still laugh in the courtyards. No one would know how close they came to death."
    "But the cost..."
    "Magnus was taken, unconscious and bound in chains. I wasn't allowed to see his face. Not a word, not a goodbye."
    "The Prosperity Dragon's voice fell into silence. It did not return. It left me completely. Even its warmth was gone from my dreams. Its presence-snuffed out like a candle in deep water."
    "Days passed. Then weeks. Then-the world began to crumble. We heard the whispers first."

    scene mjoll_palace_throne_lightsoff with dissolve

    "Mjoll, the northern realm of snow and light, was the first to fall."
    "They said the mountains cracked open, that black mist spilled from the earth, and creatures with no mouths and too many eyes swept through the villages. The screams were swallowed. The snow ran red."
    "Hinami, Gale, the Centennial Isles, all of them destroyed by yaoguai."
    "But Tianho... Tianho remained untouched. Exactly as he promised. Perfectly, horrifically untouched. We had no contact with other nations. Not that we had a choice. There was no one left to contact. People began to leave. Not to run... just to fade."
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

    dorian "Never."

    "The word left my mouth like thunder-final and resolute."
    "The Yaoguai King's expression shifted. No longer smug. No longer amused."
    "It twisted-wrath incarnate, as though my defiance was the deepest betrayal he'd ever known. A thick silence bloomed between us. It pulsed like a second heartbeat, dense and waiting."

    yk "Then so be it. Let them drown in fire."

    "He took a step forward, face inches from mine, his breath a rot of ash and centuries."

    yk "Remember this night. It will become legend. And the blood spilled will be on your hands, dragonkin."
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

    "I closed my eyes, my hands shaking."

    dorian "...Please. I don't know what to do."
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

    "Chace: But... love, come on! I barely know him!"
    "Isagani: You said he just turned fourteen a few days ago, love. Fourteen. And his mother just died trying to keep him from being deported. Don't you care what happens to Yevhen?"
    "Chace: Of course I care! It's just-I don't know how to be anything to him. He's just a half-sibling. I didn't even know my dad had another kid until days ago."
    "Isagani: Funny. That didn't stop you with Maja."
    "Chace: Don't bring her into this, love. She's different."
    "Isagani: How? Because she was already in your life? Because loving her didn't feel like a risk?"
    "Chace: Yevhen's just a kid. A scared, angry kid who definitely doesn't want anything to do with me."
    "Isagani: Then be the first person who doesn't walk away. Love, if you turn your back on him now... that's not the man I said yes to."
    "Storyteller: Find out what happens next... in the explosive sequel to-A Tropical-"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep

    show yuxuan normal_neutral at left_char
    show niko normal_base at right_char
    show svante normal_base at center_char
    with Dissolve(0.2)

    roboto "A-A-Audiodrama paused by M-M-Master Yuxuan."
    yuxuan "So... thoughts? Come on, I want honest feedback here!"
    niko   "For starters, I love the acting. The guy who played Chace was perfect for the role."
    svante "I-I agree! Even his younger voice! The way he cried... it brought tears to my eyes!"

    show magnus normal at right_char

    magnus "~Noel's voice... was heaven-sent... like silk, like rain, like sweet lament~"
    yuxuan "YES!! Roboto, take note of that. Praise from Magnus is a sign we're about to break the market!"

    show roboto normal at left_char

    roboto "N-N-Noted. Cheng Industries... preparing hit tracker update. Logging Magnus endorsem-m-ment."
    niko   "Great. *yawns* Are we done here? I'm late for prayer."
    yuxuan "Honestly, I think Isagani's voice is underrated too. So grounded. So real. But enough about my tastes, I-"

    hide niko
    hide svante
    hide magnus
    hide roboto
    show dorian normal_alt_tense at center_char with Dissolve(0.2)

    "And then... I stepped into the room, the weight of urgency pressing on my shoulders."

    dorian "They're coming."

    show magnus normal at right_char with Dissolve(0.2)

    magnus "Who?"

    "The room stilled. Every eye turned to me."

    dorian "The Yaoguai King has made his move. The attack has begun."
    yuxuan "Wait... w-what?"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep

    show roboto normal at left_char with Dissolve(0.2)

    roboto "I-I-Incoming threat? P-Please reconfirm?"
    dorian "There's no time. Tianho will be attacked under an hour."

    jump ch10_departure


# =============================================================================
# SECTION 10: LABEL CH10_DEPARTURE — Underground Door / Goodbye to Kids
# =============================================================================

label ch10_departure:

    scene spare_room with dissolve

    "We woke up everyone inside the underground lab-Chung-hee, Miss Weng, and the kids. Tedda quietly gathered Elias and Tim and led them into a single room, locking the door behind her to keep them safe."

    show tedda_human at center_char
    show elias sleepwear_neutral at left_char_kids
    show tim sleepwear_normal at right_char_kids
    with Dissolve(0.2)

    dorian      "Please... take care of Elias, Tedda."
    tedda_alive "Don't worry, Sir Dorian. I'll make sure Elias and Tim are safe. I'll lock the door."

    "They slept together in a pile of pillows."
    "The rest of us-me, Niko, Yuxuan, Chung-hee, Svante, Magnus, Miss Weng, and Roboto-hurried to the living room for a quick, urgent meeting."

    scene yuxuan_lab with dissolve

    show chunghee normal_neutral at left_char
    show magnus normal at right_char
    show yuxuan normal_neutral at center_char
    with Dissolve(0.2)

    chung_hee "Are you certain this is happening?"
    magnus    "I trust Dorian. That's enough for me."
    yuxuan    "It has to be that damned Yaoguai King. Probably the one who sent a doppelgänger to impersonate me! For all we know, anyone here could be fake!"
    chung_hee "Yuxuan, don't worry. I saw through each of your minds. We're all safe."
    yuxuan    "Oh... thank the Prosperity Dragon."
    dorian    "Yu, can you send a message to Gao and Jiang immediately? We need to reach Paladin Feng. If he's still at Tianho at this hour, he might be able to mobilize the other paladins in time."

    "Paladin Feng... My old friend. Once my closest ally. If he's still there, he'll act. He has to act."

    show svante normal_base at right_char
    show niko normal_base at left_char
    with Dissolve(0.2)

    svante "What about Lady Aoi? She's an incredible water channeler. She could make a huge difference."
    niko   "That is, if she's still in Tianho."
    svante "She sang during the festivities, right? That means she might still be nearby. Though... she might ask for compensation."
    weng   "Her song was beautiful! What a lovely young woman."
    magnus "Wait... she's the one who sang at the festival? AND she's an incredible water channeler?"
    svante "Yes! That's why Father hired her as a mercenary after Dorian. She deserted when Paladin Feng made a better offer."
    chung_hee "She deserted when she and Tian Xun failed to eliminate me. Anyway, let's just hope she's still working with Feng. If she is, we might have a fighting chance."
    yuxuan "Roboto, establish connection with Li Gao and Sun Jiang immediately!"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep

    show roboto normal at center_char with Dissolve(0.2)

    roboto "G-G-Got it, Master Yuxuan. Establishing connection in 3...2...1..."

    "The device crackled. A hologram shimmered to life-a flickering image of Jiang in his Cheng Industries uniform."

    jiang  "Good evening, sir Yuxuan. We're receiving your transmission. What's going on?"
    yuxuan "Yes, Jiang. This is a full-scale alert. Patch in Gao-now."
    jiang  "Right away, sir."
    yuxuan "Listen closely. There is no time for pleasantries. The Yaoguai are coming."
    gao    "Y-Yaoguai? What are they doing here?"
    jiang  "Gao, Paladin Feng is still here. I'm telling this to him now."
    jiang  "Anything else, Master Yuxuan?"
    yuxuan "Nothing else. Please, just tell Paladin Feng."
    jiang  "Yes, sir. Let's get to it, Gao. Hurry!"

    "The screen blinked out."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep

    roboto "C-C-Connection terminated, Master Yuxuan."

    $ feng_score += 1                           # +1 Feng alerted

    scene yuxuan_lab with dissolve

    show dorian normal_alt_tense at left_char
    show chunghee normal_neutral at right_char
    with Dissolve(0.2)

    "I exhaled, realizing I'd been holding my breath. The lab felt heavier now-like the walls themselves could sense what was coming."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep

    show roboto normal at center_char with Dissolve(0.2)

    roboto    "F-F-Fear levels in the room are fluctuating at 63%%. Suggesting calming ambient music-"
    chung_hee "If this happens tonight, we don't have long. We leave for Tianho now."
    svante    "We can set up a makeshift command post there. An hour's not enough to mount full defense-but we have to try."
    niko      "No more waiting. We move. Now."
    magnus    "Four hundred years, I slept in ice, and this is the week I wake to? Part of me thinks... maybe I was waiting for this."
    weng      "Roboto and I will stay behind to protect the kids. This lab's shielded, reinforced. It'll hold."

    "She snapped her fingers. A flame sparked in her palm, steady and sharp."

    show weng normal at right_char with Dissolve(0.2)

    weng      "Any yaoguai stupid enough to get through that door? I'll make sure they burn to ash."

    "A loud crack echoed from her spine as she stretched."

    magnus    "Such fire from a woman of iron and ember. But bones do not lie, Miss Weng."
    weng      "Oh shush, Magnus. Believe me, I've felled more enemies than I could count when I was your age."
    weng      "By the stars-getting old is not for the weak. Still... I trust the door holds. It always has."
    weng      "Roboto, be a dear and brew me a cup of tea, will you?"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep

    roboto "T-T-Take care, Masters! Please stay alive!"
    roboto "I'll make you a quick cup of tea, Miss W-W-Weng."

    scene underground_door with dissolve

    show magnus normal at left_char
    show niko normal_base at right_char
    show yuxuan normal_neutral at center_char
    with Dissolve(0.2)

    "We exited the door. The big metallic door for the underground laboratory closed."

    door_voice "Good evening, Master Yuxuan. A reminder: Tonight is still the Fifth Anniversary of the Tragedy of Tianho. A day of remembrance for those we lost."
    door_voice "Current city events include an afterparty at the Tavern of the Jade Serpent. Please drink responsibly."
    magnus "A... talking door!"
    niko   "The city's partying... Not that I can blame them. But there's going to be a yaoguai attack. Soon."
    yuxuan "Double the security protocols. We cannot allow anyone unauthorized to go inside."

    play sound sfx_door_chime                   # PLACEHOLDER — door chime

    door_voice "Security enhancement confirmed. Initiating Protocol Lockdown: JIN-SHIELD. All channeling frequencies-nullified."
    door_voice "Perimeter defenses active. Unauthorized entry will result in automated defense response."
    door_voice "No unauthorized being shall pass."
    niko   "Are you sure this thing can hold, Yuxuan?"
    door_voice "I am forged from Jinyan steel, tempered in the magma-forges of Yonghai. I do not buckle. I do not burn. I do not break."

    show svante normal_base at left_char
    show chunghee normal_neutral at right_char
    with Dissolve(0.2)

    "Svante lifted his hand, trying to channel the metal. It won't budge."

    svante "It's right. My energy's getting dampened. Can't push even a breeze through it."
    door_voice "Thank you for your feedback. Here at Cheng Industries, we bring change. And yes, we take custom orders."
    dorian "We're counting on you to protect them. The children... Weng... everyone inside."
    door_voice "Affirmative. As per Master Yuxuan's settings, this unit will not play the Cheng Industries jingle unless he is 10 meters away."

    "The door's lights flickered once, then faded, locking into silent vigilance."

    "Everyone stood in a circle-Yuxuan's eyes scanning a datapad, Niko gripping his prayer beads, Svante nervously adjusting his gloves. Magnus, tapping his foot impatiently. Chung-hee, arms crossed, his brows drawn low."
    "All their attention was on Tianho."

    yuxuan    "We'll head straight to the eastern gate. We can set up defenses there."
    niko      "We need to get people to safety first."
    svante    "I really hope Lady Aoi is still there. We'll need her..."
    chung_hee "We only have 40 minutes. We need to hurry. I can use the amulet of teleportation to-"
    dorian    "Everyone, I'm not coming with you."

    "Heads turned. Silence fell like a blade."

    magnus "What? No, Dorian, we need every fighter we can get-"
    dorian "You need to go. All of you. Tianho needs you. You're stronger together-and you'll be able to set up defenses faster without me slowing you down."
    chung_hee "You're thinking of facing the Yaoguai King alone?"

    "I nodded once. My throat tightened."

    dorian "Elara. Sarah. Daniel. Emily... Lucas."

    "Their names cut into me like glass."

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

    play music ost_ch10_alert fadein 1.0        # PLACEHOLDER — urgent alert theme

    if love_route_locked == "yuxuan":

        show dorian normal_alt_tense at left_char with Dissolve(0.2)

        "I kept walking."
        "Each step carried the weight of ghosts I could no longer protect. My fists clenched. My jaw tightened. I had to do this. Alone."
        "Then I heard it-footsteps pounding fast behind me."

        yuxuan "DORIAN!"

        "I stopped. His voice cut through the silence like a blade. Urgent. Cracked. Furious."

        show yuxuan normal_angry at right_char with Dissolve(0.2)

        yuxuan "What in the Prosperity Dragon's name are you doing!?"

        "I turned halfway. There he was-panting."

        dorian "Yu, please. Go back. Go to Tianho."
        yuxuan "No. No, no, no-you don't get to play hero right now. This is suicide, Dorian! You know what the Yaoguai King can do! You really think you can take him alone?"
        dorian "I have to do this."
        yuxuan "No, you don't! You could help us! You could protect more people! Why throw yourself away for revenge? It's selfish."
        yuxuan "I thought we were past this. I thought we were a team. I... I thought we were family ever since the blizzard at Frostcradle. I..."

        "His voice broke."

        show yuxuan normal_sad at right_char

        yuxuan "I don't want to lose you, Dorian..."
        dorian "I don't plan on dying, Yu."
        yuxuan "Well, neither did your wife. Nor your kids. Nor Count Vasily. Nor my friends. Nor-"
        yuxuan "You know what? Fine."

        "His hands shook. His eyes shimmered from the underground lights, unshed tears."

        yuxuan "Do what you want. Be the tragic Paladin. Die a noble death if that's what helps you sleep."

        "He turned, robe whipping behind him as he ran. His footsteps faded behind me."
        "And I kept walking. Toward the dark. Toward him."
        "I'm so sorry, Yu."

    elif love_route_locked == "chunghee":

        show dorian normal_alt_tense at left_char with Dissolve(0.2)

        "I kept walking."
        "Each step carried the weight of ghosts I could no longer protect. My fists clenched. My jaw tightened. I had to do this. Alone."
        "Then a voice thundered inside my head, not spoken aloud but pulsing through my chest like a divine decree."

        chung_hee "Dorian. What do you think you are doing?"

        "Footsteps followed, fast, heavy, resolute. Chung-hee was behind me-his presence unmistakable."

        show chunghee normal_angry at right_char with Dissolve(0.2)

        dorian    "Go to Tianho. They need you more than I do."
        chung_hee "The Yaoguai King isn't some warlord you can stab through the heart. He's not a man-he's a force. A storm. You'll be throwing yourself into a hurricane fueled by rot and fury."
        chung_hee "You'll die for vengeance, Dorian. And it won't bring them back."
        dorian    "This is personal, Chung."
        chung_hee "Personal? You think you're the only one who's ever lost someone? You're not the only man dragging corpses through the dark, Dorian."

        "I froze. Just for a second."

        chung_hee "I once told Aunt Ji-hye I had to face King Gustav alone. Said no one else could understand. That no one else could carry my war. I thought I was being noble. Brave."
        chung_hee "I was wrong. I stood there in the battleground. Like a fool. Begging for mercy for anyone who would come by."
        chung_hee "Then you and the others came along. You, Niko, Svante, Yuxuan and Elias. You nursed me back to health."
        chung_hee "Then I realized I made a mistake. A mistake that nearly cost me my life. I would've died there if you-if all of you-hadn't been there."
        dorian    "This is different. You don't know what he took from me, Chung. I can't even hear his voice without seeing my family's faces-burning, screaming, gone."
        chung_hee "You think I don't know what that feels like?"
        chung_hee "Every night, I lie awake imagining how my mother and father must have died. Whether they were afraid. Whether they suffered. Whether they called for me before dying at Tianho."

        "He stepped closer, and the air thickened."

        chung_hee "Their deaths hang on me like chains, Dorian. But I bear them. And I'm telling you-don't add your name to the dead by going alone. I'm begging you-don't do this."

        "I stared at him for a moment. And I turned. Started walking again. Behind me, I heard nothing. No words. No movement. Only silence."
        "...I'm sorry, Chung."

    elif love_route_locked == "svante":

        show dorian normal_alt_tense at left_char with Dissolve(0.2)

        "I kept walking."
        "Each step carried the weight of ghosts I could no longer protect. My fists clenched. My jaw tightened. I had to do this. Alone."
        "Then I heard it-footsteps pounding fast behind me."

        svante "Dorian!"

        "It was Svante. Breathless. His face flushed, eyes wide with panic and frustration as he caught up beside me."

        show svante normal_angry at right_char with Dissolve(0.2)

        svante "You can't go alone! The Yaoguai King-he's not just some monster. He's old, Dorian. Too powerful. Please, come back. Come with us to Tianho."
        svante "Yuxuan's worried sick. I'm worried sick. We need to-"
        dorian "Svante, go back. I have to do this alone."
        svante "W-What? Why?! Why does it have to be you, and why does it have to be alone?"
        dorian "It... It's personal."

        "He grabbed my arm-his grip trembling."

        show svante normal_sad at right_char

        svante "You're being selfish. What about Elias? You're all he has. He lost Queen Ekaterina, his mother-don't make him lose you, too!"

        "I looked at him, my heart twisting."

        dorian "I'm not planning to die."

        "Svante looked down."

        svante "Neither did Kristin when she stood up to Count Vasily."
        svante "You were there, Dorian. You saw what they did to her. And then I blamed you and Elias."
        svante "So don't lie to me now. Don't say you'll survive just because you want to."

        "Silence."

        dorian "I have to do this."

        "He stared at me, breath ragged, anger and sorrow warring on his face. And then-He let go."
        "He turned away, shoulders slumped. But just before he walked back to the others, he looked over his shoulder. His eyes-violet-met mine."

        svante "I know we only met a few days ago but..."
        svante "...Please don't make me mourn you too."

        "I watched him disappear into the shadows, his silhouette swallowed by the dim underground lights. I stood there for a moment longer, the ache in my chest heavier than before."
        "I'm sorry, Svante."

    elif love_route_locked == "niko":

        show dorian normal_alt_tense at left_char with Dissolve(0.2)

        "I kept walking."
        "Each step carried the weight of ghosts I could no longer protect. My fists clenched. My jaw tightened. I had to do this. Alone."
        "Then I heard it-footsteps pounding fast behind me."

        niko "Dorian."

        "I stopped, but didn't turn. The sound of his footsteps caught up with mine."

        show niko normal_anger at right_char with Dissolve(0.2)

        niko "Forget me. Forget about the others. But what about Elias?"

        "I flinched."

        niko "You know the Yaoguai King isn't just some monster in the dark. You've seen what he is. What he does."
        niko "You're not invincible, Dorian. Please... come back to Tianho. Maybe we can-"
        dorian "I have to do this, Niko."
        niko "Then I'm coming with you. You shouldn't-"

        "I shook my head and raised my hand. And he stopped. Stilled. His expression twisted, somewhere between pleading and fury."

        show niko normal_sad at right_char

        niko "Are you really willing to leave Elias behind? Leave him fatherless? To chase a death you know is coming?"
        dorian "I'm not planning to die."
        niko "Well, neither did Kaito."
        niko "He thought he could save everyone in that burning building. Thought strength would be enough. Now he's in Xianlun."

        "I turned slightly. Just enough to look at him from the corner of my eye."

        dorian "You, of all people-Enoch's chosen and a Prophet of the Death God-should understand. Death is natural. Normal. I'm choosing this. That's the Law of Enoch, right?"
        dorian "Don't deny someone their death."

        "That silenced him. For a beat. Then-he stepped back, something breaking behind his eyes."

        niko "Fine."
        niko "Then may the Death God, Lord Enoch, greet your sacrifice with open arms and empty hands."

        "He turned without another word and began walking away."
        "I turned, too and walked forward. I didn't look back."
        "Forgive me, Niko."

    else:

        show dorian normal_alt_tense at left_char with Dissolve(0.2)

        "I kept walking."
        "Each step carried the weight of ghosts I could no longer protect. My fists clenched at my sides. My jaw tightened. My breath came steady, but heavy-measured like the silence between thunder."
        "I had to do this. Alone."

        magnus "Wait, Dorian! Wait!"

        "I didn't stop."

        show magnus normal at right_char with Dissolve(0.2)

        magnus "Heavens, you walk like you're marching into hell-...which, okay, fair, you kind of are, but still."

        "He stepped in front of me, arms stretched out like a wall I didn't ask for."

        magnus "Hey. Hey. Look at me for a second, yeah? Just... listen."
        magnus "I-uh... I don't know how to do the whole \"pep talk\" thing. So... I'm gonna do the only thing I do know."

        "He cleared his throat dramatically."

        magnus "Don't throw yourself into doom, my friend, The world still needs your flame to mend..."
        magnus "We've fought, we've cried, we've bled, we've burned, But some of us still need you returned..."

        "He trailed off. He shrugged sheepishly."

        magnus "Okay, that was terrible. I know. But the message is clear, right?"
        magnus "The Yaoguai King is powerful, Dorian. You know that. You're not stupid. If he wants you to come alone. He wants you to die."
        magnus "Why give him what he wants? Just... come with us to Tianho. Ignore him. Help save lives there."
        dorian "I have to do this."

        "Magnus flinched."

        magnus "Why? Because of vengeance? Because of pride? You think you're doing this for your family-but what about the ones still here?"
        magnus "I'm talking about Elias. You know, the one that dresses up like a girl?"

        "I turned to look at him."

        magnus "Yuxuan told me. I didn't know until now that he's your son. He's alive, Dorian. He still needs you."

        "A long silence. I shook my head."
        "Magnus looked at me like I had just slapped him."

        magnus "You're being selfish."

        "He turned, started to walk away... but then stopped. Glanced back over his shoulder."

        magnus "I... I remembered that my lover once said to me."
        magnus "\"I don't intend on dying.\" That was the last thing she ever said. And now that's... one of the only memories I have of her."

        "His voice dropped to a whisper."

        magnus "Please... let me come with you."

        "I looked at him. The pain in his eyes. The history in his voice."
        "But I shook my head. The Yaoguai King is after him. I can't risk it."

        "Magnus stepped back. Wounded. Silent."

        magnus "Fine."

        "And I walked away-toward the dark, toward the fire, toward the one thing that had taken everything from me."
        "Behind me, Magnus didn't follow."
        "I'm sorry, Magnus..."

    jump ch10_sealed_door


# =============================================================================
# SECTION 12: LABEL CH10_SEALED_DOOR — Sealed Door / Yaoguai King
# =============================================================================

label ch10_sealed_door:

    scene underground_door with dissolve

    "After minutes of walking, I reached the place where we had found Magnus."
    "A bottomless chasm wrapped around the edge, and a single narrow bridge stretching towards the center."

    scene underground_magnus with dissolve
    play music ost_ch10_boss fadein 1.0         # PLACEHOLDER — boss theme

    "Two yaoguai hunched over mangled bodies-unrecognizable, barely even bones now. The sound-"

    "MUNCH. CRUNCH."

    "-echoed across the stone. One of them slurped something wet and vile, then burped loudly, its bloated belly sagging against the ground."

    show yg at left_char with Dissolve(0.2)

    yg "Mmmh... That one tasted like fear. My favorite seasoning."
    yg "You always say that. I think this one tasted like despair. Much richer. Earthier. You wouldn't know taste if it chewed you."
    yg "Bah. Give me fear with a side of broken dreams any day."
    yg "We already ate all of them, Your Majesty. Nothing but bones left!"
    yk "You're spoiling your appetites, boys. The main course has arrived."

    hide yg
    show yk at center_char with Dissolve(0.2)

    "At the center stood the Yaoguai King."
    "He was crouched low, fingers trailing along the broken ice where Magnus had once been entombed."

    yk "This was where he slept. Four centuries in silence... and still, his presence lingers, dragonkin."
    dorian "Hmph. I didn't know I was expected."
    yk "Oh, you were always expected, dragonkin. Ever since your wife screamed my name with her dying breath."

    "I didn't flinch. Not on the outside."

    show yg at left_char with Dissolve(0.2)

    yg "The dragonkin smells like righteous fury. I love when they're angry. It makes the blood sweeter."
    yg "Do you think we can have a taste before the king breaks him?"
    dorian "Tell me what happened. And maybe I'll make this quick."
    yg "Ohh, he wants answers now. How precious. Maybe if you ask real nice, we'll write it on your tombstone."
    yg "He's burning up! Let's bite him now! Hot blood's the sweetest!"
    yk "Hush, boys... Let the dragonkin grieve with context."
    yk "Very well. This will be fun. I suppose you've earned a peek behind the curtain. After all, you have played your part well, dragonkin."

    hide yg

    "He circled slowly, claws clicking against the cracked ice where Magnus once hung, suspended in frost. His grin widened, revealing fangs too long for his face."

    yk "Magnus is... a clone. A clone of the death god."

    "My breath caught. My pulse thundered in my ears. A clone?"

    yk "Yes. A clone. Of the Death God's reincarnation."

    "I said nothing. Not from fear-but disbelief. He watched me closely, savoring the silence like wine."

    yk "You should've seen your face just now. Delicious..."

    show yg at left_char with Dissolve(0.2)

    yg "Delicious! Delicious! Good enough to eat!"

    hide yg

    "He tapped the icy platform with a clawed foot, sending tiny shards skittering."

    yk "I overheard it all, you know. A whispered little meeting between King Long Shen of Tianho and King Tatsuya Fujiwara of Hinami."
    yk "Did you know they meet in secret? So many secrets among old men with too much power."

    "He leaned closer, voice dropping to a conspiratorial murmur."

    yk "They spoke of the Rebirth. Said the Death God always reincarnates. Again and again and again. Death, reborn to die once more. Beautiful, isn't it? The god of endings trapped in an eternal loop."
    yk "When Enoch died, a new vessel emerged. But they caught him. Froze him in true ice. Buried him deep beneath Tianho like a shameful relic."

    "My heart pounded. Four centuries. No sign of the Death God. And now I knew why."

    yk "From that vessel, they made the clone. It took centuries. Science, sorcery, desperation. But they did it."
    dorian "Why? Why make a clone?"
    yk "I don't care. Let the royals cling to their reasons. All that matters is the truth: the Death God's body still exists. And even without will... it is still a weapon."
    yk "Bone forged in divinity. Blood soaked in finality. Imagine it-an army raised from his marrow. Corpses that do not rot. Channelers who wield death as birthright. The dead, reborn to kill."

    "The Divine Weapon... is Magnus? This can't be..."

    yk "The original body-the one that brought the Tragedy of Tianho-was destroyed. That meddling paladin, Cyrus, actually managed to kill him and destroyed the body."
    yk "But Magnus? Still intact. Still potent. Was supposed to be mine."
    yk "I had everything. I was so close. If not for that ridiculous spectacle with the rulers..."

    "The Yaoguai King raised his claw. Shadows coiled around my head."
    "And I saw a vision..."

    jump ch10_vision_rulers


# =============================================================================
# SECTION 13: LABEL CH10_VISION_RULERS — Vision: Rulers' Meeting 5 Years Ago
# =============================================================================

label ch10_vision_rulers:

    scene underground_magnus with fade

    "We were in this very hall, though the memory shimmered like heat rising from frost."

    show king_gustav at center_char
    show king_long_shen at left_char
    show olympia at right_char
    with Dissolve(0.2)

    king_gustav "UNHAND ME this instant, or I will order every soldier in my empire to raze this palace to ash!"
    long_shen   "You butchered my family, Gustav! You sent your aldorith assassins in the dead of night! My wife and my two sons-you knew what you were doing!"
    king_gustav "Pft. Do you have proof? Do you have proof, Shen? Or just grief and wild accusations?"

    "Silence fell. It was thick with outrage."

    long_shen         "Any objections?"
    emperor_minjoon   "None. Then let it be known: if this is the way Ena kings govern, Kyeongjang disavows your alliance entirely."
    emperor_minjoon   "I should never have brought my wife here."
    seo_yeon          "You couldn't have known, love. But now we do."
    olympia           "Min-joon... Seo-yeon, I apologize on behalf of our alliance. Gustav will be punished. I swear it."
    emperor_minjoon   "You brought Jin-haeng back. You brought our son back from the dead... That is the only reason I still stand in this room."
    seo_yeon          "I would have torn apart time itself for that miracle. You gave me back my son... when my own body could not."
    olympia           "You have my thanks. It is my pleasure to give you your infant son back."
    long_shen         "DEATH ISN'T ENOUGH FOR HIM!"
    emperor_minjoon   "I cannot imagine your grief, Shen. And I do not intend to stand idle through it. Gustav must be killed."
    olympia           "We can't. We would risk the project getting known."
    olympia           "First-we reseal the chamber. That weapon must never be touched again."
    olympia           "I'll take the Amulet of Frost. I will guard it with my life. And I swear-Gustav will never hold power over the key again."
    king_gustav       "That's mine! I hold the third key to the door! Not you!"
    emperor_minjoon   "One of the keys is draconic fire, and only Tianho's royal blood can channel it. You knew that. That's why you murdered Long Shen's family-to ensure no one could ever seal the door again."
    long_shen         "YOU KILLED MY FAMILY because they could channel draconic fire!"
    king_gustav       "GIVE ME THE AMULET OF FROST! YOU ARE VIOLATING THE AGREEMENT!"
    olympia           "The gall of you to even make demands!!"
    emperor_minjoon   "Your right to that amulet died with Shen's family. You forfeited your claim the moment you became a murderer."
    long_shen         "THEN EXECUTE HIS WIFE TOO! STRIKE HER DOWN AND EVEN THE SCORE!"
    olympia           "Shen. Calm down."
    long_shen         "THEY WERE MY FAMILY, OLYMPIA! My sons... my wife... They were the last heirs to the Prosperity Dragon's bloodline!"
    olympia           "I know, Shen... *softly* And I would've died in their place if it meant undoing this. But we have to think clearly now."
    emperor_minjoon   "I will guard the Amulet of Teleportation-the second key. I will make sure that it's safe in Kyeongjang."
    long_shen         "By the Prosperity Dragon-"
    king_gustav       "TOOK YOU LONG ENOUGH!"

    show boy_ald_normal at center_char with Dissolve(0.2)
    show girl_ald_normal at right_char with Dissolve(0.2)

    boy_ald   "They have Father! Destroy them!"
    girl_ald  "YAHHHH!!"

    "The doors exploded inward as Gustav's hidden soldiers stormed in, blades drawn and channeling elements."

    emperor_minjoon "Gustav, you dare wage war in the heart of peace?"
    long_shen       "You'll burn for this!"

    "A spire of earth struck Empress Olympia across the side, sending her tumbling. But even as blood trickled down her brow, she rose."

    long_shen       "OLYMPIA! ARE YOU ALRIGHT?"
    olympia         "I'm fine, Shen."
    king_gustav     "Heh. You will give me the amulet of frost, skank!"
    olympia         "You want the weapon, Gustav? Then come and take it!"

    scene underground_door with dissolve

    "The vision shifted-like flame caught in a gust."
    "Screams. Roars. Metal clashing. The ground trembled beneath the weight of monsters unleashed."
    "And I stood before them. King Gustav lay broken on the blood-soaked ground, battered and heaving, his armor cracked, his face streaked with ash and blood."
    "Standing over him was King Long Shen, surrounded by scorched earth and a seething aura of draconic power."

    show king_gustav at right_char
    show king_long_shen at left_char
    with Dissolve(0.2)

    king_gustav "Do it... Kill me..."

    "King Long Shen's voice thundered."

    long_shen   "You released the Death God onto Tianho! What madness took root in your soul, Gustav?!"
    king_gustav "I... I had everything under control. It was an accident!"
    king_gustav "If you and the other rulers hadn't fought me-none of this would've happened! If you would have just given me the divine weapon like I asked-"

    "I felt the ground shaking harder. A beast screamed in the distance."
    "King Long Shen's eyes blazed gold-his veins glowing faintly with draconic fire."

    long_shen "You insufferable wretch. Your ambition knows no end!"

    "He stepped forward and thrust his palm toward the door."

    long_shen "By frost and flame, by blood made pure, the weapon be sealed behind this door. Three keys shall break what now I bind-Frost and flight, and fire combined."

    "A burst of pure fire channeled from his chest to the seal. The door screeched shut, etchings flaring with molten gold as the door locked."

    king_gustav "NO!! NOOOOO!!"
    long_shen   "You will never open it again. Ena will be safer without you. The Amulet of Teleportation-Min-joon already sent it to Kyeongjang."
    long_shen   "You'll never see it again."

    "He held up the second amulet-the Amulet of Frost, gleaming with icy light."

    long_shen   "As for this? It stays with me."

    "King Gustav snarled."

    king_gustav "I swear, as long as I draw breath, I will-"

    "A scream tore from his throat as Long Shen slammed a flaming fist into his ribs, the heat searing armor and flesh. Gustav collapsed, choking on pain."

    king_gustav "AAHHHHH!!!!"

    "King Long Shen took a knife from his pouch."

    long_shen "This is for my sons. For my wife. For every soul you damned."

    "But then-"

    vasily "YOUR MAJESTY!!"

    scene bg_tianho_underground_2 with flash

    show king_gustav at right_char
    show king_long_shen at left_char
    show vasily neutral at center_char
    with Dissolve(0.2)

    "A beam of divine light tore through the haze. Count Vasily, brilliant and fast as lightning, surged in. In one blinding motion, he drove a knife through Long Shen's back."

    long_shen   "N.... No..."

    "The fire in his eyes flickered out. He crumpled, lifeless."

    king_gustav "Vasily... what have you done? We needed him alive! We needed that seal!"

    "Count Vasily's eyes were hard."

    vasily "He would've killed you, Your Majesty."
    vasily "The yaoguai are overrunning the palace. Tianho is a ruin. We have to move-now."
    vasily "Are you listening to me, Your Majesty? Your Majesty!"

    "King Gustav roared."

    king_gustav "We'll never access the Divine Weapon now! You FOOL! You-BELLIGERENT, SANCTIMONIOUS-"

    "Count Vasily slapped him."

    king_gustav "?!"
    vasily "Forgive me, Your Majesty. But Mjoll needs you alive. The death god is laying waste to everything."

    "He reached down, gripping Gustav's arm and hoisting him up with surprising gentleness."

    vasily "We have a carriage waiting. We're evacuating through the hidden passage beneath the north wing. Can you walk?"
    king_gustav "O... Of course."
    vasily "Then let me help you. We must hurry."

    scene underground_magnus with fade

    "The vision ended yet I stood frozen. The echo of the vision still burned in my mind-the roar of fire, the flash of betrayal, the final breath of a king."
    "Count Vasily was the one who saved Gustav. That loyal dog."
    "King Gustav was the reason for the death god's release in his ice prison."
    "And in that chaos... King Long Shen-the last known wielder of draconic fire-was killed."

    show yk at center_char with Dissolve(0.2)

    "The Yaoguai King let out a low, satisfied hum behind me, as if relishing my silence."

    yk "Now you understand... The divine seal needs something more than brute strength or blood. It needs fire. Not the mortal kind. Draconic fire."

    "I turned toward him, my fists clenched."

    dorian "You needed someone of Tianho royal blood."

    "The King's smile split wider, showing rows of jagged, gleaming teeth."

    yk "Precisely. I could scour the continents for the two amulets. But it would be meaningless without a soul the seal would answer to. And then I saw you."
    yk "You, dragonkin... Speaking to the Prosperity Dragon as if it were an old friend. Whispering. Smiling. Laughing. Like it was nothing."

    "His voice grew quieter, darker-deadly."

    yk "Even kings and queens of Tianho have waited lifetimes to hear a whisper from that spirit. Some died without ever glimpsing it. The Prosperity Dragon has remained silent for generations..."
    yk "Yet it spoke to you for some reason. Very casually."

    "My heart pounded."

    yk "That's when I knew. You are not just a warrior. You are the key. A flame born to break open what Long Shen sealed."
    yk "And I was right..."

    "He tilted his head, his tone mocking."

    yk "And whether you want to or not... I will have your flames."
    dorian "THEN WHY KILL ELARA AND MY CHILDREN?! THEY DIDN'T HAVE TO DIE FOR THIS!"

    "The words ripped from my chest-raw and seething."
    "It all came running back to me. How he disrespected Elara, the kids."

    yk "Because I needed you broken. The legends say draconic fire awakens only through sheer desperation. When your heart is torn apart and all that remains... is rage."

    show yg at left_char with Dissolve(0.2)

    "Then came the voices-those cursed, laughing mouths beside him."

    yg "And they were yummy! Yummy delicious!"
    yg "That woman- what a skank! Hahaha! And the little ones-"

    hide yg
    hide yk

    "They didn't finish. I didn't let them."
    "My rage ignited. Draconic fire erupted around me like a storm-blazing gold and crimson, heat warping the air in violent waves. I thrust both hands forward and unleashed a roaring inferno across the platform."

    play sound sfx_draconic_fire                # PLACEHOLDER — draconic fire SFX

    "The flames consumed the two yaoguai instantly, their screams shrill and choking as fire melted flesh from bone and turned the stone beneath them black."

    yg "AAAAAGHHH-!!"
    yg "NO! STOP-GRRAHHHH!!"

    "Ash and smoke whirled in the air."
    "The Yaoguai King didn't move as the flames engulfed him-but his grin was gone."

    show yk at center_char with Dissolve(0.2)

    yk "HOW DARE YOU! AFTER I JUST TOLD YOU EVERYTHING! I could have given you power. Dominion. Revenge. I was going to make you a god, Dragonkin!"

    "My flames blazed brighter, the fire pulsing from my chest like a heartbeat."

    dorian "This is for Elara. This is for my children. Daniel. Emily. Sarah. Lucas."

    "The King bared his jagged teeth."

    yk "SUCH POWER! SUCH GLORIOUS FIRE! But how foolish! YOU WILL RUE THE DAY YOU FACE ME!"

    "He raised his claws, darkness gathering behind him in a wave of corrupted energy."

    yk "Come, dragonkin... I'LL BURN YOU TO ASHES!"

    "The Yaoguai King roared-a sound that cracked stone and shook the platform beneath our feet. Shadows curled around him like tendrils, twisting into monstrous limbs. His claws-longer than swords-gleamed."

    yk "Let's see if that draconic fire still burns as bright... when you're bleeding."

    "Then... a voice called out to me. It called out to me again."

    prosperity_dragon "Child..."

    "The world slowed."

    prosperity_dragon "He is old. Two centuries of strength. Unmatched. Unrelenting."
    prosperity_dragon "You are new. You are fast. Heed my advice. Don't meet force with force."
    prosperity_dragon "Wait and slip past the storm. I trust you, child. Do not let this monstrosity get the better of you."

    "The world resumed its pace. The king lunged. Fast. Too fast. His claw came down like a guillotine, aiming to cleave me in half."

    jump ch10_boss_fight_1


# =============================================================================
# SECTION 14: LABEL CH10_BOSS_FIGHT_1 — Boss Fight Round 1
# =============================================================================

label ch10_boss_fight_1:

    "QUICK TIMED CHOICE:"

    menu:

        "Dodge to the side and counter with a burst of flame.":
            $ yking_score += 1                  # +1 YKing score

            "I ducked low and rolled to the left. His claw slammed into the ground where I'd been standing, splintering the stone with a deafening crack. Mid-roll, I threw my hand forward and unleashed a torrent of fire straight at his side."
            "The flames roared against his ribs, and I caught the scent of scorched rot as bits of his corrupted armor blackened and burned."

            yk "Not bad... but not enough."

        "Block the strike with a crossed-arm guard reinforced with draconic fire.":

            "I braced my arms in front of me, channeling draconic fire as a shield. His claw tore through it like paper. Pain exploded through my shoulder as his strike connected, slashing flesh and armor alike."

            yk "WATCH HOW MY CLAWS TEAR YOUR FLESH LIKE PAPER!"

            "I choked out, staggering back as blood streamed down my arm. But I stayed standing. I had to."

    "The Yaoguai King stepped back, dark eyes gleaming with menace."

    yk "You'll be joining your family soon..."

    "He spread his arms. The air warped and twisted. A cyclone of corrupted wind and shadow coiled above us, rising higher and higher into the sky like a black storm."

    jump ch10_boss_fight_2


# =============================================================================
# SECTION 15: LABEL CH10_BOSS_FIGHT_2 — Boss Fight Round 2: Spirits Wave
# =============================================================================

label ch10_boss_fight_2:

    "QUICK TIMED CHOICE:"

    menu:

        "Stay grounded and summon a shield of fire around you to brace for impact.":

            "I stood my ground and summoned a dome of fire around me. The cyclone hit with the force of a hurricane, blades of shadow slicing through the flames. The shield held-then shattered."
            "The impact hurled me across the arena. I crashed hard, pain tearing through my side."

            yk "What's wrong, dragonkin? Had enough?"

            "I groaned, coughing up blood, but pushed myself to my knees. I wasn't done yet."

        "Leap into the air, aiming to slam down with a draconic flame punch.":
            $ yking_score += 1                  # +1 YKing score

            "I clenched my fists and launched into the air, draconic fire roaring beneath my feet."
            "I plummeted from above, fist wreathed in flame, and slammed it into his chest like a meteor. The impact cracked the ground and sent him skidding back, trails of fire left in my wake."

            yk "Ghhh-! Screw you dragonkin!"

    "The arena smoldered. The ground cracked beneath us. My shoulder ached, my ribs screamed, but the fire in my heart wouldn't die."
    "The Yaoguai King stood tall, smoke rising off his hide. His smile widened."

    yk "You're still alive? Good. That means I can keep breaking you-piece by piece."

    "My draconic fire flickered across the cracked stone, and I could feel the pulse of the Prosperity Dragon burning in my veins."
    "But the Yaoguai King was far from done."
    "With a snarl, he spread his arms wide. Black mist gushed from his body, and behind him rose the silhouettes of twisted spirits-dead yaoguai, their wailing souls clawing for release."

    dorian "Impossible... The spirits?"

    play sound sfx_yaoguai_roar                 # PLACEHOLDER — yaoguai spirit roar

    show yg at left_char with Dissolve(0.2)

    yg "Raaaaaaawwrrr!!! Grrraaawwwrrr!! Rawwwrrr!!"
    yk "Their hatred will be my shield. Their screams, my chorus."

    hide yg

    "He hurled them toward me in a wave of screaming shadow."

    jump ch10_boss_fight_3


# =============================================================================
# SECTION 16: LABEL CH10_BOSS_FIGHT_3 — Boss Fight Round 3: Cyclone
# =============================================================================

label ch10_boss_fight_3:

    "Quick Timed Choice:"

    menu:

        "Channel wind to slice through the spirits before they could touch you.":
            $ yking_score += 1                  # +1 YKing score

            "I need to slice through them before they could touch me. I closed my eyes and inhaled-then roared."
            "A surge of wind erupted from my core, sharp as blades and fast as thunder. The spirits shrieked as the gust shredded through them, dissipating their forms into wailing mist."

            play sound sfx_yaoguai_roar         # PLACEHOLDER — yaoguai roar

            yg "Raaaaaaawwrrr!!! AAHHHH!!"

        "Cover yourself in fire and charge through.":

            "I cloaked myself in fire and tried to power through. The spirits screamed louder as they tore at my flame, phasing into me like knives. Cold dread flooded my mind as ghostly claws scraped at my soul."

            play sound sfx_yaoguai_roar         # PLACEHOLDER — yaoguai roar

            yg "Gwaaaaarrrrr!!"

            "I stumbled, gasping."
            "They faded-but not before leaving my skin ice-cold and raw."

            yk "That sting, Dragonkin? Hahaha!"

    jump ch10_boss_outcome


# =============================================================================
# SECTION 17: LABEL CH10_BOSS_OUTCOME — Good or Bad Ending Gate
# =============================================================================

label ch10_boss_outcome:

    show yk at center_char with Dissolve(0.2)

    yk "The halls of Xianlun await you... you'll see your kin again... Aren't you excited?"

    "He sneered."

    yk "Foolish boy. This ends now."

    "And then he moved."
    "Faster than before. A blur of darkness and bone."
    "One claw arced high, slicing down like a falling guillotine. The other swept low, fast and vicious."

    "Quick Timed Choice:"

    menu:

        "Stand your ground and counter.":

            "His lower claw slammed into me mid-motion, slicing across my hip. I howled and hit the ground hard, blood soaking into the dirt."
            "Still, I forced myself to rise."

            yk "Futile, dragonkin. This is what you get for challenging me."

            "I was running out of time."

        "Duck between the claws and twist behind him.":
            $ yking_score += 1                  # +1 YKing score

            "I took one sharp breath and dove between his incoming arms. The wind of his swipe grazed my skin, but I twisted my torso mid-dodge and rolled behind him in one smooth motion."
            "The King spun, eyes wild. Too late."
            "I had flames blazing in both fists. I brought them down on his back."

            yk "GGGRRAAAAAAAAAGHHH!!!"

            "His howl tore the room. Fire scorched his corrupted back, searing deep. Smoke rose from his shoulders as he stumbled forward."

    if yking_score < 3:
        jump ch10_bad_end_fight
    else:
        jump ch10_boss_good


# =============================================================================
# SECTION 18: LABEL CH10_BAD_END_FIGHT — BAD END: YKing < 3
# =============================================================================

label ch10_bad_end_fight:

    hide yk

    "The Yaoguai King snarled-scorched, bleeding, but very much alive. His charred skin peeled at the edges, smoke curling from every wound... and still, he laughed."

    show yk at center_char with Dissolve(0.2)

    yk "Pathetic. I expected more from the Dragon of Gale."

    "I could barely move. My limbs were trembling, my vision was swimming."
    "The King straightened, his body still crackling from the flames I had left on him."

    yk "You're wasting my time."

    "In the space between heartbeats, he vanished."
    "A blinding pain tore across my chest. Cold flooded my lungs. I fell to my knees as warmth spilled from the open wound. My blood."

    dorian "GAHHH!!"

    "The world began to tilt."
    "He stepped before me-towering, monstrous, victorious."

    yk "You tried, little dragonkin. You really did."
    yk "Look on the bright side. At least you'll get to be with your family now. Elani or whats-her-name... those tasty children of yours... I'm sure they've been waiting."

    "I fell forward. My face hit the cold stone. My fingers twitched, reaching for fire that would never come. Behind me, I heard the jeering laughter of his minions. The Yaoguai. Loud. Cruel. Victorious."
    "Darkness crept in-but before I faded completely, I heard the King speak again. A promise. A curse."

    yk "Ena will fall. Just as Tianho will. I will raze it to the roots. Their temples, their thrones... Once the Divine Weapon is mine..."

    "And then.. Darkness."

    jump ch10_bad_end_credits


# =============================================================================
# SECTION 19: LABEL CH10_BOSS_GOOD — YKing >= 3: Illusion of Elara / Rescue
# =============================================================================

label ch10_boss_good:

    hide yk

    "I dropped low and slammed my hand into the ground."
    "A jagged spike of stone shot up and slammed into his jaw, snapping his head back in a brutal crunch."
    "Smoke curled from his wounds. His charred, half-melted body hissed and crackled like dying coals. But he didn't fall. Not yet."

    show yk at center_char with Dissolve(0.2)

    yk "You... You've gotten strong. Too strong."

    "His voice was trembling-not from fear, but fury. There was rage in his eyes now. Genuine. Feral. I had wounded his pride."
    "I stood tall, even as my body ached to collapse. Flames continued to swirl around me. The shadows behind him rippled."
    "And from them... she stepped forward."

    hide yk
    show cg_elara_children_death with dissolve

    elara "Dorian... you did it. You're safe now. Come home."

    "My knees nearly buckled. Her eyes. Her smile. Her soft, glowing skin. She reached toward me with trembling fingers."
    "But then I saw it. Just a flicker. The smirk behind the eyes. The hunger behind the tears. The way her shadow curved wrong against the floor."
    "Too late."

    hide cg_elara_children_death
    scene underground_magnus with flash

    "Something sharp, searing, punched through my gut. My hands trembled."
    "The illusion melted away. Elara vanished like mist in the sun. And standing there, face twisted in delight, was the Yaoguai King."

    show yk at center_char with Dissolve(0.2)

    yk "Still so gullible. That's what makes you fun."

    "He lifted me by the throat. My legs kicked uselessly beneath me, blood dripping down his arm. The fire around me sputtered-waning."
    "He pulled me close, face inches from mine. I could smell the rot of his breath."

    yk "Watching you break, watching you cling to the fantasy that you could win? That's ART."

    "The Yaoguai King leaned in, claws poised to rip the last of my life away."

    yk "I was supposed to give you power once I get my hands on that Magnus and take his power."
    yk "A shame. But at least you'll join your wife. Your little ones. Perhaps they'll still recognize what's left of you."

    dorian "D... Do it..."

    "I closed my eyes, accepting my fate."

    yk "This is farewell, dragonkin. DIE-"

    # Branch on love route for rescue
    if love_route_locked == "yuxuan":
        jump ch10_rescue_yuxuan
    elif love_route_locked == "chunghee":
        jump ch10_rescue_chunghee
    elif love_route_locked == "svante":
        jump ch10_rescue_svante
    elif love_route_locked == "niko":
        jump ch10_rescue_niko
    else:
        jump ch10_rescue_magnus


# =============================================================================
# SECTION 20: LABEL CH10_RESCUE_YUXUAN — Yuxuan Rescues Dorian
# =============================================================================

label ch10_rescue_yuxuan:

    play sound sfx_cheng_jingle                 # PLACEHOLDER — Cheng jingle SFX

    "\"HERE AT CHENG'S, WE BRING CHANGE!\""

    "The jingle blared through the chamber-loud, off-key, and utterly ridiculous. It echoed off the walls like a commercial from a forgotten dream."
    "The Yaoguai King froze mid-strike, his claws still around my neck."

    yk "Hmm?"

    "FWOMP!"

    play sound sfx_electric_net                 # PLACEHOLDER — electric net SFX

    "A massive net dropped from the ceiling-crackling with electricity. It slammed down on him like a divine trap, snapping around his limbs and torso with violent force."

    yk "WHAT IS THIS?!"

    "He thrashed, roaring in disbelief as sparks shot through his body. The net pulsed again, chaining him down like a wild beast caught in a god's snare."

    "Supply Bot: Electric net protocol engaged."

    "I looked up-barely conscious, my body trembling."

    dorian "Y-Yuxuan?"

    hide yk
    show yuxuan normal_happy at left_char with Dissolve(0.2)
    show supply_robot normal at right_char with Dissolve(0.2)

    "Smoke billowed from the shattered archway above, and through it walked a figure wielding an absolutely massive cannon strapped to a rig of copper coils and glowing tubes."
    "It was Yuxuan. A supply bot rolled behind him, wheels screeching slightly as it dragged what looked like an absurdly overloaded battery."

    yuxuan "PRESENTING CHENG INDUSTRIES' NEW PROTOTYPE WEAPON! You like this, beastie?"
    yk     "WHO?! WHO DARES-"

    "A voice rang out-calm, powerful, ancient."

    prosperity_dragon "The renowned inventor, Cheng Yuxuan. CEO of Cheng Industries. A beacon of ingenuity... and a symbol of hope for all of Tianho."

    yk "The... the Prosperity Dragon...?!"

    "The net pulsed again, blindingly bright."

    yuxuan "Oh, you're really screwed now. These tunnels? These are my turf, freak."

    "He flicked a switch. The cannon began to hum, and the coils down its barrel lit up like lightning in a bottle."

    yuxuan "Voltage check?"
    "Supply Bot: CALIBRATION COMPLETE. VOLTAGE: 100,000%%. MEGABOOM PROTOCOL READY."

    "The air vibrated. The cannon whined, glowing dangerously."

    yk     "You insolent, insignificant-!"
    yuxuan "I'm not insignificant. I'm an icon."
    yuxuan "DORIAN, MOVE!"

    "He slammed his palm down on a button. With the last ounce of strength I had, I rolled out of the way."

    play sound sfx_megaboom                     # PLACEHOLDER — megaboom SFX

    "Supply Bot: ENGAGING MEGABOOM. GOODBYE, YAOGUAI KING. COURTESY OF CHENG INDUSTRIES."
    yuxuan "THIS IS FOR TIANHO, YOU OVERGROWN MONSTROSITY!!"
    "BOOOOOOM."

    "The chamber erupted in light."
    "The beam of pure energy tore through the air like divine judgment-slamming into the Yaoguai King with the wrath of thunder, fire, and raw voltage. His body convulsed, twisted, and screamed."
    "Shadows shattered like glass around him. His form burned-scales cracking, bones breaking, magic unraveling."

    yk "AAAAAGHHHHH-!! NO!!! NOO!!!"

    "Then silence."
    "Smoke curled from the ruin where he stood."
    "I collapsed to my knees, gasping. My vision blurred, but I was alive-scorched, bleeding, trembling... but alive."
    "Yuxuan was already sprinting toward me, cannon clattering to the ground."

    show yuxuan normal_sad at left_char

    yuxuan "DORIAN! NO!! NO!! Are you okay?! Say something!"

    "I looked up at him weakly."

    dorian "Yu, y-you... saved me..."

    "He dropped beside me, grabbing my shoulders gently. The supply bot whirred to my side, scanning my injuries."

    "Supply Bot: Emergency assistance activated. Checking for serious injuries."
    "Supply Bot: CRITICAL DAMAGE DETECTED. WRAPPING BANDAGES. ADMINISTERING SALINE. HOLD STILL, MASTER DORIAN."

    "It clumsily began wrapping my arm in gauze."

    yuxuan "Don't worry. I've got you. You're okay. You're okay now..."

    "I tried to speak. To thank him again. But the world spun."
    "And then... the world faded to black..."

    jump ch10_tianho_battle


# =============================================================================
# SECTION 21: LABEL CH10_RESCUE_CHUNGHEE — Chung-hee Rescues Dorian
# =============================================================================

label ch10_rescue_chunghee:

    "A voice boomed through the area-not from lips, but from deep within our minds, rattling the very bones beneath our skin."

    play sound sfx_psychic_chains               # PLACEHOLDER — psychic chains SFX

    chung_hee "UNHAND HIM."

    "The Yaoguai King froze."
    "His claws still gripped my throat. Blood still dripped from my wound. But something changed in the air. The pressure shifted. The shadows that danced eagerly behind the Yaoguai King suddenly recoiled, like frightened beasts sensing something far worse."

    "I gasped, barely clinging to consciousness."

    dorian "C...Chung?"

    "My vision was fading, but I saw the flicker of his silhouette-elegant cape whipping in the wind. A flicker of white and silver."
    "Chung-hee."
    "And though his lips didn't move, his voice cracked like thunder in my mind again."

    chung_hee "You will not lay another finger on him."

    "The Yaoguai King snarled, baring his jagged teeth."

    yk "Another pest? You dare threaten-"

    hide yk
    show chunghee normal_angry at left_char with Dissolve(0.2)

    "Before he could finish, Chung-hee raised both hands, and the air around him rippled. With a sudden, sharp crack, ethereal chains-woven from pure mind energy-snapped into existence and lashed out."
    "They coiled around the Yaoguai King like living serpents, binding his arms, his legs, his neck. He thrashed, howled, clawed at them-but the psychic chains only tightened."

    yk "W-What?! WHAT THE?!"

    "The chains tightened."

    yk "Nnnghh-What are you?!"

    "A voice rang out-calm, powerful, ancient."

    prosperity_dragon "The Kyeongjang Emperor, Hyon Chung-hee... The eldest son of Hyon Min-joon. The strongest mind channeler to ever walk the lands of Kyeongjang."
    yk "The... the Prosperity Dragon...?!"

    "The Yaoguai King's pupils dilated."

    yk "No... no, no-"

    show yg at right_char with Dissolve(0.2)

    "But Chung-hee stepped forward, eyes narrowing. And then-his mind reached out."
    "From the shadows beyond, the Yaoguai spirits-twisted remnants once bound to the King-hesitated, confused by the power now overwhelming their master."
    "He... He's... controlling them telepathically."

    chung_hee "I'm casting off his control. Obey your true nature."
    chung_hee "The Yaoguai King is Dorian. Feed to your hearts content."
    yk "WHAT? NO! I AM YOUR MASTER! YOU-"
    yg "Yummy... Must feed!"

    hide yg

    "And they obeyed."
    "One by one, the once-writhing yaoguai spirits turned on their former master. They surged toward him, screeching, weeping, screaming like ghosts freed from torment-and they devoured him."

    yk "AHHH!!! NOOOO!!! NOT LIKE THIS!!!"

    "The psychic chains constricted one final time-a brilliant flash of silver and white light-and then, with an agonizing shriek, the Yaoguai King erupted into dust."
    "Silence fell."
    "Warm hands caught me before I hit the ground. I collapsed against him, gasping for air. My chest ached, my vision flickered. But I felt his arms around me-strong, trembling just slightly."

    show chunghee normal_neutral at left_char

    chung_hee "Dorian, are you alright?"

    "He stared down at me, expression unreadable-but his voice was gentle in my mind, a whisper of moonlight and wind."

    dorian "Chung..."

    "He nodded slowly, brushing the blood from my cheek with care."

    chung_hee "It's alright now. You're safe. I've got you."

    "The weight of everything caught up to me. The battle. Elara. The children. My soul was fraying at the edges."
    "But Chung-hee held me close, shielding me from the cold. He came for me."

    chung_hee "Everything's going to be alright. I'll try to-"

    "A soft whirring sound echoed in the distance."

    show supply_robot normal at right_char with Dissolve(0.2)

    "Supply Bot: Emergency assistance activated. Master Yuxuan suspected that Sir Chung-hee and Master Dorian might need assistance."
    "Supply Bot: He was, as always, correct."

    chung_hee "A supply bot. Thank Renji above for Yuxuan and his intellect."

    "The small metal drone hovered into view, arms outstretched with medkits and healing supplies."

    "Supply Bot: Analyzing injuries. Administering emergency stabilization. Please hold Master Dorian's hand. Studies show physical contact aids recovery."

    chung_hee "Everything's under control, Dorian. I-"

    "My eyelids felt heavy..."
    "And then... the world faded to black..."

    jump ch10_tianho_battle


# =============================================================================
# SECTION 22: LABEL CH10_RESCUE_SVANTE — Svante Rescues Dorian
# =============================================================================

label ch10_rescue_svante:

    "The air shrieked as something whipped past my ear-razor-sharp, blindingly fast."

    play sound sfx_metal_blades                 # PLACEHOLDER — metal blades SFX

    "CLANG!"

    "The Yaoguai King's arm was knocked aside by a gleaming dagger of steel. A flash of silver. A howl of pain."
    "The Yaoguai King's arm exploded in a spray of black ichor."

    yk     "GAHHHH-WHAT?!"

    hide yk
    show svante normal_angry at left_char with Dissolve(0.2)

    "Violet hair, eyes burning with fury. Violet armor slick with battle light."

    dorian "S... Svante?"

    "He didn't look at me. His gaze was locked on the monster in front of him."

    svante "Step. Away. From him."
    yk "You insolent little-"

    "Another blade sliced into the King's shoulder, spraying more blood. Svante raised a single hand."
    "One. Two. Then hundreds of blades shimmered into view-floating, circling him like metal constellations. Long swords. Needles. Daggers. Cleavers. All forged with deadly precision, glinting like judgment."

    svante "I won't ask again."
    yk "Nnnghh-What... what are you?!"

    "A voice rang out-calm, powerful, ancient."

    prosperity_dragon "Svante Nordström. Illegitimate son of King Gustav of Mjoll. A heart forged not from royal blood, but from undying loyalty and courage."
    yk "The... the Prosperity Dragon...?!"

    show yg at right_char with Dissolve(0.2)

    "The Yaoguai King roared, furious, his claws curling as he summoned the shadows."
    "The yaoguai spirits surrounding the Yaoguai King sprang forth-wailing specters of the dead, cloaked in fire and grief. They screeched, lunging toward Svante with blazing teeth and blade-like limbs."

    svante "M-Merciful Enoch..."

    hide yg

    "Svante ran as the swarm of spirits surged toward him. Then, he leapt in midair, meeting the spirits."
    "The pieces of metal surrounding him whirled like a hurricane, cutting through the spectral horde with blinding speed. Spirits were pierced, severed, disintegrated by in flashes of light. Svante advanced with purpose-not one step wasted."
    "He reached the Yaoguai King and pierced his leg, then his shoulder-his jaw shattered beneath a whirling disk of steel."
    "The Yaoguai King shrieked, flailing, but every attempt at retaliation was met by a storm of blades that tore through flesh and armor alike."
    "Blood. Smoke. Steel. Svante was unrelenting."
    "The King staggered, fell to one knee, face twisted in pain and disbelief."
    "Svante took a sword and stabbed the King, tore through the Yaoguai King's chest, straight through heart and spine. The monster arched back, screaming, black flames pouring from his mouth."

    yk "AAAAAGHHHHH-!! NO!!! NOOOOO!!!"

    "The shadows writhed. And then, with one final gasp..."
    "The Yaoguai King collapsed in a heap of soot and shadow, disintegrating into the earth. Silence."
    "A deafening, holy silence."
    "I stumbled, vision blurring. My legs gave out. I fell, but strong arms caught me."

    show svante normal_sad at left_char

    svante "DORIAN!"

    "He pulled me close, clutching me as though I might disappear."

    svante "Hey-hey. Look at me. Eyes open, alright? You're not dying on me. Not now. Not ever. Please..."

    "I gave a weak breath, blood trailing from my lips."

    dorian "You... You saved me..."
    svante "I guess so... D-Dorian, I was so scared. I thought I was too late. I thought I lost you."

    "I tried to say his name again, to tell him I was still here-but the darkness came too fast, too heavy."

    svante "No-no, no, no. Stay with me. Dorian-stay with me!"

    "He looked up, desperation in his eyes."

    svante "HELP! PLEASE! ANYONE!"

    "A soft whirring sound echoed in the distance."

    show supply_robot normal at right_char with Dissolve(0.2)

    "Supply Bot: Emergency assistance activated. Master Yuxuan suspected Master Dorian might be reckless. He was, in fact, correct."

    "The small metal drone hovered into view, arms outstretched with medkits and healing supplies."

    svante "Please! He needs help-now!"

    "Supply Bot: Analyzing injuries. Administering emergency stabilization. Please hold Master Dorian's hand. Studies show physical contact aids recovery."

    svante "Hold on tight, Dorian. Everything-"

    "His voice trailed off. I closed my eyes."
    "And then-darkness."

    jump ch10_tianho_battle


# =============================================================================
# SECTION 23: LABEL CH10_RESCUE_NIKO — Niko Rescues Dorian
# =============================================================================

label ch10_rescue_niko:

    "A sudden howl tore through the shadows."

    play sound sfx_shadow_burst                 # PLACEHOLDER — shadow burst SFX

    "A wind unlike any other ripped through the chamber-freezing cold, black as the void, alive with wrath. The Yaoguai King froze."

    "And then, he was slammed off his feet-hurled across the chamber as a tidal wave of darkness crashed into him."

    yk "Shadows?! I was supposed to be your master! I-!"

    "The shadows screamed."
    "And from the heart of them stepped a figure."

    hide yk
    show niko normal_anger at left_char with Dissolve(0.2)

    dorian "N... Niko?"

    "His face was cold, twisted in rage. Shadows flowed like blood from his fingertips, surpassing the Yaoguai King's. They coiled and snarled like starving wolves, eager to devour."
    "The Yaoguai King lunged from the rubble, claws raised. But Niko didn't flinch."

    yk "You insolent-"

    "With a single flick of Niko's wrist, spears of shadow launched forward-howling through the air like a chorus of executioners. They skewered the Yaoguai King's arm, nailing it to the wall."
    "He screamed, shadows biting into him like venom."

    yk "What-what are you?!"

    prosperity_dragon "Niko Tsukumo. Chosen Champion of the Death God Enoch. Former Healer in the village of Hamatame."
    yk "The... the Prosperity Dragon...?!"

    "The Yaoguai King's eyes widened in horror."

    yk   "You were chosen?! The Dragon talks to you?! But how?! I don't-"
    niko "You hurt him. You dared to pretend to be her. You mocked his pain."

    "He raised both hands, and an enormous ring of shadow erupted around them."

    niko "Your death won't be quick. I want you to remember what fear tastes like."
    yk   "T-These shadows... M-Mercy! I didn't mean to insult the death god! I thought he wasn't supposed to intrude with my killing!"
    niko "I'll tear your soul apart piece by piece."
    yk   "Mercy! Please-PLEASE!"

    "The Yaoguai King screamed as the shadows surged forward-latching onto his limbs, face, chest. His flesh began to burn with a fire blacker than night. His bones cracked. His blood evaporated into mist."

    yk "AHHHHHH-!! NO-NO!! STOP! I BEG-PLEASE-AAAGHHH!!"

    "His skin peeled back. His eyeballs shriveled and popped, leaking black tears. His spine bent backwards as his legs twisted in unnatural angles."
    "The shadows clawed deeper-not just through body, but soul. Memory. Identity. Existence. He was undone."
    "Every lie. Every cruelty. Every scream he'd ever silenced-torn back into the world and used to shred him."
    "He shrank. Withered. Turned to ash. Until there was nothing left."
    "Nothing but soot."
    "Niko remained still. Unblinking. Merciless."
    "The air went still-eerily silent-as if the world itself dared not speak. I felt my legs give out. My body couldn't take it anymore. I collapsed. But strong arms caught me."

    show niko normal_sad at left_char

    niko "DORIAN!"

    "He knelt, cradling me with shaking hands. My vision was fractured-blurry outlines, streaks of red. I tasted iron."

    niko "No-no no no. Look at me. Look at me."

    "He pulled me into his arms. His shaking hands cupped my face, his breath frantic."

    niko "I got you. I got you, okay? You're safe now."

    "His voice cracked."
    "He ripped open his pouch and quickly crushed a handful of dried herbs, shoving the bitter powder into my mouth, followed by a flask of water."

    niko "Swallow. That's it. Come on. Stay awake."
    dorian "N... Niko... You saved me..."

    "My vision dimmed. I could barely see his face anymore."

    niko "You won't die. First, I need to get you to-"

    "A soft whirring sound echoed in the distance."

    show supply_robot normal at right_char with Dissolve(0.2)

    "Supply Bot: Sir Niko detected. Emergency assistance activated. Master Yuxuan suspected Master Dorian might be reckless. He was, in fact, correct."

    "The small metal drone hovered into view, arms outstretched with medkits and healing supplies."

    niko "Hey! Over here! HELP HIM-NOW!"

    "Supply Bot: On it, sir Niko. Hastening services for emergency. Administering trauma-grade stabilizers. Please remain still, Master Dorian."

    niko "Everything will be alright, Dori-"

    "His voice trailed off. I closed my eyes. And then-darkness."

    jump ch10_tianho_battle


# =============================================================================
# SECTION 24: LABEL CH10_RESCUE_MAGNUS — Magnus Rescues Dorian
# =============================================================================

label ch10_rescue_magnus:

    "Magnus: Really? You really want me?"

    "A voice, bright and thundering, cut through the suffocating dark like a blade of sunlight cleaving stormclouds."

    hide yk
    show magnus normal at left_char with Dissolve(0.2)

    magnus "Well, I am absolutely and positively flattered!"

    "From the smoke and ruin, he stepped forward. His golden eyes were ablaze, full of fury. Sweat clung to his face. His chest rose and fell, breath ragged."

    magnus "Then come and face me, demon. Here I am."
    dorian "M... Magnus? No... I-"

    "He ripped off his shirt in one sharp motion, his body glowing with sacred marks. Wings erupted from his back."

    play sound sfx_divine_lance                 # PLACEHOLDER — divine lance SFX

    show magnus clothed_wings at left_char

    magnus "Touch him again and I'll rip your cursed throat out."
    yk     "At last. The Divine Weapon."

    show yk at right_char with Dissolve(0.2)

    "The Yaoguai King hissed and flung me aside like a discarded toy. I hit the ground, groaning weakly. I could barely keep my eyes open."
    "The Yaoguai King laughed manically."

    yk "HAHAHAHAHA!! AT LAST! AT LONG LAST! THE DIVINE WEAPON IS FINALLY MINE!!"
    yk "Now drop to your knees. I want to see you-"

    "He never finished."
    "FLASH."

    yk "Ughhh-ack..."

    hide yk

    "Magnus reappeared behind him, a golden lance piercing straight through the king's chest. Light surged. The Yaoguai King convulsed."

    yk "ARGHHH! What... What are you doing?!"

    prosperity_dragon "Magnus Wyndham. The so-called Divine Weapon. A new man."
    yk     "The... the Prosperity Dragon...?!"

    show yk at right_char with Dissolve(0.2)

    "The Yaoguai King's eyes widened in horror."

    yk     "You were chosen?! The Dragon talks to you?! But how?! I don't-"
    magnus "Aww you're too kind, Dragon. Now if you'll excuse me."

    hide yk

    "He launched skyward, dragging the king with him, wings leaving a burning wake. Then-"

    play sound sfx_draconic_fire                # PLACEHOLDER — fire burst SFX

    "BOOM."

    "A blazing sigil erupted across the underground rooftop, ancient and divine. The king screamed as the flames consumed him-white-hot fire pouring from his eyes and mouth."

    yk "GRAHHH!! NOOO!!! AHHHH!!!"
    magnus "YOU. SHALL. NEVER. TOUCH HIM. AGAIN!"

    "The Yaoguai King exploded in a storm of ash and shadow. The light swallowed it all. And then-Silence."
    "Magnus landed hard beside me, stumbling, dropping to his knees at my side."

    show magnus normal_sad at left_char

    magnus "Dorian? Dorian! Hey-no, no, no, stay with me. Please."
    dorian "M.. Magnus... You... came..."

    "His hands were trembling as he gathered me in his arms, pressing his forehead to mine."

    magnus "You're okay. You're okay. I've got you. Just breathe... You idiot..."
    magnus "Weaver's bollocks, why'd you fight him alone...?"

    "I tried to say his name again, to tell him I was still here-but the darkness came too fast, too heavy."

    magnus "No... No..."
    magnus "PLEASE! SOMEONE HELP! IS THERE ANYONE HERE?!"

    "A soft whirring sound echoed in the distance."

    show supply_robot normal at right_char with Dissolve(0.2)

    "Supply Bot: Sir Magnus detected. Emergency medical protocol online. Master Yuxuan suspected Master Dorian might be reckless. He was, in fact, correct."

    "The small metal drone hovered into view, arms outstretched with medkits and healing supplies."

    magnus "Wh-what? Yuxuan sent you?"

    "Supply Bot: Affirmative. Master Yuxuan stated, quote: 'If Magnus goes after Dorian, which he absolutely will, bring everything and prepare for melodrama.'"

    magnus "Melodrama? I-Never mind, help Dorian!"

    "Supply Bot: Vital signs stabilizing. Continue holding his hand. Data suggests you refusing to let go improves patient survival by 6.8%%"

    "Magnus cradled me close. Then, softly-tenderly-he began to hum."

    magnus "I'll follow you through fire and flame... Wherever you go, I'll bear your name..."

    "Supply Bot: Please be advised that Master Yuxuan advises songs should be reserved until after stabilization."

    magnus "O-Oh! S-Sorry, robot sir. Please-carry on!"
    "Supply Bot: Affirmative."

    magnus "Everything will be-"

    "His voice trailed off. I closed my eyes. And then-darkness."

    jump ch10_tianho_battle


# =============================================================================
# SECTION 25: LABEL CH10_TIANHO_BATTLE — Tianho / Gao / Jiang / Feng Gate
# =============================================================================

label ch10_tianho_battle:

    play music ost_ch10_alert fadein 1.0        # PLACEHOLDER — battle theme

    scene cheng_industries_bunk with flash

    play sound sfx_yaoguai_roar                 # PLACEHOLDER — yaoguai roar

    show soldier_jiang at left_char
    show soldier_gao at right_char
    show yg at center_char
    with Dissolve(0.2)

    jiang "Everyone, fall back! Get inside your homes, now! Barricade the doors!"
    gao   "GO! Don't look back! Get to Cheng Industries!"
    yg    "GRAWWRR!!!"

    jiang "GAO! We've got incoming! Left flank!"
    gao   "I see it!"
    jiang "Nice! You hit it!"

    if love_route_locked == "yuxuan":

        show yuxuan normal_neutral at center_char with Dissolve(0.2)

        yuxuan "Jiang! Gao! Don't do anything reckless! Please-stay sharp, stay alive. My companions will handle the front."
        jiang  "Understood, Master Yuxuan. We'll hold the line. You can count on us."
        gao    "Wouldn't be the first time we've danced with monsters."

        show svante normal_base at left_char with Dissolve(0.2)

        svante "Leave the heavy lifting to us. We'll make sure nothing gets past."
        yuxuan "Alright... We're trusting you. All of you. Make it count."

        show magnus normal at right_char with Dissolve(0.2)

        magnus "I shall scout up in the air. I shall see if there are more yaoguai."
        yuxuan "Oh that's actually a very good idea, Magnus."

        show niko normal_base at left_char with Dissolve(0.2)

        niko   "Everyone! In position! No mistakes. We hold the gate or we die trying."
        yuxuan "Come on, Dorian... wherever you are. Don't die on us now."

    else:

        show chunghee normal_neutral at center_char with Dissolve(0.2)

        chung_hee "Jiang. Gao. Do not act without thought. Stay sharp. Stay alive. My companions will handle the front."
        jiang  "Understood, sir Chung-hee. We'll hold the line. You can count on us."
        gao    "Wouldn't be the first time we've danced with monsters."
        "Female Soldier: We'll fight to our last breath to protect Tianho, my lord!"
        "Male Soldier: I can't believe the Emperor of Kyeongjang is fighting with us! For our children... for every home still standing. For Tianho!"
        chung_hee "To arms! Let the Yaoguai learn that Tianho's spirit does not break. Not now. Not ever."
        chung_hee "Let no yaoguai survive!"
        chung_hee "Dorian... Wherever you are, you have to survive."

    scene bg_tianho_city_night with dissolve

    play sound sfx_yaoguai_roar                 # PLACEHOLDER — yaoguai roar

    show soldier_jiang at left_char
    show soldier_gao at right_char
    with Dissolve(0.2)

    man_1 "HELP! SOMEONE, PLEASE-AHHH!!!"
    yg    "Graawwwr!!"
    jiang "I'll help you, sir! Gao, cover me!"
    gao   "On it, Jiang!"

    hide soldier_jiang
    hide soldier_gao
    show yg at center_char with Dissolve(0.2)

    yg    "Graawwwr!!"

    if feng_score < 2:

        show soldier_jiang at left_char with Dissolve(0.2)
        show soldier_gao at right_char with Dissolve(0.2)

        jiang "GAO! We've got incoming! Left flank!"
        gao   "I see it!"
        jiang "Gao, we failed-AHHH!!! We failed, Gao! I-"
        gao   "JIANG!! LOOK BEHIND YOU!"
        jiang "What the-"

        show yg at center_char with Dissolve(0.2)

        yg    "GRAAAAAAARRR!!"

        play sound sfx_claws                    # PLACEHOLDER — claws SFX

        hide soldier_jiang
        show soldier_gao at right_char

        jiang "ARGHH!!!"
        gao   "JIANG!! NO!! PLEASE!! GET UP!!"
        yg    "GWAAARR!!"
        gao   "No... Please!! No! Not me!! AHHH!!"

        play sound sfx_claws                    # PLACEHOLDER — claws SFX

        hide soldier_gao
        show yg at center_char

        yg "GWAAARR!"

        if love_route_locked == "yuxuan":
            niko "ENOCH ABOVE!! GAO!! JIANG!! NO!!"
        else:
            yuxuan "NO!! GAO!! JIANG!! *cries*"

    else:

        show soldier_jiang at left_char
        show soldier_gao at right_char
        with Dissolve(0.2)

        gao   "JIANG!! LOOK BEHIND YOU!"
        jiang "What the-"
        feng  "GET BACK!"
        gao   "Wait... PALADIN FENG!!"
        feng  "Stay low. You're not dying today."
        jiang "F-Feng?! P-Paladin! SIR!"
        feng  "I've seen too many good people fall today. I won't lose you two. Not tonight."
        yg    "GWAAARR!!"
        feng  "HYAAAA!!"
        gao   "S... So cool...."
        feng  "Heh. Five years of working together and you're crushing on me now, Gao? I'm touched."
        man_1 "Th-thank you! May the Prosperity Dragon bless you!"
        feng  "Get inside. And lock all the damn doors. And for the love of, we told you to get inside!"
        man_1 "Y-Yes, sir!!"
        jiang "Let's move, everyone! Let's move!"

        hide soldier_jiang
        hide soldier_gao
        show feng_suit at center_char with Dissolve(0.2)

        if love_route_locked == "yuxuan":
            niko "Paladin Feng... Seems we'll need to put our differences aside. We're grateful for your help."
        else:
            yuxuan "Paladin Feng!! Oh!! Thank the Prosperity Dragon you're still here..."

        feng "Heh. You're lucky my best friend still owes me a drink. Now-how about we roast some yaoguai? My blue flame's just getting warmed up."

    jump ch10_tianho_aoi


# =============================================================================
# SECTION 26: LABEL CH10_TIANHO_AOI — Babala / Aoi Gate
# =============================================================================

label ch10_tianho_aoi:

    scene tianho_food_stalls_fire with dissolve

    play sound sfx_yaoguai_roar                 # PLACEHOLDER — yaoguai roar

    show babala at left_char with Dissolve(0.2)

    babala "Damned Weaver... I-I can't for the life of me... My arms... they won't respond. I can't channel... not like I used to..."
    male_guard "We already told you to stay inside your homes! Why won't you listen?!"
    female_guard "Mam, please! We have to move-now!"
    babala "I'm trying!"
    babala "I shouldn't have come here. These old bones were never meant for battle. This was foolish..."

    show yg at center_char with Dissolve(0.2)

    yg     "GRAWWWRR!!"
    babala "HELP! Someone-please!"

    if aoi_score < 1:

        hide babala
        female_guard "It's right behind us-AAHHH!!!"
        yg "GRAWWRRRRR!!!"
        babala "ARGHHH!!"
        male_guard "NO! NO!! AHH!!"

    else:

        $ aoi_score += 1
        female_guard "No!! No!!"
        male_guard "Get behind me, mam!"
        yg  "GRAWWRRRRR!!!"
        aoi "Not today."
        yg  "GYAAAAA!!!"

        hide yg
        show aoi_base at center_char with Dissolve(0.2)

        babala "Heavens! What a stunning young woman! Thank the Weaver, you-"
        aoi "Save the flattery. More are coming. Why are you even out here? We told you to evacuate!"
        babala "Alright, alright! No need to shout!"
        aoi "What was that?"
        babala "Nothing! Just grateful, is all. Pft."
        male_guard "That was incredible water channeling... Wait... Aren't you the songstress who performed earlier?"
        aoi "Yes. I'm Aoi. Aoi Mizuhara. Pleasure to meet you."
        aoi "You-come with me. We don't have time to waste."
        aoi "There are more in this sector. I won't let a single one of them leave unscathed. They'll learn what it means to challenge a mistress of water."
        female_guard "Mam!"

        if feng_score >= 2 and aoi_score >= 1:

            show feng_suit at right_char with Dissolve(0.2)

            feng "Well, well... You wear the battlefield well, Lady Aoi. Quite the vision outside your kimono. Long hair really does suit you."
            aoi  "Ugh. Really, Feng? Save the charm for after we've cleaned up this mess. Now move-we're not done yet."
            yg   "GRAWWRRRRR!!!"
            aoi  "To think... they've learned from their attack yesterday."
            feng "Heh. More fun for us. Let's do it. I'll even give you a nice bonus if we survive."
            aoi  "Agreed. You're on. It would be an opportunity to go all out with my water channeling."
            feng "And me with my blue fire."
            feng "Side by side, you and me? These yaoguai won't know what hit them."
            feng "They will be sorry they messed with Tianho."

    jump ch10_epilogue


# =============================================================================
# SECTION 27: LABEL CH10_EPILOGUE — Prosperity Dragon Narration / Kitchen / Sail
# =============================================================================

label ch10_epilogue:

    scene bg_tianho_city_morning with fade
    stop music fadeout 2.0
    play music ost_ch10_aftermath fadein 2.0    # PLACEHOLDER — aftermath / hopeful theme

    prosperity_dragon "And so, the attack on Tianho was repelled. The fires of war were extinguished not by luck, but by the bravery of those who stood unwavering in the face of despair."
    prosperity_dragon "Among them... one still rests."
    prosperity_dragon "Dorian-the Dragon of Gale, bearer of grief, fire, and unyielding will-now lies in recovery, his body battered, but his soul no longer burdened by vengeance."
    prosperity_dragon "When he awoke, it was not to battle horns or the roar of flame, but to a familiar warmth. A small hand in his own. A voice, soft and sweet."

    show elias normal_happy at right_char_kids with Dissolve(0.2)

    elias "Daddy! You're awake!"

    show roboto normal at left_char with Dissolve(0.2)

    "Supply Bot: Vitals stable. Blood pressure within optimal range. Neural activity increasing... Welcome back, Master Dorian."

    prosperity_dragon "The weight that had pressed on his heart for so long finally lifted in that moment. For the first time in what felt like lifetimes... he breathed without ache."
    prosperity_dragon "And beside him, the one who had saved him-the partner who stood between him and death-remained close."
    prosperity_dragon "To him, Dorian knew only gratitude. And perhaps, something deeper."
    prosperity_dragon "The Yaoguai King was no more. Justice-delayed, but never denied-was finally delivered. His family could rest. And so, too, could he."
    prosperity_dragon "The flames of revenge no longer consumed him. In their place... new embers flickered. Softer ones. Hopeful ones."
    prosperity_dragon "Dorian now stands at the edge of a new chapter. Not written in blood or fury-but perhaps... in love."
    prosperity_dragon "As for our tale... it is not yet over."

    scene yuxuan_lab with dissolve

    show yuxuan normal_neutral at left_char
    show weng normal at right_char
    show magnus normal at center_char
    with Dissolve(0.2)

    "I gathered everyone in the kitchen. I told them everything. About Magnus. About the Yaoguai King. About the Divine Weapon."

    yuxuan "Wait... so let me get this straight. Magnus is a clone of the Death God?!"
    weng   "By the stars... I can't believe it. The Death God..."

    show magnus normal_alt_neutral at center_char

    "Magnus sat off to the side, silent, his brows furrowed in confusion. I didn't blame him."

    magnus "I... don't really feel like a clone. I don't even know what that means. I have memories. Feelings. I've laughed, cried, bled. How do you explain that?"

    show svante normal_base at right_char with Dissolve(0.2)

    svante "I'm with Magnus. I haven't seen clones before. But I know he's not one. He's real to me. Maybe the Yaoguai King was just trying to mess with your head."

    show niko normal_base at left_char with Dissolve(0.2)

    niko   "I highly doubt that. Normally, I'd call it blasphemy outright. But considering that the Prosperity Dragon is involved with this... it aligns. All too well."

    show chunghee normal_neutral at right_char with Dissolve(0.2)

    chung_hee "If what you're saying is true, I can take Magnus back to Kyeongjang with me. If he really is the Divine Weapon, we can't risk him falling into King Gustav's hands."
    svante "My father would never harm Magnus. He has merciful and kind tendencies! I don't think he'll want to doom us all."
    elias  "Ooh! Can I come? I wanna go to Kongjong!"
    tim    "I'd be honored to visit Kyeongjang!"
    tedda_alive "ME THREE! I WANNA GO TOOOO!"
    weng   "Kids, hush now. Don't interrupt the adults. Roboto, could you get them some snacks before they break my back and my nerves?"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep

    roboto "R-R-R-Right away, Miss Weng. Snacks incoming."

    dorian "We need answers first, Chung. We need to know why the Divine Weapon was created. What its purpose is. Who it was meant to destroy-or protect."
    niko   "To think they caged the reincarnation of the Death God for four hundred years. Encased in some wretched contraption like a tool, a thing!"
    niko   "Have the great kings of Ena know no shame? Enoch weeps for what they've done! Heresy! Apostasy! No amount of gilded temples will cleanse that sin!"
    yuxuan "Calm down, Niko. Calm down."
    dorian "The Yaoguai King said... he overheard two rulers speaking about it. King Long Shen of Tianho. And King Tatsuya Fujiwara of Hinami."

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep

    roboto "U-Unfortunately, K-K-King Long Shen has long been deceased. No further logs are available on his activities."
    yuxuan "Then we turn to the other. King Tatsuya of Hinami."

    show dorian normal_alt_tense at left_char with Dissolve(0.2)

    "I looked down, my fists tight."

    dorian "I need to go. But... after everything that's happened, I don't think I want to go alone. Will some of you come with me?"

    "Chung-hee placed a hand on my shoulder."

    chung_hee "You have me, Dorian. I'd use the Amulet of Teleportation, but it's only stable for one person at a time. We'll need another route."
    tim   "I volunteer! I may be small, but I can catalog everything! Diplomats always bring scholars."
    elias "Daddy I wanna come too! I wanna go swimmwing!"

    "I winced. The thought of them anywhere near danger twisted in my gut like a blade."

    dorian "Elias... Tim... I'm sorry. It's too dangerous. You'll have to stay here where it's safe."
    weng   "That's final. Listen to the adults, little ones. Tim, you stay here and play with Elias. There's plenty of adventure in stories and sweets."
    tim    "WHAAAT?! But I wanted to wear my sailor hat!!"
    yuxuan "Luckily for all of us-I have just the thing. A luxury boat, custom-built, smooth as silk and fast as wind. Enough beds for everyone, even Tedda. And the kitchen makes warm bao buns on demand."
    tedda_alive "Yeyyy!! Does that mean I'll be coming along?"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep

    roboto "No, Miss Tedda. You'll stay in the lab and c-c-c-clean up after Lady Elias. And maybe assist in kitchen duties if you don't burn rice again."
    tedda_alive "Aww boo..."
    niko   "Dorian, you'll need someone who knows the island. I'll go. For Enoch. And for the truth they've long buried."

    show magnus normal at center_char

    "Magnus looked up from where he sat-his carefree demeanor dimmed. His eyes serious now, thoughtful."

    magnus "I... I'll go. I need to know who I really am. I need to understand what this 'Divine Weapon' means."
    svante "I'm happy for you, Magnus. This will be a step in knowing who you actually are."
    magnus "Thank you, Svante."
    svante "I'm also in. I've never been to Hinami before, and honestly? I wanna see the beaches."
    magnus "Wait... beaches?"

    play sound sfx_roboto_beep                  # PLACEHOLDER — Roboto beep

    roboto "Yes. Hinami's coastal line is considered one of the most breathtaking in all Ena. T-T-Turquoise waters. Shimmering white sand."
    roboto "Crystal-clear coves. And the sunsets? Like fire melting into the sea. P-P-P-People write poetry about it. Some even propose there."
    magnus "WOOHOO!!! BEACH TRIP!!! Let's go swimming!!"
    niko   "Oh brother."
    magnus "Svante! Let's go swimming once we're there!"
    svante "Of course! We probably deserve a little sun! I remember me and my fellow aldoriths bathing in the waterfall in Mjoll! I can't imagine swimming in a beach! It must be fun!"
    yuxuan "Everyone, please! This isn't vacation time, we-"

    "Magnus leaned over and whispered something."

    yuxuan "D-D-Dorian in... Magnus: Absolutely..."
    yuxuan "I-I-I CHANGE MY MIND! Everyone pack your swimwear!!"
    niko   "Well, if the opportunity arises, I suppose a little dip wouldn't hurt. Hinami does have quite a few resorts, after all."
    svante "A white sandy beach... Is it really that beautiful?"
    niko   "As someone born there... yes. The beaches of Hinami are magic made real. Waters that glow under moonlight. Tide pools with starfish that shimmer."
    niko   "They don't exaggerate. It is beautiful. And the castle of Hinami? It floats upon the sea itself."
    yuxuan "What? How do they do that?"
    niko   "Water channelers. Probably empowered by the Dragon of the Depths... or some ancient art lost to time. Nobody really knows."
    magnus "I can't wait! Hinami, here we come!"
    elias  "No faiw!! Daddy!! That's so unfaiw!!"
    tim    "Elias... maybe it's time for Operation: Sneak-Aboard. Listen carefully. Here's the plan-"

    "Chung-hee approached me, rubbing his temples."

    chung_hee "Well... these people sure are excited."
    dorian    "Tell me about it..."
    weng      "Don't worry, Sir Dorian. I'll take care of Elias. He'll be safe here-with Tim, Tedda, and Roboto. He'll be happy."
    chung_hee "I'm sorry you're not feeling well enough to join us, Miss Weng."
    weng      "It's alright, sir Chung. I'll be fine here with the little ones. A good cup of tea and some poetry by Takayori Sogen will keep me company."
    chung_hee "That's it, everyone. We leave at first light. Prepare yourselves."

    "And just like that, the decision was made."
    "Tomorrow-we set sail. To Hinami."

    jump ch10_credits_scene


# =============================================================================
# SECTION 28: LABEL CH10_CREDITS_SCENE — End Credits Scene: Gustav / Cyrus
# =============================================================================

label ch10_credits_scene:

    scene black with fade
    stop music fadeout 2.0
    pause 1.0

    "( Credits )"

    scene destroyed_land with fade
    play music ost_ch10_credits fadein 2.0      # PLACEHOLDER — ominous credits theme
    play sound sfx_carriage_rumble              # PLACEHOLDER — carriage rumble SFX

    show king_gustav at left_char
    show cyrus at right_char
    with Dissolve(0.2)

    "The imperial carriage rumbled down the muddy trail, wheels slick with rainwater. Thunder cracked in the distance, the sky bruised with approaching storm."

    king_gustav "Damn that Yaoguai attack. Everything has to fall apart the moment I take a detour."
    cyrus "You seem surprised, Gustav. Monsters rarely wait their turn."
    cyrus "Besides, you'll be inside the comfort of your castle soon."

    "The carriage lurched slightly. A knock sounded. The door creaked open to reveal three kneeling figures-hooded Aldoriths, rain dripping from their cloaks."

    show boy_ald_normal at center_char with Dissolve(0.2)

    boy_ald "Father... we are humbly asking for your permission to-"
    cyrus   "CAN'T YOU SEE HE IS TALKING TO ME?!"
    boy_ald "F-Forgive us..."
    king_gustav "Cyrus. Calm yourself. It's alright... My children, speak."
    boy_ald "Thank you Father. I appreciate your kindness."
    girl_ald "Father, forgive the intrusion. We bring urgent news."
    boy_ald "We found him. Our brother... Svante. He lives."

    show king_gustav normal_alt_anger at left_char

    "King Gustav's eyes narrowed, tension rising in his shoulders."

    girl_ald "We wished to bring him to you... but..."
    king_gustav "But what?"
    girl_ald "He is not alone. He travels with others. A man named Dorian... and others whose names we don't know."
    king_gustav "Dorian?! What?!"
    boy_ald "There is also one who is called Magnus."
    king_gustav "Magnus?"
    boy_ald "Yes, Father. He has wings. And he burns with light."
    mjoll_lars "We compared your past descriptions, Father. The signs match."
    mjoll_helga "According to your descriptions, we believe he's the Divine Weapon."
    cyrus "And? Are you certain of this information? We don't tolerate false information."
    mjoll_helga "As certain as breath and bone, Paladin Cyrus."
    mjoll_lars "We also inspected the sealed chamber, as you taught us. The seal was ultimately broken."
    mjoll_lars "The area was in utter disarray. Scorched stone. Scattered feathers. A battle, by all signs."
    cyrus "Dorian and Magnus... Interesting."
    king_gustav "Enoch above... The Divine Weapon."

    "A long silence fell, punctuated only by the rolling wheels and distant thunder."

    girl_ald "Our agents in Tianho saw them together... just yesterday."
    king_gustav "INSOLENCE! You took too long to report this! TURN THE DAMN CARRIAGE AROUND! I want to-"
    cyrus "Back to Tianho? Don't bother. You'll only be wasting your time, Gustav."
    king_gustav "You think they're not in Tianho anymore?"
    cyrus "No, they're not. I feel it. A pull in my blood. In my bones."
    cyrus "They're either headed towards the Empire of Gale or the Island of Hinami."
    cyrus "But if I were to bet my coin, I'd place it on Hinami."
    mjoll_helga "But... Paladin. Forgive me-but the ferries bound for Hinami are booked solid because of the festivities of the anniversary of the tragedy."
    mjoll_lars  "Helga, stop questioning the Paladin."
    mjoll_helga "I'm not, Lars! But there's no passage left for them to go to the Kingdom of Hinami! We-"
    cyrus "Then that narrows it down. Who in Tianho is powerful or influential enough to reach the Island of Hinami without needing a ferry?"

    "He leaned forward slightly."

    cyrus "Tell me, Gustav. Which king failed to attend the rulers' meeting during the Tragedy of Tianho?"
    king_gustav "Tatsuya..."

    "King Gustav froze."

    king_gustav "Hinami..."

    "[ DEMO OVER ]"

    scene black with fade
    stop music fadeout 3.0
    pause 2.0

    return


# =============================================================================
# SECTION 29: LABEL CH10_BAD_END_CREDITS — GAME OVER / BAD END Credits
# =============================================================================

label ch10_bad_end_credits:

    scene black with fade
    stop music fadeout 1.0
    play music ost_ch10_bad_end fadein 1.0      # PLACEHOLDER — bad end music

    "GAME OVER - BAD END / CREDITS"

    prosperity_dragon "The savior is gone. The one who could have rescued Ena lies dead."

    "The dragon's massive head lowered, smoke billowing from its nostrils as it turned its gaze to the horizon, where darkness gathered like a storm."

    prosperity_dragon "And now... who will save them?"

    "The land of Ena lay silent, its fate uncertain. The savior-its last hope-was gone."

    "( CREDITS )"

    scene black with fade
    stop music fadeout 3.0
    pause 2.0

    return


# =============================================================================
# END OF CHAPTER 10
# =============================================================================