# # The script of the game goes in this file.

# # Declare characters used by this game. The color argument colorizes the
# # name of the character.

# define e = Character("Eileen")


# # The game starts here.

# label start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg room

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show eileen happy

#     # These display lines of dialogue.

#     e "You've created a new Ren'Py game."

#     e "Once you add a story, pictures, and music, you can release it to the world!"

#     # This ends the game.

#     return

# =============================================================================
# CUSTOM TRANSITIONS — defined once, available to all .rpy files
# =============================================================================
# Ren'Py built-ins used for reference:
#   fade      = fade through black, ~1.0s  (scene changes, calm moments)
#   dissolve  = cross-dissolve,     ~0.5s  (smooth cuts, sprite changes)
#   flash     = white flash,        ~0.5s  (explosions, divine moments)
#   None      = instant hard cut           (no animation at all)

# shock_cut — jarring instant cut for violence, monster attacks, sudden shocks.
# Uses ImageDissolve with a pure black image to simulate a hard frame snap.
# Duration 0.1s is fast enough to feel instant but avoids a single-frame flash.
define shock_cut = Fade(0.0, 0.0, 0.1)

# slow_fade — heavier cinematic fade for chapter ends, deaths, sedation.
# Longer than the built-in 'fade' — use for weight and finality.
define slow_fade = Fade(0.3, 0.5, 0.3)

# fast_dissolve — quicker version of dissolve for sprite swaps mid-scene.
define fast_dissolve = Dissolve(0.2)    

label start:
    jump prologue