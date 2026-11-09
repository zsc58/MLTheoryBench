# Problem

## Setup

Let $\mathcal S$ be a finite nonempty state space, let $P$ be an irreducible aperiodic transition matrix with stationary distribution $\pi$, and let $0<\gamma<1$. Let $r:\mathcal S\times\mathcal S\to\mathbb R$ be a reward function. Let $d\geq1$ be an integer and let $X\in\mathbb R^{|\mathcal S|\times d}$ have full column rank, with row $s$ equal to $x_s^T$. Unsubscripted vector norms are Euclidean, and $\log$ denotes the natural logarithm. Write $D={\rm diag}(\pi)$ and define

$$
L_{\rm Dir}=D-\frac{DP+P^TD}{2},\qquad
||v||_D^2=v^TDv,\qquad ||v||_{\rm Dir}^2=v^TL_{\rm Dir}v.
$$

Let $(s_t)_{t\geq0}$ be a Markov chain with transition matrix $P$, started from any fixed state $s_0\in\mathcal S$. Observe $Z_t=(s_t,s_{t+1})$. Write

$$
\mathcal Z=\{(i,j)\in\mathcal S\times\mathcal S:P(i,j)>0\},
$$

and let $P_Z$ denote the transition matrix of $(Z_t)$ on $\mathcal Z$. Its stationary law is $\pi_Z(i,j)=\pi_iP(i,j)$. For probability measures on $\mathcal Z$, use the convention

$$
||\nu-\nu'||_{\rm TV}=\frac12\sum_{z\in\mathcal Z}|\nu(z)-\nu'(z)|.
$$

Assume that, for some fixed finite $m\geq1$,

$$
\sup_{z\in\mathcal Z}||P_Z^k(z,\cdot)-\pi_Z||_{\rm TV}\leq4\,2^{-k/m}\quad(k\geq0).
$$

For $z=(s,s')\in\mathcal Z$, set

$$
b_z=r(s,s')x_s,\qquad A_z=x_s(x_s-\gamma x_{s'})^T,
$$

and let $A={\mathbb E}_{\pi_Z}A_Z$ and $b={\mathbb E}_{\pi_Z}b_Z$. Let $w_*$ be the unique solution of $Aw_*=b$. Starting from any fixed $w_0\in\mathbb R^d$, run the unprojected recursion

$$
w_{t+1}=w_t+\alpha_t(b_{Z_t}-A_{Z_t}w_t),\qquad t\geq0.
$$

Define

$$
L=\max_{s\in\mathcal S}||x_s||,
\qquad B=\max_{s,s'\in\mathcal S}|r(s,s')|,
$$

$$
V(w)=(1-\gamma)||X(w-w_*)||_D^2+\gamma||X(w-w_*)||_{\rm Dir}^2,
$$

and

$$
\omega=(1-\gamma)\lambda_{\min}(X^TDX)>0.
$$

Let $(a_t)_{t\geq0}$ be a deterministic positive nonincreasing sequence, with $a_0\leq1$ and $Q=\sum_{t\geq0}a_t^2<\infty$. Fix $\delta\in(0,1)$ and define

$$
A_1=1536\sqrt Q\sqrt{2\log(8/\delta)}+2304,
\qquad A_2=2706Q,
$$

$$
c_{\min}=\frac{A_1+\sqrt{A_1^2+4A_2}}2.
$$

Choose any fixed $c>c_{\min}$ and set

$$
\alpha_t=\frac{a_t}{cmL^2},\qquad
H=\sum_{t\geq0}\alpha_t^2,\qquad
S_T=\sum_{t=1}^T\alpha_{t-1},
$$

$$
R_0=\max\left\{||w_0-w_*||,||w_*||,\frac{B}{L}\right\},
\qquad
\kappa=\frac{2c}{\sqrt{c^2-A_1c-A_2}}.
$$

Finally, define the weighted average $\bar w_T=S_T^{-1}\sum_{t=1}^T\alpha_{t-1}w_{t-1}$ and

$$
C_{\rm fast}=\kappa R_0\left[2+2mL^2\left(264\alpha_0+176\sqrt H\sqrt{2\log(8/\delta)}\right)+192mL^4H\right],
$$

$$
C_{\rm robust}=\kappa^2R_0^2\left[\frac12+2mL^2\left(288\alpha_0+192\sqrt H\sqrt{2\log(8/\delta)}\right)+(672m+4.5)L^4H\right].
$$

## Task

Prove that, with probability at least $1-\delta$, the following statements hold simultaneously:

1. $\sup_{t\geq0}||w_t||\leq\kappa R_0$.
2. For every integer $T\geq1$,

$$
V(\bar w_T)\leq
\min\left\{\frac{C_{\rm fast}^2}{\omega S_T^2},\ \frac{C_{\rm robust}}{S_T}\right\}.
$$
