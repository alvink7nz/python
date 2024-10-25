from tkinter import *

root = Tk()

canvas = Canvas(root)
canvas.create_text(100, 100, text="hello")
canvas.pack()

root.mainloop()