
from itertools import permutations 

def list_to_num(l):
    n = ""
    for e in l:
        n += str(e)
    return int(n)

def special_property(n):
    primes = [2, 3, 5, 7, 11, 13, 17] 
    i = 1
    flag = True
    while (i + 2) < len(n):
        if list_to_num(n[i:i+3]) % primes[i - 1] != 0:
            flag = False
            return flag
        i += 1
    return flag

if __name__ == "__main__":
    per = list(permutations(range(0, 9+1)))
    result = []
    for l in per:
        if special_property(l):
            result.append(list_to_num(l))
            print(list_to_num(l))

    print(result, sum(result))
