import json
import subprocess
import sys
from pathlib import Path

def test_ra1n_residual_surface_classifier_generates_audit():
    subprocess.run(
        [sys.executable, "tools/classify_ra1n_residual_surfaces.py"],
        check=True,
    )
    p = Path("artifacts/ra1n_residual_surface_classification.json")
    assert p.exists()
    data = json.loads(p.read_text())
    assert data["status"] == "classification_only"
    assert data["closure_claim"] is False
    assert data["canonical_unary_surface"] == r"r_k(ξ)=\widehat G_k(ξ)−P_k\widehat G_k(ξ)"
    assert "unary" in data["summary"]
    assert "records" in data
    assert isinstance(data["records"], list)
