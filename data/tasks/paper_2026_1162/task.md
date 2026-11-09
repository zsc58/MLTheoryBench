# Problem

## Setup

Let M and U be real separable Hilbert spaces, possibly finite dimensional, and let Z=R^{d_z} be a finite-dimensional Euclidean space. A bounded Lipschitz reference domain is mapped by W^{1,infinity} diffeomorphisms chi_z to a family of bounded Lipschitz domains. After pullback to the reference domain, the state equation is a residual equation R(u,m,z)=0 with a unique solution, defining a solution map u:M x B->U, where B subset Z is open.

All derivatives below are Frechet derivatives. Write X' for the continuous dual of a Hilbert space X and L(X,Y) for the bounded linear maps from X to Y. For A in L(Z,U), define

||A||_{HS(Z,U)}^2=sum_{j=1}^{d_z}||A e_j||_U^2,

where e_1,...,e_{d_z} is the standard orthonormal basis of Z. Expectations of norms use the indicated Borel probability measure.

Assume:

1. mu_m is a fixed Borel probability measure on M with

integral_M ||m||_M^p dmu_m(m)<infinity

for a fixed real p in [2,infinity). The admissible set Z_ad subset B is nonempty, compact, and convex.

2. The solution map u is C^1 on M x B. There are finite constants kappa_u,kappa_uz>0 such that for all m_1,m_2 in M and z_1,z_2 in B,

||u(m_2,z_2)-u(m_1,z_1)||_U <=kappa_u(||m_2-m_1||_M+||z_2-z_1||_Z),

||D_z u(m_2,z_2)-D_z u(m_1,z_1)||_{HS(Z,U)} <=kappa_uz(||m_2-m_1||_M+||z_2-z_1||_Z).

3. The quantity map Q:U x M x B->R is C^2. There are finite constants kappa_Qu,kappa_Quz>0 such that for all v_1,v_2 in U, m in M, and z in B,

||D_u Q(v_2,m,z)-D_u Q(v_1,m,z)||_{U'} <=kappa_Qu||v_2-v_1||_U,

||D_u(D_z Q)(v_2,m,z)-D_u(D_z Q)(v_1,m,z)||_{L(U,Z')} <=kappa_Quz||v_2-v_1||_U.

There are finite nonnegative constants M_Q,M_Qu,M_Qz,M_Quz such that for every m in M and z in B,

|Q(0,m,z)|<=M_Q,
||D_u Q(0,m,z)||_{U'}<=M_Qu,
||D_z Q(0,m,z)||_{Z'}<=M_Qz,
||D_u(D_z Q)(0,m,z)||_{L(U,Z')}<=M_Quz.

4. Let P:B->R be a common C^1 penalty. Define the exact mean objective and, for a neural operator u_theta of the form below, its surrogate mean objective by

J(z)=E_{m~mu_m}[Q(u(m,z),m,z)]+P(z),
J_theta(z)=E_{m~mu_m}[Q(u_theta(m,z),m,z)]+P(z),

for z in B. Assume J is C^1 on B and is lambda-strongly convex there for some lambda>0, meaning that for every z_1,z_2 in B,

J(z_2)>=J(z_1)+<DJ(z_1),z_2-z_1>+(lambda/2)||z_2-z_1||_Z^2.

Here the angle brackets denote duality pairing. Let z_star be the constrained minimizer of J over Z_ad.

5. Fix arbitrary complete orthonormal bases (psi_i) of M and (phi_i) of U and arbitrary centers b_m in M and b_u in U. These remain fixed. For permitted finite ranks r_m,r_u define

Psi_{r_m}^* m=(<m,psi_i>_M)_{i=1}^{r_m},
Phi_{r_u} c=sum_{i=1}^{r_u}c_i phi_i.

In a finite-dimensional space, ranks cannot exceed its dimension. A rank-zero encoder or decoder uses R^0 and the empty sum.

A reduced-basis neural operator has the form

u_theta(m,z)=b_u+Phi_{r_u}g_theta(Psi_{r_m}^*(m-b_m),z),

where g_theta:R^{r_m} x R^{d_z}->R^{r_u} is a finite feedforward network made from affine maps, componentwise hidden-layer activations

sigma(t)=t Phi_Gauss(t),

and an affine output map. Here Phi_Gauss is the cumulative distribution function of the standard normal distribution; sigma is the GELU activation.

A constrained first-order stationary point of J_theta is a point z_dagger in Z_ad satisfying

<DJ_theta(z_dagger),z-z_dagger>>=0 for every z in Z_ad.

## Task

Prove the following integrated theorem. For every epsilon>0, there exist finite permitted ranks r_m,r_u and a GELU reduced-basis neural operator u_theta, using the fixed bases and centers above, such that

sup_{z in Z_ad} E_{m~mu_m}||u(m,z)-u_theta(m,z)||_U^p
+sup_{z in Z_ad} E_{m~mu_m}||D_z u(m,z)-D_z u_theta(m,z)||_{HS(Z,U)}^p
<=epsilon^p.

For the same operator, every constrained first-order stationary point z_dagger of J_theta satisfies

||z_dagger-z_star||_Z<=epsilon,
J(z_dagger)-J(z_star)<=epsilon^2.
