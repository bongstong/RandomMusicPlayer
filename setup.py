"""Setup file that takes info about system so that the Music
player works properly"""

from json import dump

de: int = 1
print("As of now, for linux only Gnome is supported for the background")
print("changing feature.\n Answer the questions for the setup.")
os: int = int(
    input("What OS are you using?[Windows(0); Linux/MacOS/BSD(1)]\n"),
)
if os == 1:
    de: int = int(input("are you using gnome light theme(0) or dark theme(1)"))
song_path: str = input(
    "Enter the path to the folder of the songs(e.g ~/Music/)\n",
)
cover_path: str = input(
    "Enter the path to the folder containing the album covers\n",
)


intel: list = [
    {"OS": os, "song_path": song_path, "cover_path": cover_path, "de": de},
]

with open(file="source/intel.json", mode="w") as file:
    dump(intel, file)
