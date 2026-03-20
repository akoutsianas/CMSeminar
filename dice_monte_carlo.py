import numpy as np


def dice(size):
    rng = np.random.default_rng()
    observations = rng.integers(low=1, high=7, size=size)
    avg = np.mean(observations)
    return avg


size = 10**8
print(dice(size))