# Problem

## Setup

Let \((X,\mathcal B)\) be a measurable space and let \(\mathsf P(X)\) denote its probability measures. Fix a finite-valued convex function \(f:(0,\infty)\to\mathbb R\) with \(f(1)=0\). Define its endpoint extensions by
\[
f(0)=\lim_{t\downarrow0}f(t),\qquad
f'(\infty)=\lim_{t\to\infty}\frac{f(t)}{t},
\]
where either limit may be \(+\infty\). For probability measures \(\alpha,\beta\), choose any sigma-finite common dominating measure \(\lambda\), write \(a=d\alpha/d\lambda\), \(b=d\beta/d\lambda\), and define
\[
D_f(\alpha\|\beta)=\int_{\{b>0\}} b\,f(a/b)\,d\lambda+f'(\infty)\,\alpha(\{b=0\}),
\]
with the convention \(0\cdot(+\infty)=(+\infty)\cdot0=0\).

Let \(T:\operatorname{dom}(T)\to Y\) be a partial statistic on probability measures, with target \(\mu\in\operatorname{dom}(T)\) and variational family \(\mathcal V\subseteq\operatorname{dom}(T)\). Assume that
\[
\min_{\nu\in\mathcal V}D_f(\mu\|\nu)
\]
has the unique minimizer \(\nu^\star\).

Let \(H\) be a group of measurable bijections of \(X\) whose inverses are measurable. It acts on measures by \(h_\#\pi(A)=\pi(h^{-1}(A))\). Assume:

1. \(h_\#\mu=\mu\) for every \(h\in H\);
2. \(h_\#\mathcal V\subseteq\mathcal V\) for every \(h\in H\);
3. \(h_\#\operatorname{dom}(T)\subseteq\operatorname{dom}(T)\) for every \(h\in H\), and for every \(h\in H\) and \(\pi_1,\pi_2\in\operatorname{dom}(T)\), whenever \(T(\pi_1)=T(\pi_2)\), then \(T(h_\#\pi_1)=T(h_\#\pi_2)\).

For \(y\in Y_0:=T(\operatorname{dom}(T))\), define \(\varrho_h(y)=T(h_\#\pi)\) for any \(\pi\in\operatorname{dom}(T)\) with \(T(\pi)=y\); condition 3 makes this well-defined. Define
\[
\Gamma_T(H)=\{y\in Y_0:\varrho_h(y)=y\text{ for every }h\in H\}.
\]

## Task

Prove that
\[
T(\mu)\in\Gamma_T(H)\qquad\text{and}\qquad T(\nu^\star)\in\Gamma_T(H).
\]
