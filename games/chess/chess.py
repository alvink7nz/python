import tkinter as tk

root = tk.Tk()
root.geometry("800x600")

def playSinglePlayer():
    import singlePlay
    singleChess = singlePlay.Chess(root)

play = tk.Button(root, text="Play single player", command=playSinglePlayer)  # Call the function
play.pack()

root.mainloop()