# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Defines empirical Walsh correlations and the signed sparse test class; proves its logarithmic cardinality is O(sn); and obtains the upper concentration requirement C(1+sigma^2)s(sn+log(1/delta))/epsilon^2. For the reference route, this includes design variance at most s, empirical second-moment control using fourth moments at most s^3, and conditional weighted-noise concentration. The public tail-based subgaussian convention permits universal numerical losses in concentration constants.
- **2 points:** Proves the hard-thresholding coefficient bound and converts it to uniform prediction error. Handles a true support of size less than s, ties, and zero empirical entries by using an exactly s-element selected index set, or an equivalent valid argument. Obtains the upper sample bound uniformly over the allowed noises.
- **3 points:** Constructs and verifies the bounded structured sparse family, proves tuple-Hamming-to-uniform separation, and carries out coordinatewise adaptive KL/Fano and the projection/risk conversion yielding the sigma^2 n s^2/epsilon^2 lower term. Specifies admissible block sizes, handles s=1 and bounded dimensions, and covers randomized adaptive learners. A valid alternative lower-bound construction is equally acceptable.
- **2 points:** Proves the sigma^2 s log(1/delta)/epsilon^2 confidence obstruction for log(1/delta)>=s. For the Gaussian-prior route, specifies the singleton-coordinate support and prior scale mu=C_0 epsilon/sqrt(s log(1/delta)); distinguishes posterior covariance of G from that of mu G; proves the inverse-trace estimate and existence of a cube point with large posterior variance; verifies the Gaussian tail and prior boundedness estimates; and transfers risk from the unconditioned to the bounded prior with enough slack to exceed delta.
- **1 point:** Combines both lower bounds and the upper bound, handles log(1/delta)<s by absorption, and verifies strict exclusion of successful learners, integer budgets, the full parameter range, and constant dependence in the final noise-bounded-below characterization.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental choices, including its cutoff n=12, sixteen constant alternatives, particular concentration constants, or exact prior-boundedness argument.

Do not accept the former reference's displayed signed-sparse concentration bound: its sparsity and confidence factors do not prove the claimed upper rate. An upper proof must justify the sharp s log(1/delta) term rather than silently replace it by s^2 log(1/delta).

The structured parameter is a tuple of subsets of a second coordinate block, not an undefined sign matrix. Repeated hidden subsets are allowed; distinct first-block coordinates make the full Walsh characters distinct. A claim that pairwise coefficient distance always equals uniform distance on arbitrary Walsh supports is false.

A coordinatewise Fano bound does not automatically give a probability lower bound for many Hamming errors. Require that conversion, or an equivalent argument. For a two-element alphabet, decreasing a sample-size constant cannot produce error at least 3/4; bounded-dimensional cases need a valid treatment.

Gaussian conjugacy applies to the unconditioned Gaussian prior and the sequential adaptive likelihood. It does not hold unchanged after conditioning the prior onto the coefficient ball. A trace lower bound of s/2 concerns the standardized vector G; the scaled coefficient covariance carries the factor mu^2. The output may be an arbitrary function, so lower bounds must not assume the estimator belongs to the chosen linear subclass.

Treat an asserted concentration, thresholding, KL/Fano, or Gaussian-posterior conclusion without verification as a substantial gap; propagate a missing lower-bound component to the final characterization. A worst-case risk bound merely equal to delta does not by itself exclude a learner required to have risk at most delta; accept explicit slack or another valid resolution. There are no unresolved obligations in the audited reference proof.
