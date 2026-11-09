# Reference Proof

## Proof Structure

Construct a normalized snapshot latent-variable model with the prescribed decoder. Restrict its marginal integral to the conditional snapshot support before applying Jensen, and justify the finite parameter-independent constant. Prove the snapshot and path cross-entropy decompositions separately in the extended reals. Subtract only when the difference is defined. Establish the entropy comparison from conditional expectation and entropy concavity, then prove minimizer calibration using KL nonnegativity and representability.

## Complete Proof

### Snapshot Model and Bound

Let \(\lambda\) be counting measure on \(V\) times Lebesgue measure on \([0,1]\). For \(s=(y,t)\), define
\[
a_x(s)=K_t(y,x),\qquad b(s)=\sum_{z\in V}p_0(z)a_z(s)=q_t(y).
\]
The conditional snapshot law given \(X_0=x\) has density \(a_x\), and the snapshot marginal law \(\pi_S\) has density \(b\), both relative to \(\lambda\).

Define
\[
p_\theta^{\rm snap}(x,ds)=\pi_S(ds)\mu_\theta(s)_x,
\qquad
m_\theta(x)=p_\theta^{\rm snap}(x)=\int b(s)\mu_\theta(s)_x\,\lambda(ds).
\]
Measurability makes these integrals defined. Their integrands are nonnegative, and
\[
\sum_{x\in V}m_\theta(x)
=\int b(s)\sum_{x\in V}\mu_\theta(s)_x\,\lambda(ds)=1.
\]
Thus this is a probability model with a parameter-independent latent law and the prescribed decoder. On a \(\pi_S\)-null set the decoder version is immaterial.

Fix \(x\) with \(p_0(x)>0\). Under the conditional snapshot law, \(a_x(S)>0\) almost surely, and \(b(S)\ge p_0(x)a_x(S)>0\). Set
\[
Y_x(S)=\frac{b(S)\mu_\theta(S)_x}{a_x(S)}.
\]
The support restriction gives
\[
\mathbb E_{S\mid X_0=x}Y_x(S)
=\int_{\{a_x>0\}}b(s)\mu_\theta(s)_x\,\lambda(ds)
\le m_\theta(x)\le1.
\]
In particular, equality with the full marginal is not needed and need not hold.

The relevant logarithmic Jensen statement is: if \(Y\ge0\) has finite expectation, then \(\mathbb E\log Y\le\log\mathbb EY\), with \(\log0=-\infty\). For positive expectation this follows by applying ordinary Jensen to \(\log(Y+\varepsilon)\) and letting \(\varepsilon\downarrow0\); the positive logarithmic part is integrable because \(\log^+Y\le Y\). If the expectation is zero, \(Y=0\) almost surely and both sides are \(-\infty\). The verified bound above supplies the finite-expectation hypothesis. Consequently,
\[
\log m_\theta(x)
\ge\log\mathbb E_{S\mid X_0=x}Y_x(S)
\ge\mathbb E_{S\mid X_0=x}\log Y_x(S).
\]

We next justify the likelihood-ratio constant and all logarithmic expectations used here. Bayes' formula gives, on the sampled joint support,
\[
r_S(x)=\frac{p_0(x)a_x(S)}{b(S)},
\qquad
\log\frac{b(S)}{a_{X_0}(S)}
=\log p_0(X_0)-\log r_S(X_0).
\]
The sampled posterior coordinate is positive almost surely: conditioning on \(S\), the probability assigned to coordinates with \(r_S(x)=0\) is zero. Moreover,
\[
\mathbb E[-\log r_S(X_0)]
=\mathbb E\left[-\sum_xr_S(x)\log r_S(x)\right]
=H(X_0\mid S)\le\log|V|,
\]
and \(\mathbb E[-\log p_0(X_0)]=H(X_0)\le\log|V|\). These entropy bounds follow from finite-alphabet KL nonnegativity relative to the uniform distribution, proved below. Thus the likelihood-ratio logarithm is integrable. Since \(V\) is finite, it is also integrable conditional on each \(x\) with \(p_0(x)>0\).

It follows that
\[
\mathbb E_{S\mid X_0=x}\log Y_x(S)
=-\mathbb E[-\log\mu_\theta(S)_x\mid X_0=x]
+\mathbb E\left[\log\frac{b(S)}{a_x(S)}\mid X_0=x\right],
\]
including when the conditional loss is infinite. Average the conditional bound over the support of \(p_0\). Terms outside that support are not included. We obtain
\[
\mathbb E\log p_\theta^{\rm snap}(X_0)
\ge-L_{\rm snap}(\theta)+C,
\]
where
\[
C=\mathbb E\log\frac{b(S)}{a_{X_0}(S)}
=H(X_0\mid S)-H(X_0).
\]
This is a finite real constant depending only on the fixed data and forward observation law, not on \(\theta\). If \(L_{\rm snap}=+\infty\), the claimed lower bound has right-hand side \(-\infty\) and remains valid.

### KL and Cross-Entropy

For probability vectors \(r,p\), if \(p_x=0<r_x\) for some \(x\), both the cross-entropy and \(\operatorname{KL}(r\|p)\) are infinite. Otherwise the finite sum over \(\{x:r_x>0\}\) gives
\[
\sum_xr_x(-\log p_x)
=-\sum_xr_x\log r_x+\operatorname{KL}(r\|p).
\]
This establishes the identity in all cases with the conventions in the task.

For completeness, when KL is finite, \(\log u\le u-1\) gives
\[
-\operatorname{KL}(r\|p)
=\sum_{r_x>0}r_x\log\frac{p_x}{r_x}
\le\sum_{r_x>0}(p_x-r_x)\le0.
\]
Hence KL is nonnegative, also in the infinite case. Equality requires \(p_x/r_x=1\) for every positive \(r_x\), and then normalization requires zero mass elsewhere. Thus KL is zero exactly when \(p=r\). Applying this inequality to the uniform vector gives \(-\sum_xr_x\log r_x\le\log|V|\); entropy is nonnegative term by term.

For either observation \(U=S\) or \(U=\Omega\), and its corresponding measurable predictor \(p_\theta(U)\), conditioning the nonnegative loss on \(U\) gives
\[
\mathbb E[-\log p_\theta(U)_{X_0}]
=\mathbb E_U\sum_xr_U(x)(-\log p_\theta(U)_x).
\]
This conditioning identity remains valid for infinite expectations, by truncation of the nonnegative loss. Apply the pointwise cross-entropy identity and average. The entropy term is bounded and finite, and the KL term is nonnegative, so no undefined subtraction is involved. This proves
\[
L_{\rm snap}=H(X_0\mid S)+\mathbb E_S\operatorname{KL}(r_S\|\mu_\theta(S)),
\]
\[
L_{\rm path}=H(X_0\mid\Omega)+\mathbb E_\Omega\operatorname{KL}(r_\Omega\|\rho_\theta(\Omega)).
\]
Here \(L_{\rm path}\) is precisely the clean-token conditional NLL defined in the task; it is not the separate eventwise reverse-jump objective.

### Loss Difference and Entropy Comparison

Because each conditional entropy is finite, a loss is finite exactly when its expected KL term is finite. If both losses are finite, ordinary subtraction gives the required identity. If only the snapshot loss is finite, both the loss difference and the calibration difference are \(-\infty\). If only the path loss is finite, both differences are \(+\infty\). Adding the finite entropy difference is legitimate in each case. No identity involving a difference is asserted when both losses are infinite.

Since \(S\) is a measurable function of \(\Omega\), the tower property gives, coordinatewise,
\[
r_S(x)=\mathbb E[r_\Omega(x)\mid S].
\]
The function \(h(r)=-\sum_xr_x\log r_x\) is continuous and concave on the finite simplex: each summand \(-u\log u\) is concave on \((0,1]\) and has its continuous value zero at zero. Conditional Jensen therefore yields
\[
h(r_S)\ge\mathbb E[h(r_\Omega)\mid S].
\]
All terms are bounded by \(\log|V|\). Taking expectations proves
\[
H(X_0\mid S)-H(X_0\mid\Omega)\ge0.
\]
This explicitly establishes the finite-alphabet data-processing statement needed here, with its measurable-map hypothesis verified by the setup.

### Calibration of Every Minimizer

Suppose some \(\theta_*\) satisfies \(\mu_{\theta_*}(S)=r_S\) almost surely. Its expected snapshot KL is zero, so
\[
L_{\rm snap}(\theta_*)=H(X_0\mid S)\le\log|V|.
\]
The snapshot decomposition and KL nonnegativity show that this is the global minimum. Every global minimizer therefore has finite risk and zero expected snapshot KL. A nonnegative random variable with expectation zero vanishes almost surely. The equality characterization of KL then gives \(\mu_\theta(S)=r_S\) almost surely for every minimizer.

## Audit Closure

Model construction, normalization, the support-correct Jensen step, constant integrability, both extended-real decompositions, subtraction cases, the entropy comparison, and minimizer calibration are explicitly established above. No unresolved private proof obligation remains.
