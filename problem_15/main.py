#!/opt/miniconda3/bin/python

import math

def get_ways(rows, cols):
    total = rows + cols

    num = math.factorial(total)
    den = math.factorial(rows) * math.factorial(cols)

    return num // den

if __name__ == '__main__':
    rows = 20
    cols = 20

    print(get_ways(20, 20))
