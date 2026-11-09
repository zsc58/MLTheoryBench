# Reference Proof

## Contract and proof obligations

The loss class uses outcome-wise smoothness, as stated in the repaired public task. All regret guarantees are upper bounds on expected regret for each fixed loss. The algorithm uses fresh conditional randomization; its samples need not be unconditionally independent when the sampling subspaces depend on the history.

We prove, in order: admissibility and the comparator identity; the smooth FTL and perturbation bounds; the interior geometric TV estimate; its extension to the actual boundary-supported sampling laws; stability summation; the affine-outcome and rotation-coupling BTPL bound; parameter substitution; and transfer to a non-anticipating adversary. No specialized external theorem is used to close these obligations.

Throughout the initial argument fix a deterministic outcome sequence. Write p_t=hat p_t, p_0=(1/d,...,1/d), and B(p)=L(p,p). A terminal draw at p_n may be introduced to define q_{n+1}; it is only an analysis variable.

## 1. Admissibility and comparator

For any p in the simplex, a sample U in H(p) has <p,U>=0 and |U_i|<=rho. Thus q_i=p_i(1+U_i)>=0 and sum_i q_i=1. This holds on boundary faces as well as in the interior. Symmetry gives E[U]=0 and E[diag(p)U]=0.

Properness gives min_q sum_t ell(q,y_t)=n B(p_n), because the empirical outcome distribution is p_n. Bounded measurable losses make every expectation below well defined.

## 2. Smooth losses: derive the FTL bound

First derive a consequence of the source's outcome-wise smoothness, rather than using it as a replacement definition. For an interior p, properness implies that the tangent gradient of q -> L(q,p) at q=p is zero. Averaging the outcome-wise smoothness inequalities therefore gives

L(q,p)-B(p) <= (beta/2)||q-p||_2^2.

This holds for boundary p as well: approach p through interior distributions, keep q fixed, and use continuity of each differentiable loss on the closed simplex.

The empirical update is p_t=((t-1)p_{t-1}+y_t)/t, including t=1 with the zero coefficient on p_0. Hence

t L(p_{t-1},p_t)=(t-1)B(p_{t-1})+ell(p_{t-1},y_t).

Telescoping gives the exact identity

sum_t ell(p_{t-1},y_t)-nB(p_n)
= sum_t t[L(p_{t-1},p_t)-B(p_t)].

Since ||y_t-p_{t-1}||_2^2<=2, the right side is at most beta sum_{t=1}^n 1/t. This proves the required logarithmic FTL guarantee directly, including the first round and boundary empirical distributions.

For the noisy prediction, use the outcome-wise smoothness inequality at p_{t-1}. Its linear term has zero expectation, so

E[ell(q_t,y_t)-ell(p_{t-1},y_t)] <= (beta/2) E||xi_t||_2^2.

Here is a complete noise-moment calculation. A uniform ball of radius rho in an m-dimensional Euclidean space has radial distribution P(R<=r)=(r/rho)^m. Thus E R^2=m rho^2/(m+2). Rotational symmetry makes its covariance rho^2 I/(m+2). In our sampler m=d-1, so

E[U_t U_t^T]=rho^2 Pi_{H(p_{t-1})}/(d+1).

Consequently

E||diag(p_{t-1})U_t||_2^2
= rho^2 tr(diag(p_{t-1})^2 Pi_{H(p_{t-1})})/(d+1)
<= rho^2 ||p_{t-1}||_2^2/(d+1)
<= rho^2/(d+1).

This is stronger than the source's sufficient O(rho^2 log d/d) estimate and holds without an interior assumption. Summing proves

Reg_ell(n) <= beta(1+log n)+beta n rho^2/(2(d+1)).

In particular it implies the requested smooth-loss bound after substitution.

## 3. Interior uniform-ellipsoid TV estimate

We establish the geometric estimate before applying it to the algorithm. Use dimension k>=2 and a noise radius r with 0<r<=1/2. For an interior p in Delta_k, define

E_r(p)={x in Delta_k: Q_p(x)<=r^2},
Q_p(x)=sum_i (x_i/p_i-1)^2.

A uniform sample in r B_2^k intersected with p-perp, mapped by u -> p+diag(p)u, is uniform on E_r(p), since this is an invertible affine map between the corresponding (k-1)-dimensional spaces.

Let p,p' be neighboring empirical averages on this same support, let j be the current outcome, and set a=1/(t-1), b=1/c_{t-1,j}. Assume the previous count is positive. The empirical update gives, in either orientation of the pair,

|p_i'/p_i-1|<=a for i!=j,
|p_j'/p_j-1|<=b,
and a<=b.

Indeed non-updated coordinates have ratio (t-1)/t or its inverse. For the updated coordinate, write its probabilities as c/(t-1) and (c+1)/t; both relative changes are at most 1/c.

### Correct section volume

Let A have orthonormal columns spanning the sum-zero hyperplane, let D=diag(p), and let v=1/sqrt(k) times the all-ones vector. In coordinates x=p+Az, the defining quadratic form is z^T A^T D^{-2}A z. Thus

V_r(p)=C_{k-1}r^{k-1} det(A^T D^{-2}A)^{-1/2}.

Complete A by v to an orthogonal matrix. The cofactor formula for the last diagonal entry of the inverse gives

det(A^T D^{-2}A)=det(D^{-2}) v^T D^2 v
=(prod_i p_i^{-2})||p||_2^2/k.

Therefore

V_r(p)=C_{k-1}r^{k-1} sqrt(k)(prod_i p_i)/||p||_2.

This corrects the source's projection-versus-section calculation. If b<=1/2, the coordinate ratios also imply

|log(V_r(p')/V_r(p))|<=2kb+2b<=3kb.

For the norm factor, use (1-b)||p||<=||p'||<=(1+b)||p||; for the product factor, use |log(1+delta_i)|<=2b.

### Quadratic-form perturbation

Assume b<=r<=1/2. For x in E_r(p), put s_i=x_i/p_i-1 and delta_i=p_i'/p_i-1. Then ||s||_2<=r and

Q_{p'}(x)-Q_p(x)
=sum_i [-2s_i delta_i(1+s_i)+delta_i^2(1-s_i^2)]/(1+delta_i)^2.

Since |s_i|<=1/2 and |delta_i|<=1/2, denominators are at least 1/4. Therefore

|Q_{p'}(x)-Q_p(x)|
<=12 sum_i |delta_i||s_i|+4 sum_i delta_i^2
<=12r(sqrt(k)a+b)+4(ka^2+b^2)
<=4ka^2+12sqrt(k)ar+16br.

If x belongs to E_r(p') instead, exchange p and p'. The same bidirectional coordinate-ratio bounds apply, and the normalized displacement in the containing ellipsoid again has norm at most r. Consequently, with

Q_* = sup_{x in E_r(p) union E_r(p')} |Q_{p'}(x)-Q_p(x)|,

we have Q_*<=4ka^2+12sqrt(k)ar+16br. This also proves the weaker quadratic-form estimate stated in the source, without its invalid denominator step.

### Shell and TV

Suppose t-1>=54k^{3/2}/r and c_{t-1,j}>=57k/r. The preceding estimate gives

k Q_*/r^2 <= 4/(54^2 k)+12/54+16/57 < 0.51.

Set epsilon=Q_*/r^2. The symmetric difference of the two ellipsoids lies in

{x: r^2-Q_*<=Q_p(x)<=r^2+Q_*}.

Indeed, for a point belonging to exactly one ellipsoid, compare its two quadratic-form values with r^2. The shell's outer radius in normalized coordinates is r sqrt(1+epsilon)<1, so it is not truncated by simplex nonnegativity. Its relative volume is

(1+epsilon)^{(k-1)/2}-(1-epsilon)^{(k-1)/2}=O(k epsilon),

with a universal constant because k epsilon<0.51. The same assertion applies with p and p' exchanged.

For uniform laws on sets A,B, integration of their densities gives

2 TV(Unif(A),Unif(B))
<= |V(A)-V(B)|/max(V(A),V(B))
   +V(A symmetric-difference B)/min(V(A),V(B)).

Use the shell based on the smaller-volume ellipsoid. The logarithmic volume bound gives a relative-volume term O(kb), and the shell gives O(kQ_*/r^2). The a^2 term is absorbed using the time threshold. Therefore

TV(Unif(E_r(p)),Unif(E_r(p')))
<= C[k^{3/2}/(r(t-1))+k/(r c_{t-1,j})].

This inequality, with a larger universal C, holds whenever the previous count is positive, without the numerical thresholds: if either threshold fails, the expression in brackets is at least 1/57, so TV<=1 suffices. This extension is important when integrating over a random radius below.

## 4. The actual sampling law on boundary faces

The algorithm does not sample uniformly from a face ellipsoid merely because p lies on that face. We now account for its actual ambient-dimensional law.

Suppose neighboring empirical averages have the same support I of size k>=2. Write m=k-1 and h=d-k. Orthogonally decompose

H(p)= {u supported on I: <u,p>=0} direct-sum R^{I-complement}.

A uniform radius-rho ball in this (d-1)-dimensional space can be sampled by first drawing its inactive component z and then drawing the active component uniformly from an m-dimensional ball of radius

R=sqrt(rho^2-||z||_2^2).

The inactive component has density proportional to R^m. This mixing law depends only on d,k,rho, not on p. Multiplication by diag(p) annihilates z. Conditional on z, the prediction is therefore uniform on E_R(p) within its active face.

For h=0, R=rho deterministically. For h>0, radial integration gives

E[R^{-2}]=(d-1)/((k-1)rho^2).

For completeness, write A_j=integral_0^rho s^{h-1}(rho^2-s^2)^{j/2} ds. The desired expectation is A_{m-2}/A_m. Integrating the derivative of s^h(rho^2-s^2)^{m/2}, whose boundary terms vanish, gives

h A_m=m(rho^2 A_{m-2}-A_m).

The formula follows, and it also agrees with the h=0 case. Cauchy-Schwarz now gives

E[R^{-1}]<=rho^{-1}sqrt((d-1)/(k-1)).

TV between mixtures with the same mixing law is at most the average conditional TV: this follows immediately by integrating the signed-measure differences, or by applying the triangle inequality to their densities under a common dominating measure. Applying the all-radius estimate from Section 3 yields

TV(F(p),F(p'))
<= C[k^{3/2}/(t-1)+k/c_{t-1,j}] E[R^{-1}]
<= C'[d^{3/2}/(rho(t-1))+d/(rho c_{t-1,j})].

The last inequalities use k>=2 and k<=d. If k=1 and the support does not change, both prediction laws are the same point mass, so TV is zero. A newly appearing outcome changes support and is handled as an exceptional round.

## 5. Stability summation

Let F_t be the prediction law at p_{t-1} for the fixed outcome sequence. For any measurable function f with |f|<=1,

|integral f dF-integral f dG|<=2 TV(F,G).

This remains valid for singular laws by taking F+G as a dominating measure. Thus the stability term satisfies

Stab = sum_t E[ell(q_t,y_t)-ell(q_{t+1},y_t)]
<=2 sum_t TV(F_t,F_{t+1}).

Charge t=1 directly. Also charge rounds with t-1<54d^{3/2}/rho or c_{t-1,i_t}<57d/rho directly by TV<=1. There are O(d^2/rho) such rounds: the first condition concerns an initial time interval, and for each outcome its pre-round count takes each integer value at most once on rounds when that outcome occurs. These exceptions include every support change.

On all other rounds apply Section 4. The time denominators sum to at most 1+log n, and the count denominators sum to at most d(1+log n), by summing a harmonic sequence for each outcome separately. Hence

Stab <= C d^2(1+log n)/rho.

## 6. Affine outcomes and BTL

We record and prove the BTL fact used here. For arbitrary functions f_1,...,f_n, if a_t minimizes sum_{s<=t}f_s, then sum_t f_t(a_t)<=sum_t f_t(a) for every fixed a. Inductively, the first t-1 terms are at most sum_{s<t}f_s(a_{t-1}), which is at most sum_{s<t}f_s(a_t); add f_t(a_t), and use the minimizing property at t for the final comparison. No convexity is needed.

Let ell_vec(q)=(ell(q,e_i))_i. For any sequence xi_t such that q_t=p_{t-1}+xi_t lies in the simplex, define nu_0=0 and nu_t=t xi_{t+1}. Set

f_t(q)=<ell_vec(q), y_t+nu_t-nu_{t-1}>.

The cumulative coefficient vector is t(p_t+xi_{t+1})=t q_{t+1}, so properness makes q_{t+1} a minimizer of sum_{s<=t}f_s. Apply BTL with comparator p_n and rearrange:

sum_t [ell(q_{t+1},y_t)-ell(p_n,y_t)]
<=sum_t <ell_vec(p_n)-ell_vec(q_{t+1}),nu_t-nu_{t-1}>
<=2 sum_t ||t xi_{t+1}-(t-1)xi_t||_1.

The artificial outcome vectors need not themselves be probabilities; only their cumulative vectors, divided by t, must be valid predictions. Thus no unmentioned extension of the prediction domain is used.

## 7. Rotation coupling and the expected BTPL bound

Continue to fix the entire outcome sequence. For this analysis only, draw U_1 correctly and set U_{t+1}=R_t U_t, where R_t is the plane rotation sending p_{t-1}/||p_{t-1}|| to p_t/||p_t|| and fixing the orthogonal complement of their span. Use the identity rotation if the directions agree. The directions are nonnegative and nonzero, so no antipodal ambiguity occurs. This construction preserves the required marginal uniform law at each time.

For such a plane rotation,

||R_t-I||op=||p_t/||p_t||-p_{t-1}/||p_{t-1}||||_2
<=2||p_t-p_{t-1}||_2/||p_{t-1}||_2
<=4sqrt(d)/t.

Here ||p_{t-1}||_2>=1/sqrt(d) and ||p_t-p_{t-1}||_2<=2/t. It follows that

||U_{t+1}-U_t||_2<=4sqrt(d)rho/t.

This is an operator-norm inequality, not the source's invalid claim that a rotation moves every unit direction equally far.

Let D_t=diag(p_t). Then

||xi_{t+1}-xi_t||_1
<=||(D_t-D_{t-1})U_{t+1}||_1
  +||D_{t-1}(U_{t+1}-U_t)||_1
<=2rho/t+4sqrt(d)rho/t.

For the first term use ||p_t-p_{t-1}||_1<=2/t and ||U_{t+1}||_infinity<=rho. For the second use sum_i p_{t-1,i}|v_i|<=||v||_infinity<=||v||_2. Also ||xi_{t+1}||_1<=rho. Consequently

||t xi_{t+1}-(t-1)xi_t||_1
<=||xi_{t+1}||_1+(t-1)||xi_{t+1}-xi_t||_1
<=7sqrt(d)rho.

Section 6 gives BTPL regret at most 14n sqrt(d)rho for every realization of this coupled sequence. Because the outcome sequence is fixed and the loss sum is additive over time, its expectation depends only on the one-time marginals. Therefore the original independently sampled sequence has the same expected BTPL loss and satisfies

BTPL <=14n sqrt(d)rho.

Do not claim that changing the coupling preserves realized regret for arbitrary independent draws. The source's stronger pathwise wording is qualified accordingly.

## 8. Combine and substitute

Insert the shifted prediction at each round. The decomposition is an equality of expected sums:

Reg_ell(n)=Stab+BTPL.

For bounded proper losses this proves

Reg_ell(n)<=C[d^2(1+log n)/rho+n sqrt(d)rho].

With rho=d^{3/4}/sqrt(n), both algebraic terms have order d^{5/4}sqrt(n), proving the first claim.

For smooth losses, Section 2 gives

Reg_ell(n)<=beta(1+log n)+beta d^{3/2}/(2(d+1))
=O(beta log n+beta sqrt(d) log d).

The last expression follows since d>=2 and rho<=1/2 implies n>=4d^{3/2}>1. Constants are universal and the algorithm does not depend on the loss or beta.

## 9. Non-anticipating adversaries

For a fixed loss define g(p,y)=E_{U uniform on rho B intersect p-perp}[ell(p+diag(p)U,y)]. The fixed-sequence proofs above establish, for every deterministic sequence of outcomes, the appropriate upper bound on

sum_t g(p_{t-1},y_t)-n B(p_n).

This is a deterministic inequality for every outcome path. Under a non-anticipating adversary, condition at round t on the past history and the chosen y_t. The fresh sampler has precisely its prescribed conditional law, so the conditional expected learner loss is g(p_{t-1},y_t). Taking expectations and summing identifies actual expected regret with the expectation of the preceding path functional. The deterministic inequality applies to every realized outcome path and proves the same bound.

This argument does not condition the noise on the complete future outcome sequence and does not attempt to impose the rotation coupling on the adaptive online experiment.

## Audit closure

All theorem-critical obligations are derived above. The corrected section calculation, boundary mixture, and coupling qualification repair local source errors while retaining the frozen expected-regret theorem. The specialized external FTL and adaptive-transfer citations are not needed as unproved dependencies. There are no remaining private proof-completeness warnings.
