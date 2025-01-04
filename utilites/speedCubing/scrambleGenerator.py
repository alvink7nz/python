import random

possibleMoves = ["R","L","U","D","B","F"]
scramble = ""
goodMoves = 0
letter = " "
while goodMoves < 15:
    oldLetter = letter
    letter = random.choice(possibleMoves)
    if letter != oldLetter[0]:
        acsessories = ["", "", "'", "2", "2"]
        acsessory = random.choice(acsessories)
        letter = "".join([letter, acsessory])
        scramble = " ".join([scramble, letter])
        goodMoves += 1