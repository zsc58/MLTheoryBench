# Reference Proof

## Proof Structure

For a fixed time index, recover the target-density ratio from the exact score by a line integral. The segment bound supplies the absolute-continuity justification even when the density is merely differentiable. The bounded Poisson product coin has success probability equal to the density ratio multiplied by exp(-C), including the zero-bound case. Analyze the independent outer trials to obtain almost-sure termination and Barker acceptance. Establish detailed balance, then prove Harris recurrence from every state using the positive accepted-move density and invariance. Positive rejection probability gives aperiodicity. Finally apply the standard convergence theorem for aperiodic positive Harris chains.

## Complete Proof

Fix t and h>0 throughout, suppress t in the density notation, and let pi(dx)=p(x)dx.

### 1. Line-integral identity and well-definedness

Fix x,y, write v=y-x, and put I(u)=<s(x+uv,t),v> and g(u)=log p(x+uv). Positivity and differentiability of p give g'(u)=I(u). The assumed bound |I(u)|<=C(x,y)<infinity and the mean value theorem imply that g is Lipschitz on [0,1]. Therefore g is absolutely continuous. Its derivative is measurable, and the fundamental theorem for absolutely continuous functions gives

log r = log(p(y)/p(x)) = integral_0^1 I(u) du.

Thus no assumption of continuous score derivatives is needed. The integral is a Lebesgue integral. Also |log r|<=C.

The score is Borel measurable: each partial derivative of the continuous function log p is a pointwise limit of continuous difference quotients. The specified Borel-measurable finite bound C therefore makes the randomization parameters measurable functions of the proposal pair. The Gaussian proposal, acceptance ratios, and all subsequent experiments are well defined.

### 2. Product-coin probability

First suppose C=C(x,y)>0. Let N have the Poisson distribution with mean 2C, independently of an iid uniform sequence U_1,U_2,... on [0,1], and define

W = product_{j=1}^N (1/2+I(U_j)/(2C)).

Use the empty product equal to one. Each factor lies in [0,1], so W lies in [0,1] almost surely and is a valid Bernoulli success parameter. Conditional on N=n, independence gives

E[W|N=n] = (1/2+log r/(2C))^n,

where the n=0 value is one, also when the base is zero. Averaging over N yields

E W = exp(2C((1/2+log r/(2C))-1)) = exp(-C)r.

If C=0, the bound forces I(u)=0 for every u. The line identity gives r=1, and the stipulated deterministic product coin succeeds with probability one. Consequently its success probability is exp(-C)r in all cases.

Every generated Poisson count is finite almost surely, so each individual outer trial performs finitely many draws and score evaluations almost surely.

### 3. Independent restarts and eventual acceptance

For the fixed pair (x,y), H=q(x|y)/q(y|x) is finite and strictly positive. Set

b = alpha' = 1/(1+H exp(C)),
a = (1-b) exp(-C)r.

The independence specified in the procedure implies that one trial rejects with probability b, accepts with probability a, and restarts with probability z=1-a-b. These are valid probabilities because the product-coin success probability belongs to [0,1]. Also b>0, so 0<=z<1.

Successive trials use fresh independent randomness. If T denotes their number until a terminal decision, then P(T>n)=z^n tends to zero. Hence T is finite almost surely. Together with finite Poisson counts this proves termination of the complete correction almost surely.

The eventual acceptance probability is

sum_{n=1}^infinity z^(n-1)a = a/(a+b) = H r/(1+H r).

This includes C=0, in which case the first trial always terminates. Thus the correction implements the Barker acceptance probability alpha_B(x,y).

### 4. Detailed balance and invariance

Define R(x,y)=H(x,y)r(x,y). Then

R(x,y)=p(y)q(x|y)/(p(x)q(y|x)),
R(y,x)=1/R(x,y).

The function a_B(R)=R/(1+R) obeys a_B(R)=R a_B(1/R). Therefore

p(x)q(y|x)alpha_B(x,y) = p(y)q(x|y)alpha_B(y,x).

Let

k(x,y)=q(y|x)alpha_B(x,y),
lambda(x)=integral k(x,y)dy,
rho(x)=1-lambda(x).

The transition kernel is

P_h(x,dy)=k(x,y)dy+rho(x)delta_x(dy).

The displayed balance identity makes its accepted-move part symmetric under pi. Its rejection part is supported on the diagonal and is symmetric as well. Hence P_h is reversible with invariant probability pi.

For every x,y, the Gaussian density is positive and the ratios are finite and positive. Thus k(x,y)>0 and 0<alpha_B(x,y)<1. Integrating against the proposal gives 0<lambda(x)<1 and 0<rho(x)<1 for every x. In particular, every set of positive Lebesgue measure has positive one-step transition probability from every state. Since p is positive everywhere, pi and Lebesgue measure have the same null sets.

### 5. Harris recurrence from every state

Irreducibility and an invariant probability alone must not be used as a general all-state Harris-recurrence implication. Here the special form of P_h gives a direct proof.

Fix any Borel set A with pi(A)>0. Define

f(x)=P_x(X_n belongs to A for some n>=0).

Then 0<=f<=1, f=1 on A, and the Markov property gives f=P_h f on A^c. Invariance implies

0 = integral (f-P_h f)dpi = integral_A (1-P_h f)dpi.

The integrand on the right is nonnegative. Since pi(A)>0, there exists x_0 in A with P_h f(x_0)=1. At this state,

0 = 1-P_h f(x_0) = integral k(x_0,y)(1-f(y))dy,

because f(x_0)=1. Strict positivity of k(x_0,y) forces f(y)=1 for Lebesgue-almost every y.

For any x outside A, the harmonic equation and this almost-everywhere equality give

f(x)=rho(x)f(x)+integral k(x,y)f(y)dy
    =rho(x)f(x)+lambda(x).

Since lambda(x)=1-rho(x)>0, this implies f(x)=1. On A it already equals one. Thus A is hit with probability one from every state.

Because f is now identically one, the probability of a visit to A at some strictly positive time is P_h f(x)=1 for every x. Applying the strong Markov property successively at visits shows that A is visited infinitely often almost surely. This proves Harris recurrence from every state with irreducibility measure pi, equivalently Lebesgue measure. Existence of the invariant probability pi makes the chain positive Harris recurrent.

### 6. Aperiodicity and total-variation convergence

The positive holding probability rho(x)>0 excludes a nontrivial cyclic decomposition. Indeed, in a decomposition of period m>1, a state in one cyclic class must move to the next disjoint class with probability one, whereas its positive holding mass remains in its current class. Thus the irreducible chain is aperiodic.

The standard independent convergence result used here is: an aperiodic positive Harris recurrent Markov kernel on a standard Borel state space, with invariant probability pi, satisfies ||P^n(x,.)-pi||_TV -> 0 for every state x. The state space R^d with its Borel sigma-algebra is standard Borel. Sections 4-6 verify invariance, positive Harris recurrence from every state, and aperiodicity. Consequently

||P_h^n(x,.)-pi||_TV -> 0 as n->infinity

for every initial state x. There are no unresolved proof obligations.
