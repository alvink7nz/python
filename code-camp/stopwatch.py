from tkinter import Button, Tk, Canvas
from time import sleep 

def resetn():
    pass
def count_time(stop_count, count_thing):
    resetn()
    while stop_count is not True: # TODO: this is an infinite loop, how to solve it?
        sleep(1)
        count_thing = count_thing + 1




root = Tk()
root.title('stopwatch')
c = Canvas(root, height=420, width=420, bg='green')
c.pack() # TODO: why it doesn't show the canvas?
count_thing = 0
count_num = c.create_text(160, 210, anchor='center', font='Comfortaa 30 bold', fill='white', text=count_thing)
reset_n = Button(root, anchor='e', text='reset', height=3, width=3)
stop_count = Button(root, anchor='s', text='stop', height=3, width=3)

start = Button(root, anchor='w', text='start', height=3, width=3, command=count_time(stop_count, count_thing))
stopwatch = c.create_text(420, 150, anchor='s', font='Courier 28 bold underline', fill='black', text='stopwatch')
reset_n.pack()
start.pack()
