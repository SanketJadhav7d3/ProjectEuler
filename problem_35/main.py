
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_circular_prime(n):
    n = str(n)
    rotated = n
    rotations = []

    for i in range(len(n)):
        # take the last n - 1 elements
        rotated = rotated[1:] + rotated[0]
        rotations.append(int(rotated))

    for i in rotations:
        if not is_prime(i):
            return False
    return True


if __name__ == '__main__':
    circular_primes = []
    for i in range(2, 1000000):
        if is_circular_prime(i):
            print(i)
            circular_primes.append(i)

    print(circular_primes, len(circular_primes))
