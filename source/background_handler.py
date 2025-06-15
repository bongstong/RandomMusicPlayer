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

    def change_background(self, cover_path: str, operating_sys: int) -> None:
        match operating_sys:
            case 1:
                command: list = [
                    "gsettings",
                    "set",
                    "org.gnome.desktop.background",
                    "picture-uri-dark",
                ]
            case 0:
                command: list = [
                    "reg",
                    "add",
                    "HKEY_CURRENT_USER\\Control Panel\\Desktop",
                    "/v",
                    "Wallpaper",
                    "/t",
                    "REG_SZ",
                    "/d",
                ]
            case _:
                print("Run setup program first")
                quit()
        print("changing background")
        album: str = self.album.replace(" ", "").lower().replace("'", "")
        album_name: str = cover_path + album + ".png"
        command.append(album_name)
        print(self.album)
        run(command)
        print(command)
        return None
