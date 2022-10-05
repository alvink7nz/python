from tkinter import Button, Tk, Label

def resetn(reseter):
    reseter = 0

def count_time(num):
    num+=1
    
def stop_num(count_n):
    return count_time(count_n)


root = Tk()
root.title('stopwatch')
count_thing = 0
count_num = Label(root, anchor='center', font='Comfortaa 30 bold', text=count_thing)
reset_n = Button(root, anchor='e', text='reset', height=3, width=3,  command=resetn(count_thing))
stop_count = Button(root, anchor='sw', text='stop', height=3, width=3, command=stop_num(count_thing))

start = Button(root, anchor='w', text='start', height=3, width=3, command=count_time(count_thing))
stopwatch = Label(root, anchor='n', font='Pacifica 28 bold', text='stopwatch')
while count_time is True:
    root.after(1000, count_time(count_thing))

count_num.pack()
reset_n.pack()
start.pack()
stop_count.pack()
stopwatch.pack()

root.mainloop()