# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the top-k omission bound, retaining eta and the requested exponent p=beta/(beta+2). A complete route establishes top-k disagreement implies TV>=Delta/2, then obtains r<=eta+C u^beta+2e/u^2 from the margin assumption and Pinsker, optimizes for e>0, and handles e=0. The constant must depend only on the stated margin parameters, not on the policy or decision count.
- **2 points:** Applies flat search completeness to a successful teacher certificate and uses a union bound plus the joint occurrence-law normalization to obtain the flat success guarantee. The evaluation law is the success-conditioned initial-state marginal. The proof must not replace occurrence weighting by uniform-per-trace weighting or assume independent decisions within a trace.
- **3 points:** Defines graph coverage and both hierarchical omission families under the original joint experiment, applies memoized completeness, and proves the hierarchical bound with the separate L_hi and L_lo terms. Coverage may be correlated with omission events. The argument must not use unconditional risks as though they were coverage-conditioned risks without justification, or grant mu access to the hidden test certificate. The counted decisions must match the certificate traces.
- **2 points:** Substitutes the assumed total-KL power laws, checks both intrinsic-error budgets, allocates delta/2 to the flat learned term and delta/4 to each hierarchical learned term, and derives exactly the displayed sufficient thresholds. Handles positive integer trace counts by ceilings where needed, preserves the conditional interpretation of the learning hypotheses, and identifies the results as sufficient certificates rather than necessary sample counts.
- **1 point:** Constructs a terminal implication chain and a reusable conjunction family, explains why the chosen closing/assembly convention gives L_hi=d+1 and L_lo=ell, and derives L_flat=2^d ell+(2^d-1). Uses the explicit threshold formulas and depth-uniform comparability to obtain a positive depth-independent C0 and the exponential lower bound. Does not claim shortest-proof or minimax hardness.

# Evaluator Notes

Accept any complete valid alternative proof, including another valid omission estimate that implies the requested bound with permitted constants. Do not require the particular optimizing constant displayed in the reference proof.

An estimate of the form eta+C u^beta+O(sqrt(e)/u) does not by itself establish p=beta/(beta+2): direct optimization gives beta/(2(beta+1)). Award full omission-bound credit only if a valid argument reaches the requested exponent.

Use realized failure indicators before averaging randomized graph proposals or search. Equivalent conditional-probability arguments are acceptable when all conditioning is explicit and correct. Merely naming a union bound, Pinsker, search completeness, or memoization without deriving the necessary inequalities is not a completed step.

The learning curves are assumptions on total KL error. There is no obligation to prove a geometric ERM rate, infer latent graphs, derive a graph-prediction rate, or establish a training-confidence statement. Conversely, a proof may not silently discard a nondecaying approximation, inference, or graph-coverage error.

The exact hierarchical counts concern the specified protocol, which charges nonterminal structural assembly to a high-level closing action. Counting those steps separately is a different convention and must not be silently substituted for the required equalities. The family concerns chosen teacher certificates and their unfolding, not all possible proofs in the underlying logic.

The comparison must use the explicit real-valued certificates, a common alpha fixed across depth, and a depth-independent comparison constant. Dividing only unspecified upper envelopes is insufficient. The final qualification that these are sufficient certificates, not minimax lower bounds, must be retained.
