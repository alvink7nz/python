from tkinter import *

class CreateMaze():
    def __init__(self, root, rows, columns) -> None:
        self.root = root
        self.rows = rows
        self.columns = columns
        self.button_width = 10
        self.button_height = 10
        self.buttons = {}
        self.button_positions = {}
        self.mazeSize = [self.rows, self.columns]
        self.maze = [[1] * columns for _ in range(rows)]
    def userInput(self):
        row = 0
        column = 0
        for i in range(100):
            self.buttons[f"{i}"] = False
        for i in range(self.rows):
            self.button_row = []
            row += 50
            column = 0
            for j in range(self.columns):
                column += 50
                self.btn_id = i * self.columns + j  # Generate unique button ID
                self.button = Button(root)
                self.button.place(x=column, y=row, width=20, height=20)
                self.button_row.append(self.button)

    def draw_line(self, btn_id1, btn_id2):
        x1, y1 = self.button_positions[btn_id1]
        x2, y2 = self.button_positions[btn_id2]
        canvas.create_line(x1 + self.button_width // 2, y1 + self.button_height // 2, x2 + self.button_width // 2, y2 + self.button_height // 2, fill="black")

    def button_click(self, btn_id):
        if btn_id % self.columns != self.columns - 1:  # Check if not in the last column
            self.draw_line(btn_id, btn_id + 1)  # Draw line with the next button
        elif btn_id + self.columns < self.rows * self.columns:  # Check if not in the last row
            self.draw_line(btn_id, btn_id + self.columns)  # Draw line with the button below

root = Tk()
root.title("Maze Solver")
canvas = Canvas(root, width=350, height=350)
canvas.pack()
app = CreateMaze(root, 10, 10)
app.userInput()

root.mainloop()