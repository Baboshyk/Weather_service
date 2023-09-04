import requests
from enum import Enum
from typing import NamedTuple
from datetime import datetime
from get_coordinates import Coordinates
from requests.exceptions import RequestException


class WeatherType(Enum):
    """An enumeration of weather types."""
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
    """
        Represents weather information.

        Attributes:
            clouds (str): The cloudiness description.
            description (str): A detailed weather description.
            wind_speed (float): The wind speed in meters per second.
            temperature (float): The temperature in Kelvin.
            wether_type (WeatherType): The type of weather.
            sunrise (datetime): The time of sunrise.
            sunset (datetime): The time of sunset.
            city (str): The name of the city.
            country (str): The country code.
        """
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
    """
    Retrieves weather information based on provided coordinates.

    Args:
        coordinates (Coordinates): The geographic coordinates.

    Returns:
        Weather: An object containing weather information.

    Raises:
        RequestException: If there is an issue with the HTTP request.
        KeyError: If there is an issue with parsing the JSON response.
        Exception: For any unexpected errors.
    """

    try:
        api_key = 'e5c8bfde52ec53797a39286f2aa73105'  # an API key provided by the weather service to registered users

        if not api_key:  # checking the presence of a key
            raise ValueError("API key is missing. Please provide a valid API key.")
        else:
            # formed bearing, from the received coordinates (latitude and longitude) and our key
            openwethermap_url = f"http://api.openweathermap.org/data/2.5/weather?lat=" \
                                f"{coordinates.latitude}&lon={coordinates.longitude}&appid={api_key}"

        response = requests.get(openwethermap_url)  # sending a request
        data = response.json()                      # the result of the request is converted into JSON format

        # Check the 'cod' key in the response data to verify if the request was successful.
        # If the 'cod' value is not equal to 200, it indicates an error.
        if 'cod' in data and data['cod'] != 200:

            # Retrieve the error message from the response data or use 'Unknown error' if not available.
            message = data.get('message', 'Unknown error')

            # Raise an exception with the error message from OpenWeatherMap.
            raise Exception(f"Error from OpenWeatherMap: {message}")

        # Extract weather data from the response JSON.
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

        # Return a Weather object with values assigned to its attributes.
        return Weather(wind_speed=wind_speed, temperature=temperature,
                       wether_type=weather_main, description=weather_description,
                       sunrise=sunrise, sunset=sunset, country=country, city=city, clouds=clouds)

    # Handle request-related errors.
    except RequestException as e:
        print(f'Request error: {e}')

    # Handle JSON response parsing errors.
    except KeyError as e:
        print(f'Error in JSON response: {e}')

    # Handle unexpected errors.
    except Exception as e:
        print(f'Unexpected error: {e}')


