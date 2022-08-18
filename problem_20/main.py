
import math

if __name__ == '__main__':

    a = str(math.factorial(100))
    
    s = 0

    for c in a:
        s += int(c)

    print(s)
