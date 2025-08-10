from math import e, log
from random import random, randint
from data_reader import *



def sigmoid(x: float) -> float:
    return 1 / (1+e**(-x))


def discrete(x: float) -> int:
    return 1  if x>0.5 else  0


def predict(input_data: list[float], weights: list[float], bias: float) -> float:
    # print(sum([input_data[i] * weights[i] for i in range(len(weights))]) + bias)
    return sigmoid(sum([input_data[i] * weights[i] for i in range(len(weights))]) + bias)


def slope(realdata: int, prediction: float, inputval: list[float] = [1.0]) -> list[float]:
    return [(realdata - prediction) * x for x in inputval]


def err(realdata: int, prediction: float) -> float:
    if prediction == 1:  return 0
    return (realdata-1) * log(-prediction+1, e) - realdata * log(prediction, e)


def learn_row(weights: list[float], slopes: list[float], step: float) -> list[float]:
    return [weights[i] + step * slopes[i]  for i in range(len(weights))]


def learn(data: list[list], real_data: list[list], weight: list[float], bias: float, step: float) -> tuple[list[float], float]:
    weight_rlt = weight.copy()
    bias_rlt = bias
    for i in range(len(data)):
        prediction = predict(data[i], weight_rlt, bias_rlt)
        weight_rlt = learn_row(weight_rlt, slope(real_data[i][0], prediction, data[i]), step)
        bias_rlt = learn_row([bias_rlt], slope(real_data[i][0], prediction), step)[0]
    
    return weight_rlt, bias_rlt


def read_data(paths: list[str]) -> list[list[float]]:
    rlt = []
    for path in paths:
        rlt.append([])

        with open(path, 'r') as f:
            for i in range(10000):
                rlt[-1].append(float(f.readline()))
    
    return rlt



data = read_csv('./inputs/darwin (testdata).csv', [int, str, str] + [float] * 19 + [int, int])[1:]
data_split = split_data(data, (3, 20, 1))


step = 0.0001
# inputval = [random() * 6 -3  for _ in range(2)]
inputval = data_split[1][:-1]
# real_data = randint(0,1)
real_data = data_split[2][:-1]
# weight = [random() * 10 - 5  for _ in range(len(data_split[1][0]))]
weight = [0] * (len(data_split[1][0]))
# bias = random() * 5 - 2
bias = random()


# err_pred = predict(data_split[1][-1], weight, bias)
# print(err(data_split[2][-1][0], err_pred))
for i in range(10**3):
    weight, bias = learn(inputval, real_data, weight, bias, step)

    # if i%10**6 == 0:
    #     print(err(real_data, prediction))

for i in range(len(inputval)):
    if real_data[i][0]:
        print(predict(inputval[i], weight, bias), end = ' ')
        print(real_data[i])