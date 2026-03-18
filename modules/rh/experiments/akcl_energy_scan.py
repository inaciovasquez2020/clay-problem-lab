import numpy as np

def weight(x):
    return np.exp(-x)

def f_sample(xs):
    return xs - np.mean(xs)

def energy(xs):
    E = 0.0
    for x in xs:
        for y in xs:
            E += (x - y)**2 * weight(x) * weight(y)
    return E

xs_list = [np.linspace(0.5, L, 20) for L in [2,3,4,5]]

for xs in xs_list:
    f = f_sample(xs)
    E = energy(xs)
    norm = np.sum(f**2 * weight(xs))
    print("L =", xs[-1], "E/norm =", E / norm)
