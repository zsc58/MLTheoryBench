# Reference Proof

Write

m_r(z) = integral p(u) ell(u)^(lambda_r) q_{s_r}(z | u) mu(du).

Because nu_r is sigma-finite and the measure p(u) ell(u)^(lambda_r) mu(du) is finite with mass Z_r, Tonelli's theorem gives

integral m_r(z) nu_r(dz) = Z_r.

Consequently m_r is finite nu_r-almost everywhere. Moreover, for every measurable A,

eta_r(A) = Z_r^(-1) integral_A m_r(z) nu_r(dz).

Thus eta_r assigns zero mass to {m_r=0} and to {m_r=infinity}. The arbitrary branch in the definition of K_r therefore affects no population identity. On {0<m_r(z)<infinity},

K_r(dx | z) = m_r(z)^(-1) p(x) ell(x)^(lambda_r) q_{s_r}(z | x) mu(dx).

Integrating against eta_r and using that Q_{s_r} is a Markov kernel gives

eta_r K_r(dx)
 = Z_r^(-1) p(x) ell(x)^(lambda_r)
   integral q_{s_r}(z | x) nu_r(dz) mu(dx)
 = pi_r(dx).

For r>=1, P_{r-1}=Q_{s_{r-1}}, so directly from the definition of eta_{r-1},

pi_{r-1}P_{r-1}=eta_{r-1}.

In particular, eta_0K_0=pi_0.

For the stage-r proposal, the density of M_r with respect to nu_r(dz_r) mu(dx) nu_{r-1}(dz_{r-1}) is, M_r-almost everywhere,

Z_r^(-1) p(x) ell(x)^(lambda_r)
 q_{s_r}(z_r | x) q_{s_{r-1}}(z_{r-1} | x).

The normalized extended target has density

Z_{r-1}^(-1) p(x) ell(x)^(lambda_{r-1})
 q_{s_r}(z_r | x) q_{s_{r-1}}(z_{r-1} | x).

It is normalized because both auxiliary kernels integrate to one and the remaining integral is Z_{r-1}. Therefore the Radon-Nikodym derivative is, M_r-almost everywhere,

W_r(z_r,x,z_{r-1})
 = (Z_r/Z_{r-1}) ell(x)^(lambda_{r-1}-lambda_r).

The common positive factor Z_r/Z_{r-1} cancels after normalization. Hence the algorithm may use G_r(x)=ell(x)^(lambda_{r-1}-lambda_r), which is a measurable version of the stage factor up to a positive stage constant and is independent of both auxiliary states. This also verifies that applying the factor immediately after reconstruction is equivalent to applying the proposal-based Radon-Nikodym derivative before propagation.

Let Psi_G(mu)(A)=mu(G 1_A)/mu(G). Since G_r is bounded and pi_r(G_r)>0,

Psi_{G_r}(pi_r)=pi_{r-1},

because multiplication by G_r changes the exponent of ell from lambda_r to lambda_{r-1}.

We now prove particle consistency while also proving the weight-dispersion fact needed for independent mutation. For a weighted particle system with weights summing to one, write

rho_N(f)=sum_i w_i f(X_i),

and let a_N=max_i w_i. If conditional independent mutation with a Markov kernel K is applied, then for bounded f,

E[rho_N^K(f) | input] = rho_N(Kf),

and

Var(rho_N^K(f) | input)
 <= ||f||_infinity^2 sum_i w_i^2
 <= ||f||_infinity^2 a_N.

Therefore, if rho_N is consistent for rho and a_N tends to zero in probability, then rho_N^K is consistent for rho K. This follows by applying consistency to the bounded measurable function Kf and using the conditional variance bound.

We also use the following elementary weight observation. Suppose a weighted system with maximum weight a_N tends to zero is reweighted by a bounded potential H, and let D_N=sum_i w_i H(X_i). If D_N tends in probability to a strictly positive limit D, then on the event D_N>0,

max_i (w_i H(X_i)/D_N) <= ||H||_infinity a_N/D_N,

so the new maximum weight tends to zero. If D_N=0, use the stipulated fallback and retain the entering normalized weights; since the probability of D_N=0 tends to zero, the same conclusion holds. Resampling resets the maximum weight to 1/N.

Initialization has equal weights, so its maximum weight is 1/N. Since lambda_R=0,

pi_R(dx)=p(x)mu(dx),

and hence eta_R is exactly the initialization law. The iid initial particles are therefore consistent for eta_R, and their maximum weight tends to zero.

Assume inductively that the weighted auxiliary particles at stage r are consistent for eta_r and have maximum weight tending to zero. Independent reconstruction with K_r is consistent for eta_rK_r=pi_r by the mutation estimate above. Thus the empirical averages of G_r and of G_r times any bounded test function converge to their pi_r expectations. In particular, the unnormalized weight total converges in probability to pi_r(G_r)>0. The probability of the zero-total-weight event consequently tends to zero. On the complementary event, normalized weighting is consistent for Psi_{G_r}(pi_r)=pi_{r-1}; on the fallback event the same assertion holds asymptotically because that event has vanishing probability. The weight observation shows that the post-weight maximum tends to zero. If resampling is used, its stated consistency property preserves the pi_{r-1} limit and resets the maximum to 1/N. If it is omitted, the weighted system and its maximum are unchanged.

Independent propagation with P_{r-1} is then consistent for pi_{r-1}P_{r-1}=eta_{r-1}, again by the conditional variance estimate, and the weights still have maximum tending to zero. This completes the induction from eta_R down to eta_0.

Finally, independent reconstruction with K_0 is consistent for eta_0K_0=pi_0. Hence, for every bounded measurable h,

sum_i w_0^(i) h(x_0^(i)) converges in probability to pi_0(h).

Since lambda_0=1,

pi_0(dx)=Z_0^(-1)p(x)ell(x)mu(dx)=p(x | y)mu(dx).

The asserted convergence for bounded measurable h is stronger than needed for weak convergence. In particular it holds for every bounded continuous h, so the final weighted empirical measures converge weakly in probability to the posterior.
