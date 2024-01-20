import numpy as np


def vectorization_example_a():
    b = 4
    w = np.array([1.0, 2.5, -3.3])
    x = np.array([10, 20, 30])
    f = 0
    n = 3
    for j in range(n):
        f = f + w[j] * x[j]
    f = f + b
    return f


def vectorization_example_b():
    b = 4
    w = np.array([1.0, 2.5, -3.3])
    x = np.array([10, 20, 30])
    f = np.dot(w, x) + b
    return f


if __name__ == '__main__':
    print(vectorization_example_a())
    print(vectorization_example_b())
