# Reference Proof

Let
\[
L(Z,S)=\Phi(Z,S)+2\lambda\operatorname{rank}(Z)+\mu\|S\|_0
\]
on \(\{(Z,S):\operatorname{rank}(Z)\le r,\ S\in\mathcal B^S\}\), and let
\[
F(X,Y,S)=\Phi(XY^\top,S)+\lambda\bigl(\operatorname{nnzc}(X)+\operatorname{nnzc}(Y)\bigr)+\mu\|S\|_0
\]
on \(\mathbb R^{m\times r}\times\mathbb R^{n\times r}\times\mathcal B^S\). All normal cones and subdifferentials below are limiting ones.

## Rank/column identity and global minimizers

Fix \(Z\) with \(q=\operatorname{rank}(Z)\le r\). If \(Z=XY^\top\), then
\[
q\le\operatorname{rank}(X)\le\operatorname{nnzc}(X),\qquad
q\le\operatorname{rank}(Y)\le\operatorname{nnzc}(Y).
\]
Thus \((\operatorname{nnzc}(X)+\operatorname{nnzc}(Y))/2\ge q\). Conversely, write a compact SVD
\[
Z=U\Sigma V^\top,
\]
where \(\Sigma\in\mathbb R^{q\times q}\) is positive diagonal, and set
\[
X_Z=[U\Sigma^{1/2},0]\in\mathbb R^{m\times r},\qquad
Y_Z=[V\Sigma^{1/2},0]\in\mathbb R^{n\times r}.
\]
Then \(X_ZY_Z^\top=Z\) and both factors have exactly \(q\) nonzero columns. Hence
\[
\operatorname{rank}(Z)=\min_{XY^\top=Z}\frac{\operatorname{nnzc}(X)+\operatorname{nnzc}(Y)}2.
\tag{1}
\]

For every feasible factor triple, (1) gives
\[
F(X,Y,S)\ge L(XY^\top,S).
\tag{2}
\]
For every feasible \((Z,S)\), its padded compact-SVD factors attain equality in (2). Taking infima proves \(\inf F=\inf L\).

If \((X,Y,S)\in G_F\), then (2) implies
\[
\inf L\le L(XY^\top,S)\le F(X,Y,S)=\inf F=\inf L.
\]
Thus \((XY^\top,S)\in G_L\). Conversely, a padded compact-SVD lift of any \((Z,S)\in G_L\) attains equality in (2), and is therefore in \(G_F\). This proves
\[
G_L=\{(XY^\top,S):(X,Y,S)\in G_F\},
\]
and gives the asserted lift of every global minimizer.

## Bounded models

Let \(Z\in\mathcal B^Z\). In the compact-SVD lift above, each nonzero factor column has norm \(\sqrt{\sigma_i(Z)}\), so
\[
\| (X_Z)_i\|_2,\ \|(Y_Z)_i\|_2\le\sqrt{\|Z\|_2}
\le\|\mathcal B^Z\|_{\max}^{1/2}\le\tau.
\tag{3}
\]
Consequently every feasible point of \(L_B\) has an equality-attaining lift feasible for \(F_B\), so \(V_{F_B}\le V_{L_B}\). Since the feasible set of \(F_B\) is contained in that of \(F\),
\[
V_L=V_F\le V_{F_B}\le V_{L_B}.
\]
The assumption \((\mathcal B^Z\times\mathcal B^S)\cap G_L\ne\varnothing\) gives \(V_{L_B}=V_L\). Hence
\[
V_{L_B}=V_{F_B}=V_L.
\]
An equality-attaining bounded lift of a minimizer of \(L_B\) is a minimizer of \(F_B\). A minimizer of \(F_B\) is feasible for \(F\), has value \(V_L\), and therefore projects to a member of \(G_L\). Thus
\[
G_{L_B}\subseteq\{(XY^\top,S):(X,Y,S)\in G_{F_B}\}\subseteq G_L.
\]

## Local-minimizer lifting

Let \((\bar Z,\bar S)\) be a local minimizer of \(L\), and choose its padded compact-SVD lift \((\bar X,\bar Y)\). Equality holds in (2) at this lift. By continuity of \((X,Y)\mapsto XY^\top\), all sufficiently near factor pairs have products in a neighborhood on which \((\bar Z,\bar S)\) minimizes \(L\). Therefore, for all sufficiently near feasible \((X,Y,S)\),
\[
F(X,Y,S)\ge L(XY^\top,S)\ge L(\bar Z,\bar S)
=F(\bar X,\bar Y,\bar S).
\]
Hence \((\bar X,\bar Y,\bar S)\) is a local minimizer of \(F\).

## Stationary-point lifting

For a feasible \((Z,S)\), write \(q=\operatorname{rank}(Z)\), \(I=I_S\), and
\[
\mathcal Q_{\lambda,Z}=
\{W:\operatorname{rank}(W)\le r,\ \lambda\operatorname{rank}(W)=\lambda q\}.
\]
If \(\lambda>0\), this is the rank-\(q\) manifold. If \(Z=U\Sigma V^\top\) is compact, its normal space is
\[
N_{\mathcal R_q}(Z)=
\{U_\perp M V_\perp^\top:M\in\mathbb R^{(m-q)\times(n-q)}\}.
\tag{4}
\]
Indeed, differentiating a full-rank local parametrization of the rank-\(q\) manifold gives the tangent space
\[
\{UAV^\top+U_\perp BV^\top+UCV_\perp^\top:A,B,C\ \text{arbitrary}\},
\]
whose orthogonal complement is exactly (4). For \(\lambda=0\), the standard rank-set inclusion used here is
\[
N_{\{W:\operatorname{rank}(W)\le r\}}(Z)\subseteq N_{\mathcal R_q}(Z).
\tag{5}
\]

Suppose \((\bar Z,\bar S)\in\mathcal S_L\). There is \((H_Z,H_S)\in\partial\Phi(\bar Z,\bar S)\) with
\[
-H_Z\in N_{\mathcal Q_{\lambda,\bar Z}}(\bar Z),
\qquad
-H_S\in N_{\mathcal T_{I_{\bar S}}}(\bar S).
\tag{6}
\]
By (4)--(5), \(H_Z\) is orthogonal to the left and right singular spaces of \(\bar Z\). For the padded compact-SVD lift \((\bar X,\bar Y)\), this gives
\[
H_Z\bar Y=0,\qquad H_Z^\top\bar X=0.
\tag{7}
\]
If \(\lambda>0\), the active factor-column sets are the first \(q\) columns; if \(\lambda=0\), they are all columns. In either case, (7) gives
\[
-H_Z\bar Y\in N_{\mathcal C^m_{J_{\bar X}}}(\bar X),
\qquad
-H_Z^\top\bar X\in N_{\mathcal C^n_{J_{\bar Y}}}(\bar Y).
\]
Together with the second condition in (6), these are the three factor stationarity conditions. Thus every member of \(\mathcal S_L\) has a padded-SVD lift in \(\mathcal S_F\).

## Converse stationary projection for \(\lambda>0\)

Let \((X,Y,S)\in\mathcal S_F\), let \(J_X,J_Y\) be its active-column sets, and put \(A=J_X\cap J_Y\). Factor stationarity supplies \((H_Z,H_S)\in\partial\Phi(XY^\top,S)\) such that
\[
-H_ZY\in N_{\mathcal C^m_{J_X}}(X),\qquad
-H_Z^\top X\in N_{\mathcal C^n_{J_Y}}(Y),\qquad
-H_S\in N_{\mathcal T_{I_S}}(S).
\tag{8}
\]
The normal to \(\mathcal C^m_{J_X}\) vanishes on columns in \(J_X\), and analogously for \(Y\). Hence
\[
H_ZY_A=0,\qquad H_Z^\top X_A=0.
\tag{9}
\]
Since columns outside \(A\) make no contribution to the product,
\[
Z:=XY^\top=X_AY_A^\top.
\]
Equations (9) imply
\[
ZH_Z^\top=X_A(H_ZY_A)^\top=0,
\qquad
H_Z^\top Z=(H_Z^\top X_A)Y_A^\top=0.
\tag{10}
\]
Let \(Z=U\Sigma V^\top\) be compact. From (10), \(H_ZV=0\) and \(U^\top H_Z=0\), so \(H_Z=U_\perp M V_\perp^\top\) for some \(M\). By (4),
\[
-H_Z\in N_{\mathcal R_{\operatorname{rank}(Z)}}(Z).
\]
When \(\lambda>0\), \(\mathcal Q_{\lambda,Z}=\mathcal R_{\operatorname{rank}(Z)}\), so the first original-model stationarity condition follows. The \(S\)-condition in (8) is unchanged by projection. Therefore \((XY^\top,S)\in\mathcal S_L\). Combined with the lifting result,
\[
\mathcal S_L=\{(XY^\top,S):(X,Y,S)\in\mathcal S_F\}
\qquad(\lambda>0).
\]
