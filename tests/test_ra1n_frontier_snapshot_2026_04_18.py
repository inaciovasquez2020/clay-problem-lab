from pathlib import Path

def test_ra1n_frontier_snapshot_2026_04_18():
    s = Path("docs/status/RA1N_FRONTIER_SNAPSHOT_2026_04_18.md").read_text()
    assert "RA1N_KERNEL_PARITY_NORMAL_FORM.md" in s
    assert "RA1N_PROJECTOR_CONSISTENT_KERNEL.md" in s
    assert "RA1N_PROJECTOR_PAIRED_SYMMETRY.md" in s
    assert "\\Gamma_{j,k}(y,x)=\\Gamma_{j,k}(x,y)" in s
    assert "\\mathsf T^{(1),\\mathrm{proj}}_{j,k}=0" in s
    assert "paired commutator closure" in s
    assert "Claim 5" in s
    assert "deviatoric coercivity" in s
    assert "final DDYO continuum closure" in s
    assert "Status: Conditional." in s
