import requests
from apikey import API_TOKEN

city = input("Please enter your city: ")

params = {"q":  city.capitalize(), "appid": API_TOKEN}

api_url = "https://api.openweathermap.org/data/2.5/weather"
response = requests.get(api_url, params=params)

if response:
    pogoda_json = response.json()
    type_pogoda = pogoda_json["weather"][0]["main"]
    print(f"In {city} now: {type_pogoda}")
else:
    print("Error")
