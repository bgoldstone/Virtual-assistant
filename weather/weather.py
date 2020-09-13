#Description: Sending requests to The Weather api used in this project


#import modules
import config
from pprint import pprint
import json
import requests

api_url = f"http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={config.api_key}"

#sending the request to the api and collecting informations
response = requests.get(api_url)
data = response.json()

to_find = "weather"

if type(data[to_find]) == list:
    weather_data = data["weather"]
    for i in range(len(weather_data)):
        print(weather_data[i]["main"])
        break


