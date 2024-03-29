from tkinter import *

class Slides():
    def __init__(self, root:Tk, canvas:Canvas) -> None:
        self.root = root
        self.canvas = canvas
        self.pre = Button(root, text="Previous")
        self.pre.pack(side="left")

        self.next = Button(root, text="Next")
        self.next.pack(side="left")
        self._dragData = {}

        self.create_button = Button(self.root, text="New Text", command=self.createMovableText)
        self.create_button.pack()

    def createMovableText(self):
        self.movable_text = self.canvas.create_text(100, 100, text="Text", font=("Helvetica", 12), fill="black")
        self.canvas.tag_bind(self.movable_text, "<B1-Motion>", self.moveToMouse)
    def moveToMouse(self, event):
        x, y = self.root.winfo_pointerxy()
        self.canvas.move(self.movable_text, x, y)
root = Tk()
root.title("Slides")
canvas = Canvas(root, width=400, height=400, bg="white", highlightthickness=1, highlightbackground="black")
canvas.pack()
slides = Slides(root, canvas)

root.mainloop()