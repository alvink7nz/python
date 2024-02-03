import tkinter as tk
from tkinter import scrolledtext, simpledialog
import sys

class PrintRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)

def ask(prompt):
    result = simpledialog.askstring("Input", prompt)
    return result

def run_code():
    code = code_editor.get("1.0", tk.END)
    
    # Redirect sys.stdout to result_text
    original_stdout = sys.stdout
    sys.stdout = PrintRedirector(result_text)

    try:
        # Execute the Python code
        exec(code)
    except Exception as e:
        result_text.insert(tk.END, f"Error: {str(e)}")

    # Restore sys.stdout
    sys.stdout = original_stdout

# Create the main window
root = tk.Tk()
root.title("Python Code Editor")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Create a text widget for code input
code_editor = scrolledtext.ScrolledText(root, width=80, height=20)
code_editor.pack(padx=10, pady=10)

# Create a button to run the code
run_button = tk.Button(root, text="Run Code", command=run_code)
run_button.pack(pady=5)

# Create a text widget for the result
result_text = scrolledtext.ScrolledText(root, width=60, height=10)
result_text.pack(padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()
