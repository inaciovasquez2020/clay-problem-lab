# RA1n L1 symbol status

Status: CONDITIONAL

Canonical wall:
- RA1N_L1_SYMBOL_WALL

Fixed conditions:
- wallCardinality = 1
- Irr = 1
- E = 1

Open conditions:
- allCertified = true
- C = 1

Meaning of C:
- C = 1 iff the actual RA1n Fourier kernel Ghat is proved L^1(R^3)

Witness blocks:
- symbol_extraction
- origin_integrability
- tail_decay
- L1_split
- registry_lift

Truthfulness rule:
- Do not promote to CANONICAL unless allCertified = true and C = 1 are both certified.
