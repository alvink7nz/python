from tkinter import *

class Compile:
    def __init__(self, page) -> None:
        self.keyword = page.split()
    def Strings(self, string) -> list:
        if "print" in string:
            self.index = string.index("print")
            self.printThing = self.index

