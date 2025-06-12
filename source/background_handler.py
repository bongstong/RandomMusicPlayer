from tinytag import TinyTag
from subprocess import run


class BackgroundHandler:
    def __init__(self, current_track: str) -> None:
        self.current_track: str = current_track
        tag: TinyTag = TinyTag.get(self.current_track)
        self.artist: str = str(tag.artist)
        self.album: str = str(tag.album)
        self.title: str = str(tag.title)
        self.duration: str = str(tag.duration)
        pass

    def change_background(self, cover_path: str) -> None:
        print("changing background")
        album: str = self.album.replace(" ", "").lower().replace("'", "")
        album_name: str = cover_path + album + ".png"
        print(album_name)
        run(
            [
                "gsettings",
                "set",
                "org.gnome.desktop.background",
                "picture-uri-dark",
                album_name,
            ]
        )
        print("No file with album name found in the directory")
        return None
