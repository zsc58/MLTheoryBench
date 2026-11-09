# Reference Proof

## Audit status and obligations

This proof establishes the frozen public claim without invoking the specialized external master regret theorem. The theorem-critical obligations are: ridge and perturbation confidence; a legitimate Gaussian-to-Brownian embedding; common-clock time-uniform exceedance; uniformity over directions with the stated numerical ensemble size; and conversion of optimism into high-probability cumulative regret. Sections 1–4 establish the first four obligations. Sections 5–7 explicitly derive the final obligation by a finite-ensemble comparison and a bounded martingale calculation. Section 8 makes the final substitution.

The generic master theorem recorded as theory_018 is still an external specialized result, not standard background proved here. Unlike the preceding reference revision, this proof does not depend on it. Nor does it require the exact numerical prefactor of the source's separate auxiliary regret lemma.

## 1. Notation and concentration

Write \(\ell=\log(n/\delta)>1\), and use the sequential history \(\mathcal H_t\) defined in the public task. In particular, \(X_s\) is chosen before the fresh vector \((\xi_s^j)_{j\le m}\), and that vector is independent of the history through \(Y_s\).

For positive definite \(A\), write \(\|v\|_A=(v^\top Av)^{1/2}\). Define
\[
\gamma_t^\alpha=\sqrt d+2\sqrt{2\log(4/\alpha)+d\log(1+t/(\lambda d))},\qquad 0<\alpha<1.
\]
The standard self-normalized inequality used here is the following: if \(Z_s\) is predictable and \(\epsilon_s\) is conditionally centered 1-subgaussian before its draw, then, for \(A_t=\lambda I+\sum_{s\le t}Z_sZ_s^\top\), with probability at least \(1-q\), simultaneously in \(t\),
\[
\left\|\sum_{s\le t}Z_s\epsilon_s\right\|_{A_t^{-1}}\le
\sqrt{2\log(1/q)+\log(\det A_t/\lambda^d)}.
\]
This is the standard independent concentration result underlying the source's confidence lemma and perturbation estimates. Its hypotheses hold for reward noise with the pre-reward filtration and for each fixed particle's perturbations with the pre-perturbation filtration. The determinant bound is
\[
\log(\det V_t/\lambda^d)\le d\log(1+t/(\lambda d)),
\]
by the trace bound and arithmetic-geometric mean inequality for eigenvalues.

The ridge identity
\[
\widehat\theta_t-\theta_\star=V_t^{-1}\left(\sum_{s\le t}X_s\eta_s-\lambda\theta_\star\right)
\]
and \(\|\theta_\star\|_2\le1\) therefore give the event
\[
\mathcal C_q=\{\forall t\in\{0,\ldots,n\}:\ \|\widehat\theta_t-\theta_\star\|_{V_t}\le\beta_t^q\},\qquad
\Pr(\mathcal C_q)\ge1-q,
\]
where \(\beta_t^q=\sqrt\lambda+\sqrt{2\log(1/q)+\log(\det V_t/\lambda^d)}\). These auxiliary radii do not change the algorithm's use of \(\beta_t^\delta\). The time-zero inequality follows directly from \(\|\theta_\star\|_2\le1\).

For a fixed particle \(j\), Gaussian norm concentration gives
\[
\Pr\{\|\zeta^j\|_2>\sqrt d+\sqrt{2\log(4/\alpha)}\}\le\alpha/4.
\]
Apply the self-normalized inequality to \(\sum X_s\xi_s^j\) with failure \(\alpha/4\), and use
\[
\|S_t^j\|_{V_t^{-1}}\le\|\zeta^j\|_2+\left\|\sum_{s\le t}X_s\xi_s^j\right\|_{V_t^{-1}}.
\]
Consequently, with probability at least \(1-\alpha/2\),
\[
\forall t\in\{0,\ldots,n\}:\quad \|S_t^j\|_{V_t^{-1}}\le\gamma_t^\alpha.\tag{1}
\]
No independence between the resulting particle events is asserted or needed.

## 2. Exact Gaussian embedding for a fixed direction

Fix deterministic \(u\in\mathbb S^{d-1}\). Set \(\xi_0=(\langle u,\zeta^j\rangle)_{j\le m}\), \(D_0=\sqrt\lambda\), and \(D_s=\langle u,X_s\rangle\) for \(s\ge1\). Then
\[
M_{t,j}=\langle u,S_t^j\rangle=\sum_{s=0}^tD_s\xi_s^j,
\qquad A_t^2=\sum_{s=0}^tD_s^2=\|u\|_{V_t}^2.
\]
The initial projected Gaussian vector is standard normal with independent coordinates. For subsequent increments, \(D_s\) is known before the fresh independent standard Gaussian vector \(\xi_s\). Use the history through the choice of \(X_s\), or through \(Y_s\), as the pre-increment history. Future perturbations are not included.

For every \((s,j)\), take an independent auxiliary Brownian motion \(\widetilde B_s^j\), independent of the original experiment, and form
\[
B_s^j(r)=\widetilde B_s^j(r)-r\widetilde B_s^j(1)+r\xi_s^j,\qquad 0\le r\le1.
\]
This is a centered Gaussian process with covariance \(r\wedge v\), and \(B_s^j(1)=\xi_s^j\). Thus it is a Brownian segment. Its bridge innovation is independent of the original experiment. Before segment \(s\), its endpoint vector is independent of the available history; the segment is revealed progressively, not by revealing its endpoint at its left endpoint.

Stitch scaled segments on consecutive unit intervals:
\[
N^j(s+r)=\sum_{a<s}D_a\xi_a^j+D_sB_s^j(r),\qquad 0\le r\le1.
\]
At integer boundaries reveal the original history needed to determine the next coefficient. Freshness of the next Gaussian vector and independence of the auxiliary bridges ensure that each \(N^j\) is a continuous local martingale for this progressive filtration. Its bracket on this interval is
\[
\langle N^j\rangle_{s+r}=\sum_{a<s}D_a^2+rD_s^2.
\]
Cross-brackets vanish because the driving Brownian coordinates have zero cross-bracket; random predictable scaling preserves that property. Zero coefficients cause no difficulty.

The standard DDS theorem represents a continuous local martingale started at zero by a Brownian motion evaluated at its bracket. The standard Knight theorem makes the DDS Brownian motions independent when the martingales are pairwise strongly orthogonal. Their hypotheses have just been checked. One may append independent Brownian increments to all coordinates after the finite construction, so every bracket diverges before applying these results; this does not change any required finite-time values. Thus, on an extension, independent standard Brownian motions \(W^1,\ldots,W^m\) satisfy
\[
M_{t,j}=W^j(A_t^2).
\]
All coordinates have the same clock. Since \(\lambda\le A_t^2\le\lambda+n\) for the relevant times, a simultaneous Brownian bound on this deterministic interval applies even though the common clock is random and depends on the history. Coordinatewise clock bounds alone would not suffice without the common-clock property.

## 3. Time-uniform Brownian exceedance

Let \(0<\tau<\tau'\), \(c>0\), and \(0<p<\frac14(1-\Phi(c))\), where \(\Phi\) is the standard normal distribution function. Define
\[
a=\frac{\Phi^{-1}(1-4p)-c}{3}>0,
\quad h_\star=\min\left\{1,2\log\frac{c+3a}{c+2a},\log\left(1+\frac{2a^2}{\log8}\right)\right\}.
\]
Choose \(0<h\le h_\star\), put \(K=\lceil\log(\tau'/\tau)/h\rceil\), and let \(s_k=\log\tau+kh\). Define \(U_j(s)=e^{-s/2}W^j(e^s)\). Its marginal law is standard normal. For any fixed \(s_k\), Brownian independent increments and scaling give
\[
U_j(s_k+r)=e^{-r/2}U_j(s_k)+e^{-r/2}\widetilde W_{j,k}(e^r-1),
\]
where \(\widetilde W_{j,k}\) is standard Brownian motion independent of \(U_j(s_k)\). The pairs are independent across \(j\); no independence across \(k\) is required.

For each interval, count particles for which \(U_j(s_k)\ge c+3a\) and the fluctuation stays at least \(-2a\) throughout \([0,h]\). The first event has probability \(4p\). The failure probability of the second is at most
\[
4\exp\{-2a^2/(e^h-1)\}\le1/2.
\]
Indeed, reflection and symmetry give \(\Pr(\sup_{r\le T}|B(r)|\ge b)\le4\Pr(N(0,T)\ge b)\le4e^{-b^2/(2T)}\). Also \(e^{-h/2}(c+3a)-2a\ge c\), so every counted particle exceeds \(c\) throughout the interval.

The count is binomial with success probability at least \(2p\). The standard multiplicative Chernoff inequality \(\Pr(\operatorname{Bin}(m,r)\le rm/2)\le e^{-rm/8}\) bounds interval failure by \(e^{-pm/4}\). A union bound gives
\[
\Pr\left\{\inf_{v\in[\tau,\tau']}\frac1m\sum_j\mathbf1\{W^j(v)/\sqrt v\ge c\}<p\right\}\le Ke^{-pm/4}.\tag{2}
\]

For \(c=1/20\) and \(p=1/10\), \(\Phi(1/4)<0.6\), since the normal density is less than \(0.4\). Hence \(a\ge1/15\). The drift constraint permits \(h\le2\log(15/11)\), and
\[
\log\left(1+\frac{2}{225\log8}\right)>1/250.
\]
Thus \(h=1/250\) is admissible.

Define
\[
E_{t,m}(u,c)=\frac1m\sum_j\mathbf1\{\langle u,S_{t-1}^j\rangle/\|u\|_{V_{t-1}}\ge c\}.
\]
Sections 2 and 3 show that, for fixed unit \(u\), all \(t\le n\) satisfy \(E_{t,m}(u,1/20)\ge1/10\) except with probability \(\delta'\), provided
\[
m\ge40\log(K/\delta'),\qquad K=\lceil250\log(1+n/\lambda)\rceil.\tag{3}
\]
Here \(K\ge1\), even when \(\lambda\) is very large.

## 4. Uniformity over directions and the numerical threshold

Use (1) with \(\alpha=\delta/m\) and union-bound over particles. With failure at most \(\delta/2\), every relevant particle and time satisfies \(\|S_{t-1}^j\|_{V_{t-1}^{-1}}\le\Gamma\), where \(\Gamma=\gamma_{n-1}^{\delta/m}\).

For unit \(u\),
\[
\frac{\langle u,S\rangle}{\|u\|_V}=\left\langle\frac{V^{1/2}u}{\|V^{1/2}u\|_2},V^{-1/2}S\right\rangle.
\]
The inequality \(\|a/\|a\|-b/\|b\|\|\le2\|a-b\|/\min(\|a\|,\|b\|)\), together with \(\lambda I\preceq V\preceq(\lambda+n)I\), gives Lipschitz constant
\[
L=2\Gamma\sqrt{1+n/\lambda}.
\]
Take a deterministic \(\varepsilon\)-net of the unit sphere with \(\varepsilon=1/(40L)<1\), of cardinality at most \((3/\varepsilon)^d\). This covering bound follows by taking a maximal separated set and comparing volumes of disjoint balls. Apply (3) to every net point at failure level \(\delta'=(\delta/2)/(3/\varepsilon)^d\). On the intersection, an exceedance of \(1/20\) at the nearest net point implies an exceedance of \(1/40\) at the original direction.

The sufficient ensemble-size condition holds for all permitted \(m\), not only for one chosen ensemble size. Since \(\lambda\ge1\), \(K\le501\ell\) and \(\log(2K/\delta)\le10\ell\). Put \(x=\log(4m/\delta)\). Then
\[
\Gamma\le4\sqrt{d\ell+x}.
\]
Under \(m\ge2000d\ell\), one has \(d\ell\le m\), \(x\le2m\), and consequently
\[
\log\Gamma\le3+\tfrac12\log m,
\qquad \log(3/\varepsilon)\le\ell+9+\tfrac12\log m.
\]
It follows that the right side of the required net-size condition is at most
\[
40[\log(2K/\delta)+d\log(3/\varepsilon)]\le20d\log m+800d\ell.
\]
Let \(M=2000d\ell\). Since \(d\le n\), \(\log d\le\ell\), \(\log\ell\le\ell\), and \(\log2000<8\le8\ell\), we have \(\log M\le10\ell\). Thus \(20d\log M+800d\ell\le1000d\ell<M\). The function \(m-20d\log m\) is increasing for \(m\ge M\), proving the required inequality for every \(m\ge M\).

We have established an event \(\mathcal U\), with \(\Pr(\mathcal U)\ge1-\delta\), on which
\[
\forall t\le n:\quad\inf_{u\in\mathbb S^{d-1}}E_{t,m}(u,1/40)\ge1/10.\tag{4}
\]

## 5. Controlling bad-particle fractions and selected particles

We now use (1) with the private proof parameter
\[
\alpha=\frac{\delta}{20n},\qquad
b_{t-1}=40\gamma_{t-1}^{\alpha}\beta_{t-1}^\delta.
\]
This changes no algorithm parameter. The radius \(b_{t-1}\) is predictable and nondecreasing.

At round \(t\), call particle \(j\) good when
\[
\|S_{t-1}^j\|_{V_{t-1}^{-1}}\le\gamma_{t-1}^{\alpha}.
\]
Let \(\mathcal I_t\subseteq\{1,\ldots,m\}\) be the set of good indices, and let
\[
Q_t=\frac1m\sum_{j=1}^m\mathbf1\{j\notin\mathcal I_t\}
\]
be the bad fraction. Both are measurable with respect to \(\mathcal H_{t-1}\). By (1), for every fixed \(j,t\), the bad probability is at most \(\alpha/2=\delta/(40n)\). Therefore
\[
\mathbb E Q_t\le\frac{\delta}{40n}.
\]
Markov's inequality and a union bound yield
\[
\Pr\{\exists t\le n:Q_t>1/20\}
\le20\sum_{t=1}^n\mathbb E Q_t\le\delta/2.\tag{5}
\]
Write \(\mathcal Q=\{\forall t\le n:Q_t\le1/20\}\).

Fresh uniform selection also gives
\[
\Pr\{J_t\notin\mathcal I_t\}=\mathbb E Q_t\le\frac{\delta}{40n}.
\]
Thus the event \(\mathcal S=\{\forall t\le n:J_t\in\mathcal I_t\}\) has failure probability at most \(\delta/40\). This averaging argument does not assume independence between particle events and does not union-bound over all particles to obtain a regret radius. In particular, no \(\log m\) term enters \(b_{t-1}\).

For every good particle,
\[
\|\theta_{t-1}^j-\widehat\theta_{t-1}\|_{V_{t-1}}\le b_{t-1}.
\]
On \(\mathcal C_\delta\), the true parameter also lies in this larger ball, since its radius is at most \(\beta_{t-1}^\delta\le b_{t-1}\). We will still use the smaller beta radius, not just membership in the larger ball, when establishing optimism.

## 6. Explicit conditional comparison for regret

Because \(\mathcal X\) is nonempty and compact, fix an optimal action \(x_\star\) and put \(v_\star=\langle\theta_\star,x_\star\rangle\). Define the value function
\[
F(\theta)=\max_{x\in\mathcal X}\langle\theta,x\rangle.
\]
Given the pre-index history, denote by \(a_t^j\) the action the specified tie-breaking rule takes if \(J_t=j\). These are measurable functions of that history, satisfy
\[
a_t^j\in\arg\max_{x\in\mathcal X}\langle x,\theta_{t-1}^j\rangle,
\]
and \(X_t=a_t^{J_t}\). Such versions follow from the prescribed measurability and the finite index space; conditional uniformity ensures that the greedy condition holds for every index outside a common null set.

Let
\[
w_t^j=\|a_t^j\|_{V_{t-1}^{-1}},\qquad
w_t=\|X_t\|_{V_{t-1}^{-1}},\qquad
\mu_t=\mathbb E[w_t\mid\mathcal H_{t-1}]=\frac1m\sum_jw_t^j.
\]
All widths lie in \([0,1/\sqrt\lambda]\).

First establish the optimistic fraction. If \(x_\star=0\), then \(0\in\mathcal X\) and \(F(\theta)\ge0=v_\star\) for every model. Otherwise put \(u_t=V_{t-1}^{-1}x_\star\ne0\). On the current beta-confidence event,
\[
\langle\theta_\star-\widehat\theta_{t-1},x_\star\rangle
\le\beta_{t-1}^\delta\|x_\star\|_{V_{t-1}^{-1}}.
\]
Since \(\|u_t\|_{V_{t-1}}=\|x_\star\|_{V_{t-1}^{-1}}\), every particle satisfying
\[
\frac{\langle S_{t-1}^j,u_t\rangle}{\|u_t\|_{V_{t-1}}}\ge1/40
\]
has \(F(\theta_{t-1}^j)\ge v_\star\). By (4) and positive homogeneity in the direction, on \(\mathcal C_\delta\cap\mathcal U\) at least a fraction \(1/10\) is optimistic at every round.

On \(\mathcal C_\delta\cap\mathcal U\cap\mathcal Q\), at least a fraction \(1/20\) of all particles is simultaneously optimistic and good. Let \(\mathcal O_t\) be this nonempty set. Choose \(k_t\in\mathcal O_t\) minimizing \(w_t^j\), breaking ties by index. Then
\[
\mu_t\ge\frac{|\mathcal O_t|}{m}w_t^{k_t}\ge\frac1{20}w_t^{k_t},
\qquad w_t^{k_t}\le20\mu_t.\tag{6}
\]
This is a comparison within each fixed pre-index history; it does not condition a martingale on a future high-probability event.

Consider any selected index \(j\in\mathcal I_t\). Write \(\theta_j=\theta_{t-1}^j\) and \(\theta_k=\theta_{t-1}^{k_t}\). Optimism of \(k_t\) and greediness of \(a_t^j\) give
\[
\begin{aligned}
v_\star-\langle\theta_\star,a_t^j\rangle
&\le F(\theta_k)-F(\theta_j)+\langle\theta_j-\theta_\star,a_t^j\rangle,\\
F(\theta_k)-F(\theta_j)
&\le\langle\theta_k-\theta_j,a_t^{k_t}\rangle.
\end{aligned}
\]
Both model vectors are within \(b_{t-1}\) of the same ridge estimate, and on \(\mathcal C_\delta\) the true vector is also within \(b_{t-1}\). Cauchy--Schwarz therefore implies
\[
v_\star-\langle\theta_\star,a_t^j\rangle
\le2b_{t-1}(w_t^{k_t}+w_t^j)
\le2b_{t-1}(20\mu_t+w_t^j).\tag{7}
\]
In particular, on \(\mathcal C_\delta\cap\mathcal U\cap\mathcal Q\cap\mathcal S\), inequality (7) holds for the actually selected action in every round, including nonoptimistic rounds. This is the conditional comparison missing from the preceding reference revision.

## 7. Martingale summation and the potential bound

We derive the needed deviation bound directly. If a conditionally centered variable \(Z\) lies in an interval of length \(a\), then
\[
\mathbb E[e^{sZ}\mid\mathcal H]\le e^{s^2a^2/8}.
\]
For completeness, the logarithm of its conditional moment-generating function has value and first derivative zero at zero. Its second derivative is a variance under an exponentially tilted distribution supported on the same interval. That variance is at most \(a^2/4\): subtract the interval midpoint and use the bound \(a^2/4\) on the squared centered location, noting that variance is no larger than this second moment. Integrating the second-derivative bound proves the displayed estimate.

Apply it to \(Z_t=\mu_t-w_t\), conditionally on \(\mathcal H_{t-1}\). The conditional mean is zero and the interval length is \(1/\sqrt\lambda\). Iterating conditional expectations gives
\[
\mathbb E\exp\left(s\sum_{t=1}^n(\mu_t-w_t)\right)
\le\exp\left(\frac{ns^2}{8\lambda}\right).
\]
Exponential Markov inequality, optimized at \(s=4\lambda x/n\), yields
\[
\Pr\left\{\sum_{t=1}^n(\mu_t-w_t)\ge x\right\}
\le e^{-2\lambda x^2/n}.
\]
Consequently an event \(\mathcal M\) of probability at least \(1-\delta\) satisfies
\[
\sum_{t=1}^n\mu_t\le\sum_{t=1}^nw_t+D_n,
\qquad D_n=\sqrt{\frac n{2\lambda}\log(1/\delta)}.\tag{8}
\]
This estimate is unconditional on the confidence, exceedance, and particle events.

The potential calculation is
\[
\sum_{t=1}^nw_t^2\le2\log(\det V_n/\lambda^d)
\le2d\log(1+n/(d\lambda)).\tag{9}
\]
Indeed, \(w_t^2\le1/\lambda\le1\), the determinant update contributes \(\log(1+w_t^2)\), and \(z\le2\log(1+z)\) for \(0\le z\le1\). Thus Cauchy--Schwarz gives
\[
\sum_{t=1}^nw_t\le\sqrt{2dn\log(1+n/(d\lambda))}.\tag{10}
\]

Intersect \(\mathcal C_\delta,\mathcal U,\mathcal Q,\mathcal S,\mathcal M\). Their failure probabilities are at most \(\delta,\delta,\delta/2,\delta/40,\delta\), respectively. No independence is needed. The total is
\[
\frac{141}{40}\delta<4\delta.
\]
On this intersection, summing (7), using the nonnegativity of the widths and the monotonicity of \(b_t\), and then applying (8) and (10), gives
\[
\begin{aligned}
R_n
&\le2b_{n-1}\left(\sum_{t=1}^nw_t+20\sum_{t=1}^n\mu_t\right)\\
&\le42b_{n-1}\sum_{t=1}^nw_t+40b_{n-1}D_n\\
&\le42b_{n-1}\sqrt{2dn\log(1+n/(d\lambda))}
+40b_{n-1}\sqrt{\frac n{2\lambda}\log(1/\delta)}.\tag{11}
\end{aligned}
\]
Every probabilistic and comparison step needed for (11) has now been derived. In particular, (11) is not conditional on the specialized external master theorem.

## 8. Final substitution and asymptotic consequence

Recall \(\alpha=\delta/(20n)\). Since \(\ell=\log(n/\delta)>\log8\),
\[
\log(4/\alpha)=\log(80n/\delta)\le4\ell,
\qquad \log(1+n/(\lambda d))\le2\ell.
\]
Therefore
\[
\gamma_{n-1}^{\alpha}
\le\sqrt d+2\sqrt{8\ell+2d\ell}
\le10\sqrt{d\ell}.
\]
Also, for \(a=n/\lambda>0\),
\[
\sqrt{\frac a2\log(1/\delta)}
\le\sqrt{(a+1)\log\left(\frac{\sqrt{a+1}}\delta\right)}.
\]
Substituting \(b_{n-1}=40\gamma_{n-1}^{\alpha}\beta_{n-1}^\delta\) in (11) and absorbing numerical constants proves, with probability at least \(1-4\delta\),
\[
R_n\le C\beta_{n-1}^\delta\sqrt{d\log(n/\delta)}
\left[\sqrt{dn\log\left(1+\frac n{d\lambda}\right)}
+\sqrt{\left(\frac n\lambda+1\right)\log\left(\frac{\sqrt{n/\lambda+1}}\delta\right)}\right]
\]
for a universal \(C\), as required.

For \(\lambda=80\), the determinant bound gives \(\beta_{n-1}^\delta=O(\sqrt{d\ell})\). Both bracketed terms are \(O(\sqrt{dn\ell})\), using \(d\ge1\) and \(n\ge2\). Hence the bound is \(O(d^{3/2}\sqrt n\,\ell^{3/2})\), in particular the stated soft-O rate. Choosing an integer ensemble size of order \(d\ell\) satisfying the lower bound gives the stated ensemble scaling.

## Source-repair and dependency record

The prior public repairs remain in force: future perturbations are unavailable, perturbations are sampled freshly after the reward, the action set is nonempty, m is integral, and the asymptotic consequence specifies lambda=80.

The source-local confidence-event issue recorded under theory_007 is not reintroduced. Optimism in Section 6 explicitly uses the beta-confidence event; membership in the larger b-radius ball is used only for the subsequent comparison of vectors. The preceding audit's alternative source-local repair—applying the quoted master theorem at failure level delta/2 and separately intersecting the beta-confidence and exceedance events—remains a valid conditional application with total failure at most 7delta/2. Its additional logarithmic factor is harmless for the frozen universal-constant target. The present proof no longer needs that application because Sections 5–7 directly establish the required regret bound.

Theory_018 remains classified as a nonstandard external dependency in the source inventory. Its generic statement is neither proved nor invoked here. The narrower obligation needed for this task has instead been fully discharged by (5)–(11), without changing any public assumption or algorithm parameter. No theorem-critical GT obligation remains unresolved.
