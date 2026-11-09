# Problem

## Setup

Fix an integer T\geq1 and \delta\in(0,1). Let \Theta\subseteq\mathbb R^d, d\geq1, be nonempty, compact, and convex, and let (\mathcal F_t)_{t\geq0} be a filtration with trivial \mathcal F_0. At time t+1 a sample X_{t+1}, measurable with respect to \mathcal F_{t+1}, is observed and g_{t+1}=\nabla h(\theta_t,X_{t+1}), where \theta_t\in\Theta is \mathcal F_t-measurable. For x\in\Theta define the finite conditional risk H_{t+1}(x)=\mathbb E[h(x,X_{t+1})\mid\mathcal F_t], conditional mean gradient \bar g_{t+1}(x)=\mathbb E[\nabla h(x,X_{t+1})\mid\mathcal F_t], and conditional coordinatewise second moment s_{t+1}(x)=\mathbb E[(\nabla h(x,X_{t+1}))^{\odot2}\mid\mathcal F_t]. Assume these conditional quantities admit \mathcal F_t-measurable versions. For t\geq1 let \theta_t^* be an \mathcal F_{t-1}-measurable minimizer of H_t in the interior of \Theta, with \bar g_t(\theta_t^*)=0. Fix \mathcal F_0-measurable \theta_0,\theta_0^*\in\Theta, and set \Delta_t=\|\theta_{t+1}^*-\theta_t^*\|.

Assume 0<\beta_1,\beta_2<1, \epsilon,G,L,\sigma,\mu,\alpha>0. Almost surely, at every time, \sup_{x\in\Theta}\|\nabla h(x,X_{t+1})\|\leq G and \|\bar g_{t+1}(x)-\bar g_{t+1}(y)\|\leq L\|x-y\| for all x,y\in\Theta. Write \xi_{t+1}=g_{t+1}-\bar g_{t+1}(\theta_t). Assume, conditionally on \mathcal F_t, \mathbb E[\exp(\langle u,\xi_{t+1}\rangle^2/\sigma^2)\mid\mathcal F_t]\leq2 for every deterministic unit vector u\in\mathbb R^d.

Initialize m_0=v_0=0 and run
\[
m_{t+1}=\beta_1m_t+(1-\beta_1)g_{t+1},\quad v_{t+1}=\beta_2v_t+(1-\beta_2)g_{t+1}^{\odot2},
\]
\[
\widehat m_{t+1}=m_{t+1}/(1-\beta_1^{t+1}),\quad \widehat v_{t+1}=v_{t+1}/(1-\beta_2^{t+1}),
\]
\[
P_{t+1}=\operatorname{Diag}((\sqrt{\widehat v_{t+1}}+\epsilon)^{-1}),\qquad
\theta_{t+1}=\Pi_\Theta(\theta_t-\alpha P_{t+1}\widehat m_{t+1}),
\]
where \Pi_\Theta is Euclidean projection. Set q_-=(G+\epsilon)^{-1}, q_+=\epsilon^{-1}, \widetilde v_{t+1}=\mathbb E[v_{t+1}\mid\mathcal F_t], and \widetilde P_{t+1}=\operatorname{Diag}((\sqrt{\widetilde v_{t+1}}+\epsilon)^{-1}). Assume, almost surely for all t\geq0 and x,y\in\Theta,
\[
\langle x-y,\widetilde P_{t+1}(\bar g_{t+1}(x)-\bar g_{t+1}(y))\rangle\geq q_-\mu\|x-y\|^2.
\]
For i\in\{1,2\} and 0\leq k\leq t-1, let
\[
w_{i,t,k}=\frac{(1-\beta_i)\beta_i^{t-1-k}}{1-\beta_i^t},\quad
\kappa_{1,t}=\frac{(1-\beta_1)(1+\beta_1^t)}{(1+\beta_1)(1-\beta_1^t)},
\]
\[
c_{1,t}=\frac{\beta_1}{1-\beta_1}-\frac{t\beta_1^t}{1-\beta_1^t},\quad
\omega_{1,t}=\frac{1-\beta_1}{1-\beta_1^t},\quad
\vartheta_{2,t}=\beta_2^t+1-\beta_2,\quad D_1(a)=aLG/\epsilon+2G\quad(a>0),
\]
and, for the step size \alpha,
\[
R_t=c_{1,t}D_1(\alpha)+\sigma\sqrt{2d\kappa_{1,t}\log(2T/\delta)}+\frac{4G}{3}\omega_{1,t}\log(2T/\delta).
\]

## Task

Assume \alpha\leq\alpha_{\max}:=\min\{q_-\mu/(4q_+^2L^2),(q_-\mu)^{-1}\}. Prove that, with probability at least 1-\delta, simultaneously for every integer 0\leq t\leq T,
\[
\|\theta_t-\theta_t^*\|^2\leq \rho^t\|\theta_0-\theta_0^*\|^2+\sum_{\ell=0}^{t-1}\rho^{t-1-\ell}\left[\frac{5\Delta_\ell^2}{\alpha q_-\mu}+\frac{10\alpha q_+^2}{q_-\mu}R_{\ell+1}^2+\frac{10\alpha G^4\epsilon^{-4}}{q_-\mu}\vartheta_{2,\ell+1}\right],
\]
where \rho=1-\alpha q_-\mu/2.

If \Delta_t\leq\Delta for all t for a fixed \Delta\geq0, put b=q_-\mu, h=\log(2T/\delta), and, for 0<a\leq\alpha_{\max},
\[
A(a,\delta,T)=\frac{\beta_1D_1(a)}{1-\beta_1}+\sigma\sqrt{\frac{2d(1-\beta_1)}{1+\beta_1}h}+\frac{4G}{3}(1-\beta_1)h,
\]
\[
F(a,\delta,T)=\frac{10\Delta^2}{a^2b^2}+\frac{20q_+^2}{b^2}A(a,\delta,T)^2+\frac{20G^4\epsilon^{-4}}{b^2}(1-\beta_2).
\]
Prove the uniform bound \|\theta_t-\theta_t^*\|^2\leq\rho^t\|\theta_0-\theta_0^*\|^2+F(\alpha,\delta,T) for 0\leq t\leq T, and the bound 2F(\alpha,\delta,T) after
\[
t\geq\left\lceil\frac{\log_+(\|\theta_0-\theta_0^*\|^2/F(\alpha,\delta,T))}{-\log\rho}\right\rceil,
\]
within the horizon. Here \log_+(0)=0 and \log_+(x)=\max\{0,\log x\} for x>0.

For the restarted schedule, suppose there are an integer K\geq2 and \alpha^*\in(0,\alpha_{\max}) such that \alpha^* minimizes F(a,\delta/K,T) over 0<a\leq\alpha_{\max} and K=1+\lceil\log_2(\alpha_{\max}/\alpha^*)\rceil. Fix such a pair. Set \alpha_0=\alpha_{\max} and \alpha_j=\alpha^*+(\alpha_0-\alpha^*)2^{-j} for 0\leq j<K. At each epoch reset m=v=0 and the bias-correction indices, use step size \alpha_j, and assign confidence \delta/K. Define F_j=F(\alpha_j,\delta/K,T), \rho_j=1-\alpha_jb/2, e_0=\|\theta_0-\theta_0^*\|^2, and fixed epoch lengths
\[
n_0=\max\left\{1,\left\lceil\frac{2}{b\alpha_0}\log_+\frac{2e_0}{F_0}\right\rceil\right\},\qquad
n_j=\max\left\{1,\left\lceil\frac{2\log8}{b\alpha_j}\right\rceil\right\}\quad(1\leq j<K).
\]
Assume the specified horizon T contains these epochs, and write s_0=0, s_{j+1}=s_j+n_j. In the restarted-run assertion, \theta_t and g_{t+1}=\nabla h(\theta_t,X_{t+1}) denote that run's iterates and gradients. For each epoch j, write v_k^{(j)} for its uncorrected second moment after k local steps, with v_0^{(j)}=0. At global time t=s_j+k, 0\leq k<n_j, its predictable preconditioner is
\[
\widetilde P_{k+1}^{(j)}=\operatorname{Diag}\!\left(\left(\sqrt{\beta_2v_k^{(j)}+(1-\beta_2)s_{t+1}(\theta_t)}+\epsilon\right)^{-1}\right).
\]
Assume for this restarted run, almost surely for every j, every 0\leq k<n_j, and all x,y\in\Theta,
\[
\langle x-y,\widetilde P_{k+1}^{(j)}(\bar g_{t+1}(x)-\bar g_{t+1}(y))\rangle\geq q_-\mu\|x-y\|^2,\qquad t=s_j+k.
\]
Also assume for its iterates, every such t, and every deterministic unit vector u, that
\[
\mathbb E\!\left[\exp\!\left(\langle u,g_{t+1}-\bar g_{t+1}(\theta_t)\rangle^2/\sigma^2\right)\middle|\mathcal F_t\right]\leq2.
\]
Prove that, with probability at least 1-\delta, every epoch endpoint satisfies \|\theta_{s_{j+1}}-\theta_{s_{j+1}}^*\|^2\leq2F_j; show that the final endpoint is at most a constant multiple of F(\alpha^*,\delta/K,T) and that
\[
s_K=O\!\left(\frac{1+\log_+(e_0/F_0)}{b\alpha_0}+\frac{1}{b\alpha^*}\right).
\]
The assertion about an optimizing step size is conditional on the stated pair's existence.
