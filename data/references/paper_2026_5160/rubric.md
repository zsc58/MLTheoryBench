# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly bounds \(\log p(S)\) and the negative KL term by zero on the stated feasible domain, including their equality conditions.
- **3 points:** Verifies that the stated uniform-on-\(S\), zero-off-\(S\) policy is feasible and attains objective value zero.
- **4 points:** Establishes uniqueness by deriving simultaneously \(p(S)=1\) and \(q=u\) for any maximizer, then correctly converts these facts into the probabilities on and off \(S\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A solution that only identifies the candidate policy without proving both equality conditions and their implication for the full policy cannot receive full credit.
