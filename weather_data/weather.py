#Description: Sending requests to The Weather api used in this project
import sys
sys.path.insert(0, r'\Python_Projects\Virtual assistant')

#import modules
from weather_data import config
from pprint import pprint
import json
import requests

city = "London"

#sending the request to the api and collecting informations
try:
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city},uk&appid={config.api_key}"
    response = requests.get(api_url)
    print("[Success]Connection has been established")
    data = response.json()

    to_find = "weather"
    def get_weather(tofind):
        if type(data[tofind]) == list:
            weather_data = data["weather"]
            for i in range(len(weather_data)):
                print(weather_data[i]["main"])
                break

    #get_weather(to_find)
except:
    print("An anonymous error occured!")




