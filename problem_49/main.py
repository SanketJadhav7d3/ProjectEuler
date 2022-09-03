
import math

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def are_primes(primes):
    for prime in primes:
        if not is_prime(prime):
            return False

    return True

def permutations(primes):

    perms = []
    for prime in primes:
        perms.append([x for x in str(prime)])

    for i in range(len(perms) - 1):
        for j in range(i+1, len(perms)):
            if perms[i] != perms[j] and sorted(perms[i]) == sorted(perms[j]):
                continue
            return False
    return True


def construct_nums(n):
    l = []
    for i in range(0, 3):
        l.append(n)
        n += 3330
    return l

if __name__ == "__main__":

    for i in range(1000, 10000):
        l = construct_nums(i)
        if are_primes(l) and permutations(l):
            print(*l)
