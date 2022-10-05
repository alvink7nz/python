from tkinter import *
from tkinter import messagebox

tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('PythonExamples.org - Tkinter Example')

def showMsg():  
    messagebox.showinfo('Message', 'You clicked the Submit button!')

button = Button(tkWindow,
	text = 'Submit',
	command = showMsg)  
button.pack()  
  
tkWindow.mainloop()