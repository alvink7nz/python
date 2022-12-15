from tkinter import *
from tkinter.simpledialog import askstring
import winsound

is_going = False

def reset():
    global is_going, timer_label, sec_label, timer_num, sec, counter_num, user_input
    is_going = False
    timer_num = counter_num
    timer_label.config(text='minutes: {}'.format(timer_num))
    sec = 0
    sec_label.config(text='seconds: {}'.format(sec))
    yes_or_no = askstring(title='change or not', prompt='do you want to change your number?')
    if yes_or_no == 'no':
        is_going = True
    if yes_or_no == 'yes':
        user_input = askstring(title='what number', prompt='what\'s your number of minutes?')
        timer_num = int(user_input)
        counter_num = timer_num
        timer_label.config(text='minutes: {}'.format(timer_num))

def start_loop():
    global timer_num, timer_label, sec, sec_label, user_input
    if is_going:
        if sec == 0:
            timer_num -= 1
            timer_label.config(text='minutes: {}'.format(timer_num))
            sec = 60       
        sec = sec - 1
        sec_label.config(text='seconds: {}'.format(sec))
    if sec == 0 and timer_num == 0:
        for i in range(40):
            winsound.Beep(2000, 200) 
        reset()
    root.after(1000, start_loop)

def start():    
    global is_going
    is_going = True
    
def stop():
    global is_going
    is_going = False

root = Tk()
root.title('timer')
user_input = askstring(title='timer number', prompt='enter the number of minutes you want your timer to be: ')
timer_num = int(user_input)
counter_num = timer_num
seconds = askstring(title='second number', prompt='what\'s the number of seconds you want it to be?')
sec = int(seconds)
counter_sec = sec
timer_label = Label(root, anchor='center', font='arial 28 bold', text='minutes: {}'.format(timer_num))
sec_label = Label(root, anchor='center', font='arial 28 bold', text=f'seconds: {sec}')
reset_button = Button(root, anchor='center', font='arial 28', text='reset', command=reset)
start_num = Button(root, anchor='center', font='arial 28', text='start', command=start)
stop_num = Button(root, anchor='center', font='arial 28', text='stop', command=stop)
reset_button.pack()
timer_label.pack()
sec_label.pack()
start_num.pack()
stop_num.pack()
start_loop()
root.mainloop()