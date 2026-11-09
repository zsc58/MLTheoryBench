# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points: Exact group identity.** Correctly computes the two possible standardized coefficients, partitions the score sum by reward, and simplifies the coefficient to \(S\), obtaining \(U=S(\overline S_+-\overline S_-)\), or supplies an equivalent valid derivation. Handles the stipulated unanimous case and correctly explains baseline invariance through centering. Merely asserting the identity without deriving it does not earn full credit. The baseline operation is a common reward shift before recomputing the mean and standard deviation; an additive shift of already-standardized advantages is not the same operation.
- **2 points: Exact expected update.** In the Bernoulli-logit specialization, establishes that the successful-minus-unsuccessful mean score is one, obtains \(U(k)=\sqrt{k(G-k)}/G\), and averages against the \(\operatorname{Binomial}(G,p)\) law with the correct limits and normalization. The expectation is unconditional, with unanimous groups contributing zero; conditioning on a mixed group without accounting for its probability does not establish the requested formula.
- **3 points: Interior asymptotic.** Applies a justified expansion to \(f(K/G)=\sqrt{(K/G)(1-K/G)}\), uses the binomial variance and the correct value \(f''(p)=-1/[4(p(1-p))^{3/2}]\), and controls the remainder sufficiently to derive the stated \(O(G^{-2})\) expansion for fixed \(p\in(0,1)\). One valid route retains the signed cubic Taylor term, uses the third and fourth centered moments, and controls the complement of a fixed interior neighborhood. The reference proof's fourth-moment tail bound is sufficient, but a justified concentration bound or another valid remainder argument is equally acceptable. Constants may depend on the fixed \(p\); endpoint-uniform control is not required.
- **1 point: Arcsine-gradient identification.** Uses \(dp/d\theta=p(1-p)\) and differentiates \(2\arcsin\sqrt p\) to show that its derivative with respect to \(\theta\) is \(\sqrt{p(1-p)}\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The exact group identity is the characteristic bottleneck and must be derived, not merely named. If that identity is not proved but the scalar update formula is independently established, award later points according to the conclusions actually justified.

Treat an unjustified claim that a second-order Taylor formula automatically has an \(O(G^{-2})\) expected remainder as a material gap unless higher moments or an equivalent remainder argument are supplied. In particular, the signed third centered moment can be \(O(G^{-2})\) even though the third absolute centered moment need not have that order. A localization argument must account for the function and any Taylor-polynomial terms on the complementary event; controlling only the endpoint masses does not by itself justify an expansion on an entire interior neighborhood. Standard moment or concentration results may be used when their applicable statements and hypotheses are clear; solvers need not reproduce the reference proof's elementary derivations verbatim.
