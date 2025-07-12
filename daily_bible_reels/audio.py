# Handles text-to-speech audio generation
from gtts import gTTS

def generate_tts_audio(text, output_path='output/audio.mp3', lang='en'):
    tts = gTTS(text, lang=lang)
    tts.save(output_path)
    return output_path
