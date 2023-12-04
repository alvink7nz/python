from tkinter import Button, Tk, Label

count_thing_milisec = -1
count_thing_sec = -1
isnotStopped = True

def counter_loop_milisec():
    global isnotStopped, count_thing_milisec
    if isnotStopped:
        count_thing_milisec+=1
        count_num_milisec.config(text=count_thing_milisec)
    root.after(1, counter_loop_milisec)
def counter_loop_sec():
    global isnotStopped, count_thing_sec
    if isnotStopped:
        count_thing_sec+=1
        count_num_sec.config(text=count_thing_sec)
    root.after(1000, counter_loop_sec)
def resetn():
    global isnotStopped, count_thing_sec, count_thing_milisec
    count_thing_sec = 0
    count_thing_milisec = 0
    isnotStopped = False
    count_num_milisec.config(text=count_thing_milisec)
    count_num_sec.config(text=count_thing_sec)



def start_loop():
    global isnotStopped
    isnotStopped = True
    
def stop_loop():
    global isnotStopped
    isnotStopped = False

root = Tk()
root.title('stopwatch')
root.geometry("1000x600")
count_num_sec = Label(root, anchor='center', font='Comfortaa 30 bold', text=count_thing_sec)
count_num_milisec = Label(root, anchor='center', font='Comfortaa 30 bold', text=count_thing_milisec)
reset_n = Button(root, anchor='e', text='reset', height=3, width=5,  command=resetn)
stop_count = Button(root, anchor='e', text='stop', height=3, width=5, command=stop_loop)

start = Button(root, anchor='w', text='start', height=3, width=5, command=start_loop)

stopwatch = Label(root, anchor='n', font='Pacifica 28 bold', text='stopwatch')

separator = Label(root, anchor='center', font="Comfortaa 30 bold", text=".")

if count_thing_sec == 1000:
    isnotStopped = False

count_num_sec.pack(side='up')
separator.pack(side='up')
count_num_milisec.pack(side='up')
reset_n.pack()
start.pack()
stop_count.pack()
stopwatch.pack()
counter_loop_milisec()
root.mainloop()