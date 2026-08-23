screen cheng_letter():
    modal True

    # dissolve effect
    on "hide" action With(dissolve)

    add "gui/chengletter_bg.jpg":
        xalign 0.5
        yalign 0.0
        yoffset -55
        zoom 1.0
    
    # Click anywhere to close
    button:
        xfill True
        yfill True
        background None
        action Hide("cheng_letter"), Return()
    
    viewport:
        xalign 0.5
        yalign 0.7
        xsize 700
        ysize 900
        draggable True
        mousewheel True
        
        vbox:
            spacing 15
            text "Dearest Paladin Dorian,":
                font "fonts/© 2020 NUGS Project Khiara Script.ttf"
                size 65
                color "#000000"
                xalign 0.0
            text "I hope this letter finds you well, though I fear it may be too long since we last spoke. I often think of the day you saved me from the tragedy that befell Tianho. Without your bravery, I would not be alive to write these words today. For that, I am eternally grateful. For the Prosperity Dragon, and to you.\n":
                font "fonts/© 2020 NUGS Project Khiara Script.ttf"
                size 55
                color "#000000"
                justify True
            text "Word has reached me that you were seen in Mjoll, alive and—dare I hope—well. Knowing this fills my heart with relief. You've been on my mind these past years, and I've often wondered how you've managed, given the burdens you carry.":
                font "fonts/© 2020 NUGS Project Khiara Script.ttf"
                size 55
                color "#000000"
                justify True
            text "\nPlease, do not hesitate to reach out if ever you are in need of anything. Cheng Industries owes you a debt that cannot be repaid with gold alone. Your kindness and courage have left an indelible mark on my life.":
                font "fonts/© 2020 NUGS Project Khiara Script.ttf"
                size 55
                color "#000000"
                justify True
            text "\nIf you are interested, I would like to invite you to have tea with me. The city may have changed, but my doors will always remain open to you. Perhaps I can repay a fraction of what you have given me, even if it's only with the comfort of good tea and company.":
                font "fonts/© 2020 NUGS Project Khiara Script.ttf"
                size 55
                color "#000000"
                justify True
            text "\nProsperity Dragon willing, we will see again.\n\nWith deepest gratitude and fondness,\nCheng Yuxuan.\n\n\n\n":
                font "fonts/© 2020 NUGS Project Khiara Script.ttf"
                size 55
                color "#000000"
                xalign 0.0

init python:
    # One entry per page - only days that actually have content. Add/remove
    # dicts here to add/remove pages; no other code needs to change.
    HWAN_SIK_PAGES = [
        {
            "day": "Day 1",
            "ink": "#2b1c12",
            "paragraphs": [
                "I failed him. I failed my sworn duty. His Majesty, the Emperor Lord. Pyeha and pyeha-sshi was killed… Murdered in cold blood. Pyeha and pyeha-sshi's body was dragged out by the aldoriths… Bastards that they are…",
                "I do not know if anyone will ever read this, but I must write. If only to keep my mind from slipping. If only to leave something behind when my body joins the others.",
                "We came here for knowledge. That was what they told us. His Majesty was led by the rulers and scholars deep into this place. I was ordered to protect him, but I— I was struck down before I could even raise my blade. Now I am alone.",
                "The door is sealed. I have pounded on it until my fists bled. No one is coming.",
                "The pain is dulling, which should bring me relief, but it does not. The skin is turning dark. Swollen. I do not think I will last long.",
            ],
        },
        {
            "day": "Day 3",
            "ink": "#3a1414",
            "paragraphs": [
                "I found something. A button —hidden beneath dust and debris. It took a while for me to solve the puzzle, but I managed to follow her footsteps. I think I unlocked something.",
                "But my hand trembles as I write. The infection is spreading. The veins in my arm are blackened. It hurts to breathe. I hope it gets better tomorrow.",
            ],
        },
        {
            "day": "Day 5",
            "ink": "#3a1414",
            "paragraphs": [
                "My arm… the skin is splitting. Fever grips me like a vice. I tried to burn the infection out, but I could not hold the knife steady.",
                "I keep hearing things. Scraping in the dark. Breathing. But I know I am alone. Aren't I?",
            ],
        },
        {
            "day": "Day 8",
            "ink": "#3a1414",
            "paragraphs": [
                "The rations are gone. I can barely stand. My stomach feels like a hollow pit. My body is light—too light.",
                "The dead are everywhere, but some of them… they should not be this well preserved. Some of them have been here for decades. Maybe centuries. And yet, they have not rotted.",
                "I found records. They were studying the dead. What were they trying to do? Why did they bring rulers, scholars—the Emperor Lord, pyeha, himself—into this cursed place?",
            ],
        },
        {
            "day": "Day 13",
            "ink": "#4a0000",
            "paragraphs": [
                "I tried everything. Every switch. Every carving. Every prayer I can still remember.",
                "I do not have the power to free him. But I know someone is inside that stupid ice. By Xianlun, I do not have the power to free myself.",
                "My breath is shallow, my vision fading. The infection has reached my chest. I will not last much longer.",
                "I found a container of syringes. A potent sleeping agent. A quiet way to go. There are two. I only need one.",
                "But if anyone finds this… if you are reading, hearing these words— Know that Kyeongjang did not fall to cowards.",
                "Xianlun, I draw near… Seok-jin, I love you. I'm sorry I couldn't fulfill my promise…",
            ],
        },
    ]

    HWAN_SIK_PAGE_COUNT = len(HWAN_SIK_PAGES)

    def hwan_sik_prev_page():
        if store.hwan_sik_page > 1:
            store.hwan_sik_page -= 1
            renpy.restart_interaction()

    def hwan_sik_next_page():
        # only called while NOT on the last page - see the button's If() below,
        # the last-page case is handled directly by Hide+Return instead.
        store.hwan_sik_page += 1
        renpy.restart_interaction()

default hwan_sik_page = 1

screen hwan_sik_paper():
    modal True

    # dissolve effect
    on "hide" action With(dissolve)

    $ page_data = HWAN_SIK_PAGES[hwan_sik_page - 1]

    # TODO: placeholder - replace with the actual 4096x6144 diary page art.
    # "fit" contain scales the whole image down to fit on screen without
    # cropping or distorting it (letterboxed left/right on a 1920x1080
    # screen since the art is portrait) - swap to fit="cover" if you'd
    # rather fill the screen and crop the edges instead.
    add Transform("images/Assets/parchmentish 1.png", zoom=0.25):
        xalign 0.5
        yalign 0.5

    # ---------------- left click zone: previous page ----------------
    button:
        xpos 0
        ypos 0
        xsize 480
        yfill True
        background None
        action If(hwan_sik_page > 1, Function(hwan_sik_prev_page), None)

    # ---------------- right click zone: next page / exit on last page ----------------
    button:
        xpos 1440
        ypos 0
        xsize 480
        yfill True
        background None
        action If(
            hwan_sik_page < HWAN_SIK_PAGE_COUNT,
            Function(hwan_sik_next_page),
            [Hide("hwan_sik_paper"), Return()],
        )

    # page hints - purely optional, remove if the art already signals turnable edges
    if hwan_sik_page > 1:
        text "◀":
            xpos 40
            yalign 0.5
            size 40
            color "#e8d9b0"

    text ("▶" if hwan_sik_page < HWAN_SIK_PAGE_COUNT else "Close"):
        xpos 1880
        xanchor 1.0
        yalign 0.5
        size 40
        color "#e8d9b0"

    text "[hwan_sik_page]/[HWAN_SIK_PAGE_COUNT]":
        xalign 0.5
        ypos 30
        size 28
        color "#e8d9b0"

    # ---------------- page content (scrollable if the entry runs long) ----------------
    viewport:
        xalign 0.5
        yalign 0.55
        xsize 900
        ysize 780
        draggable True
        mousewheel True

        vbox:
            spacing 15

            text page_data["day"]:
                # TODO: placeholder - swap for a rougher/handwritten diary font
                font "fonts/© 2020 NUGS Project Khiara Script.ttf"
                size 60
                color page_data["ink"]
                xalign 0.0

            for paragraph in page_data["paragraphs"]:
                text paragraph:
                    font "fonts/© 2020 NUGS Project Khiara Script.ttf"
                    size 50
                    color page_data["ink"]
                    justify True

label show_hwan_sik_diary:

    $ hwan_sik_page = 1

    show screen hwan_sik_paper
    with Dissolve(0.6)

    $ ui.interact()

    hide screen hwan_sik_paper
    with Dissolve(0.6)

    return
