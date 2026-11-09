# Reference Proof

## Proof Structure

The direction-uniform representation, including its higher-order remainder property, is a premise. Work on the event that the estimated direction belongs to its domain and on the probability-one event of simultaneous validity. Evaluate the representation there, then use the exact identity obtained by adding and subtracting the population quantile at the estimated direction.

## Theorem-Critical Obligations

1. The population and empirical quantiles are finite, and their evaluations at a measurable direction are measurable.
2. The local density denominator is finite, measurable, and strictly positive wherever it is used.
3. The representation holds on a common probability-one event for all local directions, so substitution at a sample-dependent direction is legitimate.
4. The algebra produces the three terms with the stated signs and evaluation points.
5. The event on which the resulting identity is defined and valid has probability tending to one.

The proof below closes these obligations. Establishing a uniform Bahadur representation or its assumed higher-order remainder property is not an obligation of this task. In particular, the proof does not infer either property from local uniform CDF convergence or from a fixed-direction external quantile theorem.

## Complete Proof

Because each projected loss is a finite real random variable and \(0<\alpha<1\), its CDF tends to zero and one at the two ends of the real line. Thus every population quantile in the setup is finite. The empirical quantile is the \(\lceil n\alpha\rceil\)-th order statistic of the finite projected observations, so it is finite as well.

For completeness, \(F(w,t)\) is jointly measurable: its integrand \(\mathbf 1\{-w^\top x\le t\}\) is jointly measurable, and integration against the fixed distribution preserves measurability. The generalized-inverse quantile is measurable in \(w\), since for each real \(a\),
\[
\{w:q_\alpha(w)<a\}
=\bigcup_{t\in\mathbb Q,\,t<a}\{w:F(w,t)\ge\alpha\}.
\]
The empirical quantile is a measurable order statistic of jointly measurable projected observations. On \(U\), differentiability implies
\[
f_w(q_\alpha(w))
=\lim_{m\to\infty}m\bigl[F(w,q_\alpha(w)+1/m)-F(w,q_\alpha(w))\bigr],
\]
so this density evaluation is measurable. Its value is finite and at least \(c>0\) by assumption. Joint measurability of \(r_n\) makes \(r_n(\widehat w)\) measurable on \(\{\widehat w\in U\}\). Consequently, all terms used below are well defined and measurable on that event. Local terms may be assigned an arbitrary measurable value off the event if global random variables are desired; no identity is asserted there.

Let \(E_n=\{\widehat w\in U\}\). By assumption, \(\mathbb P(E_n)\to1\). For each \(n\), let \(A_n\) be the probability-one event on which the assumed representation holds simultaneously for every \(w\in U\). On \(A_n\cap E_n\), substitute \(\widehat w\) into that representation to obtain
\[
\widehat q_\alpha(\widehat w)-q_\alpha(\widehat w)
=\frac{\alpha-F_n(\widehat w,q_\alpha(\widehat w))}{f_{\widehat w}(q_\alpha(\widehat w))}+r_n(\widehat w).
\]
This substitution requires no independence between \(\widehat w\) and the observations: the premise holds simultaneously over its direction domain.

Also, identically on this event,
\[
\widehat q_\alpha(\widehat w)-q_\alpha(w_0)
=\bigl[q_\alpha(\widehat w)-q_\alpha(w_0)\bigr]
+\bigl[\widehat q_\alpha(\widehat w)-q_\alpha(\widehat w)\bigr].
\]
Substitution gives
\[
\widehat q_\alpha(\widehat w)-q_\alpha(w_0)
=\underbrace{q_\alpha(\widehat w)-q_\alpha(w_0)}_{\Delta_{\rm dir}}
+\underbrace{\frac{\alpha-F_n(\widehat w,q_\alpha(\widehat w))}{f_{\widehat w}(q_\alpha(\widehat w))}}_{\Delta_{\rm emp}}
+\underbrace{r_n(\widehat w)}_{\Delta_{\rm rem}}.
\]
The first term compares two population quantiles and is the population directional movement. The second is the empirical-CDF linear term evaluated at the perturbed direction and its population quantile. The third is the assumed Bahadur remainder. These interpretations assert neither independence nor probabilistic orthogonality of the terms.

Finally, \(\mathbb P(A_n\cap E_n)=\mathbb P(E_n)\to1\). Hence the displayed decomposition holds with probability tending to one. No consistency conclusion for the total quantile error or quantitative \(n^{-3/4}\) remainder bound is claimed.
