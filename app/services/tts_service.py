from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_audio(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )

    with open("narration.mp3", "wb") as f:
        f.write(response.content)

    return "narration.mp3"
