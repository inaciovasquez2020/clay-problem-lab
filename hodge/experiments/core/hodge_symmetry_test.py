import numpy as np

# mock Hodge diamond test
# H^{p,q} should satisfy H^{p,q} = H^{q,p}

def generate_hodge(n=4):
    H = np.random.randint(0,5,(n,n))
    for i in range(n):
        for j in range(n):
            H[j,i] = H[i,j]
    return H

H = generate_hodge()

print("Hodge matrix:")
print(H)

print("Symmetry check:", np.all(H == H.T))
