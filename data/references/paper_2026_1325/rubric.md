# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Defines the actual perturbed margin \(m_q=\lambda_{\min}(\operatorname{sym}(I-W_q))\), proves \(m_q\ge m-\epsilon>0\), and derives \(|L-\epsilon|\le L_q\le L+\epsilon\) under \(\epsilon<m\).
- **3 points:** Correctly establishes, or invokes after verifying, that the stated full-domain locally Lipschitz monotone \(G\) is maximal monotone with an everywhere-defined firmly nonexpansive resolvent; then proves the quantized equilibrium/fixed-point equivalence, forward-backward contraction, uniqueness, and linear forward convergence under the stated stepsize.
- **3 points:** At a point where the displayed parameter derivatives exist, differentiates the equilibrium equation columnwise using a chain-rule-compatible Clarke generalized-Jacobian element, obtains \(r\) and the backward inclusion, and justifies monotonicity and resolvent applicability for the backward linear operator.
- **1 point:** Transfers the same \(m_q\), \(L_q\), stepsize condition, and contraction modulus to the compatible backward iteration.

# Evaluator Notes

Accept any correct alternative proof. Do not require the reference proof's incidental presentation choices. Do not award the sensitivity-inclusion step for treating an arbitrary Clarke generalized-Jacobian element as automatically compatible with the chain-rule derivative.
