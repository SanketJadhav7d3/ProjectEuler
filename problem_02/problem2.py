
s = 0
fib = 0
a = 0
b = 1

while (fib < 4000000):
    fib = a + b
    a, b = b, fib
    if (fib % 2 == 0):
        s += fib


print(s)
