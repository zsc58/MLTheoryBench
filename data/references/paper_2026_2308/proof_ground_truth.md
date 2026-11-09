# Reference Proof

## Proof Structure and Obligations

First check evidence normalization and the posterior conventions. Separate the extended-real cases before subtracting any utilities or suprema. In the finite-envelope case, prove integrability of the centered likelihood functionals, rewrite each evidence-weighted IPM as their supremum, compare the suprema, apply the growth-profile bound, and control the evidence difference by the integrated likelihood difference. These steps close all obligations; no specialized external result is required.

## Complete Proof

All products of nonnegative extended quantities use the convention specified in the task.

### 1. Evidence normalization and exceptional sets

Joint measurability, nonnegativity, and likelihood normalization allow Tonelli's theorem to give
\[
\int_Y z(y)\,\nu(dy)=\int_X\int_Y\ell(y\mid x)\,\nu(dy)\,\mu(dx)=1,
\qquad
\int_Y\widetilde z(y)\,\nu(dy)=1.
\]
Thus both evidences are finite outside a measurable \(\nu\)-null set. When \(z(y)=0\), nonnegativity implies \(\ell(y\mid x)=0\) for \(\mu\)-almost every \(x\); the analogous assertion holds for the other likelihood. The posterior convention assigns \(\mu\) outside finite positive evidence, so its IPM from \(\mu\) is zero there. Consequently the corresponding evidence-weighted contribution is zero, including at infinite evidence under the stated product convention. Null-set modifications of these integrands do not affect the utilities.

Let
\[
R=\int_Y\int_X(\omega(x)+\bar\omega)
 |\ell(y\mid x)-\widetilde\ell(y\mid x)|\,\mu(dx)\,\nu(dy).
\]
The public assumptions make this a nonnegative extended integral and ensure that \(|U_{\mathcal F}-\widetilde U_{\mathcal F}|\) is defined.

### 2. Extended-real cases

If \(R=\infty\), the requested inequality is immediate.

Suppose \(R<\infty\) and \(\bar\omega=\infty\). Wherever the two likelihoods differ, the integrand defining \(R\) is infinite. Its finite integral therefore implies
\[
\ell(y\mid x)=\widetilde\ell(y\mid x)
\quad\text{for }(\nu\otimes\mu)\text{-almost every }(y,x).
\]
Tonelli applied to the indicator of the disagreement set shows that, for \(\nu\)-almost every \(y\), the likelihood slices agree \(\mu\)-almost everywhere. The evidences and the posterior probability measures then agree for almost every observation. Hence the utilities are equal. Since at least one is finite, both are finite and their difference is zero. This proves the bound in this case as well.

It remains to consider \(\bar\omega<\infty\).

### 3. Integrability and the centered-functional identity

Define
\[
b(y)=\int_X\omega(x)\ell(y\mid x)\,\mu(dx),
\qquad
\widetilde b(y)=\int_X\omega(x)\widetilde\ell(y\mid x)\,\mu(dx).
\]
Tonelli and normalization give
\[
\int_Y b(y)\,\nu(dy)=\int_Y\widetilde b(y)\,\nu(dy)=\bar\omega.
\]
Thus \(z,\widetilde z,b,\widetilde b\) are finite on a common measurable set of full \(\nu\)-measure. On this set, for every \(f\in\mathcal F\), the following integrals are absolutely convergent:
\[
A_f(y)=\int_X f(x)(z(y)-\ell(y\mid x))\,\mu(dx),
\qquad
\widetilde A_f(y)=\int_X f(x)(\widetilde z(y)-\widetilde\ell(y\mid x))\,\mu(dx).
\]
Indeed, \(|f|\leq\omega\), so their absolute values are bounded by \(z(y)\bar\omega+b(y)\) and \(\widetilde z(y)\bar\omega+\widetilde b(y)\), respectively.

At positive evidence, substitution of the posterior density yields
\[
z(y)\gamma_{\mathcal F}(\mu,\mu^y)=\sup_{f\in\mathcal F}|A_f(y)|.
\]
At zero evidence, the likelihood slice vanishes \(\mu\)-almost everywhere and both sides are zero. The analogous identity holds for the other likelihood. Put
\[
S(y)=\sup_{f\in\mathcal F}|A_f(y)|,
\qquad
\widetilde S(y)=\sup_{f\in\mathcal F}|\widetilde A_f(y)|
\]
on the full-measure set, and set both to zero off it. The utility-map measurability assumptions and the identities make these measurable. Moreover,
\[
S(y)\leq z(y)\bar\omega+b(y),
\qquad
\widetilde S(y)\leq\widetilde z(y)\bar\omega+\widetilde b(y).
\]
Integration gives
\[
U_{\mathcal F}=\int_Y S\,d\nu\leq2\bar\omega,
\qquad
\widetilde U_{\mathcal F}=\int_Y\widetilde S\,d\nu\leq2\bar\omega.
\]
All utility and pointwise supremum subtractions used below are therefore legitimate almost everywhere.

### 4. Uniform comparison and evidence control

Write
\[
\Delta(y,x)=\ell(y\mid x)-\widetilde\ell(y\mid x),
\qquad
\Delta z(y)=z(y)-\widetilde z(y).
\]
On the full-measure set, absolute convergence gives
\[
A_f(y)-\widetilde A_f(y)
=\Delta z(y)\int_X f\,d\mu-\int_X f(x)\Delta(y,x)\,\mu(dx).
\]
Consequently, uniformly over \(f\in\mathcal F\),
\[
|A_f(y)-\widetilde A_f(y)|
\leq\int_X\omega(x)|\Delta(y,x)|\,\mu(dx)+\bar\omega|\Delta z(y)|.
\]
Also,
\[
|\Delta z(y)|
=\left|\int_X\Delta(y,x)\,\mu(dx)\right|
\leq\int_X|\Delta(y,x)|\,\mu(dx).
\]
Let
\[
B(y)=\int_X\omega(x)|\Delta(y,x)|\,\mu(dx)+\bar\omega|\Delta z(y)|.
\]
For each \(f\), the triangle inequality gives \(|A_f(y)|\leq|\widetilde A_f(y)|+B(y)\). Taking suprema yields \(S(y)\leq\widetilde S(y)+B(y)\), and reversing the roles yields \(\widetilde S(y)\leq S(y)+B(y)\). Thus
\[
|S(y)-\widetilde S(y)|\leq B(y)
\leq\int_X(\omega(x)+\bar\omega)|\Delta(y,x)|\,\mu(dx).
\]
This argument does not require a separate measurability assumption on a supremum of functional differences.

### 5. Integration

Finally, integrability of \(S\) and \(\widetilde S\), the integral triangle inequality, and the preceding measurable nonnegative majorant give
\[
\begin{aligned}
|U_{\mathcal F}-\widetilde U_{\mathcal F}|
&\leq\int_Y|S(y)-\widetilde S(y)|\,\nu(dy)\\
&\leq\int_Y\int_X(\omega(x)+\bar\omega)
|\ell(y\mid x)-\widetilde\ell(y\mid x)|\,\mu(dx)\,\nu(dy).
\end{aligned}
\]
Tonelli justifies the nonnegative iterated integrals. Together with the preceding cases, this proves the claim on the entire stated domain.
