# Reference Proof

## Proof Structure
We derive a rarity-sensitive conditional-inclusion tail bound from a standard realizable VC inequality. A weighted recursion then controls moments of the overlap of the error sets from two independent blocks. Finally, a deterministic majority-error reduction, the Lq triangle inequality, and Markov's inequality yield the stated bound.

## Complete Proof

### step_001: Error sets and the standard VC input
Fix the distribution P, target f*, sample size m, and deterministic learning rule. Define
\[
\mathcal C=\{\{x:f(x)\ne f^*(x)\}:f\in\mathcal F\},\qquad A(S)=\{x:\hat f_S(x)\ne f^*(x)\}.
\]
On every finite set, taking disagreement with the fixed target flips a fixed subset of the coordinates of each binary trace. This is a bijection of the trace space, so \(\operatorname{VC}(\mathcal C)=d\). Consistency gives \(A(S)\in\mathcal C\) and \(A(S)\cap S=\varnothing\). The public measurability assumptions make the membership indicator \((S,x)\mapsto\mathbf1\{x\in A(S)\}\) jointly measurable, so the integrals and finite-prefix probabilities below are measurable.

We use the following standard independent realizable VC bound. For a class of VC dimension at most d, a probability measure Q, an integer N>=0, and \(\varepsilon\in(0,1]\),
\[
\Pr_{Y\sim Q^N}\bigl(\exists R\in\mathcal C:\ R\cap\{Y_1,\ldots,Y_N\}=\varnothing,\ Q(R)>\varepsilon\bigr)
\le 2(13/\varepsilon)^{2d}\exp(-\varepsilon N/4),
\]
with the usual measurability interpretation of the uniform event. We only need its standard measurable-selector version: the same upper bound holds for \(\Pr(Q(B(Y,U))>\varepsilon)\), where B is a jointly measurable selection of a range avoiding all Y_i and U is auxiliary randomness independent of the iid Q-sample Y. The deterministic-selector bound is the consistent-classifier form of the VC inequality; conditioning on U and integrating gives the version with auxiliary randomness. This formulation does not require introducing a measurable uncountable union into the task. For N=0 the displayed upper bound is at least one, so this case is automatic.

### step_002: Conditional-inclusion tail estimate
For a fixed finite prefix \(z=(z_1,\ldots,z_r)\), let
\[
E_z=\{z_1,\ldots,z_r\in A(S)\},\qquad p_z=\Pr_S(E_z).
\]
When \(p_z>0\), define
\[
\alpha_z(x)=\Pr_S(x\in A(S)\mid E_z).
\]
We claim that, for \(a\in(0,1]\) and \(X\sim P\),
\[
\Pr(\alpha_z(X)>a)\le \frac{160}{am}\left[d\log(e/a)+\log(e/p_z)\right]. \tag{1}
\]
Put \(G=\{x:\alpha_z(x)>a\}\) and \(\beta=P(G)\). If \(\beta=0\), the claim holds immediately; this includes a=1. Otherwise define \(P_G(B)=P(B\cap G)/\beta\). Conditional Fubini gives
\[
\mathbb E[P_G(A(S))\mid E_z]=\frac1\beta\int_G\alpha_z(x)\,dP(x)>a.
\]
Since \(0\le P_G(A(S))\le1\),
\[
a<\mathbb E[P_G(A(S))\mid E_z]
\le a/2+\Pr(P_G(A(S))>a/2\mid E_z).
\]
Consequently the unconditional probability satisfies
\[
\Pr(P_G(A(S))>a/2)\ge ap_z/2. \tag{2}
\]
Here G is fixed once z is fixed: it depends on the distribution of the training sample, not on the realized training sample to which the VC bound is applied.

Let \(N=\sum_{j=1}^m\mathbf1\{S_j\in G\}\). Conditional on the membership pattern of the sample in G, the N observations in G are iid from \(P_G\), independently of the observations outside G. The latter observations serve only as independent auxiliary inputs to the selector. Its restricted output \(A(S)\cap G\) belongs to \(\{R\cap G:R\in\mathcal C\}\), a class of VC dimension at most d, and avoids every observation in G. Thus the measurable-selector VC bound, with \(Q=P_G\) and \(\varepsilon=a/2\), gives
\[
\Pr(P_G(A(S))>a/2\mid N)\le2(26/a)^{2d}\exp(-aN/8).
\]
For N=0 this is simply the trivial bound by a number at least one. Since \(N\sim\operatorname{Bin}(m,\beta)\),
\[
\mathbb E e^{-aN/8}
=(1-\beta+\beta e^{-a/8})^m
\le e^{-\beta m(1-e^{-a/8})}
\le e^{-a\beta m/16}.
\]
The last inequality uses \(1-e^{-t}\ge t/2\) for \(0\le t\le1/8\). Therefore
\[
\Pr(P_G(A(S))>a/2)\le2(26/a)^{2d}e^{-a\beta m/16}. \tag{3}
\]
Importantly, (3) is unconditional on E_z. Combining (2) and (3), and taking logarithms, yields
\[
\frac{a\beta m}{16}\le \log\frac4{ap_z}+2d\log\frac{26}a
\le10d\log\frac ea+\log\frac e{p_z}
\le10\left(d\log\frac ea+\log\frac e{p_z}\right).
\]
For the middle inequality, write \(t=\log(1/a)\ge0\); its constant term follows from \(\log4+2d\log26\le10d+1\), and its t coefficient from \(1+2d\le10d\), using d>=1. This proves (1).

### step_003: Moment identity and weighted recursion
For independent \(S,T\sim P^m\), put
\[
Z=P(A(S)\cap A(T)).
\]
Fix an integer q>=1. Take iid \(X_1,\ldots,X_q\sim P\), independently of S and T, and define
\[
p_k(x_1,\ldots,x_k)=\Pr_S(x_1,\ldots,x_k\in A(S)),\qquad p_0=1.
\]
Fubini and independence of S and T give
\[
\mathbb E_{S,T}Z^q
=\mathbb E_X\left[\Pr_S(X_1,\ldots,X_q\in A(S))\Pr_T(X_1,\ldots,X_q\in A(T))\right]
=\mathbb E_X p_q(X)^2. \tag{4}
\]
Define
\[
M_k=\mathbb E_{X_{1:k}}\left[p_k^2\left(64(d+q)+\log(e/p_k)\right)^{q-k}\right],\quad 0\le k\le q,
\]
with zero integrand when p_k=0. These expectations are finite: for each fixed nonnegative integer h, \(p^2(c+\log(e/p))^h\) extends continuously to zero at p=0 and is bounded on [0,1]. We have \(M_q=\mathbb E Z^q\) and \(M_0=(64(d+q)+1)^q\).

We prove
\[
M_k\le\frac{960}{m}M_{k-1},\qquad 1\le k\le q. \tag{5}
\]
Fix the preceding prefix. If \(p=p_{k-1}=0\), all its extensions have p_k=0, and the required inequality is immediate. Otherwise put
\[
L=\log(e/p),\qquad r=64(d+q)+L,\qquad h=q-k,
\]
and let \(\alpha(x)\) be the conditional inclusion probability given that prefix. Then \(p_k=p\alpha(X_k)\). For \(0<a\le1\), define
\[
\phi(a)=p^2a^2(r+\log(1/a))^h,
\]
with \(\phi(0)=0\). Differentiating gives
\[
\phi'(a)=p^2a(r+\log(1/a))^h\left(2-\frac{h}{r+\log(1/a)}\right),
\]
so \(0\le\phi'(a)\le2p^2a(r+\log(1/a))^h\). The formula also covers h=0. Tonelli and (1) therefore imply
\[
\begin{aligned}
\mathbb E_X\phi(\alpha(X))
&\le2p^2\int_0^1a(r+\log(1/a))^h\Pr(\alpha(X)>a)\,da\\
&\le\frac{320p^2}{m}\int_0^1[d\log(e/a)+L](r+\log(1/a))^h\,da\\
&=\frac{320p^2}{m}\int_0^\infty[d(1+u)+L](r+u)^h e^{-u}\,du.
\end{aligned}
\]
Now \(d(1+u)+L\le r(1+u)\) and \(h/r\le1/64\), so
\[
(r+u)^h\le r^h e^{hu/r}\le r^h e^{u/64}.
\]
Consequently
\[
\mathbb E_X\phi(\alpha(X))
\le\frac{320p^2r^{h+1}}m\int_0^\infty(1+u)e^{-63u/64}\,du
=\frac{320p^2r^{h+1}}m\left(\frac{64}{63}+\left(\frac{64}{63}\right)^2\right)
\le\frac{960}{m}p^2r^{h+1}.
\]
Averaging over the preceding prefix proves (5). Iterating and using (4),
\[
\|Z\|_{L_q}=M_q^{1/q}
\le\frac{960}{m}(64(d+q)+1)
\le\frac{62400(d+q)}m. \tag{6}
\]

### step_004: Majority reduction
For the three independent blocks, put \(E_i=A(S_i)\) and \(Y=\operatorname{err}_P(\operatorname{Maj})\). At every point misclassified by the majority, at least two individual classifiers err. Hence
\[
Y\le P(E_1\cap E_2)+P(E_2\cap E_3)+P(E_1\cap E_3).
\]
Each pair consists of outputs of the same fixed selector on independent blocks, so each overlap has the law of Z. The three overlaps need not be mutually independent; the Lq triangle inequality does not require this. From (6) and m=n/3,
\[
\|Y\|_{L_q}\le\frac{3\cdot62400(d+q)}m
=\frac{561600(d+q)}n. \tag{7}
\]

### step_005: Probability conversion
Let \(\ell=\log(1/\delta)>0\) and \(q=\lceil\ell\rceil\ge1\). If \(\|Y\|_{L_q}=0\), then Y=0 almost surely and the conclusion is immediate. Otherwise Markov's inequality gives
\[
\Pr(Y>e\|Y\|_{L_q})\le e^{-q}\le\delta.
\]
Since \(q\le\ell+1\) and d>=1,
\[
d+q\le d+\ell+1\le2(d+\ell).
\]
Using (7) and \(2e\cdot561600<10^7\), we obtain
\[
e\|Y\|_{L_q}\le\frac{10^7(d+\log(1/\delta))}{n}.
\]
Thus the asserted event has probability at least 1-delta. If its numerical upper bound exceeds one, the claim is also trivially valid because Y<=1. All estimates are independent of P, f*, and the choice of the fixed consistent rule, establishing the required uniformity.
