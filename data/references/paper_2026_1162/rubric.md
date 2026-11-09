# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes integrability and differentiation of the exact and constructed surrogate mean objectives from explicit growth and domination bounds. Derives a uniform gradient-mismatch estimate with linear and quadratic state/shape-derivative error terms and constants independent of the surrogate. Checks the regularity and moment properties of the chosen GELU network rather than inferring them solely from approximation accuracy.
- **4 points:** Proves mixed-norm approximation with the arbitrary fixed complete bases and centers. Controls output and input truncation uniformly over the compact shape set, verifies the latent target and pushforward-measure hypotheses, and proves simultaneous value/shape-derivative approximation for unbounded parameter inputs. If using the cutoff route, covers its entire transition region with the compact approximant, controls multiplication in value and derivative, and obtains integrable error envelopes independent of the approximation radius and accuracy before choosing the input radius. Transfers the estimates through the orthonormal decoder and obtains the sum of the separate suprema.
- **2 points:** Uses strong convexity and the exact and surrogate variational inequalities to derive the stationary-point distance bound. Derives the objective-gap upper bound using strong convexity based at the surrogate stationary point and its surrogate variational inequality, followed by maximizing the resulting quadratic.
- **2 points:** Coordinates the tolerances and quantifiers, choosing finite permitted ranks and one GELU RBNO for each requested epsilon so that both the mixed approximation and both optimization guarantees hold for every constrained stationary point of that same surrogate. Retains fixed bases and centers and handles division by zero distance and the applicable finite-dimensional or degenerate cases.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, numerical constants, network depth, or use of Dini's theorem where another justified compactness argument works.

The standard compact finite-dimensional C^1 approximation theorem may be invoked after stating its relevant form and checking the activation and target-domain hypotheses. It does not by itself prove mixed uniform-in-shape approximation on unbounded parameter inputs. A paper-specific mixed-norm theorem or named specialized method cannot replace that obligation without a derivation.

An approximate cutoff is sufficient; an exact nontrivial compactly supported GELU network is not required. Merely asserting polynomial growth is insufficient under a finite p-th input moment unless the required moment order and construction-dependent constants are controlled. A bounded compact approximant alone also does not close the tail argument when its bound can grow with the chosen radius or accuracy.

Failure to approximate the shape derivative, omission of a valid tail argument, a circular radius/network-bound choice, or substitution of tolerance-dependent bases for the arbitrary fixed bases is theorem-critical. Do not penalize a valid proof for avoiding cutoffs through another complete unbounded-input approximation argument.

For a gradient bound delta<=C eta, the objective-gap target epsilon^2 requires eta<=sqrt(2 lambda)epsilon/C, not sqrt(2 lambda epsilon)/C. The final accuracy must satisfy this and the distance and mixed-error requirements simultaneously.

All theorem-critical obligations in the replacement reference are closed; there is no unresolved private GT warning.
