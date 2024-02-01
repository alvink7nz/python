from tkinter import *
from tkinter.messagebox import showinfo

class Compile:
    def Strings(self, string, output):
        if "print" in string:
            self.index = string.index("print")
            self.printStr = self.index + 1
            output.config
root = Tk()
output = Label(root)
codeText = Text(root, height=50, width=120)
code = codeText.get("1.0", "end-1c")
codeText.pack()
keyword = code.split()
compiler = Compile()
run = Button(root, text="Run", command=compiler.Strings(string=keyword, output=output))
run.pack()

root.mainloop()