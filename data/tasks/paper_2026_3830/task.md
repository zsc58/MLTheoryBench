# Problem

## Setup

Let \(E,p,k\) be fixed integers with \(E\geq1\) and \(1\leq k<p\). For each domain \(e\in\{1,\ldots,E\}\), let \(x_e\in\mathbb R^p\) be a zero-mean random vector with finite covariance \(\Sigma_e\), where \(\Sigma_e\) is symmetric positive semidefinite and \(\operatorname{Tr}(\Sigma_e)>0\). Choose an orthonormal top-\(k\) eigenbasis \(W_e\in\mathbb R^{p\times k}\) of \(\Sigma_e\), and write \(\Pi_k^{(e)}=W_eW_e^\top\). These choices, including choices at eigenvalue ties, are fixed throughout.

Define
\[
\operatorname{St}(p,k)=\{W\in\mathbb R^{p\times k}:W^\top W=I_k\},\qquad
\Pi_W=WW^\top,
\]
\[
\overline\Sigma=\frac1E\sum_{e=1}^E\Sigma_e,\qquad
\overline\Pi=\frac1E\sum_{e=1}^E\Pi_k^{(e)}.
\]
Here \(\|H\|_F=\sqrt{\operatorname{Tr}(H^\top H)}\) and \(\|H\|_{\mathrm{op}}=\sup_{\|v\|_2=1}\|Hv\|_2\). For a subspace \(S\), let \(\Pi_S\) denote its orthogonal projector.

Let
\[
S_*:=\bigcap_{e=1}^E\operatorname{Im}(\Pi_k^{(e)}),\qquad
m:=\dim(S_*),
\]
and assume \(1\leq m\leq k\). Define the compressed covariance operator
\[
A_*:S_*\longrightarrow S_*,\qquad
A_*v:=\Pi_{S_*}\overline\Sigma v.
\]
Let \(\mu_1\geq\cdots\geq\mu_m\) be its eigenvalues, counted with multiplicity, and fix an orthonormal eigenbasis \(s_1,\ldots,s_m\) of \(S_*\) satisfying \(A_*s_i=\mu_i s_i\).

For \(\lambda>0\), a soft optimizer is any maximizer over \(W\in\operatorname{St}(p,k)\) of
\[
\operatorname{Tr}(W^\top\overline\Sigma W)
-\lambda\sum_{e=1}^E\|\Pi_W-\Pi_k^{(e)}\|_F^2.
\]
A hard optimizer \(W_\infty\in\operatorname{St}(p,k)\) is defined lexicographically: first maximize \(\operatorname{Tr}(W^\top\overline\Pi W)\), then maximize \(\operatorname{Tr}(W^\top\overline\Sigma W)\) among those maximizers.

For each \(\lambda>0\), define
\[
M_\lambda=\overline\Sigma+2E\lambda\overline\Pi.
\]
Write its ordered eigenvalues as \(\lambda_1(M_\lambda)\geq\cdots\geq\lambda_p(M_\lambda)\), counted with multiplicity, and choose any orthonormal eigenvectors \(w_1^\lambda,\ldots,w_k^\lambda\) satisfying \(M_\lambda w_i^\lambda=\lambda_i(M_\lambda)w_i^\lambda\). Choices within tied eigenspaces may be arbitrary. Let \(P_\lambda\) be the orthogonal projector onto \(\operatorname{span}(w_1^\lambda,\ldots,w_m^\lambda)\).

## Task

Prove the following integrated theorem.

Every hard optimizer satisfies
\[
S_*\subseteq\operatorname{Im}(W_\infty).
\]
Its solution subspace admits an orthonormal representative basis whose first \(m\) vectors are \(s_1,\ldots,s_m\), ordered by the corresponding eigenvalues \(\mu_1\geq\cdots\geq\mu_m\).

For every choice of the ordered eigenvectors specified above,
\[
\|P_\lambda-\Pi_{S_*}\|_{\mathrm{op}}\longrightarrow0
\qquad\text{as }\lambda\longrightarrow\infty.
\]

If \(\mu_1>\cdots>\mu_m\), then, for every \(i\leq m\),
\[
\lambda_i(M_\lambda)-2E\lambda\longrightarrow\mu_i,
\]
and there exist signs \(\varepsilon_i(\lambda)\in\{-1,1\}\) such that
\[
\varepsilon_i(\lambda)w_i^\lambda\longrightarrow s_i
\qquad\text{as }\lambda\longrightarrow\infty.
\]
