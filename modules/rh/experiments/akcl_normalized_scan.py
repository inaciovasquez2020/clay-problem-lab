import numpy as np

def weight(x):
    return np.exp(-x)

def kernel(x,y):
    return (x-y)**2

def energy(xs):
    E = 0.0
    for x in xs:
        for y in xs:
            E += kernel(x,y) * weight(x) * weight(y)
    return E

def D(xs):
    vals = []
    for x in xs:
        s = 0.0
        for y in xs:
            s += kernel(x,y) * weight(y)
        vals.append(s)
    return max(vals)

def f_sample(xs):
    return xs - np.mean(xs)

for L in [2,3,4,5]:
    xs = np.linspace(0.5, L, 20)
    f = f_sample(xs)
    E = energy(xs)
    norm = np.sum(f**2 * weight(xs))
    d = D(xs)
    print("L =", L, "E_norm/norm =", (E/d)/norm)
