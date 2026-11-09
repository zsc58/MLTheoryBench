# Reference Proof

## Proof Structure

Convexity decomposes regret into hidden-target linearized regret plus an implementation gap. Euclidean projection geometry gives a scalar positive-part recursion for that gap. Conditional demand positivity supplies clearing windows, while projected OGD controls target regret and movement. The lower-bound environment uses equality lost-sales dynamics on a two-coordinate simplex: actions cannot change between demand shocks, and independent coordinate-loss choices on these intervals yield a weighted random-sign fluctuation.

## 1. Well-definedness and degenerate cases

Since x_1=0 and Y is nonempty and nonnegative, J_1=Y. If y_t is feasible, then x_{t+1}<=(y_t-d_t)^+<=y_t, so y_t belongs to J_{t+1}. Thus every J_t is nonempty, compact, and convex. Euclidean nearest-point projections onto J_t and Y exist and are unique.

If D_2=0, Y is a singleton and every comparator loss equals the learner loss. If G_2=0, every observed g_t is zero, and the subgradient inequality gives ell_t(y_t)-ell_t(u)<=0 for all u in Y. A constant action is feasible throughout, since x_{t+1}<=y_t. These cases require no stepsize division. Below assume D_2,G_2>0.

## 2. Regret decomposition and geometric recursion

Set q_t=||z_t-y_t||_2, a_t=||z_{t+1}-z_t||_2 for t<T, and d_t^min=min_i d_{t,i}. Write Delta_base(u)=sum_{t=1}^T <g_t,z_t-u>, Delta_gap=sum_{t=1}^T q_t, and Delta_mv=sum_{t=1}^{T-1}a_t.

The convex subgradient inequality and Cauchy-Schwarz give

ell_t(y_t)-ell_t(u)<=<g_t,y_t-u>=<g_t,z_t-u>+<g_t,y_t-z_t><=<g_t,z_t-u>+G_2 q_t.

Consequently R_T(u)<=Delta_base(u)+G_2 Delta_gap. This is pathwise and holds for every u simultaneously.

For t<T, put r_t=||z_{t+1}-y_t||_2. Euclidean distance dominates each coordinate difference. If r_t<=d_t^min, then z_{t+1,i}>=y_{t,i}-d_{t,i} for every i. Nonnegativity of z_{t+1} implies z_{t+1}>=(y_t-d_t)^+>=x_{t+1}, so q_{t+1}=0.

If r_t>d_t^min, let alpha=d_t^min/r_t and w_t=(1-alpha)y_t+alpha z_{t+1}. Convexity gives w_t in Y, and ||w_t-y_t||_2=d_t^min. The same coordinate argument gives w_t>=x_{t+1}, so w_t is in J_{t+1}. Projection optimality yields

q_{t+1}<=||z_{t+1}-w_t||_2=r_t-d_t^min.

Since r_t<=q_t+a_t, both cases give

q_{t+1}<=[q_t+a_t-d_t^min]^+.

Initialization gives q_1=0 because z_1 is feasible.

## 3. Deterministic and probabilistic clearing

Whenever q_tau=0, induction using q_{r+1}<=q_r+a_r gives q_t<=sum_{r=tau}^{t-1}a_r for t>=tau. If B>=T, summing this bound from tau=1 gives Delta_gap<=T Delta_mv<=B Delta_mv, without any clearing assumption.

Now suppose B<T, every length-B demand window contained in the horizon has an s with d_s^min>=rho, and sum_{r=t}^{t+B-1}a_r<=rho for 1<=t<=T-B. If q_tau=0 and tau<=T-B, choose such an s in [tau,tau+B-1]. Then

q_{s+1}<=[sum_{r=tau}^s a_r-d_s^min]^+<=0.

Starting at tau_1=1, choose the next zero time within B rounds whenever tau_j<=T-B. Once tau_j>T-B, end the partition at T+1. Every resulting interval [tau_j,tau_{j+1}-1] has length at most B and starts with zero queue. On each interval,

sum_{t=tau_j}^{tau_{j+1}-1}q_t<=sum_{r=tau_j}^{tau_{j+1}-2}(tau_{j+1}-1-r)a_r<=B sum_{r=tau_j}^{tau_{j+1}-2}a_r.

These movement-index sets are disjoint subsets of {1,...,T-1}; hence Delta_gap<=B Delta_mv.

For the probabilistic step let A_s={d_s^min<rho}. The filtration contract makes A_s measurable with respect to F_s, and UPPD gives P(A_s|F_{s-1})<=1-mu. For a fixed window starting at t, repeated conditional expectation gives

P(intersection_{s=t}^{t+B-1} A_s)<= (1-mu)^B<=exp(-mu B).

Indeed, when removing its last event, the product of all preceding event indicators is F_{t+B-2}-measurable. Repeating this argument proves the bound without demand independence. The union bound over at most T contained windows gives failure probability at most T exp(-mu B). Thus B=B_delta gives probability at least 1-delta when B_delta<T. When B_delta>=T, use the deterministic bound instead. The resulting event is independent of the comparator choice.

## 4. OGD estimates and achievability

The standard independent projection fact used here is: for a nonempty closed convex Euclidean set C, ||Proj_C(v)-Proj_C(w)||_2<=||v-w||_2. Its hypotheses hold for Y. Since z_t belongs to Y,

a_t<=eta_t||g_t||_2<=gamma D_2/sqrt(t).

The decreasing sequence t^{-1/2} satisfies sum_{r=1}^b r^{-1/2}<=2sqrt(b), for example by integrating r^{-1/2}. Therefore every applicable length-B_delta movement window has total movement at most 2gamma D_2 sqrt(B_delta)<=rho. Also Delta_mv<=2gamma D_2 sqrt(T).

For each u in Y, nonexpansiveness and expansion of the square give

<g_t,z_t-u><=(||z_t-u||_2^2-||z_{t+1}-u||_2^2)/(2eta_t)+eta_t||g_t||_2^2/2.

Write A_t=||z_t-u||_2^2<=D_2^2. Because eta_t is positive and nonincreasing,

sum_{t=1}^T (A_t-A_{t+1})/(2eta_t)
= A_1/(2eta_1)-A_{T+1}/(2eta_T)+sum_{t=2}^T A_t(1/eta_t-1/eta_{t-1})/2
<=D_2^2/(2eta_T).

It follows that

Delta_base(u)<=D_2^2/(2eta_T)+(G_2^2/2)sum_{t=1}^T eta_t
<=D_2G_2(1/(2gamma)+gamma)sqrt(T).

Combining this with the clearing result proves, on one event of probability at least 1-delta and simultaneously for every u,

R_T(u)<=D_2G_2(1/(2gamma)+gamma+2gamma B_delta)sqrt(T).

At gamma=rho/(2D_2sqrt(B_delta)), the parenthesized factor is

D_2sqrt(B_delta)/rho+rho(1+2B_delta)/(2D_2sqrt(B_delta))
<=(D_2/rho+3rho/(2D_2))sqrt(B_delta),

because B_delta>=1. This proves the stated boundary-choice bound.

For every realization and comparator, the observed subgradient inequality alone gives ell_t(y_t)-ell_t(u)<=G_2D_2. No global Lipschitz hypothesis is required. For T>=2 choose delta=1/T and the boundary gamma. On the success event use the preceding bound; on its complement use R_T(u)<=D_2G_2T. Taking expectations gives the stated bound plus D_2G_2. For T=1, the same one-round subgradient inequality gives E R_1(u)<=D_2G_2. Since the positive part of R_T(u) is bounded, these expectations are well-defined, possibly equal to minus infinity if the negative part is not integrable.

## 5. A single hard environment for all randomized learners

Let Y={(y_1,y_2)>=0:y_1+y_2=1}, x_1=0, and generate iid xi_1,...,xi_T with Bernoulli(mu) law, independently of learner randomization. Set d_t=xi_t(1,1) and x_{t+1}=(y_t-d_t)^+. The demands are independent of the preceding filtration, so P(d_t^min>=1|F_{t-1})=mu.

A shock xi_t=1 clears the state. If xi_t=0 and t<T, then x_{t+1}=y_t, and feasibility plus the coordinate-sum constraint forces y_{t+1}=y_t. Partition {1,...,T} after every shock with t<T. Thus the number of nonempty blocks is

K=1+N, where N=sum_{t=1}^{T-1}xi_t.

Their positive lengths L_1,...,L_K sum to T. In particular, xi_T does not create an additional block inside the horizon.

At each block start, after the action has been committed, draw a fresh independent uniform sign sigma_j in {-1,+1}, independently of all demands and learner randomness. Throughout block j use

ell_t(y)=((1-sigma_j)/2)y_1+((1+sigma_j)/2)y_2.

This specifies one randomized environment law, not a different law chosen for each learner. It can be implemented sequentially: a new sign is needed precisely on round 1 or the round after a shock. Sampling the current demand before choosing the current loss respects the model. Neither future demands nor unused signs are revealed to the learner. These losses are linear functions of the order level, independent of the inventory state as a loss argument, and their gradients are e_1 or e_2, of Euclidean norm one.

Condition on the whole demand path for analysis only. It determines the blocks and lengths. For each j, the constant action a_j on that block can depend on previous feedback and learner randomness, but not on its fresh sign sigma_j. Conditional additionally on previous signs and learner randomness, its expected block loss is L_j(a_{j,1}+a_{j,2})/2=L_j/2. Summing and removing the conditioning shows that every randomized learner has expected total loss T/2.

Set S=sum_j L_j sigma_j. For a static u=(u_1,1-u_1), cumulative loss is (T+S)/2-u_1 S. Its minimum over u_1 in [0,1] is T/2-|S|/2. Therefore expected hindsight-best static regret equals E|S|/2, with minimization inside the expectation as required.

## 6. Fluctuation lower bound

Conditional on the block lengths, the signs are independent and symmetric. Expanding their moments gives

E[S^2|L]=V:=sum_j L_j^2,

E[S^4|L]=sum_j L_j^4+6sum_{i<j}L_i^2L_j^2=3V^2-2sum_j L_j^4<=3V^2.

Here 0<V<=T^2, so all moments are finite. The standard independent Paley-Zygmund inequality states that for nonnegative X with finite second moment and positive mean, P(X>=theta E X)>=(1-theta)^2(E X)^2/E[X^2], for 0<theta<1. Applied conditionally to X=S^2 and theta=1/2, it gives P(S^2>=V/2|L)>=1/12 and thus

E[|S||L]>=sqrt(V/2)/12.

For nonnegative N, Markov's inequality gives P(N>2mu T)<=E N/(2mu T)<=1/2 because E N=(T-1)mu<=mu T. Consequently P(N<=2mu T)>=1/2. Since mu T>=1, on this event K<=2mu T+1<=3mu T. Cauchy-Schwarz gives T^2=(sum_j L_j)^2<=K V, hence V>=T/(3mu) there. It follows that

E|S|>=(1/(12sqrt(2))) E sqrt(V)>=(1/(24sqrt(6)))sqrt(T/mu).

The expected regret is therefore at least sqrt(T/mu)/(48sqrt(6)). This proves the converse with a universal constant, including mu=1 and T=1 when permitted by T>=mu^{-1}.

The upper and lower bounds establish the claimed matching dependence in the regime T>=mu^{-1}, up to logarithmic factors and the displayed problem-dependent constants. All theorem-critical proof obligations are closed.
