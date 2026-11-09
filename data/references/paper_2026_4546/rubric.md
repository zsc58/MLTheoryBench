# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly establishes well-definedness and the regularity needed for the argument. In the reference route, constructs the Minkowski gauge, justifies alpha=H composed with gamma, proves the needed continuity/Lipschitz properties of alpha and q, and establishes local Lipschitzness of p. Gauge-zero directions must not be excluded by an unstated boundedness assumption.
- **2 points:** Proves continuity, strict monotonicity, and the exact range of every ray scalar map psi_v, including finite and infinite boundary-distance cases.
- **3 points:** Establishes that every output lies in Int(C), uses ray preservation and scalar ranges to prove injectivity and surjectivity, handles zero, and correctly obtains continuity of the inverse. Invariance of Domain is an acceptable route, not a required one.
- **3 points:** Proves almost-everywhere differentiability and invertibility at every differentiability point. In the reference route, 1 point covers Rademacher, the justified product rule, and the interior calculation including the anchor; 2 points cover pointwise exterior invertibility and complete treatment of the boundary. An exterior calculation performed only where the gauge is differentiable must be supplemented by an argument that every exterior differentiability point of p has the required gauge differentiability, or by another valid pointwise argument.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular complementary subspace, or use of a gauge when another method closes the same obligations. Allocate the corresponding core-step credit to mathematically equivalent arguments.

The raywise bijection and the everywhere-it-exists Jacobian assertion are theorem-critical. Merely invoking a homeomorphism does not establish invertibility of its derivative. Almost-everywhere differentiability of the gauge does not by itself establish invertibility at every differentiability point of p.

For the reference route, differentiability of p implies differentiability of q because the scalar multiplier r(||x||^2) is positive and C1. In the strict exterior, gamma(x)=||x||^2/(x^T q(x)) then supplies the needed pointwise gauge differentiability. At the boundary, the two radial one-sided derivatives of q differ, so p is not differentiable there. A valid conditional argument establishing invertibility at any hypothetical boundary differentiability point is also sufficient; proving boundary nondifferentiability is not itself a public target.

The representation q(x)=x/gamma(x) may be differentiated directly in the strict exterior, where it holds on a neighborhood. Its validity at a boundary point alone does not justify differentiating it there. Do not award full credit to a proof that silently applies this exterior derivative formula across the boundary.

If boundary distance continuity is used, it is continuity into (0,infinity] with the extended-value convention, not finite-valued continuity. No smooth boundary, boundedness, symmetry, or strictly positive gauge in every nonzero direction may be assumed.

Merely naming a projection or an unrelated method earns no credit for the theorem-critical arguments.
