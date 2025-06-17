from source.data_handler import DataHandler
import tkinter as tk
from source.music_player import MusicPlayer
from source.song_handler import SongHandler
import os
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
mixData: DataHandler = DataHandler("")
mixtape_info: list = mixData.mixtape_data(path=path)


def main() -> None:
    """main program which handles music playing and background
    changing and data dumping, basically everyting"""
    # music playing system
    played_songs: list = songHandler.load_song_list()
    print(len(played_songs))
    print(num_songs)
    print(len(played_songs) >= num_songs)
    if len(played_songs) >= num_songs:
        print("yes")
        print("played all songs")
        os.remove("played_songs.json")
    song: str = yeezy.get_random_song(
        played_songs=played_songs,
    )
    # background changing function/class
    songInspector: DataHandler = DataHandler(
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


def get_track_id() -> int:
    """func that gets activated when clicking button.
    gets index of specific song to play it
    returns the index"""
    print(int(track_id.get()))
    return int(track_id.get())


while True:
    try:

        # window and text input/output
        window: tk.Tk = tk.Tk()
        window.title("Jam Player")
        label: tk.Label = tk.Label(
            window,
            text="Input track id to play specific song",
        )
        label.pack()
        track_id: tk.Entry = tk.Entry()
        track_id.pack()

        # buttons
        play_button: tk.Button = tk.Button(text="Ok", command=get_track_id)
        play_button.pack()
        pause_btn: tk.Button = tk.Button(
            text="Pause/Unpause",
            command=yeezy.pause_song,
        )
        pause_btn.pack()
        play_random_button: tk.Button = tk.Button(
            text="Play/Skip random song",
            command=main,
        )
        play_random_button.pack()

        window.mainloop()

    except KeyboardInterrupt:
        print("\nAborting program")
        quit()
