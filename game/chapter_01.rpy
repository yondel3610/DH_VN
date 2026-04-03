# The use of ClaudeCode and Deepseek V3 are stricly for formatting and debugging purposes
# AI has been used to make production and documentation faster, not to make the whole thing itself

#  CONTENTS:
#    Section 1  — Character Definitions (Chapter 1 cast)
#    Section 2  — Image Declarations   (all BGs and CGs)
#    Section 3  — Audio Declarations   (all music and SFX)
#    Section 4  — Game Variables       (affection, trackers, visit flags)
#    Section 5  — label chapter_1      (Dorian's Room opening)
#    Section 6  — label ch1_city       (repeatable city exploration menu)
#    Section 7  — City sub-scenes      (Deng / Fanrong / Xiangli / Zhong)
#    Section 8  — label ch1_common_fireworks  (city convergence)
#    Section 9  — label ch1_auditions  (D2 — Niko/Kaito)
#    Section 10 — label ch1_long_shen  (D3 — Cyrus interruption)
#    Section 11 — label ch1_elara_chat (D4 — repeatable night chat)
#    Section 12 — label ch1_battle     (D5–D10 — castle battle + Taotie QTCs)
#    Section 13 — label game_over      (shared GAME OVER screen)
#    Section 14 — label ch1_common_end (post-battle convergence + epilogue)

# =============================================================================
# SECTION 1: CHARACTER DEFINITIONS
# =============================================================================
# All characters who speak in Chapter 1.
# Move all character defines to a shared characters.rpy once you have
# more than one chapter file — Ren'Py loads all .rpy files in /game/ together,
# so a single characters.rpy visible to every chapter is best practice.

# Characters already defined in prologue.rpy (yk, boy_ald, girl_ald, kristin)
# are NOT redefined here. Ren'Py will load both files simultaneously.
# =============================================================================
# TODO: make compiled character files

define dorian         = Character("Dorian",          color="#d4af37")  # Gold — paladin, protagonist
define narrator       = Character("",                color="#ffffff")  # Blank name = pure narration
define elara          = Character("Elara",           color="#f4a7b9")  # Soft rose — warm, loving
define lucas          = Character("Lucas",           color="#87ceeb")  # Sky blue — youngest, excited
define sarah          = Character("Sarah",           color="#dda0dd")  # Plum — artistic, quiet
define emily          = Character("Emily",           color="#f0e68c")  # Khaki — witty, streetwise
define daniel         = Character("Daniel",          color="#90ee90")  # Light green — cool, sarcastic
define cyrus          = Character("Paladin Cyrus",   color="#8b0000")  # Dark red — authoritarian
define feng           = Character("Paladin Feng",    color="#4169e1")  # Royal blue — loyal, warm
define olympia        = Character("Empress Olympia", color="#9370db")  # Medium purple — regal
define long_shen      = Character("King Long Shen",  color="#228b22")  # Forest green — Tianho king
define emperor_minjoon = Character("Emperor Min-joon", color="#b8860b") # Dark gold — Kyeongjang
define niko           = Character("Niko",            color="#e0c8a0")  # Warm parchment — healer, devout
define kaito          = Character("Kaito",           color="#b0d0e0")  # Pale blue — Niko's brother
define yuxuan         = Character("Cheng Yuxuan",    color="#00ced1")  # Dark turquoise — inventor
define vasily         = Character("Count Vasily",    color="#c0c0c0")  # Silver — Dorian's commander
define gao            = Character("Soldier Gao",     color="#a0a0a0")  # Grey — reliable soldier
define jiang          = Character("Soldier Jiang",   color="#a0a0a0")  # Grey — reliable soldier
define prosperity_dragon = Character("Prosperity Dragon", color="#ffd700") # Bright gold — divine voice
define performers     = Character("Nervous Performer", color="#ff8c00") # Orange — festival performers
define vendor         = Character("Vendor",          color="#cd853f")  # Peru — market vendor
define taotie_roar    = Character("",                color="#ff0000")  # Red, no name — monster sounds

# =============================================================================
# SECTION 2: IMAGE DECLARATIONS + BACKGROUND/SPRITE GUIDE
# =============================================================================
# PLACEHOLDER: Replace all path strings with real asset paths.
# All paths are relative to the /game/ folder.
# =============================================================================
# TODO: add image assets
# --- Backgrounds: Dorian's Room and Hotel ---
image bg_tianho_dorians_room:
    "images/Assets/Background/Livingroom.LightsON.1920x1080.png"
    size (1920, 1080) # STANDARD FOR ALL FUTURE BG
    xalign 0.5
    yalign 1.0
    
# --- Backgrounds: Tianho City Night ---
image bg_tianho_city_night       = "images/backgrounds/bg_tianho_city_night.png"         # PLACEHOLDER

# --- Backgrounds: City Exploration Locations ---
image bg_tianho_deng_blossom     = "images/backgrounds/bg_tianho_deng_blossom.png"       # PLACEHOLDER

image bg_tianho_fanrong_square   = "images/backgrounds/bg_tianho_fanrong_square.png"     # PLACEHOLDER

image bg_tianho_xiangli_stalls   = "images/backgrounds/bg_tianho_xiangli_stalls.png"     # PLACEHOLDER

image bg_tianho_zhong_promenade  = "images/backgrounds/bg_tianho_zhong_promenade.png"    # PLACEHOLDER

# --- Backgrounds: Castle and Ceremony ---
image bg_tianho_castle_interior  = "images/backgrounds/bg_tianho_castle_interior.png"    # PLACEHOLDER
image bg_tianho_castle_balcony   = "images/backgrounds/bg_tianho_castle_balcony.png"     # PLACEHOLDER
image bg_tianho_celeb_deng       = "images/backgrounds/bg_tianho_celeb_deng.png"         # PLACEHOLDER

# --- Backgrounds: Night and Dream ---
image bg_dorians_room_night      = "images/backgrounds/bg_dorians_room_night.png"        # PLACEHOLDER
image bg_dream_white             = "images/backgrounds/bg_dream_white.png"               # PLACEHOLDER

# --- Backgrounds: Battle ---
image bg_tianho_castle_gate      = "images/backgrounds/bg_tianho_castle_gate.png"        # PLACEHOLDER
image bg_tianho_castle_interior_battle = "images/backgrounds/bg_tianho_castle_interior_battle.png" # PLACEHOLDER
image bg_tianho_stairway         = "images/backgrounds/bg_tianho_stairway.png"           # PLACEHOLDER
image bg_tianho_city_on_fire     = "images/backgrounds/bg_tianho_city_on_fire.png"       # PLACEHOLDER
image bg_tianho_underground_2    = "images/backgrounds/bg_tianho_underground_2.png"      # PLACEHOLDER

# --- CGs (Full-screen Event Illustrations) ---
image cg_emperor_arrival         = "images/cg/cg_emperor_arrival.png"                    # PLACEHOLDER
image cg_prosperity_dragon_dream = "images/cg/cg_prosperity_dragon_dream.png"            # PLACEHOLDER
image cg_olympia_vision          = "images/cg/cg_olympia_vision.png"                     # PLACEHOLDER
image cg_elara_children_death    = "images/cg/cg_elara_children_death.png"               # PLACEHOLDER
image cg_winged_god_appears      = "images/cg/cg_winged_god_appears.png"                 # PLACEHOLDER
image cg_taotie_charge           = "images/cg/cg_taotie_charge.png"                      # PLACEHOLDER
image cg_feng_eye_injury         = "images/cg/cg_feng_eye_injury.png"                    # PLACEHOLDER
image cg_black                   = "images/cg/cg_black.png"                              # PLACEHOLDER

# =============================================================================
# SECTION 3: AUDIO DECLARATIONS
# =============================================================================
# All audio used in Chapter 1.
# Format: define audio.name = "path/to/file.ogg"
# PLACEHOLDER: Replace each path with your real .ogg file.
# =============================================================================
# TODO: fix audio 
# --- Music ---
# define audio.ost_tianho_festival # upbeat plays during the city exploration sequence
# define audio.ost_emperor_arrival  #Grand ceremonial fanfare — plays as Emperor Min-joon enters
# define audio.ost_dream_dragon   #ethereal — prosperity Dragon dream sequence
# define audio.ost_tension_rising      
# define audio.ost_battle_tianho       
# define audio.ost_taotie_battle       
# define audio.ost_tragedy     

# --- SFX ---
# define audio.sfx_fireworks #find free fireworks sfx   
# define audio.sfx_yaoguai_roar # monster roar
# define audio.sfx_explosion #find free explosion audio
# define audio.sfx_stone_spike #stone spike 
# define audio.sfx_wind_blast #wind blast from other games basta kung ano mas fit
# define audio.sfx_heartbeat  #heartbeat audio
# define audio.amb_festival_crowd   #festival crowd (anime festival sounds type shit?) | to be called again in ch2
# define audio.amb_castle_battle   #get from asian war dramas

# ========== VOICE LINES ==========
# TODO: add voice lines

# =============================================================================
# SECTION 4: GAME VARIABLES
# =============================================================================
# --- Affection / relationship trackers (persist across all chapters) ---
default niko_affection    = 0   # Niko romance/trust tracker
default feng_affection    = 0   # Feng respect/loyalty tracker

# --- Chapter-specific trackers ---
default yuki_tracker      = 0   # YUKI — unlocks Yuki-onna content in later chapters

# --- City exploration visit flags ---
# True once the player visits that location (Zhong locks after first visit)
default city_visited_deng    = False
default city_visited_fanrong = False
default city_visited_xiangli = False
default city_visited_zhong   = False   # Locks permanently after first visit

# --- Elara chat topic flags (for the repeatable D4 menu) ---
default elara_talked_cyrus   = False
default elara_talked_feng    = False
default elara_talked_olympia = False
# Note: Talking about Emperor Min-joon ends the chat loop — no flag needed

# --- Chapter 1 choice records (for optional flavour callbacks later) ---
default ch1_audition_choice  = ""   # "intervene" or "silent"
default ch1_cyrus_choice     = ""   # "obey" or "told_off"
default ch1_gate_qtc         = ""   # "nothing" / "shield" / "fireball"
default ch1_castle_qtc       = ""   # "freeze" / "spikes"
default ch1_stair_qtc        = ""   # "wind" / "stumble"

# =============================================================================
# SECTION 5: LABEL CHAPTER_1 — Opening (Dorian's Room)
# =============================================================================
# Entry point. Jumped to from prologue.rpy via 'jump chapter_1'.
# Scene: Tianho hotel room, evening. Dorian watches the city with binoculars.
# Elara drags him out to the lantern markets.
# =============================================================================
label chapter_1:

    # -------------------------------------------------------------------------
    # OPENING — Dorian's Room, evening
    # BG: bg_tianho_dorians_room
    # Music: ost_tianho_festival (soft intro volume)
    # -------------------------------------------------------------------------

    # Fade in from the chapter title card black
    scene bg_tianho_dorians_room with fade

    # Festival music starts soft — they're inside looking out
    play music ost_tianho_festival volume 0.4 fadein 2.0  # PLACEHOLDER — ost_tianho_festival

    # Pure narration — no character tag, no name box
    "I exhale a slow breath, watching the evening lights bathe the city of Tianho through my binoculars, reflecting off the rivers that weave through its heart like threads of silver."
    "The air smells of spiced tea and roasted chestnuts from the market stalls below, mingling with the faint fragrance of cherry blossoms that line the cobblestone streets."
    "The streets below are bustling with life, lined with towering pagodas adorned in colors of crimson, gold, and jade. Lanterns of every imaginable hue float above the streets, their light glowing softly."

    # show elara happy at right with dissolve   # PLACEHOLDER — Elara sprite (leaning on doorframe, amused)

    elara "Dorian. Are you even listening to me? You've been standing there for a while now."

    "I turn to face her, sighing as I pocket my binoculars. She's leaning against the doorframe, arms crossed, a wry smile playing on her lips."

    elara "You've been standing there long enough to memorize every single detail of the city. Meanwhile, the children are pestering me about seeing the nighttime lantern markets."
    elara "I would very much like my HUSBAND to take me there as soon as possible before he vanishes to work tomorrow."

    "I sigh, turning back to the view."

    dorian "My heart, you know how important tomorrow is. Everything has to be perfect."

    # show elara understanding at right         # PLACEHOLDER — Elara, softer expression

    elara "I know, Dorian. I know how important it is. The entire world will be watching as Kyeongjang's emperor makes his first public appearance in centuries."
    dorian "For centuries, Kyeongjang was nothing more than a legend. Many doubted it even existed, and now, their emperor is emerging from the shadows to reconnect."
    dorian "This meeting isn't just a reunion—it's a turning point. Alliances will shift. Trade will flourish—or collapse. Power balances will be rewritten."
    dorian "And you know Her Majesty. She won't settle for anything less than perfection."

    # Elara steps closer — tender moment before the city adventure
    # show elara gentle at right                # PLACEHOLDER — Elara stepping closer, soft smile

    elara "And you, sir Dorian. You're part of that perfection, aren't you? The Dragon of Gale, second only to the High Paladin himself. You'll make sure it all goes smoothly, like you always do."

    "I manage a faint smile, but the tension in my chest doesn't ease. She notices, of course. She always does."

    elara "But, my heart. That's tomorrow. Tomorrow is for the world, the king and the empress and the emperor and their grand, history-altering plans. But tonight?"

    "She steps even closer, giving my cheek a kiss."

    elara "Tonight, you're not the Dragon of Gale. You're not a paladin. You're my husband. And the father of four wonderful, slightly rambunctious children who are dying to explore this incredible city."
    dorian "But, my heart…"
    elara "No excuses, my heart. You've been working tirelessly ever since we left Gale. Tonight is for us. For me. For the kids who adore their father. For a family that rarely gets days like this together."

    "I sigh, a small smile finally breaking through my resolve. I kiss her."

    dorian "Alright, my heart. You win."

    "She returns my kiss, but only briefly as she quickly pulls away. She grabs my hand and pulls me toward the door, her laughter filling the balcony."

    elara "Come on, Dragon of Gale. The lantern markets won't wait, and neither will the kids!"

    # -------------------------------------------------------------------------
    # CUT TO: Tianho City Night
    # BG: bg_tianho_city_night
    # 'scene' wipes Elara's sprite automatically — no need to hide her first
    # Music: ost_tianho_festival (full volume — now outside in the festival)
    # -------------------------------------------------------------------------

    scene bg_tianho_city_night with dissolve    # PLACEHOLDER — Tianho city night, festival crowds

    play music ost_tianho_festival volume 0.8   # Full volume now — city is loud and alive
    play audio amb_festival_crowd loop fadein 1.5  # PLACEHOLDER — crowd ambient loop

    "The moment we step out into the street, the kids swarm us, buzzing with excitement."

    # show lucas excited at left with dissolve   # PLACEHOLDER — Lucas sprite (tugging at Dorian's sleeve)

    lucas "Dad! Dad! Look! Look at all the people! This place is huge!"

    "Lucas' eyes are open wide as he keeps tugging at the hem of my tunic with both hands."
    "I chuckle, bending down to ruffle his hair."

    dorian "Yes, it is. But remember what I said—stay close, okay?"

    # show sarah distracted at center with dissolve  # PLACEHOLDER — Sarah sprite (nose in sketchbook)

    "Sarah, as expected, is lost in her own world, flipping through her sketchbook and occasionally glancing up to capture the essence of the city in her drawings."

    elara "Sarah… Sarah… Honey. *snaps her fingers* Your father is here."

    sarah "*mumbles* Oh, hey dad!"

    "She glances quickly at me, smiles, then turns back, completely absorbed in her art."

    sarah "This place is full of colors. I need to capture the lanterns. But, I don't know what color they should be…"

    # show emily conspiratorial at right         # PLACEHOLDER — Emily sprite (whispering to Daniel)
    # show daniel smirking at right              # PLACEHOLDER — Daniel sprite (trying not to laugh)

    "Emily leans over to Daniel and whispers something in his ear, making him roll his eyes but smirk at the same time."

    emily "Come on, Daniel! You have to at least pretend to be excited!"
    daniel "Hey, I am excited! Just not the way you are."
    dorian "Come on, kids. We're going to the market."

    elara "But stay close to your father and me. Tianho may be beautiful, but—"
    emily "You never know what lurks beneath the hearts of strangers and how we kids are gullible and—"
    daniel "We know that, mom! Stranger Danger a thousand times. Can we just hurry up? I wanna see some dragons."

    sarah "Mom, we need to see the dragons!"

    # show elara amused at left                  # PLACEHOLDER — Elara, sighing fondly

    "Sarah finally closes her sketchbook, tucking it under her arm."

    elara "Alright, alright. Let's go see them. But remember, no pretending to be dragons."

    # =========================================================================
    # SECTION 6: D1 — CITY EXPLORATION (Repeatable Menu)
    # =========================================================================
    # The player can visit 3 of 4 locations freely.
    # Zhong Lotus Promenade locks after the first visit (flag: city_visited_zhong).
    # The menu loops back to itself after each visit via 'call' + 'jump'.
    # Selecting "Head to the castle ceremony" ends the exploration phase.
    #
    # PATTERN USED:
    #   jump ch1_city  →  the menu label
    #   Each option:   call ch1_city_LOCATION  (temporary jump, returns here)
    #                  then jumps back to ch1_city to show menu again
    # =========================================================================

    jump ch1_city   # Jump to the city exploration menu


# =============================================================================
# SECTION 6: LABEL CH1_CITY — Repeatable City Menu (Static Choices)
# =============================================================================

label ch1_city:

    menu:
        "Deng Blossom Avenue — Lanterns.":
            $ city_visited_deng = True
            call ch1_city_deng
            jump ch1_city

        "Fanrong Dragon Square — Dragon Dances.":
            $ city_visited_fanrong = True
            call ch1_city_fanrong
            jump ch1_city

        "Xiangli Centre — Food Stalls.":
            $ city_visited_xiangli = True
            call ch1_city_xiangli
            jump ch1_city

        "Zhong Lotus Promenade — Inventors." if not city_visited_zhong:
            $ city_visited_zhong = True
            call ch1_city_zhong
            jump ch1_city

        "Head to the castle — the ceremony is soon.":
            jump ch1_common_fireworks

# =============================================================================
# SECTION 7: CITY SUB-SCENES
# Each is a 'label' called from ch1_city. They end with 'return'
# which sends execution back to the 'call' line in ch1_city.
# =============================================================================

# -----------------------------------------------------------------------------
# D1-A: DENG BLOSSOM AVENUE — Lanterns
# BG: bg_tianho_deng_blossom
# Sarah sketches. Family watches fire channelers rehearse.
# -----------------------------------------------------------------------------

label ch1_city_deng:

    scene bg_tianho_deng_blossom with dissolve  # PLACEHOLDER — Deng Blossom Avenue

    "The avenue glows with hundreds of hanging lanterns, each one a different hue—crimson, jade, saffron, pearl. Fire channelers on the central stage rehearse their act, conjuring spiraling ribbons of flame."

    # show sarah sketching at center             # PLACEHOLDER — Sarah sprite (sketching, wonder)
    # show lucas pointing at left                # PLACEHOLDER — Lucas sprite (pointing at fire)
    # show elara watching at right               # PLACEHOLDER — Elara sprite (warm smile)

    sarah "The light… it changes every second. I can't keep up."
    lucas "FIRE! They made a DRAGON out of fire!! Dad, did you see?!"
    dorian "I saw, Lucas. I saw."
    elara "She hasn't stopped drawing since we arrived. Look at that concentration."

    "The fire channelers spiral their flames into the shape of a great serpentine dragon. The crowd around them gasps and applauds."

    # show performers nervous at left with dissolve  # PLACEHOLDER — Nervous Performer sprite

    performers "Is it too fast? The finale is supposed to hold for ten counts, but my partner keeps breaking early."
    performers "Sorry, sorry—let's go from the top."

    "Sarah tears a page from her sketchbook and holds it up — a rough sketch of the fire dragon, surprisingly accurate."

    sarah "I captured it. Before it disappeared."
    lucas "Whoa! Sarah that looks REAL!"
    daniel "Not bad, sis."

    return   # Returns to ch1_city menu


# -----------------------------------------------------------------------------
# D1-B: FANRONG DRAGON SQUARE — Dragon Dances
# BG: bg_tianho_fanrong_square
# Dragon dance rehearsal. Dorian encourages nervous performers.
# -----------------------------------------------------------------------------

label ch1_city_fanrong:

    scene bg_tianho_fanrong_square with dissolve  # PLACEHOLDER — Fanrong Dragon Square

    "The square is wide and golden, its center cleared for the dragon dance troupe. Six performers carry an enormous silk dragon — crimson and gold — swirling it through the air in long, sweeping arcs."

    # show performers anxious at center          # PLACEHOLDER — Performers sprite (anxious, fumbling)

    performers "No, no — the turn has to be sharper! The judges from the Empress's court are watching tomorrow and we can't—"

    "One of the younger performers fumbles the footwork, causing the dragon's head to dip awkwardly. The troupe sighs."

    performers "Again. From the beginning."

    "I watch them reset. The head performer's hands are trembling."

    dorian "The footwork on the pivot is off by half a beat. If you drop the inside shoulder on the turn, the silk will follow naturally."

    # show performers surprised at center        # PLACEHOLDER — Performers (looking up, surprised)

    performers "You… you know dragon dancing?"
    dorian "I grew up near the Gale festivals. My mother made me watch every year."

    "The performer stares, then laughs — tension breaking."

    performers "Alright then. Inside shoulder. Let's try it."

    "They try it. The silk dragon sweeps cleanly through the pivot, its head rising exactly as it should. The troupe cheers."

    lucas "YES! It worked, Dad! YOU fixed it!"
    emily "Dad just accidentally became a dragon dance coach."
    daniel "That's actually kind of cool."

    return


# -----------------------------------------------------------------------------
# D1-C: XIANGLI CENTRE — Food Stalls
# BG: bg_tianho_xiangli_stalls
# Family dines. Soldiers interrupt with a perimeter report.
# -----------------------------------------------------------------------------

label ch1_city_xiangli:

    scene bg_tianho_xiangli_stalls with dissolve  # PLACEHOLDER — Xiangli food stalls

    "The food quarter overwhelms every sense at once. Dozens of stalls crowd the narrow lane — skewers of spiced meat, steamed lotus buns, caramelized hawthorn clusters, and soup that smells like a warm memory."

    # show elara delighted at left               # PLACEHOLDER — Elara sprite (face lit up, sniffing the air)
    # show lucas mouth full at center            # PLACEHOLDER — Lucas sprite (cheeks stuffed with food)

    lucas "Mm—mph—this is—mmph—SO GOOD."
    elara "Lucas. Chew first. Then talk."

    # show vendor cheerful at right              # PLACEHOLDER — Vendor sprite

    vendor "First time in Tianho? You must try the five-spice duck and the lotus dumplings — both from a recipe that's older than the city walls."
    dorian "We'll take both."
    vendor "Wise choice, sir. Wise choice!"

    emily "Daniel, you have to try this. It's spicy but like… good spicy."
    daniel "I know what spicy means, Em."
    emily "Just try it!"

    "Daniel tries it. His eyes water slightly. He says nothing."

    daniel "…It's fine."

    "A pair of soldiers weave through the crowd toward us, their expressions businesslike but not alarmed."

    # show gao at right with dissolve            # PLACEHOLDER — Soldier Gao sprite
    # show jiang beside gao                      # PLACEHOLDER — Soldier Jiang sprite

    jiang "Sir Dorian. Apologies for the interruption. Routine perimeter report — all sectors confirmed clear ahead of tomorrow's ceremony. No anomalies."
    dorian "Good. Keep the southern approach double-staffed tonight."
    gao "Already done, sir. Enjoy your evening."

    # hide gao with dissolve                     # Soldiers leave
    # hide jiang with dissolve

    "They disappear back into the crowd. Elara raises an eyebrow."

    elara "…Work follows you even to the dumplings."
    dorian "It always does."

    return


# -----------------------------------------------------------------------------
# D1-D: ZHONG LOTUS PROMENADE — Inventors (locks after first visit)
# BG: bg_tianho_zhong_promenade
# First meeting with Cheng Yuxuan and Roboto.
# -----------------------------------------------------------------------------

label ch1_city_zhong:

    scene bg_tianho_zhong_promenade with dissolve  # PLACEHOLDER — Zhong Lotus Promenade

    "The promenade is quieter than the other districts — wider paths lined with lotus ponds, and stalls that display not food or fabric, but devices. Curious, spinning, clicking, humming devices."

    "A small crowd has gathered around one stall in particular, watching in amazed silence."

    # show yuxuan enthusiastic at center         # PLACEHOLDER — Yuxuan sprite (showman energy)

    yuxuan "—and THAT, my friends, is Cheng Industries' Mk-3 atmospheric purifier! Filters out smoke, pollen, AND the smell of bad decisions! Patent pending!"

    "The crowd applauds. A small wheeled automaton beside him waves a tiny flag."

    # Roboto is a character object — voice comes through as narration with his stutter
    "Roboto: Ch-Ch-Cheng Industries! We bring change!"

    lucas "Dad. Dad, what IS that?"
    dorian "I have absolutely no idea."
    emily "I want one."

    "The inventor spots us — or rather, spots that someone isn't clapping, which seems to offend him profoundly."

    yuxuan "You there! The serious-looking one with the paladin posture and the four children! You're not applauding!"
    dorian "I'm… assessing."
    yuxuan "ASSESSING! I love it! A critical audience!"

    "He bounds over, hand extended."

    yuxuan "Cheng Yuxuan. CEO of Cheng Industries, inventor of forty-seven patented devices, and the man who will one day build a bridge between the stars."
    dorian "Dorian. Paladin."
    yuxuan "A PALADIN! Roboto, log this — our first paladin customer!"

    "Roboto: L-L-Logging! Paladin customer detected. Adjusting sales pitch to: 'sturdy, reliable, and built for combat.'"

    emily "I REALLY want one."
    sarah "What does it do when it rains?"
    yuxuan "Excellent question! It opens an umbrella."

    "He presses a button. A tiny umbrella pops out of Roboto's head. Lucas collapses with laughter."

    return


# =============================================================================
# SECTION 8: LABEL CH1_COMMON_FIREWORKS — City Exploration Convergence
# =============================================================================
# All four city options converge here.
# Scene: the family watches the pre-ceremony fireworks from Deng Blossom Avenue.
# Then cuts to: the castle interior for the Emperor's arrival ceremony.
# =============================================================================

label ch1_common_fireworks:

    # Stop festival ambient — replace with dedicated fireworks SFX
    stop audio fadeout 1.0

    scene bg_tianho_celeb_deng with dissolve    # PLACEHOLDER — Deng Ave packed with celebration crowd

    play sound sfx_fireworks                    # PLACEHOLDER — sfx_fireworks

    "The sky above Tianho erupts in cascading light. Gold. Crimson. Jade. The fireworks bloom over the pagodas, their reflections shimmering on every river canal below."

    # show elara joyful at left with dissolve   # PLACEHOLDER — Elara sprite (head tilted back, lit by fireworks)
    # show lucas awed at center                  # PLACEHOLDER — Lucas (mouth open, eyes wide)
    # show sarah sketching at right              # PLACEHOLDER — Sarah (already drawing)

    "Lucas grabs my sleeve with both hands and refuses to let go."

    lucas "Dad this is the BEST night of my whole entire life."
    elara "I think we can all agree on that one."
    daniel "Don't tell anyone I said this, but… yeah. Pretty amazing."
    emily "I'm telling everyone."
    daniel "Emily."
    emily "I'm telling EVERYONE."

    "I look at my family — all of them lit by gold and fire — and for a moment, the weight of tomorrow lifts completely."

    dorian "Alright. Tomorrow belongs to the empire. But tonight… tonight belonged to us."

    # -------------------------------------------------------------------------
    # CUT TO: Castle Interior — Emperor Min-joon's Arrival Ceremony
    # BG: bg_tianho_castle_interior
    # Music: ost_emperor_arrival (grand, ceremonial)
    # -------------------------------------------------------------------------

    scene bg_tianho_castle_interior with fade   # PLACEHOLDER — Tianho Castle grand hall

    play music ost_emperor_arrival fadein 2.0   # PLACEHOLDER — ost_emperor_arrival

    "The grand hall of Tianho Castle is transformed. Silk banners hang from jade columns, soldiers stand at perfect attention, and dignitaries from across Ena fill the tiered galleries."

    # show olympia regal at center               # PLACEHOLDER — Empress Olympia sprite (throne dais)
    # show long_shen proud at right              # PLACEHOLDER — King Long Shen sprite
    # show cyrus stern at left                   # PLACEHOLDER — Paladin Cyrus sprite
    # show feng composed at left                 # PLACEHOLDER — Paladin Feng sprite

    "Empress Olympia stands at the dais, composed as carved marble."

    # CG: Emperor Min-joon's arrival — full screen illustration
    scene cg_emperor_arrival with dissolve      # PLACEHOLDER — cg_emperor_arrival
    pause 2.0
    scene bg_tianho_castle_interior with dissolve  # Return to castle hall BG

    "And then — he arrives."
    "Emperor Hyon Min-joon of Kyeongjang. The man the world had spent centuries debating the existence of."
    "He is younger than the legends suggested. His posture carries not arrogance, but a quiet, immovable certainty."

    emperor_minjoon "Empress Olympia. King Long Shen. It has been… a long time since Kyeongjang has stood among the nations."
    olympia "Too long, Your Highness. We are glad you have emerged."
    long_shen "Tianho extends its warmest welcome. May this meeting be the first of many."

    # Jump to the auditions decision — happening concurrently nearby
    jump ch1_auditions


# =============================================================================
# SECTION 9: D2 — INTERPRETER AUDITIONS (Static Choice)
# =============================================================================

label ch1_auditions:

    "Near the side corridor, a commotion draws my attention away from the ceremony preparations."

    "Two young men — brothers, clearly, sharing the same dark eyes and careful posture — stand before Paladin Cyrus. They're dressed neatly, holding interpreter credentials."

    cyrus "Hinami nationals. You expect to interpret for the Emperor of Kyeongjang? This is a diplomatic ceremony, not a charity audition."
    niko "We are qualified interpreters, Paladin. Fluent in Kyeongjang, Tianho dialect, and High Enaric. Our credentials are in order."
    cyrus "I don't care about your credentials. I care about who I can trust in that hall."
    kaito "We just want to help. We've trained for this. Please—"
    cyrus "Enough. You're dismissed. Take your brother and go find someone who wants a sideshow."

    "Kaito's shoulders drop. Niko's jaw tightens — he doesn't argue, but his eyes say everything."

    menu:
        "Step in and defend them.":
            $ ch1_audition_choice = "intervene"
            $ niko_affection += 1

            dorian "Paladin Cyrus. Their credentials are in order — I've already reviewed the interpreter list. These two are on it."
            cyrus "Dorian. This isn't your concern."
            dorian "It is when it affects the ceremony. We need the best interpreters in that hall. These are two of them. Stand down."

            "Cyrus holds my gaze for a long moment, then steps aside — not gracefully, but he steps aside."

            niko "…Thank you, Paladin Dorian."
            dorian "Do well in there."

            "Kaito exhales. His hands stop shaking."

        "Say nothing. This isn't your fight.":
            $ ch1_audition_choice = "silent"

            "I watch. I don't move."
            "Cyrus waves a hand and two guards move to escort the brothers out. Kaito stumbles — his eyes are wet."

            "Niko looks back at me as they're led away. His expression is unreadable. But his eyes linger."
            "Cyrus turns, satisfied, and walks back to his post."

            "I look away."

    jump ch1_long_shen

# =============================================================================
# SECTION 10: D3 — LONG SHEN'S ADDRESS (Static Choice)
# =============================================================================

label ch1_long_shen:

    "King Long Shen addresses the assembled paladins and representatives. His voice carries across the hall — measured, warm, carrying the weight of someone who has governed long and survived much."

    long_shen "The nations of Ena have gathered not as rivals, but as family. The first meeting in generations. Let none of us forget what this moment represents — or how fragile it is."

    "Beside me, Feng listens with the focused attention of someone who actually cares."

    "Then Cyrus steps close and speaks under his breath."

    cyrus "Dorian. I need you to review the east wing security rotation. Now, while Long Shen has everyone's attention."

    "Feng side-eyes Cyrus without turning his head."

    menu:
        "Excuse yourself quietly and go with Cyrus.":
            $ ch1_cyrus_choice = "obey"

            dorian "Excuse me."

            "I slip out with Cyrus. Feng watches me go, saying nothing."
            "His expression doesn't change. But something in his posture does — just slightly."

        "Tell him to wait.":
            $ ch1_cyrus_choice = "told_off"
            $ feng_affection += 1

            dorian "Cyrus. Not now."
            cyrus "Excuse me?"
            dorian "The east wing has been staffed since this morning and you know it. Sit down and listen — this is exactly the kind of address you should be paying attention to."

            "Cyrus's face goes red. He opens his mouth. Closes it. Turns and walks stiffly to the back of the room."

            "Feng doesn't look at me, but his shoulders shake once — silent laughter."

            feng "Well played."
            dorian "Don't make it a habit."
            feng "I'd never dream of it."

    jump ch1_elara_chat

# =============================================================================
# SECTION 11: D4 — LATE-NIGHT CHAT WITH ELARA (Repeatable 4 topics)
# =============================================================================
# Back at the hotel room. The children are asleep.
# Dorian and Elara talk — 4 topics available, all repeatable except
# "Talk about Emperor Min-joon" which leads to Common and ends the loop.
# =============================================================================

label ch1_elara_chat:

    scene bg_dorians_room_night with fade
    stop music fadeout 2.0

    "The children are finally asleep. Elara sits on the edge of the bed, her hair loose around her shoulders, watching the city lights drift through the window."

    elara "So. Paladin off-duty. How does it feel?"
    dorian "Strange. Like I've forgotten how."
    elara "You haven't. I can tell. You're almost smiling."

    "She pats the space beside her. I sit."

    elara "Ask me anything. Or tell me. Or just — talk to me the way you used to."

    jump ch1_elara_topic_menu


label ch1_elara_topic_menu:

    menu:

        # TOPIC 1: Cyrus — light banter, no stat effect (repeatable)
        "Talk about Cyrus.":

            dorian "Cyrus is exactly as impossible as the last time you met him."
            elara "He once told me that emotional support was a 'peacetime indulgence.'"
            dorian "That sounds right."
            elara "I told him he needed a hug. He reported me to High Paladin's office."
            dorian "He didn't."
            elara "He did. It was one page long and very formally worded."

            "I laugh. A real one. She looks triumphant."

            jump ch1_elara_topic_menu

        # TOPIC 2: Feng — reveals Feng's family is in Tianho (repeatable)
        "Talk about Feng.":

            dorian "Feng's been quieter than usual tonight."
            elara "Mmm. Did you know his family lives here? In Tianho?"
            dorian "He's never mentioned them."
            elara "He doesn't. But I saw him looking out toward the east quarter when we were in the castle. That's the residential ward."
            elara "I think he misses them. And I think he feels like he's not allowed to."

            "I'm quiet for a moment."

            dorian "I'll make sure he gets time tomorrow. After the ceremony."
            elara "That's why I love you."

            jump ch1_elara_topic_menu

        # TOPIC 3: Empress Olympia — Dorian's political perspective (repeatable)
        "Talk about Empress Olympia.":

            dorian "Olympia held that room with seventeen rulers in it and not one of them doubted she was in charge."
            elara "She has that thing. That quality. What do you call it?"
            dorian "Command presence."
            elara "Command presence. Yes. You have it too, you know."
            dorian "Not like her."
            elara "Different. But real. I've watched you walk into disaster six times and the people around you never stopped trusting you."

            "She squeezes my hand."

            elara "That's its own kind of Olympia."

            jump ch1_elara_topic_menu

        # TOPIC 4: Emperor Min-joon — LEADS TO COMMON, ends the chat loop
        "Talk about Emperor Min-joon.":

            dorian "What did you make of Min-joon?"
            elara "Younger than I expected. Quieter."
            dorian "But not uncertain."
            elara "No. Definitely not uncertain."

            "She shifts, pulling her knees up."

            elara "Dorian… Emily hit her head this evening. At the fireworks. She's fine, before you panic — just a bump. But I wanted to keep the younger ones close tonight."
            elara "So it was just you and me and the lanterns anyway."
            dorian "I'm glad it was."

            "She leans her head against my shoulder."

            elara "Me too."

            jump ch1_elara_chat_common


label ch1_elara_chat_common:

    "The city quiets outside the window. The lanterns drift lower. The festival is ending."

    elara "Tomorrow is going to be extraordinary."
    dorian "Or terrifying."
    elara "Both. Hopefully mostly extraordinary."

    "She kisses my cheek and settles into sleep. I watch the last lanterns float past the window."

    "I close my eyes."

    # -------------------------------------------------------------------------
    # DREAM SEQUENCE — Prosperity Dragon
    # BG: bg_dream_white
    # Music: ost_dream_dragon (soft, celestial)
    # -------------------------------------------------------------------------

    scene bg_dream_white with fade

    play music ost_dream_dragon fadein 3.0

    "A warm light shimmered behind my eyelids."

    prosperity_dragon "Child… something dark stirs in the deep of this city tonight."
    prosperity_dragon "The bones of Tianho remember what happened before. And what will happen again."
    prosperity_dragon "Be ready. Be watchful. The fire in you will be needed soon."

    "I reached toward the voice—"
    "Darkness."

    # -------------------------------------------------------------------------
    # WAKING — Vision of Olympia
    # BG: bg_dorians_room_night
    # -------------------------------------------------------------------------

    scene bg_dorians_room_night with fade

    stop music fadeout 1.0

    play music ost_tension_rising fadein 2.0

    "I woke in a cold sweat."
    "The room was still. Elara breathed softly beside me."
    "And then—"

    scene cg_olympia_vision with shock_cut
    pause 1.0
    scene bg_dorians_room_night with dissolve

    "A vision. Olympia — bloodied, reaching — her mouth forming one word."
    "Danger."

    dorian "The castle."

    "I was dressed and out the door before she finished forming in my mind."

    jump ch1_battle


# =============================================================================
# SECTION 12: CH1_BATTLE — Castle Gate through Taotie (D5–D10)
# =============================================================================
# Six Quick Timed Choices. Three of them (D8, D9, D10) are HARD GATES:
# wrong answer = 'jump game_over'.
#
# QTC NOTE: All menus here are standard 'menu:' blocks for playtesting.
# Replace with the timed-screen call when your QTE UI is built.
# =============================================================================

label ch1_battle:

    # -------------------------------------------------------------------------
    # ARRIVAL AT CASTLE GATE
    # BG: bg_tianho_castle_gate
    # Music: ost_battle_tianho (full combat)
    # -------------------------------------------------------------------------

    scene bg_tianho_castle_gate with shock_cut  # PLACEHOLDER — castle gate, chaos

    play music ost_battle_tianho fadein 1.0     # PLACEHOLDER — battle OST
    play audio amb_castle_battle loop           # PLACEHOLDER — ambient battle sounds

    "The castle gate is already a war zone."
    "Soldiers scatter. Yaoguai pour from the darkness beyond the torchlight — shapes that should not exist, made of shadow and hunger."

    # show gao desperate at left                 # PLACEHOLDER — Gao, fighting
    # show jiang desperate at right              # PLACEHOLDER — Jiang, shielding a soldier

    gao "Sir Dorian! The north gate — it's overrun!"
    jiang "We can't hold them! Sir, we—"

    "A massive yaoguai lunges directly at Gao and Jiang."

    play sound sfx_yaoguai_roar                 # PLACEHOLDER — yaoguai roar SFX

    play sound sfx_heartbeat loop               # Heartbeat SFX — tension

    # =====================================================================
    # D5 — TIMED QTC: Castle Gate (3 options)
    # All three outcomes converge — none is GAME OVER here.
    # =====================================================================

    menu:

        # Option 1: Do nothing — Jiang saves Dorian
        "Do nothing.":
            $ ch1_gate_qtc = "nothing"
            stop sound

            "I freeze — just a half-second too long."
            "Jiang shoves me aside, taking the claw strike on his pauldron instead. The metal crumples. He grunts."

            jiang "Dorian—MOVE!"

            "The yaoguai is disoriented by the impact. We have a second."

        # Option 2: Fiery shield — soldiers escape safely
        "Raise a fiery shield to protect Gao and Jiang.":
            $ ch1_gate_qtc = "shield"
            stop sound

            "I throw my hands out. A disc of draconic fire expands between the yaoguai and the soldiers — not enough to destroy it, but enough to stop it cold."

            play sound sfx_wind_blast           # PLACEHOLDER — fire shield SFX

            "The creature recoils from the heat. Gao grabs Jiang's arm and they dive clear."

            gao "Shield held, sir! We're through!"

        # Option 3: Fireball — yaoguai disoriented, soldiers escape
        "Hurl a fireball at its head.":
            $ ch1_gate_qtc = "fireball"
            stop sound

            "I channel fast — no ceremony — and send a tight bolt of fire straight at its skull."

            play sound sfx_wind_blast           # Reuse for now — PLACEHOLDER

            "The yaoguai staggers, its trajectory broken. Gao and Jiang scramble out of its path."

            jiang "Nice shot, sir!"

    # All three gate options converge here — inside the castle
    # -------------------------------------------------------------------------
    # CUT TO: Castle Interior
    # BG: bg_tianho_castle_interior_battle
    # -------------------------------------------------------------------------

    scene bg_tianho_castle_interior_battle with shock_cut  # PLACEHOLDER — castle interior, mid-battle

    # show vasily fighting at right with dissolve  # PLACEHOLDER — Count Vasily sprite (commanding)

    vasily "Dorian! East wing — two of them in the gallery!"

    # =====================================================================
    # D6 — TIMED QTC: Castle Interior (2 options)
    # Freeze = Vasily saves you (mild criticism)
    # Earth spikes = both yaoguai impaled, Vasily impressed
    # =====================================================================

    play sound sfx_heartbeat loop

    menu:

        # Option 1: Freeze — Vasily intervenes
        "Freeze up.":
            $ ch1_castle_qtc = "freeze"
            stop sound

            "My channeling fails me for a moment — the scale of the battle pressing on my mind."
            "Vasily is already moving. Two precise earth spikes rise from the floor and pin both yaoguai."

            vasily "Shake it off, Dorian. This is not the time for hesitation."

        # Option 2: Earth spikes — Vasily impressed
        "Drive earth-channeling spikes through both yaoguai.":
            $ ch1_castle_qtc = "spikes"
            stop sound

            play sound sfx_stone_spike          # PLACEHOLDER — stone spike SFX

            "I slam both palms to the floor. Two jagged columns of stone erupt simultaneously, impaling both yaoguai through the torso. They don't get back up."

            vasily "Efficient. Very efficient."

    # Converge — head for the stairway

    vasily "Olympia is on the upper floor. We need to reach her. Move!"

    # -------------------------------------------------------------------------
    # CUT TO: Stairway
    # BG: bg_tianho_stairway
    # -------------------------------------------------------------------------

    scene bg_tianho_stairway with dissolve      # PLACEHOLDER — castle stairway

    "We take the stairs at a run. Halfway down, two yaoguai drop from the ceiling above us."

    play sound sfx_heartbeat loop

    # =====================================================================
    # D7 — TIMED QTC: Stairway (wind vs stumble)
    # Channel wind = yaoguai thrown back, safe
    # Stumble = +YUKI TRACKER, Vasily kills one, Dorian counters second
    # =====================================================================

    menu:

        # Option 1: Channel wind — safe
        "Channel wind to throw them back.":
            $ ch1_stair_qtc = "wind"
            stop sound

            play sound sfx_wind_blast           # PLACEHOLDER — wind blast SFX

            "I exhale and push — a concentrated burst of wind. Both yaoguai are hurled backward, crashing into the wall above the stairs."

            vasily "Keep moving."

        # Option 2: Stumble — +yuki_tracker
        "Stumble on the step.":
            $ ch1_stair_qtc = "stumble"
            $ yuki_tracker += 1                # +1 YUKI tracker — unlocks Yuki content later
            stop sound

            "My foot catches. I go down on one knee."
            "Vasily drives his sword through the first yaoguai in the same motion he uses to catch my arm."

            vasily "I have you."

            "I recover fast enough to drive a fire strike through the second one."

            vasily "Next time — watch your footing."

    # Both stair options converge — approaching the Taotie

    "We reach the lower courtyard — and stop dead."

    scene bg_tianho_city_on_fire with shock_cut  # PLACEHOLDER — city on fire, Taotie visible

    "In the burning courtyard below the castle — it is enormous. Ancient. A Taotie."
    "A stone-armoured beast the size of a building, its mouth a furnace of lava, its eyes like twin suns of hunger."

    play music ost_taotie_battle fadein 1.0     # PLACEHOLDER — Taotie battle OST

    taotie_roar "GRRRAAAAAAAGHHH!!!"

    scene cg_taotie_charge with shock_cut       # PLACEHOLDER — cg_taotie_charge
    pause 0.5
    scene bg_tianho_city_on_fire with dissolve  # Return to burning city BG

    vasily "Olympia — she's in its path! We have to draw it away!"

    # show feng arriving at left with dissolve   # PLACEHOLDER — Feng arriving, one eye already damaged
    scene cg_feng_eye_injury with shock_cut     # PLACEHOLDER — cg_feng_eye_injury
    pause 0.4
    scene bg_tianho_city_on_fire with dissolve

    feng "Dorian! My eye — one of the yaoguai — it doesn't matter. The Taotie — it's going to bring down the east wing!"

    play sound sfx_heartbeat loop

    # =====================================================================
    # D8 — TIMED QTC: Taotie — Dodge or Stumble (HARD GATE)
    # Stumble = GAME OVER
    # =====================================================================

    "The Taotie swings its massive head — directly at me."

    menu:

        # ✓ CORRECT: Dodge left
        "Dodge left.":
            stop sound

            "I throw myself sideways. The Taotie's head crashes into the building behind me. Stone explodes. I'm pelted with debris but I'm alive."

            vasily "Move! Get to its flank!"

        # ✗ WRONG: Stumble — GAME OVER
        "Stumble.":
            stop sound

            scene cg_black with shock_cut       # PLACEHOLDER — impact black

            "I don't move fast enough."
            "The stone colossus's arm catches me full force. The world becomes white, then nothing."

            jump game_over                      # ← HARD GATE: GAME OVER

    # D8 correct path continues

    play sound sfx_heartbeat loop

    # =====================================================================
    # D9 — TIMED QTC: Taotie — Shut mouth or Run (HARD GATE)
    # Run toward flank = GAME OVER
    # =====================================================================

    "The Taotie opens its lava-filled maw — a roar that turns the air into a wall of heat."

    menu:

        # ✓ CORRECT: Channel wind to force its mouth shut
        "Channel wind to force its mouth shut.":
            stop sound

            play sound sfx_wind_blast           # PLACEHOLDER

            "I drive a compressed column of wind directly into the Taotie's open mouth. The force slams its jaw shut — the lava blast contained. A crack runs up its stone jaw."

            feng "ITS NECK — aim for the neck!"

        # ✗ WRONG: Run toward flank — GAME OVER
        "Run toward its flank.":
            stop sound

            "I run — but the lava erupts before I reach it. The ground turns to fire beneath my feet."

            scene cg_black with shock_cut

            jump game_over                      # ← HARD GATE: GAME OVER

    # D9 correct path continues

    play sound sfx_taotie_lava              # PLACEHOLDER — lava cracking SFX
    play sound sfx_heartbeat loop

    # =====================================================================
    # D10 — TIMED QTC: Taotie — Seal lava cracks or Run (HARD GATE)
    # Run away = GAME OVER (lava cuts off escape)
    # Seal cracks = battle continues to Olympia rescue
    # =====================================================================

    "The ground cracks beneath the Taotie's weight — lava seeping up through the fissures."

    menu:

        # ✗ WRONG: Try to run — GAME OVER
        "Try to run away.":
            stop sound

            "I turn to run — but the lava cracks spread faster than I can move. The escape route closes in fire."

            scene cg_black with shock_cut

            jump game_over                      # ← HARD GATE: GAME OVER

        # ✓ CORRECT: Seal the cracks with earth channeling
        "Channel earth to seal the lava cracks.":
            stop sound

            play sound sfx_stone_spike          # PLACEHOLDER — earth sealing SFX

            "I drop to one knee and push both palms flat on the ground. Earth flows — thick, fast — pouring into the cracks like clay. The lava is contained."

            feng "THAT'S IT! The stone jaw is weakened — one clean strike!"

    # All three QTCs survived — converge at Olympia rescue

    jump ch1_common_end


# =============================================================================
# SECTION 13: LABEL GAME_OVER — Shared GAME OVER Screen
# =============================================================================
# Jumped to from any failed timed choice in the battle sequence.
# Shows a black screen, a brief narration, and the game's BAD END credits.
# The player must reload from their last save and try again.
# =============================================================================

label game_over:

    # -------------------------------------------------------------------------
    # HOW GAME OVER WORKS:
    # 'jump game_over' redirects here permanently from any failed QTC.
    # 'return' at the end sends execution back to the Ren'Py main menu.
    # There is no "continue from here" — the player must use a save slot.
    #
    # TIP: Encourage players to save before the battle sequence starts.
    # You can add a "(Recommended Save Point)" note before ch1_battle.
    # -------------------------------------------------------------------------

    scene cg_black with fade                    # PLACEHOLDER — black screen

    stop music fadeout 1.0
    stop audio

    pause 1.0

    "The fire went out."
    "And with it — everything."

    pause 1.5

    # show text "GAME OVER" at truecenter with dissolve  # PLACEHOLDER — replace with custom GAME OVER screen
    pause 2.0

    "Reload your last save to try again."

    pause 1.0

    return   # Returns to Ren'Py main menu / game over screen


# =============================================================================
# SECTION 14: LABEL CH1_COMMON_END — Post-Battle Convergence + Chapter End
# =============================================================================
# Reached after all six QTCs are survived.
# The Taotie is defeated. Olympia is rescued, but gravely wounded.
# The winged death god appears. Elara and the children are killed.
# Dorian is sedated by his own soldiers.
# Chapter ends with 'jump chapter_2'.
# =============================================================================

label ch1_common_end:

    # -------------------------------------------------------------------------
    # TAOTIE DEFEAT — Feng loses his eye during the final strike
    # -------------------------------------------------------------------------

    scene bg_tianho_city_on_fire with dissolve  # PLACEHOLDER — burning city

    play music ost_tragedy fadein 3.0           # PLACEHOLDER — grief OST begins

    "Feng brings his blue fire across the cracked jaw — one searing arc."
    "The Taotie's head shatters. The body collapses inward. Stone and magma scatter across the burning courtyard."

    # show feng wounded at left                  # PLACEHOLDER — Feng, eye wound, exhausted

    feng "Olympia—! Someone get to Olympia!"

    vasily "She's here. She's breathing. Barely."

    # show olympia injured at center             # PLACEHOLDER — Olympia, wounded, being supported

    olympia "Dorian… I tried to warn you. I tried to warn all of you. Something is still here. Above the castle. Something—"

    "She couldn't finish."

    "A shadow crossed the moon."

    # CG: the winged death god — enormous, divine, catastrophic
    scene cg_winged_god_appears with shock_cut  # PLACEHOLDER — cg_winged_god_appears
    pause 2.0
    scene bg_tianho_city_on_fire with dissolve

    "Not a yaoguai. Something older. Something that had no name in any language I knew."
    "It spread wings across the entire sky above Castle Tianho."
    "And the castle — stone and jade and silk and centuries — came apart beneath them."

    play sound sfx_explosion                    # PLACEHOLDER — massive explosion SFX

    scene bg_tianho_underground_2 with shock_cut  # PLACEHOLDER — driven underground by the impact

    # -------------------------------------------------------------------------
    # THE CENTRAL TRAUMA — Elara and the children
    # CG: cg_elara_children_death
    # This is the irreversible moment. No choice. No QTC. It simply happens.
    # -------------------------------------------------------------------------

    stop music

    pause 1.0

    "And then — across the burning street — I saw them."

    scene cg_elara_children_death with fade     # PLACEHOLDER — cg_elara_children_death
    pause 3.0
    scene cg_black with fade                    # Hard cut to black after the CG

    pause 2.0

    "There are no words for what I saw."
    "There are no words for what I felt."
    "There was only fire. And then there was only the absence of everything the fire had taken."

    pause 1.5

    "I moved. I don't know how. I moved toward them."

    "And then I heard Vasily's voice — somewhere far away."

    vasily "Hold him. HOLD HIM. Don't let him through."
    gao "Sir Dorian — please — Sir—"

    "They held me. Four soldiers. Then six."

    "A needle. Cold. Fast."

    "And the world went away."

    pause 2.0

    # -------------------------------------------------------------------------
    # END OF CHAPTER 1 — Chapter Title Card + Transition
    # -------------------------------------------------------------------------

    show text "CHAPTER 2" at truecenter with dissolve  # PLACEHOLDER — replace with custom chapter screen
    pause 2.5
    hide text with dissolve

    # 'jump chapter_2' — this label must exist in chapter_02.rpy
    # Create a stub file now to prevent errors:
    #
    #   File: chapter_02.rpy
    #   Contents:
    #       label chapter_2:
    #           "Chapter 2 coming soon."
    #           return
    #

    jump chapter_2   # Defined in chapter_02.rpy


# =============================================================================
# END OF CHAPTER 1
# =============================================================================
