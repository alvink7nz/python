import tkinter as tk
import singlePlay

root = tk.Tk()
root.geometry("800x600")

def playSinglePlayer():
    root.destroy()
    singlePlay.Chess()

play = tk.Button(root, text="Play single player", command=playSinglePlayer)
play.pack()

root.mainloop()