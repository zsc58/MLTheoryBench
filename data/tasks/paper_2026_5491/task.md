# Problem

## Setup

Fix an integer precision $b\ge1$ and $W>0$. Let
\[
\delta=\frac{2W}{2^b},\qquad w=-W+\delta\,\operatorname{code}(w),\qquad \operatorname{code}(w)=\sum_{k=0}^{b-1}b_k(w)2^k,
\]
where $b_k(w)\in\{0,1\}$. Thus $w$ is a stored value on this quantization grid, whose range is $[-W,W-\delta]$. Define $s_k(w)=1-2b_k(w)$. A flip of stored bit $k$ changes the decoded value by $s_k(w)2^k\delta$.

Assume a rectangular barrier of width $d>0$, effective mass $m^*>0$, and real barrier height and energy $V_b,E$ with $E<V_b$. Let $\hbar>0$ denote the reduced Planck constant. Each electron has $n=f\tau$ independent tunneling attempts during an interval of duration $\tau>0$, where $f>0$ and $n\in\{1,2,\ldots\}$ is the actual number of attempts. Attempt outcomes are also independent across electrons. An escaped electron does not return during the interval. The supplied single-attempt WKB transmission probability is
\[
q=\exp(-\alpha d),\qquad \alpha=\frac{2}{\hbar}\sqrt{2m^*(V_b-E)}.
\]
Set $P_{\rm esc}=1-(1-q)^n$. For an integer electron count $N_e\ge1$ and an integer threshold $X_{\rm thr}\in\{1,\ldots,N_e\}$, a cell flips when at least $X_{\rm thr}$ electrons escape; define its flip probability by
\[
p=\sum_{j=X_{\rm thr}}^{N_e}{N_e\choose j}P_{\rm esc}^{\,j}(1-P_{\rm esc})^{N_e-j}.
\]
Across the $b$ stored bits, flips $\xi_k$ are independent Bernoulli$(p)$ variables, conditional on the stored weight $w$.

## Task

Prove the following integrated theorem. Conditional on any stored weight $w$, the perturbation
\[
\Delta w=\delta\sum_{k=0}^{b-1}\xi_k s_k(w)2^k
\]
has characteristic function, for every real $t$,
\[
\phi_{\Delta w\mid w}(t)=\prod_{k=0}^{b-1}\left[1-p+p\exp\!\left(it\,s_k(w)2^k\delta\right)\right].
\]
Moreover,
\[
\mathbb E[\Delta w\mid w]=-2pw-p\delta,
\qquad
\operatorname{Var}(\Delta w\mid w)=p(1-p)\delta^2\frac{4^b-1}{3}.
\]

Establish both the escape bound
\[
P_{\rm esc}\le nq
\]
and the relative small-escape estimate
\[
P_{\rm esc}=nq\bigl(1+O(nq)\bigr)
\]
as $nq\to0$ through positive integers $n$ and $q\in(0,1)$, with an absolute implicit constant.

For the precision limit, fix $W>0$ and $p\in(0,1)$, and let $w_b$ be any sequence of stored values on the respective $b$-bit grids. Write $\delta_b=2W/2^b$, use $\xi_{b,k}$ for the bit indicators at precision $b$, and write $\Delta w_b$ for the corresponding perturbation. Define the centered bit contributions and conditional variance by
\[
Y_{b,k}=\delta_b\xi_{b,k}s_k(w_b)2^k-\mathbb E[\delta_b\xi_{b,k}s_k(w_b)2^k\mid w_b],
\qquad
\sigma_b^2=\operatorname{Var}(\Delta w_b\mid w_b).
\]
Define the third-absolute-moment Lyapunov ratio and the standardized perturbation by
\[
L_b=\frac{\sum_{k=0}^{b-1}\mathbb E[|Y_{b,k}|^3\mid w_b]}{\sigma_b^3},
\qquad
Z_b=\frac{\Delta w_b-\mathbb E[\Delta w_b\mid w_b]}{\sigma_b}.
\]
Prove that
\[
\frac{\operatorname{Var}(Y_{b,b-1}\mid w_b)}{\sigma_b^2}\longrightarrow\frac34,
\qquad
\lim_{b\to\infty}L_b\in(0,\infty),
\]
and that, for every such sequence of stored values, the conditional laws of $Z_b$ do not converge in distribution to $\mathcal N(0,1)$ as $b\to\infty$.
