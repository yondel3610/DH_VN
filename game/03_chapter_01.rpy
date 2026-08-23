# The use of ClaudeCode and Deepseek V4 are stricly for formatting and debugging purposes
# AI has been used to make production and documentation faster, not to make the whole thing itself

# =============================================================================
# SECTION 1: CHARACTER DEFINITIONS
# =============================================================================
# compiled character definitions

# =============================================================================
# SECTION 2: IMAGE DECLARATIONS + BACKGROUND/SPRITE
# =============================================================================
# added to 01_bg_cg.rpy | centralized bg images file

# =============================================================================
# SECTION 3: AUDIO DECLARATIONS
# =============================================================================
# All audio used in Chapter 1.
# =============================================================================
# TODO: fix audio

# --- SFX ---
# define audio.sfx_fireworks          # find free fireworks sfx
# define audio.sfx_yaoguai_roar       # monster roar DONE
# define audio.sfx_explosion          # find free explosion audio
# define audio.sfx_stone_spike        # stone spike
# define audio.sfx_wind_blast         # wind blast from other games
# define audio.sfx_heartbeat          # heartbeat audio
# define audio.sfx_taotie_lava        # lava cracking SFX DONE
# define audio.amb_festival_crowd     # festival crowd | to be called again in ch2
# define audio.amb_castle_battle      # get from asian war dramas

# =============================================================================
# SECTION 4: GAME VARIABLES
# =============================================================================

# =============================================================================
# SECTION 5: LABEL CHAPTER_1 — Opening (Dorian's Room)
# =============================================================================

label chapter_1:
    $ save_name = "Chapter 1"
    # -------------------------------------------------------------------------
    # OPENING — Dorian's Room, evening
    # BG: dorians_room
    # Music: ost_tianho_festival (soft intro volume)
    # -------------------------------------------------------------------------
    scene black
    with fade
    pause 0.5
    scene bg_dorians_room with fade # PLACEHOLDER
    # play music ost_tianho_festival volume 0.4 fadein 2.0  # PLACEHOLDER — ost_tianho_festival

    show elara at right_char with Dissolve(0.2)
    voice audio.elara_ch1_line1
    elara "Tianho… Tetrad above… It's even more beautiful than the stories."
    voice audio.elara_ch1_line2
    elara "Dorian, we should take the kids to see the market! Lucas is going to love this!"

    show dorian serious at left_char with Dissolve(0.2)
    "I exhale a slow breath, watching the evening lights bathe the city of Tianho through my binoculars, reflecting off the rivers that weave through its heart like threads of silver."
    "The air smells of spiced tea and roasted chestnuts from the market stalls below, mingling with the faint fragrance of cherry blossoms that line the cobblestone streets."
    "The streets below are bustling with life, lined with towering pagodas adorned in colors of crimson, gold, and jade. Lanterns of every imaginable hue float above the streets, their light glowing softly."

    voice audio.elara_ch1_line3
    elara "Dorian. Are you even listening to me? You've been standing there for a while now."

    show dorian sad at left_char
    "I turn to face her, sighing as I pocket my binoculars. She's leaning against the doorframe, arms crossed, a wry smile playing on her lips."

    
    voice audio.elara_ch1_line4
    elara "You've been standing there long enough to memorize every single detail of the city."
    voice audio.elara_ch1_line5
    elara "Meanwhile, the children are pestering me about seeing the nighttime lantern markets."

    voice audio.elara_ch1_line6
    elara "I would very much like my HUSBAND to take me there as soon as possible before he vanishes to work tomorrow."

    "I sigh, turning back to the view."

    show dorian neutral at left_char
    voice audio.dorian_ch1_line1
    dorian "My heart, you know how important tomorrow is. Everything has to be perfect."

    "She sighs."

    voice audio.elara_ch1_line7
    elara "I know, Dorian. I know how important it is. The entire world will be watching as Kyeongjang's emperor makes his first public appearance in centuries."

    show dorian serious at left_char
    voice audio.dorian_ch1_line2
    dorian "For centuries, Kyeongjang was nothing more than a legend. Many doubted it even existed, and now, their emperor is emerging from the shadows to reconnect."
    voice audio.dorian_ch1_line3
    dorian "This meeting isn't just a reunion—it's a turning point. Alliances will shift. Trade will flourish—or collapse. Power balances will be rewritten."
    voice audio.dorian_ch1_line4
    dorian "And you know Her Majesty. She won't settle for anything less than perfection."

    "Elara steps closer, her soft smile returning. She reaches up and brushes her fingertips against my cheek."

    voice audio.elara_ch1_line8
    elara "And you, sir Dorian. You're part of that perfection, aren't you?"
    voice audio.elara_ch1_line9
    elara "The Dragon of Gale, second only to the High Paladin himself. You'll make sure it all goes smoothly, like you always do."

    show dorian neutral at left_char
    "I manage a faint smile, but the tension in my chest doesn't ease. She notices, of course. She always does."

    voice audio.elara_ch1_line10
    elara "But, my heart. That's tomorrow. Tomorrow is for the world, the king and the empress and the emperor and their grand, history-altering plans. But tonight?"

    "She steps even closer, giving my cheek a kiss."

    voice audio.elara_ch1_line11
    elara "Tonight, you're not the Dragon of Gale. You're not a paladin. You're my husband. And the father of four wonderful, slightly rambunctious children who are dying to explore this incredible city."

    show dorian sad at left_char
    voice audio.dorian_ch1_line5
    dorian "But, my heart…"
    voice audio.elara_ch1_line12
    elara "No excuses, my heart. You've been working tirelessly ever since we left Gale. Tonight is for us. For me. For the kids who adore their father. For a family that rarely gets days like this together."

    show dorian neutral at left_char
    "I sigh, a small smile finally breaking through my resolve. I kiss her."

    voice audio.dorian_ch1_line6
    dorian "Alright, my heart. You win."

    "She returns my kiss, but only briefly as she quickly pulls away. She grabs my hand and pulls me toward the door, her laughter filling the balcony."
    voice audio.elara_ch1_line13
    elara "Come on, Dragon of Gale. The lantern markets won't wait, and neither will the kids!"

    # -------------------------------------------------------------------------
    # CUT TO: Tianho City Night
    # BG: bg_tianho_city_night
    # Music: ost_tianho_festival (full volume — now outside in the festival)
    # -------------------------------------------------------------------------
    scene bg_tianho_city_night with dissolve

    play music ost_tianho_festival volume 0.4
    #play audio amb_festival_crowd loop fadein 1.5  # PLACEHOLDER — crowd ambient loop
    
    "The moment we step out into the street, the kids swarm us, buzzing with excitement."

    show lucas at right_char_kids
    voice audio.lucas_ch1_line1
    lucas "Dad! Dad! Look! Look at all the people! This place is huge!"

    show dorian normal_alt_neutral at left_char
    "Lucas' eyes are open wide as he keeps tugging at the hem of my tunic with both hands."
    "I chuckle, bending down to ruffle his hair."

    voice audio.dorian_ch1_line7
    dorian "Yes, it is. But remember what I said—stay close, okay?"

    "Sarah, as expected, is lost in her own world, flipping through her sketchbook and occasionally glancing up to capture the essence of the city in her drawings."

    hide lucas
    show elara at right_char
    voice audio.elara_ch1_line14
    elara "Sarah… Sarah… Honey. *snaps her fingers* Your father is here."

    hide elara
    show sarah at right_char_kids
    voice audio.sarah_ch1_line1
    sarah "*mumbles* Oh, hey dad!"
    "She glances quickly at me, smiles, then turns back, completely absorbed in her art."
    voice audio.sarah_ch1_line2
    sarah "This place is full of colors. I need to capture the lanterns. But, I don't know what color they should be…"

    "Emily leans over to Daniel and whispers something in his ear, making him roll his eyes but smirk at the same time."

    hide sarah
    show emily at right_char_kids
    emily "Come on, Daniel! You have to at least pretend to be excited!"

    hide emily
    show daniel at right_char_kids
    voice audio.daniel_ch1_line1
    daniel "Hey, I am excited! Just not the way you are."
    voice audio.dorian_ch1_line8
    dorian "Come on, kids. We're going to the market."

    hide dorian
    show elara at left_char
    voice audio.elara_ch1_line15
    elara "But stay close to your father and me. Tianho may be beautiful, but—"

    hide daniel
    show emily at right_char_kids
    emily "You never know what lurks beneath the hearts of strangers and how we kids are gullible and—"
    hide emily
    show daniel at right_char_kids
    voice audio.daniel_ch1_line2
    daniel "We know that, mom! Stranger Danger a thousand times. Can we just hurry up? I wanna see some dragons."

    hide daniel
    show sarah at right_char_kids
    voice audio.sarah_ch1_line3
    sarah "Mom, we need to see the dragons!"

    "Elara sighs and kisses Sarah on her forehead."

    voice audio.elara_ch1_line16
    elara "Alright, alright. Let's go see them. But remember, no pretending to be dragons."

    hide sarah
    voice audio.sarah_ch1_line4
    "Yes, mom. (in unison)"

    "With that, the children take off ahead of us, their chatter and laughter blending into the sounds of the city."
    "Elara walks beside me and I hold her hand."

    show elara at right_char with Dissolve(0.2)
    voice audio.elara_ch1_line17
    elara "So, where should we go first?"

    show dorian normal at left_char with Dissolve(0.2)
    "I look around, taking in the scenery of the market."
    voice audio.dorian_ch1_line9
    dorian "Well, all of the kids seem intent on finding dragons, and you say that you want to eat at the stalls. I say we follow the flow of the crowd and see where it takes us."

    "Elara nods, her eyes sparkling with the same excitement I see in the children."

    voice audio.elara_ch1_line18
    elara "Sounds like a plan. But don't think you're getting off easy, Dragon of Gale. You're carrying the bags."

    voice audio.dorian_ch1_line10
    dorian "Of course, I am."

    "As we move deeper into the marketplace, the city seems to come alive around us. Elara looks at me, her hand still in mine, while the kids fidget and bounce with anticipation."
    "We can go to the Deng Blossom Avenue, where the lanterns for tomorrow are being prepared. There is also the Fanrong Dragon Square, where the rehearsals for tomorrow's Dragon Dances are being held."
    "I can also bring them to the Xiangli Centre, where the food stalls are. Or maybe I can lead them straight to the Zhong Lotus Promenade, where inventors are showcasing their inventions for a chance to speak to the Kyeongjang Emperor himself."
    "Either way, we're still going to the Zhong Lotus Promenade. Maybe I can take them to the other places first."

    "I glance at Elara, who's watching the children with an amused smile as they eagerly debate where to go first. She meets my eyes and tilts her head slightly."

    voice audio.elara_ch1_line19
    elara "Well, my heart, you're the Father. What'll it be? The kids can't wait."
    hide elara
    show lucas at right_char_kids with Dissolve(0.2)
    voice audio.lucas_ch1_line2
    lucas "Hurry up, dad!"

    jump ch1_city


# =============================================================================
# SECTION 6: LABEL CH1_CITY — Repeatable City Menu (Static Choices)
# =============================================================================
default city_visited_deng    = False
default city_visited_fanrong = False
default city_visited_xiangli = False
default city_visited_zhong   = False

label ch1_city:
    menu:
        "Deng Blossom Avenue — Lanterns." if not city_visited_deng:
            $ city_visited_deng = True
            call ch1_city_deng from _call_ch1_city_deng
            jump ch1_city

        "Fanrong Dragon Square — Dragon Dances." if not city_visited_fanrong:
            $ city_visited_fanrong = True
            call ch1_city_fanrong from _call_ch1_city_fanrong
            jump ch1_city

        "Xiangli Centre — Food Stalls."if not city_visited_xiangli:
            $ city_visited_xiangli = True
            call ch1_city_xiangli from _call_ch1_city_xiangli
            jump ch1_city

        "Zhong Lotus Promenade — Inventors." if not city_visited_zhong:
            $ city_visited_zhong = True
            call ch1_city_zhong from _call_ch1_city_zhong

# =============================================================================
# SECTION 7: CITY SUB-SCENES
# Each is a 'label' called from ch1_city. They end with 'return'
# which sends execution back to the 'call' line in ch1_city.
# =============================================================================

# -----------------------------------------------------------------------------
# D1-A: DENG BLOSSOM AVENUE — Lanterns
# BG: bg_tianho_deng_blossom
# -----------------------------------------------------------------------------

label ch1_city_deng:

    scene bg_tianho_deng_blossom with dissolve  # PLACEHOLDER — Deng Blossom Avenue
    show fireflies
    "We turn toward Deng Blossom Avenue, a decision met with a satisfied hum from Sarah and nods of approval from the others."
    "The moment we step onto the avenue, lanterns — hundreds, perhaps thousands of them — float effortlessly in the air, their glow soft and ethereal."
    "They seem alive, swaying gently as though in sync with the faint breeze that carries the sweet scent of lotus blossoms and jasmine."

    show daniel at right_char_kids with Dissolve(0.2)
    voice audio.daniel_ch1_line3
    daniel "Look! They're moving!"
    hide daniel

    show lucas at right_char_kids
    voice audio.lucas_ch1_line3
    lucas  "Are they alive? How are they doing that?"
    hide lucas

    show elara at right_char
    voice audio.elara_ch1_line20
    elara "It's breathtaking."
    show dorian smile at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line11
    dorian "It is, my heart."
    show dorian neutral at left_char

    "Sarah, predictably, has already flipped open her sketchbook, her pencil moving furiously as she tries to capture the scene."

    hide elara
    show sarah at right_char_kids
    voice audio.sarah_ch1_line5
    sarah "Oh gosh! This is so beautiful! The colors… I need to get the colors just right!"
    voice audio.sarah_ch1_line6
    sarah "But how do I even start? The reds aren't just red—they're ruby, garnet, scarlet—oh, this is impossible!"

    show dorian normal_alt_neutral at left_char
    voice audio.dorian_ch1_line12
    dorian "Take your time, Sarah. The lanterns aren't going anywhere."

    hide sarah
    show lucas at right_char_kids
    "Lucas points to a massive lantern shaped like a koi fish."

    voice audio.lucas_ch1_line4
    lucas "Dad look! That lantern's huge!"

    "He darts forward to get a better look. I quickly grab his hand."

    voice audio.dorian_ch1_line13
    dorian "Careful, Lucas. Stay close."
    hide lucas
    show daniel at right_char_kids
    voice audio.daniel_ch1_line4
    daniel "How do they even make those?"
    show dorian normal at left_char
    voice audio.dorian_ch1_line14
    dorian "With bamboo and silk, Daniel."

    # show lead_fire_channeler at center

    "Lead Fire Channeler: Alright, that's enough! Bring them back, fire channelers!" #TODO: fix fire channeler sprites

    "A group of figures in crimson robes steps into view at the far end of the avenue, their hands raised in precise, fluid motions. Flames flicker in their palms."
    "One by one, the lanterns return to the fire channelers, floating gently into their hands like obedient birds."

    hide daniel
    show emily at right_char_kids
    emily "Dad! They're making them come back!"

    "Emily tugs at my sleeve, her excitement bubbling over."

    emily "Dad, you're a fire channeler right? Can you make the lanterns move like that?"

    voice audio.dorian_ch1_line15
    dorian "Of course, Emily."
    hide emily
    show daniel at right_char_kids
    voice audio.daniel_ch1_line5
    daniel "That's a stupid question, Emily! Dad's the strongest!"
    hide daniel
    show elara at right_char
    voice audio.elara_ch1_line21
    elara "Shh! Daniel, watch your words or you'll be heading back to our room at the inn!"

    "All of us watch intently as the last lantern disappears into the robes of the fire channelers."
    "The lead fire channeler finally addresses the crowd."

    "Lead Fire Channeler: This is just a rehearsal. Tomorrow, we'll perform before the Emperor of Kyeongjang himself. We better bring our A game." #TODO: fix fire channeler sprites
    "Channelers: Sir!" # TODO: fix fire channeler sprites

    "Sarah closes her sketchbook and walks toward Lucas."

    hide elara
    hide dorian
    show sarah at right_char_kids with Dissolve(0.2)
    voice audio.sarah_ch1_line7
    sarah "I'm done!"
    # hide sarah
    show daniel at left_char_kids with Dissolve(0.2)
    voice audio.daniel_ch1_line6
    daniel "Really? Lemme see!"
    voice audio.sarah_ch1_line8
    sarah "Later, Daniel! I'll show it once I place some finishing touches! *giggles*"
    voice audio.daniel_ch1_line7 
    hide daniel
    hide sarah
    show lucas at right_char_kids with Dissolve(0.2)
    voice audio.lucas_ch1_line5
    lucas "Let's go somewhere else, Dad!"

    return

# -----------------------------------------------------------------------------
# D1-B: FANRONG DRAGON SQUARE — Dragon Dances
# BG: bg_tianho_fanrong_square
# -----------------------------------------------------------------------------

label ch1_city_fanrong:
    scene cg_dorian_w_kids with fade
    "I decided that we go to Fanrong Dragon Square to watch the Dragon dance rehearsals."
    "As we arrive, we find that the square is alive with rhythm and energy, the pounding of drums and clanging of cymbals echoing off the towering pagodas."
    "Brightly colored dragons — red, gold, and violet — twist and coil through the crowd, their movements fluid yet deliberate, each step in perfect harmony with the beat of the music."
    scene bg_tianho_fanrong_square with dissolve  # PLACEHOLDER — Fanrong Dragon Square
    show lucas at right_char_kids
    voice lucas_ch1_line6
    lucas "Look at them, Dad! It's a real dragon!"

    hide lucas
    show sarah at right_char_kids
    voice audio.sarah_ch1_line9
    sarah "Mom! Dad! It's the Prosperity Dragon!"

    show dorian serious at left_char
    "I glance at the gilded dragon costume, its shimmering scales catching the lantern light with every fluid motion."
    voice audio.dorian_ch1_line16
    dorian "Yeah… The Prosperity Dragon…"

    hide dorian
    hide sarah
    show lucas at right_char_kids
    "Lucas can't contain himself. His arms flail as he mimics the twisting, serpentine motions of the dragon dancers, his tiny legs stomping a rhythm of their own on the cobblestone square."
    show sarah at left_char_kids
    "Sarah joins in, her movements more graceful, while Daniel smirks and crosses his arms, clearly too cool to dance but not immune to the energy."

    hide sarah
    hide lucas
    show dorian neutral at left_char
    voice audio.dorian_ch1_line17
    dorian "Careful, kids. You'll wear yourselves out before we even explore the rest of the city."
    show daniel at right_char_kids
    voice audio.daniel_ch1_line8
    daniel "I never get tired, Dad."
    hide daniel
    show emily at right_char_kids
    emily "Daniel, please…"
    hide emily

    "As we step closer to the rehearsal, I notice some of the dragon dancers stealing glances in our direction. Whispers ripple through their group, and I catch snippets of their murmurs."


    performers "It's him… The Dragon of Gale…"
    performers "Is he watching us? Oh no, my steps are all wrong!"
    performers "Do you think he'll criticize us?"
    performers "C-Calm down, you guys. He might report us to the Empress!"

    "One of the performers, a young man holding the golden dragon's head, stumbles slightly, his confidence clearly shaken. He regains his footing quickly, but his face is flushed with embarrassment."
    "I sigh softly and step forward, raising a hand in greeting."

    show dorian smile at left_char
    voice audio.dorian_ch1_line18
    dorian "You're doing well. Keep your movements calm and deliberate. The Prosperity Dragon commands respect, not chaos."

    "The young man straightens immediately, nodding with wide eyes."

    show dorian neutral at left_char
    performers "Th-thank you, sir. We're… we're just nervous, you see. Tomorrow's performance is for the Emperor of Kyeongjang, the King of Tianho, and, of course, Empress Olympia."
    performers "We're just very nervous… Our dance, we just want it to be perfect."

    voice audio.dorian_ch1_line19
    dorian "You'll be fine. Focus on your training, not the audience."
    "Channelers: Sir!"

    show lucas at right_char_kids
    voice audio.lucas_ch1_line7
    lucas "Can I try to be a dragon, Dad? Please? I want to be a dragon too!"

    "Lucas runs to Daniel, making sweeping motions with his hands."

    voice audio.lucas_ch1_line8
    lucas "Look at me! I'm the Dragon of Gale! Rwarrr!!"
    hide lucas
    "Emily mimics the performers too, her hands weaving imaginary dragon movements in the air. Daniel crosses his arms as he studies the drummers."
    show emily at right_char_kids
    emily "Roaaarr!!! Look, Dad! I can do it too!"
    hide emily
    show daniel at right_char_kids

    voice audio.daniel_ch1_line9
    daniel "I could totally play the drums better than that guy."
    hide daniel
    show elara at right_char
    "Elara says gently, placing a hand on my arm."

    voice audio.elara_ch1_line22
    elara "Kids, calm down. My heart, maybe we should move on before they start asking to join the rehearsal."
    voice audio.dorian_ch1_line20
    dorian "Alright, let's head somewhere else."

    "As we turn to leave, one of the young performers in the dragon costume calls out."
    hide elara

    performers "Thank you for your encouragement. We'll make sure tomorrow's performance is flawless!"
    show dorian normal_alt_neutral at left_char
    voice audio.dorian_ch1_line21
    dorian "I'm sure you will."

    show elara at right_char
    "As we walk away, Elara links her arm through mine."

    voice audio.elara_ch1_line23
    elara "That was nice of you, you know. Giving them a little confidence boost."
    show dorian normal at left_char
    voice audio.dorian_ch1_line22
    dorian "It's the least I could do."

    return

# -----------------------------------------------------------------------------
# D1-C: XIANGLI CENTRE — Food Stalls
# BG: bg_tianho_xiangli_stalls
# REWRITTEN from PDF p13-15: Three specific Tianho foods (FOOD1/2/3), vendor
# refuses payment, Tianho soldiers interrupt (not Gao/Jiang), Daniel salutes.
# -----------------------------------------------------------------------------

label ch1_city_xiangli:

    scene cg_dorian_w_kids with fade
    "I decided to take the family out for dinner at the stalls at Xiangli Centre."
    "My family surges ahead, the kids' excitement pulling me along like a tide. Lanterns strung overhead illuminate the bustling food stalls, casting everything in a warm, golden glow."
    scene bg_tianho_xiangli_stalls with dissolve  # PLACEHOLDER — Xiangli food stalls
    show elara at right_char with Dissolve(0.2)
    voice audio.elara_ch1_line24
    elara "Come on, Dorian. Even you can't resist this."
    hide elara
    show lucas at right_char_kids with Dissolve(0.2)
    "Lucas is already at the first stall, pressing his face as close as he can without falling into the sizzling grill."

    voice audio.lucas_ch1_line9
    lucas "Dad! They've got... uh... what are these?"
    show dorian normal at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line23
    dorian "Those are Tianho's famous 'Spring Bite Skewers.' Roasted jiān yán chūn shì, Lucas."
    hide lucas
    # [COMMENT: FOOD1 — Spring Bite Skewers: bite-sized glazed meat with charred fruit slices and crispy greens]
    # food illus at food_pos with dissolve
    "The vendor lifts a skewer of the food. Each skewer has bite-sized pieces of meat glazed in a tangy-sweet sauce, interspersed with charred fruit slices and crispy greens. Lucas' mouth hangs open as he stares at it."

    vendor "Tianho's finest! Would you like to have some?"
    hide dorian
    # hide food1 here

    show lucas at left_char_kids with Dissolve(0.2)
    voice audio.lucas_ch1_line10
    lucas "Yes please! Yes please!"
    hide lucas
    show emily at left_char_kids with Dissolve(0.2)
    emily "I want some! I want some!"
    hide emily
    show daniel at left_char_kids with Dissolve(0.2)
    voice audio.daniel_ch1_line10
    daniel "Hey! I'm older than you, Lucas! I should have one before you!"
    hide daniel
    "Sarah closes her sketchbook and quickly grabs a seat."
    show sarah at left_char_kids with Dissolve(0.2)
    voice audio.sarah_ch1_line10
    sarah "I suppose having one won't hurt me."
    hide sarah

    show elara at left_char with Dissolve(0.2)
    voice audio.elara_ch1_line25
    elara "I'll be getting seconds hehe. You know me, my heart."
    hide elara
    show dorian normal_alt_neutral at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line24
    dorian "We'll get ten."

    "I nod to the vendor as I hand him a few coins. The vendor freezes, his eyes widening."

    vendor "Merciful Tetrad! P-Paladin Dorian! I apologize."

    "He stammers, nearly dropping the skewer in his hand."

    vendor "P-Please, my lord, I couldn't possibly charge you. The food is yours—no payment needed!"
    show dorian neutral at left_char
    voice audio.dorian_ch1_line25
    dorian "*sighs* Just take it. Please."

    "There's a brief pause before the vendor relents, nodding gratefully and motioning for us to sit."

    vendor "As you wish, Paladin. Please, take a seat. I'll serve your family the best this night has to offer."

    "Lucas snatches his skewer, taking a big bite and promptly burning his tongue."
    show lucas at right_char_kids with Dissolve(0.2)
    voice audio.lucas_ch1_line11
    lucas "Ow! Ow! It's hot! Hot hot hot!"
    hide lucas
    show elara at right_char with Dissolve(0.2)
    voice audio.elara_ch1_line26
    elara "Lucas. It's the fifth time this month you burnt your tongue!"
    hide elara
    show emily at right_char_kids with Dissolve(0.2)
    emily "Haha! Lucas burnt his tongue again!"
    hide emily
    show sarah at right_char_kids with Dissolve(0.2)
    voice audio.sarah_ch1_line11
    sarah "Emily, you're one to talk! You kept burning your tongue last year!"
    hide sarah
    # [FOOD2 — Dragon Heart Soup (lóng xīn tāng): deep red spicy broth, dragon scale dumplings]
    "The vendor gives us steaming bowls of lóng xīn tāng — 'Dragon Heart Soup.' The broth is deep red, spicy and rich, with delicate dumplings shaped like dragon scales floating on top."

    voice audio.dorian_ch1_line26
    dorian "This one's delicious. Lóng xīn tang. You're going to love it."

    show daniel at right_char_kids with Dissolve(0.2)
    "Daniel grabs a bowl immediately, his cheeks flushing pink as the heat hits his tongue."

    voice audio.daniel_ch1_line11
    daniel "This is so spicy! Mom, try it!"

    "He shoves the bowl toward Elara, who takes a dainty sip."
    hide daniel
    show elara at right_char with Dissolve(0.2)
    voice audio.elara_ch1_line27
    elara "Wow, that has a kick."

    # [COMMENT: FOOD3 — Bamboo Crystal Cakes (zhū yè píng gāo): translucent jelly squares with fruit]
    "Meanwhile, Sarah picks at a plate of zhū yè píng gāo — 'Bamboo Crystal Cakes.' The translucent, jelly-like squares shimmer under the lantern light, filled with bursts of fruit and a faintly sweet flavor."
    "She sketches the cakes in her notebook before taking a single, careful bite."
    hide elara

    show sarah at right_char_kids with Dissolve(0.2)
    voice audio.sarah_ch1_line12
    sarah "Oh my! It's like eating a jewel!"
    show dorian normal at left_char
    "Just as I'm starting to enjoy myself, a voice breaks through the din of the market."
    hide sarah
    show dorian serious at left_char
    show male_soldier_1 at right_char with Dissolve(0.2)
    male_soldier_1 "Paladin Dorian!"
    "I turn to see three soldiers in Tianho's imperial armor weaving through the crowd. They salute sharply as they reach me."

    show dorian normal_alt_annoyed at left_char
    male_soldier_1 "Paladin! Apologies for the interruption."

    hide male_soldier_1
    show lucas at right_char_kids with Dissolve(0.2)
    voice audio.lucas_ch1_line12
    lucas  "Cool! A soldier! Hello—"
    hide lucas
    show elara at right_char with Dissolve(0.2)
    voice audio.elara_ch1_line28
    elara  "Not now, sweetie. Finish your skewer."
    hide elara
    show male_soldier_1 at right_char with Dissolve(0.2)
    show dorian normal_alt_calm at left_char
    voice audio.dorian_ch1_line27
    dorian "At ease, soldiers. What is it?"
    show dorian normal_alt_annoyed at left_char

    "The second soldier steps forward, holding a folded parchment."
    hide male_soldier_1
    show male_soldier_2 at right_char with Dissolve(0.2)
    male_soldier_2 "The perimeter reports for the event tomorrow, sir. We wanted to ensure you were informed."

    "The third soldier, younger and clearly nervous, clears his throat."
    hide male_soldier_2
    show soldier_gao at right_char with Dissolve(0.2)
    voice audio.gao_ch1_line1
    gao "Paladin, we were hoping you might join us for a quick assessment. Your presence would be... reassuring."

    "I feel Elara's eyes on me, and when I glance her way, she's arching a single eyebrow."

    show dorian serious at left_char
    voice audio.dorian_ch1_line28
    dorian "Can it wait until morning?"

    "The first soldier hesitates, then nods."
    hide soldier_gao
    show male_soldier_1 at right_char
    male_soldier_1 "Of course, sir. We didn't mean to disrupt your evening."
    voice audio.dorian_ch1_line29
    dorian "Good. Keep me updated."
    show dorian
    "The soldiers bow slightly before disappearing back into the crowd. I turn back to my family, only to find Daniel mimicking the soldiers. He salutes dramatically, puffing out his chest."
    hide male_soldier_1

    show daniel at right_char_kids with Dissolve(0.2)
    voice audio.daniel_ch1_line12
    daniel "Paladin Dorian, sir!"
    show dorian neutral at left_char
    hide daniel
    show elara at right_char with Dissolve(0.2)
    voice audio.elara_ch1_line29
    elara  "Oh, Daniel. You'll make a fine soldier one day."
    show dorian normal at left_char
    voice audio.dorian_ch1_line30
    dorian "Alright. Let's continue exploring."

    return

# -----------------------------------------------------------------------------
# D1-D: ZHONG LOTUS PROMENADE — Inventors (locks after first visit)
# BG: bg_tianho_zhong_promenade
# Crowd mocks Yuxuan. Dorian and Elara disagree about his potential.
# -----------------------------------------------------------------------------

label ch1_city_zhong:

    scene bg_tianho_zhong_promenade with dissolve

    "We stroll down Zhong Lotus Promenade, where the air hums with the clinking of metal, the hiss of steam, and the occasional outburst of an overly enthusiastic inventor."
    "Sarah slows down, sketchbook in hand, capturing the finer details of the pagodas surrounding the promenade. Meanwhile, Lucas is giggling at a toy soldier marching in uneven, jerky steps."
    "As we walk further, Daniel suddenly stops, eyes lighting up as he points to a large wooden sign adorned with intricate calligraphy:"
    "'EXHIBIT OF FUTURE INNOVATIONS - INSPIRED BY THE KYEONGJANG EMPIRE!'"
    show daniel at right_char_kids with Dissolve(0.2)
    voice audio.daniel_ch1_line13
    daniel "The Empire of Kyeongjang?"

    show dorian neutral at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line31
    dorian "Yeah, I forgot to mention. They're doing an exhibit inspired by mythical advanced technology of the Hidden Empire of Kyeongjang."

    "It's an opportunity for local inventors to showcase their creations, with the winner receiving the honor of speaking directly to the Emperor of Kyeongjang during tomorrow's historic meeting."
    "The thought alone makes me pause — Kyeongjang, the most advanced civilization this world has seen in 400 years, reconnecting with us at last."

    voice audio.dorian_ch1_line32
    dorian "They're longing for a chance to showcase their technological advancement to the Emperor."
    voice audio.daniel_ch1_line14
    daniel "Tetrad above! We have to see it, dad! Think of all the science we can see!"
    hide daniel
    show sarah at right_char_kids with Dissolve(0.2)
    voice audio.sarah_ch1_line13
    sarah  "Hey! I thought you hated science!"
    hide sarah
    show lucas at right_char_kids with Dissolve(0.2)
    voice audio.lucas_ch1_line13
    lucas  "Yeah! Remember the time you called me a dork for picking up a science book?"
    hide lucas
    show daniel at right_char_kids with Dissolve(0.2)
    voice audio.daniel_ch1_line15
    daniel "I, um… Well…"
    hide daniel
    show elara at right_char with Dissolve(0.2)
    voice audio.elara_ch1_line30
    elara  "All right, kids. Settle down. Let's just look at the exhibits."
    hide dorian
    hide elara
    "The exhibit area is packed with people. At the center is a small stage, where a young man with wild, unkempt hair and smudges of soot on his face is gesturing grandly to the crowd. His robes are slightly singed, and his eyebags were… apparent."

    show yuxuan normal_happy at center_char with Dissolve(0.2)
    voice audio.yuxuan_ch1_line1
    yuxuan "Ladies and gentlemen! My name is Cheng Yuxuan, an aspiring visionary inventor! Thank you for coming to my humble exhibit!"

    "With a dramatic flourish, he pulls a sad piece of red fabric off a large, boxy contraption."
    show yuxuan normal_sad at center_char
    "It's... well, it's a square metal box with arms made of mismatched pipes and legs that are little more than broomsticks. Its 'head' is an old television screen, flickering with static."
    "The kids are trying hard to stifle a laugh."
    hide yuxuan with Dissolve(0.15)
    # show roboto happy at right_robot with moveinright

    show emily at left_char_kids with Dissolve(0.2)
    emily "Pftt… W-What's that?"
    hide emily
    show lucas at left_char_kids with Dissolve(0.2)
    voice audio.lucas_ch1_line14
    lucas "Dad… I thought you said the exhibit was filled with inventors…"
    hide lucas
    show yuxuan normal_neutral at center_char with Dissolve(0.2)
    "Yuxuan presses a large red button on the side of the contraption. The television screen blinks to life, displaying a faint grainy smile."
    # hide yuxuan
    show yuxuan normal_happy at center_char
    # with Dissolve(0.2)
    voice audio.yuxuan_ch1_line2
    yuxuan "I present to you the marvel of modern ingenuity, the pinnacle of technological advancement… ROBOTO!"
    hide yuxuan
    show roboto happy at center_robot
    voice audio.roboto_ch1_line1
    roboto "H-H-Hello. My name is R-Roboto— I-I-I-…."
    show roboto happy at right_robot with moveinright

    show lucas at left_char_kids with Dissolve(0.2)
    voice audio.lucas_ch1_line15
    lucas "It talks like it's choking!"
    hide lucas
    show yuxuan normal_neutral at left_char with Dissolve(0.2)
    voice audio.yuxuan_ch1_line3
    yuxuan "Roboto will revolutionize your life! It can assist with daily chores, answer your questions, and even tell jokes! Observe!"

    "He flips a switch, and Roboto's screen flashes with a bright light."
    hide yuxuan
    voice audio.roboto_ch1_line2
    roboto "W-w-w-why did the chicken from Tianho c-c-crossed the road?"
    show man_1 at left_char with Dissolve(0.2)
    man_1  "Oh I love these types of jokes! Why?"
    voice audio.roboto_ch1_line3
    roboto "*weird robotic noises* I-I-I-I— Error… Error… T-T-T-…"
    # roboto error sprite
    hide man_1

    "Daniel couldn't help but snort. He whispers to Sarah."

    show daniel at left_char_kids with Dissolve(0.2)
    voice audio.daniel_ch1_line16
    daniel "Maybe it's speaking in Kyeongjangese?"
    hide daniel
    show sarah at left_char_kids with Dissolve(0.2)
    voice audio.sarah_ch1_line14
    sarah  "Pfttt… Hahaha!"
    hide sarah

    show yuxuan normal_neutral at left_char with Dissolve(0.2)
    "Yuxuan, undeterred, holds up a hand for silence."

    show yuxuan normal_lying at left_char with Dissolve(0.2)
    voice audio.yuxuan_ch1_line4
    yuxuan "This is merely a minor adjustment issue! Roboto is fully capable of... of… uh…"

    show roboto malfunction at right_robot
    "He presses another button, and Roboto's screen suddenly flashes a random image of a fish before its voice returns."
    hide yuxuan
    show man_1 at left_char with Dissolve(0.2)
    man_1  "A fish? What gives?!"
    voice audio.roboto_ch1_line4
    roboto "T-To get to the o-o-other s-s-s-s-s…. ERROR… ERROR… sideeee…. S-s-s-s-s— *glitches*"
    hide man_1
    show woman_1 at left_char with Dissolve(0.2)
    woman_1 "W-What's happening?"
    hide woman_1
    show man_2 at left_char with Dissolve(0.2)
    man_2  "Look out! It's gonna explode!"
    hide man_2

    "Roboto begins to shake violently, its screen flashing with bright, chaotic patterns. The arms jerk wildly, one of them flinging off and landing with a loud clank near Lucas' feet."
    show roboto error at right_robot
    "The legs collapse, and the entire contraption falls over with a resounding thud. A puff of smoke rises from its side."
    show yuxuan normal_sad at left_char with Dissolve(0.2)
    show roboto malfunction at right_robot
    voice audio.yuxuan_ch1_line5
    yuxuan "I uh… um… well—"
    show roboto error at right_robot
    voice audio.roboto_ch1_line5
    roboto "BeboOoOot… Bebooot! Bebottt! *electric static*"
    show roboto malfunction at right_robot
    "The crowd erupts in laughter. Lucas is doubled over, tears streaming down his face. Even Daniel can't hold back a chuckle, and Emily is covering her mouth, her shoulders shaking."
    show roboto error at right_robot
    hide yuxuan
    show daniel at left_char_kids with Dissolve(0.2)
    voice audio.daniel_ch1_line17
    daniel "I… I think it's dead."
    hide daniel
    show emily at left_char_kids with Dissolve(0.2)
    emily  "More like it never lived! Hahahaha!"
    hide emily
    show sarah at left_char_kids with Dissolve(0.2)
    "Sarah, ever the artist, sketches the fallen Roboto in her book with exaggerated arms and legs."
    voice audio.sarah_ch1_line15
    sarah "Very interesting…"
    hide sarah
    show man_1 at left_char with Dissolve(0.2)
    man_1  "Aww brother this guy stinks!"
    hide man_1
    show woman_1 at left_char with Dissolve(0.2)
    woman_1 "Come on! We came here for nothing?"
    hide woman_1
    show man_2 at left_char with Dissolve(0.2)
    man_2  "Tianho will look bad if this man was given a chance to talk to the Kyeongjang Emperor!"
    hide man_2

    show yuxuan normal_sad at left_char with Dissolve(0.2)
    voice audio.yuxuan_ch1_line6
    yuxuan "Umm… A minor setback! I'll have Roboto up and running by tomorrow! You'll see!"
    hide yuxuan
    hide roboto
    show dorian normal_alt_neutral at left_char with Dissolve(0.2)
    "I let out a quiet chuckle, shaking my head."
    voice audio.dorian_ch1_line33
    dorian "Well, he's certainly memorable. I'll give him that. But no way he'll win an audience with the Emperor of Kyeongjang."
    show dorian normal at left_char # with Dissolve(0.2)

    show elara at right_char with Dissolve(0.2)
    "Elara's sharp elbow finds its way to my ribs."

    voice audio.elara_ch1_line31
    elara  "Dorian! That's so mean! What if he actually succeeds one day?"

    "I glance at her, raising a brow. I point to the detached arms near Lucas' feet."

    voice audio.dorian_ch1_line34
    dorian "My heart, do you actually think that this is deserving of the Emperor's presence?"
    voice audio.elara_ch1_line32
    elara  "Well, I—"
    show dorian normal_alt_neutral at left_char
    voice audio.dorian_ch1_line35
    dorian "The Emperor of Kyeongjang would only entertain the most brilliant minds. That's why we made this exhibit."
    voice audio.elara_ch1_line33
    elara  "Hmph. You really shouldn't underestimate people like him, Dorian. Ambition can surprise you."
    voice audio.dorian_ch1_line36
    dorian "You're not wrong, but sometimes ambition needs a little… refinement."
    voice audio.elara_ch1_line34
    elara  "And sometimes, it just needs a little time."
    hide dorian

    # hide elara
    show sarah at left_char_kids with Dissolve(0.2)
    voice audio.sarah_ch1_line16
    sarah  "I kinda feel bad for him."
    show elara at right_char with Dissolve(0.2)
    voice audio.elara_ch1_line35
    elara  "Me too, sweetie."
    hide sarah
    show emily at left_char_kids with Dissolve(0.2)
    emily  "Hey Sarah. Maybe you should draw a better version of Roboto for him. He clearly needs help."
    hide emily
    voice audio.elara_ch1_line36
    elara  "Emily. Be nice."
    show lucas at left_char_kids with Dissolve(0.2)
    voice audio.lucas_ch1_line16
    lucas  "Dad, can we come  back tomorrow? I want to see it break down again!"
    hide lucas

    show dorian normal at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line37
    dorian "Be nice, Lucas."

    "I shake my head, a small smile tugging at my lips. Elara links her arm with mine."
    show dorian normal_alt_neutral at left_char
    voice audio.dorian_ch1_line38
    dorian "Alright, my heart. We've had our fill. Shall we head back to the inn?"
    voice audio.elara_ch1_line37
    elara  "Of course, my heart."

    jump ch1_common_fireworks

# =============================================================================
# SECTION 8: LABEL CH1_COMMON_FIREWORKS — City Convergence + Return to Inn
# =============================================================================
# All four city options converge here.
# ADDED LATER: Trumpet announcement, fireworks, walk back to inn, kids bedtime.
# (PDF p19-21)
# =============================================================================

label ch1_common_fireworks:

    stop audio fadeout 1.0
    scene bg_tianho_city_night with dissolve
    "As we make our way back through the bustling streets of Tianho, the sound of a trumpet pierces the night, echoing through the city."
    "I stop in my tracks. Elara looks at me curiously."

    show elara at right_char with Dissolve(0.2)
    show dorian neutral at left_char with Dissolve(0.2)
    voice audio.elara_ch1_line38
    elara "What is it? Is something wrong?"

    "I glance up at the dark sky, and smiled at her."

    voice audio.dorian_ch1_line39
    dorian "They sounded the trumpet. There will be preparatory fireworks to honor the Emperor of Kyeongjang. Look up, my heart."

    hide dorian
    hide elara
    "The kids immediately crane their necks, their excitement bubbling over. Emily grabs Daniel's arm, bouncing on her toes."

    show emily at left_char_kids
    show daniel at right_char_kids
    with Dissolve(0.2)
    emily "Fireworks? Really?"
    voice audio.daniel_ch1_line18
    daniel "Now, dad? I wanna see!"
    hide emily
    hide daniel
    show lucas at right_char_kids with Dissolve(0.2)
    voice audio.lucas_ch1_line17
    lucas "Shhh!! I want to hear them!!"

    "Sarah doesn't say a word, but she quickly flips open her sketchbook, pencil poised and ready."

    hide lucas
    scene bg_tianho_deng_blossom with dissolve    # PLACEHOLDER — Tianho city, fireworks above | use bg_tianho_deng_blossom for bg_tianho_celeb_deng

    # play sound sfx_fireworks                    # PLACEHOLDER — sfx_fireworks

    "Then, with a loud crack, the first firework bursts into the sky, painting the night with streaks of vibrant crimson and gold."
    "The crowd around us pauses, heads tilting back as more fireworks follow in rapid succession — emerald greens, sapphire blues, and fiery oranges dancing across the night sky."

    show lucas at left_char_kids
    show daniel at right_char_kids
    with Dissolve(0.2)
    voice audio.lucas_ch1_line18
    lucas "Whoa! Did you see that? That one looked like a dragon!"
    voice audio.daniel_ch1_line19
    daniel "Pft. No it doesn't, Lucas."
    hide daniel
    show emily at right_char_kids with Dissolve(0.2)
    emily "Oh, let him have his fun, Mr. Serious."
    hide emily
    hide lucas

    show elara at right_char
    show dorian normal at left_char
    with Dissolve(0.2)
    voice audio.elara_ch1_line39
    elara "They really go all out here, don't they?"
    voice audio.dorian_ch1_line40
    dorian "Well, with such a momentous occasion tomorrow, we can't afford to."

    "I watch as the sky explodes in a final cascade of shimmering gold and silver, like falling stars."

    "Sarah, sketching furiously, finally looks up as the last spark fades."

    hide elara
    show sarah at right_char_kids with Dissolve(0.2)
    voice audio.sarah_ch1_line17
    sarah "I think I got it."

    "She holds up her page to show a hastily drawn but striking depiction of the fireworks."

    voice audio.sarah_ch1_line18
    sarah "I think I'll call it: The resplendence of fireworks."
    hide sarah
    show emily at right_char_kids with Dissolve(0.2)
    emily "Wow!"
    hide emily
    show dorian smile at left_char
    voice audio.dorian_ch1_line41
    dorian "Haha. Looks good, Sarah."
    show daniel at right_char_kids with Dissolve(0.2)
    voice audio.daniel_ch1_line20
    daniel "It looks like a bunch of bull—"
    hide daniel
    show elara at right_char with Dissolve(0.2)
    voice audio.elara_ch1_line40
    elara "Daniel, be nice."

    "As the crowd starts to disperse, we gather the children and head back toward the inn."

    hide elara
    hide dorian
    scene bg_dorians_room with fade      # PLACEHOLDER — Dorian's hotel room, evening
    stop music fadeout 1.0

    "By the time we reach the inn, the kids are noticeably calmer. Elara ushers them inside, and one by one, they begin to settle."
    "Lucas and Emily curl up together, still whispering about the dragons they hope to see tomorrow. Daniel sits by the window for a moment, staring out at the now-still city before finally joining his siblings."
    "Sarah places her sketchbook neatly by her side before lying down with a satisfied sigh."

    show sarah at right_char_kids with Dissolve(0.2)
    voice audio.sarah_ch1_line19
    sarah "Good night mom. Good night dad. *yawns* Today… was amazing."
    hide sarah

    show elara at right_char with Dissolve(0.2)
    voice audio.elara_ch1_line41
    elara "Good night, babies. See you tomorrow."

    show lucas at left_char_kids with Dissolve(0.2)
    voice audio.lucas_ch1_line19
    lucas "I had a lot of fun, mom. And dad. *yawns*"
    hide lucas

    "She smiles and turns to me."

    show dorian neutral at left_char with Dissolve(0.2)
    voice audio.elara_ch1_line42
    elara "They'll remember this night forever."
    voice audio.dorian_ch1_line42
    dorian "So will I. Thank you, my heart. I needed this."
    voice audio.elara_ch1_line43
    elara "*yawns* We better get back to bed. Want me to brew ourselves some hot tea before going to bed?"
    voice audio.dorian_ch1_line43
    dorian "Gladly."

    "The room falls quiet as the children drift off, their breathing soft and steady."
    "Elara and I exchange a knowing glance before settling into our own space, the night finally giving way to a deep, peaceful calm."
    "As we lay together on the soft bedding of the inn, her hand rested lightly on my chest, her breathing even and serene."
    "The sounds of Tianho—distant chatter, the faint clatter of late-night carts—lulled me to sleep."

    # -------------------------------------------------------------------------
    # PROSPERITY DRAGON DREAM — Balcony / Promise
    # BG: bg_dream_white (or dorians_room — dragon on balcony)
    # ADDED LATER: Full dream from PDF p21-23 — much longer than original
    # -------------------------------------------------------------------------

    hide elara
    hide dorian
    stop music fadeout 2.0
    scene black with fade
    scene bg_dorians_room_off with fade # PLACEHoLDER

    "I awaken in the quiet hours before dawn, a strange sense of unease pressing against my chest."
    "Moonlight filters through the wooden lattice windows, painting the room in pale silver hues. Everything is still—Elara sleeps soundly beside me, her breaths soft and rhythmic."
    "Then, I see him."

    scene bg_tianho_city_night_sleeping with fade
    play music audio.ost_dream_dragon

    # show prosperity_dragon on balcony — Prosperity Dragon sprite on balcony
    # cg_prosperity_dragon_balcony here — dragon on the balcony overlooking Tianho

    "He hovers just beyond the balcony, suspended against the backdrop of Tianho's breathtaking view. An enormous dragon, his scales a vibrant blend of red and gold, shimmers in the faint light."
    "He was floating on the balcony, staring at the beautiful scenery of Tianho."
    "The glow radiating from him reflects off the walls, casting patterns that flicker and twist like living embers."

    "I rise quietly, careful not to wake Elara, and step toward the open balcony."
    "His gaze is fixed on the city below. The lantern-lit streets and winding waterways of Tianho stretch out before us like a dream."

    voice audio.dorian_ch1_line44
    dorian "Beautiful, isn't it?"
    voice audio.prosperity_dragon_ch1_line1
    prosperity_dragon "Very. Tianho never ceases to amaze me."
    voice audio.prosperity_dragon_ch1_line2
    prosperity_dragon "Beauty, prosperity... it lives in every corner of this place."

    "As he turns to face me fully, his claws click softly against the wooden floor."

    voice audio.prosperity_dragon_ch1_line3
    prosperity_dragon "I felt I needed to talk to you."

    "His gaze flicked briefly to Elara, then back to me."

    show dorian sleepware_serious at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line45
    dorian "What is it? Is it about tomorrow?"

    "He pauses, and the silence stretches. The hum of energy around him grows faintly louder, like a distant pulse."

    voice audio.prosperity_dragon_ch1_line4
    prosperity_dragon "Dorian. You must promise me something."

    "I frown, unease curling in my gut"

    show dorian sleepware_serious at left_char
    voice audio.dorian_ch1_line46
    dorian "Promise you what?"

    "His energy shifts, intensifying. Small sparks ripple around him, dancing in the air before dissipating."
    voice audio.prosperity_dragon_ch1_line5
    prosperity_dragon "Promise me that no matter what happens you will not lose connection with me."
    voice audio.prosperity_dragon_ch1_line6
    prosperity_dragon "You will not lose yourself."
    show dorian sleepware_serious at left_char
    voice audio.dorian_ch1_line47
    dorian "What are you talking about? You're not making sense. Is something wrong?"

    "His energy grows stronger. Sparks fly around him."

    voice audio.prosperity_dragon_ch1_line7
    prosperity_dragon "There are things I cannot say, Dorian. Things even I, with all my power, am forbidden to interfere with."

    "The hum grows louder now, his form brighter, casting shadows that flicker like flames."

    voice audio.prosperity_dragon_ch1_line8
    prosperity_dragon "But you must trust me. There will come a time when you feel like all is lost. In that moment, you must hold on to who you are—and hold on to me."

    show dorian sleepware_sad at left_char
    voice audio.dorian_ch1_line48
    dorian "You're not making this any easier."

    "His massive head lowers until we are eye-to-eye, his breath warm against my face."

    voice audio.prosperity_dragon_ch1_line9
    prosperity_dragon "The Weaver's threads of fate bind even me. All I can do is remind you of what matters. Your connection to me, to the fire that burns within you, is your anchor."
    voice audio.prosperity_dragon_ch1_line10
    prosperity_dragon "Do not sever it, Dorian. No matter what."

    "He pulls back, his towering form retreating into the shadows."

    voice audio.prosperity_dragon_ch1_line11
    prosperity_dragon "Dawn is coming. I must go. But remember, Dorian—promise me."

    "His words linger in the air as his body begins to shimmer, his form dissolving into a cascade of molten light. The warmth he leaves behind clings to the air, fading as quickly as it came."
    stop music fadeout 2.5
    show dorian sleepware_serious at left_char
    voice audio.dorian_ch1_line49
    dorian "What? Wait, I—"

    hide dorian
    jump ch1_castle_morning

# =============================================================================
# SECTION 9: LABEL CH1_CASTLE_MORNING — Next Morning (Castle)
# =============================================================================
# ADDED LATER: Entire next-day sequence from PDF p23-29.
# Gao/Jiang/Cyrus wake Dorian. Walk through castle. Audition line inspection.
# The desperate woman. Leads into ch1_auditions.
# =============================================================================

label ch1_castle_morning:

    # -------------------------------------------------------------------------
    # WAKING — Gao and Jiang with spilled coffee; Cyrus arrives
    # BG: bg_tianho_castle_interior
    # -------------------------------------------------------------------------

    scene bg_dorians_room with fade   # PLACEHOLDER — Tianho Castle interior, morning | use dorians_room as placeholder

    # play music ost_tianho_festival volume 0.1 fadein 2.0  # PLACEHOLDER — softer morning version

    show soldier_gao at left_char
    show soldier_jiang at right_char
    with Dissolve(0.2)
    voice audio.jiang_ch1_line1
    jiang "Paladin! Paladin Dorian! Wake up, sir!"
    voice audio.gao_ch1_line2
    gao   "Jiang, you're too loud! You're going to give the Paladin a heart attack before he even gets up!"
    voice audio.jiang_ch1_line2
    jiang "Well, you weren't helping when you spilled hot coffee on the way here, were you, Gao? You're practically useless!"

    "I rub my temples, trying to shake off the haze of interrupted sleep, when the air suddenly grows tense. A shadow looms over the two soldiers."

    show cyrus at center_char with Dissolve(0.2)
    voice audio.cyrus_ch1_line1
    cyrus "What is the meaning of this racket?!"

    "The soldiers freeze, their backs stiffening as though turned to stone. Soldier Gao, who just moments ago seemed on the verge of nervous collapse, spins on his heel and salutes so sharply he nearly hits himself in the face."

    voice audio.gao_ch1_line3
    gao "P-P-Paladin Cyrus! Sir! I-I was just—"
    voice audio.cyrus_ch1_line2
    cyrus "Spit it out, boy! I haven't the time to decipher your blubbering!"
    voice audio.jiang_ch1_line3
    jiang "Paladin Dorian fell asleep, sir. Gao thought coffee would help, but he, uh… tripped."

    "Gao swallows hard, his voice barely above a whisper."

    voice audio.gao_ch1_line4
    gao "I… I'm sorry, sir…"

    "I decide it's time to intervene before Cyrus verbally flattens them both."
    "Swinging my legs over the side of the bed, I rise and straighten my tunic, rubbing the back of my neck as I address the scene."
    hide soldier_jiang
    hide soldier_gao
    hide cyrus
    show dorian sleepware_neutral at left_char
    show cyrus at right_char
    with Dissolve(0.2)
    voice audio.dorian_ch1_line50
    dorian "Enough, Cyrus. They were only doing their job — clumsily, I'll admit, but well-intentioned. Let it go."

    "Cyrus narrows his eyes at me, clearly annoyed."

    voice audio.cyrus_ch1_line3
    cyrus "Your leniency is why discipline among the ranks is slipping, Dorian. Soldiers like these will never survive the battlefield if they can't even handle a simple morning task."
    show dorian sleepware_serious at left_char
    voice audio.dorian_ch1_line51
    dorian "Berating them further isn't going to change anything."
    voice audio.cyrus_ch1_line4
    cyrus "Fine. But don't let this happen again, Dorian. The Emperor's procession waits for no one — not even the Dragon of Gale and his soldiers."
    hide soldier_gao
    hide soldier_jiang
    "The four of us stride through the expansive halls of Tianho Castle, the sound of our boots echoing against polished stone floors."
    "Delicate silk banners sway gently in the morning breeze filtering through open lattice windows, each banner bearing an embroidered sigil of Tianho's imperial line."
    scene bg_tianho_city_morning with fade

    show dorian normal at left_char
    show cyrus at right_char
    with Dissolve(0.2)
    voice audio.cyrus_ch1_line5
    cyrus "The Emperor of Kyeongjang will be arriving shortly. His appearance has been meticulously planned. Extravagance is expected."
    voice audio.dorian_ch1_line52
    dorian "We got that covered, Cyrus. Every single guard and soldier have been stationed on all locations of the city."
    voice audio.dorian_ch1_line53
    dorian "We secured the area from the Qiaxing Square to the Xiangli Centre. Guarded by trained fire, wind and earth channelers from Tianho, Gale and Mjoll."

    "Soldier Gao and Soldier Jiang exchange nervous glances behind him, clearly on edge."

    # -------------------------------------------------------------------------
    # THE AUDITION LINE — Applicants for the Emperor's son's interpreter
    # -------------------------------------------------------------------------

    "As we approach the central courtyard, the sound of hushed murmurs grows louder. A long line of people snakes through the courtyard."
    "The line stretches endlessly through the courtyard, weaving past the garden ponds and stone bridges."
    "Most of them clutch documents, some carrying small tokens or gifts."
    hide dorian
    show soldier_gao at left_char with Dissolve(0.2)
    voice audio.gao_ch1_line5
    gao "What's with the line, sir?"

    voice audio.cyrus_ch1_line6
    cyrus "They're here to apply for the position of a sign language interpreter for the Emperor of Kyeongjang's son. The lad's deaf mute, and the Emperor insists on finding the very best for him."
    hide soldier_gao
    show dorian normal_alt_neutral at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line54
    dorian "There's no need to prolong this. My men already found someone qualified — his name is Jiyo. He's more than capable to serve the son for the night."

    voice audio.cyrus_ch1_line7
    cyrus "Jiyo? You're suggesting a convict, Dorian. A man with a criminal record to serve the Emperor's son?"
    voice audio.dorian_ch1_line55
    dorian "He's served his time and turned his life around. He's an exceptional signer, far better than most of these applicants. My men vetted him thoroughly."

    voice audio.cyrus_ch1_line8
    cyrus "Clearly, your men need to learn what 'thorough' means. A man's past cannot be ignored so easily, not when it concerns the imperial family."
    show dorian normal_alt_annoyed at left_char
    voice audio.dorian_ch1_line56
    dorian "Are you questioning my men's judgment or mine, Cyrus?"

    "Before Cyrus can respond, a commotion breaks out near the front of the line. A woman falls to her knees, clutching the hem of a guard's armor. Her face is streaked with tears, her voice desperate."
    hide dorian
    hide cyrus
    show woman_2 kneeling at left      # PLACEHOLDER — desperate woman sprite
    show female_guard at right                 # PLACEHOLDER — female guard sprite
    with Dissolve(0.2)

    woman_2 "Please, I beg you! Let me audition! My son is starving, and this is my only chance to provide for him. I'll do anything!"

    "The female guard standing before her doesn't flinch."

    female_guard "I'm sorry, mam but according to your criminal record, you were convicted of stealing food from your workplace at a bathhouse. We're disqualifying your application. Next!"
    woman_2 "*sobbing* Please, no! What does that have to do with this?"

    "The woman clings tighter, her sobs echoing across the courtyard. The guard sighs, her patience wearing thin."

    female_guard "Such a waste of time. Get her out of my sight."

    "With a curt nod, two other guards step forward and grab the woman by the arms, dragging her away as she struggles."

    woman_2 "No! Please, my son — he needs me! Just give me a chance, please!"
    female_guard "Good riddance. Pft."
    hide female_guard
    hide woman_2

    show dorian normal_alt_calm at left_char
    show cyrus at right_char
    with Dissolve(0.2)
    voice audio.dorian_ch1_line57
    dorian "Your people are quick to dismiss, Cyrus. Not everyone's past defines them. Sometimes all they need is a second chance."
    show dorian normal_alt_annoyed at left_char
    voice audio.cyrus_ch1_line9
    cyrus  "You're being too soft, Paladin Dorian. A second chance is a gamble we cannot afford to take."
    hide dorian
    show soldier_jiang at left_char with Dissolve(0.2)
    voice audio.jiang_ch1_line4
    jiang  "The compensation must be prestigious for so many people to be desperate to apply for a one-time job."
    voice audio.cyrus_ch1_line10
    cyrus  "Prestigious doesn't even begin to cover it. Whoever is chosen will not only serve the royal family of Kyeongjang. It's a chance to rise far above their station."
    hide soldier_jiang
    show dorian normal_alt_neutral at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line58
    dorian "And chances are, if they like their service, they might take the person to live with them in Kyeongjang."
    voice audio.cyrus_ch1_line11
    cyrus  "Imagine living in an empire that lives only in legends. Gah! The dream! One can—"

    hide dorian
    hide cyrus
    hide soldier_jiang
    jump ch1_auditions

# =============================================================================
# SECTION 10: LABEL CH1_AUDITIONS — D2: Niko and Kaito (Expanded)
# =============================================================================
# REWRITTEN from PDF p25-29: Full prophet backstory, female guard threatens duel,
# Cyrus's personal grievance about his cousin. Much longer than original.
# =============================================================================

label ch1_auditions:

    "Before Cyrus can utter another word, the next applicants step forward. Two men approach the front of the line."
    "The older man speaks first, his voice steady and respectful."

    show niko normal_base at left_char
    show cyrus at right_char
    with Dissolve(0.25)
    voice audio.niko_ch1_line1
    niko "Honored officials, my name is Niko Tsukumo, a doctor from the village of Hamatame. This is my younger brother, Kaito."
    voice audio.niko_ch1_line2
    niko "He is here to apply for the role of interpreter for the Imperial Son. Kaito is fluent in sign language and possesses exceptional skill."

    "Kaito bows deeply, his hands trembling slightly as he unfolds a scroll of qualifications."

    voice audio.kaito_ch1_line1
    kaito "G-good morning. It's an honor to be here. I am prepared to demonstrate my abilities."

    "For a brief moment, a hush falls over the courtyard."

    show niko normal_smile at left_char
    voice audio.niko_ch1_line3
    niko "You got this, Kaito. Remember what we practiced."

    "Before either man can say more, Cyrus raises a hand, his face hardening like stone."
    voice audio.cyrus_ch1_line12
    cyrus "That's enough. Guards, take these men out of here."

    "The two men exchange a glance, confusion flickering across their faces. Niko's expression tightens."

    show niko normal_serious at left_char
    voice audio.niko_ch1_line4
    niko "Paladin, with respect — may I ask why?"
    voice audio.cyrus_ch1_line13
    cyrus "Do you think I am ignorant of who you are, Tsukumo? Or of who your brother is? Do you think your false civility cloaks who you truly are?"
    voice audio.niko_ch1_line5
    niko "If you know who we are, then you must also know that we have done nothing wrong. My brother seeks only to serve."
    voice audio.cyrus_ch1_line14
    cyrus "You are prophets of the death god, are you not? The one whose disciples are forbidden to save a dying man — even if he begs for breath. You let children bleed out on cold stone if it is 'their time.' You would stand silent as plague takes a village, all in the name of some sacred death. And now you want to 'serve' the palace?"
    "A murmur ripples through the line of applicants, and a few people take a cautious step back."

    hide niko
    show woman_1 at left_char with Dissolve(0.2)
    woman_1 "Tetrad save us… a prophet of the death god?"
    hide woman_1
    show man_2 at left_char with Dissolve(0.2)
    man_2 "A Chosen of Enoch? Oh no! He'll bring misfortune upon us!"
    hide man_2
    show man_3 at left_char with Dissolve(0.2)
    man_3 "Get him out of here!"
    hide man_3

    "The younger brother, Kaito, stiffens under the hostile murmurs, his knuckles white as he clutches the hem of his robe. Niko, however, remains calm, though his voice tightens."

    show niko normal_base at left_char with Dissolve(0.2)
    voice audio.kaito_ch1_line2
    kaito "B-Brother…"
    voice audio.niko_ch1_line6
    niko  "Yes. We serve Enoch. But we do not bring death. We offer peace to those whose time has come. We comfort. We do not decide. That is not our place."

    "Cyrus' lips curl into a sneer."
    voice audio.cyrus_ch1_line15
    cyrus "Don't twist your heresies into compassion. Your order watched my cousin bleed out on a battlefield — because he had 'met his time'. Your order knelt beside him, praying, as his lungs filled with blood. Don't you dare speak of comfort."

    hide niko
    show female_guard at left_char with Dissolve(0.2)
    female_guard "So this is what the Death God's kindness looks like? Letting the weak die, untouched? And you think we'll let you serve the royal family?"
    hide female_guard
    show man_3 at left_char with Dissolve(0.2)
    man_3 "They worship death. That's all you need to know. Get them out of here before misfortune falls on all of us!"
    hide man_3
    show man_1 at left_char with Dissolve(0.2)
    voice man1_ch1_line1
    man_1 "Please! Let them out!"
    hide man_1

    show niko normal_serious at left_char with Dissolve(0.2)
    voice audio.niko_ch1_line7
    niko "We came to serve. Not to interfere, not to harm. My brother only asks for a chance to interpret — not to pass judgment on life or death."
    voice audio.cyrus_ch1_line16
    cyrus "Spare me your platitudes, Tsukumo. Prophets of Enoch have no place in this court. Your kind are lunatics — worshippers of a barbaric, ritualistic god who revels in death and despair."
    hide niko
    show soldier_jiang at left_char with Dissolve(0.2)
    voice audio.jiang_ch1_line5
    jiang "That's right! Tell him like it is, Paladin!"
    hide soldier_jiang
    voice audio.kaito_ch1_line3
    kaito "P-Please… I only want to help. Please."

    "The female guard scoffs, her hand resting on the hilt of her sword."

    show female_guard at left_char with Dissolve(0.2)
    female_guard "You want to help? Then prove you're not a coward hiding behind your god's silence. Face me in a duel to the death!"
    hide female_guard
    show soldier_gao at left_char with Dissolve(0.2)
    voice audio.gao_ch1_line6
    gao "Th-that won't be necessary, ma'am! We're here to evaluate — not shed blood!"
    hide soldier_gao

    voice audio.kaito_ch1_line4
    kaito "M-Mercy… Brother, I think we should go…"
    hide cyrus
    show dorian normal_alt_calm at left_char
    show niko normal_serious at right_char
    with Dissolve(0.2)

    "My instincts scream at me to intervene, but I know that doing so will draw the ire of Cyrus and possibly the entire court. Yet, as I look at the Tsukumo brothers, I see no malice in their eyes."
    "What should I do?"
    menu:

        # -----------------------------------------------------------------------
        # CHOICE 1: Intervene (+niko_affection)
        # -----------------------------------------------------------------------
        "Intervene.":
            $ ch1_audition_choice = "intervene"
            $ niko_affection += 1

            "Before the female guard can step forward, I raise a hand, silencing her with a sharp look."

            show dorian normal_alt_annoyed at left_char
            voice audio.dorian_ch1_line59
            dorian "Enough."

            "I step forward, positioning myself between the guards and the brothers."

            hide niko
            show female_guard at right_char with Dissolve(0.2)
            female_guard "P-Paladin Dorian? I don't understand. Why would you defend these lunatics? I—"
            hide female_guard
            show cyrus at right_char with Dissolve(0.2)
            voice audio.cyrus_ch1_line17
            cyrus "Dorian, you overstep your bounds."

            "I turn to him, meeting his glare."

            show dorian normal_alt_annoyed at left_char with Dissolve(0.2)
            voice audio.dorian_ch1_line60
            dorian "Do I? Or is it you who's letting personal prejudice blind you? They came to prove their worth, not to be humiliated. I won't allow any violence to be inflicted upon innocents in my presence."

            "Cyrus glares at me, his fists tightening at his sides."

            voice audio.cyrus_ch1_line18
            cyrus "'Innocents'?! Have you lost your bloody mind, Dorian? You really believe these barbarians are innocent? May I remind you that they serve the death god Enoch? Tsukumo is a chosen of the Death God! He and his brother are part of the prophets!"
            hide cyrus
            show niko normal_serious at right_char with Dissolve(0.2)
            voice audio.niko_ch1_line8
            niko  "We've harmed no one. Let Lord Enoch himself bear witness to that."
            show dorian serious at left_char
            voice audio.dorian_ch1_line61
            dorian "Leave them be, Cyrus. I won't ask again."

            "Cyrus scoffs and finally steps back, though it's clear he does so grudgingly."

            hide niko
            show cyrus at right_char with Dissolve(0.2)
            voice audio.cyrus_ch1_line19
            cyrus "Fine. But I still don't trust them near the imperial family. Guards, remove them."

            "Before the guards can act, Kaito raises his chin, his voice trembling but defiant."

            hide cyrus
            show niko normal_base at right_char with Dissolve(0.2)
            voice audio.niko_ch1_line9
            niko "We'll leave on our own. We don't need your escort."

            voice audio.kaito_ch1_line5
            kaito "Yeah! K-Keep your damned position!"
            voice audio.niko_ch1_line10
            niko "I held out hope that you people would be different. The truth will reveal itself in time. Until then, I wish you peace."
            voice audio.niko_ch1_line11
            niko "Let's go brother. We're too good for this place."

            hide niko
            show man_1 at right_char with Dissolve(0.2)
            voice man1_ch1_line2    
            man_1 "Get out of here before I crack your skull with this rock!"
            hide man_1
            show soldier_jiang at right_char with Dissolve(0.2)
            voice audio.jiang_ch1_line6
            jiang "Get out of here, lunatics!"
            hide soldier_jiang

            "The brothers ignore him, their dignity intact despite the hostility. Just before they disappear into the crowd, Niko turns back, his gaze locking with mine. His expression softens, and he dips his head slightly."

            show niko normal_smile at right_char with Dissolve(0.2)
            voice audio.niko_ch1_line12
            niko "Thank you, Paladin. I do not know your name but I know that few would risk standing against their peers. You have my respect."

            "As the brothers vanish from sight, Cyrus scoffs, his expression sour with contempt."
            hide niko
            show cyrus at right_char with Dissolve(0.2)
            voice audio.cyrus_ch1_line20
            cyrus "Siding with those disgusting lunatics… pft! We shall not speak of this again, Dorian. Even the thought of them disgusts me."

            "I turn to Cyrus, my voice low and firm."

            show dorian neutral at left_char with Dissolve(0.2)
            voice audio.dorian_ch1_line62
            dorian "Fair enough. But don't mistake my actions for siding with anyone, Cyrus. I act for justice, not for prejudice."

        # -----------------------------------------------------------------------
        # CHOICE 2: Stay Silent — no stat effect
        # -----------------------------------------------------------------------
        "Stay Silent.":
            $ ch1_audition_choice = "silent"

            "I hesitate, my hands curling into fists at my sides. Cyrus is seething, and the female guard's mocking laughter grates on my nerves, but I hold back."

            show dorian normal_alt_tense at left_char with Dissolve(0.2)
            hide niko
            show soldier_gao at right_char with Dissolve(0.2)
            voice audio.gao_ch1_line7
            gao "P-Paladin Cyrus, think of the time being wasted on these, um…"
            hide soldier_gao
            show soldier_jiang at right_char with Dissolve(0.2)
            voice audio.jiang_ch1_line7
            jiang "Lunatics. They're lunatics."
            hide soldier_jiang
            show soldier_gao at right_char with Dissolve(0.2)
            voice audio.gao_ch1_line8
            gao "J-Jiang! Stop it!"
            hide soldier_gao

            "Cyrus takes a deep breath."

            show cyrus at right_char with Dissolve(0.2)
            voice audio.cyrus_ch1_line21
            cyrus "You're right. I won't have the imperial family sullied by the hands of a prophet of Enoch. Guards, remove them."

            "The female guard spits on Kaito's feet."

            hide cyrus
            show female_guard at right_char with Dissolve(0.2)
            female_guard "You heard the Paladin. Out!"
            hide female_guard

            show niko normal_sad at right_char with Dissolve(0.2)
            voice audio.kaito_ch1_line6
            kaito "You people are awful."
            voice audio.niko_ch1_line13
            niko  "I expected more from all of you. May Enoch have mercy on your souls. Let's go Kaito."
            hide niko
            show cyrus at right_char with Dissolve(0.2)
            voice audio.cyrus_ch1_line22
            cyrus "May Enoch have mercy on your souls — spare me. If it were up to me, I'd gut their corpses and toss them to the crows."
            hide cyrus
            show soldier_jiang at right_char with Dissolve(0.2)
            voice audio.jiang_ch1_line8
            jiang "Hahahaha! Disgusting!"
            hide soldier_jiang

            "The crowd shifts uneasily. As the Tsukumo brothers disappear, Cyrus smirks, clearly satisfied with the outcome."

    hide dorian
    jump ch1_long_shen


# =============================================================================
# SECTION 11: LABEL CH1_LONG_SHEN — D3: Cyrus During King's Address
# =============================================================================
# ADDED LATER: Feng's arrival, his wife story, Zhuo Yin / coupons (PDF p31-32).
# The Cyrus choice is expanded from the original.
# =============================================================================

label ch1_long_shen:
    # [bg_tianho_imperial_gardens — sprawling gardens, lanterns, musicians tuning]
    scene bg_tianho_deng_day with fade
    "The Emperor of Kyeongjang, along with his family, will be arriving at nighttime."
    "We decide to pass the time by heading to the Imperial Gardens, a sprawling, meticulously maintained space filled with flowering trees, stone lanterns, and koi ponds."
    "Together with Paladin Cyrus, Soldier Jiang, and Soldier Gao, we inspect the venue for the Emperor of Kyeongjang's arrival."
    "Guards rehearse their formations with military precision while musicians tune their instruments in preparation for the grand ceremonial procession."

    "I personally oversee the placements of banners bearing Tianho's imperial crest, ensuring every detail reflects the dignity of the moment."
    "Paladin Cyrus supervises the final security checks, scrutinizing every station with his sharp eyes… and sharp tongue."

    show cyrus at right_char
    show dorian normal at left_char
    with Dissolve(0.25)
    voice audio.cyrus_ch1_line23
    cyrus "MERCIFUL TETRAD! If I see one more screw-up, I will personally see to it that you spend the night scrubbing latrines!"
    hide cyrus
    hide dorian
    show soldier_jiang at right_char with Dissolve(0.2)
    voice audio.jiang_ch1_line9
    jiang "Y-Y-Yes, sir!"
    hide soldier_jiang
    show soldier_gao at right_char with Dissolve(0.2)
    voice audio.gao_ch1_line9
    gao   "O-O-On it, sir!"
    hide soldier_gao
    show dorian normal_alt_neutral at left_char
    show cyrus at right_char
    with Dissolve(0.25)
    voice audio.dorian_ch1_line63
    dorian "Cyrus. Calm down, old man. You're scaring the soldiers."
    hide dorian
    hide cyrus
    scene bg_tianho_deng_night with fade
    "As the sun begins its descent, the imperial kitchens prepare an elaborate feast. The scent of roasted duck, spiced noodles, and sweet lotus cakes wafts through the air."

    # [COMMENT: bg_tianho_deng_blossom — twilight, hundreds of lanterns, ceremony bells]
    # BG -Tianho Celeb– Deng Blossom

    scene bg_tianho_deng_blossom with dissolve    # PLACEHOLDER — ceremony grounds, lanterns lit

    "As twilight fades, the courtyard of Tianho comes alive, illuminated by hundreds of lanterns. Their warm glow bathes the intricate carvings and towering pillars."
    "The ceremonial bells chime, signaling the imminent arrival of the Emperor of Kyeongjang. The air is heavy with expectation, the collective breath of the crowd held in reverence."

    "Paladin Qi Feng arrives, his commanding presence impossible to ignore."
    "His armor gleams under the lantern light, his expression one of calm authority."
    "He walks alongside none other than the Empress of Gale, Olympia Wyndham. The sight of her golden robes embroidered with phoenixes draws gasps from the courtiers and nobles."
    "I stand a little straighter as her gaze lands on me."

    show olympia at right_char
    show dorian serious at left_char
    with Dissolve(0.25)
    voice audio.olympia_ch1_line1
    olympia "Paladin Dorian. Paladin Cyrus."
    voice audio.dorian_ch1_line64
    dorian  "Your Grace."
    hide dorian
    show cyrus at left_char with Dissolve(0.2)
    voice audio.cyrus_ch1_line24
    cyrus   "Your Grace."

    "Olympia's lips curl into a faint smile, her sharp eyes glinting."

    voice audio.olympia_ch1_line2
    olympia "Both of you have done well. The preparations are flawless."
    voice audio.cyrus_ch1_line25
    cyrus   "Thank you, Your Grace. It's truly an honor."

    "She turns to address the assembled crowd, her voice carrying with regal authority."

    voice audio.olympia_ch1_line3
    olympia "Tonight marks a momentous occasion — a meeting not just of emperors, but of legacies. This event is more than symbolic; it is a promise. A promise of unity, prosperity, and shared destiny."
    voice audio.olympia_ch1_line4
    olympia "The Emperor of Kyeongjang, a ruler of wisdom and strength, comes to Tianho not as a stranger but as a brother."

    "As she finishes, a new figure enters — King Long Shen of Tianho. Dressed in crimson and gold robes embroidered with the Prosperity Dragon, he radiates authority and poise."
    "Flanked by ceremonial guards with ornate halberds, he ascends the dais with deliberate grace, acknowledging Olympia with a respectful bow."
    "Raising his hand, he signals for silence, and the courtyard stills completely."
    hide cyrus
    hide olympia
    show king_long_shen at center_char with Dissolve(0.2)
    voice audio.shen_ch1_line1
    long_shen "My loyal subjects, noble guests, and esteemed allies. Tonight, we stand on the precipice of a historic union. Together, our empires shall forge a bond unbroken by time or trials, a testament to the enduring power of unity."
    voice audio.shen_ch1_line2
    long_shen "Let tonight's gathering be remembered not merely as a meeting of monarchs but as the dawn of an era. An era where our peoples prosper side by side, bound by mutual respect and unwavering friendship. We —"
    hide king_long_shen with Dissolve(0.2)

    "Paladin Feng, my long time friend, approaches me with a grin. He and I have been serving the Empress for years."

    show feng_suit at right_char
    show dorian normal_alt_neutral at left_char
    with Dissolve(0.2)
    feng   "Dorian. How are you holding up? You look like you haven't slept a wink."
    voice audio.dorian_ch1_line65
    dorian "Managing. You know how it is — no rest for the weary."
    feng   "You're telling me. Yesterday, my wife dragged me all around the city. Said she needed to find 'the perfect gift' for tonight's feast."
    voice audio.dorian_ch1_line66
    dorian "You tell me. Elara did the same. Something about 'immersing ourselves in Tianho's culture.' My legs still ache from all the walking. But, yeah. I had fun. The kids had fun as well."
    show dorian normal_alt_confident at left_char
    feng   "Kids, huh? You've got no excuse then."
    show dorian normal_alt_neutral at left_char
    voice audio.dorian_ch1_line67
    dorian "Where did you go? Too bad we didn't bump into each other. I would have loved for you to meet my kids."
    feng   "Zhuo Yin! Man, you should have been there! Her Grace the Empress also got me coupons for the all-you-can-eat! It was fantastic!"
    voice audio.dorian_ch1_line68
    dorian "Wait… coupons? She didn't give me any. I'm starting to think you're the favorite Paladin."

    "Before Feng could reply, Paladin Cyrus storms over, his weathered face flushed with irritation."

    show cyrus at center_char with Dissolve(0.25)
    voice audio.cyrus_ch1_line26
    cyrus "You two fools! Standing here gossiping like washerwomen while the King of Tianho is giving his address? Do you have no sense of decorum?"

    show feng_suit at right_char with Dissolve(0.2)
    feng "Relax, Cyrus. We're just killing time. You should try it sometime — it might help with your blood pressure."

    "I suppress a laugh, but Cyrus' glare deepens, his face reddening."

    voice audio.cyrus_ch1_line27
    cyrus "I suggest that you obey and listen to the address. This is no time for your childish antics!"

    menu:

        # -----------------------------------------------------------------------
        # CHOICE 1: Obey Cyrus
        # -----------------------------------------------------------------------
        "Obey Cyrus.":
            $ ch1_cyrus_choice = "obey"

            "I bite back the retort forming in my throat and glance at Qi Feng, who smirks knowingly. Taking a deep breath, I nod and focus my attention back on King Long Shen."
            "The King's voice resonates across the courtyard, each word deliberate and weighted."

            hide cyrus
            hide dorian
            hide feng_suit
            show king_long_shen at center_char with Dissolve(0.25)
            voice audio.shen_ch1_line3
            long_shen "Together, our nations will stand as a beacon of unity…"

            "Cyrus shoots me a sideways glance and gives the faintest of approving nods, as if my silence was a small victory for him. I roll my eyes but hold my tongue."

            hide king_long_shen
            show feng_suit at right_char
            show dorian normal_alt_neutral at left_char
            with Dissolve(0.2)
            feng "Well, that was… enlightening. Glad you kept the peace, but you owe me for sitting through that without cracking a joke."
            show cyrus at center_char with Dissolve(0.25)
            voice audio.cyrus_ch1_line28
            cyrus "The two of you could learn something from the King's wisdom. Perhaps you should take notes."

        # -----------------------------------------------------------------------
        # CHOICE 2: Tell the old man to shut up (+feng_affection)
        # -----------------------------------------------------------------------
        "Tell the old man to shut up.":
            $ ch1_cyrus_choice = "told_off"
            $ feng_affection += 1

            "I narrow my eyes at Cyrus, my patience with his nagging finally snapping."

            show dorian normal_alt_annoyed at left_char with Dissolve(0.2)
            voice audio.dorian_ch1_line69
            dorian "Shut up, old man. You've been yelling all day — take a break before you keel over."

            "Feng snorts beside me, clearly amused, while Cyrus' face flushes an even deeper shade of crimson."

            show feng_suit at right_char with Dissolve(0.2)
            feng "Pft— Hahahaha!"
            show dorian normal_alt_neutral at left_char with Dissolve(0.2)
            voice audio.dorian_ch1_line70
            dorian "You heard me. Save the theatrics for the soldiers, Cyrus. It's not like the King will notice if I miss one line of his speech."
            voice audio.cyrus_ch1_line29
            cyrus "I-well… Tsk…"
            feng "Dorian's right, Cyrus. We're all tired, and honestly, you yelling at us isn't helping your blood pressure. Maybe you should sit down for a minute before you pop a vein."
            voice audio.dorian_ch1_line71
            dorian "Just loosen up, will you?"

            "The look on Cyrus' face is priceless. He opens his mouth to retort but snaps it shut again, storming off with a muttered string of curses. Qi Feng and I exchange a triumphant grin."

            hide cyrus with Dissolve(0.1)
            feng "That was bold. I didn't think you had it in you."


    jump ch1_ceremony


# =============================================================================
# SECTION 12: LABEL CH1_CEREMONY — Emperor's Arrival + Feast + Dorian Leaves
# =============================================================================
# ADDED LATER: Full Emperor arrival scene, feast, Dorian leaves early (PDF p33-35)
# =============================================================================


label ch1_ceremony:
    hide dorian
    hide feng_suit
    hide cyrus
    scene bg_tianho_city_night with fade   # PLACEHOLDER — castle interior, ceremony begins

    "As the ceremonial bell tolls, the low, resonant chime echoes through the courtyard. My thoughts wander briefly to Elara and the kids. Are they watching this momentous event unfold from somewhere within the palace grounds?"
    "I picture Sarah with her sketchpad balanced on her knees. Daniel, Lucas, and Emily, I imagine, are pretending to be guards, mimicking the disciplined stances of the soldiers."
    "Elara probably hushes them with a smile, pulling them close to keep them still."
    "Wherever they are, I hope they're enjoying this night more than I am."
    "The bell tolls one last time, the air heavy with expectation, and suddenly a wave of energy ripples through the courtyard. In a dazzling display of light, the Emperor of Kyeongjang and his entourage appear."

    scene bg_tianho_fanrong_square
    show cg_emperor_arrival
    with fade
    play music ost_emperor_arrival fadein 2.0   # PLACEHOLDER — ceremonial fanfare

    "The Emperor of Kyeongjang steps forward, wearing ornate robes shimmering as though woven from starlight. Beside him stands a woman, her presence just as regal, which I presume to be his Empress."
    stop music
    "Flanking them is a retinue of guards, their armor polished to perfection, reflecting the warm glow of the courtyard's lanterns. Their long spears, held with practiced precision, glint like silver under the night sky."
    "A collective gasp ripples through the crowd, followed by a wave of hushed murmur. Even Paladin Cyrus falls silent, his usual scowl replaced with a rare expression of awe"
    "I straighten instinctively, adjusting my stance and gripping the hilt of my sword at my side. This is the moment we've been preparing for."
    "As the Emperor takes another step forward, his eyes sweep across the gathered assembly. For a brief moment, I feel his gaze linger on me, and I resist the urge to fidget. Behind him, his guards form a protective arc, their movements precise and synchronized."

    hide cg_emperor_arrival
    scene bg_tianho_city_night
    with fade
    "When he speaks, his voice is deep and resonant, carrying effortlessly across the courtyard."
    voice audio.minjoon_ch1_line1
    emperor_minjoon "People of Tianho. My name is Hyon Min-joon, and I am the Emperor of Kyeongjang."
    voice audio.minjoon_ch1_line2
    emperor_minjoon "Let this meeting be a testament to what can be achieved when wisdom prevails over conflict, when unity triumphs over division. The bond we forge tonight will guide our empires into an era of unparalleled peace and prosperity."

    "The Emperor pauses, his gaze sweeping over the crowd again, then rests briefly on the Empress, who gives him a slight nod of encouragement."

    voice audio.minjoon_ch1_line3
    emperor_minjoon "Together, we will shape a future that honors our past and secures the well-being of generations to come. Let us begin."

    "As he finishes, he steps forward to meet Empress Olympia and the King of Tianho. The three rulers exchange formal bows before clasping hands in a gesture of unity."
    play music audio.ost_tianho_emperor volume 0.6
    "The crowd erupts into applause, the sound reverberating through the courtyard like a thunderous wave."
    # add crowd applause sfx
    "I give the signal, and the courtyard springs to life. The musicians begin their symphony, a vibrant blend of drums, strings, and flutes."
    # music + fanrong_square for bg
    "Dragon dancers burst into motion, their costumes shimmering in the lantern light as they weave intricate patterns across the open space."
    "Fireworks crackle and explode overhead, painting the night sky with vivid bursts of red, gold, and green."
    "The crowd cheers even louder, swept up in the grandeur of the moment. I glance upward toward the balconies, half-expecting to catch a glimpse of Elara and the kids."
    "Though I know they're likely watching from a private chamber with the other families, a small part of me still hopes to see them, to know they're witnessing this historic event."

    scene bg_tianho_castle_interior with dissolve

    "As the applause gradually fades and the fireworks dwindle into soft crackles in the sky, the Emperor of Kyeongjang, the Empress of Gale, and the King of Tianho are escorted with great fanfare into the grand halls of Tianho Castle."
    "Inside, the festivities begin in earnest. The central hall is adorned with silk banners in shades of crimson and gold, and long tables are lined with exotic dishes, their aromas blending into a tantalizing symphony."
    "Long tables groan under the weight of an extravagant feast—roasted duck glazed to perfection, steaming bamboo baskets of dumplings, delicate candied fruits, and spiced lotus cakes."
    "The air hums with lively conversation, the laughter of nobles, and the harmonious tunes of zithers and flutes."
    "Courtiers, nobles, and foreign dignitaries mingle, raising cups of fine rice wine in celebration, while dancers clad in flowing silks perform graceful routines in perfect synchronization, to the beat of Tianho's ceremonial tunes."
    "Fire channelers perform a dazzling routine in the center, conjuring fiery dragons that swirl and dissolve into embers, earning applause from the crowd."
    "I stand at the edge of the gathering, my hand resting on the hilt of my sword, my thoughts far from the revelry."
    "The dragon's cryptic words in my dream earlier still weigh heavily on my mind."
    stop music fadeout 2.0

    prosperity_dragon "There will come a time when you feel like all is lost. In that moment, you must hold on to who you are — and hold on to me."

    "I scan the room until my gaze lands on Feng, effortlessly charming a group of nobles with his jokes."

    show feng_suit at right_char
    show woman_1 at left_char
    with Dissolve(0.2)
    feng "And then I said — what do you want me to do? Pray to Adriana to hand me a new daughter?!"
    woman_1 "Hahaha! Paladin Feng, that's hilarious!"
    hide woman_1
    show man_1 at left_char with Dissolve(0.2)
    voice man1_ch1_line3
    man_1 "That is so funny! Haha! One more, good sir!"
    hide man_1

    "I shake my head, a faint smile tugging at my lips despite myself, and approach Feng."

    show dorian serious at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line72
    dorian "Feng… Can I have a word with you?"
    feng "Dorian? Oh sure, man!"

    "Feng raises a curious eyebrow but excuses himself with a dramatic flourish, much to the nobles' disappointment. He leads me to a quieter corner, away from prying ears."

    show dorian neutral at left_char
    feng  "What's up? You look like you've been chewing on a rock all night."
    show dorian sad at left_char
    voice audio.dorian_ch1_line73
    dorian "Feng, I need to leave. I need to be with Elara and the kids. Something doesn't feel right, and I can't shake it off."
    "Feng turns to me, his usual relaxed grin softening as he studies my face."

    feng  "Really? The party's just about to start! They haven't even brought out the roasted pig yet!"
    voice audio.dorian_ch1_line74
    dorian "I'll pass… I just have this feeling, you know?"
    feng  "You're as tense as a bowstring, Dorian. Alright, I'll cover for you. Enjoy your time with your family. If anyone asks, I'll tell them you're handling some critical duty."
    show dorian normal at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line75
    dorian "Thanks, Feng. You're the best."
    feng  "I know. Now go before I change my mind. And before Cyrus catches you."
    hide dorian
    hide feng_suit

    scene bg_tianho_xiangli_stalls with fade
    "As I step out into the cool night air, the distant music fades, replaced by the soft rustling of leaves in the breeze."
    "The streets are quiet, illuminated only by scattered lanterns casting gentle light on the cobblestone path."

    jump ch1_elara_chat


# =============================================================================
# SECTION 13: LABEL CH1_ELARA_CHAT — D4: Elara Chat at Inn After Party
# =============================================================================
# Dorian returns to inn after leaving the party.
# Kids sleeping. Elara talks. Ends with Olympia vision
# =============================================================================

label ch1_elara_chat:

    scene bg_dorians_room with fade # PLACEHOLDER
    stop music fadeout 2.0

    "When I reach the inn, I push the door open as silently as I can. Inside, the warm glow of a single lantern illuminates the cozy room."
    "Elara is there, seated near the bed where our children sleep peacefully, their small faces relaxed in dreams."

    show elara at right_char
    show dorian neutral at left_char
    with Dissolve(0.2)
    voice audio.elara_ch1_line44
    elara "You're back early, my heart. How was the celebration?"
    show dorian normal at left_char
    voice audio.dorian_ch1_line76
    dorian "I didn't want to stay. I'd rather be here — with all of you."
    show dorian neutral at left_char
    "She rises and steps toward me, her arms wrapping around me in a gentle embrace. The weight of the day slips away as I hold her close."
    "I glance at the bed where Sarah clutches her sketchpad even in sleep, and Daniel, Lucas, and Emily are nestled together under the blankets."

    voice audio.elara_ch1_line45
    elara "Let me pour you some water."

    "After a moment, she pulls away and pours me a glass of chilled water from the jug on the table, handing it to me with a knowing smile."

    voice audio.elara_ch1_line46
    elara "The kids ran wild through Tianho again today. Sarah's got her eye on this little porcelain doll in the market. She says she wants to name it 'Tedda,' of all things."
    voice audio.elara_ch1_line47
    elara "Lucas, of course, won't stop teasing her about it. Said he'd steal it and make it a pirate instead. They were chasing each other for hours."

    "She laughed softly, the sound delicate as windchimes. I took a slow sip from the glass, chuckling through a yawn."

    voice audio.elara_ch1_line48
    elara "How's work? Any interesting stories you wanna tell me?"

    jump ch1_elara_topic_menu


label ch1_elara_topic_menu:
    menu:
        # TOPIC 1: Cyrus — light banter
        "Talk about Cyrus." if not elara_talked_cyrus:
            $ elara_talked_cyrus = True

            show dorian normal_alt_neutral at left_char
            voice audio.dorian_ch1_line77
            dorian "Cyrus barked at nearly everyone today. Even the flagbearers weren't spared."
            voice audio.elara_ch1_line49
            elara  "Well, what's new? He's an old man who doesn't know the meaning of 'relax.'"
            show dorian smile at left_char
            voice audio.dorian_ch1_line78
            dorian "Pft… haha! Elara! But… you're not wrong. One of the younger soldiers nearly dropped his spear when Cyrus got in his face. I had to step in before he made the poor kid cry."
            voice audio.elara_ch1_line50
            elara  "You've always had a softer touch with people. Cyrus… well, he's been that way for as long as I've known him."
            show dorian normal_alt_neutral at left_char
            voice audio.dorian_ch1_line79
            dorian "Feng and I tried to get him to calm down, but you know how he is. He even berated us for talking while the King of Tianho was giving his address."

            "Elara reaches for her water and downs it all in one go."

            voice audio.elara_ch1_line51
            elara "You and Feng will be the end of that poor man. But you need someone like Cyrus around — someone to keep you in line."
            show dorian smile at left_char
            voice audio.dorian_ch1_line80
            dorian "Maybe. Or maybe we just like riling him up."

            jump ch1_elara_topic_menu

        # TOPIC 2: Feng — Zhuo Yin and coupons
        "Talk about Feng." if not elara_talked_feng:
            $ elara_talked_feng = True

            show dorian normal_alt_neutral at left_char
            voice audio.dorian_ch1_line81
            dorian "So… Feng was in rare form tonight. You'd think he was the Emperor himself with how he was strutting around. He had everyone in stitches at the party."
            voice audio.elara_ch1_line52
            elara  "That doesn't surprise me. He loves these kinds of events, doesn't he?"
            voice audio.dorian_ch1_line82
            dorian "Oh, absolutely. He told me he's going to take full credit for all the preparations since I skipped out early."
            voice audio.dorian_ch1_line83
            dorian "I swear, he could convince a stone to laugh if he tried. At one point, he even joked about Adriana granting him a new daughter — right in front of the clerics."
            voice audio.elara_ch1_line53
            elara  "The clerics of Adriana? Tetrad above, the nerve of that man! Please tell me he didn't start a scene."
            voice audio.dorian_ch1_line84
            dorian "No scene, just some very awkward looks. By the way, he said he brought his family here."
            voice audio.elara_ch1_line54
            elara  "Oh, we met them earlier today while out shopping. His youngest is adorable. Reminds me of Lucas at that age."

            "She grabs a cookie and offers me one before finishing hers."
            jump ch1_elara_topic_menu

        # TOPIC 3: Empress Olympia
        "Talk about Empress Olympia." if not elara_talked_olympia:
            $ elara_talked_olympia = True

            show dorian normal_alt_neutral at left_char
            voice audio.dorian_ch1_line85
            dorian "Olympia gave a speech tonight. You would've been proud of her. She had the whole audience hanging on her every word."
            voice audio.elara_ch1_line55
            elara  "I've always admired her ability to command a room. What did she say?"
            voice audio.dorian_ch1_line86
            dorian "She spoke about unity and peace between the empires. Made it sound like tonight was the beginning of a new era."
            voice audio.elara_ch1_line56
            elara  "And do you believe it?"
            show dorian neutral at left_char
            voice audio.dorian_ch1_line87
            dorian "It's my job to believe it, isn't it? But whether or not I do doesn't really matter."
            voice audio.elara_ch1_line57
            elara  "Were there any other rulers present?"
            show dorian normal_alt_neutral at left_char
            voice audio.dorian_ch1_line88
            dorian "King Long Shen was there to deliver an address."
            voice audio.dorian_ch1_line89
            dorian "King Gustav from Mjoll and King Tatsuya from Hinami were present at the party. They didn't deliver a speech though."

            jump ch1_elara_topic_menu

        # TOPIC 4: Emperor Min-joon — LEADS TO COMMON, ends the chat loop
        "Talk about the Kyeongjang Emperor, Hyon Min-joon.":

            show dorian normal_alt_neutral at left_char
            voice audio.dorian_ch1_line90
            dorian "The Emperor of Kyeongjang made quite an entrance tonight. Teleported right into the courtyard with his entourage."
            voice audio.elara_ch1_line58
            elara  "Teleportation? That's… bold. What was he like?"
            voice audio.dorian_ch1_line91
            dorian "Weren't you and the kids watching?"

            "Elara shakes her head."

            voice audio.elara_ch1_line59
            elara  "No. Emily tripped and hit her head earlier, so the kids decided to stay back and help me take care of her. We had a quiet dinner here at the inn instead."
            show dorian serious at left_char
            voice audio.dorian_ch1_line92
            dorian "Emily's alright, though, right?"
            voice audio.elara_ch1_line60
            elara  "She's fine. A little bump, but nothing a kiss and some cookies couldn't fix."
            voice audio.elara_ch1_line61
            elara  "So, how was this Emperor? Did he live up to all the stories?"
            show dorian normal_alt_neutral at left_char
            voice audio.dorian_ch1_line93
            dorian "He was… impressive. Even Cyrus was speechless for once."
            voice audio.elara_ch1_line62
            elara  "Now that's an accomplishment. What about his son? I heard there were a lot of applicants to be his translator."
            voice audio.dorian_ch1_line94
            dorian "The son wasn't there. It was just the Emperor, his wife, and guards."
            voice audio.elara_ch1_line63
            elara  "Really? That's too bad. I hope the interpreter still gets paid, though."

            jump ch1_elara_chat_common

label ch1_elara_chat_common:

    show dorian neutral at left_char
    show elara at right_char
    voice audio.elara_ch1_line64
    elara "*yawns* I think it's time for bed, my heart."
    voice audio.dorian_ch1_line95
    dorian "You're right. It's been a day."

    "Before heading to the bedroom, I walk over to each of our children and kiss them on the forehead."

    scene bg_dorians_room_off with fade # PLACEHOLDER
    hide dorian
    hide elara
    show dorian normal at left_char
    voice audio.dorian_ch1_line96
    dorian "Good night, kids."

    "When I turn back, Elara is leaning against the doorway."

    show elara at right_char with Dissolve(0.2)
    voice audio.elara_ch1_line65
    elara "They're already asleep, you know. You might wake them up."
    show dorian sad at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line97
    dorian "Maybe, but I can't shake this feeling. I needed to do that."

    # ADDED LATER: Elara's goodbye kiss, "I love you" exchange (PDF p39)
    "Elara walks up to me and gently places her hands on my shoulders. She pulls me down into a kiss, soft and lingering."

    voice audio.elara_ch1_line66
    elara "Whatever's weighing on you… let it go for tonight. Just rest. Remember, Dragon of Gale, I've got you."

    "We head to bed together."

    voice audio.elara_ch1_line67
    elara "I love you."
    show dorian smile at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line98
    dorian "I love you too, my heart."

    "As her breathing slows beside me, I close my eyes and drift to sleep."

    # -------------------------------------------------------------------------
    # OLYMPIA VISION — Much more detailed than original (PDF p39)
    # -------------------------------------------------------------------------

    hide elara
    hide dorian
    with fade
    stop music fadeout 1.0
    play music ost_tension_rising volume 0.2 fadein 2.0    # PLACEHOLDER — low dread music
    scene black with fade

    "Elara sleeps soundly beside me, her face serene in the faint moonlight filtering through the window. But I can't shake the twisting unease in my chest."
    voice prosperity_dragon_ch1_line5
    prosperity_dragon "Promise me that no matter what happens, you will not lose connection with me."
    voice prosperity_dragon_ch1_line6
    prosperity_dragon"You will not lose yourself."

    "I can't help but remember those words."

    "A wave of cold crashes over me, and the room seems to darken unnaturally. My body stiffens as a figure materializes at the foot of the bed."
    "Empress Olympia."
    "Her face is pale, streaked with blood. A jagged wound runs from her temple down to her jaw. Her gown is torn and soaked in crimson, her chest heaving as though every breath might be her last."

    # show olympia wounded at center

    show olympia at center_char with Dissolve(0.2)
    voice audio.olympia_ch1_line5
    olympia "Dorian… wake up. You must go to the castle. Now. Tianho… is in grave danger!"
    "She steps closer — the blood drips from her fingertips onto the floor, the crimson pooling and spreading unnaturally fast."
    voice audio.olympia_ch1_line6
    olympia "DO NOT TALLY!"

    camera at bigshake(5.0, rate=0.020, time=0.09), shattered_glass_transform
    with shattered_glass_transition
    hide olympia
    camera

    "Her image shatters like glass, and I'm left gasping for air, my heart pounding in my chest. The room is silent again, save for Elara's steady breathing."
    "I sit up, my breath coming in shallow gasps. The weight of her words presses on my chest like a stone."
    "I look at Elara, her peaceful expression so at odds with the storm raging in my head. I want to wake her, to tell her what I've seen, but something stops me."
    "Instead, I rise quietly, grabbing my sword and cloak. I kiss her on the forehead."

    show dorian serious at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line99
    dorian "Stay safe, my heart."

    hide dorian
    jump ch1_battle


# =============================================================================
# SECTION 14: LABEL CH1_BATTLE — Castle Gate Through Taotie (D5–D10)
# =============================================================================
label ch1_battle:
    # -------------------------------------------------------------------------
    # ARRIVAL AT CASTLE GATE — Gao/Jiang already there; yaoguai emerges from ground
    # BG: bg_tianho_castle_gate (using food stalls diff lighting as proxy for now)
    # -------------------------------------------------------------------------

    # [COMMENT: bg_tianho_food_stalls_fire — streets outside castle, still lit, just before chaos]
    scene bg_tianho_xiangli_stalls with fade  # PLACEHOLDER — castle gate, pre-chaos

    # TODO: add audio sfx
    # play music ost_battle_tianho fadein 1.0     # PLACEHOLDER — battle OST
    # play audio amb_castle_battle loop           # PLACEHOLDER — ambient battle sounds

    "The inn is silent as I step into the cool night. Tianho sleeps on. The streets are quiet."
    "As I approach the castle gates, I spot two familiar figures in the torchlight — Soldiers Gao and Jiang. They stand rigid, their hands gripping their weapons tightly."

    show soldier_gao at left_char
    show soldier_jiang at right_char
    with Dissolve(0.25)
    voice audio.gao_ch1_line10
    gao  "Paladin Dorian? You're here!"
    voice audio.jiang_ch1_line10
    jiang "Paladin Cyrus and Paladin Feng are already inside. They went inside an hour ago!"
    hide soldier_gao
    show dorian serious at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line100
    dorian "Did Cyrus or Feng mention anything specific? Anything strange before they went in?"

    "Before either of them can answer, a deafening rumble erupts beneath us. The ground quakes violently, and cracks spiderweb across the cobblestones."
    hide soldier_jiang
    show soldier_gao at right_char with Dissolve(0.2)
    voice audio.gao_ch1_line11
    gao "What the—"

    "Before he can finish, the earth beneath Jiang explodes."

    hide soldier_gao
    hide soldier_jiang
    hide dorian
    scene bg_tianho_city_on_fire with flash
    play music ost_battle

    "A monstrous yaoguai emerges, its massive, grotesque form dripping with black ichor that hisses and sizzles against the stone. Its six glowing red eyes scan the courtyard, its maw filled with jagged, rotting teeth that emit a foul stench."

    show yaoguai at center_yg with flash
    voice audio.yg_scream 
    yg "Raaaaaaawwrrr!!!"

    hide yaoguai
    show dorian dragon_eyes at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line101
    dorian "Dragon's Bollocks! A yaoguai?!"

    voice audio.gao_ch1_line12
    "Soldier Gao and Jiang scream, stumbling back as the creature lets out a piercing roar that shakes the very air around us."

    hide dorian
    $ renpy.save("quick-1")
    show soldier_jiang at left_char with Dissolve(0.2)
    voice audio.jiang_ch1_line11
    jiang "It's a yaoguai! Tetrad above, it's a yaoguai!"
    show soldier_gao at right_char with Dissolve(0.2)
    voice audio.gao_ch1_line13
    gao   "We're going to die! We're all going to—"

    hide soldier_gao
    hide soldier_jiang
    with Dissolve(0.1)

    # =====================================================================
    # D5 — TIMED QTC: Castle Gate (3 options) — all converge
    # =====================================================================
    $ _choice_timeout = 5.0
    menu:
        "Do nothing.":
            $ _choice_timeout = 0
            $ ch1_gate_qtc = "nothing"

            show dorian serious at left_char with Dissolve(0.2)
            "For a split second, I freeze, my mind racing as the yaoguai's eyes bore into mine."
            "Its guttural snarl sends chills down my spine, and I feel every instinct screaming at me to move, but I can't."
            show dorian angry at left_char
            "What in Tetrad's name is happening?!"

            show soldier_gao at right_char with Dissolve(0.2)
            voice audio.gao_ch1_line14
            gao "P-Paladin! Watch out!"

            "The yaoguai lunges, its claws carving through the air with terrifying speed. At the last second, Jiang dives to the side, pulling Gao and I with him."
            hide soldier_gao
            show yaoguai at right_yg with Dissolve(0.2)
            voice audio.yg_screech
            yg "Grrraaaaawwwww!!!"

            "The creature's attack slams into the ground, sending shards of stone flying everywhere."
            hide dorian
            hide yaoguai
            show soldier_jiang at left_char
            show soldier_gao at right_char
            with Dissolve(0.2)
            voice audio.jiang_ch1_line12
            jiang "Paladin Dorian! Are you alright?"
            voice audio.gao_ch1_line15
            gao   "That was close..."
            hide soldier_jiang
            hide soldier_gao
            show dorian serious at left_char with Dissolve(0.2)
            voice audio.dorian_ch1_line102
            dorian "Get up! Move!"

            "I shove Gao and Jiang toward the nearby wall as the yaoguai snarls, its glowing eyes locking on me now. My hands ignite with fire, the heat surging up my arms."

            hide soldier_gao
            hide soldier_jiang

        "Channel fire into a blazing shield to protect Gao and Jiang.":
            $ _choice_timeout = 0
            $ ch1_gate_qtc = "shield"

            show dorian serious at left_char with Dissolve(0.2)
            play sound sfx_wind
            "The yaoguai's claws slam into the ground, sending shockwaves through the courtyard. Without thinking, I thrust my hands forward, summoning a fiery barrier between us and the creature."
            show dorian dragon_eyes at left_char
            "Flames roar to life, swirling in a protective arc that absorbs the beast's attack with a deafening crack."
            "The heat from my shield is intense, but Gao and Jiang hold their ground."

            show yaoguai at right_yg with Dissolve(0.2)
            voice audio.toatie_roar_ch1_line3
            voice audio.yg_scream 
            yg "Grrraaawwwrrr!!"
            hide yaoguai

            show dorian serious at left_char
            voice audio.dorian_ch1_line103
            dorian "Are you alright?"
            show soldier_jiang at right_char with Dissolve(0.2)
            voice audio.jiang_ch1_line13
            jiang  "Paladin… Thank you!"
            voice audio.dorian_ch1_line104
            dorian "Get ready to run when I say."

            show dorian dragon_eyes at left_char
            "I concentrate, channeling more power into the shield until the flames burst outward in a controlled explosion. The yaoguai stumbles back, momentarily dazed."

            voice audio.dorian_ch1_line105
            dorian "Go now!"
            hide soldier_jiang with Dissolve(0.2)
            "Gao and Jiang dart to safety, and I extinguish the shield, stepping forward to face the creature head-on."

        "Hurl a fireball directly at the yaoguai's head to disorient it.":
            $ _choice_timeout = 0
            $ ch1_gate_qtc = "fireball"
            stop sound

            show dorian dragon_eyes at left_char with Dissolve(0.2)
            "The yaoguai lunges, its glowing red eyes locked on me. Without hesitation, I channel fire into my palm, condensing the heat into a pulsing orb."
            "I hurl the fireball with all my strength. The orb smashes into the yaoguai's face, erupting in a fiery explosion that engulfs its head in flames."

            show yaoguai at right_yg
            voice audio.toatie_roar_ch1_line1
            voice audio.toatie_roar_ch1_line3
            yg "Raaaaaaawwrrr!!! Grrraaawwwrrr!!"

            "The yaoguai lets out an ear-splitting roar, thrashing wildly as it tries to shake off the fire. Gao and Jiang take the opportunity to scramble to safety."
            hide yaoguai
            show soldier_gao at right_char with Dissolve(0.2)
            voice audio.gao_ch1_line16
            gao "P-Paladin! What should we do?"
            hide soldier_gao

            show yaoguai at right_yg
            voice audio.toatie_roar_ch1_line2
            "The yaoguai recovers, shaking off the flames, but I can see the scorch marks left behind. It snarls at me, more furious than ever."

    # All gate options converge — screams from city
    # [COMMENT: bg changes to food stalls on fire — city under siege]

    scene bg_tianho_city_on_fire with shock_cut  # PLACEHOLDER — city streets on fire
    "All of a sudden, I hear screams. Random screams. They pierce the night, each one twisting like a blade in my gut."

    # no sprite call for these 2
    woman_1 "Ahhhhh!!!"
    man_2 "No!! No!!"

    "The ground trembles beneath my feet again, but this time, it's not just from the yaoguai before me. Deep, guttural growls rise from all directions, reverberating through the night air."

    show yaoguai at center_yg with Dissolve(0.2)
    voice audio.yg_scream 
    yg "Raaaaaaaaawwrrrrr!!!"

    "The city of Tianho is under siege."

    hide yaoguai
    show dorian serious at left_char
    show soldier_jiang at right_char
    with Dissolve(0.2)

    voice audio.dorian_ch1_line106
    dorian "Wait, Gao! Jiang! Sound the alarm! Now!"
    voice audio.jiang_ch1_line14
    jiang  "Y-Yes, sir! Gao, come quick!"

    "He grabs Gao by the arm, pulling him toward the bell tower."

    hide soldier_jiang
    hide dorian

    show yaoguai at center_yg with Dissolve(0.2)
    "The yaoguai in front of me snarls, its molten eyes locking onto mine. It lunges, claws slicing through the air like scythes. I brace myself, raising my sword, but before its strike can land—."
    "A blinding light erupts from the darkness, illuminating the courtyard as though the sun itself had descended."

    voice audio.toatie_roar_ch1_line3
    yg "Raaaaaaa!!!!"

    "The yaoguai's roar is cut short, replaced by a piercing screech as its monstrous form is enveloped in the radiance. In seconds, its body is reduced to ash, the air filling with the acrid smell of sulfur."
    hide yaoguai
    stop music fadeout 2.0
    scene cg_blindinglight with flash
    "I lower my sword, blinking against the sudden brightness, and as the light fades, a figure steps forward."
    scene bg_tianho_city_on_fire with Dissolve(2.0)
    show vasily neutral at right_char
    show dorian neutral at left_char
    with Dissolve(0.2)

    voice audio.vasily_ch1_line1
    vasily "You must be Dorian. The Dragon of Gale. You're welcome, Paladin."
    voice audio.dorian_ch1_line107
    dorian "I don't think we've met, yet. Who are you?"

    "The man steps closer, his boots clicking against the fractured stone."

    show vasily alt_normal at right_char
    voice audio.vasily_ch1_line2
    vasily "Count Vasily, royal advisor to His Majesty King Gustav of Mjoll."

    "He gives a shallow, calculated bow before rising to meet my gaze. He glances toward the castle, his expression grave."

    show vasily alt_think at right_char
    voice audio.vasily_ch1_line3
    vasily "The King of Mjoll is here. He's inside the castle. I felt his spirit call out to me."

    show dorian serious at left_char
    voice audio.dorian_ch1_line108
    dorian "Olympia — I mean Her Grace called out to me as well."

    "The bell suddenly rings, its sound sharp and frantic."
    "I glance back to see Gao and Jiang pulling the ropes with everything they have."

    show vasily alt_aggressive at right_char
    voice audio.vasily_ch1_line4
    vasily "We haven't a moment to lose. The castle is under siege, and the forces within are far beyond what you've seen here."
    "He gestures toward the castle gates, his eyes narrowing."
    voice audio.vasily_ch1_line5
    vasily "Come, Dorian. If we delay, there may be nothing left to save."

    hide vasily
    hide dorian
    with Dissolve(0.1)

    "I nod and we sprint towards the castle."

    # -------------------------------------------------------------------------
    # INSIDE THE CASTLE — Vasily and Dorian fight yaoguai together
    # BG: bg_tianho_city_on_fire
    # ADDED LATER: From PDF p43-46
    # -------------------------------------------------------------------------

    scene bg_tianho_city_on_fire with shock_cut  # PLACEHOLDER — castle interior, blood everywhere

    "The moment we stepped into the castle, the metallic stench of blood hits like a tidal wave. The grand halls, once symbols of Tianho's majesty, are now painted red."
    "Bodies of guards, attendants, and clerics lie strewn across the floor, their lifeless eyes staring blankly into the void."
    "Broken spears, shattered shields, and torn banners scatter the area."

    show dorian dragon_eyes at left_char
    with Dissolve(0.2)
    voice audio.dorian_ch1_line109
    dorian "Tetrad above…"

    "I hear a guttural snarl, and my gaze snaps to the end of the hall. Two yaoguai stand there, their claws dripping with fresh blood, their glowing red eyes locked on us. They charge."

    show yaoguai at right_yg with Dissolve(0.2)
    play music audio.ost_battle 
    voice audio.yg_scream 
    yg "Raaaaaaawwrrr!!!"
    play music audio.ost_battle
    $ renpy.save("quick-1")

    # =====================================================================
    # D6 — TIMED QTC: Castle Interior (2 options)
    # =====================================================================

    $ _choice_timeout = 5.0
    menu:
        "Freeze up and do nothing.":
            $ _choice_timeout = 0
            $ ch1_castle_qtc = "freeze"

            show dorian normal_alt_tense at left_char
            "I tense up, my nerves getting the best of me after seeing all of those bodies piled up. Count Vasily steps forward."

            hide dorian
            show vasily alt_mad at left_char with Dissolve(0.2)
            "Raising a hand, a brilliant burst of light erupts from his palm, enveloping the yaoguai in a searing glow. Their screeches fill the air as their bodies disintegrate into ash the light burning away their monstrous forms in seconds."
            scene cg_blindinglight with flash
            scene bg_tianho_city_on_fire with Dissolve(1.0)
            hide yaoguai
            show vasily alt_aggressive at right_char with Dissolve(0.2)
            voice audio.vasily_ch1_line6
            vasily "Focus, Paladin. I can handle this, but you're not here to stand idle."
            show vasily alt_normal at right_char
            show dorian sad at left_char
            voice audio.dorian_ch1_line110
            dorian "I apologize. I just…"

            show vasily alt_think at right_char
            voice audio.vasily_ch1_line7
            vasily "I understand. But we might become one of them if we don't stay alert."

        "Use your earth channeling powers.":
            $ _choice_timeout = 0
            $ ch1_castle_qtc = "spikes"

            # play sound sfx_stone_spike          # PLACEHOLDER — stone spike SFX
            hide yaoguai
            show dorian dragon_eyes at left_char
            with Dissolve(0.2)

            show yaoguai at right_yg with Dissolve(0.2)
            play sound audio.sfx_earth
            "I slam my hand to the ground, channeling the raw power of the earth beneath me. Jagged spikes of stone erupt from the floor with a deafening crack, impaling the yaoguai before they can take another step."

            voice audio.toatie_roar_ch1_line3
            yg "Raaaaaaa!!!!"
            hide yaoguai with Dissolve(0.2)
            play sound audio.sfx_body_thud
            "Their bodies twitch once before falling limp, pinned like broken marionettes."

            show vasily neutral at right_char with Dissolve(0.2)
            voice audio.vasily_ch1_line8
            vasily "Impressive. Fire channeling, Earth channeling and, if I'm not mistaken, wind as well. The stories about you aren't just legend, it seems."

            show dorian normal at left_char
            voice audio.dorian_ch1_line111
            dorian "Thanks. I was just born with this. Nothing special."

    # --- Post-QTC: both branches converge here ---

    show vasily alt_aggressive at right_char
    show dorian serious at left_char
    "Before I can catch my breath, a third yaoguai lunges from the shadows, its claws aimed for Vasily."
    "But he's faster."

    show vasily alt_savage at right_char
    voice audio.vasily_ch1_line9
    vasily "Enough."

    "Vasily steps forward, his hand glowing with light. His light pierces through the yaoguai, frying the creature instantly."
    scene cg_blindinglight with flash
    scene bg_tianho_city_on_fire with Dissolve(1.0)
    "We stand amidst the silence, our breaths heavy. Our eyes won't leave the lifeless bodies surrounding us."

    show dorian angry at left_char
    show vasily alt_normal at right_char
    with Dissolve(0.2)
    voice audio.dorian_ch1_line112
    dorian "This… this isn't an attack. It's a slaughter."

    show vasily alt_think at right_char
    voice audio.vasily_ch1_line10
    vasily "If the yaoguai made it this far… the throne room—"

    show bg_tianho_throne with fade
    "Ahead of us, a door creaks, its sound cutting through the silence like a knife. It swings open fully, revealing a stone stairway that spirals downward into the depths of the castle. Faint, ominous red light glows from below, flickering like firelight."

    show vasily alt_think at right_char
    show dorian serious at left_char
    with Dissolve(0.2)

    voice audio.vasily_ch1_line11
    vasily "It… might be a trap."
    "I grip the hilt of my sword tighter, stepping forward."

    show vasily alt_aggressive at right_char

    voice audio.vasily_ch1_line12
    vasily "Wait. We don't know what's down there."

    show dorian dragon_eyes at left_char
    voice audio.dorian_ch1_line113
    dorian "We'll soon find out."

    hide vasily
    hide dorian
    with Dissolve(0.1)

    "I glance back at the hall one last time, at the blood-soaked walls and lifeless bodies, and steel myself for what lies ahead."
    scene bg_underground_dim with fade
    "We descend the spiral stairs, the flickering red light growing brighter with every step. The air is heavy, filled with the stench of sulfur and iron, and each breath feels like inhaling fire."
    "At the bottom, we step into a massive chamber carved into the very foundations of the castle. The ceiling arches high above us."

    # =====================================================================
    # D7 — TIMED QTC: Underground Chamber (wind vs stumble)
    # =====================================================================
    $ renpy.save("quick-1")
    show yaoguai at center_yg with Dissolve(0.2)

    voice audio.toatie_roar_ch1_line3
    yg "Raaaaaaawwrrr!!!"
    hide yaoguai
    show vasily alt_aggressive at right_char
    show dorian serious at left_char
    with Dissolve(0.2)

    $ renpy.save("quick-1")

    voice audio.vasily_ch1_line13
    vasily "Dorian! Look out!"
    play sound sfx_heartbeat loop

    $ _choice_timeout = 5.0
    menu:
        "Use wind channelling.":
            $ _choice_timeout = 0
            $ ch1_stair_qtc = "wind"
            stop sound
            play sound sfx_wind_blast           # PLACEHOLDER — wind blast SFX

            hide vasily
            show dorian dragon_eyes at left_char
            show yaoguai at right_yg with Dissolve(0.2)
            "I thrust my arms forward, summoning the wind with a roar. A sharp gale tears through the room, slamming into the yaoguai with the force of a hurricane. They're thrown backward, smashing into the far wall with bone-cracking force."

            yg "Gaaaahhhh—"
            hide yaoguai with flash

        "Stumble and fall.":
            $ _choice_timeout = 0
            $ ch1_stair_qtc = "stumble"
            $ yuki_tracker += 1                # +1 YUKI tracker
            stop sound

            hide vasily
            show dorian angry at left_char
            voice audio.dorian_ch1_line114
            dorian "Ahhh!"

            "The yaoguai's sudden attack catches me off guard, and I trip on a loose stone, hitting the ground hard."
            scene cg_blindinglight with flash
            "Before they can close in, Vasily steps forward, raising a glowing hand. With a burst of crimson light, one yaoguai disintegrates."
            scene bg_underground_dim with fade
            hide yaoguai
            show vasily alt_aggressive at right_char with Dissolve(0.2)
            voice audio.vasily_ch1_line14
            vasily "Dorian, there's another one!"


            hide yaoguai
            show dorian dragon_eyes at left_char with Dissolve(0.2)
            # add sfx
            "I roll to the side and summon a quick gust of wind to send the second one flying into the wall."

    stop sound
    # bg: tianho underground dim
    scene bg_underground_dim with fade

    show dorian serious at left_char

    "With the yaoguai dealt with, I look around, my heart sinking."
    stop music fadeout 2.0
    show olympia at right_char with Dissolve(0.2)
    "At the far end of the room, Empress Olympia is slumped against the wall, her once-pristine robes soaked in blood."
    "Paladins Cyrus and Feng are crouched beside her, their armor dented and smeared with gore."

    voice audio.dorian_ch1_line115
    dorian "Your Grace!"

    "They look up as I approach."
    hide olympia
    show feng_suit at right_char with Dissolve(0.2)

    "Feng's face is tight with worry, his usual confidence replaced by relief as I approach. Cyrus looks grim, his jaw set like iron."
    feng "Dorian! It's great to see that you're still alive, man."

    show dorian neutral at left_char

    voice audio.dorian_ch1_line116
    dorian "You too, Feng. What happened here?"
    feng "No clue. We were summoned by the Empress."

    show dorian serious at left_char

    voice audio.dorian_ch1_line117
    dorian "Where are the others? The Kyeongjang Emperor? The King of Tianho?"
    "Feng shakes his head, his eyes filled with frustration and shame."

    hide feng_suit
    show cyrus at right_char with Dissolve(0.2)

    voice audio.cyrus_ch1_line30
    cyrus "We couldn't find them. We searched the upper levels and the throne room. It's as if they vanished."

    hide cyrus
    show vasily alt_mad at right_char with Dissolve(0.2)
    voice audio.vasily_ch1_line15
    vasily "Vanished? That's impossible!"
    "He curses under his breath, his frustration palpable."
    voice audio.vasily_ch1_line16
    vasily "Damn it…"

    show vasily alt_aggressive at right_char
    "He spins on his heel and storms toward a shadowy corridor on the far side of the chamber."
    voice audio.vasily_ch1_line17
    vasily "If they're not here, they must've been taken deeper. I'll find them myself if I have to."

    show dorian serious at left_char
    voice audio.dorian_ch1_line118
    dorian "Vasily, wait!"

    hide vasily with Dissolve(0.1)
    "But he's already gone, disappearing into the darkened passage without another word."

    show olympia at right_char with Dissolve(0.2)

    show dorian neutral at left_char

    voice audio.dorian_ch1_line119
    dorian "Your Grace, can you hear me? Everything's going to be alright."
    "I turn back to Olympia, her eyes fluttering open as she struggles to focus on me. Her hand weakly grips my arm, smearing it with blood."

    voice audio.olympia_ch1_line7
    olympia "Tianho… Danger…"

    hide olympia
    show feng_suit at right_char with Dissolve(0.2)
    feng "We need to get her out of here. She's lost too much blood."
    show dorian serious at left_char
    voice audio.dorian_ch1_line120
    dorian  "Feng, Cyrus — we need a plan. And fast."

    hide feng_suit
    show cyrus at right_char with Dissolve(0.2)

    voice audio.cyrus_ch1_line31
    cyrus "There might be a doctor here who can—"

    # add shaking effect
    "The ground beneath us begins to tremble. Then, the entire castle shakes violently, dust and debris raining down from the ceiling."

    show cyrus at right_char
    voice audio.cyrus_ch1_line32
    cyrus "The castle's collapsing! We need to get out — NOW!"
    hide cyrus
    show feng_suit at right_char with Dissolve(0.2)
    feng  "In Tetrad's name… What is going on here?!"

    hide feng_suit

    "I glance toward the corridor Vasily disappeared into. There's no time to go after him."
    "Cyrus throws Olympia over his shoulder, her weak protests drowned out by the growing roar of the earthquake. I grab Feng by the arm, and we all sprint toward the stairs we came down from."

    show dorian serious at left_char with Dissolve(0.2)

    voice audio.dorian_ch1_line121
    dorian "Come on, man. Hurry up!"

    hide dorian

    scene bg_tianho_city_on_fire with shock_cut  # PLACEHOLDER — city on fire, courtyard

    # play music ost_battle_tianho fadein 1.0

    "Finally, we burst out into the courtyard, gasping for air."
    "The city of Tianho is in chaos. Streets are lit by the glow of fires, their smoke curling into the night sky. People are screaming, running in every direction. Buildings collapse in the distance, their foundations giving way as the earth continues to quake."

    voice man1_ch1_line4
    man_1 "Wait… Look… Up in the sky!"

    "And then, the most chilling sight of all—a massive, winged shadow looms atop the highest spire of Castle Tianho. Its form is obscured by the darkness."

    woman_1 "It… It's the death god!"
    man_2 "W-We're all doomed!"

    # scene cg_winged_god_appears with shock_cut  # PLACEHOLDER — cg_winged_god_appears
    # pause 1.5
    # scene bg_tianho_city_on_fire with dissolve

    "It fires a red beam towards the castle. The ancient structure groans in protest. Parts of it falling off."
    "As the castle collapses, a shockwave ripples outward, sending dust and debris flying into the air. The ground beneath our feet trembles again, nearly throwing us off balance."

    show feng_suit at right_char with Dissolve(0.2)

    feng "The castle… It's gone…"

    voice toatie_roar_ch1_line1
    "The sound of more yaoguais roaring echo eerily through the chaos as the ground beneath Tianho begins to crack open. The air grows hotter, thick with sulfur, and an ominous red glow spills through the fissures."

    show dorian angry at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line122
    dorian "What in the Tetrad's name…?"

    hide dorian
    hide feng_suit

    "The earth erupts in fury. Flames and molten rock burst from the ground, and the distant peaks of volcanoes surrounding Tianho belch columns of fire and ash into the darkened sky."
    scene tianho_food_stalls_fire with shock_cut
    man_3 "It… It's erupting! The volcanoes under Tianho are erupting!"

    show soldier_gao at right_char
    show soldier_jiang at left_char
    with Dissolve(0.2)

    "From the watchtower, I spot Gao and Jiang, their faces pale. I shout to them, my voice cutting through the panic."

    hide soldier_jiang
    show dorian serious at left_char
    with Dissolve(0.2)

    voice audio.dorian_ch1_line123
    dorian "Gao! Jiang! RUN! Evacuate as many civilians as you can! That's an order!"
    voice audio.gao_ch1_line17
    gao "Y-Yes, sir!"

    hide soldier_gao
    hide soldier_jiang

    "I turn to Paladin Feng."

    show feng_suit at right_char
    with Dissolve(0.2)

    voice audio.dorian_ch1_line124
    dorian "Feng, we need to help them evacuate! The city will burn if we don't act now!"
    feng  "On it. I'll clear the streets and rally anyone who can still fight."
    hide feng_suit
    show cyrus at right_char
    with Dissolve(0.2)

    voice audio.dorian_ch1_line125
    dorian "Cyrus, what about you?"

    voice audio.cyrus_ch1_line33
    cyrus "Dorian, you evacuate the city. I'll deal with the winged monster."

    show dorian serious at left_char

    voice audio.dorian_ch1_line126
    dorian "Cyrus, you can't—"

    voice audio.cyrus_ch1_line34
    cyrus "Listen to me. This city still needs a future, and that future doesn't happen unless someone stops that thing."

    "He tightens his grip on his sword, a rare softness in his gaze as he meets my eyes."

    voice audio.cyrus_ch1_line35
    cyrus "Protect the people, Dorian. That's your duty now."

    hide cyrus
    hide dorian

    "Before I can argue, Cyrus charges toward the ruins of the castle, his figure soon swallowed by the smoke and flames."

    show feng_suit at right_char
    show dorian serious at left_char
    with Dissolve(0.2)

    feng "Let's go, Dorian! We—"

    hide feng_suit
    hide dorian

    "The ground beneath us splits once more, sending a fresh wave of heat and ash into the air. Then, a deafening roar cuts through the screams and crackling flames."
    "A monstrous Taotie, its grotesque form towering above the crumbling city, emerges from the fiery chasm. Its gaping maw seems endless, filled with jagged teeth dripping molten saliva."

    scene bg_tianho_city_on_fire with dissolve
    # play music ost_taotie_battle fadein 1.0     # PLACEHOLDER — Taotie battle OST

    show taotie at center_tt with Dissolve(0.2)
    voice audio.toatie_roar_ch1_line3
    taotie "GRAAAWWRRRR!!"

    hide taotie
    show dorian angry at left_char with Dissolve(0.2)

    voice audio.dorian_ch1_line127
    dorian "Tetrad above… What the—"

    show feng_suit at right_char with Dissolve(0.2)

    "Paladin Feng steps forward, unwavering, his sword burning with blue fire."
    feng "Dorian, get the civilians out! I'll handle this beast!"

    show dorian serious at left_char
    voice audio.dorian_ch1_line128
    dorian "Feng, wait! We can't take this thing alone!"
    hide dorian with Dissolve(0.1)

    "But Feng doesn't listen. With a battle cry, he charges toward the Taotie, leaping high and slashing at its massive head."
    # blade sfx and meat searing
    "His blade slices across one of its glowing eyes, the blue fire searing into its flesh. The Taotie roars in pain, its head snapping back as it reels from the attack."
    play sound audio.sfx_claw
    "But it's not enough. The beast retaliates with a vicious swipe of its massive claws, faster than Feng can react."

    show dorian angry at left_char with Dissolve(0.2)

    voice audio.dorian_ch1_line129
    dorian "FENG, LOOK OUT!"

    hide dorian
    hide feng_suit

    scene cg_feng_eye_injury with shock_cut     # PLACEHOLDER — cg_feng_eye_injury
    pause 0.5
    voice audio.toatie_roar_ch1_line3
    taotie "GRAAAWWRRRR!!"

    "The claws rake across his face, sending him flying backward. He crashes into the ground, rolling to a stop near me. Blood gushes from deep, savage gashes across his eyes, the blue fire extinguished from his blade as it clatters to the ground."

    feng "ARGGGHHHH!!!!"
    scene bg_tianho_city_on_fire with shock_cut
    show dorian angry at left_char with Dissolve(0.2)

    $ renpy.save("quick-1")
    voice audio.dorian_ch1_line130
    dorian "NO!! FENG!!"

    show taotie at right_tt with Dissolve(0.2)
    voice audio.toatie_roar_ch1_line1
    "The Taotie roars again, shaking the ground beneath us. I glance up, my heart pounding. The creature is already advancing, its massive jaws snapping at the air."
    "I think of rushing towards his aid, but somehow I need to kill this creature first."

    voice audio.toatie_roar_ch1_line3
    taotie "GRAAAWWRRRR!!"
    show dorian dragon_eyes at left_char
    "The Taotie lunges forward, its gaping maw threatening to devour me whole. I only have a moment to act."
    # play sound sfx_heartbeat loop

    # =====================================================================
    # D8 — TIMED QTC: Dodge or Stumble (HARD GATE)
    # =====================================================================
    $ _choice_timeout = 5.0
    menu:
        "Dodge to the left.":
            $ _choice_timeout = 0
            stop sound
            "I roll just in time, the Taotie's jaws snapping shut inches from my face. Its momentum causes it to crash into a nearby building, buying me precious seconds."
            "Its rancid breath washes over me, nearly making me gag."
            "I spot Feng lying nearby, motionless, his blood pooling beneath him. My chest tightens, but I force myself to focus."

        "Stumble.":
            $ _choice_timeout = 0
            stop sound
            "I try to dodge, but my footing slips on the rubble beneath me. I fall hard onto my side, the impact knocking the wind out of me."
            voice audio.toatie_roar_ch1_line3
            taotie "GRAAAWWRRRR!!"

            voice audio.dorian_ch1_line131
            dorian "AAHHHH!!!"
            hide dorian
            hide taotie
            show feng_suit at right_char with Dissolve(0.2)
            feng "DORIAN!!"
            hide feng_suit
            show olympia at right_char with Dissolve(0.2)
            voice audio.olympia_ch1_line8
            olympia "PALADIN! NO!"
            hide olympia
            scene black with shock_cut
            jump game_over

    # play sound sfx_heartbeat loop     # PLACEHOLDER — sfx_heartbeat

    # =====================================================================
    # D9 — TIMED QTC: Shut mouth or Run (HARD GATE)
    # =====================================================================

    # show taotie at right_tt with Dissolve(0.2)
    voice audio.toatie_roar_ch1_line1
    taotie "GRAAAWWRRRR!!!"
    "The Taotie opens its maw wide, preparing to unleash a devastating roar that shakes the ground."

    $ renpy.save("quick-1")
    $ _choice_timeout = 5.0
    menu:
        "Channel wind to force its mouth shut.":
            $ _choice_timeout = 0
            stop sound
            play sound sfx_wind_blast           # PLACEHOLDER

            "I focus my energy, summoning a powerful gust of wind that slams into the Taotie's gaping maw. The force is enough to snap its jaws shut with a thunderous clang, cutting off the ear-splitting roar."

            voice audio.toatie_roar_ch1_line2
            taotie "Mmmmmmm—"
            voice audio.dorian_ch1_line132
            dorian "Think again, mate."

        "Run toward its flank to avoid the blast.":
            $ _choice_timeout = 0
            stop sound

            "I dash to the side, hoping to avoid the roar. But the Taotie's roar is deafening, its force throwing me into the air like a ragdoll."
            "The ground beneath me erupts, molten lava surging upward. I scream as the searing heat engulfs me."

            dorian "AHHH!!!"
            feng "DORIAN!!"
            voice audio.olympia_ch1_line9
            olympia "PALADIN! NO!"
            scene black with shock_cut
            jump game_over                      # ← HARD GATE: GAME OVER

    # play sound sfx_taotie_lava
    # play sound sfx_heartbeat loop

    # =====================================================================
    # D10 — TIMED QTC: Seal cracks or Run (HARD GATE)
    # =====================================================================
    $ renpy.save("quick-1")
    "The beast stumbles backward, momentarily disoriented. But the reprieve is brief — molten lava begins to bubble and crackle from fissures in the earth."

    # show taotie at right_tt with Dissolve(0.2)
    "It slams its claws into the ground. Fissures spread rapidly."

    $ _choice_timeout = 5.0
    menu:
        "Try to run away.":
            $ _choice_timeout = 0
            stop sound

            show dorian serious at left_char
            "Seeing the molten lava consuming everything, I turn to flee."
            "The ground beneath me erupts violently as molten lava bursts forth, cutting off my escape. The heat is unbearable, and I fall to my knees as the flames consume me."

            hide dorian
            hide taotie
            dorian "AHHH!!!"
            feng "DORIAN!!"
            voice audio.olympia_ch1_line10
            olympia "PALADIN! NO!"

            scene black with shock_cut
            jump game_over                      # ← HARD GATE: GAME OVER

        "Channel earth to seal the cracks.":
            $ _choice_timeout = 0
            stop sound
            # play sound sfx_stone_spike          # PLACEHOLDER — earth sealing SFX

            show dorian dragon_eyes at left_char with Dissolve(0.2)
            "I slam my hands onto the ground, channeling my earth powers with every ounce of strength I have left."
            "The cracks begin to close, the flow of molten lava slowing as the earth seals itself shut. Sweat pours down my face, but I keep pushing until the fissures are completely sealed."
            voice audio.dorian_ch1_line133
            dorian "*pants* Not on my watch."
    stop sound fadeout 1.0
    # All QTCs survived — Olympia delivers the killing blow
    "The Taotie rears back, its monstrous body quaking with fury. Its eyes glow like molten orbs."
    "The ground beneath us trembles as the beast lets out a guttural roar, louder and more furious than before. Lava bursts from its jagged maw, spraying the battlefield with scorching droplets."
    "The Taotie lunges, its massive jaws aiming straight for me. But before it can strike, a sudden burst of wind slams into its side like a battering ram."
    "The beast roars in confusion and stumbles back, teetering precariously on the edge of a deep pit. The wind intensifies, forcing the Taotie to lose its balance."
    "With a final deafening roar, it plummets into the pit below, disappearing into the fiery abyss."

    hide taotie
    voice audio.toatie_roar_ch1_line3
    taotie "GRAAAWWRRRR!!"

    "I whirl around, heart pounding, to see the source of the wind. There stands Empress Olympia, barely upright."

    show olympia at right_char with Dissolve(0.2)
    show dorian serious at left_char
    voice audio.olympia_ch1_line11
    olympia "Are… are you alright, Dorian?"

    "She sways on her feet, the effort clearly too much for her weakened body. Before I can reach her, she collapses again."
    voice audio.dorian_ch1_line134
    dorian "Your Grace!"
    "I rush over, kneeling by her side. She's conscious but barely—her breaths shallow, her face pale."

    show olympia at right_char
    voice audio.olympia_ch1_line12
    olympia "I… I'm fine. *coughs*"
    show dorian normal_alt_calm at left_char
    voice audio.dorian_ch1_line135
    dorian  "You'll be alright. Stay with me!"

    "Before I can process what just happened, movement catches my eye. A group of soldiers rushes toward us, their armor clinking as they surround the scene."
    "One of them kneels by Olympia, while others approach me."

    hide olympia
    show soldier_gao at right_char with Dissolve(0.2)
    male_soldier_1 "Paladin, sir! Soldier Jiang sent us. We'll handle this."
    hide soldier_gao
    show dorian angry at left_char
    voice audio.dorian_ch1_line136
    dorian "FENG!"

    "I dash toward Paladin Feng, who is slumped against a pile of rubble, blood dripping from his face. His eyes are squeezed shut, the blue fire he wielded earlier now extinguished."
    "He groans, his hand instinctively reaching toward his injured eyes. Blood streaks his cheeks, and the sight makes my stomach twist."

    hide dorian
    show feng_suit at right_char with Dissolve(0.2)
    feng "Dorian… I-I'm not out yet. Just help me up."

    "Two more soldiers appear, offering to take Feng to the medics. My chest tightens as I watch them lift him gently, his face contorted in pain."

    hide feng_suit
    show female_guard at right_char with Dissolve(0.2)
    female_guard "We'll take it from here, Paladin. I'm a trained medic."
    hide female_guard
    show feng_suit at right_char with Dissolve(0.2)
    feng "Dorian. Your family."

    "And then it hits me like a thunderclap."

    hide feng_suit
    show dorian dragon_eyes at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line137
    dorian "Elara... Elara and the kids."
    show dorian sad at left_char
    voice audio.dorian_ch1_line138
    dorian "But I can't leave you… Her Grace…"
    show olympia at right_char with Dissolve(0.2)
    voice audio.olympia_ch1_line13
    olympia "We'll be fine, Dorian. Get to your family now. That's an order."

    hide olympia
    show soldier_gao at right_char with Dissolve(0.2)
    male_soldier_2 "You can leave the empress and Paladin Feng to us, Paladin."

    hide soldier_gao
    hide dorian
    jump ch1_common_end


# =============================================================================
# SECTION 15: LABEL GAME_OVER — Shared GAME OVER Screen
# =============================================================================

label game_over:
    scene black with fade
    stop music fadeout 1.0
    stop audio
    pause 1.0
    call screen game_over_screen

# =============================================================================
# SECTION 16: LABEL CH1_COMMON_END — Post-Battle + Yaoguai King Reveal
# =============================================================================
# REWRITTEN from PDF p53-57: Yuxuan rescue scene added. Yaoguai King reveal
# is much more detailed — names each child, Dorian held back by soldiers, dart.
# =============================================================================

label ch1_common_end:

    stop music fadeout 1.0
    play music ost_tragedy fadein 3.0           # PLACEHOLDER — grief OST begins

    scene bg_tianho_city_on_fire with dissolve

    "Without another word, I turn and sprint through the crumbling streets of Tianho."
    "Please, let them be safe. Please, Tetrad, don't take them from me."
    "I sprint through the streets of Tianho, the wails of the injured and the cries of the terrified ring in my ears, drowning out the thunder of my own panicked footsteps."
    "The streets are littered with the bodies of fallen townsfolk, their lifeless eyes staring at nothing. Soldiers and civilians alike run past me, their faces twisted in fear."

    show dorian serious at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line139
    dorian "{i}Please, please let them be safe. Let Elara and the kids be safe.{/i}"

    "As I sprint, my gaze locks onto a building half-consumed by flames. The roof is sagging, embers raining down like hellfire. Faint cries reach my ears through the roaring inferno."

    hide dorian
    show man_3 at right_char with Dissolve(0.2)
    man_3 "Help! Someone, help us!"
    hide man_3

    show yuxuan normal_sad at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch1_line7
    yuxuan "Please, we're trapped! *coughs*"
    hide yuxuan
    voice audio.woman3_ch1_line1
    woman_3 "My baby! My child and I are inside!"

    "I skid to a halt. The doorway is blocked by debris, the flames licking hungrily at the edges. I stretch out a hand, summoning my power."
    "With a forceful motion, I manipulate the earth, shattering the debris blocking the entrance."

    show dorian angry at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line140
    dorian "Go! Now! Get out of here!"

    "Coughing and clutching one another, the mother and her child stumble out, tears streaming down their soot-streaked faces. A man runs out, carrying some clothes with him."
    show dorian serious at left_char
    voice audio.dorian_ch1_line141
    dorian "Are you alright? Run straight and you'll find soldiers who will help you. Now!"

    "The man and woman nod, sobbing their thanks before disappearing into the chaotic streets."
    "A cry pierces the air."

    hide dorian
    show yuxuan normal_sad at right_char with Dissolve(0.2)
    voice audio.yuxuan_ch1_line8
    yuxuan "Ahhh! Help! I'm stuck!"

    "I rush back to the entrance, finding a young man pinned beneath a beam. The flames are already roaring back to life, encroaching dangerously close."

    voice audio.yuxuan_ch1_line9
    yuxuan "The fire! It's too strong— Prosperity Dragon, I'm going to die here like the others! *weeps*"

    "I kneel beside him, gripping his trembling shoulder."

    show dorian serious at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line142
    dorian "Hey! Hey! Look at me."

    "His wide, tear-filled eyes meet mine."

    show yuxuan normal_neutral at right_char
    voice audio.dorian_ch1_line143
    dorian "You're not going to die here. What's your name?"
    voice audio.yuxuan_ch1_line10
    yuxuan "Y-Yuxuan. Cheng Yuxuan."
    show dorian neutral at left_char
    voice audio.dorian_ch1_line144
    dorian "Alright, Yuxuan. I'm Paladin Dorian. On three, I'm going to lift this beam, and you're going to run. Got it?"

    "He nods shakily, his breaths shallow and quick."

    show dorian angry at left_char
    "I grip the beam, summoning strength into my arms."
    voice audio.dorian_ch1_line145
    dorian "One… Two… Three! Run!"

    "I heave the beam aside, flames licking at my boots as Yuxuan scrambles free."
    "Yuxuan hesitates for a moment, his gaze fixed on me with an intensity I can't place, then bolts toward safety."
    "When he reaches a safe distance, he turns back, his voice trembling but filled with emotion."

    show dorian serious at left_char
    show yuxuan alt_mid_close_eyes at right_char
    voice audio.yuxuan_ch1_line11
    yuxuan "You… You saved me. I…"
    voice audio.yuxuan_ch1_line12
    yuxuan "P-Paladin D-Dorian, right?"
    show dorian neutral at left_char
    voice audio.dorian_ch1_line146
    dorian "Don't mention it, Yuxuan. I want you to run. Head straight and you'll find soldiers who will help you. Hurry!"
    show yuxuan alt_smile at right_char
    voice audio.yuxuan_ch1_line13
    yuxuan "T-Thank you for saving me…"

    "I give him a quick nod, urgency pulling me back to my original mission. Elara, the kids... hold on."
    "As I sprint away, I feel Yuxuan's gaze lingering."

    hide yuxuan
    hide dorian
    stop music
    # TODO: LAVA SFX
    "Soon, the inn comes into view, but my heart plummets as I see the hellscape before me."
    "The building where my family rested is now submerged in molten lava, its structure reduced to ash and smoldering debris."

    "No…"
    "No…"
    stop music fadeout 1.0

    show yk at left_char, silhouette with Dissolve(1.5)
    "Standing in the center of the destruction is a massive figure, nearly twice the height of a man. Its body is grotesque — hulking and sinewy, its skin a mottled mix of black and crimson, with molten veins pulsing across its form."
    "Its claws drip with blood, and its eyes glow like twin embers. Horns twist from its head, curling like a jagged crown, and its gaping maw splits into a sinister grin."
    show yk at left_char, silhouette_reveal with Dissolve(1.5)
    "This is no ordinary yaoguai. This is a Yaoguai King — a lord of their kind, radiating a dark, oppressive aura that makes the air feel heavy."
    "In its clawed hand, it holds something small and pale."

    pause 1.0

    "My stomach drops as I realize what it is."

    scene cg_elara_children_death with fade     # PLACEHOLDER — cg_elara_children_death
    pause 3.0
    scene cg_black with fade

    pause 1.5
    scene bg_tianho_city_on_fire with fade
    show dorian angry at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line147
    dorian "ELARA! ELARA NO!"

    "The yaoguai king throws its head back and laughs, a deep, guttural sound that shakes the ground."

    show yk at right_char with Dissolve(0.2)
    yk "Such fragile creatures… humans. So soft. So full of fear."
    voice audio.yk_ch1_line3
    yk "I've searched through fire and blood for you, Dragonkin. At last, I've found you."

    "It raises Elara's severed head higher, as if to taunt me."

    voice audio.yk_ch1_line4
    yk "You're looking for this, aren't you?"
    show dorian sad at left_char
    voice audio.dorian_ch1_line148
    dorian "No… No…"
    voice audio.yk_ch1_line2
    yk "She begged for you. Cried your name with her last breath. Where were you, Paladin?"
    show dorian angry at left_char
    voice audio.dorian_ch1_line149
    dorian "YOU MONSTER! WHAT HAVE YOU DONE TO HER? TO MY KIDS?"

    "He opens his other clawed hand — bloodied objects slip through his fingers. I recognize them."
    "Sarah's drawing book. Daniel's sash."

    voice audio.yk_ch1_line5
    yk "The little ones screamed louder than she did."
    voice audio.yk_ch1_line6
    yk "I feasted on their fear. On their hope. Hope in their tiny voices. Such belief that you would come."
    voice audio.yk_ch1_line7
    yk "When they broke down and cried — I saved the last scream for you."

    show dorian sad at left_char
    voice audio.dorian_ch1_line150
    dorian "Emily… Daniel… Sarah… Lucas…"

    voice audio.yk_ch1_line8
    yk "You should have heard Emily. Her voice cracked when she cried for you… Oh, and Lucas…"

    "The words barely register. My world is spinning, collapsing in on itself. My knees hit the ground as a scream tears from my throat."

    show dorian dragon_eyes at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line151
    dorian "I'LL KILL YOU! I'LL KILL YOU! I SWEAR BY THE TETRAD'S NAME, I'LL RIP YOU APART!"

    "I try to rush forward, to throw myself at the yaoguai king, but strong hands grab my shoulders."
    hide dorian
    show soldier_gao at left_char with Dissolve(0.2)
    voice audio.gao_ch1_line18
    gao "Paladin, no! You can't! We have to go, now!"
    hide soldier_gao
    show soldier_jiang at left_char with Dissolve(0.2)
    voice audio.jiang_ch1_line15
    jiang "Paladin, please! He's just baiting you!"
    hide soldier_jiang
    show dorian dragon_eyes at left_char with Dissolve(0.2)
    "I thrash against them, roaring, but more soldiers appear, holding me back. I can feel flames coming out of my eyes."
    voice audio.dorian_ch1_line152
    dorian "LET ME GO! I'LL KILL HIM! LET ME GO!"

    show yk at right_char with Dissolve(0.2)
    yk "YES! YES! HAHAHA! That's it! Cry! Rage! Let your soul split open!"
    voice audio.yk_ch1_line10
    yk "Burn for me! Show me what grief can do to a god-touched soul!"

    hide dorian
    show soldier_jiang at left_char with Dissolve(0.2)
    voice audio.jiang_ch1_line16
    jiang "Gao! Do something!"
    hide soldier_jiang
    show soldier_gao at left_char with Dissolve(0.2)
    voice audio.gao_ch1_line19
    gao "Ok! Ok!"
    voice audio.gao_ch1_line20
    gao "I'm sorry, Paladin. This is for your own good."
    hide soldier_gao
    show dorian dragon_eyes at left_char with Dissolve(0.2)
    voice audio.dorian_ch1_line153
    dorian "I'LL HUNT YOU DOWN TO THE ENDS OF THE EARTH YOU FIEND! THEN I—"
    hide dorian
    show soldier_jiang at left_char with Dissolve(0.2)
    voice audio.jiang_ch1_line17
    jiang "Do it!! Now!!"
    hide soldier_jiang

    show dorian dragon_eyes at left_char with Dissolve(0.2)
    "I barely notice the glint of metal in his hand until it's too late."
    show dorian sad at left_char with Dissolve(0.2)
    "The sharp sting of the dart pierces my neck, and a wave of numbness washes over me."

    hide dorian
    hide yk
    scene black with fade
    stop audio fadeout 1.0

    voice audio.dorian_ch1_line154
    dorian "No… Elara…"

    "My body grows heavy, my vision blurring as I slump to the ground. The last thing I hear is the yaoguai king's laughter."

    yk "Come find me, dragonkin… But remember this… no matter how fast you chase me… you'll never outrun what I've taken from you."

    "Then, Elara's voice… and the kids' laughter."

    hide dorian
    voice audio.elara_ch1_line68
    elara "I love you, my heart…"
    voice audio.dorian_ch1_line155
    dorian "E…lara…"

    hide dorian
    pause 2.0

    "And then — darkness."

    # -------------------------------------------------------------------------
    # END OF CHAPTER 1 — Chapter Title Card + Transition
    # -------------------------------------------------------------------------

    show text "CHAPTER 1 - FINISHED" at truecenter with dissolve
    pause 2.5
    hide text with dissolve

    jump chapter_2

# =============================================================================
# END OF CHAPTER 1
# =============================================================================