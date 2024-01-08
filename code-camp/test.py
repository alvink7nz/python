import tkinter as tk
from tkinter import messagebox

def ask_question():
    result = messagebox.askquestion("Question", "Do you want to proceed?")
    if result == 'yes':
        label.config(text="You chose to proceed.")
    else:
        label.config(text="You chose not to proceed.")

# Create the main window
root = tk.Tk()
root.title("Tkinter Question Demo")

# Create a label
label = tk.Label(root, text="Click the button to ask a question.")
label.pack(pady=10)

# Create a button to ask the question
button = tk.Button(root, text="Ask Question", command=ask_question)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
