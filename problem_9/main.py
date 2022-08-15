
import math

def isPerfectSquareRoot(n):
    return math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n))

for i in range(1, 100000):
    for j in range(1, 100000):
        if (i < j):
            if (isPerfectSquareRoot(i ** 2 + j ** 2)):
                print(i, j, i + j + math.sqrt(i ** 2 + j ** 2))
                if 1000 == (i + j + round(math.sqrt(i ** 2 + j ** 2))):
                    print("Answer: ", i * j * math.sqrt(i ** 2 + j ** 2))
                    exit()
