# Problem

## Setup

Fix \(1\le p<\infty\), integers \(d\ge1\) and \(K\ge2\), a scale \(0<s<1\), and \(0<\lambda_{\min}\le\lambda_{\max}\le1\). Write \([K]=\{1,\ldots,K\}\) and \(B_p^d(x,a)=\{z\in\mathbb R^d:\|z-x\|_p\le a\}\). Let \(x_0\in\mathbb R^d\). Let \(r:\mathbb R^d\to\mathbb R^{d\times K}\) be a map for which there exists \(s_{\rm sep}>0\) such that, for every \(x\in B_2^d(0,1)\),
\[
\lambda_{\min}\le\|r(x)_k\|_2\le\lambda_{\max}\quad(k\in[K]),
\qquad
\|r(x)_k-r(x)_j\|_2\ge s_{\rm sep}\quad(k\ne j).
\]
No continuity of \(r\) is assumed.

Set \(x_{\emptyset}=x_0\) and \(C_{\emptyset}=B_p^d(x_0,\lambda_{\max})\). For an address \(\alpha\in[K]^\ell\), define
\[
x_{\alpha k}=x_\alpha+s^{\ell+1}r(x_\alpha)_k,
\qquad
C_{\alpha k}=\{z\in C_\alpha:\|z-x_{\alpha k}\|_p\le\min_{j\in[K]}\|z-x_{\alpha j}\|_p\}.
\]
Assume that every recursively generated center, including the root, belongs to \(B_2^d(0,1)\), and that every recursively defined cell is nonempty and compact.

The address vertices with parent-child edges form a rooted \(K\)-ary tree. On its underlying undirected graph, give the edge \(\alpha\to\alpha k\), where \(|\alpha|=\ell\), tree weight \(s^{\ell+1}\); denote the resulting address-tree metric by \(d_{\rm tree}\).

Identify address vertices having both identical centers and identical cells to form a geometric vertex set. Retain each projected genealogical edge individually, allowing parallel edges, and assign it cell weight
\[
s^\ell\lambda_{\max}d_{H,p}(C_\alpha,C_{\alpha k}),
\]
where \(d_{H,p}\) is the Hausdorff distance induced by \(\|\cdot\|_p\). Forget orientations and let \(\rho_{\rm cell}\) be the infimum of total cell weights over finite walks joining two geometric vertices. This is interpreted as a pseudometric: identify vertices at zero \(\rho_{\rm cell}\)-distance and denote the induced metric by \(d_{\rm cell}\). Let \(X_{\rm cell}\) be its metric completion, with metric \(\overline d_{\rm cell}\). Let \(Y_L\subseteq X_{\rm cell}\) be the image of all address vertices through level \(L\), equipped with the restriction of the full metric. Hausdorff distance in this completion is denoted by \(d_H^{\overline d_{\rm cell}}\).

A ReLU predictor means a finite feedforward network with affine layers, componentwise activation \(t\mapsto\max\{0,t\}\) in its hidden layers, and an affine output layer, reshaped to \(\mathbb R^{d\times K}\). Its width is the maximum hidden-layer dimension and its depth is the number of affine layers. Real weights and biases are unrestricted.

## Task

Prove that for every \(\varepsilon\in(0,1)\), with
\[
L_\varepsilon=\max\left\{2,\left\lceil{\log\!\big(2\lambda_{\max}^2/((1-s)\varepsilon)\big)\over-\log s}\right\rceil\right\},
\]
there exists a ReLU predictor \(\widehat r_{L_\varepsilon}:\mathbb R^d\to\mathbb R^{d\times K}\) whose recursive rollout, using the same root, center rule, and Voronoi rule, agrees exactly with the true center and cell at every address through level \(L_\varepsilon\). Its image truncation is therefore \(Y_{L_\varepsilon}\), and
\[
d_H^{\overline d_{\rm cell}}(Y_{L_\varepsilon},X_{\rm cell})\le\varepsilon.
\]
For \(L\ge2\), define
\[
\delta_{0,L}=\min\{\|x_\alpha-x_\beta\|_2:x_\alpha\ne x_\beta,\ 0\le|\alpha|,|\beta|\le L-1\},
\quad
B_L={2\lambda_{\max}s(1-s^{L-1})\over(1-s)\delta_{0,L}}.
\]
If the parent-center set has only one distinct point, do not evaluate this minimum or ratio and use \(B_L=1\). Write \(\log_+(t)=\max\{0,\log t\}\) for \(t>0\).

Show that the predictor may be chosen with width \(O(K^{L_\varepsilon})\) and depth
\[
O\!\left(K^{3L_\varepsilon/2}\sqrt{L_\varepsilon\log K}\left[1+{\log_+(B_{L_\varepsilon})\over L_\varepsilon\log K}\right]\right).
\]
The constants may depend only on the fixed parameters \(d,K,p,s,\lambda_{\min},\lambda_{\max},s_{\rm sep}\), and not on \(\varepsilon\), the field \(r\), or the center separations except through the displayed factor.

Equivalently, as \(\varepsilon\downarrow0\), for \(\gamma=\log K/(-\log s)\), the width is \(O(\varepsilon^{-\gamma})\) and the depth is
\[
\widetilde O\!\left(\varepsilon^{-3\gamma/2}\left[1+\frac{\log_+(B_{L_\varepsilon})}{\log(1/\varepsilon)}\right]\right),
\]
where \(\widetilde O\) suppresses factors polynomial in \(1+\log(1/\varepsilon)\). In particular, the depth is \(\widetilde O(\varepsilon^{-3\gamma/2})\) when \(B_{L_\varepsilon}\le C\varepsilon^{-a}\) for some fixed \(C,a>0\) and all sufficiently small \(\varepsilon\).
