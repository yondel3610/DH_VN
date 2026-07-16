import os
import subprocess
from pathlib import Path

def convert_audio_folder(input_folder, output_folder=None, bitrate="128k", samplerate=44100):
    """
    Convert all audio files in a folder to .ogg format.
    Args:
        input_folder: Path to folder containing audio files
        output_folder: Path to output folder (default: input_folder/ogg_output)
        bitrate: Bitrate for output (e.g., "128k", "192k")
        samplerate: Sample rate (e.g., 44100, 48000)
        
    use: Get-Command ffmpeg
    on powershell
    """
    # Set default output folder
    if output_folder is None:
        output_folder = os.path.join(input_folder, "ogg_output")
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Supported input formats
    supported_formats = {'.mp3', '.wav', '.flac', '.m4a', '.aac', '.wma', '.aiff', '.alac'}
    
    # Get all audio files
    audio_files = []
    for ext in supported_formats:
        audio_files.extend(Path(input_folder).glob(f"*{ext}"))
        audio_files.extend(Path(input_folder).glob(f"*{ext.upper()}"))
    
    if not audio_files:
        print(f"No audio files found in {input_folder}")
        return
    
    print(f"Found {len(audio_files)} audio file(s)")
    print(f"Output folder: {output_folder}")
    print("-" * 50)
    
    converted = 0
    failed = []
    
    for audio_file in audio_files:
        input_path = str(audio_file)
        output_path = os.path.join(output_folder, f"{audio_file.stem}.ogg")
        
        # Skip if output already exists
        if os.path.exists(output_path):
            print(f"⏭️  Skipping (already exists): {audio_file.name}")
            continue
        
        try:
            # Build ffmpeg command
            cmd = [
                "ffmpeg",
                "-i", input_path,
                "-c:a", "libvorbis",
                "-b:a", bitrate,
                "-ar", str(samplerate),
                "-y",  # Overwrite output if exists
                output_path
            ]
            
            # Run conversion
            print(f"🔄 Converting: {audio_file.name} -> {audio_file.stem}.ogg")
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            converted += 1
            print(f"✅ Success: {audio_file.stem}.ogg")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed: {audio_file.name}")
            print(f"   Error: {e.stderr}")
            failed.append(audio_file.name)
        except FileNotFoundError:
            print("❌ ffmpeg not found! Please install ffmpeg first.")
            print("   Windows: Download from https://ffmpeg.org/")
            print("   Mac: brew install ffmpeg")
            print("   Linux: sudo apt install ffmpeg")
            return
    
    # Summary
    print("-" * 50)
    print(f"✅ Converted: {converted} file(s)")
    if failed:
        print(f"❌ Failed: {len(failed)} file(s)")
        for f in failed:
            print(f"   - {f}")
    print(f"📁 Output folder: {output_folder}")

# ============================================================
# USAGE
# ============================================================

if __name__ == "__main__":
    # --- Option 1: Convert with default settings ---
    convert_audio_folder("game/audio/sfx and ost/sfx")
    
    # --- Option 2: Convert and specify output folder ---
    # convert_audio_folder("audio/raw", "audio/ogg")
    
    # --- Option 3: Convert with custom bitrate and sample rate ---
    # convert_audio_folder("audio/raw", "audio/ogg", bitrate="192k", samplerate=48000)
    
    # --- Option 4: Convert all subfolders recursively ---
    # for folder in Path("audio").iterdir():
    #     if folder.is_dir():
    #         convert_audio_folder(str(folder))