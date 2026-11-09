# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the recurrent-block reversal identity, its probability normalization, the PageRank equation, and the coordinate value formula; handles zero reward.
- **2 points:** Uses the finite transient/recurrent block decomposition and correctly solves recurrent blocks independently.
- **3 points:** For a positive-spectral-radius transient block, establishes the needed Perron eigenstructure, stochastic reversed kernel, probability normalization, and PageRank formula with parameter gamma lambda and reward-weighted restart. A valid direct algebraic derivation is as acceptable as one using a Doob transform.
- **3 points:** Processes transient blocks in reverse downstream order with gamma on every cross-block contribution; handles zero effective reward and the singleton zero-spectral-radius case; assembles the unique global value.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's presentation. Merely naming PageRank, time reversal, Perron-Frobenius, or a Doob transform without establishing the identities and applicable hypotheses earns no credit for those identities. Do not penalize a correct direct treatment of the zero-spectral-radius block for not defining a Doob transform there.
