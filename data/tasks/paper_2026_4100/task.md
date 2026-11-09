# Problem

## Setup

Let $m,p,q$ be positive integers and let $X$ be a discrete set. The target and proxy embeddings are
$f:X\to\mathbb R^m$ and $g:X\to\mathbb S^{p-1}$, where $\mathbb S^{p-1}=\{z\in\mathbb R^p:\|z\|_2=1\}$. Define
\[
d_g(x',x)=\|g(x')-g(x)\|_2,
\qquad N_\eta(x)=\{x'\in X:d_g(x',x)\le\eta\},
\]
for a budget $\eta>0$.

Fix $x\in X$. Let $U_x\subset\mathbb R^q$ be an open neighborhood of $0$, and let
\[
F:U_x\to\mathbb R^m,\qquad G:U_x\to\mathbb S^{p-1}
\]
be $C^2$ maps with $F(0)=f(x)$ and $G(0)=g(x)$. These maps describe a continuous local relaxation; the conclusions below concern coordinates $u$, not the existence of corresponding elements of the discrete set $X$. Derivatives of $G$ are taken in the ambient space $\mathbb R^p$.

Set
\[
J=DF(0),\qquad K=DG(0),\qquad A=J^TJ,\qquad B=K^TK,
\]
and assume $B$ is positive definite. For $t\ge0$, define
\[
Q_t=\{u\in\mathbb R^q:u^TBu\le t^2\}.
\]
Also define
\[
\Lambda=\lambda_{\max}(A,B):=\sup_{u\ne0}\frac{u^TAu}{u^TBu},
\qquad T=JB^{-1}J^T,
\qquad \sigma_w=w^TTw
\]
for each unit vector $w\in\mathbb R^m$.

For $b\in\mathbb R$, the affine score and margin at $x$ are
\[
s_{w,b}(x)=w^Tf(x)+b=:s_0,
\qquad \gamma_w(x)=|s_0|.
\]
Use the binary convention $\operatorname{sign}(z)=+1$ for $z\ge0$ and $\operatorname{sign}(z)=-1$ for $z<0$. The linearized and exact local scores are
\[
s_{\rm lin}(u)=s_0+w^TJu,
\qquad s_{\rm ex}(u)=w^TF(u)+b.
\]
A prediction flip means that the sign of the perturbed score differs from $\operatorname{sign}(s_0)$. When $s_0\ne0$, a strict sign reversal means that the product of the base and perturbed scores is negative.

For the nonlinear conclusions, choose a control radius $\rho\ge\eta$ such that $Q_\rho\subset U_x$. Let $\beta>0$ and finite constants $C_M,C_P\ge0$ satisfy
\[
B\succeq\beta I,\qquad
\|D^2F(v)\|_{\rm bil}\le C_M,\qquad
\|D^2G(v)\|_{\rm bil}\le C_P
\quad(v\in Q_\rho),
\]
where, for a vector-valued bilinear map $H$,
\[
\|H\|_{\rm bil}:=\sup_{\|a\|_2\le1,\ \|c\|_2\le1}\|H[a,c]\|_2.
\]
These constants concern the fixed chart and control region; they need not be uniform in $x$. The exact proxy-feasible set within this region is
\[
P_{\eta,\rho}:=\{u\in Q_\rho:\|G(u)-G(0)\|_2\le\eta\}.
\]

## Task

Prove the following integrated theorem.

1. The quadratic local attack problem satisfies
\[
\max_{u\in Q_\eta}u^TAu=\eta^2\Lambda.
\]
An attaining vector can be chosen to satisfy
\[
Au=\Lambda Bu,\qquad u^TBu=\eta^2.
\]
Include the case $A=0$. Moreover, $T$ is symmetric positive semidefinite, $\|T\|_{\rm op}=\Lambda$, and $\sigma_w\le\Lambda$ for every unit $w$.

2. For every unit readout direction $w$ and bias $b$ with $\gamma_w(x)>0$,
\[
\sup_{u\in Q_\eta}|w^TJu|=\eta\sqrt{\sigma_w}.
\]
Give an attaining vector when $\sigma_w>0$, including the choice that moves the score toward zero. Prove that a strict sign reversal in the linearized model is achievable if and only if
\[
\eta\sqrt{\sigma_w}>\gamma_w(x).
\]
Under the specified binary prediction convention, prove that a prediction flip is achievable if and only if
\[
\begin{cases}
\eta\sqrt{\sigma_w}>\gamma_w(x),&s_0>0,\\
\eta\sqrt{\sigma_w}\ge\gamma_w(x),&s_0<0.
\end{cases}
\]
Handle zero sensitivity and equality explicitly.

3. Continue with a unit $w$ and positive margin. For $0\le t\le\rho$, let
\[
r_{M,w}(t)=\sup_{u\in Q_t}|w^T(F(u)-F(0)-Ju)|.
\]
Prove
\[
r_{M,w}(t)\le\frac{C_Mt^2}{2\beta}.
\]
If
\[
\eta\sqrt{\sigma_w}>\gamma_w(x)+r_{M,w}(\eta),
\]
an exact local prediction flip occurs for some $u\in Q_\eta$; if
\[
\eta\sqrt{\sigma_w}<\gamma_w(x)-r_{M,w}(\eta),
\]
no exact local prediction flip occurs on $Q_\eta$.

Finally, quantify the second-order discrepancy between $\|G(u)-G(0)\|_2$ and $\sqrt{u^TBu}$ on the controlled region. State and justify how this discrepancy modifies feasibility and the sufficient flip and no-flip tests when the feasible set is $P_{\eta,\rho}$ rather than $Q_\eta$.
