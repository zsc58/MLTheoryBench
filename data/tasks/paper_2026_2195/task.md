# Problem

## Setup

Let q>=2 be an integer. Let X have a fixed rooted full q-ary partition: at each integer depth h>=0 there are q^h nonempty disjoint cells P_{h,i} covering X; P_{0,0}=X; and the q children of each cell partition that cell. Each cell has a fixed representative x_{h,i} belonging to it.

Fix v>0, r in (0,1),

0<=d<=log(q)/log(1/r),

and C>1 satisfying

C>=(q/r^{-d})^{floor(log(3)/log(1/r))}.

An admissible objective F:X->R has an attained global maximum at some x*. For every integer h>=0, every point x in the depth-h cell containing x* satisfies F(x)>=F(x*)-v r^h. At most C r^{-dh} depth-h cells have supremum at least F(x*)-3v r^h. The parameter d is any dimension satisfying this bound; it need not be the smallest such dimension.

A query (x,z), with z in [0,1], returns the raw deterministic scalar F_z(x) and costs ell(z). The cost function ell:[0,1]->[0,+infinity] is known. There exist an unknown bias function zeta:[0,1]->[0,+infinity] and unknown strictly increasing functions g_z:R->R such that

||F-g_z composed with F_z||_infinity<=zeta(z)

for every z. The functions g_z are not supplied to the learner.

For every c>=1 the learner can request a selectable fidelity z_c with ell(z_c)<=c. The selection mechanism is fixed as part of the instance. Write Phi(c)=zeta(z_c). Fix one of these three fidelity classes, with its parameters fixed independently of the budget:

- **Polynomial:** A>0 and alpha>0, with Phi(c)<=A c^{-alpha} for every c>=1.
- **Exponential:** B0>0, beta>0, and sigma>0, with Phi(c)<=B0 exp(-c^beta/sigma) for every c>=1.
- **Threshold:** a>=1, with Phi(c)=0 for every c>=a.

A budget-B policy, where B>=1, uses the known partition, representatives, costs and fidelity-selection mechanism, its own randomness, and past raw observations to make a finite, possibly random number of adaptive queries whose total cost is at most B almost surely. It then outputs a point hat x_B in X, not necessarily one it queried. Queries and output must make the regret a measurable random variable. Its expected simple regret is

R_B=E[F(x*)-F(hat x_B)],

where the expectation is only over the policy's internal randomness. No objective or fidelity values are available except through queries.

## Algorithm A

All logarithms are natural. Set

B'=floor((e-1)B/(2qe(log B+1)^2)).

If B'=0, make no queries and return x_{0,0}. Otherwise set J=floor(log B'). Fidelity level j means the fidelity z_{e^j}.

Maintain the raw observation at each evaluated cell representative and level. Opening a cell at level j means evaluating every child's representative at every level u=0,...,j, unless that cell-level observation has already been obtained. These queries are paid. Mark the opened cell as opened; each cell is opened at most once. A cell is eligible at level j when its level-j observation has been obtained and the cell has not yet been opened.

Initialize by opening the root at level J. For h=1,...,B', and then m=1,...,floor(B'/h), set

j=floor(log(B'/(hm))).

Among eligible depth-h cells at level j, open one with largest level-j raw observation. If no such cell exists, skip that operation. Resolve ties by a fixed rule.

For each j=0,...,J, let x_j^c be a representative with largest raw level-j observation among all cells evaluated at that level, including cells that have not been opened. Query each x_j^c once at fidelity z_{B'}, at cost at most B', and return a candidate with largest validation observation, resolving ties by a fixed rule.

## Task

Prove budget feasibility of algorithm A for every B>=1. Prove the following five lower and upper rates.

For each fixed partition, fixed smoothness/count parameters, and fixed fidelity-class parameters, there are strictly positive constants in the table and a finite B_* >1, depending only on those fixed parameters and q, such that for every B>=B_*:

1. For every budget-B policy, there exists an admissible objective, cost function, fidelity-selection mechanism and fidelity family for which its expected regret is at least the corresponding lower bound.
2. For every admissible instance, algorithm A has regret at most the corresponding upper bound, although it does not know v,r,d,C, the bias function, the calibrations, or the fidelity-class parameters.

| Regime | Worst-case lower bound for every policy | Upper bound for algorithm A |
|---|---|---|
| Polynomial | l_1 B^{-1/(d+1/alpha)} | U_1 (B/(log B)^3)^{-1/(d+1/alpha)} |
| Exponential, d=0 | l_2 exp(-k_2 B^{beta/(1+beta)}) | U_2 exp(-K_2 (B/(log B)^2)^{beta/(1+beta)}) |
| Exponential, d>0 | l_3 B^{-1/d} | U_3 (B/(log B)^{3+1/beta})^{-1/d} |
| Threshold, d=0 | l_4 exp(-k_4 B) | U_4 exp(-K_4 B/(log B)^2) |
| Threshold, d>0 | l_5 B^{-1/d} | U_5 (B/(log B)^3)^{-1/d} |

All table constants are independent of B and of the policy; the upper-bound constants are uniform over admissible instances with the fixed class parameters. The lower and upper exponential constants are separate constants and are not asserted to coincide. Thus the upper and lower rates match up to logarithmic factors. The lower bound is worst-case over admissible cost/fidelity instances; the existence of an easier, even free exact-fidelity instance does not remove it.
