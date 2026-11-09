# Problem

## Setup

Consider a sequence of experiments with an integer \(p\ge2\), and fix a node \(j\in\{1,\ldots,p\}\). Let \(\mathcal A\) be a finite known set of positive source-domain labels, fixed independently of the observed samples; it may be empty. Write \(\mathcal R=\{0\}\cup\mathcal A\). Each sample size \(n_r\), \(r\in\mathcal R\), is a positive integer fixed before sampling.

For each \(r\in\mathcal R\), let \(\Theta^{(r)}\in\mathbb R^{p\times p}\) be a symmetric zero-diagonal matrix. Domain \(r\) supplies independent copies \(X_1^{(r)},\ldots,X_{n_r}^{(r)}\) with probability mass function
\[
\mathbb P_r(X=x)=
\frac{\exp\!\left(\sum_{1\le k<\ell\le p}\Theta^{(r)}_{k\ell}x_kx_\ell\right)}
{\displaystyle\sum_{y\in\{-1,1\}^p}\exp\!\left(\sum_{1\le k<\ell\le p}\Theta^{(r)}_{k\ell}y_ky_\ell\right)},
\qquad x\in\{-1,1\}^p.
\]
The samples from different domains are independent. Domain \(0\) is the target domain.

Put \(I=\{1,\ldots,p\}\setminus\{j\}\). All nodewise vectors below belong to \(\mathbb R^{p-1}\), with coordinates indexed by \(I\); complements of coordinate sets are taken in \(I\). Vector norms are the usual \(\ell_q\) norms. For a matrix \(H\), \(\|H\|_1=\max_k\sum_\ell|H_{\ell k}|\) denotes its induced \(\ell_1\) norm.

Define
\[
\vartheta=\Theta^{(0)}_{j,-j},\qquad b^{(r)}=\Theta^{(r)}_{j,-j}\quad(r\in\mathcal A),
\qquad S=\operatorname{supp}(\vartheta),\qquad s=|S|.
\]
For \(z_i^{(r)}=2X_{ij}^{(r)}X_{i,-j}^{(r)}\) and \(f(t)=\log(1+e^{-t})\), define
\[
\ell_r(u)=\frac1{n_r}\sum_{i=1}^{n_r}f\bigl((z_i^{(r)})^Tu\bigr),
\qquad L_r(u)=\mathbb E\ell_r(u),\qquad u\in\mathbb R^{p-1}.
\]
Let
\[
N=n_0+\sum_{r\in\mathcal A}n_r,
\qquad \alpha_r=\frac{n_r}{N},
\qquad \ell_P=\sum_{r\in\mathcal R}\alpha_r\ell_r,
\qquad L_P=\mathbb E\ell_P.
\]
Let \(w^\circ\) minimize \(L_P\) over \(\mathbb R^{p-1}\), and define \(d^\circ=\vartheta-w^\circ\).

For a fixed \(a>2\) and a positive penalty level \(\lambda\), define
\[
P_\lambda(t)=
\begin{cases}
\lambda|t|,& |t|\le\lambda,\\
\dfrac{-t^2+2a\lambda|t|-\lambda^2}{2(a-1)},&
\lambda<|t|\le a\lambda,\\
\dfrac{(a+1)\lambda^2}{2},&|t|>a\lambda.
\end{cases}
\]
For positive \(\lambda_w,\lambda_d,\lambda\), the two-stage estimator is
\[
\widehat w\in\arg\min_{u\in\mathbb R^{p-1}}
\{\ell_P(u)+\lambda_w\|u\|_1\},
\]
followed by a returned local solution \(\widehat d\in\mathbb R^{p-1}\) of
\[
Q(d)=\ell_0(\widehat w+d)+\lambda_d\|d\|_1
       +\sum_{k\in I}P_\lambda(\widehat w_k+d_k),
\qquad
\widehat\vartheta=\widehat w+\widehat d.
\]
Returned solutions are understood as measurable selections. No symmetrization is applied to the vector \(\widehat\vartheta\) considered here.

For the stationarity condition below, define
\[
G(t)=\begin{cases}\{\operatorname{sign}(t)\},&t\ne0,\\[-1,1],&t=0,\end{cases}
\qquad
D_\lambda(t)=\begin{cases}\{P_\lambda'(t)\},&t\ne0,\\[-\lambda,\lambda],&t=0.\end{cases}
\]
The notation \(\partial Q(d)\) means the set of vectors
\[
\nabla\ell_0(\widehat w+d)+\lambda_d g+q,
\qquad
 g_k\in G(d_k),\quad q_k\in D_\lambda(\widehat w_k+d_k)\quad(k\in I),
\]
and \(\operatorname{dist}_\infty(0,\partial Q(d))=\inf_{\xi\in\partial Q(d)}\|\xi\|_\infty\).

Assume the following.

1. **Sparsity and heterogeneity.** For a nonnegative heterogeneity level \(h\), one has \(s=o(n_0/\log p)\), and for every \(r\in\mathcal A\),
\[
\|\vartheta-b^{(r)}\|_1\le h.
\]

2. **Population Hessian comparability and true-parameter fields.** There is a convex set \(\mathcal U\subseteq\mathbb R^{p-1}\) containing \(\vartheta,w^\circ\), and every \(b^{(r)}\), and a fixed constant \(C_H>0\), such that \(\nabla^2L_P(u)\) is invertible for every \(u\in\mathcal U\) and
\[
\|\{\nabla^2L_P(u)\}^{-1}\nabla^2L_r(v)\|_1\le C_H
\qquad(r\in\mathcal R,\ u,v\in\mathcal U).
\]
For \(q\in\mathcal R\cup\{P\}\) and \(u_0,u_1\in\mathcal U\), write
\[
\overline H_q[u_0,u_1]
=\int_0^1\nabla^2L_q\bigl(u_0+t(u_1-u_0)\bigr)\,dt.
\]
For every \(r\in\mathcal R\) and every \(u_0,u_1,v_0,v_1\in\mathcal U\), the matrix \(\overline H_P[u_0,u_1]\) is invertible and
\[
\|\overline H_P[u_0,u_1]^{-1}\overline H_r[v_0,v_1]\|_1\le C_H.
\]
There is also a fixed finite \(M\ge0\) such that
\[
\max_{r\in\mathcal R}\ \max_{1\le m\le p}\ \max_{x\in\{-1,1\}^p}
2\left|\sum_{k\ne m}\Theta^{(r)}_{mk}x_k\right|\le M.
\]
In particular, \(\inf_{|t|\le M}f''(t)>0\). This field bound concerns the true domain matrices; empirical curvature is specified separately below.

3. **Empirical pooled curvature (E1).** There are fixed constants \(\kappa_P>0,\tau_P\ge0\) and a radius \(r_P>0\) such that, for every \(\Delta\in\mathbb R^{p-1}\) satisfying
\[
\|\Delta_{S^c}\|_1\le3\|\Delta_S\|_1+4\|(w^\circ)_{S^c}\|_1
\]
and every \(u\in\mathbb R^{p-1}\) with \(\|u-w^\circ\|_1\le r_P\),
\[
\Delta^T\nabla^2\ell_P(u)\Delta
\ge \kappa_P\|\Delta\|_2^2-\tau_P\frac{\log p}{N}\|\Delta\|_1^2.
\]
Also \(\|\widehat w-w^\circ\|_1\le r_P\).

4. **Empirical target curvature (E2).** Choose a fixed \(C_h\ge1\) satisfying \(\|d^\circ\|_1\le C_hh\), and put
\[
t_0=\left\lceil\frac{C_hh}{\lambda_d}\right\rceil.
\]
There are fixed constants \(\kappa_0>0,\tau_0\ge0\) and a radius \(r_0>0\) such that, for every \(T\subseteq I\) with \(|T|\le t_0\), every \(\Delta\in\mathbb R^{p-1}\) satisfying
\[
\|\Delta_{T^c}\|_1\le3\|\Delta_T\|_1+3C_hh,
\]
and every \(u\in\mathbb R^{p-1}\) with \(\|u-\vartheta\|_1\le r_0\),
\[
\Delta^T\nabla^2\ell_0(u)\Delta
\ge \kappa_0\|\Delta\|_2^2-\tau_0\frac{\log p}{n_0}\|\Delta\|_1^2.
\]

5. **Returned correction (E3) and correction cone (E4).** For some \(r_d>0\) and \(\epsilon_n\ge0\), condition (E3) requires
\[
\operatorname{dist}_\infty(0,\partial Q(\widehat d))\le\epsilon_n,
\qquad \|\widehat d-d^\circ\|_1\le r_d,
\]
and
\[
Q(\widehat d)\le Q(d)\qquad
\text{for every }d\in\mathbb R^{p-1}\text{ with }\|d-d^\circ\|_1\le r_d.
\]
Both \(\widehat w+d^\circ\) and \(\widehat w+\widehat d\) are within \(\ell_1\)-distance \(r_0\) of \(\vartheta\). Condition (E4) requires that, with
\[
v=\widehat d-d^\circ,
\qquad T=\{k\in I:|d_k^\circ|>\lambda_d\},
\]
one has
\[
\|v_{T^c}\|_1\le3\|v_T\|_1+3C_hh.
\]

Suppose (E1)–(E4) hold simultaneously with probability at least \(1-C_1p^{-C_2}\), for fixed \(C_1,C_2>0\). Choose sufficiently large fixed positive constants in
\[
\lambda_w=C_w\sqrt{\frac{\log p}{N}},
\qquad
\lambda_d=C_d\sqrt{\frac{\log p}{n_0}},
\qquad
\lambda=C_\lambda\sqrt{\frac{\log p}{n_0}}.
\]
Finally, assume
\[
\frac{\log p}{n_0}=o(1),
\qquad
\frac{s\log p}{N}+\frac{\log p}{N}h^2=o(1),
\]
and that there is a fixed \(K\ge1\) such that, for all sufficiently large indices of the sequence,
\[
s\sqrt{\frac{\log p}{N}}+h\le K\lambda_d.
\]
All asymptotic statements refer to this sequence. The constants described as fixed do not depend on \(n_0,N,p,s,h\).

## Task

Prove that there are constants \(C,C_0,c_0>0\), depending only on the fixed constants in the setup and not on \(n_0,N,p,s,h\), such that, for all sufficiently large indices, with probability at least \(1-C_0p^{-c_0}\), both
\[
\|\widehat\vartheta-\vartheta\|_2
\le C\left[
\sqrt{\frac{s\log p}{N}}
+\min\left\{\left(\frac{\log p}{N}\right)^{1/4}h^{1/2},h\right\}
+\min\left\{\left(\frac{\log p}{n_0}\right)^{1/4}h^{1/2},h\right\}
\right]
\]
and
\[
\|\widehat\vartheta-\vartheta\|_1
\le C\left(s\sqrt{\frac{\log p}{N}}+h\right)
\]
hold.
