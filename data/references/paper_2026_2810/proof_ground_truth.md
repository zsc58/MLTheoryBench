# Reference Proof

## Proof Structure

1. Identify the boundary conditional velocity law from independence, with the appropriate almost-everywhere interpretation.
2. Prove common-translation invariance of quadratic Wasserstein distance and obtain the exact surrogate reduction.
3. Apply the stated compression assumption.
4. Prove the Wasserstein second-moment inequality, apply it at each boundary condition, and integrate using the source's scalar moment argument.

## Complete Proof

Write \(\gamma=N(0,I_d)\), and for \(x\in\mathbb R^d\) define
\[
\nu_x=\operatorname{Law}(X_1-x),\qquad
\widetilde\nu_x=\operatorname{Law}(\widetilde X_1-x).
\]
Both measures have finite second moments. At \(t=0\), \(X_t=X_0\) and \(V=X_1-X_0\). Independence implies that \(x\mapsto\nu_x\) is a version of the conditional law of \(V\) given \(X_0=x\). Indeed, for Borel sets \(A,B\), independence and integration under the product law give
\[
\Pr(X_0\in A,V\in B)
=\int_A\int \mathbf 1_B(y-x)\,\rho_1(dy)\,\rho_0(dx)
=\int_A\nu_x(B)\,\rho_0(dx).
\]
Thus \(\pi(\cdot\mid x,0)=\nu_x\) for \(\rho_0\)-almost every \(x\). This is sufficient for every expectation defining \(D\); alternatively, choose this explicit conditional version everywhere.

### Translation invariance and well-definedness

For any coupling of two probability measures \(\mu,\nu\in\mathcal P_2(\mathbb R^d)\), translating both coordinates by the same vector preserves the squared Euclidean transport cost. Translating back gives the inverse correspondence between couplings. Taking infima in both directions therefore proves
\[
W_2(\operatorname{Law}(U-x),\operatorname{Law}(W-x))=W_2(\mu,\nu),
\]
where \(U\sim\mu\) and \(W\sim\nu\).

The kernels \(x\mapsto\nu_x\) and \(x\mapsto\widetilde\nu_x\) are measurable. More explicitly, coupling the same endpoint variable at two different translations gives
\[
W_2(\nu_x,\nu_{x'})\le\|x-x'\|,
\qquad
W_2(\widetilde\nu_x,\widetilde\nu_{x'})\le\|x-x'\|.
\]
By the triangle inequality for the Wasserstein metric, the distances used below are measurable functions of \(x\). The exact surrogate reduction below makes its cost finite. For the Gaussian source, let \(Z\sim\gamma\) be independent of \((X_0,X_1)\). The product coupling at each fixed \(x\) gives
\[
\mathbb E_{X_0}W_2^2(\gamma,\nu_{X_0})
\le \mathbb E\|Z-X_1+X_0\|^2
=2d+\mathbb E\|X_1\|^2<\infty.
\]
Here all cross terms vanish by independence and the zero means of \(Z\) and \(X_0\).

### Surrogate source

By definition, \(Q_S(\cdot\mid x,0)=\widetilde\nu_x\). Common-translation invariance gives, for \(\rho_0\)-almost every \(x\),
\[
W_2^2\bigl(Q_S(\cdot\mid x,0),\pi(\cdot\mid x,0)\bigr)
=W_2^2(\widetilde\rho_1,\rho_1).
\]
The right-hand side is independent of \(x\). Taking the expectation and the nonnegative square root yields
\[
D(Q_S)=W_2(\rho_1,\widetilde\rho_1).
\]
The stated compression assumption now gives
\[
D(Q_S)\le C_QK^{-1/d}.
\]
No quantization theorem or guarantee for a surrogate-fitting algorithm is needed: the approximation rate is an explicit premise.

### Gaussian source

First, for \(\mu,\nu\in\mathcal P_2(\mathbb R^d)\), set \(m_2(\mu)=\int\|u\|^2\mu(du)\). For any coupling \((U,W)\) of \(\mu,\nu\), the reverse triangle inequality in \(L^2\) gives
\[
\left(\mathbb E\|U-W\|^2\right)^{1/2}
\ge\left|\sqrt{m_2(\mu)}-\sqrt{m_2(\nu)}\right|.
\]
Squaring and taking the infimum over couplings proves
\[
W_2^2(\mu,\nu)
\ge\left(\sqrt{m_2(\mu)}-\sqrt{m_2(\nu)}\right)^2.
\]

Define the nonnegative function
\[
S(x)=\left(\mathbb E_{X_1}\|X_1-x\|^2\right)^{1/2}.
\]
It is finite and measurable: writing \(m=\mathbb E X_1\), which exists by the finite second moment,
\[
S(x)^2=\mathbb E\|X_1\|^2-2\langle m,x\rangle+\|x\|^2.
\]
Since \(m_2(\gamma)=d\), the moment inequality at fixed \(x\) gives
\[
W_2^2(\gamma,\nu_x)\ge(\sqrt d-S(x))^2.
\]
Independence and \(\mathbb E X_0=0\) imply
\[
\mathbb E S(X_0)^2
=\mathbb E\|X_1-X_0\|^2
=\mathbb E\|X_1\|^2+d
=d(\sigma_1^2+1).
\]
In particular, \(S(X_0)\) is integrable, and Jensen's inequality gives
\[
\mathbb E S(X_0)\le\sqrt{\mathbb E S(X_0)^2}
=\sqrt{d(\sigma_1^2+1)}.
\]
Integrating the fixed-condition lower bound and expanding the square therefore yields
\[
\begin{aligned}
D(Q_G)^2
&\ge\mathbb E(\sqrt d-S(X_0))^2\\
&=d-2\sqrt d\,\mathbb E S(X_0)+\mathbb E S(X_0)^2\\
&\ge d-2\sqrt d\sqrt{d(\sigma_1^2+1)}+d(\sigma_1^2+1)\\
&=d\bigl(\sqrt{\sigma_1^2+1}-1\bigr)^2.
\end{aligned}
\]
The substitution uses the negative coefficient of \(\mathbb E S(X_0)\), so the inequality direction is preserved. Since \(\sigma_1^2\ge0\), taking nonnegative square roots proves
\[
D(Q_G)\ge\sqrt d\,\bigl(\sqrt{\sigma_1^2+1}-1\bigr).
\]
This includes \(\sigma_1^2=0\), when the asserted lower bound is zero. No nondegeneracy assumption is required. Both conclusions follow.
