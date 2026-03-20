import numpy as np


def integral_computation(f, size):
    x_values = np.random.rand(size)
    f_values = [f(x0) for x0 in x_values]
    avg = np.mean(f_values)
    return avg

f = lambda x: x**2
N = 10**6
integral = integral_computation(f, N)
print(integral)