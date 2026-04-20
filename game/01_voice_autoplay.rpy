init python:
    # Initialize persistent setting
    if persistent.voice_auto_forward is None:
        persistent.voice_auto_forward = False
    
    # Voice tracking variables
    voice_playing = False
    voice_channel = None
    auto_forward_enabled = False
    
    def get_voice_auto_forward():
        """Check if auto-forward should be active for current line"""
        if not persistent.voice_auto_forward:
            return False
        
        # Check if current line has voice
        current_voice = getattr(renpy.store, 'current_voice', None)
        if current_voice is None:
            # Try alternate method
            try:
                current_voice = renpy.game.script.current_voice
            except:
                pass
        
        has_voice = current_voice is not None and current_voice != ""
        return has_voice
    
    def voice_auto_forward_callback(event, interact=True, **kwargs):
        """Callback to handle auto-forward after voice finishes"""
        global voice_playing, auto_forward_enabled
        
        if event == "begin":
            auto_forward_enabled = get_voice_auto_forward()
            
            if auto_forward_enabled:
                # Get current voice file
                current_voice = getattr(renpy.store, 'current_voice', None)
                if current_voice is None:
                    try:
                        current_voice = renpy.game.script.current_voice
                    except:
                        pass
                
                if current_voice:
                    voice_playing = True
                    renpy.music.play(current_voice, channel="voice", loop=False)
                    global voice_channel
                    voice_channel = renpy.audio.music.get_channel("voice")
        
        elif event == "end":
            # Check if voice finished and should auto-forward
            if auto_forward_enabled and voice_playing:
                # Wait for voice to finish if still playing
                if voice_channel and renpy.music.is_playing(channel="voice"):
                    # Schedule a check for when voice finishes
                    renpy.music.queue_done_callback(
                        lambda: renpy.display.behavior.queue_event("rollforward"),
                        channel="voice"
                    )
            
            voice_playing = False
            auto_forward_enabled = False
    
    # Register callback
    config.character_callback = voice_auto_forward_callback

# Initialize voice channel
init -1:
    $ renpy.music.register_channel("voice", "voice", loop=False, stop_on_mute=True, tight=True)

# Visual indicator for auto-forward mode
screen voice_auto_indicator():
    if persistent.voice_auto_forward and get_voice_auto_forward():
        hbox:
            xalign 1.0
            yalign 0.0
            xoffset -20
            yoffset 10
            
            frame:
                background "#00000080"
                xpadding 10
                ypadding 5
                
                text "▶ AUTO" size 16 color "#88ff88"