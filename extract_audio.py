import ffmpeg
import sys

def extract_audio_from_video(video_path, audio_path):
    try:
        (
            ffmpeg
            .input(video_path)
            .output(audio_path, acodec='pcm_s16le', ar='16000', ac='1') # mono, 16kHz, 16-bit PCM WAV
            .run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
        )
        print(f"Audio extracted successfully to {audio_path}")
    except ffmpeg.Error as e:
        print("FFmpeg Error:")
        print(e.stderr.decode('utf8'))
        raise # Re-raise the exception to indicate failure

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_audio.py <input_video_path> <output_audio_path>")
        sys.exit(1)
    
    input_video = sys.argv[1]
    output_audio = sys.argv[2]
    extract_audio_from_video(input_video, output_audio)
