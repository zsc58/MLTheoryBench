# Problem

## Setup

Let S, A, and O be finite nonempty sets of states, actions, and observations. Let T(s'|s,a) be a transition probability kernel, beta(o|s) an observation probability kernel, r:S\times A\to\mathbb R a bounded reward function, and gamma\in(0,1). A memoryless stochastic observation policy is a collection pi(a|o)\ge0 with \sum_{a\in A}pi(a|o)=1 for every o\in O. Its induced transition and reward are
\[
P^pi_{ss'}=\sum_{o\in O,a\in A}\beta(o|s)\,pi(a|o)\,T(s'|s,a),\qquad
r^pi_s=\sum_{o\in O,a\in A}\beta(o|s)\,pi(a|o)\,r(s,a).
\]
For each policy, V^pi is the unique solution of (I-gamma P^pi)V=r^pi. Let
\[
\mathcal V=\{V^pi:pi\text{ is a memoryless stochastic observation policy}\}\subseteq\mathbb R^S.
\]
Write m=|O||A| and index coordinates by pairs (o,a). For x\in\mathbb R^S define
\[
M(x)_{s,(o,a)}=\beta(o|s)\left(r(s,a)+\gamma\sum_{s'\in S}T(s'|s,a)x_{s'}\right).
\]
Let R be the |O|\times m matrix with R_{o,(\tilde o,a)}=1 when \tilde o=o and 0 otherwise, and put
\[
C(x)=\begin{bmatrix}M(x)\\R\end{bmatrix},\qquad f(x)=\binom{x}{\mathbf1_{|O|}}.
\]
For row and column index sets I,B of the same size rho, let C(x)_{I,B} denote the corresponding square minor. For t\in B, let C(x)_{I,B,t} denote that minor with the column t replaced by f(x)_I.

## Task

Prove the following theorem. The feasible value set is the finite union
\[
\mathcal V=\bigcup_{\rho=1}^{\min(|S|+|O|,m)}\ \bigcup_{\substack{I\subseteq\{1,\ldots,|S|+|O|\},\ |I|=\rho}}\ \bigcup_{\substack{B\subseteq\{1,\ldots,m\},\ |B|=\rho}}\mathcal U_{\rho,I,B},
\]
where \mathcal U_{\rho,I,B} consists exactly of those x\in\mathbb R^S such that:

1. det C(x)_{I,B}\ne0;
2. every (rho+1)\times(rho+1) minor of C(x) is zero (whenever such minors exist);
3. every (rho+1)\times(rho+1) minor of the augmented matrix [C(x)\mid f(x)] is zero (whenever such minors exist);
4. for every t\in B, det C(x)_{I,B,t}\,det C(x)_{I,B}\ge0.

Consequently, \mathcal V is a finite union of basic semi-algebraic sets described by determinant nonvanishing, determinant vanishing, and polynomial sign inequalities in x.
