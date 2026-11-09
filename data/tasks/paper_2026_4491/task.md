# Problem

## Setup

For probability laws $U,V$ on the same measurable space, define
\[
H_\gamma(U\|V)=\sup_{S\text{ measurable}}\bigl(U(S)-\gamma V(S)\bigr),\qquad \gamma>0.
\]
Say that $(A,B)$ dominates $(U,V)$ if $H_\gamma(U\|V)\le H_\gamma(A\|B)$ for every $\gamma>0$. A mechanism is $(\varepsilon,\delta)$-differentially private if, for every ordered pair of neighboring datasets and every measurable output event $S$, its output laws $U,V$ satisfy $U(S)\le e^\varepsilon V(S)+\delta$.

Let $k,b,d$ be positive integers, set $N=kb$, and fix $\sigma>0$. Let $C\in\mathbb R^{N\times N}$ be a fixed invertible lower-triangular matrix with nonnegative entries, and let $E\in\mathbb R^{N\times N}$ have entries $E_{nt}=\mathbf1\{t\le n\}$.

Consider the following mechanism on finite datasets of records. Each record occurrence $x$ is assigned an independent uniform batch index $B_x\in\{1,\ldots,b\}$, used in every epoch. These assignments are independent of a noise matrix $Z\in\mathbb R^{N\times d}$ whose entries are independent $\mathcal N(0,\sigma^2)$ variables. For each round $n$, fix a measurable map $g_n(x;t_{1:n-1})\in\mathbb R^d$ with norm at most 1 for every record and every earlier transcript. These maps are common to neighboring datasets. Define recursively
\[
G_n=\sum_{x:\,B_x=1+((n-1)\bmod b)}g_n(x;T_{1:n-1}),
\qquad T=E(G+C^{-1}Z),
\]
and let $M$ release $T$ row by row. Neighboring datasets differ by adding or removing one record occurrence. The lower-triangular matrices and the restriction of $g_n$ to earlier outputs make this recursion well defined.

Define deterministic vectors
\[
m_j=\sum_{e=0}^{k-1}C_{:,j+eb}\in[0,\infty)^N,\qquad j=1,\ldots,b,
\]
and the auxiliary laws on $\mathbb R^N$
\[
P=\frac1b\sum_{j=1}^b\mathcal N(m_j,\sigma^2I_N),\qquad
Q=\mathcal N(0,\sigma^2I_N).
\]
Under $P$, equivalently choose a single uniform index $J\in\{1,\ldots,b\}$ independently of $W\sim\mathcal N(0,I_N)$ and set $X=m_J+\sigma W$. The index is chosen once for the entire vector. Under $Q$, set $X=\sigma W$. These are auxiliary experiments; they are not definitions of the actual neighboring output laws of $M$.

For a history $h\in\mathbb R^{n-1}$, let $\rho_{n,j}(h)$ be the posterior probability of $J=j$ under the $P$ experiment, using the version determined by its positive Gaussian densities. Define
\[
P_n^h=\sum_{j=1}^b\rho_{n,j}(h)\mathcal N(m_{j,n},\sigma^2),\qquad
Q_n^h=\mathcal N(0,\sigma^2).
\]
Thus the remove-oriented conditional pair is $(P_n^h,Q_n^h)$ and the add-oriented pair is $(Q_n^h,P_n^h)$. In the latter pair the same posterior function is evaluated at histories sampled under $Q$. At $n=1$, the history space consists of the empty history and the posterior is uniform.

Fix deterministic budgets $\beta_n\in(0,1)$ and put $\delta_E=\sum_{n=1}^N\beta_n$.

## Task

For each round, construct deterministic probability vectors $w_n^-,w_n^+$ on $\{1,\ldots,b\}$, depending only on the fixed mean array, $\sigma$, and the budgets, and form
\[
A_n^-=\sum_jw_{n,j}^-\mathcal N(m_{j,n},\sigma^2),\qquad B_n^-=\mathcal N(0,\sigma^2),
\]
\[
A_n^+=\mathcal N(0,\sigma^2),\qquad B_n^+=\sum_jw_{n,j}^+\mathcal N(m_{j,n},\sigma^2).
\]
The two probability vectors may differ and must not depend on an observed history.

Prove that there are measurable sets $F_n^-,F_n^+\subseteq\mathbb R^{n-1}$ such that
\[
P\{X_{1:n-1}\in F_n^-\}\le\beta_n,\qquad
Q\{X_{1:n-1}\in F_n^+\}\le\beta_n,
\]
with $(A_n^-,B_n^-)$ dominating $(P_n^h,Q_n^h)$ for every $h\notin F_n^-$ and $(A_n^+,B_n^+)$ dominating $(Q_n^h,P_n^h)$ for every $h\notin F_n^+$.

Then prove, for every $\gamma\ge1$, that
\[
H_\gamma(P\|Q)\le
H_\gamma\!\left(\bigotimes_{n=1}^N A_n^-\middle\|\bigotimes_{n=1}^N B_n^-\right)+\delta_E,
\]
\[
H_\gamma(Q\|P)\le
H_\gamma\!\left(\bigotimes_{n=1}^N A_n^+\middle\|\bigotimes_{n=1}^N B_n^+\right)+\delta_E.
\]
Use these bounds to establish a deterministic $(\varepsilon,\delta)$ privacy accountant for $M$, valid for every choice of the specified adaptive maps, with $\varepsilon\ge0$ and $\delta\in[0,1]$. Justify the connection between the auxiliary experiments and actual neighboring outputs rather than identifying their laws.

Given the mean array, state the construction costs $O(N^2b^2)$ for remove and $O(N^2b)$ for add. With the mean array fixed and only the common noise multiplier $\sigma$ varied, state the costs after preprocessing as $O(Nb^2)$ and $O(Nb\log b)$, respectively, for $b\ge2$; give the $b=1$ case separately. These are arithmetic-operation counts with a fixed scalar numerical-iteration budget, not bit-complexity claims. They concern constructing all per-step comparison pairs and exclude forming the mean array and evaluating the final product divergences. Any numerical approximations used to report privacy must preserve an upper bound.
