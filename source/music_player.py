from pygame import mixer, USEREVENT
from random import seed, randint, shuffle
from datetime import datetime
from pathlib import Path
from os import walk, urandom


class MusicPlayer:
    def __init__(self, music_path: str = "~/Music/") -> None:
        mixer.init()
        self.path: str = music_path
        self.current_song: str = ""
        return None

    def play_random_song(self) -> str:
        print("playing:", self.current_song)
        mixer.music.load(self.current_song)
        mixer.music.play()
        mixer.music.set_endevent(USEREVENT + 1)
        return self.current_song

    def pause_song(self):
        print("pausing/starting")
        if mixer.music.get_busy() is True:
            print("music is playing")
            mixer.music.pause()
        else:
            print("music is already paused")
            mixer.music.unpause()

    def get_random_song(self, played_songs: list) -> str:
        print("getting random song")
        songs: list = list()
        index: int = 0
        dir: str = str()
        self.current_song: str = ""
        for dir, _, songs in walk(self.path):
            pass
        for song in songs:
            song: str = dir + str(Path(song))
        try:
            while self.current_song in played_songs:
                shuffle(songs)
                seed(self.get_seed())
                index: int = randint(0, len(songs))
                self.current_song: str = dir + "/" + songs[index]
        except IndexError:
            while self.current_song in played_songs:
                self.current_song: str = (
                    dir
                    + "/"
                    + songs[
                        randint(
                            0,
                            len(songs),
                        )
                    ]
                )

        return self.current_song

    def get_seed(self) -> int:
        print("getting seed")
        seed1: int = int(datetime.now().strftime("%f"))
        RAND_SIZE = 4
        random_data = urandom(RAND_SIZE)
        random_seed: int = int.from_bytes(random_data, byteorder="big")
        return random_seed * seed1

    def handle_played_music(
        self,
        played_song: str,
        list_of_played_songs: list,
    ) -> list:
        print("adding song to played songs")
        list_of_played_songs.append(played_song)
        return list_of_played_songs
