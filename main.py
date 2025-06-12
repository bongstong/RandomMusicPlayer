from background_handler import BackgroundHandler
from music_player import MusicPlayer
from song_handler import SongHandler
from os import remove


path: str = "/run/media/nathanv/ssd1/Music/"
yeezy: MusicPlayer = MusicPlayer(music_path=path)
songHandler: SongHandler = SongHandler()


def main(path: str = path):
    played_songs: list = songHandler.load_song_list()
    if len(played_songs) == songHandler.num_songs(path=path):
        print("played all songs")
        remove("played_songs.json")
    song: str = yeezy.get_random_song(
        played_songs=played_songs,
    )
    songInspector: BackgroundHandler = BackgroundHandler(
        current_track=song,
    )
    songInspector.change_background(
        cover_path="/home/nathanv/Pictures/album_covers/",
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
