# Problem

## Setup

Let \(G\subseteq\mathrm{GL}(n,\mathbb R)\) be a matrix Lie group with Lie algebra \(\mathfrak g\subseteq\mathbb R^{n\times n}\), where \(\dim\mathfrak g\ge1\). Equip the ambient matrix space and \(\mathfrak g\) with the Frobenius inner product. Let \(H\subseteq G\) be closed, and let \(M=G/H\) have a transitive action of \(G\).

Consider a discounted Markov decision process on \(M\), with compact action space \(\mathcal A\subseteq\mathfrak g\), Markov transition kernel \(P\), a fixed initial-state distribution \(\nu\), measurable rewards satisfying \(|r(s,a)|\le R_{\max}<\infty\), and discount \(\gamma\in[0,1)\). The action-to-group map used by the dynamics is \(a\mapsto\exp(a)\).

Use a Gaussian exploration proposal with fixed scale \(\sigma>0\) and bounded executed noise. More precisely, for fixed \(B_a>0\), define
\[
C_{B_a}(x)=
\begin{cases}
x,&\|x\|_F\le B_a,\\
B_a x/\|x\|_F,&\|x\|_F>B_a.
\end{cases}
\]
At state \(s\), the policy \(\pi_\theta\) executes
\[
a=\mu_\theta(s)+C_{B_a}(\xi),\qquad
\xi\sim\mathcal N(0,\sigma^2I)
\]
in orthonormal Frobenius coordinates on \(\mathfrak g\), with fresh proposal noise conditional on the state. Here \(\mu_\theta(s)\in\mathfrak g\), and the executed actions belong to \(\mathcal A\). The Gaussian covariance refers to the proposal before clipping. Assume these policies and the transition kernel define the trajectory laws, and put
\[
J(\theta)=\mathbb E_{\nu,\pi_\theta,P}\left[\sum_{k=0}^{\infty}\gamma^k r(s_k,a_k)\right],
\qquad J^*=\sup_{\theta\in\mathfrak g}J(\theta)<\infty.
\]

Let \(P_{\mathfrak g}\) denote the Frobenius-orthogonal projector onto \(\mathfrak g\). Fix \(\theta_0\in\mathfrak g\) deterministically. Let \((\mathcal F_t)\) be a filtration representing the history before the estimator for update \(t\) is sampled. The parameter \(\theta_t\) is \(\mathcal F_t\)-measurable, and the ambient matrix-valued estimator \(\widehat g_t\) is \(\mathcal F_{t+1}\)-measurable, with
\[
\mathbb E[\widehat g_t\mid\mathcal F_t]=\nabla J(\theta_t),\qquad
\mathbb E[\|\widehat g_t-\nabla J(\theta_t)\|_F^2\mid\mathcal F_t]\le\sigma_g^2
\]
for a fixed \(0\le\sigma_g<\infty\).

For the ambient gradient notation, assume \(J\) has a continuously differentiable extension to an open neighborhood of the parameter ball
\[
K=\{\theta\in\mathfrak g:\|\theta\|_F\le B_\theta\},
\]
where \(B_\theta<\infty\) is deterministic. Assume that, for a fixed \(L>0\),
\[
\|\nabla J(\theta)-\nabla J(\theta')\|_F\le L\|\theta-\theta'\|_F
\quad(\theta,\theta'\in K).
\]
Define \(d_t=P_{\mathfrak g}\nabla J(\theta_t)\), and use deterministic positive step sizes in the recursion
\[
\theta_{t+1}=\theta_t+\eta_tP_{\mathfrak g}\widehat g_t,
\qquad 0<\eta_t\le1/L.
\]
Assume all iterates of the run under consideration belong to \(K\) almost surely.

For an infinite-horizon run, assume
\[
\sum_{t=0}^{\infty}\eta_t=\infty,
\qquad \sum_{t=0}^{\infty}\eta_t^2<\infty.
\]
Separately, for a fixed-horizon run with integer \(T\ge1\), use \(\eta_t=\eta/\sqrt T\) for \(0\le t<T\), where \(0<\eta\le1/L\); the infinite-horizon summability conditions are not imposed on this finite schedule.

Let \(F_t\) be measurable symmetric positive-definite operators on \(\mathfrak g\), possibly random and dependent on the iterates. In orthonormal Frobenius coordinates, write their smallest and largest eigenvalues as
\[
0<\lambda_{\min,t}\le\lambda_{\max,t}<\infty,
\qquad \kappa_t=\lambda_{\max,t}/\lambda_{\min,t},
\qquad n_t=F_t^{-1}d_t.
\]
For \(d_t\ne0\), define
\[
\alpha_t=\frac{\langle d_t,n_t\rangle_F}{\|d_t\|_F\|n_t\|_F}.
\]
For each finite horizon define the deterministic number
\[
m_T=\operatorname{ess\,inf}_{\omega}\min_{0\le t<T}\lambda_{\min,t}(\omega).
\]
Here the essential infimum is the greatest almost-sure lower bound, with respect to the probability law of the run. It may be zero. Expectations of nonnegative quadratic forms or inverse-eigenvalue-weighted squared norms are interpreted as extended nonnegative integrals.

## Task

Prove the following integrated theorem.

For the infinite-horizon schedule, \(J(\theta_t)\) converges almost surely and
\[
\sum_{t=0}^{\infty}\eta_t\mathbb E\|d_t\|_F^2<\infty,
\qquad
\sum_{t=0}^{\infty}\eta_t\|d_t\|_F^2<\infty\quad\text{almost surely}.
\]
For the fixed-horizon schedule,
\[
\frac1T\sum_{t<T}\mathbb E\|d_t\|_F^2
\le\frac{2(J^*-J(\theta_0))}{\eta\sqrt T}+\frac{L\eta\sigma_g^2}{\sqrt T}.
\]
Moreover, almost surely at each iterate,
\[
\frac{\|d_t\|_F^2}{\lambda_{\max,t}}
\le\langle d_t,F_t^{-1}d_t\rangle_F
\le\frac{\|d_t\|_F^2}{\lambda_{\min,t}},
\]
and for every finite horizon,
\[
\frac1T\sum_{t<T}\mathbb E\langle d_t,F_t^{-1}d_t\rangle_F
\le\frac1T\sum_{t<T}\mathbb E\left[\frac{\|d_t\|_F^2}{\lambda_{\min,t}}\right].
\]
Whenever \(m_T>0\), also prove
\[
\frac1T\sum_{t<T}\mathbb E\langle d_t,F_t^{-1}d_t\rangle_F
\le\frac1{m_T}\frac1T\sum_{t<T}\mathbb E\|d_t\|_F^2.
\]
Finally, almost surely whenever \(d_t\ne0\), prove
\[
\alpha_t\ge\frac{2\sqrt{\kappa_t}}{\kappa_t+1}.
\]
All quadratic forms and operator coordinates use the Frobenius inner product.
