def apply_types(target: list, types: list) -> list:
    return [types[i](target[i]) for i in range(len(target))]


def read_csv(path: str, types: list) -> list[list]:
    '''
    converts csv file to 2-dimentional list
    types must be a list of types;
    ex) [str, str, int, float, float ... ]
    '''

    rlt = []
    with open(path, 'r') as file:
        if rlt == []:
            rlt.append(file.readline().strip().split(','))

        while file.read(1):
            rlt.append(apply_types(file.readline().strip().split(','), types))

    return rlt

print(*read_csv('./inputs/darwin (testdata).csv', [int, str, str] + [float] * 19 + [int, int]), sep = '\n')