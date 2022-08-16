#!/opt/miniconda3/bin/python

def generatechain(n):
    count = 1
    while (n > 1):
        if (n % 2 != 0):
            n = 3 * n + 1
        else:
            n //= 2
        count += 1
    return count

if __name__ == '__main__':
    count = 1
    i = 0
    for i in range(2, 1000000):
        if count < generatechain(i):
            count = generatechain(i)
            print(i, count)
