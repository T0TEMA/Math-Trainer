import math
import random
import time


def game():
    correct = 0
    bad = 0
    timer = 0
    questions = []
    init_time = time.time()
    while timer < 10:
        question = []
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        cx = random.randint(0, 3)
        OPERATORS = ('+', '-', '/', '.')
        if cx == 0:
            res = x + y
            question.append(f"{x}+{y}")
        elif cx == 1:
            res = x - y
            question.append(f"{x}-{y}")
        elif cx == 2:
            res = x / y
            question.append(f"{x}/{y}")
        else:
            res = x * y
            question.append(f"{x}.{y}")
        question.append(res)
        print(f"{x}{OPERATORS[cx]}{y} =", end=' ')
        answer = eval(input())
        if answer == res:
            correct += 1
        else:
            bad += 1
            question.append(answer)
        questions.append(question)
        timer = time.time() - init_time
    print(f"v = {correct} | x = {bad}")
    return questions


def main():
    command = ""
    while command != 'E':
        command = str(input('?'))
        if command.upper() == 'M':
            history = game()
            for question in history:
                print(question)


if '__main__' == __name__:
    main()
