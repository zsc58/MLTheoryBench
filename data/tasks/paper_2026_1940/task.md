# Problem

## Setup

Fix a finite interval \([t,s]\) and let \(D=D([t,s],\mathbb R^d)\) be the Skorokhod space of cadlag paths, where \(d\ge1\). Let \(\mu_s\) be a Borel probability law on \(D\). For a path \(\gamma\), its time extension is \(\widetilde\gamma(u)=(u,\gamma(u))\). Assume that the Marcus time-extended signature \(S(\widetilde\gamma)\in\mathcal H_{\mathrm{sig}}\) is defined on \(\operatorname{supp}(\mu_s)\), is strongly measurable under \(\mu_s\), and is Bochner-integrable, where \(\mathcal H_{\mathrm{sig}}\) is a real Hilbert space. Define
\[
\Phi_{\mu_s}=\mathbb E_{\gamma\sim\mu_s}[S(\widetilde\gamma)].
\]

Let \(\Omega_s\) be the bounded, self-adjoint, nonnegative long-run covariance operator of the augmented signature increments, and fix \(\lambda>0\). The law \(\mu_s\) and operator \(\Omega_s\) are fixed relative to the sample drawn below. Define
\[
Q_s=(\Omega_s+\lambda I)^{-1},\qquad
\langle u,v\rangle_{Q_s}=\langle u,Q_sv\rangle_{\mathcal H_{\mathrm{sig}}},
\quad \|u\|_{Q_s}=\sqrt{\langle u,u\rangle_{Q_s}}.
\]
Assume the signature map has finite uniform radius
\[
R_s:=\sup_{\gamma\in\operatorname{supp}(\mu_s)}
\|S(\widetilde\gamma)\|_{Q_s}<\infty.
\]
For an integer \(n\ge1\), draw independent \(\gamma_1,\ldots,\gamma_n\sim\mu_s\), and set \(X_i=S(\widetilde\gamma_i)\) and \(\widehat\Phi_{n,s}=n^{-1}\sum_{i=1}^nX_i\). For \(M>0\), let
\[
\mathcal F_{M,s}=\{f\in\mathcal H_{\mathrm{sig}}:\|f\|_{Q_s}\le M\},
\]
and define its conditional empirical Rademacher complexity by
\[
\widehat{\mathfrak R}_{n,s}(\mathcal F_{M,s})
=\mathbb E_\sigma\left[\sup_{f\in\mathcal F_{M,s}}
\frac1n\sum_{i=1}^n\sigma_i\langle f,X_i\rangle_{Q_s}\right],
\]
where the \(\sigma_i\) are independent uniform signs, independent of the sample, and \(\mathbb E_\sigma\) holds the sample fixed. Write \(\mathbb E_{\gamma_{1:n},\sigma}\) for expectation over both the iid path sample and these signs.

## Task

Prove that for every \(0<\delta<1\), with probability at least \(1-\delta\) over the sample,
\[
\|\Phi_{\mu_s}-\widehat\Phi_{n,s}\|_{Q_s}
\le \frac2n\,\mathbb E_{\gamma_{1:n},\sigma}\left\|\sum_{i=1}^n\sigma_iS(\widetilde\gamma_i)\right\|_{Q_s}
+2R_s\sqrt{\frac{\log(1/\delta)}{2n}}.
\]
Moreover, for every realised sample and every \(M>0\),
\[
\widehat{\mathfrak R}_{n,s}(\mathcal F_{M,s})
\le \frac{M}{n}\left(\sum_{i=1}^n
\|S(\widetilde\gamma_i)\|_{Q_s}^2\right)^{1/2}.
\]
