from tkinter import *
from tkinter import filedialog

class TextFileExplorerApp:
    def __init__(self, root):
        self.root = root

        # Create a Text widget for input
        self.page = Text(root, height=10, width=40)
        self.page.pack(pady=10)

        # Create a button to open a file explorer
        open_button = Button(root, text="Open File", command=self.open_file)
        open_button.pack(pady=5)

        # Create a button to save the text to a file
        save_button = Button(root, text="Save to File", command=self.save_to_file)
        save_button.pack(pady=5)

    def open_file(self):
        # Open a file explorer to select a file
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        # Read the contents of the selected file and insert it into the Text widget
        if file_path:
            with open(file_path, "r") as file:
                file_contents = file.read()
                self.page.delete(1.0, END)  # Clear previous content
                self.page.insert(END, file_contents)

    def save_to_file(self):
        # Open a file explorer to select a destination file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        # Get the contents of the Text widget
        text_contents = self.page.get(1.0, END)

        # Write the contents to the selected file
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_contents)

def increase_font_size(line):
    global page
    start, end = page.tag_ranges("sel")
    highlighted_text = page.get(start, end)
    
    # Increase the font size of the highlighted text
    current_size = page.tag_cget("highlight", "font").split()[line]
    new_size = int(current_size) + 2
    page.tag_configure("highlight", font=("Arial", new_size))
    
    # Update the highlighted text
    page.tag_add("highlight", start, end)

def decrease_font_size(line):
    start, end = page.tag_ranges("sel")
    highlighted_text = page.get(start, end)
    
    # Increase the font size of the highlighted text
    current_size = page.tag_cget("highlight", "font").split()[line]
    new_size = int(current_size) - 1
    page.tag_configure("highlight", font=("Arial", new_size))
    
    # Update the highlighted text
    page.tag_add("highlight", start, end)

root = Tk()
root.title = "Write a Document"

page = Text(root, wrap="word", width=70, height=50)

TextFileExplorerApp(root=root)

highlightedSpace = StringVar()
increaseFont = Button(root, text="+", command=increase_font_size)
decreaseFont = Button(root, text="-", command=decrease_font_size)

page.pack(padx=10, pady=10)
increaseFont.pack(pady=15)
decreaseFont.pack(pady=20)
root.mainloop()