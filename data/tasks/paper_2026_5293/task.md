# Problem

## Setup

Let \(d,m\) be positive integers, let \(s_1,\ldots,s_m\in\mathbb R^d\), and let \(J\) be uniform on \(\{1,\ldots,m\}\). Set \(B=s_J\). Let \(Y_0\sim N(0,I_d)\) be independent of \(J\). Fix \(\epsilon\in(0,1]\). For \(t\in(0,1]\), define
\[
\tau_t=1-(1-\epsilon)t,\qquad h_t=\frac{\tau_t}{t},\qquad Y_t=tB+\tau_tY_0.
\]
Let \(p_t\) denote the continuous density of \(Y_t\), and define its conditional velocity field using the continuous version of the conditional mean:
\[
v_t(x)=\mathbb E\left[B-(1-\epsilon)Y_0\mid Y_t=x\right].
\]

For \(h>0\), write
\[
\phi_h(z)=(2\pi h^2)^{-d/2}\exp\left(-\frac{\|z\|^2}{2h^2}\right).
\]
For \(y\in\mathbb R^d\), define
\[
\omega_i(t,y)=\frac{\phi_{h_t}(y-s_i)}{\sum_{j=1}^m\phi_{h_t}(y-s_j)},
\qquad
M_t(y)=\sum_{i=1}^m\omega_i(t,y)s_i.
\]

Consider a single cross-attention head with query \(y\), keys and values \(s_1,\ldots,s_m\), and logits
\[
\ell_i(t,y)=-\frac{\|y-s_i\|^2}{2h_t^2}.
\]
Its output is
\[
H_t(y)=\sum_{i=1}^m
\frac{\exp\left(-\|y-s_i\|^2/(2h_t^2)\right)}
{\sum_{j=1}^m\exp\left(-\|y-s_j\|^2/(2h_t^2)\right)}s_i.
\]
Define the affine output map
\[
A_t(y,z)=y+\frac{z-y}{\tau_t}.
\]

## Task

Prove that, for every \(t\in(0,1]\) and \(y\in\mathbb R^d\),
\[
t^d p_t(ty)=\frac1m\sum_{i=1}^m\phi_{h_t}(y-s_i),
\]
and that the corresponding velocity field satisfies
\[
v_t(ty)=y+\frac{M_t(y)-y}{\tau_t}.
\]
Moreover, prove that the attention output satisfies \(H_t(y)=M_t(y)\), and consequently
\[
A_t\bigl(y,H_t(y)\bigr)=v_t(ty).
\]
