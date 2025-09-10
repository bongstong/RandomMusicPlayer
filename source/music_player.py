"""program that plays the song, and pseudo-randomly chhooses the song.
Also includes all related features as pausing the song."""

from random import seed, randint, shuffle
from datetime import datetime
from pathlib import Path
from os import walk, urandom
from subprocess import run


class MusicPlayer:
    """handles application, playing music, fetching random songs
    kwargs: music_pathL str is the path of the mixtape"""

    def __init__(self, music_path: str = "~/Music/") -> None:
        self.path: str = music_path
        self.current_song: str = ""
        return None

    def play_random_song(self, visual_check: bool = False) -> str:
        """func that plays the song. outputs ths song"""
        print(f"playing: {self.current_song}")
        match visual_check:
            case False:
                run(["killall", "ffplay"])
                run(
                    [
                        "ffplay",
                        self.current_song,
                        "-showmode",
                        "0",
                        "-autoexit",
                        "-nodisp",
                    ]
                )
            case True:
                run(["killall", "ffplay"])
                run(
                    [
                        "ffplay",
                        self.current_song,
                        "-showmode",
                        "1",
                        "-autoexit",
                    ]
                )
        return self.current_song

    def play_specific_song(self, song: str, visual_check: bool) -> str:
        """gets song to play as input, obviously"""
        match visual_check:
            case False:
                run(["killall", "ffplay"])
                run(
                    [
                        "ffplay",
                        song,
                        "-showmode",
                        "0",
                        "-autoexit",
                        "-nodisp",
                    ]
                )
            case True:
                run(["killall", "ffplay"])
                run(
                    [
                        "ffplay",
                        song,
                        "-showmode",
                        "1",
                        "-autoexit",
                    ]
                )
        return song

    def get_random_song(self, played_songs: list) -> str:
        """func that get's random song from playlist
        kwargs: played_songs: list is the list of already played songs
        output: randomly selected song"""
        print("getting random song")
        songs: list = list()
        dir: str = str()
        self.current_song: str = ""
        for dir, _, songs in walk(self.path):
            pass
        for song in songs:
            song: str = dir + str(Path(song))
        print("outside loop")
        while self.current_song in played_songs:
            print("searching for song")
            shuffle(songs)
            seed(self.get_seed())
            index: int = randint(0, len(songs))
            try:
                self.current_song: str = dir + "/" + songs[index]
            except IndexError:
                self.current_song: str = dir + "/" + songs[index - 2]
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
