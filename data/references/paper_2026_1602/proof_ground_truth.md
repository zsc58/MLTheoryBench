# Reference Proof

## Contract and Obligations

The projection is computed from the exact normalized Gram matrix of K. The augmented feature consists of scalar initialization indicators, its coefficient vector is in R^m, and both parameter blocks are trained. Initialization is independent of the observations. The target is fixed, k0>=1 is fixed, and all constants below may depend on the fixed parameters listed in the task.

We prove, on common events, the harmonic spectrum and gap, initialization concentration, finite-width projected residual recursion, uniform iterate decomposition, RKHS norm control, empirical target-complement bound, empirical clean-error estimate, and localized population transfer. Nonstandard imported concentration and spectral-tail results are not assumed: the consequences needed here are derived below. The only quoted standard independent results are the covariance concentration statement and the fixed-class localized theorem, whose statements and hypotheses are given below.

Put q=d^{k0}/n, L=log(C/delta), G=[K(x_i,x_j)]/n, P=P_{r0}, and A=I-eta GP. Write xi for the noise vector and u_t=f_t(S)-y. Let E be the population harmonic subspace through degree k0.

## 1. Harmonic Structure

Use harmonics orthonormal under the spherical probability measure. The hemisphere indicator has Funk-Hecke coefficients s_0=1/2, s_{2j}=0 for j>=1, and, for j>=1,

s_{2j-1}=(omega_{d-2}/omega_{d-1})2^{-(2j-1)}(-1)^{j-1} Gamma((d-1)/2)Gamma(2j-1)/[Gamma(j)Gamma(j+(d-1)/2)].

Indeed these are obtained by inserting the Rodrigues expression for the normalized Gegenbauer polynomial into the hemisphere integral and integrating its derivative over [0,1]; the endpoint at 1 vanishes and the remaining derivative at 0 gives the displayed Gamma expression. Expanding each hemisphere indicator in harmonics and integrating their product over its uniformly distributed direction shows that the K^(0) harmonic eigenvalues are b_ell=s_ell^2: orthonormality eliminates cross terms.

The identity tP_ell(t)=ell P_{ell-1}(t)/(2ell+d-2)+(ell+d-2)P_{ell+1}(t)/(2ell+d-2) gives the K^(1) eigenvalues

c_0=b_1,

c_ell=ell b_{ell-1}/(2ell+d-2)+(ell+d-2)b_{ell+1}/(2ell+d-2), ell>=1.

Thus mu_ell=b_ell+c_ell. The exact Gamma ratio gives

b_{2j+1}/b_{2j-1}=((2j-1)/(2j+d-1))^2<1.

For even ell>=2, c_ell is strictly between the adjacent positive odd b values; for odd ell>=3, c_ell=0. Also c_1=b_0/d and mu_0=b_0+b_1>mu_1=b_1+b_0/d for d>1. Consequently the augmented eigenvalues are positive and strictly ordered by degree. The fixed-degree Gamma estimates give b_ell asymptotic to d^{-ell} for odd ell and b_0=1/4; the recurrence then gives mu_ell asymptotic to d^{-ell} for every fixed ell. Therefore

r0=sum_{ell<=k0}N(d,ell) asymptotic to d^{k0},

Delta=mu_{k0}-mu_{k0+1} asymptotic to d^{-k0}.

The multiplicity scaling follows directly from the harmonic dimension formula. The target lies in E, has H_K norm at most gamma_0, and satisfies |f*(x)|<=gamma_0 because K(x,x)=1.

## 2. Initialization Concentration Without Specialized Citations

Let M=m/2 be the number of independent Gaussian seeds. Consider the classes of indicators of intersections of two origin halfspaces and of slabs |g^T x|<=R, where R is deterministic. On N points, the number of possible masks is at most (1+2N)^{C d}. To see this, regard x as the parameter: changes of a mask occur on N linear hyperplanes for one gate and 2N affine hyperplanes for a slab. The number of regions satisfies the recurrence obtained by adding the last hyperplane: the newly split regions are controlled by the arrangement induced on that hyperplane in one lower dimension. Including lower-dimensional faces, and multiplying the counts for two gates, gives the stated polynomial bound. Weak inequalities are included by counting faces.

Here is the uniform deviation calculation. Introduce M independent ghost points. For a function witnessing a deviation epsilon from its mean, Chebyshev's inequality gives probability at least one half that its ghost average is within epsilon/2 of that mean, once M epsilon^2 is sufficiently large. Conditional on the doubled sample, exchange independently the two points in each original/ghost pair. The difference of the two empirical averages is now a signed sum of independent bounded terms. The elementary exponential Hoeffding bound followed by a union over the possible masks gives

Pr(sup_f |P_M f-P f|>epsilon)<=4(1+4M)^{C d} exp(-M epsilon^2/8).

The Hoeffding bound follows by multiplying the exponential-moment bounds for the centered bounded summands and optimizing the exponential parameter. Choose

alpha=C sqrt((d log(2+m)+log n)/m).

The Gaussian angle in the plane spanned by u,v is uniform, so the probability that both dot products are nonnegative is (pi-arccos(u^T v))/(2pi). For a slab and unit x, g^T x is standard normal and its probability is at most 2R/sqrt(2pi), by bounding its density by its value at zero. Duplication of paired seeds leaves the empirical averages unchanged. Therefore, except on events totaling 2/n,

sup_{u,v}|hat h_0(u,v)-K^(0)(u,v)|<=alpha,

rho_R:=sup_x m^{-1}sum_r 1{|w_r(0)^T x|<=R}<=C R+alpha.

The width condition m>=C n^{2/d} absorbs log n into C d log m. Hence alpha<=C sqrt(d log m/m). Multiplication by |u^T v|<=1 gives the corresponding K^(1) approximation.

## 3. Projected Finite-Width Dynamics

Choose a deterministic residual envelope c_u larger than a fixed multiple of gamma_0+sigma_0+1 and set R=eta c_u T/sqrt(m). The choices occur before drawing the seeds. Define the private tolerance

tau_*=min{1,sqrt(q),1/(eta T)}.

Since T is comparable to 1/q and eta is fixed, tau_* is comparable to 1/T in the stated regime. It is not an additional algorithm parameter or public assumption.

Conditional on S, independence and the scalar sub-Gaussian moment bound imply that every unit linear combination of xi is sub-Gaussian with proxy sigma_0^2. A maximal half-separated net of the unit sphere in an r-dimensional Euclidean space has at most 5^r points, by disjoint-ball volume comparison, and the norm of a vector is at most twice its largest net inner product. A union of scalar sub-Gaussian tail bounds therefore gives

||xi||<=C sigma_0 sqrt(n)

with failure at most exp(-cn). If sigma_0=0, the moment bound implies xi=0 almost surely and the conclusion is immediate.

Suppose the residual bound holds up to time t. Each first-layer increment satisfies

||w_r(t+1)-w_r(t)||<=eta ||u_t||/(sqrt(nm))<=eta c_u/sqrt(m).

Thus every displacement through T is at most R. A gate can change only if its initial preactivation has absolute value at most R. Expanding one output increment, retaining the scalar augmented-feature update exactly, and replacing the initial gate kernel by K gives

u_{t+1}=A u_t+zeta_{t+1},

||zeta_{t+1}||<=C eta c_u sqrt(n)(alpha+rho_R).

For completeness, the stable ReLU neurons give the current trained-weight tangent Gram contribution. The remaining neurons contribute at most C eta c_u rho_R per coordinate by the increment bound. Replacing current gates by initial gates costs the same order. The scalar augmented-feature Gram contributes hat h_0, while the initial ReLU tangent Gram contributes (x_i^T x_j)hat h_0; their sum differs entrywise from K by at most 2alpha. A normalized matrix with entrywise error at most epsilon has operator norm at most epsilon, proving the displayed recursion estimate.

G is positive semidefinite, tr(G)=1, and 0<eta<1. Since P is a spectral projector of G, ||A||<=1; it equals one on the complementary subspace when that subspace is nonempty. Iteration gives

u_t=-A^t(f*(S)+xi)+e_{2,t},

e_{2,t}=sum_{j=1}^t A^{t-j}zeta_j.

In particular,

||e_{2,t}||/sqrt(n)<=C T(alpha+rho_R).

The estimates alpha<=C sqrt(d log m/m), rho_R<=C T/sqrt(m)+alpha, and m>=C T^{5/3} imply the convenient bound

C T(alpha+rho_R)<=C sqrt(d)m^{-1/5}T^{3/2}.

Here sqrt(log m)m^{-3/10} is bounded, and T^{1/2}m^{-3/10} is bounded under m>=C T^{5/3}. The width term C d^{5/2}T^{25/2}, with a sufficiently large constant, makes this at most tau_*. The ideal residual has norm at most gamma_0 sqrt(n)+||xi||. Increasing c_u closes the residual and movement induction simultaneously for all t<=T. Consequently

||e_{2,t}||<=sqrt(n)tau_*,  ||u_t||<=c_u sqrt(n),  ||w_r(t)-w_r(0)||<=R.

## 4. Uniform Function Decomposition

Linearize the ReLU part at its initial gates and retain the augmented term exactly. The ReLU approximation error is at most

2sqrt(m)R rho_R<=C eta c_u T rho_R

uniformly on the sphere. Substitute the two projected update sums into this approximation. The main initial-feature term is (1+x^T x_j)hat h_0(x,x_j), so define

h_t(x)=-(eta/n)sum_{s<t}sum_j K(x,x_j)[P u_s]_j.

The coefficients lie in range(P), so h_t belongs to the exact empirical leading RKHS subspace. Kernel approximation and gate changes give a further error at most C eta c_u T(alpha+rho_R). Therefore

f_t=h_t+e_t,  ||e_t||_infinity<=C sqrt(d)m^{-1/5}T^{3/2}.

The width term C T^{15/2}d^{5/2}w^{-5} makes this at most w=q. This is a uniform assertion for all t<=T and all inputs.

## 5. Covariance Concentration and Projection Control

The standard independent covariance result used here states the following. For a continuous kernel on a compact domain with sup_x K(x,x)<=1 and i.i.d. observations, the operators on H_K

C=E[K_x tensor K_x],  C_n=n^{-1}sum_i K_{x_i} tensor K_{x_i}

satisfy ||C-C_n||_HS<=2sqrt(2) sqrt(log(2/rho)/n) with probability at least 1-rho. These hypotheses hold: the sphere is compact, K is continuous, K(x,x)=1, and the covariates are i.i.d. The RKHS is separable, for example by continuity of the kernel sections and a countable dense subset of the sphere.

The eigenvalues of C are the harmonic kernel eigenvalues, with H_K-normalized eigenvectors v_j=sqrt(lambda_j)e_j. The nonzero eigenvalues of C_n are the eigenvalues hatlambda_i of G. Eigenvalue perturbation gives |hatlambda_i-lambda_{i-1}|<=||C-C_n||_op. With rho a fixed fraction of delta and n>=C L d^{2k0}, the deviation is at most Delta/4. Thus

hatlambda_{r0}>=c d^{-k0},  hatlambda_{r0+1}<=C d^{-k0}.

Let P_E be the population leading projector on H_K and Q the empirical leading projector there. A direct projection estimate follows from the eigenbasis equation

(lambda_i-hatlambda_j)<v_i,Phi_j>=<v_i,(C-C_n)Phi_j>.

For population-leading and empirical-complementary indices the denominator is at least 3Delta/4. Sum the squared equation over those indices. Bessel's inequality bounds the numerators by ||C-C_n||_HS^2. The reverse cross-sum is equal to the first because both projections have rank r0. Hence

||P_E-Q||_HS^2<=C ||C-C_n||_HS^2/Delta^2<=C L d^{2k0}/n.

It follows that

||(I-Q)f*||_H^2<=C gamma_0^2 L d^{2k0}/n,

||(I-P_E)h||_H^2<=C B^2 L d^{2k0}/n

uniformly for h in range(Q) with ||h||_H<=B. The second assertion concerns h, not an arbitrary bounded perturbation f=h+e.

For an orthonormal empirical RKHS eigenfunction Phi_j, indexed from j=0,

Phi_j(S)=sqrt(n hatlambda_{j+1})U^{[j+1]}.

Its coefficient in any g in H_K is therefore U^{[j+1]T}g(S)/sqrt(n hatlambda_{j+1}). Bessel's inequality gives the interpolation estimate

n^{-1}sum_i |U^{[i]T}g(S)|^2/hatlambda_i<=||g||_H^2.

Likewise,

n^{-1}||(I-P)f*(S)||^2

=sum_{j=r0}^{n-1}hatlambda_{j+1}|<f*,Phi_j>_H|^2

<=hatlambda_{r0+1}||(I-Q)f*||_H^2

<=C gamma_0^2 L q.

## 6. RKHS Norm and Empirical Risk

Conditional on S, the net argument from Section 3, now in range(P), gives ||P xi||^2<=C sigma_0^2 r0 with failure at most exp(-cr0). P depends only on S, not on xi.

Split h_t into its target, noise, and recursion-error accumulations using u_s=-A^s f*(S)-A^s xi+e_{2,s}. In empirical eigen-coordinates, the first two accumulations have multiplier

[1-(1-eta hatlambda_i)^t]/sqrt(n hatlambda_i), i<=r0.

The interpolation estimate bounds the target H_K norm by gamma_0. The noise H_K norm is at most

||P xi||/sqrt(n hatlambda_{r0})<=C sigma_0 sqrt(d^{2k0}/n)<=C.

Each error accumulation has H_K norm at most eta sqrt(hatlambda_1)tau_*. Their sum is at most eta T tau_*<=1. Therefore ||h_t||_H<=B=gamma_0+C uniformly for t<=T.

The clean empirical error is

f_t(S)-f*(S)=-A^t f*(S)+(I-A^t)xi+e_{2,t}.

Orthogonal leading/complement decomposition, followed by the three-term and two-term squared-norm inequalities, gives

P_n(f_t-f*)^2<=3n^{-1}sum_{i<=r0}(1-eta hatlambda_i)^{2t}|U^{[i]T}f*(S)|^2

+3||P xi||^2/n+2||(I-P)f*(S)||^2/n+5tau_*^2.

Since lambda exp(-2eta t lambda)<=1/(2e eta t), the interpolation estimate bounds the first term by 3gamma_0^2/(2e eta t). The other terms have already been controlled, and tau_*^2<=q. Thus, uniformly for t>=1,

P_n(f_t-f*)^2<=C gamma_0^2/(eta t)+C(gamma_0,sigma_0)Lq.

## 7. Localized Population Transfer with a Fixed Class

Do not conditionally apply a fixed-class theorem to a class selected by S. Set

A_H=C B sqrt(L d^{2k0}/n)

and introduce the deterministic class

D={h in H_K: ||h||_H<=B, ||(I-P_E)h||_H<=A_H}.

Every h_t belongs to D on the preceding projection event. This class is fixed before sampling and is separable. For h in D with P(h-f*)^2<=r, decompose h-f*=v+z with v in E and z orthogonal to E. These parts are also orthogonal in L2(P), so ||v||_{L2(P)}<=sqrt(r). If e_1,...,e_{r0} is an orthonormal L2(P) basis of E, Cauchy-Schwarz and Jensen give

R({v:||v||_{L2(P)}<=sqrt(r)})<=sqrt(r) [E sum_j(n^{-1}sum_i sigma_i e_j(x_i))^2]^{1/2}=sqrt(r r0/n).

For the tail, the reproducing identity gives

R({z:||z||_H<=A_H})<=A_H n^{-1}E||sum_i sigma_i K_{x_i}||_H<=A_H/sqrt(n).

Therefore the localized complexity of h-f* is at most

C sqrt(r r0/n)+C sqrt(L)q.

The standard independent localized theorem used here is the fixed-class result stated in the source: for a bounded measurable class G with range [a,b], Var(F)<=T(F)<=B_0' P F, and a sub-root envelope psi satisfying psi(r)>=B_0' R({F:T(F)<=r}), its fixed point r_* gives, for K_0>1 and x>0, simultaneously over G with probability at least 1-exp(-x),

P F<=K_0/(K_0-1)P_n F+(704K_0/B_0')r_*+x[11(b-a)+26B_0'K_0]/n.

Apply it to G={(h-f*)^2:h in D}. RKHS evaluation gives |h-f*|<=B+gamma_0=:B_0. Hence 0<=F<=B_0^2 and Var(F)<=P F^2<=B_0^2 P F. Take T(F)=B_0^2 P F and B_0'=B_0^2. The stated standard contraction inequality, applied to the square map on [-B_0,B_0], verifies a sub-root envelope of the form

psi(r)=C sqrt(L)q+C sqrt(r r0/n).

Its fixed point is at most C(sqrt(L)q+r0/n): insert r_*=psi(r_*) and use C sqrt(r_*r0/n)<=r_*/2+C' r0/n. Choose K_0=3 and x=c r0. The theorem gives, with failure exp(-cr0),

P(h-f*)^2<=(3/2)P_n(h-f*)^2+C sqrt(L)q

uniformly over D. All of its hypotheses have now been verified for a deterministic class.

Finally f_t=h_t+e_t and ||e_t||_infinity<=w<1. Since h_t and f* are uniformly bounded,

|(f_t-f*)^2-(h_t-f*)^2|<=Cw

pointwise. The same inequality holds after either population or empirical averaging. Therefore

P(f_t-f*)^2<=2P_n(f_t-f*)^2+C sqrt(L)q+Cw

simultaneously for all t<=T. The coefficient 2 follows from the preceding coefficient 3/2 and nonnegativity of empirical risk.

## 8. Final Rate, Probability, and Boundary Checks

Use covariance confidence rho equal to a sufficiently small fixed fraction of delta; its one event supplies eigenvalue and projection bounds. The initialization events fail with probability at most 2/n. The full-noise norm event fails with probability exp(-cn), the projected-noise event with exp(-cr0), and the fixed-class transfer event with exp(-cr0). Their union therefore has failure at most delta+exp(-cn)+2exp(-cr0)+2/n. All events are shared across time, so no union over T is needed.

For integer t in [c_tT,T], t>=1 and 1/(eta t)<=C q, with C depending on the fixed eta,c_t and horizon comparison constants. Combining the empirical bound, population transfer, w=q, and sqrt(L)<=C L yields

P(f_t-f*)^2<=C_1 log(4/delta)d^{k0}/n

on that event, simultaneously for every specified iterate.

Choose the constants and dimension threshold so that n>r0 and w<1; these follow from n>=C_0 log(4/delta)d^{2k0}, fixed k0>=1, and sufficiently large d. Zero noise is covered separately by its moment bound. The positive target-radius assumption is restored from the source, while a zero target itself is allowed. Initialization at ReLU boundaries and spectral ties are covered by the task's explicit conventions. The width ensures the privately chosen tolerance; no assertion is made for arbitrary smaller tolerances.

For any epsilon>0, the two sample-size requirements in the task respectively ensure applicability and C_1 log(4/delta)d^{k0}/n<=epsilon, after increasing C_2. Since delta<1/2, log(4/delta) and log(1/delta) differ by only an absolute constant factor. The other stated width and horizon requirements remain in force. This proves the sample-complexity consequence with the same probability bound.

## Proof Completeness

No selected-chain obligation is left open. The full exact-constant nonstandard imported statements are not asserted as independently proved; their only needed consequences were replaced by explicit derivations. No minimax lower bound or adaptive-degree claim is part of this proof.
