from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.font import Font

root = Tk("Writing")

mainFont = Font(family="Arial", size=18, underline=True)

SCREENWIDTH = root.winfo_screenwidth()
SCREENHEIGHT = root.winfo_screenheight()
root.configure(bg="blue")
root.geometry(f"{SCREENWIDTH}x{SCREENHEIGHT}")
script = ScrolledText(root, width=115, height=20, font=mainFont)
script.configure(bg="lightblue")
script.pack()
with open("c:/Users/alvin/code/python/utilites/writing/writing.txt", "r") as oldText:
    oldText = oldText.read()
    script.insert(END, oldText)

def submit(text:ScrolledText):
    with open("c:/Users/alvin/code/python/utilites/writing/writing.txt", "w") as textToWriteInto:
        text = text.get("1.0", END)
        textToWriteInto.write(text)

submitButton = Button(root, text="Save Writing", command=lambda x=script: submit(x))
submitButton.pack()

root.mainloop()