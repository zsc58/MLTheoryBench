# Reference Proof

## Proof Structure

Condition on the covariate to identify and attain the Bayes routing risk, decompose the conditional surrogate risk into an entropy baseline and categorical and Bernoulli KL divergences, identify the population surrogate infimum, bound plug-in routing regret in all four action-type cases, and apply Pinsker's and Jensen's inequalities.

## Complete Proof

### 1. Conditional probabilities and the Bayes risk

Choose measurable versions
\[
\pi_k(x)=\Pr(Y=k\mid X=x),\qquad
\rho_j(x)=\Pr(M_j=Y\mid X=x)=\mathbb E[T_j\mid X=x].
\]
These are conditional probabilities of finitely many events. After modification on an irrelevant null set, take \(\pi(x)\in\Delta^K\) and \(\rho(x)\in[0,1]^J\) everywhere. No independence assumption is used.

For any measurable policy \((h,r)\), conditioning on \(X=x\) gives
\[
R_\perp(h,r\mid x)
=\mathbf1\{r(x)=0\}(1-\pi_{h(x)}(x))
+\sum_{j=1}^J\mathbf1\{r(x)=j\}(1-\rho_j(x)).
\]
Thus predicting class \(k\) has conditional loss \(1-\pi_k(x)\), and deferring to expert \(j\) has conditional loss \(1-\rho_j(x)\). Put
\[
a(x)=\max_k\pi_k(x),\qquad b(x)=\max_j\rho_j(x).
\]
A Bayes policy predicts a maximizing class if \(a(x)\ge b(x)\), and otherwise selects a maximizing expert. Finite maxima with fixed tie-breaking are measurable, so this policy belongs to the domain of the infimum and attains it. Consequently,
\[
R_\perp^*(x)=1-\max\{a(x),b(x)\},\qquad
\mathcal E_\perp^*=\mathbb E[R_\perp^*(X)].
\]

### 2. Exact surrogate excess and its population infimum

For finite probability vectors define
\[
\operatorname{KL}(v\|w)=\sum_i v_i\log\frac{v_i}{w_i},
\]
with zero-mass terms equal to zero and a term equal to \(+\infty\) when \(v_i>0=w_i\). This divergence is nonnegative: if it is finite, \(-\log t\ge1-t\) gives
\[
\operatorname{KL}(v\|w)
\ge\sum_{i:v_i>0}(v_i-w_i)\ge0;
\]
the infinite case is immediate.

Write
\[
H(v)=-\sum_i v_i\log v_i,\qquad
H_B(t)=-t\log t-(1-t)\log(1-t),
\]
using \(0\log0=0\), and define
\[
A(x)=\operatorname{KL}(\pi(x)\|p(x)),\qquad
B_j(x)=\operatorname{KL}(\operatorname{Bern}(\rho_j(x))\|\operatorname{Bern}(u_j(x))).
\]
Conditioning the nonnegative loss on \(X\) and expanding its finite sums gives
\[
\begin{aligned}
R_{\rm dec}(p,u\mid x)
&=-\sum_k\pi_k(x)\log p_k(x)\\
&\quad-\frac{\lambda}{J}\sum_j\bigl[\rho_j(x)\log u_j(x)+(1-\rho_j(x))\log(1-u_j(x))\bigr]\\
&=H(\pi(x))+\frac{\lambda}{J}\sum_j H_B(\rho_j(x))
+A(x)+\frac{\lambda}{J}\sum_jB_j(x).
\end{aligned}
\]
The identities hold also at endpoints under the stated loss conventions. In conditional sums, a zero probability multiplying an infinite loss contributes zero.

Let
\[
H_0(x)=H(\pi(x))+\frac{\lambda}{J}\sum_jH_B(\rho_j(x)),\qquad
S(x)=A(x)+\frac{\lambda}{J}\sum_jB_j(x).
\]
Nonnegativity of KL against uniform distributions gives \(H(\pi(x))\le\log K\) and \(H_B(\rho_j(x))\le\log2\). Therefore
\[
0\le H_0(x)\le\log K+\lambda\log2.
\]
Every measurable estimate has risk at least \(\mathbb E H_0(X)\). The measurable choice \(p=\pi,u=\rho\) is admissible in the closed probability domains and has all KL terms zero. It attains this lower bound. Hence
\[
\mathcal E_{\rm dec}^*=\mathbb E H_0(X)<\infty,
\qquad
\mathcal E_{\rm dec}(p,u)-\mathcal E_{\rm dec}^*=\mathbb E S(X).
\]
This is an extended-real equality with a finite quantity subtracted, so no undefined difference of infinities occurs.

### 3. Plug-in regret in all action-type cases

Fix an input outside the null set used above and suppress its argument. Let \(k_*\) maximize \(\pi_k\), \(j_*\) maximize \(\rho_j\), \(\widehat k\) maximize \(p_k\), and \(\widehat j\) maximize \(u_j\). Define
\[
e_c=\max_k|p_k-\pi_k|,\qquad e_e=\max_j|u_j-\rho_j|,
\qquad
\delta_\perp=R_\perp(f_{p,u}\mid x)-R_\perp^*(x).
\]

If both policies predict, then
\[
\delta_\perp=\pi_{k_*}-\pi_{\widehat k}
=(\pi_{k_*}-p_{k_*})+(p_{k_*}-p_{\widehat k})+(p_{\widehat k}-\pi_{\widehat k})
\le2e_c.
\]

If the Bayes policy defers and the plug-in policy predicts, then \(p_{\widehat k}\ge u_{\widehat j}\ge u_{j_*}\), so
\[
\delta_\perp=\rho_{j_*}-\pi_{\widehat k}
=(\rho_{j_*}-u_{j_*})+(u_{j_*}-p_{\widehat k})+(p_{\widehat k}-\pi_{\widehat k})
\le e_e+e_c.
\]

If both policies defer, then \(u_{\widehat j}\ge u_{j_*}\), so
\[
\delta_\perp=\rho_{j_*}-\rho_{\widehat j}
=(\rho_{j_*}-u_{j_*})+(u_{j_*}-u_{\widehat j})+(u_{\widehat j}-\rho_{\widehat j})
\le2e_e.
\]

If the Bayes policy predicts and the plug-in policy defers, the true utilities satisfy \(a\ge b\), including equality. The plug-in ordering gives \(u_{\widehat j}>p_{\widehat k}\ge p_{k_*}\), and therefore
\[
\delta_\perp=\pi_{k_*}-\rho_{\widehat j}
=(\pi_{k_*}-p_{k_*})+(p_{k_*}-u_{\widehat j})+(u_{\widehat j}-\rho_{\widehat j})
\le e_c+e_e.
\]
Thus every case, including class-expert ties for the Bayes policy, satisfies
\[
\delta_\perp(x)\le2\max\{e_c(x),e_e(x)\}.
\]

### 4. Pinsker bounds with the correct expert maximum

The standard-independent Pinsker inequality for finite probability distributions, using natural logarithms, is
\[
\frac12\|v-w\|_1\le\sqrt{\frac12\operatorname{KL}(v\|w)}.
\]
It remains valid with infinite KL. Applied to the categorical distributions \(\pi(x),p(x)\), it yields
\[
e_c(x)\le\|\pi(x)-p(x)\|_1\le\sqrt{2A(x)}.
\]
For Bernoulli distributions their total variation distance equals the absolute difference of their parameters. Applying Pinsker to each pair therefore gives
\[
|u_j(x)-\rho_j(x)|\le\sqrt{B_j(x)/2}.
\]
Taking the maximum only after this coordinatewise inequality gives
\[
e_e(x)\le\sqrt{\frac12\max_jB_j(x)}
\le\sqrt{\frac12\sum_jB_j(x)}.
\]
All distributions used here are valid probability distributions, including when their parameters lie at endpoints. Since \(\lambda/J>0\) and all KL terms are nonnegative,
\[
e_c(x)\le\sqrt{2S(x)},\qquad
e_e(x)\le\sqrt{\frac{J}{2\lambda}S(x)}.
\]
Combining with the routing estimate yields
\[
\delta_\perp(x)
\le\max\left\{2\sqrt2,\sqrt{\frac{2J}{\lambda}}\right\}\sqrt{S(x)}.
\]

### 5. Population transfer and consequences

Let \(C=\max\{2\sqrt2,\sqrt{2J/\lambda}\}\). If \(\mathcal E_{\rm dec}(p,u)=+\infty\), its excess is infinite whereas the defer-risk excess lies in \([0,1]\), so the desired inequality is immediate.

Otherwise \(S(X)\) is nonnegative and integrable. Jensen's inequality for the concave square-root function states that \(\mathbb E\sqrt Z\le\sqrt{\mathbb E Z}\) for a nonnegative integrable random variable \(Z\). Its hypotheses hold for \(Z=S(X)\); in particular \(\sqrt Z\le1+Z\) is integrable. Thus
\[
\begin{aligned}
\mathcal E_\perp(f_{p,u})-\mathcal E_\perp^*
&=\mathbb E\delta_\perp(X)\\
&\le C\,\mathbb E\sqrt{S(X)}\\
&\le C\sqrt{\mathbb E S(X)}\\
&=\max\left\{2\sqrt2,\sqrt{\frac{2J}{\lambda}}\right\}
\sqrt{\mathcal E_{\rm dec}(p,u)-\mathcal E_{\rm dec}^*}.
\end{aligned}
\]
For a fixed distribution and fixed \(K,J,\lambda\), this bound sends any sequence with surrogate excess tending to zero to a sequence with defer-risk excess tending to zero. If \(\lambda/J=c>0\) is fixed across expert-pool sizes, the displayed constant becomes \(\max\{2\sqrt2,\sqrt{2/c}\}\), independent of \(J\).

## Obligation Closure and Source Notes

The measurable Bayes minimizer is constructed in Section 1. The conditional decomposition, finite entropy baseline, and population infimum are established in Section 2. All four routing cases, including ties, are derived in Section 3. Section 4 states and correctly applies the standard-independent Pinsker inequality, and Section 5 states and verifies the hypotheses of Jensen's inequality and handles infinite risk. There are no unresolved proof obligations.

The source's strict comparison in the Bayes-predicts case at L000854 is locally corrected to a non-strict comparison, as required by its own tie convention. The previous reference proof's inequality bounding the maximum expert error by every individual expert KL is a separate construction error, corrected by taking the maximum and then the sum as in the source at L000872-L000887. Endpoint log-loss conventions are ordinary definition closure, not a substantive source repair.
