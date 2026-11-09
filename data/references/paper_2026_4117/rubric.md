# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes parameter containment, applies optimism, and reduces cumulative pseudo-regret to directional supports. Bounds supports by ellipsoidal widths and supplies a valid deterministic support bound from the parameter domain when needed for the final truncation argument.
- **3 points:** Constructs a valid enclosing ellipsoid for a half-space cut after affine normalization, obtains the volume-ratio upper bound and the decrease $\Omega_{d,\xi}\ge(1-\xi)^2/[2(d+1)]$, verifies containment of the regularized updated set, and telescopes the potential with the correct initial and final volume comparisons. Exact optimality of the explicitly constructed cut ellipsoid is not required.
- **3 points:** Uses predictable boundary thresholds and fresh noise to lower-bound the probability of a deep cut on large-width rounds; proves a sufficient martingale concentration estimate and obtains the stated truncated cumulative-width bound with probability at least $1-\delta$.
- **2 points:** Splits small-width and large-width rounds, validly removes truncation from the support sum, substitutes the geometric lower bound, and obtains exactly the requested finite-time regret expression. Handles zero selected contexts and the case $L=0$ without undefined normalized offsets.

# Evaluator Notes

Accept any complete valid alternative proof; the listed route is not mandatory. In this route, missing justification for the geometric decrease, the conditional noise argument, or the probabilistic conversion is theorem-critical unless replaced by another valid argument.

The correct center of the truncated-ball enclosing ellipsoid is $(d q-1)/(d+1)$, not $(q-1)/(d+1)$. Enclosure and a volume comparison suffice; do not demand a contact-point optimality proof.

Do not accept the inference that containment of a convex body in a ball bounds every directional width of its MVEE by the ball's diameter. MVEE volume monotonicity does not establish ellipsoid containment. A sufficient final argument is $h_t\le\min\{W_t,M\}$, with $M=2L(2S\sqrt d+\mu)$, followed by $\min\{W,M\}\le(1+M/w_\xi)\min\{W,w_\xi\}$. A different valid truncation-removal argument is equally acceptable.

The target is the regret bound, not the stronger cumulative untruncated-width claim stated in the source. Do not require proof of that unnecessary claim or treat it as an available lemma. The replacement reference proof closes the target without it.

The high-probability event is for each fixed choice of $\delta,\mu,\xi$; simultaneous uniformity over these parameters is not required. No assumption that $S>0$ or $\eta_{\max}>0$ may be added.
