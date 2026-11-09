# Reference Proof

## Contract and proof obligations

The network class has a common hidden width and the factor \(L+2\) normalization in the public definition. Both Lipschitz continuity and output approximation use infinity norms. The proof must establish: (i) an exact computational representation; (ii) stability on the inputs actually used here; (iii) input-independent compression to one fixed architecture; (iv) a fixed-architecture parameter lower bound; (v) the explicit parameter comparison; and (vi) the strict approximation contradiction.

The source's unrestricted stability and bias-stationarity assertions for arbitrary computational signals are not used. General computational signals need not be unit-bounded or have unit bias. We prove the required input specializations below. We also derive the weak-regularity ingredient rather than treating its nonstandard citation as a completed proof.

## 1. Computational representation

Put \(M=\operatorname{lcm}(d_0,d_L)\). Repeating every hidden neuron the same number of times, with identical incoming and outgoing parameters on the copies, preserves every normalized average and every bias. Thus a network of common width \(d\) can be represented, without changing its function or parameter bound, at width \(Md\). We may assume its width is divisible by \(M\).

Partition \([0,1]\) into equal intervals \(U^{(0)},\ldots,U^{(L)},U^{(b)}\), each of measure \(1/(L+2)\). Partition each hidden interval into \(d\) equal neuron cells, the input interval into \(d_0\) coarse cells, and the output interval into \(d_L\) coarse cells. Define a kernel \(K\) by putting \(W^{(\ell)}_{ij}/B\) on adjacent-layer neuron blocks, \(b_i^{(\ell)}/B\) on bias-to-layer blocks for every \(1\leq\ell\leq L\), and \((L+2)/B\) on the bias self-block. All other blocks, including all outgoing output blocks, are zero. Since \(B\geq L+2\), \(|K|\leq1\).

For \(x\in[0,1]^{d_0}\), let \(f_x\) take value \(x_j\) on input cell \(j\), value one on bias, and zero elsewhere. In particular \(0\leq f_x\leq1\). Iterate
\[
 f^{(\ell)}=B\operatorname{ReLU}\left(\int K(\cdot,y)f^{(\ell-1)}(y)\,dy\right)
 \quad(1\leq\ell<L),
\]
with the same integral update but no ReLU at \(\ell=L\).

The bias value remains one: its update is \(B((L+2)/B)/(L+2)=1\), with ReLU making no difference. On a layer-\(\ell\) neuron cell, the integral update before activation equals
\[
 \frac{1}{L+2}\left(\frac1{d_{\ell-1}}\sum_j W^{(\ell)}_{ij}h_j^{(\ell-1)}+b_i^{(\ell)}\right).
\]
Induction, applying ReLU only on hidden layers, therefore identifies the network output with the final signal on each output cell.

## 2. Cut-norm stability on the required input domain

For an integrable signal \(h\), define \(\|h\|_\square=\sup_S|\int_S h|\). This is the larger of its positive and negative masses, so \(\|h\|_1\leq2\|h\|_\square\). Multiplication by a measurable function taking values in \([0,1]\) cannot increase this norm. For a kernel \(Q\), define \(\|Q\|_\square=\sup_{S,T}|\int_{S\times T}Q|\). Layer-cake integration shows that
\[
 \left|\int a(x)Q(x,y)b(y)\,dx\,dy\right|\leq\|Q\|_\square
 \quad\text{if }0\leq a,b\leq1.
\]

Consider two kernels bounded by one and initial signals in \([0,1]\). Their layer signals have absolute value at most \(B^\ell\); all signals before the final update are nonnegative. Write \(c_\ell\) for their signal cut-norm difference and \(r\) for their kernel cut-norm difference. For real preactivations \(u,v\), write \(\operatorname{ReLU}(u)-\operatorname{ReLU}(v)=s(u-v)\), where the measurable secant multiplier \(s\) lies in \([0,1]\). At the final linear update use \(s=1\). Splitting the integral difference into propagation of the signal difference and a kernel perturbation gives
\[
 c_\ell\leq2B c_{\ell-1}+B^\ell r.
\]
Indeed, the propagated signal term has \(L^1\) norm at most the previous signal's \(L^1\) difference, and the kernel term is bounded using the nonnegative multiplier \(f^{(\ell-1)}/B^{\ell-1}\). The secant multiplier does not enlarge the signal cut norm. Solving the recurrence yields
\[
 c_\ell\leq B^\ell\bigl(2^\ell c_0+(2^\ell-1)r\bigr)
 \leq(2B)^\ell(c_0+r).
\]

Admissible relabelings preserve each hidden interval and are the identity on the input, output, and bias intervals, modulo null sets. The integral recursion is equivariant under such relabelings. For the same cube input, \(f_x\) is invariant under them. Restriction to the output interval cannot increase the signal cut norm, and the output there is not relabeled. Applying the preceding estimate for every admissible relabeling and then taking an infimum gives
\[
 \|\mathbf1_{U^{(L)}}(f_K^{(L)}-f_J^{(L)})\|_\square
 \leq(2B)^L\delta_\square^{\rm comp}(K,J).
\]
No minimizing relabeling is required.

## 3. Weak regularity, with its derivation

For a finite measurable partition \(\mathcal P\), write \(K_{\mathcal P}\) for the block average of \(K\). It is the orthogonal projection in \(L^2\) onto the corresponding step functions, stays in \([-1,1]\), and has energy \(\|K_{\mathcal P}\|_2^2\leq1\).

Fix \(t>0\). Starting with the trivial partition, whenever \(\|K-K_{\mathcal P}\|_\square>t\), choose a rectangle \(S\times T\) witnessing this strict inequality and refine every part by membership in \(S\) and \(T\). This multiplies the number of parts by at most four. If \(\mathcal Q\) is the refinement, its projection has the same integral as \(K\) over the witnessing rectangle. Cauchy-Schwarz therefore gives \(\|K_{\mathcal Q}-K_{\mathcal P}\|_2>t\). Orthogonality shows that the energy increases by more than \(t^2\). Since energy never exceeds one, the procedure stops within \(\lceil1/t^2\rceil\) refinements. Consequently it produces a step kernel on at most \(4^{\lceil1/t^2\rceil}\) parts with cut error at most \(t\).

This proves the quantitative weak-regularity statement needed here; it is not an unproved appeal to the source's specialized citation.

## 4. Structural equitization and compression

Fix \(0<\rho<1\) and put
\[
 k=2^{2\lceil16/\rho^2\rceil},\qquad
 D=8ML\left\lceil k/\rho\right\rceil.
\]
Apply the preceding construction with \(t=\rho/4\), obtaining \(K_0\) on a partition with at most \(k\) parts. Refine that partition with all hidden intervals, all coarse input/output cells, and the bias interval, and call the refinement \(\mathcal P\). Put \(F=K_{\mathcal P}\).

Block averaging is a contraction for the kernel cut norm: integrals of a block average over a rectangle equal integrals of the original kernel against the two blockwise membership fractions, which lie in \([0,1]\). Since \(K_0\) is measurable for the refined partition,
\[
 \|F-K_0\|_\square\leq\|K-K_0\|_\square,
 \qquad \|K-F\|_\square\leq\rho/2.
\]

The complete feedforward block structure implies that \(F\) retains coarse input-column and output-row constancy, zero input rows and output columns, bias-column constancy, and the fixed bias row. Thus its partition can retain the original coarse input/output cells and the entire bias interval. On each hidden interval it has at most \(k\) parts.

Equitize each hidden interval into \(D\) measurable cells of measure \(1/((L+2)D)\). To do this, cut full cells of that measure from each old part and combine the remaining pieces into equal cells. There are at most \(k\) remainder cells per hidden interval. The union \(R\) of all hidden remainder cells consequently satisfies
\[
 \mu(R)\leq\frac{(L-1)k}{(L+2)D}.
\]
Keep input, output, and bias partitions fixed, and let \(\mathcal E\) be the resulting partition. Crucially, define \(H=F_{\mathcal E}\), not \(K_{\mathcal E}\). Outside \(([0,1]\times R)\cup(R\times[0,1])\), the two cells refine old parts and hence \(H=F\). Since both kernels are bounded by one,
\[
 \|F-H\|_\square\leq\|F-H\|_1
 \leq4\mu(R)
 \leq\frac{4(L-1)k}{(L+2)D}<\rho/2.
\]
All structural zeros, coarse constancies, and the bias self-block survive this averaging.

Map the equal cells of each hidden interval to its standard interval partition, using measure-preserving bijections modulo null sets, and use the identity elsewhere. Such cellwise maps exist because equal-measure measurable subsets of a Lebesgue interval are measure-isomorphic modulo null sets. The map is admissible. Since \(M\mid D\), the unchanged coarse input and output partitions, and the unchanged bias interval, can be further subdivided into the standard fine interval cells without changing kernel values. The resulting kernel \(K'\) is induced by a network with common hidden width exactly \(D\), parameters bounded by \(B\), and
\[
 \delta_\square^{\rm comp}(K,K')<\rho.
\]
Every choice in this construction depends on \(K\), not on the input.

Set
\[
 A=(L+2)d_L(2B)^L.
\]
For \(0<\epsilon<A\), apply the construction with \(\rho=\epsilon/A\). An output cell has measure \(1/((L+2)d_L)\), and the output difference is constant there. The representation and stability estimates therefore give, simultaneously for every input and every output coordinate,
\[
 |N(x)_j-N'(x)_j|
 \leq(L+2)d_L(2B)^L\delta_\square^{\rm comp}(K,K')<\epsilon.
\]
Thus every network has a uniformly \(\epsilon\)-close network of the single exact common hidden width
\[
 D(\epsilon)=8ML\left\lceil
 2^{2\lceil16A^2/\epsilon^2\rceil}\frac{A}{\epsilon}
 \right\rceil.
\]
For completeness, if \(\epsilon\geq A\), the zero network of this width suffices: the representation gives output magnitude at most \(B^L<A\). Hence the compression statement holds for every positive tolerance.

## 5. Fixed-architecture Lipschitz approximation lower bound

The standard independent VC theorem used here states that the Boolean class obtained by thresholding a scalar output of a fixed ReLU architecture with \(W\) scalar weights and biases has VC dimension at most \(cW^2\). Parameters can be unrestricted. A threshold can be absorbed into the unrestricted final bias, so it does not add a parameter. A bounded-parameter subclass satisfies the same upper bound. The normalized layer factors are fixed for a fixed architecture and do not obstruct this application.

Let \(0<\epsilon<1/3\), and consider the grid
\[
 G=\{6\epsilon j:0\leq j\leq\lfloor1/(6\epsilon)\rfloor\}^{d_0}.
\]
It contains \((\lfloor1/(6\epsilon)\rfloor+1)^{d_0}\geq(6\epsilon)^{-d_0}\) points. Distinct grid points have infinity distance at least \(6\epsilon\). For any Boolean labeling \(z_p\), define
\[
 q_z(x)=\max\left(\{0\}\cup
 \{(3\epsilon-\|x-p\|_\infty)_+:p\in G,\ z_p=1\}\right).
\]
Every term is infinity-norm 1-Lipschitz, so their maximum is too. Also \(0\leq q_z\leq3\epsilon<1\), and \(q_z(p)=3\epsilon z_p\). Embed \(q_z\) as the first coordinate of a vector-valued target with other coordinates zero.

If a fixed architecture approximates every such target with error at most \(\epsilon\), thresholding its first output at \(3\epsilon/2\) realizes every labeling of \(G\): zero labels have output at most \(\epsilon\), and one labels have output at least \(2\epsilon\). The unrestricted fixed-architecture threshold class therefore shatters \(G\), and
\[
 cW^2\geq(6\epsilon)^{-d_0},\qquad
 W\geq c^{-1/2}(6\epsilon)^{-d_0/2}.
\]
This argument requires no additional external approximation theorem. It does not assert a VC bound for a union of different architectures.

## 6. Explicit parameter comparison

Put \(\epsilon_0=1/8\), \(\eta=1/16\), and \(D=D(\eta)\). Define
\[
 U=A\,2^{2^{13}A^2+6},\qquad
 Q=8d_0d_LL U,
 \qquad a=\frac1{8L}.
\]
The compression formula and \(\lceil t\rceil\leq t+1\) imply
\[
 D\leq8ML(U+1).
\]
Indeed, the inner exponent is \(2\lceil2^{12}A^2\rceil\), and the factor \(1/\eta\) contributes \(2^4\), giving the stated \(U\) after bounding the inner ceiling. Since \(M\leq d_0d_L\), \(A\geq L+2\), and \(U\geq8L\),
\[
 D\leq Q(1+a).
\]
Let \(C=d_0+d_L+L\). For positive integer dimensions,
\[
 C\leq(L+2)d_0d_L\leq2Ld_0d_L,
\]
and the definition of \(Q\) gives \(Q\geq8LC\), or \(C\leq aQ\).

The exact parameter count of the common-width architecture is
\[
 W=(L-2)D^2+(d_0+d_L+L-1)D+d_L.
\]
This includes the case \(L=2\), with no hidden-to-hidden matrix. Since \(D\geq d_L\), it is bounded by \((L-1)D^2+CD\). Consequently
\[
 W\leq\bigl((L-1)(1+a)^2+a(1+a)\bigr)Q^2<LQ^2.
\]
For the last inequality, the coefficient equals \(L-3/4-7/(64L)\). Expanding \(LQ^2\) gives exactly
\[
 LQ^2=d_0^2d_L^4L^3(L+2)^2(2B)^{2L}
 2^{2^{14}(L+2)^2d_L^2(2B)^{2L}+18}
 =\widetilde W.
\]
The public dimension condition therefore yields
\[
 W<\widetilde W<c^{-1/2}(4/3)^{d_0/2}
 =c^{-1/2}(6\epsilon_0)^{-d_0/2}.
\]
The additional public assumption \(d_0>1800\) is retained from the source's logarithmic comparison; the direct strict comparison is all this step needs.

## 7. Contradiction for one fixed compressed architecture

Apply the lower bound to the single architecture with common hidden width exactly \(D(\eta)\). Its parameter count is below the threshold, so there exists a target \(f\in\operatorname{Lip}(d_0,d_L)\) that cannot be approximated by this architecture with error below \(\epsilon_0\). It is unnecessary, and would not follow from the fixed-architecture VC statement alone, to claim a common hard function for every low-parameter architecture.

If the full public class were universal, choose \(N\) with \(\|f-N\|_\infty<\eta\). Compress it to \(N'\) in that exact fixed architecture with \(\|N-N'\|_\infty<\eta\). Then
\[
 \|f-N'\|_\infty<2\eta=\epsilon_0,
\]
contradicting the choice of \(f\). The class is therefore not universal.

All theorem-critical obligations listed at the start are closed. The counterexamples to the source's unrestricted auxiliary signal statements do not apply to any input or estimate used in this proof.
