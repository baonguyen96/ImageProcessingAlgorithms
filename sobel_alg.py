import numpy as np
import math


def sobel(window):
    x = np.matrix(
        '-1 0 1; '
        '-2 0 2; '
        '-1 0 1'
    )

    y = np.matrix(
        '-1 -2 -1; '
        '0 0 0; '
        '1 2 1'
    )

    delta_x = 0
    delta_y = 0

    for ix in range(3):
        for iy in range(3):
            delta_x += x[ix, iy] * window[ix, iy]
            delta_y += y[ix, iy] * window[ix, iy]

    return math.sqrt(delta_x ** 2 + delta_y ** 2)


def main():
    window = np.matrix(
        '9 9 9; '
        '9 9 9; '
        '9 9 9'
    )

    print(sobel(window))


main()
