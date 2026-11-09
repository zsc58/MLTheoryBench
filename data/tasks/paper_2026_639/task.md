# Problem

## Setup

Let n and m be positive integers, and let \(\mathcal S=\{1,\ldots,n\}\) and \(\mathcal A=\{1,\ldots,m\}\) be finite state and action sets. For every positive integer d, write
\[
\Delta_d=\{x\in\mathbb R_+^d:\mathbf 1^\top x=1\}.
\]
For every state-action pair \((s,a)\), let \(q_{sa}\in\Delta_n\) be a nominal transition row, let \(W_{sa}\) be a positive diagonal matrix, and let \(r_{sa}\in\mathbb R_+^n\). Fix \(\eta\in(0,1)\) and \(\kappa>0\), and define
\[
\mathcal Q_s=\left\{(x_a)_{a\in\mathcal A}\in(\Delta_n)^m:
\sum_{a\in\mathcal A}\|W_{sa}(x_a-q_{sa})\|_2^2\leq\kappa\right\}.
\]
For \(v\in\mathbb R^n\), define the robust Bellman operator
\[
[T(v)]_s=
\max_{\pi\in\Delta_m}\min_{(x_a)_a\in\mathcal Q_s}
\sum_{a\in\mathcal A}\pi_a x_a^\top(r_{sa}+\eta v).
\]
Let
\[
U=\frac{\max_{s,a,i}(r_{sa})_i}{1-\eta}.
\]

For \(q\in\Delta_n\), positive diagonal \(W\), \(b\in\mathbb R_+^n\), and \(\beta\geq0\), define the generalized projection value
\[
P(q,W;b,\beta)=
\min\left\{\|W(x-q)\|_2^2:x\in\Delta_n,
\ b^\top x\leq\beta\right\},
\]
with value \(+\infty\) when the feasible set is empty.

For a projection in the nontrivial regime
\(\min_i b_i\leq\beta<b^\top q\), impose the following nondegeneracy conditions on \((q,W,b)\). Put
\[
a_i=(W_{ii})^{-2},\qquad c_i=2(W_{ii})^2q_i.
\]
Require:

1. The coordinates of b are pairwise distinct. For distinct indices define
   \[
   \delta_{ij}=\frac{c_i-c_j}{b_i-b_j}.
   \]
2. For every \(I\subseteq\mathcal S\) and every i,
   \[
   2+\sum_{k\in I}a_k(c_i-c_k)\ne0.
   \]
3. For every \(I\subseteq\mathcal S\) and distinct i,j,
   \[
   2+\sum_{k\in I\setminus\{i\}}
   a_k(b_k-b_i)(\delta_{ij}-\delta_{ik})\ne0.
   \]
   The term with k=j is defined by this same formula; no \(\delta_{ii}\) is used.

For the Bellman conclusion, impose the following requirement at the value vector v in question: for every \((s,a)\), set \(b_{sa}=r_{sa}+\eta v\). If
\[
\min_i(b_{sa})_i<b_{sa}^\top q_{sa},
\]
then the three nondegeneracy conditions hold with \((q,W,b)=(q_{sa},W_{sa},b_{sa})\). No such condition is imposed on a pair for which these two quantities are equal. This requirement is at the given v, not a simultaneous requirement over all value vectors.

Complexities count exact real-arithmetic operations and comparisons, each at unit cost.

## Task

Prove the following integrated theorem.

Every generalized projection \(P(q,W;b,\beta)\), including an exact optimizer whenever it is feasible, can be computed in \(O(n^2)\) operations under the stated assumptions. Consequently, for every \(v\in[0,U]^n\) satisfying the stated Bellman requirement and every \(\varepsilon>0\), one can compute a vector \(\widehat t\in\mathbb R^n\) satisfying
\[
\|\widehat t-T(v)\|_\infty\leq\varepsilon
\]
in
\[
O\!\left(mn^3\left[1+\log\!\left(\max\left\{1,\frac{U}{\varepsilon}\right\}\right)\right]\right)
\]
operations. The constants in these operation bounds are independent of the numerical input data.
