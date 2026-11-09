# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes the pointwise domination \(\ell_0(h)\le\mathbf 1\{W d_h\le0\}\le\Phi(Wd_h-\gamma)/\Phi(-\gamma)\), correctly using non-increase of \(\Phi\), nonnegativity away from the error event, the margin shift, and positivity of the denominator. An equivalent direct proof of the first-to-last inequality earns the same credit.
- **3 points:** Correctly compares conditional target and surrogate risks using their common conditional label law and derives the conditional-regret decomposition, including the best-in-class conditional surrogate term. Equivalent correct expansion and cancellation of the population gap terms earns the same credit; conditioning is not a mandatory proof route.
- **2 points:** Identifies or correctly incorporates the residual term as \(A_\gamma(\mathcal H)\), without assuming it is zero or dropping it.
- **2 points:** Correctly converts expected conditional regrets into risk regrets plus minimizability gaps, or performs the equivalent direct algebra, and obtains the stated inequality throughout its specified domain. Arithmetic must respect the prohibition on \(\infty-\infty\); the allowed case of infinite evaluated surrogate risk must be covered explicitly or by valid extended-real reasoning.

# Evaluator Notes

Accept any complete valid alternative proof. In particular, expanding the gap definitions reduces the requested inequality to the population-risk domination \(R_{\ell_0}(h)\le R_{\ell_{\Phi_\gamma}}(h)/\Phi(-\gamma)\), provided the cancellations are justified. Such a proof can earn full credit without presenting a conditional-regret argument.

The ranking convention assigns prediction \(+1\) at a zero score difference. Thus \(\ell_0=\mathbf 1\{W d_h\le0\}\) is not a valid identity. A mistaken equality is a readily repairable local error if replacing it by the correct inequality leaves the proof valid; proving a different target loss without connecting its risks and gaps to the stated ones is not a complete solution.

The existing admissibility restriction implies finite best-in-class surrogate risk and finite expected conditional optimal surrogate risk, but it does not require every scorer to have finite surrogate risk. Do not require a separate infinite-risk paragraph when the argument already handles that case correctly. Do not accept undefined cancellation of infinities.

No attainment of an infimum, convexity, regularity, equicontinuity, hard-margin constraint, realizability, finite support, or scaling closure is required. Nonnegativity of \(A_\gamma\) is a valid optional observation, not an additional target that every solution must prove.

A proof that omits the approximation term without a valid cancellation, uses an invalid loss-direction inequality, or lacks a valid risk-gap conversion has a theorem-critical gap.
