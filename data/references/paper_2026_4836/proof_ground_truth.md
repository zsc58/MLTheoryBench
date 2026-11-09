# Reference Proof

## Proof Structure

Establish weighted unbiasedness, including the zero-potential justification required by the stated non-extinction condition. Reduce total variation of the expected terminal law to normalizer error. Analyze that error with a ratio martingale, conditional iid second moments, and weighted Cauchy–Schwarz. Finally use action-level coverage and the normalized chi-square identity.

## Complete Proof

Write \(K_h f(x)=\int f(y)K_h(dy\mid x)\), and let \(\mathcal F_h\) be the particle history through level \(h\). All functions defining the instance are fixed. The reference Markov property and the definition of the value functions give
\[
K_hV_h=V_{h-1}\quad\pi_{h-1}\text{-almost surely},\qquad \pi_h(V_h)=Z.
\]
The given finite positive normalizers make the tilted measures probabilities. We use the root-scaled normalizer in the task, so \(\widehat W_0=\widehat V_0(\perp)\).

### 1. Positivity and weighted unbiasedness

We prove jointly, for every level, that \(\widehat V_h>0\) \(\pi_h\)-almost surely and that
\[
\mathbb E[\widehat W_h\widehat\nu_h(g)]=\pi_h(\widehat V_hg)                       \tag{1}
\]
for every nonnegative measurable \(g\). Both claims hold at level zero. The empirical law is supported on positive-potential particles: zero-weight particles have zero mass, and the root potential is positive. Consequently sampled parents have positive denominators. Finite-valued potentials and non-extinction ensure \(0<\widehat W_h<\infty\) almost surely at every step.

Suppose the joint claims hold at level \(h-1\). Put
\[
p_h(x)=K_h(\{y:\widehat V_h(y)=0\}\mid x).
\]
Given \(\mathcal F_{h-1}\), the probability that all \(N\) incremental weights vanish is
\[
[\widehat\nu_{h-1}(p_h)]^N.
\]
Non-extinction therefore implies \(\widehat\nu_{h-1}(p_h)=0\) almost surely. Applying (1) at level \(h-1\) gives
\[
0=\mathbb E[\widehat W_{h-1}\widehat\nu_{h-1}(p_h)]
 =\pi_{h-1}(\widehat V_{h-1}p_h).
\]
Since \(\widehat V_{h-1}>0\) almost surely under \(\pi_{h-1}\), we have \(p_h=0\) almost surely under that marginal. Thus \(\pi_h(\widehat V_h=0)=\pi_{h-1}(p_h)=0\).

For nonnegative measurable \(g\), cancellation of the empirical normalization and conditional iid sampling give
\[
\mathbb E[\widehat W_h\widehat\nu_h(g)\mid\mathcal F_{h-1}]
=\widehat W_{h-1}\widehat\nu_{h-1}\left(
\frac{K_h(\widehat V_hg)}{\widehat V_{h-1}}\right).                       \tag{2}
\]
Define the displayed quotient arbitrarily on the zero set of its denominator; that set has both empirical and reference-marginal measure zero. Applying the inductive identity to this nonnegative test function yields
\[
\mathbb E[\widehat W_h\widehat\nu_h(g)]
=\pi_{h-1}(K_h(\widehat V_hg))=\pi_h(\widehat V_hg).
\]
Nonnegative integration and monotone convergence justify this argument even for unbounded test functions. The identity extends by positive and negative parts whenever \(\pi_h(\widehat V_h|g|)<\infty\). In particular,
\[
\mathbb E\widehat W_h=\widehat Z_h<\infty.
\]

At level \(H\), positivity implies \(r>0\) \(\pi_H\)-almost surely. Consequently \(V_h>0\) \(\pi_h\)-almost surely: if \(V_h=0\) on a set of positive marginal probability, the nonnegative terminal reward would have zero integral on the corresponding event, contradicting its almost-sure positivity. Also \(V_h<\infty\) almost surely because \(\pi_h(V_h)=Z<\infty\). These are consequences of the existing assumptions, not additional hypotheses.

### 2. Terminal total-variation reduction

Since \(\widehat V_H=r\), (1) gives, for every bounded measurable \(f\),
\[
\mathbb E[\widehat W_H\widehat\nu_H(f)]=Z\pi_H^*(f).
\]
For \(|f|\le1\),
\[
\left|Z\mathbb E\widehat\nu_H(f)-Z\pi_H^*(f)\right|
=\left|\mathbb E[(Z-\widehat W_H)\widehat\nu_H(f)]\right|
\le\mathbb E|\widehat W_H-Z|.
\]
Using the bounded-test-function characterization of total variation for two probability measures gives
\[
D_{\rm TV}(\mathbb E\widehat\nu_H,\pi_H^*)
\le\frac{\mathbb E|\widehat W_H-Z|}{2Z}.                                  \tag{3}
\]
This is a bound on TV of the expected law, not on expected TV.

### 3. Ratio martingale

If any intermediate chi-square divergence is infinite, the desired inequality is immediate. Henceforth assume they are all finite. Define \(d_j=D_{\chi^2}(\pi_j^*\|\widehat\pi_j)\) for \(1\le j<H\), and put \(d_0=0\).

Set \(\rho_h=V_h/\widehat V_h\) on the almost-sure positive finite domain, assigning arbitrary values on marginal null sets, and define
\[
M_h=\widehat W_h\widehat\nu_h(\rho_h).
\]
Identity (1) gives \(\mathbb EM_h=\pi_h(V_h)=Z\), so each \(M_h\) is integrable. Marginal null sets have zero empirical mass almost surely: apply (1) to their indicators and use \(\widehat W_h>0\). The same observation and conditional propagation allow all reference-almost-sure identities below to be used on sampled pairs.

Using (2) and \(K_hV_h=V_{h-1}\),
\[
\mathbb E[M_h\mid\mathcal F_{h-1}]
=\widehat W_{h-1}\widehat\nu_{h-1}
 \left(\frac{K_hV_h}{\widehat V_{h-1}}\right)=M_{h-1}.
\]
Moreover \(M_0=Z\), and terminal equality gives \(\rho_H=1\) on the terminal empirical support, hence \(M_H=\widehat W_H\). Therefore
\[
\mathbb E|\widehat W_H-Z|\le\sum_{h=1}^H\mathbb E|M_h-M_{h-1}|.             \tag{4}
\]

### 4. Quantitative increment bound

Given \(\mathcal F_{h-1}\), define the iid variables
\[
Y_h^i=\frac{V_h(X_h^i)}{\widehat V_{h-1}(A_{h-1}^i)}.
\]
Their conditional mean is \(\widehat\nu_{h-1}(\rho_{h-1})\), and
\[
M_h-M_{h-1}=\widehat W_{h-1}
\left(\frac1N\sum_{i=1}^NY_h^i-\mathbb E[Y_h^1\mid\mathcal F_{h-1}]\right).
\]
Put
\[
q_{h-1}(x)=\frac{K_h(V_h^2)(x)}{\widehat V_{h-1}(x)^2},\qquad
\Delta_{h-1}=\frac1N\widehat\nu_{h-1}(q_{h-1}),
\]
with arbitrary zero-set values. Conditional independence makes all cross terms of the centered sum vanish, so
\[
\mathbb E[(M_h-M_{h-1})^2\mid\mathcal F_{h-1}]
\le\widehat W_{h-1}^2\Delta_{h-1}.                                        \tag{5}
\]
The finiteness assertions needed for this calculation follow from the next identities and estimates.

Applying (1) to the nonnegative function \(q_{h-1}\),
\[
\mathbb E[\widehat W_{h-1}\Delta_{h-1}]
=\frac1N\pi_{h-1}\left(\frac{K_h(V_h^2)}{\widehat V_{h-1}}\right).          \tag{6}
\]
For \(0\le j<H\), direct substitution of the normalized densities gives
\[
1+d_j=\frac{\widehat Z_j}{Z^2}
\pi_j\left(\frac{V_j^2}{\widehat V_j}\right),                              \tag{7}
\]
where \(\widehat Z_0=\widehat V_0(\perp)\). For \(j=0\), the right side equals one. For \(j>0\), (7) follows by expanding \(\int(d\pi_j^*/d\widehat\pi_j)^2d\widehat\pi_j\), which equals \(1+d_j\). More generally, the same identity holds in the extended sense with \(0/0=0\) in the reference integral; it does not require replacing \(\widehat Z_j/Z\) by an expectation that could omit PRM mass on \(\{V_j=0\}\).

Action-level coverage gives
\[
V_h(y)^2\le C_{\rm act}V_{h-1}(x)V_h(y)
\]
on reference transitions. Integrating conditionally and using the conditional-value identity yields
\[
K_h(V_h^2)(x)\le C_{\rm act}V_{h-1}(x)^2
\quad\pi_{h-1}\text{-almost surely}.                                     \tag{8}
\]
Equations (6)–(8), finite \(d_{h-1}\), and \(0<\widehat Z_{h-1}<\infty\) show that \(\mathbb E[\widehat W_{h-1}\Delta_{h-1}]<\infty\). Since \(\widehat W_{h-1}>0\), \(\Delta_{h-1}<\infty\) almost surely, justifying the conditional second moments in (5). Global square-integrability of the martingale is not needed.

The elementary Cauchy–Schwarz inequality \((\mathbb E AB)^2\le\mathbb EA^2\mathbb EB^2\) follows by expanding \(\mathbb E(A-tB)^2\ge0\); it applies conditionally as well. First apply it conditionally to the increment and the constant one, then apply it to \(A=\sqrt{\widehat W_{h-1}}\) and \(B=\sqrt{\widehat W_{h-1}\Delta_{h-1}}\). Their squared expectations are finite by (1) and (6)–(8). Thus
\[
\begin{aligned}
\mathbb E|M_h-M_{h-1}|
&\le\mathbb E[\widehat W_{h-1}\sqrt{\Delta_{h-1}}]\\
&\le\sqrt{\mathbb E\widehat W_{h-1}\,
             \mathbb E[\widehat W_{h-1}\Delta_{h-1}]}\\
&=\frac1{\sqrt N}
\sqrt{\widehat Z_{h-1}\,
\pi_{h-1}\left(\frac{K_h(V_h^2)}{\widehat V_{h-1}}\right)}\\
&\le Z\sqrt{\frac{C_{\rm act}}N}\sqrt{1+d_{h-1}}.
\end{aligned}                                                            \tag{9}
\]

### 5. Summation and cases

Combining (3), (4), and (9),
\[
D_{\rm TV}(\mathbb E\widehat\nu_H,\pi_H^*)
\le\frac12\sqrt{\frac{C_{\rm act}}N}
\sum_{j=0}^{H-1}\sqrt{1+d_j}
\le\frac12\sqrt{\frac{C_{\rm act}}N}
\left(H+\sum_{j=1}^{H-1}\sqrt{d_j}\right).
\]
Here \(\sqrt{1+d}\le1+\sqrt d\) for \(d\ge0\). Dropping the factor \(1/2\) proves the requested bound. For \(H=1\), the intermediate sum is empty and the argument uses only \(d_0=0\). The argument applies to every positive integer \(N\), including \(N=1\).

## Source Corrections and Obligation Closure

The auxiliary normalizer uses the initialization explicitly employed in the source unbiasedness proof, correcting the algorithm display's omitted root factor. The intermediate TV bound requires division by \(2Z\), and its chi-square product requires \(Z^2\). The general chi-square conversion uses the actual normalizer ratio rather than an unsupported common-support cancellation. These repairs do not change the output law or the flagship target.

All theorem-critical obligations are explicitly derived above. No specialized external theorem or unresolved paper-specific dependency is used.
