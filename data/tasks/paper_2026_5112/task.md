# Problem

## Setup

Let $d_x,d_\theta$ be positive integers, let $K\ge2$ be an integer, and let $U\subseteq\mathbb R^{d_x}$ be open. Let $(X,Y)\sim\pi$, where $X\in U$ almost surely and $Y\in\{1,\ldots,K\}$. Fix $\epsilon>0$ and assume $x+\delta\in U$ whenever $x$ is in the support of the marginal distribution of $X$ and $\|\delta\|_2\le\epsilon$.

For $\theta\in\mathbb R^{d_\theta}$, let $z_\theta:U\to\mathbb R^K$ be measurable in $x$ and differentiable with respect to $\theta$, with measurable Jacobian. Define
\[
p_{\theta,j}(x)=\frac{e^{z_{\theta,j}(x)}}{\sum_{k=1}^K e^{z_{\theta,k}(x)}},\qquad
\hat y_\theta(x)=\arg\max_j z_{\theta,j}(x),\qquad
\hat p_\theta(x)=\max_j p_{\theta,j}(x),
\]
using a fixed ordering of the labels to resolve ties. For $x\in U$ and $y\in\{1,\ldots,K\}$, define
\[
m_\theta(x,y)=z_{\theta,y}(x)-\max_{j\ne y}z_{\theta,j}(x).
\]
For $x$ in the support of $X$, define
\[
m_{\epsilon,\theta}(x,y)=\inf_{\|\delta\|_2\le\epsilon}m_\theta(x+\delta,y).
\]
This infimum may equal $-\infty$. Assume that $m_{\epsilon,\theta}(X,Y)$ is measurable for each parameter under consideration.

Fix a positive integer $M$ and deterministic edges $0=b_0<b_1<\cdots<b_M=1$, and set $B_r=(b_{r-1},b_r]$ for $r=1,\ldots,M$. Writing $C=\hat p_\theta(X)$ and $A=\mathbf1\{\hat y_\theta(X)=Y\}$, define
\[
\operatorname{ECE}_M(\theta;\pi)=\sum_{r:\,\Pr(C\in B_r)>0}\Pr(C\in B_r)\,\big|\mathbb E[A\mid C\in B_r]-\mathbb E[C\mid C\in B_r]\big|.
\]
For an indexed dataset $D=\{(x_i,y_i)\}_{i=1}^n$ with $n\ge1$ and $(x_i,y_i)\in U\times\{1,\ldots,K\}$, write $\hat p_i=\hat p_\theta(x_i)$ and $\hat y_i=\hat y_\theta(x_i)$. Let
\[
n_r=|\{i\in\{1,\ldots,n\}:\hat p_i\in B_r\}|,
\]
and, for $n_r>0$, let
\[
a_r=\frac1{n_r}\sum_{i:\hat p_i\in B_r}\mathbf1\{\hat y_i=y_i\},\qquad
c_r=\frac1{n_r}\sum_{i:\hat p_i\in B_r}\hat p_i.
\]
Define
\[
\operatorname{ECE}_M(\theta;D)=\sum_{r:n_r>0}\frac{n_r}{n}|a_r-c_r|.
\]

Let $J_\theta(x)=\partial z_\theta(x)/\partial\theta\in\mathbb R^{K\times d_\theta}$, let $H_z(p)=\operatorname{diag}(p)-pp^\top$, and define
\[
H_{\mathrm{GN}}(\theta;\pi)=\mathbb E[J_\theta(X)^\top H_z(p_\theta(X))J_\theta(X)],\qquad
H_{\mathrm{GN}}(\theta;D)=\frac1n\sum_{i=1}^nJ_\theta(x_i)^\top H_z(p_\theta(x_i))J_\theta(x_i).
\]
The population matrix expectation is taken entrywise and is defined when every entry of $J_\theta(X)^\top H_z(p_\theta(X))J_\theta(X)$ has a finite absolute first moment. Write $\lambda_{\max}$ for the largest eigenvalue of a real symmetric matrix and $\|\cdot\|_{\mathrm{op}}$ for the operator norm induced by Euclidean norms. Define
\[
Q(\theta;\pi)=\mathbb E_\pi e^{-m_{\epsilon,\theta}(X,Y)},\qquad
Q_D(\theta)=\frac1n\sum_{i=1}^n e^{-m_\theta(x_i,y_i)}.
\]
The nonnegative expectations $Q(\theta;\pi)$ and $\mathbb E e^{-m_\theta(X,Y)}$ may equal $+\infty$. Use $e^{-(-\infty)}=+\infty$ and the convention $0\cdot(+\infty)=0$ for the nonnegative extended-real products in the bounds below.

## Task

Prove the following integrated theorem for every distribution and parameter satisfying the setup.

1. **Population regime.**
\[
\operatorname{ECE}_M(\theta;\pi)\le (K-1)\mathbb E e^{-m_\theta(X,Y)}\le (K-1)Q(\theta;\pi).
\]
If $\|J_\theta(X)\|_{\mathrm{op}}\le C_J$ almost surely for a constant $C_J\in[0,\infty)$, then the population Gauss–Newton matrix is defined and
\[
\lambda_{\max}(H_{\mathrm{GN}}(\theta;\pi))
\le2C_J^2(K-1)\mathbb E e^{-m_\theta(X,Y)}
\le2C_J^2(K-1)Q(\theta;\pi).
\]

2. **Interpolating finite-sample regime.** For $D=\{(x_i,y_i)\}_{i=1}^n$, let $\gamma=\min_{1\le i\le n}m_\theta(x_i,y_i)$ and assume $\gamma>0$. Then
\[
\frac1KQ_D(\theta)\le\operatorname{ECE}_M(\theta;D)\le(K-1)Q_D(\theta)\le(K-1)e^{-\gamma}.
\]
If additionally $\|J_\theta(x_i)\|_{\mathrm{op}}\le C_J$ for every $i$, for a constant $C_J\in[0,\infty)$, then
\[
\lambda_{\max}(H_{\mathrm{GN}}(\theta;D))\le2C_J^2(K-1)Q_D(\theta)
\le2C_J^2K(K-1)\operatorname{ECE}_M(\theta;D).
\]
When $C_J>0$, the resulting curvature–ECE inequality can equivalently be written as
\[
\operatorname{ECE}_M(\theta;D)\ge
\frac{\lambda_{\max}(H_{\mathrm{GN}}(\theta;D))}{2C_J^2K(K-1)}.
\]
