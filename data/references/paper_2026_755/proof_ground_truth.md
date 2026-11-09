# Reference Proof

## Proof Structure

For each fixed index partition and sample, derive the two Gaussian residual laws and their scaled chi-square squared norms. Bound their scales using purity feasibility and the maximal admissible size. Establish a dependence-robust Chernoff bound, check strict scale ordering, and compare its tail factor with the specified \(\rho_q\). Finally, union-bound over samples and over the deterministic family of approximately balanced index partitions.

## Audited Background

The standard background used here is recorded in theory_016. A deterministic linear combination of independent Gaussian vectors is Gaussian, with covariance obtained by summing the squared-coefficient covariance contributions. If \(G\sim N(0,aI_d)\), then \(\|G\|^2\sim a\chi_d^2\). For \(Z\sim\chi_d^2\),
\[
\mathbb E e^{sZ}=(1-2s)^{-d/2},\qquad s<1/2.
\]
Consequently, for \(a>0\), \(\mathbb E e^{s(aZ)}=(1-2as)^{-d/2}\) for \(s<1/(2a)\). Markov's inequality applies to nonnegative random variables; Cauchy--Schwarz applies when the relevant second moments are finite. A finite union has probability at most the sum of its event probabilities, without independence. There are \(2^n\) assignments of \(n\) indices to two labeled sets.

The missing scale factors in the source's background MGF displays are corrected by deterministic rescaling. The source's actual Chernoff calculation already uses the corrected scaled formulas.

## Complete Proof

All parameters and the true label classes are fixed. Probability is over the independent centers and noises. Let \(\mathcal B_q\) be the deterministic family of labeled index bipartitions satisfying the public strict balance definition. If this family is empty, the requested simultaneous statement is true with probability one. Hence suppose a partition in this family is available, and fix one such partition \(A_1\sqcup A_2=[n]\), independently of the random observations. Its cluster sizes exceed 2.

Write \(c_j=|A_j|\), \(p_j^\ell=|A_j\cap T_\ell|/c_j\), and \(\bar j=3-j\), \(\bar\ell=3-\ell\). Fix \(i\in A_j\cap T_\ell\). The current-centroid residual is
\[
y_i-\bar y_j=(1-p_j^\ell)(\theta_\ell-\theta_{\bar\ell})
 +(1-c_j^{-1})\epsilon_i
 -c_j^{-1}\sum_{k\in A_j\setminus\{i\}}\epsilon_k.
\]
The center difference has covariance \(2I_d\), is independent of all noises, and the separated noise terms are independent. Thus the residual is a centered Gaussian with covariance \(a_{\rm cur}I_d\), where
\[
\begin{aligned}
a_{\rm cur}
&=2(1-p_j^\ell)^2+
 \left[(1-c_j^{-1})^2+(c_j-1)c_j^{-2}\right]\sigma^2\\
&=2(1-p_j^\ell)^2+(1-c_j^{-1})\sigma^2.
\end{aligned}
\]
Similarly, because \(i\notin A_{\bar j}\),
\[
y_i-\bar y_{\bar j}
 =(1-p_{\bar j}^\ell)(\theta_\ell-\theta_{\bar\ell})
 +\epsilon_i-c_{\bar j}^{-1}\sum_{k\in A_{\bar j}}\epsilon_k
\]
is a centered Gaussian with covariance \(a_{\rm alt}I_d\), where
\[
a_{\rm alt}=2(1-p_{\bar j}^\ell)^2+(1+c_{\bar j}^{-1})\sigma^2.
\]
Consequently,
\[
D_{\rm cur}:=\|y_i-\bar y_j\|^2\sim a_{\rm cur}\chi_d^2,
\qquad
D_{\rm alt}:=\|y_i-\bar y_{\bar j}\|^2\sim a_{\rm alt}\chi_d^2.
\]
These two variables need not be independent. Coordinate independence and the chi-square laws follow from the centered isotropic Gaussian residual distributions, not from independence between the two residuals.

### A dependence-robust tail inequality

Let \(Y_1\sim u\chi_d^2\), \(Y_2\sim v\chi_d^2\), with \(u>v>0\), under any joint distribution, and let \(h\in\mathbb R\). For \(0<t<1/(4v)\), Markov and Cauchy--Schwarz give
\[
\begin{aligned}
\Pr(Y_1-Y_2\le h)
&\le e^{th}\mathbb E(e^{-tY_1}e^{tY_2})\\
&\le e^{th}\left[\mathbb E e^{-2tY_1}\,
                         \mathbb E e^{2tY_2}\right]^{1/2}\\
&=e^{th}\bigl[(1+4tu)(1-4tv)\bigr]^{-d/4}.
\end{aligned}
\]
The specified domain ensures the finite second moments needed by Cauchy--Schwarz. Choose
\[
t_*=(u-v)/(8uv)>0.
\]
Then \(4t_*v=(u-v)/(2u)<1\), so this choice lies in the MGF domain, and
\[
(1+4t_*u)(1-4t_*v)=\frac{(u+v)^2}{4uv}.
\]
It follows that
\[
\Pr(Y_1-Y_2\le h)
\le \exp\!\left(\frac{h(u-v)}{8uv}\right)
 r(u,v)^{d/4},
\qquad
r(u,v):=\frac{4uv}{(u+v)^2}
=1-\left(\frac{u-v}{u+v}\right)^2.
\]
The chosen \(t_*\) maximizes the quadratic denominator factor; it need not optimize the complete bound when \(h\ne0\). Only \(h=0\) is needed below.

### Uniform scale ordering

Because \(i\in A_j\cap T_\ell\), \(p_j^\ell\ge1/c_j\). Since \((1-p)^2\) is decreasing on \([0,1]\),
\[
a_{\rm cur}\le\omega_{\rm cur}(c_j),
\qquad
\omega_{\rm cur}(c):=2(1-c^{-1})^2+(1-c^{-1})\sigma^2.
\]
Dropping the nonnegative alternative signal term gives
\[
a_{\rm alt}\ge\omega_{\rm alt}(c_{\bar j}),
\qquad
\omega_{\rm alt}(c):=(1+c^{-1})\sigma^2.
\]
These are universal scale envelopes; their equality configurations need not be attainable for the fixed true-label classes.

Put
\[
m=\frac{n+q\sqrt n}{2}.
\]
Strict approximate balance gives \(c_j,c_{\bar j}<m\). For real \(c>1\), direct differentiation gives
\[
\omega_{\rm cur}'(c)
 =\frac{\sigma^2+4(1-c^{-1})}{c^2}>0,
\qquad
\omega_{\rm alt}'(c)=-\frac{\sigma^2}{c^2}<0.
\]
Therefore
\[
a_{\rm cur}\le b_2:=2(1-m^{-1})^2+(1-m^{-1})\sigma^2,
\qquad
a_{\rm alt}\ge b_1:=(1+m^{-1})\sigma^2.
\]
Evaluating both envelope functions at \(m\) is a bound; it does not assert that both clusters can simultaneously have that size.

The prescribed noise level is
\[
\sigma=\beta\frac{m-1}{\sqrt m}.
\]
Here \(m>1\), and hence \(\sigma>0\). In particular,
\[
b_1-b_2
=\frac{2\sigma^2}{m}-2(1-m^{-1})^2
=\frac{2(m-1)^2}{m^2}(\beta^2-1)>0.
\]
Also \(b_2>0\), and the actual current scale is positive because \(c_j>2\). Thus
\[
a_{\rm alt}\ge b_1>b_2\ge a_{\rm cur}>0.
\]
This establishes all hypotheses of the tail inequality without relying on the source's malformed derivative simplifications.

On the ordered positive-scale domain,
\[
\partial_u r(u,v)=\frac{4v(v-u)}{(u+v)^3}<0,
\qquad
\partial_v r(u,v)=\frac{4u(u-v)}{(u+v)^3}>0.
\]
All intermediate scale replacements remain in this domain, so
\[
r(a_{\rm alt},a_{\rm cur})\le r(b_1,b_2)=\rho_q.
\]
The final equality follows immediately by substituting \(m=(n+q\sqrt n)/2\) into the public definition. Positive ordered scales also give \(0<\rho_q<1\).

For explicit verification against the source's rational expression, write \(N=n+q\sqrt n=2m\). Then
\[
b_1=\frac{(N+2)\sigma^2}{N},
\qquad
b_2=\frac{(N-2)[N\sigma^2+2(N-2)]}{N^2},
\]
and therefore
\[
\rho_q
=\frac{\sigma^2(N-2)N(N+2)[N(\sigma^2+2)-4]}
       {[N^2\sigma^2+(N-2)^2]^2}.
\]
Since \(N=\sqrt n(\sqrt n+q)\), this is exactly the source's specified factor. This algebraic identity is private verification, not an additional public assumption.

Applying the tail inequality to the actual distance scales with \(h=0\) yields
\[
\Pr(D_{\rm alt}<D_{\rm cur})
\le\Pr(D_{\rm alt}-D_{\rm cur}\le0)
\le r(a_{\rm alt},a_{\rm cur})^{d/4}
\le\rho_q^{d/4}.
\]

### Ties and simultaneous fixed points

For completeness, ties have probability zero for every nonempty index bipartition. The full observation vector has a Lebesgue density, because conditional on the centers its noises have positive definite covariance. For a fixed partition and index, the difference of the two squared distances is a polynomial in that vector and is not identically zero. If the current cluster has another index \(k\), take \(y_i=0\), \(y_k\) equal to a coordinate unit vector, and all remaining observations zero: the competing-minus-current difference is \(-1/c_j^2\). If the current cluster is a singleton, instead put a coordinate unit vector at one competing-cluster index, obtaining difference \(1/c_{\bar j}^2\).

A nonzero polynomial has a Lebesgue-null zero set: induct on the number of variables, expand in the last variable, exclude the null set where all coefficient polynomials vanish, and use the finite number of roots of a nonzero one-variable polynomial together with Fubini. The finite number of partitions and indices thus permits discarding all ties simultaneously.

For each fixed \(A\in\mathcal B_q\), let \(E_{A,i}\) be the strict reassignment event for index \(i\). A union bound gives
\[
\Pr(A\text{ is not a Lloyd fixed point})
\le\sum_{i=1}^n\Pr(E_{A,i})
\le n\rho_q^{d/4}.
\]
There are at most \(2^n\) labeled index bipartitions, so
\[
\Pr\{\exists A\in\mathcal B_q:\ A\text{ is not a Lloyd fixed point}\}
\le\sum_{A\in\mathcal B_q} n\rho_q^{d/4}
\le2^n n\rho_q^{d/4}.
\]
No independence among these events is used. Taking complements proves the requested probability bound. The event is simultaneous over the entire deterministic family and therefore also covers any subsequently chosen admissible partition, without asserting a chi-square law conditional on an observation-dependent choice. If the displayed lower bound is negative, the same inequality remains valid; no extra dimension restriction is necessary.

## Upstream Boundary Verification

The selected support chain includes a single-sample result allowing a singleton current cluster. Although no approximately balanced cluster is a singleton, its proof must still be audited. If \(c=1\), the current centroid equals the observation, so strict reassignment is impossible. The source's rational tail factor has numerator zero and positive denominator for \(\sigma>0\), giving \(\rho=0\). For \(c>1\), the prescribed pointwise threshold ensures positive ordered envelope scales and the preceding Chernoff-and-monotonicity argument applies. This closes the source's omitted boundary case without restricting its statement.

## Theorem-Critical Obligation Ledger

1. Fixed-label, fixed-index-partition observation experiment: explicit in the setup and maintained throughout.
2. Current and competing Gaussian residual laws: derived by the displayed expansions and covariance calculations.
3. Dependence-robust scaled-chi-square tail inequality: derived using audited standard facts, with finite moments and the MGF domain checked.
4. Purity and cluster-size envelopes: derived without assuming extremal configurations are attainable.
5. High-noise ordering and factor monotonicity: derived explicitly from beta>1 and the displayed derivatives.
6. Identification of rho_q and its range: verified by substitution and algebra.
7. Tie-nullness and finite-event measurability: established by the polynomial argument and finite enumeration.
8. Simultaneous probability conclusion: obtained by the two explicit union bounds, including the empty-family case.
9. Upstream singleton support case: closed directly rather than by an inapplicable positive-scale lemma.

All obligations are closed. No nonstandard external result or unresolved private GT gap is used.
