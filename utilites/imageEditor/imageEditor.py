from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
import PIL.Image
import PIL.ImageTk
import PIL.ImageFilter

class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(self.root, bg="gray", width=700, height=550)
        self.canvas.pack(pady=20)
        self.frame = Frame(root, bg="green")
        self.frame.pack()
        self.image = None
        self.filePath = None
        self.tk_image = None
        self.history = []
        self.createWidgets()

    def createWidgets(self):
        self.loadImg = Button(self.frame, text="Load Image", command=self.loadImage)
        self.loadImg.pack(side=LEFT, padx=5)
        self.saveImg = Button(self.frame, text="Save Image", command=self.saveImage)
        self.saveImg.pack(side=LEFT, padx=5)
        self.cropImg = Button(self.frame, text="Crop Image", command=self.cropImage)
        self.cropImg.pack(side=LEFT, padx=5)
        self.blurImg = Button(self.frame, text="Blur Image", command=self.blurImage)
        self.blurImg.pack(side=LEFT, padx=5)
        self.grayImg = Button(self.frame, text="Grayscale", command=self.grayScale)
        self.grayImg.pack(side=LEFT, padx=5)
        self.undoBtn = Button(self.frame, text="Undo", command=self.undo)
        self.undoBtn.pack(side=LEFT, padx=5)

    def loadImage(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if self.file_path:
            self.history = []
            self.image = PIL.Image.open(self.file_path)
            self.history.append(self.image)
            self.display_image()
        else:
            messagebox.showerror("Error", "Failed to load image!")

    def cropImage(self):
        if self.image:
            cropDimensions = None
            inputDimensions = self.getUserInput("Enter Dimensions (seperate them with a comma and a space)", "Crop Dimensions")
            if inputDimensions == None:
                messagebox.showerror("Error", "DO NOT CLOSE IT!!!!!!!!!!!!")
            else:
                cropDimensions = inputDimensions.split(", ")
                for i in range(4):
                    cropDimensions[i] = int(cropDimensions[i])
                self.image = self.image.crop(cropDimensions)
                self.display_image()
                self.save_to_history()
        else:
            messagebox.showerror("Error", "No Image Loaded!")

    def saveImage(self):
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

    def blurImage(self):
        if self.image:
            # Apply blur filter
            self.image = self.image.filter(PIL.ImageFilter.BLUR)
            self.display_image()
            self.save_to_history()
        else:
            messagebox.showerror("Error", "No image loaded!")

    def grayScale(self):
        if self.image:
            self.image = self.image.convert("L")
            self.save_to_history()
            self.display_image()
        else:
            messagebox.showerror("Error", "No Image Loaded!")
    def getUserInput(self, text, title):
        answer = simpledialog.askstring(title, text)
        return answer
    
    def undo(self):
        # Undo the last operation
        if self.image:
    # Undo the last operation
            if len(self.history) > 0:  # Ensure there's at least one previous state
                self.history.pop()  # Remove the current state
                try:
                    self.image = self.history[-1]  # Restore to the previous state
                except IndexError:
                    print(len(self.history))
                self.display_image()
            else:
                messagebox.showinfo("Undo", "Cannot undo any further! Initial state reached.")
        else:
            messagebox.showerror("Error", "No Image Loaded!")

    def save_to_history(self):
        # Save the current image state to the history stack
        if self.image:
            self.history.append(self.image.copy())

    def display_image(self):
        # Convert image to PhotoImage and display it on the canvas
        self.tk_image = PIL.ImageTk.PhotoImage(self.image)
        self.canvas.delete("all")  # Clear the canvas
        self.canvas.create_image(350, 275, image=self.tk_image, anchor=CENTER)

root = Tk()
root.title("Image Editor")
root.geometry("1000x700")
root.configure(bg="yellow")

ImageEditor(root)

root.mainloop()