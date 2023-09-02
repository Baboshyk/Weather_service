import requests
from enum import Enum
from get_coordinates import Coordinates


class Wether(Enum):
    pass

def get_wether(coordinates: Coordinates):
    """The function that sends the current coordinates to the weather service
    "https://openweathermap.org" and returns the current state of the weather in json format"""

    api_key = 'e5c8bfde52ec53797a39286f2aa73105'

    openwethermap_url = f"http://api.openweathermap.org/data/2.5/weather?lat=" \
                        f"{coordinates[0]}&lon={coordinates[1]}&appid={api_key}"

    response = requests.get(openwethermap_url)
    data = response.json()
    return data

