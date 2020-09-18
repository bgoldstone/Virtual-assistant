#Description: Sending requests to The Weather api used in this project
import sys
sys.path.insert(0, r'\Python_Projects\Virtual assistant')

#import modules
from weather_data import config
from pprint import pprint
import json
import requests

city = "Paris"

#sending the request to the api and collecting informations
try:
    def get_weather():
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.api_key}"
        response = requests.get(api_url)
        print("[Success]Connection has been established")
        data = response.json()
        
        get_weather.to_find = "weather"
        
        if type(data[get_weather.to_find]) == list:
            weather_data = data["weather"]
            for i in range(len(weather_data)):
                get_weather.final_data = weather_data[i]["main"]
                #print(get_weather.final_data)
                break

        return get_weather.final_data

except:
    print("An anonymous error occured!")







