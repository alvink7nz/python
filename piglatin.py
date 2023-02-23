encode = input('Enter a word for pig latin')
change_message = []
constanants = []
def encode_message():
    global constanants, change_message
    index = 0
    while index <= len(encode):
        change_message.append('')
        index = index + 1
    index = 0 
    while index <= len(encode):
        change_message[index] = encode[index]
        index = index + 1
    print(change_messsage)
encode_message()
