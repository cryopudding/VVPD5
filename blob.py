import math


def m_cos(x, terms):
    result = 0
    for n in range(terms):
        result += (-1)**n * (x**(2*n)) / math.factorial(2*n)
    return result