"""
Program that downloads album covers and modifies them to suit PC background
"""

from data_handler import DataHandler


class ImageHandler:
    """class that downloads album cover and modifies it
    album_name: str is the name of the album of the song."""
    def __init__(self, album_name: str) -> None:
        self.album_name = album_name
        return None
