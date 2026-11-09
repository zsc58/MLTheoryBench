# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the given Gaussian source posterior and its precision, recognizing that the positive prior precision makes the covariance well defined even for a rank-deficient design. Re-derivation of the supplied source posterior formulas is not required.
- **3 points:** Evaluates Z_theta(x) by a valid Gaussian integral or equivalent argument, obtaining Z_w^{-1} exp(beta theta^T phi(x) + beta^2 sigma^2/2), and thereby establishes its finite positive value and its parameter dependence. Theta-independent factors may be left implicit if their finiteness and independence are justified.
- **3 points:** Applies the defining per-observation correction and completes the square, or gives an equivalent valid argument, to obtain the mean shift -beta Sigma_theta sum_i phi(x_i).
- **2 points:** Identifies the full normalized Gaussian adjusted posterior and establishes that its covariance is exactly Sigma_theta. A completed-square expression with positive definite precision suffices to justify normalizability; an explicit normalizing constant is not required.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. In particular, the public task already defines the adjusted posterior, so deriving a conditional target/source likelihood ratio is not a separate scoring requirement.

If a solver discusses that ratio, distinguish the locally normalized conditional tilting model from a globally normalized joint distribution. The product p_s(x)Z_theta(x) is an unnormalized covariate marginal unless an appropriate global normalizer has been included. No additional global exponential-moment condition over x is needed to prove the task.

Do not interpret the adjusted posterior as a posterior obtained from genuine target training data. Do not require source representativeness, predictive-tilting arguments, or conformal-calibration results.

Deduct for an unsupported evaluation of Z_theta(x), a wrong sign or scale in the mean shift, or claiming an unchanged covariance merely from an unchanged mode equation without identifying the Gaussian density or an equivalent distributional argument. A valid quadratic-density argument establishes both the distribution and covariance.

The proof must apply to beta=0, zero feature sums, and rank-deficient design matrices. Separate discussions of these cases are unnecessary when the argument already includes them.
