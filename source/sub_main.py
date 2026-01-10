"""cleanup file, just so hat main.py isn't too long"""

from source.image_handler import ImageHandler
from source.music_player import MusicPlayer
from source.file_handler import FileHandler
from source.data_handler import DataHandler
from json import load
import os
import threading

stop_sleep_thread: bool = False


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
    display_format: int = information.get("display")


musicPlayer: MusicPlayer = MusicPlayer(music_path=path)
fileHandler: FileHandler = FileHandler()
all_songs_num: int = len(fileHandler.all_songs(path))
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


def main(
    random: bool = True,
    song_play: str = "",
    infi: bool = False,
) -> None:
    """main program which handles music playing and background
    changing and data dumping, basically everyting"""
    print("In main func")
    global stop_sleep_thread
    if infi is True:
        print("infi is True")
        while True:
            print("in the loop thread")
            print(stop_sleep_thread)
            sub_main(random, song_play, infi)
            if stop_sleep_thread is True:
                stop_sleep_thread = False
                break
    else:
        print("Infi is Fals")
        sub_main(random, song_play)


def infi() -> threading.Thread:
    """plays songs non stop but blocks pause etc."""
    thread0: threading.Thread = threading.Thread(
        target=main,
        args=(True, "", True),
    )
    thread0.start()
    return thread0


def handle_images_notifications(
    icon_file: str,
    songInspector: DataHandler,
    album_file: str,
) -> None:
    """func that downloads pictures if needed and sends notification"""
    image_handling: ImageHandler = ImageHandler(
        artist_name=songInspector.artist,
        album_name=songInspector.album,
        path=cover_path,
    )
    if os.path.exists(album_file) is False:
        image_handling.download_cover()
        image_handling.blur_and_adjust(display_format=display_format)
    if os.path.exists(icon_file) is False:
        image_handling.run_download(px="600", is_icon=True)
    songInspector.change_background(operating_sys=operating_system, de=desktop)
    songInspector.send_notification()
    return None


def sub_main(random: bool = True, song_play: str = "", infi: bool = False):
    played_songs: list = fileHandler.load_song_list()
    print(all_songs_num)
    print(len(played_songs) - 1)  # TODO: KILL MYSELF
    if all_songs_num <= len(played_songs) - 1:
        print("All songs played")
        os.remove("played_songs.json")
        played_songs: list = [""]
    if song_play == "":
        print("going to look for song")
        song: str = musicPlayer.get_random_song(played_songs=played_songs)
        print("found song")
        print(song)
        fileHandler.dump_song_list(
            musicPlayer.handle_played_music(song, played_songs),
        )
    else:
        song: str = song_play
    # background changing function/class
    songInspector: DataHandler = DataHandler(song, cover_path)
    album_file: str = f"{cover_path}{songInspector.album_fmt}.png"
    icon_file: str = f"{cover_path}{songInspector.album_fmt}icon.png"
    if random is True:
        handle_images_notifications(icon_file, songInspector, album_file)
        musicPlayer.play_random_song()
        # if infi is True:
        #     __import__("time").sleep(float(songInspector.duration))
    else:
        handle_images_notifications(icon_file, songInspector, album_file)
        musicPlayer.play_specific_song(song)
    return None


def stop_sleep_fn() -> None:
    global stop_sleep_thread
    stop_sleep_thread = True
    return None


def abort() -> None:
    print("Quitting program")
    __import__("subprocess").run(["killall", "ffplay"])
    os._exit(0)
