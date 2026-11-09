# Problem

## Setup

Time is indexed by the nonnegative integers. Let $(\mathcal F_t)_{t\ge0}$ be a filtration, let $\mathcal V$ be a fixed finite set with $|\mathcal V|\ge2$, and let $W_t$ be the observed $\mathcal V$-valued token at time $t\ge1$. At each time $t\ge1$, the auxiliary random vector is
\[
\zeta_t=(U_{t,j})_{j\in\mathcal V}\in[0,1]^{\mathcal V}.
\]
Define
\[
Y_t:=U_{t,W_t},\qquad Z_t:=-\log(1-Y_t),\qquad \mathcal G_t:=\sigma(Z_1,\ldots,Z_t),
\]
using the convention $-\log 0=+\infty$. Let $\mathcal G_0$ be trivial, and assume the reduced history is contained in the full history: $\mathcal G_t\subseteq\mathcal F_t$ for every $t$.

Under every distribution in the null family $\mathcal P_0$, for every $t\ge1$, conditional on $\mathcal F_{t-1}$, the coordinates $U_{t,j}$ are iid Uniform$(0,1)$ and $W_t$ is conditionally independent of $\zeta_t$ given $\mathcal F_{t-1}$. An e-process for $\mathcal P_0$, as used here, is a nonnegative $(\mathcal G_t)$-adapted process $M_t$ with $M_0=1$ and $\mathbb E_P[M_t\mid\mathcal G_{t-1}]\le M_{t-1}$ for every $t\ge1$ and every $P\in\mathcal P_0$.

## Task

Fix $\lambda\in(0,1)$. Prove that
\[
M_t(\lambda):=(1-\lambda)^t\exp\!\left(\lambda\sum_{s=1}^t Z_s\right),\qquad t\ge0,
\]
with the empty sum equal to zero, is an e-process for $\mathcal P_0$. Deduce that for every $\alpha\in(0,1)$ the stopping rule
\[
\tau_\alpha:=\inf\{t\ge1:M_t(\lambda)\ge1/\alpha\},\qquad \inf\varnothing:=\infty,
\]
has $\sup_{P\in\mathcal P_0}P(\tau_\alpha<\infty)\le\alpha$, so validity is preserved under arbitrary optional stopping.
