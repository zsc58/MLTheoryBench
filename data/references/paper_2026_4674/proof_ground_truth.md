# Reference Proof

## Proof Structure

Use the displacement from the shared minimizer. The strict all-batch threshold gives a uniform Euclidean contraction for the linear parts. A common analytic coefficient majorant then supplies both an invariant neighborhood and summable bounds for the scaled tensor-moment operator. Independence gives the exact moment recurrence. The block row/column estimate proves boundedness, absolute summability of block norms proves compactness, and compact spectral approximation transfers the diagonal spectral bounds to the full operator. Decay of operator powers gives the required even moments.

The invariant-neighborhood argument is essential for justifying use of the local Taylor series along the nonlinear trajectories. All constants and the radius are chosen using the fixed problem data, before choosing the initialization or the moment order.

## Complete Proof

### Step 1: Displacement dynamics and uniform linear contraction

Let \(y_t=z_t-z^\star\). For each batch \(S\), define
\[
G_S(y)=y-\alpha\nabla\widehat L_S(z^\star+y),\qquad A_S=DG_S(0)=I-\alpha H_S.
\]
The sample gradients vanish at \(z^\star\), so \(G_S(0)=0\). Each \(H_S\) is an average of positive-definite symmetric matrices and is therefore positive definite. The step-size assumption implies
\[
0<\alpha\lambda_{\min}(H_S)\leq\alpha\lambda_{\max}(H_S)<2.
\]
Thus every eigenvalue of the symmetric matrix \(A_S\) lies in \((-1,1)\). There are finitely many batches, so
\[
\gamma:=\max_{|S|=b}\|A_S\|_2\in[0,1).
\]
In particular, \(\gamma=0\) is allowed. Neither distinct Hessian eigenvalues nor a nonzero batch Jacobian is needed.

### Step 2: Analytic coefficients and an invariant neighborhood

Equip every tensor power of \(\mathbb R^d\) with its Euclidean tensor-product norm. On a common neighborhood, write
\[
G_S(y)=\sum_{q\geq1}C_{S,q}y^{\otimes q},\qquad C_{S,1}=A_S,
\]
where \(C_{S,q}=D^qG_S(0)/q!\), represented as a matrix from \((\mathbb R^d)^{\otimes q}\) to \(\mathbb R^d\).

Here is an explicit consequence of analyticity sufficient for all subsequent estimates. Each coordinate of each batch map has an absolutely convergent multivariate power series on a sufficiently small common coordinate box. Since there are finitely many coordinates and batches, its monomial coefficients can be bounded by \(M R^{-|\nu|}\), for common \(M,R>0\). For an ordered derivative index of total degree \(q\) and multiplicity multi-index \(\nu\), the corresponding entry of \(C_{S,q}\) is the monomial coefficient multiplied by \(\nu!/q!\), whose absolute value is at most one. Hence every entry of \(C_{S,q}\) is bounded by \(M R^{-q}\). The matrix has \(d\) rows and \(d^q\) columns, so its operator norm is at most its Frobenius norm, giving
\[
\|C_{S,q}\|_2\leq M d^{(q+1)/2}R^{-q}.
\]
Increasing a constant \(D>0\), we therefore have
\[
\|C_{S,q}\|_2\leq D^{q+1}\qquad(q\geq2)
\]
uniformly over batches. Fix also \(r_0>0\) such that the Taylor representations hold for \(\|y\|_2<r_0\).

Choose \(\rho>0\) sufficiently small that
\[
\rho<r_0,\qquad D\rho<1,\qquad
\theta:=\gamma+\frac{D^3\rho}{1-D\rho}<1.
\]
This is possible because the second term tends to zero with \(\rho\). Since \(D,\rho>0\), we have \(0<\theta<1\), including when \(\gamma=0\).

For \(\|y\|_2\leq\rho\), absolute convergence and the coefficient bound imply
\[
\begin{aligned}
\|G_S(y)\|_2
&\leq\gamma\|y\|_2+\sum_{q\geq2}D^{q+1}\|y\|_2^q\\
&\leq\left(\gamma+\sum_{q\geq2}D^{q+1}\rho^{q-1}\right)\|y\|_2
=\theta\|y\|_2.
\end{aligned}
\]
Consequently, for any deterministic \(\|y_0\|_2<\rho\), every batch sequence generates well-defined iterates in the common Taylor neighborhood, and induction gives
\[
\|y_t\|_2\leq\theta^t\|y_0\|_2<\rho.
\]
The iterates are measurable functions of the batches. All their moments are finite. This argument supplies the domain and integrability needed below; no global analyticity is required.

### Step 3: Exact tensor-moment recurrence

For \(p\geq k\geq1\), set
\[
\Psi_{k,p}(S)=
\sum_{\substack{q_1,\ldots,q_k\geq1\\q_1+\cdots+q_k=p}}
 C_{S,q_1}\otimes\cdots\otimes C_{S,q_k},
\qquad
\Psi_{k,p}=\mathbb E_S[\Psi_{k,p}(S)].
\]
These are linear maps from degree-\(p\) tensors to degree-\(k\) tensors. Expanding the tensor power gives
\[
G_S(y)^{\otimes k}=\sum_{p\geq k}\Psi_{k,p}(S)y^{\otimes p}.
\]
For \(\|y\|_2\leq\rho\), the sum of the norms of all terms in the expanded product is at most
\[
\left(\gamma\rho+\sum_{q\geq2}D^{q+1}\rho^q\right)^k=(\theta\rho)^k.
\]
Thus the expansions are absolutely and uniformly convergent on this ball. This bound justifies taking expectations termwise. The fresh batch \(S_t\) is independent of \(y_t\), since the latter depends only on the deterministic initialization and earlier batches. Therefore, with
\[
m_t^{(k)}=\mathbb E[y_t^{\otimes k}],
\]
we obtain
\[
m_{t+1}^{(k)}=\sum_{p\geq k}\Psi_{k,p}m_t^{(p)}.
\]
Define \(\bar m_t^{(k)}=\rho^{-k}m_t^{(k)}\), and let
\[
\mathcal H=\bigoplus_{k\geq1}(\mathbb R^d)^{\otimes k}
\]
with the square-sum norm. If \(a=\|y_0\|_2/\rho<1\), the pathwise bound implies
\[
\|\bar m_t^{(k)}\|_2
\leq\mathbb E[(\|y_t\|_2/\rho)^k]
\leq a^k.
\]
Hence \(\bar m_t\in\mathcal H\) for every \(t\), including \(y_0=0\). The scaled component recurrence has blocks
\[
(\Psi_\rho)_{k,p}=\rho^{p-k}\Psi_{k,p}\quad(p\geq k),
\]
and zero blocks otherwise. We next verify that these blocks define a bounded operator on \(\mathcal H\).

### Step 4: Quantitative block bounds and boundedness

Put \(a_1=\gamma\) and \(a_q=D^{q+1}\) for \(q\geq2\). The tensor-product norm identity and the triangle inequality give
\[
\|\Psi_{k,p}\|_2\leq
\sum_{\substack{q_1,\ldots,q_k\geq1\\q_1+\cdots+q_k=p}}
 a_{q_1}\cdots a_{q_k}.
\]
Summing these nonnegative bounds yields
\[
\begin{aligned}
\sum_{p\geq k}\rho^{p-k}\|\Psi_{k,p}\|_2
&\leq\rho^{-k}\left(\sum_{q\geq1}a_q\rho^q\right)^k\\
&=\left(\gamma+\frac{D^3\rho}{1-D\rho}\right)^k
=\theta^k.
\end{aligned}
\]
In particular, the row sums are bounded by \(\theta\), and
\[
\sum_{k\geq1}\sum_{p\geq k}\rho^{p-k}\|\Psi_{k,p}\|_2
\leq\sum_{k\geq1}\theta^k=\frac{\theta}{1-\theta}.
\]
Every column sum is therefore at most \(\theta/(1-\theta)\).

For completeness, the block row/column estimate follows directly from Cauchy–Schwarz. If \(b_{k,p}=\|T_{k,p}\|\), the row sums are at most \(R_T\), and the column sums at most \(C_T\), then for finitely supported \(u\),
\[
\begin{aligned}
\|Tu\|^2
&\leq\sum_k\left(\sum_p b_{k,p}\|u_p\|\right)^2\\
&\leq\sum_k\left(\sum_p b_{k,p}\right)
              \left(\sum_p b_{k,p}\|u_p\|^2\right)\\
&\leq R_T C_T\sum_p\|u_p\|^2.
\end{aligned}
\]
The estimate extends the block operator continuously to the square-sum space, with \(\|T\|\leq\sqrt{R_TC_T}\). Applying it here proves boundedness of \(\Psi_\rho\). Thus the componentwise identities from Step 3 give the actual Hilbert-space identity
\[
\bar m_{t+1}=\Psi_\rho\bar m_t.
\]

### Step 5: Compactness by finite truncation

Let \(P_N\) project onto tensor degrees \(1,\ldots,N\), and put \(T_N=P_N\Psi_\rho P_N\), regarded as an operator on the full space. Each \(T_N\) has finite rank. Embedding a single block into the full space preserves its operator norm. Absolute summability of the block norms therefore gives
\[
\|\Psi_\rho-T_N\|
\leq
\sum_{\substack{k\geq1,\ p\geq k\\k>N\ \text{or}\ p>N}}
\rho^{p-k}\|\Psi_{k,p}\|_2
\longrightarrow0.
\]
Indeed, the omitted terms form a tail of a convergent nonnegative double series. Thus \(\Psi_\rho\) is an operator-norm limit of finite-rank operators and is compact.

### Step 6: Spectral control

Each finite truncation is block upper triangular. Its diagonal blocks are
\[
\Psi_{k,k}=\mathbb E_S[A_S^{\otimes k}],
\]
so
\[
r(\Psi_{k,k})\leq\|\Psi_{k,k}\|_2
\leq\mathbb E_S\|A_S^{\otimes k}\|_2
=\mathbb E_S\|A_S\|_2^k
\leq\gamma^k.
\]
The spectrum of the finite-dimensional restriction of \(T_N\) is the union of the spectra of its diagonal blocks; extending it by zero to the full space only adds zero. Thus every spectral value of every \(T_N\) has modulus at most \(\gamma\).

Use the following standard-independent compact spectral approximation result, in precisely the form needed here: if compact operators \(T_N\) converge in operator norm to a compact operator \(T\) on a complex Banach space, then every nonzero spectral value of \(T\) is an isolated eigenvalue of finite algebraic multiplicity and is approached by spectral values of \(T_N\). This is the relevant content of the source's cited compact-operator lemma; no enumeration of nonexistent nonzero eigenvalues is needed.

Apply the result after complexifying the tensor Hilbert space. The coefficient bounds, finite rank, compactness, and operator-norm convergence remain valid there. Consequently, every nonzero spectral value of \(\Psi_\rho\) has modulus at most \(\gamma\); zero satisfies the same bound. Hence
\[
r(\Psi_\rho)\leq\gamma<1.
\]
This includes \(\gamma=0\).

### Step 7: Operator powers and even moments

Use the standard-independent spectral-radius formula for a bounded operator \(T\) on a complex Banach space:
\[
r(T)=\lim_{t\to\infty}\|T^t\|^{1/t}.
\]
Boundedness was proved in Step 4. Choose \(q\) with \(\gamma<q<1\). The formula and Step 6 imply \(\|\Psi_\rho^t\|\leq q^t\) for all sufficiently large \(t\); increasing a finite constant gives
\[
\|\Psi_\rho^t\|\leq Cq^t\qquad(t\geq0).
\]
For the deterministic initialization,
\[
\|\bar m_0\|_{\mathcal H}^2
=\sum_{k\geq1}(\|y_0\|_2/\rho)^{2k}<\infty.
\]
The recurrence therefore gives
\[
\bar m_t=\Psi_\rho^t\bar m_0\longrightarrow0
\quad\text{in }\mathcal H.
\]
In particular, \(\rho^{-k}m_t^{(k)}\to0\) for each fixed \(k\).

If \(k=2\ell\), define the linear functional \(F_k\) on degree-\(k\) tensors by summing the coordinates indexed by
\((i_1,i_1,i_2,i_2,\ldots,i_\ell,i_\ell)\), over all \(i_1,\ldots,i_\ell\in\{1,\ldots,d\}\). Then
\[
F_k(y^{\otimes k})
=\left(\sum_{i=1}^d y_i^2\right)^\ell
=\|y\|_2^k.
\]
This is a continuous functional on a finite-dimensional tensor space. Thus
\[
\rho^{-k}\mathbb E\|z_t-z^\star\|_2^k
=F_k(\rho^{-k}m_t^{(k)})\longrightarrow0.
\]
The same \(\rho\) works for every deterministic initialization in the specified ball and every even \(k\geq2\).

## Alternative Proof and Source-Contract Check

The invariant-ball estimate in Step 2 already gives a complete shorter proof:
\[
0\leq\rho^{-k}\mathbb E\|y_t\|_2^k
\leq(\|y_0\|_2/\rho)^k\theta^{kt}\longrightarrow0.
\]
A solver may instead obtain that invariant-ball estimate from continuity of the finitely many Jacobians and integration along the segment from zero to \(y\). Neither tensor operators nor spectral theory is mandatory for full credit.

For comparison with the source statement, for every fixed \(k\geq2\),
\[
\|y\|_k^k\leq\|y\|_2^k\leq d^{k/2-1}\|y\|_k^k.
\]
Hence the source's normalized ell_k moment conclusion and the public normalized Euclidean moment conclusion are equivalent with the same radius. No limit uniform in \(k\) is asserted or required.
