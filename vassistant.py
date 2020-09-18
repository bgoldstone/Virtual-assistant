"""Description: This is a virtual assistant that receive the voice of a user as input and talk back
what the user want it to say or do as output
Modules to import:
pip install pyaudio
pip install SpeechRecognition
pip install gTTs"""

#importing the modules
import os
import sys
import time
import playsound
import speech_recognition as sr
from gtts import gTTS #google text to speach module

sys.path.insert(0, r'\Python_Projects\Virtual assistant')
from weather_data import weather


#defining the function for listening through the Mic
#the text based might be removed after being repaced by the UI
def get_inaudio():
    language = input("Please enter the language you want(fr/en/es): ")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[Listening...]")
        audio = r.listen(source)
        said = ""

        try:
            if language == "en":
                said = r.recognize_google(audio, language="en-GB")
                print(f"You said: {said}")
            elif language == "fr":
                said = r.recognize_google(audio, language="fr-FR")
                print(f"You said: {said}")
            elif language == "es":
                said = r.recognize_google(audio, language="es-ES")
                print(f"You said: {said}")
            else:
                print("Sorry unsupported language yet.")

        except Exception as e:
            print(f"An error occured: {e}")

    return said #use this variable containing the input data

def speak(text):
    pass





