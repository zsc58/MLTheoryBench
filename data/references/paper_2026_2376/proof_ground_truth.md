# Reference Proof

## Proof Structure

Establish the convolution identities, their regularity, and the test functions needed for C0-vague convergence. Reconstruct block field identifiability, including the elliptic and degenerate cases. Normalize any nonzero cluster limit to identify its law. Finally use the overlap condition to fix its mass and upgrade full C0-vague convergence to weak convergence.

## Standard Independent Background

The external facts used below are recorded in theory_022. Their relevant forms are:

- If f belongs to C0 intersect L1 and nu is a finite nonnegative measure, then f*nu belongs to C0 intersect L1, with ||f*nu||_1 <= nu(R^d)||f||_1. Bounded kernels also give the analogous Linfinity bound. Distributional convolution derivatives are valid when Fubini's theorem is justified by the integrability bounds below.
- Local Sobolev product and smooth chain rules apply to bounded W^{1,1}_{loc} functions, with the usual derivative formulas.
- Fourier transforms are unique for finite signed measures, and the Fourier transform of an L1 kernel convolved with a finite measure is the product of their transforms.
- Probabilities on a compact metrizable space are weakly sequentially compact. The one-point compactification of R^d is compact metrizable, and each C0 function extends continuously to it by taking value zero at infinity.
- The local Sobolev renormalization principle explicitly invoked in the source has the following form. If b is in W^{1,1}_{loc}(R^d;R^d), rho is in L^{infinity}_{loc}(R_t;L1 intersect Linfinity), and partial_t rho+div(b rho)=0 distributionally, then

  partial_t beta(rho)+div(b beta(rho))+(rho beta'(rho)-beta(rho))div b=0

  for beta in C1 with beta(0)=0, beta' bounded, and z beta'(z)-beta(z) bounded.

The paper-specific companion and identifiability conclusions are not assumed as external facts.

## 1. Kernel and Convolution Regularity

Finite products of bounded C0 functions on their respective blocks belong to C0 on the product space. Indeed, outside a sufficiently large product of balls at least one factor is uniformly small, while the other factors are bounded. Fubini gives their L1 bounds. For a coordinate j in block alpha,

partial_j kappa(z)=(partial_j kappa_alpha)(z_alpha) product_{beta != alpha} kappa_beta(z_beta),

so kappa belongs to W^{1,1} as well. The same product argument gives eta^[alpha] and grad_alpha eta^[alpha] in C0 intersect L1 intersect Linfinity. Their kernel identities are

grad_alpha eta^[alpha](z)=-z_alpha kappa(z)/c_{1,alpha},

L_alpha eta^[alpha](z)=c_{2,alpha}kappa(z),

where L_alpha=lambda_{0,alpha}I-lambda_{1,alpha}Delta_alpha. Consequently z kappa(z) belongs to C0 intersect L1 intersect Linfinity, componentwise.

For a probability r define privately

Psi_{alpha,r}=eta^[alpha]*r.

All these convolutions are finite. Since kappa and eta^[alpha] are strictly positive, u_r and Psi_{alpha,r} are strictly positive everywhere. The bound

integral ||y|| kappa(x-y)r(dy) <= ||x|| ||kappa||_infinity + sup_z ||z|| kappa(z)

establishes absolute integrability of m_r without any moment assumption on r. Convolution closure gives u_r, Psi_{alpha,r}, and grad_alpha Psi_{alpha,r} in C0 intersect L1 intersect Linfinity. Also partial_j u_r=(partial_j kappa)*r, with L1 norm bounded by ||partial_j kappa||_1, so u_r is in W^{1,1}.

Block first and second derivatives of eta^[alpha] are bounded and continuous. Differentiation under the finite-measure integral, followed by dominated convergence for continuity, therefore gives classical continuous block derivatives of Psi_{alpha,r} through order two. Convolving the two kernel identities yields

m_{r,alpha}-x_alpha u_r=c_{1,alpha}grad_alpha Psi_{alpha,r},

L_alpha Psi_{alpha,r}=c_{2,alpha}u_r,

a_{r,alpha}-x_alpha=c_{1,alpha}c_{2,alpha}grad_alpha Psi_{alpha,r}/(L_alpha Psi_{alpha,r}).

In particular m_r and a_r are continuous. No global C0 or L1 claim about m_r itself is needed.

We also need full-space local Sobolev regularity of v_{alpha,r}=grad_alpha Psi_{alpha,r}. For a component g_i of grad_alpha eta^[alpha], a derivative within block alpha is a component of Hess eta_alpha times the other kappa factors. If K is contained in a compact rectangle product_beta K_beta, its absolute integral over every translate K-y is bounded by

||Hess eta_alpha||_infinity |K_alpha| product_{beta != alpha} ||kappa_beta||_1.

A derivative in block beta != alpha is a component of grad eta_alpha times a derivative of kappa_beta times the remaining factors. Its full-space L1 norm is bounded by

||grad eta_alpha||_1 ||grad kappa_beta||_1 product_{gamma != alpha,beta} ||kappa_gamma||_1.

These estimates justify weak differentiation of g_i*r by Fubini on every compact region and show that its derivatives are locally L1. Thus v_{alpha,r} belongs to W^{1,1}_{loc} and is bounded.

Finally, for fixed x,

y_j kappa(x-y)=x_j kappa(x-y)-(x_j-y_j)kappa(x-y).

Since kappa and z kappa(z) belong to C0, both y -> kappa(x-y) and y -> y_j kappa(x-y) are C0 test functions.

## 2. Block Field Identifiability

Let p and r be probabilities with a_p=a_r=:a. Fix a block alpha, abbreviate P=Psi_{alpha,p}, Q=Psi_{alpha,r}, and set

b_alpha=(a_alpha-x_alpha)/(c_{1,alpha}c_{2,alpha}).

The identities above give

grad_alpha P=b_alpha L_alpha P,qquad grad_alpha Q=b_alpha L_alpha Q.

Define

J_alpha=Q grad_alpha P-P grad_alpha Q.

If lambda_{1,alpha}=0, multiplication of the two equations by Q and P and subtraction immediately gives J_alpha=0.

Suppose lambda=lambda_{1,alpha}>0. Classical block differentiation gives

s_alpha=div_alpha J_alpha=Q Delta_alpha P-P Delta_alpha Q.

The same subtraction yields

J_alpha=-lambda b_alpha s_alpha,

s_alpha+lambda div_alpha(b_alpha s_alpha)=0

in distributions. Substituting the elliptic identities gives

s_alpha=(c_{2,alpha}/lambda)(P u_r-Q u_p).

Thus s_alpha is continuous and belongs to L1 intersect Linfinity: each product has an L1 bound from one bounded factor and one L1 factor, and a Linfinity bound from two bounded factors. Similarly,

||J_alpha||_1 <= ||Q||_infinity ||grad_alpha P||_1 + ||P||_infinity ||grad_alpha Q||_1 < infinity.

Moreover,

b_alpha=grad_alpha Q/(c_{2,alpha}u_r).

On each relatively compact region, continuity and positivity bound u_r away from zero. The Sobolev chain rule applied to a smooth bounded extension of t -> 1/t, together with the bounded Sobolev product rule, proves b_alpha in W^{1,1}_{loc}, using the regularity of u_r and grad_alpha Q established above.

Embed b_alpha into the full-space vector field B_alpha by setting all other blocks to zero, and similarly embed J_alpha as tilde J_alpha. Then

s_alpha+lambda div(B_alpha s_alpha)=0,

B_alpha s_alpha=-tilde J_alpha/lambda.

Set rho(t,x)=exp(t/lambda)s_alpha(x). It satisfies

partial_t rho+div(B_alpha rho)=0.

All hypotheses of the stated standard renormalization principle hold: B_alpha is locally W^{1,1}; rho is locally bounded in time with values in L1 intersect Linfinity; the equation holds distributionally; and B_alpha rho=-exp(t/lambda)tilde J_alpha/lambda is locally bounded in time with values in L1.

For completeness, choose beta_delta(z)=sqrt(z^2+delta^2)-delta. It satisfies beta_delta(0)=0, |beta_delta'|<=1, 0<=|z|-beta_delta(z)<=delta, and |z beta_delta'(z)-beta_delta(z)|<=delta. The renormalized identity therefore converges, on compact space-time sets, to

partial_t |rho|+div(B_alpha |rho|)=0.

The divergence-error term is bounded by delta |div B_alpha|, which is locally integrable; the other terms converge by local domination.

Choose chi_R(x)=chi(x/R), with chi smooth compactly supported, 0<=chi<=1, and chi=1 near the origin. Test against phi(t)chi_R(x). The absolute value of the boundary flux term is bounded by

(||phi||_infinity ||grad chi||_infinity/R) integral_{supp phi} ||B_alpha rho(t)||_1 dt,

which tends to zero. Dominated convergence in the density term then gives

integral phi'(t)||rho(t)||_1 dt=0.

Hence the density's L1 norm is distributionally constant. But it equals exp(t/lambda)||s_alpha||_1, so ||s_alpha||_1=0. Continuity implies s_alpha=0 everywhere, and J_alpha=-lambda b_alpha s_alpha gives J_alpha=0 everywhere.

We have proved J_alpha=0 in both cases. Since Q>0,

grad_alpha(P/Q)=J_alpha/Q^2=0.

This proves only fiberwise constancy: P(x)=C_alpha(x_{outside alpha})Q(x), with C_alpha positive and independent of x_alpha. Applying L_alpha on each fixed fiber gives

u_p(x)=C_alpha(x_{outside alpha})u_r(x).

Therefore the common continuous ratio h=u_p/u_r is independent of block alpha. The argument holds for every block. Changing blocks one at a time between any two points shows that h is a single positive constant C, so u_p=C u_r. Tonelli gives

integral u_p(x)dx=integral u_r(x)dx=integral kappa(z)dz>0,

and hence C=1.

To justify deconvolution, use the Fourier convention hat f(xi)=integral exp(-i z dot xi)f(z)dz. For each factor, z kappa_alpha=-c_{1,alpha}grad eta_alpha is L1, so hat kappa_alpha is C1. Transforming its two companion identities gives

i xi hat eta_alpha=-(i/c_{1,alpha})grad hat kappa_alpha,

(lambda_{0,alpha}+lambda_{1,alpha}||xi||^2)hat eta_alpha=c_{2,alpha}hat kappa_alpha.

When lambda_{1,alpha}>0, Delta eta_alpha=(lambda_{0,alpha}eta_alpha-c_{2,alpha}kappa_alpha)/lambda_{1,alpha} is L1, which also justifies the second transform. When lambda_{1,alpha}=0 it is an algebraic transform. Elimination gives

grad hat kappa_alpha=-(c_{1,alpha}c_{2,alpha}/(lambda_{0,alpha}+lambda_{1,alpha}||xi||^2))xi hat kappa_alpha.

Along each ray the initial value is hat kappa_alpha(0)=integral kappa_alpha>0. Solving the scalar ODE yields

hat kappa_alpha(xi)=hat kappa_alpha(0)exp(-c_{1,alpha}c_{2,alpha}||xi||^2/(2lambda_{0,alpha}))

if lambda_{1,alpha}=0, and

hat kappa_alpha(xi)=hat kappa_alpha(0)(1+(lambda_{1,alpha}/lambda_{0,alpha})||xi||^2)^(-c_{1,alpha}c_{2,alpha}/(2lambda_{1,alpha}))

otherwise. Every factor transform is consequently nonzero everywhere. Fubini gives hat kappa(xi)=product_alpha hat kappa_alpha(xi_alpha), also nonzero everywhere. The identity u_p=u_r implies hat kappa(hat p-hat r)=0. Fourier uniqueness for the finite signed measure p-r now gives p=r. This closes the paper-specific identifiability obligation.

## 3. C0-Vague Compactness and Identification of Cluster Limits

View each probability q_n on the compact metrizable one-point compactification X=R^d union {infinity}. The stated compactness fact yields a weakly convergent subsequence with limit bar mu in P(X). Its restriction mu to R^d is a nonnegative measure of mass at most one, and extension of C0 functions by zero at infinity gives C0-vague convergence to mu. This applies to every subsequence.

Any specified C0-vague limit is also a subprobability. Positivity follows by testing nonnegative compactly supported continuous functions; testing cutoffs 0<=chi_R<=1 increasing to one gives mu(R^d)<=1. Equivalently, apply the preceding compactification extraction to the specified convergent subsequence and use uniqueness of its C0 limit.

Let q_{n_k} converge C0-vaguely to mu, and put c=mu(R^d). If c=0, positivity gives mu=0=cp. Otherwise set r=mu/c, a probability. The C0 test functions from Section 1 give, for every fixed x,

u_{q_{n_k}}(x) -> c u_r(x),qquad m_{q_{n_k}}(x) -> c m_r(x).

Since c>0 and u_r(x)>0, division gives a_{q_{n_k}}(x) -> a_r(x). The field hypothesis, with V_{p,q}=a_p-a_q, also gives a_{q_{n_k}}(x) -> a_p(x). Thus a_r=a_p everywhere, and Section 2 proves r=p. Therefore mu=cp with c in [0,1].

## 4. Fixing the Mass and Obtaining Weak Convergence

The function u_p is strictly positive, bounded, and in C0. In particular

0<Z_p(p)<=||kappa||_infinity.

Take any subsequence and then a further C0-vaguely convergent subsequence. Its limit is cp by Section 3, and testing with u_p gives

Z_p(q_{n_k}) -> c Z_p(p).

The liminf condition for the whole sequence also bounds this subsequential limit from below by Z_p(p). Positivity of Z_p(p) gives c>=1; since c<=1, c=1.

Every subsequence thus has a further C0-vague subsequence converging to p. For any f in C0, failure of convergence of integral f dq_n to integral f dp would supply a subsequence whose discrepancy is bounded below by a positive number. Its further subsequence converging to p contradicts that bound. Hence q_n converges C0-vaguely to p.

To upgrade this to weak convergence, fix epsilon>0 and choose compact K with p(K)>1-epsilon, then a compactly supported continuous cutoff chi with 0<=chi<=1 and chi=1 on K. Convergence of integral chi dq_n implies that all sufficiently late q_n assign at least 1-2epsilon mass to supp chi. Finitely many initial probabilities are made tight by enlarging the compact set. Thus the whole sequence is tight.

For any bounded continuous h, choose compact K with sup_n q_n(K^c)+p(K^c) arbitrarily small and another cutoff chi equal to one on K. Since h chi is in C0, its integrals converge. The remaining discrepancy is bounded by ||h||_infinity(q_n(K^c)+p(K^c)). Letting the tail bound tend to zero proves convergence against every bounded continuous h, hence weak convergence to p.

## Obligation Audit

All theorem-critical obligations are closed: global domains without moment hypotheses; convolution and local Sobolev regularity; C0 test-function closure; block Wronskian vanishing in both coefficient cases; the renormalization application and integrable-flux cutoff argument; fiberwise-to-global proportionality; Fourier nonvanishing and finite-measure uniqueness; subprobability compactness; zero-mass handling and normalization; positive overlap and the liminf argument; full-sequence convergence; and the weak-convergence upgrade. No unresolved nonstandard dependency remains.
