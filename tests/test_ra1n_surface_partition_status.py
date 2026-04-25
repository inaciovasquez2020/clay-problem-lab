from pathlib import Path

DOC = Path("docs/status/RA1N_SURFACE_PARTITION_STATUS.md").read_text()

def test_ra1n_surface_partition_status_is_conditional():
    assert "Status: CONDITIONAL." in DOC
    assert "canonical unary candidates: 23" in DOC
    assert "noncanonical / auxiliary surfaces: 51" in DOC

def test_ra1n_surface_partition_status_rule():
    assert "Only unary canonical candidates may enter the RA1n first-moment closure lane." in DOC
    assert "binary, ternary, transverse high-high, sampled surrogate" in DOC
    assert "No full RA1n closure claim is admissible from this partition alone." in DOC
