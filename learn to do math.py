from tkinter import *
from tkinter.simpledialog import *
from tkinter.messagebox import *
from random import *
from keyboard import *

class Questions:
    def __init__(self, type) -> None:
        try:
            self.hardness = int(askstring(prompt="Difficulty: 1-10"))
        except ValueError:
            showerror(message="That is not a number!")
            return
        else:
            self.hardness *= 10
        if type == 1:
            self.add()
        elif type == 2:
            self.subtract()
        elif type == 3:
            self.multiply()
        elif type == 4:
            self.divide()
        elif type == 5:
            self.algebra()
        elif type == 6:
            self.log()
        elif type == 7:
            self.geometry()
        elif type == 8:
            self.FIN()
        elif type == 9:
            self.negative()
        
    def add(self):
        num1 = randint(1, self.hardness)
        num2 = randint(1, self.hardness)
        question = askinteger(prompt=f"{num1}+{num2}=")
        answer = num1 + num2
        if question == answer:
            showinfo(message=u"\u2713")
        else:
            showinfo(message=u"\u2717")
    def subtract(self):
        pass
    def multiply(self):
        pass
    def divide(self):
        pass
    def algebra(self):
        pass
    def log(self):
        pass
    def geometry():
        pass
    def FIN():
        pass
    def negative():
        pass

class Learn():
    def __init__(self) -> None:
        pass
root = Tk()
root.withdraw()

while True:
    showinfo(message="Press L to learn, Press T to test or press Q to quit")
    if is_pressed("q"):
        break
    if is_pressed("l"):
        pass
    if is_pressed("t"):
        for i in range(9):
            type = 1
            Questions(type=type)