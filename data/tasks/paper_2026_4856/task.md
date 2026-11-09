# Problem

## Setup

Let \(p,q,N\) be positive integers and \(T\ge1\). Here \(C_0([0,T];\mathbb R^d)\) denotes all continuous functions from \([0,T]\) to \(\mathbb R^d\); no value at time zero is prescribed. For vectors, write \(|z|_1=\sum_j|z_j|\) and \(|z|_2=(\sum_j|z_j|^2)^{1/2}\). Use the norms
\[
\|f\|_\infty=\sup_{t\in[0,T]}|f(t)|_1,
\qquad
\|f\|_{L^2}^2=\int_0^T|f(t)|_2^2\,dt.
\]
For a matrix, \(\|A\|_{\infty,\infty}=\max_{i,j}|A_{ij}|\); for a vector, \(\|b\|_\infty=\max_j|b_j|\).

Let \(K\subset C_0([0,T];\mathbb R^p)\) be compact, and let \(\mu\) be a Borel probability law with \(\mu(K)=1\). Suppose \(B_K\ge1\), \(L_K>0\), and
\[
|u_j(t)|\le B_K\qquad(u\in K,\ t\in[0,T],\ 1\le j\le p).
\]
There are continuous nondecreasing functions \(\phi_{K,j}:[0,\infty)\to[0,\infty)\), vanishing at zero, such that
\[
|u_j(t)-u_j(s)|\le\phi_{K,j}(|t-s|),
\qquad
\phi_K(r):=\sum_{j=1}^p\phi_{K,j}(r)=pL_Kr.
\]

Let \(\Phi:C_0([0,T];\mathbb R^p)\to C_0([0,T];\mathbb R^q)\) be uniformly continuous and causal: if two inputs agree on \([0,t]\), their outputs at \(t\) agree. Suppose a finite constant \(B_\Phi(K)\ge0\) satisfies
\[
|\Phi[u]_j(t)|\le B_\Phi(K)
\qquad(u\in K,\ t\in[0,T],\ 1\le j\le q).
\]
For each \(j\), assume every function \(\Phi[u]_j\) is temporally differentiable and
\[
\sup_{u\in C_0([0,T];\mathbb R^p)}\sup_{t\in[0,T]}
\left|\frac{d}{dt}\Phi[u]_j(t)\right|\le D_j<\infty,
\]
with one-sided derivatives at the endpoints. Let \(\phi_{\Phi,j}:[0,\infty)\to[0,\infty)\) be continuous nondecreasing functions vanishing at zero such that, for every pair of inputs in the full domain,
\[
\sup_t|\Phi[u]_j(t)-\Phi[v]_j(t)|
\le\phi_{\Phi,j}(\|u-v\|_\infty).
\]
Set \(\phi_\Phi=\sum_{j=1}^q\phi_{\Phi,j}\), so in particular
\[
\|\Phi[u]-\Phi[v]\|_\infty\le\phi_\Phi(\|u-v\|_\infty).
\]

Let \(M_0\) be a fixed positive integer and \(c_1,c_2>0\) be fixed constants. They may depend on the deterministic operator and input setup, but are held fixed as \(M,H,N\), and \(\delta\) vary. Take integers \(M>M_0\) and \(H\ge1\), and set \(h_\Pi=H+1\). Define
\[
\varepsilon_{\rm app}
=\phi_\Phi\!\left(c_1\frac{pL_KT(\ln M)^2}{M}\right)
+c_2\frac{qp^3M^5}{H^{1/[p(M+1)+1]}}.
\]

For an input \(u\), define \(x=\Phi_\Gamma[u]\), taking values in \(\mathbb R^{pM}\), by
\[
x''(t)=\Gamma(x(t),x'(t),u(t)),\qquad x(0)=x'(0)=0,
\]
and define
\[
F_{\Gamma,\Pi}[u](t)=\Pi(x(t),u(0),t).
\]
Here \(\Gamma\) has two affine layers with componentwise ReLU between them, and \(\Pi\) has \(h_\Pi\) affine layers with componentwise ReLU after each nonfinal layer. Their final layers are affine. Use widths
\[
w_{\Gamma,\rm in}=p(2M+1),\quad w_\Gamma=2pM,\quad w_{\Gamma,\rm out}=pM,
\]
\[
w_{\Pi,\rm in}=p(M+1)+1,\quad w_\Pi=q[p(M+1)+4],\quad w_{\Pi,\rm out}=q,
\]
where every hidden layer of \(\Pi\) has width \(w_\Pi\).

Fix finite nonnegative bounds \(B_W,B_b,B_{\widetilde W},B_{\widetilde b}\) and a finite constant \(B_\Pi>0\). The weights and biases obey
\[
\|W_i\|_{\infty,\infty}\le B_W,\quad \|b_i\|_\infty\le B_b
\quad(i=1,2),
\]
\[
\|\widetilde W_j\|_{\infty,\infty}\le B_{\widetilde W},\quad
\|\widetilde b_j\|_\infty\le B_{\widetilde b}
\quad(1\le j\le h_\Pi).
\]
Additionally, each admissible readout satisfies
\[
|\Pi_j(z)|\le B_\Pi
\qquad(z\in\mathbb R^{p(M+1)+1},\ 1\le j\le q).
\]
Let \(\mathcal F\) consist of all oscillators with these architectures and constraints. Assume that there exists \(F^*\in\mathcal F\) such that
\[
\sup_{u\in K,\ t\in[0,T]}|\Phi[u](t)-F^*[u](t)|_1
\le\varepsilon_{\rm app}.
\]
The setup, architecture, bounds, and approximation constants are deterministic and fixed independently of the sampled inputs. Put \(B_{\rm loss}=B_\Pi+B_\Phi(K)\).

Draw \(u_1,\ldots,u_N\) independently from \(\mu\), observe the full noiseless outputs \(v_i=\Phi[u_i]\), and define
\[
\widehat\ell(F)=\frac1N\sum_{i=1}^N\|v_i-F[u_i]\|_{L^2}^2,
\qquad
\ell(F)=\mathbb E_{u\sim\mu}\|\Phi[u]-F[u]\|_{L^2}^2.
\]
Let \(\widehat F\) be any empirical-risk minimizer over \(\mathcal F\). Set
\[
B_{\max}=\max(B_W,B_b,B_{\widetilde W},B_{\widetilde b}),
\]
\[
w_{\max}=\max(w_{\Pi,\rm in},w_\Pi,w_{\Pi,\rm out},w_{\Gamma,\rm in},w_\Gamma,w_{\Gamma,\rm out}).
\]

## Task

Prove that for every \(\delta\in(0,1)\), there is a measurable event of sampled inputs of probability at least \(1-\delta\) on which every empirical-risk minimizer satisfies
\[
\ell(\widehat F)\le T\varepsilon_{\rm app}^{2}
+\frac{3TqB_{\rm loss}^{2}}{\sqrt N}
\left[86w_{\max}^{3/2}h_\Pi\sqrt{\ln(3+6B_{\max}\Delta)}
+\sqrt{\tfrac12\ln(2\delta^{-1})}\right],
\]
where
\[
\Delta=30w_{\max}^{11/2}h_\Pi^2
\bigl(w_{\max}^{h_\Pi}B_{\max}^{h_\Pi}+1\bigr)
(w_{\max}^2B_{\max}^2+1)T^2
 e^{2T(w_{\max}^2B_{\max}^2+1)}
 B_\Pi^{-1}B_K(B_{\max}^3+1).
\]
