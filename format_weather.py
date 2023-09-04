from get_weather import Weather


def format_weather(weather: Weather) -> str:
    """
    Formats weather data for display.

    Args:
        weather (Weather): The weather data to format.

    Returns:
        str: The formatted weather information as a string."""

    return (f"{weather.country}, {weather.city}:\n"
            f"{int(weather.temperature - 273.15)}°C, {weather.wether_type}, {weather.description}\n"
            f"Сloudiness: {weather.clouds}%, wind speed: {weather.wind_speed}m/s\n"
            f"Sunrise: {weather.sunrise.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Sunset: {weather.sunset.strftime('%Y-%m-%d %H:%M:%S')}")
