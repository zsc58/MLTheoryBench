# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes or correctly invokes the gamma-contraction of T and derives the residual estimate ||W-V*||_infty <= (1-gamma)^(-1)||W-TW||_infty using V*=TV*. Justifies the nonexpansiveness of Gamma where used. A separate proof of nonexpansiveness of L is not required.
- **3 points:** Uses the assumed Bellman compatibility and W=Gamma Vbar in V to control the difference between concrete Bellman updates by D_H(s,u). The argument must cover both possible signs of the difference; a valid symmetry argument or equivalent unified argument suffices.
- **3 points:** Correctly uses the state round trip to bound ||TW-Gamma Tbar_dagger Vbar||_infty by Delta_H(kappa_S;d_V). In the reference route this consists of identifying Gamma Tbar_dagger Vbar with the kappa_S-average of TW, using stochastic normalization and the triangle inequality, and then taking the supremum over the starting state.
- **2 points:** Combines the abstraction bridge, grounding nonexpansiveness, and the residual estimate, or an equivalent valid argument, to obtain the exact claimed bound for every admissible Vbar, including the factor (1-gamma)^(-1).

# Evaluator Notes

Accept a complete valid alternative proof and allocate full credit for mathematically equivalent work. Do not require the reference proof's incidental notation, order, or displayed intermediate identities.

In an argument using the pointwise Hausdorff comparison, leaving one sign of the difference unjustified is a substantive gap; explicitly saying that the reverse case follows by exchanging the states and using symmetry is sufficient. A proof covering both signs in one argument does not need two separately written cases.

In an argument using the round-trip bridge, the necessary averaging or an equivalent justification must be established; displaying the particular reference identity is not an independent scoring requirement. Similarly, an alternative proof need not establish an intermediate bound it does not use.

The public task already introduces V* as the fixed point of T. A solver may use that fact without separately proving existence and uniqueness. If a fixed-point theorem is invoked to establish existence, its standard completeness and contraction hypotheses must hold.

Do not require nonexpansiveness of L, nonempty abstract action sets at unused abstract states, full support of the encoders, decoder consistency, V* in V, invariance of V, a Wasserstein representation of d_V, or any rate-distortion optimization argument. These are not obligations of the target.

A purported proof may not replace the worst-case Hausdorff distortion by an average over starting states, assume compatibility for values outside V, or replace Tbar_dagger by a different abstract Bellman operator without justification. Failure to obtain the stated factor (1-gamma)^(-1), or an explicitly justified stronger bound implying it, leaves the requested conclusion unproved.
