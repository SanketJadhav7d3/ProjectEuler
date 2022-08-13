
from math import lcm

if __name__ == '__main__':
    n = 1

    for i in range(1, 21):
        n = lcm(n, i)

    print(n)
