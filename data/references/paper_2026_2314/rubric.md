# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Apply the assumed derivative representation along an arbitrary tangent direction and linearity of the signed-measure integral to derive $D F(w)[v]=\sum_i v_i\mathbb E_{Q_i}[\phi_w(Y)]$. A mixture-perturbation calculation is a valid way to present this step, but need not be repeated separately when the displayed setup assumption is applied directly.
- **2 points:** Establish that the arm-wise expectations form a valid centered simplex gradient under the public definition, including the zero weighted mean $\sum_iw_i g_i(w)=0$.
- **3 points:** Use the stated action/reward sampling law to compute the expectation of $Z_k=(\mathbf 1\{A=k\}-w_k)\phi_w(Y)$ and establish the required unbiasedness calculation. Conditioning on the arm, direct integration against the joint law, or an equivalent valid calculation is acceptable. Obtaining $\mathbb E[Z]=\operatorname{diag}(w)g(w)$ is sufficient for this step, but that particular intermediate expression is not mandatory.
- **2 points:** Use the softmax differential and the chain rule, or equivalent coordinate differentiation, to identify the resulting expectation with $\nabla_h(F\circ\sigma)(h)=J(h)g(w)$.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. In particular, a separate proof of uniqueness modulo the all-ones vector is not required: the public target specifies derivative representation and weighted centering as the requested centered-gradient properties. Such a uniqueness argument is valid supplementary material, not an additional scoring obligation.

Treat omission of a valid centering justification or a valid unbiasedness calculation as a theorem-critical gap. Merely naming influence functions or softmax differentiation without justifying the relevant identities earns no credit for those steps. Equivalent calculations may combine core steps; award credit for the mathematics established rather than for matching the reference proof's order or intermediate expressions.
