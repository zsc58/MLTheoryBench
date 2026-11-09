# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Population discrepancy and off-support mass.** Establishes a usable bound \(\|d^\circ\|_1=O(h)\) and the consequence \(B=\|(w^\circ)_{S^c}\|_1\le\|d^\circ\|_1=O(h)\). A derivation using population first-order conditions, integral Taylor expansion, and integrated-Hessian comparability is fully valid. Because the public task already chooses \(C_h\) satisfying \(\|d^\circ\|_1\le C_hh\), a proof may instead use that stipulated bound and derive the off-support consequence; do not withhold credit merely because it does not rederive an available premise.
- **3 points: Pooled initializer.** Establishes a valid pooled score bound at the fixed population minimizer, accounts for the potentially nonzero domain-specific score means, derives the shifted cone including \(B\), applies localized pooled curvature, and controls both parts of its tolerance. Obtains both the stated \(\ell_2\) rate, including its minimum term, and the \(\ell_1\) rate. The latter follows, for example, by controlling \(\sqrt{s\lambda_wB}\) with \(s\lambda_w+B\). The proof must remain valid for \(s=0\) and \(B=0\).
- **4 points: Target correction.** Derives a valid correction basic inequality from objective comparison and controls the score at the data-dependent shifted point. A uniformly bounded entrywise Hessian gives the necessary gradient Lipschitz bound; Hessian Lipschitz continuity is not required. Uses SCAD's bounded slope, the effective-support bound \(|T|\le C_hh/\lambda_d\), the assumed correction cone, and applicable target curvature to control the tolerance and obtain \(\|\widehat d-d^\circ\|_2=O(\min\{(\lambda_dh)^{1/2},h\})\) and \(\ell_1\) error \(O(h)\), or establishes these bounds by another complete valid argument. Merely naming restricted strong convexity, effective sparsity, or SCAD is insufficient. The proof must cover an empty \(T\) and \(h=0\).
- **1 point: Completion and probability.** Combines the two error bounds to obtain exactly the claimed final rates on a common event. Correctly combines score concentration with the assumed empirical-condition event using a union bound, without assuming independence of events or of the two stages. Constants may depend on the fixed assumption, tuning, and compatibility constants but not on \(n_0,N,p,s,h\).

# Evaluator Notes

Accept any complete valid alternative proof and assign full credit when it establishes the public claim, even if it avoids intermediate steps used by the reference proof. The allocations above describe mathematical coverage rather than a mandatory sequence of lemmas.

The known source set and population quantities are fixed independently of the samples. The theorem concerns one asymmetric nodewise vector, not a symmetrized graph or a data-selected source set. Do not require source-screening, support-recovery, or uniform-over-nodes arguments.

Conditions (E1)–(E4), including the returned solution's objective comparison, localization, and cone bound, are assumptions. The solver need not prove that an optimization routine attains them. Approximate stationarity is included in the contract, but the rate proof need not use it, and no unstated decay condition on \(\epsilon_n\) or inequality comparing \(\kappa_0\) with SCAD concavity may be imposed.

A proof that treats \(d^\circ\) as exactly sparse, drops the shifted off-support mass without justification, concentrates a score at a data-dependent point as though it were fixed, or invokes restricted curvature without checking localization and tolerance control has a theorem-critical gap unless an independent valid argument supplies the missing conclusion.

Score a later step when its needed premise is independently established or explicitly assumed in the public task, even if an earlier attempted derivation of that premise is flawed. Boundary cases may be handled explicitly or by inequalities that remain valid without division by \(s\), \(h\), \(B\), or \(|T|\).
