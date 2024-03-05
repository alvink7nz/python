from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
def browse_image(label:tk.Label):
    file_img = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;")], initialdir="c:/Users/alvin/Downloads/Pictures")
    if file_img:
        img = Image.open(file_img)
        img.thumbnail((300, 200))  # Resize the image to fit the window
        img_tk = ImageTk.PhotoImage(img)
        label.img = img_tk
        label.config(image=img_tk)

root = tk.Tk()
root.title("Photos")

image_label = tk.Label(root)
image_label.pack()

browse_btn = tk.Button(root, text="Browse Image", command=lambda: browse_image(image_label))
browse_btn.pack()

root.mainloop()