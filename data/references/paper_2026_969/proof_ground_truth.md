# Reference Proof

## Proof Structure

Verify that the mixtures and barycenters lie in the finite-second-moment domain. Use the one-dimensional Wasserstein quantile identity to work in L2((0,1)). Insert each within-group barycenter between the group mixture and global barycenter, expand the squared norm, and sum over groups. Apply Cauchy–Schwarz to the interaction term.

## Complete Proof

### 1. Domain and barycenter existence

Write P2(R) for the probability laws on R with finite second moment. Each group mixture belongs to P2(R), since
\[
\int z^2\,d\nu_s^{\times}(z)
=\sum_j\pi_{j|s}\int z^2\,d\nu_{j,s}(z)<\infty.
\]
For a law \(\mu\), its generalized quantile sends a uniform random variable on (0,1) to a variable with law \(\mu\): the generalized-inverse property gives
\[
\bigl|\{u\in(0,1):Q_\mu(u)\le x\}\bigr|=F_\mu(x).
\]
Consequently, for \(\mu\in\mathcal P_2(\mathbb R)\),
\[
\int_0^1 Q_\mu(u)^2\,du=\int z^2\,d\mu(z)<\infty.
\]

We use the standard independent one-dimensional Wasserstein quantile identity: for any \(\mu,\eta\in\mathcal P_2(\mathbb R)\),
\[
W_2(\mu,\eta)^2=\int_0^1|Q_\mu(u)-Q_\eta(u)|^2\,du.
\]
This is the result indexed by theory_018, stated in the source at L000119–L000123 and L000773–L000781. Its hypotheses hold for the local laws and mixtures, and the following construction verifies them for the barycenters as well.

For a finite collection \(\mu_i\in\mathcal P_2(\mathbb R)\) with weights \(w_i\ge0\) and \(\sum_iw_i=1\), put
\[
q(u)=\sum_iw_iQ_{\mu_i}(u).
\]
This function is finite on (0,1), nondecreasing, and left-continuous. Moreover,
\[
\int_0^1q(u)^2\,du\le\sum_iw_i\int_0^1Q_{\mu_i}(u)^2\,du<\infty.
\]
Let \(\rho\) be the law of \(q(U)\), with U uniform on (0,1). Then \(\rho\in\mathcal P_2(\mathbb R)\) and \(Q_\rho=q\) almost everywhere. To see the latter directly, at each continuity point u of q and for sufficiently small \(h>0\), monotonicity implies
\[
q(u-h)\le Q_\rho(u)\le q(u+h).
\]
For the lower inequality, if \(x<q(u-h)\), the set where \(q\le x\) has measure at most \(u-h<u\); for the upper inequality, the set where \(q\le q(u+h)\) has measure at least \(u+h\). Let h decrease to zero. A monotone function has at most countably many discontinuities, proving the almost-everywhere assertion.

For any \(\eta\in\mathcal P_2(\mathbb R)\), weighted least squares and the quantile identity give
\[
\sum_iw_iW_2(\mu_i,\eta)^2
=\sum_iw_i\|Q_{\mu_i}-q\|_2^2+\|q-Q_\eta\|_2^2.
\]
Thus \(\rho\) is a minimizer, and every minimizer has quantile q almost everywhere and hence the same law. Applying this argument first with weights \(\pi_{j|s}\) and then with weights \(\alpha_s\) proves existence and uniqueness of the centers in the task and gives
\[
Q_s^*=\sum_j\pi_{j|s}Q_{j,s},\qquad
Q^{\times *}=\sum_s\alpha_sQ_s^{\times}
\quad\text{almost everywhere}.
\]
These characterizations verify the setup; the remaining proof needs only that the centers are in P2(R).

### 2. Exact decomposition

Set
\[
a_s=Q_s^{\times}-Q_s^*,\qquad b_s=Q_s^*-Q^{\times *}.
\]
All these functions belong to L2((0,1)), so their inner products and the remainder are finite. Since \(Q_s^{\times}-Q^{\times *}=a_s+b_s\), the quantile identity yields
\[
\begin{aligned}
G_2
&=\sum_s\alpha_s\|a_s+b_s\|_2^2\\
&=\sum_s\alpha_s\|a_s\|_2^2
 +\sum_s\alpha_s\|b_s\|_2^2
 +2\sum_s\alpha_s\langle a_s,b_s\rangle\\
&=V_{\rm mix}+V_{\rm bar}+R.
\end{aligned}
\]

### 3. Remainder estimate

Cauchy–Schwarz in L2, followed by Cauchy–Schwarz for the finite vectors \((\sqrt{\alpha_s}\|a_s\|_2)_s\) and \((\sqrt{\alpha_s}\|b_s\|_2)_s\), gives
\[
\begin{aligned}
|R|
&\le2\sum_s\alpha_s\|a_s\|_2\|b_s\|_2\\
&\le2\left(\sum_s\alpha_s\|a_s\|_2^2\right)^{1/2}
       \left(\sum_s\alpha_s\|b_s\|_2^2\right)^{1/2}\\
&=2\sqrt{V_{\rm mix}V_{\rm bar}}.
\end{aligned}
\]
No step divides by a weight or variance. Thus zero weights and zero variance terms require no additional assumption or separate limiting argument.

## Obligation Audit

- Finite moments of mixtures: derived by integration against a finite mixture.
- Square-integrability of quantiles: derived from the generalized-inverse distribution identity.
- Admissibility, existence, and finite moments of barycenters: derived by the monotone quantile construction and weighted least squares.
- Wasserstein-to-quantile reduction: supplied by the audited standard independent result theory_018, with its hypotheses checked.
- Exact identity: derived by expansion of the squared L2 norm.
- Remainder bound, including degenerate weights and zero terms: derived by the two Cauchy–Schwarz inequalities.

There are no unresolved theorem-critical obligations. Approximation, quantile-inversion, and concentration results are not used.
