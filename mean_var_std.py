import numpy as np


def calculate(data: list):
    # check if data is a list
    if len(data) != 9:
        raise ValueError("List must contain nine numbers.")

    # reshape data into 3x3 matrix
    matrix = np.array(data).reshape(3, 3)

    # calculate mean, variance, standard deviation, max, min, and sum
    mean = [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()]
    variance = [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()]
    std_dev = [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()]
    max_val = [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()]
    min_val = [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()]
    sum_flat = [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()]

    # wrapping result in a dictionary
    calculations = {
        "mean": mean,
        "variance": variance,
        "standard deviation": std_dev,
        "max": max_val,
        "min": min_val,
        "sum": sum_flat,
    }

    return calculations
