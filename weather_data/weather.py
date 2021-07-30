# Description: Sending requests to The Weather api used in this project
import sys

sys.path.insert(0, r'\Python_Projects\Virtual assistant')

# import modules
from weather_data import config
from pprint import pprint
import json
import requests

# sending the request to the api and collecting informations
try:
    def get_weather(city, lang, unit):
        api_url = ''
        # gets weather in Celcius of Fahrenheit
        if unit == 'Celsius':
            api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang={lang}&units=metric&appid={config.api_key}"
        elif unit == 'Fahrenheit':
            api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang={lang}&units=imperial&appid={config.api_key}"
        # Kelvin (Default)
        else:
            api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang={lang}&appid={config.api_key}"


        response = requests.get(api_url)
        # print("[Success]Connection has been established")
        data = response.json()
        get_weather.to_find = "weather"
        get_weather.temp = data['main']['temp']
        # print(get_weather.temp)

        if type(data[get_weather.to_find]) == list:
            weather_data = data[get_weather.to_find]
            for i in range(len(weather_data)):
                get_weather.final_data = weather_data[i]["description"]
                # print(get_weather.final_data)
                break

        return get_weather.final_data, get_weather.temp

except:
    print("An unknown error occured!")
