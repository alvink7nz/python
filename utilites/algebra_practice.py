import random
import sympy as alg

def generateQuestion(variable):
    question = []
    answer = []
    length = random.randint(2, 4)
    while length % 2 == 0:
        length = random.randint(2, 4)
    for i in range(length):
        symbol = random.choice(['+', '-', '*', '/'])
        num = random.randint(1, 9)
        answerNum = num
        num = str(num)
        yesOrNoX = random.choice([True, False])
        if yesOrNoX:
            num = num + 'x'
            answer.append(str(answerNum * variable))
            question.append(num)
        elif length == i+1:
            question.append(num)
            answer.append(num)
            print(i)
        else:
            question.append(num)
            question.append(symbol)
            answer.append(num)
            answer.append(symbol)
    answer = ''.join(answer)
    answerInt = eval(answer)
    multiplier = 1
    print("start")
    while True:
        result = answerInt * multiplier
        if isinstance(result, int):
            answerInt = result
            print(answerInt)
            break
        multiplier += 1
    print(question)
    return answer

print(generateQuestion(3))