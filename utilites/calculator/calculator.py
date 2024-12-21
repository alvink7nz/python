from tkinter import *
from tkinter.font import Font
import math

class Calculator:
    def __init__(self, root):
        self.mainFont = Font(root, ("Arial", 18))
        
        # Display for the equation
        self.equation = StringVar()
        self.result = StringVar()
        
        Entry(root, textvariable=self.equation, font=self.mainFont, border=2, background="lightgray", width=22).grid(row=0, column=0, columnspan=4, pady=5)
        
        # Buttons layout
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('C', 5, 0), ('0', 5, 1), ('.', 5, 2), ('+', 5, 3),
            ('(', 6, 0), (')', 6, 1), ('x^y', 6, 2), ('√', 6, 3),
            ('\u2190', 7, 0), ('=', 7, 2, 2), ('%', 7, 1)

        ]
        
        for text, row, col, *span in buttons:
            Button(
                root, text=text, font=self.mainFont, command=lambda t=text: self.on_button_click(t)
            ).grid(row=row, column=col, columnspan=(span[0] if span else 1), sticky="nsew", padx=5, pady=5)
    

    def on_button_click(self, char):
        if char == "=":
            self.solveEquation()
        elif char == "C":
            self.equation.set("")
        elif char == "\u2190":
            current_eq = self.equation.get()
            self.equation.set(current_eq[:-1])
        elif char == "√":
            current_eq = self.equation.get()
            try:
                result = math.sqrt(float(current_eq))
                self.equation.set(result)
            except ValueError:
                self.result.set("Error")
        elif char == "x^y":
            self.equation.set(self.equation.get() + "**")
        else:
            self.equation.set(self.equation.get() + char)

    def solveEquation(self):
        try:
            equation = self.equation.get()
            result = eval(equation)
            self.equation.set(result)
        except Exception:
            self.equation.set("Error")

# Main Application
root = Tk()
root.title("Calculator")
root.configure(bg="blue")
Calculator(root)
root.mainloop()

