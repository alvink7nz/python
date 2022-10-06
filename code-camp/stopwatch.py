from tkinter import Button, Tk, Label

count_thing = -1
isnotStopped = True

def counter_loop():
    global isnotStopped, count_thing
    if isnotStopped:
        count_thing+=1
        count_num.config(text=count_thing)
    root.after(1000, counter_loop)

def resetn():
    global isnotStopped, count_thing
    count_thing = 0
    isnotStopped = False
    count_num.config(text=count_thing)


def start_loop():
    global isnotStopped, count_thing  
    isnotStopped = True
    
def stop_loop():
    global isnotStopped
    isnotStopped = False

root = Tk()
root.title('stopwatch')
count_num = Label(root, anchor='center', font='Comfortaa 30 bold', text=count_thing)
reset_n = Button(root, anchor='e', text='reset', height=3, width=3,  command=resetn)
stop_count = Button(root, anchor='e', text='stop', height=3, width=3, command=stop_loop)

start = Button(root, anchor='w', text='start', height=3, width=3, command=start_loop)

stopwatch = Label(root, anchor='n', font='Pacifica 28 bold', text='stopwatch')

count_num.pack()
reset_n.pack()
start.pack()
stop_count.pack()
stopwatch.pack()
counter_loop()
root.mainloop()