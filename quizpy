def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt <= 3:
        if guess.lower() == answer:
            print('correct answer!')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('wrong! Try again ')
            attempt += 1
    if attempt > 3:
        print('the correct answer is' + answer)
score = 0
print('this is a quiz')
guess1 = input('What is the most popular language?')
check_guess(guess1, 'chinese')
guess2 = input('there are more vending machines in Japan than people in New zealand. True or False?')
check_guess(guess2, 'true')
guess3 = input('round the approximate number of people by 2030 to the nearest 500 million.')
check_guess(guess3, '8.5 billion')
guess4 = input('what is the approximate number of people that came from  Asia in some random 10 people?')
check_guess(guess4, '6')
guess5 = input('why was the olympics 2020 moved to 2021?')
check_guess(guess5, 'because of the covid-19 pandemic')
print(f'you got, {score}, out of 5')

