# Reference Proof

## Proof Structure

1. Establish joint definability of every node state and the scalar readout by induction over the finite DAG.
2. Derive a sufficient polynomial trace bound from qualitative cylindrical cell decomposition, and conclude finite VC dimension.
3. Verify measurability and apply the standard finite-VC deviation theorem, with a positive complexity floor.

## Standard Results Used

The o-minimal cell-decomposition theorem says that any finite collection of definable sets has a compatible finite cylindrical cell decomposition. For a definable relation in variables (a,t,u), with u the final real coordinate, it provides finitely many definable base cells in (a,t) and finitely many continuous definable boundary functions over these cells. Membership in the relation is constant on every boundary section and intervening sector. Definable sets are Borel, and the usual definable closure operations preserve definability.

The finite-VC deviation theorem used here has the following form. If V is a nonempty class of measurable binary functions on a standard Borel space, its VC dimension is d<infinity, and its empirical supremum is universally measurable, then, in the completion of the iid sample law, with probability at least 1-delta,

sup_{v in V}|Qv-Q_Nv| <= a sqrt((d+1+log(1/delta))/N),

where a>0 is universal, N is a positive integer, and delta is in (0,1).

For the measurability verification, we use the standard facts that bounded jointly Borel functions have Borel parameter-dependent integrals against a fixed probability measure, and that projections of Borel subsets of products of standard Borel spaces are analytic and universally measurable.

## Complete Proof

### Joint Definability

Order the finite DAG topologically. Input states are obtained by fixed linear maps and are therefore semialgebraic and S-definable. Suppose the parent states of a computation node are jointly definable in (x,theta). Concatenating these states with the projected local parameter coordinates is definable. Composing this map with the fixed jointly definable gate gives a jointly definable child state. All evaluations lie in the gates' domains because the network is assumed to be defined everywhere.

The induction reaches every output state. If z(x,theta) is their concatenation and A(theta) is the readout row extracted from the complete parameter vector, then

f(x,theta)=sum_j A_j(theta) z_j(x,theta).

Each parameter projection is definable, multiplication is semialgebraic, and finite sums preserve definability. Thus the readout is jointly definable even though its coefficients vary with theta. Consequently f and the relation R={(x,theta):f(x,theta)>0} are jointly definable.

### A Polynomial Arrangement Bound

We prove the following auxiliary assertion using qualitative cell decomposition. For any fixed finite list of definable families of subsets of R^p, an arbitrary collection of M instances from that list admits a definable partition of R^p compatible with all instances, having at most B(M+1)^{e_p} pieces. Here B depends on the fixed families, not on the selected instances or M, and one may take e_0=0 and e_p=2e_{p-1}+1=2^p-1. The partition pieces need not themselves be connected cells.

For p=0, parameter space is a singleton, and the assertion holds with one piece.

For the induction step, write a parameter as (t,u) in R^{p-1} x R. Apply cylindrical cell decomposition to each fixed family relation, placing its instance-index coordinates first, then t, then u. This gives a fixed finite list of base domains and partial definable vertical boundary functions. For each selected instance, slicing the decomposition yields at most b boundary functions in t, for a constant b depending only on the original families. Its membership is determined by its active base domain and the position of u relative to those boundaries.

Form lower-dimensional instances describing all active base domains and all comparisons between pairs of selected boundary functions. A comparison is restricted to the intersection of the two functions' domains. There are at most b'(M+1)^2 such instances. They belong to a fixed finite list of definable families: their index variables consist of one or two original instance indices and a choice from the finite list of boundary types. In particular, this list is independent of M and of the numerical indices selected.

By the induction hypothesis, partition R^{p-1} compatibly with these domain and comparison instances. There are at most

B'(b'(M+1)^2+1)^{e_{p-1}}

base pieces. On each base piece, the active boundaries and their weak ordering are fixed. Choose representatives for equal boundaries and lift the piece into their sections and intervening vertical sectors. At most 2bM+1 lifted pieces are needed over each base piece. Each original instance has constant membership on each lifted piece, by the sliced cell decomposition and the fixed boundary ordering. Absorbing fixed constants proves the bound with exponent 2e_{p-1}+1. The construction also covers M=0 and pieces with no active boundary.

Now let S_0={x_1,...,x_N} be any N-point subset of R^n, and set

T_i={theta in R^P:f(x_i,theta)>0}.

These are instances of one fixed definable family of subsets of R^P. A compatible partition from the auxiliary assertion has at most B(N+1)^{e_P} pieces. The membership vector in T_1,...,T_N is constant on each piece, and these vectors are precisely the labelings induced by H on S_0. Therefore

|H restricted to S_0| <= B(N+1)^{e_P}.

If S_0 is shattered, then 2^N <= B(N+1)^{e_P}. The exponential eventually exceeds this fixed polynomial, so sufficiently large sets cannot be shattered. Thus d=VCdim(H)<infinity. This argument only needs a fixed polynomial exponent; it does not require the sharper exponent P asserted in the source's quantitative trace bound.

### Loss Class and Measurability

Every h_theta is Borel because its positive set is definable. The binary loss

v_theta(x,y)=1{h_theta(x)!=y}

is jointly Borel in (x,y,theta), and its population expectation is well-defined and lies in [0,1].

Let V={v_theta:theta in R^P}. Its VC dimension is at most d. Indeed, a shattered set of labeled pairs cannot contain both (x,0) and (x,1), since their losses are complementary for every theta. Hence its input coordinates are distinct. On such a set, the loss labeling is obtained from the hypothesis labeling by flipping the coordinates whose fixed label is one. Shattering by V therefore implies shattering of those input coordinates by H.

For fixed Q, the map theta -> L_Q(h_theta) is Borel by the parameter-dependent integration theorem. For a sample s=((x_i,y_i))_{i=1}^N, the map

(s,theta) -> |L_Q(h_theta)-N^{-1}sum_i v_theta(x_i,y_i)|

is Borel. For any real r, the event that its supremum over theta exceeds r is the projection of a Borel set in the product of sample space and R^P. It is analytic and universally measurable. Thus the supremum and the success event in the public task are measurable in the completion of Q^N. No countable parameter reduction or restriction of parameter magnitudes is assumed.

### Uniform Convergence and Constants

Apply the stated finite-VC deviation theorem to V. Its functions are measurable, its domain is standard Borel, its supremum has the required measurability, its VC dimension is at most d, and the observations are iid with law Q. Therefore, with probability at least 1-delta,

sup_{theta in R^P}|L_Q(h_theta)-L_N(h_theta)| <= a sqrt((d+1+log(1/delta))/N).

Set K=max{1,d}. Then d+1 <= 2K. Taking, for example, C=2a^2, the public sample-size condition implies that the displayed upper bound is at most epsilon.

K depends only on the fixed definable network family, hence only on the architecture and its fixed gate formulas, with S fixed. C is universal. Both constants are independent of Q, N, epsilon, delta, and the numerical magnitudes of theta. In particular, d=0 is covered by K=1.

## Obligation Closure

Joint definability, including the variable readout, is explicitly derived. The polynomial trace bound is explicitly derived from the stated qualitative cell-decomposition theorem. Finite VC dimension follows by exponential-versus-polynomial comparison. The loss-class dimension and completed-probability measurability are verified. The precise standard finite-VC theorem is stated and all relevant hypotheses are checked. No theorem-critical proof obligation remains unresolved.
