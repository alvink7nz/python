from tkinter import *
 
def update():
    mylabel.configure(fg = "blue", text = "This is some blue text")
 
root = Tk()
root.geometry('200x200')
 
mylabel = Label(root, text = "This is some black text")
mylabel.pack(pady = 5)
 
root.after(3000, update)
 
root.mainloop()