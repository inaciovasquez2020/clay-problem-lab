import json
from pathlib import Path

def test_ra1n_surface_partition_exists_and_is_nonclosing():
    p = Path("artifacts/ra1n_surface_partition.json")
    assert p.exists()
    data = json.loads(p.read_text())
    assert data["status"] == "surface_partition_only"
    assert data["closure_claim"] is False
    assert "canonical_candidate_count" in data
    assert "noncanonical_count" in data
    assert isinstance(data["canonical_candidates"], list)
    assert isinstance(data["noncanonical"], list)
