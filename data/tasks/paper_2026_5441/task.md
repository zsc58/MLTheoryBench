# Problem

## Setup

Fix integers d >= 2 and N >= 2, a number c with 0 < c < 1, and deterministic unit vectors x_1,...,x_N,x_o in R^d satisfying

x_i^T x_j = c for distinct i,j in {1,...,N}, and x_i^T x_o = 0 for i in {1,...,N}.

The parameters d,N,c and all these vectors remain fixed in every limit below. Let Ical={1,...,N,o} and X={x_1,...,x_N,x_o}. The inverse temperature beta tends to infinity; in particular beta/log N tends to infinity.

For any finite nonempty multiset Y of vectors in R^d, define

E(xi | Y; beta) = -(1/beta) log sum_{y in Y} exp(beta y^T xi) + (1/2)||xi||^2,

where the sum counts multiplicities. For k in Ical, define

p_k(xi | X; beta) = exp(beta x_k^T xi) / sum_{j in Ical} exp(beta x_j^T xi).

For all sufficiently large beta, let xi_k^*=xi_k^*(beta) denote a deterministic Task-1 fixed-point branch satisfying

xi_k^* = sum_{j in Ical} p_j(xi_k^* | X; beta)x_j,

and

||xi_k^*(beta)-x_k|| -> 0 as beta -> infinity.

These branches depend only on beta and the fixed Task-1 configuration, not on the subsequent rotation. In the comparisons below, cl1 denotes index 1 and cl2 denotes index 2.

Let W be a d-by-d matrix with independent standard-normal entries, set Omega=(W-W^T)/2, and, for epsilon>0, set V=exp(epsilon Omega). Task 2 stores the rotated memories VX. Define

Delta E_k^fp(V) = E(xi_k^* | VX; beta) - E(xi_k^* | X; beta),

Delta E_k^fp = E_W[Delta E_k^fp(V)].

For r in Ical, let X_2^{+r}(V) be the multiset obtained from VX by appending one unrotated copy of x_r. The appended copy is counted separately even when V is the identity I_d. Define

R_{r->k}(V) = E(xi_k^* | VX; beta) - E(xi_k^* | X_2^{+r}(V); beta),

Delta_{r->k} = E_W[R_{r->k}(V)-R_{r->k}(I_d)],

p_{r|k} = exp(beta x_r^T xi_k^*) / sum_{j in Ical} exp(beta x_j^T xi_k^*),

rho_{r|k} = p_{r|k}/(1+p_{r|k}).

Every expectation is over W alone, with the configuration, beta, epsilon, and Task-1 fixed points held fixed.

## Task

Prove the small-rotation factorization

Delta_{r->k} = rho_{r|k} Delta E_k^fp + O(beta rho_{r|k} epsilon^4)

for every r,k in Ical. More precisely, prove that there are B>0 and C<infinity, depending only on the fixed configuration, such that for every beta>=B there is epsilon_0(beta)>0 for which

|Delta_{r->k} - rho_{r|k} Delta E_k^fp| <= C beta rho_{r|k} epsilon^4

for all r,k in Ical and 0<epsilon<epsilon_0(beta).

Prove also the hierarchy

Delta_{o->o} > Delta_{cl1->cl1} >> Delta_{cl1->cl2} >> {Delta_{cl1->o}, Delta_{o->cl1}},

with Delta_{cl1->o} asymptotically equivalent to Delta_{o->cl1}.

The asymptotic conventions are as follows. The five gains are positive, and the displayed ordinary strict inequality holds, for every sufficiently large fixed beta and all sufficiently small positive epsilon, with the epsilon threshold allowed to depend on beta. For positive gains A(beta,epsilon) and B(beta,epsilon), A >> B means

lim_{beta->infinity} lim_{epsilon->0+} A(beta,epsilon)/B(beta,epsilon) = infinity.

Asymptotic equivalence means that the same iterated ratio limit equals one. The comparison with braces requires the divergent ratio separately for each enclosed gain. Thus the small-rotation limit is taken at fixed beta before the large-beta comparison; no assertion is made about taking beta to infinity at a fixed positive epsilon.
