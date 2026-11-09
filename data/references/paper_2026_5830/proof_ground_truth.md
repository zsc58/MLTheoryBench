# Reference Proof

## Proof Structure

Fix the training data and hence the learned witness. Verify integrability and the tower identity, apply the iid CLT and laws of large numbers to the held-out scores, and studentize. Under the null, the assumed zero conditional displacement centers the scores. Under a fixed positive-alignment alternative, the signal term diverges while the centered term is tight. This proves consistency; comparison with the limit of the stated Gaussian expression then proves the required absolute-o(1) power formula.

## Standard Background

The following standard independent results are used under each fixed conditional evaluation law. For iid integrable real variables, the empirical mean converges in probability to their expectation. For iid real variables with mean mu and variance tau^2 in (0,infinity), sqrt(n)(sample mean-mu)/tau converges in distribution to N(0,1). Slutsky's theorem states that if A_n converges in distribution to A and B_n converges in probability to a constant b, then A_n B_n converges in distribution to bA. Convergence in distribution to a real-valued limit implies tightness. These results require no fourth moment here: the law of large numbers is applied to the scores and their squares, whose first moments are finite.

## Complete Proof

### Step 001: Conditional experiment

Let G denote the training sigma-field. Work at any training realization outside the null set on which the stated conditional assumptions might fail. The witness psi is now fixed, belongs to L^2(P_M;R^d), and does not vary with n. Independence from G leaves the evaluation pairs iid with law P times Q. Thus the scores S_i are iid under this conditional law, with mean T=E[S_i|G] and variance sigma^2=Var(S_i|G) in (0,infinity). All probabilities, expectations, and limits in the rest of the proof refer to this fixed conditional law.

### Step 002: Integrability and the tower identity

Finite second moments of X and Y imply

\[
\mathbb E\|D\|^2\leq 2\mathbb E\|X\|^2+2\mathbb E\|Y\|^2<\infty.
\]

By Cauchy-Schwarz,

\[
\mathbb E[\|\psi(M)\|\,\|D\|]
\leq (\mathbb E\|\psi(M)\|^2)^{1/2}(\mathbb E\|D\|^2)^{1/2}<\infty.
\]

Conditional Jensen gives E||v(M)||^2 <= E||D||^2, so the corresponding product with v(M) is integrable as well. Consequently the conditional-expectation multiplication rule and tower property apply, yielding

\[
T=\mathbb E\langle\psi(M),D\rangle
 =\mathbb E\langle\psi(M),\mathbb E[D\mid M]\rangle
 =\mathbb E\langle\psi(M),v(M)\rangle.
\]

For completeness, the multiplication rule for this possibly unbounded witness follows by first using the bounded field psi times the indicator of {||psi|| <= k}, then passing to the limit using the two integrable product bounds above.

### Step 003: Null centering

Under P=Q, the public null implication gives v(M)=0 almost surely. The tower identity therefore gives T=0.

There is also an elementary verification of the needed implication that does not rely on the external criterion's converse. Under P=Q, exchanging the independent endpoints preserves their joint law and transforms (M,D) into (M,-D). For every bounded measurable scalar h, integrability of D gives E[h(M)D]=-E[h(M)D], hence E[h(M)D]=0. The defining characterization of conditional expectation then gives E[D|M]=0 almost surely. Only this null direction is needed.

### Step 004: CLT, variance consistency, and studentization

The conditional variance assumption and finite T imply E[S_i^2]=sigma^2+T^2<infinity. The iid CLT gives

\[
\frac{\sqrt n(\bar S_n-T)}{\sigma}\Rightarrow N(0,1).
\]

The laws of large numbers for S_i and S_i^2 give bar S_n -> T and n^{-1} sum_i S_i^2 -> E[S_i^2] in probability. Since

\[
\widehat\sigma_n^2
=\frac{n}{n-1}\left(\frac1n\sum_{i=1}^n S_i^2-\bar S_n^2\right),
\]

we have sigma_hat_n^2 -> sigma^2 and sigma_hat_n -> sigma>0 in probability. In particular,

\[
\Pr(\widehat\sigma_n=0)
\leq\Pr\left(|\widehat\sigma_n^2-\sigma^2|\geq\sigma^2/2\right)\longrightarrow0.
\]

Define R_n=sigma/sigma_hat_n when sigma_hat_n>0 and R_n=0 otherwise. Then R_n -> 1 in probability, and the centered ratio W_n, defined to be zero when its denominator vanishes, satisfies

\[
W_n=\frac{\sqrt n(\bar S_n-T)}{\sigma}R_n\Rightarrow N(0,1)
\]

by Slutsky's theorem. This proves the centered conditional limit. Under the null, T=0, so W_n=Z_n, including on the zero-denominator event. Hence Z_n converges conditionally in distribution to N(0,1). In particular, its rejection probability at the fixed threshold z_{1-alpha} tends to alpha.

### Step 005: Positive-alignment power

Fix an alternative and a training realization with T>0. Let B_n=sqrt(n)T/sigma_hat_n when sigma_hat_n>0, and let B_n=0 otherwise. With the conventions in the task,

\[
Z_n=W_n+B_n.
\]

The centered term W_n is tight. Also,

\[
\frac{B_n}{\sqrt n}=\frac{T}{\sigma}R_n\xrightarrow{p}\frac{T}{\sigma}>0,
\]

so B_n tends to positive infinity in probability. To make the last implication for Z_n explicit, for every epsilon>0 choose K so that the limiting upper bound of Pr(W_n<-K) is less than epsilon. Then

\[
\Pr(Z_n\leq z_{1-\alpha})
\leq\Pr(W_n<-K)+\Pr(B_n\leq z_{1-\alpha}+K).
\]

The second probability tends to zero, and epsilon is arbitrary. Thus the conditional power p_n=Pr(Z_n>z_{1-alpha}|G) tends to one.

Since SNR=T/sigma is a fixed positive number,

\[
g_n=1-\Phi\left(z_{1-\alpha}-\sqrt n\,\mathrm{SNR}\right)\longrightarrow1.
\]

Therefore |p_n-g_n| <= |1-p_n|+|1-g_n| -> 0, proving

\[
\Pr(Z_n>z_{1-\alpha}\mid\mathcal G)
=1-\Phi\left(z_{1-\alpha}-\sqrt n\,\mathrm{SNR}\right)+o(1).
\]

All conclusions hold for almost every training realization satisfying the assumptions, and the positive-signal conclusions apply on {T>0}. This is a pointwise fixed-witness statement with an absolute error tending to zero, not a rate, relative-tail approximation, or uniform local-alternative result. In particular, the proof does not assert sqrt(n)T/sigma_hat_n=sqrt(n)T/sigma+o_p(1), which variance consistency alone does not justify.
