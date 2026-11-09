# Reference Proof

## Contract and Scope

Write d=d_s+d_a, q=H-1, and r_T=R_tilde. The finite-horizon model is fixed as T=NH increases. Only inputs x_{n,h} with h<=q have observed transition responses. The determinant defining gamma_T uses every visited input, including h=H. All processes and selections have the measurable, separable versions specified in the task. A posterior draw uses fresh randomness and is conditionally independent of the true process given the preceding history.

The proof below explicitly closes confinement, the event-weighted Bellman reduction, finite-net concentration, episodic variance control, interpolation, growing-radius information-gain asymptotics, and final absorption. No paper-specific intermediate lemma is assumed without derivation.

## 1. Gaussian Suprema and Confinement

The kernel assumptions imply

    d_c(x,y)^2=c(x,x)-2c(x,y)+c(y,y)<=2L||x-y||_2^alpha,
    diam_{d_c}(B(u))<=2sqrt(C).

A proper Euclidean delta-cover of a d-dimensional ball has at most (1+2u/delta)^d points, by the usual disjoint-ball volume comparison. Consequently its proper canonical covering numbers satisfy

    N_pr(B(u),d_c,z)<= (1+2u(2L)^{1/alpha}/z^{2/alpha})^d.

We need a vector chaining calculation with its mean terms retained. For a centered independent-coordinate vector GP g with pointwise coordinate variance at most v and canonical diameter Delta, take proper covers at scales Delta*2^{-j}, starting with a single point at j=0. An edge increment has mean norm at most sqrt(d_s) times its canonical distance. Its centered norm has sub-Gaussian scale equal to that distance: represent the increment as its canonical standard deviation times a standard d_s-dimensional Gaussian and apply Gaussian Lipschitz concentration. The edge distances are at most min(3Delta*2^{-j},Delta), whose sum over j>=1 is (5/2)Delta. The expected maximum of M centered a-sub-Gaussian variables is at most a sqrt(2log M), as follows directly from the exponential moment bound and optimization over its parameter. There are at most N_j N_{j-1}<=N_j^2 edges at level j. Summing their centered maxima and comparing the dyadic sum with the entropy integral gives

    E sup ||g|| <=12 integral_0^infty sqrt(log N_pr(z)) dz
                    +sqrt(v d_s)+(5/2)Delta sqrt(d_s).

In particular, when Delta<=2sqrt(v), the last two terms are at most 6sqrt(v d_s). The argument first applies to finite subsets; the vanishing last-scale remainder and then separability give the full supremum. If Delta=0, the process is constant on the index set almost surely and the claim follows directly.

For the prior process on B(u), substituting the displayed covering bound and setting z=2sqrt(C)t gives

    integral sqrt(log N_pr) <=2sqrt(2) alpha^{-1/2}
                               sqrt(Cd log(5+5u^alpha L/C)).

For completeness, use sqrt(a+b)<=sqrt(a)+sqrt(b), integrate sqrt(log(1/t)) on (0,1), and use 1+b^{1/alpha}<=(1+b)^{1/alpha} for alpha<=1. The resulting coefficient for E sup ||f*|| is at most

    24sqrt(2)+6/sqrt(log 5)<42.

Thus the source's explicit bound with coefficient 42 is valid despite its omitted vector mean factor.

For a finite index set, sup ||f*(x)|| is a sqrt(C)-Lipschitz function of a finite standard Gaussian vector: each evaluation-norm map has operator norm sqrt(c(x,x)), and a maximum preserves the Lipschitz constant. Gaussian concentration, followed by the separable limit, therefore yields

    P(sup_{||x||<=u}||f*(x)||>=v)<=exp(-v^2/(8C))

when v>=84 alpha^{-1/2}sqrt(Cd log(5+5u^alpha L/C)). This is an unconditional prior-process estimate. An uncentered posterior draw does not satisfy this same conditional estimate.

Likewise, for a fresh noise vector epsilon,

    P(||epsilon||>v)<=exp(-v^2/(8sigma^2)),  v>=2sigma sqrt(d_s),

because its mean norm is at most sigma sqrt(d_s) and its norm is sigma-Lipschitz in a standard Gaussian vector.

Set M=max(C,sigma^2), b=max(1,L/C),

    R_1=max(2sigma sqrt(d_s),4sigma sqrt(log T)),
    R_h=max(8sqrt(M log T),D sqrt(log(5+5(R_{h-1}^2+R_a^2)^{alpha/2}L/C)))

for h>=2. At a first exit from these radii, a noninitial state can exceed R_h only if either the prior-process supremum on the preceding input ball exceeds R_h/2 or the fresh noise norm exceeds R_h/2. This is a pathwise inclusion; it does not condition the prior process on the preceding-state event. Each resulting probability is at most T^{-2}. The initial-state term is also at most T^{-2}. The first-exit indicator decomposition and a union bound give probability at most 2/T for any exit.

Here every R_h is at most the public R. To verify this, put ell=10b. The assumed real-valued T inequality implies

    T^2>=T^2/2+D^2 log(D ell(R_a+1))
        >=D^2 log(T ell(R_a+1))
        >=D^2 log((T+R_a)ell).

The middle inequality follows from y^2/2>=log y for y=T/D>0. Thus R<=T. The base radius and the term 8sqrt(M log T) are at most R. Inductively R_{h-1}<=R implies sqrt(R_{h-1}^2+R_a^2)<=T+R_a, and

    5+5(T+R_a)^alpha L/C<=10(T+R_a)b.

This proves the induction. Define

    A={max_{n,h}||s_{n,h}||<=R},
    B={max_{n,h}||x_{n,h}||<=r_T}.

Then A is a subset of B and P(A^c)<=2/T. In particular P(B^c)<=2/T. The argument does not require D>=1.

## 2. Posterior-Sampling and Bellman Reductions

Conditionally on F_{n-1}, f* and f^(n) are independent draws from the same posterior law. The episode's initial state is fresh and independent of both. The optimal-value expectations therefore agree, giving

    R_T=E sum_n Delta_{n,1}(s_{n,1}),
    Delta_{n,h}=V^{(n)}_{pi_n,h}-V^*_{pi_n,h}.

This identity is established before inserting the full-trajectory event A.

Let

    b_{n,h}=<P^(n)(x_{n,h})-P*(x_{n,h}),V^{(n)}_{pi_n,h+1}>.

Bellman telescoping along the true trajectory gives the sum of the realized b_{n,h}, plus two martingale sums: one replacing a conditional expectation of Delta_{n,h+1} by its realized next-state value, and one replacing the policy-averaged Bellman error by the realized-action Bellman error. Use a filtration that includes f*, posterior draws already made, and the interaction up to the current state, but not the fresh action and transition randomizations. Each difference has conditional mean zero and conditional sub-Gaussian scale at most 2H R_max, since the relevant values or Bellman errors lie in [-2H R_max,2H R_max]. There are at most T differences in each sum.

Iterating conditional exponential-moment bounds gives, for each sum Y,

    P(Y>=z)<=exp(-z^2/(8T H^2 R_max^2)).

For any event E, E[1_E Y]<=E[Y_+], and integrating this tail gives E[Y_+]<=H R_max sqrt(2pi T). The event need not be predictable. Thus

    E[1_A sum_n Delta_{n,1}(s_{n,1})]
      <=E[1_A sum_{n,h<=q}b_{n,h}]+2H R_max sqrt(2pi T).

This controls the absolute size of a total martingale sum when needed, not the sum of absolute increment sizes.

For equal-covariance Gaussian transitions, KL(P^(n)||P*)=||f^(n)(x)-f*(x)||^2/(2sigma^2). Pinsker's inequality and ||V||_infty<=H R_max give

    |b_{n,h}|<=H R_max ||f^(n)(x_{n,h})-f*(x_{n,h})||/sigma.

Also |sum_n Delta_{n,1}|
<=2NH R_max=2T R_max. Therefore

    R_T<= (H R_max/sigma) E[1_A sum_{n,h<=q}||f^(n)(x_{n,h})-f*(x_{n,h})||]
           +2H R_max sqrt(2pi T)+4R_max.

## 3. Finite-Net Errors With the Indicator Preserved

Choose a proper Euclidean epsilon-cover Q of B(r_T), with deterministic measurable nearest-point map omega. Its size is at most (1+2r_T/epsilon)^d. Let sigma_{n-1}(x) denote the posterior coordinate standard deviation based on observed transitions before episode n. It is positive: in the kernel-feature representation the posterior operator is the inverse of I plus a finite positive operator, and the feature norm is positive.

Given F_{n-1}, the difference f^(n)-f* is a centered independent-coordinate GP with covariance 2c_{n-1}. Define

    Z_n=max_{z in Q}||f^(n)(z)-f*(z)||/sigma_{n-1}(z).

Finite-dimensional Gaussian concentration gives centered sub-Gaussian scale sqrt(2). The mean is at most sqrt(2d_s)+2sqrt(log |Q|), by the Gaussian norm mean bound and the finite-max exponential moment bound. Consequently

    P(Z_n>=u|F_{n-1})<=exp(-u^2/16)

for u at least twice that mean. Choose u also at least 10 and 8sqrt(log(eT)).

Posterior canonical increment variances cannot exceed prior increment variances. The conditional L2 reverse triangle inequality therefore gives, pathwise in the history,

    |sigma_{n-1}(x)-sigma_{n-1}(y)|<=d_c(x,y)
       <=sqrt(2L)||x-y||^{alpha/2}.

At each visited input on A, split according to Z_n<=u and Z_n>u. Keep 1_A in the bounded part and drop it only from the nonnegative tail part. Since posterior standard deviations are at most sqrt(C), conditional tail integration gives

    E[1_A ||f^(n)(omega(x))-f*(omega(x))||]
      <=u E[1_A sigma_{n-1}(x)]
        +u sqrt(2L epsilon^alpha)
        +sqrt(C)(u+8/u)exp(-u^2/16).

No conditional-expectation identity involving 1_A is used. Summing at most T terms, the last term is bounded by a fixed constant with the selected threshold.

## 4. Observed-Transition Episodic Variance Bound

The two matrix inequalities used here are deterministic, so adaptive input selection creates no extra hypothesis.

For a sequence of observed inputs z_1,...,z_m, write v_j(x) for its posterior coordinate variance after j noisy responses. Successive Schur complements give

    log det(I+K_m/sigma^2)=sum_{j=1}^m log(1+v_{j-1}(z_j)/sigma^2).

Because 0<=v_{j-1}(z_j)<=C and log(1+t/sigma^2)/t is decreasing,

    sum_j v_{j-1}(z_j)<=a log det(I+K_m/sigma^2),
    a=C/log(1+C/sigma^2).

For the variance-ratio inequality, use kernel features phi_x and the posterior operator A_i=I+sigma^{-2}sum_{ell<=i}phi_{z_ell}phi_{z_ell}^*. After conjugation by A_i^{-1/2}, the additional positive operator has norm at most its trace, namely sigma^{-2}sum_{ell=i+1}^j v_i(z_ell). Inverting the resulting operator inequalities yields

    v_i(x)<=v_j(x)[1+sigma^{-2}sum_{ell=i+1}^j v_i(z_ell)].

Now reindex only the m=Nq actual observed-transition inputs. There are no terminal inputs in this sequence. Let i_j be the number of observations preceding the episode containing z_j. Then v_{i_j}(z_j)=sigma_{n(j)-1}(z_j)^2. Applying the ratio inequality with j-1, summing square roots, and using Cauchy-Schwarz gives

    sum_j sqrt(v_{i_j}(z_j))
      <=sqrt(sum_j v_{j-1}(z_j))
         sqrt(m+(q/sigma^2)sum_j v_{i_j}(z_j)).

In each episode select, measurably with deterministic tie-breaking, one of its q observed inputs y_n having maximum episode-start variance. Conditioning on all preceding observed inputs gives no larger variance than conditioning only on preceding representatives. Applying the determinant identity to the representative sequence therefore gives

    sum_j v_{i_j}(z_j)<=q a log det(I+K_y/sigma^2).

Define the private auxiliary quantity

    eta_N=E[1_A (1/2)log det(I+K_y/sigma^2)].

It is not the public information gain of the first N visited inputs. The determinant on all observed inputs is bounded by the determinant on all T visited inputs: adding inputs multiplies the determinant by Schur-complement factors at least one. Also 1_A<=1_B. Cauchy-Schwarz in expectation now yields

    E[1_A sum_{n,h<=q}sigma_{n-1}(x_{n,h})]
      <=sqrt(2a gamma_T(sigma^2,r_T)
                   [T+(2a q^2/sigma^2)eta_N]).

This proves the required episodic bound without any phantom terminal observations.

## 5. Uniform Information-Gain Control at the Growing Radius

Here is a direct repair of the sample-size-dependent cutoff argument. For any m points in B(r), choose a proper Euclidean delta-net with k<=(1+2r/delta)^d points. In the kernel-feature Hilbert space, project onto the span of their features. The kernel matrix splits as K=K_0+E, where both parts are positive semidefinite, rank(K_0)<=k, tr(K_0)<=Cm, and

    tr(E)<=2Lm delta^alpha.

The residual bound follows by approximating each feature by the nearest net feature and using ||phi_x-phi_y||^2=d_c(x,y)^2<=2L delta^alpha. The determinant derivative along K_0+tE, or integration of its inverse trace, gives

    log det(I+K/sigma^2)
       <=k log(1+Cm/sigma^2)+2Lm delta^alpha/sigma^2.

This is uniform over all point sequences in the ball. With r=O(sqrt(log m)) and delta=m^{-1/(2d)}, division by m makes both terms tend to zero. No cutoff depends on the realized sequence, and no exchange of a limit with such a cutoff is involved.

For fixed H>=2, T=NH implies r_T=O(sqrt(log N)). Applying the uniform bound to the representative points on A proves eta_N=o(N). Hence

    T+(2a q^2/sigma^2)eta_N=T(1+o(1)).

This simplification is for the fixed finite-horizon asymptotic experiment, not a joint limit with H increasing.

## 6. Interpolation Errors

For a prior process f define g(x)=f(x)-f(omega(x)). Its coordinate variance is at most 2L epsilon^alpha, and its canonical diameter is at most sqrt(8L epsilon^alpha). Within a nearest-point cell, omega(x)=omega(y), so the residual canonical distance is exactly d_c(x,y), bounded by sqrt(2L)||x-y||^{alpha/2}.

Construct proper Euclidean covers within each cell. A proper delta_0-cover of a cell contained in an epsilon-ball needs at most (1+4epsilon/delta_0)^d points. Set delta_0=(z^2/(2L))^{1/alpha}. Combining with the original cover size gives, for z<=sqrt(8L epsilon^alpha) and epsilon<=r_T,

    N_pr(B(r_T),d_g,z)
      <=(7sqrt(L)r_T^{alpha/2}/z)^{2d/alpha}.

The constant is justified by [3(4*2^{1/alpha}+8^{1/alpha})]^{alpha/2}<=sqrt(48)<7. This avoids the incorrect numerical simplification in the source.

Let y=sqrt(8L epsilon^alpha), z_0=7sqrt(L)r_T^{alpha/2}, and b=log(3(r_T/epsilon)^{alpha/2}). Substitute z=y exp(-t) in the entropy integral and use Jensen's inequality under density exp(-t):

    integral_0^y sqrt(log(z_0/z)) dz
       <=y sqrt(log(z_0/y)+1).

Since epsilon<=r_T, the logarithms are positive. It follows, with slack, that the residual entropy integral is at most

    6 alpha^{-1/2}sqrt(dL epsilon^alpha b).

Combining this with the corrected vector chaining calculation in Section 1 bounds the residual supremum by a fixed numerical multiple of

    alpha^{-1/2}sqrt(dL epsilon^alpha log(3(r_T/epsilon)^{alpha/2})).

This also implies the source's looser explicit interpolation bound; the available entropy-constant slack absorbs the restored vector mean factor. Separability is used within each of the finitely many cells.

For each posterior draw f^(n), its unconditional process law is the prior law, by integrating its conditional posterior law. Thus each sampled-process interpolation error is bounded by the corresponding prior-marginal supremum after dropping 1_A and taking the supremum over the ball. The true-process interpolation error is bounded in the same way. We do not assert equality of joint laws with their dependent trajectory inputs.

Choose

    epsilon=min(r_T/2,L^{-1/alpha}T^{-2/alpha}).

It is admissible for all T and equals the source's choice eventually. Then u=O(sqrt(d log T)), T sqrt(L epsilon^alpha)=O(1), and the sum of both interpolation bounds is O(sqrt(d log T)). Combining Sections 3-6 proves

    E[1_A sum_{n,h<=q}||f^(n)(x_{n,h})-f*(x_{n,h})||]
      <=O(sqrt(d log T))
        +O(sqrt(d log T))sqrt(gamma_T[T+O(q^2 eta_N)]).

## 7. Lower-Order Absorption and Final Rate

The information gain is eventually bounded below by a positive constant, uniformly over policy tie-breaking. Choose a fixed input radius r_0>R_a for which p=P(||s_{1,1}||<=sqrt(r_0^2-R_a^2))>0. Continuity and strict positivity of c(x,x) on B(r_0) give kappa=min_{||x||<=r_0}c(x,x)>0. On the intersection of this initial-state event with A, the full determinant is at least 1+kappa/sigma^2. Hence

    gamma_T(sigma^2,r_T)
       >=(p-2/T)(1/2)log(1+kappa/sigma^2).

For all sufficiently large T this is a positive constant. This justifies absorbing O(sqrt(d log T)), the O(H sqrt(T)) martingale term, and fixed bad-event terms into the asserted rate.

For fixed H>=2, eta_N=o(N) now gives

    R_T=O(H sqrt(d gamma_T(sigma^2,r_T) T log T)).

When H=1 there are no transitions affecting reward, and any policy optimal for a sampled model is optimal for the true model because rewards are known and common. Regret is exactly zero. The same observation handles T=1 when admissible. Zero rewards, singleton action spaces, and singular kernel matrices create no problem: rewards can vanish, actions need not have an interior, and sigma^2 I makes all regression inverses nonsingular.

Every constant and asymptotic step above is independent of T for the fixed model. No additional unspecified polylogarithmic multiplier is needed beyond the displayed order.
