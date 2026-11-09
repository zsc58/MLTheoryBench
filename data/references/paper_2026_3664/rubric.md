# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes a valid uniform upper-bound route for the expected countable-coordinate supremum, such as the pointwise comparison with the Euclidean norm and Jensen's inequality.
- **2 points:** Completes the upper bound uniformly in p and n, for example by justifying exchange of the nonnegative sum and expectation and computing sum_i Var(hat p_i)=(1-sum_i p_i^2)/n<=1/n.
- **3 points:** Establishes Delta_n(p*)=Omega(n^(-1/2)), with a justified binomial or Rademacher lower bound valid for all sufficiently large n.
- **2 points:** Combines the bounds with universal constants to prove both the fixed-p* comparison for every p and the two-sided supremum rate.

# Evaluator Notes

Accept any complete valid alternative proof under the public assumptions, including a correctly justified decoupling route. The Euclidean-norm route needs neither decoupling nor a sharp independent-Bernoulli maximum characterization. Merely naming a nonstandard result without stating an applicable bound and checking its hypotheses does not establish a step that relies on it. Do not deduct credit for omitting machinery unnecessary to an otherwise complete proof.
