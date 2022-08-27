
import math

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def unique_prime(n):
    n = str(n)
    flag = True
    # from left to right
    for i in range(len(n)):
        if not is_prime(int(n[i:])):
            flag = False

    # from right to left
    for i in range(1, len(n)):
        if not is_prime(int(n[:-i])):
            flag = False

    return flag


if __name__ == '__main__':
    unique_primes = []
    for i in range(10, 1000000):
        if unique_prime(i):
            unique_primes.append(i)
    
    print(len(unique_primes), unique_primes, sum(unique_primes))
