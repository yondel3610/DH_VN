###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  SCENE: PROLOGUE — Tianho Underground
#
###############################################################################

# =============================================================================
# SECTION 1: CHARACTER DEFINITIONS
# =============================================================================
#centralized character definitions

# =============================================================================
# SECTION 2: IMAGE DECLARATIONS
# =============================================================================

# centralized bg/cg file

# TODO: check image folder again, illus and bg
# --- CG / Event Images (full screen, fit to cover) ---
image cg_black:
    "images/cg/cg_black.png"
    zoom 2.26 

# =============================================================================
# SECTION 3: AUDIO DECLARATIONS
# =============================================================================
# TODO: file paths
# --- Ambient ---

# =============================================================================
# SECTION 4: CUSTOM SCREENS (for prl only)
# =============================================================================

define flash = Fade(0.1, 0.0, 0.1, color="#fff")

# -----------------------------------------------------------------------------
# 4.2 CHAPTER TITLE SCREEN
# -----------------------------------------------------------------------------
screen chapter_title_screen(chapter_num, chapter_title, subtitle="", duration=2.0):
    timer duration action Hide("chapter_title_screen")
    frame:
        background None
        xfill True
        yfill True
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            text "CHAPTER [chapter_num]" size 48 color "#ffcc88"
            text chapter_title size 36 color "#ffffff"
            if subtitle:
                text subtitle size 20 color "#ccccaa" italic True

# =============================================================================
# SECTION 5: GAME VARIABLES (added to a compiled file)
# =============================================================================

# default prologue_choice = ""
# default quick_timer_active = False
# default tutorial_shown = False

# =============================================================================
# SECTION 6: PROLOGUE LABEL
# =============================================================================
label prologue:
    $ save_name = "Prologue"
    # -------------------------------------------------------------------------
    # OPENING — Silence and darkness
    # -------------------------------------------------------------------------
    scene black with fade
    pause 0.5
    

    # $ renpy.save(new_slot, extra_info=save_name)

    # --- Opening narration ---
    "{i}Let their spirits pass without suffering. Let their memories remain unspoiled.{/i}" 
    "{i}Let Your cloak be warm. Let their burdens fall at Your feet, Almighty Enoch.{/i}" 
    
    "A young woman with silver hair knelt in the dust and shadow, her fingers cold against the bloodspattered floor."
    "The torchlight flickered against her trembling form. She closed her eyes and spoke softly, her voice barely more than a breath."
    scene kristin_kneeling with fade

    voice audio.kristin_ald_prl_line1
    kristin "Grant me strength to carry out your will: to lay these bodies to rest with reverence, to honor their passage, and to usher them into your sacred silence."
    scene underground_prl with fade
    # --- Aldorith soldiers enter ---
    "Two aldorith soldiers stood at the threshold, their faces sharp with impatience, their breath fogging faintly in the chill of the underground."

    show boy_ald_normal at left_char
    show girl_ald_normal at right_char
    with Dissolve(0.2)
    
    voice audio.boy_ald_prl_line1
    boy_ald "She's still praying. It's been five minutes."
    #voice audio.girl_ald_prl_
    girl_ald "You're right. We cannot linger. The rot will draw attention."
    
    "Kristin's voice quivered as she continued to whisper her prayer—begging Enoch to take their souls gently."
    "To let them find peace. To weigh the sins of the living, not the dead."
    
    voice audio.boy_ald_prl_line2
    boy_ald "Enough of this, Kristin."

    hide boy_ald_normal 
    hide girl_ald_normal
    "Kristin flinched as if struck. She turned, eyes wide, lips pale."

    show kristin_normal at center_char with Dissolve(0.2)

    voice audio.kristin_ald_prl_line2
    kristin "I was only… I was praying to Lord Enoch."

    show girl_ald_normal at right_char with Dissolve(0.2)
    #voice audio.girl_ald_prl_
    girl_ald "A prayer that's lasted too long. For minutes, sister. We've listened. Are you certain you're not harboring doubts?"
    
    voice audio.kristin_ald_prl_line3
    kristin "D-Doubts? No, sister."
    voice audio.kristin_ald_prl_line4
    kristin "But… What we did—what happened—was it really right? We killed the queen and her two sons."
    
    show boy_ald_normal at left_char with Dissolve(0.2)
    voice audio.boy_ald_prl_line3
    boy_ald "What are you saying? That our Father was wrong?"
    voice audio.kristin_ald_prl_line5
    kristin "N-no! I would never—why would I?"
    
    show girl_ald_normal at right_char

    #voice audio.girl_ald_prl_
    girl_ald "Your blood-brother Svante didn't hesitate. He slit their throats without blinking. He was useful. You? You pray for corpses."
    voice audio.boy_ald_prl_line4
    boy_ald "Useless."
    
    "Kristin dropped her gaze. Her hands trembled at her sides."
    
    show kristin_normal at center_char
    
    voice audio.kristin_ald_prl_line6
    kristin "I'm very sorry… I just—"
    voice audio.boy_ald_prl_line5
    boy_ald "We don't need you anymore. You're only stalling."
    voice audio.boy_ald_prl_line6
    boy_ald "Count Vasily might have better use for someone like you."
    
    # --- Kristin leaves ---
    "She didn't argue. With her head bowed and hands trembling at her sides, Kristin turned and walked away."
    "Her footsteps echoed faintly down the underground tunnel—slow and hesitant."
    
    hide kristin_normal with dissolve
    
    "The two Aldoriths watched her disappear into the dark before exchanging a glance."
    "Their gazes drifted to the lifeless forms behind them: the Queen of Tianho, regal even in death, and her two sons, wrapped in the stillness of final silence."
    voice audio.boy_ald_prl_line7
    boy_ald "That Kristin… soft-hearted as ever."
    #voice audio.girl_ald_prl_line
    girl_ald "She won't last. We both know Father only kept her around to control Svante."

    "They moved wordlessly to the bodies, the ritual of burial unfolding with grim familiarity."
    "Cloth unrolled. Blood wiped. Limbs bound with reverent efficiency."
    "Their hands worked swiftly—mechanical, practiced—but there was a flicker of hesitation behind their eyes."

    voice audio.boy_ald_prl_line8
    boy_ald "Why do you think Father really wanted them dead?"
    girl_ald "I don't know. And I really don't plan to ask. Best not to chase answers when you're already neck-deep in secrets."
    
    "She reached for the Queen's hand, cold and graceful, and began to wrap the burial cloth tight around her wrist."
    
    voice boy_ald_prl_line9
    boy_ald "This feels… different. We've carried out assassinations before, but never like this."
    voice boy_ald_prl_line10
    boy_ald "A queen. Two princes. Royals of Tianho."
    #voice audio.girl_ald_prl_
    girl_ald "Exactly why we need to hurry. If anyone finds out what's buried down here—before the earth swallows it whole—we're finished."


    voice audio.boy_ald_prl_line11
    boy_ald "Still… Svante didn't even blink. Just walked in and—"
    #voice audio.girl_ald_prl_
    girl_ald "Cold as stone. That's why he's Father's favorite. A metal channeler with no hesitation? That's worth more than loyalty."
    #voice audio.girl_ald_prl_
    girl_ald "Which is why he still keeps that skank Kristin…"
    
    "She tied the final knot, sealing the last shroud."
    "The flickering torchlight danced across the linen, casting their silhouettes long and stretched across the stone."
    
    #voice audio.girl_ald_prl_
    girl_ald "And you should remember that."

    "A breath passed between them."

    play sound ost_tension_short
    # TENSION RISES — Something is wrong
    "A pressure, subtle at first, then sudden and suffocating, pressed down on the tunnel."
    "The torches guttered, flames trembling like they, too, felt the change."
    
    # play music ost_tension volume 0.3 fadein 3.0

    voice boy_ald_prl_line12
    boy_ald "D-Do you feel that?"
    
    
    "A shriek—deep, guttural, wrong—ripped through the silence."
    
    #voice audio.girl_ald_prl_
    girl_ald "Did you hear that?"
    
    # -------------------------------------------------------------------------
    # YAOGUAI KING ENTRANCE
    # -------------------------------------------------------------------------

    play sound sfx_yaoguai_burst
    scene underground_prl with flash
    
    play music yaoguai_theme volume 0.8
    
    "The wall exploded inward, a mass of claws, horns, and red-hot eyes surging forward."
    "The Yaoguai King emerged from the rubble, obsidian-scaled and crowned in bone, the shadows clinging to his form like loyal hounds."
    
    show yk at center_char with Dissolve(0.5)
    
    voice audio.yk_ald_prl_line1
    yk "You bury corpses… while your own hearts still beat? How generous. More for my yaoguai to feed on."

    show girl_ald_normal at right_char 
    show boy_ald_normal at left_char
    with Dissolve(0.2)


    #voice audio.girl_ald_prl_
    girl_ald "Enoch above…"
    voice boy_ald_prl_line13
    boy_ald "Sister, run!! I'll hold him off-!"
    
    "He slammed his palm to the ground, trying to channel earth. A ripple of stone shifted—but it was too late."
    "The Yaoguai King blurred. One moment he was across the chamber—"
    "The next, he was upon them."
    
    play sound sfx_body_thud
    scene bg_underground_red with flash
    pause 0.4
    # scene bg_underground_red with dissolve
    
    #voice audio.girl_ald_prl_
    girl_ald "AHHH!!! NO!!!"
    
    "His claws tore through the air and the girl aldorith fell, her body thudding against the stone in a lifeless heap." with hpunch
    # scene bg_underground_red with flash
    show boy_ald_normal at left_char with Dissolve(0.2)

    voice boy_ald_prl_line14
    boy_ald "SISTER!!"
    
    show yk at right_char with Dissolve(0.2)

    voice audio.yk_ald_prl_line2
    yk "Your turn, little one…"

    $ _choice_timeout = 5.0
    menu:
        "Dash toward the entrance of the burial tunnel.":
            $ _choice_timeout = 0
            jump prologue_choice_dash
        "Try to raise a stone wall.":
            $ _choice_timeout = 0
            jump prologue_choice_wall

# =============================================================================
# SECTION 7: QTC BRANCH LABELS
# =============================================================================

label prologue_choice_wall:
    
    $ prologue_choice = "wall"
    stop sound
    
    "He dropped to one knee, forcing all his will into the trembling ground."
    
    voice boy_ald_prl_line15
    boy_ald "Come on, come on—!"
    
    "A slab of earth surged upward between him and the Yaoguai King."
    "Then—CRACK!"
    
    play sound sfx_stone_break
    
    "A single claw punctured through the wall—then shattered it in one swipe."
    "The force sent him flying, crashing against the tunnel wall."
    
    #scene cg_boy_ald_wall with flash
    pause 0.3
    scene bg_underground_red with Dissolve(0.4)
    
    voice boy_ald_prl_line16
    boy_ald "ARGHH!!!"
    
    "His ribs burned. Blood filled his mouth."
    
    voice boy_ald_prl_line17
    boy_ald "—gkkhh—!"
    
    "He collapsed."
    
    jump prologue_common


label prologue_choice_dash:
    
    $ prologue_choice = "dash"
    stop sound
    
    "He bolted down the side corridor, heart hammering."
    
    show boy_ald_normal at left_char

    voice boy_ald_prl_line18
    boy_ald "Come on… Come on…"
    
    voice audio.yk_ald_prl_line3
    yk "Running away from me? Pathetic."
    
    "He didn't make it ten steps."
    "Too fast."
    "A blur. A slash. A body fell."
    
    scene bg_underground_red with flash
    pause 0.4
    scene bg_underground_red with dissolve
    jump prologue_common

# =============================================================================
# SECTION 8: COMMON ENDING
# =============================================================================

label prologue_common:
    
    stop music fadeout 2.0
    
    "Silence returned—oppressive and final."

    show yk at center_char with Dissolve(0.4)
    
    "The Yaoguai King stood among the dead. His eyes drifted to the bodies wrapped in burial cloth: a queen and two princes, now claimed by darkness."
    
    "He inhaled deeply, tasting the air."
    
    voice audio.yk_ald_prl_line4
    yk "Three royal corpses, wrapped so lovingly… yet buried in secret…"
    voice audio.yk_ald_prl_line5
    yk "And not a whisper in the winds? No fanfare. No grief. No mourning bells."
    
    "His eyes narrowed. Slowly, he stepped closer to the bodies, talons clicking against the stone."

    scene bg_underground_red with dissolve
    
    voice audio.yk_ald_prl_line6
    yk "That old man… What are you plotting?"
    
    "He leaned down, baring rows of jagged teeth."
    
    voice audio.yk_ald_prl_line7
    yk "Tianho… it seems your game has begun again. And I've always loved a good hunt."
    
    # -------------------------------------------------------------------------
    # FADE OUT
    # -------------------------------------------------------------------------
    window show dissolve
    scene black with fade
    stop audio fadeout 1.5
    
    pause 1.5
    
    # -------------------------------------------------------------------------
    # CHAPTER TITLE CARD
    # -------------------------------------------------------------------------
    show screen chapter_title_screen("1", "Lorem Ipsum", "Lorem Ipsum", duration=3.0)
    pause 3.0
    
    # -------------------------------------------------------------------------
    # TRANSITION TO CHAPTER 1
    # -------------------------------------------------------------------------
    jump chapter_1

# =============================================================================
# END OF PROLOGUE
# =============================================================================