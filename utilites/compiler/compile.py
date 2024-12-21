from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.simpledialog import askstring
import sys
from io import StringIO
root = Tk()
SCREENWIDTH = root.winfo_screenwidth()
SCREENHEIGHT = root.winfo_screenheight()
root.geometry(f"{SCREENWIDTH}x{SCREENHEIGHT}")
root.configure(bg="black")
script = ScrolledText(root, width=180, height=40)
script.configure(bg="gray")
with open("c:/Users/alvin/code/python/utilites/compiler/code.txt", "r") as oldCode:
    oldCode = oldCode.read()
    script.insert(END, oldCode)

script.pack()
def input(prompt):
    result = askstring("Input", prompt)
    return result
def run_code():
    code = script.get("1.0", END)
    with open("c:/Users/alvin/code/python/utilites/compiler/code.txt", "w") as oldCode:
        oldCode.write(code)
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
output.configure(bg="gray")
run.pack()
output.pack()
root.mainloop()