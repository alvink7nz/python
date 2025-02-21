import tkinter as tk

# Function to start drawing
def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

# Function to draw on canvas when mouse moves
def draw(event):
    global last_x, last_y
    canvas.create_line(last_x, last_y, event.x, event.y, fill="black", width=3)
    last_x, last_y = event.x, event.y

# Create main window
root = tk.Tk()
root.title("Drawing App")
root.geometry("1000x600")
root.configure(bg="gray")

# Create a Canvas widget
canvas = tk.Canvas(root, bg="white", width=900, height=550)
canvas.pack(anchor="sw")

# Bind mouse events
canvas.bind("<ButtonPress-1>", start_draw)  # When left mouse button is pressed
canvas.bind("<B1-Motion>", draw)  # When mouse is moved while holding left button

# Run the application
root.mainloop()
