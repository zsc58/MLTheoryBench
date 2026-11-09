# Problem

## Setup

Let \(p\to\infty\) index a sequence of instances with positive integers \(n_p,d_p,k_p\), where \(d_p=p\) and \(n_p\to\infty\), and realized rank-\(k_p\) matrices \(X_p\in\mathbb R^{n_p\times d_p}\). Write a thin singular value decomposition
\[
X_p=U_pD_pV_p^T,
\]
where \(U_p\in\mathbb R^{n_p\times k_p}\) and \(V_p\in\mathbb R^{d_p\times k_p}\) have orthonormal columns and \(D_p\in\mathbb R^{k_p\times k_p}\) is diagonal with positive entries in nonincreasing order. Fix a choice of singular basis if singular values are repeated. Let \(P_{X,p}=U_pU_p^T\). For coefficient vectors \(\beta_{0,p},b_{0,p}\in\mathbb R^{d_p}\), define
\[
f_{0,p}=X_p\beta_{0,p},\qquad g_{0,p}=X_pb_{0,p}.
\]
Let \(Y_p,\varepsilon_p\in\mathbb R^{n_p}\) be random vectors satisfying
\[
Y_p=f_{0,p}+g_{0,p}+\varepsilon_p,
\qquad E[\varepsilon_p\mid X_p]=0.
\]
All expectations are taken under the conditional distribution given the realized design \(X_p\), under which \(\varepsilon_p\) is integrable. The coefficient vectors, chosen singular basis, spectral weights, and iteration counts are fixed under this conditioning; they are not selected using \(Y_p\) or \(\varepsilon_p\). All bounds and limits below are along the sequence of realized designs.

Fix a positive integer \(q\) independent of \(p\), with \(q<k_p\) for all sufficiently large \(p\). All definitions involving \(q\) below are made on this eventual tail. Define \(P_{H,p}=\sum_{i=1}^q u_{p,i}u_{p,i}^T\), where \(u_{p,i}\) is the \(i\)-th column of \(U_p\). Let
\[
W_p=U_p\operatorname{diag}(w_{p,1},\ldots,w_{p,k_p})U_p^T,
\qquad 0\le w_{p,i}\le1,
\]
and define the weighted squared loss \(L_{W_p}(f)=\tfrac12\|W_p^{1/2}(Y_p-f)\|_2^2\) for \(f\in\mathbb R^{n_p}\). Use a fixed learning rate \(\nu\in(0,1)\). Spectral boosting starts at zero and updates, for integers \(m\ge0\),
\[
\hat f^{\mathrm{sp}}_{m+1}=\hat f^{\mathrm{sp}}_m+\nu P_{X,p}W_p(Y_p-\hat f^{\mathrm{sp}}_m).
\]
Ordinary boosting starts at zero and updates, for integers \(m\ge0\),
\[
\hat f^{\mathrm{or}}_{m+1}=\hat f^{\mathrm{or}}_m+\nu P_{X,p}(Y_p-\hat f^{\mathrm{or}}_m).
\]
Set \(w_{H,p}=\max_{1\le i\le q}w_{p,i}\) and \(w_{M,p}=\min_{q<i\le k_p}w_{p,i}\). Assume
\[
\frac{\|f_{0,p}\|_2}{\sqrt{n_p}}=O(1),\qquad \frac{\|g_{0,p}\|_2}{\sqrt{n_p}}=O(1),
\]
\[
\frac{\|(I_{n_p}-P_{H,p})g_{0,p}\|_2}{\sqrt{n_p}}\to0,\qquad
\frac{\|P_{H,p}f_{0,p}\|_2}{\sqrt{n_p}}\to0,
\]
and
\[
w_{H,p}\to0,\qquad \liminf_{p\to\infty}w_{M,p}\ge c>0,
\]
where \(c\) is independent of \(p\).

## Task

Prove the following integrated theorem. For every sequence of positive integer iteration counts \(m_p\) such that
\[
m_p\to\infty,\qquad m_p\nu w_{M,p}\to\infty,\qquad m_p\nu w_{H,p}\to0,
\]
spectral boosting satisfies
\[
\frac{\|E[\hat f^{\mathrm{sp}}_{m_p}\mid X_p]-f_{0,p}\|_2}{\sqrt{n_p}}\to0.
\]
In contrast, if additionally \(\liminf_{p\to\infty}\|g_{0,p}\|_2/\sqrt{n_p}>0\), then for every sequence of positive integer iteration counts \(m_p\) with \(m_p\to\infty\), ordinary boosting satisfies
\[
\frac{\|E[\hat f^{\mathrm{or}}_{m_p}\mid X_p]-f_{0,p}\|_2}{\sqrt{n_p}}\not\to0.
\]
