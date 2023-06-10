

import math
from fractions import Fraction
    

def construct(n):
    fraction = Fraction(1, 2)

    for i in range(n):
        fraction = 2 + fraction
        fraction = Fraction(1, fraction) 
    fraction += 1

    return int(math.log10(fraction.numerator)) + 1 > int(math.log10(fraction.denominator)) + 1
        

if __name__ == "__main__":
    count = 0
    for i in range(1000):
        print(i)
        if construct(i):
            count += 1

    print("Total count", count)
