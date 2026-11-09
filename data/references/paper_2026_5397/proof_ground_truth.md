# Reference Proof

## Audit Status and Proof Structure

This is a complete reference proof for the unchanged public task. The argument retains the source's degree controls, direct coordinate estimate, global perturbation estimate, heterogeneous leave-one-out construction, and final self-bounding inequality. The norm used for row-vector perturbation is specified and justified below; no specialized perturbation or ranking theorem is invoked without a derivation.

All vectors in matrix products are treated as row vectors. All pair-indexed sums exclude diagonal indices unless explicitly stated otherwise. Constants denoted C_h or K_h depend only on h; constants denoted C_{h,s} depend only on h and s. Their values may increase between displays. The fixed parameters h, s, and gamma may enter the sufficiently-large-n threshold. The density constant c0 will depend only on h and gamma and will be chosen at least 10240h^2/gamma^2.

Put L=log n, M=||r||_infinity, and R=M sqrt(L/(n rho k)). We work with sufficiently large n, so L>=1. The score condition implies h>=1 whenever the parameter set is nonempty, r_max/r_min<=h, and M sqrt(n)<=h||r||_2.

For each unordered pair, generate its k comparisons independently of all graph indicators, whether or not that pair will be observed. Let tilde b_ij be the resulting empirical fraction and epsilon_ij=tilde b_ij-b_ij. Use complementary outcomes for the reverse orientation. Thus epsilon_ji=-epsilon_ij and hat b_ij=A_ij tilde b_ij. This construction has exactly the public observation law.

Write D_i=sum_{j!=i}A_ij, D=max_i D_i, d=min_i D_i, and m_i=sum_{j!=i}a_ij. The spectral event is E_gap={1-|lambda_2(P)|>gamma}. It has probability at least 1-n^-5.

## Standard Concentration Statements

The following standard independent inequalities are used with their indicated hypotheses.

1. For a sum X of independent Bernoulli variables with mean m and 0<eta<1, P(|X-m|>=eta m)<=2 exp(-eta^2 m/3).
2. For independent real variables X_t with interval lengths ell_t, P(|sum_t(X_t-E X_t)|>=u)<=2 exp(-2u^2/sum_t ell_t^2).
3. For independent centered real variables X_t with |X_t|<=b and sum_t E X_t^2<=v, the absolute sum is at most sqrt(2vt)+2bt/3 except on an event of probability at most 2 exp(-t).
4. For independent centered n-by-n real matrices X_t, with ||X_t||_2<=b and max{||sum E X_t X_t^T||_2,||sum E X_t^T X_t||_2}<=v, P(||sum X_t||_2>=u)<=2n exp(-u^2/[2(v+bu/3)]).

These statements also apply conditionally when the conditioning fixes the coefficients and leaves the indicated variables independent. A zero variance or zero interval-length sum is interpreted as a deterministic centered sum. We never assume that incident graph indicators remain independent after conditioning on E_gap. Instead, we construct concentration events under the original product experiment and intersect them with E_gap at the end.

## 1. Degrees, Denominators, and Direct Coordinate Noise

Apply the Bernoulli bound with eta=1/4 and union bound over vertices. Since m_i>=(n-1)rho, choosing c0 sufficiently large gives an event E_D with failure probability O(n^-20) on which, for every i,

3m_i/4 <= D_i <= 5m_i/4.

For n>=3 this implies D_i>=n rho/2, and also m_i<=2D_i. In particular d>=n rho/2 and D>0. This avoids inferring n rho/2 from the weaker lower bound (n-1)rho/2.

Let B_i=sum_{j!=i}hat b_ij. Conditional on the graph, kB_i is a sum of independent Bernoulli variables with mean at least kD_i/(1+h). Therefore

P(B_i<D_i/[2(1+h)] | A) <= exp(-kD_i/[8(1+h)]).

On E_D, the union of these denominator failures is O(n^-20), after increasing c0 as permitted.

Detailed balance gives r_i b_ij=r_j b_ji. Consequently the centered numerator

N_i=sum_{j!=i}(hat b_ji r_j-hat b_ij r_i)

is -sum_{j!=i}A_ij(r_i+r_j)epsilon_ij. Conditional on the graph, its representation using individual repetitions has total squared interval length at most 4M^2D_i/k. Hoeffding therefore gives, simultaneously over i with failure O(n^-19),

|N_i| <= M sqrt(40D_i L/k).

On the denominator event, stationarity gives

hat r_i = [sum_{j!=i}hat b_ji hat r_j]/B_i.

Define bar r_i=[sum_{j!=i}hat b_ji r_j]/B_i on this event. Outside it, bar r may be assigned any fixed values, since all subsequent identities involving it are restricted to the event. Thus

|bar r_i-r_i|=|N_i|/B_i <= C_h M sqrt(L/(D_i k)) <= C_h R.                 (1)

Notice also that sum_j hat b_ji<=D_i. This incoming sum is not identified with B_i; their ratio is bounded by 2(1+h) on the denominator event.

## 2. A Fully Specified Perturbation Inequality

For a row vector u define the reciprocal stationary-weight norm

||u||_* = (sum_j u_j^2/r_j)^(1/2),

and let ||E||_* be its induced right-action operator norm. This is a private analytical norm, distinct from the pi-weighted left norm defined in the source.

Set H=diag(sqrt(r)) P diag(1/sqrt(r)). Detailed balance makes H symmetric. If u has coordinate sum zero, u diag(1/sqrt(r)) is orthogonal to sqrt(r). Therefore, with g=1-|lambda_2(P)|,

||uP||_* <= (1-g)||u||_*.

Let Q be any stochastic matrix, let nu be a stationary probability vector of Q, and suppose eta=||Q-P||_*<g. For any probability vector mu, u=mu-nu has coordinate sum zero and

||uQ||_* <= (1-g+eta)||u||_*.

Since mu(I-Q)=u(I-Q), the triangle inequality gives

||mu-nu||_* <= ||mu(I-Q)||_* /(g-eta).                                  (2)

In particular, Q has only one stationary probability vector: apply this inequality to any two of them. Existence follows from the finite-state stationary-distribution theorem, or directly by taking a convergent subsequence of Cesaro averages of probability vectors multiplied by powers of Q. The norm conversions needed below are

||u||_2 <= sqrt(r_max)||u||_*,
||u||_* <= ||u||_2/sqrt(r_min),
||E||_* <= sqrt(h)||E||_2 <= h||E||_2.

Thus when Q=hat P, g>gamma, and ||hat P-P||_*<=gamma/2, (2) implies

||mu-hat r||_2 <= (2sqrt(h)/gamma)||mu(I-hat P)||_2.                     (3)

This proves the exact perturbation statement used both for the population vector and for each leave-one-out vector. It does not require the empirical chain to be reversible.

## 3. Empirical Transition Concentration and the Global l2 Bound

Conditional on a graph with D>0, E=hat P-P is the sum, over present unordered pairs u<v and repetitions ell, of independent centered matrices

X_uvell = [(Y_uv^(ell)-b_uv)/(kD)] (e_u+e_v)(e_v-e_u)^T.

Each matrix has norm at most 2/(kD). Since a Bernoulli variance is at most 1/4, the two matrix variance sums are bounded respectively by the graph's signless Laplacian and Laplacian, multiplied by 1/(2kD^2). Both graph matrices have operator norm at most 2D: for either sign, sum_edges(v_u +/- v_v)^2<=2D||v||_2^2. Hence both variance norms are at most 1/(kD).

Matrix Bernstein now gives

P(||E||_2>=u | A) <= 2n exp(-kD u^2/[2+4u/3]).

When kD>=L, substitution of u=80 sqrt(L/(kD)) yields failure at most 2n^-50. On E_D, k>=5 and n rho>=c0 L ensure kD>=L and

||E||_* <= 80h sqrt(L/(kD)) <= 80h sqrt(2/(c0 k)) <= gamma/2.            (4)

The last inequality holds for c0>=10240h^2/gamma^2. The constant may subsequently be increased for the absorptions.

A separate vector estimate, not (4) alone, supplies the logarithm-free l2 bound. Put z=rE. Its independent-summand representation is

z=sum_{u<v:A_uv=1} sum_ell [(Y_uv^(ell)-b_uv)(r_u+r_v)/(kD)](e_v-e_u)^T.

For every fixed unit vector v, the squared interval lengths of the scalar sum zv total at most

[4M^2/(kD^2)] sum_edges(v_v-v_u)^2 <= 8M^2/(kD).

Consequently

P(|zv|>t | A) <= 2 exp(-kD t^2/(4M^2)).

A Euclidean 1/2-net of the unit sphere has cardinality at most 5^n, as follows by the usual disjoint-ball volume argument for a maximal separated set. For this net, ||z||_2<=2 max_v|zv|. Taking t=10M sqrt(n/(kD)) and union bounding therefore gives

||z||_2 <= 20M sqrt(n/(kD))

except on an event of probability at most 2 exp(-(25-log 5)n). Apply (3) with mu=r, use rP=r, M sqrt(n)<=h||r||_2, and D>=n rho/2. On E_gap and the preceding events,

E_2:=||hat r-r||_2 <= C_h ||r||_2/[gamma sqrt(n rho k)].                (5)

In particular E_2/sqrt(n)<=C_h R/gamma for L>=1. Equations (2)-(5) also prove uniqueness of the empirical stationary distribution on the good event, so the public minimum-norm selection agrees with it there.

## 4. Leave-One-Out Objects and Their Independence

For each i, define off-diagonal rates

W_uv^(-i)=a_uv b_uv if u=i or v=i,
W_uv^(-i)=hat b_uv otherwise,

for u!=v. Let K^(-i) have these off-diagonal rates and diagonal entries minus their row sums. Define Q^(-i)=I+K^(-i)/n. Every off-diagonal rate lies in [0,1], so Q^(-i) is stochastic with diagonal at least 1/n. Its deterministic positive rates between i and every other vertex make it irreducible. Let mu^i be its unique stationary probability vector.

This definition uses no incident graph indicator or incident comparison outcome. Consequently mu^i is measurable with respect to all nonincident observations and is independent of the incident observations. In particular, random D is not used to define this vector. Stationarity is equivalent to mu^i K^(-i)=0 and is invariant under any admissible common positive rate normalization.

For j!=i define

bar r_j^(-i) = [sum_{l notin {i,j}}hat b_lj r_l + a_ij b_ij r_i] / [sum_{l notin {i,j}}hat b_jl + a_ij b_ji].

For the removed coordinate define bar r_i^(-i)=r_i, the ratio obtained by replacing all of that coordinate's incident rates by their expectations and using detailed balance. Each denominator for j!=i is strictly positive because a_ij b_ji>0. Thus the entire vector is defined and is independent of incident data. Put delta^i=mu^i-bar r^(-i).

The centered numerator of bar r_j^(-i)-r_j is

sum_{l notin {i,j}}(hat b_lj r_l-hat b_jl r_j).

Conditional on the graph, Hoeffding applies to its independent nonincident comparisons with total squared interval lengths at most 4M^2D_j/k. The denominator is at least B_j-1, which is at least D_j/[4(1+h)] on the denominator event for sufficiently large n. Applying the same threshold as in Section 1 and union bounding over the at most n^2 ordered pairs gives

max_i ||bar r^(-i)-r||_infinity <= C_h R                              (6)

with additional failure O(n^-18). For j=i the error is exactly zero. These concentration estimates are established before conditioning on the leave-one-out vectors; no remaining randomness is incorrectly claimed for an already fixed auxiliary vector.

## 5. Coordinate Decomposition and Heterogeneous Sampling

Let x=||hat r-r||_infinity and c_i=||hat r-mu^i||_2. Adding and subtracting mu^i and bar r^(-i) in the stationary equation gives the exact decomposition

hat r_i-bar r_i=(T_1i+T_2i+T_3i)/B_i,

T_1i=sum_{j!=i}hat b_ji(hat r_j-mu_j^i),
T_2i=sum_{j!=i}hat b_ji delta_j^i,
T_3i=sum_{j!=i}hat b_ji(bar r_j^(-i)-r_j).

Cauchy-Schwarz and (6) imply

|T_1i|/B_i <= 2(1+h)c_i/sqrt(D_i),
|T_3i|/B_i <= C_h R.                                                   (7)

The second inequality uses sum_j hat b_ji<=D_i and the established lower bound for B_i, not equality of incoming and outgoing sums.

For T_2i condition on the sigma-field generated by all nonincident observations and all pre-generated incident comparison fractions. Then delta^i and the fractions are fixed, whereas the incident A_ij remain independent Bernoulli(a_ij). Its conditional mean is

sum_{j!=i}a_ij tilde b_ji delta_j^i.

The absolute value is at most sqrt(sum_j a_ij^2)||delta^i||_2. The rowwise variation assumption and E_D give

sqrt(sum_j a_ij^2) <= sqrt(s)m_i/sqrt(n) <= 2sqrt(s)D_i/sqrt(n).

For the centered sum, the coefficients have absolute value at most ||delta^i||_infinity and the conditional variance is at most m_i||delta^i||_infinity^2. Scalar Bernstein with t=20L therefore bounds its absolute value by

C||delta^i||_infinity(sqrt(m_i L)+L)

with conditional failure at most 2n^-20. This estimate remains meaningful when the coefficient vector or variance is zero.

Define v_i=sqrt(L/D_i)+L/D_i. Using (6),

||delta^i||_2 <= c_i+E_2+C_h sqrt(n)R,
||delta^i||_infinity <= c_i+x+C_h R.

After division by B_i and use of m_i<=2D_i, the preceding bounds yield, simultaneously over i,

|T_2i|/B_i <= C_h{sqrt(s)(c_i+E_2)/sqrt(n) + sqrt(s)R + v_i(c_i+x+R)}.   (8)

All conditioning here precedes intersection with E_D, denominator events, and E_gap; these events are subsequently used only to simplify bounds.

## 6. Full/Leave-One-Out Displacement

Let K be the empirical rate generator, with off-diagonal entries hat b_uv and diagonal entries minus their row sums. Thus hat P=I+K/D when D>0. Since mu^i K^(-i)=0,

mu^i(I-hat P)=mu^i(K^(-i)-K)/D.

Equation (3) therefore gives

c_i <= (2sqrt(h)/gamma)||mu^i(K^(-i)-K)/D||_2.                          (9)

No claim that I+K^(-i)/D is stochastic is needed.

Introduce the intermediate generator K^(i,A), which uses A_uv b_uv on incident pairs and retains the empirical rates on nonincident pairs. Split the residual in (9) into a graph part G_i=mu^i(K^(-i)-K^(i,A))/D and a comparison part H_i=mu^i(K^(i,A)-K)/D.

For the graph part, detailed balance shows r(K^(-i)-K^(i,A))=0. Set e=mu^i-r. For j!=i, its coordinate is

(G_i)_j=(a_ij-A_ij)(e_i b_ij-e_j b_ji)/D,

and its i-th coordinate is minus the sum of the other coordinates. Conditional on all nonincident observations, e and the coefficients are fixed. Their magnitudes are at most 2||e||_infinity.

For the non-i coordinates, deterministically on E_D,

sum_{j!=i}(a_ij-A_ij)^2 <= D_i+sum_j a_ij^2 <= D_i+m_i <= 3D_i.

This uses the actual absent-edge coefficient a_ij, not the lower bound rho. For the i-th coordinate, apply scalar Bernstein directly to the unnormalized weighted sum. Its variance is at most 4||e||_infinity^2 m_i and its summands are bounded by 2||e||_infinity. Thus, with failure at most 2n^-20,

||G_i||_2 <= [C||e||_infinity/D](sqrt(D_i)+sqrt(m_i L)+L)
             <= C||e||_infinity v_i.                                  (10)

Applying concentration to the unnormalized sum avoids treating random D as a fixed conditional coefficient. The norm bound also follows from the rowwise squared-probability bound; the simpler inequality a_ij^2<=a_ij suffices at this particular step.

For the comparison part, conditional on the full graph and all nonincident comparisons, mu^i is fixed and the incident comparisons remain independent. For j!=i,

(H_i)_j=A_ij(mu_i^i+mu_j^i)(b_ij-tilde b_ij)/D,

and again the i-th coordinate is minus their sum. Individual Hoeffding estimates give |epsilon_ij|<=sqrt(10L/k) simultaneously for the needed pairs with failure O(n^-18). For the i-th coordinate, apply Hoeffding directly to the weighted sum, whose total squared interval lengths before division by D are at most 4||mu^i||_infinity^2 D_i/k. It follows that, simultaneously over i,

||H_i||_2 <= [C||mu^i||_infinity/D]sqrt(D_i L/k)
             <= C||mu^i||_infinity t_i,

t_i=sqrt(L/(kD_i)).                                                     (11)

In particular, the weights mu_i^i+mu_j^i are retained inside the concentration argument; they are not pulled out of an absolute signed sum.

The elementary bounds ||mu^i-r||_infinity<=x+c_i and ||mu^i||_infinity<=M+x+c_i, combined with (9)-(11), give

c_i <= (K_h/gamma){M t_i+(x+c_i)(t_i+v_i)}.                             (12)

On E_D,

t_i<=sqrt(2/(5c0)),
v_i<=sqrt(2/c0)+2/c0,
M t_i<=sqrt(2)R.

Choose c0=c0(h,gamma), still at least 10240h^2/gamma^2, large enough that

(K_h/gamma){sqrt(2/(5c0))+sqrt(2/c0)+2/c0} <= 1/4.

Then (12) and ordinary algebra yield

c_i <= K'_h R/gamma + x/3                                               (13)

simultaneously for all i. This is the required displacement absorption. There is no dependence on s in this choice of c0.

## 7. Final Absorption and Probability

Let c=max_i c_i and v=max_i v_i. Combine (1), (7), and (8), and use (5). For constants with the stated dependencies,

x <= C_{h,s}(1+gamma^-1)R + alpha_n c + beta_n x,

alpha_n=C_h(d^-1/2+sqrt(s)n^-1/2+v),
beta_n=C_h v.                                                          (14)

The constants C_h in (14) may be chosen as one fixed sufficiently large constant before choosing c0. Increase c0, still using only h and gamma, so that

C_h(sqrt(2/c0)+2/c0)<=1/8.

For sufficiently large n, since d>=c0 L/2 and s is fixed,

C_h(d^-1/2+sqrt(s)n^-1/2)<=1/8.

Thus alpha_n<=1/4 and beta_n<=1/8. Substitute (13) into (14). The coefficient of x is at most alpha_n/3+beta_n<=5/24<1/2, while the coefficient of R is bounded by C_1(h,s)/gamma+C_2(h,s). Absorption therefore gives

x/M <= (c_1/gamma+c_2)sqrt(log n/(n rho k))

for positive constants c_1,c_2 depending only on h,s. No extra gamma dependence is hidden in these constants. The sufficiently-large-n threshold may depend on the fixed h,s,gamma.

The concentration events above have total failure O(n^-10): degree and denominator failures have the indicated polynomial bounds, the matrix failure is smaller, the directional-net failure is exponentially small, and at most O(n^2) scalar events have failure O(n^-20) each. They were constructed without conditioning incident graph indicators on E_gap. Intersecting them with E_gap adds at most n^-5, giving total failure O(n^-5). Equivalently, their remaining failure conditional on E_gap is O(n^-10), since P(E_gap)>=1-n^-5.

Finally, the public estimator is defined everywhere. A finite stochastic matrix has a nonempty compact convex set of stationary probability vectors, on which the squared Euclidean norm has a unique minimizer. For each fixed n,k the observation space is finite, so this selection is measurable. If D=0 then P=I and E_gap fails for n>=2. Zero denominators are likewise excluded by the good event. Deterministic edges, rho=1, equal scores, and zero conditional variances require no separate restriction. On the good event the empirical stationary vector is unique by (2), so every permitted stationary selection has the bound.

## Theorem-Critical Obligation Ledger

- Closed: the observation law, normalization, stationary-vector domain, and exceptional outcomes.
- Closed: simultaneous degree, denominator, and direct coordinate controls.
- Closed: reversible row-vector contraction and the precise residual perturbation inequality, derived in Section 2.
- Closed: empirical transition concentration, including summand and variance bounds, in Section 3.
- Closed: the logarithm-free global l2 numerator and error bounds, using the explicit directional-net calculation in Section 3.
- Closed: leave-one-out existence, coordinate definitions, and independence from incident graph and comparison data.
- Closed: heterogeneous conditional means, coefficient-aware graph fluctuations, and comparison fluctuations.
- Closed: displacement and entrywise absorptions with the required constant dependencies and unconditional probability.

There is no unresolved specialized external dependency or private ground-truth proof gap.
