# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Finite-sample bulk calibration.** Conditions correctly on the fitting data or independently fitted score, uses the uniform empirical-CDF deviation bound with radius $r_m$, verifies that the threshold is finite and attained when $\gamma\ge r_m$ and $\gamma<1$, and concludes $\Pr\{P(B)\ge1-\gamma\}\ge1-\delta$. The argument must include the feasible boundary $\gamma=r_m$ and may identify the appropriate empirical order statistic. The measurable fitted-procedure assumptions ensure that the selected threshold and event are measurable; a separate lengthy measurability proof is not required.
- **2 points: Restricted-law representation.** Derives from $d_-(P_B,C_B)=e_c$ the eventwise domination $P_B\ge(1-e_c)C_B$ and hence the contamination representation of $P_B$, including the $e_c=0$ case. The residual is a nonnegative countably additive measure with the claimed total mass. Merely asserting this representation without justification does not earn full credit.
- **3 points: Conditioned contamination composition.** Establishes $D(B)>0$, conditions $D=(1-\alpha)P+\alpha R$ on $B$, identifies the in-bulk contaminating weight $\eta=\alpha R(B)/D(B)=\alpha\rho$, handles $R(B)=0$, and composes the representations to obtain exactly $e_{\mathrm{eff}}=e_c+\alpha\rho-\alpha e_c\rho$. Correctly treats zero-weight components and the case $e_{\mathrm{eff}}=0$. This is the central step. A direct residual-measure or domination proof is equally acceptable.
- **3 points: Tail control and simultaneous certificate.** Establishes $D(B^c)\le(1-\alpha)\gamma+\alpha(1-R(B))$, obtains the bulk expectation bound, performs the bulk-tail risk decomposition, applies Holder's inequality with exponent $1/q$, justifies dropping the bulk-mass factor using nonnegativity, and concludes that the bound holds simultaneously for every decision on the single calibration event. Uses the stated convention when $e_{\mathrm{eff}}=0$ and the pointwise supremum is infinite. An infinite supremum with positive coefficient makes the certificate immediate; it is not a counterexample.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A later step may receive credit if its needed conclusion is established independently. An unproved or incorrect conditioned-mixture composition is a major gap because it leaves the effective tolerance unsupported.

The centre may depend on both fitting and held-out data. No independence of the centre is needed: only the calibration step conditions on the fitting data, and the risk argument is deterministic on $E$. Do not require a union bound, countability of the loss family, or a measurable supremum over the decision index; the statement asks for an inequality for every decision on the explicitly measurable event $E$.

Do not infer that a measurable loss is bounded on a bounded set. Do not impose continuity, a finite pointwise bulk supremum, an additional centre-moment assumption, or restrictions on the contaminant beyond those in the task. In fact $1-e_{\mathrm{eff}}>0$ and the derived domination imply finite centre p-moments from the deployment moment assumption. This may be shown explicitly or handled through a valid nonnegative-integral argument; it is not a separate mandatory scoring step.

Omission of a zero-mass residual law is correct. It is unnecessary to define $R_B$ when $R(B)=0$ or to divide by $e_c$ or $e_{\mathrm{eff}}$ when either is zero. Apply the public zero-weight convention rather than treating $0\cdot(+\infty)$ as a defect in the repaired task.
