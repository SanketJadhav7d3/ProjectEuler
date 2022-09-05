

def are_permutations(a, b):
    a = [int(x) for x in str(a)]
    b = [int(x) for x in str(b)]

    if sorted(a) == sorted(b):
        return True

    return False

def permuted_multiples(num):
    multiples = []

    for n in range(2, 7):
        multiples.append(num * n)


    for i in range(len(multiples) - 1):
        for j in range(i+1, len(multiples)):
            if not are_permutations(multiples[i], multiples[j]):
                return False
    return True


if __name__ == "__main__":
    for i in range(1, 10000000):
        if permuted_multiples(i):
            print(i)
            break
