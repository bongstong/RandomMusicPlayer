from source.background_handler import BackgroundHandler
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
list_of_songs: list = songHandler.all_songs(path=path)
num_songs: int = songHandler.num_songs(path=path)
pause: bool = False


def main() -> None:
    # music playing system
    played_songs: list = songHandler.load_song_list()
    if len(played_songs) == num_songs is True:
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
    yeezy.play_random_song()

    return None


while True:
    try:

        window = tk.Tk()
        window.title("Jam Player")
        label = tk.Label(window, text="Input track id")
        label.pack()

        play_button = tk.Button(text="Play", command=main)
        play_button.pack()

        pause_button = tk.Button(text="Pause", command=yeezy.pause_song)
        pause_button.pack()

        window.mainloop()

    except KeyboardInterrupt:
        print("\nAborting program")
        quit()
