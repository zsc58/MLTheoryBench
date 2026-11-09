# Problem

## Setup

Let \(\mathcal Y\) be a finite nonempty output set with item vectors \(\gamma_y\in\mathbb R^d\), and let \(\lambda\in\mathbb R^d\). Define
\[
A(\lambda)=\log\sum_{y\in\mathcal Y}e^{\lambda^\top\gamma_y},\qquad P_\lambda(y)=e^{\lambda^\top\gamma_y-A(\lambda)}.
\]
Assume \(A\) is differentiable. Set \(\phi(\lambda)=\nabla A(\lambda)\), the dual coordinate. For strictly positive probability distributions \(Q,R\) on the same finite set \(S\), write
\[
D_{\rm KL}(Q\|R)=\sum_{s\in S}Q(s)\log\frac{Q(s)}{R(s)}.
\]

Fix a partition
\[
\mathcal Y=\left(\bigsqcup_{i=1}^{n_W}\{y_i^0,y_i^1\}\right)\sqcup N_W,
\]
where the two outputs in each pair are distinct, \(n_W\) is a nonnegative integer, and \(N_W\) is the set of neutral outputs. Define
\[
Z_W=\{z_i:1\leq i\leq n_W\}\sqcup\{z_y:y\in N_W\},
\]
using a distinct label for each pair and each neutral output.

For each \(\lambda\), let \(P_\lambda^W\) be the probability law of a binary concept \(W\) on \(\{0,1\}\), and use the notation \(P_\lambda(W=w)=P_\lambda^W(w)\). The output distribution \(P_\lambda\) is concept-factorizable with respect to this concept law and partition if there is a normalized probability distribution \(P_\lambda^Z\) on \(Z_W\) such that
\[
P_\lambda(y_i^w)=P_\lambda^W(w)P_\lambda^Z(z_i)\quad(1\leq i\leq n_W,\ w\in\{0,1\}),\qquad
P_\lambda(y)=P_\lambda^Z(z_y)\quad(y\in N_W).
\]

Assume a linear logistic probe: for fixed \(\beta_W\in\mathbb R^d\) and \(b_W\in\mathbb R\),
\[
P_\lambda(W=1)=\sigma(\beta_W^\top\lambda+b_W),\qquad \sigma(r)=\frac1{1+e^{-r}},
\]
for every \(\lambda\in\mathbb R^d\). For a target level \(c\in\mathbb R\) with nonempty affine constraint set
\[
\Lambda_W(c)=\{\lambda\in\mathbb R^d:\beta_W^\top\lambda=c\},
\]
fix an initial \(\lambda_0\in\mathbb R^d\) and assume that a minimizer \(\hat\lambda\in\Lambda_W(c)\) of \(D_{\rm KL}(P_{\lambda_0}\|P_\lambda)\) exists. Assume also that \(P_\lambda\) is concept-factorizable for every \(\lambda\in\Lambda_W(c)\cup\{\lambda_0\}\).

## Task

Prove the following integrated theorem: there exists \(t\in\mathbb R\) such that
\[
\phi(\hat\lambda)=\phi(\lambda_0)+t\beta_W.
\]
Moreover, every constrained minimizer (in particular \(\hat\lambda\)) minimizes the off-target divergence
\[
D_{\rm KL}(P_{\lambda_0}^Z\|P_\lambda^Z)
\]
over \(\lambda\in\Lambda_W(c)\). On the constraint set the target probability is \(P_\lambda(W=1)=\sigma(c+b_W)\), so whenever this differs from its value at \(\lambda_0\), the KL projection changes the target concept while achieving the stated off-target minimum.
