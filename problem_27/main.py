

def is_prime(n):
    if n <= 1:
        return False

    i = 2
    while i * i <= n:

        if n % i == 0:
            return False

        i += 1

    return True
        
def eq(a, b, n):
    return n ** 2 + a * n + b

if __name__ == '__main__':

    primes = [1]

    for a in range(2, 1000):
        if is_prime(a):
            primes.append(a)

    b = []

    for a in primes:
        b += [-1*a]

    for a in b:
        primes.append(a)


    ns = {}
    aa = []
    bb = []
    
    for a in primes:
        for b in primes:
            n = 1
            while n:
                pr = eq(a, b, n)
                if is_prime(pr):
                    aa.append(n)      
                    ns[n] = a * b
                    n += 1
                else:
                    break

    print(ns[max(aa)])

