try:
    import TTS
    import ffmpeg
    print("TTS and ffmpeg-python imported successfully.")
except ImportError as e:
    print(f"Error importing libraries: {e}")
