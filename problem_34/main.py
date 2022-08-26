
import math

def factorial_digit_sum(a):
    s = 0
    for ch in str(a):
        s += math.factorial(int(ch))
    return s

if __name__ == '__main__':

    s = 0
    for i in range(3, 10000000):
        if factorial_digit_sum(i) == i:
            print(i)
            s += i
    print(s)
