import requests
from enum import Enum
from typing import NamedTuple
from datetime import datetime
from get_coordinates import Coordinates
from requests.exceptions import RequestException


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

    try:
        api_key = 'e5c8bfde52ec53797a39286f2aa73105'

        if not api_key:
            raise ValueError("API key is missing. Please provide a valid API key.")
        else:
            openwethermap_url = f"http://api.openweathermap.org/data/2.5/weather?lat=" \
                                f"{coordinates.latitude}&lon={coordinates.longitude}&appid={api_key}"

        response = requests.get(openwethermap_url)
        data = response.json()

        if 'cod' in data and data['cod'] != 200:
            message = data.get('message', 'Unknown error')
            raise Exception(f"Error from OpenWeatherMap: {message}")
        else:
            wind_speed = data.get('wind', {}).get('speed', None)
            temperature = data.get('main', {}).get('temp', None)
            weather_main = data.get('weather', [{}])[0].get('main', None)
            weather_description = data.get('weather', [{}])[0].get('description', None)
            sunrise = datetime.utcfromtimestamp(data.get('sys', {}).get('sunrise', 0))
            sunset = datetime.utcfromtimestamp(data.get('sys', {}).get('sunset', 0))
            country = data.get('sys', {}).get('country', None)
            city = data.get('name', None)
            clouds = data.get('clouds', {}).get('all', None)

        return Weather(wind_speed=wind_speed, temperature=temperature,
                       wether_type=weather_main, description=weather_description,
                       sunrise=sunrise, sunset=sunset, country=country, city=city,clouds=clouds)

    except RequestException as e:
        print(f'Request error: {e}')

    except KeyError as e:
        print(f'Error in JSON response: {e}')

    except Exception as e:
        print(f'Unexpected error: {e}')


