import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter

class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Image Editor")
        self.root.geometry("800x600")
        
        # Initialize variables
        self.image = None
        self.tk_image = None
        self.file_path = None

        # GUI Elements
        self.create_widgets()

    def create_widgets(self):
        # Canvas for displaying the image
        self.canvas = tk.Canvas(self.root, bg="gray", width=600, height=400)
        self.canvas.pack(pady=20)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Load Image", command=self.load_image).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Save Image", command=self.save_image).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Resize", command=self.resize_image).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Rotate", command=self.rotate_image).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Blur", command=self.apply_blur).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Grayscale", command=self.convert_grayscale).pack(side=tk.LEFT, padx=5)

    def load_image(self):
        # Load an image file
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if self.file_path:
            self.image = Image.open(self.file_path)
            self.display_image()
        else:
            messagebox.showerror("Error", "Failed to load image!")

    def save_image(self):
        # Save the edited image
        if self.image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"),
                                                                ("JPEG files", "*.jpg"),
                                                                ("All Files", "*.*")])
            if save_path:
                self.image.save(save_path)
                messagebox.showinfo("Success", f"Image saved to {save_path}!")
        else:
            messagebox.showerror("Error", "No image to save!")

    def resize_image(self):
        if self.image:
            # Resize the image
            try:
                new_width = int(self.get_user_input("Enter new width:"))
                new_height = int(self.get_user_input("Enter new height:"))
                self.image = self.image.resize((new_width, new_height))
                self.display_image()
            except Exception:
                messagebox.showerror("Error", "Invalid dimensions!")
        else:
            messagebox.showerror("Error", "No image loaded!")

    def rotate_image(self):
        if self.image:
            # Rotate the image
            try:
                angle = int(self.get_user_input("Enter rotation angle (degrees):"))
                self.image = self.image.rotate(angle)
                self.display_image()
            except ValueError:
                messagebox.showerror("Error", "Invalid angle!")
        else:
            messagebox.showerror("Error", "No image loaded!")

    def apply_blur(self):
        if self.image:
            # Apply blur filter
            self.image = self.image.filter(ImageFilter.BLUR)
            self.display_image()
        else:
            messagebox.showerror("Error", "No image loaded!")

    def convert_grayscale(self):
        if self.image:
            # Convert to grayscale
            self.image = self.image.convert("L")
            self.display_image()
        else:
            messagebox.showerror("Error", "No image loaded!")

    def display_image(self):
        # Convert image to PhotoImage and display it on the canvas
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.delete("all")  # Clear the canvas
        self.canvas.create_image(300, 200, image=self.tk_image, anchor=tk.CENTER)

    def get_user_input(self, prompt_text):
        # Simple dialog for user input
        return tk.simpledialog.askstring("Input", prompt_text)

# Create the application window
root = tk.Tk()
app = ImageEditor(root)
root.mainloop()
