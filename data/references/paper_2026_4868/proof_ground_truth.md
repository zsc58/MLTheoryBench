# Reference Proof

## Proof Structure

The positive clause uses only evaluations of indexed class members. A finite-prefix search excludes previously generated elements and protects finitely many distinguishing witnesses. A uniform cardinality bound establishes finite-round termination; witness protection establishes eventual criticality of the target's first index; criticality then gives validity and novelty.

For the separation, a directly verified integer generator is combined with the observed marker index. A deterministic replay diagonalization then forces infinitely many outputs outside one fixed target support. All specialized dependencies are derived below rather than invoked without proof.

## Complete Proof

### Indexed class access and the positive construction

An empty class has no targets, so its guarantee is vacuous. On nonempty input histories the rule that returns the first input supplies a generator for this case; if the domain is empty there are no such histories. Hence consider a nonempty countable UUS class. Its domain is necessarily infinite. Use the supplied domain enumeration `y_1,y_2,...`, write `[m]={y_1,...,y_m}`, and order domain elements by their enumeration indices. A finite nonempty class may be listed with repetitions.

Write `H_i=supp(h_i)`. All tests of membership in `H_i` use the allowed oracle `M(i,x)`. There is no hidden-target membership oracle.

For the generator's history, put `O_0=emptyset`, `O_t={o_1,...,o_t}`, and

`S_t={x_s:1<=s<=t and x_s notin O_{s-1}}`.

For any legal replay sequence for a target `h`, every element of `S_t` belongs to `supp(h)`: a presented element that was not previously output cannot be an off-target replay. Also,

`{x_1,...,x_t} subseteq S_t union O_{t-1}`.

Indeed, each input either entered the sure set when presented or was already a previous output. The sure sets are increasing, and `x_1 in S_t` for every `t>=1`.

At round `t`, form the finite active set

`V_t={i<=t:S_t subseteq H_i}`.

For `n in V_t`, call `n` critical at prefix `m` when, for every `i in V_t` with `i<n`,

`H_n intersect [m] subseteq (H_i intersect [m]) union O_{t-1}`.

For every pair `j<i` in `V_t`, form

`Delta_ij(t,m)=(H_i intersect [m]) minus ((H_j intersect [m]) union O_{t-1})`.

If this difference is nonempty, protect its least element in the domain order. Let `W(t,m)` be the set of these protected elements.

Initialize a persistent prefix length `m=0`. After receiving the round's input and updating the sure set, proceed as follows. If `V_t` is empty, output `x_1`, which is an available sure example. Otherwise, replace `m` by the maximum of its current value and the domain index of `x_t`. Repeatedly increase `m` by one, compute the protected set and the largest critical index `n(t,m)` in `V_t`, and check whether

`(H_n(t,m) intersect [m]) minus (S_t union O_{t-1} union W(t,m))`

is nonempty. When it is, output its least element and end the round. Update `O_t` with that output.

Each individual iteration uses only finitely many class-membership queries: consistency is checked on the finite set `S_t`, and criticality, witnesses, and candidate outputs are checked on the finite prefix `[m]`. The search never queries membership in the hidden target or full-support inclusion.

### Finite-round termination

The empty-active-set branch immediately returns `x_1`. If `V_t` is nonempty, its least index is critical at every prefix, so the largest critical index is defined.

Fix this round. Once a given active index fails criticality at a prefix, a witnessing element continues to witness failure at every larger prefix. Consequently `n(t,m)` is nonincreasing as the prefix grows. Since its values lie in the finite nonempty set `V_t`, it eventually stabilizes at an index `n_bar`.

The excluded set can depend on `m`, but its cardinality has the uniform bound

`|S_t union O_{t-1} union W(t,m)| <= t+(t-1)+t(t-1)/2`.

There is at most one protected element for each ordered pair `j<i` of active indices. UUS implies that `|H_n_bar intersect [m]|` tends to infinity. Therefore a sufficiently large prefix contains more elements of `H_n_bar` than the displayed uniform bound, and at least one is admissible. The search terminates in finitely many iterations, each containing finitely many operations and oracle queries. This argument also establishes termination on arbitrary finite histories, not just histories admissible for a particular target.

### Eventual criticality of the target index

Fix a target and any enumeration with replay for the constructed generator. Let `z` be the first index representing that target. For every `t>=z`, the index `z` belongs to `V_t`, because `S_t subseteq H_z`.

Consider an earlier index `j<z` consistent with `S_z`. If

`H_z minus (H_j union O_{z-1})`

is empty, the resulting inclusion remains true when `O_{z-1}` is enlarged to any later output set. Otherwise let `w_j` be the least element of this difference. Let `B` be the finite collection of earlier consistent indices with such a witness.

For `j in B`, the witness has not appeared as an input by round `z`. If it had, its exclusion from `O_{z-1}` would imply that it entered `S_z`, contradicting consistency of `j` with `S_z`.

We now show that `w_j` is never output while `j` remains active after round `z`. Initially it is outside `O_{z-1}`. Inductively suppose it is outside `O_{t-1}` and `j` is active at round `t>=z`. Every earlier element of `H_z minus H_j` was already in `O_{z-1}`, by minimality of `w_j`, and remains in `O_{t-1}`. Thus, whenever the searched prefix contains `w_j`, the witness for the active pair `(z,j)` is exactly `w_j`, so the output rule excludes it. If the prefix does not contain `w_j`, no candidate output equals it. This proves the induction.

The enumeration eventually presents `w_j`, say at round `r_j`. If `j` was already inconsistent, it remains so because the sure sets increase. Otherwise the induction through round `r_j-1` shows that this presentation is not a replay of an earlier output. It enters `S_r_j` and makes `j` inconsistent at that round. Thus every index in `B` is permanently eliminated at finite time.

Take `T=max({z} union {r_j:j in B})`, with `T=z` when `B` is empty. Every earlier index still consistent at time `t>=T` was consistent at time `z` and is not in `B`. Hence

`H_z subseteq H_j union O_{z-1} subseteq H_j union O_{t-1}`

for every surviving `j<z`. Intersecting with any prefix proves that `z` is critical at every prefix for every `t>=T`.

### Eventual validity and novelty

For `t>=T`, the selected largest critical index satisfies `n(t,m)>=z`. If it equals `z`, its selected output belongs to the target. If it is larger, its criticality relative to the active index `z` gives

`H_n(t,m) intersect [m] subseteq (H_z intersect [m]) union O_{t-1}`.

Since the output is outside `O_{t-1}`, it belongs to `H_z`. It is also outside `S_t union O_{t-1}`, which contains every input seen so far. Thus it is valid and novel at every such round. The same finite-query procedure works for every supplied indexed countable UUS class and every target enumeration with replay, proving the first clause.

### The separation class is UUS and uncountable

Use exactly the integer families and disjoint markers in the public task. Every support in `H_1^b` contains an infinite upper integer tail; every support in `H_2^b` contains all integers below `b`; the all-marker support is also infinite. Padding preserves infinitude.

Already the subfamily with `b=0` and supports `Z_<0 union A`, where `A` ranges over all subsets of the positive integers, is uncountable. For completeness, if these supports could be listed as `L_1,L_2,...`, choose `A={n>=1:n notin L_n}`. Then `Z_<0 union A` is a member different from `L_n` at the positive integer `n` for every `n`, a contradiction.

### Direct proof of ordinary no-query generation

First verify the specialized integer generator rather than assuming its guarantee. Fix `b in N_0`. For a nonempty finite integer history `v_1,...,v_r`, define its virtual outputs `p_s^b` recursively for `1<=s<=r` by

`p_s^b=max({s} union {p_1^b,...,p_(s-1)^b} union {v_1,...,v_s})+1`

if the integer `b` has appeared among `v_1,...,v_s`, and otherwise by

`p_s^b=min({b} union {p_1^b,...,p_(s-1)^b} union {v_1,...,v_s})-1`.

Both extrema are of nonempty finite sets of integers. These are the base generator's own recursively determined outputs, not outputs of a different generator that may include markers.

On an ordinary enumeration of a member of `H_1^b`, the integer `b` eventually appears. Subsequently the first branch always applies. Its outputs exceed every observed integer and exceed the integer-input count `s`; eventually they exceed the target's cutoff `j` and hence belong to the support. On an ordinary enumeration of a member of `H_2^b`, the integer `b` never appears, so every output is below `b` and below every observed integer. It is therefore valid and novel. This proves the base guarantee directly from the formula.

Now define a single generator for the padded union. On a full history, let

`m(t)=max({0} union {k:mu^k has appeared among x_1,...,x_t})`,

and let `Z_t` be the ordered integer subsequence, of length `r_t`. If `r_t=0`, output `mu^(m(t)+1)`. Otherwise evaluate the just-defined base function for `b=m(t)` on the whole finite sequence `Z_t`, and output `p_(r_t)^(m(t))`. This means that the virtual base outputs are computed for that fixed value of `b` on the integer subsequence; they are not the actual mixed-history outputs.

For the all-marker target, every output is a valid marker not yet seen as input. For a padded target with index `b`, ordinary inputs never contain markers of index greater than `b`. If `b>=1`, eventual presentation of `mu^b` makes `m(t)=b` permanently. If `b=0`, no marker occurs and `m(t)=0` from the start; no marker `mu^0` is needed. The integer part of the target is infinite, so an integer eventually appears and `r_t` tends to infinity. Thereafter the base guarantee applies with the correct `b`. Integer outputs are distinct from all observed integers and automatically distinct from all marker inputs. They are eventually valid, proving ordinary limit generation without queries. Repeated outputs during intervals with no new integer input are harmless: the required novelty is relative to inputs, not to previous outputs.

### Replay impossibility without queries

Suppose a deterministic no-query generator `G` succeeds with replay for every target in this class.

First feed `mu^1,mu^2,...` until a round `tau` at which `G` outputs a marker not yet presented. Such a round exists by its guarantee on the all-marker target. Write that output as `mu^z`; necessarily `z>tau`. Continue presenting the remaining markers through `mu^z`, and set `J_0=z`.

For each phase `n>=1`, present the integer `z-n`, not a marker. Then present the increasing integer tail `J_(n-1)+1,J_(n-1)+2,...`. After each round of the phase, stop the phase as soon as the output is an integer greater than `J_(n-1)` and has not occurred among any inputs so far. Denote this output by `J_n` and its round by `t_n`. This stopping test may also succeed immediately after the initial integer `z-n`.

Inductively, every previously presented integer is less than `J_(n-1)`. If the phase stops after some tail inputs, a fresh output above `J_(n-1)` must exceed the largest tail integer already presented, because the intervening integers have been presented consecutively. If it stops before any tail input, the same required invariant follows directly. Thus all integers presented through phase `n` are less than `J_n`. Later descending inputs are below `z`, while later tails begin above the current, strictly increasing `J` value. Consequently no selected `J_n` is ever presented, either earlier or later.

It remains to prove that every phase terminates. Assume earlier phases have terminated and suppose phase `n` never stops. Let `F_n` be the finite set of integers presented before the phase. Define an alternative support

`L_hat=F_n union {z-n} union {x in Z:x>J_(n-1)} union M_(z-1)`.

The integer `z-1` is included: it is the current descending input if `n=1`, and was presented in phase 1 otherwise. Also `J_(n-1)>=z>z-1`. Thus `L_hat` belongs to the padded first family with index `z-1`, using cutoff `J_(n-1)`.

The nonterminating stream enumerates every element of `L_hat`. Its only input outside `L_hat` is `mu^z`, which was output at round `tau` before being presented at round `z`. That input is therefore a legal replay. The stream is an enumeration with replay for the alternative target. Since the generator has no target-dependent oracle, its outputs on these histories are exactly the outputs used in the construction.

All members of `F_n union {z-n} union M_(z-1)` have already been presented. The assumed eventual validity and novelty for `L_hat` therefore force a fresh output in the tail above `J_(n-1)` at a finite round. This is precisely the phase's stopping condition, a contradiction. Induction proves that all phases terminate.

Let `S` be the set of all integers presented over the completed infinite construction. Every integer below `z` appears as `z-n`, the integer `z` never appears, and all remaining integer inputs are greater than `z`. Therefore

`S=Z_<z union A`, where `A=S intersect Z_>z`.

The support `L_star=S union M_z` belongs to the padded second family with index `z`. The complete stream enumerates exactly this support, so in particular it is an enumeration with replay for that fixed target. Every selected `J_n` is an integer absent from `S`, and hence absent from `L_star`. At the infinitely many distinct rounds `t_n`, the output is invalid, contradicting the assumed guarantee.

There is no change of the target during an actual interaction. For each fixed deterministic `G`, the argument constructs one target-stream pair. The full construction can be considered before that pair is used in the game; fixing `L_star` at the outset yields exactly the same outputs on the constructed histories. The alternative targets are used only to establish phase termination under the universal success assumption.

This proves the replay non-generation claim and completes the integrated theorem.

## Proof-Obligation Audit

All theorem-critical obligations are closed above: the precise oracle interface and uniform algorithm, nonempty fallback, finite candidate selection, a prefix-uniform exclusion bound, finite-round termination, preservation and eventual presentation of witnesses, elimination of earlier hypotheses, eventual validity and input novelty, UUS and uncountability of the explicit class, direct correctness of the specialized base generator, stabilization including b=0, deterministic target-independent simulation, finite termination of every adversarial phase, and identification of one fixed target with infinitely many invalid outputs. No specialized result is accepted solely on the basis of a citation.
