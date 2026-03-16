import numpy as np

A = np.random.randn(64,64)
K = A.T @ A
vals = np.linalg.eigvalsh(K)
vals = np.sort(vals)[::-1]
print("gap:", vals[0]-vals[1])
