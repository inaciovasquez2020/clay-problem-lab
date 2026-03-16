import numpy as np

def gram_matrix(n):
    A = np.random.randn(n,n)
    return (A + A.T)/2

G = gram_matrix(64)
vals = np.linalg.eigvalsh(G)

print("top eigenvalues:", vals[-5:])
