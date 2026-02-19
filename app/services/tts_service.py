from gtts import gTTS
import os

def generate_audio(text):
    tts = gTTS(text=text, lang="en")
    
    audio_path = "narration.mp3"
    tts.save(audio_path)

    return audio_path
