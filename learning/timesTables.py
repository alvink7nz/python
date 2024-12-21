def test(table, num):
    isANum = False
    while not isANum:
        for i in range(3):
            x1 = input(f"What is {table} x {num}? ")
            try:
                x1 = int(x1)
                isANum = True
            except ValueError:
                print("That is not a number")
                isANum = False
            if x1 == table * num:
                print("Correct!")
                break
            else:
                if i == 2:
                    print(f"Wrong! The answer is {table*num}")
                else:
                    print("Wrong! Try again")
		
def learn(table, num):
    isANum = False
    while not isANum:
        x1 = input(f"What do you think {table} x {num} is? ")
        try:
            x1 = int(x1)
            isANum = True
        except ValueError:
            print("That is not a number")
            isANum = False
    if x1 == table * num:
        print("Wow, you got it first try!")
    else:
        print(f"You got it wrong but it's okay, but the answer is {table*num}")

playing = True
while playing:
    learning = input('press q to quit, press l to learn and t to test.')
    if learning == 't':
        error = True
        while error:
            tables = input('what table to you want to test?')
            try:
                tables = int(tables)
                error = False
            except ValueError:
                print('This is not a number')
                error = True
        for i in range(12):
            test(tables, i+1)
    elif learning == 'l':
        error = True
        while error:
            tables = input('what table to you want to learn?')
            try:
                tables = int(tables)
                error = False
            except ValueError:
                print('This is not a number')
                error = True
        for i in range(12):
            learn(tables, i+1)
    elif learning == "q":
        playing = False