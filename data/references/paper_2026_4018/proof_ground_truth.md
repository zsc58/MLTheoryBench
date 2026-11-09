# Reference Proof

## Obligations and source-local corrections

We establish well-defined constrained states and weights, uniform local coercivity, the three limiting vector fields and their loss inequalities, quantitative residual and velocity bounds, and finally trajectory confinement, global forward existence, and convergence. The finite-dimensional Implicit Function Theorem is used with its hypotheses stated and checked below.

Two source-local corrections are relevant in addition to the recorded CL gradient/dissipation wording correction. Neighborhood coercivity constants must be allowed to be strictly smaller than the pointwise constants at the reference point. Also, if beta denotes the CL output-multiplier derivative, its sign is beta=-Dr; the physical response is y=-RQ beta=RQDr. Neither correction changes the physical learning field or the local convergence target.

## 1. Constrained linear algebra and domains

Write A= Lhat and Qhat=[Q;0]. For a vector in the kernel of A, the equations are Lz+P alpha=0 and P^T z=0. Taking the inner product with z gives z^T Lz=0. Positive semidefiniteness and the input-kernel assumption give z=0, and full column rank of P then gives alpha=0. Thus A is invertible. Its inverse and the free state are smooth on a neighborhood of k_* inside the positive-conductance domain.

Let R be the N by N upper-left block of A^{-1}. For any f, the vector z=Rf solves Lz+P alpha=f, P^T z=0. Hence f^T Rf=z^T Lz>=0. Symmetry of A gives symmetry of R. Moreover, f^T Rf=0 implies z=0 and f lies in range(P); conversely f in range(P) gives z=0. Thus R is positive semidefinite with kernel range(P).

Let J(k)=D_k r(k). Since P^T x_0=v, we have P^T partial_e x_0=0. If Qu lies in range(P), then J(k_*)^T u=0. Full row rank of J(k_*) forces u=0. It follows that B=Q^T RQ=Qhat^T A^{-1}Qhat is positive definite for nonzero output dimension. In particular D=B^{-1} exists and is smooth. This also shows that [P,Q] has full column rank. The fully constrained KKT matrix

K=[[L,P,Q],[P^T,0,0],[Q^T,0,0]]

is invertible: the same energy argument kills its state component, and independence of [P,Q] kills its multiplier components. All clamped problems therefore have unique states and multipliers locally, for every sufficiently small nudge. On a sufficiently small compact neighborhood, D has uniform eigenvalue bounds

0<d_- <= lambda_min(D(k)) <= lambda_max(D(k)) <= d_+<infinity.

If O=0, the residual and adjoint multiplier are empty vectors. Every nudged minimizer equals its reference state and all three vector fields vanish. The unique zero-dimensional linear map is invertible, all losses are zero, and the conclusion follows by taking a small positive-conductance neighborhood. We henceforth treat O>0. This also guarantees a nonempty active set under the rank hypothesis.

## 2. Residual Jacobian and uniform coercivity

Set b_e=d_e^T x_0 and a_e=Qhat^T A^{-1} d_hat_e in R^O. Differentiating A hat x_0=(0,v) gives

partial_e hat x_0=-A^{-1} d_hat_e b_e,

so the e-th column of J is -b_e a_e. Consequently, for every u in R^O,

||J^T u||^2=sum_e b_e^2(a_e^T u)^2.

At k_* the zero-drop terms vanish, leaving exactly

||J(k_*)^T u||^2=||Lambda^{1/2} Dprime^T A(k_*)^{-1} Qhat u||^2.

This verifies the equivalence of the stated rank conditions. Continuity of the fixed-size matrix J and full row rank yield a neighborhood and a constant kappa>0 such that

||J(k)^T u||^2>=kappa||u||^2.

All matrices and state-dependent coefficients used below have bounded norms after restricting to a compact subneighborhood. One must not argue that a varying active-edge matrix has a fixed size. Alternatively, one can retain only the edges active at k_*; their drops remain nonzero nearby and their contribution provides a lower bound for the full sum.

For clarity about the source's rate constants, if lambda_0 and c_0 are its pointwise active-edge constants, then sigma_min(J(k_*))^2>=lambda_0 c_0^2. For any fixed theta in (0,1), continuity permits kappa=theta lambda_0 c_0^2 after shrinking. It does not in general permit the unchanged pointwise product throughout a neighborhood.

## 3. EP

Differentiation of the EP constrained equations in eta, with k and its residual fixed, gives a state response y_EP=RQ r. Since partial_e G(x;k)=(d_e^T x)^2/2 with x held fixed, the limiting update is

(F_EP)_e=b_e d_e^T y_EP=b_e a_e^T r.

Thus F_EP=-J^T r. With Phi=||r||^2/2,

dot Phi=r^T J F_EP=-||J^T r||^2<=-2 kappa Phi.

As long as the trajectory remains in the chosen neighborhood,

||r(k(t))||<=exp(-kappa t)||r(k(0))||,

and boundedness of J gives ||F_EP||<=C_EP||r||.

## 4. CL, including the cubic remainder

The CL nudge derivative solves

Ly+P alpha+Q beta=0, P^T y=0, Q^T y=r.

Eliminating the input constraints gives y=-RQ beta, so beta=-Dr and y=RQDr. Therefore

(F_CL)_e=b_e a_e^T Dr,

or F_CL=-J^T Dr.

Differentiate B=Qhat^T A^{-1}Qhat. Since partial_e A=d_hat_e d_hat_e^T,

partial_e B=-a_e a_e^T,

partial_e D=D a_e a_e^T D.

For Phi_D=r^T Dr/2, differentiation along CL gives

dot Phi_D=-||J^T Dr||^2+(1/2)sum_e b_e(a_e^T Dr)^3.

This is update dissipation, not an assertion that CL is exact gradient flow of Phi_D. Uniform bounds on b_e, a_e, and D, and finiteness of the edge set give a constant C such that the absolute value of the second term is at most C||r||^3, and therefore at most C(2/d_-)^{3/2} Phi_D^{3/2}.

Meanwhile,

||J^T Dr||^2>=kappa||Dr||^2>=kappa d_-^2||r||^2.

Since r(k_*)=0, shrink the neighborhood until C||r||<=kappa d_-^2/2. Then

dot Phi_D<=-(kappa d_-^2/2)||r||^2<=-a_D Phi_D,

where a_D=kappa d_-^2/d_+>0. Hence

Phi_D(k(t))<=exp(-a_D t)Phi_D(k(0)),

||r(k(t))||<=sqrt(d_+/d_-) exp(-a_D t/2)||r(k(0))||.

Also ||F_CL||<=C_CL||r|| by the formula -J^T Dr. All these estimates hold while the trajectory remains local.

## 5. AL: gradient identity, coercivity, and comparison with the free residual

Subtract the free KKT equations from the fully constrained reference equations. The state difference satisfies

x^a-x_0=-RQ mu.

Taking Q^T gives -r=-B mu, hence

mu=D r.

In particular, mu=0 if and only if r=0, and x^a=x_0 at k_*. Locally,

d_-||r||<=||mu||<=d_+||r||.

The derivative of the AL nudged state solves K(y,alpha,beta)=(0,0,mu); its physical-state component is y=RQD mu. Put b_e^a=d_e^T x^a and H=D_k mu. Differentiating the reference system gives

K partial_e(x^a,lambda,mu)=-(b_e^a d_e,0,0).

For any u in R^O, solve K(y_u,alpha_u,beta_u)=(0,0,u), so y_u=RQD u. Symmetry of K then gives

u^T partial_e mu=-b_e^a d_e^T RQD u.

Thus (H^T u)_e=-b_e^a a_e^T D u. The AL update, using x^a rather than the free state as its reference, is

(F_AL)_e=b_e^a a_e^T D mu=-(H^T mu)_e.

Therefore F_AL=-grad Phi_* and

dot Phi_*=-||H^T mu||^2.

At k_*, b_e^a=b_e and H(k_*)=D(k_*)J(k_*). Hence H(k_*) has full row rank. Equivalently, its active-edge factorization is the AL condition stated in the task, with the invertible right factor D. Continuity gives kappa_a>0 such that ||H^T u||^2>=kappa_a||u||^2 locally. Consequently

dot Phi_*<=-2 kappa_a Phi_*,

Phi_*(k(t))<=exp(-2 kappa_a t)Phi_*(k(0)).

The quantitative comparison mu=Dr yields

||r(k(t))||<= (d_+/d_-) exp(-kappa_a t)||r(k(0))||.

Finally, boundedness of H and D gives ||F_AL||<=C_AL||r||. Equality of zero sets alone would not have supplied this residual decay or velocity estimate; the quantitative comparison is needed.

## 6. Local solution chart and error-distance estimate

The finite-dimensional Implicit Function Theorem states that if a C^1 map F(u,z) into R^O vanishes at (u_*,z_*) and its O by O derivative in z is invertible there, then its nearby zero set is exactly a C^1 graph z=psi(u). Here r is smooth, r(k_*)=0, and full row rank provides such a coordinate block. Thus, after reordering conductance coordinates as k=(u,z), the theorem applies with E=partial_z r(k_*) invertible.

Choose smaller product neighborhoods whose z-neighborhood is convex and whose solution graph remains inside it. By continuity, shrink further so that throughout this chart

||partial_z r(k)-E||<=1/(2||E^{-1}||).

For k=(u,z), the segment from (u,psi(u)) to (u,z) stays in the chart. The fundamental theorem of calculus gives

r(u,z)=A_bar(u,z)(z-psi(u)),

A_bar(u,z)=integral_0^1 partial_z r(u,psi(u)+s(z-psi(u))) ds.

The same closeness bound holds for A_bar-E. Thus ||E^{-1}(A_bar-E)||<=1/2, and the geometric-series inverse gives ||A_bar^{-1}||<=2||E^{-1}||. Therefore

dist(k,S)<=||z-psi(u)||<=2||E^{-1}||||r(k)||.

This argument uses uniform closeness to E, not merely invertibility of every matrix being averaged.

## 7. First exit, forward existence, and convergence

Intersect the neighborhoods above. Choose R_0>0 so that the closed ball of radius R_0 about k_* is contained in this intersection and in the positive-conductance domain. Let U be its open ball. All required estimates hold on a neighborhood of its closure.

For the three methods choose common constants K_0>=1, nu>0, and V>0 so that, on any trajectory segment lying in U,

||r(k(t))||<=K_0 exp(-nu t)||r(k(0))||,

||dot k(t)||<=V||r(k(t))||.

These constants are obtained by taking the largest prefactors and velocity constants and the smallest positive residual exponent from the three estimates. Because r(k_*)=0 and r is C^1, a uniform bound on J on this ball gives ||r(k)||<=C_0||k-k_*||.

Choose rho>0 with

rho(1+VK_0 C_0/nu)<R_0/2.

Each field is smooth, hence locally Lipschitz. The standard finite-dimensional ODE local-existence theorem gives a unique local solution from every initial point in this ball. While a solution lies in U,

||k(t)-k(0)||<=V integral_0^t ||r(k(s))|| ds<=VK_0||r(k(0))||/nu.

Thus any solution starting within rho of k_* satisfies

||k(t)-k_*||<rho(1+VK_0 C_0/nu)<R_0/2.

It cannot have a first exit from U. Nor can its maximal forward existence time be finite: on the compact closed ball of radius R_0/2, the smooth field is bounded, so a solution approaching a finite maximal time is Cauchy in time and has a limit in that compact ball. Local existence at that interior limit extends it, a contradiction. This verifies the continuation hypotheses explicitly and proves existence for all t>=0, with all conductances remaining strictly positive.

The loss and residual inequalities now hold for all time. For 0<=s<=t,

||k(t)-k(s)||<=VK_0 exp(-nu s)||r(k(0))||/nu.

Therefore k(t) converges to a limit k_infinity in the closed ball of radius R_0/2, which is a subset of U. Continuity and exponential residual decay give r(k_infinity)=0, so k_infinity belongs to S. The chart estimate also yields dist(k(t),S)->0. Initial points with r=0 are stationary for all three fields, so the argument includes that case. All constants depend only on the fixed local circuit data and k_*, not on the chosen initial point within rho.

Every theorem-critical obligation is closed; no specialized external convergence theorem or unresolved paper-specific dependency is being assumed.
