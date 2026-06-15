#Prologue
define kristin     = Character("Kristin",      color="#b0c4de", what_prefix='"', what_suffix='"', callback=name_callback, cb_name="kristin")
define boy_ald     = Character("Boy Aldorith", color="#cd5c5c", what_prefix='"', what_suffix='"', callback=name_callback, cb_name="boy_ald")
define girl_ald    = Character("Girl Aldorith",color="#cd5c5c", what_prefix='"', what_suffix='"', callback=name_callback, cb_name="girl_ald")
define yk          = Character("Yaoguai King", color="#8b0000", what_prefix='"', what_suffix='"', callback=name_callback, cb_name="yk") 
define narrator = Character(None, what_italic=False, callback=name_callback, cb_name=None)

# Chapter 1
define dorian                   = Character("Dorian",               color="#d4af37", callback=name_callback, cb_name="dorian")  # Gold — paladin, protagonist
define elara                    = Character("Elara",                color="#f4a7b9", callback=name_callback, cb_name="elara")  # Soft rose — warm, loving
define lucas                    = Character("Lucas",                color="#87ceeb", callback=name_callback, cb_name="lucas")  # Sky blue — youngest, excited
define sarah                    = Character("Sarah",                color="#dda0dd", callback=name_callback, cb_name="sarah")  # Plum — artistic, quiet
define emily                    = Character("Emily",                color="#f0e68c", callback=name_callback, cb_name="emily")  # Khaki — witty, streetwise
define daniel                   = Character("Daniel",               color="#90ee90", callback=name_callback, cb_name="daniel")  # Light green — cool, sarcastic
define cyrus                    = Character("Paladin Cyrus",        color="#8b0000", callback=name_callback, cb_name="cyrus")  # Dark red — authoritarian
define feng                     = Character("Paladin Feng",         color="#4169e1", callback=name_callback, cb_name="feng")  # Royal blue — loyal, warm
define olympia                  = Character("Empress Olympia",      color="#9370db", callback=name_callback, cb_name="olympia")  # Medium purple — regal
define long_shen                = Character("King Long Shen",       color="#228b22", callback=name_callback, cb_name="long_shen")  # Forest green — Tianho king
define emperor_minjoon          = Character("Emperor Min-joon",     color="#b8860b", callback=name_callback, cb_name="emperor_minjoon") # Dark gold — Kyeongjang
define niko                     = Character("Niko",                 color="#e0c8a0", callback=name_callback, cb_name="niko")  # Warm parchment — healer, devout
define kaito                    = Character("Kaito",                color="#b0d0e0", callback=name_callback, cb_name="kaito")  # Pale blue — Niko's brother
define yuxuan                   = Character("Cheng Yuxuan",         color="#00ced1", callback=name_callback, cb_name=["supply_robot", "yuxuan"])  # Dark turquoise — inventor
define vasily                   = Character("Count Vasily",         color="#c0c0c0", callback=name_callback, cb_name="vasily")  # Silver — Dorian's commander
define gao                      = Character("Soldier Gao",          color="#a0a0a0", callback=name_callback, cb_name="gao")  # Grey — reliable soldier
define jiang                    = Character("Soldier Jiang",        color="#a0a0a0", callback=name_callback, cb_name="jiang")  # Grey — reliable soldier
define prosperity_dragon        = Character("Prosperity Dragon",    color="#ffd700", callback=name_callback, cb_name="prosperity_dragon") # Bright gold — divine voice
define performers               = Character("Nervous Performer",    color="#ff8c00", callback=name_callback, cb_name="performers") # Orange — festival performers
define vendor                   = Character("Vendor",               color="#cd853f", callback=name_callback, cb_name="vendor")  # Peru — market vendor
define taotie                   = Character("Taotie",               color="#ff0000", callback=name_callback, cb_name="taotie")  # Red, no name — monster sounds
define lead_fire_channeler      = Character("Lead Fire Channeler",  color="#ff4500", callback=name_callback, cb_name="lead_fire_channeler")  # Red-orange — rehearsal leader
define female_guard             = Character("Female Guard",         color="#708090", callback=name_callback, cb_name="female_guard")  # Slate — castle guard
define male_soldier_1           = Character("Soldier",              color="#a0a0a0", callback=name_callback, cb_name="male_soldier_1")  # Grey — generic soldier
define male_soldier_2           = Character("Soldier",              color="#a0a0a0", callback=name_callback, cb_name="male_soldier_2")  # Grey — generic soldier
define woman_1                  = Character("Woman 1",              color="#f4a7b9", callback=name_callback, cb_name="woman_1")  # Rose — desperate audition applicant | NPC
define woman_3                  = Character("Woman 1",              color="#f4a7b9", callback=name_callback, cb_name="woman_3")  # Rose — desperate audition applicant | NPC
define man_1                    = Character("Man 1",                color="#0054ca", callback=name_callback, cb_name="man_1") # NPC
define man_2                    = Character("Man 2",                color="#0054ca", callback=name_callback, cb_name="man_2") # NPC
define man_3                    = Character("Man 3",                color="#0054ca", callback=name_callback, cb_name="man_3") # NPC
define yg                       = Character("Yaoguai",              color="#6c0909", callback=name_callback, cb_name="yg") #Yaoguai beast

# Chapter 2
define svante          = Character("Svante",             color="#9b59b6", callback=name_callback, cb_name="svante")  # Purple — violet-haired aldorith
define king_gustav     = Character("King Gustav",        color="#c0392b", callback=name_callback, cb_name="king_gustav")  # Crimson — hard, imperious
define queen_ekaterina = Character("Queen Ekaterina",    color="#8e44ad", callback=name_callback, cb_name="queen_ekaterina")  # Dark violet — sharp, venomous
define babala          = Character("Babala",             color="#27ae60", callback=name_callback, cb_name="babala")  # Green — earthy, prophetic
define herald          = Character("Herald",             color="#7f8c8d", callback=name_callback, cb_name="herald")  # Grey — ceremonial announcer
define messenger       = Character("Messenger",          color="#7f8c8d", callback=name_callback, cb_name="messenger")  # Grey — palace runner
define mjoll_pavel     = Character("Soldier Pavel",      color="#95a5a6", callback=name_callback, cb_name="mjoll_pavel")  # Light grey — nervous mercenary
define mjoll_helga     = Character("Soldier Helga",      color="#95a5a6", callback=name_callback, cb_name="mjoll_helga")  # Light grey — steady mercenary
define mjoll_lars      = Character("Soldier Lars",       color="#95a5a6", callback=name_callback, cb_name="mjoll_lars")  # Light grey — blunt mercenary
define boy_ald_spa     = Character("Boy Aldorith",       color="#cd5c5c", callback=name_callback, cb_name="boy_ald_spa")  # Muted red — spa child worker
define girl_ald_spa    = Character("Girl Aldorith",      color="#cd5c5c", callback=name_callback, cb_name="girl_ald_spa")  # Muted red — spa child worker
define noblewoman      = Character("Noblewoman",         color="#f39c12", callback=name_callback, cb_name="noblewoman")  # Amber — cruel spa patron
define vendor_mjoll    = Character("Vendor",             color="#cd853f", callback=name_callback, cb_name="vendor_mjoll")  # Peru — Mjollian food vendor
define male_guard      = Character("Male Guard",         color="#7f8c8d", callback=name_callback, cb_name="male_guard")  # Grey — palace guard
define female_guard    = Character("Female Guard",       color="#7f8c8d", callback=name_callback, cb_name="female_guard")  # Grey — palace guard
define frost_oni       = Character("",                   color="#5dade2", callback=name_callback, cb_name="frost_oni")  # Ice blue, no name — monster
define qiongqi         = Character("Qiongqi",            color="#77bbe9", callback=name_callback, cb_name="qiongqi" ) # Chapter 2 intro monster
define supply_robot    = Character("Supply Bot",         color="#17a8be", callback=name_callback, cb_name="supply_robot")
define prophet_1       = Character("Prophet 1",            color="#727477", callback=name_callback, cb_name="prophet_1")
define prophet_2       = Character("Prophet 2",            color="#727477", callback=name_callback, cb_name="prophet_2")

# Chapter 3
define yuki_onna      = Character("Yuki-onna",         color="#aee8f8", callback=name_callback, cb_name="yuki_onna")  # Pale ice blue — spirit form
define ekaterina_ghost= Character("Queen Ekaterina",   color="#d8b4fe", callback=name_callback, cb_name="ekaterina_ghost")  # Soft violet — ghost/vision
define elias          = Character("Elias",             color="#fcd34d", callback=name_callback, cb_name="elias")  # Warm yellow — toddler, innocent
define niko_raven     = Character("Niko",              color="#e0c8a0", callback=name_callback, cb_name="niko_raven")  # Parchment — raven form
define weng           = Character("Miss Weng",         color="#f97316", callback=name_callback, cb_name="weng")  # Orange — Yuxuan's chef/caretaker
define boy_ald_soldier = Character("Boy Aldorith",      color="#cd5c5c", callback=name_callback, cb_name="boy_ald_soldier")  # Muted red — Gustav's soldier
define girl_ald_soldier =Character("Girl Aldorith",     color="#cd5c5c", callback=name_callback, cb_name="girl_ald_soldier")  # Muted red — Gustav's soldier

# Chapter 4
define chung_hee      = Character("Hyon Chung-hee",   color="#a78bfa", callback=name_callback, cb_name="chung_hee")  # Soft violet — deaf-mute Emperor of Kyeongjang
define captain_sunwoo = Character("Captain Sunwoo",    color="#60a5fa", callback=name_callback, cb_name="captain_sunwoo")  # Sky blue — Imperial Guard captain
define ji_hye         = Character("Royal Advisor Ji-hye", color="#f9a8d4", callback=name_callback, cb_name="ji_hye")  # Soft pink — Chung-hee's aunt/advisor
define tian_xun       = Character("Tian Xun",          color="#f97316", callback=name_callback, cb_name="tian_xun")  # Orange — volatile explosives fanatic
define aoi            = Character("Aoi",               color="#67e8f9", callback=name_callback, cb_name="aoi")  # Cyan — cold water channeler from Hinami
define tim            = Character("Tim",               color="#4ade80", callback=name_callback, cb_name="tim")  # Green — green-haired child prodigy
define tedda    = Character("Tedda",                    color="#f94294", callback=name_callback, cb_name="tedda=")  # Warm yellow — animated stuffed bear
define carriage_driver = Character("Carriage Driver",  color="#9ca3af", callback=name_callback, cb_name="carriage_driver")  # Grey — Cheng Industries driver
define prophet        = Character("Prophet",           color="#c4b5fd", callback=name_callback, cb_name="prophet")  # Soft purple — Niko's fellow brother
define courtier_1     = Character("Courtier 1",        color="#d1d5db", callback=name_callback, cb_name="courtier_1")  # Light grey — Kyeongjang courtier
define courtier_2     = Character("Courtier 2",        color="#d1d5db", callback=name_callback, cb_name="courtier_2")  # Light grey — Kyeongjang courtier
define servant        = Character("Servant",           color="#9ca3af", callback=name_callback, cb_name="servant")  # Grey — Kyeongjang servant
define dae_hyun       = Character("Park Dae-hyun",     color="#6b7280", callback=name_callback, cb_name="dae_hyun")  # Grey — Head of Infrastructure

# Chapter 5
define roboto        = Character("Roboto",      color="#22d3ee", callback=name_callback, cb_name="roboto")  # Cyan — Yuxuan's robot companion
define magnus        = Character("Magnus",      color="#fbbf24", callback=name_callback, cb_name="magnus")  # Gold — winged figure in the white void
define seo_yeon      = Character("Empress Seo-yeon", color="#e9d5ff", callback=name_callback, cb_name="seo_yeon") # Soft purple — Chung-hee's mother
define door_voice    = Character("Door",        color="#9ca3af", callback=name_callback, cb_name="door_voice") # door_voice uses a neutral grey — the automated door AI at Yuxuan's lab.

# Chapter 6
define hundun        = Character("",                color="#6b21a8", callback=name_callback, cb_name="hundun")  # Deep purple, no name — chaos monster
define vasily_illusion = Character("Vasily",        color="#c0c0c0", callback=name_callback, cb_name="vasily_illusion")  # Silver — illusion copy of Vasily
define olympia_illusion= Character("Empress Olympia",color="#9370db", callback=name_callback, cb_name="olympia_illusion") # Purple — illusion copy of Olympia
define gustav_illusion = Character("King Gustav",   color="#c0392b", callback=name_callback, cb_name="gustav_illusion")  # Crimson — illusion copy of Gustav
define minjoon_illusion= Character("Emperor Min-joon",color="#93c5fd", callback=name_callback, cb_name="minjoon_illusion")# Light blue — illusion copy of Min-joon
define yaoguai_ch6    = Character("",               color="#6c0909", callback=name_callback, cb_name="yaoguai_ch6")  # Dark red, no name — Yaoguai sounds

# Chapter 7
define woman_2       = Character("Woman 2",      color="#f4a7b9", callback=name_callback, cb_name="woman_2")  # Rose — wounded civilian
define male_soldier_ch7 = Character("Male Soldier", color="#a0a0a0", callback=name_callback, cb_name="male_soldier_ch7") # Grey — young wounded soldier

#Chapter 8
define hwan_sik   = Character("Baek Hwan-sik",  color="#c0c0c0", callback=name_callback, cb_name="hwan_sik")  # Silver — Kyeongjang royal guard, mind-letter voice
define spirit     = Character("Spirit",          color="#ffd700", callback=name_callback, cb_name="spirit")  # Gold — voice of the sealed chamber's spirit
define olympia    = Character("Empress Olympia", color="#9370db", callback=name_callback, cb_name="olympia")  # (reused — illusion in paintings)

# Chapter 9
define huli_jing   = Character("Huli Jing",    color="#f0c040", callback=name_callback, cb_name="huli_jing")  # Amber gold — nine-tailed fox spirit
define fynn        = Character("Fynn",          color="#cd5c5c", callback=name_callback, cb_name="fynn")  # Muted red — the zealot, Mjoll
define katashi     = Character("Katashi",       color="#8b7355", callback=name_callback, cb_name="katashi")  # Earth brown — the fisherman, Hinami
define emi         = Character("Emi",           color="#f9a8d4", callback=name_callback, cb_name="emi")  # Soft pink — Katashi's daughter
define seorin      = Character("Seorin",        color="#a8d8ea", callback=name_callback, cb_name="seorin")  # Pale blue — the alchemist, Kyeongjang
define feng        = Character("Paladin Feng",  color="#ff8c00", callback=name_callback, cb_name="feng")  # Orange — Dorian's best friend, emcee
define soldier_gao = Character("Soldier Gao",   color="#a0a0a0", callback=name_callback, cb_name="soldier_gao")  # Grey — Dorian's old soldier

# Chapter 10
# none