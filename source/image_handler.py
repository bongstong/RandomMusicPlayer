"""
Program that downloads album covers and modifies them to suit PC background
"""

from subprocess import run


class ImageHandler:
    """class that downloads album cover and modifies it
    album_name: str is the name of the album of the song."""

    def __init__(self, artist_name: str, album_name: str, path: str) -> None:
        self.album = album_name
        self.artist = artist_name
        self.covers_path = path
        return None

    def download_cover(self) -> None:
        run(
            [
                "sacad",
                self.artist,
                self.album,
                "1600",
                f"{self.covers_path}/{self.album.lower().strip()}.jpg",
            ]
        )
        return None

    def blur_and_adjust(self) -> None:
        run([
            "ffmpeg",
            "-y",
            "-i",
            f"{self.covers_path}/{self.album.lower().strip()}.jpg",
            "-lavfi",
            "[0:v]scale=3840:2400:force_original_aspect_ratio=increase,\
            crop=3840:2400,\
            boxblur=40[blurred];\
            [0:v]scale=3840:2400:force_original_aspect_ratio=decrease[orig];\
            [blurred][orig]overlay=(W-w)/2:(H-h)/2",
            f"{self.covers_path}/{self.album.lower().strip()}.png",
        ])
        return None


image: ImageHandler = ImageHandler(
    artist_name="Nas",
    album_name="Illmatic",
    path="/home/nathanv/Music/MusicPlayer/source/test",
)
image.download_cover()
image.blur_and_adjust()
