
import math

def choose(n, r):
    d = math.factorial(n - r)
    r = math.factorial(r)
    n = math.factorial(n)

    return n // (r * d)


if __name__ == "__main__":
    result = []

    for n in range(1, 101):
        for r in range(1, n+1):
            ways = choose(n, r)
            if ways > 1000000:
                result.append(ways)

    print(len(result))
