import numpy as np
import math
import scipy.signal


def non_normalized_correlation(lamda, f):
    return scipy.signal.correlate2d(f, lamda)


def get_match_measure_normalization(c, n2):
    h = len(c)
    w = len(c[0])
    q = np.zeros(shape=(h, w))

    for x in range(w):
        for y in range(h):
            q[y][x] = (c[y][x]) / math.sqrt(n2[y][x])

    return q


def square(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            v = img[x][y]
            img[x][y] = v ** 2
    return img


def fill_one(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            img[x][y] = 1
    return img


def normalized_correlation(lamda, f):
    c = non_normalized_correlation(lamda, f)
    f2 = square(f)
    lamda1 = lamda.copy()
    fill_one(lamda1)
    n2 = non_normalized_correlation(lamda1, f2)
    return get_match_measure_normalization(c, n2)


# lamda = template, f = image
image = [
    [4, 4, 4],
    [1, 2, 1]
]

template = [
    [1, 2, 1]
]

print('non_normalized_correlation')
print(non_normalized_correlation(template, image))
print()
print('normalized_correlation')
print(normalized_correlation(template, image))
