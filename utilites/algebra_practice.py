import random
from sympy import symbols, solve, Eq

def generateQuestion():
    length = random.randint(2, 5)
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
    coeffecient = random.randint(2, 5)
    coeffecient = str(coeffecient)
    coeffecient = coeffecient + '*' + 'x'
    symbol = random.choice(["+", "-", "*"])
    question = question + '=' + coeffecient + symbol + result
    print(question)
    return question

def rightAnswer(equation:str):
    badX = 'x'
    index = equation.find(badX)
    equation = equation[:index] + '*' + equation[index:]
    equation = equation.split('=')
    equation = Eq(equation[1], equation[2])
    x = symbols('x')
    answer = solve(equation, x)
    return answer

generateQuestion()

answer = input("\nAnswer: ")
correctAnswer = rightAnswer(generateQuestion())
if correctAnswer == answer:
    print("Correct!")
else:
    print(f"Wrong, the answer is {correctAnswer}")