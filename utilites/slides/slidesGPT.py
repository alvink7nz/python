import tkinter as tk
from tkinter import PhotoImage

# Create a Tkinter window
root = tk.Tk()
root.title("Editable Tkinter Presentation")
root.geometry("800x600")

# List of slides (each slide contains a title and content)
slides = [
    {"title": "Welcome to the Presentation", "content": "This is the first slide."},
    {"title": "What is Python?", "content": "Python is a popular programming language."},
    {"title": "Tkinter GUI", "content": "Tkinter is used to create graphical user interfaces."},
    {"title": "End of Presentation", "content": "Thank you for watching!"}
]

# Global variable to track the current slide index
slide_index = 0

# Function to update the slide content
def update_slide():
    global slide_index
    slide_title_entry.delete(0, tk.END)
    slide_title_entry.insert(0, slides[slide_index]["title"])
    
    slide_content_text.delete(1.0, tk.END)
    slide_content_text.insert(tk.END, slides[slide_index]["content"])

# Function to save the edited slide data
def save_slide():
    global slide_index
    slides[slide_index]["title"] = slide_title_entry.get()
    slides[slide_index]["content"] = slide_content_text.get(1.0, tk.END).strip()

# Functions to navigate between slides
def next_slide():
    global slide_index
    if slide_index < len(slides) - 1:
        save_slide()  # Save current slide data before moving to the next one
        slide_index += 1
        update_slide()

def previous_slide():
    global slide_index
    if slide_index > 0:
        save_slide()  # Save current slide data before moving to the previous one
        slide_index -= 1
        update_slide()

# Editable slide title (Entry widget for single-line text)
slide_title_entry = tk.Entry(root, font=("Arial", 24), width=40)
slide_title_entry.pack(pady=20)

# Editable slide content (Text widget for multi-line text)
slide_content_text = tk.Text(root, font=("Arial", 16), wrap=tk.WORD, height=15, width=70)
slide_content_text.pack(pady=10)

# Navigation buttons
prev_button = tk.Button(root, text="Previous", command=previous_slide)
prev_button.pack(side=tk.LEFT, padx=20, pady=20)

next_button = tk.Button(root, text="Next", command=next_slide)
next_button.pack(side=tk.RIGHT, padx=20, pady=20)

# Initialize with the first slide
update_slide()

# Run the Tkinter event loop
root.mainloop()
