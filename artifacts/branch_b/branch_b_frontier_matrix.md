# Branch B frontier matrix

| file | status | tagged evidence |
|---|---:|---|
| `docs/math/DDYO_RA1N_CONDITIONAL.md` | OPEN | `L1` [open,branchb] # DDYO RA1n (Conditional)...<br>`L4` [branchb] RA1n = Rigidity Atom 1n...<br>`L6` [open] ## Conditional statement... |
| `docs/math/DDYO_SOLVE_REQUIREMENTS.md` | OPEN | `L3` [open] ## Missing parts to have a solve...<br>`L50` [budget] C_\varepsilon\Bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\Bigr)_{j,k}....<br>`L53` [close,branchb] ### 5. Claim 5 / paired remainder closure... |
| `docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md` | MIXED | `L1` [open] # DDYO Open Problem: Shell-Product Moment Control...<br>`L3` [open] ## Precise missing theorem...<br>`L19` [close] this implies the shell-product H^1 gain, the deviatoric coercivity estimate,... |
| `docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md` | OPEN | `L1` [open] # DDYO Shell-Product Moment Frontier...<br>`L3` [open] ## Weakest sufficient remaining lemma...<br>`L18` [open,close] this is sufficient to recover the shell-product \(H^1\) gain and hence... |
| `docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md` | OPEN | `L1` [open] # DDYO Deviatoric Coercivity Frontier...<br>`L3` [open] ## Sole remaining theorem-level object...<br>`L19` [open] It is equivalently sufficient to prove that for every \(\varepsilon\in(0,1)\),... |
| `docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md` | OPEN | `L1` [branchb] # DDYO Claim 5 Final Dichotomy...<br>`L3` [open] ## Frontier object...<br>`L4` [branchb] Let \(\mathsf T^{(1)}_{j,k}\) denote the post-symmetrized first-order leakage term.... |
| `docs/math/DDYO_FIRST_ORDER_LEAKAGE_SPLIT.md` | OPEN | `L1` [branchb] # DDYO First-Order Leakage Split...<br>`L11` [close] ## Two admissible closure branches...<br>`L19` [branchb] ### Branch B: lower-order routing... |
| `docs/math/DDYO_PAIRING_IBP_FRONTIER.md` | OPEN | `L1` [open] # DDYO Pairing IBP Frontier...<br>`L7` [open] Thus the weakest sufficient next ingredient is to replace the monolithic pairing...<br>`L47` [open] ## Weakest sufficient IBP form... |
| `docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md` | OPEN | `L14` [budget] C_j\bigl(\Phi_j[u]+\lambda R_j^{\mathrm{cont}}[u]\bigr),...<br>`L20` [budget] \sum_j C_j\bigl(\Phi_j[u]+\lambda R_j^{\mathrm{cont}}[u]\bigr)...<br>`L22` [budget] \Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u].... |
| `docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md` | MIXED | `L14` [budget] C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr),...<br>`L31` [open] ## Weakest sufficient bound...<br>`L33` [open] It is sufficient to prove... |
| `docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md` | OPEN | `L1` [close] # DDYO Closure Status — 2026-04-10...<br>`L10` [open] - max_fight remaining failures: NONE...<br>`L12` [open] ## Frozen frontier files... |
| `docs/status/DDYO_RA1N_STATUS_2026_04_10.md` | OPEN | `L1` [branchb] # DDYO RA1n Status — 2026-04-10...<br>`L10` [open] - max_fight remaining failures: NONE...<br>`L12` [open] ## Frozen frontier files... |
| `docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md` | OPEN | `L1` [open] # Navier--Stokes Frontier Snapshot (2026-04-10)...<br>`L14` [open] - J2B sampled frontier now includes:...<br>`L26` [open] ## DDYO commutator frontier... |

## Expanded evidence
### docs/math/DDYO_RA1N_CONDITIONAL.md
Status: **OPEN**
- tags: `open,branchb`
  L1: # DDYO RA1n (Conditional)
  L2: 
- tags: `branchb`
  L3: ## Name
  L4: RA1n = Rigidity Atom 1n
  L5: 
- tags: `open`
  L5: 
  L6: ## Conditional statement
  L7: 
- tags: `branchb`
  L7: 
  L8: Assume there exists a constant \(C_{\mathrm{RA1n}}<\infty\) such that for all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
  L9: \[
- tags: `branchb`
  L17: \le
  L18: C_{\mathrm{RA1n}}\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
  L19: \]
- tags: `close,branchb`
  L22: 
  L23: RA1n implies the shell-product \(H^1\) gain
  L24: \[

### docs/math/DDYO_SOLVE_REQUIREMENTS.md
Status: **OPEN**
- tags: `open`
  L2: 
  L3: ## Missing parts to have a solve
  L4: 
- tags: `budget`
  L49: +
  L50: C_\varepsilon\Bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\Bigr)_{j,k}.
  L51: \]
- tags: `close,branchb`
  L52: 
  L53: ### 5. Claim 5 / paired remainder closure
  L54: For all dyadic indices with \(|j-k|\le C\),
- tags: `close`
  L62: 
  L63: ### 6. Final DDYO continuum closure
  L64: High-high absorbability closes, hence the DDYO continuum argument closes.
- tags: `close,budget`
  L63: ### 6. Final DDYO continuum closure
  L64: High-high absorbability closes, hence the DDYO continuum argument closes.
  L65: 
- tags: `open`
  L67: 
  L68: The sole real missing object is Item 2, or any equivalent estimate strong enough to imply Item 4.
  L69: 

### docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md
Status: **MIXED**
- tags: `open`
  L1: # DDYO Open Problem: Shell-Product Moment Control
  L2: 
- tags: `open`
  L2: 
  L3: ## Precise missing theorem
  L4: 
- tags: `close`
  L18: \]
  L19: this implies the shell-product H^1 gain, the deviatoric coercivity estimate,
  L20: Claim 5, and final DDYO continuum closure.
- tags: `close,branchb`
  L19: this implies the shell-product H^1 gain, the deviatoric coercivity estimate,
  L20: Claim 5, and final DDYO continuum closure.
  L21: 
- tags: `open`
  L23: 
  L24: Open.
  L25: No theorem-level proof is currently present in this repository.

### docs/math/DDYO_SHELL_PRODUCT_MOMENT_FRONTIER.md
Status: **OPEN**
- tags: `open`
  L1: # DDYO Shell-Product Moment Frontier
  L2: 
- tags: `open`
  L2: 
  L3: ## Weakest sufficient remaining lemma
  L4: 
- tags: `open,close`
  L17: \]
  L18: this is sufficient to recover the shell-product \(H^1\) gain and hence
  L19: \[
- tags: `open`
  L32: 
  L33: It is equivalently sufficient to prove that for every \(\varepsilon\in(0,1)\),
  L34: \[
- tags: `budget`
  L41: +
  L42: C_\varepsilon\Bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\Bigr)_{j,k}.
  L43: \]
- tags: `open`
  L47: Computational verification is green.
  L48: The program remains formally open at the shell-product moment-control frontier.
  L49: No theorem-level closure is claimed here.

### docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md
Status: **OPEN**
- tags: `open`
  L1: # DDYO Deviatoric Coercivity Frontier
  L2: 
- tags: `open`
  L2: 
  L3: ## Sole remaining theorem-level object
  L4: 
- tags: `open`
  L18: 
  L19: It is equivalently sufficient to prove that for every \(\varepsilon\in(0,1)\),
  L20: \[
- tags: `budget`
  L27: +
  L28: C_\varepsilon\Bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\Bigr)_{j,k}.
  L29: \]
- tags: `open`
  L32: 
  L33: A sufficient route is the shell-product estimate
  L34: \[
- tags: `open`
  L52: Computational verification is green.
  L53: This file records the exact remaining mathematical frontier only.
  L54: No theorem-level closure is claimed here.

### docs/math/DDYO_CLAIM5_FINAL_DICHOTOMY.md
Status: **OPEN**
- tags: `branchb`
  L1: # DDYO Claim 5 Final Dichotomy
  L2: 
- tags: `open`
  L2: 
  L3: ## Frontier object
  L4: Let \(\mathsf T^{(1)}_{j,k}\) denote the post-symmetrized first-order leakage term.
- tags: `branchb`
  L3: ## Frontier object
  L4: Let \(\mathsf T^{(1)}_{j,k}\) denote the post-symmetrized first-order leakage term.
  L5: 
- tags: `branchb`
  L13: 
  L14: ### Branch B: lower-order routing
  L15: \[
- tags: `budget`
  L17: \le
  L18: C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr)_{j,k}.
  L19: \]
- tags: `open`
  L20: 
  L21: ## Weakest sufficient consequence
  L22: Either branch implies that the remaining paired remainder satisfies

### docs/math/DDYO_FIRST_ORDER_LEAKAGE_SPLIT.md
Status: **OPEN**
- tags: `branchb`
  L1: # DDYO First-Order Leakage Split
  L2: 
- tags: `close`
  L10: 
  L11: ## Two admissible closure branches
  L12: 
- tags: `branchb`
  L18: 
  L19: ### Branch B: lower-order routing
  L20: Prove
- tags: `budget`
  L23: \le
  L24: C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr)_{j,k}.
  L25: \]
- tags: `open`
  L26: 
  L27: ## Weakest sufficient outcome
  L28: 
- tags: `open,branchb`
  L28: 
  L29: Either Branch A or Branch B is sufficient to conclude that the remaining paired remainder satisfies
  L30: \[

### docs/math/DDYO_PAIRING_IBP_FRONTIER.md
Status: **OPEN**
- tags: `open`
  L1: # DDYO Pairing IBP Frontier
  L2: 
- tags: `open`
  L6: 
  L7: Thus the weakest sufficient next ingredient is to replace the monolithic pairing
  L8: \[
- tags: `open`
  L46: 
  L47: ## Weakest sufficient IBP form
  L48: 
- tags: `open`
  L48: 
  L49: It is sufficient to prove an identity of the form
  L50: \[
- tags: `close,budget`
  L82: 
  L83: Any such paired decomposition closes the pairing-level second-gain lemma and completes the DDYO continuum high-high absorbability step.

### docs/math/DDYO_CRITICAL_COMMUTATOR_LEMMA.md
Status: **OPEN**
- tags: `budget`
  L13: +
  L14: C_j\bigl(\Phi_j[u]+\lambda R_j^{\mathrm{cont}}[u]\bigr),
  L15: \]
- tags: `budget`
  L19: \qquad
  L20: \sum_j C_j\bigl(\Phi_j[u]+\lambda R_j^{\mathrm{cont}}[u]\bigr)
  L21: \lesssim
- tags: `budget`
  L21: \lesssim
  L22: \Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u].
  L23: \]
- tags: `open`
  L24: 
  L25: ## Weakest sufficient local estimate
  L26: 
- tags: `open`
  L26: 
  L27: It is sufficient to establish
  L28: \[
- tags: `budget`
  L36: +
  L37: C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr).
  L38: \]

### docs/math/DDYO_MOLLIFIED_SYMMETRIC_COMMUTATOR_BOUND.md
Status: **MIXED**
- tags: `budget`
  L13: +
  L14: C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr),
  L15: \qquad 0<\varepsilon<1.
- tags: `open`
  L30: 
  L31: ## Weakest sufficient bound
  L32: 
- tags: `open`
  L32: 
  L33: It is sufficient to prove
  L34: \[
- tags: `close,budget`
  L47: Combined with mollified skew cancellation and lower-order projector replacement,
  L48: this closes continuum DDYO high-high absorbability.

### docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md
Status: **OPEN**
- tags: `close`
  L1: # DDYO Closure Status — 2026-04-10
  L2: 
- tags: `open`
  L9: - unittest_discover: rc=0
  L10: - max_fight remaining failures: NONE
  L11: 
- tags: `open`
  L11: 
  L12: ## Frozen frontier files
  L13: - docs/math/DDYO_DEVIATORIC_COERCIVITY_FRONTIER.md
- tags: `open`
  L15: 
  L16: ## Current weakest sufficient remaining lemma
  L17: For all dyadic indices with |j-k| <= C, all tensor indices a,b, and all coordinate indices l,
- tags: `open`
  L29: \]
  L30: this is sufficient to recover the shell-product H^1 gain and the target deviatoric coercivity bound.
  L31: 
- tags: `open`
  L33: - Computationally closed
  L34: - Formally open at the shell-product moment frontier

### docs/status/DDYO_RA1N_STATUS_2026_04_10.md
Status: **OPEN**
- tags: `branchb`
  L1: # DDYO RA1n Status — 2026-04-10
  L2: 
- tags: `open`
  L9: - unittest_discover: rc=0
  L10: - max_fight remaining failures: NONE
  L11: 
- tags: `open`
  L11: 
  L12: ## Frozen frontier files
  L13: - docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md
- tags: `branchb`
  L13: - docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md
  L14: - docs/math/DDYO_RA1N_CONDITIONAL.md
  L15: - docs/math/DDYO_SOLVE_REQUIREMENTS.md
- tags: `open,close,branchb`
  L17: 
  L18: ## RA1n (conditional closure atom)
  L19: Assume there exists \(C_{\mathrm{RA1n}}<\infty\) such that for all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
- tags: `branchb`
  L18: ## RA1n (conditional closure atom)
  L19: Assume there exists \(C_{\mathrm{RA1n}}<\infty\) such that for all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
  L20: \[

### docs/status/NAVIER_STOKES_FRONTIER_SNAPSHOT_2026_04_10.md
Status: **OPEN**
- tags: `open`
  L1: # Navier--Stokes Frontier Snapshot (2026-04-10)
  L2: 
- tags: `open`
  L13:   - theta-tail monotonicity
  L14: - J2B sampled frontier now includes:
  L15:   - exact gradient-level stretch split into strain + skew
- tags: `open`
  L25: 
  L26: ## DDYO commutator frontier
  L27: - sampled same-scale commutator split verified
- tags: `open,budget`
  L31: 
  L32: ## DDYO commutator absorbability frontier
  L33: - sampled strain/rotation commutator split verified
- tags: `budget`
  L36: - sampled epsilon-proxy integer-dilation stability verified
  L37: - active wall: continuum commutator-absorbability lemma
  L38: 
- tags: `open`
  L38: 
  L39: ## Exact skew-adjoint reduction frontier
  L40: - sampled exact pairing split into symmetric + rotational parts verified

