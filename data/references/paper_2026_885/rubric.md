# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly sets up the bounded-support Poisson empirical-Bayes model, oracle posterior mean, hierarchical prior-on-priors, estimator, and regret. Establishes well-definedness, including degenerate test priors, and derives the correct leave-one-out identity. The unweighted posterior average of theta_G(X_i) uses the full-data posterior; a leave-one-out average requires the likelihood factor and its normalization. Keeps Pi_n fixed when conditioning on n-1 observations.

2. **4 points:** Proves thickness uniformly over every test prior. Constructs an O(log n/log log n)-component moment-matching approximation with a TV error budget leaving room for perturbation; handles zero locations and zero or tiny weights; proves quantitative chi-square control in the correct direction over the whole count range; and computes a Uniform-location/Dirichlet-weight neighborhood probability at least exp(-C k log n). Concludes E(n^-2,r)<=C_{A,c0}log^2 n/log log n for r^2>=1/n and chooses r_n with the correct constant dependence. Ordinary Caratheodory gives L+1 atoms for matching moments through degree L; equivalent indexing is acceptable. Merely naming moment matching, continuity, a small Poisson tail, or a volume argument is insufficient.

3. **2 points:** Establishes posterior-predictive Hellinger contraction with the required probability tail and scale epsilon_n^2+r_n^2+n^-1. Supplies the local square-root entropy argument and a valid testing application, controls the numerator and denominator with normalized conditioning on the thick neighborhood, obtains posterior mean Hellinger control, and transfers from the intermediate density to the test density by product TV. A precisely stated standard independent robust testing theorem may be invoked after its hypotheses are verified; merely citing posterior contraction does not complete this step.

4. **2 points:** Establishes the Poisson-mixture regret-Hellinger bound, applies it conditionally using the correct leave-one-out representation, integrates the Hellinger tail with H^2<=2, and substitutes r_n^2 of order log^2 n/[n log log n] to obtain the uniform C(A,c0)log^3 n/[n(log log n)^2] regret bound. The reference proof gives an elementary square-root derivation of the regret-Hellinger inequality; an equivalent valid derivation is accepted. The truncation parameter can be fixed at 1/n and need not be integrated.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, specific perturbation radii, or numerical constants. Do not make the displayed route mandatory when a different route establishes the full public claim.

For the displayed route, the theorem-critical finite-mixture thickness construction and quantitative prior-mass rate must be derived, not assumed. The standard moment-matching TV lemma may be used with its relevant statement and hypotheses supplied. The specialized regret-Hellinger citation, or a paper-specific contraction lemma asserted without proof, does not by itself close the corresponding obligation.

Do not penalize harmless choices of posterior-mean versions on null observations. Do distinguish the full-data posterior from the leave-one-out posterior and the training prior Pi_n from Pi_{n-1}. Constants must be uniform over G0; the sufficiently-large threshold for c0 is absolute, while C and n0 may depend on A and c0.

The revised reference proof has no unresolved theorem-critical proof obligation.
