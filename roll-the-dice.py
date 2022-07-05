from tkinter import Button, Tk, Canvas 
from random import randint
random_number = randint(1,6)
def roll():
    c.create_rectangle(100, 100, 300, 100, outline='black')
    c.create_text(200, 200, text=random_number, fill='forest green', font='Courier 40 bold')

root = Tk()
c = Canvas(root, width=500, height=400)
rolled = Button(c, command=roll(), text='press to roll', width=10, height=3)
rolled.place(x=150, y=150)
root.mainloop()

