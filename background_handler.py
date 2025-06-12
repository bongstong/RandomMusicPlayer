from tinytag import TinyTag
from subprocess import run


class BackgroundHandler:
    def __init__(self, current_track: str) -> None:
        self.current_track: str = current_track
        tag: TinyTag = TinyTag.get(self.current_track)
        self.artist: str = str(tag.artist)
        self.album: str = str(tag.album)
        self.title: str = str(tag.title)
        pass

    def change_background(self, cover_path: str) -> None:
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
        return None
