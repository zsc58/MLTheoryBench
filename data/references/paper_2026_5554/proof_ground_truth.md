# Reference Proof

## Contract and Proof Obligations

The ideal trajectory lies in M. The stability trajectory is a separate, prescribed rank-r trajectory in the stated neighborhood of M; its driving matrix G is not identified with the least-squares gradient G_ls(W). Both compact polar factors in the stability statement are taken on rank-r matrices with their stated positive lower singular-value bounds. All differential comparisons are made at the same current W, not between independently evolving trajectories.

The obligations are: the ideal singular-value rates and norm contraction; the exact normalized-functional derivative and its sign interpretation; strict opposite ordering of q; attainment and uniqueness of the unconstrained fixed-radius spectral minimum; the two pointwise stability estimates; the compact-polar perturbation bound; and exactness under equality of polar factors. The rank/gap-preserving interval is a hypothesis, not a conclusion requiring a quantitative existence time.

The standard-independent singular-value differential used below is: if sigma_i(A)>0 is a simple singular value with unit singular vectors u_i,v_i, then D sigma_i(A)[H]=u_i^T H v_i. Positive simplicity separates sigma_i(A)^2 from every other eigenvalue of AA^T, including zero. Thus the local positive singular-value branch is differentiable. Differentiating A v_i=sigma_i u_i and using the differentiated unit-vector identities proves the displayed differential formula. These hypotheses hold for every singular value differentiated below. The external material record theory_015 records this result. The compact-polar inequality associated with theory_014 is proved directly in step_007, so no unverified extension of a square full-rank result is needed.

## Complete Proof

### step_001: Projection geometry

Because X has full row rank, XX^dagger=I_p. Consequently P_perp=I_m-X^dagger X is the orthogonal projector onto ker X, acting separately on each column of a matrix. It is symmetric and idempotent. Since p<m, its range is nonzero and its operator norm is one.

For W in M and an arbitrary matrix H, the affine set M equals W plus the matrix space {K:XK=0}. Therefore

Pi_M(W+H)=W+P_perp H.

In particular, for a time increment h>0,

Pi_M(W-h eta P(W))=W-h eta P_perp P(W).

Dividing the increment by h gives the supplied ideal vector field. This projection calculation is context, not an additional public proof target.

### step_002: Ideal singular-value dynamics and norm contraction

Write W=U diag(sigma_1,...,sigma_r)V^T. The positive singular values are simple, so the audited differential formula gives

dot sigma_i=u_i^T dot W v_i=-eta u_i^T P_perp U V^T v_i=-eta u_i^T P_perp u_i.

Since P_perp is an orthogonal projector,

alpha_i=u_i^T P_perp u_i=||P_perp u_i||_2^2 in [0,1].

Constant rank gives ||W||_F^2=sum_i sigma_i^2. Hence

d||W||_F^2/dt=2 sum_i sigma_i dot sigma_i=-2eta sum_i alpha_i sigma_i<=0.

### step_003: Normalization and the exact flattening criterion

Put s_i=tilde sigma_i and a=sum_i alpha_i s_i. Since rho>0,

dot rho=-eta a,    dot s_i=(eta/rho)(s_i a-alpha_i).

For R_pw(s)=-sum_{i ne j}log(s_i+s_j), differentiation in the positive orthant gives partial R_pw/partial s_i=-2S_i. Thus

d tilde R_pw/dt=(2eta/rho)[sum_i alpha_i S_i-a sum_i s_i S_i].

Every unordered pair contributes

s_i/(s_i+s_j)+s_j/(s_i+s_j)=1

to sum_i s_i S_i. Therefore sum_i s_i S_i=C=binom(r,2), and

d tilde R_pw/dt=(2eta/rho)sum_i alpha_i(S_i-C s_i)=(2eta/rho)sum_i alpha_i q_i.

Because 2eta/rho>0, the derivative is nonpositive exactly when sum_i alpha_i q_i<=0. This proves flattening in the definition supplied in the task; it does not assert any additional majorization or convergence property.

### step_004: Strict opposite ordering

If s_i>s_k, the terms involving the pair {i,k} cancel when S_i-S_k is formed. Consequently

q_i-q_k=sum_{j not in {i,k}}[1/(s_i+s_j)-1/(s_k+s_j)]-C(s_i-s_k).

Every displayed reciprocal difference is negative, and the last term is strictly negative because C>0. Thus q_i<q_k. This argument applies to any unequal coordinates of a positive spectrum; no derivative along the sphere is being asserted.

### step_005: Fixed-radius minimization

Define Phi(sigma)=R_pw(sigma)/2=-sum_{i<j}log(sigma_i+sigma_j). Its Hessian quadratic form is

v^T Hess Phi(sigma) v=sum_{i<j}(sigma_i+sigma_j)^(-2)(v_i+v_j)^2.

All weights are positive. If this form vanishes, then v_i+v_j=0 for all pairs. For r>=3, the pairs (1,2), (1,3), and (2,3) force v_1=v_2=v_3=0; the remaining pairs force every other coordinate to vanish. Thus Phi is strictly convex on the positive orthant.

To establish attainment as well as uniqueness, start with any positive sigma satisfying ||sigma||_2=c, rather than assuming a minimizer exists. Let mu=(sum_i sigma_i)/r and let bar_sigma=mu(1,...,1), the average of all coordinate permutations of sigma. Permutation symmetry and convexity give

Phi(bar_sigma)<=Phi(sigma).

Cauchy--Schwarz gives ||bar_sigma||_2<=c, with equality exactly when sigma is constant. Define t=c/||bar_sigma||_2>=1. Then t bar_sigma=(c/sqrt(r))(1,...,1), and

Phi(t bar_sigma)=Phi(bar_sigma)-C log t<=Phi(bar_sigma)<=Phi(sigma).

If sigma is not constant, then t>1 and the first inequality is strict. The positive flat spectrum therefore attains the global minimum and is its unique spectral minimizer. This also handles the fact that the positive portion of the sphere is not closed: existence is established by direct comparison with an explicit feasible spectrum, not by compactness. The functional depends only on singular values, so every allowed choice of singular-vector frames gives the same value. No constraint XW=Y is imposed in this variational problem.

### step_006: Stability at the current actual matrix

At a fixed time, let E=F-F_0. Orthogonal-projector nonexpansiveness gives

||E||_F=eta ||P_perp(P(G)-P(W))||_F<=eta delta_P(t).

Let Z_i=u_i v_i^T. These matrices are orthonormal in the Frobenius inner product. Define e_i=<Z_i,E>_F. The singular-value differential gives

dot sigma_i=-eta alpha_i+e_i,    |e_i|<=||E||_F,

and orthonormality gives sum_i e_i^2<=||E||_F^2. Thus the first estimate holds with C_1=1.

The algebraic identity u_i^T F_0 v_i=-eta alpha_i does not require XW=Y. Also,

W+hF_0=(U diag(sigma)-h eta P_perp U)V^T

has rank r for sufficiently small h, because its r-column factor has full column rank at h=0. Thus the self-polar directional comparison is legitimate on the rank-r stratum even when the actual W is only near M.

For the normalized functional as a function of sigma, write s=sigma/rho. Its normalization differential is

D_sigma s=(I_r-ss^T)/rho.

The identity s^T S=C established in step_003 shows that q=(I_r-ss^T)S. Hence its spectral gradient is

g:=nabla_sigma R_pw(sigma/||sigma||_2)=-(2/rho)(I_r-ss^T)S=-(2/rho)q.

Because ||s||_2=1, I_r-ss^T is an orthogonal projector. Moreover, each s_i+s_j>=2 sigma_min/rho, so

S_i<=rho(r-1)/(2 sigma_min),

||g||_2<=(2/rho)||S||_2<=sqrt(r)(r-1)/sigma_min.

The actual spectral rate vector is -eta alpha+e. Applying the chain rule therefore gives

d tilde R_pw/dt=(2eta/rho)sum_i alpha_i q_i+g^T e.

It follows that

|d tilde R_pw/dt-(2eta/rho)sum_i alpha_i q_i|

<=||g||_2 ||e||_2

<=sqrt(r)(r-1) eta delta_P(t)/sigma_min(t)

<=sqrt(r)(r-1) eta bar_delta_P/sigma_min(t).

Thus C_2=sqrt(r)(r-1) suffices. These constants depend only on r, which is stronger than the permitted dependence. The lower singular-value and gap hypotheses ensure the stated trajectory domain and differential regularity; no additional numerical gap dependence is necessary in these first-derivative estimates.

Both polar factors have Frobenius norm sqrt(r), so delta_P(t)<=2sqrt(r) and bar_delta_P is finite. All estimates are uniform on the prescribed interval. They do not establish that polar misalignment alone preserves rank or determines a positive interval length. In particular, the ancillary horizon expression in source L000371 is not used: the theorem's interval is already assumed to have the required rank and gap properties.

### step_007: Compact-polar perturbation and exactness

We verify the needed standard-independent polar bound directly, including possible ambient zero singular values. At a fixed time set A=G(t), B=W(t), and d=min(delta_G,delta_W)>0. Form the real symmetric matrices

H_A=[[0,A],[A^T,0]],    H_B=[[0,B],[B^T,0]].

Define sign(H) by applying sign(lambda) to each eigenvalue, with sign(0)=0. The compact SVD of A gives eigenvectors (u_i,v_i)/sqrt(2) and (u_i,-v_i)/sqrt(2) with eigenvalues sigma_i(A) and -sigma_i(A); the remaining eigenvalues are zero. Consequently

sign(H_A)=[[0,P(A)],[P(A)^T,0]],

and the same identity holds for B.

Choose orthonormal eigenbases {a_i} and {b_j} of H_A and H_B, with eigenvalues lambda_i and mu_j. Every nonzero eigenvalue has absolute value at least d. For every such pair, including pairs involving zero,

|sign(lambda_i)-sign(mu_j)|<=(2/d)|lambda_i-mu_j|.

Indeed, equal signs give zero on the left; one zero gives |lambda_i-mu_j|>=d; and opposite nonzero signs give |lambda_i-mu_j|>=2d. The entries in the two eigenbases satisfy

a_i^T(sign(H_A)-sign(H_B))b_j=(sign(lambda_i)-sign(mu_j))a_i^T b_j,

a_i^T(H_A-H_B)b_j=(lambda_i-mu_j)a_i^T b_j.

Squaring the entrywise inequality and summing, using orthogonal invariance of the Frobenius norm, yields

||sign(H_A)-sign(H_B)||_F<=(2/d)||H_A-H_B||_F.

Each block-matrix norm is sqrt(2) times the corresponding rectangular-matrix norm. Cancelling sqrt(2) proves

||P(G(t))-P(W(t))||_F<=2||G(t)-W(t)||_F/min(delta_G,delta_W).

Finally, equality P(G(t))=P(W(t)) makes delta_P(t)=0 and F=F_0 at that time. If the equality holds throughout the interval, all displayed ideal spectral identities hold exactly along the actual flow. Shared compact singular frames with positive diagonal singular-value matrices imply equality of polar factors, as in the source definition, but that sufficient condition is not identified with a necessary condition.

Every theorem-critical obligation is now closed. No quantitative horizon guarantee, probabilistic buffer nondegeneracy claim, or result from the unselected discrete-step or noise branches is required.
