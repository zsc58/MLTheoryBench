# Reference Proof

## Theorem-Critical Obligations

The proof must establish: (1) one observation probability valid for every dataset and record position; (2) a common output component and correctly normalized observed components; (3) both the observed-to-observed and observed-to-all-missing DP comparisons, with valid coupling marginals; (4) the correct amplified mixture inequality; and (5) uniform, two-sided DP, including all boundary and degenerate cases. Each obligation is derived below. No specialized amplification theorem is assumed.

## step_001: Common Observation Probability and Ambient Contract

The same feature rule `F` is applied independently to each record. Set `q(x)=K(x,empty)`. Any two records agree on the coordinates retained by the empty mask, so pointwise MAR gives `q(x)=q(x')` for all `x,x' ∈ Z`. Since `Z` is nonempty, this defines one constant `q ∈ [0,1]`. Consequently `p=1-q` is independent of the record value, dataset, and record position. This proves the well-definedness and uniformity of the public parameter.

The inputs in the privacy comparison are fixed datasets; no distribution or independence assumption on their record values is needed. Independence concerns the mask draws conditional on those inputs. The base DP guarantee applies to all neighboring incomplete datasets, including pairs with different masks at their differing record. The invocation of `A` has its usual output law conditional on its incomplete input.

An identical input pair has identical output laws and satisfies the required inequality because the eventual multiplicative factor is at least one and the additive term is nonnegative. It remains to compare distinct neighboring datasets `X,X'`, with differing position `i`.

If `p=0`, every record mask is empty almost surely. Therefore `B(X)` has the law of `A((NA,...,NA),...,(NA,...,NA))` for every complete dataset. The algorithm is `(0,0)`-DP, exactly the asserted parameters. Henceforth assume `p>0`.

## step_002: Explicit Output Components

Let `r=(S_j)_{j≠i}` denote the other-record masks. Their common probability mass function is

`lambda(r) = product_{j≠i} K(x_j,S_j) = product_{j≠i} K(x'_j,S_j)`.

Its total mass is one. When `n=1`, there is exactly one empty residual mask and the empty product equals one.

For nonempty masks `s,t`, define

`nu(s)=K(x_i,s)/p`, and `nu'(t)=K(x'_i,t)/p`.

Both are probability mass functions, since each numerator sums to `p` over nonempty masks. Independence implies that the joint conditional law of `(r,S_i)` given `S_i≠empty` is `lambda(r)nu(S_i)` under `X`, and `lambda(r)nu'(S_i)` under `X'`.

Let `Y(r,s)` be the incomplete version of `X` using residual mask `r` and mask `s` at position `i`; define `Y'(r,t)` analogously from `X'`. Let `Y_0(r)` have the common masked records at positions `j≠i` and the entirely missing record at position `i`. All these inputs belong to `Z_miss^n`.

For a measurable output event `E`, put

`C(E) = sum_r lambda(r) P[A(Y_0(r)) ∈ E]`,

`R(E) = sum_{r,s≠empty} lambda(r)nu(s) P[A(Y(r,s)) ∈ E]`,

`R'(E) = sum_{r,t≠empty} lambda(r)nu'(t) P[A(Y'(r,t)) ∈ E]`.

These are output probability laws, not masked-input laws. The definition of `C` is a direct experiment, so it remains meaningful when `p=1`; it never requires conditioning on a null event. When `p<1`, it is also the conditional output law given that position `i` is entirely missing.

The composition rule and the finite mask partition give

`P := Law(B(X)) = (1-p)C + pR`,

`Q := Law(B(X')) = (1-p)C + pR'`.

The common component follows from the identical other records, their common residual mask law, and the fixed all-missing record at position `i`.

## step_003: Both Necessary DP Comparisons

Set `alpha=exp(epsilon)`. First couple the observed components by giving `(r,s,r',t)` mass

`pi_1((r,s),(r',t)) = 1_{r=r'} lambda(r)nu(s)nu'(t)`.

Summing over `(r',t)` gives the marginal `lambda(r)nu(s)`, and summing over `(r,s)` gives `lambda(r')nu'(t)`. Thus both marginals are exactly the required conditional mask laws. On the support of this coupling, `Y(r,s)` and `Y'(r,t)` agree outside position `i` and are neighboring incomplete datasets, even when `s` and `t` differ. Apply base DP to each such ordered pair and sum against `pi_1`. For every measurable `E`, this yields

`R(E) - alpha R'(E) ≤ delta`.

For the comparison with the common component, draw `(r,s)` with mass `lambda(r)nu(s)` and pair `Y(r,s)` with `Y_0(r)`. The first marginal produces `R`; the second produces `C`, because summing `nu(s)` over nonempty `s` gives one. The paired incomplete datasets again differ only at position `i`. Summing their base-DP inequalities therefore gives

`R(E) - alpha C(E) ≤ delta`.

Applying the same arguments after interchanging `X` and `X'` gives

`R'(E) - alpha R(E) ≤ delta`, and `R'(E) - alpha C(E) ≤ delta`.

No maximality or optimality property of either coupling is needed. The important properties are its marginals and its support on neighboring incomplete inputs.

## step_004: Correct Amplified Mixture Calculation

For probability laws `U,V` on the output space and `a≥1`, define

`D_a(U||V) = sup_E (U(E)-a V(E))`,

where the supremum is over measurable output events. Thus the event inequalities in step_003 imply both `D_alpha(R||R')≤delta` and `D_alpha(R||C)≤delta`, with the analogous reversed comparisons.

Set

`alpha' = 1+p(alpha-1)`, and `beta = alpha'/alpha`.

Because `alpha>1` and `0<p≤1`, one has `0<beta≤1` and

`alpha(1-beta) = (1-p)(alpha-1)`.

For every event `E`, direct expansion of the two mixtures gives the exact identity

`P(E)-alpha'Q(E)`

`= p [R(E)-alpha'R'(E)-(1-p)(alpha-1)C(E)]`

`= p [(1-beta)(R(E)-alpha C(E)) + beta(R(E)-alpha R'(E))]`.

Taking suprema and using the nonnegative coefficients yields the correct bound

`D_{alpha'}(P||Q) ≤ p [(1-beta) D_alpha(R||C) + beta D_alpha(R||R')]`.

Both divergences on the right are at most `delta`, so

`D_{alpha'}(P||Q) ≤ p delta`.

Equivalently, one can apply the two event inequalities from step_003 directly to the displayed identity and obtain the same bound without introducing divergence notation. Interchanging the datasets gives `D_{alpha'}(Q||P)≤p delta` as well.

It is not valid to replace the two-term right-hand side by `p D_alpha(R||R')` for arbitrary `C,R,R'`. The observed-to-all-missing comparison is an essential proof obligation, not an optional strengthening.

## step_005: Uniform DP, Boundaries, and MCAR

The definition of `D_a` immediately implies that a bound `D_a(U||V)≤b` is equivalent to `U(E)≤aV(E)+b` for every measurable event `E`. Applying this with `a=alpha'` proves the privacy inequality for every ordered neighboring complete-dataset pair. The constant `p`, and hence `alpha'`, is independent of that pair. Therefore the same inequality holds uniformly over all pairs, establishing DP for the entire algorithm `B` with

`epsilon'=log(alpha')=log(1+p(exp(epsilon)-1))`, and `delta'=p delta`.

The case `p=0` was proved before any conditional observed law was introduced. For `p=1`, all definitions above remain valid, `beta=1`, and the mixture argument reduces to the observed-to-observed comparison, giving the original parameters `(epsilon,delta)`. No step divides by `delta` or `1-p`, so `delta=0` and `delta=1` are included. The empty residual product handles `n=1`. If the complete data domain has only one record value, all complete datasets are identical and the direct identical-input argument applies; the parameter `p` remains defined through `H_i`.

Increasing the additive parameter from `p delta` to any value in `[p delta,1]` preserves the inequalities. Every MCAR rule satisfies the stated MAR condition, so the MCAR specialization follows.

## Private Source Alignment

The two-component privacy comparisons and mixture calculation recover the proof route at L000654-L000808. The calculation is derived explicitly, so no unproved specialized mixture result is imported. The equivalence between event inequalities and divergence bounds is also derived from the supremum definition. The existing source correction replacing the final `q_*delta` at L000814 by `p_*delta` is retained. All five theorem-critical obligations are closed.
