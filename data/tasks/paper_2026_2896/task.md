# Problem

## Setup

Let \(\mathsf H\) be a real separable Hilbert space with orthonormal basis \((u_j)_{j\ge1}\). Let \(I\) be finite or countable, with weights \(w_i>0\), \(\sum_iw_i=1\). For every \(i\in I\), set
\[
a_i=\sum_{j\ge1}a_{ij}u_j,\qquad S_i u_j=s_{ij}u_j,
\]
where \(s_{ij}>0\), \(\sum_ja_{ij}^2<\infty\), and \(\sum_js_{ij}<\infty\). Define envelopes
\(\underline s_j=\inf_i s_{ij}>0\), \(\overline s_j=\sup_i s_{ij}<\infty\), \(\overline a_j=\sup_i|a_{ij}|\), and \(\Delta a_j=\sup_{i,l}|a_{ij}-a_{lj}|\).

For \(d\ge1\), identify \(\operatorname{span}(u_1,\ldots,u_d)\) with \(\mathbb R^d\), and set
\[
a_i^d=(a_{i1},\ldots,a_{id}),\qquad S_i^d=\operatorname{Diag}(s_{i1},\ldots,s_{id}),\qquad \pi_*^d=\sum_iw_i\,\mathcal N(a_i^d,S_i^d).
\]
Let \((\ell_j)_{j\ge1}\) and \((g_j)_{j\ge1}\) be fixed positive sequences, and define
\[
C^d=\operatorname{Diag}(\ell_1,\ldots,\ell_d),\qquad \Gamma^d=\operatorname{Diag}(g_1,\ldots,g_d).
\]
All these coordinate data are fixed across truncation dimensions.

For \(T>0\) and \(t\in[0,T]\), put \(\kappa_t=(T-t)/T\), \(B_t^d=\operatorname{Diag}(\underline s_j+\kappa_t\ell_j)_{j=1}^d\), and
\[
\pi_t^d=\pi_*^d*\mathcal N(0,\kappa_tC^d),\qquad D_{i,t}^d=S_i^d+\kappa_tC^d.
\]
Define \(G_t^d\) by the mixture-score decomposition
\[
\nabla\log\pi_t^d(x)=-(B_t^d)^{-1}x+G_t^d(x).
\]
The preconditioned annealed Langevin diffusion is
\[
dX_t=\Gamma^d\nabla\log\pi_t^d(X_t)dt+\sqrt{2\Gamma^d}\,dW_t,
\]
where \(W_t\) is standard Brownian motion in \(\mathbb R^d\), independent of \(X_0\sim\pi_0^d\). Denote its terminal law by \(\pi_T^{\rm ALD,d}\).

The ELP scheme uses a finite deterministic mesh \(0=t_0<\cdots<t_N=T\), with \(N\ge1\), \(h_n=t_{n+1}-t_n\), \(h_{\max}=\max_nh_n\), and \(Y_0^d\sim\pi_0^d\). For \(j=1,\ldots,d\), set
\[
\phi_{n,j}=\exp\!\left(-\int_{t_n}^{t_{n+1}}\frac{g_j}{\underline s_j+\kappa_r\ell_j}\,dr\right),
\]
\[
\psi_{n,j}=\int_{t_n}^{t_{n+1}}\exp\!\left(-\int_s^{t_{n+1}}\frac{g_j}{\underline s_j+\kappa_r\ell_j}\,dr\right)g_j\,ds.
\]
For each fixed dimension, let \(\xi_{n,j}\) be mutually independent centered Gaussian random variables across mesh intervals and coordinates, independent of \(Y_0^d\), with variance
\[
2g_j\int_{t_n}^{t_{n+1}}\exp\!\left(-2\int_s^{t_{n+1}}\frac{g_j}{\underline s_j+\kappa_r\ell_j}\,dr\right)ds.
\]
Update
\[
Y_{n+1,j}^d=\phi_{n,j}Y_{n,j}^d+\psi_{n,j}G_{t_n,j}^d(Y_n^d)+\xi_{n,j}.
\]

Assume the following sums, all over \(j\ge1\), are finite:
\[
\text{(A1)}\quad \sum_j(\overline s_j+\ell_j+\overline a_j^2),
\]
\[
\text{(A2)}\quad \sum_jg_j,\qquad \sum_j\frac{g_j^2(\overline s_j+\ell_j+\overline a_j^2)}{\underline s_j^2},
\]
\[
\text{(A3)}\quad \sum_j\frac{g_j[(\overline s_j-\underline s_j)^2+\underline s_j^2\overline a_j^2]}{\underline s_j^4},
\]
\[
\text{(A4)}\quad \sum_j\frac{(\overline s_j-\underline s_j)^2}{\underline s_j^4}(\overline s_j+\ell_j+\overline a_j^2),\qquad \sum_j\frac{\Delta a_j^2}{\underline s_j^2},
\]
\[
\text{(A5)}\quad \sum_j\frac{\ell_j(\overline s_j-\underline s_j)}{\underline s_j^3}(\overline s_j+\ell_j+\overline a_j^2),\qquad \sum_j\frac{g_j\ell_j^2(\overline s_j-\underline s_j)^2(\overline s_j+\ell_j+\overline a_j^2)}{\underline s_j^6},
\]
\[
\text{(A6)}\quad \sum_j\frac{\ell_j^2}{\underline s_j^2}\left(\frac{\Delta a_j^2}{\underline s_j^2}+\frac{\overline a_j^2(\overline s_j-\underline s_j)^2}{\underline s_j^4}\right),\qquad \sum_j\frac{g_j\ell_j^2\overline a_j^2}{\underline s_j^4},
\]
\[
\text{(A7)}\quad \sum_j\frac{\ell_j^2}{g_j\underline s_j}.
\]

## Task

Prove that there exists a constant \(C_{\rm disc}>0\), depending only on the numerical values of the summability bounds above and not on \(d,T\), or the mesh, such that for every \(d\ge1\), every \(T>0\), and every finite deterministic mesh,
\[
\mathrm{KL}\!\left(\pi_*^d\,\middle\|\,\mathcal L(Y_N^d)\right)
\le \frac1{8T}\sum_{j=1}^d\frac{\ell_j^2}{g_j\underline s_j}+C_{\rm disc}(1+T^2)h_{\max}.
\]
Consequently, for any prescribed \(\varepsilon_{\rm ann},\varepsilon_{\rm disc}>0\), choosing the same horizon and mesh for all dimensions so that
\[
\frac1{8T}\sum_{j\ge1}\frac{\ell_j^2}{g_j\underline s_j}\le\varepsilon_{\rm ann},\qquad C_{\rm disc}(1+T^2)h_{\max}\le\varepsilon_{\rm disc}
\]
yields
\[
\sup_{d\ge1}\mathrm{KL}(\pi_*^d\|\mathcal L(Y_N^d))\le\varepsilon_{\rm ann}+\varepsilon_{\rm disc}.
\]
