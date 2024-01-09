from tkinter import *
from tkinter import filedialog

class TextFileExplorerApp:
    def __init__(self, root):
        self.root = root
        self.page = Text(root, height=50, width=75)
        self.page.pack(pady=10)

        open_button = Button(root, text="Open File", command=self.open_file)
        open_button.pack(side="left")

        save_button = Button(root, text="Save to File", command=self.save_to_file)
        save_button.pack(side="left")

        increaseFont = Button(root, text="+", command=self.increase_font_size)
        decreaseFont = Button(root, text="-", command=self.decrease_font_size)
        increaseFont.pack(side="left")
        decreaseFont.pack(side="left")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                file_contents = file.read()
                self.page.delete(1.0, END)
                self.page.insert(END, file_contents)

    def save_to_file(self):
        # Temporarily remove the "highlight" tag before saving
        self.page.tag_remove("highlight", 1.0, END)

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        text_contents = self.page.get(1.0, END)
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_contents)

        # Reapply the "highlight" tag after saving
        self.page.tag_add("highlight", 1.0, END)

    def increase_font_size(self):
        self.adjust_font_size(2)

    def decrease_font_size(self):
        self.adjust_font_size(-2)

    def adjust_font_size(self, delta):
        try:
            current_size = int(self.page.tag_cget("highlight", "font").split()[1])
        except (TclError, ValueError, IndexError):
            current_size = 12  # Default font size if not set

        new_size = max(1, current_size + delta)  # Ensure font size doesn't go below 1
        self.page.tag_configure("highlight", font=("Arial", new_size))

        # Check if any text is selected
        if self.page.tag_ranges("sel"):
            start, end = self.page.tag_ranges("sel")
            self.page.tag_add("highlight", start, end)

root = Tk()
root.title = "Write a Document"

TextFileExplorerApp(root=root)

root.mainloop()