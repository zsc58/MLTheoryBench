# Reference Proof

## Contract and coefficient conventions

The latent law and activation are fixed as dimension varies. The spike directions are fixed, orthogonal, and have norm sqrt(d). Put e_u=u^star/sqrt(d), e_v=v^star/sqrt(d), kappa=E[nu^2], and eta=(1+kappa)^(-1/2). The specified whitening matrix is the identity on e_v-perpendicular and multiplies e_v by eta. Thus the data coordinates in the two spike directions are

U=lambda+Z_u,    V=eta(nu+Z_v),

where Z_u,Z_v are independent standard Gaussians, independent of the latents. All remaining coordinates are independent standard Gaussians.

Throughout this proof, C_ij means a literal monomial coefficient of F. The named source quantities therefore have the public normalizations

C2=2C_20,    C3=2C_21,    C_(3,1)=6C_31,    C_(2,2)=4C_22.

In particular, C3 is not C_30. The third regime's inequality is equivalent to C_22>C_20.

## 1. Covariance and the linear minimizers

Let q=E[lambda^2]. The likelihood-ratio L2 hypothesis implies finite polynomial moments of U,V by Cauchy-Schwarz against Gaussian measure. The additive-noise representations then give finite latent moments as well. Since a centered almost-surely constant lambda would equal zero and be independent of nu, dependence of the latents implies q>0.

Centering, whitening, and E[lambda nu]=0 give

Sigma=E[xx^T]=I_d+q e_u e_u^T.

Its leading eigenvalue is 1+q and its leading eigenspace is span(e_u).

For sigma=id, expansion of the squared error gives

R_lin(w)=Tr(Sigma)-2w^T Sigma w/d+||w||^2 w^T Sigma w/d^2.

For a unit direction e, write w=sqrt(d) r e. Then

R_lin(w)=Tr(Sigma)+(r^4-2r^2)e^T Sigma e.

Positive definiteness makes the directional quadratic form positive, so the optimal radial value is r^2=1. Rayleigh-Ritz, in the form max_{||e||=1} e^T Sigma e=lambda_max(Sigma), with equality exactly on the leading eigenspace, applies to this finite real symmetric matrix. Consequently the minimizers are exactly w=plus or minus u^star. Their overlap with v^star is zero. The same conclusion holds when minimization is restricted from the outset to the stated sphere.

The general source statement needs an exception only when Sigma=0: then every weight minimizes the identically zero risk. For a nonzero singular Sigma, kernel directions are not global minimizers because their risk Tr(Sigma) exceeds Tr(Sigma)-lambda_max(Sigma).

## 2. Hermite reduction and the coefficient facts

Let gamma_j denote standard Gaussian measure in j dimensions, and define f(z)=sigma(z)^2-2z sigma(z). The activation assumptions give f in L2(gamma_1). The data likelihood ratio factors through the two spike coordinates; write it as ell in L2(gamma_2). Define probabilists' Hermite polynomials by

exp(tz-t^2/2)=sum_{k>=0} He_k(z)t^k/k!,

and set

a_k=E[f(G)He_k(G)],

b_ij=E[ell(G_1,G_2)He_i(G_1)He_j(G_2)]
    =E[He_i(U)He_j(V)].

The Gaussian expectations here use independent standard G_1,G_2, and the final expectation uses the data coordinates U,V.

For jointly standard Gaussian X,Y,Z with E[XY]=0, E[XZ]=rho_1, and E[YZ]=rho_2, Gaussian regression and the generating function give

E[He_i(X)He_j(Y) exp(tZ-t^2/2)]
=t^(i+j)rho_1^i rho_2^j.

Matching coefficients proves

E[He_i(X)He_j(Y)He_k(Z)]
=1_{k=i+j} k! rho_1^i rho_2^j.

For s=w/sqrt(d), the reconstruction loss on the sphere is

R(w)=E||x||^2+E[f(s^T x)].

Under the Gaussian reference measure, (e_u^T x,e_v^T x,s^T x) has the preceding Gaussian structure with rho_1=m_u and rho_2=m_v. Expanding ell and f in their Hermite bases and applying the contraction yields

C_ij=b_ij a_{i+j}/(i!j!),    i+j>=1,

with the constant term absorbed into C0. The calculation first holds for finite Hermite sums and extends by L2 approximation, since conditional expectation is an L2 contraction.

For completeness, absolute convergence follows from

sum_{i,j>=0} |b_ij a_{i+j} m_u^i m_v^j|/(i!j!)
<= (sum b_ij^2/(i!j!))^(1/2)
   (sum_{k>=0} a_k^2(m_u^2+m_v^2)^k/k!)^(1/2).

Both factors are finite on the feasible disk m_u^2+m_v^2<=1 by Parseval. Applying the same estimate to total-degree tails proves uniform absolute convergence there. On every smaller disk the geometric factor also controls differentiated series of every fixed order, giving analyticity near the origin. This justifies the local remainders used below; the public C4 assumption is retained.

The first moments and whitened covariance give

b_10=b_01=b_11=b_02=0.

Hence

C_10=C_01=C_11=C_02=0.

No assumption forces every cubic coefficient to vanish. In particular C_30, C_12, and C_03 may be present even when C_21=0.

The latent-moment identity can also be checked directly. Conditional on lambda,

E[exp(t(lambda+Z_u)-t^2/2)|lambda]=exp(t lambda),

so E[He_p(lambda+Z_u)|lambda]=lambda^p. Conditioning on both latents and on the independent Z_v gives

b_{p,1}=eta E[He_p(lambda+Z_u)nu]
       =eta E[lambda^p nu].

The expectations are integrable: the L2 density implies all polynomial moments of U,V, and inequalities applied to lambda=U-Z_u and nu=eta^(-1)V-Z_v give all polynomial latent moments. Thus these conditioning and polynomial expectation steps are legitimate. The factor eta must not be omitted.

## 3. Exact overlap flow and initialization

For the d-rescaled spherical flow, differentiation and orthogonal projection give exactly

u_dot=-F_u+u(uF_u+vF_v),

v_dot=-F_v+v(uF_u+vF_v),

where u=m_u and v=m_v. These formulas use the extension F of the spherical risk; its projected derivative is independent of the extension off the sphere.

Uniform spherical initialization can be represented by

w(0)=sqrt(d) G/||G||,

with G standard Gaussian in dimension d. In an orthonormal basis beginning with e_u,e_v,

u(0)=G_1/||G||,    v(0)=G_2/||G||.

For every fixed epsilon>0, both absolute overlaps lie between d^(-1/2-epsilon) and d^(-1/2+epsilon) with probability tending to one. The upper bounds follow from Gaussian tails and norm concentration; the lower bounds follow from the Gaussian density bound near zero and norm concentration.

Moreover, for every Gamma>0,

P(|v(0)|>Gamma|u(0)|)=(2/pi)arctan(1/Gamma).

This follows because the common normalization cancels and the angle of (G_1,G_2) is uniform. Thus, given a fixed failure tolerance, Gamma can be chosen independently of d to make this probability small. It is incorrect to claim that a fixed Gamma makes this probability tend to zero as d grows.

## 4. A common local exit estimate

Suppose C2<0. Set A=C_20 and a=-2A=-C2>0. The coefficient vanishings and the exact flow imply, locally,

u_dot=a u+O((|u|+|v|)^2),

v_dot=g(u)+h(u,v)v,

where

g(u)=-F_v(u,0),    |h(u,v)|<=K(|u|+|v|).

Indeed, define h by the integral of the v-derivative of the second vector-field component along the segment from (u,0) to (u,v). That derivative vanishes at the origin, giving the bound. Analyticity gives

g(u)=-C_21 u^2-C_31 u^3+O(u^4).

When every C_{p,1}, p>=1, vanishes, centering also gives C_01=0, so g is identically zero locally.

Fix Gamma>=1. On an initialization event with u(0) nonzero and |v(0)|<Gamma|u(0)|, let s=sign(u(0)) and x=s u. Choose a sufficiently small constant epsilon>0, depending on Gamma and the fixed model, and consider the cone

0<x<epsilon,    |v|<Gamma x.

Within it, the local equations give

(a/2)x<=x_dot<=(3a/2)x,

|v_dot|<=K_Gamma x^2.

At either boundary |v|=Gamma x, the upper derivative of |v|-Gamma x is at most

K_Gamma x^2-Gamma(a/2)x<0

when epsilon is small enough. Also x cannot reach zero because x_dot>0. The first exit therefore occurs at x(T)=epsilon. Integration gives

(2/(3a)) log(epsilon/x(0))<=T<=(2/a) log(epsilon/x(0)).

The initialization estimates make this a logarithmic stopping time with the required fixed confidence for all sufficiently large d. Constants and thresholds are selected after the confidence tolerance, not before it.

The same inequalities give the dimension-independent bounds

integral_0^T x(t) dt<=2epsilon/a,

integral_0^T x(t)^k dt>=2(epsilon^k-x(0)^k)/(3ak),    k>=1.

Since |h(sx,v)|<=K_Gamma x, the primitive H(t)=integral_0^t h(u(r),v(r))dr satisfies |H(t)|<=M_Gamma throughout [0,T], for a dimension-independent constant M_Gamma. The exact variation-of-constants formula is

v(t)=exp(H(t))[v(0)+integral_0^t exp(-H(r))g(sx(r))dr].

This estimate retains all permitted cubic terms and replaces the source's unjustified pointwise contraction assertions.

## 5. The two forcing regimes

If C3 is nonzero, then C_21 is nonzero. For sufficiently small epsilon, g(sx) has constant sign for 0<x<=epsilon and

|g(sx)|>=gamma x^2

for some gamma>0, for either s. If C3=0 but C_(3,1) is nonzero, the same assertion holds with x^3 in place of x^2, since C_21=0 and C_31 is nonzero. Its sign may depend on s, which is harmless because recovery uses absolute overlaps.

Let k=2 or 3 respectively. The integrating-factor formula and the integral lower bound yield

|v(T)|>=exp(-2M_Gamma) gamma 2(epsilon^k-x(0)^k)/(3ak)
          -exp(M_Gamma)|v(0)|.

On the initialization event, x(0) and v(0) tend to zero. Therefore the right-hand side is eventually bounded below by a positive dimension-independent constant. Simultaneously |u(T)|=epsilon and T lies between positive constant multiples of log d. Choosing the ratio event and the initialization event with total failure at most the prescribed tolerance proves both positive regimes.

## 6. The no-direct-forcing regime

When every direct C_{p,1} vanishes, g=0. The integrating-factor formula immediately gives

sup_{0<=t<=T}|v(t)|<=exp(M_Gamma)|v(0)|.

For every delta2>0, the initialization bound |v(0)|<=d^(-1/2+delta2/2) holds with probability tending to one. The fixed amplification factor is eventually at most d^(delta2/2), proving

sup_{0<=t<=T}|v(t)|<=d^(-1/2+delta2).

Meanwhile |u(T)|=epsilon and T is logarithmic by the common exit estimate. Selecting Gamma for the requested delta1 proves the stated probability bound.

The source condition C_(2,2)>2C2 is retained. A stronger pointwise claim that v must be monotonically attracted to zero does not follow from that condition, because C_12 may be nonzero. Such monotonicity is unnecessary: bounded integrated amplification proves exactly the required random-scale conclusion before the first u-exit. No behavior after that exit is asserted.

## 7. The nonnegative-quadratic regime

Suppose C2>=0, equivalently A>=0. Let M(t)=max(|u(t)|,|v(t)|). The coefficient vanishings give

u_dot=-2A u+O(M^2),    v_dot=O(M^2).

The linear term cannot increase |u|. Thus, while M is in a fixed sufficiently small neighborhood, its upper right Dini derivative satisfies

D^+ M<=K M^2.

The scalar comparison bound is

M(t)<=M(0)/(1-K M(0)t)

as long as the denominator is positive and the trajectory stays in that neighborhood.

Fix any deterministic t_d=o(sqrt(d)). Choose B_d tending to infinity so slowly that B_d/sqrt(d) tends to zero and B_d t_d/sqrt(d) tends to zero. Gaussian initialization gives M(0)<=B_d/sqrt(d) with probability tending to one. On this event, scalar comparison and continuation give, for all sufficiently large d,

sup_{0<=t<=t_d}M(t)<=2B_d/sqrt(d)=:A_d.

Since A_d tends to zero, the fourth regime follows, including the boundary C2=0.

## 8. Time normalization and obligation closure

If w_res solves the d-rescaled flow and w_un solves the unrescaled flow from the same initialization, then w_un(tau)=w_res(tau/d). Thus logarithmic rescaled times become times of order d log d, and rescaled horizons o(sqrt(d)) become unrescaled horizons o(d^(3/2)).

Every theorem-critical obligation is derived above. Rayleigh-Ritz is the only external theorem used for closure, and its statement and hypotheses are explicit. The Gaussian generating-function, Parseval, conditioning, cone, integrating-factor, and scalar-comparison calculations are supplied rather than replaced by citations. No unresolved GT obligation remains.
