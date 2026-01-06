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
        self.parsed_album: str = (
            self.album.lower()
            .replace(" ", "")
            .replace("'", "")
            .replace("-", "")
            .replace(":", "")
            .replace("&", "and")
            .replace("$", "s")
            .replace("(", "")
            .replace("[", "")
            .replace("]", "")
            .replace(")", "")
        )
        self.image = f"{self.path}/{self.parsed_album}.jpg"
        return None

    def run_download(self, px: str, is_icon: bool = False) -> None:
        if is_icon:
            filename: str = f"{self.path}/{self.parsed_album}icon.png"
            print("run_download icon")
        else:
            filename: str = self.image
        run(
            [
                "sacad",
                self.artist,
                self.album,
                px,
                filename,
            ]
        )
        return None

    def download_cover(self) -> None:
        """downloads the cover using sacad"""
        self.run_download(px="1600")
        if path.exists(self.image) is True:
            print("album cover was found")
            return None
        print("alum cover was not found")
        self.run_download(px="1000")
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
                f"{self.path}/{self.parsed_album}.png",
            ]
        )
        try:
            remove(self.image)
        except FileNotFoundError:
            return None
        return None
