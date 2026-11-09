# Problem

## Setup

Let \(m\ge1\) be an integer, let \((\Delta,\mathcal A,\mathbb P)\) be a probability space, and let \(Z\) be a measurable decision space. For each criterion \(i\in\{1,\ldots,m\}\) and uncertainty realization \(\delta\in\Delta\), let \(Z_i(\delta)\subseteq Z\) be its appropriateness set. Assume that \((z,\delta)\mapsto\mathbf1_{\{z\in Z_i(\delta)\}}\) is measurable.

Write \(\mathbb N_0=\{0,1,2,\ldots\}\). A single decision map \(M\) is defined on every tuple of finite labelled lists \(E=(E_1,\ldots,E_m)\), where observations in \(E_i\) carry label \(i\). Empty component lists are allowed. Its restriction to each fixed size vector \(n\in\mathbb N_0^m\) is measurable. For every pair of tuples of sublists \(A,B\) selected at fixed positions from a finite input, assume also that the event \(M(A)=M(B)\) is measurable as a function of that input. Lists retain multiplicities, and deleting a sample means deleting one occurrence.

For a decision \(z\), define
\[
V_i(z)=\mathbb P\{\delta\in\Delta:z\notin Z_i(\delta)\},\qquad
V(z)=(V_1(z),\ldots,V_m(z)).
\]
For a tuple of lists \(E\), an occurrence in \(E_i\) is a **support scenario** if deleting it while retaining every other occurrence changes \(M(E)\). Let \(S_i(E)\) be the sublist of all support scenarios in \(E_i\), and let \(s_i(E)=|S_i(E)|\).

Assume the following properties of \(M\):

1. **Permutation invariance:** for every finite input, permuting observations within any component list does not change the decision.
2. **Consistency and responsiveness:** for any finite input \(E\) and any tuple \(T=(T_1,\ldots,T_m)\) of finite additional labelled lists, let \(E+T\) denote componentwise concatenation and put \(z=M(E)\). If \(z\in Z_i(\delta)\) for every occurrence \(\delta\in T_i\) and every \(i\), then \(M(E+T)=z\). If at least one such occurrence satisfies \(z\notin Z_i(\delta)\), then \(M(E+T)\ne z\).
3. **Non-degeneracy:** for every \(n\in\mathbb N_0^m\), when all uncertainty components of the observations in an input \(E\) of size \(n\) are independent draws from \(\mathbb P\),
   \[
   M(S_1(E),\ldots,S_m(E))=M(E)
   \]
   almost surely under \(\mathbb P^{|n|}\), where \(|n|=\sum_i n_i\). The product law for \(|n|=0\) is the point mass on the empty input.

Fix positive integers \(N_1,\ldots,N_m\), and write \(N=(N_1,\ldots,N_m)\). Sample labelled lists \(D_i\) of sizes \(N_i\), with every uncertainty component drawn independently from \(\mathbb P\), both within and across the lists. Set
\[
z_N^\star=M(D_1,\ldots,D_m),\qquad
s_{i,N}^\star=s_i(D),\qquad
s_N^\star=(s_{1,N}^\star,\ldots,s_{m,N}^\star).
\]

For multi-indices, inequalities are coordinatewise. For \(0\le b\le a\), write \(\binom ab=\prod_i\binom{a_i}{b_i}\). Write \((1-v)^r=\prod_i(1-v_i)^{r_i}\) wherever these powers are defined, using \(0^0=1\).

## Task

Fix a deterministic integer multi-index \(H\ge N\), a confidence parameter \(\beta\in(0,1)\), and deterministic real numbers \(\lambda_h\), indexed by \(0\le h\le H\), satisfying
\[
\lambda_h\le0\quad(h\ne N),\qquad
\lambda_N\le1,\qquad
\sum_{0\le h\le H}\lambda_h=1-\beta.
\]
For every \(0\le k\le N\), define
\[
R(k)=\left\{v\in[0,1]^m:
(1-v)^{N-k}>0\ \text{ and }\
\sum_{k\le h\le H}\lambda_h
\frac{\binom hk}{\binom Nk}(1-v)^{h-N}\ge0
\right\}.
\]
The sum in this definition is evaluated only at points satisfying \((1-v)^{N-k}>0\); all other points are excluded from \(R(k)\).

Prove the collective confidence statement
\[
\mathbb P^{|N|}\!\left\{V(z_N^\star)\in R(s_N^\star)\right\}\ge1-\beta.
\]
The region is a coupled subset of \([0,1]^m\); no Cartesian-product decomposition is assumed.
