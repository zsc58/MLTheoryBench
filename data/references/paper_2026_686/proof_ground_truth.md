# Reference Proof

## Scope and audited background

Fix n>=1, an arbitrary finite R>0, an arbitrary p in (0,1/2), and a finite even coercive convex loss phi:R^n -> [0,infinity). We construct one admissible instance with Abar=0. All constants and the attack process may depend on these fixed choices, but not on the trajectory length T.

The following standard independent facts are used. A finite convex function on Euclidean space is continuous, locally Lipschitz, and differentiable outside a set of Lebesgue measure zero. An integrable i.i.d. sequence satisfies the almost-sure strong law. Dominated convergence applies to difference quotients with an integrable dominating bound. A continuous function attains a minimum on a nonempty compact set. The hypotheses needed here are verified below. Uniform convergence is derived directly from finite nets, rather than assumed from a specialized theorem.

## 1. Radial growth and bounded-noise smoothing

Let W be uniform on [-1,1]^n, and put b=sqrt(n). Thus ||W||_2<=b, W and -W have the same law, E[W]=0, and E[WW^T]=I_n/3. Define psi(z)=E[phi(z+W)]. This is finite and convex because phi is continuous and the translated support is compact. It is even by symmetry. Jensen gives psi(z)>=phi(z), so psi is coercive.

For completeness, the source's asymptotic-slope assertion can be justified as follows. For any finite even coercive convex function f, put h_r(u)=(f(ru)-f(0))/r for r>0 and ||u||_2=1. Convexity makes h_r(u) nondecreasing in r; continuity of f makes h_r continuous in u. Let a(r)=min_{||u||=1} h_r(u), and L(u)=sup_{r>0} h_r(u). Then a(r) is nondecreasing. Moreover,

  lim_{r->infinity} a(r) = inf_{||u||=1} L(u).

To see the nontrivial inequality, suppose the limit a is finite, choose r_j->infinity and minimizing directions u_j, and pass to a convergent subsequence u_j->u. For each fixed s>0, eventually h_s(u_j)<=a(r_j), hence h_s(u)<=a. Taking the supremum over s gives L(u)<=a. The opposite inequality follows from a(r)<=h_r(u)<=L(u). If a=+infinity, the equality is immediate. The left side is precisely the radial liminf defining m_f.

Coercivity gives a radius r_0 at which f(r_0u)-f(0)>=1 for every unit u. Monotonicity then gives m_f>=1/r_0>0. The value +infinity is allowed. Equivalently, L is a lower semicontinuous extended-real function on the compact sphere; it need not be continuous.

For f=phi and its smoothing psi, Jensen and convexity give, for each unit u and t>0,

  phi(tu) <= psi(tu) <= phi(2tu)/2 + E[phi(2W)]/2.

The last expectation is finite because W is bounded. Divide by t and use the monotone directional limits to obtain equality of the directional recession slopes. The preceding compactness argument then gives m_psi=m_phi in (0,+infinity].

Choose a finite eta with 0<eta<m_phi. By the radial liminf characterization there exists a finite c>0 such that

  psi(cu)-psi(0) >= eta c    for every ||u||_2=1.

This selection also covers m_phi=+infinity. No upper growth restriction on phi is needed.

## 2. Construction and admissibility

Take x_0 and w_0,w_1,... to be independent copies of W. Generate all node indicators delta_{t,i} independently with parameter p, independently of these variables. Let C_t be the event that every coordinate indicator at time t equals one, and write q=p^n>0. Define d(x)=x/||x||_2 for x!=0 and d(0)=0. Set

  Abar=0,
  v_t=c 1_{C_t} d(x_t) if t is odd,
  v_t=0 if t is even,
  x_{t+1}=w_t+v_t.

The attack is selected from the current state and indicators before w_t. If any node is not permitted, the entire attack is zero; consequently each coordinate is zero whenever its own indicator is zero. The norm bound ||v_t||_2<=c is deterministic, so it supplies a uniform conditional sub-Gaussian bound under every state history. The initial state and noise are bounded as well; choosing sufficiently large finite sigma_v and sigma_w verifies the public exponential-moment formulation. The dynamics matrix is stable.

The states satisfy ||x_t||_2<=b+c for all t, with the sharper bound b at t=0. At odd times t>=1, v_{t-1}=0, so x_t=w_{t-1}. At even times t>=2,

  x_t=w_{t-1}+c 1_{C_{t-1}} d(w_{t-2}).

For the public state-history filtration F_t=sigma(x_0,...,x_t), fresh w_{t-1} is independent of both F_{t-1} and v_{t-1}. Hence, for every t>=1,

  E[x_t x_t^T | F_{t-1}]
    = E[v_{t-1}v_{t-1}^T | F_{t-1}] + I_n/3
    >= I_n/3.

Thus lambda=1/sqrt(3) is valid. This computation does not assume that future attacks are independent of past noises.

## 3. The correct population objective and its derivative

Let K={A:||A||_F<=R}, g_t(A)=phi(x_{t+1}-Ax_t), and F_T(A)=T^{-1} sum_{t=0}^{T-1} g_t(A).

Let U,V,Z be independent copies of W, and let B be an independent Bernoulli(q) variable. For odd times, the loss has the law

  g_o(A)=phi(V+c B d(U)-AU).

For even times t>=2, it has the law

  g_e(A)=phi(Z-A(V+c B d(U))).

Define

  F(A)=(E[g_o(A)]+E[g_e(A)])/2.

The two expectations are generally different; F is not an unspecified E[g_t(A)]. Both are finite convex functions.

All states have norm at most b+c. For A in any fixed bounded matrix neighborhood of K, every residual lies in one deterministic compact ball. The local Lipschitz property of phi therefore supplies a deterministic Lipschitz bound for g_o and g_e in that neighborhood. It also bounds their gradients wherever they exist.

At A=0, the odd residual V+c B d(U), conditional on U,B, is a translate of an absolutely continuous variable. The even residual is Z, also absolutely continuous. Consequently phi is differentiable at these residuals almost surely. Composition with the affine residual map gives

  gradient g_t(0)=-gradient phi(w_t+v_t) x_t^T

almost surely. The deterministic Lipschitz bound dominates difference quotients, so dominated convergence shows that F is differentiable at zero and its gradient is the half-sum of the expected odd and even gradients. This establishes a unique population gradient, not merely one selected subgradient.

Evenness of phi implies gradient phi(-z)=-gradient phi(z) wherever both gradients exist. Symmetry and absolute continuity therefore give E[gradient phi(W)]=0. Independence of the fresh noise from the regressor implies that the even contribution to gradient F(0) is zero. The unattacked odd contribution is likewise zero.

For an attacked odd time, condition on U=x!=0. At almost every V, the subgradient inequality at V+c d(x), evaluated against V, gives

  gradient phi(V+c d(x))^T d(x)
    >= [phi(V+c d(x))-phi(V)]/c.

Multiply by ||x||_2 and average over V. The choice of c yields

  E_V[gradient phi(V+c d(x))^T x]
    >= (||x||_2/c)[psi(c d(x))-psi(0)]
    >= eta ||x||_2.

At x=0 the corresponding inequality holds with both sides zero. Thus the Frobenius pairing with I_n satisfies

  <gradient F(0),I_n>_F
    <= -(q eta/2) E||U||_2 < 0.

Strict positivity of E||U||_2 follows directly from the chosen uniform law. Neither the paper's adapted small-ball lemma nor its external dependency is needed.

Because zero is interior to K and ||epsilon I_n||_F=epsilon sqrt(n), differentiability gives a sufficiently small epsilon>0 with A_*=epsilon I_n in K and

  F(A_*)<F(0).

This is the required population separation. Merely exhibiting a nonzero member of a possibly nonsingleton subdifferential would not establish it.

## 4. Uniform almost-sure convergence

For t>=1, each odd g_t(A) depends only on w_{t-1}, w_t, and C_t. Each even g_t(A), for t>=2, depends only on w_{t-2}, w_{t-1}, w_t, and C_{t-1}. Consequently, within each fixed residue class modulo four, after omitting t=0, the losses are independent and identically distributed. Odd residue classes have expectation E[g_o(A)], and even residue classes have expectation E[g_e(A)]. Consecutive even-indexed losses need not be independent, which is why a parity split alone is insufficient.

For each fixed A, bounded residuals make g_t(A) uniformly bounded and therefore integrable. Apply the ordinary i.i.d. SLLN within the four residue classes. Each class has asymptotic frequency 1/4. The initial term g_0(A)/T vanishes, yielding

  F_T(A)->F(A) almost surely.

To make this uniform on K, note that all residuals for A in K lie in the ball of radius (1+R)(b+c). Choose a Lipschitz constant L for phi on a slightly larger ball. Then, for every t and every A,A' in K,

  |g_t(A)-g_t(A')| <= L(b+c)||A-A'||_F.

The same bound holds for F_T and F. For each positive integer j, choose a finite 1/j-net N_j in K. Intersect the probability-one pointwise-convergence events at the countable union of these finite nets. On the resulting single probability-one event,

  sup_{A in K}|F_T(A)-F(A)|
    <= max_{A in N_j}|F_T(A)-F(A)| + 2L(b+c)/j.

First let T->infinity and then j->infinity. Therefore

  sup_{A in K}|F_T(A)-F(A)|->0 almost surely.

## 5. Simultaneous exclusion of all minimizers

Every F_T is continuous and K is nonempty and compact, so empirical minimizers exist. Let Delta=F(0)-F(A_*)>0. Continuity of F gives a deterministic r>0 such that

  F(A)>F(A_*)+Delta/2

whenever A in K and ||A||_F<r.

On the single probability-one uniform-convergence event, eventually sup_K|F_T-F|<Delta/8. For every such T and every A in K with ||A||_F<r,

  F_T(A)>F_T(A_*)+Delta/4.

Thus no empirical minimizer lies in that neighborhood for any sufficiently large T. This statement holds simultaneously for all choices of minimizers on each sample path in the probability-one event. In particular, no sequence of empirical minimizers can converge to Abar=0.

## Obligation closure

Admissibility and conditional excitation are verified in Section 2. Radial growth, finite smoothing, and the infinite-slope case are established in Section 1. Population differentiability and strict directional separation are established in Section 3. Independence, integrability, the two-phase limit, and uniform almost-sure convergence are established in Section 4. Existence of empirical minimizers and the pathwise all-selections conclusion are established in Section 5. No theorem-critical nonstandard dependency remains unresolved.
