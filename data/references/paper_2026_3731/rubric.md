# Scoring Guide

- **0:** No correct relevant idea.
- **1–2:** Relevant ideas, but no completed core step.
- **3–7:** Some correct core steps, with material obligations unresolved.
- **8–9:** Essentially complete proof with only readily repairable local omissions.
- **10:** Complete proof, including domain and conditioning checks.

# Core Steps

1. **2 points:** Derive the forward and backward mixed-rank means and the positive expected log drift for admissible oracle coefficients; account for pure-segment factors.
2. **3 points:** Verify independent-coordinate bounded differences in both directions. Use valid forward blocks with $1\le m_k\le k$, sum the resulting tail probabilities, and handle the joint conditioning probability and critical logarithmic rate.
3. **3 points:** Use backward blocks containing only existing pre-change observations, including the $u_k=T$ boundary. Establish a super-uniform finite or capped survival threshold, split the stopping-dependent threshold, and prove summability under both strict conditions on $s'$.
4. **2 points:** Combine the two contributions under the same event $E_T$ and obtain all three rates and $o(1)$ relative size.

# Evaluator Notes

Accept any complete alternative proof under the public assumptions. A backward argument cannot receive full credit merely by citing the forward calculation without checking its reversed rank and observation sensitivities. Neither an undefined $X_0$ block nor an undefined $r_\infty$ closes a proof step. Do not require the particular auxiliary sequences in the reference proof if another valid choice proves the stated rates. Propagate a failed dependency only to conclusions that use it.
