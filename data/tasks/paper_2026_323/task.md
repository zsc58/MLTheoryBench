# Problem

## Setup

For each integer \(n\ge3\), let \([n]=\{1,\ldots,n\}\), let \(K_n\) be a positive integer, and let \(\rho=(\rho_1,\ldots,\rho_{K_n})\) be a deterministic probability vector with positive entries. Write \(\rho_{\min}=\min_a\rho_a\). Let \(B\in[0,1]^{K_n\times K_n}\) be deterministic with pairwise distinct rows, and let \(0<\gamma_n\le1\). These parameters may depend on \(n\).

The latent labels \(z_1,\ldots,z_n\) are iid with \(\Pr(z_i=a)=\rho_a\). Define, for all \(i,j\in[n]\), including \(i=j\),
\[
P^0_{ij}=B_{z_i z_j},\qquad P_{ij}=\gamma_nP^0_{ij}.
\]
Conditional on the labels, the directed off-diagonal edges \(A_{ij}\), \(i\ne j\), are independent Bernoulli variables with parameters \(P_{ij}\). Set \(A_{ii}=0\); the diagonal entries of \(P\) remain as defined above.

Let
\[
G=\frac1nAA^\top
\]
and, for distinct \(i,r\), define
\[
d(i,r)=\max_{k\in[n]\setminus\{i,r\}}|G_{ik}-G_{rk}|.
\]
Choose a deterministic \(h=h_n\in(0,1)\). Define the empirical \(h\)-quantile \(q_i(h)\) to be the \(\lceil h(n-1)\rceil\)-th smallest member of the list \(\{d(i,s):s\ne i\}\), counting repetitions. Set
\[
N_i=\{r\ne i:d(i,r)\le q_i(h)\},
\qquad
\widetilde P_{i\cdot}=\frac1{|N_i|}\sum_{r\in N_i}A_{r\cdot}.
\]
Thus all ties at the quantile are included.

Let \(\varepsilon_\pi,\varepsilon_{AP},\varepsilon_m>0\) be deterministic tolerances satisfying
\[
h<\rho_{\min}-\varepsilon_\pi,
\qquad \varepsilon_{AP}>4/n.
\]

For the asymptotic assertion, assume \(\gamma_n\to0\). Assume there are constants \(C_\rho>C_\pi>0\) and an integer \(n_0\) such that, for all \(n\ge n_0\),
\[
\rho_{\min}\ge C_\rho\sqrt{\frac{\log n}{n}},
\qquad
\rho_{\min}>\varepsilon_\pi\ge C_\pi\sqrt{\frac{\log n}{n}},
\]
and assume
\[
K_n n^{-C_\pi^2/4}\longrightarrow0,
\qquad
\frac{n\varepsilon_\pi^2/4}{1+\varepsilon_\pi}-\log(2K_n)\longrightarrow+\infty,
\]
\[
\frac{n(\varepsilon_{AP}-4/n)^2/4}{1+\varepsilon_{AP}}-2\log n\longrightarrow+\infty,
\qquad
\frac{n\varepsilon_m^2/4}{1+\varepsilon_m}-\log(n(n-1))\longrightarrow+\infty.
\]
Also assume \(h(n-1)\to\infty\), \(\varepsilon_{AP}\to0\), and \(\varepsilon_m\to0\).

## Task

Prove that, with probability at least
\[
1-2K_n\exp\!\left[-\frac{n\varepsilon_\pi^2/4}{1+\varepsilon_\pi}\right]
-2n^2\exp\!\left[-\frac{n(\varepsilon_{AP}-4/n)^2/4}{1+\varepsilon_{AP}}\right]
-n(n-1)\exp\!\left[-\frac{n\varepsilon_m^2/4}{1+\varepsilon_m}\right],
\]
simultaneously for every vertex \(i\),
\[
\frac1n\|\widetilde P_{i\cdot}-P_{i\cdot}\|_2^2
\le \frac{2}{|N_i|}+\varepsilon_m+\frac2n+16\varepsilon_{AP},
\]
where \(\|\cdot\|_2\) denotes the Euclidean norm and probability includes both the labels and the edges.

Consequently, prove that
\[
\max_{1\le i\le n}\frac1n\|\widetilde P_{i\cdot}-P_{i\cdot}\|_2^2\longrightarrow0
\]
in probability under the stated asymptotic assumptions.
