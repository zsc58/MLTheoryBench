# Problem

## Setup

For \(t\in\mathbb R\), let
\[
s(t)=\frac{1}{1+e^{-t}},\qquad \tau(t)=\tanh t,
\]
and define, for parameters \(a,b>0\),
\[
F_{a,b}(x)=s\bigl(b\,\tau(ax)\bigr),\qquad x\in\mathbb R.
\]
Let the hard threshold be \(H(x)=\mathbf 1\{x\ge 0\}\). Fix \(0<\varepsilon<1/2\) and put \(L=\log((1-\varepsilon)/\varepsilon)\).

## Task

Prove the following integrated claim. If
\[
b>L\quad\text{and}\quad a\ge \frac{1}{2\varepsilon}\log\frac{b+L}{b-L},
\]
then
\[
\sup_{x\ge\varepsilon}|1-F_{a,b}(x)|\le\varepsilon,
\qquad
\sup_{x\le-\varepsilon}|F_{a,b}(x)|\le\varepsilon.
\]
Moreover, for every \(a,b>0\),
\[
\lim_{|x|\to\infty}\frac{F'_{a,b}(x)}{e^{-2a|x|}}
=4ab\,s(b)\bigl(1-s(b)\bigr),
\qquad
F'_{a,b}(0)=\frac{ab}{4}.
\]
