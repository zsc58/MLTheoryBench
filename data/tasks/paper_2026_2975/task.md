# Problem

## Setup

Fix an integer \(D\geq1\), an assimilation time \(t\), an observed history through time \(t\), and a new observation at time \(t+1\). These observations are fixed throughout. Work on \(\mathcal C=C([t,t+1],\mathbb R^D)\) with its Borel sigma-field. Let \(\mu\) be a probability distribution for the initial state based on the history through time \(t\).

Let \(b_s(x,z)\in\mathbb R^D\) be jointly Borel measurable in \((s,x,z)\), where \(z\) denotes the initial state. The initial distribution and \(b\) use only the history through time \(t\). Let \(\Sigma_s\) be a deterministic measurable symmetric positive-semidefinite \(D\times D\) matrix, with
\[
\int_t^{t+1}\operatorname{tr}(\Sigma_s)\,ds<\infty,
\]
and write \(a_s=\Sigma_s^{1/2}\) for its symmetric positive-semidefinite square root. Let \(G_s(x)\) be a real-valued measurable function, differentiable in \(x\) with jointly measurable gradient, which may also depend on the fixed new observation.

Let \(P_t\) be the prior path law and \(Q_t\) the guided path law, with weak SDE representations
\[
dX_s=b_s(X_s,X_t)\,ds+a_s\,dW_s,
\]
\[
dX_s^G=\bigl(b_s(X_s^G,X_t^G)+\Sigma_s\nabla_xG_s(X_s^G)\bigr)\,ds+a_s\,dW_s^G,
\qquad t\leq s\leq t+1,
\]
where \(W,W^G\) are \(D\)-dimensional Brownian motions and both initial states have law \(\mu\). Assume the equations admit continuous weak solutions on the whole interval, with finite time integrals of their drift norms almost surely, and that the uncontrolled equation has a unique law for initial distribution \(\mu\).

Set \(u_s=a_s\nabla_xG_s(X_s^G)\) and assume the Novikov condition
\[
E_{Q_t}\!\left[\exp\!\left(\frac12\int_t^{t+1}\|u_s\|^2\,ds\right)\right]<\infty.
\]
Write \(R=dP_t/dQ_t\) for the resulting path density.

Let \(\ell_{t+1}:\mathbb R^D\to[0,\infty)\) be a measurable terminal likelihood for the fixed new observation, and assume
\[
Z_{t+1}:=E_{P_t}[\ell_{t+1}(X_{t+1})]\in(0,\infty).
\]
Define the posterior path law by
\[
\frac{dP_{t+1}}{dP_t}(X)=\frac{\ell_{t+1}(X_{t+1})}{Z_{t+1}},
\]
and define
\[
w_{t+1}(X^G)=\ell_{t+1}(X_{t+1}^G)R(X^G).
\]

## Task

Prove that for every bounded measurable path functional \(\Phi:\mathcal C\to\mathbb R\),
\[
E_{Q_t}[w_{t+1}(X^G)\Phi(X^G)]
=Z_{t+1}E_{P_{t+1}}[\Phi(X)].
\]
In particular, for every bounded measurable endpoint function \(\varphi:\mathbb R^D\to\mathbb R\),
\[
E_{Q_t}[w_{t+1}(X^G)\varphi(X_{t+1}^G)]
=Z_{t+1}E_{P_{t+1}}[\varphi(X_{t+1})].
\]
For iid guided paths \(X^{G,(1)},\ldots,X^{G,(N)}\sim Q_t\), put \(w_i=w_{t+1}(X^{G,(i)})\) and define
\[
\widehat\pi_{t+1}^N(\varphi)=
\begin{cases}
\displaystyle\frac{\sum_{i=1}^Nw_i\varphi(X_{t+1}^{G,(i)})}{\sum_{i=1}^Nw_i},&\sum_{i=1}^Nw_i>0,\\[6pt]
0,&\sum_{i=1}^Nw_i=0.
\end{cases}
\]
Prove that this estimator converges in probability, as \(N\to\infty\), to \(E_{P_{t+1}}[\varphi(X_{t+1})]\).
