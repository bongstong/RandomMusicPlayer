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
    print("are you using gnome light theme(0) or dark theme(1) or sway(2)?")
    de: int = int(input())
song_path: str = input(
    "Enter the path to the folder of the songs(e.g ~/Music/)\n",
)
cover_path: str = input(
    "Enter the path to the folder containing the album covers\n",
)
display: int = int(input("What is your display type(16:9/16:10)?[1/2]\n"))

if display == 1:
    display = 2160
else:
    display = 2400


intel: list = [
    {
        "OS": os,
        "song_path": song_path,
        "cover_path": cover_path,
        "de": de,
        "display": display,
    },
]

with open(file="source/intel.json", mode="w") as file:
    dump(intel, file)
