# Problem

## Setup

Condition on a sigma-field fixing measurable real-valued scores \(A\) and \(S\) and a threshold \(t_*\in\mathbb R\cup\{+\infty\}\). Let \(P\) be the clean law and \(Q\) a contaminating law on the same measurable space. Calibration observations are conditionally i.i.d. with law
\[
P^*=(1-\varepsilon)P+\varepsilon Q,
\qquad 0\leq\varepsilon<1,
\]
and the clean test point is conditionally independent with law \(P\). Put \(K=\mathbf1\{S\leq t_*\}\),
\[
p_c=P(K=1)>0,\qquad p_d=Q(K=1),\qquad
\mu=(1-\varepsilon)p_c+\varepsilon p_d>0,
\]
and \(R=P^*(\cdot\mid K=1)\). Write \(P_k=P(\cdot\mid K=1)\) and, when \(p_d>0\), \(Q_k=Q(\cdot\mid K=1)\). A dirty component with zero mixture weight contributes zero. Define
\[
\widetilde\varepsilon=\frac{\varepsilon p_d}{\mu}.
\]
For score CDFs \(F_M(a)=M(A\leq a)\), with all suprema below over \(a\in\mathbb R\), let
\[
d_{M\to N,+}=\sup_a(F_M(a)-F_N(a))_+,\quad
\Delta_+=\sup_a(F_{P_k}(a)-F_P(a))_+,\quad
\Delta=\sup_a|F_{P_k}(a)-F_P(a)|,
\]
\[
D_+=\sup_a(F_{Q_k}(a)-F_P(a))_+,
\qquad
\rho=\sup_a\left|\operatorname{Cov}_P(\mathbf1\{A\leq a\},K)\right|.
\]
When \(Q_k\) is undefined and its mixture coefficient is zero, interpret its weighted discrepancy term as zero. Let \([x]_+=\max\{x,0\}\) and \(\alpha\in(0,1)\).

## Task

Prove the integrated trimming diagnostic: every real threshold \(q\) satisfying \(F_R(q)\geq1-\alpha\) obeys
\[
P(A\leq q)\geq\left[1-\alpha-(1-\widetilde\varepsilon)\Delta_+-\widetilde\varepsilon D_+\right]_+.
\]
Show within the same theorem that, for \(\lambda\in[0,\infty)\), if \(p_d\leq\lambda p_c\), then
\[
\widetilde\varepsilon\leq\frac{\varepsilon\lambda}{1-\varepsilon+\varepsilon\lambda}.
\]
Thus, holding \(\varepsilon<1\) fixed, \(p_d/p_c\to0\) implies \(\widetilde\varepsilon\to0\), whereas \(p_d=p_c\) implies \(\widetilde\varepsilon=\varepsilon\). In the no-separation case \(p_c=p_d=r>0\), prove the covariance-refined diagnostic
\[
P(A\leq q)\geq\left[1-\alpha-(1-\varepsilon)\frac{\rho}{r}-\varepsilon D_+\right]_+
\]
for every such \(q\), and establish that \(\Delta=\rho/r\). Conclude that equal retention probabilities yield no reduction in the retained contamination coefficient; any improvement must arise from the retained dirty score law and/or clean-side covariance distortion.
