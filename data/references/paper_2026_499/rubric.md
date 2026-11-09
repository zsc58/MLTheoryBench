# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points: Peripheral quotient characterization and minimality.** Correctly proves both directions of \(\rho(\overline P_L)<1\iff\mathcal K\subseteq L\), including why an omitted unit-modulus primary component survives in the quotient, and concludes that \(\mathcal K\) is the unique least, hence unique inclusion-minimal, stable quotient kernel.
- **3 points: Gauge-fixed reward decomposition.** Establishes solvability of the quotient equation, by contraction or any other valid argument, identifies \(\operatorname{ran}G\) with the quotient, and proves existence and uniqueness of \((g,v)\in\mathcal K\times\operatorname{ran}G\), including \(v=G(r+Pv)\).
- **3 points: Exact gain-bias comparison.** Uses the Cesaro projection correctly, establishes the normalized bias, proves invertibility of \(I-P\) on \(\mathcal K\cap\ker C\), constructs the unique \(\psi\), and derives \(h=v+\psi-Cv\), \(Gh=v\), and \(g=\rho+(I-P)(I-G)h\).

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the particular primary-decomposition coordinates, Lyapunov-series norm, or ordering used in the reference proof. Merely asserting that peripheral modes must be removed, or naming a contraction or Poisson-equation method without deriving the required implications and identities, does not earn the corresponding core-step credit. Score later achievements when they are independently established even if an earlier route contains an error.

The projection \(G\) is arbitrary subject to the public assumptions. Do not require it to be orthogonal, commute with \(P\), or arise from anchors. The private anchor-basis audit is dependency documentation, not an additional solver obligation and not an additional source of points.

Zero-dimensional quotient spaces and \(\mathcal K\cap\ker C=\{0\}\) are allowed. Use the usual spectral-radius convention of zero on the zero space. A proof valid in these cases need not isolate them in a separate paragraph. Do not deduct points for omitting the private supporting contraction construction when invertibility of the quotient equation is correctly established by another argument.
