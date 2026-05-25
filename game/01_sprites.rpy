# ================================================================
#                       CHARACTER SPRITES
# ================================================================
# the following sprites are used for chapter 1 onwards
# the sprites declared at prologue will stay there

# --- Character Sprites Syntax ----
# image char_name:
#     At("images/path.png", sprite_highlight("name in game"))
#     fit "contain"

# =============================================================================
# DORIAN - All Sprite Variants
# =============================================================================
# Usage examples:
#   show dorian neutral at left
#   show dorian angry at center
#   show dorian normal_alt confident at right
#   show dorian sleepware dragon_eyes at far_left
#   show dorian tianho_ceremonial smile at far_right
#   show dorian underwear serious
# =============================================================================

# Character list folders from assets:
# dorian
# yuxuan
# elias
# vasily
# hyon chung-hee
# magnus
# niko
# supply robot
# roboto
# svante
# tim
# weng
# other chars folder (added)
# single sprites from upper dir

# TODO: fix file path
# =============================================================================
# DORIAN — NORMAL OUTFIT (7 emotions)
# =============================================================================
image dorian neutral:
    At("images/Assets/Character Sprites/Dorian/Normal/dorian-emotion suit neutral.png", sprite_highlight("dorian"))
    fit "contain"
image dorian angry:
    At("images/Assets/Character Sprites/Dorian/Normal/dorian-emotion suit angry.png", sprite_highlight("dorian"))
    fit "contain"
image dorian sad:
    At("images/Assets/Character Sprites/Dorian/Normal/dorian-emotion suit sad.png", sprite_highlight("dorian"))
    fit "contain"
image dorian dragon_eyes:
    At("images/Assets/Character Sprites/Dorian/Normal/dorian-emotion suit dragon eyes.png", sprite_highlight("dorian"))
    fit "contain"
image dorian serious:
    At("images/Assets/Character Sprites/Dorian/Normal/dorian-emotion suit serious.png", sprite_highlight("dorian"))
    fit "contain"
image dorian smile:
    At("images/Assets/Character Sprites/Dorian/Normal/dorian-emotion suit smile.png", sprite_highlight("dorian"))
    fit "contain"
image dorian normal:
    At("images/Assets/Character Sprites/Dorian/Normal/dorian-mc battlesuit.png", sprite_highlight("dorian")) # BASE SPRITE
    fit "contain"

# ===============================
# DORIAN — NORMAL ALT POSES (5 emotions)
# ===============================
image dorian normal_alt_neutral:
    At("images/Assets/Character Sprites/Dorian/Normal - Alternate Pose/dorian-emotion suit neutral.png", sprite_highlight("dorian"))
    fit "contain"
image dorian normal_alt_tense:
    At("images/Assets/Character Sprites/Dorian/Normal - Alternate Pose/dorian-emotion suit neutral new pose tense.png", sprite_highlight("dorian"))
    fit "contain"
image dorian normal_alt_calm:
    At("images/Assets/Character Sprites/Dorian/Normal - Alternate Pose/dorian-emotion suit neutral new pose calmed.png", sprite_highlight("dorian"))
    fit "contain"
image dorian normal_alt_confident:
    At("images/Assets/Character Sprites/Dorian/Normal - Alternate Pose/dorian-emotion suit neutral new pose confident.png", sprite_highlight("dorian"))
    fit "contain"
image dorian normal_alt_annoyed:
    At("images/Assets/Character Sprites/Dorian/Normal - Alternate Pose/dorian-emotion suit neutral new pose annoyed.png", sprite_highlight("dorian"))
    fit "contain"

# ===============================
# DORIAN — SLEEPWARE (7 emotions)
# ===============================
image dorian sleepware_neutral:
    At("images/Assets/Character Sprites/Dorian/Sleepwear/dorian-mc pajama neutral.png", sprite_highlight("dorian"))
    fit "contain"
image dorian sleepware_angry:
    At("images/Assets/Character Sprites/Dorian/Sleepwear/dorian-mc pajama angry.png", sprite_highlight("dorian"))
    fit "contain"
image dorian sleepware_sad:
    At("images/Assets/Character Sprites/Dorian/Sleepwear/dorian-mc pajama sad.png", sprite_highlight("dorian"))
    fit "contain"
image dorian sleepware_dragon_eyes:
    At("images/Assets/Character Sprites/Dorian/Sleepwear/dorian-mc pajama dragon eyes.png", sprite_highlight("dorian"))
    fit "contain"
image dorian sleepware_serious:
    At("images/Assets/Character Sprites/Dorian/Sleepwear/dorian-mc pajama serious.png", sprite_highlight("dorian"))
    fit "contain"
image dorian sleepware_smile:
    At("images/Assets/Character Sprites/Dorian/Sleepwear/dorian-mc pajama smile.png", sprite_highlight("dorian"))
    fit "contain"
image dorian sleepware_normal:
    At("images/Assets/Character Sprites/Dorian/Sleepwear/dorian-mc pajama.png", sprite_highlight("dorian")) # BASE SPRITE
    fit "contain"

# ===============================
# DORIAN — TIANHO CEREMONIAL (7 emotions)
# ===============================
image dorian tianho_ceremonial_neutral:
    At("images/Assets/Character Sprites/Dorian/Tianho Ceremonial/dorian-robe neutral.png", sprite_highlight("dorian"))
    fit "contain"
image dorian tianho_ceremonial_angry:
    At("images/Assets/Character Sprites/Dorian/Tianho Ceremonial/dorian-robe angry.png", sprite_highlight("dorian"))
    fit "contain"
image dorian tianho_ceremonial_sad:
    At("images/Assets/Character Sprites/Dorian/Tianho Ceremonial/dorian-robe sad.png", sprite_highlight("dorian"))
    fit "contain"
image dorian tianho_ceremonial_dragon_eyes:
    At("images/Assets/Character Sprites/Dorian/Tianho Ceremonial/dorian-robe dragon eyes.png", sprite_highlight("dorian"))
    fit "contain"
image dorian tianho_ceremonial_serious:
    At("images/Assets/Character Sprites/Dorian/Tianho Ceremonial/dorian-robe serious.png", sprite_highlight("dorian"))
    fit "contain"
image dorian tianho_ceremonial_smile:
    At("images/Assets/Character Sprites/Dorian/Tianho Ceremonial/dorian-robe smile.png", sprite_highlight("dorian"))
    fit "contain"
image dorian tianho_ceremonial_normal:
    At("images/Assets/Character Sprites/Dorian/Tianho Ceremonial/dorian-mc kimono-yello.png", sprite_highlight("dorian")) # BASE SPRITE
    fit "contain"

# ===============================
# DORIAN — UNDERWEAR (7 emotions)
# ===============================
image dorian underwear_neutral:
    At("images/Assets/Character Sprites/Dorian/Underwear/dorian-mc with emotions neutral.png", sprite_highlight("dorian"))
    fit "contain"
image dorian underwear_angry:
    At("images/Assets/Character Sprites/Dorian/Underwear/dorian-mc with emotions angry.png", sprite_highlight("dorian"))
    fit "contain"
image dorian underwear_sad:
    At("images/Assets/Character Sprites/Dorian/Underwear/dorian-mc with emotions sad.png", sprite_highlight("dorian"))
    fit "contain"
image dorian underwear_dragon_eyes:
    At("images/Assets/Character Sprites/Dorian/Underwear/dorian-mc with emotions dragon eyes.png", sprite_highlight("dorian"))
    fit "contain"
image dorian underwear_serious:
    At("images/Assets/Character Sprites/Dorian/Underwear/dorian-mc with emotions serious.png", sprite_highlight("dorian"))
    fit "contain"
image dorian underwear_smile:
    At("images/Assets/Character Sprites/Dorian/Underwear/dorian-mc with emotions smile.png", sprite_highlight("dorian"))
    fit "contain"
image dorian underwear_normal:
    At("images/Assets/Character Sprites/Dorian/Underwear/dorian-mc base.png", sprite_highlight("dorian"))
    fit "contain"

# TODO: fix file path
# =============================================================================
# COUNT VASILY - All Sprite Variants
# =============================================================================
# Usage examples:
#   show vasily neutral at left
#   show vasily alt_aggressive at center
#   show vasily alt_think at right
# =============================================================================
# =============================================================================
# VASILY — NORMAL (base image)
# =============================================================================
image vasily neutral:
    At("images/Assets/Character Sprites/Count Vasily/count vasilynorubics.png", sprite_highlight("vasily"))
    fit "contain"

# ===============================
# VASILY — NORMAL ALT POSES (5 emotions)
# ===============================
image vasily alt_normal:
    At("images/Assets/Character Sprites/Count Vasily/Normal - Alternate Pose/count vasilynorubics.png", sprite_highlight("vasily"))
    fit "contain"
image vasily alt_aggressive:
    At("images/Assets/Character Sprites/Count Vasily/Normal - Alternate Pose/count vasilynorubics aggressive.png", sprite_highlight("vasily"))
    fit "contain"
image vasily alt_mad:
    At("images/Assets/Character Sprites/Count Vasily/Normal - Alternate Pose/count vasilynorubics mad.png", sprite_highlight("vasily"))
    fit "contain"
image vasily alt_savage:
    At("images/Assets/Character Sprites/Count Vasily/Normal - Alternate Pose/count vasilynorubics savage.png", sprite_highlight("vasily"))
    fit "contain"
image vasily alt_think:
    At("images/Assets/Character Sprites/Count Vasily/Normal - Alternate Pose/count vasilynorubics think.png", sprite_highlight("vasily"))
    fit "contain"

# TODO: fix file path
# =============================================================================
# ELIAS - All Sprite Variants
# =============================================================================
# Usage examples:
#   show elias first_meet_neutral at left
#   show elias normal_cute at center
#   show elias alt_crying at right
#   show elias sleepware_evil at far_left
#   show elias swimwear_happy at far_right
#   show elias ceremonial_mad
# =============================================================================
# =============================================================================
# ELIAS — FIRST MEET (4 emotions, Ch2-3 only)
# =============================================================================
image elias first_meet_neutral:
    At("images/Assets/Character Sprites/Elias/Chapter 2 & 3 Only/elias first meet with dorian colored v2.png", sprite_highlight("elias"))
    fit "contain"
image elias first_meet_crying:
    At("images/Assets/Character Sprites/Elias/Chapter 2 & 3 Only/elias first meet with dorian colored v2 crying.png", sprite_highlight("elias"))
    fit "contain"
image elias first_meet_happy:
    At("images/Assets/Character Sprites/Elias/Chapter 2 & 3 Only/elias first meet with dorian colored v2 happy.png", sprite_highlight("elias"))
    fit "contain"
image elias first_meet_sad:
    At("images/Assets/Character Sprites/Elias/Chapter 2 & 3 Only/elias first meet with dorian colored v2 sad.png", sprite_highlight("elias"))
    fit "contain"

# ===============================
# ELIAS — NORMAL OUTFIT (7 emotions)
# ===============================
image elias normal_cute:
    At("images/Assets/Character Sprites/Elias/Normal/kid girl dress cute.png", sprite_highlight("elias"))
    fit "contain"
image elias normal_evil:
    At("images/Assets/Character Sprites/Elias/Normal/kid girl dress evil.png", sprite_highlight("elias"))
    fit "contain"
image elias normal_happy:
    At("images/Assets/Character Sprites/Elias/Normal/kid girl dress happy.png", sprite_highlight("elias"))
    fit "contain"
image elias normal_lying:
    At("images/Assets/Character Sprites/Elias/Normal/kid girl dress lying.png", sprite_highlight("elias"))
    fit "contain"
image elias normal_mad:
    At("images/Assets/Character Sprites/Elias/Normal/kid girl dress mad.png", sprite_highlight("elias"))
    fit "contain"
image elias normal_sad:
    At("images/Assets/Character Sprites/Elias/Normal/kid girl dress sad.png", sprite_highlight("elias"))
    fit "contain"
image elias normal_neutral:
    At("images/Assets/Character Sprites/Elias/Normal/kid girl dress.png", sprite_highlight("elias"))
    fit "contain"

# ===============================
# ELIAS — NORMAL ALT POSES (5 emotions)
# ===============================
image elias alt_crying:
    At("images/Assets/Character Sprites/Elias/Normal - Alternative Pose/elias new pose crying.png", sprite_highlight("elias"))
    fit "contain"
image elias alt_doubt:
    At("images/Assets/Character Sprites/Elias/Normal - Alternative Pose/elias new pose doubt.png", sprite_highlight("elias"))
    fit "contain"
image elias alt_joy:
    At("images/Assets/Character Sprites/Elias/Normal - Alternative Pose/elias new pose joy.png", sprite_highlight("elias"))
    fit "contain"
image elias alt_smirk:
    At("images/Assets/Character Sprites/Elias/Normal - Alternative Pose/elias new pose smirk.png", sprite_highlight("elias"))
    fit "contain"
image elias alt_neutral:
    At("images/Assets/Character Sprites/Elias/Normal - Alternative Pose/elias new pose.png", sprite_highlight("elias"))
    fit "contain"

# ===============================
# ELIAS — SLEEPWEAR (7 emotions)
# ===============================
image elias sleepware_cute:
    At("images/Assets/Character Sprites/Elias/Sleepwear/kid girl pajama cute.png", sprite_highlight("elias"))
    fit "contain"
image elias sleepware_evil:
    At("images/Assets/Character Sprites/Elias/Sleepwear/kid girl pajama evil.png", sprite_highlight("elias"))
    fit "contain"
image elias sleepware_happy:
    At("images/Assets/Character Sprites/Elias/Sleepwear/kid girl pajama happy.png", sprite_highlight("elias"))
    fit "contain"
image elias sleepware_lying:
    At("images/Assets/Character Sprites/Elias/Sleepwear/kid girl pajama lying.png", sprite_highlight("elias"))
    fit "contain"
image elias sleepware_mad:
    At("images/Assets/Character Sprites/Elias/Sleepwear/kid girl pajama mad.png", sprite_highlight("elias"))
    fit "contain"
image elias sleepware_sad:
    At("images/Assets/Character Sprites/Elias/Sleepwear/kid girl pajama sad.png", sprite_highlight("elias"))
    fit "contain"
image elias sleepware_neutral:
    At("images/Assets/Character Sprites/Elias/Sleepwear/kid girl pajama.png", sprite_highlight("elias"))
    fit "contain"

# ===============================
# ELIAS — SWIMWEAR (7 emotions)
# ===============================
image elias swimwear_cute:
    At("images/Assets/Character Sprites/Elias/Swimwear/kid girl base emotions cute.png", sprite_highlight("elias"))
    fit "contain"
image elias swimwear_evil:
    At("images/Assets/Character Sprites/Elias/Swimwear/kid girl base emotions evil.png", sprite_highlight("elias"))
    fit "contain"
image elias swimwear_happy:
    At("images/Assets/Character Sprites/Elias/Swimwear/kid girl base emotions happy.png", sprite_highlight("elias"))
    fit "contain"
image elias swimwear_lying:
    At("images/Assets/Character Sprites/Elias/Swimwear/kid girl base emotions lying.png", sprite_highlight("elias"))
    fit "contain"
image elias swimwear_mad:
    At("images/Assets/Character Sprites/Elias/Swimwear/kid girl base emotions mad.png", sprite_highlight("elias"))
    fit "contain"
image elias swimwear_sad:
    At("images/Assets/Character Sprites/Elias/Swimwear/kid girl base emotions sad.png", sprite_highlight("elias"))
    fit "contain"
image elias swimwear_neutral:
    At("images/Assets/Character Sprites/Elias/Swimwear/kid girl base.png", sprite_highlight("elias"))
    fit "contain"

# ===============================
# ELIAS — TIANHO CEREMONIAL (7 emotions)
# ===============================
image elias ceremonial_cute:
    At("images/Assets/Character Sprites/Elias/Tianho Ceremonial/kid girl robe cute.png", sprite_highlight("elias"))
    fit "contain"
image elias ceremonial_evil:
    At("images/Assets/Character Sprites/Elias/Tianho Ceremonial/kid girl robe evil.png", sprite_highlight("elias"))
    fit "contain"
image elias ceremonial_happy:
    At("images/Assets/Character Sprites/Elias/Tianho Ceremonial/kid girl robe happy.png", sprite_highlight("elias"))
    fit "contain"
image elias ceremonial_lying:
    At("images/Assets/Character Sprites/Elias/Tianho Ceremonial/kid girl robe lying.png", sprite_highlight("elias"))
    fit "contain"
image elias ceremonial_mad:
    At("images/Assets/Character Sprites/Elias/Tianho Ceremonial/kid girl robe mad.png", sprite_highlight("elias"))
    fit "contain"
image elias ceremonial_sad:
    At("images/Assets/Character Sprites/Elias/Tianho Ceremonial/kid girl robe sad.png", sprite_highlight("elias"))
    fit "contain"
image elias ceremonial_neutral:
    At("images/Assets/Character Sprites/Elias/Tianho Ceremonial/kid girl robe.png", sprite_highlight("elias"))
    fit "contain"

# TODO: fix file path
# =============================================================================
# CHENG YUXUAN - All Sprite Variants
# =============================================================================
# Usage examples:
#   show yuxuan normal_neutral at left
#   show yuxuan alt_think at center
#   show yuxuan sleepware_sad at right
#   show yuxuan underwear_angry at far_left
#   show yuxuan ceremonial_happy at far_right
# =============================================================================
# =============================================================================
# YUXUAN — NORMAL OUTFIT (6 emotions)
# =============================================================================
image yuxuan normal_neutral:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Normal/cheng yuxuan kimono.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan normal_angry:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Normal/cheng yuxuan kimono angry.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan normal_happy:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Normal/cheng yuxuan kimono happy.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan normal_lying:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Normal/cheng yuxuan kimono lying.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan normal_normal:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Normal/cheng yuxuan kimono normal.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan normal_sad:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Normal/cheng yuxuan kimono sad.png", sprite_highlight("yuxuan"))
    fit "contain"

# ===============================
# YUXUAN — NORMAL ALT POSES (5 emotions)
# ===============================
image yuxuan alt_close_eyes:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Normal - Alternate Pose/cheng yuxuan kimono new pose close eyes.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan alt_mid_close_eyes:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Normal - Alternate Pose/cheng yuxuan kimono new pose mid close eyes.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan alt_smile:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Normal - Alternate Pose/cheng yuxuan kimono new pose wide smile.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan alt_think:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Normal - Alternate Pose/cheng yuxuan kimono new thinktense.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan alt_neutral:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Normal - Alternate Pose/cheng yuxuan kimono new pose.png", sprite_highlight("yuxuan"))
    fit "contain"

# ===============================
# YUXUAN — SLEEPWEAR (6 emotions)
# ===============================
image yuxuan sleepwear_angry:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Sleepwear/cheng yuxuan pajama angry.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan sleepwear_happy:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Sleepwear/cheng yuxuan pajama happy.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan sleepwear_lying:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Sleepwear/cheng yuxuan pajama lying.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan sleepwear_normal:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Sleepwear/cheng yuxuan pajama normal.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan sleepwear_sad:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Sleepwear/cheng yuxuan pajama sad.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan sleepwear_neutral:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Sleepwear/cheng yuxuan pajama.png", sprite_highlight("yuxuan"))
    fit "contain"

# ===============================
# YUXUAN — UNDERWEAR (6 emotions)
# ===============================
image yuxuan underwear_neutral:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Underwear/cheng yuxuan base.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan underwear_angry:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Underwear/cheng yuxuan emotions angry.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan underwear_happy:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Underwear/cheng yuxuan emotions happy.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan underwear_lying:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Underwear/cheng yuxuan emotions lying.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan underwear_normal:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Underwear/cheng yuxuan emotions normal.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan underwear_sad:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Underwear/cheng yuxuan emotions sad.png", sprite_highlight("yuxuan"))
    fit "contain"

# ===============================
# YUXUAN — TIANHO CEREMONIAL (6 emotions)
# ===============================
image yuxuan ceremonial_neutral:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Underwear/cheng yuxuan base.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan ceremonial_angry:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Underwear/cheng yuxuan emotions angry.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan ceremonial_normal:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Underwear/cheng yuxuan emotions normal.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan ceremonial_happy:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Underwear/cheng yuxuan emotions happy.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan ceremonial_lying:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Underwear/cheng yuxuan emotions lying.png", sprite_highlight("yuxuan"))
    fit "contain"
image yuxuan ceremonial_sad:
    At("images/Assets/Character Sprites/Cheng Yuxuan/Underwear/cheng yuxuan emotions sad.png", sprite_highlight("yuxuan"))
    fit "contain"

# =============================================================================
# ROBOTO - All Sprite Variants
# =============================================================================
# Usage examples:
#   show roboto neutral at left
#   show roboto bad_mood at center
#   show roboto error at right
#   show roboto happy at far_left
#   show roboto malfunction at far_right
# =============================================================================
# TODO: fix file path
# =============================================================================
# ROBOTO — ALL VARIANTS (5 sprites)
# =============================================================================
image roboto bad_mood:
    At("images/Assets/Character Sprites/Roboto/roboto-bad mood.png", sprite_highlight("roboto"))
    fit "contain"
image roboto error:
    At("images/Assets/Character Sprites/Roboto/roboto-error.png", sprite_highlight("roboto"))
    fit "contain"
image roboto fin:
    At("images/Assets/Character Sprites/Roboto/roboto-fin.png", sprite_highlight("roboto"))
    fit "contain"
image roboto happy:
    At("images/Assets/Character Sprites/Roboto/roboto-happy.png", sprite_highlight("roboto"))
    fit "contain"
image roboto malfunction:
    At("images/Assets/Character Sprites/Roboto/roboto-malfunction.png", sprite_highlight("roboto"))
    fit "contain"

# TODO: fix file path
# =============================================================================
# CHUNG-HEE - All Sprite Variants
# =============================================================================
image chunghee normal_angry:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Normal/chung hee suit angry.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee normal_happy:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Normal/chung hee suit happy.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee normal_neutral:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Normal/chung hee suit neutral.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee normal_power_up:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Normal/chung hee suit power up.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee normal_sad:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Normal/chung hee suit sad.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee normal_v2:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Normal/chung hee suit-v2.png", sprite_highlight("chung_hee"))
    fit "contain"

# ===============================
# CHUNG-HEE — NORMAL ALT POSES
# ===============================
image chunghee alt_charging:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Normal - Alternate Pose/chung hee new pose charging.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee alt_smirk:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Normal - Alternate Pose/chung hee new pose smirk.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee alt_tense:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Normal - Alternate Pose/chung hee new pose tense.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee alt_wink:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Normal - Alternate Pose/chung hee new pose wink.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee alt_neutral:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Normal - Alternate Pose/chung hee new pose.png", sprite_highlight("chung_hee"))
    fit "contain"

# ===============================
# CHUNG-HEE — SLEEPWEAR
# ===============================
image chunghee sleepwear_angry:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Sleepwear/chung hee pajama angry.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee sleepwear_happy:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Sleepwear/chung hee pajama happy.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee sleepwear_neutral:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Sleepwear/chung hee pajama neutral.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee sleepwear_power_up:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Sleepwear/chung hee pajama power up.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee sleepwear_sad:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Sleepwear/chung hee pajama sad.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee sleepwear_default:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Sleepwear/chung hee pajama.png", sprite_highlight("chung_hee"))
    fit "contain"

# ===============================
# CHUNG-HEE — TIANHO CEREMONIAL
# ===============================
image chunghee ceremonial_angry:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Tianho Ceremonial/chung hee robe angry.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee ceremonial_happy:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Tianho Ceremonial/chung hee robe happy.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee ceremonial_neutral:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Tianho Ceremonial/chung hee robe neutral.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee ceremonial_power_up:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Tianho Ceremonial/chung hee robe power up.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee ceremonial_sad:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Tianho Ceremonial/chung hee robe sad.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee ceremonial_default:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Tianho Ceremonial/chung hee robe.png", sprite_highlight("chung_hee"))
    fit "contain"

# ===============================
# CHUNG-HEE — UNDERWEAR
# ===============================
image chunghee underwear_base:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Underwear/chung hee base.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee underwear_angry:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Underwear/chung hee emotions angry.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee underwear_happy:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Underwear/chung hee emotions happy.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee underwear_neutral:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Underwear/chung hee emotions neutral.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee underwear_power_up:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Underwear/chung hee emotions powerup.png", sprite_highlight("chung_hee"))
    fit "contain"
image chunghee underwear_sad:
    At("images/Assets/Character Sprites/Hyon Chung-hee/Underwear/chung hee emotions sad.png", sprite_highlight("chung_hee"))
    fit "contain"

# TODO: fix file path
# =============================================================================
# MAGNUS WYNDHAM - All Sprite Variants
# =============================================================================
image magnus normal:
    At("images/Assets/Character Sprites/Magnus Wyndham/Normal/magnus form.png", sprite_highlight("magnus"))
    fit "contain"

# ===============================
# MAGNUS — NORMAL ALT  (EVIL EYE)
# ===============================
image magnus alt_anger:
    At("images/Assets/Character Sprites/Magnus Wyndham/Normal - Alternative Pose/base magnus file newpose evil eye anger.png", sprite_highlight("magnus"))
    fit "contain"
image magnus alt_close:
    At("images/Assets/Character Sprites/Magnus Wyndham/Normal - Alternative Pose/base magnus file newpose evil eye close.png", sprite_highlight("magnus"))
    fit "contain"
image magnus alt_shocked:
    At("images/Assets/Character Sprites/Magnus Wyndham/Normal - Alternative Pose/base magnus file newpose evil eye shocked.png", sprite_highlight("magnus"))
    fit "contain"
image magnus alt_evil_eye:
    At("images/Assets/Character Sprites/Magnus Wyndham/Normal - Alternative Pose/base magnus file newpose evil eye.png", sprite_highlight("magnus"))
    fit "contain"
image magnus alt_smirk:
    At("images/Assets/Character Sprites/Magnus Wyndham/Normal - Alternative Pose/base magnus file newpose smirk.png", sprite_highlight("magnus"))
    fit "contain"
image magnus alt_newpose:
    At("images/Assets/Character Sprites/Magnus Wyndham/Normal - Alternative Pose/base magnus file newpose.png", sprite_highlight("magnus"))
    fit "contain"

# ===============================
# MAGNUS — CLOTHED
# ===============================
image magnus clothed_no_wings:
    At("images/Assets/Character Sprites/Magnus Wyndham/Normal-Clothed/magnus form upper suit without wings.png", sprite_highlight("magnus"))
    fit "contain"
image magnus clothed_wings:
    At("images/Assets/Character Sprites/Magnus Wyndham/Normal-Clothed/magnus form upper suit.png", sprite_highlight("magnus"))
    fit "contain"

# ===============================
# MAGNUS — SLEEPWEAR
# ===============================
image magnus sleepwear:
    At("images/Assets/Character Sprites/Magnus Wyndham/Sleepwear/magnus pajama.png", sprite_highlight("magnus"))
    fit "contain"

# ===============================
# MAGNUS — TIANHO CEREMONIAL
# ===============================
image magnus ceremonial:
    At("images/Assets/Character Sprites/Magnus Wyndham/Tianho Ceremonial/magnus robe.png", sprite_highlight("magnus"))
    fit "contain"

# ===============================
# MAGNUS — UNDERWEAR
# ===============================
image magnus underwear_angry:
    At("images/Assets/Character Sprites/Magnus Wyndham/Underwear/magnus base head emotions angry.png", sprite_highlight("magnus"))
    fit "contain"
image magnus underwear_ignore:
    At("images/Assets/Character Sprites/Magnus Wyndham/Underwear/magnus base head emotions ignore.png", sprite_highlight("magnus"))
    fit "contain"
image magnus underwear_powered:
    At("images/Assets/Character Sprites/Magnus Wyndham/Underwear/magnus base head emotions powered.png", sprite_highlight("magnus"))
    fit "contain"
image magnus underwear_sad:
    At("images/Assets/Character Sprites/Magnus Wyndham/Underwear/magnus base head emotions sad.png", sprite_highlight("magnus"))
    fit "contain"
image magnus underwear_serious:
    At("images/Assets/Character Sprites/Magnus Wyndham/Underwear/magnus base head emotions serious.png", sprite_highlight("magnus"))
    fit "contain"
image magnus underwear_base:
    At("images/Assets/Character Sprites/Magnus Wyndham/Underwear/magnus base.png", sprite_highlight("magnus"))
    fit "contain"

# TODO: bookmark niko
# =============================================================================
# NIKO TSUKUMO - All Sprite Variants
# =============================================================================
image niko normal_anger:
    At("images/Assets/Character Sprites/Niko Tsukumo/Normal/niko tsukumo suit emotions anger.png", sprite_highlight("niko"))
    fit "contain"
image niko normal_ignore:
    At("images/Assets/Character Sprites/Niko Tsukumo/Normal/niko tsukumo suit emotions ignore.png", sprite_highlight("niko"))
    fit "contain"
image niko normal_meditate:
    At("images/Assets/Character Sprites/Niko Tsukumo/Normal/niko tsukumo suit emotions meditate.png", sprite_highlight("niko"))
    fit "contain"
image niko normal_sad:
    At("images/Assets/Character Sprites/Niko Tsukumo/Normal/niko tsukumo suit emotions sad.png", sprite_highlight("niko"))
    fit "contain"
image niko normal_serious:
    At("images/Assets/Character Sprites/Niko Tsukumo/Normal/niko tsukumo suit emotions serious.png", sprite_highlight("niko"))
    fit "contain"
image niko normal_smile:
    At("images/Assets/Character Sprites/Niko Tsukumo/Normal/niko tsukumo suit emotions smile.png", sprite_highlight("niko"))
    fit "contain"
image niko normal_base:
    At("images/Assets/Character Sprites/Niko Tsukumo/Normal/niko tsukumo suit.png", sprite_highlight("niko"))
    fit "contain"

# =============================================================================
# NIKO — NORMAL ALT POSES
# =============================================================================
image niko alt_annoyed:
    At("images/Assets/Character Sprites/Niko Tsukumo/Normal - Alternate Pose/niko tsukumo new pose annoyed.png", sprite_highlight("niko"))
    fit "contain"
image niko alt_disappointed:
    At("images/Assets/Character Sprites/Niko Tsukumo/Normal - Alternate Pose/niko tsukumo new pose dissapointed.png", sprite_highlight("niko"))
    fit "contain"
image niko alt_irritate:
    At("images/Assets/Character Sprites/Niko Tsukumo/Normal - Alternate Pose/niko tsukumo new pose irritate.png", sprite_highlight("niko"))
    fit "contain"
image niko alt_tense:
    At("images/Assets/Character Sprites/Niko Tsukumo/Normal - Alternate Pose/niko tsukumo new pose tense.png", sprite_highlight("niko"))
    fit "contain"
image niko alt_base:
    At("images/Assets/Character Sprites/Niko Tsukumo/Normal - Alternate Pose/niko tsukumo new pose.png", sprite_highlight("niko"))
    fit "contain"

# =============================================================================
# NIKO — SLEEPWEAR
# =============================================================================
image niko sleepwear_anger:
    At("images/Assets/Character Sprites/Niko Tsukumo/Sleepwear/niko tsukumo pajama anger.png", sprite_highlight("niko"))
    fit "contain"
image niko sleepwear_ignore:
    At("images/Assets/Character Sprites/Niko Tsukumo/Sleepwear/niko tsukumo pajama ignore.png", sprite_highlight("niko"))
    fit "contain"
image niko sleepwear_meditate:
    At("images/Assets/Character Sprites/Niko Tsukumo/Sleepwear/niko tsukumo pajama meditate.png", sprite_highlight("niko"))
    fit "contain"
image niko sleepwear_sad:
    At("images/Assets/Character Sprites/Niko Tsukumo/Sleepwear/niko tsukumo pajama sad.png", sprite_highlight("niko"))
    fit "contain"
image niko sleepwear_serious:
    At("images/Assets/Character Sprites/Niko Tsukumo/Sleepwear/niko tsukumo pajama serious.png", sprite_highlight("niko"))
    fit "contain"
image niko sleepwear_smile:
    At("images/Assets/Character Sprites/Niko Tsukumo/Sleepwear/niko tsukumo pajama smile.png", sprite_highlight("niko"))
    fit "contain"
image niko sleepwear_base:
    At("images/Assets/Character Sprites/Niko Tsukumo/Sleepwear/niko tsukumo pajama.png", sprite_highlight("niko"))
    fit "contain"

# =============================================================================
# NIKO — TIANHO CEREMONIAL
# =============================================================================
image niko ceremonial_anger:
    At("images/Assets/Character Sprites/Niko Tsukumo/Tianho Ceremonial/niko tsukumo robe emotion anger.png", sprite_highlight("niko"))
    fit "contain"
image niko ceremonial_meditate:
    At("images/Assets/Character Sprites/Niko Tsukumo/Tianho Ceremonial/niko tsukumo robe emotion meditate.png", sprite_highlight("niko"))
    fit "contain"
image niko ceremonial_sad:
    At("images/Assets/Character Sprites/Niko Tsukumo/Tianho Ceremonial/niko tsukumo robe emotion sad.png", sprite_highlight("niko"))
    fit "contain"
image niko ceremonial_serious:
    At("images/Assets/Character Sprites/Niko Tsukumo/Tianho Ceremonial/niko tsukumo robe emotion serious.png", sprite_highlight("niko"))
    fit "contain"
image niko ceremonial_smile:
    At("images/Assets/Character Sprites/Niko Tsukumo/Tianho Ceremonial/niko tsukumo robe emotion smile.png", sprite_highlight("niko"))
    fit "contain"
image niko ceremonial_base:
    At("images/Assets/Character Sprites/Niko Tsukumo/Tianho Ceremonial/niko tsukumo robe.png", sprite_highlight("niko"))
    fit "contain"

# =============================================================================
# NIKO — UNDERWEAR
# =============================================================================
image niko underwear_base:
    At("images/Assets/Character Sprites/Niko Tsukumo/Underwear/niko tsukumo base.png", sprite_highlight("niko"))
    fit "contain"
image niko underwear_anger:
    At("images/Assets/Character Sprites/Niko Tsukumo/Underwear/niko tsukumo emotions anger.png", sprite_highlight("niko"))
    fit "contain"
image niko underwear_ignore:
    At("images/Assets/Character Sprites/Niko Tsukumo/Underwear/niko tsukumo emotions ignore.png", sprite_highlight("niko"))
    fit "contain"
image niko underwear_meditate:
    At("images/Assets/Character Sprites/Niko Tsukumo/Underwear/niko tsukumo emotions meditate.png", sprite_highlight("niko"))
    fit "contain"
image niko underwear_sad:
    At("images/Assets/Character Sprites/Niko Tsukumo/Underwear/niko tsukumo emotions sad.png", sprite_highlight("niko"))
    fit "contain"
image niko underwear_serious:
    At("images/Assets/Character Sprites/Niko Tsukumo/Underwear/niko tsukumo emotions serious.png", sprite_highlight("niko"))
    fit "contain"
image niko underwear_smile:
    At("images/Assets/Character Sprites/Niko Tsukumo/Underwear/niko tsukumo emotions smile.png", sprite_highlight("niko"))
    fit "contain"

# TODO: fix file path
# =============================================================================
# SVANTE - All Sprite Variants
# =============================================================================
image svante normal_angry:
    At("images/Assets/Character Sprites/Svante Nordstrom/Normal/svante armor angry.png", sprite_highlight("svante"))
    fit "contain"
image svante normal_happy:
    At("images/Assets/Character Sprites/Svante Nordstrom/Normal/svante armor happy.png", sprite_highlight("svante"))
    fit "contain"
image svante normal_nervous:
    At("images/Assets/Character Sprites/Svante Nordstrom/Normal/svante armor nervous.png", sprite_highlight("svante"))
    fit "contain"
image svante normal_neutral:
    At("images/Assets/Character Sprites/Svante Nordstrom/Normal/svante armor neutral.png", sprite_highlight("svante"))
    fit "contain"
image svante normal_sad:
    At("images/Assets/Character Sprites/Svante Nordstrom/Normal/svante armor sad.png", sprite_highlight("svante"))
    fit "contain"
image svante normal_base:
    At("images/Assets/Character Sprites/Svante Nordstrom/Normal/svante armor.png", sprite_highlight("svante"))
    fit "contain"

# ===============================
# SVANTE — NORMAL ALT POSES
# ===============================
image svante alt_catface:
    At("images/Assets/Character Sprites/Svante Nordstrom/Normal - Alternate Pose/svante armor new pose catface.png", sprite_highlight("svante"))
    fit "contain"
image svante alt_funny:
    At("images/Assets/Character Sprites/Svante Nordstrom/Normal - Alternate Pose/svante armor new pose funny.png", sprite_highlight("svante"))
    fit "contain"
image svante alt_guilty:
    At("images/Assets/Character Sprites/Svante Nordstrom/Normal - Alternate Pose/svante armor new pose guilty.png", sprite_highlight("svante"))
    fit "contain"
image svante alt_weird:
    At("images/Assets/Character Sprites/Svante Nordstrom/Normal - Alternate Pose/svante armor new pose weird.png", sprite_highlight("svante"))
    fit "contain"
image svante alt_base:
    At("images/Assets/Character Sprites/Svante Nordstrom/Normal - Alternate Pose/svante armor new pose.png", sprite_highlight("svante"))
    fit "contain"

# ===============================
# SVANTE — SLEEPWEAR
# ===============================
image svante sleepwear_angry:
    At("images/Assets/Character Sprites/Svante Nordstrom/Sleepwear/svante pajama angry.png", sprite_highlight("svante"))
    fit "contain"
image svante sleepwear_happy:
    At("images/Assets/Character Sprites/Svante Nordstrom/Sleepwear/svante pajama happy.png", sprite_highlight("svante"))
    fit "contain"
image svante sleepwear_nervous:
    At("images/Assets/Character Sprites/Svante Nordstrom/Sleepwear/svante pajama nervous.png", sprite_highlight("svante"))
    fit "contain"
image svante sleepwear_neutral:
    At("images/Assets/Character Sprites/Svante Nordstrom/Sleepwear/svante pajama neutral.png", sprite_highlight("svante"))
    fit "contain"
image svante sleepwear_sad:
    At("images/Assets/Character Sprites/Svante Nordstrom/Sleepwear/svante pajama sad.png", sprite_highlight("svante"))
    fit "contain"
image svante sleepwear_base:
    At("images/Assets/Character Sprites/Svante Nordstrom/Sleepwear/svante pajama.png", sprite_highlight("svante"))
    fit "contain"

# ===============================
# SVANTE — TIANHO CEREMONIAL
# ===============================
image svante ceremonial_angry:
    At("images/Assets/Character Sprites/Svante Nordstrom/Tianho Ceremonial/svante robe angry.png", sprite_highlight("svante"))
    fit "contain"
image svante ceremonial_happy:
    At("images/Assets/Character Sprites/Svante Nordstrom/Tianho Ceremonial/svante robe happy.png", sprite_highlight("svante"))
    fit "contain"
image svante ceremonial_nervous:
    At("images/Assets/Character Sprites/Svante Nordstrom/Tianho Ceremonial/svante robe nervous.png", sprite_highlight("svante"))
    fit "contain"
image svante ceremonial_neutral:
    At("images/Assets/Character Sprites/Svante Nordstrom/Tianho Ceremonial/svante robe neutral.png", sprite_highlight("svante"))
    fit "contain"
image svante ceremonial_sad:
    At("images/Assets/Character Sprites/Svante Nordstrom/Tianho Ceremonial/svante robe sad.png", sprite_highlight("svante"))
    fit "contain"
image svante ceremonial_base:
    At("images/Assets/Character Sprites/Svante Nordstrom/Tianho Ceremonial/svante robe.png", sprite_highlight("svante"))
    fit "contain"

# ===============================
# SVANTE — UNDERWEAR
# ===============================
image svante underwear_angry:
    At("images/Assets/Character Sprites/Svante Nordstrom/Underwear/svante emotions angry.png", sprite_highlight("svante"))
    fit "contain"
image svante underwear_happy:
    At("images/Assets/Character Sprites/Svante Nordstrom/Underwear/svante emotions happy.png", sprite_highlight("svante"))
    fit "contain"
image svante underwear_nervous:
    At("images/Assets/Character Sprites/Svante Nordstrom/Underwear/svante emotions nervous.png", sprite_highlight("svante"))
    fit "contain"
image svante underwear_neutral:
    At("images/Assets/Character Sprites/Svante Nordstrom/Underwear/svante emotions neutral.png", sprite_highlight("svante"))
    fit "contain"
image svante underwear_sad:
    At("images/Assets/Character Sprites/Svante Nordstrom/Underwear/svante emotions sad.png", sprite_highlight("svante"))
    fit "contain"
image svante underwear_base:
    At("images/Assets/Character Sprites/Svante Nordstrom/Underwear/svante base.png", sprite_highlight("svante"))
    fit "contain"

# TODO: fix file path
# =============================================================================
# SUPPLY ROBOT - All Sprite Variants
# =============================================================================
image supply_robot lied:
    At("images/Assets/Character Sprites/Supply Robot/supply robot colored v2hologram lied.png", sprite_highlight("supply_robot"))
    fit "contain"
image supply_robot normal:
    At("images/Assets/Character Sprites/Supply Robot/supply robot colored v2hologram normal.png", sprite_highlight("supply_robot"))
    fit "contain"
image supply_robot sad:
    At("images/Assets/Character Sprites/Supply Robot/supply robot colored v2hologram sad.png", sprite_highlight("supply_robot"))
    fit "contain"
image supply_robot base:
    At("images/Assets/Character Sprites/Supply Robot/supply robot colored v2hologram.png", sprite_highlight("supply_robot"))
    fit "contain"

# TODO: fix file path
# =============================================================================
#                            OTHER CHARACTERS
# =============================================================================
# =============================================================================
# OTHER SPRITES - Single Variants
# =============================================================================
image king_gustav:
    At("images/Assets/Character Sprites/Other Characters/king gustav nordstrom.png", sprite_highlight("king_gustav"))
    fit "contain"
image feng suit:
    At("images/Assets/Character Sprites/Other Characters/paladin feng suit.png", sprite_highlight("feng"))
    fit "contain"
image tedda_human:
    At("images/Assets/Character Sprites/Other Characters/tedda human form.png", sprite_highlight("tedda_alive"))
    fit "contain"
image vasily_rubric:
    At("images/Assets/Character Sprites/Other Characters/count vasilynorubics.png", sprite_highlight("vasily"))
    fit "contain"
image olympia:
    At("images/Assets/Character Sprites/Other Characters/empress olympia.png", sprite_highlight("olympia"))
    fit "contain"

# TODO: bookmark
# =============================================================================
# SINGLE SPRITES
# =============================================================================
image babala:
    At("images/Assets/Character Sprites/Babala.png", sprite_highlight("babala"))
    fit "contain"
image captain_kang:
    At("images/Assets/Character Sprites/captain kang sun woo colored.png", sprite_highlight("captain_sunwoo"))
    fit "contain"
image daniel:
    At("images/Assets/Character Sprites/daniel.png", sprite_highlight("daniel"))
    fit "contain"
image elara:
    At("images/Assets/Character Sprites/elara colored.png", sprite_highlight("elara"))
    fit "contain"
image emily:
    At("images/Assets/Character Sprites/emily.png", sprite_highlight("emily"))
    fit "contain"
image huli_jing:
    At("images/Assets/Character Sprites/Huli Jing.png", sprite_highlight("huli_jing"))
    fit "contain"
image hundun:
    At("images/Assets/Character Sprites/hundun.png", sprite_highlight("hundun"))
    fit "contain"
image king_long_shen:
    At("images/Assets/Character Sprites/king long shen copy.png", sprite_highlight("long_shen"))
    fit "contain"
image aoi_battle_suit:
    At("images/Assets/Character Sprites/lady aoi battle suit.png", sprite_highlight("aoi"))
    fit "contain"
image aoi_base:
    At("images/Assets/Character Sprites/lady aoi colored.png", sprite_highlight("aoi"))
    fit "contain"
image lucas:
    At("images/Assets/Character Sprites/lucas.png", sprite_highlight("lucas"))
    fit "contain"
image cyrus:
    At("images/Assets/Character Sprites/Paladin Cyrus colored.png", sprite_highlight("cyrus"))
    fit "contain"
image feng_suit:
    At("images/Assets/Character Sprites/paladin feng suit.png", sprite_highlight("feng"))
    fit "contain"
image pavel:
    At("images/Assets/Character Sprites/pavel colored v2.png", sprite_highlight("mjoll_pavel"))
    fit "contain"
image qiongqi:
    At("images/Assets/Character Sprites/Qiongqi.png", sprite_highlight("qiongqi"))
    fit "contain"
image queen_ekaterina:
    At("images/Assets/Character Sprites/Queen Ekaterina Drakos.png", sprite_highlight("queen_ekaterina"))
    fit "contain"
image sarah:
    At("images/Assets/Character Sprites/sarah.png", sprite_highlight("sarah"))
    fit "contain"
image soldier_gao:
    At("images/Assets/Character Sprites/soldier gao colored.png", sprite_highlight("gao"))
    fit "contain"
image soldier_jiang:
    At("images/Assets/Character Sprites/soldier Jiang colored.png", sprite_highlight("jiang"))
    fit "contain"
image taotie:
    At("images/Assets/Character Sprites/taotie.png", sprite_highlight("taotie"))
    fit "contain"
image tian_xun:
    At("images/Assets/Character Sprites/tian xun copy.png", sprite_highlight("tian_xun"))
    fit "contain"
image ya_ji_hye:
    At("images/Assets/Character Sprites/ya ji hye colored (1).png", sprite_highlight("ji_hye"))
    fit "contain"
image yaoguai:
    At("images/Assets/Character Sprites/yaoguai.png", sprite_highlight("yg")) # beast not yg king
    fit "contain"
image yuki_onna:
    At("images/Assets/Character Sprites/yuki onna v2.png", sprite_highlight("yuki_onna"))
    fit "contain"


# =============================================================================
# FOOD ILLUS
# =============================================================================
# TODO: add food illus in the game
image food1:
    At("images/Assets/Food Illustrations/FOOD1.png")
    fit "contain"
image food3:
    At("images/Assets/Food Illustrations/FOOD3.png")
    fit "contain"
image food4:
    At("images/Assets/Food Illustrations/FOOD4.png")
    fit "contain"
image food6:
    At("images/Assets/Food Illustrations/FOOD6.png")
    fit "contain"
image food7:
    At("images/Assets/Food Illustrations/FOOD7.png")
    fit "contain"
image food8:
    At("images/Assets/Food Illustrations/FOOD8.png")
    fit "contain"
image food9:
    At("images/Assets/Food Illustrations/FOOD9.png")
    fit "contain"
image food11:
    At("images/Assets/Food Illustrations/FOOD11.png")
    fit "contain"
image food12:
    At("images/Assets/Food Illustrations/FOOD12.png")
    fit "contain"
image food13:
    At("images/Assets/Food Illustrations/FOOD13.png")
    fit "contain"
image food14:
    At("images/Assets/Food Illustrations/FOOD14.png")
    fit "contain"
image food15:
    At("images/Assets/Food Illustrations/FOOD15.png")
    fit "contain"

