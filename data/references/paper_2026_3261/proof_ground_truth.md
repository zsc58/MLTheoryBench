# Reference Proof

## Proof Structure

Let V be the span of the rank-one vector learners in the task. First prove privately that V equals the Cartesian product of the scalar learner span. Then, for each coordinate, use its infinitely recurring selected subsequence, separability, smoothness descent, compactness, and convexity to prove convergence to the scalar-span minimum. Sum the coordinate limits and use the span identity.

## Complete Proof

Let H=span{h_w:w in W} and Lambda=H^M. The rank-one span V equals Lambda. For one inclusion, every finite sum of functions h_w beta has each coordinate in H. Conversely, if f=(f_1,...,f_M) with f_m in H, write each f_m as a finite linear combination of h_w functions and multiply each term by the corresponding canonical basis vector; these basis vectors are allowed rank-one directions.

Fix m and write F_m(f)=sum_i ell_m(y_i,f(x_i)). Let rho_m(1)<rho_m(2)<... enumerate the iterations with m_t=m, and let f_t=g_{t,m}. Every f_t belongs to H because g_0=0. Separability implies that, at every iteration, the mth component of gamma_t minimizes F_m(f_{t-1}+gamma h_{w_t}) over gamma in R. Since zero is an available trial value, convexity and alpha in (0,1] give F_m(f_t)<=F_m(f_{t-1}). Thus every f_t lies in the compact prediction sublevel set specified for m.

At a selected iteration t=rho_m(s), define

kappa_t=-min_w sum_i partial_2 ell_m(y_i,f_{t-1}(x_i)) h_w(x_i) >= 0.

The inequality follows from sign symmetry, and w_t attains this minimum. For h=h_{w_t}, the pointwise bound gives sum_i h(x_i)^2<=1. K-smoothness therefore gives

F_m(f_{t-1}+eta h)<=F_m(f_{t-1})-eta kappa_t+(K/2)eta^2.

The exact scalar line search is no worse than the trial eta=kappa_t/K. Convexity for the shrinkage update consequently yields

F_m(f_t)<=F_m(f_{t-1})-alpha kappa_t^2/(2K).

All intervening iterations also leave F_m nonincreasing. Telescoping over all iterations and using F_m>=0 shows that sum_s kappa_{rho_m(s)}^2 is finite, so kappa_{rho_m(s)}->0.

Compactness supplies a subsequence of the pre-update prediction vectors of f_{rho_m(s)-1} converging to the prediction vector of some f_infty in H. For every w, greedy optimality and sign symmetry bound the absolute value of

sum_i partial_2 ell_m(y_i,f_{rho_m(s)-1}(x_i)) h_w(x_i)

by kappa_{rho_m(s)}. K-smoothness makes the derivatives continuous, so this inner product is zero at f_infty for every base learner. Linearity makes the directional derivative zero for every direction in H. Convexity then gives F_m(f)>=F_m(f_infty) for every f in H. Continuity of F_m along the subsequence and monotonicity of the full sequence imply F_m(f_t)->min_{f in H}F_m(f).

Applying this to every m and using separability and V=Lambda gives

Rhat(g_t)->sum_m min_{f in H}F_m(f)=min_{g in Lambda}Rhat(g)=min_{g in V}Rhat(g).

This is the stated conclusion.
