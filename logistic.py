# from random import random
# def generate_x(path: str, start: float, end: float, cnt: int):
#     rlt = [random() * (end - start) + start for _ in range(cnt)]
#     with open(path, 'w') as f:  f.write('')
#     with open(path, 'a') as f:
#         for x in rlt:
#             f.write(str(x) + '\n')

# for path in ['./inputs/x1-input.txt', './inputs/x2-input.txt', './inputs/w1-input.txt', './inputs/w2-input.txt', './inputs/b-input.txt', ]:
#     generate_x(path, -3, 3, 10000)

from math import e
def sigmoid(x: float) -> float:
    return 1 / (1+e**(-x))

def discrete(x: float) -> int:
    return 1  if x>0.5 else  0


input_data = []
for path in ['./inputs/x1-input.txt', './inputs/x2-input.txt', './inputs/w1-input.txt', './inputs/w2-input.txt', './inputs/b-input.txt']:
    input_data.append([])
    with open(path, 'r') as f:
        for i in range(10000):
            input_data[-1].append(float(f.readline()))

print([discrete(sigmoid(input_data[0][i]*input_data[2][i] + input_data[1][i]*input_data[3][i] + input_data[4][i])) for i in range(10000)])