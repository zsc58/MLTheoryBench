# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Reference-Proof Status

The reference derives the statistical and optimization steps and now supplies the efficient interval-truncated Gaussian implementation previously left open. Its central-uniform and tail-exponential rejection envelopes have a universal positive acceptance bound; a logarithmic attempt cap with a supported fallback gives the required TV tolerance and deterministic polynomial real-valued runtime. This construction closes the former specialized computational obligation without relying on its citation. Judge each submitted proof on its own merits.

# Core Steps

1. **Warm start and projection (2 points).** Derive a constant-radius empirical OLS estimate under the jointly conditioned observation law and construct a computable convex ball containing the true vector with the required probability. Verify concentration hypotheses and use the correct inverse-matrix norm and ball diameter. An equivalent residual-based derivation is fully acceptable.

2. **Unknown-set learning (3 points).** Establish a smooth, sampleable reference response law near the warm start and prove that the actual observed positive responses suffice for interval learning. Do not identify the actual positive law with the positive conditional of the D_obs-based untruncated law without proof: generally they differ. A direct gap-counting proof using domination of the target restricted measure is valid. Control both false negatives and false positives, polynomial interval complexity, computable response clipping, sample/time bounds, and failure probability. The VC dimension is 2k, not k+1. Treat k=1 and zero-displacement smoothness correctly.

3. **Perturbed likelihood control (3 points).** Define the objective with D_obs as its outer law and the Gaussian truncated to the intersection of estimated and true sets as its inner law. Verify positive normalizers, finiteness, and differentiation. Derive the Hessian, uniform curvature on the actual projection ball, and the gradient perturbation bound. Observed moments carry conditioning factors; an expected survival lower bound is not a pointwise bound. Conclude proximity of the constrained minimizer by strong monotonicity and constrained first-order optimality. Bounded-support conditional-TV estimates are an acceptable alternative to the source's change-of-measure presentation.

4. **Gradient implementation, PSGD, and composition (2 points).** Approximately generate the required interval-truncated Gaussian responses with verified support, TV, and computational complexity; derive conditional gradient bias and second moments; choose both set accuracy and sampling tolerance; analyze fresh-sample projected optimization and confidence boosting; and compose the claimed sample/time bounds. Roughly one point concerns statistical oracle control and optimization, and one concerns efficient oracle implementation and end-to-end computational closure. The reference's envelope construction is one valid implementation: verify proposal weights, the accepted-point law, a uniform positive acceptance bound, and the supported fallback's TV error. Ordinary rejection from the full Gaussian with expected cost inverse in survival probability does not by itself establish the required runtime. An interval-mixture representation alone likewise does not establish computational complexity.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental constants, sample allocation, or presentation choices.

A complete proof must close theorem-critical specialized dependencies by derivation, or replace them by an independently justified construction. Merely naming the positive-only learner, truncated-Gaussian sampler, perturbed-likelihood method, or specialized optimization theorem does not itself prove its applicable guarantee. Standard independent concentration or uniform-convergence theorems may be invoked with their relevant statements and verified hypotheses.

Check information access: only iid observed pairs, the supplied numerical bounds, and internal randomization are available. Synthetic untruncated responses must use fresh observed features, not samples from the unknown original feature distribution. Shared preprocessing does not make later samples reusable as independent adaptive gradients.

Check boundary cases without adding substantive assumptions: centered or deterministic features, zero parameter radius, alpha=1, unbounded true intervals, and k=1. Bounds can be padded to one for resource accounting, but endpoint formulas must not vanish incorrectly.

The computational conclusion uses the source's real-valued model. Do not impose an additional bit-encoding model absent from the task, or silently assume a specialized Gaussian-CDF or inverse-CDF oracle whose complexity has not been justified. The reference uses elementary exponential/logarithmic evaluations and internal uniform randomization to implement its proposals directly.

Do not award full correctness to a proof whose efficient sampler remains an unsupported specialized black box. Conversely, do not penalize a submitted proof because it closes that obligation differently from the reference. If sampling is capped, verify either that its fallback preserves support and its distributional error is included in the oracle analysis, or that a separately justified failure budget covers the cap. The central set-learning transfer, curvature/minimizer control, and computational gradient analysis remain theorem-critical.
