import tkinter as tk
from pynput import mouse


class MovableTextBox:
    def __init__(self, root, x, y):
        self.root = root
        
        # Create the text box with a custom border color and thickness
        self.textBox = tk.Text(root, height=5, width=20, 
                                highlightthickness=2,             # Border thickness
                                highlightbackground="red",        # Border color (when not focused)
                                highlightcolor="blue")             # Border color (when focused)
        # Place the text box at the provided x, y coordinates
        self.textBox.place(x=x, y=y)
        
        # Bind mouse events to the text box
        self.textBox.bind("<ButtonPress-1>", self.startMove)
        self.textBox.bind("<B1-Motion>", self.onDrag)

    # Method to handle the start of the move
    def startMove(self, event):
        self.startX = event.x
        self.startY = event.y

    # Method to handle dragging
    def onDrag(self, event):
        # Calculate the new position
        dx = event.x - self.startX
        dy = event.y - self.startY
        x = self.textBox.winfo_x() + dx
        y = self.textBox.winfo_y() + dy

        # Move the text box to the new position
        self.textBox.place(x=x, y=y)

class NewTextBox:
    def __init__(self, root):
        self.root = root
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()
    def on_click(self, x, y, button, pressed):
        if pressed:
            if button == "left":
                MovableTextBox(self.root, x, y)


root = tk.Tk()
root.title("Movable Text Box Example")
root.geometry("800x600")

slide = tk.Text(root, width=80, height=30)
slide.pack(side="bottom")
createText = tk.Button(root, text="Text Box", command=NewTextBox(root))
createText.pack(side="top")

root.mainloop()