# Reference Proof

## Proof Structure

Establish a strict bound of `3/N` for every single point move, including moves into and out of a one-cluster state. For moves whose two states both have at least two nonempty clusters, control the squared-size sum and each leave-one-out baseline, then use an exact bystander/endpoint decomposition. Telescope over the integer number of moves.

## Complete Proof

At every stage, the indexed sizes are nonnegative integers summing to `N`. In a state with at least two nonempty clusters, every indexed size satisfies `n_i<N`, so all leave-one-out baselines are defined. Write
\[
Q=\sum_j n_j^2,\qquad
S_i=\frac{Q-n_i^2}{N-n_i},\qquad
g_i=1-\frac{|n_i-S_i|}{N},\qquad
U=\sum_i\frac{n_i}{N}g_i.
\]
For each index, the complementary sizes are nonnegative and sum to `N-n_i`, so
\[
0\le Q-n_i^2=\sum_{j\ne i}n_j^2\le(N-n_i)^2.
\]
Thus `0<=S_i<=N-n_i<=N`. Since also `0<=n_i<=N`, we have `|n_i-S_i|<=N` and hence `0<=g_i<=1`. Empty indexed clusters have zero weight. For a state with one nonempty cluster, use the stipulated convention `U=0` without evaluating its undefined occupied-cluster baseline.

A move that leaves a point in its existing cluster changes nothing and satisfies `|U'-U|=0<3/N`. Consider now a move from an occupied cluster `A` to a distinct indexed cluster `B`. Put `a=n_A>=1` and `b=n_B>=0`. After the move, `a'=a-1`, `b'=b+1`, and the other sizes are unchanged.

### One-Cluster Boundary Transitions

If the old state has one nonempty cluster, then `a=N` and `b=0`, and the new state has occupied sizes `(N-1,1)`. If the new state has one nonempty cluster, then `a=1` and `b=N-1`, and the old state has occupied sizes `(1,N-1)`.

For occupied sizes `(N-1,1)`, the two leave-one-out baselines are `1` and `N-1`, respectively. Each agreement factor is
\[
1-\frac{N-2}{N}=\frac2N,
\]
so the score is `2/N`, including when `N=2`. The one-cluster score is zero. Therefore either direction of this boundary transition satisfies
\[
|U'-U|=\frac2N<\frac3N.
\]
This also covers a sequence that collapses to one cluster and later leaves that state.

### Moves Between Two Nontrivial States

It remains to consider a move for which both states have at least two nonempty clusters. Then `a<=N-1` and `b<=N-2`, and all old and new agreement factors are defined, including those of empty indexed clusters.

The change in the squared-size sum is
\[
\Delta Q=(a-1)^2+(b+1)^2-a^2-b^2=2(b-a+1).
\]

For a bystander `i` not in `{A,B}`, its size is unchanged, giving
\[
\Delta S_i=\frac{\Delta Q}{N-n_i}.
\]
Because `a>=1`, `b>=0`, and `a+b<=N-n_i`,
\[
|b-a+1|\le a+b-1<a+b\le N-n_i.
\]
Consequently `|Delta S_i|<2`, and the reverse triangle inequality yields
\[
|g_i'-g_i|\le\frac{|\Delta S_i|}{N}<\frac2N.
\]

For cluster `A`, put `d=N-a>=1` and `p=Q-a^2`. The complementary sizes imply
\[
b^2\le p\le d^2.
\]
After the move, its complementary squared-size sum is `p+2b+1` and its complementary mass is `d+1`. Hence
\[
\Delta S_A=\frac{p+2b+1}{d+1}-\frac pd
=\frac{d(2b+1)-p}{d(d+1)}.
\]
The numerator satisfies
\[
d(2b+1)-p\le d(2b+1)-b^2
=d(d+1)-(b-d)^2\le d(d+1),
\]
and
\[
d(2b+1)-p\ge d-d^2=-d(d-1)>-d(d+1).
\]
Thus `|Delta S_A|<=1`.

For cluster `B`, put `e=N-b>=2` and `q=Q-b^2`. Here
\[
a^2\le q\le e^2,\qquad 1\le a\le e.
\]
The case `a=e` is allowed. After the move, its complementary squared-size sum is `q-(2a-1)` and its complementary mass is `e-1`, so
\[
\Delta S_B=\frac{q-(2a-1)}{e-1}-\frac qe
=\frac{q-e(2a-1)}{e(e-1)}.
\]
For the upper bound, `a>=1` gives
\[
q-e(2a-1)\le e^2-e(2a-1)
=e(e-2a+1)\le e(e-1).
\]
For the lower bound,
\[
q-e(2a-1)\ge a^2-e(2a-1)
=(a-e)^2-e(e-1)\ge-e(e-1).
\]
Therefore `|Delta S_B|<=1`.

Each endpoint size changes by one. Applying the reverse triangle inequality again gives
\[
|g_A'-g_A|\le\frac{|a'-a|+|\Delta S_A|}{N}\le\frac2N,
\qquad
|g_B'-g_B|\le\frac{|b'-b|+|\Delta S_B|}{N}\le\frac2N.
\]

The exact score decomposition is
\[
U'-U=\frac1N\left[
\sum_{i\notin\{A,B\}}n_i(g_i'-g_i)
+(a-1)(g_A'-g_A)
+b(g_B'-g_B)
+(g_B'-g_A)
\right].
\]
All agreement-change coefficients are nonnegative, and their sum is
\[
(N-a-b)+(a-1)+b=N-1.
\]
Their total absolute contribution is therefore at most `2(N-1)/N^2`. Since `g_B',g_A` lie in `[0,1]`, the remaining endpoint-weight term has magnitude at most `1/N`. Thus
\[
|U'-U|\le\frac{2(N-1)}{N^2}+\frac1N
=\frac{3N-2}{N^2}<\frac3N.
\]
Together with the boundary transitions and no-ops, this proves the strict single-move bound at every possible stage.

### Telescoping

Let `U_t` be the score after `t` of the `m=epsilon N` moves. If `m=0`, the final state equals the initial state and `Delta U=0`. If `m>0`, the finite sum of strict single-move bounds gives
\[
|\Delta U|=|U_m-U_0|
\le\sum_{t=1}^m|U_t-U_{t-1}|
<\sum_{t=1}^m\frac3N
=\frac{3m}{N}=3\varepsilon.
\]
In particular, `|Delta U|<=3epsilon` for every admissible `epsilon`. The proof uses only the defined score, elementary inequalities, and the stated boundary convention; no external proof obligation remains.
