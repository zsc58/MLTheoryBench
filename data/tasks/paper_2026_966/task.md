# Problem

## Setup

Let d_X and d_Y be positive integers. There are treatment levels indexed by \(\mathcal X=\{1,\ldots,d_X\}\) and an ordinal outcome taking values in \(\{1,\ldots,d_Y\}\). For each \(x\in\mathcal X\), let \(Y_x\) be the potential outcome, and assume consistency \(Y=Y_X\). Write \(Y_{1:d_X}=(Y_1,\ldots,Y_{d_X})\), \(\mathcal Y=\{1,\ldots,d_Y\}^{d_X}\), and
\[
p_{y,x}=\Pr(Y_{1:d_X}=y,X=x),\qquad (y,x)\in\mathcal Y\times\mathcal X.
\]
Thus \(p_{y,x}\ge0\) and \(\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y}p_{y,x}=1\). Let the target be any linear functional
\[
\phi(p)=\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y}c_{y,x}p_{y,x},
\]
with fixed real coefficients \(c_{y,x}\).

The available data consist of the complete collection of experimental marginals, the complete collection of observational marginals, or both. Experimental marginals \(a_{kj}=\Pr(Y_k=j)\), for \(k\in\mathcal X\), \(j\in\{1,\ldots,d_Y\}\), impose
\[
\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y:\,y_k=j}p_{y,x}=a_{kj}.
\]
Observational marginals \(b_{\ell m}=\Pr(X=\ell,Y=m)\), for \(\ell\in\mathcal X\), \(m\in\{1,\ldots,d_Y\}\), impose
\[
\sum_{y\in\mathcal Y:\,y_\ell=m}p_{y,\ell}=b_{\ell m}.
\]
All supplied marginals are fixed.

Optionally, impose exogeneity: \(Y_k\) is independent of \(X\) for every \(k\in\mathcal X\). When this condition is imposed, include the following additional equations in the linear programs. If observational marginals are available, define \(q_\ell=\sum_{m=1}^{d_Y}b_{\ell m}\) and impose
\[
\sum_{y\in\mathcal Y:\,y_k=j}p_{y,\ell}
=q_\ell\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y:\,y_k=j}p_{y,x}
\qquad(k,\ell\in\mathcal X,\ j\in\{1,\ldots,d_Y\}).
\]
If only experimental marginals are available, instead impose
\[
\sum_{y\in\mathcal Y:\,y_k=j}p_{y,\ell}
=a_{kj}\sum_{y\in\mathcal Y}p_{y,\ell}
\qquad(k,\ell\in\mathcal X,\ j\in\{1,\ldots,d_Y\}).
\]

Fix a positive integer W. For each \(w\in\{1,\ldots,W\}\) and each pair \(s,t\in\mathcal X\) with \(s>t\), let integers \(D^{(w),-}_{st}\le D^{(w),+}_{st}\) be given. Let \(0\le L^w\le U^w\le1\), and assume
\[
L^w\le \Pr\!\left(\bigcap_{s>t}\{D^{(w),-}_{st}\le Y_s-Y_t\le D^{(w),+}_{st}\}\right)\le U^w,
\qquad w=1,\ldots,W.
\]
Assume the selected data equations and all imposed restrictions are jointly feasible.

## Task

Define, for \(y\in\mathcal Y\),
\[
I_w(y)=\prod_{s>t}{\bf1}\!\left\{D^{(w),-}_{st}\le y_s-y_t\le D^{(w),+}_{st}\right\}.
\]
Prove that, over all \(p\) satisfying the simplex, whichever experimental and/or observational marginal equations are available, any stated exogeneity equations, and
\[
L^w\le\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y}I_w(y)p_{y,x}\le U^w,
\qquad w=1,\ldots,W,
\]
the linear programs
\[
\underline\lambda=\min_p\phi(p),\qquad \overline\lambda=\max_p\phi(p)
\]
have attained optima, and these values are sharp lower and upper bounds on the target over all joint potential-outcome/observed-variable laws satisfying the setup.
