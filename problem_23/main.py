
import math

def get_divisor_sum(n):
    result = 0
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            if i == n / i:
                result += i
            else:
                result += i + (n // i)
        i += 1
    return result + 1

def get_abundant_numbers(start, end):
    abundant_numbers = []
    for i in range(start, end):
        if get_divisor_sum(i) > i:
            abundant_numbers.append(i)
    return abundant_numbers

if __name__ == '__main__':
    
    # get all the abundand numbers between 12 and 28123
    abundant_numbers = get_abundant_numbers(12, 28123)

    abundant_sum = set([])

    # get the sum of all abundand numbers 
    for a in abundant_numbers:
        for b in abundant_numbers:
             s = a + b
             if s > 28123:
                 break
             else:
                 abundant_sum.add(s)

    answer = [x for x in range(28123) if x not in abundant_sum]

    print(sum(answer))
