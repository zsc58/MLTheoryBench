# Problem

## Setup

Fix positive integers T and m. Let Y be a nonempty closed bounded convex subset of R^m_+, with Euclidean diameter at most a finite constant D_2>=0. Let G_2>=0 be a finite bound on observed subgradient norms. For a vector v, v^+ denotes its coordinatewise positive part; vector inequalities are coordinatewise.

The initial inventory is x_1=0. At round t, the learner observes x_t in R^m_+ and chooses y_t in Y with y_t>=x_t. After observing this action, the environment chooses a demand d_t in R^m_+ and then a finite-valued convex loss ell_t:Y->R. Each loss is a function of the order level, not of the current inventory state. The learner incurs ell_t(y_t) and receives a subgradient g_t in partial ell_t(y_t), with ||g_t||_2<=G_2, and the next state, which satisfies

0<=x_{t+1}<=(y_t-d_t)^+.

The feedback supplied to the learner is the observed subgradient and inventory state; full demand and full loss-function observations are not assumed. Learner actions may depend on past feedback, the current observed state, and independent internal randomization, but not on future environment choices.

Work on a filtered probability space with filtration (F_t)_{t=0}^T. At the beginning of round t, x_t and the learner's chosen action y_t are F_{t-1}-measurable; for the algorithm below z_t is also F_{t-1}-measurable. The demand d_t, loss ell_t, observed subgradient g_t, and next state x_{t+1} are F_t-measurable. The filtration includes the learner randomness used to select the current action. Expectations and probabilities include environment and learner randomness.

Define

J_t=Y intersect {y in R^m:y>=x_t},

R_T(u)=sum_{t=1}^T(ell_t(y_t)-ell_t(u)), for u in Y.

Assume that fixed parameters mu in (0,1] and rho>0 satisfy, for every t,

P(min_i d_{t,i}>=rho | F_{t-1})>=mu almost surely.

For delta in (0,1), set B_delta=ceil(mu^{-1}log(T/delta)). The parameters needed in the following algorithm are available when it is initialized. Write Proj_C for nearest-point Euclidean projection onto a nonempty closed convex set C.

When D_2,G_2>0, run hidden-target projected OGD: choose z_1 in J_1, play y_t=Proj_{J_t}(z_t), and update

z_{t+1}=Proj_Y(z_t-eta_t g_t),

where eta_t=gamma D_2/(G_2 sqrt(t)) and 0<gamma<=rho/(2D_2sqrt(B_delta)). When D_2=0 or G_2=0, use a constant action in Y instead; the formulas involving division by these parameters apply only in the positive-parameter case.

## Task

Prove the following integrated theorem.

1. **Achievability.** For every delta in (0,1), the algorithm with that choice of delta satisfies, with probability at least 1-delta and simultaneously for every u in Y,

R_T(u)<=D_2G_2(1/(2gamma)+gamma+2gamma B_delta)sqrt(T).

The boundary choice gamma=rho/(2D_2sqrt(B_delta)) gives

R_T(u)<=D_2G_2(D_2/rho+3rho/(2D_2))sqrt(B_delta T),

hence order sqrt(T/mu) up to logarithmic and problem-dependent factors. For T>=2, taking delta=1/T and the boundary choice of gamma gives, for every fixed u in Y,

E[R_T(u)]<=D_2G_2(D_2/rho+3rho/(2D_2))sqrt(B_{1/T} T)+D_2G_2.

For T=1, prove E[R_1(u)]<=D_2G_2. In the degenerate cases, prove R_T(u)=0 when D_2=0 and R_T(u)<=0 when G_2=0.

2. **Converse.** There is a universal c>0 such that for every mu in (0,1] and integer T>=mu^{-1}, a randomized environment exists with

Y={(y_1,y_2)>=0:y_1+y_2=1},

Euclidean gradient bound one, demands d_t=xi_t(1,1) for iid xi_t with Bernoulli(mu) law independent of learner randomization, and state dynamics fixed by x_{t+1}=(y_t-d_t)^+ (equality). Its losses are only the two linear functions ell_t(y)=y_1 and ell_t(y)=y_2. This environment satisfies the conditional demand assumption with rho=1, and every possibly randomized inventory algorithm obeying the stated information and feasibility constraints satisfies

E[sum_{t=1}^T ell_t(y_t)-min_{u in Y}sum_{t=1}^T ell_t(u)]>=c sqrt(T/mu).

The same randomized environment law must work for every such algorithm; the minimum is taken for each realized loss sequence before the expectation.

Together, in the regime T>=mu^{-1}, these bounds give minimax expected static regret of order sqrt(T/mu) up to logarithmic and problem-dependent factors.
