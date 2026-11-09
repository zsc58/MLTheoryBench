# Reference Proof

## Proof Structure

Establish the cell-mean coupling and a scalar finite-support quantization estimate. Couple the original and input-quantized source vectors and propagate their expected errors through the graph. Separately evaluate the input-quantized and compressed graphs on the same quantized source vector. Bound compressed support diameters by a Lipschitz envelope, propagate actual coupled errors, and expand the resulting recurrence over marked path positions. Finish with the Wasserstein triangle inequality.

## Complete Proof

Fix an integer n>=0. Throughout, L_v denotes the Lipschitz bound specified in the task, not necessarily the smallest such bound. An empty path from a vertex to itself has length zero and product one; this convention is used only in the intermediate path expansions.

### 1. Quantizer coupling and integrability

For any integrable law nu, its positive-mass depth-n cells form an ordered interval partition up to nu-null sets. Their conditional means are finite, their masses sum to one, and there are at most 2^n cells. The map Q_{nu,n} is nondecreasing on these cells. Its pushforward law is T(nu,n), directly by the cell weights in the definition.

For any real x,y,

|x-y| = integral_R |1_{x<=t}-1_{y<=t}| dt.

Consequently, every coupling of laws nu and eta has expected cost at least integral_R |F_nu(t)-F_eta(t)| dt. For Z~nu and Q=Q_{nu,n}(Z), the events {Z<=t} and {Q<=t} are nested up to null sets: both are lower sets of the same ordered input. Hence equality holds in this lower bound at every threshold and, by integration,

E|Z-Q_{nu,n}(Z)| = W_1(nu,T(nu,n)).  (1)

This proves optimality without appealing to an unproved specialized quantization result. Singleton cells cause no difficulty and have zero error.

Every original graph variable is integrable, by topological induction using

|f_v(x)| <= |f_v(0)| + L_v sum_{u in in(v)} |x_u|.

The two quantized constructions have finite support at every vertex. Thus all Wasserstein distances, means, and support diameters used below are finite.

### 2. Scalar quantization estimate

We prove a bound on the actual cell-mean coupling cost. Let nu be supported in a finite interval [a,b], let m be its mean, and write

E_k(nu)=E|Z-Q_{nu,k}(Z)|.

We claim, for every k>=0,

E_k(nu) <= 2^{-k} sqrt((m-a)(b-m)) <= (b-a)/2^{k+1}.  (2)

If a=b, or if the mean is an endpoint, the law is constant and the claim is immediate. Otherwise put A=m-a>0, B=b-m>0, and D=A+B.

For k=0, the chord bound for the convex function z -> |z-m| gives

E_0(nu) <= 2AB/D <= sqrt(AB).

Suppose the first inequality in (2) is known at depth k-1 for every bounded law. For a nonconstant law, the split at m has positive masses p=P(Z<m) and q=P(Z>=m), with p+q=1. Write the child means as m-d and m+e. The mean identity gives

t=pd=qe.

The children are supported in [a,m] and [m,b], respectively. Applying the induction hypothesis to their normalized laws bounds E_k(nu) by 2^{-(k-1)} times

p sqrt((A-d)d) + q sqrt(e(B-e))
= sqrt(t)(sqrt(pA-t)+sqrt(qB-t)).

Set U=pA-t and V=qB-t, both nonnegative. Weighted Cauchy-Schwarz gives

(sqrt(U)+sqrt(V))^2 <= (A+B)(U/A+V/B)
= D(1-tD/(AB)).

Therefore the square of the weighted child-potential sum is at most

tD(1-tD/(AB)) <= AB/4,

where the final inequality is the elementary maximum of a quadratic, or z(1-z)<=1/4 with z=tD/(AB). This proves the induction. Finally sqrt(AB)<=D/2 proves the second inequality in (2).

In particular, for a finite law of support diameter D,

E|Z-Q_{nu,n}(Z)| = W_1(nu,T(nu,n)) <= D/2^{n+1}.  (3)

The argument covers every nonnegative depth and does not require an external discrete-quantization theorem. It does not assert that a mean split halves the mass-weighted child support diameters; that assertion is false.

### 3. Source quantization and homogeneous propagation

Choose independent X_s~mu_s and set U_s=Q_{mu_s,n}(X_s). Evaluate the original graph as X_v=f_v((X_u)_u) and the input-quantized graph as U_v=f_v((U_u)_u). This realizes the prescribed source and graph laws. Define

e_v=E|X_v-U_v|.

Equation (1) gives e_s=W_1(mu_s,mu_s^(n)). At every nonsource,

e_v <= L_v sum_{u in in(v)} e_u.

Expand this recurrence in a topological ordering. Each path to v has a unique final edge, so induction gives

e_v <= sum_{s in S} sum_{gamma in P(s,v)} e_s L_gamma.

At the terminal,

W_1(mu_Delta,mu_Delta^(n))
<= sum_{s in S} sum_{gamma in P(s,Delta)} W_1(mu_s,mu_s^(n)) L_gamma.  (4)

Only the source coupling costs need be optimal. We do not replace the expected errors of dependent intermediate variables by their marginal Wasserstein distances.

### 4. Diameter envelope and local compression costs

On the same quantized source vector U_s, construct C_s=U_s and the compressed graph C_v exactly as in the task. Let Z_v=f_v((C_u)_{u in in(v)}) be the precompression variable at a nonsource.

Define

R_s=diam(supp(mu_s^(n))),
R_v=L_v sum_{u in in(v)} R_u.

Topological induction shows that both the precompression law of Z_v and the postcompression law of C_v have support diameter at most R_v. Indeed, the difference between two supported parent tuples is bounded coordinatewise by the parent support diameters, regardless of dependence. Lipschitz continuity bounds the resulting output diameter. If compression occurs, every cell mean lies in the convex hull of the precompression support, so compression cannot enlarge that diameter. Without compression there is no change.

Let

b_v=E|Z_v-C_v|.

When compression is triggered, (3) gives b_v<=R_v/2^{n+1}; otherwise b_v=0. Thus in all cases

0<=b_v<=R_v/2^{n+1}.  (5)

### 5. Coupled compression errors and marked paths

Define A_v=E|U_v-C_v| under this single joint graph construction. Then A_s=0, and the pointwise triangle inequality and Lipschitz bound give

A_v <= L_v sum_{u in in(v)} A_u + b_v.  (6)

Topological substitution, grouping paths by their final edge, yields

A_Delta <= sum_{v notin S} b_v sum_{pi in P(v,Delta)} L_pi.  (7)

The empty suffix at v=Delta includes terminal compression. This is a recurrence for actual coupling costs; separately optimal parent-marginal couplings are not assumed compatible.

The diameter recurrence similarly expands as

R_v=sum_{s in S} sum_{eta in P(s,v)} R_s L_eta.  (8)

Substituting (5) and (8) into (7) gives a sum over a source s, a nonsource vertex v, a prefix eta from s to v, and a suffix pi from v to Delta. In a DAG the prefix and suffix cannot share another vertex: that would create a directed cycle. Their concatenation is therefore a full directed path gamma from s to Delta, marked at v. Conversely, each such full path has exactly |gamma| nonsource vertices, including Delta, at which it can be marked. Products multiply as L_eta L_pi=L_gamma. Hence

W_1(mu_Delta^(n),mu_Delta^(n),c)
<= A_Delta
<= 2^{-(n+1)} sum_{s in S} sum_{gamma in P(s,Delta)} R_s |gamma| L_gamma.  (9)

This derivation uses actual path positions, not backward-neighborhood boundaries, which can overlap along a path.

### 6. Terminal bound and boundary cases

Apply the Wasserstein triangle inequality to (4) and (9). Since 2^{-(n+1)}<=3*2^{-n},

W_1(mu_Delta,mu_Delta^(n),c)
<= sum_{s in S} sum_{gamma in P(s,Delta)}
[W_1(mu_s,mu_s^(n)) + 3|gamma|2^{-n}diam(supp(mu_s^(n)))] L_gamma.

This is the required inequality. No division by a Lipschitz constant or source diameter was used, so zero constants and singleton supports are included. At n=0 all quantized sources are deterministic, hence all their graph evaluations are deterministic and no compression is triggered; the same proof applies.

## Source-Repair Accounting

The scalar estimate above replaces a false argument introduced in the previous reference proof, not a false source estimate. The source's strict-child endpoint typo is corrected according to its defining partition. The source's invalid marginal-Wasserstein inference is replaced by its already established coupled-error recurrence. The earlier diameter-envelope repair is retained. The previous height-only repairs of the backward-boundary argument are insufficient; topological recurrence expansion corrects both the homogeneous and inhomogeneous bookkeeping and supplies the intended path-length accounting. All these repairs preserve the frozen flagship target.
