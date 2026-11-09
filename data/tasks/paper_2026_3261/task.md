# Problem

## Setup

Let n and M be positive integers and K>0. Observe n independent realizations (x_i,y_i), i=1,...,n, of a common random pair (X,Y), with x_i in a feature space X and y_i in R. For each m=1,...,M, let ell_m:R x R -> R_+ be convex and K-smooth in its second argument, and define

Rhat(g)=sum_{i=1}^n sum_{m=1}^M ell_m(y_i,g_m(x_i)).

Let {h_w:X->R:w in W} be sign-symmetric and satisfy |h_w(x_i)|^2<=1/n for all i,w. Let H=span{h_w:w in W}. For each m assume the set of prediction vectors

{(f(x_1),...,f(x_n)): f in H, sum_i ell_m(y_i,f(x_i)) <= sum_i ell_m(y_i,0)}

is compact in R^n. Let V be the span of the vector functions x -> h_w(x) beta with w in W and beta in the unit sphere S^{M-1}. Assume all scalar greedy argmins, multidimensional line-search argmins, and an empirical-risk minimizer over V exist.

Initialize g_0=0. At iteration t>=1 choose m_t in {1,...,M} so every coordinate occurs infinitely often. Choose w_t minimizing

sum_i partial_2 ell_{m_t}(y_i,g_{t-1,m_t}(x_i)) h_w(x_i)

over w. Choose gamma_t in R^M minimizing Rhat(g_{t-1}+h_{w_t} gamma) over gamma, and update

g_t=g_{t-1}+alpha h_{w_t} gamma_t,

with fixed alpha in (0,1].

## Task

Prove that Rhat(g_t) converges, as t tends to infinity, to min_{g in V} Rhat(g). Equivalently, it converges to Rhat(g_*) for any empirical-risk minimizer g_* in V.
