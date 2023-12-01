from tkinter.simpledialog import *
from tkinter import *
root = Tk()
table = Entry(root, width=30)
usedTable = table.get()
table = int(table)
correct_answer = 0
for i in range(1, 13):
    guess = askstring('What\'s', i, 'x', table, '?')
    if not int(guess):
        break
    ans = i * table
    if int(guess) == ans:
        ('Correct!')
        correct_answer = correct_answer + 1
    else:
        print('No, it\'s', ans)
print(f'good job! You got {correct_answer} out of 12')