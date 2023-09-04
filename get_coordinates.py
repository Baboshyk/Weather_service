from typing import NamedTuple
import geocoder


# A Coordinates class that inherits from a named tuple
class Coordinates(NamedTuple):
    latitude: float     # Class attribute latitude of get_coordinates.Coordinates latitude: float
    longitude: float    # Class attribute longitude of get_coordinates.Coordinates longitude: float


def get_coordinates() -> Coordinates:
    """The function, that returns your current coordinates (approx)"""
    try:
        location = geocoder.ip('me')     # We determine our relative coordinates by IP address
        if location.ok:                  # Checking the request

            lat, long = location.latlng  # The latlng function returns a list of two elements of type float,
            # the first element is latitude, the second is longitude

            return Coordinates(latitude=lat, longitude=long)  # We return an object of the Coordinates class and
            # assign values of the 'lat' and 'long' variables to its attributes
        else:
            print(f'Geocoder request failed with status: {location.status_code}')

    except Exception as error:
        print(f'An error occurred: {error}')
