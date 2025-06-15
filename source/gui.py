import tkinter as tk


class GraphicalInterface:
    def __init__(self, list_of_songs: list) -> None:
        self.list_of_songs: list = list_of_songs
        window = tk.Tk()
        window.title("Jam Player")

        txt_output = tk.Text(window, height=5, width=30)
        txt_output.pack(pady=30)
        txt_output.insert(tk.END, "SONGS:\n")
        for item in self.list_of_songs:
            txt_output.insert(tk.END, item + "\n")

        window.mainloop()
        return None
