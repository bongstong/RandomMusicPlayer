"""program that plays the song, and pseudo-randomly chhooses the song.
Also includes all related features as pausing the song."""

import pygame
from os import remove
from random import seed, randint, shuffle
from datetime import datetime
from pathlib import Path
from os import walk, urandom


class MusicAlreadyPlaying(Exception):
    """Error handling class"""

    def __init__(self):
        print("music is already paused")
        pygame.mixer.music.unpause()
        return None


class MusicPlayer:
    """handles application, playing music, fetching random songs
    kwargs: music_pathL str is the path of the mixtape"""

    def __init__(self, music_path: str = "~/Music/") -> None:
        pygame.init()
        pygame.mixer.init()
        self.path: str = music_path
        self.current_song: str = ""
        return None

    def play_random_song(self) -> str:
        """func that plays the song. outputs ths song"""
        print(f"playing: {self.current_song}")
        pygame.mixer.music.load(self.current_song)
        pygame.mixer.music.play()
        return self.current_song

    def play_specific_song(self, song: str) -> str:
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
        return song

    def pause_song(self) -> None:
        """func that pauses and unpauses the song if it's playing or not"""
        print("pausing/starting")
        global pause
        try:
            if pygame.mixer.music.get_busy() is True:
                pause = True
                print("music is playing")
                pygame.mixer.music.pause()
            else:
                raise MusicAlreadyPlaying
        except MusicAlreadyPlaying:
            pass
        return None

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
            while self.current_song in played_songs:
                shuffle(songs)
                seed(self.get_seed())
                index: int = randint(0, len(songs))
                print(self.current_song in played_songs)
                print(self.current_song)
                try:
                    self.current_song: str = dir + "/" + songs[index]
                except IndexError:
                    print(
                        "###" * 4,
                        f"\nindex: {index}\nlen(list): {len(songs)}",
                    )
                    try:
                        remove("played_songs.json")
                        played_songs = [""]
                    except FileNotFoundError:
                        pass

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
