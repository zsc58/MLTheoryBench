# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Hölder/Rényi bound (3 points):** Use the likelihood ratio and the stated finite divergence to derive a per-step inequality \(\operatorname{TPR}_n\le C_\alpha\delta_n^{(\alpha-1)/\alpha}\), with a finite constant independent of \(n\). Establish the relevant integrability and conjugate-exponent calculation. The choice \(\alpha=\alpha_0\) is sufficient.
2. **Classifier impossibility (3 points):** Obtain \(p(\alpha-1)/\alpha>1\), apply the power-law schedule, and justify convergence of the resulting numerical series. Conclude that divergent classifier utility is impossible in the stated regime.
3. **Verifier soundness (2 points):** Use the reference-centered trajectory bound and strict open-ball inequality to prove that accepted parameters have trajectories outside \(U\). Invoke the oracle-certification implication and conclude that the unsafe-conditional acceptance probability is zero.
4. **Verifier utility (2 points):** Use the single constant \(q>0\), valid for every step, to lower-bound the verifier's conditional true-positive rates and establish divergent cumulative utility.

# Evaluator Notes

Accept any complete valid alternative proof. Do not award credit for merely naming Hölder/Rényi or a Lipschitz bound; the inequalities and resulting conclusions must be established.

- Do not require a divergence-monotonicity argument when the solution takes \(\alpha=\alpha_0\). If a smaller order is used, its integrability must be justified; the elementary estimate \(f^\alpha\le1+f^{\alpha_0}\) suffices for \(1<\alpha\le\alpha_0\).
- The classifier is restricted to the feature map. Absolute continuity is assumed for the feature laws \(P^+,P^-\), not for the parameter laws \(Q_n^+,Q_n^-\). Both gates use the same proposal experiment and safety labels, but their observable inputs differ. Do not impose parameter-law absolute continuity or require the verifier to be a function of the classifier features.
- The geometric hypothesis is the displayed bound relative to \(\theta_0\). A solution must not require an additional global all-pairs Lipschitz assumption. The unsafe set need not be closed.
- The false-acceptance claim concerns the unsafe-conditional law. Soundness makes the accepted set disjoint from the unsafe set of parameters, establishing zero probability directly.
- The public task supplies conditional coverage \(Q_n^+(B)\ge q\); no Gaussian coverage derivation is required. An unconditional ball probability is generally not equal to the conditional TPR. After soundness, \(Q_n^+(B)=\mu_n(B)/\mu_n(E_+)\).
- Separate positivity of every \(Q_n^+(B)\) is not a substitute for using the stated uniform lower bound.
- The argument must accommodate \(\delta_n=0\), and it may not replace the open ball by a closed ball without addressing its boundary.
- Do not require independence across steps or a sample-path conclusion. The targets concern sums of conditional rates only.
