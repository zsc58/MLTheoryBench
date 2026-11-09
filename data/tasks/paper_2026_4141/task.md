# Problem

## Setup

Let \(Z=(X,Y)\sim P\) take values in \(\mathcal X\times\mathcal Y\subset\mathbb R^d\times\mathbb R\), equipped with their relative Borel sigma-fields, and let \(Z_1,\ldots,Z_n\) be iid copies. Let \(\mathcal H\) be the real RKHS on \(\mathcal X\) with continuous bounded kernel \(K\), feature vector \(K_x=K(x,\cdot)\), and \(\sup_x\sqrt{K(x,x)}\le\kappa<\infty\).

Let \(\ell:\mathbb R\times\mathcal Y\to[0,\infty)\) be measurable, convex and twice differentiable in its first argument. Write \(\ell'\) and \(\ell''\) for its prediction derivatives and \(\ell^{(0)}=\ell\). For every \(B>0\), assume there is a finite nonnegative measurable function \(\phi_B\) such that, for every \(y\in\mathcal Y\), \(u,v\in[-B,B]\), and \(k\in\{0,1,2\}\),
\[
|\ell^{(k)}(u,y)-\ell^{(k)}(v,y)|\le\phi_B(y)|u-v|.
\]
Assume \(E\phi_B(Y)^4<\infty\) for every \(B>0\), and \(E|\ell^{(k)}(0,Y)|^4<\infty\) for \(k=0,1,2\).

Let \(\lambda_0>0\), let \(\lambda_n>0\) almost surely, and assume \(\sqrt n(\lambda_n-\lambda_0)\to0\) in probability. Define
\[
L(h)=E\,\ell(h(X),Y),\qquad
R(h)=L(h)+\tfrac{\lambda_0}{2}\|h\|_{\mathcal H}^2,
\]
and let \(h_0\) be the unique minimizer of \(R\) over \(\mathcal H\). Let
\[
L_n(h)=\frac1n\sum_{i=1}^n\ell(h(X_i),Y_i),\qquad
g(Z)=\ell'(h_0(X),Y)K_X,\qquad G=Eg(Z),
\]
\[
\Sigma=E[g(Z)\otimes g(Z)]-G\otimes G.
\]
Here \((u\otimes v)w=\langle v,w\rangle_{\mathcal H}u\), and vector and operator expectations are Bochner expectations.

Let \(\psi:\mathcal X\times\mathcal Y\to(0,\infty)\) be a fixed deterministic measurable function, independent of \(n\). Assume
\[
E\psi(Z)<\infty,\qquad
E\left[\frac{\ell'(h_0(X),Y)^2K(X,X)}{\psi(Z)}\right]<\infty.
\]
For each \(n\), set
\[
\pi_{n,i}=\frac{\psi(Z_i)}{\sum_{j=1}^n\psi(Z_j)},\qquad 1\le i\le n,
\]
and assume
\[
E\left[\max_{1\le i\le n}\left(\frac1{n\pi_{n,i}}\right)^2\right]=O(1).
\]
Let \(s_n\) be a deterministic sequence of positive integers tending to infinity. Let \(\lambda^*_{s_n}>0\) almost surely be a possibly random regularization parameter satisfying
\[
\sqrt{s_n}(\lambda^*_{s_n}-\lambda_0)\longrightarrow0
\quad\text{in probability}.
\]

Consider either of the following sampling designs, with all sampling distributions specified conditionally on \(Z_1,\ldots,Z_n\):

- **Multinomial design:** Draw \(s_n\) independent indices from \(\{1,\ldots,n\}\) with probabilities \(\pi_{n,1},\ldots,\pi_{n,n}\), and let \(\gamma_{n,i}\) be the number of times index \(i\) is drawn. Assume \(s_n/n\to c\in[0,\infty)\).
- **Poisson design:** Draw independent indicators \(\gamma_{n,i}\) with Bernoulli means \(s_n\pi_{n,i}\). Assume \(\pi_{n,i}\le1/s_n\) almost surely for every \(n,i\), and \(s_n/n\to c\in[0,1]\).

For the chosen design define
\[
L^*_{s_n}(h)=\frac1n\sum_{i=1}^n\ell(h(X_i),Y_i)\frac{\gamma_{n,i}}{s_n\pi_{n,i}},\qquad
R^*_{s_n}(h)=L^*_{s_n}(h)+\tfrac{\lambda^*_{s_n}}2\|h\|_{\mathcal H}^2,
\]
and let \(h^*_{s_n}\) be the unique minimizer of \(R^*_{s_n}\) over \(\mathcal H\). All probability limits refer to the joint law of the observations and the random quantities in the chosen design.

## Task

Prove that, as \(n,s_n\to\infty\), both estimators are consistent,
\[
\|h^*_{s_n}-h_0\|_{\mathcal H}\longrightarrow0
\quad\text{in probability},
\]
and satisfy the following RKHS-valued limits. Define
\[
\Sigma_M^*(\psi)=E\left[\frac{E\psi(Z)}{\psi(Z)}\ell'(h_0(X),Y)^2K_X\otimes K_X\right]-G\otimes G,
\]
\[
\Sigma_{P,c}^*(\psi)=E\left[\frac{E\psi(Z)}{\psi(Z)}\ell'(h_0(X),Y)^2K_X\otimes K_X\right]-cE[g(Z)\otimes g(Z)].
\]
Then
\[
\sqrt{s_n}\,\operatorname{Hess}R(h_0)(h^*_{s_n}-h_0)
\Rightarrow\mathcal{GP}\bigl(0,\Sigma_M^*(\psi)+c\Sigma\bigr)
\]
for multinomial sampling, and
\[
\sqrt{s_n}\,\operatorname{Hess}R(h_0)(h^*_{s_n}-h_0)
\Rightarrow\mathcal{GP}\bigl(0,\Sigma_{P,c}^*(\psi)+c\Sigma\bigr)
\]
for Poisson sampling. Here \(\operatorname{Hess}R(h_0)\) is the Frechet Hessian, \(\Rightarrow\) denotes weak convergence for the norm topology of \(\mathcal H\), and \(\mathcal{GP}(0,C)\) denotes the centered Gaussian measure on \(\mathcal H\) with covariance operator \(C\), allowing degenerate covariance.
