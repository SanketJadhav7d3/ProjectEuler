#!/opt/miniconda3/bin/python


import math
import numpy as np


if __name__ == '__main__':

    in_file = open('in', 'r') 

    row = 20
    col = 20

    product = 1

    grid = []

    for i in range(row):
        line = in_file.readline().strip()
        grid.append(list(map(int, line.split())))

    grid = np.asarray(grid)

    # left and right
    for r in grid:
        for i in range(len(r) - 4):
            if product < math.prod(r[i:i+4]):
                product = math.prod(r[i:i+4])
    
    # rotate the grid
    rotated_grid = grid.transpose()


    # up and down
    for r in rotated_grid:
        for i in range(len(r) - 4):
            if product < math.prod(r[i:i+4]):
                product = math.prod(r[i:i+4])

    # for diagonal elements
    for i in range(-19, 20):
        diag = grid.diagonal(i)
        if diag.size >= 4:
            for j in range(0, diag.size - 4 + 1):
                if np.prod(diag[j:j+4]) > product:
                    product = np.prod(diag[j:j+4])

    grid = np.fliplr(grid)

    # for reverse diagomal elements
    for i in range(-19, 20):
        diag = grid.diagonal(i)
        if diag.size >= 4:
            for j in range(0, diag.size - 4 + 1):
                if np.prod(diag[j:j+4]) > product:
                    product = np.prod(diag[j:j+4])

    print(product)
