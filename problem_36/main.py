
def is_palindrome(n):
    b = format(n, 'b')
    n = str(n)

    if b == b[::-1] and n == n[::-1]:
        return True
    return False

if __name__ == '__main__':
    s = 0
    for i in range(1, 1000000):
        if is_palindrome(i):
            print(i)
            s += i

    print("Sum: ", s)
