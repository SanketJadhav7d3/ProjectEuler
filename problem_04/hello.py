

def getReverse(n):
    n = str(n)
    return int(n[::-1])

def greatestPalindrome():

    greatest = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            if (i * j > greatest and i * j == getReverse(i * j)):
                greatest = i * j

    return greatest

g = greatestPalindrome()

print(g)
