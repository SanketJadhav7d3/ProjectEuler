
import math

def is_composite(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True

    return False

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def is_twice_square(n):
    s = math.sqrt(n / 2)
    return s - int(s) == 0

def can_be(n):
    for i in range(1, n):
        if is_prime(i):
            dif = n - i
            if is_twice_square(dif):
                return True

    return False

if __name__ == "__main__":
    composites = [x for x in range(1, 100000) if is_composite(x) and x % 2 != 0]
    for i in composites:
        if not can_be(i):
            print(i)
            break
