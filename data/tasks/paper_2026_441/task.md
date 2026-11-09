# Problem

## Setup

Fix an integer $d\ge2$, a particle count $N\ge2$, a parameter $\theta\ge0$, matrices $Q,K\in\mathbb R^{d\times d}$, and $\rho>0$. For $x=(x^1,\ldots,x^N)\in(\mathbb R^d)^N$, define either of the following interaction vectors:

$$
\Phi^{\mathrm{nor}}_{\theta,i}(x)
=\frac{\sum_{j=1}^N e^{\theta\langle Qx^i,Kx^j\rangle}x^j}
{\sum_{j=1}^N e^{\theta\langle Qx^i,Kx^j\rangle}},
$$

or

$$
\Phi^{\mathrm{avg}}_{\theta,i}(x)
=\frac1N\sum_{j=1}^N e^{\theta\langle Qx^i,Kx^j\rangle}x^j.
$$

Choose one of these two rules and denote it by $\Phi_\theta$.

Let $(G_n)_{n\ge1}$ be independent and identically distributed random $d\times d$ matrices whose entries are independent, centered, have variance $\rho^2$, and are almost surely bounded by one common constant. They are independent of an initial vector $X_0=(X_0^1,\ldots,X_0^N)$ with arbitrary law supported on $(\mathbb S^{d-1})^N$. For every sufficiently large integer $L$, set

$$
X_{n+1}^i=
\frac{X_n^i+L^{-1/2}G_{n+1}\Phi_{\theta,i}(X_n)}
{\|X_n^i+L^{-1/2}G_{n+1}\Phi_{\theta,i}(X_n)\|}.
$$

(The boundedness assumptions make every denominator nonzero for all sufficiently large $L$, uniformly over $n$ and the sphere-valued configurations.) Define the continuous affine interpolation by

$$
X_L^i(t)=X_n^i+L(t-n/L)(X_{n+1}^i-X_n^i),
\qquad t\in[n/L,(n+1)/L].
$$

For $u\in\mathbb R^d$, write $P_u=I_d-uu^\top$. Let $W$ be a $d\times d$ matrix whose entries are independent standard Brownian motions, independent of $U_0$ and common to all particles, and consider the Itô SDE

$$
dU_t^i=
\frac{1-d}{2}\rho^2\|\Phi_{\theta,i}(U_t)\|^2U_t^i\,dt
+\rho P_{U_t^i}\bigl[dW_t\,\Phi_{\theta,i}(U_t)\bigr],
\qquad U_0\stackrel{d}=X_0.
$$

For $N=2$, define

$$
C_+=\{\|U_t^1-U_t^2\|\to0\text{ as }t\to\infty\},
\qquad
C_-=\{\|U_t^1+U_t^2\|\to0\text{ as }t\to\infty\}.
$$

## Task

Prove the following integrated theorem.

1. For either interaction rule, $X_L$ converges in distribution to $U$ in $C([0,\infty);(\mathbb R^d)^N)$. Moreover, $U_t\in(\mathbb S^{d-1})^N$ for every $t\ge0$ almost surely, and within the stated bounded-entry class the limiting law depends on the distribution of the entries of $G_n$ only through their variance $\rho^2$.

2. Specialize to $N=2$, assume $Q^\top K=I_d$, and take deterministic initial data with $r_0=\langle U_0^1,U_0^2\rangle\in(-1,1)$. Then

$$
\mathbb P(C_+)+\mathbb P(C_-)=1,
\qquad \mathbb P(C_+)>0,
$$

and

$$
\mathbb P(C_-)=0 \quad\text{if }d-2\ge\cosh(2\theta),
$$

whereas

$$
\mathbb P(C_-)>0 \quad\text{if }d-2<\cosh(2\theta).
$$

For completeness, if $r_0=1$ then $C_+$ occurs almost surely, while if $r_0=-1$ then $C_-$ occurs almost surely.
