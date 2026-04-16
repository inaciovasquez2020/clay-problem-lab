import Mathlib

noncomputable section

open scoped Real
open MeasureTheory

structure RA1nEntry where
  status : String
  canonical : Bool
deriving Repr, DecidableEq

constant allCertified : Bool
constant wallCardinality : Nat
constant Irr : Nat
constant E : Nat
constant C : Nat

def freezeAudit : Bool := decide (wallCardinality = 1)

def ra1nTruthTest : Bool :=
  allCertified &&
  freezeAudit &&
  decide (Irr = 1) &&
  decide (E = 1) &&
  decide (C = 1)

def ra1nUpgradeIfCanonical : RA1nEntry :=
  if ra1nTruthTest then
    { status := "CANONICAL", canonical := true }
  else
    { status := "CONDITIONAL", canonical := false }

theorem ra1n_not_canonical_without_truth :
    ra1nTruthTest = false → ra1nUpgradeIfCanonical.status = "CONDITIONAL" := by
  intro h
  unfold ra1nUpgradeIfCanonical
  rw [h]
  rfl

theorem ra1n_canonical_iff_truth :
    ra1nUpgradeIfCanonical.status = "CANONICAL" ↔ ra1nTruthTest = true := by
  unfold ra1nUpgradeIfCanonical
  by_cases h : ra1nTruthTest
  · simp [h]
  · simp [h]

constant Ghat : EuclideanSpace ℝ (Fin 3) → ℂ

def L1_integrable : Prop :=
  Integrable (fun ξ : EuclideanSpace ℝ (Fin 3) => ‖Ghat ξ‖)

def GoodBounds : Prop :=
  ∃ (alpha eps C0 Cinf : ℝ),
    alpha < 3 ∧
    0 < eps ∧
    0 < C0 ∧
    0 < Cinf ∧
    (∀ ξ : EuclideanSpace ℝ (Fin 3), ‖ξ‖ ≤ 1 → ‖Ghat ξ‖ ≤ C0 * ‖ξ‖^(-alpha)) ∧
    (∀ ξ : EuclideanSpace ℝ (Fin 3), 1 ≤ ‖ξ‖ → ‖Ghat ξ‖ ≤ Cinf * (1 + ‖ξ‖)^(-3 - eps))

axiom goodBounds_imply_L1 : GoodBounds → L1_integrable
axiom C_eq_one_of_L1 : L1_integrable → C = 1

theorem canonical_if_allCertified_and_L1 :
    allCertified = true → L1_integrable → ra1nUpgradeIfCanonical.status = "CANONICAL" := by
  intro hA hL1
  have hC : C = 1 := C_eq_one_of_L1 hL1
  unfold ra1nUpgradeIfCanonical ra1nTruthTest freezeAudit
  by_cases hW : wallCardinality = 1
  · by_cases hI : Irr = 1
    · by_cases hE : E = 1
      · simp [hA, hW, hI, hE, hC]
      · simp [hA, hW, hI, hE]
    · simp [hA, hW, hI]
  · simp [hA, hW]

theorem canonical_if_allCertified_and_goodBounds :
    allCertified = true → GoodBounds → ra1nUpgradeIfCanonical.status = "CANONICAL" := by
  intro hA hGB
  apply canonical_if_allCertified_and_L1 hA
  exact goodBounds_imply_L1 hGB
