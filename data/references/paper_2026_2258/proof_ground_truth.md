# Reference Proof

## Proof Structure

Centering decomposes the observed matrix into a centered low-rank signal and projected Gaussian noise. The signal has rank zero when there is one component and rank K-1 otherwise. For K>=2, its smallest nonzero singular value is lower-bounded in terms of center separation, balance, and the condition number. Gaussian operator-norm concentration supplies a strict noise bound with probability tending to one. Weyl inequalities then place exactly K-1 empirical singular values strictly above the threshold, including when the separation assumption holds with equality.

## Complete Proof

### 1. Centered decomposition and Gaussian noise control

Write P=AZ^T, so Y=P+N. The matrix H=I_n-1_n1_n^T/n is an orthogonal projection, and therefore
\[
Y_c=YH=PH+NH=:S+W,
\qquad \|W\|\le\|N\|.
\]
Here vector norms are Euclidean and matrix norms are operator norms.

The independent N(0,I_p) noise columns imply that all entries of N are independent standard normal random variables. We use the standard independent Gaussian rectangular-matrix norm bound: for a p-by-n matrix G with independent N(0,1) entries and any t>=0,
\[
\Pr\{\|G\|\ge\sqrt p+\sqrt n+t\}\le e^{-t^2/2}.
\]
Applying it to N with t=s_n>0 gives, for
\[
F_n=\{\|N\|<\tau\},\qquad \tau=\sqrt p+\sqrt n+s_n,
\]
\[
\Pr(F_n)\ge1-e^{-s_n^2/2}\longrightarrow1.
\]
On F_n, projection contraction gives \(\|W\|<\tau\). The additional assumption s_n=o(sqrt(p)+sqrt(n)) is part of the stated threshold regime; the probability estimate only requires s_n->infinity.

### 2. The one-component case

If K=1, every column of P equals the same center vector. Since 1_n^T H=0, we have S=PH=0. On F_n every singular value of Y_c=W is strictly below tau. Consequently the threshold count is zero and K-hat=1. Thus Pr(K-hat=1)->1 without any separation assumption.

### 3. Centered membership rank and balance bound

Assume K>=2. Put B=Z^T H, so S=AB. Let
\[
c=(n_1,\ldots,n_K)^T,\qquad D=\operatorname{diag}(n_1,\ldots,n_K),\qquad m=\min_k n_k>0.
\]
Because H is symmetric and idempotent, Z^T Z=D, and Z^T1_n=c,
\[
BB^T=Z^THZ=D-\frac{cc^T}{n}.
\]
This matrix annihilates 1_K because c^T1_K=n and D1_K=c.

Write n_k=m+q_k with q_k>=0. For every v perpendicular to 1_K,
\[
v^TBB^Tv
=m\|v\|^2+\sum_kq_kv_k^2-\frac{(\sum_kq_kv_k)^2}{n}.
\]
Cauchy-Schwarz gives
\[
\left(\sum_kq_kv_k\right)^2
\le\left(\sum_kq_k\right)\left(\sum_kq_kv_k^2\right)
=(n-Km)\sum_kq_kv_k^2
\le n\sum_kq_kv_k^2.
\]
Hence
\[
v^TBB^Tv\ge m\|v\|^2\qquad(v\perp1_K).
\]
Thus the kernel of BB^T is exactly the span of 1_K, B has rank K-1, and the minimum Rayleigh quotient on 1_K perpendicular gives
\[
\sigma_{K-1}(B)\ge\sqrt m=\sqrt{\frac{\beta n}{K}}.
\]
Since A has full column rank, multiplication by A preserves the rank of B. Therefore S=AB has rank K-1 and sigma_K(S)=0. The index K exists because K<=min(p,n).

### 4. Signal singular-value lower bound

For every x in R^n, full column rank of A gives
\[
\|ABx\|^2\ge\sigma_K(A)^2\|Bx\|^2.
\]
Equivalently, B^T A^T A B is at least sigma_K(A)^2 B^T B in positive-semidefinite order. The eigenvalue min-max principle therefore implies
\[
\sigma_{K-1}(S)\ge\sigma_K(A)\sigma_{K-1}(B).
\]
For any distinct i,j in {1,...,K},
\[
\Delta\le\|a_i-a_j\|=\|A(e_i-e_j)\|\le\sqrt2\,\sigma_1(A).
\]
Using the definition of kappa,
\[
\sigma_K(A)=\frac{\sigma_1(A)}{\kappa}\ge\frac{\Delta}{\sqrt2\,\kappa}.
\]
Combining these inequalities gives
\[
\sigma_{K-1}(S)
\ge\frac{\Delta}{\kappa}\sqrt{\frac{\beta n}{2K}}.
\]
The stated separation condition makes the right-hand side at least 2 tau.

### 5. Strict threshold counting and consistency

For matrices of the same dimensions, the singular-value perturbation inequality gives
\[
|\sigma_j(S+W)-\sigma_j(S)|\le\|W\|
\qquad(1\le j\le\min(p,n)).
\]
On F_n, the signal lower bound and the strict noise bound imply
\[
\widehat\sigma_{K-1}\ge\sigma_{K-1}(S)-\|W\|
\ge2\tau-\|W\|>\tau,
\]
and
\[
\widehat\sigma_K\le\sigma_K(S)+\|W\|=\|W\|<\tau.
\]
By ordering of the singular values, exactly K-1 singular values exceed tau. Hence K-hat=K on F_n, and
\[
\Pr\{\widehat K=K\}\ge\Pr(F_n)\ge1-e^{-s_n^2/2}\longrightarrow1.
\]
This includes equality in the separation condition and allows all the stated n-dependent parameters. No assertion about the distribution of individual centered-data singular values is needed.

## Source-local Proof Repair

The source and the previous reference proof used a non-strict noise event and then invoked absolute continuity to dismiss threshold ties. Continuity of singular values and absolute continuity of the original data alone do not justify that implication. The strict event F_n is directly authorized by the source's Gaussian tail bound for {||N||>=tau}; it repairs the argument without changing the theorem or its proof architecture. All theorem-critical obligations are closed.
