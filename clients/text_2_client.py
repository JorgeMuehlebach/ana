from pathlib import Path
from openai import OpenAI


client = OpenAI()
speech_file_path = Path(__file__).parent / "speech.mp3"

# A function that takes in text as input and outputs the audio file
def text_2_speech(text):
    print("attempting to convert text to speech: " + text)
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(speech_file_path)
    return speech_file_path

