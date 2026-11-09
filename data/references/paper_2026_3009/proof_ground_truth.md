# Reference Proof

## Proof Structure

1. Prove pointwise optimality of utility-quantile threshold sets at every conditional coverage level, including both endpoints.
2. Reduce universal coverage to a scalar allocation problem.
3. Establish the dual bound, a minimizing multiplier, and the mean-coverage identity under uniqueness.
4. Reconstruct the threshold sets and prove optimality for both universal and policy-coupled formulations.

## Complete Proof

Write U=u_max, c=1-alpha, and Z_a=u(a,Y(a)). Since u is bounded, choose a finite L such that L<=u(a,y)<=U for all a,y. Use fixed versions of the conditional probability kernels given X. All assertions concerning feature values may be read almost surely, and the assumed measurable selections are used throughout.

### 1. Quantile properties and pointwise optimality

First consider any random variable Z supported on [L,U], with distribution function F. For r in [0,1), put q(r)=sup{z:F(z)<=r}. This is a finite number in [L,U]: every z<L belongs to the defining set, while no z>=U belongs to it. For every z<q(r), monotonicity of F and the definition of supremum imply F(z)<=r. Taking z increasing to q(r) gives

P(Z<q(r))<=r, and therefore P(Z>=q(r))>=1-r.

The function q is nondecreasing. It is also right-continuous on [0,1). Indeed, if r_n decreases to r, then q(r_n) decreases to a limit b>=q(r). If b>q(r), choose z strictly between them. For every n, z<q(r_n), so F(z)<=r_n. Consequently F(z)<=r, contradicting z>q(r).

Applied to each conditional utility law, these facts give, for t>0,

P(Z_a>=gamma(x,t,a)|X=x)>=t.

For t=0, gamma(x,0,a)=U and the required lower bound is zero, so coverage holds trivially. Thus the assertion holds for every t in [0,1], including t=1.

Fix x,a,t and any measurable outcome set B with conditional coverage at least t. Let b=inf_{y in B}u(a,y), using b=U when B is empty. If t=0, b<=U=gamma(x,0,a). If t>0, B cannot be empty. Were b>gamma(x,t,a), choose z strictly between these numbers. The event Y(a) in B implies Z_a>z, so P(Z_a<=z|X=x)<=1-t. This contradicts the supremum defining gamma. Hence in all cases

inf_{y in B}u(a,y)<=gamma(x,t,a).

Now define D_t(x,a)={y:u(a,y)>=gamma(x,t,a)}. These sets have conditional coverage at least t. Their worst-case utilities are at least their thresholds, including the empty-set case since the thresholds do not exceed U. The preceding upper bound gives equality for t>0. For t=0, D_0(x,a) consists of outcomes with utility U; it is either empty or has utility identically U, so its worst-case utility is again U. Therefore, for every t in [0,1],

inf_{y in D_t(x,a)}u(a,y)=gamma(x,t,a),

and nu_{D_t}(x)=theta(x,t).

In particular, any action-indexed system whose conditional coverage is at least t for every action has nu_C(x)<=theta(x,t).

### 2. Universal scalar reduction

For a measurable system C, let

p_a(x)=P(Y(a) in C(x,a)|X=x), and t_C(x)=min_{a in A}p_a(x).

The finite minimum is measurable. Fix an ordering of A and select its first minimizing action at every feature value. This gives a measurable deterministic policy with conditional coverage exactly t_C(x). Every other deterministic policy has conditional coverage at least t_C(x). By conditioning on X, universal feasibility is therefore equivalent to E[t_C(X)]>=c.

Pointwise optimality implies E[nu_C(X)]<=E[theta(X,t_C(X))]. Conversely, for any measurable t:mathcal X->[0,1] with E[t(X)]>=c, the threshold system D_t has conditional coverage at least t(x) for every action. It is universally feasible and has objective E[theta(X,t(X))]. Thus the universal problem equals the scalar program

sup{E[theta(X,t(X))]: t:mathcal X->[0,1] measurable, E[t(X)]>=c}.

### 3. Pointwise maximization and the dual minimizer

The conditional quantile properties imply that s->gamma(x,s,a) is nonincreasing and left-continuous for s>0. A finite maximum preserves these properties, so theta(x,s) is nonincreasing and left-continuous for s>0. Moreover theta(x,0)=U and theta(x,s)<=U. Consequently theta(x,.) is upper-semicontinuous on the entire compact interval [0,1]: at positive arguments this follows from monotonicity and left continuity; at zero it follows from the upper bound U.

For beta>=0, define

m_beta(x)=max_{s in [0,1]}{theta(x,s)+beta s},

D(beta)=E[m_beta(X)]-beta c.

Upper semicontinuity and compactness ensure that the pointwise maximum is attained. Measurability of m_beta follows, for example, by taking the supremum over rational s in [0,1] together with zero: every positive argument can be approached from below using left continuity. The maximizing selection g is measurable by the setup.

For every scalar-feasible t,

E[theta(X,t(X))]<=E[m_beta(X)]-beta E[t(X)]<=D(beta).

For each x, m_beta(x) is convex in beta, being a maximum of affine functions. For beta,beta'>=0,

|m_beta'(x)-m_beta(x)|<=|beta'-beta|.

Thus D is finite, continuous, and convex. Also

D(beta)>=E[theta(X,1)]+beta(1-c)>=L+alpha beta,

which tends to infinity. Hence D attains its minimum at some fixed beta*>=0.

### 4. Derivative formula and mean coverage

We derive the needed maximum-derivative formula rather than assuming it. Fix beta and a feature value x at which the maximizer at beta is unique, and put s_0=g(x,beta). For h>0, choose any pointwise maximizer s_h at beta+h. Comparing the two maxima gives

s_0 <= [m_{beta+h}(x)-m_beta(x)]/h <= s_h.

Every cluster point of s_h as h decreases to zero is a maximizer at beta. To see this, use compactness to take a convergent subsequence s_h->s_bar. The Lipschitz bound implies

theta(x,s_h)+beta s_h=m_{beta+h}(x)-h s_h -> m_beta(x).

Upper semicontinuity then gives theta(x,s_bar)+beta s_bar>=m_beta(x), so s_bar is a maximizer. Uniqueness implies s_bar=s_0. Every cluster point is therefore s_0, giving s_h->s_0 and right derivative m'_+(beta,x)=g(x,beta).

For beta>0, choose any maximizer r_h at beta-h, with 0<h<beta. The analogous comparison yields

r_h <= [m_beta(x)-m_{beta-h}(x)]/h <= s_0.

The same compactness and upper-semicontinuity argument gives r_h->s_0 and left derivative m'_-(beta,x)=g(x,beta).

All these difference quotients lie in [0,1]. At each fixed beta, uniqueness holds almost surely, so dominated convergence yields

D'_+(beta)=E[g(X,beta)]-c for beta>=0,

D'_-(beta)=E[g(X,beta)]-c for beta>0.

This argument uses uniqueness almost surely at each fixed beta; it does not require a common exceptional null set for all beta.

Since theta(x,0)=U>=theta(x,s), zero is a maximizer at beta=0. Uniqueness therefore gives g(x,0)=0 almost surely. It follows that D'_+(0)=-c<0, so zero cannot minimize D. Thus beta*>0. Both derivatives exist and agree there, and the interior minimum condition gives

E[g(X,beta*)]=c=1-alpha.

Set t*(x)=g(x,beta*). Pointwise maximization and this mean identity imply

E[theta(X,t*(X))]=E[m_{beta*}(X)]-beta* c=D(beta*).

The weak dual bound shows that t* attains the scalar optimum.

### 5. Set reconstruction and both optimization problems

Define

C*(x,a)={y:u(a,y)>=gamma(x,t*(x),a)}.

By Step 1, each action's conditional coverage is at least t*(x), and nu_{C*}(x)=theta(x,t*(x)). Thus C* is universally feasible and attains the universal optimum. It is also policy-coupled feasible because its measurable maximizing policy is one of the deterministic policies covered by the universal constraint.

Finally, take any policy-coupled-feasible system C and its chosen measurable maximizing action pi_C. Define

s_C(x)=P(Y(pi_C(x)) in C(x,pi_C(x))|X=x).

Its feasibility gives E[s_C(X)]>=c. The selected action's worst-case utility equals nu_C(x). Applying the single-action bound from Step 1 at coverage s_C(x), including the case s_C(x)=0, gives

nu_C(x)<=gamma(x,s_C(x),pi_C(x))<=theta(x,s_C(x)).

The scalar optimum therefore bounds E[nu_C(X)] from above. Since C* is policy-coupled feasible and attains that same value, it is also optimal for the policy-coupled problem. Both problems have the same attained maximal value.

## Obligation Closure

All theorem-critical obligations listed in the proof structure are derived above. The argument includes zero coverage, full coverage, empty prediction sets, a possibly non-tight utility upper bound, the zero-multiplier boundary, and the stated order of almost-sure uniqueness and multiplier quantification. No nonstandard external dependency or unresolved proof obligation remains.
