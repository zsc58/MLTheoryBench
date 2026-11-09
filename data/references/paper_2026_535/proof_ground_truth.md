# Reference Proof

## Contract and proof obligations

The population domain consists of policies absolutely continuous with respect to the reference kernel. The reference reward law has a Lebesgue density for almost every context, so every admissible population policy also has a reward density. The empirical measure need not belong to this population domain: the estimator is the explicitly defined CDF plug-in estimator in the task.

The obligations are: normalization of the transformation; the population derivative and concavity; KL-relative smoothness; conditional empirical concentration with the stated seminorm; existence and uniqueness of the optimizer; the inexact KL three-point estimate; and geometrically weighted telescoping with the stated output experiment. All are established below.

Write b=r_max. Use A(u)=integral_0^u f(v)dv for the scalar antiderivative, F[pi]=-R[pi] for the loss's non-KL part, and K[pi]=KL(pi|pi_ref). These are different objects. Pairings and KL divergences are averaged over the fixed context distribution rho unless a context is explicitly fixed.

## 1. Transformation, population derivative, and concavity

Fix a context x outside the common rho-null set in the assumptions. Let C_pi(x,s) be the reward CDF. Absolute continuity of the reward law makes this an absolutely continuous function of s, with C_pi(x,0)=0 and C_pi(x,b)=1. The first equality uses the absence of an atom at zero.

The chain rule for absolutely continuous functions gives

integral f(C_pi(x,r(x,y))) pi(dy|x)
= integral_0^b f(C_pi(x,s)) dC_pi(x,s)
= A(1)-A(0)=1.

Thus the displayed transformation is a probability kernel. Integration by parts gives the conditional transformed reward

R_x[pi] = b A(1) - integral_0^b A(C_pi(x,s)) ds.

All integrands are bounded, so these identities and subsequent directional differentiations may be averaged over rho. For an admissible policy nu, let Delta C(x,s)=C_nu(x,s)-C_pi(x,s). The CDF of pi+a(nu-pi) is C_pi+a Delta C. Since f is continuous and bounded, differentiation under the integrals gives

<dR[pi],nu-pi>
= - integral_X integral_0^b f(C_pi(x,s)) Delta C(x,s) ds rho(dx).

The CDF directional derivative is obtained directly from its definition:

Delta C(x,s)=integral 1{r(x,y)<=s}(nu-pi)(dy|x).

Fubini therefore gives the bounded representative

dR[pi](x,y) = - integral_{r(x,y)}^b f(C_pi(x,s)) ds,

g_pi(x,y)=dF[pi](x,y)=integral_{r(x,y)}^b f(C_pi(x,s)) ds.

The derivative is defined modulo an additive function of x, which vanishes in every policy-difference pairing.

Because f is nondecreasing, A is convex. Since C_pi is affine in pi, integral_X integral_0^b A(C_pi(x,s)) ds rho(dx) is convex. Consequently R is concave. Equivalently,

R[nu] <= R[pi]+<dR[pi],nu-pi>.

## 2. KL-relative smoothness

The Lipschitz hypothesis implies the scalar estimate

0 <= A(v)-A(u)-f(u)(v-u) <= (L_f/2)(v-u)^2.

For each context and reward threshold,

|C_nu(x,s)-C_pi(x,s)| <= ||nu(.|x)-pi(.|x)||_1.

The standard Pinsker inequality used here is

||P-Q||_1^2 <= 2 KL(P|Q)

for probability measures P and Q; it is interpreted as trivial if the KL divergence is infinite. Applying it contextwise, integrating over s and x, and using the derivative just derived gives

0 <= F[nu]-F[pi]-<dF[pi],nu-pi>
<= L_f b KL(nu|pi).

This is the required relative-smoothness inequality. Every L>0 with L>=L_f b is a valid algorithmic upper bound. If L_f b>0, equality may be chosen. If L_f=0, the reward functional is linear and any positive L is valid; no division by zero is necessary.

## 3. Existence and uniqueness of the optimizer

Let Q(dx,dy)=rho(dx)pi_ref(dy|x), and represent an admissible policy by its density p with respect to Q. Such densities are nonnegative and satisfy integral p(x,y)pi_ref(dy|x)=1 for rho-almost every x. Their set is closed in L1(Q): conditional integration is an L1 contraction, and nonnegativity is preserved under L1 limits.

The transformation is normalized and the reward lies in [0,b], so 0<=R[pi]<=b. The reference policy has K[pi_ref]=0. Hence the infimum m of L[pi]=F[pi]+beta K[pi] is finite and has a finite-valued minimizing sequence.

For two finite-valued policies p and q and their midpoint v=(p+q)/2, convexity of F and the entropy identity imply

(L[p]+L[q])/2-L[v]
>= (beta/2)(KL(p|v)+KL(q|v))
>= (beta/8)||p-q||_1^2.

The last inequality is Pinsker, using ||p-v||_1=||q-v||_1=||p-q||_1/2. If p_n is a minimizing sequence, L[(p_n+p_k)/2]>=m makes p_n Cauchy in L1(Q). Let p_* be its admissible L1 limit.

The CDF representation gives continuity of R in this topology. Indeed, since |A(u)-A(v)|<=f(1)|u-v|,

|R[p]-R[q]| <= b f(1)||p-q||_1.

Relative entropy is lower semicontinuous under L1 convergence: take an almost-everywhere convergent subsequence and apply Fatou to the nonnegative integrand p log p-p+1. Therefore L[p_*]<=liminf L[p_n]=m, so p_* attains the infimum and has finite reference KL. The midpoint inequality proves uniqueness up to Q-null sets.

## 4. Conditional empirical-derivative error

The task defines

ghat_t(x,y)=integral_{r(x,y)}^b f(Chat_t(x,s)) ds.

This is the source's plug-in estimator, not differentiation of an atomic right-CDF-weighted objective. By Step 1, the population counterpart is g_pi_t. Set

Z_t(x)=sup_{0<=s<=b}|Chat_t(x,s)-C_pi_t(x,s)|.

Lipschitz continuity gives, for every y,

|e_t(x,y)| <= L_f b Z_t(x).

For the half-range seminorm used in the task, ||h||_sp,x<=ess sup_y |h(x,y)|. Consequently

||e_t||_sp,x^2 <= L_f^2 b^2 Z_t(x)^2.

The standard Dvoretzky-Kiefer-Wolfowitz inequality is the following distribution-free statement: for the empirical CDF C_M of M iid real observations with CDF C,

P(sup_s|C_M(s)-C(s)|>=u) <= 2 exp(-2 M u^2), u>0.

Its hypotheses hold conditional on the current policy and a fixed context because the M rewards are measurable functions of conditionally iid responses. No independence between samples at different contexts is used. Since 0<=Z_t(x)<=1, tail integration gives

E[Z_t(x)^2|pi_t]
= integral_0^1 2u P(Z_t(x)>u|pi_t) du
<= integral_0^infinity 4u exp(-2 M u^2) du
=1/M.

Thus, for rho-almost every x,

E[||e_t||_sp,x^2|pi_t] <= L_f^2 b^2/M.

Joint measurability and Tonelli allow these nonnegative bounds to be integrated over rho.

## 5. Inexact KL step and error absorption

Write u=pi_{t+1}, v=pi_t, and define the convex surrogate

H_t[nu]=<ghat_t-r_t,nu-v>+L KL(nu|v)+beta KL(nu|pi_ref).

The update equation says that its first variation at u is constant in y for each context. Expanding the logarithms directly yields, for every comparator nu with the finite KL divergences needed here,

H_t[nu]-H_t[u]=(L+beta)KL(nu|u).

This proves the needed three-point relation without invoking an unproved specialized mirror-descent theorem. Additive context-dependent constants vanish in the pairing. The assumed finite KL divergences justify the logarithmic pairings with pi_*.

Relative smoothness gives

L[u]-L[v]
<= <dF[v],u-v>+L KL(u|v)+beta(K[u]-K[v])
= <ghat_t,u-v> - <e_t,u-v>
  +L KL(u|v)+beta(K[u]-K[v]).

The subtraction of <e_t,u-v> is essential. The source omits it in one intermediate equality but restores it in the next combined estimate.

Apply the surrogate identity with nu=pi_*, then use convexity of F to bound <dF[v],pi_*-v> by F[pi_*]-F[v]. The result is

L[pi_{t+1}]-L[pi_*]
<= L D_t-(L+beta)D_{t+1}
  +<e_t,pi_*-pi_{t+1}>-<r_t,pi_*-pi_{t+1}>,

where D_t=KL(pi_*|pi_t).

For any real measurable h with finite conditional half-range seminorm, centering at the midpoint of its essential range and using Holder and Pinsker gives

|integral h(x,y)(P-Q)(dy)|
<= ||h||_sp,x ||P-Q||_1
<= ||h||_sp,x sqrt(2 KL(P|Q)).

Let A_t=integral_X ||e_t||_sp,x^2 rho(dx) and B_t=integral_X ||r_t||_sp,x^2 rho(dx). Cauchy-Schwarz over x followed by Young's inequality implies, for alpha>0,

|<e_t,pi_*-pi_{t+1}>| <= sqrt(2 A_t D_{t+1}) <= A_t/(2alpha)+alpha D_{t+1},

|<r_t,pi_*-pi_{t+1}>| <= B_t/(2alpha)+alpha D_{t+1}.

Taking alpha=beta/4 gives the pathwise one-step inequality

L[pi_{t+1}]-L[pi_*]
<= L D_t-(L+beta/2)D_{t+1}+2(A_t+B_t)/beta.

The conditional moment assumptions and Tonelli imply E[A_t]<=epsilon and E[B_t]<=delta. This argument requires neither unbiased estimation nor independence of the residual from the samples.

## 6. Geometric telescoping and output sampling

Set mu=L+beta/2, q=mu/L>1, and S_T=sum_{k=1}^T q^k=q(q^T-1)/(q-1). Multiply the inequality for the update t=k-1 by q^k and sum over k=1,...,T. The KL terms telescope exactly:

sum_{k=1}^T q^k(L[pi_k]-L[pi_*])
<= mu(D_0-q^T D_T)+(2/beta)sum_{k=1}^T q^k(A_{k-1}+B_{k-1}).

Drop the nonpositive terminal term, divide by S_T, and take expectations. The initial policy is fixed, so D_0 is deterministic. The fresh output-index draw satisfies P(hat t=k|the generated trajectory)=q^k/S_T. Therefore

E[L[pi_hat t]-L[pi_*]]
<= (mu/S_T)KL(pi_*|pi_0)+2(epsilon+delta)/beta
= ((beta/2)KL(pi_*|pi_0))/(q^T-1)+2(epsilon+delta)/beta.

Substitution of the conditional empirical estimate yields the floor

2 L_f^2 b^2/(beta M)+2 delta/beta.

The sampling contribution is dimension-independent and O(1/M). The entire floor is O(1/M) when delta=0 or, more generally, delta=O(1/M); it need not vanish with M when delta is fixed and positive.

## Source-repair and dependency notes

The source residual statement is not missing a reference-KL term: its surrogate already includes beta KL. The replacement uses the equivalent separated form with ghat_t. The source-local proof correction is instead the missing estimation-error pairing in the intermediate empirical-gradient substitution. The corrected material record identifies its original and repaired forms.

The population continuity/density restrictions come from the existing transformation and derivative records restored to the selected closure. The empirical plug-in convention comes from the source algorithm and concentration proof. The half-range seminorm and positive L come directly from the convergence assumptions. The only independent inequalities used are the explicitly stated Pinsker and DKW inequalities, elementary Holder/Cauchy-Schwarz and Young inequalities, and elementary integration and entropy arguments whose applications are verified above. No theorem-critical obligation remains unresolved.
