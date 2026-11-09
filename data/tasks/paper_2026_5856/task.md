# Problem

## Setup

Let \((X_t)_{t\in\mathbb N_0}\) be a real-valued homogeneous Markov chain on the Borel space \(\mathbb R\), with transition kernel \(P\), arbitrary initial law, and invariant probability measure \(\pi\). For probability measures \(\mu,\nu\), use the total variation convention
\[
\|\mu-\nu\|_{\mathrm{TV}}
=\sup_{a:\mathbb R\to\mathbb R\ \mathrm{measurable},\ |a|\le1}
\left|\int a\,d(\mu-\nu)\right|.
\]
Assume that for constants \(0<C<\infty\) and \(0<\rho<1\),
\[
\sup_x\|P^t(x,\cdot)-\pi\|_{\mathrm{TV}}\le C\rho^t
\qquad(t\in\mathbb N_0),
\]
where \(P^0(x,\cdot)\) is the point mass at \(x\).

Assume also that there are finite positive constants \(R,M,\sigma\) such that, for every \(x\in\mathbb R\),
\[
\int |x'|^2P(x,dx')\le R^2,
\]
and, with \(f_\star(x)=\int x'P(x,dx')\),
\[
\int |x'-f_\star(x)|^mP(x,dx')
\le {m!\over2}\sigma^2M^{m-2}
\qquad\text{for every integer }m\ge2.
\]
Let \(\mathcal H\) be a real separable Hilbert space and let \(\Phi:\mathbb R\to\mathcal H\) be a fixed measurable map with \(\|\Phi(x)\|\le\kappa\) for every \(x\), where \(0<\kappa<\infty\). Suppose the system is well specified: there is \(w_\star\in\mathcal H\) such that \(f_\star(x)=\langle w_\star,\Phi(x)\rangle\) for every \(x\).

Fix a positive integer \(T\) and observe the single trajectory \(X_0,\ldots,X_T\). For measurable real-valued functions \(f,g\in L^2(\pi)\), define
\[
\mathcal E(f,g)=\int (f(x)-g(x))^2\,\pi(dx).
\]
For \(u,v\in\mathcal H\), let \((u\otimes v)z=\langle z,v\rangle u\), and let \(I\) denote the identity on \(\mathcal H\). Define
\[
\Sigma=\int\Phi(x)\otimes\Phi(x)\,\pi(dx),\qquad
h=\int\Phi(x)f_\star(x)\,\pi(dx),
\]
\[
\widehat\Sigma={1\over T}\sum_{t=0}^{T-1}\Phi(X_t)\otimes\Phi(X_t),\qquad
\widehat h={1\over T}\sum_{t=0}^{T-1}\Phi(X_t)X_{t+1}.
\]
The vector and operator integrals are understood in the Bochner sense. For \(\lambda>0\), let
\[
\widehat w_\lambda=(\widehat\Sigma+\lambda I)^{-1}\widehat h,
\qquad
\widehat f_\lambda(x)=\langle\widehat w_\lambda,\Phi(x)\rangle.
\]
Set
\[
D_4=96\kappa^2(R+\kappa\|w_\star\|)^2,\quad
D_2=12\kappa^2M^2,\quad
D_3=6\kappa^2\sigma^2,
\]
and
\[
\Lambda_{T,\delta}={8C\kappa^2\over1-\rho}
\left(\sqrt{{2\log(6/\delta)\over T}}+{1\over T}\right).
\]

## Task

Prove that for every \(\delta\in(0,1)\) and every fixed \(\lambda\ge\Lambda_{T,\delta}\), with probability at least \(1-\delta\) under the law of the observed trajectory,
\[
\begin{aligned}
\mathcal E(\widehat f_\lambda,f_\star)
\le{}&{2C^2D_4\over(1-\rho)^2}
\left({2\log(6/\delta)\over\lambda T}+{1\over\lambda T^2}\right)
+{2D_2\log^2(6/\delta)\over\lambda T^2}\\
&+{2D_3\log(6/\delta)\over\lambda T}
+2\lambda\|w_\star\|^2.
\end{aligned}
\]
In particular, for fixed \(\delta\), let \(\lambda_T=\gamma T^{-1/2}\), where \(\gamma>0\) is independent of \(T\) and is chosen so that \(\lambda_T\ge\Lambda_{T,\delta}\) for every positive integer \(T\). Show that such a choice exists and that the corresponding bound is of order \(T^{-1/2}\) up to logarithmic and boundary terms, explicitly retaining the substituted powers of \(T\). The probability guarantee in this specialization is for each fixed \(T\), not simultaneously over all \(T\).
