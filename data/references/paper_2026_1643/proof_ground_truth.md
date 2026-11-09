# Reference Proof

## Proof Structure

Construct a DKW p-value for each fixed candidate CDF and establish its super-uniformity, including the nonstrict-tail boundary. Derive e-value validity directly from the calibrator assumptions. Show that the displayed closed band contains the strict e-value acceptance region; exact equality of these regions is not required. Bound each selected configuration's miscoverage indicator by its e-value divided by the random threshold. Aggregate pointwise over the selected set and then over all candidates before taking expectations.

## Complete Proof

All sample sizes, distributions, delta, and the calibrator f are fixed. The selected set A=S(D) can depend on all observations. Expectations below are under their joint law; no independence between configurations or between selection and inference is assumed.

### 1. Statistics and measurability

For each fixed candidate CDF F, define

T_k(F)=sup_{x in R}|Fhat_k(x)-F(x)|,

p_k(F)=min{1,2 exp(-2 n_k T_k(F)^2)},

E_k(F)=f(p_k(F)).

Both CDFs are right-continuous, so the supremum defining T_k(F) equals the supremum over rational x. Thus T_k(F) is measurable. Also 0<=T_k(F)<=1, so p_k(F)>0. A monotone f is measurable. The measurable finite-valued selected set makes a=|A| measurable. The constructed miscoverage events below are measurable because they are events of the form T_k(F_k)>epsilon_k, with a measurable radius, or are empty.

### 2. DKW p-value validity

The standard independent DKW result used here states: for n positive iid real observations from any fixed CDF F, with empirical CDF Fhat,

P(sup_{x in R}|Fhat(x)-F(x)|>t)<=2 exp(-2 n t^2), for every t>0.

Its hypotheses hold within each configuration under the candidate null F_k=F. No continuity of F or moments of the observations are required.

For t>0, choose positive t_j increasing to t. The events {T_k(F)>t_j} decrease to {T_k(F)>=t}. Continuity of probability and the DKW bound therefore give

P(T_k(F)>=t)<=lim_j 2 exp(-2 n_k t_j^2)=2 exp(-2 n_k t^2).

For alpha in (0,1), truncation at one does not affect the event p_k(F)<=alpha, and

{p_k(F)<=alpha}={T_k(F)>=sqrt(log(2/alpha)/(2 n_k))}.

Under F_k=F, the preceding bound proves P(p_k(F)<=alpha)<=alpha. In particular, p_k(F_k) is super-uniform. The same bound holds at alpha=1 trivially, and P(p_k(F_k)=0)=0.

### 3. Calibration

Let P be any super-uniform random variable in [0,1]. For each s>=0, monotonicity implies that B_s={u in [0,1]:f(u)>s} is an initial interval, possibly empty and with either endpoint convention. If its right endpoint is b_s, super-uniformity gives

P(f(P)>s)<=b_s=Lebesgue_measure(B_s).

For b_s=0 this follows from P(P=0)=0, and for b_s=1 it is immediate. The nonnegative layer-cake representation and Tonelli's theorem yield

E[f(P)]=integral_0^infinity P(f(P)>s)ds
        <=integral_0^infinity Lebesgue_measure(B_s)ds
        =integral_0^1 f(u)du
        <=1.

Apply this argument to each P=p_k(F_k). It follows that E[E_k(F_k)]<=1. This derivation covers extended-valued calibrators and implies that the true-CDF e-values are finite almost surely.

### 4. Generalized inverse and closed-band containment

On a nonempty selection, write a=|A| and q=m/(delta a). Since 1<=a<=m and delta<1, q>1. Set r=f^{-1}(q) with the stipulated empty-set convention.

The set B={u in [0,1]:f(u)>=q} is closed by upper semicontinuity and is an initial interval by monotonicity. If r>0, B is nonempty, contains its supremum r, and contains every u<=r. Thus f(u)>=q for u<=r. Moreover,

1>=integral_0^1 f(u)du>=q r,

so 0<r<=1/q<1.

For r>0, let epsilon_k=sqrt(log(2/r)/(2 n_k)). Because both Fhat_k(x) and any candidate CDF F(x) lie in [0,1], the displayed clipped band contains F uniformly exactly when

T_k(F)<=epsilon_k.

The strict e-value acceptance region is contained in this closed band: E_k(F)<q implies p_k(F)>r and hence T_k(F)<epsilon_k. The closed band need not equal that strict acceptance region at the boundary.

What is required for validity is the following implication. If the true CDF is miscovered, then T_k(F_k)>epsilon_k, so

p_k(F_k)=2 exp(-2 n_k T_k(F_k)^2)<r,

and therefore E_k(F_k)>=q. Consequently,

1{O_k}<=1{E_k(F_k)>=q}<=E_k(F_k)/q=(delta a/m)E_k(F_k).

If r=0, epsilon_k=+infinity and the band is identically [0,1]. Its miscoverage indicator is zero, so the same indicator bound holds. The proof does not equate band miscoverage with threshold rejection.

### 5. Post-selection aggregation and expectation

On every nonempty selection, the preceding pointwise bounds imply

FCP=(1/a)sum_{k in A}1{O_k}
    <=(delta/m)sum_{k in A}E_k(F_k)
    <=(delta/m)sum_{k=1}^m E_k(F_k).

If A is empty, FCP=0 and the final inequality also holds. Thus this is a global pointwise bound, not an argument conditioning the data distribution on nonempty selection.

Taking expectations and using the separately established e-value bounds gives

FCR=E[FCP]<=(delta/m)sum_{k=1}^m E[E_k(F_k)]<=delta.

All steps remain valid under arbitrary dependence between configurations and arbitrary measurable full-data selection.

## Obligation Closure

The definition and measurability obligations are derived in Section 1. The only external inequality used is the standard independent DKW statement given in Section 2, whose iid and positive-sample-size hypotheses are verified there. Its nonstrict-tail consequence and the p-value construction are derived explicitly. Calibration is proved in Section 3. Generalized-inverse endpoints, conservative closed-band inversion, and the miscoverage inequality are proved in Section 4. Random-set aggregation, unconditional expectation, and empty selection are handled in Section 5. No specialized external result or unresolved paper-specific dependency is used.
