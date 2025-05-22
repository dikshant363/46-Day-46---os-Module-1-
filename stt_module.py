import os

def transcribe_audio(audio_path):
    """
    Simulates Speech-to-Text (STT) processing for an audio file.

    Args:
        audio_path (str): The path to the audio file.

    Returns:
        tuple: A tuple containing:
            - transcript (str): The dummy transcript of the audio.
            - timestamps (list): A list of dictionaries, where each dictionary
                                 represents a word with its start and end times.
    """
    # Check if the audio file exists (optional, but good practice)
    if not os.path.exists(audio_path):
        return "Error: Audio file not found.", []

    # Dummy transcript
    transcript = "This is a dummy transcript of the audio. It simulates the output of a real STT engine."

    # Dummy timestamps
    timestamps = [
        {"word": "This", "start_time": 0.5, "end_time": 0.8},
        {"word": "is", "start_time": 0.9, "end_time": 1.0},
        {"word": "a", "start_time": 1.1, "end_time": 1.2},
        {"word": "dummy", "start_time": 1.3, "end_time": 1.8},
        {"word": "transcript", "start_time": 1.9, "end_time": 2.5},
        {"word": "of", "start_time": 2.6, "end_time": 2.7},
        {"word": "the", "start_time": 2.8, "end_time": 3.0},
        {"word": "audio.", "start_time": 3.1, "end_time": 3.5},
        {"word": "It", "start_time": 3.8, "end_time": 4.0},
        {"word": "simulates", "start_time": 4.1, "end_time": 4.7},
        {"word": "the", "start_time": 4.8, "end_time": 5.0},
        {"word": "output", "start_time": 5.1, "end_time": 5.6},
        {"word": "of", "start_time": 5.7, "end_time": 5.8},
        {"word": "a", "start_time": 5.9, "end_time": 6.0},
        {"word": "real", "start_time": 6.1, "end_time": 6.4},
        {"word": "STT", "start_time": 6.5, "end_time": 6.8},
        {"word": "engine.", "start_time": 6.9, "end_time": 7.5},
    ]

    return transcript, timestamps

if __name__ == "__main__":
    # Assume extracted_audio.wav exists in the current directory or /app
    # For testing purposes, let's ensure a dummy file exists if not run in the full pipeline
    audio_file_path = "/app/extracted_audio.wav"
    if not os.path.exists(audio_file_path):
        # Create a dummy empty file for standalone testing if it doesn't exist
        # In the actual pipeline, this file would be created by the previous step.
        print(f"Warning: Audio file {audio_file_path} not found. Creating a dummy empty file for testing.")
        with open(audio_file_path, 'w') as f:
            pass # Create an empty file

    transcript, timestamps = transcribe_audio(audio_file_path)

    print("Transcript:")
    print(transcript)
    print("\nTimestamps:")
    if timestamps:
        for item in timestamps:
            print(item)
    else:
        print("No timestamps available.")
