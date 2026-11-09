# Reference Proof

## Proof Structure and Obligations

1. Establish the common recurrent/transient decomposition, existence and properties of the Cesaro limit, finiteness of the transient inverse, and well-definedness of the normalized relative value.
2. Derive the recurrent contribution to the performance difference and justify the cancellation of recurrent K terms.
3. Derive the transient contribution explicitly from the canonical blocks.
4. Establish continuity of the visitation measures by finite linear systems and obtain the full parameter differential.

All four obligations are proved below. No specialized external differentiability result is assumed.

## Step 1: Finite-chain structure and definitions

An edge s to s' has positive probability under a positive policy exactly when P(s'|s,a)>0 for at least one action a. Thus all positive policies have the same directed support graph, the same closed communicating classes, and the same transient set. Write these sets as R_1,...,R_m and T, with R their recurrent union. Moreover, if s belongs to R_i, every action remains in R_i: otherwise its positive policy probability would produce an edge leaving that closed class.

Here are the finite-chain facts needed in the proof, together with their elementary justifications. For a finite stochastic matrix M, its powers are bounded in the maximum row-sum norm. Consequently every eigenvalue has modulus at most one, and every Jordan block for an eigenvalue on the unit circle has size one. Averaging the powers in Jordan form therefore converges: eigenvalues other than 1 contribute zero in the Cesaro limit. Denote that limit by E. It is stochastic, and telescoping gives ME=EM=E. Since EM^t=E for every t, averaging once more gives E^2=E. Its range is exactly ker(I-M): the inclusion follows from ME=E, and a fixed vector of M is fixed by every Cesaro average.

For an irreducible stochastic block R_i, every real vector fixed by R_i is constant. Indeed, a coordinate attaining its maximum forces every successor with positive transition probability to attain the same maximum, and irreducibility propagates this to all coordinates. Thus its Cesaro limit has the form E_i=1 g_i^T, with g_i a probability vector. The identity E_i R_i=E_i gives g_i^T R_i=g_i^T. Every invariant row z^T satisfies z^T E_i=z^T, so z^T=(z^T1)g_i^T; hence the stationary probability vector is unique. Its coordinates are positive: a positive coordinate exists, and stationarity along paths to every other state propagates positivity.

If T is nonempty, every transient state has a finite positive-probability path to a closed recurrent class. There are finitely many transient states, so for a fixed policy there exist an integer L and q>0 such that the probability of leaving T within L steps is at least q from every transient state. For the transient-to-transient block T^pi this gives ||(T^pi)^L||_infinity <= 1-q. Hence its powers decay geometrically in blocks of length L, its spectral radius is below one, and

N^pi=(I-T^pi)^-1=sum_{t>=0}(T^pi)^t

exists. This proves the finite transient-resolvent fact under the actual hypotheses of the task.

In canonical order, write

P^pi = [[R^pi,0],[S^pi,T^pi]],

where R^pi is block diagonal with irreducible blocks R_i^pi. Let E_R^pi be block diagonal with blocks 1(g_i^pi)^T. The transient columns of the Cesaro limit are zero, since the transient powers decay. Its recurrent rows are the recurrent block limits. Finally, P^pi P_*^pi=P_*^pi determines its remaining block, giving

P_*^pi = [[E_R^pi,0],[N^pi S^pi E_R^pi,0]].

The source transient matrix is the full-state matrix bar T^pi=diag(0,T^pi). Consequently

d_mu^pi=mu^T P_*^pi,

delta_mu^pi=(mu_R^T,mu_T^T N^pi).

In particular, d_mu^pi is zero on T, but delta_mu^pi is generally not zero on R. Only the transient coordinates of delta enter the targets.

Expected cumulative reward from each initial state is sum_{t=0}^{H-1}(P^pi)^t r^pi. Thus its average converges and the public liminf definition gives J^pi=P_*^pi r^pi. It follows that P^pi J^pi=J^pi and P_*^pi J^pi=J^pi.

For completeness, the normalized Bellman definition of V is well posed. For M=P^pi and E=P_*^pi, put C=I-M+E. If Cx=0, multiplying by E gives Ex=0, and then (I-M)x=0. The range property of E implies Ex=x, so x=0. Thus C is invertible. The vector

V=C^-1(I-E)r^pi

satisfies EV=0, by multiplication by E, and (I-M)V=(I-E)r^pi=r^pi-J^pi. These equations also imply uniqueness. They identify the source relative value: for this V,

sum_{t=0}^{h-1}M^t(r^pi-J^pi)=V-M^h V,

whose Cesaro average over h converges to V-EV=V. Thus the normalized definition agrees with the source expected-sum definition, including periodic chains.

If T is empty, all transient blocks and products are omitted; bar T^pi=0 and delta_mu^pi=mu^T. No transient inverse estimate is needed in that case.

## Step 2: Recurrent contribution

Fix positive policies pi and pi'. Abbreviate M=P^pi, M'=P^pi', E=P_*^pi, J=J^pi, J'=J^pi', V'=V^pi', and define state vectors

q(s)=sum_a (pi(a|s)-pi'(a|s)) Q^pi'(s,a),

k(s)=sum_a (pi(a|s)-pi'(a|s)) K^pi'(s,a).

Since K^pi'=P J', we have k=(M-M')J'. By the source definition Q^pi'=r+PV'-K^pi',

q+k=r^pi-r^pi'+(M-M')V'.

The average reward J' is constant on each common recurrent class, because the corresponding Cesaro block of M' has identical rows. Every action stays in that class, so K^pi'(s,a)=J'(s) there, independently of a. Since both policies sum to one at each state, k is zero on R. As E has zero transient columns, Ek=0.

The normalized Bellman equation in particular gives r^pi'=J'+V'-M'V'. Therefore

E(q+k)
=E[r^pi-r^pi'+(M-M')V']
=E[r^pi-J'+(M-I)V']
=J-EJ'.

Here EM=E and Er^pi=J were used. Since Ek=0, this yields Eq=J-EJ'. Multiplication by mu^T gives exactly

mu^T Eq=sum_{s in R} d_mu^pi(s) sum_a (pi(a|s)-pi'(a|s)) Q^pi'(s,a).

## Step 3: Transient contribution

Decompose

J-J'=(J-EJ')+(E-I)J'=Eq+(E-I)J'.

On R, E_R^pi J'_R=J'_R because J' is constant on each common recurrent class. Thus (E-I)J' is zero on R. Using the canonical form from Step 1, its transient coordinates are

[(E-I)J']_T
=N^pi S^pi J'_R-J'_T
=N^pi[S^pi J'_R+(T^pi-I)J'_T]
=N^pi[(M-I)J']_T.

Since M'J'=J', the final vector is N^pi[(M-M')J']_T=N^pi k_T. Hence

mu^T(E-I)J'
=mu_T^T N^pi k_T
=sum_{s in T} delta_mu^pi(s) sum_a (pi(a|s)-pi'(a|s)) K^pi'(s,a).

Combining Steps 2 and 3 proves the performance-difference formula. This also proves the formula when T is empty, with the second sum equal to zero.

## Step 4: Continuity and the parameter differential

The block pattern is fixed on the positive-policy interior, and all transition blocks depend affinely on the policy. We establish their required regularity without invoking the specialized differentiability citations as black boxes.

For an irreducible n-by-n recurrent block R, let g be its stationary column vector, normalized by 1^Tg=1. Set

B=I-R^T+11^T.

If Bz=0, multiplication by 1^T gives n(1^Tz)=0. Then (I-R^T)z=0, so uniqueness of the stationary eigenspace from Step 1 gives z=cg. The zero-sum condition implies c=0. Thus B is invertible, and Bg=1 shows

g=B^-1 1.

The entries of a matrix inverse are ratios of polynomials with nonzero determinant denominator. It follows that g, and hence each recurrent Cesaro block, depends smoothly on the policy in relative coordinates. The same reasoning applies to N^pi=(I-T^pi)^-1. Equivalently, differentiating A A^-1=I gives D(A^-1)[H]=-A^-1 H A^-1. No interchange of differentiation and an infinite series is required.

The canonical expression for P_*^pi now implies smoothness of P_*^pi, d_mu^pi, delta_mu^pi, and J^pi=P_*^pi r^pi on the positive-policy interior. These arguments do not require aperiodicity or a uniform lower bound on policy probabilities over the entire interior.

Work in any local parameter coordinates at theta. Set pi=pi_theta and pi_h=pi_{theta+h}. Differentiability of the parameterization means

pi_h-pi=D pi_theta[h]+o(||h||).

Apply the performance-difference formula to (pi_h,pi), keeping Q^pi and K^pi fixed at the base policy. Since the state sets are common and the visitation measures are continuous, replacing d_mu^{pi_h} and delta_mu^{pi_h} by their values at pi creates an o(||h||) error: their differences are o(1), while pi_h-pi is O(||h||), and all sums are finite. Consequently

J_mu^{pi_h}-J_mu^pi
=sum_{s in R} d_mu^pi(s) sum_a D pi_theta(a|s)[h] Q^pi(s,a)
+sum_{s in T} delta_mu^pi(s) sum_a D pi_theta(a|s)[h] K^pi(s,a)
+o(||h||).

This establishes the full differential. Reading its coordinate coefficients gives the stated gradient formula. The proof also covers a single action, zero rewards, identical policies, multiple recurrent classes, and periodic recurrent classes. There are no unresolved proof obligations.
