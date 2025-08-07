# from random import random, randint
# def generate_x(path: str, start: float, end: float, cnt: int):
#     rlt = [random() * (end - start) + start for _ in range(cnt)]
#     with open(path, 'w') as f:  f.write('')
#     with open(path, 'a') as f:
#         for x in rlt:
#             f.write(str(x) + '\n')

# for path in ['./inputs/x1-input.txt', './inputs/x2-input.txt', './inputs/w1-input.txt', './inputs/w2-input.txt', './inputs/b-input.txt', ]:
#     generate_x(path, -3, 3, 10000)

# with open('./inputs/real.txt', 'w') as f:  f.write('')
# with open('./inputs/real.txt', 'a') as f:
#     for i in range(10000):
#         f.write(str(randint(0,1))+'\n')

# exit()



from math import e
from random import random, randint



def sigmoid(x: float) -> float:
    return 1 / (1+e**(-x))


def discrete(x: float) -> int:
    return 1  if x>0.5 else  0


def predict(input_data: list[float], weights: list[float], bias: float) -> float:
    return sigmoid(sum([input_data[i] * weights[i] for i in range(len(weights))]) + bias)


def slope(realdata: float, prediction: float, inputval: float = 1.0) -> float:
    return (realdata - prediction) * inputval


def read_data(paths: list[str]) -> list[list[float]]:
    rlt = []
    for path in paths:
        rlt.append([])

        with open(path, 'r') as f:
            for i in range(10000):
                rlt[-1].append(float(f.readline()))
    
    return rlt



inputval = [random() * 6 -3  for _ in range(2)]
real_data = [randint(0, 1) for _ in range(2)]
weight = [random() * 10 - 5  for _ in range(2)]
bias = random() * 5 - 2

# input_data = read_data(['./inputs/x1-input.txt', './inputs/x2-input.txt'])
# real_data = read_data(['./inputs/real.txt'])[0]
prediction = predict(inputval, weight, bias)
print([slope(real_data[i], prediction, inputval[i]) for i in range(10000)])