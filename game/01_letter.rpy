screen cheng_letter():
    modal True

    # dissolve effect
    on "show" action With(dissolve)
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