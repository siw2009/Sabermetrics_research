from random import random
def generate_x(path: str, start: float, end: float, cnt: int):
    rlt = [random() * (end - start) + start for _ in range(cnt)]
    with open(path, 'w') as f:  f.write('')
    with open(path, 'a') as f:
        for x in rlt:
            f.write(str(x) + '\n')

for path in ['./inputs/x1-input.txt', './inputs/x2-input.txt', './inputs/w1-input.txt', './inputs/w2-input.txt', './inputs/b-input.txt', ]:
    generate_x(path, -100, 100, 10000)

# from math import e
# def sigmoid(x: float) -> float:
#     return 1 / 1+e**(-x)

# print([sigmoid() for i in range(10000)])