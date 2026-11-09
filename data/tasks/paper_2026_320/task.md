# Problem

## Setup

Let $G=(V,E)$ be a finite directed acyclic graph with a unique terminal vertex $\Delta$ (it has incoming edges, no outgoing edges, and every vertex reaches it). Let $S\subset V$ be the set of vertices with no incoming edges, and let $\operatorname{in}(v)$ denote the predecessors of $v$. For each nonsource $v$, let
$f_v:\mathbb R^{\operatorname{in}(v)}\to\mathbb R$ satisfy
\[
|f_v(x)-f_v(y)|\le L_v\|x-y\|_1
\]
for some finite $L_v\ge0$. For a directed path $\gamma$, let $|\gamma|$ be its number of edges and set
\[
L_\gamma=\prod_{(u,v)\in\gamma}L_v.
\]

Let $\mathcal P_1(\mathbb R)$ denote the probability laws with finite first absolute moment. For $\mu,\nu\in\mathcal P_1(\mathbb R)$, define
\[
W_1(\mu,\nu)=\inf\mathbb E|X-Y|,
\]
where the infimum is over all couplings with laws $\mu$ and $\nu$.

For $\nu\in\mathcal P_1(\mathbb R)$ and an integer $n\ge0$, define its depth-$n$ recursive mean quantizer as follows. Begin with the cell $\mathbb R$. At each of $n$ splitting rounds, split each positive-mass current cell $I$ at its conditional mean $m_I$ into
\[
I\cap(-\infty,m_I),\qquad I\cap[m_I,\infty),
\]
discarding zero-mass pieces. At the end assign each positive-mass cell its conditional mean and its original $\nu$-mass. The resulting atomic law is $T(\nu,n)$; in particular $T(\nu,0)$ is the point mass at the mean. Let $Q_{\nu,n}(z)$ denote the conditional mean of the final cell containing $z$, defined $\nu$-almost everywhere.

Each source $s$ has a law $\mu_s\in\mathcal P_1(\mathbb R)$. Choose independent $X_s\sim\mu_s$ and evaluate
\[
X_v=f_v((X_u)_{u\in\operatorname{in}(v)})
\]
in a topological order. Write $\mu_v=\operatorname{Law}(X_v)$.

Fix $n\ge0$ and write $\mu_s^{(n)}=T(\mu_s,n)$. Choose independent source variables $U_s\sim\mu_s^{(n)}$ and evaluate
\[
U_v=f_v((U_u)_{u\in\operatorname{in}(v)}).
\]
The input-quantized law is $\mu_v^{(n)}=\operatorname{Law}(U_v)$.

Define the compressed evaluation recursively from these quantized sources. Set $C_s=U_s$. For each nonsource $v$, form
\[
Z_v=f_v((C_u)_{u\in\operatorname{in}(v)}),\qquad
\nu_v=\operatorname{Law}(Z_v).
\]
If $\nu_v$ has more than $2^n$ atoms, set $C_v=Q_{\nu_v,n}(Z_v)$; otherwise set $C_v=Z_v$. This rule applies also at $\Delta$. The same variable $C_v$ is used by every successor: intermediate variables are not independently resampled from their marginal laws. Write $\mu_v^{(n),c}=\operatorname{Law}(C_v)$.

Let $\operatorname{supp}$ denote support, $\operatorname{diam}$ its diameter, and $\mathcal P(s,\Delta)$ the set of directed paths from $s$ to $\Delta$.

## Task

Prove that for every integer $n\ge0$,
\[
W_1(\mu_\Delta,\mu_\Delta^{(n),c})
\le
\sum_{s\in S}\sum_{\gamma\in\mathcal P(s,\Delta)}
\left[
W_1(\mu_s,\mu_s^{(n)})
+3|\gamma|2^{-n}\operatorname{diam}(\operatorname{supp}\mu_s^{(n)})
\right]L_\gamma.
\]
