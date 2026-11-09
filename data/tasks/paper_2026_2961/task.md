# Problem

## Setup

Let \(p\ge1\), \(Q=[-1,1]^p\), and let \(X\) be supported on \(Q\) almost surely, with joint density \(f\) with respect to Lebesgue measure \(\lambda\) on \(Q\), satisfying
\[
0<c_1\le f(x)\le c_2<\infty\quad (x\in Q).
\]
Write \(\mu_f=f\,d\lambda\) and \(L^2=L^2(Q,\mu_f)\). For \(S\subseteq[p]\), let \(f_S\) be the marginal density of \(X_S\), with \(f_\varnothing=1\). Let \(P_n\) be the Legendre polynomial and \(\widetilde P_n=((2n+1)/2)^{1/2}P_n\). For nonempty \(S\) and multi-indices \(m_S\in\mathbb N_{\ge1}^{S}\), define
\[
\xi_S^{(m_S)}(x)=2^{-(p-|S|)/2}\frac{\prod_{j\in S}\widetilde P_{m_j}(x_j)}{f_S(x_S)},
\qquad \xi_\varnothing=1,
\]
and let \(\Xi\) be this family.

Assume also the following generalized decomposition fact: for every \(\nu\in L^2\), there is a unique family \(\{\nu_S\}_{S\subseteq[p]}\) of square-integrable measurable functions, with \(\nu_S\) depending only on \(x_S\), that minimizes
\[
\mathbb E\!\left[\left(\nu(X)-\sum_{S\subseteq[p]}g_S(X_S)\right)^2\right]
\]
over square-integrable measurable functions \(g_S\) depending only on \(x_S\), subject, for every \(T\subsetneq S\), to
\[
\mathbb E[g_S(X_S)h(X_T)]=0
\quad\text{for every square-integrable measurable function }h(X_T).
\]
This unique family sums to \(\nu\) in \(L^2\). Functions of \(X_\varnothing\) are constants.

## Task

Prove that \(\Xi\) is a Riesz basis of \(L^2\). Moreover, for every \(\nu\in L^2\), there is a unique coefficient family \(\{a_S^{(m_S)}\}\) such that
\[
\nu_S(x_S)=\sum_{m_S}a_S^{(m_S)}\xi_S^{(m_S)}(x_S)
\]
(including \(\nu_\varnothing=a_\varnothing\xi_\varnothing\)), the component series converge in \(L^2\), and the resulting components are exactly the unique constrained least-squares decomposition specified above. Equalities of components are understood in \(L^2\), or equivalently almost surely under the corresponding marginal law.
