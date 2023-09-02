from get_wether import get_wether
from get_coordinates import Coordinates, get_coordinates
from format_wether import format_wether


def main():
    coordinates = get_coordinates()
    wether = get_wether(get_coordinates())
    print(format_wether(wether))


if __name__ == "__main__":
    main()

a = 304.03 - 273.15
