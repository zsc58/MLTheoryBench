# Problem

## Setup

Let \((X,Y)\in\mathbb R^d\times\mathbb R\) have finite second moments and be centered. Assume that \(\Sigma=\mathbb E[XX^T]\) is positive definite. Define
\[
 \beta_0=\Sigma^{-1}\mathbb E[XY],\qquad
 \tau^2=\mathbb E[(Y-\beta_0^TX)^2].
\]

A linear rule \((\beta,b)\in\mathbb R^d\times\mathbb R\) is deployed after an individual chooses an action \(a\in\mathbb R^d\). The individual receives score \(\beta^T(X+a)+b\) and pays cost \(\tfrac12a^TCa\), where \(C\in\mathbb R^{d\times d}\) is a fixed symmetric positive-definite matrix. Thus the best response is \(a=C^{-1}\beta\). Define the resulting risk
\[
 \mathcal R(\beta,b)=\mathbb E\!\left[\bigl(\beta^T(X+C^{-1}\beta)+b-Y\bigr)^2\right],
 \qquad
 \mathcal O=\min_{\beta\in\mathbb R^d,\,b\in\mathbb R}\mathcal R(\beta,b).
\]

For \(J\subseteq[d]\), let \(\Theta(J)=\{\beta\in\mathbb R^d:\beta_{J^c}=0\}\). For nonempty \(J\), define the support-restricted ordinary-ridge coefficient by
\[
 \widehat\beta_J(J,\lambda)=(\Sigma_{JJ}+\lambda I)^{-1}\mathbb E[X_JY],
 \qquad
 \widehat\beta_{J^c}(J,\lambda)=0,
 \qquad \lambda\ge0.
\]
For \(J=\varnothing\), define \(\widehat\beta(\varnothing,\lambda)=0\) for every \(\lambda\ge0\). Its fitted intercept is zero. Define the zero-intercept benchmarks
\[
 \mathcal V=\min_{\beta\in\mathbb R^d}\mathcal R(\beta,0),
 \qquad
 \mathcal V(J)=\min_{\beta\in\Theta(J)}\mathcal R(\beta,0).
\]

For nonempty \(J\), let \(R=[d]\setminus J\),
\[
 m_J=\Sigma_{JJ}^{-1}\mathbb E[X_JY],
 \qquad
 p(J)=\beta_{0,R}^T
 \bigl(\Sigma_{RR}-\Sigma_{RJ}\Sigma_{JJ}^{-1}\Sigma_{JR}\bigr)\beta_{0,R},
\]
where the expression for \(p(J)\) is defined to be zero when \(J=[d]\). Define
\[
 g(J)=\min_{\eta\in\mathbb R^{|J|}}
 \left\{(\eta-m_J)^T\Sigma_{JJ}(\eta-m_J)
 +\bigl(\eta^T(C^{-1})_{JJ}\eta\bigr)^2\right\},
\]
\[
 h(J)=\inf_{\gamma\ge0}
 \left\|\Sigma_{JJ}^{-1/2}\bigl((C^{-1})_{JJ}-\gamma I\bigr)\Sigma_{JJ}^{-1/2}\right\|_{\rm op},
\]
\[
 A_C(J)=1+6\left\|\Sigma_{JJ}^{-1/2}(C^{-1})_{JJ}\Sigma_{JJ}^{-1/2}\right\|_{\rm op}^{2}
 \left\|\Sigma_{JJ}^{1/2}m_J\right\|_2^2,
\]
\[
 B_C(J)=4A_C(J)
 \left\|\Sigma_{JJ}^{-1/2}(C^{-1})_{JJ}\Sigma_{JJ}^{-1/2}\right\|_{\rm op}^{2}
 \left\|\Sigma_{JJ}^{1/2}m_J\right\|_2^6.
\]
For the empty support, set
\[
 p(\varnothing)=\beta_0^T\Sigma\beta_0,
 \qquad
 g(\varnothing)=h(\varnothing)=B_C(\varnothing)=0.
\]

## Task

Prove the following integrated claim.

For every \(J\subseteq[d]\) and every \(\lambda\ge0\),
\[
 \mathcal R(\widehat\beta(J,\lambda),0)-\mathcal O
 \ge \mathcal V-\mathcal O.
\]
Moreover, for every \(J\subseteq[d]\),
\[
 \min_{\lambda\ge0}\mathcal R(\widehat\beta(J,\lambda),0)-\mathcal V
 \le p(J)-[g([d])-g(J)]+B_C(J)h(J)^2.
\]
Consequently, for any \(J\subseteq[d]\) and any real \(\epsilon\), if the right-hand side is at most \(\epsilon\), then a ridge rule supported on \(J\) has risk at most \(\mathcal V+\epsilon\), and hence at most \(\mathcal O+(\mathcal V-\mathcal O)+\epsilon\).
