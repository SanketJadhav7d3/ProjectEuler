
import math
import numpy as np

def get_triples(limit):
    triples = []

    for a in range(1, limit):
        for b in range(1, limit):
            c = a ** 2 + b ** 2
            if math.sqrt(c) == int(math.sqrt(c)):
                s = a + b + int(math.sqrt(c))
                # append perimeter
                triples.append(s)
    return triples

if __name__ == "__main__":
    tr = get_triples(1000)

    # get perimeter less than or equal to 1000
    tr = [x for x in tr if x <= 1000]
    
    max_count = tr[0]

    for t in tr:
        if tr.count(max_count) < tr.count(t):
            max_count = t

    # because triples whose sum are equal are repeated ex. (3, 4, 5) and (4, 3, 5) 
    # that's why count divided by 2
    print(max_count, tr.count(max_count) // 2)
