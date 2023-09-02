from get_weather import get_weather, Weather
from get_coordinates import Coordinates, get_coordinates
from get_weather import get_weather


def format_weather(wether: Weather):
    """The function that formats the weather data required for output"""
    pass


def main():
    coordinates = get_coordinates()
    weather = get_weather(get_coordinates())
    # print(format_wether(weather))
    # print(weather['weather'][0]['main'], weather['weather'][0]['description'])
    print(weather)


if __name__ == "__main__":
    main()

a = 304.03 - 273.15
# print(str(int(a)) + '°')

