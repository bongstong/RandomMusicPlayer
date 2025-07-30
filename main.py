"""Main program file, must run this file to launch the app.
Music playing application featuring a graphical user interface,
advanced shuffling system and automatic background changer."""

from time import sleep
from tkinter import (
    Label,
    Tk,
    Entry,
    BOTH,
    Canvas,
    BOTTOM,
    RIGHT,
    Frame,
    Button,
    LEFT,
    TOP,
    END,
    Scrollbar,
    Y,
)
from source.data_handler import DataHandler
from source.music_player import MusicPlayer
from source.song_handler import SongHandler
from source.image_handler import ImageHandler
from os import remove
import os
from json import dump, load

with open(file="source/intel.json", mode="r") as file:
    intel: list = load(file)

path: str = ""
songs: list = list()
operating_system: int = 0
for information in intel:
    operating_system: int = information.get("OS")
    desktop: int = information.get("de")
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


def main(random: bool = True, song_play: str = "", inf: bool = False) -> None:
    """main program which handles music playing and background
    changing and data dumping, basically everyting"""
    # music playing system
    played_songs: list = songHandler.load_song_list()
    print("number of played songs:", (played_songs))
    print("number of total songs:", (num_songs))
    print(len(played_songs) == num_songs)
    if len(played_songs) == num_songs:
        print("played all songs")
        remove("played_songs.json")
    if song_play == "":
        song: str = yeezy.get_random_song(
            played_songs=played_songs,
        )
    else:
        song: str = song_play
    # background changing function/class
    songInspector: DataHandler = DataHandler(current_track=song)
    foo: str = songInspector.album.replace(" ", "").lower()
    album_file: str = f"{cover_path}{foo}.png"
    print(album_file)
    print(os.path.exists(album_file))
    if os.path.exists(album_file) is False:
        image_handling: ImageHandler = ImageHandler(
            artist_name=songInspector.artist,
            album_name=songInspector.album,
            path=cover_path,
        )
        image_handling.download_cover()
        image_handling.blur_and_adjust()
    songInspector.change_background(
        cover_path=cover_path, operating_sys=operating_system, de=desktop
    )
    songHandler.dump_song_list(
        yeezy.handle_played_music(song, played_songs),
    )
    if random is True:
        yeezy.play_random_song()
        if inf is True:
            sleep(float(songInspector.duration))
    else:
        return None


def play_song() -> None:
    """func that gets activated when clicking button.
    gets index of specific song and plays it
    """
    main(
        random=False,
        song_play=yeezy.play_specific_song(filenames[int(track_id.get())]),
    )
    return None


def infi() -> None:
    """plays songs non stop but blocks pause etc.
    to exit non stop must control C"""
    try:
        while True:
            main(inf=True)
    except KeyboardInterrupt:
        with open(file="played_songs.json", mode="r") as file:
            songs: list = load(file)
        with open(file="played_songs.json", mode="w") as file:
            dump(songs, file, indent=4)
        return None


# window and text input/output
root: Tk = Tk()
root.title("Bongstong Music Player")
label: Label = Label(
    root,
    text="Input track id to play specific song",
)
label.pack()
track_id: Entry = Entry()
track_id.pack()

# buttons
play_specific_song: Button = Button(
    text="Ok",
    command=play_song,
)
play_specific_song.pack()
nostop: Button = Button(text="Sleep Mode", command=infi)
nostop.pack()
quit_button: Button = Button(text="Quit program", command=quit)
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
scrollbar: Scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
canvas: Canvas = Canvas(grid_frame, height=800, width=1000)
grid_frame.pack()
canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set)
inner_frame: Frame = Frame(canvas)
canvas.create_window((800, 800), window=inner_frame)
canvas.bind(
    "<Configure>",
    lambda _: canvas.configure(
        scrollregion=canvas.bbox("all"),
    ),
)

for i in range(len(mixtape_info)):
    for j in range(len(gui_data[0])):
        entry: Entry = Entry(inner_frame, width=30)
        entry.grid(row=i, column=j)
        entry.insert(END, gui_data[i][j])

root.mainloop()
