# Problem

## Setup

Let $p,d$ be positive integers with $p\ge d$. Let $A\in\mathbb R^{p\times d}$ be known and have full column rank, with columns $a_1,\ldots,a_d$. The latent vector is $X\in\mathbb R^d$ and the observed vector is
\[
Y=AX+\varepsilon,
\]
where $\varepsilon\sim\mathcal N(0,\operatorname{diag}(\sigma_1^2,\ldots,\sigma_p^2))$ is independent of $X$ in every interventional regime considered below and has the same distribution under all these interventions.

For each $i\in\{1,\ldots,d\}$, choose an available intervention targeting latent coordinate $i$, possibly together with other coordinates, and use $\operatorname{do}(i)$ to label this chosen regime. Its targeted interventional variance
\[
v_i=\operatorname{Var}(X_i\mid\operatorname{do}(i))\in[0,\infty)
\]
is finite and known, and the corresponding population variance of any projected observation is observable.

A vector $t\in\mathbb R^p$ is called admissible for target $i$ if
\[
A_{-i}^Tt=0\quad\text{and}\quad a_i^Tt\ne0,
\]
where $A_{-i}$ is $A$ with column $i$ removed. For admissible vectors $t_1,\ldots,t_p$, let $i_r$ be the target associated with $t_r$, define
\[
T_2=(t_{r,k}^2)_{r,k=1}^p,
\]
and set
\[
q_r=\operatorname{Var}(t_r^TY\mid\operatorname{do}(i_r))-(a_{i_r}^Tt_r)^2v_{i_r}.
\]

## Task

Prove that for Lebesgue-almost-every full-column-rank matrix $A\in\mathbb R^{p\times d}$, admissible vectors $t_1,\ldots,t_p$ can be selected (with suitable associated intervention targets) so that $T_2$ is invertible. Conclude that the measurement-noise variance vector $(\sigma_1^2,\ldots,\sigma_p^2)^T$ is uniquely identifiable from the resulting projected interventional variances, equivalently as the unique least-squares solution of the resulting linear system over $\mathbb R^p$, and also over the nonnegative variance domain $[0,\infty)^p$.
