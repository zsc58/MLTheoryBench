# Reference Proof

## Obligations and conventions

The obligations are: (1) global flow, invariance, and moment control; (2) joint-KL conservation and marginal-KL control; (3) the weighted average-KL estimate, including its regular-case derivation and approximation passage; (4) triangular-time contraction; (5) exponential-time contraction; and (6) iteration, boundary cases, and time complexity. Each is proved below.

During one deterministic Hamiltonian segment write eta_t for the phase law and p_t for its position marginal. This distinguishes continuous segment time from the algorithm's iteration-indexed laws mu_k. Put H_0=KL(p_0||nu), h(t)=KL(p_t||nu), and W(t)=W_2^2(p_t,nu)/2.

We use the following standard independent transport facts, in precisely the form recorded in theory_013. For absolutely continuous probability laws p and nu with finite second moments, the quadratic optimal transport from p to nu is R=grad phi for a convex potential. Its distributional derivative is a positive-semidefinite matrix-valued Radon measure, locally finite, with decomposition DR=G dx+N sigma, where both G and N are positive semidefinite and sigma is a positive singular measure. When both densities are positive, the Monge-Ampere identity is p(x)=nu(R(x)) det G(x) for p-almost every x; in particular G is positive definite there. In our applications p and nu have positive densities on all of R^d and finite second moments, so these hypotheses hold. Integration by parts against compactly supported C^1 matrix fields follows from the definition of this distributional derivative, by smooth approximation of the test field.

We also use the probability facts recorded in theory_016: the KL chain rule, convexity under mixtures, weak lower semicontinuity of KL in both arguments, and equivalence of W_2 convergence with weak convergence plus second-moment convergence. The first two follow by density factorization and convexity of s log s. The lower semicontinuity follows from the variational formula KL(P||Q)=sup_g{integral g dP-log integral exp(g) dQ}, with bounded continuous g. All uses below involve probability laws and explicitly established weak or W_2 convergence. No paper-specific entropy-decay or second-variation theorem is assumed.

## step_001: Flow, invariance, and moments

The vector field b(x,y)=(y,-grad f(x)) is C^1 and globally (1+L)-Lipschitz. Global ODE existence and uniqueness give a C^1 flow Phi_t, inverse Phi_{-t}, and the estimate

||Phi_t(z)-Phi_t(z')|| <= exp((1+L)|t|)||z-z'||.

Along this flow, the derivative of f(x_t)+||y_t||^2/2 is zero. Also div b=0. The Jacobian equation therefore gives d(det D Phi_t)/dt=(div b)(Phi_t) det D Phi_t=0 and det D Phi_0=1. Thus Phi_t preserves volume and the probability law pi=nu tensor gamma.

We need a moment estimate that can be integrated against arbitrarily long exponential times; the exponential-in-time Lipschitz estimate alone is insufficient for that purpose. Smoothness gives

Z >= exp(-f(x)+||grad f(x)||^2/(2L))(2 pi/L)^(d/2).

This follows by integrating exp(-f(x)-grad f(x) dot (u-x)-L||u-x||^2/2) over u. Consequently f has a finite lower bound m. Also |f(x)|<=A(1+||x||^2) for a finite A, by the bounded Hessian. For a phase initialization with finite second moment, B=E[f(X_0)+||Y_0||^2/2-m] is finite and nonnegative. Conservation of energy gives

E||Y_t||^2 <= 2B,
E||X_t||^2 <= 2E||X_0||^2+4t^2 B.

The second inequality follows from X_t=X_0+integral_0^t Y_s ds and Cauchy-Schwarz. A C^1 diffeomorphism preserves absolute continuity and positivity almost everywhere; projecting its positive phase density gives a positive position density. Thus all finite-time position marginals are admissible. Mixtures over either prescribed time distribution have finite second moment because those distributions have finite second moments. Positivity and absolute continuity persist under these mixtures as well.

## step_002: KL control and continuity

Volume preservation and invariance of pi imply

d eta_t/d pi = (d eta_0/d pi) composed with Phi_{-t}.

Changing variables in the relative-entropy integral proves KL(eta_t||pi)=KL(eta_0||pi), without subtracting potentially undefined differential entropies. For eta_0=p_0 tensor gamma this equals H_0. Disintegrating eta_t gives

H_0=h(t)+integral KL(eta_t(dy|x)||gamma) p_t(dx).

In particular 0<=h(t)<=H_0. This is domination by the initial KL, not a claim that h(t) is monotone in t. Convexity also gives KL(integral p_t D(dt)||nu)<=H_0 for any independent random time D.

The laws eta_t and p_t are weakly continuous by the continuous flow and bounded convergence. Hence p_t tensor gamma is weakly continuous. Both terms in the preceding chain-rule identity are lower semicontinuous in t. Their sum is the finite constant H_0, so both are continuous. Thus h is continuous. The energy bounds give L^2 continuity of X_t on finite intervals, and therefore W_2 continuity of p_t and continuity of W(t).

## step_003: Derivation of the average-KL estimate

### Temporary regular initialization

First suppose q_0=p_0/nu is C^1, its gradient is bounded, and 0<zeta<=q_0<=xi<infinity. These are temporary proof assumptions, not public hypotheses.

Invariance gives the phase relative density

g_t(x,y)=d eta_t/d pi(x,y)=q_0(Phi_{-t}^X(x,y)).

Define q_t(x)=integral g_t(x,y) gamma(dy), j_t(x)=integral y g_t(x,y) gamma(dy), and B_t(x)=integral yy^T g_t(x,y) gamma(dy). Then p_t=q_t nu, the conditional velocity mean is u_t=j_t/q_t, the conditional second moment is B_t/q_t, and the conditional covariance is Sigma_t=B_t/q_t-u_t u_t^T.

On each fixed finite time interval, zeta<=g_t,q_t<=xi. The flow derivative bound gives bounded spatial derivatives of g_t, whereas |partial_t g_t(x,y)|<=A_T(1+||x||+||y||). Differentiation under the Gaussian integrals is therefore justified, locally uniformly in x and t, including for the first two conditional moments. It follows that p_t,u_t,Sigma_t are C^1; u_t, its spatial derivative, and Sigma_t are bounded on that interval; and |partial_t u_t(x)|<=A_T(1+||x||). In particular

a_t=partial_t u_t+(D u_t)u_t

is continuous and |a_t(x)|<=A_T(1+||x||). The conditional density relative to gamma is g_t/q_t, bounded above and below by positive constants. Its covariance is positive definite and its Gaussian relative entropy is finite.

Differentiating expectations of compactly supported scalar test functions of X_t, and vector test functions paired with Y_t, gives the continuity and momentum equations

partial_t p_t+div(p_t u_t)=0,
partial_t(p_t u_t)+div(p_t(u_t u_t^T+Sigma_t))+p_t grad f=0.

The energy bounds justify Fubini and differentiation in these weak identities. All their terms are continuous under the regular initialization, so the identities hold classically. Subtracting u_t times the first equation from the second gives

a_t=-grad f-p_t^(-1) div(p_t Sigma_t).

### Characteristic flow and upper second variation

Let Xi_t solve dot Xi_t=u_t(Xi_t), Xi_0=id. Boundedness and the bounded spatial derivative of u give a global characteristic flow on every finite time interval. Along its characteristics, the continuity equation gives

p_t(Xi_t(x)) det D Xi_t(x)=p_0(x),

so (Xi_t)_#p_0=p_t. Moreover |Xi_t(x)-x|<=A_T T. The acceleration bound supplies an L^2(p_0) dominating function A_T(1+||x||), and continuity supplies pointwise convergence. The integral forms of the characteristic equation and its derivative consequently yield

(Xi_{t+h}-Xi_t)/h -> u_t composed with Xi_t,
(Xi_{t+h}+Xi_{t-h}-2Xi_t)/h^2 -> a_t composed with Xi_t

in L^2(p_0), at each interior t. These follow directly by dominated convergence applied to the first-difference integral and to the triangular-kernel average of a_{t+s}(Xi_{t+s}).

Let R_t be the Brenier map from p_t to nu and v_t=id-R_t. The couplings (Xi_{t+h},R_t composed with Xi_t)_#p_0 and (Xi_{t-h},R_t composed with Xi_t)_#p_0 are admissible for the nearby marginals. Expanding their squared costs, and using optimality at time t, gives

limsup_{h->0} [W(t+h)+W(t-h)-2W(t)]/h^2
<= integral (||u_t||^2+v_t dot a_t) p_t.

Indeed, the two squared first differences contribute integral ||u_t||^2 p_t after division by 2h^2, and the central second difference paired with v_t contributes integral v_t dot a_t p_t. The L^2 limits justify both passages because integral ||v_t||^2 p_t=W_2^2(p_t,nu)<infinity.

At time zero u_0=0. Integrating the L^2 acceleration bound twice gives ||Xi_t-id||_{L^2(p_0)}=O(t^2). Therefore W_2(p_t,p_0)=O(t^2), and the triangle inequality implies W(t)-W(0)=O(t^2). In particular W'_+(0)=0. This proves the endpoint fact needed below without invoking a specialized Wasserstein differentiability result.

### Integration by parts and the conditional entropy estimate

Fix an interior time and temporarily suppress its subscript. Choose a smooth nonincreasing eta on [0,infinity), equal to 1 on [0,1] and 0 on [4,infinity). Such a function is obtained by integrating a nonnegative smooth bump supported in (1,4) and normalizing its integral. Put chi_R(x)=eta(||x||^2/R^2). Then chi_R increases to 1, is compactly supported, and ||grad chi_R||<=A/R with derivative supported on R<=||x||<=2R. No compact support of eta on the negative half-line is required or possible together with global monotonicity.

Write DR=G dx+N sigma for the distributional Hessian of the Brenier potential. Thus Dv=(I-G)dx-N sigma. Integration by parts against chi_R p Sigma gives

-integral v dot div(chi_R p Sigma)
= integral chi_R p tr((I-G)Sigma) dx - integral chi_R p tr(N Sigma) d sigma
<= integral chi_R p tr((I-G)Sigma) dx.

The singular contribution is nonpositive because N and Sigma are positive semidefinite. Replacing chi_R div(p Sigma) by div(chi_R p Sigma)-p Sigma grad chi_R incurs a boundary error whose absolute value is at most

(A/R)(integral_{||x||>=R} ||v||^2 p)^(1/2)(integral_{||x||>=R} ||Sigma||_op^2 p)^(1/2),

which tends to zero. Here v is square-integrable, Sigma is bounded, and p is a probability density. Also v dot a and v dot grad f are integrable by Cauchy-Schwarz, the linear growth bounds, and the finite second moments.

Let k(x)=KL(eta_t(dy|x)||gamma). Gaussian maximum entropy, or equivalently nonnegativity of relative entropy to the Gaussian with the same mean and covariance, gives

2k(x)>=||u(x)||^2+tr Sigma(x)-log det Sigma(x)-d.

To verify this directly, expand KL of the conditional law to gamma and to N(u,Sigma); subtracting cancels its differential entropy and leaves half the displayed quadratic/covariance expression. All terms are finite here because the conditional density is bounded above and below relative to gamma.

For positive definite matrices G and Sigma, applying lambda>=1+log lambda to the eigenvalues of Sigma^(1/2) G Sigma^(1/2) gives

tr(G Sigma)>=d+log det G+log det Sigma.

The Monge-Ampere identity gives

log det G=log(p/nu)+f(R)-f(x).

Finally, semi-convexity gives

-grad f(x) dot v(x)<=f(R(x))-f(x)+(M/2)||v(x)||^2.

Combining the last four displays yields, almost everywhere,

||u||^2+tr((I-G)Sigma)-grad f dot v
<=2k-log(p/nu)+(M/2)||v||^2.

Multiply this inequality by chi_R p and combine it with the cutoff integration by parts. Pass to the limit only after this combination. The left-hand side involving ||u||^2+v dot a converges by integrability and the vanishing absolute boundary error. On the right, k is integrable by the chain rule, log(p/nu) is bounded under regular initialization, and v is square-integrable. Thus

integral (||u_t||^2+v_t dot a_t) p_t
<=2H_0-3h(t)+M W(t).

This limiting argument does not assume global integrability of an unweighted Brenier Hessian.

### Twice integrating the second-difference inequality

For every fixed t in (0,T) we have established

limsup_{h->0} [W(t+h)+W(t-h)-2W(t)]/h^2
<=2H_0-3h(t)+M W(t).

The right-hand side is continuous. Define

F(t)=W(t)-integral_0^t (t-s)[2H_0-3h(s)+M W(s)] ds.

Then F is continuous and its upper symmetric second derivative is at most zero at every interior point. This implies concavity. For completeness, if F lies below a chord on some interval [a,b], adding a sufficiently small positive multiple of (t-a)(b-t) to F minus that chord leaves a negative interior minimum. At that minimum the symmetric second difference of F is at least 2c h^2 for some c>0, a contradiction. This proves the required concavity criterion directly.

The integral term has right derivative zero at zero, and W'_+(0)=0. Hence F'_+(0)=0. Concavity gives F(T)<=F(0), which expands to

W(T)+3 integral_0^T (T-t)h(t) dt-M integral_0^T (T-t)W(t) dt
<=W(0)+T^2 H_0.                                           (A)

The case T=0 is equality.

### Removing the temporary regularity assumption

We reconstruct the approximation rather than assume this internal result. Let q=p_0/nu. Truncate by bar q_n=min(q,n) 1_{||x||<=n} and normalize by m_n=integral bar q_n dnu. Then m_n increases to 1, and the resulting probability densities hat p_n=(bar q_n/m_n)nu converge to p_0 in weighted L^1 with weight 1+||x||^2. This follows from bar q_n<=q and dominated convergence, followed by normalization. Consequently they converge in W_2.

Their KL values converge as well: with psi(s)=s log s and psi(0)=0,

KL(hat p_n||nu)=m_n^(-1) integral psi(bar q_n) dnu-log m_n.

The positive parts converge by domination by psi(q)_+, and the negative parts by |psi(s)_-|<=1/e. Both limiting integrals are finite because H_0 is finite.

For each fixed n, convolve hat p_n with a nonnegative smooth compactly supported approximate identity of radius delta. As delta tends to zero, the convolution converges in L^1, with all supports in the fixed ball of radius n+1 for delta<1. Thus it converges in W_2. Its entropy integral converges: convolution and Jensen give the upper bound for integral p log p, while weak lower semicontinuity of KL relative to the uniform law on that fixed ball gives the lower bound. The potential integral converges because f is continuous and bounded on the ball. Hence KL to nu converges. The convolved density divided by the positive C^2 density nu is C^1 with compact support and bounded derivative. Choose a diagonal sequence tilde p_n preserving W_2 and KL convergence to p_0.

Finally set p_{0,n}=(1-zeta_n)tilde p_n+zeta_n nu with zeta_n>0 sufficiently small. The relative density is C^1 with bounded derivative and positive lower and finite upper bounds. For fixed n,

W_2^2((1-zeta)tilde p_n+zeta nu,tilde p_n)<=zeta W_2^2(nu,tilde p_n),
KL((1-zeta)tilde p_n+zeta nu||nu)<=(1-zeta)KL(tilde p_n||nu).

Lower semicontinuity supplies the reverse limiting KL inequality. Choosing another diagonal sequence gives W_2(p_{0,n},p_0)->0 and KL(p_{0,n}||nu)->H_0.

Couple p_{0,n} and p_0 optimally and use the same independent Gaussian initial velocity in both flows. For each finite T,

sup_{0<=t<=T} W_2(p_{t,n},p_t)<=exp((1+L)T) W_2(p_{0,n},p_0)->0.

The triangle inequality then gives uniform convergence of W_2^2(p_{t,n},nu) to W_2^2(p_t,nu) on [0,T]; these distances are uniformly bounded there. In particular both the endpoint term and the negative integrated Wasserstein term in (A) converge. For the nonnegative KL integral, weak lower semicontinuity at each time and Fatou give the required lower bound. The initial right-hand side converges by the constructed W_2 and KL convergence. Applying (A) to every p_{0,n} and passing to the limit proves (A) for the public initialization. This closes the entire average-KL obligation, including its signed-term limiting passage.

## step_004: Triangular-time contraction

Put r=M/alpha. Talagrand gives W(t)<=h(t)/alpha and W(0)<=H_0/alpha. Using the sign of the negative term in (A) and dropping W(T)>=0 gives

(3-r) integral_0^T (T-t)h(t) dt <= (T^2+1/alpha)H_0.

For an independent triangular time, the output position law is bar p_T=integral_0^T 2(T-t)p_t/T^2 dt. Convexity of KL therefore yields

KL(bar p_T||nu)<=2/T^2 integral_0^T (T-t)h(t) dt
<= [2/(3-r)] [1+1/(alpha T^2)] H_0=C_T H_0.

This holds for every T>0, including values for which C_T is not less than 1.

## step_005: Exponential-time contraction

Let S have density s^2 exp(-s/T)/(2T^3) on (0,infinity), independently of the phase initialization, and conditionally draw tau from the triangular law with scale S. For t>=0 its marginal density is

integral_t^infinity [s^2 exp(-s/T)/(2T^3)] [2(s-t)/s^2] ds
=exp(-t/T)/T.

Hence the exponential-time position law is the mixture E[bar p_S]. All changes in order of integration of probability densities are justified by Tonelli. Furthermore

E[S^(-2)]=integral_0^infinity exp(-s/T)/(2T^3) ds=1/(2T^2).

Convexity of KL and the triangular bound consequently give

KL(E[bar p_S]||nu)
<= [2/(3-r)] [1+1/(2alpha T^2)] H_0
<=C_T H_0.

The output has finite second moment by the quadratic moment estimate in step_001, not by integrating an exponential-in-time flow estimate. Its density is positive and its KL is finite by step_002. These observations also apply to the triangular output.

## step_006: Iteration and complexity

Every step thus preserves the assumptions needed to restart the one-step argument. Fresh independent times and Gaussian velocities implement precisely the position-law kernels used above. Induction gives

KL(mu_K||nu)<=C_T^K KL(mu_0||nu)

for every integer K>=0; K=0 is equality. These are KL divergences of the unconditional position laws, not expectations of conditional KL divergences.

Let H_0=KL(mu_0||nu) and epsilon>0. If H_0<=epsilon, choose K=0; there is no logarithm to evaluate and the time is zero. Otherwise take T=2/sqrt(alpha-M). Direct substitution gives

C_T=(5alpha-M)/(6alpha-2M)=[1+(alpha-M)/(5alpha-M)]^(-1)<1.

The stated ceiling therefore implies C_T^K H_0<=epsilon. If S_K=sum_{k=1}^K tau_k, triangular times give S_K<=KT almost surely, whereas exponential times give E S_K=KT. The latter is not a deterministic bound on S_K.

To state the asymptotic precisely, let r=M/alpha and a_r=log(1+(1-r)/(5-r))>0. In the nontrivial case,

KT<=2/sqrt(alpha-M) [1+log(H_0/epsilon)/a_r].

Consequently, for fixed r and H_0>0 as epsilon/H_0 tends to zero, the deterministic triangular bound and the exponential expectation are O_r((alpha-M)^(-1/2) log(H_0/epsilon)). The ceiling prevents dropping the additive 1 uniformly near epsilon=H_0. Also a_r tends to zero as r tends to 1, so the O constant is not claimed uniform in r. All six proof obligations are closed.
