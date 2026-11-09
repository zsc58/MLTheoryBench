# Problem

## Setup

Let \(\mathcal X\) be an input space. For each input \(x\), let \(\mathcal C_x\) be the canonical candidate universe, and let \(c_x\) map raw answers (including the true answer) to canonical classes, respecting semantic equivalence. A black-box agent with arbitrary parameter \(\theta\) produces independent responses from an arbitrary kernel \(Q_\theta(\cdot\mid x)\). Using a fixed integer batch size \(m\ge1\), canonicalize the responses and rank the resulting classes by empirical frequency, breaking frequency ties uniformly at random; denote the resulting ranked list by \(R_x\).

For finite \(M\ge1\), let \(S_M(x)\) be the top-\(M\) classes in \(R_x\) (or all available classes if fewer than \(M\) exist), and define \(S_{+\infty}(x)=\mathcal C_x\). For a true answer \(y\), define \(s_{R_x}(x,y)\) as the position of \(c_x(y)\) in \(R_x\), or \(+\infty\) if absent.

Let \((X_i,Y_i)_{i=1}^{n+1}\) be exchangeable calibration/test examples, with independent agent-sampling and tie-breaking randomness across examples. For \(i\le n\), write \(T_i=s_{R_{X_i}}(X_i,Y_i)\), let \(T_{(k)}\) be the \(k\)-th smallest calibration score, and set
\[
k=\left\lceil (n+1)(1-\alpha)\right\rceil,\qquad
M^*=\begin{cases}T_{(k)},&k\le n,\\+\infty,&k=n+1.\end{cases}
\]
The test prediction set is \(S_{M^*}(X_{n+1})\).

## Task

Prove that for every \(\alpha\in(0,1)\), every agent parameter \(\theta\), every black-box output kernel \(Q_\theta\), and every exchangeable law of the examples,
\[
\Pr_\theta\!\left\{c_{X_{n+1}}(Y_{n+1})\in S_{M^*}(X_{n+1})\right\}\ge 1-\alpha.
\]
When \(k\le n\) and the \(n+1\) scores are almost surely tie-free, also prove
\[
\Pr_\theta\!\left\{c_{X_{n+1}}(Y_{n+1})\in S_{M^*}(X_{n+1})\right\}=\frac{k}{n+1}\le 1-\alpha+\frac1{n+1}.
\]
Conclude that the lower-coverage guarantee is uniform over arbitrary systematic agent bias and output distributions.
