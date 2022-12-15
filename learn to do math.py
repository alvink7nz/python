from tkinter.simpledialog import askstring
from tkinter import messagebox

def add():
    global count_num, count_operator, limit, counter, count_num2
    counter2 = int(count_num)
    while limit != 0:
        count_num = askstring('what\'s {} {} {}?'.format(counter2, count_operator, counter), 'what\'s {} {} {}?'.format(counter2, count_operator, counter))
        count_num2 = int(count_num)
        if count_num2 !=  counter2 + counter:
            semi_counter = counter2 + counter
            messagebox.showinfo('that\'s wrong', 'that\'s wrong! the corect answer was {}'.format(semi_counter))
            count_num = semi_counter
        limit -= 1
        counter = count_num2
        counter2 = int(count_num)

def subtract():
    pass

def multiply():
    pass

def divide():
    pass

count_operator = askstring(title='the operator', prompt='do you want to add, subtract, mutiply or divide?')
count_num = askstring(title='the number', prompt='what number do you want to {} with?'.format(count_operator))
count_num2 = count_num
if count_operator == 'add' or 'multiply':
    count_add_mul = askstring(title='what number to {} from'.format(count_operator), prompt='what number do you want to {} from'.format(count_operator))
if count_operator == 'divide' or 'subtract':
    count_sub_div = askstring(title='which number to subtract or divide with', prompt='what number do you want to {} from'.format(count_operator))
counter = int(count_add_mul)
limit = 15
if count_operator == 'add':
    count_operator = 'plus'
    add()
if count_operator == 'subtract':
    count_operator= 'minus'
    subtract()
if count_operator == 'multiply':
    count_operator = 'multiplied by'
    multiply()
if count_operator == 'divide':
    count_operator = 'divided by'
    divide()

