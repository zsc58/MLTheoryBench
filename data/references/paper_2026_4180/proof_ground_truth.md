# Reference Proof

## Contract and obligations

All dual trajectories under consideration are Lipschitz. Uniqueness is asserted in that class, not among arbitrary a.e.-differentiable functions. The primal accumulation conclusion concerns a single sequence of trajectories converging almost everywhere on a fixed interval.

The proof must establish: the rescaled equations; a valid quadratic transformation including reconstruction when the matrix is singular; existence and uniqueness of the limiting dual flow; Mosco convergence with an explicit moving-translation recovery argument; the hypotheses of evolutionary convergence; weighted gradient and loss convergence; instantaneous minimization; and the accumulation conclusion with its stated quantifiers.

## Standard independent background

We use the following standard results in the forms stated or invoked in the source.

1. **Convex calculus.** If \(f\in\Gamma_0(\mathbb R^d)\), \(A\) is linear, and \((a+\operatorname{Range}A)\cap\operatorname{ri}\operatorname{dom}f\ne\varnothing\), then
   \[
   \partial[f(a+A\cdot)](u)=A^\top\partial f(a+Au).
   \]
   Subtracting a linear function subtracts its coefficient from the subdifferential. Also, \(w\in\partial g(x)\) if and only if \(x\in\partial g^*(w)\), and a finite convex function on the whole space has a nonempty subdifferential everywhere. A proper convex function is continuous relative to the relative interior of its domain. These are the independent convex-calculus facts invoked in the source's chain rule and translation argument.
2. **Subgradient-flow existence and minimal norm.** For \(F\in\Gamma_0\) and \(u_0\in\operatorname{dom}\partial F\), there is a unique Lipschitz solution of \(\dot u+\partial F(u)\ni0\) with initial value \(u_0\). Almost everywhere, \(-\dot u\) is the element of minimum Euclidean norm in \(\partial F(u)\). This is theory_009.
3. **Evolutionary convergence.** Suppose \(F_\varepsilon,F\in\Gamma_0\), \(F_\varepsilon\) Mosco-converges to \(F\), \(u_{0,\varepsilon}\in\operatorname{dom}\partial F_\varepsilon\), \(u_0\in\operatorname{dom}\partial F\), and \(u_{0,\varepsilon}\to u_0\). The corresponding Lipschitz solutions converge uniformly on every finite interval, and their derivatives converge in \(L^2([0,S],s\,ds)\). This is theory_011.

Here Mosco convergence in finite dimensions means the liminf inequality along every convergent sequence and, at every target point, the existence of a convergent recovery sequence satisfying the limsup inequality. The paper-specific transformed-energy convergence and minimization properties are proved below, not assumed as external results.

## 1. Rescaling and the singular-matrix transformation

Put
\[
A=M^{1/2},\qquad B=(M^\dagger)^{1/2},\qquad b=Bq,\qquad R=\operatorname{Span}M.
\]
The square roots are the positive semidefinite square roots and \(M^\dagger\) is the Moore–Penrose pseudoinverse. Spectral calculus gives
\[
AB=BA=P_R,\qquad BM=A,\qquad Ab=q,
\]
where \(P_R\) is orthogonal projection onto \(R\). These identities remain valid when \(M=0\).

Write
\[
\eta_\varepsilon=\mu_\varepsilon^{-1},\qquad
 g_\varepsilon=\eta_\varepsilon h,\qquad
 a_\varepsilon=\bar w_0^\varepsilon,\qquad a=\bar w_0.
\]
All these quantities are used only for sufficiently small \(\varepsilon\), when \(\mu_\varepsilon>0\). Differentiating the rescaled dual variable and scaling the subdifferential gives
\[
\dot{\bar w}^{\varepsilon}=-(M\bar x^\varepsilon-q),\qquad
\bar w^\varepsilon\in\partial g_\varepsilon(\bar x^\varepsilon)
\]
almost everywhere.

We record the transformation carefully. Let \((w,x)\) be a Lipschitz dual mirror flow for a potential \(g\), initialized at \(a_g\). Since \(\dot w\in R\) almost everywhere, absolute continuity implies
\[
w(t)-a_g\in R\quad\text{for every }t.
\]
Consequently, defining \(u=B(w-a_g)\) gives the actual reconstruction
\[
w=a_g+Au.
\]
This reconstruction is essential when \(M\) is singular; it cannot be inferred from the definition of \(u\) for an arbitrary trajectory.

If \(a_g\in\operatorname{ri}\operatorname{dom}g^*+R\), the qualified chain rule gives, for
\[
F_g(u)=g^*(a_g+Au)-\langle b,u\rangle,
\]
that
\[
\partial F_g(u)=A\partial g^*(a_g+Au)-b.
\]
Fenchel subgradient inversion and the mirror equation therefore yield
\[
\dot u=-(Ax-b)\in-\partial F_g(u),\qquad u(0)=0.
\]

Conversely, let \(u\) be a Lipschitz solution of this inclusion with \(u(0)=0\), and define \(w=a_g+Au\). The subdifferential formula provides, almost everywhere, an \(x\in\partial g^*(w)\) with
\[
-\dot u=Ax-b.
\]
It follows that \(\dot w=-Mx+q\) and \(w\in\partial g(x)\). Values of the primal variable on the exceptional null set can be assigned arbitrarily. Also \(\partial F_g(u)\subset R\), so \(u(t)\in R\), consistently with the inverse transformation.

For the finite-parameter flow this produces
\[
F_\varepsilon(u)=g_\varepsilon^*(a_\varepsilon+Au)-\langle b,u\rangle,
\qquad
u^\varepsilon=B(\bar w^\varepsilon-a_\varepsilon).
\]
In the rest of the proof denote this transformed trajectory by \(u^\varepsilon\), so
\[
\dot u^\varepsilon+\partial F_\varepsilon(u^\varepsilon)\ni0,
\qquad u^\varepsilon(0)=0,
\qquad \bar w^\varepsilon=a_\varepsilon+Au^\varepsilon.
\]
The chain-rule qualification holds because
\(g_\varepsilon^*(v)=\eta_\varepsilon h^*(v/\eta_\varepsilon)\) is finite everywhere.

## 2. Limiting existence, uniqueness, and minimization

For the limiting potential \(g=\iota_C\), define
\[
F(u)=\sigma_C(a+Au)-\langle b,u\rangle.
\]
The assumption \(a\in\operatorname{ri}\operatorname{dom}\sigma_C+R\) verifies the chain-rule qualification, and \(a\in\operatorname{dom}\partial\sigma_C\) implies
\[
\partial F(0)=A\partial\sigma_C(a)-b\ne\varnothing.
\]
Thus \(F\in\Gamma_0\), \(0\in\operatorname{dom}\partial F\), and the standard existence theorem supplies a unique Lipschitz solution \(u\) with \(u(0)=0\). Reconstruction gives a Lipschitz limiting mirror-flow dual trajectory
\[
\bar w=a+Au.
\]
Any other Lipschitz dual solution has its displacement in \(R\), transforms to the same subgradient flow with initial value zero, and reconstructs to the same \(\bar w\). This proves uniqueness in the required class and existence of an associated primal variable.

For any associated primal variable \(\bar x\), almost everywhere
\[
\bar x\in\partial\sigma_C(\bar w),\qquad
A\bar x-b=-\dot u.
\]
The latter vector is the minimum-norm element of
\(\partial F(u)=A\partial\sigma_C(\bar w)-b\). For every \(y\in\mathbb R^d\),
\[
\|Ay-b\|^2
=\langle y,My\rangle-2\langle q,y\rangle+\langle q,M^\dagger q\rangle
=2\ell(y)-2c+\langle q,M^\dagger q\rangle.
\]
Minimizing this norm over \(y\in\partial\sigma_C(\bar w)\) is therefore equivalent to minimizing \(\ell(y)\). Hence, almost everywhere,
\[
\bar x(s)\in\operatorname*{Argmin}_{y\in\partial\sigma_C(\bar w(s))}\ell(y).
\]
This derives the paper-specific minimization property. It also shows that all associated primal variables have the same loss and gradient almost everywhere.

## 3. Mosco convergence of the moving energies

Because \(h^*(0)<\infty\),
\[
m:=\inf h=-h^*(0)>-\infty.
\]
First, \(g_\varepsilon=\eta_\varepsilon h\) Mosco-converges to \(\iota_C\): outside the closed set \(C\), convergent sequences are eventually outside \(C\); inside \(C\), the lower bound \(\eta_\varepsilon m\to0\) gives the liminf inequality, and constant sequences give recovery because \(h\) is finite on \(C\).

The moving affine composition requires an additional argument. Set
\[
\Psi_\varepsilon(u)=g_\varepsilon^*(a_\varepsilon+Au),\qquad
\Psi(u)=\sigma_C(a+Au).
\]
We prove both Mosco inequalities explicitly. This is a direct version of the source's relative-interior translation argument and lower-bound estimate; no paper-specific convergence lemma is being assumed.

For every \(v\in\mathbb R^d\) and \(z\in C\), the conjugate supremum formula and \(h\ge m\) give
\[
\langle v,z\rangle-\eta_\varepsilon h(z)
\le g_\varepsilon^*(v)
\le\sigma_C(v)-\eta_\varepsilon m.
\]
If \(u_\varepsilon\to u\), the first inequality gives, for each fixed \(z\in C\),
\[
\liminf_{\varepsilon\to0}\Psi_\varepsilon(u_\varepsilon)
\ge\langle a+Au,z\rangle.
\]
Taking the supremum over \(z\in C\) proves the liminf inequality, including the case \(\Psi(u)=+\infty\).

For recovery, only \(\Psi(u)<\infty\) needs consideration. Write
\[
D=\operatorname{dom}\sigma_C,\qquad
\delta_\varepsilon=a_\varepsilon-a.
\]
The set \(D\) is a convex cone containing zero, so \(\operatorname{aff}D\) is a linear subspace. Choose \(v\) such that
\[
r:=a+Av\in\operatorname{ri}D,
\]
which is possible by the relative-interior assumption. Choose, for example,
\[
t_\varepsilon=\sqrt{\|\delta_\varepsilon\|}+\varepsilon.
\]
For sufficiently small \(\varepsilon\), \(0<t_\varepsilon<1\), \(t_\varepsilon\to0\), and \(\delta_\varepsilon/t_\varepsilon\to0\). This choice also handles identically zero translation errors. Since \(\delta_\varepsilon\in\operatorname{aff}D\),
\[
r_\varepsilon=r+\delta_\varepsilon/t_\varepsilon
\]
belongs to \(\operatorname{ri}D\) for sufficiently small \(\varepsilon\), and relative continuity yields \(\sigma_C(r_\varepsilon)\to\sigma_C(r)\).

Define the recovery sequence
\[
u_\varepsilon=(1-t_\varepsilon)u+t_\varepsilon v.
\]
Then \(u_\varepsilon\to u\), and
\[
a_\varepsilon+Au_\varepsilon
=(1-t_\varepsilon)(a+Au)+t_\varepsilon r_\varepsilon.
\]
Convexity and the upper bound for \(g_\varepsilon^*\) imply
\[
\Psi_\varepsilon(u_\varepsilon)
\le(1-t_\varepsilon)\sigma_C(a+Au)
+t_\varepsilon\sigma_C(r_\varepsilon)-\eta_\varepsilon m.
\]
Taking the limsup proves the recovery inequality. At targets where \(\Psi(u)=+\infty\), the constant sequence suffices for the limsup requirement.

Thus \(\Psi_\varepsilon\) Mosco-converges to \(\Psi\). Subtracting the fixed continuous linear function \(\langle b,u\rangle\) preserves both inequalities, so
\[
F_\varepsilon\xrightarrow{M}F.
\]

## 4. Evolutionary convergence and the two observables

Every \(F_\varepsilon\) is finite, convex, and continuous, so it belongs to \(\Gamma_0\). More explicitly, the chain rule and everywhere-finite \(g_\varepsilon^*\) give
\[
\partial F_\varepsilon(0)=A\partial g_\varepsilon^*(a_\varepsilon)-b\ne\varnothing.
\]
The limiting initial-domain condition was checked in Section 2. All transformed initial points equal zero. The hypotheses of the standard evolutionary-convergence theorem are therefore verified, and, for every \(S>0\),
\[
u^\varepsilon\to u\quad\text{uniformly on }[0,S],
\qquad
\int_0^S s\,\|\dot u^\varepsilon-\dot u\|^2\,ds\to0.
\]
Here and below \(u^\varepsilon\) denotes the transformed trajectory defined in Section 1. Reconstruction and \(a_\varepsilon\to a\) give
\[
\bar w^\varepsilon=a_\varepsilon+Au^\varepsilon\to a+Au=\bar w
\]
uniformly on \([0,S]\).

Moreover,
\[
\nabla\ell(\bar x^\varepsilon)=-A\dot u^\varepsilon,
\qquad
\nabla\ell(\bar x)=-A\dot u.
\]
Multiplication by the fixed matrix \(A\) proves the asserted weighted \(L^2\) gradient convergence.

The quadratic identity from Section 2 gives
\[
\|\dot u^\varepsilon\|^2=2\ell(\bar x^\varepsilon)-2c+\langle q,M^\dagger q\rangle,
\qquad
\|\dot u\|^2=2\ell(\bar x)-2c+\langle q,M^\dagger q\rangle.
\]
Writing \(\|\cdot\|_{2,s}\) for the \(L^2([0,S],s\,ds)\) norm, Cauchy–Schwarz therefore yields
\[
\int_0^S s\,|\ell(\bar x^\varepsilon)-\ell(\bar x)|\,ds
\le\tfrac12\|\dot u^\varepsilon-\dot u\|_{2,s}
\bigl(\|\dot u^\varepsilon\|_{2,s}+\|\dot u\|_{2,s}\bigr)\to0.
\]
No additional energy-convergence theorem is required. The observables are measurable up to null sets because these formulas express them in terms of derivatives of Lipschitz trajectories. No uniqueness or continuity of the primal variable is needed.

## 5. Accumulation functions

Fix \(S>0\), a sequence \(\varepsilon_k\to0\), and a function \(\bar y\) such that
\[
\bar x^{\varepsilon_k}(s)\to\bar y(s)
\quad\text{for almost every }s\in[0,S].
\]
Remove the null set where this convergence fails, together with the countable union of the exceptional sets for the mirror relations along this sequence. At every remaining time, put \(x_k=\bar x^{\varepsilon_k}(s)\). Then \(x_k\in C\), so closedness gives \(\bar y(s)\in C\). For every \(z\in C\), the scaled subgradient inequality gives
\[
\langle\bar w^{\varepsilon_k}(s),z-x_k\rangle
\le\eta_{\varepsilon_k}\bigl(h(z)-h(x_k)\bigr)
\le\eta_{\varepsilon_k}\bigl(h(z)-m\bigr).
\]
Uniform dual convergence and pointwise primal convergence imply
\[
\langle\bar w(s),z-\bar y(s)\rangle\le0
\quad\text{for every }z\in C.
\]
Thus \(\bar w(s)\in\partial\iota_C(\bar y(s))\), equivalently
\(\bar y(s)\in\partial\sigma_C(\bar w(s))\). This directly proves the graph-limit step needed here.

Continuity of \(\ell\) gives \(\ell(\bar x^{\varepsilon_k})\to\ell(\bar y)\) almost everywhere. Section 4 gives convergence to \(\ell(\bar x)\) in weighted \(L^1\), hence in measure for the finite measure \(s\,ds\). Almost-everywhere convergence also implies convergence in that measure, whose limit is unique. Therefore
\[
\ell(\bar y(s))=\ell(\bar x(s))
\]
for almost every \(s\). The measures \(s\,ds\) and Lebesgue measure have the same null sets on \((0,S]\), and the singleton endpoint is irrelevant. Combining this equality with membership and the minimization property proves the requested argmin inclusion.

The exceptional set may depend on the sequence and accumulation function. The proof does not assert a stronger conclusion for independently chosen pointwise subsequences. All obligations are closed, including singular and zero \(M\).
