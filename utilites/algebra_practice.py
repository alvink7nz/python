import random

def generateQuestion():
    question = []
    part1 = []
    part2 = []
    for j in range(2):
        variableCount = 0
        length = random.randint(2, 7)
        while length % 2 == 0:
            length = random.randint(2, 7)
        for i in range(length):
            num = random.randint(1, 15)
            num = str(num)
            if variableCount <= 2:
                variableX = random.choice([True, False])
            if variableX:
                num = num + 'x'
                variableCount += 1
            if i % 2 == 1:
                symbol = random.choice(["+", "-", "*", "/"])
                if j == 0:
                    part1.append(symbol)
                elif j == 1:
                    part2.append(symbol)
            else:
                if j == 0:
                    part1.append(num)
                elif j == 1:
                    part2.append(num)
    part1 = ' '.join(part1)
    part2 = ' '.join(part2)
    question.append(part1)
    question.append(part2)
    question = ' = '.join(question)
    return question

def rightAnswer():
    x = random.randint
    
print(generateQuestion())