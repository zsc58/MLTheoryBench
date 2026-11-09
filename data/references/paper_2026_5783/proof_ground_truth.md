# Reference Proof

## Proof Structure and Obligation Ledger

The proof establishes: (i) well-defined finite positive static hardness and the pairwise minimization needed for localization; (ii) explicit quadratic hardness estimates, including the case with no later arms; (iii) the incompatible-allocation max-min bound; (iv) uniform local NEF comparison and cancellation of scaling factors; (v) the adaptive lower bound with its stated quantifier order; and (vi) both impossibility consequences.

The static-allocation exponent identity and adaptive information inequality are explicit hypotheses of the public task. Their derivations are not additional obligations of this conditional theorem. No paper-specific lemma or external specialized result is otherwise invoked without its needed derivation below.

## Complete Proof

Fix a consistent algorithm family `mathcal A` and put

`C_K = 1 + sum_{j=3}^K (1+sqrt(j-1))^{-2}`.

All asymptotics below keep `K` fixed.

### 1. Pairwise minimization and well-definedness

Let `eta(theta)` be the inverse of the strictly increasing map `A'`. The density formula gives

`D(s,t) = (eta(s)-eta(t))s - A(eta(s)) + A(eta(t))`.

In particular, this divergence is finite for `s,t in Theta`. Differentiating in its first argument gives

`partial_s D(s,t) = eta(s)-eta(t)`,

`partial_s^2 D(s,t) = eta'(s) = 1/A''(eta(s)) > 0`.

Thus `D(s,t)` is strictly convex in `s`, is minimized uniquely at `s=t`, and decreases toward that point from either side.

Fix an instance `z`, its best arm `b`, an interior allocation `alpha`, and a challenger `j != b`. Separability leaves only the coordinates `b,j` to minimize, subject to `u<=v`. Both coordinates can be clipped to the compact interval `[z_j,z_b]` without increasing the objective or violating their order. A minimum therefore exists. If it had `u<v`, one could increase `u` slightly toward `z_b`, strictly decreasing its contribution while preserving feasibility. Consequently the minimizer has `u=v=m`.

The derivative of the resulting one-variable objective is

`(alpha_b+alpha_j)eta(m) - alpha_b eta(z_b) - alpha_j eta(z_j)`.

It has a unique zero strictly between `z_j` and `z_b`. Hence

`G(z,alpha) = min_{j != b} min_{m in [z_j,z_b]} {alpha_b D(m,z_b)+alpha_j D(m,z_j)}`.       (1)

Each inner minimum is strictly positive, because the two distinct means cannot both equal `m`. Thus `G(z,alpha)>0`. For any fixed challenger `j`, changing only coordinate `b` to `z_j` is feasible and shows

`G(z,alpha) <= alpha_b D(z_j,z_b) <= D(z_j,z_b)`.

Taking the supremum over interior allocations, and using any one such allocation for a positive lower bound, proves

`0 < G_so(z) < infinity` and `0 < H_so(z) < infinity`.

The same pairwise reduction applies to quadratic divergence on any interval containing the instance coordinates. For `d_G(s,t)=(s-t)^2/2`, the minimizing common coordinate is the weighted arithmetic mean, so

`G_G(z,alpha) = min_{j != b} [alpha_b alpha_j/(alpha_b+alpha_j)] (z_b-z_j)^2/2`.       (2)

Here `G_G` and `H_G=1/sup_alpha G_G` refer to the quadratic model on `R`. The minimizers in (2) lie between instance coordinates, so restricting the parameter domain to an interval containing those coordinates does not change these values.

### 2. Quadratic construction and explicit hardness estimates

Fix an integer `L>=K` and define

`x_1=0, x_2=-1, x_k=-L^k` for `k>=3`.

Define `a` by

`a_1=-sqrt(L), a_2=-1+sqrt(L), a_k=-L^k` for `k>=3`,

and, for `3<=j<=K`, let `b^(j)` agree with `x` except that

`b^(j)_j=L^j sqrt(L)`.

The best arms are respectively `1`, `2`, and `j`. Thus every member of

`E_L={a,b^(3),...,b^(K)}`

is a unique-best-arm alternative to `x`.

For `a`, choose

`alpha_1=alpha_2=(L-K+2)/(2L)`, and `alpha_k=1/L` for `k>=3`.

These weights are positive and sum to one. The challenger-1 term of (2) is

`[(L-K+2)/(4L)] (2sqrt(L)-1)^2/2 = (L/2)(1+o_L(1))`.

For challenger `k>=3`, its term is

`[(L-K+2)/(L(L-K+4))] (L^k+sqrt(L)-1)^2/2`,

which is asymptotic to `L^(2k-1)/2`, and therefore exceeds the challenger-1 term for sufficiently large `L`. It follows that

`H_G(a) <= 2L^{-1}(1+o_L(1))`.       (3)

For `b^(j)`, write `n=j-1` and let `Delta_k=b^(j)_j-b^(j)_k`. Put `tau=1/L` if `j<K`, and `tau=0` if `j=K`. Assign

`alpha_j=(1-tau)/(1+sqrt(n))`,

`alpha_i=(1-tau)/[sqrt(n)(1+sqrt(n))]` for `i<j`.

If `j<K`, also put

`S_j=sum_{k=j+1}^K Delta_k^{-2}`,

`alpha_k=tau Delta_k^{-2}/S_j` for `k>j`.

When `j=K`, there are no later coordinates and no `S_j` is needed. In both cases the allocation is interior and sums to one.

For `i<j`,

`Delta_i^2=L^(2j+1)(1+o_L(1))`,

and the corresponding term in (2) is

`[(1-tau)/(2(1+sqrt(j-1))^2)] L^(2j+1)(1+o_L(1))`.

If `j<K`, then `alpha_k<=1/L` for `k>j`, whereas `alpha_j` stays bounded away from zero. For all sufficiently large `L`, `alpha_k<=alpha_j`, and therefore the later-arm term is at least

`alpha_k Delta_k^2/4 = tau/(4S_j)`.

Since `Delta_k>=L^k`,

`S_j <= sum_{k=j+1}^infinity L^{-2k} <= (4/3)L^{-2j-2}`

for `L>=2`. Every later-arm term is consequently at least

`(3/16)L^(2j+1)`.

For every `j>=3`,

`3/16 > 1/[2(1+sqrt(j-1))^2]`.

Thus the later-arm terms are nonbinding for large `L`. The same conclusion holds without a later-arm check when `j=K`. We obtain

`H_G(b^(j)) <= 2(1+sqrt(j-1))^2 L^{-(2j+1)}(1+o_L(1))`.       (4)

Because there are only finitely many alternatives for fixed `K`, all the relative errors in (3)–(4) can be bounded by a single sequence tending to zero.

### 3. The incompatible-allocation obstruction

For every `w in Delta_K`, including boundary allocations,

`sum_k w_k d_G(x_k,a_k) = (w_1+w_2)L/2`,

`sum_k w_k d_G(x_k,b^(j)_k) = w_j L^(2j+1)(1+L^{-1/2})^2/2`.

Set `c_j=(1+sqrt(j-1))^2`. Equations (3)–(4) imply that there is a nonnegative `e_L->0`, independent of `w`, such that

`min_{y in E_L} H_G(y) sum_k w_k d_G(x_k,y_k)`

`<= (1+e_L) min{w_1+w_2,c_3w_3,...,c_Kw_K}`.       (5)

To optimize the last minimum, denote its value by `t`. Then

`w_1+w_2>=t` and `w_j>=t/c_j` for `j>=3`.

Summing gives

`1>=t[1+sum_{j=3}^K c_j^{-1}]=t C_K`.

Equality is feasible: set `w_j=C_K^{-1}/c_j` for `j>=3` and split mass `C_K^{-1}` between arms 1 and 2. Hence

`sup_{w in Delta_K} min{w_1+w_2,c_3w_3,...,c_Kw_K}=C_K^{-1}`,

and therefore

`sup_{w in Delta_K} min_{y in E_L} H_G(y) sum_k w_k d_G(x_k,y_k) <= (1+e_L)C_K^{-1}`.       (6)

This is an algebraic quadratic-model bound. No assumption about an algorithm operating on a different reward family has been used.

### 4. Uniform local quadratic comparison

Choose any `theta_0 in Theta` and write `eta_0=eta(theta_0)` and `v_0=A''(eta_0)>0`. The NEF formula also gives

`D(theta,theta')=A(eta(theta'))-A(eta(theta))-A'(eta(theta))(eta(theta')-eta(theta))`.

For distinct means, Taylor's theorem and the mean value theorem yield

`D(theta,theta') = [A''(c)/A''(d)^2](theta-theta')^2/2`,

where `c,d` are between the corresponding natural parameters. Equal means give zero on both sides of the comparison below.

Take `r_L=L^{-1/3}`. For large `L`, the closed mean interval of radius `r_L` around `theta_0` lies inside `Theta`. Its image under the continuous inverse mean map is a compact interval shrinking to `eta_0`. Let `m_L` and `M_L` be the minimum and maximum of `A''` on that natural-parameter interval. Then

`m_L -> v_0`, `M_L -> v_0`, and `m_L>0`.

The coefficient above lies between `m_L/M_L^2` and `M_L/m_L^2`. Consequently, with

`delta_L=max{|v_0 m_L/M_L^2-1|, |v_0 M_L/m_L^2-1|}`,

we have `delta_L->0`, and uniformly for both means in the mean interval,

`(1-delta_L)D_0(theta,theta') <= D(theta,theta') <= (1+delta_L)D_0(theta,theta')`,       (7)

where

`D_0(theta,theta')=(theta-theta')^2/(2v_0)`.

This applies to both orientations of the divergence. Take `L` large enough also that `delta_L<1`.

Set `epsilon_L=L^{-(K+1)}` and transform every quadratic coordinate `z_k` into `theta_0+epsilon_L z_k`. Denote the transformed baseline by `mu^(L)` and the transformed alternative set by `D_L`. Their largest displacement from `theta_0` is at most `L^{-1/2}`, which is smaller than `r_L`. Thus all coordinates belong to `Theta` for sufficiently large `L`. Positive scaling preserves all strict best-arm comparisons, so

`D_L subset Alt(mu^(L)) intersect Theta_u^K`.

For an instance `lambda in D_L`, let `G_0(lambda,alpha)` and `H_0(lambda)` be defined as their true counterparts using `D_0`, with alternatives still restricted to `Theta^K`. Formula (1) shows that the true pairwise minimizing mean lies between two instance coordinates and hence in the interval where (7) holds. At that minimizer, the lower inequality in (7) bounds the true pairwise value below by `1-delta_L` times the quadratic value there, which is itself at least the quadratic pairwise minimum. Taking the minimum over challengers yields, for every interior `alpha`,

`G(lambda,alpha) >= (1-delta_L)G_0(lambda,alpha)`.

Taking suprema and reciprocals gives

`H_so(lambda) <= H_0(lambda)/(1-delta_L)`.       (8)

The upper inequality in (7) gives, for every closed-simplex allocation `w`,

`sum_k w_k D(mu^(L)_k,lambda_k) <= (1+delta_L)sum_k w_k D_0(mu^(L)_k,lambda_k)`.       (9)

If `lambda=theta_0+epsilon_L y` for `y in E_L`, the information sum on the right equals

`(epsilon_L^2/v_0)sum_k w_k d_G(x_k,y_k)`.

The quadratic pairwise minimizers lie between the instance coordinates. They therefore remain in `Theta`, so the restriction to `Theta` does not change the quadratic pairwise expression. It follows directly from (2) that

`G_0(lambda,alpha)=(epsilon_L^2/v_0)G_G(y,alpha)`

and

`H_0(lambda)=(v_0/epsilon_L^2)H_G(y)`.

The factors cancel in the product of hardness and information. Combining (6), (8), and (9), uniformly over `w`, gives

`sup_{w in Delta_K} min_{lambda in D_L} H_so(lambda) sum_k w_k D(mu^(L)_k,lambda_k)`

`<= [(1+delta_L)/(1-delta_L)](1+e_L)C_K^{-1} =: q_L`,       (10)

where `q_L>0` and `q_L->C_K^{-1}`.

### 5. Adaptive lower bound and nonattainment

Apply the assumed information inequality with the given consistent family `mathcal A`, baseline `mu^(L)`, nonempty alternative set `D_L`, and benchmark `H_so`. All its hypotheses hold, including finite positivity of `H_so`, proved in Section 1. Equation (10) yields

`[sup_{lambda in D_L} rho_Hso(mathcal A,lambda)]^{-1} <= q_L`.

With the extended reciprocal conventions, this implies

`sup_{mu in Theta_u^K} rho_Hso(mathcal A,mu) >= sup_{lambda in D_L} rho_Hso(mathcal A,lambda) >= 1/q_L`.

Letting `L->infinity` proves

`sup_mu rho_Hso(mathcal A,mu) >= C_K`.

No attainment of this supremum is asserted or needed. Since the consistent family was arbitrary,

`inf_{mathcal A consistent} sup_mu rho_Hso(mathcal A,mu) >= C_K`.

For `K>=3`, the sum defining `C_K-1` is strictly positive. Thus no consistent family satisfies `sup_mu rho_Hso(mathcal A,mu)<=1`.

### 6. Nonexistence of a complexity

Suppose a function `H:Theta_u^K -> (0,infinity)` is a complexity for a class `C` containing all interior static-proportion families. For any such allocation `w`, the assumed exponent identity, together with `0<G(mu,w)<infinity`, gives

`rho_H(mathcal A^w,mu)=1/[H(mu)G(mu,w)]`.

The lower-bound clause of the complexity definition requires this value to be at least one for every `mu` and every interior `w`. Taking the supremum of `G(mu,w)` over `w` gives

`H(mu)G_so(mu)<=1`, or `H(mu)<=H_so(mu)`.

Let `mathcal A* in C` satisfy the achievability clause. At each fixed instance, `limsup_T h_{mu,T}/H(mu)<=1`, so eventually `h_{mu,T}<=2H(mu)`. If the error probability is nonzero, this implies

`p_{mu,T} <= exp[-T/(2H(mu))]`;

zero error already satisfies the same bound. Thus `mathcal A*` is consistent, even if consistency was not required of every member of `C`.

Since `H(mu)<=H_so(mu)`,

`rho_Hso(mathcal A*,mu)<=rho_H(mathcal A*,mu)`

for every instance. Therefore `sup_mu rho_Hso(mathcal A*,mu)<=1`, contradicting the lower bound `C_K>1`. No such complexity exists.
