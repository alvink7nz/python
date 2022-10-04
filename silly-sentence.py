name = ['Alvin', 'Tony']
verb = ['kicks', 'buys', 'throws']
noun = ['lion', 'plane', 'bycicle', 'house', 'table', 'brain']
from random import randint
def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked
while True:
    again = 'yes'
    while again =='yes':
        print(pick(name), pick(verb), 'a', pick(noun), end='.\n')
        again = input('want anoter one? yes or no.\n ')
    break