# Reference Proof

## Proof Structure

Condition posterior inference on the known realized coordinate-selection matrix. Derive the exact Gaussian-mixture posterior, prove simultaneous concentration of the observed mean separations and Gaussian noise cross-terms, and obtain the score gap. Finally, use posterior component-weight ratios to bound nonbest-component mass and transfer that bound to total variation.

## Standard Independent Background

We use the sampling-without-replacement Hoeffding inequality stated in the source: if fixed numbers \(b_1,\ldots,b_n\) belong to \([a,b]\), and \(\Omega\) is a uniform subset of size \(1\le m\le n\), then, for \(t>0\),
\[
\Pr\left(\left|\frac1m\sum_{i\in\Omega}b_i-\frac1n\sum_{i=1}^n b_i\right|\ge t\right)
\le 2\exp\left(-\frac{2mt^2}{(b-a)^2}\right).
\]
This is standard independent background, not a paper-specific theorem. Its application below uses a fixed population in \([0,4]\) and exactly the uniform sampling scheme in the task. When \(m=n\), the sample mean equals the population mean deterministically, so the inequality also holds at that endpoint.

We also use elementary properties of jointly Gaussian vectors: linear transformations are Gaussian, and jointly Gaussian blocks with zero cross-covariance are independent. The latter follows from factorization of their joint Gaussian characteristic function. The conditional Gaussian formula needed here is derived below rather than assumed as an unexpanded paper-specific result.

## Complete Proof

Write \(\kappa^2=\sigma^2+\tau^2\). Since \(A=P_\Omega\) selects distinct coordinates, \(AA^T=I_m\) and \(\Sigma=\kappa^2I_m\). Throughout the posterior calculation, fix a realized \(A\); all posterior probabilities condition on this \(A\) as well as on the observation.

### 1. Gaussian posterior decomposition

Under the Bayesian model, conditional on \(J=j\) and \(A\), the vector \((X,Y)\) is jointly Gaussian with mean \((\mu_j,A\mu_j)\) and covariance
\[
\begin{pmatrix}
\tau^2I_n&\tau^2A^T\\
\tau^2A&\Sigma
\end{pmatrix}.
\]
In particular, \(Y\mid(J=j,A)\sim N(A\mu_j,\Sigma)\).

Set \(B=\tau^2A^T\Sigma^{-1}\), and define
\[
R=X-\mu_j-B(Y-A\mu_j).
\]
Its cross-covariance with \(Y\) is \(\tau^2A^T-B\Sigma=0\). Hence \(R\) and \(Y\) are independent, conditional on \(J=j,A\), and
\[
\operatorname{Cov}(R)=\tau^2I_n-\tau^4A^T\Sigma^{-1}A=V.
\]
It follows that
\[
X\mid(Y=y,J=j,A)\sim N(m_j(y),V),
\qquad
m_j(y)=\mu_j+\tau^2A^T\Sigma^{-1}(y-A\mu_j).
\]
The covariance is positive definite: on selected coordinates its diagonal entries are \(\tau^2\sigma^2/\kappa^2>0\), and on unselected coordinates they are \(\tau^2>0\).

The component likelihood is
\[
L_j(y)=(2\pi)^{-m/2}(\det\Sigma)^{-1/2}e^{-q_j(y)}.
\]
All these likelihoods are strictly positive. Bayes' rule therefore defines, for every \(y\in\mathbb R^m\),
\[
p_j(y):=\Pr(J=j\mid y)
=\frac{w_jL_j(y)}{\sum_{i=1}^M w_iL_i(y)},
\qquad
\pi(\cdot\mid y)=\sum_{j=1}^M p_j(y)N(m_j(y),V).
\]
Here and below the task's shorthand \(\mid y\) includes conditioning on \(A\). The common likelihood normalization cancels, giving
\[
\frac{p_j(y)}{p_{j_0}(y)}
=\frac{w_j}{w_{j_0}}\exp\bigl(-(q_j(y)-q_{j_0}(y))\bigr).
\]
This calculation concerns the Bayesian mixture model. It does not treat the fixed true label \(j_0\) in the data-generating experiment as a posterior random label.

### 2. Random-measurement score gap

Now use the task's data-generating experiment. Fix \(j\ne j_0\), and put
\[
d_j=\mu_{j_0}-\mu_j,\qquad v_j=Ad_j,
\qquad \eta=A\xi+\varepsilon.
\]
The deterministic population values \(d_{j,i}^2\) belong to \([0,4]\), and their population mean is at least \(\Delta\). The stated sampling-without-replacement inequality, with \(t=\Delta/2\), yields
\[
\Pr\{\|v_j\|_2^2/m<\Delta/2\}
\le 2\exp(-m\Delta^2/32).
\]
Indeed, the event on the left requires a deviation of more than \(\Delta/2\) below the population mean.

By independence of the two noises and the mask, conditional on \(A\),
\[
\eta\sim N(0,\kappa^2I_m).
\]
Consequently,
\[
Z_j:=\frac{2}{m}\langle\eta,v_j\rangle
\]
is a centered Gaussian with conditional variance
\[
s_j^2=\frac{4\kappa^2\|v_j\|_2^2}{m^2}
\le\frac{16\kappa^2}{m},
\]
since \(\|v_j\|_2^2\le4m\). If \(v_j=0\), then \(Z_j=0\) deterministically. Otherwise, the Gaussian moment-generating function and Markov's inequality give, for \(a>0\),
\[
\Pr(Z_j\ge a\mid A)
\le\inf_{t>0}\exp(-ta+t^2s_j^2/2)
=\exp(-a^2/(2s_j^2)).
\]
Apply the same argument to \(-Z_j\). Including the zero-variance case, this proves
\[
\Pr(|Z_j|>a\mid A)
\le2\exp\left(-\frac{ma^2}{32\kappa^2}\right).
\]
Taking \(a=\Delta/4\) gives
\[
\Pr\{|2\langle\eta,v_j\rangle|/m>\Delta/4\mid A\}
\le2\exp\left(-\frac{m\Delta^2}{512\kappa^2}\right).
\]
This bound is uniform in \(A\), so averaging over \(A\) gives the same unconditional bound.

A union bound over the \(M-1\) competitors and the two types of failure shows that, with probability at least
\[
1-2(M-1)e^{-m\Delta^2/32}
-2(M-1)e^{-m\Delta^2/(512\kappa^2)},
\]
all competitors satisfy
\[
\frac{\|v_j\|_2^2}{m}\ge\frac\Delta2,
\qquad
\frac{|2\langle\eta,v_j\rangle|}{m}\le\frac\Delta4.
\]
No independence between different competitors or between these two types of events is required.

For \(y=Y^*=A\mu_{j_0}+\eta\), expansion and cancellation of \(\|\eta\|_2^2\) give
\[
q_j(y)-q_{j_0}(y)
=\frac{\|v_j\|_2^2+2\langle\eta,v_j\rangle}{2\kappa^2}
\ge\frac{m\Delta}{8\kappa^2}.
\]
The lower bound is strictly positive. Thus \(j_0\) is the unique score minimizer, and
\[
g(y)=\min_{j\ne j_0}\frac{q_j(y)-q_{j_0}(y)}m
\ge\bar\delta:=\frac\Delta{8\kappa^2}.
\]
If the advertised probability lower bound is nonpositive, the same union-bound statement remains valid; the theorem does not require that bound to be informative for every parameter choice.

### 3. Posterior selection

Fix any realized \(A\) and any observation \(y\) with unique minimizer \(j_0\) and \(g(y)\ge\bar\delta\). For every \(j\ne j_0\),
\[
q_j(y)-q_{j_0}(y)\ge m\bar\delta,
\qquad
\frac{p_j(y)}{p_{j_0}(y)}\le Ce^{-m\bar\delta}.
\]
Since \(p_{j_0}(y)\le1\),
\[
\Pr(J\ne j_0\mid y)
=p_{j_0}(y)\sum_{j\ne j_0}\frac{p_j(y)}{p_{j_0}(y)}
\le C(M-1)e^{-m\bar\delta}
\le CMe^{-m\bar\delta}.
\]
The argument also applies when \(C=1\).

### 4. Total-variation collapse

Write \(Q_j=N(m_j(y),V)\). For every Borel set \(B\subseteq\mathbb R^n\),
\[
\pi(B\mid y)-Q_{j_0}(B)
=\sum_{j\ne j_0}p_j(y)\bigl(Q_j(B)-Q_{j_0}(B)\bigr).
\]
Each difference in parentheses has absolute value at most one. Taking absolute values and then the supremum over \(B\) proves
\[
\|\pi(\cdot\mid y)-N(m_{j_0}(y),V)\|_{\rm TV}
\le\sum_{j\ne j_0}p_j(y)
\le CMe^{-m\bar\delta}.
\]
This deterministic implication holds for every observation with the prescribed gap, not merely almost surely on the high-probability event. Together with the preceding concentration estimate it proves every conclusion.

## Source-Repair Accounting

The already-recorded repair for theory_007 is retained: inserting \(a=\Delta/4\) into the source's cross-term bound produces the denominator \(512(\sigma^2+\tau^2)\). This proof establishes the frozen repaired probability guarantee. No additional source repair or unclosed paper-specific dependency is used.
