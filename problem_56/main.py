

if __name__ == "__main__":

    digital_sum = []
    for a in range(1, 100):
        for b in range(1, 100):
            digit = str(a ** b)
            s = 0
            for ch in digit:
                s += int(ch)

            digital_sum.append(s)

    print(max(digital_sum))
