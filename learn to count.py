from tkinter import simpledialog, messagebox

test_or_learn = input('Press l for learning, Press t for testing and Press q to quit')

limit = 9
def add():
    global count_num, count_operator, limit, counter, count_num2
    counter2 = int(count_num)
    while limit != 0:
        count_num = simpledialog.askstring('what\'s {} {} {}?'.format(counter2, count_operator, counter), 'what\'s {} {} {}?'.format(counter2, count_operator, counter))
        count_num2 = int(count_num)
        if count_num2 !=  counter2 + counter:
            semi_counter = counter2 + counter
            messagebox.showinfo('that\'s wrong', 'that\'s wrong! the corect answer was {}'.format(semi_counter))
            count_num = count_num2
        limit -= 1
        counter = count_num2
        counter2 = int(count_num)

count_operator = 'plus'
count_num = simpledialog.askstring(title='what number to add from', prompt='what number to add with')
count_num2 = count_num
counter_num = simpledialog.askstring(title='what number to add from', prompt='what number to add from')
counter = int(counter_num)

if test_or_learn == 'q':
    quit()

if test_or_learn == 'l':
    print('')