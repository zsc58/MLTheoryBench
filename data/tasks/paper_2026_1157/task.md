# Problem

## Setup

Let \(m,n,r\in\mathbb N_+\), let \(\lambda,\mu\ge0\), and let \(\Phi:\mathbb R^{m\times n}\times\mathbb R^{m\times n}\to\mathbb R\) be locally Lipschitz. Let
\[
\mathcal B^S=[\kappa^1,\kappa^2]
\]
be a coordinatewise box, where \(\kappa^1_{ij}\in[-\infty,0]\) and \(\kappa^2_{ij}\in[0,+\infty]\). Define
\[
L(Z,S)=\Phi(Z,S)+2\lambda\operatorname{rank}(Z)+\mu\|S\|_0
\]
for \(\operatorname{rank}(Z)\le r\) and \(S\in\mathcal B^S\), and
\[
F(X,Y,S)=\Phi(XY^\top,S)+\lambda\bigl(\operatorname{nnzc}(X)+\operatorname{nnzc}(Y)\bigr)+\mu\|S\|_0
\]
for \(X\in\mathbb R^{m\times r}\), \(Y\in\mathbb R^{n\times r}\), and \(S\in\mathcal B^S\). Here \(\operatorname{nnzc}\) counts nonzero columns. Write \(G_L,G_F\), \(\mathcal L_L,\mathcal L_F\), and \(\mathcal S_L,\mathcal S_F\) for the respective global-minimizer, local-minimizer, and stationary-point sets.

For a feasible \((Z,S)\), set
\[
\mathcal Q_{\lambda,Z}:=
\{W\in\mathbb R^{m\times n}:\operatorname{rank}(W)\le r,\ 
\lambda\operatorname{rank}(W)=\lambda\operatorname{rank}(Z)\}.
\]
For \(S\in\mathcal B^S\), let
\[
I_S:=
\begin{cases}
\operatorname{supp}(S),&\mu>0,\\
[m]\times[n],&\mu=0,
\end{cases}
\qquad
\mathcal T_I:=\{T\in\mathcal B^S:T_{I^c}=0\}.
\]
For a factor \(X\in\mathbb R^{a\times r}\), define
\[
J_X:=
\begin{cases}
\{j\in[r]:X_j\ne0\},&\lambda>0,\\
[r],&\lambda=0,
\end{cases}
\qquad
\mathcal C^a_J:=\{W\in\mathbb R^{a\times r}:W_j=0\text{ for }j\notin J\}.
\]
All normal cones and subdifferentials below are limiting ones. A feasible point \((Z,S)\) is stationary for \(L\) when some \((H_Z,H_S)\in\partial\Phi(Z,S)\) satisfies
\[
-H_Z\in N_{\mathcal Q_{\lambda,Z}}(Z),
\qquad
-H_S\in N_{\mathcal T_{I_S}}(S).
\]
A feasible point \((X,Y,S)\) is stationary for \(F\) when some \((H_Z,H_S)\in\partial\Phi(XY^\top,S)\) satisfies
\[
-H_ZY\in N_{\mathcal C^m_{J_X}}(X),\qquad
-H_Z^\top X\in N_{\mathcal C^n_{J_Y}}(Y),\qquad
-H_S\in N_{\mathcal T_{I_S}}(S).
\]

For the bounded formulations, let \(\mathcal B^Z\subseteq\mathbb R^{m\times n}\) be a coordinatewise box, define
\[
\|\mathcal B^Z\|_{\max}:=\sup_{Z\in\mathcal B^Z}\|Z\|_2,
\]
and, for \(\tau\in[0,+\infty]\), set
\[
\mathcal B^X_\tau:=\{X\in\mathbb R^{m\times r}:\|X_j\|_2\le\tau\ \forall j\},
\qquad
\mathcal B^Y_\tau:=\{Y\in\mathbb R^{n\times r}:\|Y_j\|_2\le\tau\ \forall j\}.
\]
Let \(L_B\) be \(L\) restricted to \(Z\in\mathcal B^Z\), and let \(F_B\) be \(F\) restricted to \((X,Y,S)\in\mathcal B^X_\tau\times\mathcal B^Y_\tau\times\mathcal B^S\). Denote their global-minimizer sets by \(G_{L_B}\) and \(G_{F_B}\).

## Task

Prove all of the following.

1. For every \(Z\in\mathbb R^{m\times n}\) with \(\operatorname{rank}(Z)\le r\),
\[
\operatorname{rank}(Z)=
\min_{XY^\top=Z}\frac{\operatorname{nnzc}(X)+\operatorname{nnzc}(Y)}2.
\]
Consequently \(\inf L=\inf F\) and
\[
G_L=\{(XY^\top,S):(X,Y,S)\in G_F\}.
\]
Moreover, every global minimizer of \(L\) has a padded compact-SVD lift that is a global minimizer of \(F\).

2. Assume
\[
\tau\ge\|\mathcal B^Z\|_{\max}^{1/2},
\qquad
(\mathcal B^Z\times\mathcal B^S)\cap G_L\ne\varnothing.
\]
Show that
\[
\inf L_B=\inf F_B=\inf L,
\qquad
G_{L_B}\subseteq\{(XY^\top,S):(X,Y,S)\in G_{F_B}\}\subseteq G_L.
\]
Also prove that every local minimizer of \(L\) has a padded compact-SVD factor lift that is a local minimizer of \(F\).

3. Prove that every stationary point of \(L\) has a padded compact-SVD factor lift that is stationary for \(F\). Finally, prove that, when \(\lambda>0\),
\[
\mathcal S_L=\{(XY^\top,S):(X,Y,S)\in\mathcal S_F\}.
\]
