import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageCropper:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Image Cropper")
        
        # Load image
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if not self.image_path:
            print("No file selected.")
            root.destroy()
            return
        
        self.image = Image.open(self.image_path)
        self.image_tk = ImageTk.PhotoImage(self.image)
        
        # Canvas to display the image
        self.canvas = tk.Canvas(root, width=self.image.width, height=self.image.height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)
        
        # Dots (draggable corner points)
        self.dots = [
            self.canvas.create_oval(50, 50, 60, 60, fill="red", tags="dot"),
            self.canvas.create_oval(200, 50, 210, 60, fill="red", tags="dot"),
            self.canvas.create_oval(50, 200, 60, 210, fill="red", tags="dot"),
            self.canvas.create_oval(200, 200, 210, 210, fill="red", tags="dot")
        ]
        
        # Crop rectangle
        self.crop_rect = self.canvas.create_rectangle(50, 50, 200, 200, outline="blue", width=2)
        
        # Bindings
        self.canvas.tag_bind("dot", "<Button1-Motion>", self.move_dot)
        self.root.bind("<Return>", self.crop_image)  # Press Enter to crop

    def move_dot(self, event):
        """Handles moving the dots and updating the rectangle."""
        dot_id = self.canvas.find_withtag("current")[0]
        self.canvas.coords(dot_id, event.x - 5, event.y - 5, event.x + 5, event.y + 5)
        self.update_rectangle()

    def update_rectangle(self):
        """Updates the crop rectangle based on dot positions."""
        coords = [self.canvas.coords(dot)[:2] for dot in self.dots]
        x_coords = [x for x, y in coords]
        y_coords = [y for x, y in coords]
        self.canvas.coords(
            self.crop_rect,
            min(x_coords), min(y_coords), max(x_coords), max(y_coords)
        )

    def crop_image(self, event):
        """Crops the image based on the rectangle and saves it."""
        rect_coords = self.canvas.coords(self.crop_rect)
        left, top, right, bottom = map(int, rect_coords)
        cropped_image = self.image.crop((left, top, right, bottom))
        
        # Save the cropped image
        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if save_path:
            cropped_image.save(save_path)
            print(f"Cropped image saved to {save_path}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCropper(root)
    root.mainloop()
