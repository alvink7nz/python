import tkinter as tk
import math

def press_key(key):
    # Function to handle button presses
    if key == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == 'C':
        entry.delete(0, tk.END)
    elif key == 'sqrt':
        try:
            result = math.sqrt(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == 'sin':
        entry.insert(tk.END, 'sin(')
    elif key == 'cos':
        entry.insert(tk.END, 'cos(')
    elif key == 'log':
        entry.insert(tk.END, 'log(')
    elif key == 'exp':
        entry.insert(tk.END, 'exp(')
    elif key == 'fact':
        entry.insert(tk.END, 'fact(')
    elif key == 'left':
        entry.icursor(entry.index(tk.INSERT) - 1)
    elif key == 'right':
        entry.icursor(entry.index(tk.INSERT) + 1)
    else:
        entry.insert(tk.END, key)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create entry widget
entry = tk.Entry(root, width=30, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '(', ')',
    'C', 'sqrt', 'sin', 'cos', 'log',
    'exp', 'fact', 'left', 'right'
]

# Create and place the buttons
row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, height=2, command=lambda key=button: press_key(key)).grid(row=row, column=col, padx=5, pady=5)
    elif button in ['left', 'right']:
        tk.Button(root, text=button, width=5, height=2, command=lambda key=button: press_key(key)).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=button, width=5, height=2, command=lambda key=button: press_key(key)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()