import numpy as np


def calculate_soft_max(number_array):
    return np.exp(number_array) / float(sum(np.exp(number_array)))


def cross_entropy(predictions, targets, epsilon=1e-12):
    predictions = np.clip(predictions, epsilon, 1. - epsilon)
    N = predictions.shape[0]
    ce = -np.sum(np.sum(targets*np.log(predictions+1e-9)))/N
    return ce


predictions = np.array([
    [0.25, 0.25, 0.25, 0.25]
])
targets = np.array([
    [1, 0, 0, 0]
])


# print(calculate_soft_max([1, -2, 3, -4]))
# print(calculate_soft_max([1, 2, -3, 0]))

print(cross_entropy(predictions, targets))
