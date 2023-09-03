from get_weather import Weather


def format_weather(weather: Weather) -> str:
    """The function that formats the weather data required for output"""
    return (f"{weather.country}, {weather.city}:\n"
            f"{int(weather.temperature - 273.15)}°C, {weather.wether_type}, {weather.description}\n"
            f"Сloudiness: {weather.clouds}%, wind speed: {weather.wind_speed}m/s\n"
            f"Sunrise: {weather.sunrise.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Sunset: {weather.sunset.strftime('%Y-%m-%d %H:%M:%S')}")
