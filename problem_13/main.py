#!/opt/miniconda3/bin/python

if __name__ == '__main__':

    s = 0
    numbers = []
    with open('./in') as f:

        line = f.readline()

        while line:

            numbers.append(line.strip())

            line = f.readline()

    for number in numbers:
        s += int(number)
        print(len(number))

    print(str(s)[:10])
