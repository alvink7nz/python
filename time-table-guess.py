table = 7
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
















