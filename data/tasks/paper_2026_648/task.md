# Problem

## Setup

Let $k\ge2$ and $n\ge2$ be integers, and let $m=n^{k-1}$. Let $T\in\mathbb R^{n\times\cdots\times n}$ be a fixed symmetric order-$k$ tensor. Its mode-1 unfolding indexes rows by the first coordinate and columns by the remaining ordered $(k-1)$-tuples. Write its compact singular value decomposition as
\[
A=\operatorname{Unfold}(T)=U\Sigma V^\top\in\mathbb R^{n\times m},
\]
where $1\le r=\operatorname{rank}(A)\le n$, $U$ and $V$ have orthonormal columns, the singular values satisfy $\sigma_1\ge\cdots\ge\sigma_r>0$, and $\kappa=\sigma_1/\sigma_r$. The map $\operatorname{fold}$ is the inverse of this unfolding.

Assume $A$ is $(\mu_1,\mu_2)$-incoherent:
\[
\max_i\|e_i^\top U\|_2^2\le\frac{\mu_1r}{n},\qquad
\max_\ell\|e_\ell^\top V\|_2^2\le\frac{\mu_2r}{m}.
\]
Assume also tensor incoherence with the same parameters: for each mode $j$, write the compact singular value decomposition of its unfolding as $U^{(j)}\Sigma^{(j)}(V^{(j)})^\top$, with rank $r_j$, and require
\[
\max_i\|e_i^\top U^{(j)}\|_2^2\le\frac{\mu_1r_j}{n},\qquad
\max_\ell\|e_\ell^\top V^{(j)}\|_2^2\le\frac{\mu_2r_j}{m}.
\]
Here each mode unfolding indexes its columns by the other ordered coordinates.

Let $0<p,q\le1$. For each $\ell\in[m]$ and $1\le i\le j\le n$, draw independent $\delta_{i\ell j}\sim\operatorname{Bernoulli}(p)$ and set $\delta_{j\ell i}=\delta_{i\ell j}$. The wedge observations reveal the two entries $A_{i\ell},A_{j\ell}$ whenever $\delta_{i\ell j}=1$. Define the symmetric inverse-probability estimator
\[
Z_{ij}=Z_{ji}=\frac1p\sum_{\ell=1}^m\delta_{i\ell j}A_{i\ell}A_{j\ell}.
\]
Let $\widehat U$ contain orthonormal eigenvectors associated with the $r$ largest eigenvalues of $Z$, chosen from $Z$ alone with a fixed deterministic rule for ties, and write $Q=\widehat U\widehat U^\top$.

Independently of all wedge indicators, include each ordered tensor index in $[n]^k$ independently with probability $q$. Let $\Omega$ be this set, let $P_\Omega$ retain the entries indexed by $\Omega$ and zero the rest, and set
\[
Y=\operatorname{Unfold}(q^{-1}P_\Omega(T)),\qquad
\widehat T=\operatorname{fold}\!\left(QY(Q\otimes\cdots\otimes Q)\right),
\]
where the Kronecker product has $k-1$ copies of $Q$.

For a matrix, $\|\cdot\|$ denotes its operator norm and
\[
\|M\|_{2,\infty}=\max_i\|e_i^\top M\|_2.
\]
The Frobenius norm $\|\cdot\|_F$ is the square root of the sum of squared entries, for either matrices or tensors.

## Task

Prove that there are universal constants $c,C_0,C>0$ such that, for every $a\ge2$, if
\[
p\ge C_0\frac{\kappa^4a\mu_1\mu_2r^2\log n}{n^k},
\qquad
q\ge\frac{a(k-1)\log n}{n^k},
\]
then with probability at least $1-cn^{-a}$, simultaneously:

1. There exists
\[
R\in\underset{O\in\mathbb R^{r\times r},\ O^\top O=I_r}{\operatorname{argmin}}
\|\widehat UO-U\|_F
\]
such that
\[
\|\widehat UR-U\|\le C\kappa^2\sqrt{\frac{a\mu_1\mu_2r^2\log n}{pn^k}},
\qquad
\|\widehat UR-U\|_{2,\infty}\le C\kappa^2\sqrt{\frac{a\mu_1\mu_2r^2\log n}{pn^k}}\,\|U\|_{2,\infty}.
\]
2. The projected estimator satisfies
\[
\|T-\widehat T\|_F\le C\left[
 k\sqrt r\,\kappa^2\sqrt{\frac{a\mu_1\mu_2r^2\log n}{pn^k}}
 +2^k r^{3/2+k/2}\kappa^{2k}
 \sqrt{\frac{a(k-1)\mu_1^{k+1}\mu_2\log n}{qn^k}}
\right]\|T\|_F.
\]
