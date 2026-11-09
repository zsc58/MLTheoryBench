# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Identifies the mixture likelihood and normalized posterior; justifies positive-energy differentiation and posterior-precision finiteness; derives the precision identity and h'; correctly transfers MLR through the common positive tilt and proves the reversed precision-expectation inequality. Establishes the integral formula with h(0) by integration from a positive lower endpoint and passage to the finite right limit.
- **2 points:** Correctly evaluates the inverse-gamma scale specialization, obtains the stated log-likelihood ratio, and proves h(0)=-d log r, strict increase, and limit nu log r, hence bounded per-location evidence. Correctly incorporates the class scale into the effective mixer or conditional density.
- **2 points:** Proves that strict increase makes thresholding h(q) and q equivalent for the one-location ROC, including constant endpoint decisions; distinguishes bounded evidence from unbounded raw-energy support without assuming finite energy moments.
- **2 points:** Uses the specified conditional independence and common class marginal law to identify the joint log-likelihood ratio as sum_k h(q_k), and applies Neyman-Pearson optimality at every test size, allowing boundary randomization. Obtains the corresponding K-location evidence bounds and unbounded raw-energy sum.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a particular allocation of intermediate arguments.

For positive q, the relevant integrability and dominated differentiation follow from boundedness of u^(-b)exp(-epsilon/(2u)) for epsilon,b>0, multiplied by the probability density. An equivalent rigorous justification is acceptable. Do not require moments at q=0, finite covariance of z, or restrictions such as nu>2 or nu>4.

The endpoint formula is conditional on a finite right limit of h and uses an improper integral. Do not require the individual F_c(0) to be finite when a finite limit of their log difference exists. Omitting the additive constant, leaving differentiation unjustified, or asserting the posterior expectation order without a valid argument leaves a core obligation unproved.

A correctly stated standard MLR-to-stochastic-order theorem, with its hypotheses checked, is sufficient; a direct double-integral or other valid argument is also sufficient. Zero values of the mixer densities are allowed by the cross-product formulation. Do not impose strict positivity of both densities as an additional requirement. The exact posterior ratio includes the positive factor F_-(q)/F_+(q); an omitted factor is a local normalization error if the argument only needs and correctly uses monotonicity, rather than automatically a fatal failure of the entire proof.

The specialization uses the density of u=s_c^2v in the general transform, not the unscaled common density of v in both classes. The common inverse-gamma law is resampled independently at distinct locations. A single shared latent draw across locations is a different experiment and does not justify the product likelihood.

The interval [-d log r,nu log r] is a valid bound; the upper endpoint need not be attained at a finite energy. Neyman-Pearson optimality is a most-powerful-testing statement for the two specified class distributions, not a claim of uniqueness of the statistic. No strict aggregation advantage, universally monotone AUC gap, or Gaussian-limit calculation is required by this task.
