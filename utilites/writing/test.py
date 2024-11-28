import tkinter as tk

def create_gradient(canvas:tk.Canvas, width, height, color1, color2):
    """
    Draw a vertical gradient on a Canvas.
    """
    for i in range(height):
        ratio = i / height
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, width, i, fill=color)

root = tk.Tk()
root.geometry("400x300")

# Create a Canvas to draw the gradient
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)

# Gradient colors (RGB format)
start_color = (255, 255, 0)  # Yellow
end_color = (0, 128, 255)    # Blue

create_gradient(canvas, 400, 300, start_color, end_color)

root.mainloop()
