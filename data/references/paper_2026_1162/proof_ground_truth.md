# Reference Proof

## Obligations and External Input

The obligations are: finite and differentiable mean objectives; uniform input/output truncation for fixed bases and centers; finite-dimensional GELU approximation of values and shape derivatives on unbounded parameter inputs; admissible surrogate regularity; a network-independent gradient-error estimate; constrained stationary-point transfer; and one coordinated choice of tolerances.

The sole external approximation result used is the standard compact finite-dimensional C^1 theorem: if a scalar activation rho is smooth and nonpolynomial, f is a finite-dimensional vector-valued C^1 function on a neighborhood of a compact K, and eta>0, a finite single-hidden-layer rho network approximates f and its full first derivative uniformly on K within eta. Vector components can be approximated separately. We verify its activation and domain hypotheses below. The mixed-norm, cutoff, and truncation arguments are derived here rather than assumed from a paper-specific theorem.

Write K=Z_ad. For a Hilbert-valued map F, let ||F(.,z)||_p=(E||F(m,z)||^p)^{1/p}. All expectations use the fixed measure mu_m.

## 1. Moment Bounds and Differentiability

Fix a compact shape neighborhood contained in B. The Lipschitz hypotheses give an envelope

||u(m,z)||_U+||D_z u(m,z)||_HS <= C(1+||m||_M)

uniformly on that neighborhood. Thus both maps have finite L^p norms. Their dependence on z is Lipschitz in L^p, directly by integrating the pointwise Lipschitz inequalities. In particular,

A=sup_{z in K}||u(.,z)||_2<infinity,
B_u=sup_{z in K}||D_z u(.,z)||_{L^2(HS)}<infinity.

Put L_u=kappa_Qu and L_uz=kappa_Quz. Integrating the state derivatives along the segment from 0 to v gives

|Q(v,m,z)| <= M_Q+M_Qu||v||+(L_u/2)||v||^2,
||D_u Q(v,m,z)|| <= M_Qu+L_u||v||,
||D_z Q(v,m,z)|| <= M_Qz+M_Quz||v||+(L_uz/2)||v||^2,
||D_u(D_z Q)(v,m,z)|| <= M_Quz+L_uz||v||.

The pointwise derivative of Q(u(m,z),m,z) is

A_Q(m,z)=D_u Q(u(m,z),m,z)D_z u(m,z)+D_z Q(u(m,z),m,z).

Its norm on a compact shape neighborhood is bounded by C(1+||m||^2), which is integrable since p>=2. Segment integration of the pointwise derivative bounds difference quotients by the same type of envelope. Pointwise differentiability and dominated convergence therefore give Frechet differentiability into L^1(mu_m); pointwise continuity of A_Q and that envelope give continuity of this derivative. Applying expectation yields

DJ(z)[h]=E[D_u Q(u,m,z)[D_z u h]+D_z Q(u,m,z)[h]]+DP(z)[h].

The analogous conclusion holds for every finite GELU RBNO. Indeed, sigma'(t)=Phi_Gauss(t)+t phi_Gauss(t) is bounded; every higher derivative is a polynomial times the Gaussian density and is bounded. Repeated chain rules show that every positive-order derivative of a fixed finite feedforward GELU network is globally bounded. Its output has at most linear growth. Consequently its RBNO has finite p-th moments on compact shape neighborhoods, its derivative has finite p-th moments, and the same domination argument applies. Its bounded second derivatives also imply that D_z u_theta is globally Lipschitz. This verifies the surrogate regularity instead of assuming it from its approximation error.

## 2. Fixed-Basis Truncation

Let P_M,r and P_U,r be projections onto the initial segments of the fixed complete bases. In a finite-dimensional space, the projection becomes the identity at full rank. Define

m_r=b_m+P_M,r_m(m-b_m),
u_r(m,z)=b_u+P_U,r_u(u(m_r,z)-b_u).

Completeness gives pointwise convergence of (I-P_U,r)(u(m,z)-b_u) to zero. Its p-th power is dominated by ||u(m,z)-b_u||^p. Each expected projection tail is continuous in z, because projection is a contraction and u depends continuously on z in L^p. The tails decrease with r. Dominated convergence and Dini's theorem on compact K therefore give uniform convergence to zero.

The same reasoning applies to (I-P_U,r)D_z u. For an orthonormal basis e_1,...,e_{d_z} of Z,

||(I-P_U,r)D_z u||_HS^2=sum_{j=1}^{d_z}||(I-P_U,r)D_z u e_j||_U^2,

which decreases pointwise to zero and is dominated by ||D_z u||_HS^2. This also covers d_z=0, when the sum is empty.

For input truncation,

||u(m,z)-u(m_r,z)|| <= kappa_u||(I-P_M,r_m)(m-b_m)||,
||D_z u(m,z)-D_z u(m_r,z)||_HS <= kappa_uz||(I-P_M,r_m)(m-b_m)||.

The centered input has a finite p-th moment. Completeness, contraction, and dominated convergence make the right sides tend to zero in L^p, independently of z. Thus all four output/input truncation errors can be made uniformly small. Explicitly,

||u-u_r||_p <= ||(I-P_U,r_u)(u-b_u)||_p+kappa_u||(I-P_M,r_m)(m-b_m)||_p,

and the derivative has the corresponding bound with D_z u and kappa_uz.

For the chosen ranks set

g(x,z)=Phi_r_u^*(u(b_m+Psi_r_m x,z)-b_u),
x=Psi_r_m^*(m-b_m),

and let nu be the pushforward of mu_m by this encoder. Then u_r=b_u+Phi_r_u g(x,z). The target g is C^1. Both z->g(.,z) and z->D_z g(.,z) are Lipschitz into L^p(nu), by the solution-map inequalities and encoder/decoder contraction. The reduced input has a finite p-th moment. We next derive the required network approximation for this g.

## 3. Finite-Dimensional Approximation With Tail Control

Suppose first r_m>0. We establish the construction for any C^1 target g on R^{r_m} x B whose value and z derivative depend continuously on z in L^p(nu).

### Compact Approximation

Define rho(t)=sigma(t+1)-sigma(t-1). This function is smooth and bounded, with limits 0 and 2 at negative and positive infinity. It is nonconstant and therefore nonpolynomial. All its positive-order derivatives are bounded. The compact C^1 external theorem consequently applies.

For any compact product contained in R^{r_m} x B, the target can first be multiplied by a smooth function equal to one on a neighborhood of that product and supported inside its open domain, then extended by zero. This produces a global C^1 target with unchanged values and derivatives on the product. It verifies the domain hypothesis of the external theorem.

Each rho unit is exactly two GELU units, so the resulting compact approximant h is a finite GELU network. Its output and z derivative are globally bounded. For a chosen outer ball and compact K, we can therefore obtain

sup ||g-h|| <= gamma,
sup ||D_z g-D_z h||_F <= gamma

on that product, with a finite global bound M>=1 for both h and D_z h. The bound M can depend on the compact approximation. The construction below chooses subsequent tolerances after M is known.

### Approximate Cutoff

Let phi be the standard Gaussian density. For s>=0, s Phi_Gauss(-s)<=phi(s)<=1/sqrt(2 pi). Hence

F_a(t)=[sigma(a t)+sigma(-a t)]/a

is nonnegative and differs from |t| by at most 2/(a sqrt(2 pi)). Summing over coordinates produces a nonnegative GELU network L(x) such that |L(x)-||x||_1|<=R, for any chosen R>1.

Set c=sqrt(r_m)+1. The shifted GELU difference

H_{a,b}(t)=1+[sigma(a(t-b-1))-sigma(a(t-b))]/a

differs uniformly by O(1/a) from the corresponding shifted-ReLU cutoff. Taking b=2cR and a sufficiently large makes H_{a,b} alpha-close to one for 0<=t<=cR and alpha-close to zero for t>=4cR. By the mean value theorem, |H_{a,b}|<=H_0=1+sup|sigma'|, independently of a,b,R.

The two-layer GELU network q(x)=H_{a,b}(L(x)) consequently satisfies

|q(x)-1|<=alpha when ||x||_2<=R,
|q(x)|<=alpha when ||x||_2>=5cR,
|q(x)|<=H_0 everywhere.

These are approximate bounds, not an exact compactly supported cutoff.

### Multiplication and the Global Envelope

Construct h by compact C^1 approximation on the entire ball ||x||_2<=5cR, together with K. This radius is necessary to cover the whole cutoff transition region.

On the compact range [-H_0,H_0] x [-M,M]^{r_u}, apply the compact C^1 theorem to the vector multiplication map (t,v)->t v. Choose a finite GELU network F such that

||F(t,v)-t v||_2<=beta,
||D_v F(t,v)-t I||_op<=beta

throughout that range. Define G(x,z)=F(q(x),h(x,z)). Parallel composition and composition give a finite feedforward GELU network. Different depths can be aligned using the exact identity sigma(t)-sigma(-t)=t. Since q is independent of z,

D_z G=D_v F(q,h)D_z h.

On the radius-R ball, the value and derivative errors are respectively at most

gamma+alpha M+beta,
gamma+alpha M+beta M.

For any requested s>0 choose, in order,

gamma<=min{s/3,1/(2H_0)},
alpha<=min{s/(3M),1/(2M)},
beta<=min{s/3,s/(3M),1/2,1/(2M)}.

Both compact errors are then at most s. Beyond radius 5cR, the errors are at most ||g||+1 and ||D_z g||_F+1. Within that outer radius, compact approximation of h and the bound |q|<=H_0 give errors at most

(1+H_0)(||g||+1),
(1+H_0)(||D_z g||_F+1).

Thus everywhere, with C_p=2^{p-1}(1+H_0)^p independent of R,s,M,

||g-G||_2^p<=C_p(||g||_2^p+1),
||D_z g-D_z G||_F^p<=C_p(||D_z g||_F^p+1).

In particular no higher input moment is needed. The composed network is also globally bounded, since its inner inputs remain in a compact range.

### Uniform Tail Limit

For each integer R, the functions

T_R^0(z)=integral_{||x||>R}(||g(x,z)||_2^p+1) dnu(x),
T_R^1(z)=integral_{||x||>R}(||D_z g(x,z)||_F^p+1) dnu(x)

are continuous in z. Indeed, multiplication by the fixed tail indicator is a contraction on L^p, and the p-th power of its norm is continuous. They decrease pointwise to zero by dominated convergence. Dini's theorem makes each convergence uniform on compact K.

The construction therefore gives

sup_K integral ||g-G||^p dnu <= s^p+C_p sup_K T_R^0,
sup_K integral ||D_z g-D_z G||_F^p dnu <= s^p+C_p sup_K T_R^1.

Choose R first to make the two target tails small, then choose s and the network tolerances. This proves arbitrarily small separate uniform L^p errors for values and shape derivatives with one GELU network.

If r_m=0, the reduced input is the single point of R^0 and has no tail. Compact C^1 approximation in z alone proves the same result. If all remaining input dimensions are zero, a constant affine network suffices. If U is the zero space, its state and derivative are identically zero and the zero-output network proves the approximation assertion directly; both objectives then coincide. Otherwise permitted ranks are chosen as above. These conventions also cover finite-dimensional M and U without demanding ranks beyond their dimensions.

Decoder isometry gives

||Phi_r_u(g-G)||_U=||g-G||_2,
||Phi_r_u(D_z g-D_z G)||_HS=||D_z g-D_z G||_F.

For any t>0 choose the output truncation, input truncation, and latent-network errors each at most t/6 in uniform L^p, for both values and derivatives. Each final error norm is then at most t/2. Since p>=2,

sup_K E||u-u_theta||^p+sup_K E||D_z u-D_z u_theta||_HS^p <=2(t/2)^p<=t^p.

The fixed centers and bases have not been changed.

## 4. Network-Independent Gradient Mismatch

For fixed z put

a=||u-u_theta||_2,
b=||D_z u-D_z u_theta||_{L^2(HS)}.

Subtract the differentiated mean objectives; their common penalty cancels. Split the integrand into

(D_u Q(u)-D_u Q(u_theta))D_z u,
D_u Q(u_theta)(D_z u-D_z u_theta),
D_z Q(u)-D_z Q(u_theta).

The expected norms are bounded, respectively, by

L_u B_u a,
(M_Qu+L_u A)b+L_u ab,
(M_Quz+L_uz A)a+(L_uz/2)a^2.

The last inequality follows by integrating D_u(D_z Q) along the state segment starting at u. Cauchy-Schwarz gives the displayed linear terms, and ab<=(a^2+b^2)/2 handles the cross term. Consequently

||DJ(z)-DJ_theta(z)||_{Z'} <= C_1(a+b)+C_2(a^2+b^2),

where one may take

C_1=max{L_u B_u+M_Quz+L_uz A, M_Qu+L_u A},
C_2=(L_u+L_uz)/2.

These constants are independent of the network. They depend only on the stated quantity constants and exact-state moment bounds. Since mu_m is a probability measure and p>=2, the L^2 errors are bounded by the L^p errors. If the mixed approximation is constructed at tolerance t<=1, both a and b are at most t, so

delta=sup_K ||DJ-DJ_theta|| <=2C_1 t+2C_2 t^2 <= C t,

with C=1+2C_1+2C_2>0 independent of the surrogate.

## 5. Constrained Optimization Transfer

Continuity and compactness give a constrained minimizer z_star, and strong convexity on the convex nonempty K makes it unique. Its variational inequality is

<DJ(z_star),z-z_star>>=0 for every z in K.

Let z_dagger be any constrained stationary point of J_theta and d=z_dagger-z_star. Adding the two strong-convexity inequalities gives

<DJ(z_dagger)-DJ(z_star),d>>=lambda||d||^2.

The exact and surrogate variational inequalities imply

lambda||d||^2 <= <DJ(z_dagger)-DJ_theta(z_dagger),d> <=delta||d||.

If d=0 the distance assertion is immediate; otherwise divide to obtain ||d||<=delta/lambda.

For the objective gap, apply strong convexity with its derivative at z_dagger:

J(z_dagger)-J(z_star) <=<DJ(z_dagger),d>-(lambda/2)||d||^2.

Surrogate stationarity, tested against z_star, gives <DJ_theta(z_dagger),d><=0. Hence

J(z_dagger)-J(z_star) <=delta||d||-(lambda/2)||d||^2 <=delta^2/(2lambda).

This gap argument uses surrogate stationarity at z_dagger, not the exact variational inequality alone. It holds also for singleton or lower-dimensional admissible sets. The surrogate is continuous on compact K and C^1 on B, so it has a minimizer satisfying the same variational condition; the universal stationary-point assertion is not dependent on an extra existence assumption.

## 6. One Choice of Operator

Given epsilon>0 choose

0<t<=min{epsilon,1,lambda epsilon/C,sqrt(2lambda) epsilon/C}.

Construct the single RBNO at mixed approximation tolerance t. Its mixed error is at most t^p<=epsilon^p and its gradient mismatch is at most C t. The preceding bounds give

||z_dagger-z_star||<=epsilon,
J(z_dagger)-J(z_star)<=epsilon^2

for every constrained stationary point of that same surrogate. All ranks and network dimensions are finite, while the bases and centers remain the arbitrary fixed ones from the public setup. All listed obligations are closed.
