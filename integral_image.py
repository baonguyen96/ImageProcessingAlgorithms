import numpy as np


def compute_integral_image(image):
    row = len(image)
    col = len(image[0])

    integral_image = np.zeros(shape=(row, col))

    # compute each columns
    for r in range(row):
        for c in range(col):
            if c - 1 >= 0:
                integral_image[r][c] = integral_image[r][c - 1] + image[r][c]
            else:
                integral_image[r][c] = image[r][c]

    # compute each rows
    for r in range(row):
        for c in range(col):
            if r - 1 >= 0:
                integral_image[r][c] = integral_image[r - 1][c] + integral_image[r][c]
            else:
                integral_image[r][c] = integral_image[r][c]

    return integral_image


def compute_sum_in_window(image, x1, y1, x2, y2):
    sum_of_window = 0

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            sum_of_window += image[y][x]

    return sum_of_window


original_image = [
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 2, 2, 2, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(compute_integral_image(original_image))
