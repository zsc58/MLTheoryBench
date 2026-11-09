# Reference Proof

## Source Contract and Proof Obligations

The selected result concerns only the deterministic energy-constrained relaxation. The source explicitly isolates this problem from the joint cardinality-and-energy problem at L000062–L000067; Appendix A gives the corresponding box-constrained LP at L000126–L000134. Thus no cardinality constraint, distributional assumption, or strict positivity assumption on gradient magnitudes is imposed here.

The proof must establish:

1. The correct feasible domain and existence of an optimizer.
2. Necessity and sufficiency of the common-threshold characterization, including the energy condition.
3. Optimality of the sorted budget-filling construction, with cost-weighted tie allocation and exact exhaustion.
4. The cases of budgets at least the total coordinate cost, zero scores, and optimal masks with unused energy.

The argument follows the source's LP and multiplier architecture. Its certificate sufficiency and necessity are verified directly below, so no unproved general KKT theorem or specialized external dependency is required.

## Complete Proof

### Step 1: Formulation and Existence

Put \(a_j=|g_j|\), so \(a_j\ge0\), and let
\[
C=\sum_{j=1}^d c_j>0,
\qquad
\mathcal F=\{m\in[0,1]^d:c^\top m\le E\}.
\]
The vector \(0\) is feasible. The feasible set is closed and bounded, and the objective is the finite linear function \(a^\top m\). The explicit maximizing masks constructed in Steps 3 and 4 will establish existence directly.

### Step 2: Necessary and Sufficient Threshold Conditions

Consider the Lagrangian
\[
L(m,\lambda,\alpha,\beta)
=a^\top m+\lambda(E-c^\top m)
+\sum_j\alpha_jm_j+\sum_j\beta_j(1-m_j),
\]
where \(\lambda,\alpha_j,\beta_j\ge0\). The relevant stationarity and complementary-slackness equations are
\[
a_j-\lambda c_j+\alpha_j-\beta_j=0,
\qquad
\alpha_jm_j=0,
\qquad
\beta_j(1-m_j)=0,
\qquad
\lambda(E-c^\top m)=0.
\]

For a feasible mask satisfying these equations, if \(m_j=1\), then \(\alpha_j=0\) and \(a_j-\lambda c_j=\beta_j\ge0\). If \(m_j=0\), then \(\beta_j=0\) and \(a_j-\lambda c_j=-\alpha_j\le0\). If \(0<m_j<1\), both box multipliers vanish and \(a_j=\lambda c_j\). Since \(c_j>0\), these statements imply full selection above the score threshold \(\lambda\), zero selection below it, and fractional selection only at equality. The last equation says that a positive threshold requires the energy budget to be exhausted.

We first verify sufficiency without appealing to a general optimization theorem. Suppose a feasible \(m\) satisfies the public threshold conditions with threshold \(\tau\). Set
\[
\lambda=\tau,
\qquad
\alpha_j=\max\{\lambda c_j-a_j,0\},
\qquad
\beta_j=\max\{a_j-\lambda c_j,0\}.
\]
These nonnegative multipliers satisfy stationarity. A positive \(\alpha_j\) implies \(s_j<\lambda\), hence \(m_j=0\); a positive \(\beta_j\) implies \(s_j>\lambda\), hence \(m_j=1\). The energy condition gives \(\lambda(E-c^\top m)=0\). Therefore all complementary-slackness equations hold.

For any feasible \(x\), every constraint term added to \(a^\top x\) in the Lagrangian is nonnegative, so
\[
a^\top x\le L(x,\lambda,\alpha,\beta).
\]
Stationarity makes this Lagrangian independent of \(x\):
\[
L(x,\lambda,\alpha,\beta)=\lambda E+\sum_j\beta_j.
\]
Complementary slackness at \(m\) gives
\[
\lambda E+\sum_j\beta_j=L(m,\lambda,\alpha,\beta)=a^\top m.
\]
Consequently \(a^\top x\le a^\top m\) for every feasible \(x\), proving sufficiency.

For necessity, let \(m\) be any optimal mask.

If \(c^\top m<E\), every coordinate with \(a_j>0\) must have \(m_j=1\). Otherwise, for such a coordinate with \(m_j<1\), choosing
\[
0<\varepsilon\le\min\{1-m_j,(E-c^\top m)/c_j\}
\]
and increasing \(m_j\) by \(\varepsilon\) preserves feasibility and strictly increases the objective. Thus \(\tau=0\) gives the required threshold conditions: all positive scores are fully selected, there are no negative scores, and zero-score coordinates are constrained only by feasibility.

Now suppose \(c^\top m=E\). If every coordinate is fully selected, choose \(\tau=0\). Otherwise define
\[
I=\{i:m_i<1\},
\qquad
J=\{j:m_j>0\}.
\]
The set \(I\) is nonempty by the present case assumption. The set \(J\) is nonempty because \(c^\top m=E>0\).

For every \(i\in I\) and \(j\in J\), optimality forces \(s_i\le s_j\). Indeed, if \(s_i>s_j\), the indices are distinct, and
\[
\delta=\min\{c_i(1-m_i),c_jm_j\}>0
\]
can be transferred as an amount of energy from coordinate \(j\) to coordinate \(i\). Replacing \(m_i\) by \(m_i+\delta/c_i\) and \(m_j\) by \(m_j-\delta/c_j\) preserves the box constraints and total energy, while increasing the objective by
\[
\delta(s_i-s_j)>0,
\]
a contradiction.

It follows that
\[
0\le\max_{i\in I}s_i\le\min_{j\in J}s_j.
\]
Choose any \(\tau\) in this closed interval. If \(s_j>\tau\), then \(j\notin I\), so \(m_j=1\). If \(s_j<\tau\), then \(j\notin J\), so \(m_j=0\). The energy condition holds because the budget is exhausted. This proves necessity, including cases with several fractional coordinates tied at the threshold.

Together, necessity and sufficiency establish the entire claimed characterization and verify the multiplier conditions for this LP directly.

### Step 3: Sorted Construction, Ties, and Exact Exhaustion

Order the indices so that \(s_{(1)}\ge\cdots\ge s_{(d)}\). Define cumulative costs
\[
B_0=0,
\qquad
B_r=\sum_{q=1}^r c_{(q)}\quad(1\le r\le d).
\]
Because all costs are positive, these cumulative costs are strictly increasing.

Suppose \(E<C\). There is a unique \(k\in\{1,\ldots,d\}\) such that
\[
B_{k-1}\le E<B_k.
\]
Define
\[
m_{(q)}=
\begin{cases}
1,&q<k,\\
(E-B_{k-1})/c_{(k)},&q=k,\\
0,&q>k.
\end{cases}
\]
The boundary fraction lies in \([0,1)\), and \(c^\top m=E\), so this mask is feasible. With \(\tau=s_{(k)}\), every score strictly above \(\tau\) is fully selected and every score strictly below \(\tau\) is unselected. Step 2 therefore proves optimality.

If \(E=B_r\) for some \(1\le r<d\), this construction has \(k=r+1\) and boundary fraction zero. Equivalently, any threshold in \([s_{(r+1)},s_{(r)}]\) works. Thus exact exhaustion creates no undefined boundary case.

For a tied threshold block \(T=\{j:s_j=\tau\}\), its objective contribution is
\[
\sum_{j\in T}a_jm_j=\tau\sum_{j\in T}c_jm_j.
\]
Consequently, changing the allocation within that block while preserving its total allocated energy, respecting the box constraints, and leaving other coordinates unchanged preserves both feasibility and the objective. This proves the advertised arbitrary tie allocation. The conserved quantity is \(\sum_{j\in T}c_jm_j\), not the unweighted sum of mask entries.

### Step 4: Large Budgets and Zero Scores

If \(E\ge C\), the all-ones mask is feasible. Since \(0\le m_j\le1\) and \(a_j\ge0\), every feasible mask satisfies
\[
a^\top m\le\sum_j a_j.
\]
The all-ones mask attains this bound and is therefore optimal, including the boundary case \(E=C\). It also satisfies the threshold characterization with \(\tau=0\).

This is an existence assertion, not a uniqueness assertion. For \(E\ge C\), a mask is optimal precisely when every coordinate with \(a_j>0\) is fully selected; zero-magnitude coordinates may take arbitrary values in \([0,1]\).

More generally, for any allowed budget, a feasible mask that fully selects every positive-magnitude coordinate attains the same upper bound \(\sum_j a_j\) and is optimal even if it leaves energy unused. Conversely, Step 2 shows that every slack optimum must fully select those positive-magnitude coordinates. When the threshold is zero, its tied coordinates therefore need not consume all remaining energy. When the threshold is positive, the energy condition requires exhaustion.

In particular, if \(g=0\), every feasible mask has objective zero and satisfies the characterization with threshold zero. The sorted budget-filling mask is still one valid optimal choice.

The constructions cover all \(E>0\), all positive cost vectors, and all real gradient vectors. Every listed proof obligation is closed.
