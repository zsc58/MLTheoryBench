# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Expected blurred-TV sandwich (2 points).** Correctly use the variational/Jensen argument to establish \(\mathbb EF\ge D\). Derive, rather than merely assume, the split-sample comparison and conclude \(D\ge\mathbb EF-\mathbb EA-\mathbb EB\). One valid derivation conditions on each independent block to show that its expected distance from the population is at most the expected between-block discrepancy, then uses the full empirical measure's mixture weights \(n_1/n,n_2/n\). The argument must accommodate odd sample sizes. The source's independent-copy/conditional-exchangeability argument and other valid alternatives are equally acceptable.
2. **Upper confidence bound (3 points).** Derive the coordinate sensitivities \(1/n\) and \(1/m\) of the full empirical blurred TV, apply bounded-differences concentration in the lower tail with \(\varepsilon_{n,m,\alpha}\), and combine it with \(D\le\mathbb EF\) to prove \(\Pr(D\le\widehat U_\alpha)\ge1-\alpha\).
3. **Lower confidence bound and central correction (4 points).** Analyze \(G=F-A-B\), establish the replacement sensitivities \(1/n+1/n_r\) and their \(Y\)-sample analogues, justify a squared-sensitivity sum at most \(9/(n-1)+9/(m-1)\), and apply the upper-tail bounded-differences bound with margin \(3\varepsilon_{n-1,m-1,\alpha}\). Combine this with \(\mathbb EG\le D\) and \(D\ge0\) to justify clipping and conclude \(\widehat L_\alpha\le D\) on the required event. Merely naming McDiarmid or sample splitting without establishing the needed bounds earns little credit.
4. **Boundary and distribution-free conclusion (1 point).** Handle \(\min(n,m)=1\) with the prescribed zero lower bound, without evaluating undefined split terms or zero-index margins. State that both separate one-sided coverages hold for all permitted distributions, dimensions, kernels, fixed positive bandwidths, sample sizes, and \(\alpha\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a separate measurability discussion when standard measurable-statistic facts are used correctly. Standard bounded-differences concentration may be cited without reproving it, provided the relevant tail, independence, and sensitivities are correctly applied.

Award credit for equivalent definitions of the split blocks and algebraically identical concentration margins. Equal-weight averaging of unequal blocks is not the full empirical measure and must be justified or corrected. An unsupported central split-sample comparison or unjustified concentration margin is a substantive proof gap. Merely omitting the immediate zero-boundary check is a readily repairable omitted case, consistent with the 8-9 category, rather than grounds by itself for treating an otherwise complete proof as substantially incomplete.

The two requested confidence statements are separate. Do not require simultaneous coverage of both bounds at level \(1-\alpha\), uniformity over data-dependent bandwidth choices, asymptotic convergence, or any smoothness, moment, support, or Gaussian-kernel assumption.
