# Problem

## Setup

Let \(\mathcal T\) be a finite rooted directed tree. Its root is denoted by \(0\) and has fixed state \(X_0=x_0\). Let \(S\) be the set of latent internal vertices and \(L\) the set of observed leaves. For a nonroot vertex \(v\), write \(\operatorname{pa}(v)\) for its parent. The observation at leaf \(\ell\) is the fixed value \(y_\ell\).

For every \(s\in S\), let \(P_s(\cdot\mid x_{\operatorname{pa}(s)})\) be a prior transition kernel and let \(Q_s^\theta(\cdot\mid x_{\operatorname{pa}(s)})\) be a variational transition kernel satisfying
\[
Q_s^\theta(\cdot\mid x_{\operatorname{pa}(s)})
 \ll P_s(\cdot\mid x_{\operatorname{pa}(s)}).
\]
The full variational law is the tree-factorized law
\[
Q^\theta(dx_S)=\prod_{s\in S}
 Q_s^\theta(dx_s\mid x_{\operatorname{pa}(s)}).
\]
Choose measurable Radon-Nikodym derivatives and define the internal local costs
\[
C_s^\theta
 =\log\frac{dQ_s^\theta(\cdot\mid X_{\operatorname{pa}(s)})}
 {dP_s(\cdot\mid X_{\operatorname{pa}(s)})}(X_s).
\]
If \(p_\ell(\cdot\mid x_{\operatorname{pa}(\ell)})\) is the observation density at leaf \(\ell\), define
\[
C_\ell=-\log p_\ell(y_\ell\mid X_{\operatorname{pa}(\ell)}).
\]
For parameter values for which these local expectations are finite, define the full-tree negative evidence lower bound
\[
J(\theta)=\mathbb E_{Q^\theta}\left[
 \sum_{s\in S}C_s^\theta+\sum_{\ell\in L}C_\ell
\right].
\]

Let \(\Gamma\) be any distribution on nonempty subsets of \(L\), and draw \(B\sim\Gamma\). Define
\[
A(B)=\{s\in S:\text{for some }\ell\in B,
 s\text{ lies on the unique path from }0\text{ to }\ell\},
\qquad A_0(B)=A(B)\cup\{0\}.
\]
Set
\[
\pi_s=\mathbb P_{B\sim\Gamma}\{s\in A(B)\},
\qquad
\rho_\ell=\mathbb P_{B\sim\Gamma}
 \{\operatorname{pa}(\ell)\in A_0(B)\},
\]
and assume \(\pi_s>0\) for every \(s\in S\) and \(\rho_\ell>0\) for every \(\ell\in L\).

Conditional on \(B\), simulate only the activated internal vertices according to
\[
Q_{A(B)}^\theta(dx_{A(B)})
 =\prod_{s\in A(B)}Q_s^\theta
 (dx_s\mid x_{\operatorname{pa}(s)}),
\]
and form the loss
\[
\widehat J_B(\theta)
 =\sum_{s\in A(B)}\frac{C_s^\theta}{\pi_s}
 +\sum_{\ell:\operatorname{pa}(\ell)\in A_0(B)}
 \frac{C_\ell}{\rho_\ell}.
\]

## Task

Prove that this path-subsampled loss is unbiased for the full-tree objective:
\[
\mathbb E_{B\sim\Gamma}\left[
 \mathbb E_{Q_{A(B)}^\theta}[\widehat J_B(\theta)]
\right]=J(\theta).
\]
