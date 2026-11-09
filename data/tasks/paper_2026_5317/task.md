# Problem

## Setup

Let $d\ge1$, let $F:\mathbb R^d\to\mathbb R$ be smooth, and let $z_*$ be a global minimizer of $F$. Define the graph embedding

$$\iota(x)=(x,F(x))\in\mathbb R^{d+1}$$

and equip its graph $\mathcal N$ with the metric induced by the ambient Euclidean inner product. In the coordinate $x$, its metric matrix is

$$A(x)=I_d+\nabla F(x)\nabla F(x)^T,$$

so the metric gradient of $F$ is $A(x)^{-1}\nabla F(x)$.

Fix $t_0\in\mathbb R$ and constants $c>0$ and $\lambda>0$. Let $x:[t_0,\infty)\to\mathbb R^d$ be a global twice continuously differentiable solution of

$$
\ddot x(t)
=-\left(\dot x(t)^T\nabla^2F(x(t))\dot x(t)+c\right)
 A(x(t))^{-1}\nabla F(x(t))
-\lambda\sqrt{K(t)}\,\dot x(t),
$$

where

$$K(t)=\frac12\dot x(t)^TA(x(t))\dot x(t),$$

$$U(t)=c\bigl(F(x(t))-F(z_*)\bigr),
\qquad E(t)=K(t)+U(t).$$

Assume $E(t_0)<\infty$ and that, for some stationary point $z_\infty$ of $F$,

$$\bigl(x(t),\dot x(t)\bigr)\longrightarrow(z_\infty,0)
\quad\text{as }t\to\infty.$$

For $\varepsilon>0$, use the convention $\inf\varnothing=\infty$ and define

$$\tau_\varepsilon=\inf\{t\ge t_0:K(t)\le\varepsilon\}.$$

Let the total Riemannian arc length of the graph trajectory be

$$\ell=\int_{t_0}^{\infty}
\sqrt{\dot x(t)^TA(x(t))\dot x(t)}\,dt
\in[0,\infty].$$

## Task

Prove the following integrated quantitative guarantee. For every $\varepsilon>0$,

$$\tau_\varepsilon
\le t_0+\frac{E(t_0)}{2\lambda\varepsilon^{3/2}},$$

and the full trajectory satisfies

$$K(t_0)+c\bigl(F(x(t_0))-F(z_\infty)\bigr)
\le\sqrt2\lambda E(t_0)\ell.$$

In particular, when $E(t_0)>0$, the second inequality is equivalently

$$\ell\ge
\frac{K(t_0)+c\bigl(F(x(t_0))-F(z_\infty)\bigr)}
{\sqrt2\lambda E(t_0)}.$$
