# Reference Proof

## Proof Structure

1. Resolve each clean witness moment into label-conditional measures and substitute the pointwise signed-measure decontamination identity.
2. Specialize this identity to positive-unlabeled sampling, obtaining the corrected population moment and its fixed-witness unbiased estimator.
3. Establish uniform residual control with a finite net, one-sided symmetrization, signed-multiplier contraction, and bounded-difference concentration; then deduce the stated MC deviation bound.
4. Analyze projected updates with a squared-error potential and combine fresh-batch conditional control with a finite union bound to prove termination, calibration, and the sample budgets.

## 1. Observable Witness Moments

For every measurable predictor and witness, conditioning on the label gives
\[
R_{c,w}(f)=\pi_+\mathbb E_{P_+}[c(X)w(f(X))(1-f(X))]-\pi_-\mathbb E_{P_-}[c(X)w(f(X))f(X)].
\]
Thus \(R_{c,w}(f)=\int L_{c,w}(x;f)^\top dB(x)\). Interpret the correction identity componentwise: if the observable source vector has components \(Q_j\), then
\[
B_i(dx)=\sum_j (M_{\rm corr}^{\dagger}(x))_{ij}Q_j(dx).
\]
Substituting this identity and using the stipulated integrability gives
\[
R_{c,w}(f)=\int L_{c,w}(x;f)^\top M_{\rm corr}^{\dagger}(x)\,d\bar P(x).
\]
This includes the constant-matrix case. Taking absolute values and the supremum proves the observable representation of MC.

## 2. PU Specialization and Unbiasedness

Since \(\pi_->0\),
\[
M_{\rm PU}^{-1}=\begin{pmatrix}1&0\\-\pi_+/\pi_-&1/\pi_-\end{pmatrix}.
\]
Writing \(a(x)=c(x)w(f(x))\), the correct row multiplication is
\[
L_{c,w}(x;f)^\top M_{\rm PU}^{-1}=(\pi_+a(x),-a(x)f(x)).
\]
Therefore
\[
R_{c,w}(f)=\pi_+\mathbb E_{P_+}[c(X)w(f(X))]-\mathbb E_{P_X}[c(X)w(f(X))f(X)].
\]
For a fixed predictor and witness independent of the estimating samples, each empirical average has the corresponding population expectation. Consequently \(\mathbb E\widehat R_{c,w}^{PU}(f)=R_{c,w}(f)\). This is a statement about an individual fixed witness, not about the supremum estimator or a witness selected from the same sample. All these exact statements use the true class prior.

## 3. Uniform Residual Control

We first prove a bound for one source with law \(Q\), sample size \(n\), and a fixed measurable multiplier \(a:X\to[-1,1]\). Let \(Q_n\) denote its empirical measure and write
\[
Z_{a,+}=\sup_{c\in C}(Q_n-Q)(ac),\qquad Z_{a,-}=\sup_{c\in C}(Q-Q_n)(ac).
\]
Both suprema are measurable by the public convention and are bounded. The Rademacher complexity used here is the source's non-absolute convention.

### Signed-Multiplier Contraction

For a fixed sample \(x_1,\ldots,x_n\), define the convex function
\[
F(z_1,\ldots,z_n)=\sup_{c\in C}\frac1n\sum_i z_i c(x_i).
\]
For any convex one-coordinate section and \(0\le b\le1\), convexity gives
\[
\frac{F(\ldots,b,\ldots)+F(\ldots,-b,\ldots)}2\le\frac{F(\ldots,1,\ldots)+F(\ldots,-1,\ldots)}2.
\]
Apply this successively to the coordinates with \(b_i=|a(x_i)|\). Deterministic sign changes of independent Rademacher variables preserve their joint law. It follows that
\[
\mathbb E_\sigma\sup_{c\in C}\frac1n\sum_i\sigma_i a(x_i)c(x_i)\le\mathbb E_\sigma\sup_{c\in C}\frac1n\sum_i\sigma_i c(x_i).
\]
Hence \(\mathfrak R_n(aC;Q)\le\mathfrak R_n(C;Q)\), with no assumption that the multipliers are nonnegative. Also \(\mathfrak R_n(-aC;Q)=\mathfrak R_n(aC;Q)\).

### One-Sided Symmetrization

Introduce an independent ghost sample with empirical measure \(Q'_n\). Jensen's inequality for the supremum gives
\[
\mathbb E Z_{a,+}\le\mathbb E\sup_c(Q_n-Q'_n)(ac).
\]
Independently exchanging the two members of each sample pair leaves the joint law unchanged. Thus the right side equals
\[
\mathbb E\sup_c\frac1n\sum_i\sigma_i\{a(X_i)c(X_i)-a(X'_i)c(X'_i)\}.
\]
The supremum of the difference is at most the sum of the separate suprema. Symmetry of the signs therefore bounds this expression by \(2\mathfrak R_n(aC;Q)\). The same argument applies to \(Z_{a,-}\). Consequently
\[
\mathbb E Z_{a,+},\ \mathbb E Z_{a,-}\le2\mathfrak R_n(C;Q).
\]
We have deliberately treated the two directions separately; one must not replace this argument by an unjustified absolute-supremum symmetrization using the non-absolute complexity.

### Concentration and Probability Allocation

Use the following standard independent bounded-difference result: if a measurable bounded function \(Z\) of independent coordinates changes by at most \(b_i\) when coordinate \(i\) is replaced, then
\[
\Pr\{Z-\mathbb EZ>u\}\le\exp\left(-\frac{2u^2}{\sum_i b_i^2}\right),\qquad u>0.
\]
Here \(|ac|\le1\), so replacing one observation changes either one-sided supremum by at most \(2/n\). The hypotheses of this result are therefore satisfied, and
\[
\Pr\{Z_{a,\pm}>2\mathfrak R_n(C;Q)+u\}\le e^{-nu^2/2}.
\]

Fix \(\eta\in(0,1]\), and choose a covering net \(W_\eta\subseteq W\) of size \(M=N_\infty(\eta,W)\). It is finite and nonempty. For each net witness, use the normalized multipliers
\[
a_{1,w}(x)=w(f(x)),\qquad a_{2,w}(x)=f(x)w(f(x)).
\]
They are fixed independently of their samples, measurable, and bounded by one. Allocate failure probability \(\delta/(4M)\) to each of the two directions for each of the two sources and each net witness. A union bound gives, simultaneously for all net witnesses and both sources,
\[
\sup_c|(P_{s,n_s}-P_s)(a_{s,w}c)|\le2\mathfrak R_{n_s}(C;P_s)+\sqrt{\frac{2\log(4M/\delta)}{n_s}}.
\]
Restoring the two source weights and using the PU identity gives uniform control of the corrected residual errors on the net.

For any \(w\in W\), choose \(\widetilde w\in W_\eta\) with \(\|w-\widetilde w\|_\infty\le\eta\). For each normalized source, the population difference and empirical difference are each at most \(\eta\), uniformly over \(c\). Thus
\[
\sup_{c,w}|\widehat R_{c,w}^{PU}(f)-R_{c,w}(f)|\le\sum_{s=1}^2\pi_s\left[2\mathfrak R_{n_s}(C;P_s)+2\eta+\sqrt{\frac{2\log(4M/\delta)}{n_s}}\right].
\]
Since \(M\ge1\),
\[
\sqrt{2\log(4M/\delta)}\le2\sqrt{2\log M+\log(4/\delta)}.
\]
This proves, with the exact requested constants,
\[
\sup_{c,w}|\widehat R_{c,w}^{PU}(f)-R_{c,w}(f)|\le2\sum_{s=1}^2\pi_s\left[\mathfrak R_{n_s}(C;P_s)+\eta+\sqrt{\frac{2\log N_\infty(\eta,W)+\log(4/\delta)}{n_s}}\right].
\]
Finally,
\[
|\widehat{MC}^{PU}_{C,W}(f)-MC_{C,W}(f)|\le\sup_{c,w}|\widehat R_{c,w}^{PU}(f)-R_{c,w}(f)|,
\]
which proves target 2.

### Explicit Source-Local Proof Repair

The original source combines separately obtained square-root terms into a smaller single square root without a valid numerical inequality. The signed net-wise concentration argument above repairs that inference while proving the unchanged proposition. It also avoids any unproved absolute-symmetrization step. No source statement has been weakened or given a new substantive assumption.

## 4. Adaptive Correction

### Exact Finite-W Control and Sample Sizes

For finite \(W\), use \(W\) itself in the preceding signed-process argument, without approximation. With failure probability \(\delta_0\), it gives
\[
\sup_{c,w}|\widehat R_{c,w}^{PU}(f)-R_{c,w}(f)|\le\pi_+\left[2\mathfrak R_{n_+}(C;P_+)+\sqrt{\frac{2\log(4|W|/\delta_0)}{n_+}}\right]+2\mathfrak R_{n_u}(C;P_X)+\sqrt{\frac{2\log(4|W|/\delta_0)}{n_u}}.
\]
Set \(\delta_0=\delta/(K_\epsilon+1)\), so the logarithm is \(L\). The assumed complexity bounds imply that this error is at most
\[
(2C_R+\sqrt2)\left[\pi_+\sqrt{\frac{d_C\log n_++L}{n_+}}+\sqrt{\frac{d_C\log n_u+L}{n_u}}\right].
\]
The sample-size assumptions with
\[
C_0=64(2C_R+\sqrt2)^2
\]
make each square-root term, including its source weight, at most \(\epsilon/\sqrt{C_0}\). Hence their displayed sum is at most \(\epsilon/4\). This constant depends only on \(C_R\), as the source states.

### Potential Decrease

Define
\[
\Psi(f)=\mathbb E_{P_X}[(f(X)-f^*(X))^2].
\]
For a selected witness, put \(\Delta(x)=\tau c(x)w(f(x))\). Then \(|\Delta|\le1\). Since \(f^*(x)\in[0,1]\), projection gives
\[
\Psi(\Pi_{[0,1]}(f+\lambda\Delta))\le\Psi(f)+2\lambda\mathbb E[(f-f^*)\Delta]+\lambda^2\mathbb E[\Delta^2].
\]
The conditional-expectation identity gives
\[
\mathbb E[(f-f^*)\Delta]=-\tau R_{c,w}(f).
\]
Therefore, whenever \(\tau R_{c,w}(f)>\epsilon/2\) and \(\lambda=\epsilon/2\),
\[
\Psi(f^+)\le\Psi(f)-\epsilon\tau R_{c,w}(f)+\epsilon^2/4<\Psi(f)-\epsilon^2/4.
\]
In particular each accepted valid update decreases the potential by at least \(\epsilon^2/4\).

### Conditional Events, Stopping, and Budgets

At an executed call \(t\), condition on all previously observed batches and any already used independent randomization. The selection rule has no future-batch access. Thus \(f_t\) is fixed under this conditioning, and the current samples have independent product laws \(P_+^{n_+}\) and \(P_X^{n_u}\). The finite-W calculation gives conditional failure probability at most \(\delta/(K_\epsilon+1)\) for the event
\[
E_t=\left\{\sup_{c,w}|\widehat R_{c,w}^{PU}(f_t)-R_{c,w}(f_t)|\le\epsilon/4\right\}.
\]
To make a fixed finite list of events, one may extend the predictor constantly after stopping and supply unused independent hypothetical batches. This is only a proof construction and does not alter the algorithm's sample usage. The tower property and union bound give
\[
\Pr\left(\bigcap_{t=0}^{K_\epsilon}E_t\right)\ge1-\delta.
\]
On this event, an empirical signed residual exceeding \(3\epsilon/4\) has true signed residual exceeding \(\epsilon/2\), so every accepted update has the preceding potential decrease. After \(m\) updates,
\[
0\le\Psi(f_m)\le D_0-m\epsilon^2/4.
\]
A further update after \(K_\epsilon\) successes would force negative potential because \(K_\epsilon+1>4D_0/\epsilon^2\). Therefore the procedure stops in at most \(K_\epsilon+1\) calls, with at most \(K_\epsilon\) successful updates. This includes \(D_0=0\): on \(E_0\), any update would contradict nonnegativity, so the first call stops.

At stopping, the exhaustive existence test implies \(\sup_{c,w}|\widehat R_{c,w}^{PU}(f_t)|\le3\epsilon/4\). On \(E_t\), consequently \(MC_{C,W}(f_t)\le\epsilon\). Each executed call uses exactly \(n_+\) positive and \(n_u\) unlabeled observations, proving both total budgets on the same event.

## Obligation Closure

All theorem-critical obligations are explicitly closed above. The only invoked independent concentration result is stated with its hypotheses, which are verified. The prior multicalibration references and the inherited contamination framework are not used as theorem-critical black boxes. There are no unresolved GT obligations.
