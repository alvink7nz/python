import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Update Text Widget Example")

# Create a Text widget
text_widget = tk.Text(root, height=10, width=40)
text_widget.pack()

# Function to set the text of the Text widget
def set_text(widget, content):
    # Clear existing content
    widget.delete("1.0", tk.END)
    # Insert new content
    widget.insert(tk.END, content)

# Add a Button to update the Text widget
def update_text():
    set_text(text_widget, "This is the updated text!")

update_button = tk.Button(root, text="Update Text", command=update_text)
update_button.pack()

# Run the application
root.mainloop()
