"""Description: This is a virtual assistant that receive the voice of a user as input and talk back
what the user want it to say or do as output
Modules to import:
pip install pyaudio
pip install SpeechRecognition
pip install gTTs"""

import datetime
# importing the modules
import os
import random
import sys
import webbrowser
import wikipedia

import playsound
import speech_recognition as sr
from gtts import gTTS  # google text to speech module

from Speech import *

languages = {
                "en": "GB",
                "fr": "FR",
                "es": "ES"
            },
supported_languages = ["fr", "en", "es"]

# supported web applications
supp_web_app = ['youtube', 'gmail', 'twitter', 'instagram', 'facebook']
language = input("Please enter the language you want(fr/en/es): ")


# defining the function for listening through the Mic
# the text based might be removed after being replaced by the UI...some day
def get_inaudio(language):
    # print(f"You have Chosen {language}-{languages[0][language]}")
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print("[Listening...]")
        audio = recognize.listen(source)
        get_inaudio.said = ""

        try:
            if language in supported_languages:
                get_inaudio.said = recognize.recognize_google(audio, language=f"{language}-{languages[0][language]}")
                # debugging
                # print(get_inaudio.said)
            else:
                print("Sorry unsupported language yet.")

        # automatically recall the get_inaudio() if any problem occurs
        except Exception as e:
            get_inaudio(language)

            # getting the logs fo what happened or went wrong
            with open('logs.txt', 'a') as logs:
                logs.write(f'[{datetime.datetime.now()}]: {e}\n')

    return get_inaudio.said.lower  # use this variable containing the input data


def speak(text):
    # the audio file is saved then automatically removed to avoid running into errors and avoid to create a new file
    # each time
    if language in supported_languages:
        voice = gTTS(text=text, lang=f"{language}-{languages[0][language]}")
        filename = r"resources\voice.mp3"
        voice.save(filename)
        playsound.playsound(filename)
        os.remove(r"resources\voice.mp3")


# The voice assistant class with the command methods
class Assistant:

    def run_weathercmd(self):
        for pattern in weather_patterns:
            if pattern in get_inaudio.said:
                sys.path.insert(0, r'\Python_Projects\Virtual assistant\weather_data')
                from weather_data import weather
                # speak(sentences[language]['sentence1'])
                speak(sentences[language]['sentence2'])
                get_inaudio(language)
                city = get_inaudio.said
                # prompt for C/F
                speak(sentences[language]['sentence7'])
                get_inaudio(language)
                metricStandard = get_inaudio.said
                # get weather
                weather.get_weather(city, language, metricStandard)
                speak(sentences[language]['sentence3'])
                # read weather
                speak(sentences[language]['sentence4'] + weather.get_weather.final_data + sentences[language][
                    'sentence5'] + str(weather.get_weather.temp) + sentences[language]['unit'] + metricStandard)
                break
            else:
                continue

    def greet(self):
        choice_list = ["1", "2", "3", "4", "6"]
        time = datetime.datetime.now().hour
        for pattern in greet_patterns:
            if pattern in get_inaudio.said:
                if language == 'fr':
                    speak(greetings[language][f"{random.randint(1, 3)}"])
                elif language == 'en':
                    if time >= 12:
                        speak(greetings[language]["pm"][f"{random.randint(1, 5)}"])
                        if time.hour > 18:
                            speak(greetings[language]["pm"][f"{random.choice(choice_list)}"])
                    elif time < 12:
                        speak(greetings[language]["am"][f"{random.randint(1, 5)}"])

    # function to open an executable using voice command if the .exe file exists
    def open_app(self):
        user_input = get_inaudio.said.lower()
        target_app = user_input.replace("open", "")
        try:
            if target_app in supp_web_app:
                webbrowser.open_new_tab(f"https://www.{target_app}.com")

            else:
                os.popen(f"start {target_app}.exe")
        except Exception as e:
            print('Something went wrong')

            with open('logs.txt', 'a') as logs:
                logs.write(f'[{datetime.datetime.now()}]: {e}\n')

    # function to kill a task using voice command if the .exe file is running
    def kill_app(self):
        try:
            user_input = get_inaudio.said.lower()

            target_app = user_input.replace("shut down", "")
            os.popen(f"TASKKILL /F /IM {target_app}.exe /T")
        except Exception as e:
            with open('logs.txt', 'a') as logs:
                logs.write(f'[{datetime.datetime.now()}]: {e}\n')

    def time(self):
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'This is currently: {time}')

    def run(self):
        get_inaudio(language)

        # initializes wikipedia module to users language
        wikipedia.set_lang(language)

        user_input = get_inaudio.said.lower()
        print(user_input)
        for word in user_input.split(" "):
            if word in quit[language]:
                return
            if word in greet_patterns:
                self.greet()
                # speak(sentences[language]['sentence1'])
            elif word in weather_patterns:
                self.run_weathercmd()
                # speak(sentences[language]['sentence6'])

            elif word == 'open':
                self.open_app()

            elif word == "shut":
                self.kill_app()

            elif word in ask_time:
                self.time()

            # searches wikipedia and reads first 3 sentences of article
            else:
                try:
                    speak(wikipedia.summary(wikipedia.search(user_input)[0], sentences=3))
                except wikipedia.exceptions.PageError:
                    speak('I did not get any search results from wikipedia.')
        # recalling the function so it reruns everything
        self.run()


if __name__ == '__main__':
    assistant = Assistant()
    assistant.run()
