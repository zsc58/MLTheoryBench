# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Uses differentiability, the rank condition, and continuity of the derivative to choose one local tangent ball, independently of the subsequently quantified scale, and prove the co-Lipschitz estimate with constant \(s_0/2\).
- **3 points:** Constructs a sufficiently large finite \(\rho\)-separated latent set and correctly transfers its separation through prediction accuracy and decoder Lipschitzness to obtain hidden-mean separation \((c\rho-2\delta)/L\).
- **4 points:** Projects the hidden means onto \(S\), derives the \(\sqrt{\lambda^2-4\varepsilon^2}\) separation bound in its positive-separation regime, applies the dimension-sensitive packing comparison, and correctly rearranges it, including the \(\lambda\le2\varepsilon\) and nonpositive-bracket cases, to prove the stated lower bound.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The public task requests only the final lower bound. The local co-Lipschitz estimate and the packing inequality are intermediate steps in the reference argument, not additional public conclusions that must be separately stated or labeled.

Standard finite-dimensional Euclidean packing and covering comparisons may be invoked with their correct dimensions, radii, and separation parameters; reproducing their volume proofs is not mandatory. A proof must not square a potentially negative separation lower bound without first restricting to a regime where it is nonnegative.

The hypotheses permit \(M=0\), and there need not be any admissible \(\rho\) when the approximation error is large. A general argument covering these cases is sufficient; separate case labels are not required. The conclusion need not be strictly positive, and \(d_0>k_\star\) must not be imposed as an extra hypothesis.

A valid geometric proof may use the stipulated limiting means without otherwise using the stochastic stability assumption. Do not require an inference from averaged conditional-residual convergence to convergence for every latent; that inference is not an assumption or proof step of this task. Likewise, do not require continuity of \(m\), global Lipschitzness of the decoder, or a local radius uniform over unspecified families of models.
