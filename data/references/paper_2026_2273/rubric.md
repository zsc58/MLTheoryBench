# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Transformation mechanism (2 points):** Establishes the policy-value shift and its consequence for optimal values, or an equivalent mechanism sufficient for the normalization and inverse claims. A Bellman-inverse calculation is sufficient. Advantage invariance and the identity relating policy normalization to advantages are valid supporting steps, but they are not separately required by the public task.
2. **Existence and normal characterization (3 points):** Proves that the specified normalization is normal and that a reward is normal if and only if its statewise reward maxima are zero. A proof may use Bellman optimality, an optimal policy and advantages, or an equivalent argument. If an optimal policy is used, simultaneous attainment of the optimal value must be justified or obtained from a correctly stated applicable finite discounted-MDP result.
3. **Orbit uniqueness (3 points):** Proves that two normal rewards in the same orbit coincide. Either the optimal-value shift or the policy-operator invertibility argument earns full credit. Do not require an optimal-policy calculation when a valid direct shift argument is given.
4. **Topology and principal-bundle statement (2 points):** Establishes continuity of normalization and optimal value, verifies the two inverse identities for the requested maps, and justifies the principal-bundle conclusion through the continuous fiber-preserving action and an equivariant trivialization or equivalent argument. Finite maxima of continuous policy-value maps give a valid continuity proof.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or identities that are not targets of the public task. Penalize as theorem-critical any unsupported uniqueness, normality, or homeomorphism claim.

The discount range is 0 <= gamma < 1. Arguments based on the Bellman inverse or contraction estimates include gamma=0; a separate endpoint discussion is unnecessary when the argument already applies there. Do not assume irreducibility, unique optimal policies, strictly negative rewards, or more than one action per state.

The displayed product coordinates use positive optimal value, so the original reward action subtracts the group parameter from that coordinate. This does not invalidate the principal-bundle claim: negating the value coordinate gives a standard additive equivariant trivialization. Accept any consistent equivalent convention. Do not demand that the specifically displayed product homeomorphism itself be equivariant for positive translation.

Do not accept the claim that an arbitrary continuous image of a closed noncompact set is closed. In particular, the full orbit quotient map need not be closed. A quotient-based proof must justify closedness of the relevant normal-set saturations or otherwise prove continuity of the normalization map. A direct finite-policy continuity argument avoids this issue entirely.
