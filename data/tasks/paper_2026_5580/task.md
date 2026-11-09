# Problem

## Setup

Fix positive integers \(T\) and \(n\), and a nonempty closed convex set \(\mathcal X\subset\mathbb R^n\). Let \(\mathbb B_2^n=\{x\in\mathbb R^n:\|x\|_2\le1\}\). Suppose that finite constants \(0<r<R\) and \(D>0\) satisfy
\[
r\mathbb B_2^n\subseteq\mathcal X\subseteq R\mathbb B_2^n,
\qquad
\sup_{x,y\in\mathcal X}\|x-y\|_2\le D.
\]
Before play begins, an adversary fixes the entire sequence of differentiable convex losses \(f_t:\mathcal X\to\mathbb R\) and integer delays
\[
\tau_t\in\{0,1,\ldots,T-t\},\qquad 1\le t\le T,
\]
independently of the learner's randomization. These sequences are not revealed in advance. For known finite constants \(G,M>0\), assume
\[
|f_t(x)|\le M,
\qquad
\|\nabla f_t(x)\|_2\le G
\quad(x\in\mathcal X).
\]

The learner maintains an initially empty set of tracked rounds, of size at most an integer capacity \(m\) at every time. At round \(t\):

1. Using its own randomization and information received through the end of round \(t-1\), it chooses \(x_t\in\mathcal X\) and incurs the initially unobserved loss \(f_t(x_t)\).
2. It may remove tracked indices, irrevocably discarding their pending feedback, and may then add the current index \(t\) if capacity permits. It may not add earlier untracked or removed indices.
3. At the end of the round, for every \(s\) with \(s+\tau_s=t\), it receives \((s,f_s(x_s))\) if \(s\) is tracked, and otherwise receives only an indexed acknowledgment that the delay for \(s\) has expired. Any completed tracked index is removed.

No other loss or individual-delay information is available. In particular, zero-delay feedback arrives only after the current prediction and tracking decision.

Define the pending set and maximum backlog by
\[
A_t=\{s<t:t\le s+\tau_s\},
\qquad
b=\max_{1\le t\le T}|A_t|.
\]
The learner is given \(T,n,\mathcal X,r,R,D,G,M,m\) and the value \(b\), but not the individual delays in advance. Assume
\[
m\ge\log T+1,
\]
where \(\log\) is the natural logarithm. For \(u\in\mathcal X\), define
\[
\operatorname{Reg}_T(u)=\sum_{t=1}^T\bigl(f_t(x_t)-f_t(u)\bigr),
\qquad
\rho=\frac{M}{Gr}.
\]

## Task

Prove that in each of the following regimes there is a randomized capacity-feasible strategy, depending only on the stated available information and known parameters, that satisfies the indicated upper bound for every admissible fixed loss-and-delay sequence and every fixed comparator \(u\in\mathcal X\). Expectations are over the learner's randomization. The constants \(C_{\mathrm{cv}},C_{\mathrm{sc}}>0\) must be universal.

For arbitrary convex losses, prove
\[
\mathbb E\operatorname{Reg}_T(u)
\le C_{\mathrm{cv}}GD\left[
\sqrt{Tb}
+T^{3/4}\left(1+\frac bm\right)^{1/4}\sqrt{\rho n}
\right].
\]

If, additionally, a known \(\lambda>0\) satisfies
\[
f_t(y)\ge f_t(x)+\langle\nabla f_t(x),y-x\rangle
 +\frac\lambda2\|y-x\|_2^2
\qquad(x,y\in\mathcal X,
\ 1\le t\le T),
\]
prove that a strategy for this regime satisfies
\[
\mathbb E\operatorname{Reg}_T(u)
\le C_{\mathrm{sc}}\frac{G^2}{\lambda}\left[
 b\log(eT)
 +(T^2\log(eT))^{1/3}
 \left(1+\frac bm\right)^{1/3}(\rho n)^{2/3}
\right].
\]
