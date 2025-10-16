def default_values(typestr):
    match typestr:
        case '<class \'int\'>' | '<class \'float\'>':
            return 0
        case '<class \'str\'>':
            return ''
        case _:
            return None


def apply_types(target: list, types: list) -> list:
    rlt = []
    for i in range(len(target)):
        try:
            rlt.append(types[i](target[i]))
        except ValueError:
            rlt.append(default_values(str(types[i])))
        except IndexError:
            rlt.append(None)
    
    return rlt


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



def merge_data(data1: list[list], data2: list[list]) -> list[list]:
    length = min(len(data1), len(data2))
    return [data1[i] + data2[i] for i in range(length)]