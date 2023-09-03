from get_coordinates import get_coordinates
from get_weather import get_weather
from format_weather import format_weather


def main():
    try:
        coordinates = get_coordinates()
        weather = get_weather(coordinates)
        print(format_weather(weather))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

