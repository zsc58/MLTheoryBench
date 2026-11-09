# Problem

## Setup

Fix positive integers `n,d` and a nonempty data domain `Z ⊆ R^d`. Write `[d]={1,...,d}`. A complete dataset is an ordered tuple `X=(x_1,...,x_n) ∈ Z^n`. Let `NA` be a fixed missing symbol distinct from every real number. A record mask is a subset `S ⊆ [d]` specifying the retained features. Write `T_S(x)` for the record whose j-th entry is `x_j` when `j ∈ S` and `NA` otherwise. Let `Z_miss` consist of all records obtainable this way from records in `Z`; incomplete datasets belong to `Z_miss^n`. On either dataset domain, two datasets are **neighbors** if they differ in at most one record, including a possible change of that record's missingness pattern.

Let `F` be a fixed measurable randomized rule taking a record `x ∈ Z` to a mask `S ⊆ [d]`, and write `K(x,S)=P[F(x)=S]`. Given a complete dataset, use this same rule at every position and draw the record masks independently: mask `S_i` has the law of `F(x_i)`. No independence among the feature-retention decisions within a record is required.

The rule is **MCAR** if `K(x,S)=K(x',S)` for every `x,x' ∈ Z` and every `S ⊆ [d]`. It is **MAR** if, for every `S ⊆ [d]` and every `x,x' ∈ Z` agreeing on all coordinates in `S`, one has `K(x,S)=K(x',S)`. Assume that `F` is MAR.

For a dataset `X` and a position `i`, let `H_i` be the event that `S_i` is nonempty, so that record `i` is at least partially observed. Under the stated MAR model, this event has a common probability `p ∈ [0,1]` independent of `X` and `i`; use `p` to denote that probability.

For `a ≥ 0` and `b ∈ [0,1]`, an algorithm `T` on either dataset domain is **(a,b)-differentially private** if, for every ordered neighboring pair `U,V` in its domain and every measurable output event `E`,

`P[T(U) ∈ E] ≤ exp(a) P[T(V) ∈ E] + b`.

Fix `epsilon > 0` and `delta ∈ [0,1]`. Let `A` be an `(epsilon,delta)`-differentially private randomized algorithm on `Z_miss^n`, with outputs in a fixed measurable space.

Define an algorithm `B` on complete datasets as follows: given `X`, draw the independent masks specified above, form `Y=(T_{S_1}(x_1),...,T_{S_n}(x_n))`, and run `A` on `Y` using fresh internal randomness. Conditional on the masked input `Y`, this invocation has exactly the output law of `A(Y)`. Release only its output.

## Task

Prove that `B` is `(epsilon',delta')`-differentially private on `Z^n`, where

`epsilon' = log(1 + p (exp(epsilon)-1))` and `delta' = p delta`.

Consequently, the same `epsilon'` also gives differential privacy with any `delta' ∈ [p delta,1]`. The guarantee must hold for every MAR rule satisfying the setup and, in particular, for every MCAR rule.
