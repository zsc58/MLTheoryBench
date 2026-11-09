# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly instantiates certifiability using an unlabeled certifier and a single distribution-fixed learner/certifier pair. Uses soundness for that same learner at arbitrary empirical marginals, not merely at the original marginal. Preserves the worst-case-over-hypotheses definition of error and the global soundness requirement.
- **3 points:** Constructs the size-M empirical marginal and correctly compares sampling its occurrence indices with and without replacement. Derives E_U R_C(U)<=Gamma epsilon(D,m)+1-Gamma, or an equivalent valid inequality, where R_C(U)=E_{T~Q_U^m}C(T). Relates the empirical optimum at M-1 samples to this certificate using soundness and monotonicity of the optimum. An equivalent direct comparison using a learner that discards extra samples is also acceptable.
- **3 points:** Derives the OIG comparison. Accounts for randomized/fractional orientation optimality, simulates a distribution-fixed learner using samples from the non-withheld occurrences, and proves the conditional-loss bound with omission probability (1-1/M)^(M-1)>=1/e. Converts transductive to population error by exchangeability with the supremum over hypotheses in the correct position. Merely naming OIG, a transductive reduction, or an external specialized method is insufficient.
- **2 points:** Takes M=ceil(e m^2/eta), controls the collision contribution, and proves the target at exactly M-1 samples for every m>=1 and eta in (0,1). The union bound 1-Gamma<=binom(m,2)/M handles all positive sample sizes. States the final guarantee with the correct quantifiers and integer-valued sample budget.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its intermediate notation.

The central certifier-to-empirical-marginal and OIG transductive arguments must be mathematically derived; treating either as an unexplained assumption is a theorem-critical gap. The reference proof explicitly supplies these derivations and leaves no specialized external dependency unresolved.

The collision correction is essential. The assertion Gamma E[epsilon*(Q_U,m)]<=epsilon(D,m) does not follow from the sampling argument. Accept the source-equivalent inequality E[epsilon*(Q_U,m)]<=Gamma epsilon(D,m)+1-Gamma, where the expectation is legitimate, or the reference proof's measurable certificate-envelope formulation.

An omission event must concern an occurrence index. Repeated values in U do not invalidate the argument, but the probability that a repeated instance value is entirely absent need not be at least 1/e.

Fractional orientations are relevant to the exact constant. A proof using only deterministic orientation optimality must independently justify any claimed comparison with randomized transductive rules.

It is sufficient to use delta-optimal empirical learners and pass to the infimum. Do not demand attainment or a measurable selection of such learners when the proof uses only pointwise comparisons. Likewise, no expectation of an uncountable supremum is required if the proof integrates measurable fixed-hypothesis losses against a measurable certificate upper bound.

Do not accept an unsupported claim that OIG's population error is nonincreasing with sample size. The requested budget follows directly from the proof. A different budget alone does not prove the task, and m=1,2 cannot be dismissed by an unspecified adjustment. Empty H is trivial under the stated convention.
