# Problem

## Setup

Fix an integer $d\ge1$, parameters $\rho=(\rho_1,\ldots,\rho_d)$ with $\rho_i>1$, and $M>0$. For $r>1$, define
\[
E_r=\left\{\frac{z+z^{-1}}2:z\in\mathbb C,\ 1\le |z|<r\right\},
\qquad E_\rho=\prod_{i=1}^d E_{\rho_i}.
\]
Let $A(\rho,M)$ consist of the functions $f:[-1,1]^d\to\mathbb R$ for which there is a holomorphic function $F:E_\rho\to\mathbb C$ satisfying
\[
F|_{[-1,1]^d}=f,
\qquad \sup_{z\in E_\rho}|F(z)|\le M.
\]

A feedforward ReLU network is a composition of real affine maps and coordinatewise activations $\sigma(t)=\max\{t,0\}$ in its hidden layers, followed by a real affine output map. Its width is the maximum number of coordinates in a hidden layer, and its depth is the number of hidden layers. There is no restriction on the magnitudes or precision of its real weights and biases.

Fix $\kappa\in[0,d]$ and $\beta>0$. Fix $\alpha>0$, with $\alpha=0$ also allowed if $\kappa=0$. Consider sufficiently large positive integers $L,N$ satisfying
\[
L^{\kappa+\alpha}\le N\le \exp(L^\beta).
\]

## Task

Prove that there are positive constants
\[
C_w=C_w(d,\rho),\qquad
C_D=C_D(d,\rho,\beta),\qquad
C_E=C_E(d,\rho,M),\qquad
c=c(d,\rho,\kappa,\alpha)
\]
such that, for every sufficiently large pair $L,N$ satisfying the displayed constraints and every $f\in A(\rho,M)$, there is a ReLU network $f_{N,L}:\mathbb R^d\to\mathbb R$ with
\[
\operatorname{width}(f_{N,L})\le C_wN,
\]
\[
\operatorname{depth}(f_{N,L})\le
\begin{cases}
C_DL(\log L)^2,&\kappa=d,\\
C_DL,&0\le\kappa<d,
\end{cases}
\]
and
\[
\sup_{x\in[-1,1]^d}|f(x)-f_{N,L}(x)|
\le C_E\,N^{-cL^{\tau(\kappa)}},
\]
where
\[
\tau(\kappa)=
\begin{cases}
(\kappa+1)/(d+2),&0\le\kappa\le1/(d+1),\\
\kappa,&1/(d+1)<\kappa<1/d,\\
(\kappa+1)/(d+1),&1/d\le\kappa\le d.
\end{cases}
\]
The thresholds implicit in “sufficiently large” may depend on the fixed parameters, but not on $f$. All logarithms are natural.
