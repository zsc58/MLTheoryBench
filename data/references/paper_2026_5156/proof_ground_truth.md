# Reference Proof

## Proof Structure and Obligations

The proof retains the following four stages: reduce reward-law ambiguity to mean rewards; separate the global problem over prompts; evaluate the fixed-prompt adversary; and solve the l1 problem by thresholding and reward-ordered allocation.

The theorem-critical obligations are:

1. Establish absolute integrability of the relevant returns and measurable versions of the mean rewards.
2. Prove both directions of the identification of feasible mean rewards with measurable pointwise norm-ball selections.
3. Justify the comparator maximum and the adversarial supremum over prompts, including measurable admissibility.
4. Justify the outer infimum over measurable policies for every permitted p.
5. Derive the dual-norm vertex formula, including norm endpoints and zero support-function vectors.
6. Derive the l1 formula and its attaining perturbation.
7. Prove threshold feasibility, optimal slack allocation, and optimal threshold selection, including ties and breakpoints.
8. Prove measurability and global optimality of the displayed policy.

All eight obligations are closed below. The independent background used consists of the following standard facts: Tonelli's theorem for nonnegative jointly measurable functions; Fubini's theorem for absolutely integrable jointly measurable functions; Jensen's inequality for convex functions of integrable random variables; and finite-dimensional Holder norm duality. The applicable statements and hypotheses are made explicit where used. No specialized external theorem or unresolved paper-specific dependency is required.

## 1. Integrability and Exact Mean-Reward Reduction

Fix an admissible reward model, with jointly measurable realization R on the auxiliary probability space. A coupling with a point mass has its second coordinate fixed. Consequently, for each prompt,
\[
W_{q,\|\cdot\|_p}(P_x,\delta_{r(x)})^q
=\mathbb E_\nu\|R(\omega,x)-r(x)\|_p^q.
\]
The right side is measurable in x by Tonelli. The ambiguity condition and Jensen's inequality for the scalar function u mapped to u^q give, almost everywhere,
\[
\mathbb E_\nu\|R(\omega,x)-r(x)\|_p\le\delta.
\]
For q=1 this is the same moment bound, so no separate argument or higher moment is needed.

Since the infinity norm is at most the p norm, another application of Tonelli yields
\[
\mathbb E_\nu\int_X\|R(\omega,x)\|_\infty\,D(dx)
\le\int_X\|r(x)\|_\infty\,D(dx)+\delta<\infty.
\]
Thus all policy returns under this law are absolutely integrable: the absolute value of the policy-weighted reward is at most the infinity norm of the reward vector. In particular, Fubini applies to every policy in the public class.

Define
\[
\bar r_P(x)=\mathbb E_\nu R(\omega,x)
\]
where the coordinate expectations are absolutely finite, and define it to equal r on the measurable exceptional null set. Coordinatewise integration gives a measurable version. Fubini proves
\[
J_P(\pi)=\mathbb E_D\langle\pi(x),\bar r_P(x)\rangle=J_{\bar r_P}(\pi).
\]
The comparator remains one measurable policy for the chosen reward law; it does not depend on the auxiliary reward realization.

By convexity of the norm and the preceding first-moment bound,
\[
\|\bar r_P(x)-r(x)\|_p
\le\mathbb E_\nu\|R(\omega,x)-r(x)\|_p\le\delta
\]
almost everywhere. Conversely, any measurable s satisfying this norm bound almost everywhere is integrable, since its infinity norm is at most the infinity norm of r plus delta almost everywhere. The deterministic random function R(omega,x)=s(x), realized on a one-point probability space, is jointly measurable and has
\[
W_{q,\|\cdot\|_p}(\delta_{s(x)},\delta_{r(x)})=\|s(x)-r(x)\|_p.
\]
It therefore defines a feasible reward law with mean s. This proves the exact characterization of feasible means, modulo D-null sets, in both directions.

The public almost-everywhere convention does not change the source's everywhere-constrained objective. Indeed, the set where the displayed q-th error moment exceeds delta to the q-th power is measurable and D-null. Resetting R to r on that set is jointly measurable, satisfies the bound at every prompt, and leaves all returns unchanged. No independence of rewards at different prompts is imposed or used.

## 2. Measurable Separation Over Prompts

For any vector s and simplex point z,
\[
\operatorname{Reg}(z,s)=\max_i s_i-\langle z,s\rangle,
\]
because a simplex-weighted average of the coordinates of s is at most their largest coordinate, with equality at a maximizing vertex.

For a measurable feasible mean reward s, choose the smallest index attaining the largest coordinate of s(x). Its level sets are measurable, so the resulting vertex-valued comparator belongs to the policy class. It attains
\[
\max_{\beta\in\Pi}\{J_s(\beta)-J_s(\pi)\}
=\mathbb E_D\operatorname{Reg}(\pi(x),s(x)).
\]
Both sides are finite by the integrability established above.

It remains to justify the other separations without treating arbitrary, potentially nonmeasurable pointwise choices as admissible policies or rewards. Let B be the closed p-norm ball of radius delta in finite-dimensional Euclidean space. It is compact and has a countable dense sequence (d_j). For fixed measurable pi, define
\[
f_\pi(x,d)=\operatorname{Reg}(\pi(x),r(x)+d),
\qquad
F_\pi(x)=\max_{d\in B}f_\pi(x,d).
\]
For each x the function in d is continuous, and for each fixed d it is measurable in x. Hence
\[
F_\pi(x)=\sup_j f_\pi(x,d_j)
\]
is measurable. Moreover,
\[
0\le F_\pi(x)\le 2\bigl(\|r(x)\|_\infty+\delta\bigr),
\]
so F_pi is integrable.

For any epsilon greater than zero, select the first index j(x) such that
\[
f_\pi(x,d_{j(x)})>F_\pi(x)-\varepsilon.
\]
Such an index exists by density; the first-index rule is measurable because it uses a countable sequence of measurable inequalities. Thus s_epsilon(x)=r(x)+d_{j(x)} is a measurable feasible deterministic mean reward. Every feasible s has regret at most F_pi almost everywhere, while this selection has expected regret at least the expectation of F_pi minus epsilon. Letting epsilon decrease to zero, and using the exact mean-reward characterization, proves
\[
\sup_{P\in\mathcal U_{p,q,\delta}}
\left[\max_{\beta\in\Pi}J_P(\beta)-J_P(\pi)\right]
=\mathbb E_D\Psi_p(\pi(x);r(x)). \tag{A}
\]
This is a supremum argument and does not assume an unproved measurable maximizing selector.

For the outer infimum, observe that for any z,w in the simplex,
\[
|\Psi_p(z;r(x))-\Psi_p(w;r(x))|
\le\|z-w\|_1\bigl(\|r(x)\|_\infty+\delta\bigr).
\]
To see this, for each fixed perturbation d the two regrets differ by minus the inner product of z-w and r(x)+d; taking maxima preserves the same bound. Thus the objective is continuous in the policy vector.

Choose a countable dense sequence (z_j) in the simplex and set
\[
v(x)=\inf_{z\in\Delta_n}\Psi_p(z;r(x))
=\inf_j\Psi_p(z_j;r(x)).
\]
Each term is measurable by the preceding countable-ball representation. Therefore v is measurable and lies between zero and the same integrable upper bound. For epsilon greater than zero, choose the first j(x) satisfying
\[
\Psi_p(z_{j(x)};r(x))<v(x)+\varepsilon.
\]
This defines a measurable policy. Every measurable policy has expected objective at least the expectation of v, while these policies have expected objective at most that expectation plus epsilon. Consequently
\[
\inf_{\pi\in\Pi}\mathbb E_D\Psi_p(\pi(x);r(x))
=\mathbb E_D\inf_{z\in\Delta_n}\Psi_p(z;r(x)).
\]
Together with (A), this proves (1) for every permitted p and q. No infimum-supremum interchange has been used.

## 3. Fixed-Prompt Adversary

Fix a prompt and suppress x. Finite-dimensional Holder duality states that for v in R^n, delta greater than zero, and dual exponents p and p*,
\[
\max_{\|d\|_p\le\delta}\langle v,d\rangle=\delta\|v\|_{p^*}.
\]
The upper bound is Holder's inequality. Equality is obtained, for nonzero v and 1<p<infinity, by
\[
d_j=\delta\,\frac{\operatorname{sgn}(v_j)|v_j|^{p^*-1}}{\|v\|_{p^*}^{p^*-1}}.
\]
Indeed, using (p*-1)p=p* shows its p norm is delta, and direct substitution gives the claimed inner product. For p=infinity take d_j=delta times the sign of v_j, with sign zero equal to zero. For p=1 choose a coordinate of largest absolute value and put the signed budget on that coordinate. If v=0, take d=0 rather than using a normalized expression. These cases verify the identity throughout the required domain.

The two maxima in the definition of Psi are over compact finite-dimensional sets with a continuous objective. They may be interchanged as maxima over a Cartesian product, giving
\[
\Psi_p(z;r)
=\max_{b\in\Delta_n}\left\{\langle b-z,r\rangle+\delta\|b-z\|_{p^*}\right\}.
\]
The function in braces is convex in b. More explicitly, writing b as the convex combination of vertices with coefficients b_i, its value is at most the corresponding convex combination of its vertex values and hence at most their maximum. Vertices are feasible, so
\[
\Psi_p(z;r)=\max_i\left\{r_i-\langle z,r\rangle+\delta\|e_i-z\|_{p^*}\right\},
\]
which is (2).

For an active index k, the support-function maximizer for v=e_k-z attains the full adversarial objective: evaluating regret at comparator e_k gives the value of Psi, and regret cannot exceed Psi. This also handles v=0 by the preceding zero-vector convention.

For p=1, the ith coordinate of e_i-z has absolute value 1-z_i; every other coordinate has absolute value z_j, which is at most their sum 1-z_i. Thus
\[
\|e_i-z\|_\infty=1-z_i.
\]
This reasoning includes n=1, when both sides are zero and there are no other coordinates. Substituting into (2) gives (3). If k maximizes r_i-delta z_i, then
\[
\langle e_k-z,\delta e_k\rangle=\delta(1-z_k)=\delta\|e_k-z\|_\infty.
\]
Therefore d=delta e_k attains the maximum defining Psi_1, including when e_k=z.

## 4. Threshold Optimization and the Global Policy

Work first at a prompt where r_1 is at least r_2, and so on through r_n. By (3), minimizing Psi_1 is equivalent to maximizing
\[
\langle z,r\rangle-t
\]
subject to z in the simplex and t at least r_i-delta z_i for every i. For a fixed t, these inequalities are equivalent to
\[
z_i\ge\ell_i(t):=\frac{(r_i-t)_+}{\delta}.
\]
They are feasible exactly when the sum of the lower bounds is at most one.

Let A_r(t)=sum_i(r_i-t)_+. It is continuous, tends to infinity as t tends to minus infinity, and equals zero for t at least max_i r_i. It is strictly decreasing on the region where it is positive: if t<u and A_r(u)>0, at least one positive summand decreases strictly between t and u, while no summand increases. Since delta is positive, there is a unique finite t_0 with A_r(t_0)=delta. The feasible thresholds are exactly t at least t_0.

For such a threshold, write any feasible z as ell(t)+eta, where eta has nonnegative coordinates and total mass 1-sum_i ell_i(t). Reward ordering gives
\[
\langle z,r\rangle
\le\sum_i\ell_i(t)r_i+r_1\left(1-\sum_i\ell_i(t)\right).
\]
Equality is attained by allocating all residual mass to coordinate 1. This gives
\[
z_i(t)=\frac{(r_i-t)_+}{\delta}\quad(i\ge2),
\qquad
z_1(t)=1-\frac1\delta\sum_{i=2}^n(r_i-t)_+.
\]
In particular, z_1(t) is its own lower bound plus the nonnegative residual, so all simplex and epigraph constraints hold. Ties in the rewards do not invalidate this choice; they may merely allow other optimal allocations.

The resulting objective is
\[
h(t)=r_1-t-\frac1\delta\sum_{i=2}^n(r_1-r_i)(r_i-t)_+.
\]
Its right derivative at every t is
\[
h'_+(t)=-1+\frac1\delta\sum_{i:r_i>t}(r_1-r_i).
\]
The sum in this expression is nonnegative, nonincreasing, and right-continuous, since its coefficients are nonnegative and there are only finitely many reward levels. Consequently h is concave and piecewise linear. The set defining t* is nonempty, because t=r_1 belongs to it, and its infimum is attained by right-continuity. Thus t_0 is at most t*, which is at most r_1.

Before the first feasible threshold with nonpositive right derivative, every segment has positive slope. At and after that threshold the right derivative is nonpositive. If t*=t_0, only the latter statement is needed. If t*>t_0, the left derivative at t* is nonnegative and the right derivative is nonpositive. Therefore t* maximizes h on [t_0,infinity). This argument includes simultaneous breakpoints, zero-slope intervals, and equality in the threshold condition. The policy z(t*) consequently minimizes Psi_1.

We next verify that the public formulas define a measurable policy on all of X, not merely pointwise optimizers with unspecified selection. For any two vectors r,u with infinity-norm distance at most epsilon,
\[
A_u(t_0(r)+\varepsilon)\le A_r(t_0(r))=\delta.
\]
Minimal feasibility gives t_0(u) at most t_0(r)+epsilon, and reversing r and u gives the opposite bound. Hence t_0 is a Lipschitz continuous function of the reward vector and t_0(x) is measurable.

For every finite reward vector, even if it is not ordered, the set defining t* is nonempty: at t=max_i r_i its sum is zero. Its infimum is finite and at least t_0. For a fixed vector the sum in that definition is a right-continuous step function with finitely many breakpoints. Every feasible threshold therefore has feasible rational thresholds arbitrarily close on its right. For every real c,
\[
\{x:t^*(x)<c\}
=\bigcup_{a\in\mathbb Q,\ a<c}
\left(\{x:t_0(x)\le a\}\cap
\left\{x:\sum_{i:r_i(x)>a}(r_1(x)-r_i(x))\le\delta\right\}\right).
\]
Each set on the right is measurable. This proves measurability of t* and hence of every displayed coordinate of pi*. Because t* is at least t_0, those coordinates are nonnegative and sum to one everywhere, including on the exceptional set where reward ordering might fail. On the full-measure ordered set they minimize Psi_1 by the preceding argument.

For n=1, these formulas give t_0=t*=r_1-delta and pi*_1=1, with zero regret. Equal rewards and all other ties are already covered by the same lower-bound and slope arguments. No zero-budget case is required, since delta is strictly positive in the task.

Finally, applying the pointwise optimality almost everywhere in (A) proves that pi* attains the global infimum in (1). More generally, for any measurable policy in the p=1 case, choose the smallest maximizing index of r_i(x)-delta pi_i(x). This index is measurable. The deterministic reward function
\[
s^*(x)=r(x)+\delta e_{k(x)}
\]
is integrable and feasible, and its point-mass law attains the global adversarial supremum by the perturbation result. This supplies the equality-attaining adversary asserted in the original reference proof.

## Source Alignment

The mean-reward argument follows theory_002 and theory_003, with explicit integrability supplied for their Fubini and Jensen steps. The measurable approximation arguments complete theory_004's product separations for the public measurable-policy domain. The dual calculation follows theory_006 and the standard-independent norm duality recorded in theory_020; its normalized interior formula retains the source's nonzero-vector qualification. The threshold optimization follows theory_008, with explicit breakpoint and measurability details. These are formalization completions, not substantive source repairs. There are no unresolved proof obligations.
