import urllib.request
from pathlib import Path

url = "https://odlyzko.ams.org/zeta_tables/zeros1"
out = Path("riemann/data/zeros/zeros1.txt")

out.parent.mkdir(parents=True, exist_ok=True)

print("downloading zeros dataset...")
urllib.request.urlretrieve(url, out)

print("saved to", out)
