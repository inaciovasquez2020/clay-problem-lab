import numpy as np

def weight(x):
    return np.exp(-x)

def f_sample(xs):
    return xs - np.mean(xs)

def mass_ratio(xs, theta):
    f = f_sample(xs)
    core = xs <= theta * xs[-1]
    tail = xs > theta * xs[-1]
    core_mass = np.sum((f[core]**2) * weight(xs[core]))
    tail_mass = np.sum((f[tail]**2) * weight(xs[tail]))
    return tail_mass / core_mass if core_mass > 0 else np.inf

for L in [2,3,4,5,6,8,10]:
    xs = np.linspace(0.5, L, 400)
    ratio = mass_ratio(xs, 0.8)
    print("L =", L, "tail/core =", ratio)
