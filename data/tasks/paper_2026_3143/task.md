# Problem

## Setup

For each integer \(M\ge1\), let \(N=N_M>M\) and suppose \(N_M/M\to\alpha>1\). A finite pool consists of fixed real losses \(\ell_1,\ldots,\ell_N\) and proxy losses \(\widetilde\ell_1,\ldots,\widetilde\ell_N\). Define
\[
R_M=\frac1N\sum_{i=1}^N\ell_i,\qquad \widetilde R_M=\frac1N\sum_{i=1}^N\widetilde\ell_i,\qquad c_i=\widetilde\ell_i-\widetilde R_M.
\]
Thus \(N^{-1}\sum_i c_i=0\).

Each item has a fixed, initially unqueried label \(y_i\) in a measurable space \(\mathcal Y\). Its loss is \(\ell_i=h_i(y_i)\), where \(h_i:\mathcal Y\to\mathbb R\) is a known measurable function. Let \(H_0\) denote the fixed information available before sampling, including the functions \(h_i\), all proxy losses, and any other initially available side information, but not the unqueried true labels. Querying item \(i\) reveals \(y_i\) and hence \(\ell_i\).

Draw indices \(I_1,\ldots,I_M\) sequentially without replacement. An admissible proposal process is specified by measurable maps \(\eta_1,\ldots,\eta_M\), chosen without access to unqueried true labels, with
\[
Q_m=\eta_m\bigl(H_0,(I_1,y_{I_1}),\ldots,(I_{m-1},y_{I_{m-1}})\bigr).
\]
The maps may use true labels only through the displayed queried history. At every history, \(Q_m\) is zero on previously sampled indices, strictly positive on every remaining index, and sums to one. The next index is sampled according to this distribution.

All probabilities and moments below are over this sampling procedure, with the pool and \(H_0\) fixed. Write \(\mathcal F_m=\sigma(I_1,\ldots,I_m)\), with \(\mathcal F_0\) trivial. Under this fixed-pool convention, \(Q_m\) is a deterministic function of the finite index history and
\[
\Pr(I_m=i\mid\mathcal F_{m-1})=Q_m(i).
\]
For any real array \(x=(x_i)_{i=1}^N\), define
\[
V_m=1+\frac{N-M}{N-m}\left[\frac1{(N-m+1)Q_m(I_m)}-1\right],
\qquad
\widehat R_{\mathrm{LURE}}(x)=\frac1M\sum_{m=1}^M V_m x_{I_m}.
\]
Define
\[
\widehat R_{\mathrm{PPAT}}(\lambda)=\widehat R_{\mathrm{LURE}}(\ell)-\lambda\widehat R_{\mathrm{LURE}}(c),\qquad \lambda\in\mathbb R.
\]
All these estimators use the same sampled indices and weights. In each variance comparison and minimization over \(\lambda\), hold the proposal maps and their induced sampling law fixed.

## Task

Prove that for every \(M\), every admissible adaptive proposal process, and every fixed \(\lambda\in\mathbb R\),
\[
\mathbb E\,\widehat R_{\mathrm{PPAT}}(\lambda)=R_M.
\]
With \(L=\widehat R_{\mathrm{LURE}}(\ell)\) and \(C=\widehat R_{\mathrm{LURE}}(c)\), also prove
\[
\operatorname{Var}(\widehat R_{\mathrm{PPAT}}(\lambda))
=\operatorname{Var}(L)-2\lambda\operatorname{Cov}(L,C)+\lambda^2\operatorname{Var}(C).
\]
If \(\operatorname{Var}(C)>0\), prove that the unique variance-minimizing coefficient is
\[
\lambda^*=\frac{\operatorname{Cov}(L,C)}{\operatorname{Var}(C)},
\]
and that PPAT has strictly smaller variance than LURE exactly for \(\lambda\) strictly between \(0\) and \(2\lambda^*\) (endpoints ordered). State what happens when \(\operatorname{Var}(C)=0\).
