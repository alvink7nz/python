
from tkinter import *
from tkinter.simpledialog import askstring
import winsound


root = Tk()

def resetn():
    global isnotStopped, count_thing
    count_thing = 0
    isnotStopped = False
    count_num.config(text=count_thing)

def reset():
        global count_num, count_sec, timer_num, sec, counter_num, user_input, isnotStopped
        isnotStopped = False
        timer_num = counter_num
        count_num.config(text='minutes: {}'.format(timer_num))
        sec = 0
        count_sec.config(text='seconds: {}'.format(sec))
        yes_or_no = askstring(title='change or not', prompt='do you want to change your number?')
        if yes_or_no == 'no':
            isnotStopped = True
        if yes_or_no == 'yes':
            user_input = askstring(title='what number', prompt='what\'s your number?')
            timer_num = int(user_input)
            counter_num = timer_num
            count_num.config(text='minutes: {}'.format(timer_num))

def start_the_loop():
    global timer_num, count_num,  sec, count_sec, user_input
    if isnotStopped:
        if sec == 0:
            timer_num -= 1
            count_num.config(text='minutes: {}'.format(timer_num))
            sec = 60       
        sec = sec - 1
        count_sec.config(text='seconds: {}'.format(sec))
    if sec == 0 and timer_num == 0:
        for i in range(40):
            winsound.Beep(2000, 200) 
        reset()
    root.after(1000, start_the_loop)
def counter_loop():
        global isnotStopped, count_thing, couunter
        if isnotStopped:
            couunter+=1
            count_sec.config(text=couunter)
            if sec/60 == int:
                count_thing+=1
                count_num.config(text=count_thing)
        root.after(1000, counter_loop)

def start():    
    global isnotStopped
    isnotStopped = True
        
def stop():
    global isnotStopped
    isnotStopped = False

def whole_stopwwatch():
    global reset_n, stop_count, start_button, count_num, count_sec, isnotStopped, count_thing, couunter
    count_thing = -1
    isnotStopped = True

    
    root.title('stopwatch and timer')
    couunter = -1

    count_num.config(text=count_thing)
    count_sec.config(text=couunter)
    reset_n.config(command=resetn)
    stop_count.config(command=stop)
    start_button.config(command=start)
    counter_loop()

count_thing = -1
couunter = -1



count_num = Label(root, anchor='center', font='Comfortaa 30 bold', text=count_thing)
count_sec = Label(root, anchor='center', font='comfortaa 30 bold' ,text=couunter)
reset_n = Button(root, anchor='e', text='reset', height=3, width=3)
stop_count = Button(root, anchor='e', text='stop', height=3, width=3)
start_button = Button(root, anchor='w', text='start', height=3, width=3)
whole_stopwwatch()

def whole_timer():
    global isnotStopped
    isnotStopped = False
    sec = 0

    
    
    user_input = askstring(title='timer number', prompt='enter the number of minutes you want your timer to be:')
    timer_num = int(user_input)
    counter_num = timer_num
    count_num.config(text='minutes: {}'.format(timer_num))
    count_sec.config(text='seconds: {}'.format(sec))
    reset_n.config(command=reset)
    stop_count.config(command=stop)
    start_button.config(command=start)
    start_the_loop()


timer = Button(root, anchor='center', text='timer', command=whole_timer)
stopwatch = Button(root, anchor='center', text='stopwatch', command=whole_stopwwatch)

isnotStopped = True
sec = 0


count_num.pack()
count_sec.pack()
reset_n.pack()
start_button.pack()
stop_count.pack()
timer.pack()
stopwatch.pack()
root.mainloop()