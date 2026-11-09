# Reference Proof

## Proof Structure

Derive the normalized KL optimizer from a finite attained variational minimum. Apply this derivation to the marginal conditional losses and to the joint losses. Establish that the resulting input marginals are equivalent to P_x, compute both density ratios, calibrate positive thresholds, and use the finite-label Jensen inequality for the joint implication.

## Complete Proof

### 1. Finite attained KL minima

Let B be a probability measure, let F be a finite real-valued measurable function, and fix gamma>0. Suppose the minimum of

\[
J(U)=\mathbb E_U F+\gamma\,\mathrm{KL}(U\|B),\qquad U\ll B,
\]

is attained at U_* with \(\mathbb E_{U_*}|F|<\infty\) and \(\mathrm{KL}(U_*\|B)<\infty\). Denote its finite value by m.

For \(S_n=\{|F|\le n\}\), put

\[
Z_n=\int_{S_n}e^{-F/\gamma}\,dB.
\]

For every n with Z_n>0, the probability measure with B-density \(\mathbf 1_{S_n}e^{-F/\gamma}/Z_n\) has finite loss expectation and finite KL divergence. Substitution gives objective value \(-\gamma\log Z_n\). Thus

\[
m\le-\gamma\log Z_n,\qquad Z_n\le e^{-m/\gamma}.
\]

Because F is finite B-almost surely, monotone convergence gives

\[
0<Z:=\int e^{-F/\gamma}\,dB=\lim_n Z_n<\infty.
\]

Define G by \(dG/dB=e^{-F/\gamma}/Z\). Its density is strictly positive B-almost surely, so G and B are equivalent.

At any U with finite absolute loss expectation and finite KL divergence, the logarithmic density identity gives

\[
\mathrm{KL}(U\|G)
=\mathrm{KL}(U\|B)+\frac{\mathbb E_U F}{\gamma}+\log Z.
\]

This integration is legitimate: the negative part of \(\log(dU/dB)\) is U-integrable because \(t(-\log t)\le1/e\) for 0<t<1, and the other added term is integrable by the loss assumption.

For completeness, nonnegativity and the equality case of KL follow by integrating

\[
t\log t-t+1\ge0,
\]

with equality only at t=1, against its reference probability measure. Consequently,

\[
J(U)=\gamma\,\mathrm{KL}(U\|G)-\gamma\log Z\ge-\gamma\log Z.
\]

Applying this to U_* gives \(m\ge-\gamma\log Z\). The truncated competitors above give the reverse inequality after taking n to infinity. Hence equality holds and \(\mathrm{KL}(U_*\|G)=0\), which implies U_*=G. In particular, every chosen finite minimizer is the same normalized exponential reweighting. Its finite moments follow from the assumed finite moments of that minimizer, not from an unverified integrability assertion about a proposed optimizer.

### 2. Apply the variational derivation

For a in {h,e}, let

\[
L_a(x)=\sum_{y\in Y}\eta^*(y\mid x)\ell_a(x,y).
\]

These are finite measurable functions because Y is finite and the losses are real-valued. Applying Step 1 with B=P_x and F=L_a gives

\[
\frac{dQ_m^a}{dP_x}(x)=q_m^a(x)
=\frac{e^{-L_a(x)/\gamma}}{Z_m^a},
\qquad
Z_m^a=\mathbb E_{P_x}e^{-L_a/\gamma}\in(0,\infty).
\]

Applying Step 1 with B=P and F=ell_a gives

\[
\frac{dR_j^a}{dP}(x,y)=\frac{e^{-\ell_a(x,y)/\gamma}}{Z_j^a},
\qquad
Z_j^a=\mathbb E_Pe^{-\ell_a/\gamma}\in(0,\infty).
\]

Define privately

\[
A_a(x)=\sum_{y\in Y}\eta^*(y\mid x)e^{-\ell_a(x,y)/\gamma}.
\]

For every x, A_a(x) is finite and strictly positive. Integrating the joint density over labels gives

\[
\frac{dQ_j^a}{dP_x}(x)=q_j^a(x)=\frac{A_a(x)}{Z_j^a},
\qquad Z_j^a=\mathbb E_{P_x}A_a.
\]

Both marginal-ideal densities and both joint-ideal input densities are strictly positive and finite P_x-almost surely. Therefore all four input ideals are equivalent to P_x. In particular Q_i^h is absolutely continuous with respect to Q_i^e, and every chosen version of rho_i agrees P_x-almost surely with q_i^h/q_i^e. This justifies the public version-independent almost-sure conclusions.

### 3. Marginal equivalence

The marginal ratio satisfies

\[
\rho_m(x)=\frac{Z_m^e}{Z_m^h}
\exp\left(\frac{L_e(x)-L_h(x)}{\gamma}\right)
\quad(P_x\text{-a.s.}).
\]

For the prescribed real cutoff c, choose

\[
\tau_m=\frac{Z_m^e}{Z_m^h}e^{c/\gamma}\in(0,\infty).
\]

Since gamma>0 and the exponential is strictly increasing,

\[
\rho_m(x)\le\tau_m
\iff L_e(x)-L_h(x)\le c
\iff \mathbb E_{\eta^*(\cdot\mid x)}[\ell_e(x,Y)-\ell_h(x,Y)]\le c
\]

P_x-almost surely, including equality at the boundary. This proves the first assertion.

### 4. Joint implication

The public expert-tilted kernel is well-defined because its denominator is A_e(x)>0. It is measurable and sums to one. Direct substitution gives

\[
\frac{A_h(x)}{A_e(x)}
=\mathbb E_{\widetilde\eta_\gamma(\cdot\mid x)}
\exp\left(\frac{\ell_e(x,Y)-\ell_h(x,Y)}{\gamma}\right).
\]

Thus

\[
\rho_j(x)=\frac{Z_j^e}{Z_j^h}
\mathbb E_{\widetilde\eta_\gamma(\cdot\mid x)}
\exp\left(\frac{\ell_e(x,Y)-\ell_h(x,Y)}{\gamma}\right)
\quad(P_x\text{-a.s.}).
\]

Choose

\[
\tau_j=\frac{Z_j^e}{Z_j^h}e^{c/\gamma}\in(0,\infty).
\]

On the full-measure set where the ratio identity holds, r_j(x)=1 implies that the exponential expectation above is at most e^{c/gamma}. Every loss difference is finite and there are only finitely many labels. Jensen's inequality for the convex exponential therefore applies without any additional moment condition and gives

\[
\exp\left(
\frac{\mathbb E_{\widetilde\eta_\gamma(\cdot\mid x)}[\ell_e(x,Y)-\ell_h(x,Y)]}{\gamma}
\right)
\le
\mathbb E_{\widetilde\eta_\gamma(\cdot\mid x)}
\exp\left(\frac{\ell_e(x,Y)-\ell_h(x,Y)}{\gamma}\right)
\le e^{c/\gamma}.
\]

Taking logarithms and multiplying by gamma proves the second assertion. The argument applies to every finite real c and every fixed gamma>0; the thresholds may depend on the fixed distribution, losses, gamma, and c, but not on x.

## Private Source-Convention Notes

The public c is a loss-difference cutoff. For an objective that adds a calling cost b when deferring, the conditional-risk comparison instead gives cutoff -b. This corrects the source's sign error without changing either frozen explicit inequality.

If a normalized ratio is (Z_i^e/Z_i^h) times an unnormalized ratio, the corresponding unnormalized threshold is tau Z_i^h/Z_i^e. This corrects the source's inverted threshold conversion. Both source repairs are recorded in the provenance.

## Proof-Obligation Closure

The finite normalizers, optimizer representation and uniqueness, marginalization, mutual absolute continuity, independence from Radon–Nikodym versions, marginal equivalence, joint tilted identity, Jensen hypotheses, positive constant thresholds, and boundary ties are all explicitly established above. No paper-specific prior result or specialized external method remains an unresolved obligation.
