# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(2 points)** Correctly uses the population score and its declared positive-normalizer domain. Establishes that the truthful marginals are positive, that the truthful risk is finite, and that candidate risks and the excess-risk expansion are well defined, including potentially infinite candidate risk. Correctly obtains the classwise excess-risk identity or an equivalent valid comparison without subtracting infinity from infinity.
2. **(3 points)** Proves or correctly applies the expectation-form log-sum inequality with the hypotheses and finite-equality condition needed for the class coordinates. Handles positive true-label mass on a zero forecast-coordinate set, or uses a method that validly includes that case. If an auxiliary measure is used, its normalization and the expectation identities must be valid. Continuity and the support condition must justify upgrading almost-sure proportionality to pointwise proportionality.
3. **(2 points)** Uses nonnegative coordinate gaps, or an equivalent argument, to establish minimization by the truthful kernel. Correctly uses the finite truthful risk to infer that equality of total risks forces finite equality in every relevant coordinate and hence constants of proportionality.
4. **(3 points)** Establishes positivity of the proportionality constants using completeness or the already established positive truthful marginals. Uses simplex normalization and completeness to force every constant to equal one, proves pointwise equality of the kernels, and verifies the converse, concluding strict properness on the stated domain.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, auxiliary variables, or derivation of a general lemma when a direct proof covers every candidate in the public task.

Candidate kernels may vanish at individual feature points or on measurable sets. Only their class normalizers are required to be positive. Do not require pointwise strict positivity, a uniform lower bound, compact support, finite candidate risk, or an additional integrability assumption. Conversely, the task does not require assigning a score to candidates outside the stated normalization domain.

A proof applying the log-sum inequality only with positive class means need not prove its unused zero-mean versions. If a general extended-real log-sum statement is asserted, its proportionality characterization must concern finite equality: when the denominator mean is zero and the numerator mean is positive, both sides equal positive infinity without implying proportionality. Never treat such infinite equality, or a difference of two infinities, as a zero excess-risk gap.

Routine finiteness or boundary details may be omitted only when they are readily repairable and the argument remains mathematically valid. An unaddressed singular-support case that invalidates an auxiliary-measure identity, failure to establish the equality characterization, or failure to obtain completeness-based uniqueness is a substantive gap. The conditional-feature-density assumption need not be used explicitly, since the public setup separately provides the continuity needed by this proof.
