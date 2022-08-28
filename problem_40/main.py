
from os.path import exists

if __name__ == '__main__':

    irrational = ""

    if exists("irrational.txt"):
        f = open("irrational.txt", 'r')
        irrational = f.read()

    else:
        f = open("irrational.txt", 'w')
        irrational = "0." 
        for i in range(1, 1000001):
            irrational += str(i)

        f.write(irrational)

    d = 1
    result = 1
    while d <= 1000000:
        print(irrational[d + 2 - 1], d + 2 - 1)
        result *= int(irrational[d + 2 - 1])
        d *= 10

    print(result)
