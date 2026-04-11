import numpy as np

v = np.random.randn(64, 64, 3)
grad = np.gradient(v, axis=(0, 1))
enstrophy = sum((g**2).sum() for g in grad)
print("enstrophy:", enstrophy)
