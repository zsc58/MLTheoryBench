# Problem

## Setup

Let \(J,m_j,n_j\) be positive integers with \(m_j\le n_j\), and let
\[
\mathcal X=\prod_{j=1}^J\mathbb R^{m_j\times n_j}.
\]
For tuples \(A,B\in\mathcal X\), write \(\langle A,B\rangle=\sum_j\operatorname{Tr}(A_j^TB_j)\). For \(r\in[1,\infty]\), let \(\|Z\|_{S_r}\) be the \(\ell_r\)-norm of the singular values of \(Z\), with the maximum norm at \(r=\infty\). Fix conjugate exponents \(\alpha\in[2,\infty]\), \(\beta\in[1,2]\), and for every block conjugate \(p_j\in[2,\infty]\), \(q_j\in[1,2]\), where conjugacy means that the reciprocals sum to one and \(1/\infty=0\). For positive weights \(L_j\), define
\[
\|X\|_{w,p}=\big\|(L_j^{1/2}\|X_j\|_{S_{p_j}})_j\big\|_{\alpha},\qquad
\|M\|_{v,q}=\big\|(L_j^{-1/2}\|M_j\|_{S_{q_j}})_j\big\|_{\beta}.
\]
These norms are dual under the displayed inner product. Fix a Borel-measurable ball-oracle selection
\[
\Delta^b_{w,p}(M)\in\arg\min_{\|Z\|_{w,p}\le1}\langle M,Z\rangle.
\]

Assume \(f:\mathcal X\to\mathbb R\) is differentiable and bounded below by a finite constant \(f_{\rm low}\). Assume its gradient satisfies
\[
\|\nabla f(Y)-\nabla f(X)\|_{v,q}\le\|Y-X\|_{w,p}
\qquad\text{for every }X,Y\in\mathcal X.
\]
Let \(G:\mathcal X\times\Xi\to\mathcal X\) be a measurable stochastic estimator, where \(\xi\) has a fixed probability law on \(\Xi\). Suppose there are fixed matrices \(V_j\in\mathbb R^{m_j\times m_j}\) such that, for every \(X\in\mathcal X\),
\[
\mathbb E_{\xi}G(X;\xi)=\nabla f(X),\qquad
\mathbb E_{\xi}\big[(G_j(X;\xi)-\nabla_j f(X))(G_j(X;\xi)-\nabla_j f(X))^T\big]\preceq V_jV_j^T
\quad(1\le j\le J),
\]
where \(\nabla_j f(X)\) denotes the \(j\)-th gradient block and \(\preceq\) is the positive-semidefinite order.

Fix an integer \(B\ge1\) and a deterministic starting point \(X_0\in\mathcal X\). All samples \(\xi_{k,i}\), \(k\ge0\), \(1\le i\le B\), are independent copies of \(\xi\); at iteration \(k\) they are drawn after \(X_k\) is formed. For parameters \(\theta\in(0,1]\) and \(\eta>0\), set
\[
\bar G_k=B^{-1}\sum_{i=1}^BG(X_k;\xi_{k,i}),\qquad
M_0=\bar G_0,\qquad M_k=(1-\theta)M_{k-1}+\theta\bar G_k\quad(k\ge1),
\]
and update
\[
X_{k+1}=X_k+\eta\,\Delta^b_{w,p}(M_k).
\]
Let \(\Delta_f=f(X_0)-f_{\rm low}>0\) and
\[
\sigma_{v,q,B}=B^{-1/2}\big\|(L_j^{-1/2}\|V_j\|_{S_{q_j}})_j\big\|_{\beta}.
\]

## Task

Prove that for every integer \(K\ge1\), choosing
\[
\eta=\sqrt{\Delta_f\theta/K},\qquad
\theta=\min\{\sigma_{v,q,B}^{-1}\sqrt{\Delta_f/K},1\}
\]
(with \(\theta=1\) when \(\sigma_{v,q,B}=0\)), the iterates satisfy
\[
\frac1K\sum_{k=0}^{K-1}\mathbb E\,\|\nabla f(X_k)\|_{v,q}
\le 6\sqrt{\sigma_{v,q,B}}\left(\frac{\Delta_f}{K}\right)^{1/4}
+8\sqrt{\frac{\Delta_f}{K}}
+\frac{2\sigma_{v,q,B}^{2}}{\sqrt{\Delta_f K}}.
\]
The expectation is over the sampled mini-batches.
