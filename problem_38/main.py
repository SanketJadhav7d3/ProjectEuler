
def form_pandigital(n, r):
    result = ""

    for i in range(1, r + 1):
        result += str(n * i)

    return result

def is_pandigital(n):

    pandigital = [x for x in range(1, 10)]
    s = list()
    for char in str(n):
        s.append(int(char))

    if sorted(pandigital) == sorted(s):
        return True

    return False

if __name__ == "__main__":

    # start with 1
    # multiply numbers ranging from 1 to n untill the concatenated product contains 9 digits
    # if concatenated product is pandigital then append
    # increment starting value

    pandigital_nums = []
    for i in range(1, 1000000):
        r = 1
        result = ""
        while len(result) < 9:
            result = form_pandigital(i, r)
            r += 1

        if len(result) == 9 and is_pandigital(int(result)):
            print(i, result)
            pandigital_nums.append(int(result))

    print(max(pandigital_nums))
