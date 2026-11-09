# Reference Proof

## Proof Obligations

The proof closes the following obligations: covariance well-definedness and the spectral iterate, including zero horizons and singular kernels; the Gaussian lower-tail exponential moment; a simultaneous finite-class event and valid deterministic temperature choice; the aligned-model posterior mean; the scalar inequality and covariance-KL-to-gap transfer; the Gaussian KL/cross-entropy identity; the fixed-comparator upper-tail concentration bound; and the event intersection and convergence-in-probability argument.

Throughout each finite-dimensional argument, condition on the fixed geometry and all specified deterministic parameters. No independence across dimensions is needed.

## 1. Domains and spectral iterate

Let \(B=I_n-\rho K\). If \(\lambda_i\geq0\) are the eigenvalues of \(K\), the step-size assumption gives
\[
0<1-\rho\lambda_i\leq1.
\]
The upper endpoint occurs on the nullspace of \(K\). Thus \(B\) is positive definite, and for every finite \(m\geq0\),
\[
\Sigma_m=\sigma^2B^{-m}\succeq\sigma^2I_n.
\]
All inverses and log determinants in the task are consequently finite. Since \(\Sigma_*\succ0\), also \(A_m\succ0\), so \(0<v_m<\infty\). Finiteness and nonemptiness of the candidate set give \(0<\bar v<\infty\). The scores are continuous functions of \(r\), and the stated tie-breaking convention makes the selector measurable.

Multiplying the parameter recursion by \(\Phi\) gives
\[
\widehat f_{t+1}=\widehat f_t+\rho K(r-\widehat f_t),\qquad \widehat f_0=0.
\]
Therefore \(r-\widehat f_{t+1}=B(r-\widehat f_t)\), and induction, including \(m=0\), yields
\[
\widehat f_m=(I_n-B^m)r=:H_mr. \tag{1}
\]
In particular,
\[
H_m=I_n-\sigma^2\Sigma_m^{-1}. \tag{2}
\]
These are private derived identities, not additional assumptions.

## 2. Evidence bound under an arbitrary positive-definite reference covariance

Write \(r=\Sigma_*^{1/2}Z\), where \(Z\sim N(0,I_n)\). The log determinant is deterministic and \(\mathbb E[ZZ^\top]=I_n\), so
\[
X_m:=n\{L(m\mid K)-\ell_m(r)\}
=\frac12\{\operatorname{tr}(A_m)-Z^\top A_mZ\}. \tag{3}
\]
Diagonalize \(A_m\) with eigenvalues \(a_i\geq0\). An orthogonal rotation of \(Z\) again has independent standard Gaussian coordinates. Direct integration of each Gaussian density gives
\[
\mathbb E\exp(-\beta a_i Z_i^2/2)=(1+\beta a_i)^{-1/2},\qquad \beta\geq0.
\]
Consequently,
\[
\mathbb E e^{\beta X_m}
=e^{\beta\operatorname{tr}(A_m)/2}\det(I_n+\beta A_m)^{-1/2}.
\]
The inequality \(\log(1+u)\geq u-u^2/2\) for \(u\geq0\) follows, for example, because the derivative of \(\log(1+u)-u+u^2/2\) is \(u^2/(1+u)\geq0\) and its value at zero is zero. Hence
\[
\log\mathbb E e^{\beta X_m}
\leq\frac{\beta^2}{4}\operatorname{tr}(A_m^2)
=\frac{\beta^2n}{4}v_m. \tag{4}
\]

Here is the finite-class change-of-measure argument explicitly. Fix \(\beta>0\), let \(\pi_0\) be the uniform prior, and put
\[
\psi_m=\frac{\beta^2n}{4}v_m,
\qquad S=\sum_{m\in\mathcal M}\pi_0(m)e^{\beta X_m-\psi_m}.
\]
The prior, candidate set, temperature, and certificates are deterministic in the conditional experiment. By (4), \(\mathbb E S\leq1\). Markov's inequality therefore gives an event of probability at least \(1-\delta\) on which \(S\leq1/\delta\).

On this event, for every probability vector \(\nu\) on \(\mathcal M\), concavity of the logarithm gives
\[
\begin{aligned}
\beta\mathbb E_\nu X_m-\mathbb E_\nu\psi_m-\mathrm{KL}(\nu\|\pi_0)
&=\sum_{m:\nu(m)>0}\nu(m)\log\frac{\pi_0(m)e^{\beta X_m-\psi_m}}{\nu(m)}\\
&\leq\log\sum_{m:\nu(m)>0}\pi_0(m)e^{\beta X_m-\psi_m}\\
&\leq\log S\leq\log(1/\delta).
\end{aligned}
\]
Thus, simultaneously for all such \(\nu\),
\[
\mathbb E_\nu L(m\mid K)
\leq\mathbb E_\nu\ell_m(r)
+\frac{\mathrm{KL}(\nu\|\pi_0)+\log(1/\delta)}{\beta n}
+\frac\beta4\mathbb E_\nu v_m. \tag{5}
\]
The simultaneity permits data-dependent point masses. At \(\nu=\delta_{\widehat m}\), the divergence is exactly \(\log|\mathcal M|\), regardless of the selected value. Write
\[
c=\log|\mathcal M|+\log(1/\delta)>0.
\]
Apply the preceding argument at the particular temperature
\[
\beta_*=2\sqrt{\frac{c}{n\bar v}}.
\]
This temperature is deterministic given the parameters and \(\delta\); it is fixed before constructing the Markov event. There is no optimization over a family of random-temperature events. Since \(v_{\widehat m}\leq\bar v\), (5) gives
\[
L(\widehat m\mid K)
\leq\ell_{\widehat m}(r)+\frac{c}{\beta_*n}+\frac{\beta_*\bar v}{4}
=\ell_{\widehat m}(r)+\sqrt{\frac{\bar v c}{n}}. \tag{6}
\]
The same event bounds every deterministic candidate by taking its point mass in (5). Nothing in this section requires \(\Sigma_*\) to commute with \(K\) or to have the aligned form.

## 3. Aligned-model Bayes gap and covariance KL

Now impose \(\Sigma_*=\tau^2K+\sigma^2I_n\), with \(r=f+\varepsilon\) as specified in the second part of the task. For this section suppress the additional sequence index.

The vectors \(f\) and \(r\) are jointly Gaussian, \(\operatorname{Cov}(f,r)=\tau^2K\), and \(\operatorname{Cov}(r)=\Sigma_*\succ0\). The jointly Gaussian residual
\[
u=f-\tau^2K\Sigma_*^{-1}r
\]
has mean zero and zero covariance with \(r\). Their joint Gaussian characteristic function therefore factors, so \(u\) and \(r\) are independent, even when the covariance of \(f\) is singular. It follows that
\[
f_{\rm B}=\mathbb E[f\mid r,K]
=\tau^2K\Sigma_*^{-1}r
=(I_n-\sigma^2\Sigma_*^{-1})r. \tag{7}
\]

Diagonalize \(K\). Both covariance matrices are functions of \(K\), so they are diagonal in this basis. Write their eigenvalues as
\[
s_{*,i}=\tau^2\lambda_i+\sigma^2,
\qquad s_{m,i}=\sigma^2(1-\rho\lambda_i)^{-m},
\qquad t_i=\frac{s_{*,i}}{s_{m,i}}>0.
\]
By (2) and (7), the difference of the two shrinkage coefficients in coordinate \(i\) is
\[
\sigma^2\left(\frac1{s_{*,i}}-\frac1{s_{m,i}}\right)
=\frac{\sigma^2(1-t_i)}{s_{*,i}}.
\]
Holding \(m\) fixed and averaging over \(r\mid K\), the contribution to the unnormalized squared gap is therefore
\[
\frac{\sigma^4(1-t_i)^2}{s_{*,i}}. \tag{8}
\]
Both \(s_{*,i}\) and \(s_{m,i}\) are at least \(\sigma^2\). Thus \(s_{*,i}/\sigma^2\geq\max\{t_i,1\}\), and
\[
\frac{\sigma^4(1-t_i)^2}{s_{*,i}}
\leq\sigma^2\frac{(t_i-1)^2}{\max\{t_i,1\}}. \tag{9}
\]

The required scalar inequality is
\[
t-1-\log t\geq\frac{(t-1)^2}{2\max\{t,1\}},\qquad t>0. \tag{10}
\]
For \(0<t\leq1\), let \(h(t)=t-1-\log t-(t-1)^2/2\). Then \(h(1)=h'(1)=0\) and \(h''(t)=t^{-2}-1\geq0\), so \(h(t)\geq0\). For \(t\geq1\), let \(h(t)=t-1-\log t-(t-1)^2/(2t)\). Here \(h(1)=0\) and
\[
h'(t)=\frac{(t-1)^2}{2t^2}\geq0,
\]
which proves the other case and hence (10).

For completeness, subtracting the logarithms of the two positive Gaussian densities and taking expectation under \(N(0,\Sigma_*)\) yields
\[
D_m:=\mathrm{KL}\!\left(N(0,\Sigma_*)\,\middle\|\,N(0,\Sigma_m)\right)
=\frac12\left[\log\det\Sigma_m-\log\det\Sigma_*+\operatorname{tr}(\Sigma_m^{-1}\Sigma_*)-n\right]
=\frac12\sum_i(t_i-1-\log t_i). \tag{11}
\]
Combining (8)--(11) and dividing by \(n\) proves
\[
\operatorname{Gap}_n(m\mid K)\leq\frac{4\sigma^2}{n}D_m. \tag{12}
\]
Define, only within this private proof,
\[
L_*(K)=\frac1{2n}(\log\det\Sigma_*+n).
\]
Since
\[
L(m\mid K)=\frac1{2n}\left[\log\det\Sigma_m+\operatorname{tr}(\Sigma_m^{-1}\Sigma_*)\right],
\]
(11) also gives
\[
\frac{D_m}{n}=L(m\mid K)-L_*(K). \tag{13}
\]

Both (12) and (13) are identities or inequalities between deterministic functions of the horizon. They can therefore be evaluated at the random selected horizon without moving that horizon inside an expectation. On the event in (6), evidence minimization then implies, for every comparator \(m\in\mathcal M\),
\[
\operatorname{Gap}_n(\widehat m\mid K)
\leq4\sigma^2\left[\ell_m(r)-L_*(K)
+\sqrt{\frac{\bar v(\log|\mathcal M|+\log(1/\delta))}{n}}\right]. \tag{14}
\]
This is a statement about the fixed-horizon risk function evaluated at the selected index, exactly as defined in the task.

## 4. Comparator concentration and the asymptotic conclusion

We derive the required upper-tail bound. Let \(A\succeq0\) be deterministic, \(Z\sim N(0,I_n)\), \(V=\operatorname{tr}(A^2)\), \(M=\|A\|_{\rm op}\), and \(Y=Z^\top AZ-\operatorname{tr}(A)\). If \(A=0\), then \(Y=0\). Otherwise \(V,M>0\), and diagonalizing \(A\) gives, for \(0<s<1/(2M)\),
\[
\log\mathbb E e^{sY}
=\frac12\sum_i[-\log(1-2sa_i)-2sa_i]
\leq\frac{s^2V}{1-2sM}. \tag{15}
\]
Indeed, for \(0\leq u<1\),
\[
-\log(1-u)-u=\sum_{k\geq2}\frac{u^k}{k}\leq\frac{u^2}{2(1-u)}.
\]
For \(x>0\), apply the exponential Markov inequality using
\[
s=\frac{\sqrt{x}}{\sqrt V+2M\sqrt{x}}\in(0,1/(2M)).
\]
Substitution into (15) gives
\[
\mathbb P\left(Y\geq2\sqrt{Vx}+2Mx\right)\leq e^{-x}. \tag{16}
\]

For a comparator \(m\) fixed independently of the residual draw,
\[
\ell_m(r)-L(m\mid K)=\frac1{2n}\left[Z^\top A_mZ-\operatorname{tr}(A_m)\right].
\]
Apply (16) with \(A=A_m\), \(V=nv_m\), and \(x=\log(1/\delta)\). With probability at least \(1-\delta\),
\[
\ell_m(r)\leq L(m\mid K)
+\sqrt{\frac{v_m\log(1/\delta)}n}
+\frac{\|A_m\|_{\rm op}\log(1/\delta)}n. \tag{17}
\]
The fixed-comparator condition verifies the determinism required in (15)--(17).

Restore the sequence indices and apply (14) and (17) with \(m=m_n^*\). Their two events intersect with conditional probability at least \(1-2\delta\); independence between these events is not needed. By (13),
\[
L_n(m_n^*\mid K_n)-L_*(K_n)=\alpha_n.
\]
Consequently,
\[
\operatorname{Gap}_n(\widehat m_n\mid K_n)
\leq4\sigma^2\left[\alpha_n
+\sqrt{\frac{v_{m_n^*,n}\log(1/\delta)}{n}}
+\frac{\|A_{m_n^*,n}\|_{\rm op}\log(1/\delta)}{n}
+\sqrt{\frac{\bar v_n(\log|\mathcal M_n|+\log(1/\delta))}{n}}\right].
\]
This is the asserted finite-dimensional bound. Its confidence statement is for each \(n\), not a claim of one event holding simultaneously for all \(n\).

For every fixed \(\delta\in(0,1/2)\), the deterministic right-hand side tends to zero: use \(v_{m_n^*,n}\leq\bar v_n\), the two uniform boundedness assumptions, \(\log|\mathcal M_n|=o(n)\), \(\alpha_n\to0\), and the fixed noise scale \(\sigma\). Given \(\epsilon>0\) and \(\eta>0\), choose \(\delta\in(0,1/2)\) with \(2\delta<\eta\). For all sufficiently large \(n\), the right-hand side is below \(\epsilon\), so
\[
\mathbb P\left(\operatorname{Gap}_n(\widehat m_n\mid K_n)>\epsilon\mid K_n\right)\leq2\delta<\eta.
\]
This proves convergence in probability.

All arguments include \(m=0\), singleton candidate sets, and singular or zero kernels. In the aligned model with \(K=0\), both posterior and iterative corrections are zero, so the gap is zero. No division by a positive eigenvalue or positive kernel rank was used.

## Source-Audit Notes

The source's spectral endpoint assertion at L000573 is corrected to \(0<1-\rho\lambda_i\leq1\). Its unsquared identity at L000853 is corrected to \((1-r_i)/m_{*,i}\); all subsequent squared expressions and theorem constants are unchanged. The scalar support at L000835-L000842 is represented by the existing material ID theory_027. The proof does not rely on the unrestricted posterior-temperature optimization asserted at L000814-L000820: for the selected uniform-prior point-mass theorem, the optimizing temperature is deterministic and is chosen before constructing the probability event. Every proof obligation listed at the beginning has been explicitly discharged.
