# Problem

## Setup

Let \(W=(Y,X)\) have a fixed probability law \(P_0\) on \(\mathcal W=\mathcal Y\times\mathcal X\), and let \(W_1,W_2,\ldots\) be iid validation observations from \(P_0\). Write \(\mathbb E\) for expectation under \(P_0\), and for \(n\geq1\) write
\[
\mathbb E_n[q]=\frac1n\sum_{i=1}^n q(W_i).
\]
The same notation is used when \(q\) is an estimated, sample-dependent function.

Let \(\mathcal H\) be a real Hilbert space of square-integrable measurable functions from \(\mathcal X\) to \(\mathbb R\), with inner product
\[
\langle g,h\rangle=\mathbb E[g(X)h(X)].
\]
Functions are identified when they agree almost surely under the law of \(X\). Let \(L:\mathbb R\times\mathcal W\to\mathbb R\) be a measurable loss differentiable in its prediction argument, and suppose its population risk
\[
R_0(f)=\mathbb E[L\{f(X),W\}],\qquad f\in\mathcal H,
\]
is finite and has an existing unique minimizer \(f_0\in\mathcal H\). Write \(\nabla L\) for differentiation with respect to the prediction argument. For \(g,f\in\mathcal H\), the directional score contribution is
\[
s(W;g,f)=g(X)\,\nabla L\{f(X),W\}.
\]

Let \(\varphi_0(W;g,f)\) be a given population influence-function score contribution at the law \(P_0\), and let \(\widehat\varphi(W;g,f)\) be its estimated version. The population function is fixed, whereas its estimated version may depend on \(n\) and on the validation sample. All evaluated contributions are finite, measurable real random variables. Suppress the observation argument by writing \(\varphi_0(g,f)\) and \(\widehat\varphi(g,f)\); empirical means evaluate these functions at the observations \(W_i\).

For \(g,f\in\mathcal H\), define
\[
T_n(g,f)=
\begin{cases}
\displaystyle\frac{n\bigl(\mathbb E_n[\widehat\varphi(g,f)]\bigr)^2}
{\mathbb E_n[\widehat\varphi(g,f)^2]},
&\mathbb E_n[\widehat\varphi(g,f)^2]>0,\\[6pt]
0,&\mathbb E_n[\widehat\varphi(g,f)^2]=0.
\end{cases}
\]

Fix a deterministic hypothesized predictor \(f_*\in\mathcal H\) and a deterministic nonzero direction \(h\in\mathcal H\), neither depending on \(n\) or on the validation observations. All limits below are as \(n\to\infty\) with \(P_0,f_*\), and \(h\) fixed. The notation \(o_p(1)\) denotes convergence to zero in probability. Assume:

1. For every \(g\in\mathcal H\),
\[
\mathbb E[\varphi_0(g,f_0)]=0.
\]
2. The map \(g\mapsto\mathbb E[\varphi_0(g,f_*)]\) is a continuous linear functional on \(\mathcal H\), with Riesz representer \(h^*(f_*)\in\mathcal H\), so
\[
\mathbb E[\varphi_0(g,f_*)]=\langle g,h^*(f_*)\rangle
\quad\text{for every }g\in\mathcal H.
\]
3. For every nonzero \(g\in\mathcal H\),
\[
0<\mathbb E[\varphi_0(g,f_0)^2]<\infty.
\]
4. For the fixed direction \(h\), under \(H_0:f_*=f_0\),
\[
\sqrt n\,\mathbb E_n[\widehat\varphi(h,f_0)-\varphi_0(h,f_0)]=o_p(1).
\]
5. For the fixed direction \(h\) and fixed hypothesized predictor \(f_*\), first- and second-moment consistency hold:
\[
\mathbb E_n[\widehat\varphi(h,f_*)^k-\varphi_0(h,f_*)^k]=o_p(1),\qquad k=1,2.
\]
6. Under any alternative considered below,
\[
0<\mathbb E[\varphi_0(h,f_*)^2]<\infty.
\]

## Task

Prove the following integrated theorem for the fixed predictor and direction above. Under \(H_0:f_*=f_0\),
\[
T_n(h,f_*)\Rightarrow\chi^2_1.
\]
Under \(H_1:f_*\ne f_0\), if \(\langle h,h^*(f_*)\rangle\ne0\), then for every fixed finite real critical value \(c_\alpha\),
\[
\Pr\{T_n(h,f_*)>c_\alpha\}\longrightarrow1.
\]
