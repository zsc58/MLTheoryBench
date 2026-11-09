# Reference Proof

## Proof Obligations

The proof must establish: (1) one linear-size instance family independent of the requested score tolerance; (2) the relevant block LP values and integer optimum; (3) feasible children and finite scores for every candidate throughout both complete trees; (4) score saturation after scaling; (5) the linear baseline tree under the prescribed branching and node-selection rules; (6) a uniformly close scoring rule that redirects branching; and (7) non-pruning and full binary-tree growth through depth n. Each obligation is derived below.

## 1. Instance Family and Block Calculations

Fix the score floor \(\rho>0\). For each integer \(n\ge3\), put \(M=7n+8\). First consider the unscaled 0-1 MILP with variables
\[
u_i,v_i,w_{i1},w_{i2},w_{i3}\in\{0,1\},\qquad i=1,\ldots,n,
\]
objective
\[
\sum_{i=1}^n(24u_i+Mv_i+4w_{i1}+8w_{i2}+8w_{i3}),
\]
and, independently in each block \(i\), constraints
\[
2u_i+v_i\le2,
\]
\[
u_i+w_{i1}+w_{i2}\le2,
\quad u_i+w_{i1}+w_{i3}\le2,
\quad u_i+w_{i2}+w_{i3}\le2.
\]
Use the variable ordering
\[
(u_1,\ldots,u_n,v_1,\ldots,v_n,w_{11},\ldots,w_{n1},w_{12},\ldots,w_{n2},w_{13},\ldots,w_{n3}).
\]
The LP relaxation replaces binary restrictions by bounds in \([0,1]\).

For \(t\in[0,2]\), consider
\[
w_1+w_2\le t,\quad w_1+w_3\le t,\quad w_2+w_3\le t,\quad 0\le w_k\le1.
\]
The identity
\[
4w_1+8w_2+8w_3
=2(w_1+w_2)+2(w_1+w_3)+6(w_2+w_3)
\]
gives an upper bound of \(10t\). The feasible point \((t/2,t/2,t/2)\) attains it. Equality forces all three pairwise constraints to be tight, whose unique solution is that point. This includes both endpoints \(t=0,2\).

In a free block, maximizing over \(v\) for fixed \(u\) gives
\[
v=\min\{1,2-2u\}.
\]
Taking \(t=2-u\), the block objective becomes
\[
14u+M\min\{1,2-2u\}+20.
\]
Its slope is \(14\) below \(u=1/2\) and \(14-2M<0\) above it. Thus the unique free-block optimum is
\[
u=\tfrac12,\qquad v=1,\qquad w_1=w_2=w_3=\tfrac34,
\]
with value \(M+27\).

Fixing \(u=0\) gives the unique integral optimum \(v=w_1=w_2=w_3=1\), of value \(M+20\). Fixing \(u=1\) forces \(v=0\); the three-variable calculation at \(t=1\) gives value \(24+10=34\).

If \(w_1=0\), the maximum total \(w\)-contribution for fixed \(u\) is \(8(2-u)\), attained whenever \(w_2+w_3=2-u\). The resulting objective is
\[
16u+M\min\{1,2-2u\}+16.
\]
If \(w_1=1\), the other two variables satisfy \(w_2,w_3\le1-u\). The maximum total \(w\)-contribution, including the fixed variable's contribution, is \(4+16(1-u)\), giving objective
\[
8u+M\min\{1,2-2u\}+20.
\]
Both expressions increase strictly up to \(u=1/2\) and decrease strictly thereafter. Both therefore have value \(M+24\), with \(u=1/2,v=1\) in every optimum. For \(w_1=0\), the remaining \(w\)-optimizer need not be unique: its coordinates satisfy \(w_2+w_3=3/2\). For \(w_1=1\), they are uniquely \(w_2=w_3=1/2\).

If \(w_2=0\), the maximum remaining contribution is
\[
4w_1+8w_3=12-4u,
\]
attained at \(w_3=1,w_1=1-u\). Indeed, \(4(w_1+w_3)+4w_3\le4(2-u)+4\). The resulting objective is \(20u+M\min\{1,2-2u\}+12\), maximized at \(u=1/2\) with value \(M+22\). If \(w_2=1\), setting \(w_1=w_3=1-u\) gives the maximum total \(w\)-contribution \(20-12u\). The resulting objective is \(12u+M\min\{1,2-2u\}+20\), maximized at \(u=1/2\) with value \(M+26\). The same values hold for \(w_3\) by symmetry. All the asserted slope signs follow from \(M\ge29\).

For an integer block, \(u=0\) permits value \(M+20\). If \(u=1\), then \(v=0\) and at most one \(w\)-variable can equal one, so the value is at most \(32<M+20\). Consequently the unscaled integer optimum is
\[
\operatorname{OPT}=n(M+20).
\]

## 2. Reachable Nodes and Feasibility of Every Candidate Branch

We establish a property valid for any policy restricted to fractional-variable branching, not just for the two policies used later. This is necessary because score agreement is required throughout the complete generated trees.

Consider a feasible node obtained by fixing some \(u\)- and \(w\)-variables, with no \(v\)-variable explicitly fixed by branching. In each block, if \(u\) is fixed to one, every optimum has \(v=0\). If \(u\) is fixed to zero, every optimum has \(v=1\).

If \(u\) is unfixed, an optimum again has \(v=\min\{1,2-2u\}\). Suppose an optimum had \(u>1/2\). Replace \(u\) by \(1/2\) and \(v\) by one, leaving the \(w\)-variables unchanged. This respects all fixings, satisfies \(2u+v\le2\), and only relaxes the other constraints. Its objective increase is
\[
(2M-24)(u-1/2)>0,
\]
a contradiction. Hence \(u\le1/2\) and \(v=1\) at every optimum in this case also.

Thus every \(v\)-variable is integral in every optimal solution at such a node. Starting at the root, induction shows that no permitted policy ever branches on a \(v\)-variable. This conclusion is independent of the rule used to select an optimal LP solution.

Now take any candidate at any feasible node having no \(v\)-fixings. Its zero child is feasible: lower that candidate's coordinate to zero in a feasible solution. All packing coefficients are nonnegative, and a fractional candidate was not already fixed.

For its one child, preserve every existing fixing and modify only its block as follows.

- If the candidate is \(u\), at most one \(w\)-variable can be fixed to one: two such fixings would force \(u=0\), contradicting candidacy. Set \(u=1,v=0\), and set all unfixed \(w\)-variables to zero. This is feasible.
- If the candidate is a \(w\)-variable and \(u\) is fixed to one, no other \(w\)-variable can be fixed to one, since that would force the candidate to zero. Set the candidate to one, all other unfixed \(w\)-variables to zero, and \(v=0\).
- If the candidate is a \(w\)-variable and \(u\) is not fixed to one, set \(u=0,v=1\), set the candidate to one, and set the other unfixed \(w\)-variables to zero. Existing \(u\)-fixings, if any, are to zero. Every pair of \(w\)-coordinates has sum at most two, so all constraints hold.

There is no candidate \(v\)-case. These assignments prove that both children of every reachable candidate are feasible. They also show inductively that all nodes generated by either policy are feasible. All their LP optima are attained and finite because the relaxations are closed subsets of \([0,1]^{5n}\).

## 3. Scaling and the Baseline Tree

Set
\[
\alpha=\frac{\rho}{2(M+27)}
\]
and multiply every objective coefficient by \(\alpha\). Call the resulting instance \(Q_n\). The feasible region and LP optimizers are unchanged, and all LP values and integer objective values scale by \(\alpha>0\). In particular,
\[
\operatorname{OPT}(Q_n)=\alpha n(M+20).
\]
The instance depends on \(n\) and the fixed \(\rho\), but not on \(\varepsilon\). This defines the required family before a tolerance is chosen.

A candidate branch affects only one block. By the feasibility result, its child block has a nonnegative, finite objective value. Its parent block has value at most the unrestricted value \(\alpha(M+27)\). Consequently, at every reachable candidate pair,
\[
0\le\Delta_j^b\le\alpha(M+27)=\rho/2,\qquad b\in\{0,1\}.
\]
Therefore
\[
S_{\rm sb}(N,j)=\rho^2
\]
for every candidate throughout either complete tree, not merely through depth \(n\).

The baseline consequently selects the smallest-index fractional variable. Along its all-zero path, each block with \(u_i=0\) has an integral optimum, while each untouched block has fractional \(u_i\). Thus the baseline branches successively on \(u_1,\ldots,u_n\), provided best-bound selection follows this path.

After \(k\) zero branches, the path node has LP bound
\[
B_k=\alpha\bigl(k(M+20)+(n-k)(M+27)\bigr)
=\operatorname{OPT}(Q_n)+7\alpha(n-k).
\]
The sibling created by the \(i\)-th branching, with \(u_i=1\), has bound
\[
C_i=\alpha\bigl((i-1)(M+20)+34+(n-i)(M+27)\bigr).
\]
Direct subtraction gives
\[
\operatorname{OPT}(Q_n)-C_i=\alpha(7i-6)>0.
\]
For \(k<n\), the zero-path node is fractional and its bound exceeds the integer optimum, hence every legitimate incumbent. It also has a strictly larger bound than every previously created sibling. Best-bound selection therefore follows the zero path through its \(n\) branchings. The final zero-path node is integral and attains the optimum; if an optimal incumbent was already available, the conclusion is unchanged. Every remaining sibling prunes by bound. Counting the root and the two generated children from each branching gives
\[
|\mathcal T_{S_{\rm sb}}(Q_n)|=2n+1.
\]

## 4. Perturbation and Exponential Growth

Now fix an arbitrary \(\varepsilon>0\). On every feasible node subproblem of \(Q_n\) with no \(v\)-variable explicitly fixed by branching, define, for each candidate,
\[
\widehat S(N,j)=S_{\rm sb}(N,j)
+\frac{\varepsilon}{2}\mathbf 1\{j=w_{i1}\text{ for some }i\}.
\]
At other node-candidate pairs, define \(\widehat S\) to be zero. The latter extension never affects either run, by the invariant proved above. The first case has finite real scores by the same feasibility and loss estimates. This defines a scoring rule whose error at every candidate of every node in either complete tree satisfies
\[
|\widehat S(N,j)-S_{\rm sb}(N,j)|\le\varepsilon/2\le\varepsilon.
\]

We prove inductively that a node at depth \(d\le n\) in the perturbed tree fixes exactly \(w_{11},\ldots,w_{d1}\), each to zero or one, with all other variables unfixed. For such a node, the first \(d\) blocks have LP value \(\alpha(M+24)\), and the remaining blocks have value \(\alpha(M+27)\). Hence its bound is
\[
L_d=\alpha\bigl(d(M+24)+(n-d)(M+27)\bigr),
\]
and
\[
L_d-\operatorname{OPT}(Q_n)=\alpha(7n-3d)\ge4\alpha n>0.
\]
Thus none of these nodes can be pruned by bound, even with an optimal incumbent. They are feasible by the preceding arguments.

When \(d<n\), an untouched block remains. Its unique free-block optimum has \(w_{i1}=3/4\) and \(u_i=1/2\). Therefore the node is fractional and has a designated candidate. Every available designated candidate has score \(\rho^2+\varepsilon/2\), strictly larger than the score \(\rho^2\) of every other candidate. Previously designated variables are already fixed. The prescribed tie-break therefore selects \(w_{d+1,1}\). Both children are feasible, have the displayed bound for depth \(d+1\), and establish the induction.

Every node at depth below \(n\) must eventually be branched on. Indeed, it cannot be pruned, and the entire search is finite because branching fixes a previously unfixed binary variable. Thus the generated tree contains the complete binary tree through depth \(n\), giving
\[
|\mathcal T_{\widehat S}(Q_n)|\ge\sum_{d=0}^{n}2^d=2^{n+1}-1.
\]

There are exactly \(5n\) binary variables and \(4n\) packing constraints, in addition to the variable bounds. The family is independent of \(\varepsilon\), all compared scores are finite throughout both trees, and both tree-size conclusions hold regardless of the fixed optimal-LP-solution selector and of any legitimate initial incumbent. All listed proof obligations are closed.
