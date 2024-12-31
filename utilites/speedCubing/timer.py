import time
from tkinter import *
import keyboard

class Timer():
    def __init__(self):
        self.startTime = time.time()
        self.timing = 0
        self.time = None

    def startTimer(self):
        spacePressed = False
        print("hi")
        while not spacePressed:
            self.timing = time.time()
            elapsedTime = self.timing - self.startTime
            if keyboard.KEY_DOWN == "space":
                self.time = elapsedTime
                print("hi") 
                return self.time

timer = Timer()
times = timer.startTimer()
print(times) 