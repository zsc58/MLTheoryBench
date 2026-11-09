# Reference Proof

## Proof Structure and Obligations

Fix theta throughout. We establish: (i) the majorant identities and shape properties actually used; (ii) finite-atomic coupling reduction with the correct directed-cost orientation; (iii) both lower certificates, including infinite suprema; (iv) both upper certificates, including nonattainment of the transport infimum and extended values; (v) exponent ordering; and (vi) the finite-p dichotomy by a single global affine majorant. All these obligations are derived below. No specialized external theorem is left as an unresolved dependency.

## 1. Elementary Majorant Facts

All univariate arguments in this proof are finite and nonnegative. Function values may be +infinity, with 0 times infinity equal to zero.

Each Delta_i is nonnegative because x_i belongs to its own zero-cost ball, and is nondecreasing because the balls increase with their radius. Consequently each f_i(u)=Delta_i(u^(1/p)) and f_*(u)=max_i f_i(u) is nonnegative and nondecreasing. Such extended-valued monotone functions are measurable.

Least majorants exist: the identically infinite function is an admissible majorant, and the intersection of the hypographs of all admissible majorants is respectively star-shaped or convex. Its upper boundary is the pointwise infimum defining the least majorant. Order of the underlying functions is preserved by minimality. Every nonnegative concave function is star-shaped, so S_f <= C_f.

For any nonnegative f and a>0,

S_f(a)=sup_{u>=a} a f(u)/u,

where u ranges over finite real numbers. Indeed, any star-shaped majorant H satisfies H(a)>=a H(u)/u>=a f(u)/u for u>=a. Conversely, define G(a) by the displayed supremum for a>0 and set G(0)=f(0). Then G>=f, and for 0<lambda<=1,

G(lambda a)>=sup_{u>=a} lambda a f(u)/u=lambda G(a).

The case lambda=0 follows from G(0)>=0. Thus G is an admissible star-shaped majorant and is minimal. If f is nondecreasing, the equivalent expression G(a)=sup_{v>=1} f(av)/v also shows that G is nondecreasing on positive arguments; G(a)>=f(a)>=f(0) handles zero.

We will also use elementary facts about nonnegative concave functions H on [0,infinity). Such a function either is infinite at every positive argument or is finite everywhere. To see this, an infinite value at any argument propagates to every positive argument by writing that argument as a strict convex combination of the infinite-value argument and a suitable other nonnegative argument. Thus finiteness at one positive argument excludes infinite values anywhere, including zero.

In the finite case, H is nondecreasing. Otherwise a negative secant slope between a<b, together with concavity, gives H(t)<=H(b)+(t-b)(H(b)-H(a))/(b-a) for t>b, contradicting nonnegativity for large t. Concavity also bounds the secant slopes on every compact subinterval of (0,infinity) between finite slopes to two exterior points. Hence H is locally Lipschitz and continuous on (0,infinity). These conclusions apply to a finite C_f. In the infinite case, nondecreasingness is immediate on positive arguments and at zero as well.

For completeness, the Jensen inequality needed here follows from the same secant-slope comparison. If H is finite and concave and m>0, there is a finite slope s between all right and left secant slopes at m, giving H(v)<=H(m)+s(v-m) for every v>=0. For a nonnegative random variable U with finite mean m>0, integration gives E H(U)<=H(E U). If E U=0, then U=0 almost surely, and the conclusion is equality. Measurability holds because H is continuous on the positive half-line, with a separately specified value at zero. This argument also establishes integrability of H(U), since H is nonnegative and has an affine upper bound at m.

Finally, if H is nondecreasing and concave and 0<q<=1, then H composed with u -> u^q is concave whenever H is finite: the concavity of the power function, followed by monotonicity and then concavity of H, gives

H((lambda u+(1-lambda)v)^q)
>=H(lambda u^q+(1-lambda)v^q)
>=lambda H(u^q)+(1-lambda)H(v^q).

The power function's concavity follows directly from its nonpositive second derivative on (0,infinity), extended to zero by continuity.

## 2. Couplings on the Stated Measurable Space

The transport convention is pi in Pi(Q,P_N), with first coordinate y distributed according to Q and second coordinate x distributed according to P_N. Costs are d(y,x); swapping marginals does not preserve these costs in general.

Every such coupling admits a representation

pi=sum_i mu_i (K_i tensor delta_{x_i}),

where each K_i is a probability measure on X. Here is a justification that does not require measurable singletons. Group the finitely many sample points according to whether measurable sets distinguish them. Choose finitely many measurable separating sets for the distinct groups, and use their intersections and complements to form a finite measurable partition. The cells A_j containing sample points carry all of P_N; each such cell contains just one group of measurably indistinguishable sample points. Write m_j=P_N(A_j)>0 and choose a sample representative a_j in A_j. Define K_j(B)=pi(B times A_j)/m_j. The normalized restriction of pi to X times A_j has second marginal delta_{a_j}. A joint measure with this second marginal equals K_j tensor delta_{a_j}: on a rectangle B times D, its value is K_j(B) when a_j belongs to D and zero otherwise. Equality on all product-measurable sets follows from uniqueness of finite measures agreeing on rectangles. Assign K_i=K_j to each sample point in A_j. Since these sample points have identical Dirac measures, this yields the displayed representation, including repeated sample points.

In particular, the transport moment is sum_i mu_i integral d(y,x_i)^p K_i(dy). The same representation applies to essential-cost constraints. There is no need to assume a general disintegration theorem or a standard Borel data space.

All risk expectations are understood on the domain specified in the task. Their extended values are defined, and subtracting the finite empirical risk is legitimate. Because the weights are positive and the sum is finite, a defined expectation under Q can also be integrated using the displayed coupling representation without an infinity-minus-infinity cancellation. The law P_N is feasible and has finite loss expectation, so R_p(epsilon)>=Rhat and the robust excess risk belongs to [0,+infinity].

## 3. Lower Certificates

Fix finite p and epsilon>0. The star-shaped formula gives

S_{f_i}(epsilon^p)=sup_{t>=epsilon} (epsilon/t)^p Delta_i(t),

with finite t.

Choose any finite radii t_i>=epsilon and points y_i satisfying d(y_i,x_i)<=t_i. Put eta_i=(epsilon/t_i)^p and define

Q=sum_i mu_i[(1-eta_i)delta_{x_i}+eta_i delta_{y_i}],

pi=sum_i mu_i[(1-eta_i)delta_{(x_i,x_i)}+eta_i delta_{(y_i,x_i)}].

This pi has marginals Q and P_N, and

integral d(y,x)^p dpi <= sum_i mu_i eta_i t_i^p=epsilon^p.

The finitely supported Q has finite loss expectation. Its excess risk is

sum_i mu_i eta_i[L(y_i;theta)-L(x_i;theta)].

For these fixed radii, take the supremum independently over the finitely many y_i. Each coefficient is strictly positive, each ball is nonempty, and each loss value is finite. Thus this supremum is sum_i mu_i eta_i Delta_i(t_i), with the extended-value interpretation. If a rate is infinite, its contribution is approached through arbitrarily large finite increments, not by choosing a point with infinite loss. Other atoms can be left at x_i. Next take the independent suprema over finite t_i>=epsilon. This proves

R_p(epsilon)-Rhat >= sum_i mu_i S_{f_i}(epsilon^p)=lb_p(epsilon),

whether the right side is finite or infinite. Infinite suprema over radii are handled by arbitrarily large finite objective values as well.

For p=infinity, choose y_i in the epsilon-ball of x_i and use pi=sum_i mu_i delta_{(y_i,x_i)}. Its essential cost is at most epsilon. Independent suprema over the y_i give

R_infinity(epsilon)-Rhat >= sum_i mu_i Delta_i(epsilon)=lb_infinity(epsilon).

The same finite-approximation argument covers infinite rates.

## 4. Upper Certificates

Fix finite p and set C=C_{f_*}. If C(epsilon^p)=+infinity, the requested upper bound is immediate because the robust risk is defined as an extended supremum. Otherwise the concavity facts above imply that C is finite everywhere, nondecreasing, and continuous at every positive argument.

Let Q have a defined loss expectation and satisfy W_p(Q,P_N)<=epsilon. For rho>0, the definition of the infimum supplies a coupling pi in Pi(Q,P_N) with

integral d(y,x)^p dpi <= (epsilon+rho)^p.

In its finite-atomic representation, d(y,x_i) is finite for K_i-almost every y, since its pth moment is finite and mu_i>0. Therefore

L(y;theta)-L(x_i;theta)
<=Delta_i(d(y,x_i))
<=f_*(d(y,x_i)^p)
<=C(d(y,x_i)^p)

almost surely for each component. Infinite costs on null sets need no value of C at an infinite argument. Integrating and applying the Jensen inequality established above gives

E_Q L-Rhat
<=sum_i mu_i integral C(d(y,x_i)^p) K_i(dy)
<=C(sum_i mu_i integral d(y,x_i)^p K_i(dy))
<=C((epsilon+rho)^p).

The bound also applies when E_Q L=-infinity. Taking the supremum over admissible Q and letting rho decrease to zero proves

R_p(epsilon)-Rhat <= C(epsilon^p)=cc_p(epsilon).

For p=infinity, fix rho>0. Every feasible Q admits a coupling in Pi(Q,P_N) with essential cost at most epsilon+rho. In its representation, K_i is concentrated on d(y,x_i)<=epsilon+rho. Consequently

E_Q L-Rhat <= sum_i mu_i Delta_i(epsilon+rho).

Take the supremum over Q. Then let rho decrease to zero. Nondecreasingness of the rates and finiteness of the index set give, also for extended values,

R_infinity(epsilon)-Rhat
<=sum_i mu_i lim_{t down epsilon} Delta_i(t)
=cc_infinity(epsilon).

This completes both certificates without assuming that a transport infimum is attained or that the rate functions are right-continuous.

## 5. Exponent Ordering

For a nonnegative random cost D under any fixed coupling and finite 1<=p<=p2, Jensen applied to the concave power u -> u^(p/p2) gives

(E D^p)^(1/p)<=(E D^p2)^(1/p2).

The conclusion is immediate if the right side is infinite. For p2=infinity, it follows from D<=ess sup D almost surely, or is again trivial if the essential supremum is infinite. Infimizing over the same couplings gives W_p(Q,P_N)<=W_p2(Q,P_N). The domain of defined loss expectations is the same for both exponents. Thus the feasible risk sets are nested and R_p(epsilon)>=R_p2(epsilon).

For finite exponents, the lower-certificate formula shows that every term (epsilon/t)^p Delta_i(t), t>=epsilon, is nonincreasing in p. Supremizing and summing proves the finite-exponent lower ordering. Choosing t=epsilon shows that every finite-p lower certificate dominates lb_infinity. Cases in which both compared exponents equal infinity are identities.

For finite p<=p2, put f(u)=Delta_*(u^(1/p)) and f2(v)=Delta_*(v^(1/p2)). If C_f(epsilon^p)=infinity, the desired comparison at this radius is immediate. Otherwise C_f is finite, nondecreasing and concave, so

H(v)=C_f(v^(p/p2))

is concave by the composition calculation in Section 1. Moreover H(v)>=f2(v) for all v>=0. Minimality gives C_{f2}(v)<=H(v). Evaluating at v=epsilon^p2 yields cc_p(epsilon)>=cc_p2(epsilon).

For the infinity endpoint, if cc_p(epsilon) is finite, then for each i and t>epsilon,

Delta_i(t)<=C_{f_*}(t^p).

Right-continuity of the finite concave majorant at epsilon^p gives lim_{t down epsilon}Delta_i(t)<=cc_p(epsilon). Multiply by mu_i and sum to obtain cc_infinity(epsilon)<=cc_p(epsilon). If cc_p(epsilon) is infinite, this comparison is automatic. Together these arguments give every ordering in the task, including p=1 and p=infinity.

## 6. Finite-p Dichotomy

Fix finite p. If lb_p(epsilon)=infinity for every epsilon>0, the two-sided certificates imply that both the robust excess risk and cc_p(epsilon) are infinite at every positive radius.

Otherwise lb_p(epsilon0)<infinity for some epsilon0>0. Set u0=epsilon0^p. Positivity of all mu_i implies S_{f_i}(u0)<infinity for every i. The supremum formula and the finite maximum give

M:=S_{f_*}(u0)=max_i S_{f_i}(u0)<infinity.

For u>=u0, the same formula gives f_*(u)<=M u/u0. For 0<=u<=u0, monotonicity gives f_*(u)<=f_*(u0)<=M. Hence the single affine function

A(u)=M+(M/u0)u,  u>=0,

dominates f_* on its entire domain. This remains valid when M=0. Since A is a finite nonnegative concave majorant, C_{f_*}(u)<=A(u)<infinity for all finite u>=0. Thus cc_p(epsilon) is finite at every positive radius. Each S_{f_i}<=C_{f_*}, so all lower certificates are finite too. Finally, the two-sided certificates and feasibility of P_N imply that the robust excess risk is finite and nonnegative at every positive radius.

These cases exhaust all possibilities and are mutually exclusive. This proves the integrated theorem.
