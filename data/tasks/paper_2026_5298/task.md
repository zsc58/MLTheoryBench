# Problem

## Setup

Let \(\mathcal V\) be a nonempty finite set, let \(L,K\) be positive integers, and put \(D=L|\mathcal V|\). Let \(x:\mathcal V^L\to\mathbb R^D\) encode each token as its one-hot vector, with block \(x(w)_l=e_{w_l}\). Let \(W\) have a probability distribution \(\mu\) on \(\mathcal V^L\), and let \(X_0=x(W)\). Independently of \(X_0\), let \(B\) be a standard \(D\)-dimensional Brownian motion, and let
\[
 dX_s=-X_s\,ds+\sqrt2\,dB_s.
\]
Put \(c_s=e^{-s}\) and \(\sigma_s^2=1-e^{-2s}\). Thus
\[
 X_s\mid X_0\sim\mathcal N(c_sX_0,\sigma_s^2I_D).
\]
For \(s>0\), define
\[
 m_s(z)=\mathbb E[X_0\mid X_s=z],
 \qquad
 \rho_{s,l}(e_v\mid z)=\mathbb P(X_{0,l}=e_v\mid X_s=z).
\]
Use the continuous versions in \(z\) of these conditional probabilities and means. They are defined on all of \(\mathbb R^D\) by the finite Gaussian-mixture observation model. Assume that every posterior marginal \(\rho_{s,l}(\cdot\mid z)\) is available exactly.

Fix \(T>0\) and a deterministic reverse-time grid
\[
 0=t_0<t_1<\cdots<t_K=T,
 \qquad u_k=T-t_k.
\]
Define the reversed path by \(Y_t=X_{T-t}\), \(0\le t\le T\).

An OU bridge with deterministic endpoints \(a\) at forward time \(0\) and \(y\) at forward time \(v>0\) means the continuous Gaussian conditional law of an OU process started at \(a\), conditioned to equal \(y\) at time \(v\). For \(0<s<v\), its marginal at forward time \(s\) is
\[
 \mathcal N\!\left(
 \frac{\sinh(v-s)}{\sinh v}a+
 \frac{\sinh s}{\sinh v}y,
 \frac{2\sinh s\sinh(v-s)}{\sinh v}I_D
 \right).
\]
Its states at forward times \(0\) and \(v\) are \(a\) and \(y\), respectively.

Let \(\pi_T\) be a Borel probability measure on \(\mathbb R^D\). Define two continuous, grid-interpolated samplers, each initialized with law \(\pi_T\). At reverse time \(t_k\), conditional on its current state \(y\), each sampler proceeds as follows:

- The **marginal-endpoint sampler** independently draws \(A_l\sim\rho_{u_k,l}(\cdot\mid y)\), \(l=1,\ldots,L\), and follows the OU bridge with forward endpoints \(a=A\) and \(y\), from forward time \(u_k\) down to \(u_{k+1}\).
- The **mean-endpoint sampler** follows the OU bridge with forward endpoints \(a=m_{u_k}(y)\) and \(y\), over the same forward-time interval.

At each step, conditional on the current state, all new endpoint and bridge randomness is independent of the sampler's preceding history. The sampled endpoint is retained throughout that step. The successive bridge segments are joined continuously, including their endpoint at reverse time \(T\). Denote the resulting paths by \(\widehat Y^{\rm mar}\) and \(\widehat Y^{\rm mean}\).

## Regularity assumptions

Let \(\mathcal C=C([0,T],\mathbb R^D)\), equipped with its Borel sigma-algebra, and write
\[
 P=\mathcal L(Y_{[0,T]}),\qquad
 Q^{\rm mar}=\mathcal L(\widehat Y^{\rm mar}_{[0,T]}),\qquad
 Q^{\rm mean}=\mathcal L(\widehat Y^{\rm mean}_{[0,T]}),
 \qquad \lambda_T=\mathcal L(X_T).
\]
Assume
\[
 \lambda_T\ll\pi_T,
 \qquad
 \mathrm{KL}(\lambda_T\|\pi_T)<\infty,
 \qquad
 P\ll Q^{\rm mar},
 \qquad
 P\ll Q^{\rm mean}.
\]
The last two assumptions concern the entire closed-interval path laws on \(\mathcal C\), not merely their restrictions to shorter intervals.

## Task

Prove that
\[
 \mathrm{KL}(P\|Q^{\rm mar})
 \leq
 \mathrm{KL}(P\|Q^{\rm mean}).
\]

Moreover, prove that the inequality is strict if there exist \(k\in\{0,\ldots,K-1\}\) and \(l\in\{1,\ldots,L\}\) such that, for a set of \(t\in(t_k,t_{k+1})\) of positive Lebesgue measure, with \(u=T-t\),
\[
 \mathbb E[X_{0,l}\mid X_{u_k},X_{u,l}]
 \ne
 \mathbb E[X_{0,l}\mid X_{u_k}]
\]
on an event of positive probability under the forward OU law.
