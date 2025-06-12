from background_handler import BackgroundHandler
from music_player import MusicPlayer
from song_handler import SongHandler
from os import remove
from json import load

with open(file="intel.json", mode="r") as file:
    intel: list = load(file)

path: str = ""
for information in intel:
    os: str = information.get("OS")
    path: str = information.get("song_path")
    cover_path: str = information.get("cover_path")

yeezy: MusicPlayer = MusicPlayer(music_path=path)
songHandler: SongHandler = SongHandler()


def main(path: str = path):
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
    songInspector.change_background(
        cover_path=cover_path,
    )
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
