import requests
from enum import Enum
from typing import NamedTuple
from datetime import datetime
from get_coordinates import Coordinates


class WeatherType(Enum):
    CLEAR = 'Clear'
    PARTLY_CLOUDY = 'Partly Cloudy'
    CLOUDY = 'Cloudy'
    OVERCAST_CLOUDY = 'Overcast Cloudy'
    BROKEN_CLOUDS = 'Broken Clouds'
    SCATTERED_CLOUDS = 'Scattered Clouds'
    RAIN = 'Rain'
    HEAVY_RAIN = 'Heavy Rain'
    SHOWERS = 'Showers'
    SNOW = 'Snow'
    HEAVY_SNOW = 'Heavy Snow'
    RAIN_AND_SNOW = 'Rain and Snow'
    HAIL = 'Hail'
    THUNDERSTORM = 'Thunderstorm'
    DUST_OR_SAND_IN_THE_AIR = 'Dust or Sand in the Air'
    FOG = 'Fog'
    MIST = 'Mist'
    DRIZZLE = 'Drizzle'
    LIGHT_RAIN = 'Light Rain'
    MODERATE_RAIN = 'Moderate Rain'
    HEAVY_THUNDERSTORM = 'Heavy Thunderstorm'
    SANDSTORM = 'Sandstorm'
    SMOKE = 'Smoke'
    TORNADO = 'Tornado'
    TROPICAL_STORM = 'Tropical Storm'


class Weather(NamedTuple):
    clouds: str
    description: str
    wind_speed: float
    temperature: float
    wether_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str
    country: str


def get_weather(coordinates: Coordinates) -> Weather:
    """The function that sends the current coordinates to the weather service
    "https://openweathermap.org" and returns the current state of the weather in json format"""

    api_key = 'e5c8bfde52ec53797a39286f2aa73105'

    openwethermap_url = f"http://api.openweathermap.org/data/2.5/weather?lat=" \
                        f"{coordinates.latitude}&lon={coordinates.longitude}&appid={api_key}"

    response = requests.get(openwethermap_url)
    data = response.json()
    """return data"""
    return Weather(wind_speed=data['wind']['speed'],
                   temperature=data['main']['temp'],
                   wether_type=data['weather'][0]['main'],
                   description=data['weather'][0]['description'],
                   sunrise=datetime.utcfromtimestamp(data['sys']['sunrise']),
                   sunset=datetime.utcfromtimestamp(data['sys']['sunset']),
                   country=data['sys']['country'],
                   city=data['name'],
                   clouds=data['clouds']['all'])


