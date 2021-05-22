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
from Speech import sentences,weather_patterns, greet_patterns, greetings
import datetime
import random




languages = {
    "en":"GB",
    "fr":"FR",
    "es":"ES"
},
supported_languages = ["fr","en","es"]
language = input("Please enter the language you want(fr/en/es): ")

#defining the function for listening through the Mic
#the text based might be removed after being repaced by the UI
def get_inaudio(language):
    #print(f"You have Chosen {language}-{languages[0][language]}")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[Listening...]")
        audio = r.listen(source)
        get_inaudio.said = ""

        try:
            if language in supported_languages:
                get_inaudio.said = r.recognize_google(audio, language=f"{language}-{languages[0][language]}")
                #debugging
                #print(get_inaudio.said)
            else:
                print("Sorry unsupported language yet.")

        except:
            get_inaudio(language)

    return get_inaudio.said #use this variable containing the input data


def speak(text):
    #the audio file is saved then automatically removed to avoid running into errors and avoid to create a new file each time
    if language in supported_languages:
        voice = gTTS(text=text, lang=f"{language}-{languages[0][language]}")
        filename = r"resources\voice.mp3"
        voice.save(filename)
        playsound.playsound(filename)
        os.remove(r"resources\voice.mp3")



#The voice assistant class with the command methods
class Assistant:

    def run_weathercmd(self):
        for pattern in weather_patterns:
            if pattern in get_inaudio.said:
                sys.path.insert(0, r'\Python_Projects\Virtual assistant\weather_data')
                from weather_data import weather
                #speak(sentences[language]['sentence1'])
                speak(sentences[language]['sentence2'])
                get_inaudio(language)
                city = get_inaudio.said
                weather.get_weather(city,language)
                speak(sentences[language]['sentence3']) 
                speak(sentences[language]['sentence4']+weather.get_weather.final_data+sentences[language]['sentence5']+str(weather.get_weather.temp)+sentences[language]['unit'])
                break
            else:
                continue

    def greet(self):
        choice_list = ["1","2","3","4","6"]
        time = datetime.datetime.now().hour
        for pattern in greet_patterns:
            if pattern in get_inaudio.said:
                if language == 'fr':
                    speak(greetings[language][f"{random.randint(1,3)}"])
                elif language == 'en':
                    if time >=12:
                        speak(greetings[language]["pm"][f"{random.randint(1,5)}"])
                        if time.hour > 18:
                            speak(greeting[language]["pm"][f"{random.choice(choice_list)}"])
                    elif time < 12:
                        speak(greetings[language]["am"][f"{random.randint(1,5)}"])
                        




    def run(self):
        print("[INFO]:Running.")
        get_inaudio(language)
        #print(get_inaudio.said.split(" "))
        for word in get_inaudio.said.split(" "):
            if word in greet_patterns:
                self.greet()
                speak(sentences[language]['sentence1'])
            elif word in weather_patterns:
                self.run_weathercmd()
                speak(sentences[language]['sentence6'])
        #recalling the function so it reruns everything
        self.run()
              
                

                
                
         
        


assistant = Assistant()
assistant.run()






