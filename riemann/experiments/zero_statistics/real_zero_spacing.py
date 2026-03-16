import numpy as np
from pathlib import Path

path = Path("riemann/data/zeros/zeros1.txt")

vals = []
with open(path) as f:
    for line in f:
        try:
            vals.append(float(line.strip()))
        except:
            pass

vals = np.array(vals)
spacings = np.diff(vals)

print("zeros loaded:", len(vals))
print("mean spacing:", spacings.mean())
print("variance:", spacings.var())
print("first spacings:", spacings[:10])
