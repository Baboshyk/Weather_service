from typing import NamedTuple
import geocoder


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:
    """The function, that returns your current coordinates (approx)"""
    try:
        location = geocoder.ip('me')
        lat, long = location.latlng
        return Coordinates(latitude=lat, longitude=long)

    except Exception as error:
        print(f'An error occurred: {error}')
