
if __name__ == '__main__':
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    table = [0 for _ in range(target + 1)]

    table[0] = 1

    for i in range(len(coins)):
        for j in (coins[i], target + 1):
            table[j] += table[j - coins[i]];

    print(table)
