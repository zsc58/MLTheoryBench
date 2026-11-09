# Problem

## Setup

Fix an integer \(n\geq1\). All random elements take values in standard Borel spaces and are defined on a common probability space. Let \(\mathcal W\) be the learner-state space and \(\mathcal Z\) the observation space. Let \(H_0\) be an initial learner history. Histories \(H_t\) are formed recursively by retaining the previous history and learner-side variables from the selected observations and updates, so \(\sigma(H_{t-1})\subseteq\sigma(H_t)\).

At round \(t\), conditional on \(H_{t-1}\), a latent paired row \(\widetilde Z_t=(Z_{t,0},Z_{t,1})\in\mathcal Z^2\) is sampled from a history-dependent probability kernel. Its conditional law is invariant under swapping the two coordinates. No independence across rounds or between the two coordinates is assumed. Define the conditioning sigma-field
\[
G_{t-1}=\sigma(H_{t-1},\widetilde Z_t).
\]
A selector \(U_t\in\{0,1\}\) satisfies
\[
\mathbb P(U_t=0\mid G_{t-1})=\mathbb P(U_t=1\mid G_{t-1})=\tfrac12
\quad\text{almost surely}.
\]
The learner is given only the selected observation \(Z_t=Z_{t,U_t}\), not the latent paired row or its unselected coordinate. Its update \(W_t\in\mathcal W\) satisfies
\[
\mathcal L(W_t\mid H_{t-1},\widetilde Z_t,U_t)
=K_t(\cdot\mid H_{t-1},Z_{t,U_t})
\quad\text{almost surely}
\]
for a probability kernel \(K_t\). Unselected coordinates are not supplied as inputs to the learner's history or updates; the fields \(G_{t-1}\) are used only for conditioning in the statement, not as learner observations.

Let \(Q_t\in[0,1]\) be \(\sigma(H_{t-1})\)-measurable, and let \(\ell:\mathcal W\times\mathcal Z\to[0,1]\) be measurable. Define
\[
L_t^+=Q_t\ell(W_t,Z_{t,0}),\qquad L_t^-=Q_t\ell(W_t,Z_{t,1}),
\]
\[
R_n^{\rm tr}=\frac1n\sum_{t=1}^n\mathbb E[Q_t\ell(W_t,Z_{t,U_t})],\qquad
R_n^{\rm ho}=\frac1n\sum_{t=1}^n\mathbb E[Q_t\ell(W_t,Z_{t,1-U_t})],
\]
and \(\operatorname{Err}_n^{\rm seq}=R_n^{\rm tr}-R_n^{\rm ho}\).

For a conditioning sigma-field \(G\), conditional mutual information means the scalar
\[
I(X;Y\mid G)=\mathbb E\!\left[D\!\left(P_{X,Y\mid G}\,\middle\Vert\,P_{X\mid G}\otimes P_{Y\mid G}\right)\right],
\]
where \(D\) is Kullback--Leibler divergence computed with natural logarithms.

For the excess-loss statement, fix a deterministic comparator \(w^\star\in\mathcal W\), and define
\[
e_{t,u}=Q_t\bigl(\ell(W_t,Z_{t,u})-\ell(w^\star,Z_{t,u})\bigr),\qquad u\in\{0,1\}.
\]
In that statement, use instead the excess risks
\[
R_n^{\rm tr}=\frac1n\sum_{t=1}^n\mathbb E[e_{t,U_t}],\qquad
R_n^{\rm ho}=\frac1n\sum_{t=1}^n\mathbb E[e_{t,1-U_t}].
\]
Assume \(|e_{t,u}|\leq b\) almost surely for every \(t,u\), for some finite \(b\geq0\), assume \(R_n^{\rm ho}\geq0\), and assume
\[
\frac1n\sum_{t=1}^n\mathbb E\!\left[\mathbb E[e_{t,0}^2\mid G_{t-1}]\right]\leq B R_n^{\rm ho}
\]
for some finite \(B>0\).

## Task

Prove the following integrated theorem.

1. For the ordinary losses, the sequential generalization gap obeys
\[
|\operatorname{Err}_n^{\rm seq}|
\leq\frac2n\sum_{t=1}^n\sqrt{2I(L_t^+;U_t\mid G_{t-1})}
\leq2\sqrt{\frac2n\sum_{t=1}^nI(W_t;U_t\mid G_{t-1})}.
\]
2. In the excess-loss setting, if \(b>0\), then for every \(0<\lambda<3/b\) such that \(1-B\lambda/(1-\lambda b/3)>0\),
\[
\left(1-\frac{B\lambda}{1-\lambda b/3}\right)R_n^{\rm ho}
\leq R_n^{\rm tr}+\frac{2}{\lambda n}\sum_{t=1}^nI(e_{t,0};U_t\mid G_{t-1}).
\]
If \(b=0\), show separately that both excess risks and all the displayed evaluated-excess information terms are zero.
