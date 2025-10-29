from logistic import predict



SAVEFILEPATH = './logistic_savefile/1761722135.5357535.txt'
with open(SAVEFILEPATH, 'r') as file:
    weight = []
    for _ in range(15):
        weight.append(float(file.readline().strip()))
    bias = float(file.readline().strip())


inputs = list(map(float, input('Input following data of a player:\nAB BB SO SB CS BB/(AB+BB) SO/(AB+BB) (SB+CS)/(AB+BB) SB/(SB+CS)\n').split()))
print(predict(inputs, weight, bias))