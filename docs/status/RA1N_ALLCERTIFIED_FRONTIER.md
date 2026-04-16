# Conditional: RA1n allCertified frontier

## Target
Replace the free registry flag allCertified = true by explicit certification of the required object list.

## Required statement
allCertified = true iff every required RA1n certification object is present and verified.

## Certification slots
1. terminal_symbol_registered
2. ghat_formula_explicit
3. local_bound_registered
4. tail_bound_registered
5. goodbounds_registered
6. l1_integrable_registered
7. C_eq_one_registered
8. freeze_audit_registered
9. irr_registered
10. exact_representation_registered

## Truthfulness rule
Do not set allCertified = true before all ten certification slots are explicitly locked.
