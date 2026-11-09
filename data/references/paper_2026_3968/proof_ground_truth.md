# Reference Proof

## Obligations and permitted background

The obligations are: (1) well-posedness of the regularized Dirichlet system; (2) identification with the policy infimum and the optimal feedback; (3) a gradient bound uniform over all positive temperatures; (4) the quantified obstacle estimate with the specified constant; (5) both comparisons with the classical viscosity solution; and (6) the stated asymptotic rate. All six are closed below.

We use the following standard independent facts. For a scalar uniformly elliptic operator with C^1 coefficients on a bounded smooth domain and r>0, the zero-boundary equation (r-L)v=g has a unique solution for bounded continuous g, with W^{2,p} estimates for every finite p. Its resolvent is compact as a map from bounded subsets of C into C of the closure. Locally Hölder right-hand sides give interior C^{2,alpha} regularity. A continuous compact self-map of a closed convex bounded set has a fixed point. We also use the scalar maximum principle, smooth approximation of C^1 coefficients, and localized Ito and jump-compensation formulas. For a switching diffusion the generator acting on a vector u is L_i u_i+sum_{j!=i}q_ij(u_j-u_i); discounting contributes -r u_i. These hypotheses hold here because the domain is smooth, a is uniformly elliptic, the coefficients are C^1 and bounded on the closure, r>0, and each admissible policy has bounded rates. No specialized switching regularity theorem is used to prove the gradient estimate. The classical viscosity characterization and its continuation-region C^2 regularity are the source setup.

Write u_i=V_i^lambda and
F_i^lambda(u)=L_i u_i+f_i-r u_i+lambda sum_{j!=i}(1-exp((u_i-u_j-G_ij)/lambda)).

## 1. Comparison, existence, and the stated barriers

For classical sub- and supersolutions, system comparison follows directly. If v_i-u_i has a positive maximum M over all components and the closed domain, at its interior maximizing component i we have v_i-v_j>=u_i-u_j for every j, L_i(v_i-u_i)<=0, and the difference of the nonlinear terms in F_i is nonpositive. Consequently F_i(v)-F_i(u)<=-rM<0, contrary to the subsolution inequality F_i(v)>=0 and supersolution inequality F_i(u)<=0. The same proof applies to nondecreasing truncated exponentials and to comparison on a boundary strip.

Fix lambda>0. For N>0 use h_N(t)=min(exp(t),exp(N)) and replace each exponential by h_N. This is a bounded globally Lipschitz nondecreasing function. For a continuous vector v define T(v)_i by
(r-L_i)T(v)_i=f_i+lambda sum_{j!=i}(1-h_N((v_i-v_j-G_ij)/lambda)),
with zero boundary data. The right-hand side has a bound independent of v. Scalar resolvent estimates show that T is continuous, compact, and maps a sufficiently large closed sup-norm ball into itself. The compact fixed-point theorem gives a solution. Its W^{2,p} regularity first gives C^{1,alpha} regularity; the locally Hölder right-hand side then gives C^2 regularity in the domain.

The vector zero is a subsolution, because f_i>=0 and h_N(-G_ij/lambda)=exp(-G_ij/lambda)<1. The constant vector H_lambda=(C_coef+(m-1)lambda)/r is a supersolution, since h_N>=0. Comparison gives 0<=u_i^N<=H_lambda. Choose N>H_lambda/lambda. Every argument (u_i^N-u_j^N-G_ij)/lambda is then below N, so the cutoff is inactive. This gives an untruncated solution and the requested barriers. The maximum-component-difference argument gives uniqueness.

## 2. Hamiltonian minimization and verification

For a real number c and q>=0, with 0 log 0=0,
inf_q {cq+lambda(q log q-q+1)}=lambda(1-exp(-c/lambda)),
and the unique minimizer is q=exp(-c/lambda). Apply this with c=u_j-u_i+G_ij. For every admissible policy q,
L_i u_i-r u_i+sum_{j!=i}q_ij(u_j-u_i)+f_i+sum_{j!=i}q_ij G_ij+lambda sum_{j!=i}D(q_ij|1)>=0.
Equality holds for q_ij=exp((u_i-u_j-G_ij)/lambda). Since u is bounded, this feedback is bounded for each fixed lambda and belongs to the admissible class.

Apply discounted Ito to u_{I_t}(X_t), stopped at time T and before exiting compact subdomains. Taking expectations and using the displayed inequality yields u_i(x) no greater than expected accumulated cost plus the discounted terminal value. Localization is removed using bounded u, bounded rates, and the fixed-lambda elliptic regularity. At boundary exit the terminal value is zero, while its contribution at T is bounded by H_lambda exp(-rT). Each policy's running integrand is bounded, so passage to T tending to infinity is justified. Hence u_i<=J_i^lambda(q). For the Gibbs policy every inequality is equality, giving u_i=J_i^lambda(q^lambda)=V_i^lambda.

For completeness, the expected transition-cost sum in the source equals the intensity-cost integral by jump compensation. The ancillary KL interpretation uses the joint path law stopped at S=tau_O wedge zeta, where zeta is an independent exponential time of rate r. The bounded-intensity likelihood formula gives
log(dP^q/dP^0)|_S=sum_{i!=j}integral_0^S log q_ij(X_t) 1_{I_{t-}=i} dN_t^{ij}-integral_0^S sum_{j!=I_t}(q_{I_tj}(X_t)-1)dt.
Taking controlled expectation and compensating the jump counts gives E^q integral_0^S sum_j D(q_{I_tj}|1)dt. Independent killing converts this to E^q integral_0^{tau_O}exp(-rt)sum_j D(q_{I_tj}|1)dt. Zero rates are interpreted by the standard zero-rate likelihood convention and 0 log 0=0. The likelihood must be inside a logarithm in the KL expectation. This interpretation is not needed as an additional verification assumption.

## 3. A gradient bound uniform for all lambda>0

This step repairs the source's faulty exponential-weight calculation while retaining its Bernstein argument.

### Uniform value and boundary-gradient bounds

Set K_0=C_coef+max_i sum_{j!=i}G_ij and B=K_0/r. For G>0,
lambda(1-exp(-G/lambda))<=G.
Therefore the constant vector B is a supersolution for every lambda, and 0<=u_i<=B uniformly in lambda.

Let rho be distance to the boundary in a sufficiently thin smooth boundary strip 0<=rho<=epsilon. There |D rho|=1, the Hessian of rho is bounded, and L_i rho is uniformly bounded. For sufficiently large fixed k,
L_i[A(1-exp(-k rho))]=A exp(-k rho)[k L_i rho-(k^2/2)D rho^T a D rho]
 is strictly negative throughout the strip. Choose A, independently of lambda, large enough that this expression is at most -K_0 and A(1-exp(-k epsilon))>=B. The common vector with component s=A(1-exp(-k rho)) is then a supersolution, since its switching contribution is at most sum_j G_ij. Boundary-strip comparison gives 0<=u_i<=s. Fixed-lambda Dirichlet regularity gives C^1 regularity up to the boundary. Tangential derivatives vanish; with the outward normal n, -Ak<=D_n u_i<=0. Thus the boundary gradients are bounded uniformly in lambda.

### Interior Bernstein inequality

Initially take smooth coefficients so differentiation is justified. Put p_i=Du_i, w_i=|p_i|^2/2, and W_ij=exp((u_i-u_j-G_ij)/lambda). Differentiating the equation and applying the product rule gives
L_i w_i=(1/2)a^{alpha beta}u_{i,alpha gamma}u_{i,beta gamma}-(1/2)(partial_gamma a^{alpha beta})u_{i,alpha beta}u_{i,gamma}-(partial_gamma b_i^alpha)u_{i,alpha}u_{i,gamma}+r|p_i|^2-Df_i dot p_i+sum_{j!=i}W_ij p_i dot(p_i-p_j).
Ellipticity and Young's inequality absorb the mixed Hessian term into half the positive Hessian term. Also p_i dot(p_i-p_j)>=w_i-w_j. Consequently, for finite constants A_0,A_1 independent of lambda,
L_i w_i>=-A_0 w_i-A_1+sum_{j!=i}W_ij(w_i-w_j).

Choose K>0 so that 2K sigma_0-A_0>=1, and define on [0,B]
psi(t)=K((2B+1)t-t^2),   z_i=w_i-psi(u_i).
Here psi>=0, psi'>=K>0, and psi''=-2K. Suppose z_i attains the maximum over all components and the closed domain at an interior point. At this point,
w_i-w_j>=psi(u_i)-psi(u_j)>=psi'(u_i)(u_i-u_j),
where the last inequality follows from concavity. Since
L_i u_i=r u_i-f_i+lambda sum_{j!=i}(W_ij-1),
the chain rule implies at that maximum
L_i z_i>=(2K sigma_0-A_0)w_i-A_1-psi'(u_i)(r u_i-f_i)+psi'(u_i)sum_{j!=i}[W_ij(u_i-u_j)-lambda(W_ij-1)].
The last bracket is exactly
G_ij W_ij+lambda D(W_ij|1)>=0.
Using f_i>=0, u_i<=B, and psi'<=K(2B+1), we obtain
0>=L_i z_i>=w_i-A_1-K(2B+1)rB.
Thus w_i is bounded at an interior maximizing point of z. At a boundary maximizing point, z_i=w_i is bounded by the boundary-gradient estimate. Finally w_i=z_i+psi(u_i)<=max z+max_{[0,B]}psi, giving a lambda-independent bound everywhere.

For C^1 coefficients, approximate b_i, sigma, and f_i by smooth data with uniform C^1 bounds, preserved nonnegativity, and a fixed positive ellipticity lower bound. For each fixed lambda the uniform value bound makes the equation's right-hand side bounded. Scalar W^{2,p} estimates yield subsequential C^1 convergence; the limit is the unique solution already constructed. The uniform gradient estimates pass to this limit. Enlarge the resulting constant if necessary and denote it C_Lip. Its dependencies are only the fixed data, never lambda.

## 4. Quantified obstacle violation

Let C_up=2C_coef(1+C_Lip). It is positive: C_coef also bounds the nondegenerate diffusion. Take 0<lambda<min(C_coef,C_up), and set delta=lambda log(C_up/lambda)>0.

For i!=j let w=u_i-u_j. Because a is the same in both modes, subtraction gives
L_i w=r w+f_j-f_i-(b_i-b_j) dot Du_j+lambda(W_ij-W_ji)+lambda sum_{k!=i,j}(W_ik-W_jk).
If w>G_ij+delta somewhere, its maximum is attained in the interior because w=0 on the boundary. At that maximum L_i w<=0, W_ij>C_up/lambda, and W_ji<=1. For every k distinct from i,j,
W_ik/W_jk=exp((w-G_ik+G_jk)/lambda)>1
by the strict triangle inequality. Moreover f_j-f_i>=-C_coef and -(b_i-b_j) dot Du_j>=-2C_coef C_Lip. Hence
0>=L_i w>r w-C_coef-2C_coef C_Lip+C_up-lambda=r w+C_coef-lambda>0,
a contradiction. Therefore u_i<=u_j+G_ij+delta. This proof explicitly retains the reverse-exponential contribution that the source dropped.

## 5. Upper comparison with the classical value

The correctly signed variational inequality gives the pointwise obstacle inequalities V_i^*<=V_j^*+G_ij and the viscosity inequality L_i V_i^*+f_i-rV_i^*>=0.

If M=max_{i,x}(V_i^*-u_i)>0, the maximum occurs at an interior point of some component i. The smooth function u_i+M touches V_i^* from above there. The viscosity subsolution condition for the differential branch gives L_i u_i+f_i-rV_i^*>=0. The obstacle inequalities make every exponential formed from V^* at most one, so
L_i u_i+f_i-rV_i^*+lambda sum_{j!=i}(1-exp((V_i^*-V_j^*-G_ij)/lambda))>=0.
But at this maximum V_i^*-V_j^*>=u_i-u_j, so the left side is at most F_i^lambda(u)-rM=-rM<0. Contradiction. Thus V_i^*<=u_i. This argument does not assume global C^2 regularity of V^*.

## 6. Lower comparison and the rate

For the same small-temperature regime put
kappa=min_{i!=j}G_ij/(G_ij+delta),
iota=((1-kappa)C_coef+(m-1)lambda)/r.
Then 0<kappa<=1 and kappa(G_ij+delta)<=G_ij.

Suppose l=min_{i,x}(V_i^*-kappa u_i+iota)<0. The minimum occurs in the interior, since the boundary value of this difference is iota>=0. At a minimizing component i and point z in its strict continuation region, V_i^* is C^2 and L_i V_i^*=rV_i^*-f_i. Therefore
0<=L_i(V_i^*-kappa u_i)=r(l-iota)-(1-kappa)f_i-kappa lambda sum_{j!=i}(W_ij-1)
<=r(l-iota)+(1-kappa)C_coef+(m-1)lambda=rl<0,
a contradiction.

If z is not in that continuation region, some j!=i satisfies V_i^*(z)=V_j^*(z)+G_ij. The obstacle estimate gives
V_j^*(z)-kappa u_j(z)+iota
=l+kappa(u_i(z)-u_j(z))-G_ij
<=l+kappa(G_ij+delta)-G_ij<=l.
By minimality it equals l, so the same point in component j is also minimizing. Repeat. Either a continuation component is reached, giving the preceding contradiction, or a component repeats. In the latter case the intervening obstacle equalities imply that the sum of strictly positive switching costs around a cycle is zero, impossible. Thus
kappa u_i-iota<=V_i^*<=u_i.

Let G_min=min_{i!=j}G_ij>0. Then
1-kappa=max_{i!=j}delta/(G_ij+delta)<=delta/G_min.
Using either the stated value bound for small lambda or the stronger uniform bound B proved privately above,
0<=u_i-V_i^*<=(1-kappa)B+((1-kappa)C_coef+(m-1)lambda)/r.
Because delta=lambda log(C_up/lambda)=O(lambda log(1/lambda)), this is at most C lambda log(1/lambda) for all sufficiently small lambda, uniformly in i and x. The constants depend only on the fixed data. This closes all six obligations.
