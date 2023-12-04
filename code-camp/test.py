import tkinter as tk

root = tk.Tk()

# Create labels
label1 = tk.Label(root, text="Label 1")
label2 = tk.Label(root, text="Label 2")
label3 = tk.Label(root, text="Label 3")

# Pack labels to place them on the same line
label1.pack(side=tk.LEFT)
label2.pack(side=tk.LEFT)
label3.pack(side=tk.LEFT)

root.mainloop()
