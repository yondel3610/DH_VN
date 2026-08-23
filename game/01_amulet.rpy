# ============================================================
# CH8 AMULET DOOR PUZZLE — click-to-rotate alignment (v2)
# ============================================================

init python:

    AMULET_A_CENTER = (640, 540)     # left third of 1920px width, vertical center
    AMULET_B_CENTER = (1280, 540)    # right third of 1920px width, vertical center
    AMULET_RADIUS = 220              # TODO: match real asset size
    ROTATE_STEP = 30                 # degrees per click
    GRID = [i * ROTATE_STEP for i in range(360 // ROTATE_STEP)]  # 12 positions

    def _random_grid_angle(exclude=None):
        choices = [a for a in GRID if a != exclude] if exclude is not None else GRID
        return renpy.random.choice(choices)

    def rotate_amulet(which):
        if which == "a":
            if store.amulet_a_locked:
                return
            store.amulet_a_angle = (store.amulet_a_angle + ROTATE_STEP) % 360
            store.amulet_a_locked = (store.amulet_a_angle == store.amulet_a_target)
            store.amulet_a_moved = True
        else:
            if store.amulet_b_locked:
                return
            store.amulet_b_angle = (store.amulet_b_angle + ROTATE_STEP) % 360
            store.amulet_b_locked = (store.amulet_b_angle == store.amulet_b_target)
            store.amulet_b_moved = True

        # TODO: placeholder - swap for the real amulet-turn sfx
        renpy.play(audio.stone_click)

        if store.amulet_a_locked and store.amulet_b_locked:
            store.amulet_puzzle_solved = True

        renpy.restart_interaction()

# reusable eased-rotation transform - the "ease 0.25 rotate angle" line is what
# makes each click animate smoothly to its new angle instead of snapping.
# xpos/ypos/anchor here are fractional (0.5, 0.5) so this works centered
# inside any button regardless of size.
transform amulet_spin(angle, instant):
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5
    ease (0.0 if instant else 0.25) rotate angle

# fade-in used when an amulet's glow ring first appears (i.e. once locked)
transform amulet_glow_fade:
    alpha 0.0
    linear 0.3 alpha 1.0

default amulet_a_angle = 0
default amulet_b_angle = 0
default amulet_a_target = 0
default amulet_b_target = 0
default amulet_a_locked = False
default amulet_b_locked = False
default amulet_a_moved = False
default amulet_b_moved = False
default amulet_puzzle_solved = False

screen amulet_door_puzzle():
    modal True
    zorder 200

    # TODO: placeholder - replace with the actual sealed-door background art
    add Transform("images/Assets/amulet_wall.png", zoom=1.3)

    text "Click each amulet to rotate it. Align both with the door's carvings.":
        xalign 0.5
        ypos 60
        size 34
        color "#e8d9b0"

    # ---------------- Amulet A ----------------
    button:
        xpos AMULET_A_CENTER[0] - AMULET_RADIUS
        ypos AMULET_A_CENTER[1] - AMULET_RADIUS
        xysize (AMULET_RADIUS * 2, AMULET_RADIUS * 2)
        action If(amulet_a_locked, None, Function(rotate_amulet, "a"))

        # TODO: placeholder - swap for the real jade amulet carving asset
        add Transform(
            "images/Assets/green_amulet1.png",
            xsize=AMULET_RADIUS * 2,
            ysize=AMULET_RADIUS * 2,
        ) at amulet_spin(amulet_a_angle, not amulet_a_moved)

        if amulet_a_locked:
            # TODO: placeholder - replace with real glow/particle asset
            add Transform(
                "images/Assets/green_amulet_outline.png",
                xsize=AMULET_RADIUS * 2 + 24,
                ysize=AMULET_RADIUS * 2 + 24,
                matrixcolor=TintMatrix("#00ff00"),
            ) at amulet_glow_fade:
                xpos AMULET_RADIUS
                ypos AMULET_RADIUS
                xanchor 0.5
                yanchor 0.5

    # ---------------- Amulet B ----------------
    button:
        xpos AMULET_B_CENTER[0] - AMULET_RADIUS
        ypos AMULET_B_CENTER[1] - AMULET_RADIUS
        xysize (AMULET_RADIUS * 2, AMULET_RADIUS * 2)
        action If(amulet_b_locked, None, Function(rotate_amulet, "b"))

        # TODO: placeholder - swap for the real jade amulet carving asset
        add Transform(
            "images/Assets/green_amulet1.png",
            xsize=AMULET_RADIUS * 2,
            ysize=AMULET_RADIUS * 2,
        ) at amulet_spin(amulet_b_angle, not amulet_b_moved)

        if amulet_b_locked:
            # TODO: placeholder - replace with real glow/particle asset
            add Transform(
                "images/Assets/green_amulet_outline.png",
                xsize=AMULET_RADIUS * 2 + 24,
                ysize=AMULET_RADIUS * 2 + 24,
                matrixcolor=TintMatrix("#00ff00"),
            ) at amulet_glow_fade:
                xpos AMULET_RADIUS
                ypos AMULET_RADIUS
                xanchor 0.5
                yanchor 0.5

    # status labels
    text "{}".format("Aligned" if amulet_a_locked else "Click to rotate"):
        xpos AMULET_A_CENTER[0]
        ypos AMULET_A_CENTER[1] + AMULET_RADIUS + 30
        xanchor 0.5
        color ("#88ff88" if amulet_a_locked else "#cccccc")
        size 24

    text "{}".format("Aligned" if amulet_b_locked else "Click to rotate"):
        xpos AMULET_B_CENTER[0]
        ypos AMULET_B_CENTER[1] + AMULET_RADIUS + 30
        xanchor 0.5
        color ("#88ff88" if amulet_b_locked else "#cccccc")
        size 24

    if amulet_puzzle_solved:
        # TODO: placeholder - swap for the real "stone click" sfx
        $ renpy.play(audio.amulet_door)
        timer 1.75 action Return() repeat False

label ch8_amulet_door_puzzle:

    python:
        amulet_a_target = _random_grid_angle()
        amulet_b_target = _random_grid_angle()
        amulet_a_angle = _random_grid_angle(exclude=amulet_a_target)
        amulet_b_angle = _random_grid_angle(exclude=amulet_b_target)
        amulet_a_locked = False
        amulet_b_locked = False
        amulet_a_moved = False
        amulet_b_moved = False
        amulet_puzzle_solved = False

    show screen amulet_door_puzzle
    with Dissolve(0.6)

    $ ui.interact()

    hide screen amulet_door_puzzle
    with Dissolve(0.6)

    return