import requests
from pprint import pprint

API_key = "36557acf88b24142156856e1960e9c26"

city = input("Enter your chosen city: ")

#base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+city - this one works too
base_url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_key}&q={city}"

weather_data = requests.get(base_url).json()

pprint(weather_data)
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
