# Reference Proof

## Proof Structure

Rewrite Chernoff Information as the supremum of a powered density-ratio objective. Prove convergence of the empirical powered objective at each fixed exponent by separating estimation error from sampling error. Use boundedness and pointwise consistency to control the former in training mean, and independent evaluation to control the latter conditionally on training. A common Lipschitz bound and a finite grid yield uniform convergence. A positive lower bound permits passage through the logarithm, and an elementary inequality transfers uniform convergence to convergence of optimized values.

## Complete Proof

Write \(C_\star=C(P_0,P_1)\), distinguishing the target value from the upper clipping bound \(C\). Let \(\mu\) denote the common dominating measure in the problem. Common support gives
\[
\mathbb E_{P_0}r(X)=\int p_1\,d\mu=1,
\qquad
\int p_0^{1-u}p_1^u\,d\mu=\mathbb E_{P_0}[r(X)^u]
\quad(0<u<1).
\]
Define
\[
h(u)=\mathbb E_{P_0}[r(X)^u],\qquad f(u)=-\log h(u),
\]
and
\[
h_n(u)=\frac1n\sum_{i=1}^n r_n(X_i)^u,\qquad f_n(u)=-\log h_n(u).
\]
Put
\[
a=\min\{1,c\}>0,\qquad b=\max\{1,C\}<\infty.
\]
For every \(t\in[c,C]\) and \(u\in[0,1]\), \(a\le t^u\le b\). Consequently, \(h_n(u)\) and \(h(u)\) lie in \([a,b]\), and all logarithms are finite.

### 1. Population objective and endpoints

Bounded convergence in the deterministic integration variable shows that \(h\), and hence \(f\), is continuous on \([0,1]\). Moreover,
\[
h(0)=1,\qquad h(1)=\mathbb E_{P_0}r(X)=1.
\]
For \(0<u<1\), concavity of \(t\mapsto t^u\) gives \(h(u)\le(\mathbb E r)^u=1\). Thus \(f\) has endpoint values zero and is nonnegative in the interior. In particular,
\[
C_\star=\sup_{0<u<1}f(u)=\sup_{u\in[0,1]}f(u).
\]
Equivalently, equality of these suprema follows directly from continuity and density of \((0,1)\) in \([0,1]\). No strict convexity or unique optimizer is required.

### 2. Fixed-exponent estimation error

Fix \(u\in[0,1]\). Let \(\mathcal T_n\) contain the training randomness determining \(r_n\), and define the random integral
\[
m_n(u)=\int r_n(x)^u\,dP_0(x).
\]
Here the integral is over \(x\), with the trained function held fixed.

For \(P_0\)-almost every \(x\), continuity of the power function gives
\(r_n(x)^u\to r(x)^u\) in training probability. Set
\(Z_n(x)=|r_n(x)^u-r(x)^u|\le2b\). For every \(\varepsilon>0\),
\[
\mathbb E_{\rm tr}Z_n(x)
\le\varepsilon+2b\,\mathbb P_{\rm tr}(Z_n(x)>\varepsilon).
\]
Taking the limit superior and then letting \(\varepsilon\downarrow0\) shows that \(\mathbb E_{\rm tr}Z_n(x)\to0\) for almost every \(x\). These deterministic expectations are bounded by \(2b\). Dominated convergence over the probability measure \(P_0\), together with Tonelli's theorem, therefore yields
\[
\mathbb E_{\rm tr}|m_n(u)-h(u)|
\le\int\mathbb E_{\rm tr}Z_n(x)\,dP_0(x)
\longrightarrow0.
\]
Markov's inequality implies \(m_n(u)-h(u)\to0\) in probability. This argument does not assert almost-sure convergence of the trained estimators or their integrals.

### 3. Fixed-exponent sampling error

Conditional on \(\mathcal T_n\), the evaluation points remain iid with law \(P_0\). Thus the summands defining \(h_n(u)\) are conditionally iid, have conditional mean \(m_n(u)\), and have conditional variance at most \(b^2\). For every \(\varepsilon>0\), conditional Chebyshev followed by averaging over training gives
\[
\mathbb P\bigl(|h_n(u)-m_n(u)|>\varepsilon\bigr)
\le\frac{b^2}{n\varepsilon^2}\longrightarrow0.
\]
Combining the two errors proves
\[
h_n(u)\longrightarrow h(u)
\quad\text{in probability for every fixed }u\in[0,1].
\]
The probability here includes both training and evaluation randomness. No independence across different sample sizes is needed.

### 4. Uniform convergence

For \(t\in[c,C]\) and \(u\in[0,1]\),
\[
|\partial_u t^u|=t^u|\log t|
\le L:=b\max\{|\log c|,|\log C|\}<\infty.
\]
The mean value theorem shows that every \(h_n\) is \(L\)-Lipschitz. Integrating the same bound shows that \(h\) is also \(L\)-Lipschitz.

Given \(\varepsilon>0\), choose \(\delta=\varepsilon/[4(1+L)]\) and a finite \(\delta\)-net \(G\subset[0,1]\). For every \(u\), select \(v\in G\) with \(|u-v|\le\delta\). Then
\[
|h_n(u)-h(u)|
\le |h_n(v)-h(v)|+2L\delta,
\]
so
\[
\sup_{u\in[0,1]}|h_n(u)-h(u)|
\le\max_{v\in G}|h_n(v)-h(v)|+\frac\varepsilon2.
\]
By fixed-exponent convergence and a finite union bound,
\[
\mathbb P\left(\max_{v\in G}|h_n(v)-h(v)|>\frac\varepsilon2\right)
\le\sum_{v\in G}\mathbb P\left(|h_n(v)-h(v)|>\frac\varepsilon2\right)
\longrightarrow0.
\]
Hence
\[
\sup_{u\in[0,1]}|h_n(u)-h(u)|\longrightarrow0
\quad\text{in probability}.
\]
This also covers \(L=0\).

### 5. Logarithms and optimized values

The function \(-\log\) is \(1/a\)-Lipschitz on \([a,b]\). Therefore
\[
\sup_{u\in[0,1]}|f_n(u)-f(u)|
\le\frac1a\sup_{u\in[0,1]}|h_n(u)-h(u)|
\longrightarrow0
\quad\text{in probability}.
\]
The functions involved are continuous in \(u\). Their suprema equal their suprema over the countable dense subset \(\mathbb Q\cap[0,1]\), so the optimized values and uniform errors are measurable random variables.

Finally, the definition of the estimator and Step 1 imply
\[
|\widehat C_n-C_\star|
=\left|\sup_{u\in[0,1]}f_n(u)-\sup_{u\in[0,1]}f(u)\right|
\le\sup_{u\in[0,1]}|f_n(u)-f(u)|
\longrightarrow0
\quad\text{in probability}.
\]
This proves the asserted consistency, including \(P_0=P_1\). No normalization of \(r_n\), unique optimizer, or optimizer convergence is needed.
