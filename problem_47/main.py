

def prime_factors(n):
    c = 2
    s = set()
    while (n > 1):
        if n % c == 0:
            s.add(c)
            n /= c
        else:
            c += 1
    return s

def is_distinct(nums):

    # calculate the factors of nums
    factors = []
    for n in nums:
        factors.append(prime_factors(n))

    # len of all elements of factors should be 4
    # and factors should be distince
    for f in factors:
        if len(f) != len(nums):
            return False

    for i in range(len(factors) - 1):
        for j in range(i+1, len(factors)):
            if factors[i] == factors[j]:
                return False
    return True


if __name__ == "__main__":
    for i in range(1000, 100000):
        print(i)
        if is_distinct(list(range(i, i+4))):
            print("Answer: ", i)
            break
