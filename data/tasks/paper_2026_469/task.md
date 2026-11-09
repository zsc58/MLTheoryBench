# Problem

## Setup

Fix positive numerical constants \(c_-\) and \(c_+\). Let \(d\ge4\), let \(u,q\in\mathbb R^d\) be orthonormal, and let
\[
Q=I+\lambda qq^\top,\qquad c_-\log d\le\lambda\le c_+d.
\]
All asymptotic statements refer to \(d\to\infty\) and hold for sufficiently large \(d\). Constants in estimates may depend on the two fixed numerical bounds \(c_-,c_+\). Unless explicitly indicated, they do not depend on \(d\), the allowed \(\lambda\), or the learning rate. A statement uniform over later iterates means that its bound holds simultaneously for every indicated integer index.

Let \(\sigma^2\in[0,\infty)\). Samples follow \(x\sim N(0,Q)\) and \(y=(x^\top u)^2+\nu\), with independent \(\nu\sim N(0,\sigma^2)\). For \(W\in\mathbb R^{d\times d}\), write \(M=WW^\top\), \(f_W(x)=x^\top Mx\), and
\[
\mathcal L(W)=\mathbb E[(f_W(x)-(x^\top u)^2)^2]+\sigma^2.
\]
For nonzero positive semidefinite \(M\), define
\[
\operatorname{Align}(M)=\frac{u^\top Mu}{\|M\|_F}.
\]
Set \(\rho_0=1/\log d\) and \(\mu=\rho_0/d\). Initialize both algorithms with any square factors satisfying
\[
W_0W_0^\top=\widetilde W_0\widetilde W_0^\top=\mu I.
\]
Consider population updates
\[
\widetilde W_{k+1}=\widetilde W_k-\widetilde\eta\,\nabla_W\mathcal L(\widetilde W_k),
\qquad
W_{k+1}=W_k-\eta\,\operatorname{polar}(\nabla_W\mathcal L(W_k)).
\]
Here \(\operatorname{polar}(H)=H(H^\top H)^{\dagger/2}\), where \((H^\top H)^{\dagger/2}\) is the positive semidefinite square root of its Moore-Penrose inverse. Thus the polar factor is zero on a zero singular value.

Write \(M_k=W_kW_k^\top\), \(\widetilde M_k=\widetilde W_k\widetilde W_k^\top\), and
\[
P_u=uu^\top,\qquad P_q=qq^\top,\qquad P_\perp=I-P_u-P_q.
\]
Define
\[
s_k=u^\top M_ku,\quad h_k=q^\top M_kq,\quad z_k=\frac{\operatorname{Tr}(P_\perp M_k)}{d-2},
\]
and define \(\widetilde s_k,\widetilde h_k,\widetilde z_k\) in the same way using \(\widetilde M_k\). The scaled nuisance masses are \((1+\lambda)h_k\) and \((d-2)z_k\), and analogously for GD.

For a sufficiently small fixed constant \(\delta>0\), set
\[
T_1=\inf\{k\ge0:h_{k+1}\le h_k\},\qquad
T_2=\inf\{k\ge T_1:s_k\ge\delta\},
\]
\[
\widetilde T_1=\inf\{k\ge0:\widetilde h_{k+1}\le\widetilde h_k\},\qquad
\widetilde T_2=\inf\{k\ge\widetilde T_1:\widetilde s_k\ge\delta\},
\]
with \(\inf\varnothing=+\infty\).

## Task

Prove that there are universal constants \(\kappa_0>0\) and a sufficiently small fixed \(\delta>0\) for which the following conclusions hold.

First, both matrix trajectories have the decompositions
\[
M_k=s_kP_u+h_kP_q+z_kP_\perp,
\qquad
\widetilde M_k=\widetilde s_kP_u+\widetilde h_kP_q+\widetilde z_kP_\perp.
\]

For each fixed \(\kappa\in(0,\kappa_0]\), independent of \(d\), take \(\eta=\kappa/\sqrt{d+\lambda}\). Prove that polar-normalized descent satisfies:

- The first transition has \(T_1=O_\kappa(1)\), and
  \[
  \sqrt{s_k}=\sqrt{h_k}=\sqrt{z_k}=\sqrt\mu+k\eta,
  \qquad 0\le k\le T_1.
  \]
- For every \(k\ge0\),
  \[
  (1+\lambda)h_k\le C_b,\qquad (d-2)z_k\le C_c,
  \qquad C_b=(\kappa+1/\sqrt3)^2,\quad C_c=(1+\kappa)^2.
  \]
- The signal hitting time satisfies \(T_2=O(\eta^{-1})\). Uniformly for \(k\ge T_2\), the signal is of constant order and \(\operatorname{Align}(M_k)=1-o(1)\).
- There exists an integer \(K_*\ge T_2\), with \(K_*=O(\eta^{-1})\), such that for every \(k\ge K_*\),
  \[
  1-\operatorname{Align}(M_k)\le
  \frac{1}{2A^2}\left(\frac{C_b^2}{(1+\lambda)^2}+\frac{C_c^2}{d-2}\right)=o(1),
  \qquad
  A=\left(\sqrt{1-(C_b+C_c)/3}-\eta\right)^2.
  \]
  The choices of \(\kappa_0\) and sufficiently large \(d\) must ensure that this expression is defined and \(A>0\).

At the same initialization, consider ordinary gradient descent with
\[
0<\widetilde\eta\le\min\{1/24,1/[16(1+\lambda)]\}.
\]
Prove that its first phase satisfies
\[
\widetilde T_1=O((\widetilde\eta\lambda)^{-1}\log d).
\]
At its turning time the spike dominates the individual signal and bulk coefficients, in the sense that
\[
\frac{\widetilde h_{\widetilde T_1}}
{\max\{\widetilde s_{\widetilde T_1},\widetilde z_{\widetilde T_1}\}}\longrightarrow\infty,
\]
and there is a constant \(C>0\), depending only on the fixed anisotropy bounds, such that
\[
\operatorname{Align}(\widetilde M_{\widetilde T_1})
\le C\min\{\rho_0\lambda/d,\ d^{-1/2}\}.
\]
Finally, prove
\[
\widetilde T_2-\widetilde T_1=O(\widetilde\eta^{-1}\log d),
\]
and, uniformly for every \(k\ge\widetilde T_2\),
\[
\widetilde s_k=\Theta(1),\qquad
\widetilde h_k^2+(d-2)\widetilde z_k^2=o(1),\qquad
\operatorname{Align}(\widetilde M_k)=1-o(1).
\]
