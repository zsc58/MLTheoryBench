# Problem

## Setup

Let \(d\in\mathbb N\), \(K\in\mathbb N\), and let \(\rho_1\in\mathcal P_2(\mathbb R^d)\). Let \(X_0\sim\rho_0:=N(0,I_d)\) and \(X_1\sim\rho_1\) be independent. Define the linear interpolation and velocity
\[
X_t=(1-t)X_0+tX_1,\qquad V=X_1-X_0,\qquad t\in[0,1].
\]
Let \(\pi(\cdot\mid x,t)\) denote a regular conditional law of \(V\) given \(X_t=x\). For a conditional source law \(Q(\cdot\mid x,t)\), define its boundary transport cost by
\[
D(Q):=\left(\mathbb E_{X_0\sim\rho_0}\left[W_2^2\bigl(Q(\cdot\mid X_0,0),\pi(\cdot\mid X_0,0)\bigr)\right]\right)^{1/2}.
\]

Let \(\widetilde\rho_1\in\mathcal P_2(\mathbb R^d)\) be a deployed \(K\)-component surrogate satisfying the compression assumption
\[
W_2(\rho_1,\widetilde\rho_1)\le C_QK^{-1/d},
\]
where \(C_Q\) is independent of \(K\). Define two boundary source laws by
\[
Q_S(\cdot\mid x,0)=\operatorname{Law}(\widetilde X_1-x),\quad \widetilde X_1\sim\widetilde\rho_1,
\]
and
\[
Q_G(\cdot\mid x,0)=N(0,I_d).
\]
Finally set
\[
\sigma_1^2:=\frac{1}{d}\mathbb E\|X_1\|^2.
\]

## Task

Prove the following integrated theorem:
\[
D(Q_S)=W_2(\rho_1,\widetilde\rho_1)\le C_QK^{-1/d},
\]
and
\[
D(Q_G)\ge \sqrt d\,\bigl(\sqrt{\sigma_1^2+1}-1\bigr).
\]
