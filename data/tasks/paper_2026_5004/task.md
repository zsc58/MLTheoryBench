# Problem

## Setup

Let \(D\) be a fixed finite set of inputs, let \(x_*\) be a fixed query input, and fix an integer \(M\) with \(0\le M\le |D|\). Let \(\phi(x)\in\mathbb R^p\) be fixed tangent feature vectors for \(x\in D\cup\{x_*\}\), and define the kernel \(k(x,x')=\phi(x)^\mathsf{T}\phi(x')\). Assume \(k_{**}:=k(x_*,x_*)>0\). For \(T\subseteq D\), write \(K_T=(k(x,x'))_{x,x'\in T}\) and \(b_T=(k(x,x_*))_{x\in T}\). Observations have independent Gaussian noise with variance \(\sigma^2>0\). Define the posterior marginal variance
\[
v(T):=k_{**}-b_T^\mathsf{T}(K_T+\sigma^2 I)^{-1}b_T,
\]
with \(v(\varnothing)=k_{**}\). For every \(S\subseteq D\), define
\[
G(S):=-\frac12\log\frac{v(S)}{k_{**}},\qquad
L(S):=\frac12\log\frac{v(D\setminus S)}{v(D)}.
\]
Let \(\mathcal S_M=\{S\subseteq D:|S|=M\}\) and \(a(S):=\|b_S\|_2^2\).

## Task

Prove that, as \(\sigma^2\to\infty\), uniformly for \(S\in\mathcal S_M\),
\[
G(S)=\frac{a(S)}{2k_{**}\sigma^2}+O(\sigma^{-4}),\qquad
L(S)=\frac{a(S)}{2k_{**}\sigma^2}+O(\sigma^{-4}).
\]
If \(a(S)\) has a unique maximizer \(S^\dagger\) on \(\mathcal S_M\), prove that there is \(\sigma_0^2<\infty\) such that for every \(\sigma^2\ge\sigma_0^2\), both \(G\) and \(L\) are uniquely maximized on \(\mathcal S_M\) by \(S^\dagger\).
