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


def split_data(data: list[list], split_by: tuple) -> list[list[list]]:
    if sum(split_by) > len(data[0]):  return []
    for i in split_by:
        if i<0:  return []

    rlt = [[] for _ in range(len(split_by))]
    for i in range(len(data)):
        idx = 0
        for j in range(len(split_by)):
            rlt[j].append(data[i][idx:idx + split_by[j]])
            idx += split_by[j]
    
    return rlt