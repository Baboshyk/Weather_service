from get_coordinates import get_coordinates  # Importing the function to retrieve coordinates
from get_weather import get_weather          # Importing the function to retrieve weather data
from format_weather import format_weather    # Importing the function to format weather data


# The main function of the program, which starts all other functions of our program
def main():
    # Attempt to retrieve coordinates and weather data
    try:
        # A "coordinates" variable whose value is the result of the get_coordinates function.
        # This function returns a Coordinates object.
        coordinates = get_coordinates()
        # A "weather" variable whose value is the result of the get_weather function.
        # This function takes a named tuple (coordinate variable) as input and returns a Weather object.
        weather = get_weather(coordinates)
        # We output weather data using the format_weather function,
        # which takes the variable "weather" as input and returns a string
        print(format_weather(weather))

    # Handle any exceptions and print an error message
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

