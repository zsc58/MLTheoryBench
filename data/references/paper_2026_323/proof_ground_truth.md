# Reference Proof

## Proof Structure

Concentrate the community counts, the off-diagonal entries of the adjacency Gram matrix, and centered cross-products of distinct adjacency rows. Use the count and Gram events to control the quantile neighborhoods and their population-row bias. Expand the smoothing fluctuation with the correct number of ordered cross terms. Retain the exceptional-column slack and a sharper centered-product variance bound to obtain the stated constants without changing the probability bound.

## Concentration Tool

We use Bernstein's inequality: for independent centered real variables W_j with |W_j|<=1 and sum_j E[W_j^2]<=V,
\[
\Pr\left(\left|\sum_jW_j\right|\ge t\right)
\le 2\exp\left[-\frac{t^2}{2(V+t/3)}\right],\qquad t>0.
\]
This also applies conditionally on the labels. All edge concentration calculations below are conditional on the complete label vector; their bounds are uniform in that vector and hence hold unconditionally after integration.

Write
\[
F_\pi=2K_n e^{-n\varepsilon_\pi^2/[4(1+\varepsilon_\pi)]},\quad
F_{AP}=2n^2 e^{-n(\varepsilon_{AP}-4/n)^2/[4(1+\varepsilon_{AP})]},\quad
F_m=n(n-1)e^{-n\varepsilon_m^2/[4(1+\varepsilon_m)]}.
\]
If F_pi+F_AP+F_m>=1, the requested probability lower bound is nonpositive and the finite-sample assertion is immediate. We can therefore assume their sum is less than one. Since epsilon_pi<rho_min<=1, n=3 would give F_pi>1. Thus n>=4 in the nontrivial case. Moreover, if epsilon_pi<4/n, then
\[
\frac{n\varepsilon_\pi^2}{4(1+\varepsilon_\pi)}<\frac4{n+4}\le\frac12,
\]
which again gives F_pi>1. Hence epsilon_pi>=4/n in the nontrivial case.

## 1. Community Counts

Let C_a=sum_{j=1}^n 1{z_j=a}. For each a, its summands are independent Bernoulli variables and their total variance is at most n/4. Bernstein at threshold n epsilon_pi/2 and a union bound over the K_n communities give an event E_pi on which
\[
\max_a|C_a/n-\rho_a|<\varepsilon_\pi/2,
\]
with
\[
\Pr(E_\pi^c)
\le 2K_n\exp\left[-\frac{n\varepsilon_\pi^2}{2+4\varepsilon_\pi/3}\right]
\le F_\pi.
\]
For an occupied community a, on this event,
\[
\left|\frac{C_a-1}{n-1}-\rho_a\right|
\le\frac{n|C_a/n-\rho_a|+1-\rho_a}{n-1}
<\frac{n\varepsilon_\pi/2+1}{n-1}
\le\varepsilon_\pi.
\]
The last inequality follows from epsilon_pi>=4/n>=2/(n-2). Consequently every vertex has more than (rho_min-epsilon_pi)(n-1)>h(n-1) other vertices in its community. In particular, there are at least ceil(h(n-1)) such vertices, and at least one.

## 2. Off-Diagonal Gram Concentration

Put
\[
G=AA^\top/n,\qquad Q=PP^\top/n,\qquad
\delta=\varepsilon_{AP}-2/n,\qquad t=\varepsilon_{AP}-4/n>0.
\]
For distinct i,r, the variables
\[
A_{ij}A_{rj}-P_{ij}P_{rj},\qquad j\notin\{i,r\},
\]
are conditionally independent, centered, and bounded in absolute value by one. Their total conditional variance is at most n. The two omitted columns contribute at most 2/n to |G_ir-Q_ir|, because A_ii=A_rr=0 and all entries of P are in [0,1]. Thus
\[
\Pr\bigl(|G_{ir}-Q_{ir}|\ge\delta\mid z\bigr)
\le 2\exp\left[-\frac{nt^2}{2(1+t/3)}\right]
\le 2\exp\left[-\frac{nt^2}{4(1+\varepsilon_{AP})}\right].
\]
A union bound, followed by integration over labels, gives an event E_AP with
\[
\Pr(E_{AP}^c)\le F_{AP},\qquad
\max_{i\ne r}|G_{ir}-Q_{ir}|<\delta.
\]
No diagonal Gram concentration is asserted. In general, diagonal entries of G do not concentrate around the corresponding entries of Q.

## 3. Quantile Neighborhoods and Population Bias

The matrix P is the full block matrix, including its diagonal. Therefore P_i=P_r whenever z_i=z_r. For such a pair, on E_AP and for k outside {i,r},
\[
|G_{ik}-G_{rk}|
\le |G_{ik}-Q_{ik}|+|G_{rk}-Q_{rk}|<2\delta.
\]
On E_pi there are at least ceil(h(n-1)) same-community candidates. Therefore the specified order-statistic quantile is less than 2delta, and
\[
d(i,r)<2\delta\quad\text{for every }r\in N_i.
\]

Fix a selected pair i,r. If z_i=z_r, its population-row distance is zero. Otherwise, E_pi supplies a vertex u other than i in i's community and a vertex v other than r in r's community. Because the communities are different, both u and v lie outside {i,r}. Equality of full population rows within communities gives
\[
\frac1n\|P_i-P_r\|_2^2
=Q_{ii}-Q_{ri}+Q_{rr}-Q_{ir}
=Q_{iu}-Q_{ru}+Q_{rv}-Q_{iv}.
\]
Every Gram entry on the last line is off-diagonal. Hence
\[
\frac1n\|P_i-P_r\|_2^2
\le |G_{iu}-G_{ru}|+|G_{rv}-G_{iv}|+4\delta
\le 2d(i,r)+4\delta<8\delta.
\]
Thus, simultaneously for all selected pairs,
\[
\frac1n\|P_i-P_r\|_2^2\le8\delta\le8\varepsilon_{AP}.
\]
No extra realized-community-size assumption is used, and equal-community pairs do not require a third same-community vertex.

## 4. Centered Cross-Products

Set U=A-P. For distinct r,s, define
\[
M(r,s)=\frac1{n-2}\left|\sum_{j\notin\{r,s\}}U_{rj}U_{sj}\right|.
\]
For each included column j, conditional independence of the directed edges gives
\[
\mathbb E[U_{rj}U_{sj}\mid z]=0,
\qquad
\mathbb E[(U_{rj}U_{sj})^2\mid z]
=P_{rj}(1-P_{rj})P_{sj}(1-P_{sj})\le\frac1{16}.
\]
The products are independent across included columns and bounded in absolute value by one. Bernstein therefore yields
\[
\Pr\bigl(M(r,s)\ge\varepsilon_m/2\mid z\bigr)
\le2\exp\left[-\frac{(n-2)\varepsilon_m^2}{1/2+4\varepsilon_m/3}\right].
\]
For n>=4,
\[
\frac{n-2}{1/2+4\varepsilon_m/3}
\ge\frac{n}{1+8\varepsilon_m/3}
\ge\frac{n}{4(1+\varepsilon_m)}.
\]
Since M(r,s)=M(s,r), a union bound over the n(n-1)/2 unordered pairs and integration over labels give an event E_m with
\[
\Pr(E_m^c)\le F_m,\qquad
\max_{r\ne s}M(r,s)<\varepsilon_m/2.
\]
The half-tolerance event, rather than merely M<epsilon_m, is what supports the final constants with correct ordered-pair counting.

## 5. Smoothing Fluctuation and Bias-Variance Bound

For each i write m_i=|N_i| and use the exact decomposition
\[
\widetilde P_i-P_i=X_i+Y_i,
\qquad
X_i=\frac1{m_i}\sum_{r\in N_i}U_r,
\qquad
Y_i=\frac1{m_i}\sum_{r\in N_i}(P_r-P_i).
\]
Convexity and the population-row bound give
\[
\frac1n\|Y_i\|_2^2\le8\delta.
\]
For distinct r,s, the two columns omitted in M contribute at most two in absolute value, including the generally nonzero diagonal entries U_rr=-P_rr and U_ss=-P_ss. Therefore, on E_m,
\[
\frac1n|\langle U_r,U_s\rangle|
\le\frac{n-2}{n}M(r,s)+\frac2n
\le\frac{n-2}{n}\frac{\varepsilon_m}{2}+\frac2n.
\]
Also ||U_r||_2^2/n<=1 deterministically. Expanding the quadratic norm with all m_i(m_i-1) ordered cross terms gives
\[
\begin{aligned}
\frac1n\|X_i\|_2^2
&\le\frac1{m_i}
+\frac{m_i-1}{m_i}
\left(\frac{n-2}{n}\frac{\varepsilon_m}{2}+\frac2n\right)\\
&\le\frac1{m_i}+\frac{\varepsilon_m}{2}+\frac2n.
\end{aligned}
\]
These inequalities hold for every subset of rows on the simultaneous events, so they apply to the data-dependent N_i without conditioning on its selection.

Finally,
\[
\begin{aligned}
\frac1n\|\widetilde P_i-P_i\|_2^2
&\le\frac2n\|X_i\|_2^2+\frac2n\|Y_i\|_2^2\\
&\le\frac2{m_i}+\varepsilon_m+\frac4n+16\delta\\
&=\frac2{m_i}+\varepsilon_m+16\varepsilon_{AP}-\frac{28}{n}\\
&\le\frac2{m_i}+\varepsilon_m+\frac2n+16\varepsilon_{AP}.
\end{aligned}
\]
The retained Gram-event slack is more than sufficient to cover the exceptional columns. This proves the exact frozen bound simultaneously for all rows on E_pi intersect E_AP intersect E_m.

## 6. Probability and Consistency

A union bound gives probability at least 1-F_pi-F_AP-F_m, exactly as requested. The nonpositive-lower-bound cases were already handled, so the finite-sample assertion holds throughout the stated domain.

The order-statistic definition, including ties, gives deterministically
\[
|N_i|\ge\lceil h(n-1)\rceil\ge h(n-1)>0.
\]
Consequently the simultaneous bound is at most
\[
\frac2{h(n-1)}+\varepsilon_m+\frac2n+16\varepsilon_{AP}.
\]
This tends to zero under the stated limits. The three exponent conditions make F_pi, F_AP, and F_m tend to zero. It follows directly that the maximum normalized squared row error converges to zero in probability.

## Obligation Closure

The count transfer, conditional concentration hypotheses, off-diagonal restriction, representative existence, quantile cardinality, ordered-pair expansion, exceptional columns, final constants, and asymptotic implication are explicitly derived above. Bernstein's inequality is the sole imported standard-independent result. No unresolved specialized dependency or private proof gap remains.
