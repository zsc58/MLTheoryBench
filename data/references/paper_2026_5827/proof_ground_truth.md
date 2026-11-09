# Reference Proof

## Contract and obligations

The capacity cost and geometric projection cost are different path functionals. Only the former requires nonincreasing capacity. During a discrete projection step the rate is frozen at its initial value, and a merge has pre-deletion coordinates \((f_p,f_p)\), not a single parent coordinate. The optimal scale minimizes the normalized duplicated-parent error over all positive scales. It is not the scale of a least-squares approximation to the child sum.

We prove: (1) capacity uniqueness for the stated generalized separable form; (2) the scale law, path formula, and extinction divergence; (3) the conditional straight-path bound; (4) exact fixed-magnitude parent optimization and attainment; and (5) the correlated-merge capacity guarantee. All obligations are closed below.

## 1. Capacity uniqueness

Write
\[
E(f_1,\ldots,f_N)=h\!\left(\sum_k g(\|f_k\|)\right).
\]
Singleton normalization gives \(h(g(x))=x\) for every \(x\ge0\). Partition invariance applied to a singleton of norm \(mx\) gives
\[
h(mg(x))=mx \qquad(m\ge1).
\]
We must not yet replace \(h\) by \(g^{-1}\) at arbitrary sums.

Replacing \(g\) by \(-g\) and \(h(z)\) by \(h(-z)\), if necessary, we may suppose \(g\) is increasing. Put \(d=g(0)\). If \(d>0\), continuity and strict increase imply that, for a sufficiently large integer \(m\), there is \(x>0\) with \(g(x)=(m+1)d/m\). Then
\[
mx=h(mg(x))=h((m+1)g(0))=0,
\]
a contradiction. If \(d<0\), choose \(m\) large enough that \(g(x)=md/(m+1)\) for some \(x>0\). The same argument gives
\[
(m+1)x=h((m+1)g(x))=h(mg(0))=0.
\]
Thus \(g(0)=0\).

For any \(x\ge0\) and integer \(m\ge1\), continuity gives \(y\in[0,x]\) with \(g(y)=g(x)/m\). Consequently
\[
x=h(g(x))=h(mg(y))=my,
\]
so \(g(x/m)=g(x)/m\). Integer and rational homogeneity follow, and continuity gives \(g(x)=\lambda x\), with \(\lambda\ne0\). Every finite sum of values of \(g\) is now in its image, and singleton normalization proves
\[
E(\Phi)=\sum_k\|f_k\|_{\mathcal H}.
\]
In particular, \(E(a\Phi)=aE(\Phi)\) for \(a>0\).

## 2. Capacity cost

The support-preserving radial path from \(\Phi\) to \(a\Phi\) shows that \(c(a\Phi)=c(\Phi)\). Since \(c=\xi E\), this also gives
\[
\xi(a\Phi)=a^{-1}\xi(\Phi).
\]
Equivalently, the same density law follows by applying magnitude neutrality and additivity to subsegments of a radial decreasing path.

The scalar function \(E(\Phi(t))\) is absolutely continuous on a \(C^1\) product-Hilbert path: each coordinate norm is Lipschitz on the compact parameter interval. Its derivative therefore exists almost everywhere. Additivity, zero cost on a constant path, and the infinitesimal axiom give
\[
J[\Phi]=\int_0^1-\xi(\Phi(t))\dot E(t)\,dt
=\int_0^1-c(\Phi(t))\frac{\dot E(t)}{E(\Phi(t))}\,dt.
\]
For nonincreasing capacity and a uniform lower bound \(c\ge c_{\min}>0\),
\[
J[\Phi]\ge c_{\min}\log\frac{E(\Phi(0))}{E(\Phi(1))}.
\]
With the initial state fixed and positive, this tends to infinity as terminal capacity tends to zero. Flat portions of a path contribute zero; no strictly decreasing change of variables is required.

## 3. Conditional geometric bound

By definition, for the chosen straight pre-deletion path,
\[
J_{\rm proj}=\int_0^1c(\Phi_a)\frac{\|\dot\Phi(t)\|_{\mathcal H^N}}{E(\Phi(t))}\,dt.
\]
Its speed is the constant \(D=\|\widetilde\Phi_b-\Phi_a\|_{\mathcal H^N}\). If \(E(\Phi(t))\ge E(\Phi_b)>0\) throughout the path, then
\[
J_{\rm proj}\le \frac{c(\Phi_a)D}{E(\Phi_b)}.
\]
This calculation does not require monotone capacity. For pruning, the moving coordinate is \((1-t)f_i\), so the lower-capacity condition holds automatically whenever the post-deletion capacity is positive. For merging, the pre-deletion state has two copies of the parent and the terminal state has one; the required lower bound is established in Section 5.

## 4. Exact parent direction and attainment

Let \(S=f_i+f_j\), \(q=\|f_i\|^2+\|f_j\|^2\), and \(R\ge0\) be the residual capacity. For fixed \(s>0\), a parent \(p=s\psi\), \(\|\psi\|=1\), has squared duplicated-parent error
\[
\|f_i-s\psi\|^2+\|f_j-s\psi\|^2
=q+2s^2-2s\langle\psi,S\rangle.
\]
Its normalized denominator \((R+s)^2\) is independent of \(\psi\). Thus the direction problem is exactly maximization of \(\langle\psi,S\rangle\).

Every nonzero realizable parent has nonzero input and output parameter vectors. Write their magnitudes as positive scalars and their directions as unit vectors \(u,v\). Positive homogeneity and the unit-function-norm constraint give the exhaustive parameterization
\[
\psi(x)=\frac{\Psi(u^\top\widetilde x)v}{\sqrt{K(u,u)}},
\qquad \|u\|=\|v\|=1,\quad K(u,u)>0.
\]
Conversely every such expression is realizable and has unit Hilbert norm. Define
\[
A(u)=\sum_{k\in\{i,j\}}K(u,\widetilde w_{\rm in}^k)w_{\rm out}^k.
\]
The expectation inner product gives
\[
\langle\psi,S\rangle=\frac{\langle v,A(u)\rangle}{\sqrt{K(u,u)}}.
\]
Cauchy–Schwarz maximizes this over unit \(v\) at \(A(u)/\|A(u)\|\) when \(A(u)\ne0\), with value
\[
M(u)=\frac{\|A(u)\|}{\sqrt{K(u,u)}}.
\]
When \(A(u)=0\), every unit \(v\) is optimal for that input direction.

We next prove attainment without falsely treating the positive-self-kernel set as compact. A scalar PH-1 activation has the form \(\Psi(z)=C_+z\) for \(z>0\), \(\Psi(z)=C_-z\) for \(z<0\), and \(\Psi(0)=0\). It is globally Lipschitz. Since the augmented Gaussian input has finite second moment, the activation map is continuous into scalar \(L^2\), so the kernel and \(M\) are continuous wherever \(K(u,u)>0\).

Write \(u=(r,b)\). If \(r\ne0\), then \(r^\top X+b\) has a nondegenerate Gaussian distribution with positive probability on both half-lines. Because the activation is nonzero, \(K(u,u)>0\). Hence a zero-self-kernel unit direction must have \(r=0\), \(b=\pm1\), and \(\Psi(b)=0\). Such a direction is possible only on the zero side of a one-sided activation.

Suppose feasible \(u_m\to u_0\) with \(K(u_0,u_0)=0\). Let
\[
B_m=\{x:\Psi(u_m^\top\widetilde x)\ne0\}.
\]
For every fixed \(x\), the preactivation tends to the nonzero constant \(b_0\) on the zero side, so \(\mathbf1_{B_m}(x)\to0\). For every unit output vector \(v\), Cauchy–Schwarz gives
\[
\left|\left\langle\frac{\Psi(u_m^\top\widetilde X)v}{\sqrt{K(u_m,u_m)}},S\right\rangle\right|
\le \|S\mathbf1_{B_m}\|_{\mathcal H}\longrightarrow0.
\]
The convergence follows by dominated convergence, since \(\|S(X)\|^2\) is integrable. Taking the maximum over \(v\) shows \(M(u_m)\to0\). Thus extending \(M\) by zero at zero-self-kernel directions makes it continuous on the compact unit sphere.

If \(S\ne0\), at least one child is nonzero and has positive inner product with \(S\), because
\[
\langle f_i,S\rangle+\langle f_j,S\rangle=\|S\|^2>0.
\]
Its normalized realizable direction gives a positive alignment. Therefore the maximum of the extended function is positive and cannot occur at a zero-self-kernel direction. It is attained at a feasible \(u^*\). If \(S=0\), the alignment objective is identically zero and any feasible unit input direction exists and is optimal. This also proves that zero maximum alignment is precisely the zero-child-sum case.

Substitution proves the stated magnitude-\(s\) parent formula, including its zero-alignment branch.

## 5. Correlated merge and the correct scale

Let the two children be nonzero, and write
\[
a=\|f_i\|,\quad b=\|f_j\|,\quad L=a+b,\quad q=a^2+b^2,
\quad B=\max_{\psi\in\mathcal N,\ \|\psi\|=1}\langle\psi,f_i+f_j\rangle.
\]
The maximum exists by Section 4. Comparing with the feasible directions \(f_i/a\) and \(f_j/b\) yields
\[
B\ge\max\{a+b\rho_{ij},\ b+a\rho_{ij}\}
\ge\frac{L(1+\rho_{ij})}{2}.
\]
Choose privately for this proof
\[
\rho^*(f_i,f_j)=\frac{2\sqrt{a^2+b^2}}{a+b}-1.
\]
Since \(L^2/2\le q<L^2\), this threshold lies in \((0,1)\). If \(\rho_{ij}\ge\rho^*\), then \(B\ge\sqrt q>0\).

At every positive scale an optimal direction achieves \(B\). The normalized squared objective is therefore
\[
Q(s)=\frac{2s^2-2Bs+q}{(R+s)^2}.
\]
Direct differentiation gives
\[
Q'(s)=\frac{2((2R+B)s-(BR+q))}{(R+s)^3}.
\]
Consequently it has a unique global minimizer on \(s>0\),
\[
s_* = \frac{q+BR}{2R+B}>0.
\]
Because \(q\le B^2\), we have \(s_*\le B\). Also \(B\le L\); the strict inequality \(q<L^2\) implies \(s_*<L\). Thus the source's scale property is derived in the correlated regime, not imposed by restricting the optimization domain.

Every optimal parent is \(f_p=s_*\psi\) with \(\langle\psi,S\rangle=B\). Along the duplicated-parent path,
\[
\begin{aligned}
E(\Phi(t))-R
&=\|(1-t)f_i+tf_p\|+\|(1-t)f_j+tf_p\|\\
&\ge\langle\psi,(1-t)(f_i+f_j)+2tf_p\rangle\\
&=(1-t)B+2ts_*\\
&\ge s_*.
\end{aligned}
\]
Hence \(E(\Phi(t))\ge R+s_*=E(\Phi_b)\) for every \(t\in[0,1]\). The threshold depends only on the child norms and works for every \(R\ge0\) and every optimal parent. Combining with Section 3 proves the projection-cost claim.

## Auxiliary dependency audit

The angular-kernel propositions are not needed for the exact affine-parent theorem. Their rotationally invariant reference vector is not the deterministically augmented vector \((X,1)\). In their own setting, homogeneity and an orthogonal change of variables prove angular separability.

For completeness, their Gaussian boundary identity can be checked without an unexpanded specialized citation. Let \(X,Z\) be independent standard normal variables and \(Y_\rho=\rho X+\sqrt{1-\rho^2}Z\). Identical marginals imply
\[
2(k(1)-k(\rho))=\mathbb E[(\Psi(X)-\Psi(Y_\rho))^2].
\]
As \(\rho\uparrow1\), the difference divided by \(\sqrt{2(1-\rho)}\) converges almost surely to \(-\Psi'(X)Z\). The Lipschitz bound supplies an integrable squared dominator proportional to \(X^2+Z^2\). Thus
\[
k'(1-)=\mathbb E[\Psi'(X)^2]=\tfrac12(C_+^2+C_-^2)
=\mathbb E[\Psi(X)^2]=k(1).
\]
Nontriviality gives \(k(1)>0\). This does not assert that the affine self-kernel is positive on the entire augmented unit sphere.
