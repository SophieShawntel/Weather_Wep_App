from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Bergen"):

    request_ur = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data =  requests.get(request_ur).json()
    

    return weather_data

if __name__ == "__main__":
    print("\n*** Get Current Weather Condition ***\n")

    city = input("\nPlease enter a city name: ")

    #check for empty strings or stringg with only spaces
    if not bool(city.strip()):
        city = "Bergen"
    
    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)

    
