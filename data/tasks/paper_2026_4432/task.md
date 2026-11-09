# Problem

## Setup

Let \(K\geq2\) and \(d\geq1\) be integers, let \(I_d\) denote the \(d\times d\) identity matrix, and let \(\alpha_1,\ldots,\alpha_K>0\). For probability densities \(p^{(1)},\ldots,p^{(K)}\) on \(\mathbb R^d\), define their product-of-experts density by
\[
P(p^{(1)},\ldots,p^{(K)})(x)=\frac{\left(\prod_{k=1}^K p^{(k)}(x)\right)^{1/K}}{\int_{\mathbb R^d}\left(\prod_{k=1}^K p^{(k)}(u)\right)^{1/K}\,du},
\]
whenever the normalizing integral is finite and nonzero.

Let each initial component law be \(p^{(k)}_0=\mathcal N(0,\alpha_k I_d)\). Fix a deterministic, measurable, locally integrable function \(\beta:[0,\infty)\to[0,\infty)\) such that
\[
\int_0^t\beta_s\,ds>0\qquad\text{for every }t>0.
\]
Evolve laws using the same variance-preserving SDE
\[
dz_t=-\beta_t z_t\,dt+\sqrt{2\beta_t}\,dw_t,
\]
where \(w_t\) is a standard \(d\)-dimensional Wiener process independent of the initial state.

## Task

Prove the following theorem. For every \(t>0\), let \(A_t\) be the time-\(t\) law obtained by first forming \(P(p^{(1)}_0,\ldots,p^{(K)}_0)\) and then diffusing, and let \(B_t=P(p^{(1)}_t,\ldots,p^{(K)}_t)\), where \(p^{(k)}_t\) is the separately diffused \(k\)-th component. Then
\[
A_t=B_t\quad\Longleftrightarrow\quad\alpha_1=\cdots=\alpha_K.
\]
