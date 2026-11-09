# Problem

## Setup

Let \(n,d\) be positive integers. Fix a matrix \(\Phi\in\mathbb R^{n\times d}\), put \(K=\Phi\Phi^\top\), and fix \(\rho>0\) such that
\[
\rho\lambda_{\max}(K)<1.
\]
Fix \(\sigma>0\) and a symmetric positive-definite matrix \(\Sigma_*\in\mathbb R^{n\times n}\). Observe
\[
r\mid K\sim N(0,\Sigma_*).
\]
All parameters, matrices, and candidate sets in this conditional experiment are fixed independently of the draw of \(r\mid K\).

Define \(\theta_0=0\) and, for integers \(t\geq0\),
\[
\theta_{t+1}=\theta_t+\rho\Phi^\top(r-\Phi\theta_t).
\]
For each \(m\in\mathbb N_0:=\{0,1,2,\ldots\}\), define
\[
\widehat f_m=\Phi\theta_m,
\qquad \Sigma_m=\sigma^2(I_n-\rho K)^{-m},
\]
\[
\ell_m(r)=\frac1{2n}\left(\log\det\Sigma_m+r^\top\Sigma_m^{-1}r\right),
\qquad L(m\mid K)=\mathbb E[\ell_m(r)\mid K],
\]
and
\[
A_m=\Sigma_*^{1/2}\Sigma_m^{-1}\Sigma_*^{1/2},
\qquad v_m=\frac1n\operatorname{tr}(A_m^2).
\]
Let \(\mathcal M\subset\mathbb N_0\) be finite and nonempty, equip it with the uniform prior, and choose
\[
\widehat m\in\arg\min_{m\in\mathcal M}\ell_m(r)
\]
using a fixed measurable tie-breaking rule. Set
\[
\bar v=\max_{m\in\mathcal M}v_m.
\]

## Task

Prove the following integrated theorem.

For every \(\delta\in(0,1)\), with probability at least \(1-\delta\) over \(r\mid K\),
\[
L(\widehat m\mid K)\leq\ell_{\widehat m}(r)
+\sqrt{\frac{\bar v\bigl(\log|\mathcal M|+\log(1/\delta)\bigr)}{n}}.
\]

Moreover, consider a sequence of the preceding problems indexed by \(n\), with the same fixed \(\sigma>0\), a fixed \(\tau>0\), deterministic designs \(\Phi_n\in\mathbb R^{n\times d_n}\), step sizes \(\rho_n>0\), and finite nonempty candidate sets \(\mathcal M_n\subset\mathbb N_0\). Write \(K_n=\Phi_n\Phi_n^\top\), require \(\rho_n\lambda_{\max}(K_n)<1\), and use the additional subscript \(n\) for the quantities defined in the setup. In particular,
\[
\Sigma_{m,n}=\sigma^2(I_n-\rho_nK_n)^{-m}.
\]
Assume in this sequence that
\[
f_n\sim N(0,\tau^2K_n),\qquad
\varepsilon_n\sim N(0,\sigma^2I_n),\qquad
f_n\perp\varepsilon_n,
\]
\[
r_n=f_n+\varepsilon_n,
\qquad \Sigma_{*,n}=\tau^2K_n+\sigma^2I_n.
\]
Define \(f_{{\rm B},n}=\mathbb E[f_n\mid r_n,K_n]\). For each fixed horizon \(m\), define the deterministic function
\[
\operatorname{Gap}_n(m\mid K_n)
=\frac1n\mathbb E\left[\|\widehat f_{m,n}-f_{{\rm B},n}\|_2^2\mid K_n\right],
\]
where \(m\) is held fixed while taking the expectation. The notation \(\operatorname{Gap}_n(\widehat m_n\mid K_n)\) means this function evaluated at the selected horizon \(\widehat m_n\).

For each \(n\), let \(m_n^*\in\mathcal M_n\) be a deterministic comparator, not chosen using \(r_n\). Suppose
\[
\alpha_n:=\frac1n\mathrm{KL}\!\left(N(0,\Sigma_{*,n})\,\middle\|\,N(0,\Sigma_{m_n^*,n})\right)\longrightarrow0,
\]
\[
\sup_n\bar v_n<\infty,\qquad
\log|\mathcal M_n|=o(n),\qquad
\sup_n\|A_{m_n^*,n}\|_{\rm op}<\infty.
\]
Show that for each \(n\) and every \(\delta\in(0,1)\), with probability at least \(1-2\delta\) over \(r_n\mid K_n\),
\[
\operatorname{Gap}_n(\widehat m_n\mid K_n)
\leq4\sigma^2\left[\alpha_n
+\sqrt{\frac{v_{m_n^*,n}\log(1/\delta)}{n}}
+\frac{\|A_{m_n^*,n}\|_{\rm op}\log(1/\delta)}{n}
+\sqrt{\frac{\bar v_n\bigl(\log|\mathcal M_n|+\log(1/\delta)\bigr)}{n}}\right].
\]
Consequently, prove that \(\operatorname{Gap}_n(\widehat m_n\mid K_n)\to0\) in probability under the conditional laws \(r_n\mid K_n\).
