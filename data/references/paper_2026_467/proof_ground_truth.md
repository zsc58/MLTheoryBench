# Reference Proof

## Proof Structure

There are six obligations: pass from the density inequality to event privacy; prove the sharp common-density bound with the correct almost-everywhere quantifiers; establish the fixed-interval optimum; prove global exactness of the finite search; normalize the projected kernel for every real input; and establish privacy for the independently randomized dataset. Each obligation is derived below. The prior, parameters, and selected maximizing interval are fixed throughout the comparison of neighboring datasets, as in the known-prior setup. No private-data-dependent prior estimation or interval reselection is part of this mechanism.

Write `B=2h`, `rho=exp(-epsilon)`, and `G=B+rho(b-a)`. All interval endpoints are finite real numbers, so `G>=B>0`.

## Complete Proof

### 1. Density inequalities imply event privacy

For any fixed pair of inputs, if

`r(t | y) <= exp(epsilon) r(t | y')`

for almost every output `t`, integration over any measurable output event gives the corresponding epsilon-privacy event inequality. Only this sufficient implication is needed here. In particular, we do not infer a simultaneous exceptional set for an uncountable input family from separate pairwise almost-everywhere statements.

### 2. Sharp fixed-interval mass bound

Fix `I=[a,b]`, a feasible kernel, and one input `y in I`. Its common neighborhood value is `v>0`.

For each integer `m`, put

`c_m=y+2mh`, `E_m=[c_m-h,c_m+h] intersect N_I`, and `z_m=pi_I(c_m)`.

Only finitely many of the sets `E_m` are nonempty. They cover `N_I` and have disjoint interiors; their shared endpoints have measure zero. Also, `E_0=N_y`.

For each fixed `m`, we have `E_m subset N_{z_m}`. If `c_m in I`, this follows from `z_m=c_m`. If `c_m<a`, every `t in E_m` satisfies `a-h<=t<=c_m+h<=a+h`, so `t in N_a`. If `c_m>b`, every `t in E_m` satisfies `b-h<=c_m-h<=t<=b+h`, so `t in N_b`.

The center `z_m` is fixed while `t` varies over `E_m`. Therefore the neighborhood assumption gives `r(t | z_m)=v` for almost every `t in E_m`. Combining the finitely many exceptional sets with the exceptional set for the ratio constraint gives, almost everywhere on each `E_m`,

`r(t | y) >= rho r(t | z_m)=rho v`.

On `E_0=N_y`, we have the stronger equality `r(t | y)=v` almost everywhere. Since `N_y` has length `B`, and `N_I minus N_y` has length `b-a`, normalization and support give

`1=integral_{N_I}r(t | y)dt >= Bv+rho(b-a)v=Gv`.

Thus `v<=1/G`.

This argument also covers `a=b`. It does not substitute the output-dependent center `pi_I(t)` into a per-input almost-everywhere equality; that substitution would require an additional justification not supplied by the original private proof.

### 3. Fixed-interval optimum and attainment

The neighborhood equality gives

`J_I(r)=Bv integral_a^b p(y)dy`.

Since `p>=0` and `v<=1/G`,

`J_I(r) <= (B/G) integral_a^b p(y)dy=F(a,b)`.

For `y in I`, define `r*(t | y)` to equal `1/G` on `N_y`, `rho/G` on `N_I minus N_y`, and zero outside `N_I`. These sets are measurable, and the defining inequalities also make the kernel jointly measurable. Its integral is

`[B+rho(b-a)]/G=1`.

Its neighborhood value is the common positive constant `1/G`. On its common support, any two positive density values differ by a factor of at most `1/rho=exp(epsilon)`; outside that support both densities vanish. Thus it is feasible and attains `F(a,b)`.

If the interval has zero prior mass, all feasible objectives equal zero and this kernel is still an optimizer; no uniqueness claim is needed. If `a=b`, then `G=B`, the remainder of the support has zero length, and the displayed kernel is the uniform density on `N_a`.

### 4. Exactness of the finite interval search

Let

`M(a,b)=integral_a^b p(s)ds`, so `F(a,b)=BM(a,b)/G(a,b)`.

Because `p` is a probability density on `[n_0,n_k]`,

`F(n_0,n_k)=B/[B+rho(n_k-n_0)]>0`.

An interval of zero prior mass cannot attain the global optimum. If `M(a,b)>0`, clip it to

`a'=max(a,n_0)`, `b'=min(b,n_k)`.

Positive mass ensures `a'<b'`. Clipping leaves the mass unchanged and cannot increase the length, so `F(a',b')>=F(a,b)`. The inequality is strict if a nonzero length outside the support is removed. Therefore it suffices to optimize on the compact triangle

`C={(a,b): n_0<=a<=b<=n_k}`.

The interval mass is continuous in its endpoints, and `G>=B>0`, so `F` is continuous on `C` and attains a maximum there.

For `i<j`, consider the rectangle

`[n_i,n_{i+1}] x [n_j,n_{j+1}]`.

Every point of this rectangle is feasible because `n_{i+1}<=n_j`. On the rectangle,

`M(a,b)=H_ij-alpha_i a+alpha_j b`.

Differentiating this cell restriction gives

`partial_a F=B[rho H_ij+rho(alpha_j-alpha_i)b-B alpha_i]/G^2`,

`partial_b F=B[B alpha_j-rho H_ij-rho(alpha_j-alpha_i)a]/G^2`.

These are derivatives in the cell interior, with the corresponding one-sided interpretation on its edges; no global differentiability at prior knots is asserted.

For each fixed `b`, the sign of `partial_a F` is independent of `a`. Moving `a` to a suitable endpoint of its cell therefore does not decrease `F`; if the derivative is zero, either endpoint preserves the value. With that endpoint now fixed, the sign of `partial_b F` is independent of `b`, so moving `b` to a suitable endpoint likewise does not decrease `F`. Consequently every point of an off-diagonal cell is dominated by a corner of that cell. All those corners are in `S`.

For completeness, when `alpha_i != alpha_j`, the possible derivative zeros occur at

`b=b_ij=(B alpha_i-rho H_ij)/[rho(alpha_j-alpha_i)]`,

`a=a_ij=(B alpha_j-rho H_ij)/[rho(alpha_j-alpha_i)]`.

Thus the additional critical-coordinate candidates in the problem are consistent with the derivative calculation. They are not needed for the corner-domination argument, but adding feasible points cannot invalidate exactness. When `alpha_i=alpha_j`, no division by the height difference is made; the same monotonicity argument applies, including constant restrictions.

On a diagonal cell, the correct mass is `alpha_i(b-a)`, so

`F(a,b)=B alpha_i(b-a)/[B+rho(b-a)]`.

As a function of `u=b-a`, its derivative is

`B^2 alpha_i/[B+rho u]^2>=0`.

It is therefore maximized at the vertex `(n_i,n_{i+1})`; if `alpha_i=0`, the entire cell has value zero and any listed vertex suffices. The other two listed vertices are feasible zero-width intervals. No reversed interval is evaluated.

These cells cover `C`. Their maximizing values are represented in `S`, and every member of `S` lies in `C`. Hence

`max_{a<=b}F(a,b)=max_{(a,b) in C}F(a,b)=max_{(a,b) in S}F(a,b)`.

This also verifies existence of the selected interval, including a one-bin prior, zero-height bins, ties, and equal-height cells.

### 5. The full projected response kernel

Fix any `I=[a,b]`. For every real input `y`, the projected center `pi_I(y)` belongs to `I`. Its neighborhood lies in `N_I` and has length `B`; its complement in `N_I` has length `b-a`. Therefore

`integral r_I(t | y)dt=B/G+rho(b-a)/G=1`.

The projection is continuous, so the sets specifying the density are measurable in the input and output. The displayed function is consequently a response probability kernel for all real labels, not only labels in the prior support or in `I`.

For `a=b`, all inputs project to the same point and the kernel is uniform on the same interval. Thus this degenerate case is also well-defined.

### 6. Privacy of the selected dataset mechanism

Apply the preceding facts to the fixed selected interval `I*`. Outside `N_{I*}`, every conditional density is zero. On that support, for every input `y`,

`rho/G* <= r_{I*}(t | y) <= 1/G*`.

Therefore, for every pair of labels `y,y'`,

`r_{I*}(t | y) <= exp(epsilon)r_{I*}(t | y')`.

The inequalities suffice; the extrema need not be attained at every output. Integrating establishes epsilon privacy for one response.

Now compare two finite datasets with the same features and all the same responses except at index `j`. The prior, parameters, and chosen interval are the same for both datasets. Independent response randomization gives label-output densities

`q_D(t_1,...,t_m)=product_{ell=1}^m r_{I*}(t_ell | y_ell)`

and the analogous density for `D'`. All factors except the `j`th agree. Multiplying the single-response inequality by the common nonnegative factors yields

`q_D(t_1,...,t_m) <= exp(epsilon)q_{D'}(t_1,...,t_m)`.

This argument uses multiplication rather than cancellation, so zero factors cause no difficulty. Integrating over any measurable label-output event proves the required inequality. The features are unchanged and identical in the two neighboring datasets, so taking the corresponding event section proves the same inequality for the full dataset output. Thus the selected mechanism is epsilon label differentially private.

## Proof-Closure Check

All six obligations are closed by the displayed arguments. The proof uses only elementary integration, finite unions of null sets, differentiation of explicit cell formulas, compactness for a continuous function, and the product law for independent samples. There is no unresolved specialized or paper-specific external dependency.
