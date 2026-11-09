# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly identifies \(q_r=\mathbb E[P_r\mid x]\) and computes the conditional Dirichlet mean
  \[
  \mathbb E[P_r\mid H=j,x]=\frac{a_r+s_j\mathbf 1\{r=j\}}{Z+s_j}.
  \]
- **3 points:** Correctly averages over the latent component and obtains
  \[
  q_r=a_r\sum_j\frac{w_j}{Z+s_j}+\frac{s_rw_r}{Z+s_r}.
  \]
  Merely invoking mixture marginalization without deriving this class-specific expression does not earn full credit.
- **4 points:** Performs the central reorganization: normalizes \(a\) by \(Z\), absorbs \(Z\) into the common scalar \(c\), and identifies the remaining class-dependent factor as \(d_r w_r\), thereby proving \(q_r=c u_r+d_r g_r\).
- **1 point:** Correctly concludes the vector identity for every class by using \(g=w\) and stacking the coordinate identities. An explicit verification that the resulting vector has total mass one is valid but not required.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's notation or order of presentation. A proof that treats \(d\) as a scalar coefficient, or incorrectly presents the formula as an ordinary two-component convex combination, has missed a theorem-critical class-dependent feature. Do not deduct twice for a single upstream error when assessing dependent steps, but award later credit when the needed intermediate identity is independently and correctly established.
