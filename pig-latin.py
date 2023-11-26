message = input('Enter a word and I will turn it into Pig Latin\n')
index = 0
change_message = []
constanats = []
vowel_counter = 0
while index < len(message):
    change_message.append('')
    index = index + 1
def change_message_worker():
    global change_message, message, index, constanats, vowel_counter
    message = message.lower()
    index = 0
    while index < len(message):
        change_message[index] = message[index]
        index = index + 1
    if change_message[0] == 'a'or'e'or'i'or'o'or'u':
        change_message.append('y')
        change_message.append('a')
        change_message.append('y')
    elif change_message[0] != 'a'or'e'or'i'or'o'or'u':
        while change_message[vowel_counter] != 'a'or'e'or'i'or'o'or'u':
            constanats.append(change_message[vowel_counter])
            vowel_counter = vowel_counter + 1
change_message_worker()
print(constanats)