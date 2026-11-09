# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Conditions correctly on the reference data and fixed width function, obtains iid bounded test quantities, and constructs a feasible fixed comparator with positive expected log gain for all sufficiently small positive k. Handles both signs of the mean and obtains a quantitative lower bound of order Δ0 squared when needed for the delay claim. Does not replace the expected confidence width by its maximum in the signal condition or use an optimizer outside the permitted interval.
- **3 points:** Establishes logarithmic regret for the specified ONS recursion, including its sign, initialization, coefficient 4, and projection. Verifies the relevant exp-concavity and gradient hypotheses, or proves the regret inequality directly. Derives the exact adaptive-versus-fixed log-wealth identity. Does not rely on the false assertion that all positive-k factors are at least 1/2.
- **3 points:** Gives a valid fixed-comparator growth and concentration argument, with logarithmic regret dominated by the linear growth term, and proves almost-sure eventual rejection. For the claimed delay rate, establishes adequate variance-sensitive concentration or another valid quantitative argument. A uniformly bounded variance alone combined with a drift-squared exponent does not establish the required rate. Keeps the comparator independent of the test observations and justifies transfer from the limiting benchmark to sufficiently small positive k.
- **2 points:** Uses a valid stopping-time tail bound and summation, or an equivalent argument, to obtain the stated Δ0^{-2} log(1/(αΔ0)) + Δ0^{-2} order with a universal constant. Handles the small-k quantifiers without assuming that expectations of stopping times commute with a limit. Uses non-rejection as a subset of the below-threshold event, not as an equality after possible prior crossings.

# Evaluator Notes

Accept any complete valid alternative proof; incidental comparator choices and numerical constants need not match the reference proof. An algebraically equivalent expression of the specified ONS recursion is acceptable, but changing its learning-rate coefficient, adding clipping or warm-up, or substituting a different procedure requires a proof that the original task is nevertheless solved. A standard regret or concentration theorem may be used if its relevant statement is supplied and its hypotheses are verified. Merely citing a paper-specific lemma or naming a method does not close a theorem-critical step. Distinguish an expected log gain from a lower bound for it. Preserve the betting interval when optimizing a quadratic. Zero variance and zero width are admissible; a zero effective limiting margin is excluded by the task's assumption. Do not require proof of a separate null-validity theorem.
