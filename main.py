from tkinter import BOTH, BOTTOM, Frame, Button, LEFT, TOP, END
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
    de: int = information.get("de")
    path: str = information.get("song_path")
    cover_path: str = information.get("cover_path")


yeezy: MusicPlayer = MusicPlayer(music_path=path)
songHandler: SongHandler = SongHandler()
list_of_songs: list = songHandler.all_songs(path=path)
num_songs: int = songHandler.num_songs(path=path)
mixData: DataHandler = DataHandler("")
mixtape_info: list = mixData.mixtape_data(path=path)
gui_data: list = [["ID", "ARTIST", "ALBUM", "TITLE"]]
index: int = 0
filenames: list = list()
for filename in mixtape_info:
    filenames.append(filename[-1])
    del filename[-1]
    filename.insert(0, index)
    gui_data.append(filename)
    index += 1


def main(random: bool = True, song_to_play: str = "") -> None:
    """main program which handles music playing and background
    changing and data dumping, basically everyting"""
    # music playing system
    played_songs: list = songHandler.load_song_list()
    if len(played_songs) >= num_songs:
        print("played all songs")
        os.remove("played_songs.json")
    if song_to_play == "":
        song: str = yeezy.get_random_song(
            played_songs=played_songs,
        )
    else:
        song: str = song_to_play
    # background changing function/class
    songInspector: DataHandler = DataHandler(
        current_track=song,
    )
    songInspector.change_background(
        cover_path=cover_path, operating_sys=operating_system, de=de
    )
    songHandler.dump_song_list(
        yeezy.handle_played_music(song, played_songs),
    )
    if random is True:
        yeezy.play_random_song()

    return None


def play_song() -> None:
    """func that gets activated when clicking button.
    gets index of specific song and plays it
    """
    main(
        random=False,
        song_to_play=yeezy.play_specific_song(filenames[int(track_id.get())]),
    )
    return None


while True:
    try:

        # window and text input/output
        root: tk.Tk = tk.Tk()
        root.title("Jam Player")
        label: tk.Label = tk.Label(
            root,
            text="Input track id to play specific song",
        )
        label.pack()
        track_id: tk.Entry = tk.Entry()
        track_id.pack()

        # buttons
        quit_button: tk.Button = tk.Button(text="Quit program", command=quit)
        play_specific_song: tk.Button = tk.Button(
            text="Ok",
            command=play_song,
        )
        play_specific_song.pack()
        quit_button.pack()

        top: Frame = Frame(root)
        bottom: Frame = Frame(root)
        top.pack(side=TOP)
        bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

        play_random_button = Button(
            root,
            text="Play/Skip random song",
            height=2,
            command=main,
        )
        pause_btn = Button(
            root,
            text="Pause/Unpause",
            height=2,
            command=yeezy.pause_song,
        )
        play_random_button.pack(in_=top, side=LEFT)
        pause_btn.pack(in_=top, side=LEFT)

        grid_frame: Frame = Frame(root)
        grid_frame.pack(padx=10, pady=10)

        for i in range(len(mixtape_info)):
            for j in range(len(gui_data[0])):
                entry: tk.Entry = tk.Entry(grid_frame, width=20)
                entry.grid(row=i, column=j)
                entry.insert(END, gui_data[i][j])

        root.mainloop()

    except KeyboardInterrupt:
        print("\nAborting program")
        quit()
