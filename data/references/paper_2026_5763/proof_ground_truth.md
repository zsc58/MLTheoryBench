# Reference Proof

## Proof Structure

The negative result follows in two reductions. First, exact history probability is shown #P-hard by encoding linear extensions of a partial order and separating the possible extension counts through narrow rational intervals. Second, pairwise transactions force a selected linear extension, and conditional probabilities telescope to recover the original history probability.

For the positive result, MNL rankings are represented by an exponential race. History consistency becomes integration of a log-concave exponential density over an order polytope. A lower bound on the history probability permits truncation with small relative loss; the truncated body has polynomial geometry and admits randomized relative integration. Each estimated positive history probability is projected onto a known positive interval, so the algorithm is defined even when integration fails. Applying this estimator to both the original and augmented histories and taking their ratio proves the conditional guarantee.

## Complete Proof

Write m=n+1 for the number of alternatives, including 0. All histories and queries are supplied explicitly. Repeated transactions, or repeated choices from different offers, present no difficulty: their events are intersections of the same pairwise inequalities. In particular, transactions with the same chosen alternative can be merged by taking the union of their offer sets. The empty history imposes no inequalities and has probability one.

### Exponential representation and ranking probabilities

Let T_i be independent exponential random variables with rates w_i. For every real x,

Pr[-log(T_i)-log(w_i) <= x]
= Pr[T_i >= exp(-x)/w_i]
= exp(-exp(-x)).

Thus -log(T_i)-log(w_i) is standard Gumbel. Coordinatewise transformation preserves independence, so the joint vector (-log(T_i)) has the same distribution as the utility vector. Because -log is strictly decreasing, every utility comparison U_a>U_b corresponds to T_a<T_b, simultaneously in this coupling.

For a nonempty set J of remaining alternatives,

Pr[T_i=min_{j in J} T_j]
= integral_0^infinity w_i exp(-t sum_{j in J} w_j) dt
= w_i/(sum_{j in J} w_j).

Conditioned on the first arrival and its time, the residual clocks are again independent exponentials with their original rates: this follows directly from Pr[T_j>s+t | T_j>s]=exp(-w_j t). Iterating gives, for any complete ordering sigma,

Pr[T_sigma(1)<...<T_sigma(m)]
= product_{s=1}^m w_sigma(s)/(sum_{r=s}^m w_sigma(r)).

Every such ordering has positive probability. A valid history has positive probability if and only if its preference graph is acyclic: a cycle contradicts strict inequalities, whereas a topological ordering supplies a positive-probability ranking satisfying all its transactions.

### Exact computation is #P-hard

We use the standard-independent result that counting linear extensions of a finite partial order, equivalently topological orderings of a finite DAG, is #P-complete.

Let P be a partial order on N vertices. Construct N products, one for each vertex. For every vertex x, include a transaction in which x is chosen from an offer containing x and every strict descendant of x. Since 0 is always available, this transaction imposes x above all its descendants and above 0. Thus the possible rankings of the N products consistent with the history are exactly the linear extensions of P, with 0 below every product. The history is acyclic and has positive probability.

Give every product attraction 1 and give 0 attraction W=N^N. If sigma is a linear extension, the exponential-race formula for its ranking probability is a product of N factors whose numerators are 1 and whose denominators lie between W+1 and W+N. Consequently,

1/(W+N)^N <= Pr(sigma followed by 0) <= 1/(W+1)^N.

If c is the number of linear extensions, the constructed history probability p therefore belongs to

I_c = [c/(W+N)^N, c/(W+1)^N].

These intervals are pairwise disjoint for N>=5. It suffices to show

((W+N)/(W+1))^N < 1+1/c

for every 1<=c<=N!. Put x=(N-1)/(N^N+1). Since Nx<1 and each binomial coefficient is at most N^k,

(1+x)^N <= sum_{k>=0}(Nx)^k = 1/(1-Nx).

For N>=5, N!<N^(N-2)-1. One elementary induction establishes the stronger form N!+1<N^(N-2): the base case is 121<125, and

(N+1)!+1 < (N+1)(N!+1) < (N+1)N^(N-2) < (N+1)^(N-1).

It follows that

(N!+1)N(N-1)<N^N+1,

so 1/(1-Nx)<1+1/N!<=1+1/c. This proves interval separation.

All interval endpoints have polynomial bit length, since W=N^N has O(N log N) bits. The count c can be identified by binary search among the ordered intervals using O(log(N!)) exact rational comparisons. Small N can be handled directly.

For completeness, exact answers on these reduction instances also have polynomial bit length. Every complete ranking ending in 0 has exactly the same probability 1/D, where

D=product_{s=1}^N (W+s).

Indeed, with s products and 0 remaining, each prescribed product arrival has probability 1/(W+s). Hence p=c/D, with both c and D of polynomial bit length. This observation verifies the answer-length requirement; the interval argument already supplies count recovery. Exact history probability is therefore #P-hard under polynomial-time Turing reductions.

Now suppose an oracle computes exact conditional probabilities for acyclic positive-probability histories. Begin with the history H_0 above and choose any topological ordering sigma of its products. Add transactions (sigma(i),{sigma(i),sigma(i+1)}) for missing adjacent comparisons, until the product ordering is forced. At most N-1 transactions are needed. Every product already outranks 0, and all added comparisons agree with sigma. Therefore every intermediate history H_i is acyclic and has positive probability. The final history H_r has a unique product ordering, and its probability p_H_r is directly computable from the exponential-race product formula.

If the i-th added transaction is Q_i, then the oracle answer is

p_H_(i-1)(Q_i)=p_H_i/p_H_(i-1).

Hence

p_H_0=p_H_r/product_{i=1}^r p_H_(i-1)(Q_i).

An empty product is one. Each intermediate probability has the form c_i/D, where 1<=c_i<=N!, so every oracle answer c_i/c_(i-1) has polynomial bit length. There are polynomially many queries and the subsequent exact rational arithmetic has polynomial bit complexity. The conditional oracle therefore computes the #P-hard history probability, proving the first clause.

### Relative approximation of history probabilities

Scale all attractions by their minimum, which does not change rankings. Hence 1<=w_i<=R. This rational scaling has polynomial encoding length.

For a valid history H, the exponential representation gives, up to measure-zero boundary ties,

p_H = integral_K f(t) dt,

where

K={t in nonnegative R^m : t_a<=t_b for every arc a to b in G_H}

and

f(t)=product_i w_i exp(-sum_i w_i t_i).

The density is positive and log-concave, since log f is affine. If the graph is cyclic, detect that in polynomial time and return zero. Otherwise choose a complete topological ordering. At a stage with s remaining alternatives, its prescribed next alternative has rate at least 1 while the total remaining rate is at most sR. Thus its ranking probability is at least

L=1/(R^m m!),

and consequently L<=p_H<=1. The rational number L has polynomial bit length.

Fix an accuracy parameter alpha in (0,1). To use rational geometric data, choose an integer cutoff B satisfying

log(4m/(alpha L)) <= B <= log(4m/(alpha L))/log(2)+2.

For rationally encoded accuracy parameters, one explicit choice is the binary bit length of the integer ceiling of 4m/(alpha L). This cutoff is computable by rational arithmetic in polynomial time. It has magnitude O(1+m log R+log(m!)+log(1/alpha)).

For every i, Pr[T_i>B]<=exp(-B), because w_i>=1. A union bound gives

Pr[max_i T_i>B]<=m exp(-B)<=alpha L/4<=alpha p_H/4.

Thus, for K_B=K intersect [0,B]^m and I_B=integral_K_B f,

0<=p_H-I_B<=alpha p_H/4.

The truncated body has a polynomial-time separation oracle: check its rational box inequalities and all arc inequalities, returning a violated linear inequality when necessary. Choose a topological ordering sigma and let the center z have coordinates

z_sigma(s)=sB/(m+1),  s=1,...,m.

Each coordinate is at distance at least B/(m+1) from either box boundary. For every arc a to b, z_b-z_a>=B/(m+1). If ||y-z||_2<=B/(4(m+1)), each coordinate moves by at most that amount and each ordered difference decreases by at most twice that amount. Hence

B_2(z,B/(4(m+1))) subseteq K_B.

For every y in K_B, each coordinate differs from z by at most B, so ||y-z||_2<=B sqrt(m)<=Bm. We may therefore supply rational radii

r_in=B/(4(m+1)),  r_out=Bm,

whose ratio is 4m(m+1). In particular K_B is compact, convex, and full-dimensional, with polynomial aspect ratio.

We invoke the following standard-independent randomized log-concave integration result, in the form supplied by the source. Given a full-dimensional compact convex body in R^d with a polynomial-time separation oracle, a point z and radii 0<r_in<=r_out satisfying B_2(z,r_in) subseteq K subseteq B_2(z,r_out), and a positive log-concave function f whose logarithm is evaluable to the required polynomial precision in polynomial time, suppose sup_K log f-inf_K log f<=Delta. There is a randomized relative integration algorithm with error tolerance beta and failure probability xi, running in time polynomial in d, 1/beta, log(1/xi), r_out/r_in, Delta, and the encoding lengths of the supplied data and oracles. It returns an estimate Z_raw satisfying

(1-beta) integral_K f <= Z_raw <= (1+beta) integral_K f

with probability at least 1-xi. This is the standard convex-body integration result with rounding, not a paper-specific conditional-choice theorem.

Here,

max_K_B log f-min_K_B log f <= B sum_i w_i <= mRB.

At rational oracle points, log f(t)=sum_i log(w_i)-sum_i w_i t_i can be evaluated to arbitrary requested polynomial precision using polynomial-time logarithm evaluation and rational arithmetic. The logarithmic range has polynomial magnitude in n, R, 1/alpha, and the input encoding length. All separation, center, radius, and evaluation data have the required encoding bounds. Thus all hypotheses of the stated integration result hold.

Apply it with beta=alpha/4 and failure probability xi. With probability at least 1-xi,

(1-alpha/4)I_B <= Z_raw <= (1+alpha/4)I_B.

On this event,

Z_raw <= (1+alpha/4)p_H <= (1+alpha)p_H

and

Z_raw >= (1-alpha/4)^2 p_H >= (1-alpha)p_H.

Define the actual history estimate by

Z=min{1,max{L,Z_raw}}.

Because p_H belongs to [L,1], projection onto this interval preserves any relative-error interval containing p_H. More explicitly, if a successful raw estimate is below L, replacing it by L moves it toward p_H; if it exceeds 1, replacing it by 1 also moves it toward p_H. Therefore Z retains the preceding relative guarantee. On every execution, including failures, L<=Z<=1. This ensures a strictly positive, finite estimate for every acyclic history without needing to recognize whether integration succeeded.

The history algorithm consequently has relative error alpha and failure probability at most xi, in time polynomial in n, R, 1/alpha, log(1/xi), and the input encoding length. Empty histories and histories containing only vacuous transactions satisfy the same argument; their true probability is one. The construction also works in dimension m=1.

### Passing to conditional probabilities

For a query Q=(a,S), let H'=H union {Q}. If a is unavailable, return zero. Otherwise H' is a valid history. If its graph is cyclic, return zero. In either case the queried event intersected with E_H is empty.

If neither check applies, H' is acyclic and its probability is positive. Since H is acyclic as well,

p_H(a,S)=p_H'/p_H>0.

Run the history-probability algorithm independently on H and H' with relative error eta=epsilon/4 and failure probability delta/4 for each, and return

qhat=Z_H'/Z_H.

Both estimates lie in [L,1] on every execution. Thus this ratio is always defined and strictly positive. Combined with the deterministic impossibility checks, the algorithm returns zero exactly when the conditional query is impossible, not merely on its success event.

A union bound gives simultaneous relative accuracy with probability at least 1-delta/2, hence at least 1-delta. On this event, writing q=p_H(a,S),

((1-eta)/(1+eta))q <= qhat <= ((1+eta)/(1-eta))q.

For 0<epsilon<1,

1-epsilon/4-(1-epsilon)(1+epsilon/4)=epsilon/2+epsilon^2/4>=0

and

(1+epsilon)(1-epsilon/4)-(1+epsilon/4)=epsilon(2-epsilon)/4>=0.

Dividing by the positive denominators yields

(1-epsilon/4)/(1+epsilon/4) >= 1-epsilon

and

(1+epsilon/4)/(1-epsilon/4) <= 1+epsilon.

Consequently,

Pr[(1-epsilon)q <= qhat <= (1+epsilon)q] >= 1-delta.

All probability statements here concern the algorithm's internal randomization for the fixed input history and query. The two integration calls, graph checks, projections, and final rational division have the claimed polynomial runtime. When R is polynomially bounded in n, this runtime is polynomial in the input length, 1/epsilon, and log(1/delta), so the procedure is an FPRAS.
