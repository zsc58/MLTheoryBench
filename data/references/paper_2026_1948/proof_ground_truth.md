# Reference Proof

## Contract and proof obligations

The dynamic action defines the square of the dynamic distance. The force field is the spatial gradient of a scalar first variation, and the public regularity hypothesis specifies first-order differentiability under square-integrable transport perturbations. The flow uses any jointly measurable primal measure-LMO minimizer; no positive-definite optimizing certificate is assumed.

The obligations are: establish the induced velocity norm and metric properties; justify static minimax; prove both static-dynamic inequalities with Eulerian fields; prove primal LMO existence and duality, including zero and singular cases; derive the descending local slope from the stated differentiability; obtain metric absolute continuity and the speed bound; and derive equality for the LMO flow and the energy-dissipation identity.

The source's arbitrary inverse-trace minimizing-sequence assertion is false and is not used. The conditional positive-definite selector theorem remains valid, but is unnecessary for the general flow argument.

## 1. Norm bounds and induced velocity norm

The set of PSD matrices of trace one is compact. Since gamma is the restriction of a norm, its minimum and maximum on this set give constants 0<c<=C<infinity, depending only on gamma and d, such that

c tr(S)<=gamma(S)<=C tr(S), S>=0.

Consequently, for every mu and v in L^2(mu;R^d),

sqrt(c)||v||_2<=N_mu(v)<=sqrt(C)||v||_2.

The support representation gives

N_mu(v)=max_{Q in K_gamma} ||Q^{1/2}v||_{L^2(mu)}.

A maximum of seminorms is a seminorm; the lower bound makes it a norm. Its square is convex, continuous, and weakly lower semicontinuous on L^2(mu). The same trace bounds, applied to coupling covariances, give

sqrt(c)W_2(mu,nu)<=W_gamma(mu,nu)<=sqrt(C)W_2(mu,nu).

These facts use the source's norm-comparison and norm-property arguments, with the latter applied to L^2 vector fields.

## 2. Robust static representation

Put Sigma_pi=int (y-x)(y-x)^T dpi and H(pi,Q)=tr(Q Sigma_pi). Each covariance is finite because the marginals have finite second moments. The support formula gives

W_gamma(mu,nu)^2=inf_pi max_Q H(pi,Q).

The version of Sion's theorem used here states that, for a compact convex minimizing set and a convex maximizing set, a finite function which is lower semicontinuous and convex in the minimizing variable and upper semicontinuous and concave in the maximizing variable has equal inf-sup and sup-inf values. The coupling set is convex and narrowly compact: fixed marginals give tightness and closure. K_gamma is convex and compact. H is affine in each variable, continuous in Q, and lower semicontinuous in pi by nonnegativity and continuity of the PSD quadratic integrand. Thus the theorem applies.

The function Q -> inf_pi H(pi,Q) is upper semicontinuous, being an infimum of continuous functions. Compactness of K_gamma makes its supremum a maximum. Therefore

W_gamma(mu,nu)^2=max_{Q in K_gamma} inf_pi H(pi,Q)=max_{Q in K_gamma} W_Q(mu,nu)^2.

An optimal static coupling also exists: pi -> max_Q H(pi,Q) is lower semicontinuous on the compact coupling set.

For completeness, W_gamma is a metric. For each PSD Q, glue couplings of consecutive pairs of measures and apply the L^2 triangle inequality to Q^{1/2}(Z-X)=Q^{1/2}(Y-X)+Q^{1/2}(Z-Y). Taking infima gives the triangle inequality for the pseudodistance W_Q, including singular Q. Taking maxima in W_gamma=max_Q W_Q gives the triangle inequality for W_gamma. Symmetry and the diagonal property are immediate, and separation follows from the W_2 lower bound. The trace bounds also identify its topology with the W_2 topology.

## 3. Static-dynamic equality

### Static to dynamic

Take any coupling of random variables (X,Y), write D=Y-X, and let X_t=X+tD with law mu_t. Define the Eulerian velocity by

v_t(z)=E[D | X_t=z].

Disintegration of the joint space-time law supplies a jointly measurable version for dt dmu_t. Differentiating int phi(X_t) for a compactly supported smooth test function and conditioning proves the continuity equation in distributions. The curve is narrowly continuous and has the prescribed endpoints. Conditional Jensen gives

int v_t v_t^T dmu_t <= E[DD^T]=Sigma_pi

in Loewner order for almost every t. In particular the field is square-integrable in space-time. Monotonicity gives

int_0^1 gamma(int v_t v_t^T dmu_t)dt <= gamma(Sigma_pi).

Taking the infimum over couplings proves (W_gamma^BB)^2<=W_gamma^2. An equality of Eulerian and pathwise covariances for arbitrary couplings is neither asserted nor needed.

### Dynamic to static

The superposition principle used here states: a narrowly continuous probability curve and a Borel velocity solving the continuity equation with finite space-time quadratic velocity integral admit a probability measure on absolutely continuous paths, with the prescribed time marginals, whose path derivatives equal the velocity evaluated on the paths almost everywhere. The public admissibility requirements verify these hypotheses.

Apply it to an admissible pair. Let eta be the resulting path law and pi the joint law of its endpoints. For each Q in K_gamma, time Cauchy-Schwarz gives

(X_1-X_0)^T Q(X_1-X_0) <= int_0^1 dot X_t^T Q dot X_t dt.

Integrating over eta yields

tr(Q Sigma_pi)<=int_0^1 tr(Q int v_t v_t^T dmu_t)dt<=int_0^1 gamma(int v_t v_t^T dmu_t)dt.

The endpoint coupling pi is the same for all Q. Maximize over Q to obtain gamma(Sigma_pi) bounded by the action. Hence W_gamma^2 is bounded by every admissible action. Taking the infimum proves the reverse inequality and thus W_gamma=W_gamma^BB.

## 4. Primal LMO existence and norm duality

Fix mu and g in L^2(mu;R^d), and define

D_mu(g)=sup_{N_mu(w)<=1} {-int g dot w dmu}.

Symmetry of the norm ball makes this the usual dual norm. It is finite by the L^2 norm comparison.

The functional A(v)=int g dot v dmu+N_mu(v)^2/2 is coercive and weakly lower semicontinuous on the Hilbert space L^2(mu). A bounded minimizing sequence has a weakly convergent subsequence, and the direct method yields a minimizer. No strict convexity or uniqueness is required.

For every v, duality gives

A(v)>=-D_mu(g)N_mu(v)+N_mu(v)^2/2>=-D_mu(g)^2/2.

Conversely, take unit vectors approaching the dual supremum and optimize their nonnegative scalar multiples. This gives inf A=-D_mu(g)^2/2. If v is any minimizer, differentiate A(av) at a=1 to get

int g dot v dmu=-N_mu(v)^2.

Substitution in the minimum value gives

N_mu(v)=D_mu(g),  int g dot v dmu=-D_mu(g)^2.

If D_mu(g)=0, these identities force v=0. These arguments include singular-covariance and nonunique-selector cases and do not invoke inverse-certificate limits.

If an interior inverse-trace minimizer Q_* does exist, the source's optional selector formula can be checked directly. With S=int gg^T dmu and C_*=Q_*^{-1}SQ_*^{-1}, differentiation along Q_*+t(P-Q_*) gives tr(P C_*)<=tr(Q_*C_*) for every P in K_gamma. Thus Q_* supports gamma at C_*, and -Q_*^{-1}g attains the primal minimum. This conditional verification does not justify arbitrary boundary minimizing sequences.

## 5. Derivation of the descending local slope

Fix mu, abbreviate g=g_mu, and write D=D_mu(g). The public differentiability assumption controls the first-order remainder for every sequence of couplings whose mean-square displacement tends to zero.

For nu approaching mu, choose a W_gamma-optimal coupling pi. Put r^2=int |y-x|^2 dpi and b(x)=E[y-x | x]. The trace comparison gives r<=W_gamma(mu,nu)/sqrt(c), and conditional Jensen gives

N_mu(b)^2<=gamma(Sigma_pi)=W_gamma(mu,nu)^2.

The differentiability assumption and norm duality give

F(mu)-F(nu)=-int g dot b dmu+o(r)<=D W_gamma(mu,nu)+o(W_gamma(mu,nu)).

Taking positive parts and the defining limsup proves |partial F|_{W_gamma}(mu)<=D.

For the opposite inequality take w in L^2(mu) with a=-int g dot w dmu>0 and set nu_h=(Id+h w)_#mu for h>0. The deterministic coupling gives W_gamma(mu,nu_h)<=h N_mu(w). Differentiability gives

F(mu)-F(nu_h)=h a+o(h).

The numerator is positive for sufficiently small h, so nu_h cannot equal mu then. The slope is therefore at least a/N_mu(w). Supremizing over w gives |partial F|_{W_gamma}(mu)>=D. If D=0, the upper bound already proves equality. Consequently

|partial F|_{W_gamma}(mu)=D_mu(g_mu).

This is an internal derivation, not an assumed spectral tangent-duality theorem.

## 6. Metric speed and the LMO flow

Write n(t)=N_mu_t(v_t). The public space-time integrability and norm bounds imply n in L^2(0,T). Applying the dynamic formula after restricting to [s,t] and linearly rescaling time gives

W_gamma(mu_s,mu_t)^2 <= (t-s) int_s^t n(r)^2 dr.

One also obtains the length bound W_gamma(mu_s,mu_t)<=int_s^t n(r)dr by time reparameterization. Explicitly, reparameterize using speed proportional to n+epsilon. The new unit-interval action is

(int_s^t (n+epsilon)dr)(int_s^t n^2/(n+epsilon)dr),

which tends to (int_s^t n dr)^2 as epsilon decreases to zero. Thus mu_t is metrically absolutely continuous. Standard metric absolute-continuity calculus gives existence of its metric derivative almost everywhere. Alternatively, the preceding squared bound and Lebesgue differentiation directly yield

|mu'|_{W_gamma}(t)<=n(t)

at almost every such time.

For the LMO solution, Sections 4 and 5 give n(t)=D_mu_t(g_mu_t)=|partial F|_{W_gamma}(mu_t). The public chain rule gives

-dF(mu_t)/dt=n(t)^2.

At a time where the energy is differentiable and the metric derivative exists, the definition of descending local slope, applied to forward points on the curve, implies

-dF(mu_t)/dt <= |partial F|_{W_gamma}(mu_t)|mu'|_{W_gamma}(t).

The slope is finite by Section 5. Hence

n(t)^2<=n(t)|mu'|_{W_gamma}(t)<=n(t)^2.

When n(t)>0, division gives |mu'|=n(t). When n(t)=0, the speed bound gives the same conclusion. Therefore

dF(mu_t)/dt=-|mu'|_{W_gamma}(t)^2=-one-half |mu'|_{W_gamma}(t)^2-one-half |partial F|_{W_gamma}(mu_t)^2

almost everywhere. Absolute continuity of the energy allows integration on every subinterval. Together with metric absolute continuity, this is the curve-of-maximal-slope conclusion in the convention stated in the problem.

All obligations listed at the beginning are closed. The false ancillary inverse-sequence assertion and the false speed equality for arbitrary Eulerian representatives are not dependencies of this proof.
