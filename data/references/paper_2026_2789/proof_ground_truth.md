# Reference Proof

## Proof Structure

First compare the binary and fractional feasible sets. Next analyze an optimal LP extreme point, showing that at most two coordinates are fractional. A case analysis rounds those coordinates to a feasible binary allocation with objective loss at most `2V_max`. Dividing by `n` yields the integrality conclusion, and a squeeze argument then handles the feasible threshold allocation.

## Complete Proof

The binary feasible set is contained in the LP feasible set, so
`P_n^01 <= P_n^LP`.

Choose an optimal extreme point `x*` of the LP. The polytope has box constraints and two global inequalities. At an extreme point, `n` linearly independent constraints are active; at most two can be non-box constraints. Therefore at least `n-2` coordinates are fixed at zero or one, and at most two coordinates are strictly fractional.

Let `m` be the number of coordinates of `x*` equal to one, and let the fractional coordinates (if any) be `j,k` with fractions `alpha,beta`.

If there are no fractional coordinates, use `y=x*`. If there is one fractional coordinate, the coverage sum cannot equal the integer `K_n`; hence the integer part is already at least `K_n`, and rounding the fractional coordinate down preserves feasibility and decreases the budget. If there are two fractional coordinates and `m>=K_n`, round both down; this also preserves feasibility and decreases the budget.

It remains to consider two fractional coordinates with `m=K_n-1`. Since `x*` satisfies coverage, `alpha+beta>=1`. Let `R=W_n-sum_{i:x_i*=1}w_i` be the remaining budget. Feasibility of `x*` gives `alpha w_j+beta w_k<=R`. At least one of `w_j,w_k` is at most `R`; otherwise `alpha w_j+beta w_k>R(alpha+beta)>=R`, a contradiction. Round that item up and the other fractional item down. The resulting vector has cardinality `K_n` and remains within budget.

In every case only at most two coordinates change. Since `|v_i|<=V_max`, the objective loss is at most `2V_max`. Thus
`0<=P_n^LP-P_n^01<=2V_max`.

Dividing by `n` gives
`0<=P_n^LP/n-P_n^01/n<=2V_max/n`, which converges to zero.

Let `G_n=sum_i v_i g_{n,i}`. By the assumed near-optimality, `G_n>=P_n^LP-r_n` with `r_n=o(n)`. Since `g_n` is feasible for the binary problem, `G_n<=P_n^01`. Hence
`0<=P_n^01-G_n<=P_n^LP-G_n<=2V_max+r_n`.
After division by `n`, the right-hand side tends to zero, proving asymptotic optimality of the threshold allocation.
