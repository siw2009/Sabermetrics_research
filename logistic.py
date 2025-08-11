from math import e, log
from random import random, randint
from data_reader import *



def sigmoid(x: float) -> float:
    try:
        k = e**x
        return k / (k+1)
    except OverflowError:
        return 1


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
    # return [step * slopes[i]  for i in range(len(weights))]


def learn(data: list[list], real_data: list[list], weight: list[float], bias: float, step: float) -> tuple[list[float], float]:
    # n = len(data)
    # weight_add = [0] * len(weight)
    # bias_add = 0
    weight_rlt = weight.copy()
    bias_rlt = bias
    for i in range(len(data)):
        prediction = predict(data[i], weight_rlt, bias_rlt)
        weight_rlt = learn_row(weight_rlt, slope(real_data[i][0], prediction, data[i]), step)
        # for j,x in enumerate(learn_row(weight, slope(real_data[i][0], prediction, data[i]), step)):
        #     weight_add[j] += x
        # bias_add += learn_row([bias], slope(real_data[i][0], prediction), step)[0]
        bias_rlt = learn_row([bias_rlt], slope(real_data[i][0], prediction), step)[0]

    # return [weight[i] + weight_add[i] / n for i in range(len(weight))], bias + bias_add / n
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
# weight = [random() for _ in range(len(data_split[1][0]))]
weight = [0] * len(data_split[1][0])
# bias = random() * 5 - 2
bias = random()


# err_pred = predict(data_split[1][-1], weight, bias)
# print(err(data_split[2][-1][0], err_pred))
for i in range(10**4):
    weight, bias = learn(inputval, real_data, weight, bias, step)

    if i%10**3 == 0:
        print(f'{i//100}%')
        print(weight, bias)

for i in range(len(inputval)):
    print(predict(inputval[i], weight, bias), end = ' ')
    print(real_data[i])