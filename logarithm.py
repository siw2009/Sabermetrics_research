def log(x, base, steps: int = 10**5, f = lambda x: 1/x) -> float:
    return ln(x, steps, f) / ln(base, steps, f)


def ln(x, steps: int = 10**5, f = lambda x: 1/x) -> float:
    rlt = 0
    width = (x-1) / steps

    for i in range(1, (steps-1)//2 +1):
        rlt += 2 * f(1 + width * i * 2)
    # for i in range(1, steps//2 +1):
        rlt += 4 * f(1 + width * (2 * i -1))
    
    if steps&1 == 0:
        rlt += 4 * f(1 + width * (steps -1))

    return (rlt + f(1) + f(x)) / 3 * width


import sys
sys.setrecursionlimit(10**8)
def get_e(low: float = 1.0, high: float = 3.0, x: int = 0, depth: int = 100, log_steps: int = 10000) -> float:
    m = (low + high) / 2
    if x == depth:  return m

    k = ln(m, log_steps)
    if k < 1:
        return get_e((low + m) / 2, high, x+1, depth)
    else:
        return get_e(low, (high + m) / 2, x+1, depth)



e = get_e()