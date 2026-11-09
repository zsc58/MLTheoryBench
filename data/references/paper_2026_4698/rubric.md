# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the independent per-frequency magnitude/misalignment dynamics from the ideal gradient flow and the specified Fourier normalization, including the shortest-angle formulation. The derivation must use the summed loss and loss-minimizing sign; the ideal theta and xi coefficients are respectively 2p and p. Zero constant coefficients remain zero.
- **2 points:** Establishes the conserved quantities, including their initial values, and obtains the reduced equations and invariant domain. Justifies positivity needed for polar coordinates. The product invariant is alpha_k^2 beta_k sin D_k=kappa^3 sin D_k(0), not merely an algebraic rewriting of its left side.
- **3 points:** Verifies cooperativity and applies a correctly stated ODE comparison theorem to preserve both shortest-phase order and reversed magnitude order throughout common existence. Identifies the argmin frequency as the winner and the second order statistic as the controlling competitor.
- **2 points:** Proves a high-probability event for iid uniform initial shortest phases that supplies a positive quantitative cosine gap and the lower bound on the winner's cosine. All probability estimates must use K=(p-1)/2. An event also placing the runner-up below pi/2 is acceptable, as is a valid argument covering a negatively aligned runner-up.
- **1 point:** Derives, rather than asserts, the initial ratio gap and subsequent growth estimate, proves the dominance threshold is attained before the fixed neuron's maximal time, and obtains the stated universal-constant time bound. Handles thresholds already reached during the initial stage.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's constants, auxiliary good event, or presentation when a universal-constant-equivalent bound is proved. The two invariants and intermediate estimates are reference-route components, not mandatory if a different complete proof establishes the target.

The central comparison argument and quantitative dominance-time estimate must be derived, not merely attributed to a named method. Standard cooperative ODE comparison may be invoked after its relevant statement and hypotheses are supplied.

Finite-time existence is a theorem-critical issue. Exponential growth of q=1-beta_sharp/beta_star on an interval of existence does not alone establish a hitting time if the solution can explode before the nominal integration endpoint. A valid closure may show that the reciprocal-magnitude gap stays positive, that competitors consequently remain bounded at winner blow-up, and that the ratio tends to zero. Any other correct continuation or blow-up comparison argument is equally acceptable. Do not award a fully correct score to a proof that simply evaluates a solution after its maximal time.

All times and probabilities in the target are for a fixed neuron on its own maximal interval. No simultaneous guarantee over all M neurons is required. The source's finite-scale approximation-error estimate is not an extra public assumption and need not be proved by a solver.

The published positive term log(1/(1-epsilon)) is a loose upper-bound term. A sharper sufficient time involving the positive part of log((1-epsilon)/q(t_1)) is acceptable. Do not require that the displayed upper bound be an exact hitting time.

The trajectory-symmetry lemma is not mandatory for this proof. If used, uniqueness must be applied to the smooth coupled system, not unjustifiably to the scalar square-root field at its turning point. Its finite crossing assertion concerns a standalone single-frequency solution continued on that frequency's own interval. Boundedness before crossing must justify that continuation; a positive lower angular-speed bound alone does not guarantee crossing before the multi-frequency neuron's common maximal time. Symmetry identities transfer to the neuron trajectory only when both evaluation times lie in its interval. Do not impose an extra assumption that every frequency crosses pi/2 before the neuron terminates. No source-specific identity or proof step is available as a public premise.
