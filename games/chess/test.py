import tkinter as tk
import PIL
import PIL.Image
import PIL.ImageTk

# Create the main window
root = tk.Tk()
root.title("Get Button Text")

image = PIL.Image.open("c:/Users/alvin/code/python/games/chess/pawn.jpg")
image = PIL.ImageTk.PhotoImage(image)
# Create a button
button = tk.Button(root, image=image)
button.pack(pady=20)

# Run the application
root.mainloop()
