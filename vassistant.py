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

languages = {
    "en":"GB",
    "fr":"FR",
    "es":"ES"
},
supported_languages = ["fr","en","es"]


#defining the function for listening through the Mic
#the text based might be removed after being repaced by the UI
def get_inaudio():
    language = input("Please enter the language you want(fr/en/es): ")
    print(f"You have Chosen {language}-{languages[0][language]}")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[Listening...]")
        audio = r.listen(source)
        get_inaudio.said = ""

        try:
            if language in supported_languages:
                get_inaudio.said = r.recognize_google(audio, language=f"{language}-{languages[0][language]}")
                #debugging
                print(get_inaudio.said)
            else:
                print("Sorry unsupported language yet.")

        except Exception as e:
            print(f"An error occured: {e}")

    return get_inaudio.said #use this variable containing the input data

def speak(text):
    pass



get_inaudio()
patterns = ["weather","forecast","météo","prévisions"]
for pattern in patterns:
    if pattern in (get_inaudio.said):
        sys.path.insert(0, r'\Python_Projects\Virtual assistant\weather_data')
        from weather_data import weather
        weather.get_weather()
        print("you will get weather updates...")
        print(f"The weather is : {weather.get_weather.final_data}")





