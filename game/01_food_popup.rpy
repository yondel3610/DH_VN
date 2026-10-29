# =============================================================================
# FOOD POPUP — quick 3-second "got an item" style notification (no flair)
# Usage in script:  $ food_popup("food1", "Spring Bite Skewers")
# The border color is looked up from FOOD_REGION, so call sites don't change.
# =============================================================================

define FOOD_POPUP_TIME = 3.0

# Border color per region
define FOOD_REGION_COLORS = {
    "mjoll":      "#f4f8ff",   # snow white
    "tianho":     "#a01c24",   # deep red
    "hinami":     "#2f4b8f",   # ai-iro (traditional Japanese indigo); matches Hinami's blue-teal castle art
    "kyeongjang": "#4fa38c",   # celadon / dancheong jade (Korean)
    "gale":       "#9aa8b5",   # storm grey (Dorian's home; not in your list, change freely)
}

# Which region each dish belongs to
define FOOD_REGION = {
    "food1":  "tianho",       # Spring Bite Skewers
    "food3":  "tianho",       # Bamboo Crystal Cakes
    "food4":  "mjoll",        # Zaryba Stew
    "food6":  "tianho",       # Golden Fish Omelette (Tianho white-scaled fish)
    "food7":  "tianho",       # Fish and Vegetable Soup
    "food8":  "tianho",       # Pan-Fried Golden Fish
    "food9":  "tianho",       # Fish Fried Rice
    "food11": "mjoll",        # Mjollian Mead-Braised Lamb
    "food12": "tianho",       # Tianho Flan
    "food13": "gale",         # Imperial Truffle Roast (the "Gale" dish)
    "food14": "tianho",       # Moonlit Noodles
    "food15": "hinami",       # Fisherman's Hotpot
}

init python:
    def food_border(color):
        # hollow 5px outline: four thin bars inside a 12x12 tile, stretched by Frame
        return Frame(
            Fixed(
                Transform(Solid(color, xysize=(12, 5)), pos=(0, 0)),
                Transform(Solid(color, xysize=(12, 5)), pos=(0, 7)),
                Transform(Solid(color, xysize=(5, 12)), pos=(0, 0)),
                Transform(Solid(color, xysize=(5, 12)), pos=(7, 0)),
                xysize=(12, 12)),
            5, 5)

    def food_popup(img, name="", region=None):
        # region can be passed explicitly, otherwise it comes from FOOD_REGION
        if region is None:
            region = FOOD_REGION.get(img, "tianho")
        border = FOOD_REGION_COLORS.get(region, "#ffffff")
        # hide first so back-to-back dishes restart the timer cleanly
        renpy.hide_screen("food_popup")
        renpy.show_screen("food_popup", img=img, name=name, border=border)

screen food_popup(img, name="", border="#ffffff"):
    zorder 95

    frame at food_popup_anim:
        xalign 0.5
        ypos 140
        background food_border(border)
        padding (5, 5)

        frame:
            background Solid("#00000070")
            padding (32, 22)
            hbox:
                spacing 32
                add img fit "contain" xysize (260, 260)
                if name:
                    text "[name!tq]":
                        yalign 0.5
                        size 42
                        color "#ffffff"
                        outlines [(2, "#00000080", 0, 0)]
                        xmaximum 760

    timer FOOD_POPUP_TIME action Hide("food_popup")

transform food_popup_anim:
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.4 alpha 0.0
