
def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False

def rev_num(n):
    n = str(n)
    return int(n[::-1])

def is_lychrel(n):

    for i in range(1, 51):
        s = n + rev_num(n)
        if is_palindrome(s):
            break
        n = s
    else:
        return True

    return False


if __name__ == "__main__":

    c = 0
    for i in range(1, 10001):
        if is_lychrel(i):
            print(i)
            c += 1

    print(c)
