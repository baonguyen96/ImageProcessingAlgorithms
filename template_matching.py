import numpy as np
import math
import scipy.signal


def non_normalized_correlation(lamda, f):
    return scipy.signal.correlate2d(f, lamda)


def get_match_measure_normalization(c, n2):
    h = len(c)
    w = len(c[0])
    q = np.zeros(shape=(w, h))

    for x in range(w):
        for y in range(h):
            q = (c[x][y]) / math.sqrt(n2[x][y])

    return q


def normalized_correlation(lamda, f):
    c = non_normalized_correlation(lamda, f)
    f2 = f * f
    lamda1 = lamda.copy()
    lamda1.fill(1)
    n2 = non_normalized_correlation(lamda1, f2)
    return get_match_measure_normalization(c, n2)


# lamda = template, f = image
image = [
    [1, 0, 2, 2, 10],
    [1, 0, 2, 2, 10],
    [1, 0, 1, 2, 10]
]

template = [
    [0, 2],
    [1, 2]
]

print(non_normalized_correlation(template, image))
