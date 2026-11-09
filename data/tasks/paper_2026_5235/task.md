# Problem

## Setup

Let K and n be positive integers and consider a K-armed stochastic bandit. At each round the learner chooses an arm and then observes only that arm's next reward. For each arm j, the local rewards \(Y_{j,1},Y_{j,2},\ldots\) are i.i.d. with continuous CDF \(F_j\) and density \(f_j\). The arm distributions and the numerical parameters below are held fixed when the horizon n varies.

Let \(0<\underline\alpha<\alpha<\overline\alpha<1\), and define
\[
a_j=F_j^{-1}(\alpha/2),\qquad b_j=F_j^{-1}(1-\alpha/2),
\]
where \(H^{-1}(p)=\inf\{x:H(x)\ge p\}\). Define the score
\[
s(y;\ell,u)=\max\{\ell-y,\,y-u\},
\]
and let \(G_j\) be the CDF of \(s(Y_{j,1};a_j,b_j)\). For \(\beta\in[\underline\alpha,\overline\alpha]\), put
\[
c_j(\beta)=G_j^{-1}(1-\beta),\qquad V_j(\beta)=b_j+c_j(\beta),\qquad v_j=V_j(\alpha)=b_j.
\]
Assume that A is the unique maximizer of \(v_j\). For \(j\ne A\), let \(\Delta_j=v_A-v_j\), and define
\[
R_n=\sum_{j\ne A}\Delta_j\,\mathbb E[T_j(n)],
\]
where \(T_j(n)\) is the number of pulls of arm j through time n.

For each local time \(s\ge2\), let \(\widehat F_{j,s-1}\) be the empirical CDF of the first s-1 rewards from arm j, and set
\[
\widehat a_{j,s}=\widehat F_{j,s-1}^{-1}(\alpha/2),\qquad
\widehat b_{j,s}=\widehat F_{j,s-1}^{-1}(1-\alpha/2).
\]
Rescore those same s-1 rewards using \(s(Y_{j,i};\widehat a_{j,s},\widehat b_{j,s})\). Let \(\widehat c_{j,s}(\beta)\) be the lower empirical \((1-\beta)\)-quantile of these recomputed scores, and define
\[
\widehat V_{j,s}=\widehat b_{j,s}+\widehat c_{j,s}(\beta_{j,s}).
\]

The levels are updated on each arm's local observation sequence. Start with \(\beta_{j,2}\in[\underline\alpha,\overline\alpha]\). Let \(\eta_{j,s}\) be finite step sizes, chosen measurably using the rewards already observed from arm j before its s-th pull. The initial level is likewise available before the second reward. Independent algorithmic randomness may also be used. After observing \(Y_{j,s}\), for \(s\ge2\), set
\[
e_{j,s}=\mathbf1\{s(Y_{j,s};\widehat a_{j,s},\widehat b_{j,s})>\widehat c_{j,s}(\beta_{j,s})\},
\]
\[
J_s=[\underline\alpha,\overline\alpha]\cap
\left[\alpha-\lambda\sqrt{\frac{\log s}{s}},
\alpha+\lambda\sqrt{\frac{\log s}{s}}\right],\qquad
\beta_{j,s+1}=\Pi_{J_s}\bigl(\beta_{j,s}+\eta_{j,s}(\alpha-e_{j,s})\bigr),
\]
where \(\Pi_{J_s}\) is nearest-point projection onto the nonempty closed interval \(J_s\). These updates also apply during initialization whenever the required local observations are available.

Assume there are common constants \(0<f_{\min}\le f_{\max}<\infty\), \(g_{\min}>0\), \(r_y>0\), and \(r_s>0\) such that, for every arm j and every \(\beta\in[\underline\alpha,\overline\alpha]\), the reward density satisfies \(f_{\min}\le f_j(x)\le f_{\max}\) on both intervals
\[
[a_j-c_j(\beta)-r_y,\ a_j-c_j(\beta)+r_y],\qquad
[b_j+c_j(\beta)-r_y,\ b_j+c_j(\beta)+r_y].
\]
Assume also that the score density is at least \(g_{\min}\) on
\[
[c_j(\beta)-r_s,\ c_j(\beta)+r_s]
\]
for every such j and beta. Let
\[
h_{\min}=\min\{f_{\min},g_{\min}\},\qquad
\rho=\min\{r_s,r_y/2\}.
\]

Let \(b_0=64/h_{\min}\). Choose parameters \(b\ge b_0\) and \(0<\lambda\le bg_{\min}/4\), and initialize each arm with
\[
s_0=\left\lceil\frac{b^2\log n}{16\rho^2}\right\rceil\vee2
\]
pulls. Afterwards, at time t, choose an arm maximizing
\[
\widehat V_{j,T_j(t-1)+1}+b\sqrt{\frac{\log t}{T_j(t-1)}}.
\]
Ties are resolved measurably using observed history and, if desired, independent algorithmic randomness. Assume \(n\ge Ks_0\) and, for each \(j\ne A\), \(r_y\ge\Delta_j/4\) and \(r_s\ge\Delta_j/4\).

## Task

Prove that for every suboptimal arm \(j\ne A\), there is a finite constant \(B_j\), independent of n, such that for every horizon satisfying the stated conditions,
\[
\mathbb E[T_j(n)]\le\frac{4b^2\log n}{\Delta_j^2}+B_j.
\]
Consequently, prove
\[
R_n\le\sum_{j\ne A}\frac{4b^2\log n}{\Delta_j}+O(1),
\]
where the \(O(1)\) term is independent of n.
