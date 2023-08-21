import requests
import geocoder
from dataclasses import dataclass


def get_goordinates():
    """The function, that returns your current coordinates (approx)"""
    pass

def get_wether(coordinates):
    """The function that sends the current coordinates to the weather service
    "https://openweathermap.org" and returns the current state of the weather in json format"""
    pass


def format_wether(wether):
    """The function that formats the weather data required for output"""
    pass


def main():
    coordinates = get_goordinates()
    wether = get_wether(coordinates)
    print(format_wether(wether))


if __name__ == "__main__":
    main()