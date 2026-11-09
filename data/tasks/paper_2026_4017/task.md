# Problem

## Setup

Fix an integer $p\ge1$. Let $\mathcal M_p^+$ be the set of real $p\times p$ symmetric positive-definite matrices, with Lebesgue measure on the independent symmetric entries. For unconstrained variables
\[
v\in\mathbb R,\qquad d=(d_2,\ldots,d_p)\in\mathbb R^{p-1},\qquad r_j\in\mathbb R^{j-1}\ (2\le j\le p),
\]
set $d_1=-\sum_{j=2}^p d_j$ and $s_j=d_j+v/p$. Define $\Theta_1=[e^{s_1}]$ and, recursively,
\[
\Theta_j=\begin{pmatrix}
\Theta_{j-1}+e^{-s_j}r_jr_j^\top&r_j\\
r_j^\top&e^{s_j}
\end{pmatrix},\qquad j=2,\ldots,p.
\]
Write $\Theta=\Theta_p$ and $\Sigma=\Theta^{-1}$. The Fisher-Rao metric on $\mathcal M_p^+$ is
\[
 ds_{\rm FR}^2=\tfrac12\operatorname{Tr}\!\left((\Theta^{-1}d\Theta)^2\right).
\]
Let $dd=\prod_{j=2}^p dd_j$ and let $dr$ denote Lebesgue measure over all coordinates of the vectors $r_j$.

## Task

Prove the following integrated theorem. The recursive map above is a global diffeomorphism from $\mathbb R^{p(p+1)/2}$ onto $\mathcal M_p^+$. Its Jacobians with respect to symmetric-matrix Lebesgue measure satisfy
\[
J_{(v,d,r)\to\Theta}=e^v=\det\Theta,
\qquad
J_{(v,d,r)\to\Sigma}=e^{-pv}.
\]
Moreover, with $\Sigma_{j-1}=\Theta_{j-1}^{-1}$ and $D r_j=dr_j-r_jds_j$, the pulled-back Fisher-Rao line element is
\[
 ds_{\rm FR}^2=\tfrac12\sum_{j=1}^p(ds_j)^2+
\sum_{j=2}^p e^{-s_j}(D r_j)^\top\Sigma_{j-1}(D r_j).
\]
The corresponding Fisher-Rao volume form is
\[
 d\operatorname{vol}_{\rm FR}=2^{-p/2}e^{-(p-1)v/2}\,dv\,dd\,dr.
\]
Finally, under the normalized shape coordinates $\rho_j=e^{-v/p}r_j$, it becomes
\[
 d\operatorname{vol}_{\rm FR}=2^{-p/2}\,dv\,dd\,d\rho,
\]
so the volume density is constant in $(v,d,\rho)$.
