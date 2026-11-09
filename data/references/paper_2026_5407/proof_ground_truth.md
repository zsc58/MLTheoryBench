# Reference Proof

## Proof Obligations

1. Establish normalized escorts and derive their Gibbs variational optimality, with legitimate entropy manipulations.
2. Justify the log-moment derivatives and endpoint continuity, and prove both KL monotonicities and their strictness.
3. Select the trust-region temperature and identify every optimizer, including the inactive, equality, and degenerate cases.
4. Establish finite residual-weight second moments and the variance/chi-square identity.
5. Prove variance monotonicity and strictness on the entire closed path without assuming differentiability at moment parameter two.

## Complete Proof

### step_001: Normalization and Gibbs variational identity

Put
\[
Y=\log R,\qquad M(s)=\mathbb E_P[R^s],\qquad
\Lambda(s)=\log M(s),\qquad 0\le s\le2.
\]
The density ratio is positive and finite almost surely. Since \(R^s\le1+R^2\) for \(0\le s\le2\), all these moments are finite. They are strictly positive, and dominated convergence makes \(M\), hence \(\Lambda\), continuous on \([0,2]\). Moreover, \(M(0)=M(1)=1\), so
\[
\frac{dq_\tau}{dP}=\exp\{\tau Y-\Lambda(\tau)\},\qquad
q_0=P,\qquad q_1=\Pi.
\]
Every escort is equivalent to \(P\) and \(\Pi\).

The logarithmic assumptions at parameters zero and one imply that
\[
H=(1+R)(1+|Y|^2)
\]
is integrable under \(P\). For \(0\le\tau\le1\), both \(R^\tau|Y|\) and \(R^\tau|Y|^2\) are bounded by \(H\). Consequently \(Y\) is integrable under every \(q_\tau\), and the logarithms of its densities relative to \(P\) and \(\Pi\) are integrable. In particular both escort KL divergences are finite. This also proves that \(D_{\mathrm{KL}}(P\|\Pi)\) and \(D_{\mathrm{KL}}(\Pi\|P)\) are finite.

We derive the Gibbs variational calculation directly. Suppose \(q\) has finite KL divergence to both \(P\) and \(\Pi\). For a probability density \(f\) relative to a probability measure, the negative part of \(f\log f\) has integral at most \(1/e\). Thus finite relative entropy implies absolute integrability, under \(q\), of the corresponding log density. Subtracting the two log densities shows that \(Y\) is integrable under \(q\). For \(0<\tau\le1\), the density formula therefore gives the well-defined identity
\[
D_{\mathrm{KL}}(q\|q_\tau)
=
\tau D_{\mathrm{KL}}(q\|\Pi)
+(1-\tau)D_{\mathrm{KL}}(q\|P)
+\Lambda(\tau).
\]
Relative entropy is nonnegative and vanishes only when its two probability measures agree: integrate the elementary inequality \(f\log f-f+1\ge0\), with equality only at \(f=1\).

With \(\lambda=(1-\tau)/\tau\), the identity becomes
\[
D_{\mathrm{KL}}(q\|\Pi)
+\lambda\bigl(D_{\mathrm{KL}}(q\|P)-\varepsilon\bigr)
=
\frac{1}{\tau}D_{\mathrm{KL}}(q\|q_\tau)
-\frac{\Lambda(\tau)}{\tau}-\lambda\varepsilon.
\]
Thus the normalized Gibbs density \(R^\tau/M(\tau)\) uniquely minimizes this Lagrangian among measures with both divergences finite. This supplies the variational step without invoking an unspecified infinite-dimensional KKT theorem. Every feasible competitor has finite divergence to \(P\); competitors with infinite objective cannot improve on a finite-objective feasible escort. The appropriate feasible escort is selected below.

### step_002: Escort KL geometry and endpoint regularity

On \([0,1]\), the integrable bound \(H\) justifies differentiation under the expectation and continuity of the first two moment derivatives, with one-sided interpretations at the endpoints. Thus
\[
\Lambda'(\tau)=\mathbb E_{q_\tau}[Y],\qquad
\Lambda''(\tau)=\operatorname{Var}_{q_\tau}(Y)
\]
for \(0<\tau<1\), and the first-derivative expression extends continuously to both endpoints.

Integrating the log-density formulas yields, for every \(\tau\in[0,1]\),
\[
F(\tau):=D_{\mathrm{KL}}(q_\tau\|P)
=\tau\Lambda'(\tau)-\Lambda(\tau),
\]
\[
G(\tau):=D_{\mathrm{KL}}(q_\tau\|\Pi)
=(\tau-1)\Lambda'(\tau)-\Lambda(\tau).
\]
Both functions are continuous on the closed interval. On its interior,
\[
F'(\tau)=\tau\operatorname{Var}_{q_\tau}(Y)\ge0,
\qquad
G'(\tau)=-(1-\tau)\operatorname{Var}_{q_\tau}(Y)\le0.
\]
It follows that \(F\) is nondecreasing and \(G\) is nonincreasing on \([0,1]\).

If \(P\ne\Pi\), then \(R\) is not constant almost surely: a constant density ratio would equal one by normalization. Since every escort is equivalent to \(P\), \(Y\) is nonconstant under every escort. Its finite variance is therefore strictly positive. Both derivative inequalities are strict on \((0,1)\). Continuity and weak monotonicity at the endpoints extend the strict inequalities to any two distinct parameters in \([0,1]\): one can choose two interior parameters between them and compare through those parameters.

### step_003: Trust-region temperature and exact optimizer

Let \(d=D_{\mathrm{KL}}(\Pi\|P)<\infty\). If \(\varepsilon\ge d\), then \(\Pi\) is feasible and has objective zero. Nonnegativity and its equality condition show that it is the unique optimizer. Therefore \(q_\varepsilon^*=\Pi=q_1\), including when \(\varepsilon=d\).

Now suppose \(0<\varepsilon<d\). Then \(P\ne\Pi\). The continuous strictly increasing function \(F\) satisfies
\[
F(0)=0,\qquad F(1)=d.
\]
The intermediate value theorem gives a unique \(\tau_*\in(0,1)\) with \(F(\tau_*)=\varepsilon\). In particular, \(q_{\tau_*}\) is feasible and has finite objective.

For any feasible \(q\) with finite objective, subtract the Gibbs identity evaluated at \(q_{\tau_*}\) from the identity evaluated at \(q\). This gives
\[
D_{\mathrm{KL}}(q\|\Pi)-D_{\mathrm{KL}}(q_{\tau_*}\|\Pi)
=
\frac{1}{\tau_*}D_{\mathrm{KL}}(q\|q_{\tau_*})
+\frac{1-\tau_*}{\tau_*}
\bigl(\varepsilon-D_{\mathrm{KL}}(q\|P)\bigr)
\ge0.
\]
Equality requires \(q=q_{\tau_*}\). A feasible measure with infinite objective cannot be an optimizer because this escort has finite objective. Hence every optimizer equals \(q_{\tau_*}\). The corresponding multiplier is \(\lambda=(1-\tau_*)/\tau_*>0\), and the constraint is active.

If \(P=\Pi\), then \(R=1\) almost surely and all escorts equal \(P\). Here \(d=0\), so every allowed \(\varepsilon>0\) belongs to the preceding target-feasible case. The optimizer is \(P=\Pi\), and \(\tau_*=1\) is permitted; no uniqueness of temperature is asserted in this case.

### step_004: Finite residual variance and its representation

Equivalence of the laws gives
\[
\frac{d\Pi}{dq_\tau}=M(\tau)R^{1-\tau},\qquad
W_\tau=Z\frac{d\Pi}{dq_\tau}.
\]
Changing measure to \(P\),
\[
\mathbb E_{q_\tau}\!\left[\left(\frac{d\Pi}{dq_\tau}\right)^2\right]
=M(\tau)^2\frac{\mathbb E_P[R^{2-\tau}]}{M(\tau)}
=M(\tau)M(2-\tau)<\infty.
\]
Thus all variances and chi-square divergences in the target are finite. Since the density ratio integrates to one,
\[
Z^{-2}\operatorname{Var}_{q_\tau}(W_\tau)
=\mathbb E_{q_\tau}\!\left[\left(\frac{d\Pi}{dq_\tau}\right)^2\right]-1
=\chi^2(\Pi\|q_\tau),
\]
and
\[
1+\chi^2(\Pi\|q_\tau)
=M(\tau)M(2-\tau)
=\exp\{\Lambda(\tau)+\Lambda(2-\tau)\}.
\]

### step_005: Variance monotonicity and strictness

The derivative at moment parameter two is not needed. For any compact interval \([a,b]\subset(0,2)\) and \(k=0,1,2\),
\[
\sup_{s\in[a,b]}R^s|Y|^k\le C_{a,b,k}(1+R^2).
\]
Indeed, on \(0<R\le1\), the quantity \(R^a|\log R|^k\) is bounded; on \(R\ge1\), \(R^b(\log R)^k\) is bounded by a constant times \(R^2\), because \(b<2\). Dominated differentiation therefore applies throughout \((0,2)\).

For this private calculation define the probability measure
\[
\nu_s(dx)=\frac{R(x)^s}{M(s)}P(dx),\qquad 0<s<2.
\]
Differentiating the logarithm of \(M\) now gives
\[
\Lambda''(s)
=\frac{\mathbb E_P[R^sY^2]}{M(s)}
-\left(\frac{\mathbb E_P[R^sY]}{M(s)}\right)^2
=\operatorname{Var}_{\nu_s}(Y)\ge0.
\]
Consequently \(\Lambda'\) is nondecreasing on \((0,2)\). If \(P\ne\Pi\), equivalence of \(\nu_s\) and \(P\) makes the displayed variance strictly positive, so \(\Lambda'\) is strictly increasing.

For \(0<\tau<1\), both arguments below lie in \((0,2)\), and \(\tau<2-\tau\). Hence
\[
\frac{d}{d\tau}\log\bigl(1+\chi^2(\Pi\|q_\tau)\bigr)
=\Lambda'(\tau)-\Lambda'(2-\tau)\le0,
\]
with strict inequality when \(P\ne\Pi\). Continuity of \(M\) on \([0,2]\) makes the chi-square expression continuous on \([0,1]\), extending weak monotonicity to both endpoints. In the nonconstant case, comparison through two interior points between any two distinct closed-interval parameters extends strict decrease to the whole interval. The residual variance has the same behavior by step_004.

At \(\tau=1\), \(M(1)=1\), so both quantities vanish. If \(P=\Pi\), they vanish identically. All five proof obligations are therefore closed under exactly the public assumptions.
