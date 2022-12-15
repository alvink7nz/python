from tkinter import *
from random import *

root = Tk()
root.title('roll the dice')
c = Canvas(root, height=100, width=100)
the_dice = c.create_rectangle(100, 100, -100, -100, outline='blue', fill='red')
the_num = c.create_text()

