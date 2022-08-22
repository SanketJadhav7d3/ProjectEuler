import math

def get_sum(n):
    s = 0
    for digit in str(n):
        s += (int(digit) ** 5)
    return s


if __name__ == '__main__':

    numbers = []

    r = round(math.log10(9 ** 5)) * 9 ** 5

    for i in range(2, r):
        if i == get_sum(i):
            numbers.append(i)

    print(numbers, sum(numbers))
