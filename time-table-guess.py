from tkinter.simpledialog import askstring
table = askstring('which table?', 'what table do you want(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)?')
correct_answer = 0
for i in range(1, 13):
    print('What\'s', i, 'x', table, '?')
    guess = input()
    if not int(guess):
        break
    ans = i * table
    if int(guess) == ans:
        print('Correct!')
        correct_answer = correct_answer + 1
    else:
        print('No, it\'s', ans)
print(f'good job! You got {correct_answer} out of 12')