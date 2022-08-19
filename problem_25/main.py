
def get_digits(n):
    return len(str(n))

if __name__ == '__main__':
    a = 1 
    b = 1

    digit_count = 0
    index = 2

    while digit_count < 1000:

        fib = a + b
        a = b
        b = fib

        index += 1

        print(index, fib)

        digit_count = get_digits(fib)

    print("Answer: ", index)
