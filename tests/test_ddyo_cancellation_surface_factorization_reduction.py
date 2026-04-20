from pathlib import Path

DOC = Path("docs/math/DDYO_CANCELLATION_SURFACE_FACTORIZATION_REDUCTION.md")

def test_ddyo_cancellation_surface_factorization_reduction_literals():
    text = DOC.read_text()
    required = [
        "## Status\nCONDITIONAL",
        "r_k(\\omega)=g_k(\\omega)\\,b_k(\\omega)",
        "m_b:=\\inf_{\\omega\\in K_k}|b_k(\\omega)|>0",
        "Z_k=C_k",
        "m_g(k,\\varepsilon_k):=",
        "\\gamma_{k,\\rho}:=",
        "\\widetilde{\\alpha}_{k,\\rho}:=m_b\\,\\gamma_{k,\\rho}",
        "\\kappa_{\\mathrm{adj}}(k,\\rho):=",
        "c_{\\mathrm{need}}(k,\\rho):=",
        "What is **not** proved here:",
        "### Division lemma",
        "### Nonvanishing transfer lemma",
        "Replace `CONDITIONAL` by `PROVED` only after",
    ]
    for needle in required:
        assert needle in text, needle
