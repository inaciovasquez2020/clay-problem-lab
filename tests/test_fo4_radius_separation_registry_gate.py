from pathlib import Path

def test_fo4_radius_separation_registry_gate():
    s = Path("docs/status/FO4_RADIUS_SEPARATION_STATUS.md").read_text()
    assert "KERNEL_TRANSPORT_CONFIGURATION_SOURCE" in s
    assert "SEPARATION_OBSTRUCTION_SOURCE" in s
    assert "may be used only under the certified inequality" in s
