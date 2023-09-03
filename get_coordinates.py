from typing import NamedTuple
import geocoder


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:
    """The function, that returns your current coordinates (approx)"""
    try:
        location = geocoder.ip('me')
        if location.ok:
            lat, long = location.latlng
            return Coordinates(latitude=lat, longitude=long)
        else:
            print(f'Geocoder request failed with status: {location.status_code}')

    except Exception as error:
        print(f'An error occurred: {error}')
