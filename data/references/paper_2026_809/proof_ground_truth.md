# Reference Proof

## Proof Structure

We prove the deterministic lattice obstruction, then almost-sure hitting for positive Gaussian perturbations, and finally the two finite-horizon extreme-noise limits under the deterministic margin condition.

## Probability Tools and Their Hypotheses

Use the natural filtration \(\mathcal F_n=\sigma(\xi_1,\ldots,\xi_n)\). The initial state is fixed, and the update is a Borel measurable function of the current state and the next innovation. Thus the process is adapted and is a time-homogeneous Markov chain. At an almost-surely finite stopping time \(\rho\), the future innovations are iid standard Gaussians independent of \(\mathcal F_\rho\), and the future chain has the law of the same recursion started at \(X_\rho\). This discrete-time strong Markov statement follows by partitioning over \(\{\rho=n\}\in\mathcal F_n\) and using independence of future innovations at each deterministic time.

We also use Kolmogorov's maximal inequality: for independent mean-zero random variables \(Y_1,\ldots,Y_N\) with finite variances and \(a>0\),
\[
\mathbb P\left(\max_{1\le k\le N}\left|\sum_{j=1}^kY_j\right|\ge a\right)
\le \frac{\sum_{j=1}^N\operatorname{Var}(Y_j)}{a^2}.
\]
Here the innovations are independent, centered, and each has variance one, so all its hypotheses hold.

## Complete Proof

For a fixed noise magnitude, suppress the superscript and write
\[
X_{n+1}=X_n-\alpha\bigl(\operatorname{sgn}(X_n)+\sigma\xi_{n+1}\bigr),
\qquad
T=\inf\{n\ge0:|X_n|\le\varepsilon\}.
\]
If \(|x_0|\le\varepsilon\), then \(T=0\). This already settles the positive-noise hitting claim for such initial states.

### 1. Deterministic obstruction

For \(\sigma=0\), every increment belongs to \(\{-\alpha,0,\alpha\}\). Induction gives \(X_n\in x_0+\alpha\mathbb Z\) for every \(n\). If that lattice is disjoint from \([-\varepsilon,\varepsilon]\), then \(T=\infty\).

### 2. Return to a compact interval for positive noise

Fix \(\sigma>0\). All finite-time states are integrable, since
\[
|X_n|\le |x_0|+n\alpha+\alpha\sigma\sum_{j=1}^n|\xi_j|
\]
and Gaussian innovations have finite absolute first moment.

For a positive starting state \(x\), set \(D=\alpha(1+\sigma\xi_1)\). The elementary identity
\[
|x-D|=x-D+2(D-x)_+
\]
yields
\[
\mathbb E_x|X_1|=x-\alpha+2\mathbb E(D-x)_+.
\]
For \(x\ge0\), \(0\le(D-x)_+\le D_+\), and \(\mathbb E D_+<\infty\). Dominated convergence therefore gives \(\mathbb E(D-x)_+\to0\) as \(x\to\infty\). The expectation is nonincreasing in \(x\), so choose \(R>\max\{\varepsilon,1\}\) sufficiently large that
\[
2\mathbb E(D-x)_+\le\alpha/2\qquad(x\ge R).
\]
By symmetry of the Gaussian innovations, the same bound applies to negative starting states after replacing \(x\) by \(|x|\). Consequently, with \(c=\alpha/2\),
\[
\mathbb E_x|X_1|\le |x|-c\qquad(|x|>R).
\]
Here \(R\) may depend on the fixed \(\alpha,\sigma,\varepsilon\); no uniformity in \(\sigma\) is asserted or needed.

Let
\[
\tau=\inf\{n\ge0:|X_n|\le R\},
\qquad
Z_n=|X_{n\wedge\tau}|+c(n\wedge\tau).
\]
Each \(Z_n\) is integrable. On \(\{\tau\le n\}\) it remains unchanged; on \(\{\tau>n\}\), conditional independence of the next innovation and the drift inequality give
\[
\mathbb E[Z_{n+1}-Z_n\mid\mathcal F_n]
=\mathbf1_{\{\tau>n\}}\left(\mathbb E[|X_{n+1}|-|X_n|\mid\mathcal F_n]+c\right)\le0.
\]
Thus \(\mathbb E Z_n\le |x_0|\), and hence
\[
c\,\mathbb E(n\wedge\tau)\le |x_0|.
\]
Monotone convergence gives \(\mathbb E\tau\le |x_0|/c<\infty\), so \(\tau<\infty\) almost surely. This argument holds for every fixed real starting state, which will allow its use after stopping times.

### 3. Uniform hitting attempts and their iteration

Let \(K=[-R,R]\) and \(s=\alpha\sigma>0\). Starting from \(x\in K\), the next state has Gaussian mean
\[
m(x)=x-\alpha\operatorname{sgn}(x)
\]
and variance \(s^2\). Since \(|m(x)|\le R+\alpha\), its density on \([-\varepsilon,\varepsilon]\) is bounded below by
\[
\frac1{s\sqrt{2\pi}}\exp\left(-\frac{(\varepsilon+R+\alpha)^2}{2s^2}\right).
\]
Therefore, uniformly for \(x\in K\),
\[
\mathbb P_x(|X_1|\le\varepsilon)\ge p,
\qquad
p:=\frac{2\varepsilon}{s\sqrt{2\pi}}\exp\left(-\frac{(\varepsilon+R+\alpha)^2}{2s^2}\right)>0.
\]
Also \(p<1\), since this lower bound is at most a Gaussian interval probability, which is strictly less than one. No continuity in the state variable is needed; in particular, the sign discontinuity at zero causes no difficulty.

Define attempt start times on the full, unstopped chain by
\[
\tau_0=\inf\{n\ge0:X_n\in K\},
\qquad
\tau_{k+1}=\inf\{n\ge\tau_k+1:X_n\in K\}.
\]
These are stopping times. The return argument gives \(\tau_0<\infty\) almost surely. Inductively, if \(\tau_k\) is finite, apply strong Markov at \(\tau_k+1\) and use almost-sure return from every real starting state to conclude that \(\tau_{k+1}<\infty\) almost surely.

Let
\[
A_k=\{|X_{\tau_k+1}|\le\varepsilon\},
\qquad
B_m=\bigcap_{k=0}^{m-1}A_k^c,
\quad B_0=\Omega.
\]
Strong Markov and the uniform bound give
\[
\mathbb P(A_k\mid\mathcal F_{\tau_k})\ge p.
\]
Because \(\tau_{k+1}\ge\tau_k+1\), the preceding attempt outcomes are known at \(\tau_m\), so \(B_m\in\mathcal F_{\tau_m}\). The tower property therefore implies
\[
\mathbb P(B_{m+1})
=\mathbb E\left[\mathbf1_{B_m}\mathbb P(A_m^c\mid\mathcal F_{\tau_m})\right]
\le(1-p)\mathbb P(B_m).
\]
Induction gives \(\mathbb P(B_m)\le(1-p)^m\). The event \(\{T=\infty\}\) is contained in every \(B_m\), so its probability is zero. Thus \(T<\infty\) almost surely for every \(\sigma>0\). The attempts need not be mutually independent.

### 4. Small-noise finite-horizon limit

Assume that \(|U_n|\ge\varepsilon+\Delta\) for every \(n\ge0\), where \(\Delta>0\), and fix an integer \(N\ge1\). The parameters \(\alpha,\varepsilon,x_0,\Delta,N\) remain fixed as the noise magnitude varies. Set \(S_0=0\) and \(S_k=\sum_{j=1}^k\xi_j\), and define, for \(\sigma>0\),
\[
E_\sigma=\left\{\max_{1\le k\le N}\alpha\sigma|S_k|<\Delta\right\}.
\]
On this event, induction proves both sign agreement and
\[
X_k^{(\sigma)}=U_k-\alpha\sigma S_k\qquad(0\le k\le N).
\]
At time zero these statements hold because the initial states coincide and \(|U_0|>0\). If they hold through time \(k-1\), the common sign in the update gives the displayed identity at time \(k\). Its error is less than \(\Delta\), whereas \(|U_k|\ge\varepsilon+\Delta\), so \(|X_k^{(\sigma)}|>\varepsilon\) and its sign equals that of \(U_k\). This completes the induction.

Hence \(T_\varepsilon^{(\sigma)}>N\) on \(E_\sigma\). Kolmogorov's maximal inequality, with the hypotheses verified above, gives
\[
\mathbb P(T_\varepsilon^{(\sigma)}\le N)
\le\mathbb P\left(\max_{k\le N}|S_k|\ge\frac{\Delta}{\alpha\sigma}\right)
\le\frac{N\alpha^2\sigma^2}{\Delta^2}\longrightarrow0.
\]
Therefore \(\mathbb P(T_\varepsilon^{(\sigma)}>N)\to1\) as \(\sigma\downarrow0\).

### 5. Large-noise finite-horizon limit

For \(\sigma>0\), conditionally on \(\mathcal F_{k-1}\), the state \(X_k^{(\sigma)}\) is Gaussian with variance \(\alpha^2\sigma^2\) and mean \(X_{k-1}^{(\sigma)}-\alpha\operatorname{sgn}(X_{k-1}^{(\sigma)})\). Its density is everywhere bounded by \((\alpha\sigma\sqrt{2\pi})^{-1}\), independently of the mean. Thus
\[
\mathbb P(|X_k^{(\sigma)}|\le\varepsilon\mid\mathcal F_{k-1})
\le\frac{2\varepsilon}{\alpha\sigma\sqrt{2\pi}}.
\]
Taking expectations preserves this bound. The margin assumption at time zero ensures \(|x_0|>\varepsilon\), so a hit by time \(N\) must occur at one of times \(1,\ldots,N\). A union bound yields
\[
\mathbb P(T_\varepsilon^{(\sigma)}\le N)
\le\frac{2N\varepsilon}{\alpha\sigma\sqrt{2\pi}}\longrightarrow0
\qquad(\sigma\to\infty).
\]
Therefore \(\mathbb P(T_\varepsilon^{(\sigma)}>N)\to1\) as \(\sigma\to\infty\).

All four claims follow under precisely the public assumptions.
