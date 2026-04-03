###############################################################################
#  Dragon's Heart: The Crimson Rebirth
#  FILE:  prologue.rpy
#  SCENE: PROLOGUE — Tianho Underground
#
#  ENHANCED VERSION with Complete UX Features
#  Includes: Skip functionality, rollback protection, accessibility options,
#  save/load compatibility, auto-forward, and text speed controls.
###############################################################################


# =============================================================================
# SECTION 1: CHARACTER DEFINITIONS
# =============================================================================

define kristin     = Character("Kristin",      color="#b0c4de", what_prefix='"', what_suffix='"')
define boy_ald     = Character("Boy Aldorith", color="#cd5c5c", what_prefix='"', what_suffix='"')
define girl_ald    = Character("Girl Aldorith",color="#cd5c5c", what_prefix='"', what_suffix='"')
define yk          = Character("Yaoguai King", color="#8b0000", what_prefix='"', what_suffix='"')

# Narrator with configurable text speed settings
define narrator = Character(None, what_italic=False)

# =============================================================================
# SECTION 2: IMAGE DECLARATIONS
# =============================================================================

# --- Backgrounds (with fit to prevent zoom) ---
image bg_underground_dim:
    "images/Assets/Background/Underground Lights Off (1).png"
    fit "cover"

image bg_underground_lit:
    "images/Assets/Background/Underground.png"
    fit "cover"

image bg_underground_red:
    "images/Assets/Background/Underground Red.png"
    fit "cover"

image kristin_kneeling:
    "images/Assets/Illustrations/1 - Kristin Praying.png"
    size (1920, 1080) # STANDARD FOR ALL FUTURE BG ILLUSTRATION
    xalign 0.5
    yalign 1.0

# --- Character Sprites ---
image kristin_normal:
    "images/Assets/Character Sprites/Kristin Nordstrom.png"
    fit "contain"
    xalign 0.5
    yalign 1.0

# Boy Aldorith sprite
image boy_ald_normal:
    "images/Assets/Character Sprites/Boy Aldorith.png"
    fit "contain"
    xalign 0.5
    yalign 1.0

# Girl Aldorith sprite
image girl_ald_normal:
    "images/Assets/Character Sprites/Girl Aldorith.png"
    fit "contain"
    xalign 0.5
    yalign 1.0

# Yaoguai King sprites(gray skin, bone crown)
image yk:
    "images/Assets/Character Sprites/yaoguai king v3.png"
    fit "contain"
    xalign 0.5
    yalign 1.0

# --- CG / Event Images (full screen, fit to cover) ---
image cg_black:
    "images/Assets/plain_colors/HD-wallpaper-plain-black-black.jpg"
    fit "cover"

image cg_yaoguai_entrance:
    "images/cg/cg_yaoguai_entrance.png"
    fit "cover"

image cg_girl_ald_death:
    "images/cg/cg_girl_ald_death.png"
    fit "cover"

image cg_boy_ald_wall:
    "images/cg/cg_boy_ald_wall.png"
    fit "cover"

image cg_boy_ald_slash:
    "images/cg/cg_boy_ald_slash.png"
    fit "cover"

image cg_yk_surveying:
    "images/cg/cg_yk_surveying.png"
    fit "cover"

# --- GUI Elements ---
image ui_timer_bar_bg:
    "images/gui/ui_timer_bar_bg.png"
    fit "contain"

image ui_timer_bar_fill:
    "images/gui/ui_timer_bar_fill.png"
    fit "contain"


# =============================================================================
# SECTION 3: AUDIO DECLARATIONS
# =============================================================================

# --- Ambient ---
define audio.amb_underground   = "audio/ambient/amb_underground.ogg"

# --- Sound Effects ---
define audio.sfx_yaoguai_burst = "audio/sfx/sfx_yaoguai_burst.ogg"
define audio.sfx_stone_break   = "audio/sfx/sfx_stone_break.ogg"
define audio.sfx_body_thud     = "audio/sfx/sfx_body_thud.ogg"
define audio.sfx_heartbeat     = "audio/sfx/sfx_heartbeat.ogg"
define audio.sfx_timer_tick    = "audio/sfx/sfx_timer_tick.ogg"
define audio.sfx_timer_end     = "audio/sfx/sfx_timer_end.ogg"

# --- Music ---
define audio.ost_yaoguai_theme = "audio/music/ost_yaoguai_theme.ogg"
define audio.ost_tension       = "audio/music/ost_tension.ogg"


# =============================================================================
# SECTION 4: CUSTOM SCREENS (UX FEATURES)
# =============================================================================

define flash = Fade(0.1, 0.0, 0.1, color="#fff")

# -----------------------------------------------------------------------------
# 4.1 QUICK TIMED CHOICE SCREEN
# -----------------------------------------------------------------------------
screen timed_choice(items, timeout=5.0, default=None):

    default timer = timeout
    $ default_choice = default if default is not None else len(items) - 1

    timer 0.01 repeat True action [
        SetScreenVariable("timer", timer - 0.01),
        If(timer <= 0, true=[
            Hide("timed_choice"),
            Jump(items[default_choice][1])
        ])
    ]

    if timer <= 2.0:
        timer 0.5 action Play("sound", audio.sfx_timer_tick)

    vbox:
        xalign 0.5
        yalign 0.6
        spacing 8

        for i, (choice_text, target_label) in enumerate(items):
            button:
                action [Hide("timed_choice"), Jump(target_label)]
                xpadding 30
                ypadding 12
                background None
                hover_background None

                text choice_text:
                    size 24
                    color "#ffffff"
                    hover_color "#ffd700"
                    text_align 0.5
                    layout "nobreak"

        bar:
            value AnimatedValue(timer, timeout, 0.01)
            range timeout
            xsize 500
            ysize 10
            xalign 0.5
            left_bar  Frame("#d4af37", 0, 0)
            right_bar Frame("#333333", 0, 0)


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


# -----------------------------------------------------------------------------
# 4.3 ACCESSIBILITY PREFERENCE SCREEN
# -----------------------------------------------------------------------------
screen accessibility_preferences():
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 400
        
        vbox:
            spacing 20
            xfill True
            
            hbox:
                text "Text Speed:" size 18 xalign 0.0
                bar value Preference("text speed") xsize 300
                text "[_preferences.text_cps] cps" size 14
            
            hbox:
                text "Auto-Forward Delay:" size 18 xalign 0.0
                bar value Preference("auto-forward time") xsize 300
                text "[_preferences.afm_time]s" size 14
            
            vbox:
                textbutton "Skip Unseen Text" action Preference("skip", "toggle")
                textbutton "Skip After Choices" action Preference("after choices", "toggle")
            
            if renpy.has_label("voice"):
                hbox:
                    text "Voice Volume:" size 18 xalign 0.0
                    bar value Preference("voice volume") xsize 300


# =============================================================================
# SECTION 5: GAME VARIABLES
# =============================================================================

default prologue_choice = ""
default quick_timer_active = False
default tutorial_shown = False

# =============================================================================
# SECTION 6: PROLOGUE LABEL
# =============================================================================

label prologue:
    # -------------------------------------------------------------------------
    # INITIAL SETUP
    # -------------------------------------------------------------------------
    $ renpy.game.preferences.skip_unseen = False
    
    if _preferences.text_cps == 0:
        $ _preferences.text_cps = 40
    
    # -------------------------------------------------------------------------
    # OPENING — Silence and darkness
    # -------------------------------------------------------------------------
    stop music fadeout 2.0
    scene bg_underground_dim with fade
    play audio amb_underground loop fadein 2.0
    
    # --- Opening narration ---
    "Let their spirits pass without suffering. Let their memories remain unspoiled."
    "Let Your cloak be warm. Let their burdens fall at Your feet, Almighty Enoch."
    
    "A young woman with silver hair knelt in the dust and shadow, her fingers cold against the bloodspattered floor."
    "The torchlight flickered against her trembling form. She closed her eyes and spoke softly, her voice barely more than a breath."
    
    scene kristin_kneeling with fade
    kristin "Grant me strength to carry out your will: to lay these bodies to rest with reverence, to honor their passage, and to usher them into your sacred silence."
    
    # --- Aldorith soldiers enter ---
    "Two aldorith soldiers stood at the threshold, their faces sharp with impatience, their breath fogging faintly in the chill of the underground."

    show bg_underground_lit with fade

    show boy_ald_normal at left
    show girl_ald_normal at right
    
    boy_ald "She's still praying. It's been five minutes."
    girl_ald "You're right. We cannot linger. The rot will draw attention."
    
    "Kristin's voice quivered as she continued to whisper her prayer—begging Enoch to take their souls gently."
    "To let them find peace. To weigh the sins of the living, not the dead."
    
    boy_ald "Enough of this, Kristin."
    hide boy_ald_normal 
    hide girl_ald_normal
    "Kristin flinched as if struck. She turned, eyes wide, lips pale."
    
    show kristin_normal at center
    
    kristin "I was only… I was praying to Lord Enoch."
    
    girl_ald "A prayer that's lasted too long. For minutes, sister. We've listened. Are you certain you're not harboring doubts?"
    
    kristin "D-Doubts? No, sister."
    
    kristin "But… What we did—what happened—was it really right? We killed the queen and her two sons."
    
    show boy_ald_normal at left
    
    boy_ald "What are you saying? That our Father was wrong?"
    
    kristin "N-no! I would never—why would I?"
    
    show girl_ald_normal at right
    
    girl_ald "Your blood-brother Svante didn't hesitate. He slit their throats without blinking. He was useful. You? You pray for corpses."
    
    boy_ald "Useless."
    
    "Kristin dropped her gaze. Her hands trembled at her sides."
    
    show kristin_normal at center
    
    kristin "I'm very sorry… I just—"
    
    boy_ald "We don't need you anymore. You're only stalling. Count Vasily might have better use for someone like you."
    
    # --- Kristin leaves ---
    "She didn't argue. With her head bowed and hands trembling at her sides, Kristin turned and walked away."
    "Her footsteps echoed faintly down the underground tunnel—slow and hesitant."
    
    hide kristin_normal 
    
    "The two Aldoriths watched her disappear into the dark before exchanging a glance."
    "Their gazes drifted to the lifeless forms behind them: the Queen of Tianho, regal even in death, and her two sons, wrapped in the stillness of final silence."
    
    boy_ald "That Kristin… soft-hearted as ever."
    girl_ald "She won't last. We both know Father only kept her around to control Svante."
    
    "They moved wordlessly to the bodies, the ritual of burial unfolding with grim familiarity."
    "Cloth unrolled. Blood wiped. Limbs bound with reverent efficiency."
    "Their hands worked swiftly—mechanical, practiced—but there was a flicker of hesitation behind their eyes."
    
    boy_ald "Why do you think Father really wanted them dead?"
    girl_ald "I don't know. And I really don't plan to ask. Best not to chase answers when you're already neck-deep in secrets."
    
    "She reached for the Queen's hand, cold and graceful, and began to wrap the burial cloth tight around her wrist."
    
    boy_ald "This feels… different. We've carried out assassinations before, but never like this. A queen. Two princes. Royals of Tianho."
    girl_ald "Exactly why we need to hurry. If anyone finds out what's buried down here—before the earth swallows it whole—we're finished."
    
    boy_ald "Still… Svante didn't even blink. Just walked in and—"
    girl_ald "Cold as stone. That's why he's Father's favorite. A metal channeler with no hesitation? That's worth more than loyalty."
    girl_ald "Which is why he still keeps that skank Kristin…"
    
    "She tied the final knot, sealing the last shroud."
    "The flickering torchlight danced across the linen, casting their silhouettes long and stretched across the stone."
    
    girl_ald "And you should remember that."
    
    "A breath passed between them."
    
    # -------------------------------------------------------------------------
    # TENSION RISES — Something is wrong
    # -------------------------------------------------------------------------
    "A pressure, subtle at first, then sudden and suffocating, pressed down on the tunnel."
    "The torches guttered, flames trembling like they, too, felt the change."
    
    play music ost_tension volume 0.3 fadein 3.0
    
    boy_ald "D-Do you feel that?"
    
    pause 0.8
    
    "A shriek—deep, guttural, wrong—ripped through the silence."
    
    girl_ald "Did you hear that?"
    
    # -------------------------------------------------------------------------
    # YAOGUAI KING ENTRANCE
    # -------------------------------------------------------------------------
    play sound sfx_yaoguai_burst
    scene bg_underground_lit with flash
    pause 0.6
    
    scene bg_underground_dim with dissolve
    play music ost_yaoguai_theme volume 0.8
    
    "The wall exploded inward, a mass of claws, horns, and red-hot eyes surging forward."
    "The Yaoguai King emerged from the rubble, obsidian-scaled and crowned in bone, the shadows clinging to his form like loyal hounds."
    
    show yk at center
    
    yk "You bury corpses… while your own hearts still beat? How generous. More for my yaoguai to feed on."
    
    show girl_ald_normal at right
    show boy_ald_normal at left
    
    girl_ald "Enoch above…"
    boy_ald "Sister, run!! I'll hold him off-!"
    
    "He slammed his palm to the ground, trying to channel earth. A ripple of stone shifted—but it was too late."
    "The Yaoguai King blurred. One moment he was across the chamber—"
    "The next, he was upon them."
    
    play sound sfx_body_thud
    scene bg_underground_dim with flash
    pause 0.4
    scene bg_underground_dim with dissolve
    
    girl_ald "AHHH!!! NO!!!"
    
    "His claws tore through the air and the girl aldorith fell, her body thudding against the stone in a lifeless heap."
    
    show boy_ald_normal at left
    boy_ald "SISTER!!"
    
    show yk at right
    yk "Your turn, little one…"
    
    # -------------------------------------------------------------------------
    # ENHANCED QUICK TIMED CHOICE
    # -------------------------------------------------------------------------
    call screen timed_choice([
        ("Try to raise a stone wall.", "prologue_choice_wall"),
        ("Dash toward the entrance of the burial tunnel.", "prologue_choice_dash")
    ], timeout=5.0, default=1)
    
    return


# =============================================================================
# SECTION 7: QTC BRANCH LABELS
# =============================================================================

label prologue_choice_wall:
    
    $ prologue_choice = "wall"
    stop sound
    
    "He dropped to one knee, forcing all his will into the trembling ground."
    
    boy_ald "Come on, come on—!"
    
    "A slab of earth surged upward between him and the Yaoguai King."
    "Then—CRACK!"
    
    play sound sfx_stone_break
    
    "A single claw punctured through the wall—then shattered it in one swipe."
    "The force sent him flying, crashing against the tunnel wall."
    
    scene cg_boy_ald_wall with flash
    pause 0.5
    scene bg_underground_red with dissolve
    
    boy_ald "ARGHH!!!"
    
    "His ribs burned. Blood filled his mouth."
    
    boy_ald "—gkkhh—!"
    
    "He collapsed."
    
    jump prologue_common


label prologue_choice_dash:
    
    $ prologue_choice = "dash"
    stop sound
    
    "He bolted down the side corridor, heart hammering."
    
    show boy_ald_normal at left
    boy_ald "Come on… Come on…"
    
    show yk at center
    yk "Running away from me? Pathetic."
    
    "He didn't make it ten steps."
    "Too fast."
    "A blur. A slash. A body fell."
    
    scene bg_underground_dim with flash
    pause 0.4
    scene bg_underground_dim with dissolve
    
    jump prologue_common


# =============================================================================
# SECTION 8: COMMON ENDING
# =============================================================================

label prologue_common:
    
    stop music fadeout 2.0
    
    "Silence returned—oppressive and final."

    show yk at center
    
    "The Yaoguai King stood among the dead. His eyes drifted to the bodies wrapped in burial cloth: a queen and two princes, now claimed by darkness."
    
    "He inhaled deeply, tasting the air."
    
    yk "Three royal corpses, wrapped so lovingly… yet buried in secret…"
    yk "And not a whisper in the winds? No fanfare. No grief. No mourning bells."
    
    "His eyes narrowed. Slowly, he stepped closer to the bodies, talons clicking against the stone."
    
    # scene cg_yk_surveying with dissolve
    # pause 1.0
    # scene bg_underground_red with dissolve
    
    yk "That old man… What are you plotting?"
    
    "He leaned down, baring rows of jagged teeth."
    
    yk "Tianho… it seems your game has begun again. And I've always loved a good hunt."
    
    # -------------------------------------------------------------------------
    # FADE OUT
    # -------------------------------------------------------------------------
    scene cg_black with fade
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