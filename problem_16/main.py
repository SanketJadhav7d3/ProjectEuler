#!/opt/miniconda3/bin/python

if __name__ == '__main__':
    a = 2 ** 1000

    s = str(a)

    total_sum = 0

    for i in s:
        total_sum += int(i)

    print(total_sum)
