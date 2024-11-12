# pip install pyttsx3

import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()

