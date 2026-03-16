import numpy as np

def mock_zeros(n):
    # placeholder for imaginary parts of zeta zeros
    return np.sort(np.random.rand(n) * 100)

zeros = mock_zeros(200)
spacings = np.diff(zeros)

print("mean spacing:", np.mean(spacings))
print("variance:", np.var(spacings))
print("first spacings:", spacings[:10])
