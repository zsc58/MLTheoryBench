# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly transfers expectations of observed test functions to the source space and applies the explicitly assumed source forward equation on the lifted tests, respecting the source domain and time interval.
- **3 points:** Correctly conditions or disintegrates the lifted generator action to prove the observed weak forward equation. Establishes uniqueness by the stated uniqueness assumption, not by claiming that a conditional-expectation operator automatically generates a unique process.
- **2 points:** Correctly derives the marginal linear target as the conditional mean of the sampleable target. Justifies membership of the existing vector mean in the closed convex domain and obtains the parametrisation identity for every fixed t and f, q_t-almost everywhere. Does not incorrectly exchange this quantifier order with a simultaneous assertion over all f for arbitrary versions.
- **3 points:** Derives a valid conditional Bregman-divergence identity, establishes a finite parameter-independent integrated difference between the losses, and concludes gradient equality and equality of stationary-point sets wherever the gradients exist. Finiteness may be justified by nonnegativity and domination by the conditional loss, without imposing separate global integrability of the potential terms.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A bare appeal to conditional expectation or to a Bregman identity without establishing the needed conditional/marginal relation is insufficient. Do not require differentiation under an expectation: differentiating an exact parameter-independent-offset identity is sufficient and avoids that interchange.

The source-space forward equation is a primitive hypothesis. Do not require reconstruction of the external generator-regularity theorem. The time law is uniform; the generator and target identities are required only for t<1. Uniqueness of the entire probability-law path is assumed explicitly, including its terminal law, rather than deduced from a terminal generator equation. Do not require a projected Feller-process construction or a common exceptional set for an uncountable test-function space. Norm integrals are stipulated to exist in their stated spaces; completeness of every inner-product space is not an additional requirement.
