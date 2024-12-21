from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font

root = Tk("Writing")

mainFont = Font(family="Arial", size=18)

SCREENWIDTH = root.winfo_screenwidth()
SCREENHEIGHT = root.winfo_screenheight()
root.configure(bg="blue")
root.geometry(f"{SCREENWIDTH}x{SCREENHEIGHT}")
script = ScrolledText(root, width=90, height=20, font=mainFont)
script.configure(bg="lightblue")
script.place(x=300, y=20)
with open("c:/Users/alvin/code/python/utilites/writing/writing.txt", "r") as oldText:
    oldText = oldText.read()
    script.insert(END, oldText)

def submit(text:ScrolledText):
    with open("c:/Users/alvin/code/python/utilites/writing/writing.txt", "w") as textToWriteInto:
        text = text.get("1.0", END)
        textToWriteInto.write(text)

submitButton = Button(root, text="Save Writing", command=lambda x=script: submit(x))
submitButton.place(x=850, y=570)

root.mainloop()