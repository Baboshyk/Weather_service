from get_coordinates import Coordinates, get_coordinates
from get_weather import get_weather, Weather
from format_weather import format_weather


def main():
    coordinates = get_coordinates()
    weather = get_weather(get_coordinates())
    print(format_weather(weather))
    # print(weather['weather'][0]['main'], weather['weather'][0]['description'])
    # print(weather)


if __name__ == "__main__":
    main()

a = 304.03 - 273.15
# print(str(int(a)) + '°')

