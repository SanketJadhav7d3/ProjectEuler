

import numpy as np
import math


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def form_spiral(length):

    assert length > 1, "Value error"

    assert length % 2 != 0

    spiral = np.zeros((length, length))

    x = length // 2
    y = length // 2

    # grid contains 1 upto length ** 2 numbers in spiral manner
    total_num_count = length ** 2

    step = 1
    num_step = 1
    turn_counter = 1
    state = 0

    while step <= total_num_count:

        spiral[x][y] = step

        if state == 0:
            # go right
            y += 1

        if state == 1:
            # go up
            x -= 1

        if state == 2:
            # go left
            y -= 1

        if state == 3:
            # go down
            x += 1

        if step % num_step == 0:
            state = (state + 1) % 4
            turn_counter += 1

            if turn_counter % 2 == 0:
                num_step += 1

        step += 1

    s = set(np.diag(spiral).astype(int))

    s.update(np.diag(np.rot90(spiral)).astype(int))

    s = list(s)

    count = sum(map(is_prime, s))


    return (count / len(s)) * 100


if __name__ == "__main__":
    for i in range(5, 1000):
        if i % 2 != 0:
            ratio = form_spiral(i)
            print(ratio)
            if ratio < 10:
                break
