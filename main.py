from get_coordinates import get_coordinates  # We import the get_coordinates function implemented by us
from get_weather import get_weather          # We Import the get_weather function implemented by us
from format_weather import format_weather    # We import the implemented format_weather function


# The main function of the program, which starts all other functions of our program
def main():
    try:
        # A "coordinate" variable whose value is the result of the get_coordinates function that returns -> Coordinates
        coordinates = get_coordinates()
        # A "weather" variable whose value is the result of a get_weather function that takes a named tuple as input,
        # namely a coordinate variable, and returns -> Weather
        weather = get_weather(coordinates)
        # We output weather data using the format_weather function,
        # which takes the variable "weather" as input and returns a string
        print(format_weather(weather))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

