# Problem

## Setup

Let \(\mathcal A\) be a finite or countably infinite set, let \(r\in\mathcal A\) be fixed before observing data, and let \(X_1,X_2,\ldots\) be i.i.d. from an unknown categorical law \(P\). The filtration is \(\mathcal F_t=\sigma(X_1,\ldots,X_t)\). The category set and its cardinality are not supplied to a certification procedure: its decisions may use only observed labels and observations, the target, and fixed design inputs, not information about unobserved elements of \(\mathcal A\).

Write \(N_t(a)=\sum_{i\le t}{\bf1}\{X_i=a\}\), \(\widehat p_t(a)=N_t(a)/t\), and \(\mathcal A_t=\{a:N_t(a)>0\}\). Put \(p_a=P(X=a)\) and \(p_{(2)}=\sup_{a\in\mathcal A\setminus\{r\}}p_a\), with \(p_{(2)}=0\) when \(\mathcal A\setminus\{r\}\) is empty. The hypotheses are \(H_{0,r}:p_r\le p_{(2)}\) and \(H_{1,r}:p_r>p_{(2)}\).

Fix \(\varepsilon\in(0,1)\) before observing data. All grids and weights below are deterministic design inputs fixed before observing data. For each \(a\ne r\) and \(\lambda\in(0,1)\), define
\[
E_t^{(r,a)}(\lambda)=\prod_{i=1}^t\bigl[1+\lambda({\bf1}\{X_i=r\}-{\bf1}\{X_i=a\})\bigr]
=(1+\lambda)^{N_t(r)}(1-\lambda)^{N_t(a)}.
\]
Let \(\Lambda_{pw}\subset(0,1)\) be finite with positive weights \(w_\lambda\) summing to at most one, and set \(E_t^{(r,a)}=\sum_{\lambda\in\Lambda_{pw}}w_\lambda E_t^{(r,a)}(\lambda)\). At time \(t\), when an observed non-target label exists, let \(\widehat a_t\) maximize \(N_t(a)\) over \(\mathcal A_t\setminus\{r\}\), with ties broken using the observed history.

Let \(\Lambda_r\subset(0,\infty)\) be finite with positive weights \(v_\lambda\) summing to at most one. For \(q\in(0,1]\), define \(\Lambda_r(q)=\{\lambda\in\Lambda_r:\lambda<1/q\}\) and
\[
M_t(q)=\sum_{\lambda\in\Lambda_r(q)}v_\lambda\prod_{i=1}^t[1+\lambda({\bf1}\{X_i=r\}-q)].
\]
Empty sums are zero. Set
\[
L_t=\sup\bigl(\{0\}\cup\{q\in(0,\widehat p_t(r)]:M_t(q)\ge3/\varepsilon\}\bigr),\qquad
U_t=\min\{u\in(0,1]:u^{-1}(1-u)^t\le\varepsilon/3\}.
\]
Define the pairwise check \(B_t\) to be true if \(\mathcal A_t\setminus\{r\}\) is empty, and otherwise to be the condition \(E_t^{(r,\widehat a_t)}\ge3/\varepsilon\). The procedure stops at
\[
\tau=\inf\{t\ge1:B_t\text{ is true and }L_t>U_t\},
\]
where \(\inf\emptyset=\infty\).

For the rate result, assume additionally that \(\delta=p_r-p_{(2)}>0\), that \(\Lambda_{pw}\) contains a point in \([\delta/8,\delta/4]\), and that \(\Lambda_r\) contains a point in \([1/32,1/16]\). The weights of these two selected points are at least a fixed universal constant \(\kappa>0\), independent of \(\delta,p_r,\varepsilon\) and the remaining grid design.

For the lower bound, for \(p\in(0,1/2]\) and \(0<\delta<p\), let
\[
\mathcal P(p,\delta)=\{P:p_r=p,\ p_{(2)}\le p-\delta\}.
\]
A sequential certifier is a sequence of \(\mathcal F_t\)-measurable decisions \(D_t\in\{0,1\}\), using the information allowed above, where \(D_t=1\) means certification of \(r\). Its stopping time is \(\tau'=\inf\{t\ge1:D_t=1\}\), with \(\inf\emptyset=\infty\). It has level \(\varepsilon\) if \(\sup_{P\in H_{0,r}}P(\tau'<\infty)\le\varepsilon\).

## Task

Prove the following integrated theorem. For every prespecified \(\varepsilon\in(0,1)\), the procedure above has level-\(\varepsilon\) anytime validity uniformly over all countable category sets and arbitrary data-dependent stopping. If \(\delta>0\) and the grid and weight conditions hold, then \(\tau<\infty\) almost surely and, for a universal constant \(C\),
\[
\mathbb E_P\tau\le C\left[\frac{\log(3/\varepsilon)+\log(1/\delta)}{\delta^2}+\frac{\log(3/\varepsilon)+\log(1/p_r)}{p_r}\right],
\]
independently of \(|\mathcal A|\). The constant may depend only on the fixed universal weight floor \(\kappa\), not on \(P,\delta,p_r,\varepsilon\) or the remaining grid design.

Conversely, there is a universal \(c>0\) such that every level-\(\varepsilon\) certifier that stops almost surely with finite expectation for every \(P\in\mathcal P(p,\delta)\) satisfies
\[
\sup_{P\in\mathcal P(p,\delta)}\mathbb E_P\tau'\ge c\log(1/\varepsilon)\left(\frac p{\delta^2}+\frac1p\right)
\]
whenever \(\mathcal A\) is countably infinite or has at least \(\lceil(1-p)/(p-\delta)\rceil+2\) non-target labels.
