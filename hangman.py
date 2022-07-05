import random
difficultly = input('diffucultly:\n easy\n medium\n hard\n')
if difficultly.lower() == 'easy':
    lives = 12
elif difficultly.lower() == 'medium':
    lives = 9
elif difficultly.lower() == 'hard':
    lives = 6

words = ['alice', 'lolipop', 'bottle', 'madness', 'immpossible', 'curtain']
secret_word = random.choice(words)
clue = []
index = 0
while  index < len(secret_word):
    clue.append('?')
    index = index + 1
heart_symbol = u'\u2764'
guess_word_corectly = False
unknown_letters = len(secret_word)
def upadate_clue(guessed_letter, secret_word, clue, unknown_letters):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            unknown_letters = unknown_letters - 1
        index = index + 1
    return unknown_letters

while lives > 0:
    print(clue)
    print('lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        print(f'yay! the secret word is {secret_word}')
        break
    elif guess in secret_word:
        unknown_letters = upadate_clue(guess, secret_word, clue, unknown_letters)
    else:
        print('Incorrect. You lose a life')
        lives = lives - 1
    if unknown_letters == 0:
        print(f'yay! the secret word is {secret_word}')
        break
if lives == 0:
    print(f'sorry, the answer is {secret_word}')