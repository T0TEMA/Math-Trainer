import time
import random
search_time = 30


def multiply():
    correct = 0
    bad = 0
    timer = 0
    questions = []
    init_time = time.time()
    while timer < search_time:
        question = []
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        cx = random.randint(0, 3)
        res = x * y
        question.append(f"{x}.{y}")
        question.append(res)
        print(f"{x}.{y} =", end=' ')
        answer = eval(input())
        if answer == res:
            correct += 1
        else:
            bad += 1
            question.append(answer)
        questions.append(question)
        timer = time.time() - init_time
        print(f"{search_time-timer:.0f}s left.\n")
    print(f"v = {correct} | x = {bad}")
    return questions
