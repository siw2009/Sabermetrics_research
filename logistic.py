from newrandom import *
from logarithm import *
from data_reader import *



def sigmoid(x: float) -> float:
    try:
        k = e**x
        return k / (k+1)
    except OverflowError:
        return 1


# def create_sigmoidLUT(start: float, end: float, datacount: int, filepath: str = './sigmoidLUT.csv'):
#     with open(filepath, 'w') as file:  file.write('')
#     with open(filepath, 'a') as file:
#         for x in range(datacount):
#             value = (start * (datacount - x -1) + end * x) / (datacount -1)
#             file.write(f' {value}, {sigmoid(value)},')
#             file.write('\n')

# create_sigmoidLUT(-745.2, 37.44, 2*10**6)
# exit()


def load_sigmoidLUT(filepath: str = './sigmoidLUT.csv') -> list[tuple[float, float]]:
    rlt = []
    with open(filepath, 'r') as file:
        while file.read(1):
            rlt.append(tuple(map(float, file.readline().split(',')[:-1])))

    return rlt


def sigmoidLUT_bisect(x: float, LUT: list[tuple[float, float]], low: int, high: int) -> float:
    if low >= high:  return LUT[low][1]

    print(low, high)
    m = (low + high) // 2
    if LUT[m][0] > x:
        return sigmoidLUT_bisect(x, LUT, low, m-1)
    else:
        return sigmoidLUT_bisect(x, LUT, m, high)


def sigmoidLUT(x: float, LUT: list[tuple[float, float]]) -> float:
    '''
    sigmoid LUT must be formatted as list of

    ### **(*x value*, *the sigmoid value of the corresponding x value*)**
    '''

    if x < LUT[0][0]:  return LUT[0][1]
    if x > LUT[-1][0]:  return LUT[-1][1]
    return sigmoidLUT_bisect(x, LUT, 0, len(LUT)-1)


# print(load_sigmoidLUT()[:100])
print(sigmoidLUT(10, load_sigmoidLUT()))
print(sigmoid(10))
exit()


def discrete(x: float) -> int:
    return 1  if x>0.5 else  0


def predict(input_data: list[float], weights: list[float], bias: float) -> float:
    # print(sum([input_data[i] * weights[i] for i in range(len(weights))]) + bias)
    return sigmoid(sum([input_data[i] * weights[i] for i in range(len(weights))]) + bias)


def slope(realdata: int, prediction: float, inputval: list[float] = [1.0]) -> list[float]:
    return [(realdata - prediction) * x for x in inputval]


def err(realdata: int, prediction: float) -> float:
    if prediction == 1:  return 0
    return (realdata-1) * ln(-prediction+1) - realdata * ln(prediction)


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


step = 0.00001
# inputval = [random() * 6 -3  for _ in range(2)]
inputval = data_split[1][:-1]
# real_data = randint(0,1)
real_data = data_split[2][:-1]
# weight = [random() for _ in range(len(data_split[1][0]))]
weight = [0] * len(data_split[1][0])
# bias = random() * 5 - 2
bias = random()


n = 10**5
for i in range(n):
    weight, bias = learn(inputval, real_data, weight, bias, step)

    if i%10**3 == 0:
        # print(weight, bias)

        for j in range(len(inputval)):
            print(predict(inputval[j], weight, bias), end = ' ')
            print(real_data[j])
        print(f'{i*100//n}%')
        print('-' * 100)