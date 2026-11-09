# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Boundary model and eviction-free equilibrium (2 points).** Uses the continuous saturated execute–evict–admit dynamics on B, with M>l_0+L. Correctly identifies the stage weights, computes W=sum_j w_j, and identifies the unique equal-mass fixed point x^*=(M/W)1. Distinguishes waiting arrivals from admitted active mass.

2. **Amplification and instability of the fixed point (3 points).** Establishes nondecreasing maximum and nonincreasing minimum during eviction-free evolution, or supplies an equally valid alternative. Proves finite-time breakdown using a quantitative argument, such as the running-maximum contradiction. Repeated strict spread growth together with boundedness is not sufficient by itself. Connects the breakdown to a fixed positive escape distance from the fixed point. Allows an exactly zero admission to cause the first support loss before a strict overflow.

3. **Cascade, intermediate instability, and exceptional set (3 points).** Establishes non-revival of lost relative positions, derives a correct fixed-support sampled map and normalization or an equivalent rigorous mechanism, and proves finite support loss unless the trajectory is periodic and balanced. Sampling intervals must agree with the actual completion times; they are not generally complete L-step blocks. Shows that intermediate periodic orbits are unstable and that the exceptional set consists precisely of finite-time captures by nonmaximal periodic orbits. Proves relative nullity separately on every fixed-support face, including pullbacks through support-loss branches and the countable union over capture times. Merely observing that balanced target states satisfy linear equalities does not establish nullity of their preimages. Handles singleton faces and the empty intermediate range when L=2.

4. **Maximal cycle, stability, and basin conclusion (2 points).** Identifies the one-position cycle with phase-j mass M/w_j, not a phase-independent mass. Establishes the local Lyapunov stability and attraction quantifiers outside E, for example by strict phase inequalities and finite local absorption. An asserted contraction requires an actual estimate; it is not sufficient to say residual mass is damped. Concludes that every boundary state outside E reaches the maximal cycle in finite time and subsequently has zero distance to it.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its notation, or use of normalized spread when another rigorous proof closes the same obligations. A proof of ordinary local asymptotic stability is acceptable because it implies the requested stability outside E.

The public definition of E uses intermediate periodic orbits rather than undefined balanced coordinates. A proof using the source-style normalized description must justify that every intermediate periodic orbit is balanced; it must not assume this as an additional public hypothesis.

Do not award full credit for merely naming a cascade, monotonicity, null-set argument, or stability mechanism without establishing the corresponding claims. Do not require the auxiliary worst-throughput result: it is not part of the public target.
