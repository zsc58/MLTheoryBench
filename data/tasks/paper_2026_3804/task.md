# Problem

## Setup

Let $d\ge1$ be an integer and let $\beta>0$. Let $F:\mathbb R^d\to\mathbb R$ be differentiable, and assume that $b=-\nabla F$ is differentiable. For $f\in C_c^\infty(\mathbb R^d)$, define
\[
Lf(x)=\langle b(x),\nabla f(x)\rangle+\beta^{-1}\Delta f(x).
\]
Define
\[
Z=\int_{\mathbb R^d}e^{-\beta F(x)}\,dx,\qquad
\pi(dx)=Z^{-1}e^{-\beta F(x)}\,dx,
\]
and assume $0<Z<\infty$.

Assume that for some $r>0$ and constants $L_b,m>0$ and $b_0\ge0$, and for all $x,y\in\mathbb R^d$,
\[
\|b(x)-b(y)\|\le L_b(1+\|x\|^r+\|y\|^r)\|x-y\|,
\qquad
\langle x,b(x)\rangle\le b_0-m\|x\|^{r+2}.
\]
Assume there is a deterministic continuous function $A:\mathbb R^d\to[0,\infty)$ and constants $L_A,C_A>0$ such that, for every $x\in\mathbb R^d$,
\[
\|\nabla b(x)\|_{op}\le A(x)\le L_A(1+\|x\|^r),
\qquad
\frac{\|b(x)\|}{1+A(x)}\le C_A(1+\|x\|).
\]

Fix $\alpha\in(0,1/2)$. For $0<\eta\le1$, define
\[
b_\eta(x)=\frac{b(x)}{1+\eta^\alpha A(x)}.
\]
Let $Q_\eta$ be the Markov kernel specified, for bounded Borel measurable $\varphi$, by
\[
Q_\eta\varphi(x)=\mathbb E\!\left[\varphi\!\left(x+\eta b_\eta(x)+\sqrt{2\beta^{-1}\eta}\,\xi\right)\right],
\qquad \xi\sim N(0,I_d).
\]
Equivalently, its Markov chain is
\[
Y_{k+1}=Y_k+\eta b_\eta(Y_k)+\sqrt{2\beta^{-1}\eta}\,\xi_{k+1},
\]
where the $\xi_k$ are iid $N(0,I_d)$ and independent of $Y_0$. Put $V_q(x)=1+\|x\|^q$ for real $q\ge2$.

For $\eta_0\in(0,1]$ and an integer $Q_*\ge2$, call a family $\{\mu_\eta\}_{0<\eta\le\eta_0}$ $Q_*$-admissible if each $\mu_\eta$ is an invariant probability measure for $Q_\eta$ and
\[
\sup_{0<\eta\le\eta_0}\int V_{Q_*}(x)\,\mu_\eta(dx)<\infty.
\]

Finally, assume that every probability measure $\mu$ satisfying
\[
\int Lf\,d\mu=0\qquad\text{for every }f\in C_c^\infty(\mathbb R^d)
\]
equals $\pi$.

## Task

Prove that for every real $q\ge2$ there exist constants $c_q,C_q,M_q>0$ and $\eta_q\in(0,1]$, depending only on $q$ and the fixed data in the setup, such that
\[
Q_\eta V_q(x)\le(1-c_q\eta)V_q(x)+C_q\eta
\qquad\text{for all }x\in\mathbb R^d,\quad 0<\eta\le\eta_q.
\]
Prove also that, for every such $\eta$, $Q_\eta$ has an invariant probability measure and every invariant probability measure $\nu$ of $Q_\eta$ satisfies
\[
\int V_q(x)\,\nu(dx)\le M_q.
\]
The constants and the bound must be independent of $\eta$ and of the choice of invariant measure; the permitted upper step size may depend on $q$.

Finally, prove that there exists an integer $Q_{\min}\ge2$, depending only on the fixed data in the setup, such that for every integer $Q_*\ge Q_{\min}$, every $\eta_0\in(0,1]$, and every $Q_*$-admissible family $\{\mu_\eta\}_{0<\eta\le\eta_0}$,
\[
\mu_\eta\Rightarrow\pi\qquad\text{as }\eta\downarrow0.
\]
