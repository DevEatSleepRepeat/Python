import tkinter as tk
from tkinter import filedialog
import os

def open_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        os.startfile(folder_path)

root = tk.Tk()
root.title("Open Folder Example")

open_button = tk.Button(root, text="Open Folder", command=open_folder)
open_button.pack(padx=20, pady=20)

root.mainloop()