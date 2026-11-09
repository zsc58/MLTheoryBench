# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Deterministic obstruction (2 points):** Correctly show that when \(\sigma=0\), all iterates lie in \(x_0+\alpha\mathbb Z\), and conclude non-hitting when this grid misses the target interval.
2. **Return from infinity for positive noise (3 points):** Establish a genuine negative drift (or an equivalent valid argument) for \(|X_n|\) outside a compact set and deduce almost-sure finite returns to that compact set. A drift proof must justify integrability and the stopped return argument, rather than merely naming a recurrence criterion.
3. **Probabilistic escape mechanism (2 points):** Prove a uniform positive conditional probability of hitting the interval from the compact set and use repeated strong-Markov trials to conclude almost-sure finite hitting time. Either one-step attempts or a valid bounded-window construction are acceptable. The iteration must use a justified conditional failure bound; mutual independence of attempt outcomes is not required.
4. **Extreme-noise finite-horizon limits (3 points):** Under the stated deterministic margin, prove both limits: small noise by a finite-horizon coupling/maximal inequality, and large noise by a uniform Gaussian density bound and union bound. The coupling must justify sign agreement. The large-noise proof must account for time zero using the margin assumption.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A drift argument must justify recurrence to a compact region, and merely naming a probabilistic method without establishing its hypotheses is insufficient.

For fixed positive noise, the drift radius and the attempt probability may depend on that noise magnitude and the other fixed parameters. No uniform positive lower bound across all noise magnitudes is required.

The transition mean contains the discontinuous sign function. With sign(0)=0, the symmetric-interval hitting probability need not be continuous in the starting state at zero. Do not accept continuity in the state plus compactness as a justified uniform lower-bound argument without addressing this point. A bounded-mean Gaussian density bound or compactness in the Gaussian mean variable closes the obligation.

Strong Markov makes fresh innovations independent of the past at an attempt start, but it does not make all attempt outcomes mutually independent: later starting states can depend on earlier outcomes. Accept a tower-property recursion giving a geometric upper bound on repeated failure, or another valid argument. Do not require or endorse a product identity for random conditional failure probabilities.

If a bounded-noise window is used, its increment bound must cover both signs, its approach-to-zero claim must stop before crossing, and the final hitting innovation must not be improperly conditioned to satisfy the earlier bounded-noise event.

Kolmogorov's maximal inequality applies because the innovations are independent, centered, and have variance one. A valid elementary finite-horizon substitute is also acceptable. Both limits are for each fixed finite horizon with the initialization, step size, target radius, and margin fixed; neither asserts a uniform-in-horizon limit or an expectation limit.
