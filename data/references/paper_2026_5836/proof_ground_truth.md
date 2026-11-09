# Reference Proof

## Proof Structure

1. Establish that each oracle update is a probability density and rewrite it as a multiplicative likelihood-ratio update.
2. Justify integrability of the logarithms, compare successive prior KL divergences, and use Jensen's inequality to obtain a decrease at least as large as the current marginal KL divergence.
3. Apply strong prior-identifiability to convert that marginal divergence into a fraction of the prior divergence, then iterate the resulting contraction.
4. Apply KL data processing through the simulator kernel for the marginal bound.

## Complete Proof

Write
\[
D_t=\mathrm{KL}(\pi^\star\|\pi_t),\qquad A_t=\mathrm{KL}(m^\star\|m_t).
\]
We will prove by induction that the updates are well-defined and that each \(D_t\) is finite.

We use the standard KL data-processing inequality: for probability laws \(P,Q\) and a common Markov kernel \(K\),
\[
\mathrm{KL}(PK\|QK)\le \mathrm{KL}(P\|Q).
\]
Here the common kernel is the specified simulator, and its pushforwards of \(\pi^\star\) and \(\pi_t\) are exactly \(m^\star\) and \(m_t\).

We also use an elementary integrability fact. If probability densities \(p\) and \(v\) satisfy \(p\ll v\), then
\[
\int p\left(\log\frac p v\right)^-\le \frac1e.
\]
Indeed, on \(0<p<v\), put \(u=p/v\) and use \(u\log(1/u)\le1/e\), then integrate against \(v\). Consequently, finite KL implies absolute integrability of the corresponding log density ratio under its first argument. Here \(a^- = \max\{-a,0\}\), and similarly \(a^+=\max\{a,0\}\).

### Step 1: Well-definedness and the multiplicative update

Suppose \(D_t<\infty\), as holds initially by assumption. Then \(\pi^\star\ll\pi_t\), and pushing these laws through the common kernel gives \(m^\star\ll m_t\). Data processing gives
\[
0\le A_t\le D_t<\infty.
\]
Thus the posterior is defined for \(m^\star\)-almost every observation. Its population average is nonnegative and integrates to one, so \(\pi_{t+1}\) is a probability density; posterior versions on \(m_t\)-null sets do not affect the update.

Define
\[
r_t(x)=\frac{m^\star(x)}{m_t(x)}\quad\text{when }m_t(x)>0,
\]
and set \(r_t(x)=0\) otherwise. Bayes' rule gives
\[
\pi_{t+1}(z)=\pi_t(z)s_t(z),\qquad
s_t(z)=\int q(x\mid z)r_t(x)\,dx,
\]
with the density identity understood almost everywhere. In particular,
\[
\int\pi_t(z)s_t(z)\,dz
=\int m_t(x)r_t(x)\,dx=1.
\]
Hence \(s_t<\infty\) for \(\pi_t\)-almost every \(z\), and therefore for \(\pi^\star\)-almost every \(z\).

Under the joint probability law \(\pi^\star(z)q(x\mid z)\), the observation marginal is \(m^\star\), and \(r_t(X)>0\) almost surely. It follows that \(s_t(z)>0\) for \(\pi^\star\)-almost every \(z\). Consequently \(\pi^\star\ll\pi_{t+1}\), and all prior log ratios used below are finite almost surely under \(\pi^\star\).

### Step 2: Integrability and prior-KL descent

Since \(A_t<\infty\), the integrability fact above implies
\[
\int m^\star(x)|\log r_t(x)|\,dx<\infty.
\]
Values of the logarithm on null sets are irrelevant. Therefore
\[
g_t(z)=\int q(x\mid z)\log r_t(x)\,dx
\]
is finite for \(\pi^\star\)-almost every \(z\), is integrable under \(\pi^\star\), and satisfies
\[
\int\pi^\star(z)g_t(z)\,dz=A_t.
\]
Conditional Jensen gives
\[
\log s_t(z)\ge g_t(z)
\]
for \(\pi^\star\)-almost every \(z\). In particular, \((\log s_t)^-\le g_t^-\) is integrable under \(\pi^\star\).

To justify KL subtraction without assuming the desired finiteness conclusion, set
\[
h_t=\log\frac{\pi^\star}{\pi_t},\qquad
k_t=\log\frac{\pi^\star}{\pi_{t+1}}.
\]
The first is integrable because \(D_t<\infty\). The multiplicative identity gives \(k_t=h_t-\log s_t\) almost surely under \(\pi^\star\), so
\[
k_t^+\le h_t^++(\log s_t)^-.
\]
The right-hand side is integrable. Moreover, \(\int\pi^\star k_t^-\le1/e\), because \(\pi_{t+1}\) is a probability density and \(\pi^\star\ll\pi_{t+1}\). Thus \(k_t\) is integrable and \(D_{t+1}<\infty\). It also follows that \(\log s_t=h_t-k_t\) is integrable.

We may now subtract the finite KL divergences and integrate Jensen's inequality:
\[
\begin{aligned}
D_t-D_{t+1}
&=\int\pi^\star(z)\log\frac{\pi_{t+1}(z)}{\pi_t(z)}\,dz\\
&=\int\pi^\star(z)\log s_t(z)\,dz\\
&\ge\int\pi^\star(z)\int q(x\mid z)\log\frac{m^\star(x)}{m_t(x)}\,dx\,dz\\
&=\int m^\star(x)\log\frac{m^\star(x)}{m_t(x)}\,dx=A_t.
\end{aligned}
\]
Therefore
\[
D_{t+1}\le D_t-A_t.\tag{1}
\]
This argument also closes the induction establishing well-defined updates and finite prior KL at every finite time.

### Step 3: Identifiability gives contraction

The strong prior-identifiability assumption applies to the pair \((\pi^\star,\pi_t)\), since both are prior densities in the stated model. It gives
\[
D_t\le\lambda^{-1}A_t,
\]
so \(A_t\ge\lambda D_t\). Combining this with (1),
\[
D_{t+1}\le(1-\lambda)D_t.
\]

### Step 4: Iteration and boundary cases

Induction yields
\[
D_t\le(1-\lambda)^tD_0\qquad(t\ge0).
\]
At \(t=0\), the right-hand side is \(D_0\) under the stated integer-power convention. If \(\lambda=1\), the recurrence gives \(D_1=0\) and then \(D_t=0\) for every \(t\ge1\). If \(D_0=0\), the same recurrence gives zero at every time. Thus no endpoint or zero-divergence case is excluded.

### Step 5: The marginal bound

Data processing for the same simulator kernel gives, for every \(t\ge0\),
\[
A_t=\mathrm{KL}(m^\star\|m_t)
\le\mathrm{KL}(\pi^\star\|\pi_t)=D_t.
\]
Combining this with Step 4 proves
\[
\mathrm{KL}(m^\star\|m_t)
\le(1-\lambda)^t\mathrm{KL}(\pi^\star\|\pi_0),
\]
as required.

## Dependency Closure

The population-prior identity associated with the setup needs no optimization argument: under realizability, averaging the posterior under \(m^\star\) is marginalization of the joint law \(\pi^\star(z)q(x\mid z)\), and hence returns \(\pi^\star\). The logarithmic-score citation in the attached source material is not needed for this identity or either target bound. No finiteness of a separate expected log likelihood or entropy is assumed. The standard data-processing result used above has been stated, and its common-kernel and pushforward hypotheses have been verified. All theorem-critical obligations are closed.
