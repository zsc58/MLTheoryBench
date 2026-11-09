# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points: Lifted geometry.** Constructs a threshold-augmented measurable convex objective whose population minimum equals the CVaR optimum; verifies that its population objective is finite; obtains Lipschitz constant at most $\sqrt{\Gamma^2+s^2}/\alpha$ and product-domain diameter at most $\sqrt{\Delta^2+M^2/s^2}$; and chooses $s^2=\Gamma M/\Delta$ to obtain $(\Gamma\Delta+M)/\alpha$. A direct maximum-of-convex-functions argument or a justified bounded-subgradient argument is acceptable, including on lower-dimensional domains.
- **2 points: Private upper bound.** Correctly applies the assumed upper interface in ambient dimension at most $d+1$, relates lifted excess to CVaR excess, and verifies record-level privacy and output post-processing. The learner must be chosen independently of the unknown distribution and work for every admissible distribution. Merely citing the interface without establishing the lift and excess comparison does not earn this step in full.
- **2 points: Exact tail embedding.** Starting from nonnegative ordinary convex losses of scale $R_0=\min\{M,\Gamma\Delta\}$, constructs the Bernoulli activation and proves directly from the variational definition that embedded CVaR equals ordinary expected loss for every decision. It must also verify boundedness, convexity, and the required Lipschitz bound. Any common loss shift must preserve ordinary excess risk.
- **3 points: Privacy-preserving transfer and lower bound.** Builds the $m=\lceil4n\alpha\rceil$ sample coupling, proves privacy by conditioning on its independent activation randomness, controls the overflow event by a binomial tail bound, and transfers the ordinary lower interface with the correct learner-then-distribution quantifiers. The ideal sample must have the unconditional iid embedded law; agreement with the actual sample on the no-overflow event suffices. Justifies the saturated comparison between $m$ and $n\alpha$, including $n\alpha<1$, and retains the displayed residual and inherited logarithmic factors. Merely asserting that $n\alpha$ is the effective sample size is insufficient.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The ordinary private convex-optimization interfaces are explicit primitive assumptions of the problem and need not be reproved. Their classification as imported nonstandard dependencies does not authorize claiming that their external proofs have been verified; the task asks for the conditional CVaR reductions.

A privacy argument that incorrectly invokes output post-processing for the randomized input transformation has a material gap unless it separately establishes that neighboring ordinary datasets induce neighboring synthetic datasets conditionally on the independent randomness. All synthetic records, including active dummy records on overflow, must belong to the chosen record space.

Do not require the actual synthetic sample, or the ideal sample conditioned on no overflow, to have the unconditional iid law. The valid requirement is a coupling to an unconditionally iid ideal sample that agrees outside the overflow event.

The statement is not a complete matching statistical minimax rate, nor a scale-sharp comparison for arbitrary $M,\Gamma,\Delta$. Preserve the different upper and lower statistical terms, the upper scale $\Gamma\Delta+M$, the lower scale $R_0$, the privacy-parameter ranges, saturation, and residual. Missing a routine ceiling case alone is a readily repairable omission, not a reason to reject an otherwise correct reduction.
