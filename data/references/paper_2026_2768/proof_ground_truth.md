# Reference Proof

## Proof Structure

1. Recover the actual adaptive response density and identify its restriction to each selection stratum with a fixed-trajectory Gaussian reference density.
2. Use the finite stagewise and target partitions to compute the selection-consistent slice as a finite union of intervals, retaining exact boundary assignments.
3. Under the reference law, prove fixed-weight Gaussian independence and then derive the conditional truncated-normal law under the actual adaptive experiment.
4. Verify almost-sure positivity of the normalizer and give the finite-sum normal-CDF formula.
5. Establish boundary calibration and composite-null stochastic ordering, then integrate over null selection strata.

## Complete Proof

### 1. The observation experiment and its Gaussian reference laws

For a response vector u, let x_i(u) be the location produced at stage i by the deterministic recursion. It depends only on u_1,...,u_{i-1}; x_1 is fixed. The independent Gaussian observation errors imply that the actual joint response density is

h_f(u)=product_{i=1}^N phi_{sigma^2}(u_i-f(x_i(u))).

Indeed, conditional on the earlier responses, the next query is already determined and the next error remains independent N(0,sigma^2). Multiplication of these conditional densities gives the displayed joint density. In particular, this experiment is absolutely continuous.

Fix a possible selection output e=(tau,w), where tau=(a_1,...,a_N) and w is nonzero. Let S_e={u:E(u)=e} and mu_tau=(f(a_1),...,f(a_N)). Introduce a reference vector G_tau~N(mu_tau,Sigma), with Sigma=sigma^2 I_N. Its density is

g_tau(u)=product_{i=1}^N phi_{sigma^2}(u_i-f(a_i)).

For every u in S_e, x_i(u)=a_i for all i, and hence h_f(u)=g_tau(u). Consequently, for every measurable set A,

P_f(Y in A, E(Y)=e)=P(G_tau in A, E(G_tau)=e).

This is equality of restricted, unnormalized measures. It does not claim that Y is unconditionally Gaussian or that conditioning on a trajectory leaves an untruncated Gaussian law. The auxiliary Gaussian vector is used only to evaluate the restriction to S_e.

### 2. Finite geometry and exact set computation

There are finitely many queried histories because X and N are finite. For a fixed trajectory tau, the condition that stage n chooses its specified next location is a finite union of cells in R^n from the partition belonging to that fixed history. Lift each such cell to R^N by leaving later coordinates unrestricted. Intersect these finite unions over n=1,...,N-1. This gives a finite union of polyhedral cells for the full trajectory event. If N=1, the intersection over stages imposes no constraints.

The event eta(u)=w is the union of those finitely many target cells whose label is w. Intersecting this union with the trajectory event shows that S_e is a finite union of polyhedral cells. Both E and the selected residual are measurable; E has finite range.

Put v=w^T Sigma w>0, b=Sigma w/v, and P_w=I_N-bw^T. Then w^T b=1, w^T P_w=0, and P_w b=0. For q in the range of P_w, every vector u with P_w u=q is uniquely

u=q+bz, where z=w^T u.

Substitute u=q+bz into each linear equality, strict inequality, and weak inequality defining each cell of S_e. A resulting scalar constraint has the form c z < d, c z <= d, or c z=d. When c=0 it is either automatic or inconsistent. Otherwise it gives a bound or an equality, with the appropriate endpoint assignment. A finite conjunction therefore gives an interval, possibly empty, unbounded, or a singleton. Taking the finite union over cells gives exactly

Z_{e,q}={z:E(q+bz)=e}.

Thus the set is computed by finitely many scalar linear-constraint operations and interval unions. Boundary assignments are retained for exact equality of sets. Neither replacing a TPE trajectory event by one observed quantile partition nor discarding tie decisions is required by this general construction.

### 3. Gaussian independence and the selected conditional law

Under the reference law, write T_w=w^T G_tau and Q_w=P_w G_tau. They are jointly Gaussian, with

E[T_w]=delta=w^T mu_tau, Var(T_w)=v,

Cov(Q_w,T_w)=P_w Sigma w=Sigma w-bv=0.

The joint Gaussian characteristic function consequently has a block-diagonal covariance exponent and factors into the characteristic functions of T_w and Q_w. This proves independence, including when Q_w is a singular Gaussian vector. Thus T_w~N(delta,v) independently of Q_w.

Let nu_{tau,w} denote the probability law of Q_w under this reference distribution. Combining independence, the affine representation, and the equality of restricted measures from Step 1 gives the actual joint subprobability measure on the stratum e:

P_f(E(Y)=e, R(Y) in dq, w^T Y in dz)
 = nu_{tau,w}(dq) phi_v(z-delta) 1{z in Z_{e,q}} dz.

Here R(Y)=Q_w(Y) on E(Y)=e. This identity is understood by integration over measurable sets, so no ambient Lebesgue density for the residual is asserted.

Define

D_delta(e,q)=integral_{Z_{e,q}} phi_v(z-delta) dz.

The distribution of R on the stratum e is D_delta(e,q) nu_{tau,w}(dq). Hence D_delta(e,R)>0 almost surely on that stratum. For every q, strict positivity of all normal densities implies that D_delta(e,q)>0 if and only if Z_{e,q} has positive Lebesgue measure, equivalently D_0(e,q)>0. There are finitely many selection outputs, and eta(Y) is nonzero almost surely. It follows that the p-value's denominator is positive almost surely in the actual experiment. The exceptional-input convention therefore does not affect any probability claim.

Dividing the joint subprobability measure by its residual marginal gives, for almost every observed conditioning pair (e,q),

f_delta(z | E=e,R=q)
 = phi_v(z-delta) 1{z in Z_{e,q}} / D_delta(e,q).

This is exactly the N(delta,v) distribution truncated to Z_{e,q}. Its parameters delta and v are those of the untruncated normal; they are not asserted to equal the conditional mean and variance. Once e and q are fixed, the formula depends on the objective only through delta=w^T mu_tau. The nuisance-dependent factor in nu_{tau,w} has canceled.

### 4. Exact evaluation

Write Z_{e,q} as a finite disjoint union of intervals with endpoints (a_j,b_j), keeping endpoint inclusion flags separately. Singletons contribute zero probability. Let Phi be the standard normal CDF, with Phi(-infinity)=0 and Phi(infinity)=1. Set s=sqrt(v). Endpoint inclusion does not affect integrals against the continuous normal density. The denominator is

D_0(e,q)=sum_j [Phi(b_j/s)-Phi(a_j/s)].

For observed t, the numerator is

sum_{j:b_j>t} [Phi(b_j/s)-Phi(max{a_j,t}/s)].

Thus their ratio is an exact finite expression in normal-CDF evaluations. An empty sum is zero. Infinite endpoints use the stated CDF conventions. This establishes the requested computation without a claim of finite-precision numerical exactness or a polynomial-time complexity bound.

### 5. Conditional validity

Fix an admissible conditioning pair (e,q), and abbreviate its truncation set by Z. For delta_1>delta_0, the two conditional densities satisfy

f_{delta_1}(z)/f_{delta_0}(z)
 = C exp((delta_1-delta_0)z/v), for z in Z,

where C>0 is independent of z. The ratio r(z) is increasing and has expectation one under f_{delta_0}.

For completeness, this gives stochastic ordering directly. If g is a bounded increasing function and U,U' are independent with density f_{delta_0}, then

E_{delta_1}[g(U)]-E_{delta_0}[g(U)]
 = Cov_{delta_0}(g(U),r(U))
 = (1/2) E[(g(U)-g(U'))(r(U)-r(U'))] >= 0.

The expectations are finite because g is bounded and E[r(U)]=1. In particular, upper-set probabilities increase with delta. This argument does not require Z to be connected.

Under delta=0, the conditional distribution is absolutely continuous, even when Z has gaps. Its CDF F_0 is continuous, with limits zero and one. Its upper-tail function is S_0(t)=1-F_0(t). The probability-integral transform gives F_0(T) uniform on (0,1): for each a in (0,1), continuity provides an a-quantile, and any interval on which F_0 is constant has probability zero, yielding P(F_0(T)<=a)=a. Therefore S_0(T) is also uniform. In particular,

P_0(S_0(T)<=alpha)=alpha.

The set {t:S_0(t)<=alpha} is an upper set because S_0 is nonincreasing. Applying the proved stochastic ordering with delta<=0 and boundary value zero yields

P_delta(S_0(T)<=alpha)<=P_0(S_0(T)<=alpha)=alpha.

On the stratum, p_sel(Y)=S_0(w^T Y). This proves the requested conditional rejection inequality almost surely whenever the selected effect is nonpositive. The boundary-normal family is used as a scalar reference family; its construction does not require independently varying the objective values while preserving every equality imposed by repeated query locations.

### 6. Marginal selected-null control

Let B_f={Delta_sel(Y)<=0}. The selected effect is a function of E(Y), because both the trajectory and weight are components of that output. Thus B_f is measurable with respect to E(Y). Let J=1{p_sel(Y)<=alpha}. The conditional result states E_f[J | E(Y),R(Y)]<=alpha almost surely on B_f. Therefore

P_f(p_sel(Y)<=alpha, B_f)
 = E_f[1_{B_f} E_f[J | E(Y),R(Y)]]
 <= alpha P_f(B_f).

If P_f(B_f)>0, division gives P_f(p_sel(Y)<=alpha | B_f)<=alpha. If P_f(B_f)=1, this is the ordinary marginal rejection bound P_f(p_sel(Y)<=alpha)<=alpha. If P_f(B_f)=0, the joint inequality is zero on both sides and no conditional probability given B_f is asserted.

All steps are finite-sample statements for every fixed objective f and every alpha in (0,1). No unresolved proof obligation remains.
