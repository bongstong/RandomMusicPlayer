"""program that handles data about the songs and background changing system
and sends notifications"""

from tinytag import TinyTag
from notifypy import Notify
from os import walk
from subprocess import run


class DataHandler:
    """class that handles information about songs and
    background changing feature and notifications.
    kwargs: current_track: str = current playing song"""

    def __init__(self, current_track: str, path: str = "") -> None:
        try:
            self.current_track: str = current_track
            tag: TinyTag = TinyTag.get(self.current_track)
            self.artist: str = str(tag.artist)
            self.album: str = str(tag.album)
            self.title: str = str(tag.title)
            self.duration: str = str(tag.duration)
            self.album_fmt: str = (
                self.album.replace(" ", "")
                .lower()
                .replace("'", "")
                .replace("&", "and")
                .replace("$", "s")
                .replace(":", "")
            )
            self.cover_path: str = path
        except ValueError:
            pass
        return None

    def change_background(
        self, operating_sys: int, de: int = 1
    ) -> None:
        """function that changes background by calling operating system
        commands
        kwargs: cover_path: str is the path to the album cover images
        operating_sys: int is the operating system, by number. information
        comes from the intel.json file after running setup.py"""
        command: list = []
        album_name: str = self.cover_path + self.album_fmt + ".png"
        match operating_sys:
            case 1:
                match de:
                    case 0:
                        command: list = [
                            "gsettings",
                            "set",
                            "org.gnome.desktop.background",
                            "picture-uri",
                        ]
                    case 1:
                        command: list = [
                            "gsettings",
                            "set",
                            "org.gnome.desktop.background",
                            "picture-uri-dark",
                        ]
                    case 2:
                        command: list = [
                            "swaymsg",
                            "output",
                            '"*"',
                            "bg",
                            f"'{album_name}'",
                            "fill",
                        ]
                        print(self.album)
                        run(command)
                        print(command)
                        return None
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
        command.append(f"'{album_name}'")
        print(self.album)
        run(command)
        print(command)
        return None

    def send_notification(self) -> None:
        icon_path: str = self.cover_path + self.album_fmt + "icon.png"
        print(self.album_fmt)
        print("***"*3)
        print(icon_path)
        notification = Notify()
        notification.title = self.title
        notification.message = f"by {self.artist}, from {self.album}"
        notification.icon = icon_path
        notification.send(block=False)
        return None

    def mixtape_data(self, path: str) -> list:
        """function to get info about all the songs in mixtape
        kwargs: path: str is the  path to the mixtape
        output: list with dicts with all the info about each song
        sorted in order: Artist; Album; Track title"""
        songs: list = list()
        for _, _, songs in walk(path):
            pass

        mix_data: list = list()
        for song in songs:
            song_info: list = list()
            song: str = path + "/" + song
            data_tag: TinyTag = TinyTag.get(song)
            artist: str = str(data_tag.artist)
            album_name: str = str(data_tag.album)
            title: str = str(data_tag.title)

            song_info.append(artist)
            song_info.append(album_name)
            song_info.append(title)
            song_info.append(song)
            mix_data.append(song_info)

        return sorted(mix_data)
