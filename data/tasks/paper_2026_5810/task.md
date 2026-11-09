# Problem

## Setup

For each positive integer d, write S^{d-1}={u in R^d: ||u||_2=1}. Let p be an integer with p >= 2, and identify the symmetric p x p matrices with R^n, n=p(p+1)/2, using the Frobenius inner product. Let S_+^p be the cone of positive-semidefinite matrices. For a nonzero closed cone K subset R^d and integer T >= 1, define
\[
\mu(K,T):=\min_{x_1,\ldots,x_T\in K\cap S^{d-1}}\max_{i\ne j}|\langle x_i,x_j\rangle|,
\]
where the maximum is defined to be 0 when T=1, and define
\[
C_\varepsilon(K):=\sup\{T\in\mathbb N:\mu(K,T)\le\varepsilon\}.
\]
For u in S^{p-1}, define the rank-one PSD address psi(u)=uu^T in S_+^p, so ||psi(u)||_F=1.

For an associative readout with integer T >= 2, fix unit addresses u_1,...,u_T in S^{p-1} and a matched index * in {1,...,T}, and use u_* as the query. Let d_v be a positive integer. With these addresses held fixed, let the values v_1,...,v_T be independent N(0,I_{d_v}/d_v) vectors. For coefficients a_j with positive aggregate distractor power, define
\[
\mathrm{pSNR}:=\frac{|a_*|^2}{\sum_{j\ne *}|a_j|^2};
\]
ideal retrieval means pSNR > 1. Take linear coefficients a_j^Lin=u_*^T u_j and PSD coefficients a_j^PSD=<psi(u_*),psi(u_j)>_F, with matched coefficient normalized to one.

## Task

Prove the following integrated theorem. For every 0 < epsilon < 1,
\[
C_\varepsilon(S_+^p)\ge \frac12(1-\varepsilon)^{-(p-1)/2},
\]
so rank-one PSD addresses admit an exponentially large (in p, for fixed epsilon) fixed-interference dictionary. Moreover, let T > p be an integer and set epsilon_*=(T-p)/(p(T-1)). Assume each distractor satisfies (u_*^T u_j)^2=epsilon_*. Show that
\[
\mathrm{pSNR}_{\rm Lin}=\frac p{T-p},
\qquad
\mathrm{pSNR}_{\rm PSD}=\frac{p^2(T-1)}{(T-p)^2},
\]
and conclude that ideal linear retrieval holds iff T < 2p, whereas ideal PSD retrieval holds iff (T-p)^2 < p^2(T-1). Within the assumed regime T > p, show that the PSD criterion is equivalent to T < T_+, where
\[
T_+=\frac{p^2+2p+p\sqrt{p^2+4p-4}}2=p^2+2p-2+O(p^{-1})
\]
as p tends to infinity, giving a Theta(p^2) upper retrieval threshold.
