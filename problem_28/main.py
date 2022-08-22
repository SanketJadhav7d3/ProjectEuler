
def add_diagonals(rows, cols):

    starting_value = 1
    row_diff = 2
    inner_matrix_size = 3
    matrix_size = rows * cols
    s = 1

    # matrix size with each step will increase by 2
    # row diff will increase by 2 when the matrix size increases
    while (inner_matrix_size * inner_matrix_size <= matrix_size):
        while (starting_value <= inner_matrix_size * inner_matrix_size and starting_value < matrix_size):
            if starting_value == inner_matrix_size * inner_matrix_size:
                row_diff += 2
            starting_value += row_diff
            s += starting_value
        inner_matrix_size += 2
    print(s)


if __name__ == '__main__':
    rows = 1001
    cols = 1001

    add_diagonals(rows, cols)
