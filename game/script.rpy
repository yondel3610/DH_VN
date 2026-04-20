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

# Custom chapter start transition
label chapter_start(bg_image, hold_duration=2.0, fade_duration=2.5):
    stop music fadeout 2.0
    
    # Black screen
    scene black
    with None
    $ renpy.pause(0.1, hard=True)
    
    # Hold black
    pause hold_duration
    
    # Fade to background
    scene expression bg_image
    with Fade(0.5, 0.0, 2.5)  # 0.5s fade out, no hold, 2.5s fade in
    
    pause 0.5
    return