# Reference Proof

## Audited obligations

1. Verify that the defined induced laws and objective evaluations are measurable, using the explicit finite-objective contract rather than an absolute-envelope assertion.
2. Derive the population objective-gap bound from sieve bias, uniform empirical error, and algorithmic suboptimality.
3. Prove that the objective gap vanishes in probability.
4. Apply population separation, including an empty separation set, and specialize using the stipulated equality P*=P0.

## Complete Proof

### step_001: Profiling and induced laws

Write
ell(x,z;u) = E_{theta~q_u}[log p_theta(x|z)] + log pi_Z(z).
If Sigma_theta(z) >= lambda I_m for lambda>0, the Gaussian density formula gives
log p_theta(x|z) <= c := -(m/2) log(2 pi lambda)
for every x,z,theta. Thus
ell(x,z;u) <= c + log pi_Z(z).
The right side tends to minus infinity as ||z|| tends to infinity and is bounded above by a finite constant B independent of x and u. Consequently m(x;u)<=B. This is an upper bound, not a bound on |m(x;u)|.

The task explicitly requires m to be real-valued. This requirement cannot be deduced from the preceding upper bound alone. We can nevertheless verify attainment and measurability without assuming continuity of an unbounded expectation. Use theta=a_u+s_u epsilon with epsilon standard Gaussian. For a convergent sequence (x_n,z_n,u_n), the integrands log p_{a_{u_n}+s_{u_n}epsilon}(x_n|z_n) converge pointwise and are bounded above by c. Fatou's inequality for the nonnegative functions c-log p therefore gives
limsup_n E[log p_{a_{u_n}+s_{u_n}epsilon}(x_n|z_n)] <= E[log p_{a_u+s_u epsilon}(x|z)].
This remains valid when the expectation on the right is minus infinity. Hence ell is jointly upper semicontinuous.

For fixed (x,u), choose a sequence of latent values whose ell values approach the finite real number m(x;u). The coercive upper bound forces this sequence to be bounded. A convergent subsequence and upper semicontinuity give a latent maximizer. Its set is closed and bounded, hence compact.

The same argument proves upper semicontinuity of m. Indeed, for (x_n,u_n)->(x,u), if limsup m(x_n;u_n)=-infinity there is nothing to show. Otherwise pass to a subsequence attaining that limsup and choose latent maximizers z_n. Their ell values have a common finite lower bound, so c+log pi_Z(z_n) forces z_n to be bounded. Along a convergent subsequence,
limsup_n m(x_n;u_n) <= ell(x,z;u) <= m(x;u).
Thus m is Borel measurable.

Each P_u is a probability law because it is a mixture of probability kernels against the probability measure pi_Z times q_u. The map u->P_u is continuous in bounded-Lipschitz distance. To see this, let u_n->u and write q_n,q for their Gaussian densities. They converge pointwise, and
integral |q_n-q| = 2 - 2 integral min(q_n,q) -> 0,
because min(q_n,q)<=q and dominated convergence applies. For any test function f in the definition of d_BL, integrating f first against P_theta(.|z) and then pi_Z gives a function of theta bounded in absolute value by one. Therefore
d_BL(P_{u_n},P_u) <= integral |q_n-q| -> 0.
The triangle inequality now shows that u->d_BL(P_u,P*) is continuous. In particular d_BL(P_{hat u_N},P*) is measurable.

### step_002: Objective well-definedness and measurability

The explicit assumption integral |m(x;u)| P0(dx)<infinity makes the population expectation finite for every u. Both Gaussian laws in the KL term are nondegenerate. If pi_Theta=N(b,V), direct Gaussian integration gives
KL(q_u||pi_Theta) = (1/2)[s_u^2 tr(V^{-1}) + (a_u-b)^T V^{-1}(a_u-b) - p + log det V - p log(s_u^2)],
which is finite and continuous in u. Thus J and every finite-sample objective J_N have finite values.

The upper bound m<=B and Fatou's inequality applied to B-m show that u->E_{P0}m(X;u) is upper semicontinuous. Hence J is Borel measurable. The empirical objective is jointly Borel measurable in the observations and u, and jointly upper semicontinuous. Its supremum over a nonempty compact U_N is finite, attained, and upper semicontinuous as a function of the observations: for a convergent sequence of observation vectors, choose maximizers in U_N, extract a convergent subsequence, and apply joint upper semicontinuity. This also establishes measurability of delta_N^alg after evaluation at the measurable estimator. Measurability of omega_N is explicitly part of the task's probability contract; omega_N may take the value +infinity.

No absolute integrable envelope or Glivenko-Cantelli assertion is needed. In particular, compactness of U_N does not bound |m(x;u)| uniformly over the unbounded observation space. Uniform convergence along the expanding sieves is an assumption, not a conclusion of this preliminary discussion. Attainment of the latent supremum is also not required by the remaining consistency argument.

### step_003: Objective comparison

Let Delta_N=J(u*)-J(hat u_N). Global optimality and hat u_N in U_N imply Delta_N>=0 and r_N>=0. By definition,
Delta_N = r_N + [sup_{u in U_N} J(u)-J(hat u_N)].
On the event omega_N<infinity, the definition of omega_N gives
sup_{u in U_N} J(u) <= sup_{u in U_N} J_N(u)+omega_N
and
J(hat u_N) >= J_N(hat u_N)-omega_N.
Consequently,
sup_{u in U_N} J(u)-J(hat u_N)
<= sup_{u in U_N} J_N(u)-J_N(hat u_N)+2 omega_N
= delta_N^alg+2 omega_N.
Thus
0 <= Delta_N <= r_N+2 omega_N+delta_N^alg.
When omega_N=+infinity this inequality remains true with an infinite right side.

For every t>0, eventually r_N<t/3, and then
Pr(Delta_N>=t) <= Pr(omega_N>=t/6)+Pr(delta_N^alg>=t/3).
Both terms tend to zero by the assumptions. Hence Delta_N->p0. Independence between the errors or between the estimator and the data is not needed.

### step_004: Separation and convergence

Fix epsilon>0 and set
A_epsilon={u in U : d_BL(P_u,P*)>=epsilon}.
If A_epsilon is empty, the event d_BL(P_{hat u_N},P*)>=epsilon is empty for every N.

Otherwise Delta(epsilon) is finite, since A_epsilon contains a parameter with a finite objective gap, and it is strictly positive by assumption. On the epsilon-away event, hat u_N belongs to A_epsilon, so
Delta_N >= Delta(epsilon).
Therefore
Pr(d_BL(P_{hat u_N},P*)>=epsilon)
<= Pr(Delta_N>=Delta(epsilon)) -> 0.
This proves d_BL(P_{hat u_N},P*)->p0 for every epsilon>0.

### step_005: Specified specialization

In the case stipulated in the task, P*=P0. Substitute this equality into the established convergence to obtain d_BL(P_{hat u_N},P0)->p0. No assertion that model membership alone identifies the maximizer of the profiled, penalized objective is needed.

## Source audit note

The source's absolute-envelope assertion at L000765 is false on an unbounded observation space, and L000773 proves only an upper bound. Its subsequent attempt to obtain growing-sieve uniform convergence is not used here. The consistency theorem already assumes that convergence at L000351. All obligations for the frozen public implication are closed by the explicit well-definedness contract and the argument above; the false auxiliary source claim is not treated as an unresolved dependency of this proof.
