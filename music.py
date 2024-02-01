from tkinter import *
from tkinter import filedialog

def download():
    musicfiles = []
    file = filedialog.askopenfilename(filetypes=[("Music files", "*.mp3;*.wav;*.acc;*.flac;*.m4a;*.ogg")])
    musicfiles.append(file)
    for i in musicfiles:
        pass