# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Implements exact trajectory sampling from unbiased probability-vector answers and independent product-likelihood estimation. Derives the expected, rather than almost-sure, O(n sigma^2/r) chi-square bound, with expectations over both the independent trajectory and evaluation noise. Handles zero-probability coordinates and counts calls to both oracles.
- **3 points:** Establishes stability of the normalized absolute-difference integrand, including its value when both estimated masses vanish. Constructs coupled increments using the same outer trajectory, proves geometric variance decay and the terminal bias bound, and includes integer sample counts and their cost. Obtains the stated upper bound with its exact log(1/delta) dependence over the full public confidence range. The reference uses median amplification at ordinary confidence and a routine low-success-probability wrapper near delta=1; equivalent valid treatments are accepted.
- **3 points:** Gives a complete hidden-block construction and adaptive information argument yielding Omega(n/epsilon^2). Explains why valid hidden-parent hits are identifiable in the transcript, justifies the conditional entropy bound, and supplies valid concentration, thresholding, lazy coin simulation, and sample-budget truncation. Transfers this lower bound to the noisy minimax class by selecting admissible exact oracles, or another valid argument.
- **2 points:** Constructs the rare-escape embedding on at most K symbols within the m-symbol alphabet, verifies its exact TV scaling, and supplies admissible oracle laws at all queried prefixes without a support-membership oracle. For sigma^2>0, verifies the empirical oracle's variance bound and conditional expected iid-sample consumption under adaptive querying. Preserves constant success after truncation, applies the finite-domain lower bound at the rescaled accuracy on K-1 points, uses sigma^2<=K to control the ceiling in M, handles sigma^2=0 separately, and combines the two terms.

# Evaluator Notes

Accept a complete valid alternative proof and assign credit by mathematical content rather than by matching the reference's presentation or algorithm. The point allocations identify obligations, not mandatory named techniques.

The independent finite-domain lower bound may be cited without reproducing its proof if the relevant statement is provided: estimating TV between arbitrary laws on a d-point domain to accuracy eta with fixed success probability at least 2/3 requires Omega(d/(eta^2 log d)) total iid samples in the small-accuracy regime used here. Its domain, accuracy, sampling, and success hypotheses must be checked. Merely saying 'distribution testing gives the result' does not discharge the reduction.

Likewise, standard concentration, KL tensorization, and Pinsker's inequality may be used with their relevant hypotheses. A paper-specific hidden-parent lemma or a named multilevel method is not a substitute for its required derivation.

Sharing inner oracle randomness between adjacent levels is optional; sharing the outer trajectory, or an alternative coupling with an equally valid variance proof, is what matters. Fresh evaluation noise must be independent of the trajectory-generation noise unless a different dependence analysis is supplied.

Do not accept an almost-sure chi-square bound in place of the expected bound. Do not assume that all noisy oracle laws can be simulated from exact conditional probabilities. The lower bound is worst-case over admissible oracle laws, so exact laws may be selected for its zero-noise component.

The public confidence interval is delta in (0,1). A median construction using a ceiling gives O(1+log(1/delta)) copies by itself, not a uniform O(log(1/delta)) bound as delta approaches one. A complete proof must address this endpoint without silently restricting delta or changing the target rate. An isolated omission of the elementary endpoint completion may be treated as a readily repairable omission, but does not earn full credit.

Treat an unproved main increment-variance bound, an unproved hidden-parent information bound, or an invalid rare-escape simulation as a theorem-critical gap unless another complete argument establishes the corresponding public claim. Do not penalize a valid proof for not reproducing the source's local indexing or threshold errors.
