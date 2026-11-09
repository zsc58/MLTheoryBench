# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly defines the paired disagreement probabilities and proves `gamma-beta=P_b-P_c=p_flip(2q_downarrow-1)`, including the domain condition `p_flip>0` and the resulting degradation/equality equivalence.
- **4 points:** Establishes the characteristic conditional argument: for iid paired observations, conditioning on the total disagreement count gives `b | n_flips ~ Binomial(n_flips,q_downarrow)`. Justifies why conditioning leaves the disagreement directions distributed as independent Bernoulli trials, for example by conditioning first on the disagreement indices and then mixing over sets of the same size, or by an equivalent joint-count calculation. Conditional laws need only be asserted on count events of positive probability. Merely naming McNemar's test without deriving this law earns no credit for this step.
- **2 points:** Reduces the equal-accuracy null to `q_downarrow=1/2` when `p_flip>0`, constructs the one-sided upper binomial tail, and proves why the conditional rejection probability is at most `alpha`. A valid justification identifies the rejection set as an upper tail with null probability at most `alpha`, or gives an equivalent discrete p-value argument; equality with `alpha` is not required.
- **2 points:** Correctly handles `n_flips=0` by reporting no disagreements and failing to reject, and lifts the conditional bound to unconditional type-I control. Covers the null population case `p_flip=0`, in which there are no sample disagreements almost surely and rejection probability is zero. The final decision rule must be stated coherently.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A response that assumes the conditional binomial law or exact level without justification has a theorem-critical gap. Observing `n_flips=0` implies `b=c=0`, not `P_b=P_c=0`; do not credit that invalid population inference as justification for the zero-disagreement decision. Assigning p-value one in the zero-disagreement case is an acceptable equivalent implementation of the required fail-to-reject decision.
