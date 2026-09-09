init python:

    def get_highest_affection_character():
        # dict order = tie-break priority (first one listed wins ties)
        affections = {
            "niko": A1_niko_affection,
            "svante": A2_svante_affection,
            "yuxuan": A3_yuxuan_affection,
            "chunghee": A4_chunghee_affection,
            "magnus": A5_magnus_affection,
        }
        return max(affections, key=lambda name: affections[name])


label check_affection_route:

    $ highest_character = get_highest_affection_character()

    if highest_character == "niko":
        jump ch9_route_niko        
    elif highest_character == "svante":
        jump ch9_route_svante     
    elif highest_character == "yuxuan":
        jump ch9_route_yuxuan     
    elif highest_character == "chunghee":
        jump ch9_route_chunghee  
    elif highest_character == "magnus":
        jump ch9_route_magnus    