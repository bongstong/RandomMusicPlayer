from json import load, dump
from os import walk


class SongHandler:
    def __init__(self) -> None:
        self.played_songs: list = list()

    def load_song_list(self, filename: str = "played_songs.json") -> list:
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
        print("dumping from file")
        with open(file=filename, mode="w") as file:
            dump(played_songs, file, indent=4)
        return played_songs[-1]

    def num_songs(self, path: str) -> int:
        for _, _, songs in walk(path):
            return len(songs)
        return 0
