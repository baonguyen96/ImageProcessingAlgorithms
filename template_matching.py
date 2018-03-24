import numpy as np
import math
import scipy.signal


def non_normalized_correlation(lamda, f):
    c = scipy.signal.correlate2d(f, lamda)

    if is_print:
        print('non_normalized_correlation')
        print(c)
        print()

    return c


def get_match_measure_normalization(c, n2):
    h = len(c)
    w = len(c[0])
    q = np.zeros(shape=(h, w))

    for x in range(w):
        for y in range(h):
            if n2[y][x] == 0:
                q[y][x] = 0
            else:
                q[y][x] = (c[y][x]) / math.sqrt(n2[y][x])

    return q


def square(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            img[x][y] = img[x][y] ** 2
    return img


def fill_one(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            img[x][y] = 1
    return img


def normalized_correlation(lamda, f):
    c = non_normalized_correlation(lamda, f)

    f2 = square(f)
    if is_print:
        print('f2')
        print(f2)
        print()

    lamda1 = lamda.copy()
    fill_one(lamda1)
    if is_print:
        print('lamda1')
        print(lamda1)
        print()

    n2 = non_normalized_correlation(lamda1, f2)
    if is_print:
        print('n2')
        print(n2)
        print()

    q = get_match_measure_normalization(c, n2)
    if is_print:
        print('normalized_correlation')
        print(q)
        print()

    return q


# lamda = template, f = image
image = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 0]
]

template = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

is_print = False

print(normalized_correlation(template, image))
