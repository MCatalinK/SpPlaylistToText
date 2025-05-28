import tkinter as tk
from tkinter import filedialog, messagebox

from mtd.track_info import *
from mtd.web_interaction import *
from logic.functionality import *


class DataLocationSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Location Selector")

        self.export_label = tk.Label(
            root, text="Paste the link to your Spotify playlist"
        )
        self.export_label.pack(pady=10, anchor="w")

        self.export_frame = tk.Frame(root)
        self.export_frame.pack(pady=5)

        self.url_entry = tk.Entry(self.export_frame, width=50)
        self.url_entry.insert(0,"https://open.spotify.com/playlist/4edLwaF8nNFS9i5pm9uNqa?si=55a9b26e92c64677")
        self.url_entry.pack(pady=5, side="left", anchor="w", fill="x")

        self.submit = tk.Button(
            self.export_frame, text="Submit", width=40, command=self.export_playlist
        )
        self.submit.pack(padx=5, side="left")

        self.info_label = tk.Label(
            root, text="Select a file or folder to load data from:"
        )
        self.info_label.pack(pady=10, anchor="w")

        self.info_frame = tk.Frame(root)
        self.info_frame.pack(pady=5)

        self.path_entry = tk.Entry(self.info_frame, width=50)
        self.path_entry.pack(pady=5, side="left", anchor="w", fill="x")

        self.file_button = tk.Button(
            self.info_frame, text="Select File", width=40, command=self.select_file
        )
        self.file_button.pack(padx=5, side="left")

    def select_file(self):
        filepath = filedialog.askopenfilename(
            title="Select a Data File",
            filetypes=[("CSV Files", "*.csv")],
        )
        if filepath:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, filepath)

        self.load_data()


    def export_playlist(self):
        url = self.url_entry.get()
        result = export_playlist(url)
        if result != "Successful":
            messagebox.showerror(result)

    def load_data(self):
        path = self.path_entry.get()
        if not path:
            messagebox.showwarning(
                "No Path Selected", "Please select a file."
            )
        else:
            run(path)
            


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")
    app = DataLocationSelector(root)
    root.mainloop()
