from tinytag import TinyTag
from os import walk
from subprocess import run


class DataHandler:
    """class that handles information about songs and
    background changing feature.
    kwargs: current_track: str = current playing song"""

    def __init__(self, current_track: str) -> None:
        try:
            self.current_track: str = current_track
            tag: TinyTag = TinyTag.get(self.current_track)
            self.artist: str = str(tag.artist)
            self.album: str = str(tag.album)
            self.title: str = str(tag.title)
            self.duration: str = str(tag.duration)
        except ValueError:
            pass
        return None

    def change_background(
        self, cover_path: str, operating_sys: int, de: int = 1
    ) -> None:
        """function that changes background by calling operating system
        commands
        kwargs: cover_path: str is the path to the album cover images
        operating_sys: int is the operating system, by number. information
        comes from the intel.json file after running setup.py"""
        match operating_sys:
            case 1:
                if de == 1:
                    command: list = [
                        "gsettings",
                        "set",
                        "org.gnome.desktop.background",
                        "picture-uri",
                    ]
                else:
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
            ls: list = list()
            song: str = path + "/" + song
            data_tag: TinyTag = TinyTag.get(song)
            artist: str = str(data_tag.artist)
            album_name: str = str(data_tag.album)
            title: str = str(data_tag.title)

            ls.append(artist)
            ls.append(album_name)
            ls.append(title)
            ls.append(song)
            mix_data.append(ls)

        return sorted(mix_data)
