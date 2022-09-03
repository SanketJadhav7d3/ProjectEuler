
import math

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def sieve(n):
    is_primes = [True for _ in range(1, n)]

    i = 2
    while i * i < len(is_primes):
        if is_primes[i]:
            for j in range(i*i, len(is_primes), i):
                is_primes[j] = False
        i += 1

    primes = []
    for i in range(2, len(is_primes)):
        if is_primes[i]:
            primes.append(i)
    return primes


if __name__ == "__main__":
    limit = 1000000
    primes = sieve(limit)
    s = 0
    result = []
    for i in range(len(primes)):
        r = i+2
        while r < len(primes):
            s = sum(primes[i:r])
            if is_prime(s) and s < limit:
                print(s)
                result.append((s, len(primes[i:r])))
            if s >= limit:
                break
            r += 1

    # sort the list by number of consecutive primes

    result.sort(key=lambda x: x[1])
    print("Answer: ", result[-1])
