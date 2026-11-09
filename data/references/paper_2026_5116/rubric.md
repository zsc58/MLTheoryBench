# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Correctly computes the generator on pullbacks \(u\circ q\), using projectable horizontal fields or an equivalent intrinsic argument, with the vertical connection trace and its negative sign. Derives the quotient drift \(q_*b_t-(s_t^2/2)\kappa\) and the initial quotient law. Any needed well-definedness of the pushed-forward drift and curvature field is justified from equivariance and isometry.
- **2 points:** Constructs or rigorously identifies the horizontal semimartingale lift from compatible time-zero initial data. Obtains the horizontal projected drift, lifted curvature term, and horizontally lifted Wiener noise with the intrinsic scaling convention. Establishes horizontality and the pathwise projection property. A frame calculation must include the connection correction and only horizontal diffusion directions.
- **3 points:** Proves endpoint-law preservation by establishing invariance of both total-space laws, equality of their quotient laws, and determination of invariant laws by quotient pushforward. Equivariance of the lifted coefficients or an equivalent equivariant-lift argument must be supplied; horizontality alone is not enough. Compact-group averaging, a justified disintegration argument, or another valid proof of invariant-law identification is acceptable.
- **1 point:** For arbitrary admissible common fixed initial points in the deterministic case, proves orbit correspondence and applies equivariance, isometry, and orthogonal horizontal–vertical decomposition to obtain the integrated squared-speed inequality. This part must not require the fixed initial point to have an invariant Dirac law.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, explicit coordinate calculations when an intrinsic argument suffices, or a reproof of the standard independent geometric and stochastic facts when their hypotheses are correctly checked.

A proof that omits the curvature correction, includes vertical Brownian directions in the horizontal lift, merely asserts a lift without establishing its projected process and horizontality, or infers total-space law equality from quotient law equality without invariance has a theorem-critical gap. Equality of generators gives equality in law under well-posedness; it does not by itself establish the stated pathwise equality with the given projected process. A pathwise horizontal-lift construction or an appropriate coupling and uniqueness argument supplies that property.

Interpret manifold noise intrinsically as defined in the task. Do not require addition of a standalone manifold-valued Wiener path to another manifold-valued process, and do not interpret scalar multiplication of that shorthand as multiplying an entire already-realized semimartingale's finite-variation part by only \(s_t\). If a Stratonovich frame representation is used, its Brownian connection correction scales with \(s_t^2\).

Compactness is a standing hypothesis, not an extra assumption a solver must establish. Initial lifting data must lie above \(Y_0\) and be nonanticipating. The result concerns Borel probability laws and does not require smooth densities. A correct argument may use local martingales and localization rather than claim unqualified true-martingale identities for arbitrary unbounded test functions.

Do not demand strict positivity of \(s_t\), positive orbit or quotient dimension, a connected group, or a global horizontal frame or section. Empty frame sums and zero diffusion coefficients are admissible. The deterministic target is the displayed integrated squared-speed comparison; an additional arc-length observation is optional and cannot replace the requested energy comparison.
