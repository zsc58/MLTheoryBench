# Reference Proof

## Contract and source repairs

The public theorem concerns expected discrepancies, with a fixed distinguisher outside the expectation. The current outcome may depend on the forecast distribution but not on its fresh sampled forecast. All computations below use finite forecast supports. Sampling and statistic-oracle implementation costs are separate from the stated kernel/feature oracle-arithmetic costs.

There is a local factor-two error in the source's tolerance normalization. We use the operator twice the one printed there. Equivalently, one can retain the printed operator and halve its allowed tolerance. The final bound and the prescribed tolerance parameter remain unchanged. The source's average-error complexity is interpreted on the RKHS unit ball; it is not a numerical-accuracy runtime.

The measurable computational model also matters. The kernel is jointly measurable in its two input pairs; an optional finite feature matrix is jointly measurable; and the geometric oracles have fixed Borel-measurable response rules. Measurability of each fixed RKHS function alone would not imply these properties. We verify below that the numerical construction produces measurable forecasts. We do not assume continuity of the kernel or separability of the RKHS.

The proof has six critical obligations: construct finite-support forecasts with the required inequality; establish their measurable dependence on history; prove the potential bound; transfer it to fixed RKHS tests; establish the statistic-to-OI identity; and account for the total implementation cost. Each is closed below.

## Standard finite-dimensional background used

We use the following standard independent facts, not an imported specialized EVI theorem.

1. **Central-cut ellipsoid.** In an n-dimensional Euclidean affine space, an ellipsoid containing the current feasible set can be updated after a halfspace cut through its center so that it still contains the retained part and its volume decreases by a factor at most exp(-1/(2(n+1))). Each update uses polynomially many arithmetic operations in n. Thus an initial radius-R ball cannot, after more than 2n(n+1) log(R/b) such cuts, still contain a radius-b ball. A separating cut excluding the center may be weakened to a central cut without losing containment. In dimension one the update is interval bisection.
2. **Compact convex minimax for a finite family of affine functions.** If a_1,...,a_K are continuous affine functions on a nonempty compact convex set Z, then min_{lambda in Delta_K} max_{z in Z} sum_k lambda_k a_k(z) equals max_{z in Z} min_k a_k(z). This is the finite-dimensional separating-hyperplane/minimax theorem; no continuity of a map indexing the family is required.
3. **Approximate convex optimization.** A convex Lipschitz function on a finite-dimensional compact convex domain with known relative inner and outer balls can be minimized to positive additive error using polynomially many arithmetic operations and first-order/separation-oracle calls in the dimension and logarithms of the geometric condition, function scale, and inverse error. Work is in the affine hull. A known full subgradient and function value constitute a first-order oracle. The implementation may be taken to be a deterministic finite arithmetic and comparison algorithm, with a prescribed iteration bound and fixed tie rules.

The ellipsoid and simplex domains used below have the required relative geometry. Every function to which minimax or convex optimization is applied is affine in z or a maximum of affine functions in lambda. For a fixed instance, the construction needs no continuity of the original operator S. Measurable dependence across histories is a separate obligation and uses the task's measurable primitive interfaces, as verified in Section 2.1. These background facts explain precisely what standard convex-optimization machinery is used; they do not assume the EVI construction.

## 1. A finite-support positive-tolerance construction

Let S:Z->R^d be an evaluable operator with ||S(p)||<=M, and let delta>0. We construct a finitely supported distribution Q such that

E_{p~Q}[S(p)^T(z-p)]<=delta for every z in Z.

If Z is a singleton or M=0, the point mass at the supplied c, or at the supplied singleton point, works. Also, if delta>=MD, the point mass at c works. Otherwise work in the n-dimensional affine hull of Z, n>=1, using the supplied c,rho,R with B_A(c,rho) contained in Z contained in B_A(c,R). Normal components of S do not affect its pairing with z-p.

Run a central-cut ellipsoid starting with B_A(c,R). At a center q outside Z, use the domain separation oracle and take a central cut retaining Z. At a center q in Z, evaluate S(q). If its restriction to the affine direction space is zero, the point mass at q solves the problem exactly. Otherwise record p_k=q and take the central cut

S(p_k)^T(z-p_k)>=0.

For a tolerance gamma>0, take

alpha=min{1/2, gamma/[4M(D+rho)]},   b=alpha rho.

After more than 2n(n+1) log(R/b) cuts, the recorded points satisfy

max_{z in Z} min_k S(p_k)^T(z-p_k)<=gamma.

To prove this, suppose there were z_* in Z for which all recorded pairings exceeded gamma. Every point of the ball B_A((1-alpha)z_*+alpha c, alpha rho) belongs to Z by convexity: it has the form (1-alpha)z_*+alpha v with v in B_A(c,rho). Its distance from z_* is at most alpha(D+rho). Each recorded pairing therefore decreases from its value at z_* by at most M alpha(D+rho)<=gamma/4. This entire radius-b ball satisfies all recorded operator cuts and every domain cut. It must consequently be contained in the final ellipsoid, contradicting the volume bound. If no operator point had been recorded, the inner ball of Z would similarly survive all domain cuts, so this case cannot evade the argument.

Set a_k(z)=S(p_k)^T(z-p_k). Each a_k is continuous affine in z. Compact convex minimax now gives a mixture lambda with

max_{z in Z} sum_k lambda_k a_k(z)<=gamma.

We do not select this mixture by an unspecified parameter-dependent choice of a minimizer. Instead, compute approximate weights using a finite convex optimization algorithm. For a proposed lambda, a linear optimization call over Z maximizes

(sum_k lambda_k S(p_k))^T z - sum_k lambda_k S(p_k)^T p_k.

Let z_lambda be the point returned by the supplied fixed oracle rule. Then (a_k(z_lambda))_k is a subgradient of the convex objective F(lambda)=max_z sum_k lambda_k a_k(z). Since |a_k(z)|<=MD, F is Lipschitz on the simplex with constant at most sqrt(K)MD. The simplex has explicit relative inner and outer balls. Standard approximate convex optimization therefore computes weights within additive gamma of the optimum, with polynomial dependence on K and logarithmic dependence on positive accuracy and scale. For K=1 the weight is simply 1. Taking gamma=delta/2 yields the desired bound delta.

This proves, rather than assumes, the specialized EVI claim. The number of recorded points and operator evaluations is polynomial in d and logarithmic in the geometric condition and in 2+MD/delta. Computing the mixture uses additional domain-oracle calls and arithmetic polynomial in that support size; it requires no further evaluations of S at new points. Positive tolerances are essential here: no exact-zero claim for arbitrary discontinuous S is used.

## 2. Forecast construction and potential

Write z_t=s(y_t). Let Phi(x,p):R^d->H be the feature operator, with h(x,p)^T u=<h,Phi(x,p)u> and ||Phi(x,p)||<=sqrt(G).

Maintain the distribution-averaged residual

m_0=0,
q_t=sum_j lambda_{t,j} Phi(x_t,p_{t,j})(z_t-p_{t,j}),
m_t=m_{t-1}+q_t,

where Q_t=sum_j lambda_{t,j} delta_{p_{t,j}}. These are finite algebraic sums in H. The expression q_t=E_{p~Q_t}[Phi(x_t,p)(z_t-p)] is only notation for this finite sum, with the realized history and outcome held fixed. No general Hilbert-valued integration or strong measurability of Phi is assumed.

After observing x_t and before seeing y_t, define

S_t(p)=2 Phi(x_t,p)^*m_{t-1}.

Use Section 1 to choose a finite Q_t satisfying

E_{p~Q_t}[S_t(p)^T(z-p)]<=delta_t for all z in Z.

The operator is bounded. Indeed, every previous increment has norm at most D sqrt(G), so ||m_{t-1}||<=(t-1)D sqrt(G) and

sup_p ||S_t(p)||<=2(t-1)DG.

For the numerical evaluation, use the finite kernel formula

S_t(p)=2 sum_{tau<t} sum_j lambda_{tau,j} Gamma((x_t,p),(x_tau,p_{tau,j}))(z_tau-p_{tau,j}).

Thus the operator can be evaluated from finite stored data and the kernel oracle. The pointwise construction is applicable without continuity of Phi in p. It uses only the past, x_t, and the supplied oracles; the universal inequality does not require knowing z_t. Its measurability is established in Section 2.1.

Sample p_t from Q_t and output mu_{p_t}. After the outcome is revealed, compute q_t as the finite sum over Q_t and update m_t. Averaging over Q_t while holding the current outcome fixed is legitimate precisely because that outcome does not depend on the current fresh draw.

The squared potential satisfies, on each realized history,

||m_t||^2=||m_{t-1}||^2+||q_t||^2+2<m_{t-1},q_t>
          <=||m_{t-1}||^2+D^2G+delta_t.

Here ||q_t||<=sum_j lambda_{t,j}||Phi(x_t,p_{t,j})(z_t-p_{t,j})||<=D sqrt(G), and the cross term is the expected pairing with the normalized S_t. Thus

||m_T||^2<=TD^2G+sum_{t=1}^T delta_t.

For D^2G>0, take delta_t=D^2G. This gives ||m_T||<=sqrt(2TD^2G).

## 2.1 Measurability of the implementation

We implement every numerical subroutine with fixed deterministic arithmetic, comparison, and tie-breaking rules. At round t, the deterministic bound M_t=2(t-1)DG supplies a deterministic maximum number of cuts and subsequent convex-optimization iterations. Early returns can be treated as branches of this bounded computation. Variable-length support lists can equivalently be padded with zero weights to their deterministic maximum length, using c for unused support positions.

Inductively, all stored support points and weights are measurable functions of the previously observed history. For a variable current input x and trial forecast p, the displayed kernel formula for S_t is a finite sum of products and compositions of measurable functions: the kernel is jointly measurable in both input pairs, and every previous statistic z_tau=s(y_tau) is measurable. Consequently, evaluation of S_t at a measurable trial point is measurable jointly in the observed history.

The initial ellipsoid is fixed. Each successive numerical state and center is measurable because it is obtained by arithmetic operations and Borel comparisons from the preceding state and the responses of the fixed measurable oracle rules. Zero directions and other exceptional branches have specified responses. All matrix operations are applied on their valid finite-dimensional domains. The same reasoning applies to the finite-mixture optimization: its first-order oracle uses the fixed Borel linear-optimization response and finite arithmetic. It follows that every output support point p_{t,j} and weight lambda_{t,j} is measurable in the history available to the learner. This verifies measurable construction, rather than relying on an arbitrary measurable-selection assertion for the minimax solution.

Using an independent U_t uniform on [0,1], choose the first support index whose cumulative weight exceeds U_t, with a fixed convention on endpoints. This is a measurable finite comparison rule and has distribution Q_t. In particular, Q_t(B)=sum_j lambda_{t,j}1_B(p_{t,j}) is measurable for each Borel B subset of Z. The output measure is the supplied probability kernel evaluated at the measurable p_t.

If the explicit finite-feature implementation is used, its accumulator and evaluations are measurable by joint measurability of Psi and the same finite arithmetic argument. The representation switch described later is deterministic in t and r.

Finally, for each fixed h in H, <h,m_t> is a finite sum of lambda_{tau,j} h(x_tau,p_{tau,j})^T(z_tau-p_{tau,j}), and is measurable. Squared norms of the finite residual sums can also be expressed using finitely many jointly measurable kernel evaluations. Thus every scalar random variable used in the proof is measurable. There is no need to regard m_t as a strongly measurable H-valued random variable, and no expectation of such a vector is taken.

## 3. RKHS tests and expectation order

For a fixed h in H, the reproducing identity gives

<h,q_t>=E_{p~Q_t}[h(x_t,p)^T(z_t-p)].

With a fixed adversarial sequence this directly identifies the sum with <h,m_T>. For an adaptive nonanticipating history, condition immediately before the fresh draw, including the current outcome for the purpose of analysis but not revealing it to the learner. The current fresh uniform draw is independent of this information, and the conditional law of p_t is Q_t. By Section 2.1 all scalar expressions are measurable. The tower property then gives

sum_t E[h(x_t,p_t)^T(z_t-p_t)]=E<h,m_T>.

Consequently,

|sum_t E[h(x_t,p_t)^T(z_t-p_t)]|
 <=E|<h,m_T>|
 <=||h|| sqrt(2TD^2G).

The fixed function h is outside the expectation. This is not an assertion about an expectation of a supremum or about sample-path discrepancies of the sampled forecasts.

## 4. Transfer to outcome indistinguishability and boundary cases

For each p and fixed h_f,

E_{tilde y~mu_p} f(x,p,tilde y)
 =h_f(x,p)^T E_{mu_p}s(tilde y)
 =h_f(x,p)^T p.

Therefore the OI discrepancy is exactly the expected RKHS discrepancy from Section 3, and

OIGap_T(f)<=||h_f|| sqrt(2TD^2G).

Compactness of Z bounds s(y), and the feature bound gives ||h_f(x,p)||<=sqrt(G)||h_f||. The scalar expectations are thus finite. Their measurability follows from the task's assumptions and Section 2.1.

For a class with sup_f ||h_f||<=B<infinity, taking the supremum after the pointwise inequality gives sup_f OIGap_T(f)<=B sqrt(2TD^2G)=o(T). In particular, define A_T=sup_{||h||<=1} OIGap_T(f_h)/T; then A_T<=sqrt(2D^2G/T).

If D=0, Z is a singleton and s(y_t)=p_t, so every discrepancy is zero. If G=0, every RKHS evaluation is zero, so the same conclusion holds. Choose the supplied singleton point or c as the constant feasible forecast in these cases and use its measure oracle. This is a measurable procedure. No zero-tolerance EVI invocation or division by D^2G is needed.

## 5. Total computation and the two meanings of accuracy

For positive D^2G and delta_t=D^2G, the bound M_t<=2(t-1)DG gives M_t D/delta_t<=2(t-1). Section 1 therefore uses support size and operator-call count polynomial in d and polylogarithmic in t and the relative geometric condition. If a smaller positive numerical tolerance delta_t is requested, the construction instead has polylogarithmic dependence on 2+tD^2G/delta_t. This is the source of the numerical-tolerance claim; it is distinct from the average statistical error epsilon.

Let Gamma(a,b)=Phi(a)^*Phi(b). In the kernel-only implementation,

S_t(p)=2 sum_{tau<t} E_{u~Q_tau}[Gamma((x_t,p),(x_tau,u))(z_tau-u)].

There are nearly t historical support points, up to polynomial factors in d and logarithms. Kernel evaluations cost poly(d), so each operator evaluation costs nearly poly(d)t. Computing the current support and weights has the same nearly linear-in-t cost up to the stated factors. Summing over t<=T gives nearly poly(d,D,G)T^2 arithmetic time.

If a finite feature matrix Psi(x,p) in R^{r by d} is supplied, maintain the explicit r-vector

v_t=sum_{tau<=t} E_{u~Q_tau}[Psi(x_tau,u)(z_tau-u)].

Then S_t(p)=2 Psi(x_t,p)^T v_{t-1}. Under the explicitly stated feature-evaluation accounting, evaluation and the update over the current support cost nearly poly(d)r per round. The total is nearly poly(d,D,G)rT. This is an oracle-arithmetic bound using the linear-in-r feature charge from the source's implementation; it is not inferred from an unspecified polynomial feature evaluator.

The two implementations can be combined without knowing the eventual horizon. Use the kernel representation while t<r; if that threshold is reached, form the explicit feature accumulator from the stored history and thereafter use it. The conversion costs nearly r^2, already of the same order as the kernel work accumulated by the switch. Hence, simultaneously for all horizons, total work is

~O(poly(d,D,G) T min{r,T}),

with r=infinity in the kernel-only case. There are also O(T) statistic and measure-oracle calls, whose actual implementation costs are charged separately. The measurable finite-arithmetic choices in Section 2.1 do not change these bounds. The bound is nearly linear in T when a fixed finite feature representation is used, and may be nearly quadratic for a general kernel.

For 0<epsilon<=1, take

T_epsilon=max{1,ceil(2D^2G/epsilon^2)}.

Then A_{T_epsilon}<=epsilon. Substituting this horizon gives total work

~O(poly(d,D,G) min{r,epsilon^{-2}} epsilon^{-2}),

and hence the uniform worst-case bound ~O(poly(d,D,G)epsilon^{-4}). Polynomial factors here may include a constant term, so the ceiling and small-D^2G cases are covered. In the zero-gap cases, one round suffices for every positive statistical accuracy. This establishes the claimed sample-to-accuracy computation without confusing epsilon with an optimization tolerance or multiplying a total-runtime bound by the horizon a second time.
