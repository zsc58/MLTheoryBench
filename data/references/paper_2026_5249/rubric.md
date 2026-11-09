# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly reduce universality of the shared-encoder architecture to density of the indexed architecture with the same latent dimension, using disjoint labeled copies, extension, symmetrization, and restriction. The prescribed function on permuted copies must preserve the coordinates associated with each cube label, so that the symmetric extension restricts to the original arbitrary ordered target, not its symmetrization.
- **3 points:** Establish alternating finite-difference rigidity for indexed latent maps and rigorously propagate equality from the axis subset of a finite grid to every grid point. Account for ordered tuples with repeated indices and justify the axis cardinality used in the dimension count.
- **4 points:** Carry out the obstruction construction with the correct quantifier order. Justify an antipodal-free closed cover of the tail sphere, fix the grid labels and two disjoint compact obstruction sets independently of the encoder, apply Borsuk-Ulam under \(M|A|<d(n-k)\), and propagate the resulting equality to obtain a collision between those same fixed sets for every indexed latent map. Construct one continuous separating target and prove a uniform error lower bound of \(1/2\) for every encoder-decoder pair. In the reference construction the obstruction sets are unions over all region labels, not sets selected after the encoder-dependent antipodal pair is found.
- **1 point:** Transfer the indexed lower bound to \(M_{\rm univ}\) and derive exactly the stated ceiling formula with the correct parameter ranges and integer dimension condition. Boundary cases must be covered, including \(D=d(n-k)=1\); if zero-dimensional latent spaces are admitted, exclude them rather than leaving that convention unresolved.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The central collision, finite-difference propagation, and dimension count are theorem-critical; merely naming Borsuk-Ulam or a grid argument without deriving the collision earns only partial credit.

For the obstruction route, the necessary quantifier order is a single target followed by all encoder-decoder pairs. A proof that only finds an encoder-dependent target does not establish non-density when encoders may depend on the target. Likewise, a fixed-feature injectivity argument alone does not prove the stated result.

A simplex-based construction supplies the required closed cover, but another correctly justified construction is acceptable. Tietze extension and Borsuk-Ulam may be used as standard independent results without reproving them, provided their relevant hypotheses and dimensional conditions are checked. Do not require a neural-network approximation theorem or an asserted equality between MLP and continuous-encoder minimum dimensions: the public task defines the continuous class, and the reference obstruction proves its lower bound directly.
