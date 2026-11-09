# Reference Proof

## Proof Structure

1. Rewrite the Shapley functional as a linear sum over all coalitions and pair each coalition with its complement to show that the even component contributes zero.
2. Show that admissible functions correspond bijectively to independently boundary-constrained odd and even components.
3. Decompose the residual into odd and even parts; complementary pairing with symmetric weights cancels the cross terms.
4. Prove both inclusions in the equality of minimizer sets, including empty feasible classes, without assuming uniqueness or full rank.

## Complete Proof

Write \(f_o=f_{\rm odd}\) and \(f_e=f_{\rm even}\). Throughout, an argmin is the set of all feasible points whose objective is no larger than that of every other feasible point; an argmin over an empty domain is empty.

### Shapley values of the components

Let \(h\) be even. Reindexing the defining Shapley sum gives
\[
\phi_i(h)=\sum_{T\subseteq[d]}c_i(T)h(T),\qquad
c_i(T)=
\begin{cases}
p_{|T|-1},&i\in T,\\
-p_{|T|},&i\notin T.
\end{cases}
\]
Every index of \(p\) in this piecewise definition belongs to \(\{0,\ldots,d-1\}\), including at the boundary coalitions. For a complementary pair, choose its representative \(T\) containing \(i\). Then
\[
c_i(T)=p_{|T|-1},\qquad c_i(T^c)=-p_{d-|T|}.
\]
Binomial symmetry gives
\[
p_{|T|-1}=\frac1d\binom{d-1}{|T|-1}^{-1}
=\frac1d\binom{d-1}{d-|T|}^{-1}=p_{d-|T|}.
\]
Since \(h(T^c)=h(T)\), this pair contributes zero. The pairs partition all coalitions, so \(\phi_i(h)=0\). Linearity of the defining finite sum and \(f=f_o+f_e\) yield
\[
\phi_i(f)=\phi_i(f_o)+\phi_i(f_e)=\phi_i(f_o).
\]
This argument also applies when \(d=1\), for which \(p_0=1\).

### Independent boundary constraints

Closure of \(V\) under the projections gives every \(g\in V\) a unique decomposition \(g=g_o+g_e\), with \(g_o\in V_o\) and \(g_e\in V_e\). If \(g\in\mathcal F(f)\), then
\[
g_o(\varnothing)=\frac{g(\varnothing)-g([d])}{2}
=\frac{f(\varnothing)-f([d])}{2}=f_o(\varnothing),
\]
\[
g_e(\varnothing)=\frac{g(\varnothing)+g([d])}{2}
=\frac{f(\varnothing)+f([d])}{2}=f_e(\varnothing).
\]
Oddness and evenness give the corresponding equalities at \([d]\). Thus \(g_o\in\mathcal F_o(f_o)\) and \(g_e\in\mathcal F_e(f_e)\).

Conversely, if \(g_o\in\mathcal F_o(f_o)\) and \(g_e\in\mathcal F_e(f_e)\), their sum belongs to \(V\) and, at each boundary coalition \(B\in\{\varnothing,[d]\}\), satisfies
\[
(g_o+g_e)(B)=f_o(B)+f_e(B)=f(B).
\]
Consequently, addition is a bijection from
\(\mathcal F_o(f_o)\times\mathcal F_e(f_e)\) onto \(\mathcal F(f)\). In particular,
\[
\mathcal F(f)=\mathcal F_o(f_o)+\mathcal F_e(f_e),
\]
with unique odd and even components. This also shows that \(\mathcal F(f)\) is empty exactly when at least one component class is empty.

### Separation of the objective

For any feasible pair \((g_o,g_e)\), put \(r_o=f_o-g_o\) and \(r_e=f_e-g_e\). These residuals are odd and even, respectively, so
\[
r_o(S^c)=-r_o(S),\qquad r_e(S^c)=r_e(S).
\]
Because \(d\ge1\), no coalition is its own complement. Equal complementary multiplicities partition the sampled occurrences into pairs. For each pair, weight symmetry gives
\[
\begin{aligned}
&w_{|S|}(r_o(S)+r_e(S))^2
+w_{d-|S|}(r_o(S^c)+r_e(S^c))^2\\
&\quad=w_{|S|}\bigl((r_o(S)+r_e(S))^2+(-r_o(S)+r_e(S))^2\bigr)\\
&\quad=2w_{|S|}\bigl(r_o(S)^2+r_e(S)^2\bigr).
\end{aligned}
\]
The last expression is also the sum of the odd residual squares and the even residual squares over that pair, with their weights. Summing, with multiplicity, proves
\[
Q(g_o+g_e)=Q_o(g_o)+Q_e(g_e).
\]
For an empty sample this identity holds as an equality of empty sums.

### Equality of the minimizer sets

If either component class is empty, the feasible-set bijection shows that \(\mathcal F(f)\) is empty. The left-hand argmin and the right-hand Minkowski sum are then both empty.

Otherwise, take any \(g\in\operatorname*{argmin}_{\mathcal F(f)}Q\), if such a point exists, and write its unique feasible decomposition as \(g_o+g_e\). For every \(h_o\in\mathcal F_o(f_o)\), the function \(h_o+g_e\) is feasible. Hence
\[
Q_o(g_o)+Q_e(g_e)=Q(g)
\le Q(h_o+g_e)=Q_o(h_o)+Q_e(g_e).
\]
All these quantities are finite real numbers, so cancellation yields \(Q_o(g_o)\le Q_o(h_o)\). Thus \(g_o\) minimizes \(Q_o\). Holding \(g_o\) fixed and varying the even component proves that \(g_e\) minimizes \(Q_e\). This proves inclusion of the left-hand argmin in the right-hand Minkowski sum.

Conversely, let \(g_o\) and \(g_e\) be component minimizers. For any \(h\in\mathcal F(f)\), write its feasible decomposition as \(h_o+h_e\). Then
\[
Q(g_o+g_e)=Q_o(g_o)+Q_e(g_e)
\le Q_o(h_o)+Q_e(h_e)=Q(h).
\]
Thus \(g_o+g_e\) is a full minimizer, proving the reverse inclusion and therefore
\[
\operatorname*{argmin}_{g\in\mathcal F(f)}Q(g)
=
\operatorname*{argmin}_{g_o\in\mathcal F_o(f_o)}Q_o(g_o)
+
\operatorname*{argmin}_{g_e\in\mathcal F_e(f_e)}Q_e(g_e).
\]
The two-inclusion argument does not assume that a chosen minimizer exists, and so does not require a separate attainment theorem. It also requires neither uniqueness nor injectivity of the sampled evaluation map. If the sample is empty, every feasible point minimizes its objective, and the equality reduces to the feasible-set identity already proved. Zero-dimensional component spaces are covered by the same argument.

Finally, for every full minimizer \(g=g_o+g_e\), the first part gives \(\phi_i(g)=\phi_i(g_o)\). Thus only the odd fitted component carries the fitted Shapley values. This does not assert that an arbitrary sampled fit recovers \(\phi_i(f)\) exactly.

All obligations in this proof are established by the displayed finite-sum, boundary-evaluation, and minimizer-comparison arguments. No Fourier-regression or external regression-recovery theorem is invoked.
