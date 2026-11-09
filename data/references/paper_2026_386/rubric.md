# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points: Exponentially close cross-subtree pair.** Establish, using a Euclidean covering or an equivalent volumetric argument, leaves from distinct depth-$q$ subtrees at distance at most $CA\exp(-((\log b-4\varepsilon)D)/(2p))$, with an absolute $C$. The growth-bound contradiction and the independence of $C$ from $p$ must be justified. Count leaves with multiplicity when distinct leaves have the same image. Cover all relevant resolution regimes, using the diameter bound when appropriate. Also establish that the leaves are intrinsically at least $\rho D$ apart.
- **2 points: Intrinsically smooth branch cut.** Use the lowest common ancestor and its two relevant child branches to construct the $1,-1,0$ leaf labels, and prove that every differently labelled pair is separated by at least $D$ edges, yielding leaf Lipschitz constant at most $2/(\rho D)$.
- **2 points: Whole-tree extension.** Correctly extend the leaf function to all vertices without increasing its intrinsic Lipschitz constant and preserve the range $[-1,1]$, for example by a McShane extension followed by clipping. Verify agreement with the prescribed leaf values.
- **3 points: Euclidean lower bound.** Derive an output gap of at least $1$ from the two-point approximation condition and use the collision scale to obtain the claimed exponential lower bound with a universal positive prefactor. Division by the represented distance is justified when an admissible predictor exists, since its output gap forces that distance to be positive. If the two represented points coincide, correctly conclude that the approximation condition is impossible and the required implication is vacuous.

# Evaluator Notes

Accept any complete valid alternative proof. The listed steps describe one proof architecture, not mandatory intermediate results for a different complete proof. Merely invoking pigeonhole, volume, or an extension theorem without verifying the hypotheses and quantitative constants does not complete the corresponding step. In particular, a covering estimate with a dimension-dependent base, without an additional argument yielding a universal final prefactor, does not establish the required bound.

A failed collision argument normally leaves the final lower bound unsupported. However, if the solver independently establishes a pair with the required separation and collision scale, later achievements using that pair should receive their corresponding credit.

Do not impose injectivity of $F$ or require the existence of a predictor satisfying the approximation condition. Coincident represented leaves are allowed. An explicit coincident-image case split is not mandatory if the solver correctly observes that the approximation-induced output gap implies distinct represented points before division.

The regular-growth assumptions are inconsistent when $D=1$, since the sole depth-zero subtree contains every leaf and its upper bound is smaller than the leaf lower bound. A proof need not construct witnesses for that impossible case. Do not replace the stated parameter range by a stronger hypothesis.

This is a deterministic geometric theorem under the displayed growth inequalities. No sampling model, offspring-law assumption, or proof that a regular-growth event has high probability is part of the task.
