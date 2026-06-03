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

# transform food_pos:

# ==========================================
# for monsters
# yg - yaoguia
# tt - taotie
# qq - qiongqi
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

# ==========================================
# CENTER + SILHOUETTE
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