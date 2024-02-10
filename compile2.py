from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.simpledialog import askstring
import sys
from io import StringIO
root = Tk()
script = ScrolledText(root, width=50, height=15)
script.pack()
def input(prompt):
    result = askstring("Input", prompt)
    return result
def run_code():
    code = script.get("1.0", END)
    old_stdout = sys.stdout
    redirectedOutput = sys.stdout = StringIO()
    try:
        exec(code)
    except Exception as e:
        output.insert(END, f"Error: {str(e)}")
    else:
        output.insert(END, redirectedOutput.getvalue())
    finally:
        sys.stdout = old_stdout
run = Button(root, text="Run", command=run_code)
output = ScrolledText(root, width=40, height=5)
run.pack()
output.pack()
root.mainloop()