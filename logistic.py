from random import random
def generate_x(path: str, start: float, end: float, cnt: int):
    rlt = [random() * (end - start) + start for _ in range(cnt)]
    with open(path, 'w') as f:  f.write('')
    with open(path, 'a') as f:
        for x in rlt:
            f.write(str(x) + '\n')

generate_x('./inputs/x1-input.txt', -100, 100, 10000)
generate_x('./inputs/x2-input.txt', 0, 1000, 10000)