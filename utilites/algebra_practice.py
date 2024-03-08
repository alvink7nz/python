import random
from sympy import symbols, solve

def generateQuestion():
    length = random.randint(4, 10)
    while length % 2 == 0:
        length = random.randint(4, 10)
    question = []
    for i in range(length):
        variableCount = 0
        num = random.randint(1, 15)
        num = str(num)
        if variableCount <= 2:
            variableX = random.choice([True, False])
        if variableX:
            num = num + 'x'
            variableCount += 1
        if i % 2 == 1:
            symbol = random.choice(["+", "-", "*", "/"])
            question.append(symbol)
        else:
            question.append(num)
    question = ' '.join(question)
    result = random.randint(1, 10)
    result = str(result)
    question = question + '=' + result
    print(question)
    return question

def rightAnswer(equation:str):
    x = symbols('x')
    answer = solve(equation, x)
    return answer

generateQuestion()

answer = input("\nAnswer: ")
correctAnswer = rightAnswer(generateQuestion())
if correctAnswer == answer:
    print("Correct!")