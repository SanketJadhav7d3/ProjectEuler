
import math

def d(n):
    '''
        returns the sum of the proper divisors of n
    '''
    i = 2 
    s = 0
    while i <= math.sqrt(n): 
        if n % i == 0:
            if n / i == i:
                s += i
            else:
                s += i + (n // i)
        i += 1
    return s + 1


if __name__ == '__main__':
    s = 0
    amicable_nums = []

    for a in range(1, 10000):
        b = d(a)
        if d(b) == a and a != b:
            # to make sure that same pairs do not get added to the list
            if a not in amicable_nums:
                amicable_nums.extend([a, b])

    print(sum(amicable_nums))
