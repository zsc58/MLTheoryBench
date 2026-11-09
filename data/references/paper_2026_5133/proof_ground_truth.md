# Reference Proof

## Proof Structure

We first establish the conditional optimism, bias, and second-moment inequalities for the implicit estimator. We then derive the adaptive exponential-weights bound, including normalization, the changing-rate correction, and the exact summation needed for constant 4. A discretization and graph expansion bound each Q_t. Substitution inside the expectation proves the claim.

The graph argument uses one standard independent result, stated explicitly below. Its application and every other theorem-critical obligation are verified in this proof.

## 1. Timing, Well-Definedness, and Comparator Reduction

Fix the adversary strategy and put `F_{t-1}=sigma(I_1,...,I_{t-1})`. For this fixed strategy, the current loss vector and graph are functions of the past actions. Thus they, together with `p_t`, `eta_t`, `gamma_t`, `o_t`, and `Q_t`, are measurable with respect to `F_{t-1}`. This mathematical conditioning does not give the learner access to the current graph before acting: its distribution is computed from previously revealed feedback alone. Write `E_t[X]=E[X|F_{t-1}]`.

Inductively, all cumulative estimates are finite and nonnegative, every weight is positive, and every probability p_{t,i} is positive. Self-observation gives `o_{t,i}>=p_{t,i}>0`. Therefore

`0<Q_t=sum_i p_{t,i}/(o_{t,i}+gamma_t)<=d`.

The rates are positive and nonincreasing. Also `gamma_t<=sqrt((log d)/d)<1`, so the prescribed rates satisfy the source algorithm's parameter domain. All quantities used below are integrable; for fixed d and T the estimate bounds obtained from positive rates are finite.

For each coordinate,

`E_t[hat_ell_{t,i}]=ell_{t,i} o_{t,i}/(o_{t,i}+gamma_t)<=ell_{t,i}`.

Let

`m_t=sum_i p_{t,i} hat_ell_{t,i}`,

`v_t=sum_i p_{t,i} hat_ell_{t,i}^2`.

Then

`sum_i p_{t,i} ell_{t,i}-E_t[m_t]
 =gamma_t sum_i p_{t,i} ell_{t,i}/(o_{t,i}+gamma_t)
 <=gamma_t Q_t`,

and

`E_t[v_t]
 =sum_i p_{t,i} ell_{t,i}^2 o_{t,i}/(o_{t,i}+gamma_t)^2
 <=sum_i p_{t,i}/(o_{t,i}+gamma_t)
 =Q_t`.

For a fixed arm a, define

`r_a=E[sum_{t=1}^T(ell_{t,I_t}-ell_{t,a})]`.

The sampling rule, tower property, and optimism imply

`r_a <= E[sum_{t=1}^T(m_t-hat_ell_{t,a})+sum_{t=1}^T gamma_t Q_t]`.                 (1)

This is an inequality for each fixed comparator r_a, not an assertion that the maximum R_T is bounded by the comparison with every arm. We will take the maximum only after obtaining a common upper bound.

## 2. Adaptive Exponential-Weights Bound

For analysis, extend the rate definition to

`eta_{T+1}=sqrt(L/(d+sum_{s=1}^T Q_s))`, where `L=log d`.

Use the normalized potential

`Z_t=(1/d) sum_i exp(-eta_t hat_L_{t-1,i})`.

The factor 1/d does not change the algorithm's sampling distribution. It ensures `Z_1=1`. Define the same-rate intermediate potential

`Z'_{t+1}=(1/d) sum_i exp(-eta_t hat_L_{t,i})`.

Since all estimates are nonnegative, `exp(-x)<=1-x+x^2/2` yields

`Z'_{t+1}/Z_t=sum_i p_{t,i} exp(-eta_t hat_ell_{t,i})
 <=1-eta_t m_t+(eta_t^2/2)v_t`.

The right-hand side is positive: each summand `1-x+x^2/2` is positive. Applying `log u<=u-1` for u>0 gives

`m_t <= (log Z_t-log Z'_{t+1})/eta_t+(eta_t/2)v_t`.                 (2)

Put `r=eta_{t+1}/eta_t`, so `0<r<=1`. Concavity of x^r on positive x gives, pathwise,

`Z_{t+1}
 =(1/d) sum_i (exp(-eta_t hat_L_{t,i}))^r
 <=(Z'_{t+1})^r`.

Consequently,

`log Z_{t+1}/eta_{t+1}<=log Z'_{t+1}/eta_t`.

Substituting into (2), summing, and using `Z_1=1` gives

`sum_{t=1}^T m_t
 <=-log Z_{T+1}/eta_{T+1}+(1/2)sum_{t=1}^T eta_t v_t`.

For every fixed a,

`Z_{T+1}>=(1/d) exp(-eta_{T+1} hat_L_{T,a})`,

so

`sum_{t=1}^T(m_t-hat_ell_{t,a})
 <=L/eta_{T+1}+(1/2)sum_{t=1}^T eta_t v_t`.                 (3)

Take expectations in (3). The conditional second-moment bound applies because eta_t is F_{t-1}-measurable. Combining with (1) and `gamma_t=eta_t`, we obtain

`r_a <= E[L/eta_{T+1}+(3/2)sum_{t=1}^T eta_t Q_t]`.                 (4)

Here is the entire summation argument. Let `S_t=sum_{s=1}^t Q_s` and `S_0=0`. Since `Q_t<=d`,

`d+S_{t-1}>=S_t`.

Also,

`Q_t/sqrt(S_t)
 <=2 Q_t/(sqrt(S_t)+sqrt(S_{t-1}))
 =2(sqrt(S_t)-sqrt(S_{t-1}))`.

Thus, pathwise,

`sum_{t=1}^T eta_t Q_t
 =sqrt(L) sum_{t=1}^T Q_t/sqrt(d+S_{t-1})
 <=2 sqrt(L S_T)`.

Substitution into (4), together with `L/eta_{T+1}=sqrt(L(d+S_T))`, proves

`r_a <= E[sqrt(L(d+S_T))+3 sqrt(L S_T)]
 <=4 E[sqrt(L(d+S_T))]`.

The upper bound does not depend on a. Taking the maximum over fixed arms yields

`R_T<=4 E[sqrt(L(d+sum_{t=1}^T Q_t))]`.                 (5)

## 3. Graph Estimate, Including Rounding and Zero-Mass Cases

We prove the source's supporting estimate in its general form. Let G be a loopless directed graph on d vertices, let m>=1, let `p_i in [0,1]` satisfy `sum_i p_i<=m`, and put

`N_i^-={j!=i:(j,i) is an edge of G}`,

`P_i=sum_{j in N_i^-}p_j`.

Let alpha be the independence number of the graph obtained by ignoring directions, and let c>0. We will prove

`sum_i p_i/((p_i+P_i)/m+c)
 <=2m alpha log(1+(m ceil(d^2/c)+d)/alpha)+2m`.                 (6)

The case d=1 is immediate: the left-hand side is at most m, whereas the right-hand side is at least 2m. Hence assume d>=2. If all p_i vanish, the left-hand side is zero and there is nothing to prove.

Set

`M=ceil(d^2/c)`,

`q_i=ceil(Mp_i)/M`,

`J={i:p_i>0}`.

Then `q_i=0` outside J, `q_i>0` on J, and `0<=q_i-p_i<1/M`. Coordinates outside J contribute zero and will be omitted from fractions whose denominators might otherwise vanish.

For `i in J`, let `n_i=|N_i^-|` and `A_i=n_i/M`. Rounding gives

`P_i>=sum_{j in N_i^-}q_j-A_i`,

and

`0<=A_i<=d/M<=c/d`.

Since m>=1 and d>=2, `mc>A_i`. Monotonicity of x/(x+b) for b>=0, followed by the preceding denominator comparison, gives

`p_i/(p_i+P_i+mc)
 <=q_i/(q_i+P_i+mc)
 <=q_i/(q_i+sum_{j in N_i^-}q_j+mc-A_i)`.                 (7)

For a,b>=0 and `a+b>=B>A>0`, the elementary identity

`a/(a+b-A)-a/(a+b)
 =aA/((a+b)(a+b-A))
 <=A/(B-A)`

proves the fraction comparison used by the source. For A=0 the comparison is equality. Apply it to (7) with

`a=q_i`,

`b=sum_{j in N_i^-}q_j+mc`,

`B=mc`,

`A=A_i`.

The hypotheses have just been verified. We get

`p_i/(p_i+P_i+mc)
 <=q_i/(q_i+sum_{j in N_i^-}q_j+mc)+A_i/(mc-A_i)
 <=q_i/(q_i+sum_{j in N_i^-}q_j)+A_i/(mc-A_i)`.

All denominators here are positive because i belongs to J. Moreover,

`sum_{i in J} A_i/(mc-A_i)
 <=d(c/d)/(mc-c/d)
 =1/(m-1/d)
 <=2`.

Multiplying by m and summing proves

`sum_i p_i/((p_i+P_i)/m+c)
 <=m sum_{i in J}q_i/(q_i+sum_{j in N_i^-}q_j)+2m`.                 (8)

We now bound the remaining weighted graph sum. Replace each vertex i in J by a bidirected clique of `k_i=Mq_i` vertices. Replace every original directed edge between retained vertices by all directed edges in the same direction between their cliques. This is a finite loopless directed graph G' with

`N=sum_{i in J}k_i<=M sum_i p_i+d<=mM+d`.

Every independent set of G' contains at most one vertex from each clique and projects to an independent set of G. Thus its independence number alpha' satisfies `1<=alpha'<=alpha`. Equality is not required and need not hold when zero-mass vertices are omitted.

Each clone in the clique of i has indegree

`D^-=k_i-1+sum_{j in N_i^-}k_j`.

Therefore

`sum_{i in J}q_i/(q_i+sum_{j in N_i^-}q_j)
 =sum_{v in G'}1/(1+D_v^-)`.                 (9)

The standard independent directed harmonic inequality states: for a finite loopless directed graph with N>=1 vertices, indegrees D_v^-, and independence number beta,

`sum_v 1/(1+D_v^-)<=2 beta log(1+N/beta)`.

This is the supporting result stated at source L000181-L000182. G' satisfies all of its hypotheses. Applying it to (9) gives an upper bound `2 alpha' log(1+N/alpha')`.

For a>0 and N>=0, the function `a log(1+N/a)` is increasing in both a and N. Its derivative in a is `log(1+N/a)-N/(a+N)>=0`; this follows from `log(1+x)>=x/(1+x)` for x>=0. Hence

`2 alpha' log(1+N/alpha')
 <=2 alpha log(1+(mM+d)/alpha)`.

Together with (8), this proves (6), including the zero-mass cases. In using this estimate for feedback graphs, self-loops are removed before defining N_i^-; self-observation is represented by the separate p_i term in the denominator.

## 4. Substitution and Final Expectation

At round t, apply (6) with m=1, c=gamma_t, and the off-diagonal part of G_t. Its independence number is alpha_t, and

`o_{t,i}=p_{t,i}+sum_{j!=i:(j,i) in G_t}p_{t,j}`.

Thus, on every history,

`Q_t<=2 alpha_t log(1+(ceil(d^2/gamma_t)+d)/alpha_t)+2`.                 (10)

The earlier bound Q_s<=d implies

`d+sum_{s<t}Q_s<=td`,

and therefore

`gamma_t>=sqrt(L/(td))`.

Monotonicity of the ceiling and logarithm now gives

`Q_t<=2(H_t alpha_t+1)`.

Substitute this pointwise inequality into (5), preserving the expectation:

`R_T
 <=4 E[sqrt(L(d+sum_t Q_t))]
 <=4 E[sqrt((d+2 sum_t(H_t alpha_t+1)) log d)]`.

This is the claimed bound. If the independence numbers are deterministic, its right-hand side is deterministic and the expectation can be omitted. For general adaptive graphs it cannot be dropped.

## Private Source-Audit Notes

The public comparator definition is restored from L000025. The outer expectation in the conclusion repairs the omission in L000088 by following its expressly stated derivation from L000066 and L000084. The potential proof uses conditional expectations term by term, avoiding the free-index conditional notation in L000222; it uses the elementary logarithm and concavity inequalities only on their valid domains. The graph proof corrects the clique-size notation at L000195 to Mq_i, includes mc in the fraction-comparison parameter b, and uses alpha'<=alpha when zero-mass vertices are removed. None of these corrections requires an additional structural assumption or a new proof mechanism.
