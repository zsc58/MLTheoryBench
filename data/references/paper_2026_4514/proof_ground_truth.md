# Reference Proof

## Scope and obligations

The claims concern the diagonal-second-moment surrogate, not the exact population-loss flow. In the random case the common-rate conclusion concerns the explicitly prescribed separate-expectation mean-field approximation, not concentration of a sampled embedding or the evolution of the expected trained matrix.

The proof obligations are: derive the unrestricted matrix gradient; establish entrywise decoupling and the diagonal rates for hard clusters; quantify comparable-variance scaling; determine the limiting coefficients and collision loss; derive the two embedding-ensemble means; and solve the resulting mean-field equation. Each obligation is derived below without an external theorem.

## 1. Objective and unrestricted gradient

Write
\[
\Sigma=\operatorname{diag}(\sigma_i^2),\qquad
P=WW^T,\qquad C=W\Sigma W^T,\qquad S=W\Sigma A W^T.
\]
The matrices \(P,C,S\) are symmetric, with symmetry of \(S\) following from the diagonality of \(A\) and \(\Sigma\). The surrogate objective is
\[
L_{\mathrm d}(B)=\frac12\operatorname{tr}\big[(W^TBW-A)\Sigma(W^TBW-A)^T\big]
=\frac12\left[\operatorname{tr}(A\Sigma A)+\operatorname{tr}(B^TPBC)-2\operatorname{tr}(SB)\right].
\]
For an arbitrary matrix perturbation \(H\), differentiation gives
\[
D L_{\mathrm d}(B)[H]
=\operatorname{tr}\big[(W^TBW-A)\Sigma(W^THW)^T\big]
=\langle PBC-S,H\rangle_F.
\]
Consequently
\[
\nabla_B L_{\mathrm d}=PBC-S,
\qquad \dot B=-\eta(PBC-S).
\]
There is no symmetry constraint on \(B\). Symmetry of \(P\) and \(C\) does not produce a second term \(CBP\) in this unrestricted gradient.

For clarity, the actual input law has \(\mathbb E[x_i]=p_i/2\), \(\mathbb E[x_i^2]=p_i/3\), and, for distinct indices, \(\mathbb E[x_ix_j]=p_ip_j/4\). Thus \(L_{\mathrm d}\) is deliberately a surrogate rather than an identity for the original population objective.

## 2. Hard clusters

The specified embedding gives
\[
P=\operatorname{diag}(n_1,\ldots,n_K),\qquad
C=\operatorname{diag}(C_1,\ldots,C_K),\qquad
S=\operatorname{diag}(S_1,\ldots,S_K).
\]
Every \(n_j\) and \(C_j\) is positive because clusters are nonempty and all feature frequencies are positive. The complete entrywise system is
\[
\dot B_{j\ell}=-\eta\big(n_jC_\ell B_{j\ell}-\mathbf 1_{\{j=\ell\}}S_j\big).
\]
Thus all matrix entries decouple. Off-diagonal entries satisfy
\[
B_{j\ell}(t)=B_{j\ell}(0)e^{-\eta n_jC_\ell t}\quad(j\ne\ell).
\]
For \(b_j=B_{jj}\),
\[
\dot b_j=-\eta(n_jC_jb_j-S_j),
\]
so
\[
b_j(t)=b_j^*+(b_j(0)-b_j^*)e^{-\eta n_jC_jt},
\qquad b_j^*=\frac{S_j}{n_jC_j}.
\]
This holds for any prescribed initial matrix. If a coordinate starts at equilibrium its residual vanishes identically, but its governing homogeneous rate remains \(\eta n_jC_j\).

If \(m q_j\le\sigma_i^2\le M q_j\) for every \(i\in G_j\), then
\[
m n_jq_j\le C_j\le M n_jq_j,
\]
and therefore
\[
\eta m n_j^2q_j\le\eta n_jC_j\le\eta M n_j^2q_j.
\]
The comparison constants are precisely controlled by \(m,M\). This is quadratic scaling relative to the stated variance scale; it does not assert that this scale remains fixed when the normalized feature distribution changes.

## 3. Limiting coefficients and collision error

Let
\[
T_j=\sum_{i\in G_j}a_i^2\sigma_i^2.
\]
For an input coordinate \(i\in G_\ell\), the coefficient in every output coordinate belonging to \(G_j\) is \(B_{j\ell}\). It follows that
\[
L_{\mathrm d}(B)=\frac12\sum_{\ell=1}^K\left[T_\ell-2S_\ell B_{\ell\ell}+C_\ell\sum_{j=1}^K n_jB_{j\ell}^2\right].
\]
Completing the squares gives
\[
L_{\mathrm d}(B)=L_{\mathrm d}^*+rac12\sum_{j,\ell}n_jC_\ell(B_{j\ell}-B_{j\ell}^*)^2,
\]
where \(B^*\) is diagonal with the entries found above and
\[
L_{\mathrm d}^*=\frac12\sum_{j=1}^K\left(T_j-\frac{S_j^2}{n_jC_j}\right).
\]
This is both the minimum surrogate loss and the limit along the flow.

The coefficient \(b_j^*\) is \(1/n_j\) times the variance-weighted average \(S_j/C_j\), not that average itself. Moreover, the residual is not solely an inability to fit different teacher coefficients: decoding also produces off-target outputs within a cluster.

To check positivity directly, set \(\mu_j=S_j/C_j\). Nonnegativity of the weighted sum of squares gives
\[
0\le\sum_{i\in G_j}\sigma_i^2(a_i-\mu_j)^2=T_j-\frac{S_j^2}{C_j}.
\]
Hence
\[
T_j-\frac{S_j^2}{n_jC_j}\ge\left(1-\frac1{n_j}\right)T_j.
\]
Since all \(a_i\) and \(\sigma_i^2\) are positive, a cluster with \(n_j>1\) contributes strictly positive collision loss. A singleton contributes zero. In particular, when \(b=0\), all teacher coefficients equal one, but a nonsingleton cluster still has loss contribution \(C_j(1-1/n_j)/2>0\). If every cluster is a singleton, the limiting loss is zero.

## 4. Ensemble-mean projected matrices

Let \(w_i\) be column \(i\) of the random embedding. Its norm is one, so every entry of \(w_iw_i^T\) is integrable. Rotational invariance implies invariance under coordinate reflections and permutations. Reflections make the off-diagonal entries of \(\mathbb E_W[w_iw_i^T]\) zero, and permutations make its diagonal entries equal. Its trace is \(\mathbb E_W\|w_i\|^2=1\). Therefore
\[
\mathbb E_W[w_iw_i^T]=\frac1K I_K.
\]
This also holds when \(K=1\), directly from the unit-norm condition. Independence among columns is not needed for these first-moment identities. Since the feature weights are deterministic,
\[
\mathbb E_W[P]=\sum_i\mathbb E_W[w_iw_i^T]=\frac NK I_K,
\]
\[
\mathbb E_W[C]=\sum_i\sigma_i^2\mathbb E_W[w_iw_i^T]
=\frac{\sum_i\sigma_i^2}{K}I_K
=\frac NK\bar\sigma^2 I_K.
\]
These are exact ensemble-mean identities for every finite admissible \(N,K\).

## 5. Prescribed isotropic mean-field dynamics

Fix the realized teacher forcing \(S\). By the definition of the mean-field approximation, its trajectory satisfies
\[
\dot B_{\mathrm{mf}}=-\eta\big(\mathbb E_W[P]B_{\mathrm{mf}}\mathbb E_W[C]-S\big)
=-\eta\lambda B_{\mathrm{mf}}+\eta S,
\]
where
\[
\lambda=\left(\frac NK\right)^2\bar\sigma^2>0.
\]
Thus
\[
B_{\mathrm{mf}}(t)=\frac S\lambda+
\left(B_{\mathrm{mf}}(0)-\frac S\lambda\right)e^{-\eta\lambda t}.
\]
Every homogeneous matrix direction has the common relaxation rate \(\eta\lambda\). The teacher matrix affects the forcing and equilibrium, not this homogeneous rate. Under the stipulated activation normalization, \(\sum_i\sigma_i^2=1/3\), so equivalently \(\lambda=N/(3K^2)\).

This establishes rate equalization within the defined mean-field model. It is neither an interchange of expectation with the trained dynamics nor a concentration conclusion.

## 6. Why concentration is not an additional proof obligation

The removed concentration interpretation is not available under the stated weights. For example, take \(a=2\), \(K=2\), and let \(N\) grow. Since
\[
\sum_{i=1}^N i^{-2}\le 1+\frac14+\int_2^\infty x^{-2}\,dx=\frac74,
\]
we have \(p_1\ge4/7\). For every realization of unit columns,
\[
C\succeq\frac{p_1}{3}w_1w_1^T,
\qquad \lambda_{\max}(C)\ge\frac4{21}.
\]
But \(\mathbb E_W[C]=I_2/6\). Consequently
\[
\|C-I_2/6\|_{\mathrm{op}}\ge\frac1{42}
\]
for every realization, independently of how large \(N\) is. This remains true for independent uniform unit columns. It explains why the reference proof must not claim that \(N\gg K\) alone establishes weighted-covariance concentration. The public task asks only for the precisely defined mean-field conclusion.

All requested conclusions are now derived. Neither linear calculation establishes a nonlinear power-law training exponent.
