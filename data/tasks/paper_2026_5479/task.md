# Problem

## Setup

Let the latent dimension $d$, observation dimension $m$, and horizon $h$ be positive integers, and fix a forecast origin $t$. All supplied matrices below are held fixed as the real scalar $s$ varies.

Let $J_0,\ldots,J_{h-1}\in\mathbb R^{d\times d}$ be local Jacobians and let $B\in\mathbb R^{m\times d}$ be the observation matrix. Let $\Sigma_t\in\mathbb R^{d\times d}$ and the process-noise covariance $G\in\mathbb R^{d\times d}$ be positive semidefinite, and let the observation-noise covariance $\Lambda\in\mathbb R^{m\times m}$ be positive definite. Scale each local Jacobian by $e^s$ and define
\[
P_0(s)=\Sigma_t,\qquad P_{i+1}(s)=e^{2s}J_iP_i(s)J_i^T+G,
\qquad i=0,\ldots,h-1.
\]
Define the $h$-step open-loop observation covariance
\[
\Omega_{\rm open}(s)=BP_h(s)B^T+\Lambda.
\]
For comparison, define the recursion without Jacobian transport by
\[
\widetilde P_0(s)=\Sigma_t,\qquad
\widetilde P_{i+1}(s)=\widetilde P_i(s)+G,
\qquad i=0,\ldots,h-1,
\]
and set $\widetilde\Omega_{\rm open}(s)=B\widetilde P_h(s)B^T+\Lambda$.

For a separate one-step filtered update, let $\Sigma_{t-1|t-1}\in\mathbb R^{d\times d}$ be positive semidefinite and let $J_{\rm f}\in\mathbb R^{d\times d}$. Using the same $B,G,\Lambda$, set
\[
P^-(s)=e^{2s}J_{\rm f}\Sigma_{t-1|t-1}J_{\rm f}^T+G,\quad
\Omega_t(s)=BP^-(s)B^T+\Lambda,\quad
K(s)=P^-(s)B^T\Omega_t(s)^{-1},
\]
with posterior covariance $P^+(s)=(I_d-K(s)B)P^-(s)$, where $I_d$ is the $d\times d$ identity matrix. The covariance-volume part of a Gaussian negative log likelihood is $\frac12\log\det\Omega$.

## Task

Prove the following integrated theorem. There exist $s$-independent matrices $A_0,\ldots,A_h\in\mathbb R^{m\times m}$, each positive semidefinite and determined by the covariance recursion, such that, for every $s\in\mathbb R$,
\[
\Omega_{\rm open}(s)=\Lambda+\sum_{\ell=0}^{h}e^{2\ell s}A_\ell.
\]
Consequently,
\[
\frac{d}{ds}\frac12\log\det\Omega_{\rm open}(s)
=\sum_{\ell=1}^{h}\ell e^{2\ell s}\operatorname{tr}\!\left(\Omega_{\rm open}(s)^{-1}A_\ell\right)\ge0,
\]
with strict inequality for every $s$ whenever at least one $A_\ell$ for $\ell\ge1$ is nonzero, and with derivative identically zero when $A_1=\cdots=A_h=0$. For the comparison without Jacobian transport, prove
\[
\frac{d}{ds}\frac12\log\det\widetilde\Omega_{\rm open}(s)=0.
\]
Moreover, the one-step filtered covariance-volume score satisfies
\[
\frac{d}{ds}\frac12\log\det\Omega_t(s)
=e^{2s}\operatorname{tr}\!\left(\Omega_t(s)^{-1}BJ_{\rm f}\Sigma_{t-1|t-1}J_{\rm f}^TB^T\right)\ge0,
\]
and the assimilation update localizes covariance in the Loewner order:
\[
P^+(s)\preceq P^-(s).
\]
Thus open-loop covariance-volume scoring imposes a nonnegative penalty on Jacobian expansion, while filtered innovation scoring retains local transport and repeatedly contracts covariance, in the non-strict Loewner sense, at assimilation steps.
