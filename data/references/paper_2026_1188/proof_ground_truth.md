# Reference Proof

## Proof Structure

1. Verify that the charge construction is well-defined and identify the support properties of its components.
2. Construct strategies whose payoff tends to one, proving the value is one.
3. Assume a strategy attains payoff one and use the threshold set of stages with expected reward above one half to force full measure under both charge components.
4. Use the paired-stage reward identity, translation invariance, and the accumulation-point property to obtain a contradiction.
5. Conclude that the supremum is not attained by any behavioral strategy.

## Background Verification

The public task supplies compactness and translation invariance. The following verifications also close the corresponding background dependencies privately; solvers need not reproduce them.

Tychonoff's theorem states that a product of compact spaces is compact. Embed the space of charges in the compact Hausdorff product [0,1]^{P(N)}. Normalization and each finite-additivity equation are closed coordinate conditions, so the space of charges is closed and therefore compact Hausdorff. The equations lambda({k})=0 also define a closed subspace, namely the diffuse charges.

In a compact space, the closures of the tails of a sequence have the finite-intersection property and hence a common point. Every neighborhood of such a point meets every tail. Directing neighborhood-and-tail requirements by refinement produces a convergent subnet whose indices tend to infinity. In particular, the empirical charges eta_m(A)=|A intersect {1,...,m}|/m have a tail accumulation point. At every set possessing an asymptotic density, the corresponding coordinate of eta_m converges to that density. Each singleton coordinate tends to zero. Thus this accumulation point is a frequency charge, establishing that the choice of phi is possible.

For completeness, translation invariance also follows directly from the frequency-charge definition. Fix A subset of N, and put C=A minus (A+1), D=(A+1) minus A, and K=N minus (C union D). For each m, the difference between the numbers of elements of C and D in {1,...,m} equals the corresponding difference for A and A+1, and is therefore either zero or one. Let F contain every second element of K in its increasing enumeration; this definition also applies when K is finite. The number of elements of F up to m differs from half the number of elements of K up to m by at most one. Consequently both C union F and D union F have asymptotic density 1/2. Since F is disjoint from C and D, the frequency property and finite additivity give phi(C)+phi(F)=phi(D)+phi(F), and hence phi(C)=phi(D). Adding the common part A intersect (A+1) gives phi(A)=phi(A+1).

The integral defined in the task is the uniform extension of the simple-function integral. Indeed, every bounded function admits finite-valued lower and upper approximations whose uniform difference tends to zero. For simple functions, finite additivity gives linearity, and positivity gives |integral s d lambda|≤||s||_infinity. These statements pass to uniform limits. Thus bounded-function integration is linear, positive, normalized, and linear in the integrating charge. All integrands used below are bounded functions on N, where every subset is in the domain of each charge.

## Complete Proof

### Charge construction

The densities of E_0 and E_n are 1/2 and 2^{-n}, respectively. Hence mu_0(N)=2 phi(E_0)=1 and mu_n(N)=2^n phi(E_n)=1 for every n≥1. Their definitions preserve nonnegativity and finite additivity, and they vanish on singletons because phi does. Thus they are diffuse probability charges.

Choose the tail-convergent subnet defining mu_*. Passing to the limit in every singleton coordinate shows that mu_* is diffuse. For fixed n≥1 and every m≥n, E_m is contained in E_n, so

mu_m(E_n)=2^m phi(E_m)=1.

Pointwise convergence along the subnet, whose indices tend to infinity, gives mu_*(E_n)=1. In particular, mu_*(E_1)=1 and mu_*(E_0)=0, since E_0 is the complement of E_1. Also mu_0 gives zero charge to every subset of E_1. Finally, mu=(mu_0+mu_*)/2 is a diffuse probability charge.

### Value

Let q_t be the expected reward at stage t under a behavioral strategy. Since 0≤q_t≤1, positivity and normalization of the integral imply that every payoff is at most one.

For n≥1, let E_n^-={2^n k-1:k≥1}. Define a pure strategy sigma_n that chooses B at odd stages in E_n^- and T at all other odd stages. The only actions at even stages are forced. Its reward-one stages are exactly

R_n=(E_0 minus E_n^-) union E_n.

Using the support properties established above,

u_mu(sigma_n)=mu(R_n)
= (1/2) mu_0(E_0 minus E_n^-) + (1/2) mu_*(E_n).

The set E_n^- is contained in E_0 and has asymptotic density 2^{-n}. Therefore

mu_0(E_0 minus E_n^-)=2[phi(E_0)-phi(E_n^-)]=1-2^{-(n-1)}.

Together with mu_*(E_n)=1, this gives

u_mu(sigma_n)=1-2^{-n}.

This calculation also holds for n=1, when E_0 minus E_1^- is empty. Taking n arbitrarily large and using the universal upper bound proves v_mu=1.

### Nonattainment

Suppose, for contradiction, that a behavioral strategy sigma has u_mu(sigma)=1. Set

W={t in N:q_t>1/2}.

Pointwise, 1-q_t≥(1/2)1_{N minus W}(t). Positivity and linearity of integration imply

0=1-u_mu(sigma)≥(1/2)mu(N minus W).

Thus mu(W)=1. Since mu=(mu_0+mu_*)/2 and each component is a probability charge, mu_0(W)=mu_*(W)=1.

For every odd k, the realized rewards satisfy r_k+r_{k+1}=1 on every play. This holds for either action at stage k and is unaffected by earlier history or randomization. Taking expectations gives q_k+q_{k+1}=1.

For n≥1, every element of E_n is even and at least two. Therefore the predecessor set (W intersect E_n)-1 is a subset of N. If k belongs to this set, then k is odd and q_{k+1}>1/2, so q_k<1/2. Consequently

(W intersect E_n)-1 is contained in E_0 minus W.

If mu_n(W)>0 for some n≥1, then phi(W intersect E_n)>0. Applying translation invariance to the predecessor set gives

phi((W intersect E_n)-1)=phi(W intersect E_n)>0.

The containment and monotonicity then imply phi(E_0 minus W)>0. Finite additivity yields

mu_0(W)=2 phi(W intersect E_0)
=2[phi(E_0)-phi(E_0 minus W)]<1,

contradicting mu_0(W)=1.

It follows that mu_n(W)=0 for every n≥1. Evaluating W along the subnet defining mu_* now gives mu_*(W)=0, contradicting mu_*(W)=1.

Thus no behavioral strategy has payoff one. Every payoff is at most one, so every payoff is strictly below one. Since v_mu=1, the value is not attained by any pure or randomized strategy.

## Obligation Closure

The construction's existence, normalization, and diffuseness; the limiting component's support; integration of every relevant bounded sequence; the approximation payoffs; the threshold implication; the pathwise paired-stage identity for arbitrary behavioral strategies; and both contradiction cases have all been verified. No specialized external proof obligation remains unresolved.
