# Reference Proof

## Proof Structure

1. Establish the required uniform moment bounds for the stochastic-gradient chain.
2. Solve the linear Poisson equation explicitly.
3. Telescope the recursion through this solution.
4. Show that the boundary and stochastic-gradient terms vanish, then identify the Gaussian limit.

## Complete Proof

Throughout, the stepsize superscript is suppressed. Constants in estimates may depend on the fixed matrices, dimension, dissipativity constants, moment exponent, uniform oracle and initial moment bounds, and the fixed observable, but not on the stepsize or time index.

### Algebra and the Gaussian target

Both \(P\) and \(D+Q\) are invertible. Indeed, if \((D+Q)v=0\), then
\[
0=v^\top(D+Q)v=v^\top Dv,
\]
so \(v=0\). Hence \(A=(D+Q)P\) is invertible.

The density proportional to \(e^{-x^\top Px/2}\) is \(\mu=N(0,P^{-1})\), so \(\mu(h)=0\). The full-gradient generator is
\[
\mathcal Lf(x)=-\langle Ax,\nabla f(x)\rangle+\operatorname{Tr}(D\nabla^2f(x)).
\]
For completeness, write \(\Sigma=P^{-1}\). Then
\[
A\Sigma+\Sigma A^\top=(D+Q)+(D-Q)=2D.
\]
The linear diffusion started independently with law \(N(0,\Sigma)\) remains centered Gaussian, with covariance
\[
e^{-At}\Sigma e^{-A^\top t}+2\int_0^t e^{-As}D e^{-A^\top s}\,ds=\Sigma.
\]
The equality follows by differentiating \(e^{-As}\Sigma e^{-A^\top s}\). Thus \(\mu\) is invariant. No general Poisson regularity theorem is used.

### Uniform moments

Inductively, \(X_k\) is \(\mathcal F_k\)-measurable. Conditional moment monotonicity gives, for \(1\le q\le p\),
\[
\mathbb E[\|\varepsilon_{k+1}\|^q\mid\mathcal F_k]
\le C_q(1+\|X_k\|^q).
\]
Fix a step and write \(x=X_k\), \(r=\|x\|\), and
\[
Y=\eta g(x)+\sqrt\eta\,\sigma\xi_{k+1}+\eta\varepsilon_{k+1}.
\]
Conditional centering gives \(\mathbb E[Y\mid\mathcal F_k]=\eta g(x)\). Since \(\|g(x)\|\le\|A\|_{\rm op}r\), elementary power inequalities, Gaussian moments, and the oracle bounds give
\[
\mathbb E[\|Y\|^2\mid\mathcal F_k]\le K\eta+K\eta^2(1+r^2),
\]
\[
\mathbb E[\|Y\|^p\mid\mathcal F_k]\le K\eta^{p/2}+K\eta^p(1+r^p).
\]
For \(p>2\), Taylor's formula and the Hessian bound for \(x\mapsto\|x\|^p\) imply
\[
\|x+y\|^p\le\|x\|^p+p\|x\|^{p-2}\langle x,y\rangle
+K_p\bigl(\|x\|^{p-2}\|y\|^2+\|y\|^p\bigr).
\]
Consequently, using \(\langle x,g(x)\rangle\le-mr^2+b\),
\[
\begin{aligned}
\mathbb E[\|X_{k+1}\|^p\mid\mathcal F_k]
\le{}&r^p-pm\eta r^p+K\eta r^{p-2}
+K\eta^2(r^p+r^{p-2})\\
&+K\eta^{p/2}+K\eta^p(1+r^p).
\end{aligned}
\]
For every \(\delta>0\), \(r^{p-2}\le\delta r^p+K_\delta\). Choose \(\delta\) small enough to absorb the terms of order \(\eta r^{p-2}\) into a fixed fraction of \(pm\eta r^p\). Then choose \(\eta_0>0\) small enough to absorb the remaining coefficients of orders \(\eta^2\) and \(\eta^p\). Since \(p/2>1\), all constant terms are bounded by \(K\eta\). Thus, for \(0<\eta<\eta_0\),
\[
\mathbb E[\|X_{k+1}\|^p\mid\mathcal F_k]
\le(1-c\eta)\|X_k\|^p+K\eta,
\]
where \(c>0\) and \(0<c\eta<1\). Taking expectations and iterating proves
\[
\sup_{0<\eta<\eta_0}\sup_{k\ge0}\mathbb E\|X_k\|^p
\le C_0+K/c<\infty.
\]
Jensen's inequality gives the corresponding bounds for every \(q\in[1,p]\), in particular for both endpoints of the averaging interval. It also follows that
\[
\sup_{0<\eta<\eta_0}\sup_{k\ge0}\mathbb E\|\varepsilon_{k+1}\|^2<\infty.
\]
This argument closes the moment estimate under the source's state-dependent conditional bound; it does not assume a uniform conditional bound independent of \(X_k\).

### Linear Poisson solution and exact telescoping

Set
\[
c=-(A^{-1})^\top u,\qquad \phi(x)=c^\top x.
\]
Then
\[
\mathcal L\phi(x)=-c^\top Ax=u^\top x=h(x),
\]
and
\[
2c^\top Dc=2u^\top A^{-1}D(A^{-1})^\top u=V(h).
\]
Write \(N=N_\eta\). Linearity and the recursion give
\[
\phi(X_{k+1})-\phi(X_k)
=\eta h(X_k)+\sqrt\eta\,c^\top\sigma\xi_{k+1}
+\eta c^\top\varepsilon_{k+1}.
\]
Summing and solving for the normalized empirical average gives the exact identity
\[
\eta^{-1/2}\widehat m_\eta
=\frac{\phi(X_N)-\phi(X_0)}{N\eta^{3/2}}
-\frac1{N\eta}\sum_{k=0}^{N-1}c^\top\sigma\xi_{k+1}
-\frac1{N\sqrt\eta}\sum_{k=0}^{N-1}c^\top\varepsilon_{k+1}.
\]
There is no floor-approximation remainder. Since \(N=\lfloor\eta^{-2}\rfloor\), we have \(N\eta^2\to1\) and \(N\eta\to\infty\).

### Negligible terms and the Gaussian limit

The endpoint term satisfies
\[
\mathbb E\left|\frac{\phi(X_N)-\phi(X_0)}{N\eta^{3/2}}\right|^2
\le\frac{K}{N^2\eta^3}\longrightarrow0.
\]
For the oracle term, adaptedness and conditional centering imply orthogonality of different summands. In fact, for \(i<j\),
\[
\mathbb E[(c^\top\varepsilon_{i+1})(c^\top\varepsilon_{j+1})]
=\mathbb E[(c^\top\varepsilon_{i+1})\mathbb E[c^\top\varepsilon_{j+1}\mid\mathcal F_j]]=0.
\]
All products are integrable by the second-moment bounds. Therefore
\[
\mathbb E\left|\frac1{N\sqrt\eta}\sum_{k=0}^{N-1}c^\top\varepsilon_{k+1}\right|^2
\le\frac{K}{N^2\eta}\sum_{k=0}^{N-1}\mathbb E(1+\|X_k\|^2)
\le\frac{K}{N\eta}\longrightarrow0.
\]
The middle term is exactly centered Gaussian because its coefficients are deterministic and the Gaussian innovations are independent. Its variance is
\[
\frac1{N\eta^2}c^\top\sigma\sigma^\top c
=\frac{2c^\top Dc}{N\eta^2}\longrightarrow V(h).
\]
For example, its characteristic function at \(t\) is \(\exp[-t^2V(h)/(2N\eta^2)]\), which converges to that of \(N(0,V(h))\). Slutsky's theorem, in the form that adding a term converging to zero in probability preserves a distributional limit, now applies to the two terms already shown to vanish in \(L^2\). No independence between the Gaussian sum and those negligible terms is required. Thus
\[
\eta^{-1/2}(\widehat m_\eta-\mu(h))\Rightarrow N(0,V(h)).
\]
If \(u=0\), all terms are identically zero and the conclusion is the point mass \(N(0,0)\). For \(u\ne0\), invertibility of \(A\) and positive definiteness of \(D\) give \(V(h)>0\).

Finally, when \(Q=0\), \(A=DP\), so
\[
V_0(h)=2u^\top(DP)^{-1}D\bigl((DP)^{-1}\bigr)^\top u.
\]
The proof applies to every oracle family satisfying the stated assumptions and shows that its fixed-variance stochastic-gradient perturbation contributes nothing to the leading variance.
