import requests
import geocoder
from typing import NamedTuple
from enum import Enum


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:
    """The function, that returns your current coordinates (approx)"""
    try:
        location = geocoder.ip('me')
        lat, long = location.latlng
        return Coordinates(latitude=lat, longitude=long)

    except Exception as error:
        print(f'An error occurred: {error}')

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



def format_wether(wether):
    """The function that formats the weather data required for output"""
    pass



def main():
    coordinates = get_coordinates()
    wether = get_wether(coordinates)
    # print(format_wether(wether))
    # print(wether)



if __name__ == "__main__":
    main()

a = 304.03 - 273.15

class g():
    gg: int
    ggg: int


def abc(p: g) -> g:
    return g(5, 7)
