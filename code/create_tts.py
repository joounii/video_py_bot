import pyttsx3

def create_new_tts_file(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 140)
    engine.save_to_file(text, 'assets/sound/tts/test.mp3')
    engine.runAndWait()