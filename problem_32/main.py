#!/usr/local/bin/python3

import math

digits = [str(x) for x in range(1, 10)]

def is_pandigital(multiplicand, multiplier, product):
    global digits
    n = []

    n.extend([x for x in str(multiplicand)])
    n.extend([x for x in str(multiplier)])
    n.extend([x for x in str(product)])

    if len(n) == len(digits):
        if sorted(n) == sorted(digits):
            return True
        else:
            return False
    else:
        return False


def of_product(n):

    ways = []
    for i in range(1, int(math.sqrt(n)) + 1):

        if (n % i != 0):
            continue
        j = n // i

        ways.append([i, j])
        
    return ways

if __name__ == '__main__':

    result = set()
    for i in range(2, 100000):
        res = of_product(i)
        for r in res:
            if is_pandigital(r[0], r[1], i):
                result.add(i)
                break

    print(sum(result))
