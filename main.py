from source.background_handler import BackgroundHandler
from source.gui import GraphicalInterface
from source.music_player import MusicPlayer
from source.song_handler import SongHandler
from os import remove, walk
from json import load

with open(file="source/intel.json", mode="r") as file:
    intel: list = load(file)

path: str = ""
songs: list = list()
operating_system: int = 8
for information in intel:
    operating_system: int = information.get("OS")
    path: str = information.get("song_path")
    cover_path: str = information.get("cover_path")


match operating_system:
    case 1:
        command: list = [
            "gsettings",
            "set",
            "org.gnome.desktop.background",
            "picture-uri-dark",
        ]
    case 0:
        command: list = [
            "reg",
            "add",
            "HKEY_CURRENT_USER\\Control Panel\\Desktop",
            "/v",
            "Wallpaper",
            "/t",
            "REG_SZ",
            "/d",
        ]
    case _:
        print("Run setup program first")
        quit()


yeezy: MusicPlayer = MusicPlayer(music_path=path)
songHandler: SongHandler = SongHandler()


def main(path: str = path):
    for _, _, songs in walk(path):
        pass
    Gui: GraphicalInterface = GraphicalInterface(songs)
    played_songs: list = songHandler.load_song_list()
    if len(played_songs) == songHandler.num_songs(path=path) is True:
        print("played all songs")
        remove("played_songs.json")
    song: str = yeezy.get_random_song(
        played_songs=played_songs,
    )
    songInspector: BackgroundHandler = BackgroundHandler(
        current_track=song,
    )
    songInspector.change_background(cover_path=cover_path, command=command)
    songHandler.dump_song_list(
        yeezy.handle_played_music(song, played_songs),
    )
    yeezy.play()


while True:
    try:
        main()
    except KeyboardInterrupt:
        print("quit")
        quit()
