
if __name__ == '__main__':

    in_file = open('in', 'r')

    triangle = []

    line = in_file.readline()

    while line:
        triangle.append(list(map(int, line.strip().split())))

        line = in_file.readline()

    # go from bottom to top
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    print("Maximum path sum: ", triangle[0][0])
