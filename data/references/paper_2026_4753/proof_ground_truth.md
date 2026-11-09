# Reference Proof

## Proof Structure

Decompose the empirical clipped objective around the clipped and exact population objectives. Bound the empirical-to-clipped-population deviation by two Hoeffding estimates, the clipped-to-exact mismatch by truncation, and the exact learned-to-target mismatch by a chi-square change of measure.

## Complete Proof

Let
\[
h_{\phi,\tau}(x,y)=\widehat r_\phi(x,y)-\beta\ell_\theta^\tau(x,y),\qquad
h_{\phi}(x,y)=\widehat r_\phi(x,y)-\beta\ell_\theta(x,y),
\]
and let the corresponding target integrand be \(h_*(x,y)=r^*(x,y)-\beta\ell_\theta(x,y)\). By definition,
\[
\widehat J_{n,K}^{\phi,\tau}=\frac1n\sum_{i=1}^n\frac1K\sum_{j=1}^K h_{\phi,\tau}(X_i,Y_{ij}),\quad
J^{\phi,\tau}=\mathbb E_Q h_{\phi,\tau},\quad
J^\phi=\mathbb E_Q h_\phi,\quad
J^*=\mathbb E_Q h_*.
\]
Insert the two intermediate population quantities and apply the triangle inequality:
\[
|\widehat J_{n,K}^{\phi,\tau}-J^*|\le |\widehat J_{n,K}^{\phi,\tau}-J^{\phi,\tau}|+|J^{\phi,\tau}-J^\phi|+|J^\phi-J^*|. \tag{1}
\]
Because \(0\le \widehat r_\phi\le1\) and \(|\ell_\theta^\tau|\le\tau\), every summand \(h_{\phi,\tau}\) lies in an interval of width \(1+2\beta\tau\). Conditional on the prompts, Hoeffding's inequality gives, with probability at least \(1-\delta/2\), a rollout-averaging deviation bounded by
\[
(1+2\beta\tau)\sqrt{\frac{\log(4/\delta)}{2nK}}.
\]
For the prompt average, the conditional means \(g(X)=\mathbb E[h_{\phi,\tau}(X,Y)\mid X]\) have the same range width, so Hoeffding gives, with probability at least \(1-\delta/2\),
\[
(1+2\beta\tau)\sqrt{\frac{\log(4/\delta)}{2n}}.
\]
A union bound and the triangle inequality therefore bound the first term in (1) by the sum of these two quantities.

For the clipping term, the reward parts cancel, hence
\[
J^{\phi,\tau}-J^\phi=\beta\,\mathbb E_Q[\ell_\theta-\ell_\theta^\tau],
\]
so \(|J^{\phi,\tau}-J^\phi|\le\beta\mathbb E_Q|\ell_\theta-\ell_\theta^\tau|\).

For the reward-shift term, write \(w=dQ/dP\) and \(e=\widehat r_\phi-r^*\). The KL terms cancel and \(J^\phi-J^*=\mathbb E_Q e=\mathbb E_P[we]\). Cauchy-Schwarz yields
\[
|\mathbb E_P[we]|\le\sqrt{\mathbb E_P[w^2]}\sqrt{\mathbb E_P[e^2]}
=\sqrt{1+\chi^2(Q\|P)}\,\sqrt{L_{\rm train}^{(2)}(\phi)}
=C(\theta)\sqrt{L_{\rm train}^{(2)}(\phi)}.
\]
Combining the three bounds in (1) proves the claim.
