
def hexagonal(n):
    return (n * (n + 1)) // 2

def triangle(n):
    return n * (3 * n - 1) // 2

def pentagon(n):
    return n * (2 * n - 1)

if __name__ == "__main__":
    triangles = []
    pentagons = []
    hexagonals = []

    for i in range(1, 100000):
        triangles.append(triangle(i))
        pentagons.append(pentagon(i))
        hexagonals.append(hexagonal(i))

    for t in triangles:
        if t in pentagons and t in hexagonals:
            print(t)
