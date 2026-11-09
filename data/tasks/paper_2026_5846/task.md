# Problem

## Setup

Let $G$ be a connected undirected comparison graph on vertices $\{1,\ldots,n\}$, with $n\ge2$. For each unordered edge $\{i,j\}$ let $m_{ij}=m_{ji}>0$ be its number of comparisons. Set $m_{ii}=0$ and $m_{ij}=0$ when $i\ne j$ and $\{i,j\}$ is not an edge. In the population Bradley-Terry model there is a positive strength vector $\pi^*$, normalized by $\prod_i\pi_i^*=1$, and the expected directed wins are
\[
\bar w_{ij}=m_{ij}\frac{\pi_i^*}{\pi_i^*+\pi_j^*}.
\]
For $\alpha\ge0$ and a positive vector $x\in(0,\infty)^n$, define
\[
(F_\alpha(x))_i=
\frac{\sum_{j=1}^n\bar w_{ij}\,\dfrac{\alpha x_i+x_j}{x_i+x_j}}
{\sum_{j=1}^n\dfrac{\alpha\bar w_{ij}+\bar w_{ji}}{x_i+x_j}}.
\]
Let $S(x)=x/(\prod_i x_i)^{1/n}$ and let the synchronous normalized iteration be $T_\alpha=S\circ F_\alpha$. Write $J_\alpha=DF_\alpha(\pi^*)$ and let its real eigenvalues be ordered
\[
\lambda_n(\alpha)\le\cdots\le\lambda_2(\alpha)<\lambda_1(\alpha)=1.
\]
Set
\[
\kappa=\frac{\max_i\pi_i^*}{\min_i\pi_i^*},\qquad
s_0=\frac{\lambda_2(0)+\lambda_n(0)}2,
\]
and define the local factor $\rho_{\rm sync}(\alpha)$ as the spectral radius of $DT_\alpha(\pi^*)$.

## Task

Prove that the eigenvalues can be labeled by real analytic branches $\psi_i:[0,\infty)\to\mathbb R$ (with multiplicities), with $\psi_1\equiv1$ and, for each $i=2,\ldots,n$,
\[
\frac{1-\psi_i(\alpha)}{\alpha+\kappa}\le \psi_i'(\alpha)\le
\frac{1-\psi_i(\alpha)}{\alpha+\kappa^{-1}},
\]
that $\psi_i(\alpha)\nearrow1$ as $\alpha\to\infty$, and
\[
\frac{\psi_i(0)+\kappa^{-1}\alpha}{1+\kappa^{-1}\alpha}
\le \psi_i(\alpha)\le
\frac{\psi_i(0)+\kappa\alpha}{1+\kappa\alpha}.
\]
Moreover,
\[
\rho_{\rm sync}(\alpha)=\max\{\lambda_2(\alpha),-\lambda_n(\alpha)\}
\]
is quasi-convex on $[0,\infty)$. If $s_0\ge0$, its unique minimizer is $\alpha_{\rm opt}=0$. If $s_0<0$, there is a unique minimizer $\alpha_{\rm opt}>0$ characterized by
\[
\lambda_2(\alpha_{\rm opt})=-\lambda_n(\alpha_{\rm opt}),
\]
and it obeys
\[
\kappa^{-1}|s_0|\le\alpha_{\rm opt}\le\kappa|s_0|.
\]
Finally, for every $\alpha\ge0$,
\[
\max\!\left\{\frac{\lambda_2(0)+\kappa^{-1}\alpha}{1+\kappa^{-1}\alpha},
\frac{-\lambda_n(0)-\kappa\alpha}{1+\kappa\alpha}\right\}
\le\rho_{\rm sync}(\alpha)\le
\max\!\left\{\frac{\lambda_2(0)+\kappa\alpha}{1+\kappa\alpha},
\frac{-\lambda_n(0)-\kappa^{-1}\alpha}{1+\kappa^{-1}\alpha}\right\}.
