import tkinter as tk

def button_click(btn_id):
    if btn_id % columns != columns - 1:  # Check if not in the last column
        draw_line(btn_id, btn_id + 1)  # Draw line with the next button
    elif btn_id + columns < rows * columns:  # Check if not in the last row
        draw_line(btn_id, btn_id + columns)  # Draw line with the button below

def draw_line(btn_id1, btn_id2):
    x1, y1 = button_positions[btn_id1]
    x2, y2 = button_positions[btn_id2]
    canvas.create_line(x1 + button_width // 2, y1 + button_height // 2, x2 + button_width // 2, y2 + button_height // 2, fill="black")

root = tk.Tk()
root.title("Array of Buttons with Lines")

rows = 10
columns = 10
button_width = 10
button_height = 10

buttons = {}
button_positions = {}

canvas = tk.Canvas(root, width=columns * button_width, height=rows * button_height)
canvas.pack()

for i in range(rows):
    for j in range(columns):
        btn_id = i * columns + j
        x = j * button_width
        y = i * button_height
        button = tk.Button(root, text=" ", command=lambda btn_id=btn_id: button_click(btn_id))
        button.place(x=x, y=y, width=button_width, height=button_height)
        buttons[btn_id] = False
        button_positions[btn_id] = (x, y)

root.mainloop()