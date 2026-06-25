# ==============================================================
#          FOR POSITIONING OF SPRITES AND OTHER ASSETS
# ==============================================================

transform left_char:
    xalign -0.13  
    yalign 0.3
    zoom 1.17
    yoffset 40

transform right_char:
    xalign 1.13
    yalign 0.3   
    zoom 1.17     
    yoffset 40

transform center_char:
    xalign 0.5
    yalign 0.3
    zoom 1.17
    yoffset 40

transform left_flip:
    xanchor 0.5 # used to invert image
    xzoom -1.0 # used to invert image
    xalign -0.13  
    yalign 0.3
    zoom 1.17
    yoffset 40

transform right_flip:
    xanchor 0.5 # used to invert image
    xzoom -1.0 # used to invert image
    xalign 1.13
    yalign 0.3   
    zoom 1.17     
    yoffset 40

transform center_flip:
    xanchor 0.5 # used to invert image
    xzoom -1.0 # used to invert image
    xalign 0.5
    yalign 0.3
    zoom 1.17
    yoffset 40

# ==========================================
# ROBOTO and SUPPLY ROBOT
# ==========================================
transform center_robot:
    xalign 0.5
    yalign 0.9
    zoom 1.17
    yoffset 50

transform left_robot:
    xalign -0.13
    yalign 0.9
    zoom 1.17
    yoffset 50

transform right_robot:
    xalign 1.13
    yalign 0.9
    zoom 1.17
    yoffset 50

transform center_supply:
    xalign 0.5
    yalign 1.1
    zoom 0.8
    yoffset 50

transform left_supply:
    xalign 0.0
    yalign 1.1
    zoom 0.8
    yoffset 50

transform right_supply:
    xalign 1.0
    yalign 1.1
    zoom 0.8
    yoffset 50

# ==========================================
# for children
# ==========================================
transform right_char_kids:
    xalign 1.13
    yalign 0.8
    zoom 1.30
    yoffset 40

transform left_char_kids:
    xalign -0.13  
    yalign 0.8
    zoom 1.30
    yoffset 40


# used for elias sprites
transform right_elias:
    xalign 1.13
    yalign 0.4   
    zoom 1.30     
    yoffset 40

transform left_elias:
    xalign -0.13  
    yalign 0.8
    zoom 1.30
    yoffset 40


# transform food_pos:

# ==========================================
# for monsters
# yg - yaoguia
# tt - taotie
# qq - qiongqi
# yo - yuki onna
# ==========================================
transform left_yg:
    xalign -0.15  
    yalign 0.95
    zoom 1.20
    yoffset 40

transform right_yg:
    xalign 1.15
    yalign 0.95
    zoom 1.20
    yoffset 40

transform center_yg:
    xalign 0.5
    yalign 0.95
    zoom 1.20
    yoffset 40

transform left_tt:
    xalign 0.15
    yalign 0.2
    zoom 1.20
    yoffset 40

transform right_tt:
    xanchor 0.5 # used to invert image
    xzoom -1.0 # used to invert image
    xalign 1.15
    yalign 0.2
    zoom 1.20
    yoffset 40

transform center_tt:
    xanchor 0.5
    xzoom -1.0
    xalign 0.5
    yalign 0.2
    zoom 1.20
    yoffset 40

transform left_qq:
    xalign -2.0
    yalign 0.75
    zoom 1.85
    yoffset 50

transform right_qq:
    xanchor 0.5 # used to invert image
    xzoom -1.0 # used to invert image
    xalign 2.0
    yalign 0.75
    zoom 1.85
    yoffset 50

transform center_qq:
    xanchor 0.5
    xzoom -1.0
    xalign 0.5
    yalign 0.75
    zoom 1.85
    yoffset 50

transform left_yo:
    xalign -0.50  
    yalign 0.95
    zoom 1.17
    yoffset 40

transform right_yo:
    xalign 1.1
    yalign 0.3
    zoom 1.07
    yoffset 40

transform center_yo:
    xalign 0.5
    yalign 0.3
    zoom 1.07
    yoffset 40

transform silhouette_yo_right:
    matrixcolor TintMatrix("#000000") * BrightnessMatrix(-0.5)
    xalign 1.1
    yalign 0.3
    zoom 1.07
    yoffset 40

transform silhouette_reveal_yo_right:
    matrixcolor TintMatrix("#000000") * BrightnessMatrix(-0.5)
    xalign 1.1
    yalign 0.3
    zoom 1.07
    yoffset 40
    ease 3 matrixcolor IdentityMatrix()


# ==========================================
# CENTER + SILHOUETTE
# monster reveal (if there's any)
# ==========================================

transform silhouette:
    matrixcolor TintMatrix("#000000") * BrightnessMatrix(-0.5)
    xalign 0.5
    yalign 0.3
    zoom 1.17
    yoffset 40

transform silhouette_reveal:
    matrixcolor TintMatrix("#000000") * BrightnessMatrix(-0.5)
    xalign 0.5
    yalign 0.3
    zoom 1.17
    yoffset 40
    ease 3 matrixcolor IdentityMatrix()

# =========================================
# ICE OVERLAY (CH2 frost oni fight)
# =========================================

transform frost_overlay_1:
    xalign -0.12
    yalign 0.3
    zoom 1.17
    yoffset 40
    alpha 0.0
    linear 2.0 alpha 0.35

transform frost_overlay_2:
    xalign -0.12
    yalign 0.3
    zoom 1.17
    yoffset 40
    alpha 0.0
    linear 2.0 alpha 0.65

transform frost_overlay_3:
    xalign -0.12
    yalign 0.3
    zoom 1.17
    yoffset 40
    alpha 0.0
    linear 2.0 alpha 0.85

transform left_char_ice_1:
    xalign -0.13
    yalign 0.3
    zoom 1.17
    yoffset 40
    matrixcolor SaturationMatrix(0.85) * TintMatrix("#d4e8f0")
    linear 2.0 matrixcolor SaturationMatrix(0.85) * TintMatrix("#d4e8f0")

transform left_char_ice_2:
    xalign -0.13
    yalign 0.3
    zoom 1.17
    yoffset 40
    matrixcolor SaturationMatrix(0.55) * TintMatrix("#bce0f0")
    linear 2.0 matrixcolor SaturationMatrix(0.55) * TintMatrix("#bce0f0")

transform left_char_ice_3:
    xalign -0.13
    yalign 0.3
    zoom 1.17
    yoffset 40
    matrixcolor SaturationMatrix(0.3) * TintMatrix("#90c8e0")
    linear 2.0 matrixcolor SaturationMatrix(0.3) * TintMatrix("#90c8e0")


# FROST MASKED OVERLAYS — Dorian silhouette-clipped frost
image frost_masked_angry:
    AlphaMask(
        Transform("images/frost_gradient.png", size=(1897, 2564), fit="contain"),
        "images/Assets/Character Sprites/Dorian/Normal/dorian-emotion suit angry.png"
    )
    fit "contain"

image frost_masked_sad:
    AlphaMask(
        Transform("images/frost_gradient.png", size=(1897, 2564), fit="contain"),
        "images/Assets/Character Sprites/Dorian/Normal/dorian-emotion suit sad.png"
    )
    fit "contain"

# =========================================
#               GHOST FILTER
# =========================================
transform right_ghost_flip:
    xanchor 0.5 # used to invert image
    xzoom -1.0 # used to invert image
    xalign 1.13
    yalign 0.3   
    zoom 1.17     
    yoffset 40
    alpha 0.4 # opacity

transform right_ghost:
    xalign 1.13
    yalign 0.3   
    zoom 1.17     
    yoffset 40
    alpha 0.4 # opacity

# =========================================
# HAZY DREAM
# for dream sequences
# =========================================
transform dream_haze: 
    alpha 0.0
    blur 10
    matrixcolor SaturationMatrix(0.5)
    parallel:
        linear 1.5 alpha 1.0
    parallel:
        linear 1.5 blur 0
    parallel:
        linear 1.5 matrixcolor SaturationMatrix(1.0)

transform dream_haze_in:
    blur 10
    matrixcolor SaturationMatrix(0.5)
    easein 1.5 alpha 1.0 blur 0 matrixcolor SaturationMatrix(1.0)

# =========================================
# DORIAN SPRITE GRADIENT SHIFT
# to be used for dragon eyes sprite

# show dorian dragon_eyes at left_char with Dissolve(0.3)
# show dorian dragon_eyes at draconic_rage
# =========================================

# In transforms.rpy
transform glow_outline:
    ease 1.0 alpha 0.6
    ease 0.5 alpha 0.3
    ease 1.0 alpha 0.6
    ease 1.0 alpha 0.6
    ease 0.5 alpha 0.3
    ease 1.0 alpha 0.6
    repeat #with Dissolve(0.1)

# In screens.rpy
screen draconic_rage():
    # Glow layer behind the sprite
    add "dorian dragon_eyes":
        at glow_outline
        matrixcolor TintMatrix("#f54f13c1") * BrightnessMatrix(0.3)
        xalign -0.15
        yalign 0.3
        zoom 1.20  # Slightly larger to create outline effect
        yoffset 40
        blur 8 

transform fire_pulse:
    linear 2.0 alpha 0.6
    linear 1.0 alpha 0.3
    linear 0.5 alpha 0.8
    linear 1.0 alpha 0.5
    repeat

transform fire_pulse_gold:
    linear 2.0 alpha 0.3
    linear 1.0 alpha 0.6
    linear 0.5 alpha 0.2
    linear 1.0 alpha 0.8
    repeat

screen rage_power():
    add "#ff4500":
        at fire_pulse
        xsize 1920
        ysize 1080
    
    add "#D4Af37":
        at fire_pulse_gold
        xsize 1920
        ysize 1080

# =========================================
# Flashback filter
# =========================================
transform flashback_filter:
    matrixcolor SaturationMatrix(0.0) * TintMatrix("#d4c4a0")
    blur 3
    xalign 0.5
    yalign 0.5

transform flashback_filter_enter:
    matrixcolor SaturationMatrix(1.0) * TintMatrix("#ffffff")
    blur 0
    ease 1.0 matrixcolor SaturationMatrix(0.0) * TintMatrix("#d4c4a0")
    ease 1.0 blur 3

transform flashback_filter_exit:
    matrixcolor SaturationMatrix(0.0) * TintMatrix("#d4c4a0")
    blur 3
    ease 1.0 matrixcolor SaturationMatrix(1.0) * TintMatrix("#ffffff")
    ease 1.0 blur 0

image floating_note:
    "images/Assets/Illustrations/30 - NikoPamphalet.png"
    xalign 0.5
    yalign 0.5
    
transform note_pop:
    xalign 0.5
    yalign 0.3
    zoom 0.6
    alpha 0.0
    ease 0.6 zoom 1.0 alpha 1.0
    ease 0.4 zoom 1.0



