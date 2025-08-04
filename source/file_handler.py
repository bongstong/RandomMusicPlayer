"""program that does all the filesystem work"""
from json import load, dump
from os import walk


class FileHandler:
    """class that handles songs in files, dump and load..."""
    def __init__(self) -> None:
        self.played_songs: list = list()

    def load_song_list(self, filename: str = "played_songs.json") -> list:
        """func that loads songs from JSON file
        kwargs: filename: str is the name of the file to load from
        output: list, content of the file"""
        print("loading info from file")
        output: list = list()
        while output == []:
            try:
                with open(file=filename, mode="r") as file:
                    output: list = load(file)
            except FileNotFoundError:
                with open(file=filename, mode="w") as file:
                    dump([""], file, indent=4)
        return output

    def dump_song_list(
        self,
        played_songs: list,
        filename: str = "played_songs.json",
    ) -> str:
        """func that dumps songs to JSON file
        kwargs: filename: str is the name of the file to dump to
        output: last played song"""
        print("dumping from file")
        with open(file=filename, mode="w") as file:
            dump(played_songs, file, indent=4)
        return played_songs[-1]

    def num_songs(self, path: str) -> int:
        """function that returns total number of songs in mixtape
        kwargs: path: str is the path of the mixtape
        output: int number of songs"""
        for _, _, songs in walk(path):
            return len(songs)
        return 0

    def all_songs(self, path: str) -> list:
        """function that returns total songs in mixtape
        kwargs: path: str is the path of the mixtape
        output: list list songs"""
        for _, _, songs in walk(path):
            return songs
        return []
