# Reference Proof

## Proof Structure

1. Identify no-overlap clusterings with tuples of subproblem clusterings, factor their posterior weights, and separate the finite normalizing sum.
2. Verify support admissibility of the product of the approximation's marginals and of every coupling with those marginals.
3. Expand reverse KL against the conditional product posterior. The marginal cross-entropies are fixed, and entropy subadditivity gives the unique minimizing product coupling.
4. Transfer the comparison to the full posterior by calculating the effect of conditioning on the common support event.

## Complete Proof

Write \(\mathcal Z(A)\) for the set of partitions of a finite set \(A\), and put
\[
w(z)=\alpha^{K(z)}\prod_{B\in z}\Gamma(|B|)\ell(B),\qquad
Z=\sum_{z\in\mathcal Z(\{1,\ldots,t\})}w(z).
\]
The setup gives well-defined nonnegative weights and \(0<Z<\infty\), so \(P(z)=w(z)/Z\). This is the cluster-product posterior specified in the problem; no further property of the partition prior is needed.

### 1. Conditional factorization

Every \(z\in O\) has a unique representation as the union of a tuple \((z^1,\ldots,z^m)\), where \(z^r\in\mathcal Z(E^r)\). Conversely, every such tuple defines a clustering in \(O\). Since each block belongs to exactly one partition element,
\[
w(z)=\prod_{r=1}^m w_r(z^r),\qquad
w_r(u)=\alpha^{K(u)}\prod_{B\in u}\Gamma(|B|)\ell(B).
\]
These local weights are finite and nonnegative under the setup. Define
\[
Z_r=\sum_{u\in\mathcal Z(E^r)}w_r(u).
\]
All sums are finite, and the bijection gives
\[
Z_O:=\sum_{z\in O}w(z)=\prod_{r=1}^m Z_r.
\]
Because \(P(O)>0\), we have \(Z_O>0\), so every \(Z_r>0\). It follows that
\[
P_O(z)=\frac{w(z)}{Z_O}
=\prod_{r=1}^m\frac{w_r(z^r)}{Z_r},\qquad z\in O.
\]
Each local factor is a probability distribution. Summing over the other coordinates shows that it is precisely the marginal \(p_r\), proving the claimed conditional factorization for every finite \(m\).

### 2. Support and finiteness

Let \(q\) satisfy the task's support condition, let \(q_r\) be its marginals, and set \(q^*=\bigotimes_r q_r\). If \(q_r(u)>0\), there is a tuple with positive \(q\)-mass whose \(r\)-th coordinate is \(u\). That tuple has positive \(P_O\)-mass, so factorization implies \(p_r(u)>0\). Thus
\[
\operatorname{supp}(q_r)\subseteq\operatorname{supp}(p_r)
\]
for each \(r\). Consequently \(q^*\) is supported on \(P_O\). Moreover, any coupling \(a\) with these marginals can have positive mass only on \(\prod_r\operatorname{supp}(q_r)\), so it too is supported on \(P_O\). All relevant KL divergences are therefore finite. Zero-mass coordinates may be omitted from the calculations below.

### 3. Fixed-marginal optimization and equality

For any such coupling \(a\), define its Shannon entropy by \(H(a)=-\sum_z a(z)\log a(z)\), with \(0\log0=0\). The product form of \(P_O\) gives
\[
\begin{aligned}
\mathrm{KL}(a\Vert P_O)
&=\sum_z a(z)\log a(z)-\sum_{r=1}^m\sum_{u:q_r(u)>0}q_r(u)\log p_r(u)\\
&=-H(a)-\sum_{r=1}^m\sum_{u:q_r(u)>0}q_r(u)\log p_r(u).
\end{aligned}
\]
The second term depends only on the prescribed marginals. Finite-distribution entropy subadditivity states that \(H(a)\leq\sum_r H(q_r)\), with equality exactly for the independent product coupling. Here all its hypotheses hold: \(a\) is a probability distribution on a finite product space and the \(q_r\) are its coordinate marginals.

For completeness, the inequality and its equality condition follow directly in this setting. Expanding the product \(q^*\) shows
\[
\sum_r H(q_r)-H(a)=\mathrm{KL}(a\Vert q^*).
\]
On \(T=\{z:a(z)>0\}\), the product \(q^*(z)\) is positive. Using \(\log v\leq v-1\), with equality exactly when \(v=1\), gives
\[
-\mathrm{KL}(a\Vert q^*)
\leq\sum_{z\in T}\bigl(q^*(z)-a(z)\bigr)
=q^*(T)-1\leq0.
\]
Equality in KL therefore requires \(q^*(z)=a(z)\) on \(T\) and no \(q^*\)-mass outside \(T\), and hence is equivalent to \(a=q^*\). Conversely, equality is immediate when \(a=q^*\).

Also \(H(q^*)=\sum_r H(q_r)\), by direct finite summation. Subtracting the two KL expressions yields
\[
\mathrm{KL}(a\Vert P_O)-\mathrm{KL}(q^*\Vert P_O)
=H(q^*)-H(a)\geq0,
\]
with equality exactly when \(a=q^*\). Taking \(a=q\) proves the first comparison and establishes uniqueness among all couplings with the prescribed marginals.

### 4. Full-posterior comparison and particle consequence

Let \(\rho=P(O)>0\). For \(z\in O\), \(P(z)=\rho P_O(z)\). Extend every product-space distribution by zero outside \(O\). For any admissible coupling \(a\),
\[
\begin{aligned}
\mathrm{KL}(a\Vert P)
&=\sum_{z:a(z)>0}a(z)\log\frac{a(z)}{\rho P_O(z)}\\
&=\mathrm{KL}(a\Vert P_O)-\log\rho.
\end{aligned}
\]
The additive term is identical for all couplings, so the same inequality, minimizer, and equality condition hold for KL to \(P\). No assumption that \(P(O)=1\) is used.

A supported particle approximation is a finite weighted probability distribution satisfying exactly these hypotheses. Applying the result to that distribution proves that replacing it by the product of its subproblem marginals cannot increase reverse KL to either the conditional posterior or the full posterior. The argument already covers arbitrary finite \(m\), including singleton partition elements and marginals concentrated on a single clustering.
