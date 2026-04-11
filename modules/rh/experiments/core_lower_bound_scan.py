import numpy as np


def weight(x):
    return np.exp(-x)


def f_sample(xs):
    f = xs - np.mean(xs)
    norm = np.sqrt(np.sum((f**2) * weight(xs)))
    return f / norm


def core_mass(xs, theta):
    f = f_sample(xs)
    core = xs <= theta * xs[-1]
    return np.sum((f[core] ** 2) * weight(xs[core]))


for L in [2, 3, 4, 5, 6, 8, 10]:
    xs = np.linspace(0.5, L, 400)
    cm = core_mass(xs, 0.8)
    print("L =", L, "core_mass =", cm)
