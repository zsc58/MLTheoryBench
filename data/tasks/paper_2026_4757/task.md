# Problem

## Setup

Let d and M be positive integers, let A=[a_1,...,a_M] in R^{d x M} be fixed, and let s_1,...,s_M be independent, zero-mean, unit-variance random variables with finite fourth moments. In the noiseless model x=As, fix u in R^d with sum_j (a_j^T u)^2>0. Define J={j:a_j^T u != 0}, q=|J|, and

y=(u^T x)/sqrt(Var(u^T x))=sum_{j in J} alpha_j s_j,
alpha_j=(a_j^T u)/(sum_l (a_l^T u)^2)^{1/2}.

Then sum_{j in J} alpha_j^2=1. For a zero-mean, unit-variance variable v with finite fourth moment, define K(v)=E[v^4]-3, and put K_max=max_{j in J}|K(s_j)|. Given beta>0, call the projection balanced with factor beta if max_{j in J}|alpha_j|^2 <= beta/q. Let theta>0 be a required minimum population contrast.

For the sampling comparison only, additionally assume E[|s_j|^8]<infinity for every j. Let n be a positive integer and let Y_1,...,Y_n be iid copies of this fixed projection y. Let g_n:R^n -> R be a Borel measurable function and let hat K_n=g_n(Y_1,...,Y_n) be the statistic used to estimate K(y). Assume E[hat K_n^2]<infinity and

std(hat K_n) <= tau/sqrt(n),

where std(Z)=sqrt(E[(Z-E[Z])^2]) and tau>0 is a finite constant depending only on the moments E[y^r], 1<=r<=8, not on n. The displayed standard-deviation bound is a separate hypothesis on the estimator, not a conclusion to be proved from finite eighth moments alone.

## Task

Prove that every projection balanced with factor beta satisfies |K(y)| <= beta K_max/q. The order 1/q is sharp: if alpha_j^2=1/q for all active indices and K(s_j)=K_0 for all j in J, then K(y)=K_0/q.

Consequently, under the sampling assumptions, a balanced projection whose population contrast exceeds tau/sqrt(n) must satisfy q < beta K_max sqrt(n)/tau. Also, requiring |K(y)| >= theta necessarily implies q <= beta K_max/theta. These last two inequalities are necessary screening conditions, not sufficiency claims.
