
#!/opt/miniconda3/bin/python

from num2words import num2words

def getLength(s):
    length = 0
    for char in s:
        if char.isspace() or char == '-':
            continue
        length += 1

    return length

if __name__ == '__main__':
    words = 0
    for i in range(1, 1001):
        word = num2words(i)
        words += getLength(word)

    print(words)
