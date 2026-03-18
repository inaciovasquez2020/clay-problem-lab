import numpy as np

def weight(x):
    return np.exp(-x)

def tail_mass(xs, cutoff):
    mask = xs >= cutoff
    return np.sum(weight(xs[mask]))

for L in [2, 3, 4, 5, 6, 8, 10]:
    xs = np.linspace(0.5, L, 400)
    cutoff = 0.8 * L
    print("L =", L, "cutoff =", cutoff, "tail_mass =", tail_mass(xs, cutoff))
