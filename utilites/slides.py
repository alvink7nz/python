from tkinter import *

class Slides():
    def __init__(self, root:Tk, canvas:Canvas) -> None:
        self.root = root
        self.canvas = canvas
        self.create_button = Button(self.root, text="New Text", command=self.createMovableText)
        self.create_button.pack()
        self.click1 = False
        self.click2 = False

    def createMovableText(self):
        self.movable_text = self.canvas.create_text(100, 100, text="Text", font=("Helvetica", 12), fill="black")
        self.canvas.tag_bind(self.movable_text, "<B1-Motion>", self.moveToMouse)
        self.canvas.tag_bind(self.movable_text, "<Button-1>", self.using)
        self.canvas.tag_bind(self.movable_text, "<ButtonRelease-1>", self.using)
    def onClick1(self):
        self.click1 = True
        self.delete()
    def using(self, event):
        fill = self.canvas.itemcget(self.movable_text, option="fill")
        if fill == "black":
            self.canvas.itemconfig(self.movable_text, fill="blue")
        if fill == "blue":
            self.canvas.itemconfig(self.movable_text, fill="black")
    def delete(self):
        self.canvas.delete(self.movable_text)
    def moveToMouse(self, event):
        self.canvas.coords(self.movable_text, event.x, event.y)
root = Tk()
root.title("Slides")
canvas = Canvas(root, width=400, height=400, bg="white", highlightthickness=1, highlightbackground="black")
canvas.pack()
slides = Slides(root, canvas)

root.mainloop()