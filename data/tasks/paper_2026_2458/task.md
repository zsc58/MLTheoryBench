# Problem

## Setup

Consider the continuous-time system
\\[
\\dot x=Ax+Bu,\\qquad x(t)\\in\\mathbb R^n,\\quad u(t)\\in\\mathbb R^m,
\\]
with infinite-horizon cost \\(\\int_0^\\infty (x^TQx+u^TRu)\\,dt\\), where \\(Q\\in\\mathbb R^{n\\times n}\\) is positive semidefinite and \\(R\\in\\mathbb R^{m\\times m}\\) is positive definite. Assume \\((A,B)\\) is stabilizable and \\((A,Q^{1/2})\\) is detectable. Let \\(P^*\\in\\mathbb R^{n\\times n}\\) be the unique positive-semidefinite stabilizing solution of
\\[
A^TP+PA-PBR^{-1}B^TP+Q=0,
\\]
and let \\(K^*=R^{-1}B^TP^*\\in\\mathbb R^{m\\times n}\\).

Fix an integer \\(T\\ge1\\), a length \\(\\delta>0\\), and intervals \\([t_i,t_i+\\delta]\\), \\(i=1,\\ldots,T\\), on which the state and input trajectories are observed. Define
\\[
\\tilde U=[\\tilde u_1\\ \\cdots\\ \\tilde u_T]\\in\\mathbb R^{m\\times T},\\quad \\tilde u_i=\\int_{t_i}^{t_i+\\delta}u(t)\\,dt,
\\]
\\[
\\tilde X=[\\tilde x_1\\ \\cdots\\ \\tilde x_T]\\in\\mathbb R^{n\\times T},\\quad \\tilde x_i=\\int_{t_i}^{t_i+\\delta}x(t)\\,dt,
\\]
and
\\[
\\bar X=[\\bar x_1\\ \\cdots\\ \\bar x_T]\\in\\mathbb R^{n\\times T},\\quad \\bar x_i=x(t_i+\\delta)-x(t_i).
\\]
They satisfy
\\[
\\bar X=A\\tilde X+B\\tilde U,
\\]
and assume the integrated-data rank condition
\\[
\\operatorname{rank}\\begin{bmatrix}\\tilde U\\\\ \\tilde X\\end{bmatrix}=m+n.
\\]
Define
\\[
\\mathcal G=\\{G\\in\\mathbb R^{T\\times n}:\\ \\tilde XG=I_n,\\ \\bar XG\\text{ is Hurwitz}\\}.
\\]
For \\(G\\in\\mathcal G\\), set \\(K_G=-\\tilde UG\\), and let \\(P_G\\in\\mathbb R^{n\\times n}\\) be the unique symmetric solution of
\\[
(\\bar XG)^TP_G+P_G(\\bar XG)+Q+(\\tilde UG)^TR(\\tilde UG)=0.
\\]
For any symmetric \\(P\\in\\mathbb R^{n\\times n}\\) with \\(P\\succeq0\\), define
\\[
J_P(G)=\\operatorname{tr}\\!\\left(Q+G^T\\tilde U^TR\\tilde UG+P\\bar XG+G^T\\bar X^TP\\right).
\\]
Given \\(G_k\\in\\mathcal G\\), let \\(P_k=P_{G_k}\\), and choose \\(G_{k+1}\\) to be the minimum-Frobenius-norm minimizer of \\(J_{P_k}(G)\\) subject to \\(\\tilde XG=I_n\\).

## Task

Prove that for every initial \\(G_0\\in\\mathcal G\\), this iteration is well-defined, every \\(G_k\\) belongs to \\(\\mathcal G\\), and with \\(K_k=-\\tilde UG_k\\) one has \\(K_k\\to K^*\\) and \\(P_k\\to P^*\\). Moreover, the selected matrices converge to a limit \\(G^*\\in\\mathcal G\\) satisfying \\(-\\tilde UG^*=K^*\\).
