# Problem

## Setup

Let \(n\ge 2\). Let \(w=(w_1,\ldots,w_n)\in\mathbb{R}^n\) satisfy \(w_i\ge0\) and \(\sum_i w_i=1\), with \(1-\sum_iw_i^2>0\). Let \(A\in\{0,1\}^{n\times n}\) be symmetric with \(A_{ii}=0\). Define the complete-network matrix \(C=\mathbf{1}\mathbf{1}^T-I\) and
\[
\Psi(w,A)=\frac{w^TAw}{1-\sum_iw_i^2}.
\]
For the connectivity statement assume \(L:=\sum_{i\ne j}A_{ij}\ge1\), and define
\[
\delta(A)=\frac{L}{n(n-1)},\quad
E_{\mathrm{link}}[w_iw_j]=\frac1L\sum_{i\ne j:A_{ij}=1}w_iw_j,
\quad
E_{\mathrm{all}}[w_iw_j]=\frac1{n(n-1)}\sum_{i\ne j}w_iw_j.
\]
Also consider any denominator function \(D(w)>0\) on every simplex vector having at least two positive components, and the associated ratio \(\Psi_D(w,M)=w^TMw/D(w)\).

## Task

Prove the following integrated theorem. First, \(\Psi(w,A)\) equals the weighted average of \(A_{ij}\) over ordered pairs, with pair weights proportional to \(w_iw_j\). Second, the condition \(\Psi_D(w,C)=1\) for every admissible simplex vector uniquely forces
\[
D(w)=w^TCw=1-\sum_iw_i^2.
\]
Third, for every admissible \(w\) and every such \(A\) with \(L\ge1\),
\[
\Psi(w,A)=\delta(A)\,\frac{E_{\mathrm{link}}[w_iw_j]}{E_{\mathrm{all}}[w_iw_j]}.
\]
