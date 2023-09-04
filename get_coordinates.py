from typing import NamedTuple
import geocoder


class Coordinates(NamedTuple):
    """A named tuple representing geographic coordinates."""
    latitude: float     # The latitude coordinate (float)
    longitude: float    # The longitude coordinate (float)


def get_coordinates() -> Coordinates:
    """
    Retrieves approximate current coordinates based on IP address.

    Returns:
        Coordinates: A named tuple representing latitude and longitude.

    Raises:
        Exception: If an error occurs during the process.
    """
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
