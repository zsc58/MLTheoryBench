# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly formulates persistent safety as nonpositive componentwise next-state violations over every $x_0\in X_0$ and every reference, and converts the maximum row violation to optimization over the probability simplex with the correct sign. An equivalent direct argument testing individual rows with simplex unit vectors earns the same credit.
- **4 points:** Gives the learned-QP KKT system with correct stationarity, primal and dual feasibility, and complementarity, and justifies the optimizer's KKT multipliers under the stated affine-constraint, convexity, feasibility, and attainment assumptions. If using full optimizer/KKT equivalence, also justifies sufficiency and uniqueness. A direct sufficiency proof of the safety certificate need not prove the unused converse of the optimizer/KKT correspondence.
- **3 points:** Uses the KKT system to connect every safe-state/reference optimizer to a QCQP-feasible tuple and rigorously shows that $z^*\ge0$ forces every next-state row violation to be nonpositive. Correctly uses the extended-real infimum rather than assuming an outer minimizer exists. Handles $X_0=\varnothing$ and $r=0$ directly or by an equally valid argument.
- **1 point:** Correctly proves the SOS/SDP certificate implication using the certified lower-bound relation $z_{\mathrm{SDP}}\le z^*$.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a global worst-case optimization identity when a pointwise feasible-tuple argument establishes the target.

Treat an incorrect KKT sign, omitted quantifier over references, failure to justify existence of KKT multipliers for the exact optimizer, or failure to establish the implication from the QCQP value as a theorem-critical gap. Affine constraints permit the stated KKT necessity without Slater's condition; do not require or reward adding a strict-feasibility assumption.

The inner optimizer is exact and attained by assumption. The claim does not concern an unconverged finite-iteration solver. The outer QCQP value is an extended-real infimum: infeasibility gives $+\infty$ and unboundedness below gives $-\infty$. Do not require compactness or an attained outer optimum. An empty safe set makes safety vacuous; when $r=0$, the safe set is $\mathbb R^n$ and safety is automatic. A proof otherwise complete but merely omitting these readily repairable cases belongs in the 8-9 range rather than being treated as a substantive failure.

No construction, tightness, attainment, or convergence theorem for an SOS/SDP hierarchy is required. The certified lower-bound relation is part of the public setup.
