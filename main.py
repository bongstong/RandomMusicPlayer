from source.background_handler import BackgroundHandler
import threading
import tkinter as tk
from source.music_player import MusicPlayer
from source.song_handler import SongHandler
from os import remove
from json import load

with open(file="source/intel.json", mode="r") as file:
    intel: list = load(file)

path: str = ""
songs: list = list()
operating_system: int = 0
for information in intel:
    operating_system: int = information.get("OS")
    path: str = information.get("song_path")
    cover_path: str = information.get("cover_path")


yeezy: MusicPlayer = MusicPlayer(music_path=path)
songHandler: SongHandler = SongHandler()


def main(path: str = path):
    # music playing system
    played_songs: list = songHandler.load_song_list()
    if len(played_songs) == songHandler.num_songs(path=path) is True:
        print("played all songs")
        remove("played_songs.json")
    song: str = yeezy.get_random_song(
        played_songs=played_songs,
    )
    # background changing function/class
    songInspector: BackgroundHandler = BackgroundHandler(
        current_track=song,
    )
    songInspector.change_background(
        cover_path=cover_path, operating_sys=operating_system
    )
    songHandler.dump_song_list(
        yeezy.handle_played_music(song, played_songs),
    )
    yeezy.play()


while True:
    try:

        window = tk.Tk()
        window.title("Jam Player")
        label = tk.Label(window, text="Input track id")
        label.pack()

        button = tk.Button(text="Play", command=main)
        button.pack()
        window.mainloop()

        th = threading.Thread(target=main())
        th.start()

    except KeyboardInterrupt:
        print("\nquitting program")
        quit()
