# Reference Proof

Let \(N=\lceil T^{1/3}\rceil\), \(K=\lceil4T^{1/3}\log T\rceil\), \(\varepsilon=1/(4N)\), and \(b=\varepsilon/8\). Partition \([-1,1]\) into \(N\) bins \(I_j\) of width \(2/N\), with inner halves \(J_j\). Construct \(\psi_j\) supported on \(I_j\), equal to one on \(J_j\), and zero at the bin endpoints. On each outer quarter-bin use the interpolation \(q(u)=3u^2-2u^3\), \(0\leq u\leq1\), rising on the left and falling on the right. The resulting bumps are \(C^1\), have disjoint interiors, take values in \([0,1]\), and satisfy \(\|\psi_j'\|_\infty\leq3N\).

Put \(h(x)=(1+x)/2\) and, for \(\beta\in\{-1,+1\}^N\), define
\[
 f_\beta(x)=(1-b)\left(\tfrac12+\varepsilon\sum_{j=1}^N\beta_j\psi_j(x)\right)+b h(x).
\]
These links are \(C^1\), take values in \([0,1]\), and have \(\|f_\beta'\|_\infty\leq(1-b)3/4+b/2<1\). Their endpoint bump values vanish, so, for uniform \(X\),
\[
 \mathbb E f_\beta'(X)=\frac{f_\beta(1)-f_\beta(-1)}2=\frac b2>0.
\]
They can be extended beyond the observed index range if a globally defined link is required. For sufficiently large \(T\), each single-spike member below is non-monotone: the falling side of its positive bump has negative derivative, whereas the common affine component has positive derivative. Use independent \(N(0,1)\) reward noise.

Let \(\beta^{(0)}=(-1,\ldots,-1)\), and let \(\beta^{(j)}\) flip only coordinate \(j\). Write \(P_0,P_j\) for their complete adaptive history laws and \(N_j\) for the number of chosen contexts in \(I_j\). The common affine term cancels when comparing hypotheses. Conditional on a selected context, the reward-mean difference is zero outside \(I_j\) and at most \(2(1-b)\varepsilon\) inside. The adaptive KL chain rule and the KL formula for unit-variance Gaussians therefore give
\[
 \mathrm{KL}(P_0\Vert P_j)\leq2\varepsilon^2\mathbb E_0N_j.
\]

Let \(G\) mean that every \(J_j\) contains an offered context in every round. A context lands in a given \(J_j\) with probability \(1/(2N)\). Since \(N\leq T^{1/3}+1\), for all sufficiently large \(T\),
\[
 \Pr(G^c)\leq TN\exp\!\left(-\frac K{2N}\right)
 \leq TN\,T^{-2T^{1/3}/N}\leq2N/T\leq4T^{-2/3}.
\]
The event depends only on contexts, so this bound holds under every hypothesis.

Under the null, \(\sum_j\mathbb E_0N_j=T\). Thus at least \(N/2\) bins have \(\mathbb E_0N_j\leq2T/N\). For each such bin,
\[
 \mathrm{KL}(P_0\Vert P_j)\leq4\varepsilon^2T/N=T/(4N^3)\leq1/4.
\]
Set \(A_j=\{N_j\geq T/2\}\). On every history at most two of these events occur, whence \(\sum_jP_0(A_j)\leq2\). Among the low-expected-count bins choose one with \(P_0(A_j)\leq4/N\). Bretagnolle--Huber, in the form \(P(A)+Q(A^c)\geq\tfrac12e^{-\mathrm{KL}(P\Vert Q)}\), applies to \(P_0,P_j\) and gives
\[
 P_j(A_j^c)\geq\tfrac12e^{-1/4}-4/N.
\]
This is bounded below by a positive universal constant for sufficiently large \(T\).

On \(G\), an arm in \(J_j\) under the spike has mean at least \(1/2+(1-b)\varepsilon-b/2\). An arm outside \(I_j\) belongs to a negative bin and has mean at most \(1/2+b/2\). Hence choosing outside \(I_j\) incurs regret at least \((1-b)\varepsilon-b\geq\varepsilon/2\). On \(A_j^c\cap G\), this occurs on more than \(T/2\) rounds. Consequently
\[
 \mathbb E_jR_T\geq\frac{\varepsilon T}{4}\bigl(P_j(A_j^c)-\Pr(G^c)\bigr)
 \geq c\varepsilon T\geq c'T^{2/3}
\]
for universal positive constants and all sufficiently large \(T\). The policy was arbitrary, and the constructed spike is a valid non-monotone instance satisfying the standing positive-derivative condition.
