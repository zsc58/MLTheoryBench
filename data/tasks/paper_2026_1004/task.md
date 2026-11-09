# Problem

## Setup

Let $\mathcal Y$ be a finite nonempty label set, and let $d,n,N$ be positive integers. A fixed measurable encoder maps each input to a row-vector embedding $Z\in\mathbb R^d$. Fix a symmetric positive-semidefinite matrix $M\in\mathbb R^{d\times d}$ and constants $L>0$ and $\xi>0$. Define
\[
K_M(z,z')=\exp\!\left[-\left(\frac{\sqrt{(z-z')M(z-z')^\top}}{L}\right)^{1/\xi}\right].
\]

Let $\widetilde{\mathcal R}=((\widetilde Z_j,\widetilde y_j))_{j=1}^N$ be an indexed reference sample in $\mathbb R^d\times\mathcal Y$, independent of the entire vector $((Z_i,y_i))_{i=1}^{n+1}$ of calibration and test observations. The reference observations are separate from, and not reused as, calibration or test observations; distinct observations may have identical embedding values. Conditional on $\widetilde{\mathcal R}$, the $n$ calibration observations together with the test observation $(Z_{n+1},y_{n+1})$ are jointly exchangeable.

Fix integers $1\le m_{\rm knn},m_{\rm clr}\le N$, a temperature $\tau>0$, and constants $\alpha\in(0,1)$ and $\lambda\in[0,1]$. Set
\[
\alpha_{\rm knn}=(1-\lambda)\alpha,
\qquad
\alpha_{\rm clr}=\lambda\alpha.
\]
The encoder and all these parameters are fixed independently of the calibration and test data. For each query embedding, order reference observations by decreasing kernel similarity, breaking ties by increasing reference index.

For an input $Z$, let $L_k(Z)$ be the set of distinct labels among its first $k$ reference neighbors, for $1\le k\le m_{\rm knn}$, and let $L_\infty(Z)=\mathcal Y$. Define
\[
S_{\rm knn}(Z,y)=\min\{k\in\{1,\ldots,m_{\rm knn}\}\cup\{\infty\}:y\in L_k(Z)\}.
\]
Thus the score is $+\infty$ if the label does not appear among the first $m_{\rm knn}$ neighbors.

For the contrastive score, let $Q(Z)\subseteq\{1,\ldots,N\}$ be the indices of the first $m_{\rm clr}$ reference neighbors, and let $A(Z)$ be the embedding of the first reference neighbor. For $j\in Q(Z)$ define
\[
d_M(A(Z),\widetilde Z_j)=2(1-K_M(A(Z),\widetilde Z_j)),
\]
\[
\ell(Z,\widetilde Z_j)
=-\log\frac{\exp(-d_M(A(Z),\widetilde Z_j)/\tau)}{\sum_{k\in Q(Z)}\exp(-d_M(A(Z),\widetilde Z_k)/\tau)}.
\]
Define
\[
S_{\rm clr}(Z,y)=\min\{\ell(Z,\widetilde Z_j):j\in Q(Z),\ \widetilde y_j=y\},
\]
with value $+\infty$ if the set in this minimum is empty.

For each $b\in\{\mathrm{knn},\mathrm{clr}\}$, put
\[
r_b=\lceil(1-\alpha_b)(n+1)\rceil,
\]
and define $q_b$ to be the $r_b$-th order statistic, counting multiplicities, of the $n+1$ extended-real values
\[
S_b(Z_1,y_1),\ldots,S_b(Z_n,y_n),+\infty.
\]
Equivalently, use the $r_b$-th calibration score when $r_b\le n$, and set $q_b=+\infty$ when $r_b=n+1$. All score comparisons use the extended-real order, including $+\infty\le+\infty$.

Set
\[
C_{\rm knn}(Z)=L_{q_{\rm knn}}(Z),
\qquad
C_{\rm clr}(Z)=\{y\in\mathcal Y:S_{\rm clr}(Z,y)\le q_{\rm clr}\},
\]
and
\[
C_{\rm mix}(Z)=C_{\rm knn}(Z)\cap C_{\rm clr}(Z).
\]

## Task

Prove the marginal coverage bounds
\[
\Pr\{y_{n+1}\in C_{\rm knn}(Z_{n+1})\}\ge1-\alpha_{\rm knn}
\]
and
\[
\Pr\{y_{n+1}\in C_{\rm mix}(Z_{n+1})\}
\ge1-\alpha_{\rm knn}-\alpha_{\rm clr}=1-\alpha.
\]

Additionally, under the assumptions that the $n+1$ k-NN rank scores are pairwise distinct almost surely and that $q_{\rm knn}\le m_{\rm knn}$ almost surely, prove
\[
\Pr\{y_{n+1}\in C_{\rm knn}(Z_{n+1})\}
\le1-\alpha_{\rm knn}+\frac1{n+1}.
\]
All displayed probabilities are over the joint reference, calibration, and test experiment.
