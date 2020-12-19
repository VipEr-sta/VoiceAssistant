import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

# __future__ module must be at the top


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        say = ""

        try:
            say = r.recognize_google(audio)
            print(say)
        except Exception as e:
            print("Exception: " + str(e))

    return say


text = get_audio()


def intro_dialogue():
    if "hello" in text:
        speak("hello, how are you")
    elif "what is your name" in text:
        speak("My name is Semtum")
    elif "hey" in text:
        speak("How can I help you?")
    elif "how are you" in text:
        speak("I am doing fine")


def end_dialogue():
    if "Bye" in text:
        speak("Goodbye")
    elif "Goodnight" or "good night" in text:
        speak("Goodnight, don't let the bedybugs bite")


def not_understanable():
    if text != intro_dialogue() or end_dialogue():
        speak("I don't understand")
