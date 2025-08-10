"""
Program that downloads album covers and modifies them to suit PC background
"""

from subprocess import run
from os import remove, path


class ImageHandler:
    """class that downloads album cover and modifies it
    album_name: str is the name of the album of the song."""

    def __init__(self, artist_name: str, album_name: str, path: str) -> None:
        self.album: str = album_name
        self.artist: str = artist_name
        self.path: str = path
        self.image = f"{self.path}/{self.album.lower().replace(" ", "")}.jpg"
        return None

    def download_cover(self) -> None:
        """downloads the cover using sacad"""
        run(
            [
                "sacad",
                self.artist,
                self.album,
                "1600",
                self.image,
            ]
        )
        if path.exists(self.image) is True:
            print("album cover was found")
            return None
        print("alum cover was not found")
        run(
            [
                "sacad",
                self.artist,
                self.album,
                "1000",
                self.image,
            ]
        )
        if path.exists(self.image) is True:
            print("album cover was found")
        return None

    def blur_and_adjust(self, display_format: int) -> None:
        """blurs and adjusts the cover to fit the screen background
        by bluring it"""
        run(
            [
                "ffmpeg",
                "-y",
                "-i",
                self.image,
                "-lavfi",
                f"[0:v]scale=3840:{display_format}:force_original_aspect_ratio=increase,\
            crop=3840:{display_format},\
            boxblur=40[blurred];\
            [0:v]scale=3840:{display_format}:force_original_aspect_ratio=decrease[orig];\
            [blurred][orig]overlay=(W-w)/2:(H-h)/2",
                f"{self.path}/{self.album.lower().replace(" ", "")}.png",
            ]
        )
        try:
            remove(self.image)
        except FileNotFoundError:
            return None
        return None
