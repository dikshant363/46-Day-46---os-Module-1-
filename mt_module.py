import random

def translate_to_hinglish(text_transcript, source_language="en"):
    """
    Simulates Machine Translation (MT) from a source language (default English) to Hinglish.

    Args:
        text_transcript (str): The input text transcript.
        source_language (str, optional): The source language of the transcript. Defaults to "en".

    Returns:
        str: The "translated" Hinglish string.
    """
    if source_language != "en":
        return "Error: This placeholder only supports English to Hinglish translation."

    # Simple word replacement and injection for Hinglish simulation
    words = text_transcript.split()
    hinglish_words = []
    hindi_fillers = ["yaar", "bhai", "arey", "toh"]
    replacement_map = {
        "is": "hai",
        "a": "ek",
        "of": "ka",
        "the": "yeh",
        "This": "Yeh",
        "It": "Yeh",
        "friend": "dost",
        "and": "aur",
        "audio": "audio", # Keep some words as is
        "transcript": "transcript",
        "engine": "engine"
    }

    for i, word in enumerate(words):
        # Remove punctuation for easier mapping, then re-add if present
        punctuation = ""
        clean_word = word
        if word and word[-1] in [".", ",", "!", "?"]:
            punctuation = word[-1]
            clean_word = word[:-1]

        # Replace word if in map
        translated_word = replacement_map.get(clean_word, clean_word) + punctuation
        hinglish_words.append(translated_word)

        # Occasionally inject a Hindi filler word (e.g., every 3-5 words)
        if (i + 1) % random.randint(3, 5) == 0 and i < len(words) -1: # Avoid adding at the very end
            hinglish_words.append(random.choice(hindi_fillers))

    # Join words and add a general Hinglish marker
    hinglish_transcript = " ".join(hinglish_words)
    # Ensure the last word's punctuation is maintained if the last word was a filler
    if hinglish_words and hinglish_words[-1] in hindi_fillers and words[-1][-1] in [".", ",", "!", "?"]:
         hinglish_transcript += words[-1][-1]


    return hinglish_transcript + " (Hinglish)"

if __name__ == "__main__":
    sample_english_transcript = "This is a dummy transcript of the audio. It simulates the output of a real STT engine."
    
    print("Original English Transcript:")
    print(sample_english_transcript)
    
    hinglish_translation = translate_to_hinglish(sample_english_transcript)
    
    print("\nSimulated Hinglish Translation:")
    print(hinglish_translation)

    sample_english_transcript_2 = "Hello friend, how are you and what are you doing today?"
    print("\nOriginal English Transcript 2:")
    print(sample_english_transcript_2)
    
    hinglish_translation_2 = translate_to_hinglish(sample_english_transcript_2)
    print("\nSimulated Hinglish Translation 2:")
    print(hinglish_translation_2)
