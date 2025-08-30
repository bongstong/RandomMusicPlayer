# RandomMusicPlayer

## Music player with advanced shuffle song player

Makes sure that it doesn't play the same 10 songs all the time
by keeping track of played songs accross various sessions.

## Automatic Background changer

The application finds the album name from the metadata of the track and automatically
switches the background of your PC to the album cover. You can download your
own covers or the program can also automatically download the covers and set
them up for your display ratio using ffmpeg.

Naming conventions for album covers:
If you want to use your own album covers, you must follow some file naming
conventions so that the program recognises your file and the command to change
the background works. You have to name the picture the exact same name as the
name of the album, but all small letters, no `'`, if the album name has a character
like `&` you must replace it by `and` in the filename and if you have `$` you
must replace it by `s`

## To run the program

Make sure you have python installed on your system.
first run the `setup.py` file and insert all the required information.
Then install all the required libraries from the `requirements.txt` file
using `pip install -r requirements.txt`
Then run the `main.py` file using `python main.py` while being in the `source`
directory.

## Dependencies

In order for the notifications to work you need to install some packages,
you can use the following commands:
For Fedora:

```bash
# Install required development packages
sudo dnf install gcc gcc-c++ python3-devel cairo-devel gobject-introspection-devel glib2-devel -y
sudo dnf install meson ninja-build

# Install the missing cairo-gobject development package
sudo dnf install cairo-gobject-devel
```

For Debian/Ubuntu:

```bash
# Update package list and install required development packages
sudo apt update
sudo apt install gcc g++ python3-dev libcairo2-dev libgirepository1.0-dev libglib2.0-dev -y
sudo apt install meson ninja-build

# Install the missing cairo-gobject development package
sudo apt install libcairo-gobject2-dev
```

For Arch:

```bash
# Install required development packages
sudo pacman -Syu gcc gcc-libs python python-pip cairo gobject-introspection glib2 meson ninja
```

TODO:

- Add GUI ✅

- Make the program automatically fetch the album covers ✅

- Add Notifications

- Add support to other desktop environments
  (As of now: Gnome light/dark mode, Sway)
