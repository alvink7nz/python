import tkinter as tk
from tkinter import filedialog
from tkinter.simpledialog import askstring
import pygame
import os

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def add_button(file_path):
    button_frame = tk.Frame(root)
    button_frame.pack()
    name = askstring("Name", f"Create name for {get_file_name(file_path)}")
    play_button = tk.Button(button_frame, text=f"Play {name}", command=lambda: play_music(file_path))
    play_button.pack(side=tk.LEFT, padx=5)

    delete_button = tk.Button(button_frame, text="Delete", command=lambda: delete_button_frame(button_frame, file_path))
    delete_button.pack(side=tk.LEFT)

    buttons.append(button_frame)

def get_file_name(file_path):
    return file_path.split("/")[-1]

def delete_button_frame(frame, file_path):
    frame.destroy()
    buttons.remove(frame)
    selected_files.remove(file_path)
    save_selected_files()

def save_selected_files():
    with open("selected_files.txt", "w") as file:
        for file_path in selected_files:
            file.write(f"{file_path}\n")

def load_selected_files():
    if os.path.exists("selected_files.txt"):
        with open("selected_files.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    else:
        return []

def select_music():
    file_path = filedialog.askopenfilename(filetypes=[("Music files", "*.mp3;*.wav")])
    if file_path:
        selected_files.append(file_path)
        save_selected_files()
        add_button(file_path)

def set_volume(value):
    volume = int(value) / 100.0
    increased_volume = volume * 2
    pygame.mixer.music.set_volume(min(increased_volume, 1.0))

# Initialize pygame.mixer before creating Tkinter root window
pygame.mixer.init()

# Create the Tkinter root window
root = tk.Tk()
root.title("Music Player")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))


buttons = []
selected_files = load_selected_files()

# Create a button for selecting and playing music
select_button = tk.Button(root, text="Select Music", command=select_music)
select_button.pack(pady=20)

# Create a scale for setting the volume
volume_scale = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL, label="Volume", command=set_volume)
volume_scale.pack(pady=10)

# Load previously selected files
for file_path in selected_files:
    add_button(file_path)

# Run the Tkinter event loop
root.mainloop()