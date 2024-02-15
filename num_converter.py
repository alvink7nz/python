import tkinter as tk
from PIL import Image, ImageTk

def resize_image(image, max_width, max_height):
    """
    Resize the given PIL image to fit within the specified maximum dimensions,
    preserving the aspect ratio.
    """
    width_ratio = max_width / image.width
    height_ratio = max_height / image.height
    resize_ratio = min(width_ratio, height_ratio)
    new_width = int(image.width * resize_ratio)
    new_height = int(image.height * resize_ratio)
    return image.resize((new_width, new_height))

def convert_decimal(*args):
    decimal_input = entry_decimal.get()
    if decimal_input:
        try:
            decimal_value = int(decimal_input)
            entry_binary.delete(0, tk.END)
            entry_binary.insert(0, bin(decimal_value)[2:])
            entry_octal.delete(0, tk.END)
            entry_octal.insert(0, oct(decimal_value)[2:])
            entry_hexadecimal.delete(0, tk.END)
            entry_hexadecimal.insert(0, hex(decimal_value)[2:].upper())
        except ValueError:
            pass

def convert_binary(*args):
    binary_input = entry_binary.get()
    if binary_input:
        try:
            binary_value = int(binary_input, 2)
            entry_decimal.delete(0, tk.END)
            entry_decimal.insert(0, str(binary_value))
            entry_octal.delete(0, tk.END)
            entry_octal.insert(0, oct(binary_value)[2:])
            entry_hexadecimal.delete(0, tk.END)
            entry_hexadecimal.insert(0, hex(binary_value)[2:].upper())
        except ValueError:
            pass

def convert_octal(*args):
    octal_input = entry_octal.get()
    if octal_input:
        try:
            octal_value = int(octal_input, 8)
            entry_decimal.delete(0, tk.END)
            entry_decimal.insert(0, str(octal_value))
            entry_binary.delete(0, tk.END)
            entry_binary.insert(0, bin(octal_value)[2:])
            entry_hexadecimal.delete(0, tk.END)
            entry_hexadecimal.insert(0, hex(octal_value)[2:].upper())
        except ValueError:
            pass

def convert_hexadecimal(*args):
    hexadecimal_input = entry_hexadecimal.get()
    if hexadecimal_input:
        try:
            hexadecimal_value = int(hexadecimal_input, 16)
            entry_decimal.delete(0, tk.END)
            entry_decimal.insert(0, str(hexadecimal_value))
            entry_binary.delete(0, tk.END)
            entry_binary.insert(0, bin(hexadecimal_value)[2:])
            entry_octal.delete(0, tk.END)
            entry_octal.insert(0, oct(hexadecimal_value)[2:])
        except ValueError:
            pass

# Create the main window
root = tk.Tk()
root.title("Number Converter")

# Style
root.configure(bg="#f0f0f0")
font_style = ("Comfortaa", 12)

# Picture
image_file = "Converter.png"
image_pil = Image.open(image_file)
image_pil = resize_image(image_pil, 200, 150)
image = ImageTk.PhotoImage(image_pil)
image_label = tk.Label(root, image=image, width=200, height=150)
image_label.grid(row=0, column=0, padx=5, pady=5)

# Frame for the entries
entry_frame = tk.Frame(root, bg="#f0f0f0")
entry_frame.grid(row=1, column=0, padx=20, pady=20)

# Decimal Entry
label_decimal = tk.Label(entry_frame, text="Decimal:", bg="#f0f0f0", font=font_style)
label_decimal.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_decimal = tk.Entry(entry_frame, font=font_style)
entry_decimal.grid(row=1, column=1, padx=5, pady=5)
entry_decimal.bind("<KeyRelease>", convert_decimal)

# Binary Entry
label_binary = tk.Label(entry_frame, text="Binary:", bg="#f0f0f0", font=font_style)
label_binary.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_binary = tk.Entry(entry_frame, font=font_style)
entry_binary.grid(row=2, column=1, padx=5, pady=5)
entry_binary.bind("<KeyRelease>", convert_binary)

# Octal Entry
label_octal = tk.Label(entry_frame, text="Octal:", bg="#f0f0f0", font=font_style)
label_octal.grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_octal = tk.Entry(entry_frame, font=font_style)
entry_octal.grid(row=3, column=1, padx=5, pady=5)
entry_octal.bind("<KeyRelease>", convert_octal)

# Hexadecimal Entry
label_hexadecimal = tk.Label(entry_frame, text="Hexadecimal:", bg="#f0f0f0", font=font_style)
label_hexadecimal.grid(row=4, column=0, padx=5, pady=5, sticky="e")
entry_hexadecimal = tk.Entry(entry_frame, font=font_style)
entry_hexadecimal.grid(row=4, column=1, padx=5, pady=5)
entry_hexadecimal.bind("<KeyRelease>", convert_hexadecimal)

root.mainloop()