# Reference Proof

## Proof Structure

Differentiate the squared surrogate-gradient magnitude along the flow, use the two outside-ball hypotheses to obtain a scalar differential inequality, and combine that inequality with boundedness of the gradient on the closed ball to construct a finite forward-invariant attracting interval.

## Complete Proof

Because \(S\in C^2\), the chain rule gives
\[
\begin{aligned}
\dot G(t)
&=2\left\langle \nabla S(w_t),\nabla^2S(w_t)\dot w_t\right\rangle\\
&=-2\left\langle \nabla S(w_t),\nabla^2S(w_t)\nabla F(w_t)\right\rangle
  -2\lambda\left\langle \nabla S(w_t),\nabla^2S(w_t)\nabla S(w_t)\right\rangle.
\end{aligned}
\]
Whenever \(\|w_t\|>R\), the assumptions therefore imply
\[
\dot G(t)\le 2C\|\nabla S(w_t)\|-2\lambda\mu\|\nabla S(w_t)\|^2
=2C\sqrt{G(t)}-2\lambda\mu G(t).
\]
Set
\[
a=\frac{C}{\lambda\mu}.
\]
Continuity of \(\nabla S\) and compactness of the closed radius-\(R\) ball imply that
\[
K:=\max_{\|w\|\le R}\|\nabla S(w)\|^2<\infty.
\]
Choose any
\[
q>\max\{\sqrt K,a\},\qquad M=q^2.
\]
If \(G(t)\ge M\), then \(w_t\) cannot lie in the closed radius-\(R\) ball, since there \(G(t)\le K<M\). Thus the preceding differential inequality applies, and
\[
\dot G(t)
\le -2\lambda\mu\sqrt{G(t)}\bigl(\sqrt{G(t)}-a\bigr)
\le -\delta G(t),
\]
where
\[
\delta:=2\lambda\mu\left(1-\frac aq\right)>0.
\]
In particular, at every point with \(G=M\), one has \(\dot G\le-\delta M<0\). Consequently \([0,M]\) is forward invariant: an upward crossing of the level \(M\) would have a first crossing time at which the derivative could not be strictly negative.

It remains to prove entry. If \(G(0)\le M\), take \(T=0\). Otherwise, for as long as \(G(t)>M\), the inequality \(\dot G\le-\delta G\) yields
\[
G(t)\le G(0)e^{-\delta t}.
\]
Hence \(G\) must reach \([0,M]\) no later than
\[
T=\frac1\delta\log\frac{G(0)}M.
\]
Forward invariance then gives \(G(t)\le M\) for every \(t\ge T\). The constant \(M\) depends only on the fixed functions and the stated constants, not on the chosen trajectory, so \([0,M]\) is a bounded attracting region.
