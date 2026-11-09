# Problem

## Setup

Let \((\mathcal X,\mathcal A,\mu)\) be a measurable space, and let \(\pi(x)\) be a normalized base density with respect to \(\mu\). Write \(P(dx)=\pi(x)\,d\mu(x)\). Let \(f_1,\ldots,f_m:\mathcal X\to\mathbb R\) be measurable statistics and write
\[
F(x)=(f_1(x),\ldots,f_m(x)).
\]

Let \(\Lambda\subseteq\mathbb R^m\) be a Borel measurable hyperparameter space, equipped with a reference measure \(\rho\). For each \(\lambda=(\lambda_1,\ldots,\lambda_m)\in\Lambda\), assume
\[
Z(\lambda)=\int_{\mathcal X}\pi(x)\exp\!\left(\sum_{i=1}^m\lambda_i f_i(x)\right)d\mu(x)
\]
is finite and positive. Define the canonical conditional density
\[
p(x\mid\lambda)=\frac{\pi(x)\exp\!\left(\sum_{i=1}^m\lambda_i f_i(x)\right)}{Z(\lambda)}.
\]

Let \(q:\Lambda\to[0,\infty)\) be a measurable \(\rho\)-density with
\[
\int_\Lambda q(\lambda)d\rho(\lambda)=1,
\]
and define
\[
p_q(x)=\int_\Lambda q(\lambda)p(x\mid\lambda)d\rho(\lambda).
\]
Assume this integral defines a normalized density. Maximum entropy is understood as maximizing relative entropy to \(\pi\), equivalently minimizing \(D_{\mathrm{KL}}(\cdot\|P)\), with the value \(+\infty\) when its first argument is not absolutely continuous with respect to \(P\).

## Task

Prove that there exists a nonnegative measurable function \(g:\mathbb R^m\to[0,\infty)\) such that
\[
p_q(x)=\pi(x)g\!\left(f_1(x),\ldots,f_m(x)\right)
\]
for \(\mu\)-almost every \(x\). Then prove that, among all normalized \(\mu\)-densities \(r\) whose induced probability law satisfies
\[
F_\#\bigl(r\,d\mu\bigr)=F_\#\bigl(p_q\,d\mu\bigr),
\]
this density minimizes \(D_{\mathrm{KL}}(r\,d\mu\|P)\). In other words, the hierarchical marginal is a maximum-relative-entropy distribution on \(x\) relative to \(\pi\) when the effective constraint is the complete marginal distribution of \(F(x)\).
