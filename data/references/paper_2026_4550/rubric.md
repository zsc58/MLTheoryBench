# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Inner-loop estimate (2 points).** Uses the stated coordinate update and conditional simulator law to cancel the centered cross term, handles history-dependent coordinate probabilities, and derives the cycle-start-conditioned mean-square recursion. Establishes the inverse-linear rate with the stated c1 and c2, with consistent conditioning and terminal-iterate indexing. The initial residual estimate must square the sum of norms rather than discard its cross term.
2. **Expected-norm outer estimate (2 points).** Uses conditional Cauchy-Schwarz, the norm comparison, Bellman contraction, and total expectation to obtain the expected-sup-norm recursion under the explicit c1-based frequency floor. Derives the certificate as an upper bound for actual error rather than assuming that relationship. Correctly distinguishes random conditional quantities from unconditional expected errors.
3. **Fixed-frequency result (3 points).** Proves accuracy and eventual satisfaction of the floor, handles upward rounding, and obtains the claimed parameter-dependent cost. Proves quasi-optimality against every certificate-feasible fixed comparator, allowing arbitrary outer counts and error allocations. Does not infer a necessary condition for actual stochastic accuracy from a sufficient upper bound, or assume an unsupported bound on the arbitrary initialization.
4. **Geometric result (3 points).** Establishes the weighted allocation and a valid lower bound, for example through an explicit Holder calculation. Proves accuracy, eventual satisfaction of the c1-based floor for the smallest frequency, rounding control, the epsilon^(-2) cost without a logarithmic factor, and quasi-optimality against every certificate-feasible variable comparator.

# Evaluator Notes

The required error criterion is `E[||Q_n^(0)-Q*||_infinity]`, matching the source's schedule-design claim. A correctly proved RMS bound is an acceptable stronger route to the required accuracy, but RMS is not the definition of E_n in this task. Do not require almost-sure or pathwise accuracy.

Quasi-optimality is relative to the public deterministic certificate and relaxed real-frequency comparison classes. No minimax lower bound over MDPs or instance-wise optimality over all actually accurate schedules is requested or justified.

Accept any valid alternative proof. Merely naming the specialized external optimization theorem does not close the allocation or comparison obligation; a correct direct argument or a precisely stated applicable result is needed.

The bound parameter sigma^2 is strictly positive even when actual reward variance is zero. Treat E_0=0 by the empty schedule. A minor omission of this elementary case is readily repairable; incorrectly excluding zero-noise MDPs or replacing the exploration/observation model is not. The endpoint gamma=0 is included and causes no singularity because mu>=1/2.

Big-O is asymptotic in epsilon. Multiplicative constants may depend on the fixed reward bound and variance-bound parameter, but not on gamma, xi, or the state/action cardinalities. The sufficiently-small-epsilon threshold may depend on all fixed setup parameters, including initialization. A proof may not obtain this dependence by assuming the arbitrary initialization already lies in the reward-controlled value range.
