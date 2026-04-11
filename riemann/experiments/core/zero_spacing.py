import numpy as np


def spacing(vals):
    vals = np.sort(vals)
    return np.diff(vals)


zeros = np.random.rand(100)
print(spacing(zeros)[:10])
