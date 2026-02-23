from json import load, dump


class PlaylistManager:
    def __init__(self, filename) -> None:
        """Adds another playlist. so that from all the solngs in the folder,
        if you want to only listen to your favourite ones, you can select
        the playlist mode, and it will only play those songs."""
        self.filename: str = filename
        self.songs: list = self.load_playlist_songs()
        return None

    def load_playlist_songs(self):
        """gets playlist songs from json file containing list of the songs
        in: filename
        out: list off all the songs"""
        try:
            with open(file=self.filename, mode="r") as file:
                return load(file)
        except FileNotFoundError:
            with open(file=self.filename, mode="w") as file:
                dump([""], file, indent=4)
                return []

    def add_song_to_playlist(self, song: str) -> None:
        """adds singular song to the playlist file
        arg: song = filename of the song"""
        self.songs = self.load_playlist_songs() + [song]
        with open(file=self.filename, mode="w") as file:
            dump(self.songs, file, indent=4)
        return None
