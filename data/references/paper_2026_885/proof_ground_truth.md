# Reference Proof

## Contract and proof obligations

Fix A>0. The prior Pi_n is the law of the k-component mixture in the problem, and remains this same prior when conditioning on n-1 observations. All constants below are independent of the test prior G0. Constants may depend on A and, for the thickness calculation, c0. All assertions involving n hold for sufficiently large integer n.

We close the following obligations: (1) well-definedness and the correct leave-one-out identity; (2) a uniform finite-mixture thickness construction, including boundary atoms and weights; (3) local Hellinger entropy; (4) posterior-predictive contraction, including its denominator and probability tail; (5) the regret-Hellinger inequality; and (6) tail integration and rate substitution. No specialized external regret-Hellinger inequality is assumed.

For pmfs define
\[
H^2(p,q)=\sum_{x\ge0}(\sqrt{p(x)}-\sqrt{q(x)})^2,\qquad
\operatorname{TV}(p,q)=\tfrac12\sum_{x\ge0}|p(x)-q(x)|,
\]
and \(\chi^2(p\|q)=\sum_x(p(x)-q(x))^2/q(x)\), with the usual extended-value convention. In particular, \(H^2\le2\) and \(H^2\le2\operatorname{TV}\).

## 1. Well-definedness and leave-one-out conditioning

The sampled locations are positive almost surely, and the Dirichlet weights are positive almost surely. Consequently the hierarchical marginal probability of every data vector in \(\mathbb N_0^n\) is positive. The hierarchical posterior means therefore define a unique function on this countable observation space, with values in \([0,A]^n\). Oracle posterior means on observations of zero probability are set to zero; this does not change regret.

For any mixing measure F, direct integration gives
\[
p_F(x)\theta_F(x)=(x+1)p_F(x+1).
\]
Let \(Q_i=\Pi_n(dF\mid X_{-i})\), and define \(G_i(B)=\int F(B)Q_i(dF)\) for Borel sets B. Bayes' rule gives
\[
\widehat\theta_i
=\frac{\int\theta_F(X_i)p_F(X_i)Q_i(dF)}{\int p_F(X_i)Q_i(dF)}
=(X_i+1)\frac{p_{G_i}(X_i+1)}{p_{G_i}(X_i)}
=\theta_{G_i}(X_i).
\]
Equivalently, \(\widehat\theta_i=\int\theta_F(X_i)\Pi_n(dF\mid X^n)\). The unweighted average under Q_i is generally not the estimator. Under the test experiment, G_i is a function of X_-i and is independent of X_i.

## 2. Uniform thickness of the sampled prior

A prior is thick at (delta,r) with exponent E if every G0 admits an intermediate F with TV(p_G0,p_F)<=delta and prior mass at least exp(-E) on \(\{F':\chi^2(p_F\|p_{F'})\le r^2\}\).

We use the following standard moment-matching result, in exactly the form quoted in the source: if an integer L>2eA and two probability measures on [0,A] have equal moments of degrees 0 through L, their Poisson-mixture TV distance is at most \((2eA/L)^L\). All support and moment hypotheses will hold in this application.

Choose \(L=\lceil8\log n/\log\log n\rceil\). For each fixed A and sufficiently large n, L>2eA and \((2eA/L)^L\le1/(2n^2)\). The moment vector of G0 is in the convex hull of \(\{(t,t^2,\ldots,t^L):0\le t\le A\}\). Caratheodory's theorem therefore gives a measure \(\bar G\) with at most L+1 atoms matching these moments. Thus
\[
\operatorname{TV}(p_{G_0},p_{\bar G})\le\frac1{2n^2}.
\]
This uses L+1, correcting the source's off-by-one application of ordinary Caratheodory. Choose the absolute threshold for c0 large enough that k>=L+1 for all sufficiently large n.

Represent \(\bar G=\sum_{j=1}^k\bar w_j\delta_{\bar\lambda_j}\) by padding with zero-weight components if necessary. Put
\[
b=\frac1{4n^2},\qquad \tau=\frac1{8n^2},\qquad
\lambda_j=\max(\bar\lambda_j,b),\qquad
w_j=(1-\tau)\bar w_j+\frac\tau k,
\qquad F=\sum_{j=1}^k w_j\delta_{\lambda_j}.
\]
For sufficiently large n, b<=A, so these locations remain in [0,A]. Moreover, \(\lambda_j\ge b\), \(w_j\ge1/(8n^2k)\), and \(\sum_j|w_j-\bar w_j|\le2\tau\).

Poisson coupling gives \(\operatorname{TV}(\operatorname{Poi}(u),\operatorname{Poi}(v))\le|u-v|\): add an independent Poisson variable of mean |u-v| to the smaller-mean variable. Expanding the mixture difference and using the triangle inequality gives
\[
\operatorname{TV}\left(\sum_jw_jP_j,\sum_jv_jQ_j\right)
\le\sum_j|w_j-v_j|+\max_j\operatorname{TV}(P_j,Q_j).
\]
Consequently TV(p_barG,p_F)<=2tau+b=1/(2n^2), and TV(p_G0,p_F)<=n^-2.

Here is an explicit neighborhood with the required chi-square control. Cauchy-Schwarz, applied at each outcome and then summed, gives
\[
1+\chi^2\left(\sum_jw_jP_j\middle\|\sum_jw'_jQ_j\right)
\le\sum_j\frac{w_j^2}{w'_j}\bigl(1+\chi^2(P_j\|Q_j)\bigr)
\le(1+\chi^2(w\|w'))\max_j(1+\chi^2(P_j\|Q_j)).
\]
Direct summation of the Poisson power series gives, for v>0,
\[
1+\chi^2(\operatorname{Poi}(u)\|\operatorname{Poi}(v))
=\exp((u-v)^2/v).
\]
Let h=n^-4. Restrict each sampled location to \([\lambda_j-h,\lambda_j+h]\cap[0,A]\), and restrict the sampled weight vector to
\[
\{(1-h)w+hv:v\in\Delta^{k-1}\}.
\]
Then \(|w'_j-w_j|\le h\), \(w'_j\ge(1-h)w_j\), and, for large n,
\[
\chi^2(w\|w')\le16n^2k^2h^2,\qquad
\max_j\frac{(\lambda_j-\lambda'_j)^2}{\lambda'_j}\le8n^2h^2.
\]
Both quantities are at most 1/(4n) for sufficiently large n. Thus
\[
1+\chi^2(p_F\|p_{F'})\le(1+1/(4n))e^{1/(4n)}\le1+1/n.
\]
This bound controls the entire infinite count range and does not infer chi-square control from a small unweighted tail.

Every location interval has length at least h once h<=A. Uniformity of the Dirichlet(1,...,1) distribution on its simplex implies that the homothetic weight simplex has probability exactly h^(k-1). Independence therefore gives neighborhood mass at least
\[
(h/A)^k h^{k-1}=\exp[-O_A(k\log n)]
\ge\exp\left[-B_{A,c_0}\frac{\log^2 n}{\log\log n}\right].
\]
It follows that, for every r^2>=1/n, the thickness exponent at delta=n^-2 is at most \(B_{A,c_0}\log^2 n/\log\log n\). Taking
\[
r_n^2=B'_{A,c_0}\frac{\log^2 n}{n\log\log n}
\]
with B' sufficiently large ensures both r_n^2>=1/n and E(n^-2,r_n)<=n r_n^2.

## 3. Local entropy and tests

For \(\mathcal P_A=\{p_F:F\in\mathcal P([0,A])\}\), let N(r,S,H) be the minimum number of Hellinger balls of radius r covering S, and define
\[
N_{\rm loc}(\epsilon)=\sup_{p\in\mathcal P_A}\sup_{\rho>\epsilon}
N(\rho,\mathcal P_A\cap\{q:H(p,q)\le2\rho\},H).
\]
For K>A the exponential Markov inequality for a Poisson variable gives
\[
\sup_{F\in\mathcal P([0,A])}p_F(X\ge K)\le(eA/K)^K.
\]
Choose \(J=O_A(\log(1/\epsilon)/\log\log(1/\epsilon))\) so the tail beyond J is at most a sufficiently small absolute multiple of epsilon^2. Map p to \((\sqrt{p(0)},\ldots,\sqrt{p(J)})\). A Hellinger ball of radius 2rho maps inside a Euclidean ball of radius 2rho in dimension J+1. A maximal separated set at any fixed sufficiently small multiple of rho has at most C^(J+1) points: disjoint balls of half the separation fit inside a ball of a fixed multiple of rho. The truncated coordinates and the two uniformly bounded tails then give a proper Hellinger cover. Thus
\[
\log N_{\rm loc}(\epsilon)\le C_A\frac{\log(1/\epsilon)}{\log\log(1/\epsilon)}.
\]
The same argument works for any fixed ratio between the radius being covered and the covering radius, with a different constant. Choose \(\epsilon_n^2=D_A\log n/(n\log\log n)\) with D_A large enough.

The standard independent testing result used here is the robust Hellinger test: for densities p,q relative to a common dominating measure and d=H(p,q)>0, a test based on m iid observations has type-I error under p and worst-case type-II error over H(r,q)<=d/4 bounded by C exp(-c m d^2), for absolute c,C>0. This is the classical testing input explicitly invoked by the source; it does not assert posterior contraction by itself. Here the dominating measure is counting measure, all observations are iid, and m=n-1.

To verify its covering hypotheses, fix p in the mixture class and t>=C epsilon_n. Cover each shell
\[
2^jt\le H(p,q)<2^{j+1}t
\]
by balls of radius 2^jt/8 with centers in that shell. The preceding truncated-coordinate argument, using tails controlled at epsilon_n, gives at most exp(C_A J_n) centers per shell, where \(J_n=O_A(\log n/\log\log n)\). Each cover ball lies inside the robust testing neighborhood of its center. Taking the maximum of all center tests and summing their type-I errors over shells gives a test phi with
\[
P_p(\phi=1)\le e^{-a n t^2},\qquad
\sup_{H(p,q)>t}P_q(\phi=0)\le e^{-a n t^2},
\]
after increasing C and adjusting a>0. Indeed the sum is bounded by a constant times \(\sum_{j\ge0}\exp(C_AJ_n-c n4^jt^2)\), and n t^2 dominates J_n. Only finitely many shells are nonempty because H^2<=2.

## 4. Posterior-predictive contraction

First suppose the data density is the intermediate density p=p_F supplied by thickness. Let U be the set of mixing measures F' with chi-square(p||p_F')<=r_n^2, let E_n=E(n^-2,r_n), and let nu be the normalized restriction of Pi_n to U. In particular Pi_n(U)>=exp(-E_n).

For m=n-1 observations define \(L_q=\prod_{\ell=1}^m q(X_\ell)/p(X_\ell)\), the denominator \(D=\int L_{p_{F'}}\Pi_n(dF')\), and the numerator N_t obtained by restricting this integral to H(p,p_F')>t. By the test above, change of measure and integration give
\[
\mathbb E_p[(1-\phi)N_t]\le e^{-a n t^2}.
\]
Markov's inequality bounds the probability of \(N_t>e^{-a n t^2/2}\) and phi=0 by exp(-a n t^2/2). If p has zeros, the change-of-measure expression is an inequality in the needed direction, which suffices.

For the denominator, Jensen gives
\[
D\ge e^{-E_n}\exp\left(\sum_{\ell=1}^mY_\ell\right),\qquad
Y_\ell=\int\log\frac{p_{F'}(X_\ell)}{p(X_\ell)}\,\nu(dF').
\]
For arbitrary pmfs p,q with chi-square(p||q) finite, splitting the sum into q>=p and q<p and using log z>=1-1/z proves
\[
\mathbb E_p\left[e^{|\log(q/p)|}-1-|\log(q/p)|\right]\le\chi^2(p\|q).
\]
For q>=p the summand is q-p-p log(q/p), bounded by (p-q)^2/q; for q<p it is p^2/q-p-p log(p/q), with the same bound. Convexity and integration over nu therefore give
\[
\mathbb E_p[e^{|Y_\ell|}-1-|Y_\ell|]\le r_n^2,
\qquad \mathbb E_pY_\ell\ge-r_n^2,
\]
where the second bound uses KL(p||q)<=chi-square(p||q).

For completeness, the first inequality implies \(\mathbb E|Y_\ell|^s\le s!r_n^2\) for every integer s>=2. Centering gives \(\mathbb E|Y_\ell-\mathbb EY_\ell|^s\le2^s s!r_n^2\). Expanding the exponential and using independence yields, for |u|<1/2,
\[
\mathbb E\exp\left(u\sum_{\ell=1}^m(Y_\ell-\mathbb EY_\ell)\right)
\le\exp\left(\frac{4m r_n^2u^2}{1-2|u|}\right).
\]
Exponential Markov inequality and optimization give a lower-tail bound \(\exp[-c v^2/(m r_n^2+v)]\) for a downward deviation v. Taking v=a n t^2/8, using E_n<=n r_n^2, and requiring t^2>=C r_n^2 gives
\[
P_p\{D<e^{-a n t^2/4}\}\le e^{-b n t^2}
\]
for some b>0. Combining this with the test and numerator bounds proves
\[
P_p\left\{\Pi_n(H^2(p,p_{F'})>t^2\mid X^m)>e^{-b'nt^2}\right\}
\le e^{-b''nt^2}
\]
whenever \(t^2\ge C(\epsilon_n^2+r_n^2+1/n)\), after adjustment of constants.

Apply this assertion at squared radii jt^2 for positive integers j. The sum of exceptional probabilities is a geometric series bounded by exp(-c n t^2). Off that exceptional event, layer cake gives
\[
\int H^2(p,p_{F'})\Pi_n(dF'\mid X^m)
\le t^2\left(1+\sum_{j\ge1}e^{-b'njt^2}\right)\le C t^2.
\]
Convexity of squared Hellinger distance gives the same bound for the predictive pmf \(\widehat p=\int p_{F'}\Pi_n(dF'\mid X^m)\).

Return to p0=p_G0. By construction,
\[
\operatorname{TV}(p_0^{\otimes m},p^{\otimes m})\le m n^{-2}\le n^{-1},\qquad H^2(p_0,p)\le2n^{-2}.
\]
The triangle inequality, with squared distances bounded by twice the sum of squares, now gives
\[
P_{G_0}\{H^2(p_{G_0},\widehat p)>C t^2\}
\le n^{-1}+e^{-c n t^2}
\]
for \(t^2\ge C(\epsilon_n^2+r_n^2+1/n)\). This applies to every leave-one-out predictive pmf p_Gi, always using Pi_n.

## 5. Direct regret-Hellinger inequality

This step is derived rather than delegated to the specialized external citation. Write p=p_G0, q=p_F, a_x=theta_G0(x), and b_x=theta_F(x), using zero versions at null observations. The posterior-mean identities imply
\[
\sqrt{p(x)}\sqrt{a_x}=\sqrt{x+1}\sqrt{p(x+1)},\qquad
\sqrt{q(x)}\sqrt{b_x}=\sqrt{x+1}\sqrt{q(x+1)}.
\]
Since 0<=a_x,b_x<=A, subtraction, the triangle inequality, and \((u+v)^2\le2u^2+2v^2\) give
\[
p(x)(a_x-b_x)^2
\le8A(x+1)(\sqrt{p(x+1)}-\sqrt{q(x+1)})^2
+8A^2(\sqrt{p(x)}-\sqrt{q(x)})^2.
\]
These identities also hold at zero probabilities: the next Poisson-mixture probability is then zero as well. Summing over x<K and bounding the remaining squared error by A^2 proves, for integer K>=1,
\[
\mathbb E_p[(\theta_F(X)-\theta_{G_0}(X))^2]
\le(8AK+8A^2)H^2(p,q)+A^2p(X\ge K).
\]
The Poisson tail bound from Section 3 permits \(K=O_A(\log(1/\eta)/\log\log(1/\eta))\) with p(X>=K)<=eta, for every 0<eta<e^-e. Hence
\[
\mathbb E_{p_{G_0}}[(\theta_F(X)-\theta_{G_0}(X))^2]
\le C_A\left[\frac{\log(1/\eta)}{\log\log(1/\eta)}H^2(p_F,p_{G_0})+\eta\right].
\]

## 6. Tail integration and conclusion

The contraction tail and H^2<=2 imply, uniformly in G0 and i,
\[
\mathbb E_{G_0}H^2(p_{G_i},p_{G_0})
\le C_A(\epsilon_n^2+r_n^2+n^{-1}).
\]
Indeed, integrate the tail above its threshold up to 2; the constant exceptional probability contributes at most 2/n, and the exponential part contributes O(1/n).

Condition on X_-i and apply Section 5 with F=G_i and eta=1/n. Independence of X_i from X_-i under the test law and the identity in Section 1 yield
\[
\mathcal R_n(\widehat\theta;G_0)
\le C_A\frac{\log n}{\log\log n}(\epsilon_n^2+r_n^2+n^{-1})+C_A/n.
\]
The integration is over the Hellinger tail, not over eta. Using \(\epsilon_n^2=O_A(\log n/(n\log\log n))\) gives the general thickness-to-regret bound
\[
\sup_{G_0}\mathcal R_n(\widehat\theta;G_0)
\le\frac{C_A\log n}{n\log\log n}\left(\frac{\log n}{\log\log n}+n r_n^2\right).
\]
Finally substitute \(r_n^2=B'_{A,c_0}\log^2 n/(n\log\log n)\) from Section 2. This proves
\[
\sup_{G_0\in\mathcal P([0,A])}\mathcal R_n(\widehat\theta;G_0)
\le C(A,c_0)\frac{\log^3 n}{n(\log\log n)^2}.
\]
All lower bounds on n can be absorbed into n0(A,c0). The threshold for c0 is absolute. Every listed proof obligation is closed.
