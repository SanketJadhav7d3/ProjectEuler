
import string 

def get_value(name):
    value = 0
    for ch in name:
        value += string.ascii_uppercase.index(ch) + 1

    return value

if __name__ == '__main__':

    f = open('names.txt', 'r')

    names = f.readline().split(",")

    # remove double quotes from names list elements
    names = list(map(lambda x: eval(x), names))

    names = sorted(names)

    total_value = 0

    for index, name in enumerate(names):
        total_value += (get_value(name) * (index + 1))

    print(total_value)
