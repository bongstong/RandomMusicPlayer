"""Main program file, must run this file to launch the app.
Music playing application featuring a graphical user interface,
advanced shuffling system and automatic background changer."""

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
from source.sub_main import (
    mixtape_info,
    StoppableThread,
    abort,
    infi,
    main,
    filenames,
    gui_data,
    infi_vs,
)


def play_song_vs() -> None:
    """func that gets activated when clicking "Ok "button.
    gets index of specific song and plays it
    """
    thread0: StoppableThread = StoppableThread(
        target=main,
        args=(False, filenames[int(track_id.get())], False, True),
    )
    thread0.start()
    return None


def play_song() -> None:
    """func that gets activated when clicking "Ok "button.
    gets index of specific song and plays it
    """
    thread0: StoppableThread = StoppableThread(
        target=main,
        args=(False, filenames[int(track_id.get())], False, False),
    )
    thread0.start()
    return None


def main_btn_vs():
    thread0: StoppableThread = StoppableThread(
        target=main,
        args=(True, "", False, True),
    )
    thread0.start()


def main_btn():
    thread0: StoppableThread = StoppableThread(
        target=main,
        args=(True, "", False),
    )
    thread0.start()


# window and text input/output
root: Tk = Tk()
root.title("Bongstong Music Player")
label: Label = Label(
    root,
    text="Input track id to play specific song",
)
label.pack()
track_id = Entry()
track_id.pack()

top: Frame = Frame(root)
bottom: Frame = Frame(root)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)
# buttons
play_specific_song: Button = Button(text="Play song", command=play_song)
sleep_btn_vs: Button = Button(text="sleep with animations", command=infi_vs)
sleep_btn_vs.pack()
play_specific_song_vs: Button = Button(
    text="Play song with animation",
    command=play_song_vs,
)
play_specific_song.pack(in_=top, side=LEFT)
play_specific_song_vs.pack(in_=top, side=RIGHT)
nostop: Button = Button(text="Sleep Mode", command=infi)
nostop.pack()
quit_button: Button = Button(text="Quit program", command=abort)
quit_button.pack()


play_random_button = Button(
    root, text="Play/Skip random song", height=2, command=main_btn
)
play_random_button_visuals = Button(
    root,
    text="Play/Skip random song with animation",
    height=2,
    command=main_btn_vs,
)
play_random_button.pack()
play_random_button_visuals.pack()

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
