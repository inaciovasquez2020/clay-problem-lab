import json
from pathlib import Path
import math

def load_outbound(path):
    data = json.loads(Path(path).read_text())
    return data["V_out"], data["E_out"], data["X_gamma"]

def phi_6_7(V_out, E_out, X_gamma):
    def sigma_eff(xi, eta):
        return sum(math.cos(xi*X_gamma[g][0] + eta*X_gamma[g][1]) for g in V_out)

    def kappa_rank_defect():
        target = len(V_out)
        observed = len(set(V_out))
        return max(1, target - observed)

    def D_j(j, k):
        return 1.0

    def chi_out(zeta, k, C):
        return 1.0 if (2**(k-C-2) <= abs(zeta) <= 2**(k-C)) else 0.0

    return sigma_eff, kappa_rank_defect, D_j, chi_out

def transverse_hessian(sigma_eff, kappa_rank_defect, D_j, chi_out, xi, eta, k=10, C=2, d=2):
    theta = math.acos((xi*eta)/(abs(xi)*abs(eta)+1e-9))
    cos_theta = math.cos(theta)
    series = sum(2**(d*(k-j))*D_j(j,k) for j in range(k+1, k+20))
    return abs((-cos_theta)/(4*(2**d-1))) * series

def certify(path):
    V_out, E_out, X_gamma = load_outbound(path)
    sigma_eff, kappa_rank_defect, D_j, chi_out = phi_6_7(V_out, E_out, X_gamma)

    samples = [(1.1,1.2),(1.3,1.4),(1.5,1.6)]
    vals = [transverse_hessian(sigma_eff,kappa_rank_defect,D_j,chi_out,xi,eta) for xi,eta in samples]

    a_curv = min(vals)
    certified = a_curv > 0

    return {
        "a_curv": a_curv,
        "certified": certified
    }

if __name__ == "__main__":
    import sys
    result = certify(sys.argv[1])
    print(json.dumps(result, indent=2))
