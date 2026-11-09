# Reference Proof

## Contract and standard result

Write \(s=(x,y)\), \(P_s=P_{W\mid X=x,Y=y}\), and \(Q_{\gamma,s}=\mathcal L(H_\gamma(x,y,\varepsilon)+e)\). The generator inputs \(\varepsilon,e\) are independent of each other and of the observation; the primed inputs form an independent copy. The same draw \(e\) is used when subtracting the added noise.

We use the following standard strict-propriety result for the Euclidean energy score, corresponding to theory_015. If \(P,Q\) have finite first moments and \(S,S'\sim P\), \(T,T'\sim Q\) are mutually independent, then
\[
D(P,Q)=2\mathbb E\|S-T\|-\mathbb E\|S-S'\|-\mathbb E\|T-T'\|\geq0,
\]
with equality if and only if \(P=Q\). Consequently,
\[
\int\operatorname{ES}(Q,w)P(dw)-\int\operatorname{ES}(P,w)P(dw)=\tfrac12D(P,Q).
\]
These statements apply to probability measures, without any density assumption on their supports. The public score domain supplies the finite conditional first moments; correct specification supplies the same property for \(P_s\) almost everywhere. No unconditional first-moment assumption on \(W\) is needed.

## 1. Every population minimizer recovers the proxy conditional law

Let \(\gamma_0\) be a correctly specified parameter. For each parameter \(\gamma\), on a full-\(P_{X,Y}\)-measure set where the conditional first moments are finite, define
\[
r_\gamma(s)=\int\operatorname{ES}(Q_{\gamma,s},w)P_s(dw).
\]
By the standard result,
\[
r_\gamma(s)-r_{\gamma_0}(s)=\tfrac12D(P_s,Q_{\gamma,s})\geq0.
\]
All relevant integrated risks are finite by the public loss assumption. Thus \(R(\gamma)\geq R(\gamma_0)\). If \(\gamma^*\) is any population minimizer, then
\[
0=R(\gamma^*)-R(\gamma_0)
 =\tfrac12\int D(P_s,Q_{\gamma^*,s})P_{X,Y}(ds).
\]
A nonnegative measurable function with integral zero vanishes almost everywhere. Strictness therefore yields
\[
Q_{\gamma^*,s}=P_s
\quad\text{for }P_{X,Y}\text{-almost every }s.
\]
This argument does not require the parameter class to allow separate optimization at each conditioning pair: the single correctly specified parameter attains the integrated lower bound.

## 2. Conditional deconvolution

The structural equations and mutual independence of the exogenous noises imply that \(E\) is independent of \((U,X,Y)\). In particular, a conditional law of \(W\) given \(s\) is the convolution of the conditional law of \(AU\) with \(P_E\), for almost every \(s\). Independently, the generator construction makes \(Q_{\gamma^*,s}\) the convolution of \(\mathcal L(H_{\gamma^*}(s,\varepsilon))\) with \(P_E\).

Fix \(s\) in a common full-measure set where these probability-kernel statements and the conclusion of Step 1 hold. For a probability measure \(\nu\), write \(\varphi_\nu(t)=\int e^{it^\top v}\nu(dv)\). Equality of the noisy probability laws gives, for every \(t\in\mathbb R^d\),
\[
\varphi_{H_{\gamma^*}(s,\varepsilon)}(t)\varphi_E(t)
=\varphi_{AU\mid s}(t)\varphi_E(t).
\]
The assumed Fourier normalization satisfies
\[
\varphi_E(t)=(2\pi)^{d/2}\widehat p_E(-t)\ne0.
\]
Cancellation and uniqueness of characteristic functions give
\[
\mathcal L(H_{\gamma^*}(s,\varepsilon))=\mathcal L(AU\mid s).
\]
The standard uniqueness theorem used here states that two Borel probability measures on \(\mathbb R^d\) with identical characteristic functions at every frequency are equal. Its probability-measure hypotheses hold even when \(d>k\) and the signal law is singular with respect to \(d\)-dimensional Lebesgue measure. There is no need to posit a density of \(AU\), invoke bounded completeness, or intersect frequency-dependent exceptional sets: the fixed conditioning pair already satisfies equality of the noisy probability measures.

Take the single matrix \(\widetilde A=A\), which has full column rank. Since
\[
V_{\gamma^*}(s,\varepsilon,e)-e=H_{\gamma^*}(s,\varepsilon)
\]
uses exactly the same added draw, this proves the de-noised-law assertion. Subtracting a fresh independent noise draw would not establish this assertion.

## 3. Equality of confounder information

For any full-column-rank matrix \(\widetilde A\), set
\[
Z=\widetilde A U,\qquad L=(\widetilde A^\top\widetilde A)^{-1}\widetilde A^\top.
\]
Then \(L\widetilde A=I_k\). Both maps are continuous, \(Z\) is measurable with respect to \(U\), and \(U=LZ\). Hence
\[
\sigma(Z)=\sigma(U),\qquad \sigma(Z,X)=\sigma(U,X).
\]
This proves equality of the confounder information. To obtain the all-treatment formula, however, one must also respect the public fixed-treatment version convention; observational almost-sure equality alone does not control arbitrary versions on a treatment-null slice.

## 4. Fixed-treatment adjustment

Fix any \(x\in\mathcal X\). Under the public structural-kernel convention, define
\[
m_x(u)=\int f_Y(u,x,n)P_{N_Y}(dn).
\]
The public absolute-integrability assumptions make this finite for \(P_U\)-almost every \(u\) and integrable with respect to \(P_U\). In the transformed coordinates the same outcome equation gives the regression
\[
\widetilde m_x(z)=\int f_Y(Lz,x,n)P_{N_Y}(dn)
\]
on the image of \(\widetilde A\), with irrelevant values off that image. Therefore \(\widetilde m_x(Z)=m_x(U)\), \(P_U\)-almost surely. These are the versions denoted by the conditional expectations in the problem. Independence of \(N_Y\) from \((U,X)\) verifies that they are versions of the observational outcome regressions; their structural definition additionally specifies their values on treatment-null slices.

Under \(\mathrm{do}(X=x)\), the law of \((U,N_Y)\) is unchanged and the outcome is \(f_Y(U,x,N_Y)\). Fubini's theorem, justified by the stated absolute integrability, yields
\[
\theta(x)
=\int\!\int f_Y(u,x,n)P_{N_Y}(dn)P_U(du)
=\int m_x(u)P_U(du)
=\int\widetilde m_x(z)P_Z(dz).
\]
This is precisely
\[
\theta(x)=\mathbb E\!\left[\mathbb E[Y\mid Z,X=x]\right].
\]
The outer expectation uses the marginal law of \(Z\), not its law given \(X=x\). Since \(x\) was arbitrary, the conclusion holds for every treatment value in the stipulated domain with the specified structural-model versions. The source's product-support and overlap assumptions are retained; they do not, on their own, make arbitrary regular-conditional versions unique at null treatment values.

All theorem-critical obligations are closed. The argument establishes conditional distributional recovery, not samplewise recovery of the original latent confounder.
