# Reference Proof

## Proof Structure

1. Derive the chronological recurrence for each exponential-kernel state, including the initial state.
2. Augment the affine state by a constant coordinate and identify the ordered transition products.
3. Derive the compressed scalar-vector product and prove closure, associativity, and its operation/storage costs.
4. Construct an ordered parallel prefix scan and show that it produces every exact state.
5. Recover all event intensities and the full log-likelihood, including the compensator and zero-intensity cases.
6. Count initialization, scan, auxiliary computation, processor time, and compressed-state storage, including singleton histories.

## Complete Proof

### 1. Chronological recurrence

For \(i\ge2\), put \(\Delta_i=t_i-t_{i-1}\). Strict chronological ordering partitions the events before \(t_i\) into those before \(t_{i-1}\) and the event at \(t_{i-1}\). Factoring the common additional exponential decay gives
\[
R_i^k=e^{-\gamma_k\Delta_i}R_{i-1}^k+e^{-\gamma_k\Delta_i}\alpha_{:,m_{i-1},k},
\qquad R_1^k=0.
\]
The initial state is zero because the displayed state definition contains no event strictly before the first event. This proves the recurrence directly from the public definition; no stochastic or stationarity assumption is used.

### 2. Augmentation and ordered products

Define \(\widetilde R_i^k=(R_i^k,1)^\top\). Use the auxiliary initial vector \(\widetilde R_0^k=(0,1)^\top\), and set
\[
M_1^k=I_{M+1},\qquad
M_i^k=\begin{pmatrix}s_i^k I_M&v_i^k\\0^\top&1\end{pmatrix}\quad(i\ge2),
\]
where
\[
s_i^k=e^{-\gamma_k\Delta_i},\qquad
v_i^k=s_i^k\alpha_{:,m_{i-1},k}.
\]
Thus no \(t_0\), \(m_0\), or predecessor event is accessed. The recurrence and initialization imply
\[
\widetilde R_i^k=M_i^k\widetilde R_{i-1}^k,
\qquad
\widetilde R_i^k=P_i^k\widetilde R_0^k,
\qquad
P_i^k=M_i^kM_{i-1}^k\cdots M_1^k.
\]
The product order is important: the transition with the later event index acts on the left.

### 3. Compressed associative operation

Represent a structured matrix by a scalar-vector pair \((s,v)\). Direct multiplication gives
\[
\begin{pmatrix}s_A I_M&v_A\\0^\top&1\end{pmatrix}
\begin{pmatrix}s_B I_M&v_B\\0^\top&1\end{pmatrix}
=
\begin{pmatrix}s_As_B I_M&s_Av_B+v_A\\0^\top&1\end{pmatrix}.
\]
Consequently define
\[
(s_A,v_A)\odot(s_B,v_B)=(s_As_B,\ s_Av_B+v_A).
\]
This operation is closed on scalar-vector pairs. It uses one scalar multiplication and \(O(M)\) vector operations, and its inputs and output each occupy \(M+1=O(M)\) words. Its identity is \(e=(1,0)\). Both parenthesizations of three factors give
\[
(s_As_Bs_C,\ s_As_Bv_C+s_Av_B+v_A),
\]
so the operation is associative without being assumed commutative.

### 4. Ordered scan and exact states

For each kernel, the first scan item is \(e\); item \(i\ge2\) is \((s_i^k,v_i^k)\). An inclusive ordered scan returns the compressed representation of \(P_i^k\). If that representation is \((S_i^k,V_i^k)\), then
\[
P_i^k(0,1)^\top=(V_i^k,1)^\top,
\]
so \(V_i^k=R_i^k\) for every event and kernel.

For completeness, an ordered work-efficient scan can be constructed as follows. Pad the list on the right with identities to a power-of-two length \(n'\), where \(N\le n'<2N\) unless \(N=1\), in which case \(n'=1\). At an upsweep node whose left and right children represent consecutive earlier and later intervals, store the right interval's product combined on the left of the left interval's product. Thus the stored interval total is the product of its entries in decreasing index order.

During a downsweep, let \(Q\) be the product of all entries preceding the node's interval, in the same ordered convention. At the root \(Q=e\). The left child receives \(Q\). If the left child's interval total is \(U\), the right child receives \(U\odot Q\). Hence, at leaf \(i\), the inclusive result is \(x_i\odot Q=x_i\odot\cdots\odot x_1\). This invariant proves correctness without reversing a noncommutative product. Padding does not alter any of the first \(N\) outputs.

The tree has \(O(N)\) nodes and \(O(1+\log N)=O(L_N)\) levels including initialization and leaf output. It performs \(O(N)\) combines/copies, uses \(O(N)\) compressed items, and has \(O(L_N)\) dependent stages. This is the standard-independent scan property invoked in theory_013, with its associativity, identity, ordering, and combine-cost hypotheses explicitly verified above. The construction also handles \(N=1\).

### 5. Event intensities and full likelihood

From the state definition,
\[
\lambda_p(t_i)=\mu_p+\sum_{k=1}^K\gamma_k R_{i,p}^k.
\]
All these quantities are finite and nonnegative: each is a finite sum of finite nonnegative terms.

For each component, integrate the finite sum termwise. An event \(j\) contributes only after \(t_j\); changing the value at an endpoint does not change the integral. For \(t_j\le T\),
\[
\int_{t_j}^T\alpha_{p,m_j,k}\gamma_k e^{-\gamma_k(t-t_j)}\,dt
=\alpha_{p,m_j,k}\bigl(1-e^{-\gamma_k(T-t_j)}\bigr).
\]
Therefore the compensator is
\[
C=T\sum_{p=1}^M\mu_p+
\sum_{j=1}^N\sum_{p=1}^M\sum_{k=1}^K
\alpha_{p,m_j,k}\bigl(1-e^{-\gamma_k(T-t_j)}\bigr).
\]
It is finite and nonnegative. In particular, an event at \(T\) has zero compensator contribution.

If every marked intensity is positive, evaluate its ordinary logarithm and return
\[
\ell=\sum_{i=1}^N\log\lambda_{m_i}(t_i)-C.
\]
If a marked intensity is zero, return \(-\infty\), as required by the public convention. This can be implemented without evaluating a positive-domain logarithm at zero: for event \(i\), store a zero flag and store its logarithm only when the intensity is positive, using zero for the finite-log accumulator otherwise. Reduce the flags by logical OR and the finite-log entries by addition. A true final flag selects \(-\infty\); otherwise use the finite sum minus \(C\). There is no undefined subtraction of two infinities because \(C\) is finite.

The same argument covers zero base rates or interactions, \(t_1=0\), and \(T=0\) when the strict event ordering permits it. No positivity assumption on marked intensities is added.

### 6. Resource bounds

For one kernel, forming all transition items takes \(O(MN)\) work. Each event's item takes \(O(M)\) time on one processor; the first item is initialized as the identity. The tree scan has \(O(MN)\) work, \(O(ML_N)\) span, and \(O(MN)\) storage.

More explicitly, at any scan stage having \(w\) independent item operations, assign them to processors in groups of at most \(P\). Each group takes \(O(M)\) time, so that stage takes \(O(M\lceil w/P\rceil)\) time. Summing over \(O(L_N)\) stages with \(O(N)\) total item operations gives
\[
O\!\left(M\left(\frac NP+L_N\right)\right).
\]
Initialization and output copies fit the same bound. Processing the \(K\) kernels successively, while retaining their output states, gives scan time
\[
O\!\left(KM\left(\frac NP+L_N\right)\right)
\]
and total scan/preparation work \(O(KMN)\). This is an existence bound; exploiting additional parallelism across kernels or vector entries is not required.

The auxiliary likelihood computations fit this time bound as well. Assign one task to each event. In \(O(KM)\) sequential operations, its task computes all \(M\) intensities by summing over kernels, forms its marked-intensity flag/log entry, and computes its scalar event compensator contribution by summing over \(p,k\). The \(N\) event tasks take
\[
O(KM\lceil N/P\rceil)
\]
time. Compute the base compensator in \(O(M)\) time. Balanced scalar reductions of the event compensator contributions, finite-log entries, and zero flags take \(O(N/P+L_N)\) time and \(O(N)\) work. Thus the complete computation, not just the scan, satisfies the displayed bound because \(K,M,L_N\ge1\). This argument does not incorrectly assign constant span to sums over arbitrarily large \(K\) or \(M\).

For \(N\ge2\), \(L_N=\log_2 N\), giving the original nondegenerate asymptotic expression. If \(L_N\le cN/P\), the bound is \(O(KMN/P)\), with a constant depending at most on \(c\). The source's stated sufficient regime \(N/P\ge\log_2 P\) is consistent with this: putting \(x=N/P\), that regime implies \(x\ge1\); for \(P\ge2\), \(\log_2 N=\log_2 P+\log_2 x\le2x\), and for \(P=1\), \(L_N\le N\). For \(N=1\) and arbitrarily many available processors, the positive-depth term supplies the necessary nonzero time allowance rather than claiming unbounded speedup.

Keeping all compressed prefix pairs occupies \(O(KN(M+1))=O(KMN)\) words. A scan tree for the currently processed kernel takes \(O(MN)\) additional words; all intensity outputs and event-reduction storage take \(O(MN+N)\) words. These remain within \(O(KMN)\). Idle processors require no per-processor arrays, so excess available processors do not change this storage count. The claim concerns compressed states and their working storage; it does not assert that the dense input tensor of \(KM^2\) coefficients fits in \(O(KMN)\) words.

Every theorem-critical obligation is therefore closed by explicit derivation or by the standard scan property whose relevant statement, hypotheses, and constructive verification are given above. No unresolved private proof dependency remains.
