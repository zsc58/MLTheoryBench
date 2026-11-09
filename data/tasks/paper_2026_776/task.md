# Problem

## Setup

For each integer d>=3, let u^\star,v^\star in R^d be fixed orthogonal vectors of norm sqrt(d). Let (lambda,nu) have a fixed joint law, independent of d, with centered, statistically dependent coordinates satisfying E[lambda nu]=0 and kappa:=E[nu^2] in (0,infinity). Let z~N(0,I_d) be independent of the latents. Samples use independent copies of (lambda,nu,z). Define

\[
S=I_d-\left(1-\frac1{\sqrt{1+\kappa}}\right)\frac{v^\star v^{\star\top}}d,
\qquad
x=\lambda\frac{u^\star}{\sqrt d}+S\left(\nu\frac{v^\star}{\sqrt d}+z\right).
\]

Define
\[
k^\star=\min\{k\ge1:\mathbb E[\lambda^k\nu]\ne0\},
\]
with k^\star=infinity if this set is empty, and assume k^\star>=2.

Let sigma:R->R be a fixed measurable activation, independent of d. Assume that the likelihood ratio dP_x/dN(0,I_d) exists and is square-integrable under N(0,I_d), and that sigma(G)^2 and G sigma(G) are square-integrable for G~N(0,1).

For ||w||=sqrt(d), set
\[
\widehat x(w)=\frac{w}{\sqrt d}\sigma(w^\top x/\sqrt d),
\qquad R(w)=\mathbb E\|x-\widehat x(w)\|^2,
\]
\[
m_u=d^{-1}w^\top u^\star,\qquad m_v=d^{-1}w^\top v^\star.
\]
The feasible overlaps satisfy m_u^2+m_v^2<=1. Write the overlap representation and its Hermite-induced power series locally at the origin as
\[
R(w)=F(m_u,m_v)
=C_0+\sum_{\substack{i,j\ge0\\i+j\ge1}} C_{ij}m_u^im_v^j.
\]
Here C_{ij} are the literal monomial coefficients, the series is uniformly absolutely convergent on compact subsets of the open feasible disk, and F is assumed C^4 on a neighborhood of the origin. Define the following named coefficients, with the indicated normalization:
\[
C_2=2C_{20},\qquad C_3=2C_{21},\qquad
C_{(3,1)}=6C_{31},\qquad C_{(2,2)}=4C_{22}.
\]

Consider the spherical population flow
\[
\dot w=-d\left(I_d-\frac{ww^\top}{d}\right)\nabla R(w),
\]
started independently and uniformly on {w:||w||=sqrt(d)}. The projected gradient is the derivative of the risk restricted to this sphere.

## Task

Prove the following integrated theorem.

For sigma(t)=t, every linear tied-autoencoder minimizer on the sphere is a leading eigenvector of the population covariance and has zero overlap with v^\star.

For the spherical flow, prove the following four early-stage assertions. All constants and overlap thresholds below may depend on the fixed latent law, activation, and displayed confidence parameters, but not on d. Probabilities refer to the random initialization.

1. **First forcing case.** If C_2<0 and C_3!=0, then for every delta in (0,1) there exist epsilon_1,epsilon_2>0 and 0<c<C<infinity such that, for every sufficiently large d, with probability at least 1-delta there is a time T in [c log(d),C log(d)] satisfying
\[
|m_u(T)|\ge\epsilon_1,\qquad |m_v(T)|\ge\epsilon_2.
\]

2. **Second forcing case.** The same conclusion holds if C_2<0, C_3=0, and C_{(3,1)}!=0.

3. **No direct forcing.** Suppose C_2<0, C_{p,1}=0 for every integer p>=1, and C_{(2,2)}>2C_2. For every delta_1 in (0,1) and delta_2>0 there exist epsilon_1>0 and 0<c<C<infinity such that, for every sufficiently large d, with probability at least 1-delta_1 there is a time T in [c log(d),C log(d)] satisfying
\[
|m_u(T)|\ge\epsilon_1,\qquad
\sup_{0\le t\le T}|m_v(t)|\le d^{-1/2+\delta_2}.
\]

4. **Nonnegative quadratic coefficient.** If C_2>=0, then for every deterministic sequence t_d>=0 with t_d=o(sqrt(d)), there exists a deterministic sequence A_d>0 tending to zero such that
\[
\mathbb P\left\{\sup_{0\le t\le t_d}
\max\bigl(|m_u(t)|,|m_v(t)|\bigr)\le A_d\right\}\longrightarrow1.
\]

The time T in the first three assertions may depend on the trajectory. For the unrescaled flow dot(w)=-(I_d-ww^top/d)grad R(w), the same trajectory is traversed with time tau=d t. Thus the logarithmic intervals become intervals of order d log(d), and the fourth assertion applies to unrescaled horizons o(d^(3/2)).
