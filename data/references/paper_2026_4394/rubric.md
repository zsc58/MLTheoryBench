# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Coupon-collector estimate (2 points).** Defines the number of unseen support points and proves a constant-probability event with at least d unseen points for an integer support size r=Theta(n/log(n/d)). An expectation-and-variance proof must give a quantitatively sufficient lower bound on the expectation, including d=1; merely asserting E[U]>=2d and citing Chebyshev does not establish the claimed probability uniformly. Accept an equivalent valid argument and any valid universal constants.

2. **Adaptive corruption and majority contamination (4 points).** Constructs a valid monotone adversary selecting an unseen d-set and repeating its witness point, or provides a valid alternative mechanism. Verifies that the adversary uses only permitted information and appends exactly m honestly labeled examples. For the reference route, conditions on the clean sample before using the independent uniform permutation, uses the input-length-only restriction on voter lists, handles at least t distinct indices and repeated indices, and derives constant-probability contamination bounds without assuming independence between lists. The avoidance estimate must remain valid at t=1 and t=n.

3. **Fixed ERM lower bound (2 points).** Gives a finite class of VC dimension exactly d and a well-defined consistent ERM, explicitly used as the voter's base learner. Verifies that contaminated subsamples produce a common bad labeling, obtains a strict majority or otherwise handles ties correctly, and converts the resulting event into the asserted expected-error lower bound. The instance and ERM must be selected before t and the voter.

4. **Uniformly random consistent ERM extension (2 points).** Gives a finite class of VC dimension at most d+2 and proves this dimension bound. For the replicated-hypothesis route, establishes that the copies are distinct functions, identifies the consistent hypotheses on a contaminated subsample, proves the bad-selection probability, and derives a constant-probability strict majority of bad outputs. Completes the expected-error bound with the required quantifiers and universal constants. Accept a valid equivalent construction and argument.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental support-size constant, replication count, contamination threshold, or presentation order. For solutions following the reference route, the unseen-set estimate, adaptive witness construction, contamination counting, VC bounds, and randomized-ERM selection argument must be derived rather than merely named.

A uniform adversary working for every voter is acceptable but is not required: the public theorem allows the adversary to depend on the voter. The class, distribution, target, and fixed ERM where applicable must satisfy the stated earlier quantifier placement.

Do not assume that overlapping subsamples, contamination indicators, or ERM outputs are independent. Linearity of expectation and a bounded-variable estimate suffice for the randomized extension. Exactly half the votes being wrong is not enough under an arbitrary tie convention; an elementary strict-majority correction may be treated as readily repairable, but the uncorrected inference is not a completed proof step.

Propagate a missing unseen-set, contamination, consistency, or majority argument to downstream bounds when it leaves the claimed expectation unsupported. An unproved VC claim is also a theorem-critical omission. Do not require exact VC dimension d in the second statement, and do not credit an unsupported claim that its at-most-d+2 bound is uniformly equivalent to exact dimension d at every small d.
