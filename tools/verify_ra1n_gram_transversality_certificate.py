#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

CERT = Path("artifacts/ra1n/gram_transversality_certificate.json")

def q(x: str) -> Fraction:
    return Fraction(str(x))

def solve_linear(A, b):
    n = len(A)
    M = [[A[i][j] for j in range(n)] + [b[i]] for i in range(n)]

    for col in range(n):
        pivot = None
        for row in range(col, n):
            if M[row][col] != 0:
                pivot = row
                break
        assert pivot is not None, "Gram matrix is singular"

        M[col], M[pivot] = M[pivot], M[col]

        piv = M[col][col]
        M[col] = [x / piv for x in M[col]]

        for row in range(n):
            if row == col:
                continue
            factor = M[row][col]
            if factor != 0:
                M[row] = [M[row][j] - factor * M[col][j] for j in range(n + 1)]

    return [M[i][n] for i in range(n)]

def main() -> int:
    data = json.loads(CERT.read_text())

    assert data["object"] == "RA1N exact finite-basis Gram transversality certificate"
    assert data["status"] == "conditional-angle-gap-certificate"
    assert data["certifies"] == "b^*G^{-1}b < 1"

    n = int(data["basis_dimension"])
    G = [[q(x) for x in row] for row in data["gram_matrix"]]
    b = [q(x) for x in data["b_vector"]]

    assert len(G) == n
    assert all(len(row) == n for row in G)
    assert len(b) == n

    for i in range(n):
        assert G[i][i] > 0
        for j in range(n):
            assert G[i][j] == G[j][i]

    c = solve_linear(G, b)
    bound = sum(b[i] * c[i] for i in range(n))

    assert 0 <= bound < 1

    print(f"RA1n exact Gram transversality verified: b^*G^-1b = {bound} < 1")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
