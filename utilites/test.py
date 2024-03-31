import tkinter as tk

def on_key_press(event):
    if event.keycode == 8:  # Check if Backspace key is pressed
        print("Backspace key pressed")

root = tk.Tk()

# Bind the KeyPress event to the function on_key_press
root.bind('<KeyPress>', on_key_press)

root.mainloop()