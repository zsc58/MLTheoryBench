# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly decompose the recursion into the spherical direction chain and logarithmic additive increments, justify nonvanishing and positive homogeneity for every allowed alpha, and establish the first and second logarithmic-moment bounds for both admissible matrix laws. In the entry-density case, justify the needed inverse-norm control, for example through the column-distance and bounded-density small-ball argument. In the orthogonal case, use the fixed operator and inverse norms.
2. **3 points:** Prove a uniform one-step Doeblin minorization in both cases and deduce existence and uniqueness of the stationary probability and uniform geometric total-variation mixing. In the scaled-orthogonal case, distinguish the actual positive-density law from the auxiliary Haar reference law: only the reference law is necessarily invariant. A direct contraction argument or an applicable standard uniform-ergodicity theorem is acceptable.
3. **2 points:** Prove finiteness of the stationary drift and identify it with the limiting constant. Establish the almost-sure law for every fixed nonzero input and the stated uniform-in-input L1 convergence, preserving the supremum outside expectation and the normalization by the initial norm. A verified additive-cocycle LLN or a direct martingale/coboundary argument is acceptable. The latter may use the Poisson solution constructed for the next step.
4. **3 points:** Justify the bounded Poisson-equation solution and the centered martingale or equivalent centerability construction. Complete the Gaussian-limit argument with an input-independent variance gamma^2>=0. For a martingale proof, verify convergence of averaged conditional variances and a valid Lindeberg or characteristic-function remainder condition; control the bounded endpoint correction and the fixed initial log norm. For an abstract cocycle proof, state the result being used and justify all hypotheses and its applicability to the actual semigroup setting rather than merely naming the specialized theorem.

# Evaluator Notes

Accept a complete valid alternative proof and any valid ordering of the arguments. Do not require the reference proof's incidental presentation choices or its explicit variance formula. A correct proof may derive the LLN and CLT from the same Poisson/martingale decomposition.

A response that merely names ergodicity, a Lyapunov exponent, or a central-limit theorem without verifying the relevant minorization, moments, and fluctuation hypotheses does not earn the corresponding points. In particular, a declaration of centerability followed only by the name of the specialized cocycle CLT does not establish its applicability to the non-locally-compact semigroup setting.

Do not require strict positivity of the limiting variance. Include the allowed cases d=1, alpha<0, alpha=1, and negative eta; negative eta is equivalent to positive |eta| after replacing Q by -Q. Almost-sure convergence is required for each fixed input, not on a single event simultaneously for all inputs. Do not replace the requested supremum of expectations with an expectation of a supremum.
