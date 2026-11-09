# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes a continuous hard map on the positive-dimensional coefficient cube, chosen independently of the learner. A finite-VC proof must explain continuous interpolation of arbitrary binary labels, thresholding at 1/2, and why this yields the uniform lower bound 1/2 for every network in the stated size class.
- **1 point:** Shows exact unrestricted reconstruction from the fixed samples, including recovery of r and s, and obtains the matching unrestricted adaptive result. The zero optimal errors must follow from an actual zero-error construction, not just an unsupported assertion about infima.
- **3 points:** Proves the fixed-query ReLU lower bound under the stated delta restriction. In the reference route, choose a single moving-hat location missed by all fixed samples, hold it fixed while s varies, evaluate the predictor there, and justify a forbidden bounded-size approximation of the hard map. The exact parameter budget must be accounted for: the disjoint hats make every restricted input coordinate constant or a scaled single coefficient, so substitution into the first affine layer does not increase the total number of nonzero matrix and bias entries.
- **4 points:** Constructs the adaptive ReLU learner using exactly N queries, with query maps into [0,1] on their entire stated domains, and shows that the last query reads the moving-hat value. Establishes a single joint-input ReLU predictor, verifies exact hat formation and the multiplication approximation hypotheses, sums the errors, and proves a largest-network size threshold depending only on N and eta, not on delta, G_m, or the individual task. Handles every eta > 0, for example with epsilon=min{1/2,eta/N}. Clipping is optional when another valid construction meets the domains and error bound.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular network wiring. The finite-VC and multiplication results may be invoked as standard-independent background when their relevant statements and applicable hypotheses are clear; the solver need not reprove those external theorems.

A claimed hard map without a valid hardness argument leaves a theorem-critical gap. The hard map must be selected for the task family, not chosen separately after seeing each learner. In the fixed-query lower bound the missed location may depend on the fixed sample set, but it must be held fixed over the coefficient cube used in the hardness contradiction.

Do not accept the general assertion that arbitrary affine input substitutions preserve an exact nonzero-parameter budget. A proof following that route must justify the special structure of this substitution or otherwise correctly account for network size and the initial hardness choice while preserving the stated learner budget.

The adaptive query map must actually query the recovered moving location on valid transcripts. An off-transcript codomain oversight that is fixed by ordinary clipping is a readily repairable local omission, not evidence against the theorem. Likewise, an otherwise complete proof that omits the elementary large-eta adjustment to a multiplication lemma stated only for tolerances in (0,1) has a local omission rather than a new mathematical bottleneck. A fully correct proof must nevertheless resolve both points.

Count all nonzero affine matrix and bias entries. Do not replace the largest-network budget by a total-network budget or allow uncounted computational preprocessing. Very large coefficients such as 1/delta are permitted; their magnitudes are not charged, but their nonzero occurrences are counted. The uniform error must hold over the whole task family and every test point.
