"""program that plays the song, and pseudo-randomly chhooses the song.
Also includes all related features as pausing the song."""

# from pathlib import Path
from random import seed, randint, shuffle
from datetime import datetime
from file_handler import FileHandler
from os import walk, urandom
from subprocess import run


class MusicPlayer:
    """handles application, playing music, fetching random songs
    kwargs: music_pathL str is the path of the mixtape"""

    def __init__(self, music_path: str = "~/Music/") -> None:
        self.path: str = music_path
        self.current_song: str = ""
        self.previous_song: str = ""
        self.transition_songs: dict = FileHandler().transition_songs()
        return None

    def play_with_ffmpeg(self, song: str) -> None:
        run(["killall", "ffplay"])
        run(["ffplay", "-nodisp", "-autoexit", song])
        return None

    def play_random_song(self) -> str:
        """func that plays the song. outputs ths song"""
        print(f"playing: {self.current_song}")
        self.play_with_ffmpeg(self.current_song)
        return self.current_song

    def play_specific_song(self, song: str) -> str:
        """gets song to play as input, obviously"""
        self.play_with_ffmpeg(song)
        return song

    def get_random_song(self, played_songs: list, playls: list = []) -> str:
        """func that get's random song from playlist
        kwargs: played_songs: list is the list of already played songs
        output: randomly selected song"""
        print("getting random song")
        songs: list = list()
        dir: str = ""
        self.current_song: str = ""
        for dir, _, songs in walk(self.path):
            pass
        fmt_songs: list = (
            [dir + "/" + song for song in songs] if playls == [] else playls
        )
        songs: list = [
            song
            for song in fmt_songs
            if song not in played_songs and (
                song not in self.transition_songs.values())
        ]
        shuffle(songs)
        print("SONGS THAT CAN BE PLAYED: ", len(songs))
        seed(self.get_seed())
        index: int = randint(0, len(songs))
        if self.previous_song in self.transition_songs.keys():
            self.current_song: str = self.transition_songs[self.previous_song]
            pass
        else:
            self.current_song: str = songs[index - 1]
        self.previous_song: str = self.current_song
        return self.current_song

    def get_seed(self) -> int:
        """func that get's seed to select random song.
        ouput: int the seed."""
        seed1: int = int(datetime.now().strftime("%f"))
        RAND_SIZE: int = 4
        random_data = urandom(RAND_SIZE)
        random_seed: int = int.from_bytes(random_data, byteorder="big")
        return random_seed * seed1

    def handle_played_music(
        self,
        played_song: str,
        list_of_played_songs: list,
    ) -> list:
        """func that adds current playing song to list of already
        played songs
        kwargs: played_song: str is the currently played song
        list_of_played_songs: list is the list of songs that already played
        output: list of already played songs including the current one"""
        print("adding song to played songs")
        list_of_played_songs.append(played_song)
        return list_of_played_songs
