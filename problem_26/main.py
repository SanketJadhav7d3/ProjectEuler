
def get_recurring_length(n):
    numr = 1
    denr = n

    rem = numr % denr

    res = ""

    mp = {}

    while rem != 0 and rem not in mp:
        mp[rem] = len(res)

        rem = rem * 10

        res_part = rem // denr

        res += str(res_part)

        rem = rem % denr
    
    if rem == 0:
        return ""
    else:
        return res[mp[rem]:]


if __name__ == '__main__':
    count = 0
    l = {}

    for i in range(2, 1000):
        l[i] = len(get_recurring_length(i))
    
    valueMax = max(zip(l.values(), l.keys()))[1]

    print(valueMax)
