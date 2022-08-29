
def get_nth_triangle(n):
    return (n * (n + 1)) // 2

def get_sum(s):
    result = 0
    for ch in s:
        result += ord(ch.lower()) - 96
    return result

if __name__ == "__main__":
    triangle_words = []

    with open("words.txt", "r") as f:
        words = f.readline().split(",")
        words = list(map(lambda x : x.replace('"', ''), words))

    for word in words:
        s = get_sum(word)
        i = 1
        t = get_nth_triangle(i)

        while t <= s:
            t = get_nth_triangle(i)
            i += 1
            if t == s:
                triangle_words.append(word)

    print(len(triangle_words))
