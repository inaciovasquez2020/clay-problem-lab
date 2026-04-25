#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

CERT = Path("artifacts/ra1n/projection_error_domination_certificate.json")

def q(x: str) -> Fraction:
    return Fraction(str(x))

def main() -> int:
    data = json.loads(CERT.read_text())

    assert data["object"] == "RA1N projection-error domination certificate"
    assert data["status"] == "conditional-positive-transfer-certificate"
    assert data["certifies"] == "Curv_k Gap_k |partial_xi Ghat_k| > ||P_k Ghat_k||_err"

    curvature = q(data["curvature"])
    gap = q(data["gap"])
    derivative_abs = q(data["derivative_abs"])
    projection_error = q(data["projection_error"])

    lhs = curvature * gap * derivative_abs
    margin = lhs - projection_error

    assert curvature > 0
    assert gap > 0
    assert derivative_abs > 0
    assert projection_error >= 0
    assert lhs > projection_error
    assert margin > 0

    print(f"RA1n projection-error domination verified: margin = {margin} > 0")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
