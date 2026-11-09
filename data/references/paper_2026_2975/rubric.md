# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the direction and defining change-of-measure property of the path density \(R=dP_t/dQ_t\). A solver may use the density named in the setup directly; independently deriving its stochastic-exponential representation is not required by the public targets.
- **4 points:** Multiplies the density by the terminal likelihood and rigorously derives the weighted expectation identity for every bounded measurable path functional, including absolute integrability, the normalization constant, and the posterior tilt; obtains the endpoint filtering specialization.
- **2 points:** Uses the specified iid guided samples and self-normalized estimator, and establishes nonnegative integrable weights, integrability of the weighted numerator, and a strictly positive finite limiting denominator.
- **2 points:** Applies the iid law of large numbers and a valid ratio argument to prove convergence in probability to the posterior expectation for every bounded measurable endpoint test function, accounting for the zero-denominator convention.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat a reversed or missing Radon-Nikodym factor, an assumed weighted posterior identity without derivation, or an unsupported normalization limit as theorem-critical gaps. A direct measure-theoretic proof using the path density supplied in the setup can receive full credit.

If an answer additionally derives the Girsanov representation, evaluate that derivation correctly. Novikov makes the stochastic exponential a martingale on the weak-solution probability space; preservation of the initial law and uniqueness in law identify the uncontrolled state law. Identifying the exponential itself with the state-path density also requires state-path measurability. In this task, that follows from the covariance-matched gradient control, by integration against the state martingale part, and does not require covariance invertibility. In a general weak representation, the pushforward density is a conditional expectation, not automatically the same exponential. Do not impose invertibility, strict positivity of the likelihood everywhere, second moments, or an explicit density formula on a valid proof of the requested identities and convergence.
