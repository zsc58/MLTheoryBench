# Problem

## Setup

Let \(d,N,L\in\mathbb N^+\) and \(1\leq p<\infty\). For a measurable set \(Q\subset\mathbb R^d\), let \(L^p(Q)\) be the space of real-valued measurable functions with finite norm
\[
 \|f\|_{L^p(Q)}=\left(\int_Q|f(x)|^p\,dx\right)^{1/p},
\]
where integration is with respect to Lebesgue measure and functions are identified almost everywhere.

For each dimension \(n\geq2\), define the coordinatewise mixed activation
\[
 \sigma_n(z_1,\ldots,z_n)=(\sin z_1,\sin z_2,\max\{z_3,0\},\ldots,\max\{z_n,0\}).
\]
For \(n=1\), set \(\sigma_1(z)=\sin z\). Write \(\operatorname{Aff}_{\leq m}\) for the class of all real affine maps whose input and output dimensions are positive integers at most \(m\).

For \(f\in L^p([0,1]^d)\) and \(t\geq0\), define
\[
 \mu_{f,p}(t)=\sup_{\|h\|_2\leq t}
 \|f(\cdot+h)-f(\cdot)\|_{L^p(E_h)},\qquad
 E_h=\{x\in[0,1]^d:x+h\in[0,1]^d\}.
\]

## Task

Prove that for every \(f\in L^p([0,1]^d)\), there exist affine maps
\[
 B_i\in\operatorname{Aff}_{\leq 2dN+d+2}\quad(-1\leq i\leq L),
 \qquad
 C_j\in\operatorname{Aff}_{\leq 2dN+d+2}\quad(0\leq j\leq L),
\]
with compatible dimensions, with \(B_{-1}\) having domain \(\mathbb R^d\) and every \(C_j\) scalar-valued, such that, for every \(0\leq\ell\leq L\), the prefix readout
\[
 G_\ell=
 \sum_{j=0}^\ell C_j\circ(\sigma\circ B_j)\circ(\sigma\circ B_{j-1})\circ\cdots\circ(\sigma\circ B_{-1})
\]
satisfies
\[
 \|f-G_\ell\|_{L^p([0,1]^d)}
 \leq (2d+1)\mu_{f,p}(N^{-\ell}).
\]
Here each occurrence of \(\sigma\) has the dimension determined by the preceding affine map.
