# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Universal weighted-vote reduction and finite-sample bound (3 points).** Defines the weighted miscoverage quantity, proves ensemble miscoverage forces it to be at least one-half, applies Markov and conditional base validity, and obtains coverage at least $1-2\alpha$ for every $n$.
2. **Asymptotic base-validity extension (2 points).** Uses the uniform $o_p(1)$ deviation of learner miscoverage probabilities, controls its expectation via boundedness, and derives the $1-2\alpha-o(1)$ bound and liminf conclusion.
3. **Coalition-majority argument (4 points).** Uses set-consistency and the strict optimal coalition-weight margin to show estimated coalition weight exceeds one-half with probability tending to one; combines this with the coalition union-miscoverage bound to prove liminf coverage at least $1-\alpha$.
4. **Dominant-learner specialization and scope (1 point).** Correctly identifies the singleton coalition case and states that the coalition conclusion applies in either validity regime.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the asymptotic regime or of the coalition/dominant conclusion as a theorem-critical gap.
