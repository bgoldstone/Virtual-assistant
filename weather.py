#Description: Sending requests to The Weather api used in this project


#import modules
import config
from pprint import pprint
import requests

api_url = f"http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={config.api_key}"

#sending the request to the api and collecting informations
weather_request = requests.get(api_url)
data = weather_request.json()
pprint(data)

