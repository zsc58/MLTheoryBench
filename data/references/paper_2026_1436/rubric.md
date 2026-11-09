# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Defines the signed diagonal augmentation and proves the cross-augmentation comparison with partial transport; verifies equal mass and integrability and uses Kantorovich-Rubinstein duality with Lipschitz ReLU tests to derive the global sup-norm bound.
- **3 points:** From uniform sphere convergence to a target compactly supported in X, derives vanishing diagonal, low-persistence, and high-persistence tails in persistence-weighted mass; truncates to a fixed compact core; establishes compact-core inverse convergence by a justified ReLU approximation argument or a fully justified compact-core Holder estimate; and controls discarded mass by its deletion cost. Includes the zero-target case. Do not require vanishing first-moment or r-weighted tails, which is false in general.
- **2 points:** Establishes injectivity through the positive cross-augmentation transform and a justified uniqueness argument. A complete hinge-derivative and linear-projection uniqueness argument is sufficient. Equality in L2 must be converted to equality of the continuous sphere functions when needed.
- **2 points:** For compatible A,B, proves the truncation and local sphere Lipschitz estimates, uses a correct compact-sphere L2/uniform estimate, and removes truncation using both tau_R->0 and A(B_R)tau_R->0. At fixed R, retain the truncation defect in the limsup; do not assume the truncated differences converge to zero in L2. Handle zero Lipschitz constants without division by zero.
- **1 point:** Combines the global L2 bound, injectivity, the L2-to-uniform bridge, and compact-target inverse continuity to obtain the homeomorphism onto the image, including the constant 4sqrt(2pi) for ordinary, unnormalized surface area measure.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or the stronger quantitative Holder rate, which is not a public target. The replacement reference closes the public inverse theorem by qualitative finite ReLU approximation using the same compact-core testing mechanism.

Use pers(b,d)=(d-b)/2 throughout. In particular, deletion to zero costs Pers(mu), and the growth constraint uses this same normalization.

Do not credit an assertion of the compact-core approximation bottleneck as a completed proof step without a justified derivation or an applicable audited standard-independent result. The specialized Sobolev-to-ReLU-variation embedding labeled theory_011 is not standard independent and is not proved in the supplied source. The reference's final quantitative section is a conditional reduction, not proof closure. A solver who uses that stronger route must supply a valid justification of its specialized input or otherwise close the required compact-core convergence step.

# Private GT Quality Warning

Every public conclusion is proved in the replacement reference. The retained stronger private quantitative claim still has an unresolved specialized dependency: the W^{5/2,2}(B_1)-to-affine-ReLU-variation embedding. Local normalization, dilation, scale-range, and endpoint errors have been repaired, but these repairs do not establish that embedding. This auxiliary gap is not a source-theorem counterexample and must not be treated as a completed rubric derivation.
