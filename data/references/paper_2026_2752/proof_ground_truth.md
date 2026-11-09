# Reference Proof

## Proof Structure

For every competing support at symmetric-difference distance at least \(2\delta s\), derive a two-block Chernoff bound for its residual-loss gap. Union-bound these probabilities over all supports, then apply the combinatorial entropy estimates for sublinear and linear sparsity.

## Complete Proof

Fix an admissible dimension and the deterministic true signal. Let \(S^\star=\operatorname{supp}(\theta^\star)\). For another support \(S\) of size \(s\), write \(U=S^\star\setminus S\), \(V=S\setminus S^\star\), and \(m=|U|=|V|\). Thus \(|S\triangle S^\star|=2m\). Put \(d=\theta^\star-\theta\), where \(\theta\) is the binary vector supported on \(S\). For row \(i\), let \(W_i=X_i d\). Since \(d\) is deterministic and has \(2m\) entries of magnitude one, the \(W_i\) are independent \(N(0,2m)\) variables, independent of the noise. The residual-loss difference is
\[
\Delta(S)=\|Y-X\theta\|_2^2-\|Y-X\theta^\star\|_2^2
=\sum_{i=1}^n(W_i^2+2Z_iW_i).
\]

Consider a competing support with \(m\ge\delta s\), so \(m>0\). For \(0<\vartheta<1/(2\tau_2^2)\) and an observation with noise variance \(\tau_j^2\), centered Gaussian integration gives
\[
\mathbb E\bigl[e^{-2\vartheta Z_iW_i}\mid W_i\bigr]
=e^{2\vartheta^2\tau_j^2W_i^2}.
\]
Indeed, completing the square in the \(N(0,\tau_j^2)\) density gives \(\mathbb E e^{tZ_i}=e^{t^2\tau_j^2/2}\) for every real \(t\). Therefore
\[
\mathbb E e^{-\vartheta(W_i^2+2Z_iW_i)}
=\mathbb E e^{-a_jW_i^2},
\qquad a_j=\vartheta(1-2\vartheta\tau_j^2)>0.
\]
Using the \(N(0,2m)\) density and rescaling the Gaussian integral,
\[
\mathbb E e^{-a_jW_i^2}
=\frac{1}{\sqrt{4\pi m}}\int_{\mathbb R}
\exp\left[-\left(\frac{1}{4m}+a_j\right)w^2\right]dw
=(1+4ma_j)^{-1/2}.
\]
In particular, all these expectations are finite, and
\[
\mathbb E e^{-\vartheta(W_i^2+2Z_iW_i)}
=\left(1+4m\vartheta(1-2\vartheta\tau_j^2)\right)^{-1/2}.
\]

Choose \(\vartheta=1/(4\tau_2^2)\). This lies in the stated interval, and \(1-2\vartheta\tau_j^2>0\) for both blocks because \(0<\tau_1^2<\tau_2^2\). The high-quality and low-quality factors become respectively
\[
\left(1+\frac{m(2\tau_2^2-\tau_1^2)}{2\tau_2^4}\right)^{-1/2},
\qquad
\left(1+\frac{m}{2\tau_2^2}\right)^{-1/2}.
\]
Independence across observations allows multiplication of these factors. Since \(\Delta(S)\le0\) implies \(e^{-\vartheta\Delta(S)}\ge1\), Markov's inequality gives
\[
\Pr\{\Delta(S)\le0\}\le
\left(1+\frac{m(2\tau_2^2-\tau_1^2)}{2\tau_2^4}\right)^{-n_1/2}
\left(1+\frac{m}{2\tau_2^2}\right)^{-n_2/2}.
\]
Both factors are nonincreasing in \(m\). Hence, for \(m\ge\delta s\),
\[
\Pr\{\Delta(S)\le0\}\le
\left(1+\frac{\delta(2\tau_2^2-\tau_1^2)s}{2\tau_2^4}\right)^{-n_1/2}
\left(1+\frac{\delta s}{2\tau_2^2}\right)^{-n_2/2}.
\]
The first denominator is the already recorded local source correction. The calculation is valid for dimension-dependent positive variances and for an empty block, whose product contribution is one.

Let
\[
A=n_1\log\left(1+\frac{\delta(2\tau_2^2-\tau_1^2)s}{2\tau_2^4}\right)
+n_2\log\left(1+\frac{\delta s}{2\tau_2^2}\right).
\]
A union bound over competing supports, of which there are at most \(\binom ps\), yields
\[
\Pr\{\exists S:\ |S\triangle S^\star|\ge2\delta s,\ \Delta(S)\le0\}
\le \binom ps\,e^{-A/2}.
\]
If there are no such supports, the event on the left is empty and the same inequality holds. On its complement every bad support has strictly larger loss than the true support. Since the true signal belongs to the finite search class, every minimizer then has support error strictly less than \(2\delta s\). In particular this holds for the measurable estimator in the task.

For sublinear sparsity, \(\binom ps\le p^s/s!\), and
\[
\log(s!)=\sum_{k=1}^s\log k\ge\int_1^s\log x\,dx
=s\log s-s+1\ge s\log s-s.
\]
Consequently
\[
\log\binom ps\le s\log(p/s)+s=N_*/2+s.
\]
Under \(A\ge(1+\varepsilon)N_*\), the failure probability is at most
\[
\exp\left(-\frac{\varepsilon N_*}{2}+s\right)
=\exp\left[-\frac{N_*}{2}\left(\varepsilon-\frac{1}{\log(p/s)}\right)\right].
\]
Here \(\log(p/s)\to\infty\), so the coefficient is \(\varepsilon+o(1)\), and \(N_*=2s\log(p/s)\to\infty\).

For linear sparsity, \(s=\alpha p\) along dimensions for which this is an integer. The binomial theorem gives
\[
1=(\alpha+(1-\alpha))^p
\ge\binom ps\alpha^s(1-\alpha)^{p-s}.
\]
Taking logarithms yields the entropy bound
\[
\log\binom ps\le-s\log\alpha-(p-s)\log(1-\alpha)
=h(\alpha)p=N_*/2.
\]
Thus the failure probability is at most \(\exp(-\varepsilon N_*/2)\), which implies the requested form with an \(o(1)\) term equal to zero. Also \(h(\alpha)>0\), so \(N_*\to\infty\).

Combining these cases proves
\[
\Pr\left(\left|\operatorname{supp}(\widehat\theta)\triangle\operatorname{supp}(\theta^\star)\right|<2\delta s\right)
\ge1-\exp\left(-\frac{\varepsilon+o(1)}2N_*\right)\longrightarrow1.
\]
The bound holds for each deterministic true signal, with a remainder depending only on the sparsity sequence. It is not a simultaneous-in-signal probability assertion. The ambient ordering \(n_2>n_1\) is preserved in the task, although no step of this proof needs that ordering.
