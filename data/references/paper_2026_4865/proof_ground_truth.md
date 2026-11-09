# Reference Proof

## Proof Structure

Choose one smooth score field for each dimension and target mean, independently of p and T. It has a contracting Ornstein-Uhlenbeck drift near the origin and equals the shifted-Gaussian score outside a shell. Establish global Lipschitz continuity and SDE well-posedness. Prove a unit-interval Gaussian stochastic-integral tail using metric entropy and Gaussian concentration, then combine Gaussian grid values with Brownian-scaled local increments to control the OU convolution over an exponential horizon. Couple the diffusion to the OU process until exit. Gaussian norm concentration and a measurable separating event give the TV bound; a pointwise error bound and the small target mass of the modified region give the Lp bound.

## Standard Results Used

The following are the standard independent inputs stated in the source.

1. Gaussian norm concentration: there are universal a>0 and C_g>=1 such that, for Y~N(0,I_d) and r>0,

   P(| ||Y||-sqrt(d) |>=r sqrt(d))<=C_g exp(-a r^2 d).

2. Dudley's inequality: for a separable centered Gaussian process F indexed by a set with canonical pseudometric delta(z,w)=(E|F_z-F_w|^2)^(1/2),

   E sup_z F_z <= C_D integral_0^D sqrt(log N(epsilon)) d epsilon,

   whenever the entropy integral is finite; D is the canonical diameter and N(epsilon) is its covering number.

3. Borell-TIS: for a separable, almost surely bounded centered Gaussian process, with m=E sup F and sigma^2=sup E F_z^2,

   P(sup F>m+u)<=exp(-u^2/(2 sigma^2)),  u>0.

4. A globally Lipschitz drift with a constant diffusion coefficient gives a unique non-explosive strong solution for an initial random variable independent of the Brownian motion. In particular this applies to the Gaussian initialization here. Global Lipschitz continuity implies the required linear growth bound.

We also use Ito isometry, independent Brownian increments, Brownian scaling, and the explicit integrating-factor solution of a linear SDE. All their uses below involve deterministic square-integrable integrands on finite intervals.

## 1. Unit-Interval Noise Bound

Let G_t=integral_0^t exp(s)dB_s for 0<=t<=1 and F_{t,u}=u dot G_t for u in S^{d-1}. These variables form a centered Gaussian process. The stochastic integral has continuous paths, so F has jointly continuous sample paths on the compact index set [0,1] x S^{d-1}. It is therefore separable and almost surely bounded.

For s<=t, orthogonality of the integrals over [0,s] and [s,t] gives

E|F_{t,u}-F_{s,v}|^2
=||u-v||^2 integral_0^s exp(2r)dr + integral_s^t exp(2r)dr
<=8(||u-v||^2+|t-s|).

Thus the canonical metric is bounded by sqrt(8)(||u-v||+|t-s|^(1/2)), and its diameter is bounded by a universal constant D. A maximal separated set on the sphere, with disjoint Euclidean balls around its points, gives a sphere covering bound (1+2/r)^d at radius r. A time mesh of spacing proportional to epsilon^2 has at most C/epsilon^2 points. Combining the two nets gives

N(epsilon)<=(M/epsilon)^(d+2)

for 0<epsilon<=D and a sufficiently large universal M>D. Consequently Dudley's inequality gives

E sup_{0<=t<=1}||G_t||
=E sup_{t,u} F_{t,u}
<=C_D sqrt(d+2) integral_0^D sqrt(log(M/epsilon)) d epsilon
<=K_0 sqrt(d),

where the integral is finite and K_0 is universal. Moreover

sup_{t,u} E F_{t,u}^2=(exp(2)-1)/2<4.

Borell-TIS with u=sqrt(d) therefore implies, with K=K_0+1 and b_0=1/8,

P(sup_{0<=t<=1}||G_t||>K sqrt(d))<=exp(-b_0 d).

This proves the required unit-interval estimate with its hypotheses checked.

## 2. Exponential-Horizon OU Convolution Bound

For alpha>=1 define

Z_t=integral_0^t exp(-alpha(t-s))dB_s.

Its distribution at each fixed t is N(0,v_t I_d), where

v_t=(1-exp(-2alpha t))/(2alpha)<=1/(2alpha).

Choose a universal alpha_0 large enough that 0.03 sqrt(2alpha_0)>1 and

a(0.03 sqrt(2alpha_0)-1)^2>=2.

Gaussian norm concentration then gives, for every alpha>=alpha_0 and all universally sufficiently large d,

P(||Z_t||>0.03 sqrt(d))<=C_g exp(-2d)<=exp(-d),

uniformly in t. At t=0 the probability is zero. Increase alpha_0 further so that

alpha_0>=(K/0.04)^2.

Let b=min(1,b_0), and choose a universal c>0 such that

c<=min(b/4,a/100).

For T>0 with T<=exp(cd/2), partition [0,T] into n=ceil(alpha T) intervals of length at most 1/alpha. Their left endpoints are a_j=j/alpha for 0<=j<n, and

n<=alpha T+1<=2alpha exp(cd/2).

For an interval starting at a_j and 0<=h<=1/alpha, Brownian scaling gives a standard Brownian motion W^{(j)} satisfying

Z_{a_j+h}=exp(-alpha h)Z_{a_j}+R_j(h),

R_j(h)=alpha^(-1/2)exp(-alpha h) integral_0^{alpha h} exp(u)dW^{(j)}_u.

The unit-interval estimate and the choice of alpha_0 imply

P(sup_{0<=h<=1/alpha}||R_j(h)||>0.04 sqrt(d))<=exp(-b_0 d).

This is an unconditional estimate on each local increment; no conditioning on a global grid event or independence between different bad events is required. On a shorter final interval the same estimate holds by restriction. If ||Z_{a_j}||<=0.03 sqrt(d) and the local increment stays below 0.04 sqrt(d), then ||Z||<=0.07 sqrt(d) throughout that interval. Therefore a union bound yields

P(sup_{0<=t<=T}||Z_t||>0.1 sqrt(d))
<=n(exp(-d)+exp(-b_0 d))
<=4alpha exp(-(b-c/2)d).

Since b-3c/2>0, a universal dimension threshold makes the last expression at most 3alpha exp(-cd). For T=0, the event is empty. We have proved this bound uniformly for alpha>=alpha_0 and 0<=T<=exp(cd/2).

Fix alpha=alpha_0 once and for all. This choice is independent of d, mu, p, and T.

## 3. Construction, Lipschitz Control, and Well-Posedness

Choose a fixed smooth scalar function h taking values in [0,1], zero on (-infinity,4] and one on [5,infinity), with bounded first and second derivatives. Such a function can be obtained from eta(r)=exp(-1/r) for r>0 and eta(r)=0 for r<=0 by setting

h(r)=eta(r-4)/(eta(r-4)+eta(5-r)).

For each dimension define chi(u)=h(||u||). It is smooth, including at the origin because it is constant there. On the transition annulus, ||u||>=4; the radial derivative formulas show that its gradient and Hessian operator norm are bounded by a universal constant H. These are the bump properties used by the source.

For ||mu||=7 sqrt(d), put chi_d(x)=chi(x/sqrt(d)) and

hat{s}_{d,mu}(x)=-alpha x+chi_d(x)((alpha-1)x+mu).

Then hat{s}_{d,mu}(x)=-alpha x for ||x||<=4 sqrt(d), and hat{s}_{d,mu}(x)=-(x-mu) for ||x||>=5 sqrt(d). This uses the complement of the cutoff multiplying the inner drift; it repairs the reversed cutoff orientation in the source's displayed shell formula.

The derivative is

D hat{s}_{d,mu}(x)=-alpha I+(alpha-1)chi_d(x)I+((alpha-1)x+mu)(grad chi_d(x))^T.

The last term is supported on the transition shell, where ||x||<=5 sqrt(d), ||mu||=7 sqrt(d), and ||grad chi_d||<=H/sqrt(d). Hence

||D hat{s}_{d,mu}||_op<=alpha+|alpha-1|+H(5|alpha-1|+7)=:L.

Thus L is universal, the field is globally Lipschitz, and all interfaces match smoothly. The standard well-posedness result applies to the corrupted SDE with independent Gaussian initialization. The construction does not involve p or T.

## 4. Confinement and Total Variation

Let A={x:||x||>=4 sqrt(d)} and tau=inf{t>=0:X_t in A}. Couple X to the OU process driven by the same Brownian motion and initial variable. Until tau, uniqueness and the equality of the drifts give

X_t=exp(-alpha t)X_0+sqrt(2)Z_t.

By continuity the formula also holds at a finite first hitting time. If ||X_0||<=1.1 sqrt(d) and tau<=T, then

4 sqrt(d)<=1.1 sqrt(d)+sqrt(2)||Z_tau||,

so ||Z_tau||>2 sqrt(d)>0.1 sqrt(d). Consequently

P(X_T in A)
<=P(||X_0||>1.1 sqrt(d))+P(sup_{0<=t<=T}||Z_t||>0.1 sqrt(d))
<=C_g exp(-ad/100)+3alpha exp(-cd)
<=(C_g+3alpha)exp(-cd).

This holds for every 0<=T<=exp(cd/2) above a universal dimension threshold. At T=0 the same conclusion follows directly from the initial tail bound.

A target sample has the form mu+Y with Y~N(0,I_d). If ||mu+Y||<4 sqrt(d), the reverse triangle inequality gives ||Y||>3 sqrt(d). Thus

pi_tar(A^c)<=C_g exp(-4ad)<=C_g exp(-cd).

Using the Borel event A in the definition of TV gives

TV(L(X_T),pi_tar)
>=pi_tar(A)-P(X_T in A)
>=1-(2C_g+3alpha)exp(-cd).

Take C=2C_g+3alpha and choose a universal integer d_* large enough for all the preceding dimension requirements. This proves the TV conclusion uniformly in mu and T for every d>=d_*.

## 5. Target Lp Score Error

The score error vanishes on ||x||>=5 sqrt(d). Everywhere else,

hat{s}_{d,mu}(x)+(x-mu)=-(1-chi_d(x))((alpha-1)x+mu),

and therefore

||hat{s}_{d,mu}(x)+(x-mu)||
<=||mu||+(alpha+1)||x||
<=[7+5(alpha+1)]sqrt(d)=:D_alpha sqrt(d).

If ||mu+Y||<5 sqrt(d), then ||Y||>2 sqrt(d). Gaussian norm concentration gives

pi_tar(||X||<5 sqrt(d))<=C_g exp(-ad).

It follows for every finite p>=1 that

(E_pi_tar ||hat{s}_{d,mu}-grad log pi_tar||^p)^(1/p)
<=D_alpha C_g^(1/p) sqrt(d) exp(-ad/p).

Choose d_0(p)>=d_* sufficiently large that sqrt(d)<=exp(ad/(2p)) for all d>=d_0(p). With C_p=D_alpha C_g^(1/p) and c_p=a/(2p), the required bound follows. These constants depend only on p, since all other constants have already been fixed universally. The very same family of fields gives all finite-p bounds and all stated time-horizon bounds.

## Obligation Closure

The construction and its dimension-free derivative bound are derived explicitly. SDE well-posedness uses the audited globally Lipschitz result with its hypotheses verified. The unit-interval estimate is derived using the stated Dudley and Borell-TIS inequalities with compactness, separability, boundedness, entropy, and variance checked. The long-horizon bound includes both grid values and local increments, including T=0 and a shorter last interval. Stopped OU coupling, Gaussian tails, the TV comparison, and the fixed-p polynomial absorption are all explicit. No unresolved proof obligation remains.
