
from fractions import Fraction

def remove_comman(a, b):
    a, b = [i for i in a if i not in b], [i for i in b if i not in a]
    return a, b

unique_fraction = []

def unique_fractions(a, b):

    digits_a = [int(x) for x in str(a)]
    digits_b = [int(x) for x in str(b)]

    num, den = Fraction(a, b).as_integer_ratio()

    # remove the fractions which cannot be reduced further
    if a == num or b == den:
        return False

    # remove trival examples
    if a % 10 == 0 and b % 10 == 0:
        return False

    digits_a, digits_b = remove_comman(digits_a, digits_b)

    if len(digits_a) == 1 and len(digits_b) == 1 and 0 not in digits_a and 0 not in digits_b:
        f = Fraction(digits_a[0], digits_b[0])
        if f.numerator == num and f.denominator == den:
            unique_fraction.append(f)

if __name__ == '__main__':
    for a in range(10, 99):
        for b in range(10, 99):
            if a / b < 1:
                unique_fractions(a, b)

    result = Fraction(1, 1)
    for f in unique_fraction:
        result *= f

    print("The unique fractions: ", *unique_fraction)
    print("Their denominator: ", result.denominator)
