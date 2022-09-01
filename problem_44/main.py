
import math
import os

def get_pentagon_num(n):
    return (n * (3 * n - 1)) // 2

def is_pentagon(n):
    i = 1
    while i <= n:
        p = get_pentagon_num(i)
        if p == n:
            return True
        i += 1
    return False

if __name__ == "__main__":
    pentagon_nums = []
    for i in range(1, 100000):
        pentagon_nums.append(get_pentagon_num(i))

    for i in range(0, len(pentagon_nums)):
        for j in range(i+1, len(pentagon_nums)):
            a = pentagon_nums[i] + pentagon_nums[j]
            b = abs(pentagon_nums[i] - pentagon_nums[j])
            if a in pentagon_nums and b in pentagon_nums:
                print(a, b)
