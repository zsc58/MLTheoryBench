# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives uniform inner-loop second- and fourth-moment errors of orders O(n^(-1)) and O(n^(-2)) from the projected contraction recursion. Justifies the fourth-moment perturbation bound and establishes scalar comparison coefficients sufficient for both rates under the stated eta_0 and sufficiently large t_0. The bounds must hold uniformly for adapted X-valued initializations and outer points.
- **3 points:** Proves both oracle-bias orders. For the raw query, uses uniform fast-coordinate Lipschitz continuity. For the corrected query, derives the Taylor expansions with uniform quadratic remainders and the cancellation P^*A=C, giving squared bias O(n^(-2)) from the fourth-moment inner bound. Correctly conditions on the post-inner, pre-outer-sample history, distinguishes the unconditional second-moment bias bound from a pathwise accuracy bound, and verifies a uniform conditional variance bound for the fresh primitive observations.
- **2 points:** Establishes the projected regularized outer stability estimate and converts distance to the regularized fixed point into a residual bound containing lambda^2, exp(-cN beta lambda), beta/lambda, and epsilon_H^2/lambda^2, or an equally strong sufficient estimate. Justifies the regularized fixed point, the contraction or dissipativity estimate, control of the bias term, and iteration of the scalar recursion; verifies the required stepsize condition.
- **3 points:** Correctly balances both schedules, proves that the exponential transient is dominated by the target polynomial rate for fixed b<3/4, and counts all primitive calls, including the fresh residual F call in the corrected outer query. Obtains the fixed-b total-sample exponents 2b/(3+4b) and 2b/(3+2b), and establishes the respective one-quarter and one-third limiting exponents with the correct fixed-epsilon quantifiers and horizon-independent constants. Does not charge the separate exact structured P^* query to the specified primitive count.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices or particular numerical constants. A stronger valid estimate may replace the displayed outer decomposition. A claimed cancellation without deriving the linearizations, an unsupported fourth-moment rate, or a rate claim without valid bias balancing and sample-count conversion is incomplete.

Fresh outer observations must be conditioned on the history after the inner loop; reusing an inner observation without a separate valid argument does not satisfy the stated sampling model. The bias bound used by the outer analysis is an unconditional bound on its squared norm, not an almost-sure post-inner endpoint bound.

The limiting sample-rate notation means that for every fixed positive epsilon one may choose a fixed admissible b sufficiently close to 3/4 and obtain the stated epsilon-loss bounds for sufficiently large horizons. Do not require uniform constants as b approaches 3/4, and do not accept an unsupported substitution of b=3/4 or a horizon-dependent b. Singleton stabilized sets, mu=0, and zero observation noise are allowed; the proof need not exclude them or divide by their diameters or variances.
