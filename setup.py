from json import dump

print("As of now, for linux only Gnome is supported for the background")
print("changing feature.\n Answer the questions for the setup.")
os: int = int(
    input("What OS are you using?[Windows(0); Linux/MacOS/BSD(1)]\n"),
)
song_path: str = input(
    "Enter the path to the folder of the songs(e.g ~/Music/)\n",
)
cover_path: str = input(
    "Enter the path to the folder containing the album covers\n",
)


intel: list = [{"OS": os, "song_path": song_path, "cover_path": cover_path}]

with open(file="source/intel.json", mode="w") as file:
    dump(intel, file)
