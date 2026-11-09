# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Profiles each weighted local regression, including intercept removal, centered variables, normal equations or an equivalent quadratic argument, and the inverse-Gram slope formula. Justifies minimization using nonnegative weights and the assumed invertibility.
- **3 points:** Derives the equivalence between minimizing the empirical criterion and maximizing F, with the B-independent residual term and summation over anchors.
- **2 points:** Proves invariance under \(B\mapsto BR\) for every \(R\in O(d)\) and establishes that F is a smooth Grassmannian objective. Smoothness follows from the smooth inverse on an open invertibility domain and smooth quotient descent; an explicit quotient chart is acceptable but not required.
- **3 points:** Correctly differentiates an inverse-Gram summand, obtains \(2(\mu-GBu)u^T\), verifies tangency/horizontality or an equivalent defining differential identity, identifies the Riemannian gradient under the specified Stiefel and quotient metrics, and sums over anchors.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's presentation, its auxiliary matrices, an explicit quotient chart, or a particular differentiation method. A proof identifying the claimed horizontal matrix through its inner products with tangent directions is fully acceptable.

Treat unexplained assertions of the local-regression or gradient formulas, omission of the invariance argument, or failure to justify that the claimed matrix represents the Riemannian gradient as substantive gaps. Distinguish such gaps from a routine omitted explanation of smoothness of matrix inversion or smooth quotient descent.

The weights are fixed during optimization and differentiation. No iid sampling argument, population smoothness condition, neighborhood construction, regularization result, or stochastic convergence theorem is required. Do not require all individual weights to be positive or add a sample-size hypothesis beyond feasibility of the stated invertibility assumption. The case \(d=p\) and zero response moments are included; no separate case split is needed if the argument already applies to them.

The source transpose correction recorded for theory_008 is private audit information, not an additional solver obligation. All core proof obligations are closed in the reference proof; there is no private GT quality warning.
