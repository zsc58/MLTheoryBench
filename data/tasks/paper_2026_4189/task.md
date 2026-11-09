# Problem

## Setup

Let $\theta\in\Theta$ be a latent task parameter, $\phi\in\Phi$ a sensitive attribute, $D$ the full acquired dataset generated under a fixed design policy $\pi_d$, and $z\in\mathcal Z$ a downstream prediction. Let $m\in\mathbb M$ index a nonempty collection of probabilistic models. Probability densities and conditional densities below are measurable densities with respect to fixed dominating measures on the indicated spaces; integrals include sums in the discrete case. Assume the displayed regular conditional laws and their density versions exist.

In every model, the prior factorizes as
\[
p_m(\theta,\phi)=p(\theta)p_m(\phi).
\]
The models share the same marginal law of $(\theta,D)$, written
\[
p_m(\theta,D\mid\pi_d)=p(\theta)p(D\mid\theta,\pi_d).
\]
Conditioned on $(\theta,\phi,\pi_d)$, model $m$ has conditional density $p_m(D\mid\theta,\phi,\pi_d)$. Write $p_m(D\mid\pi_d)$ for its marginal dataset law and $p_m(\theta\mid D,\phi,\pi_d)$ for its posterior density.

For $p(\theta)$-almost every fixed value $t$, define
\[
\operatorname{EIG}_{\phi\mid\theta=t}^{m}(\pi_d)
:=I_m(D;\phi\mid\theta=t,\pi_d)\in[0,\infty],
\]
where the right-hand side is the mutual information of $D$ and $\phi$ under their conditional joint law given $\theta=t$ and the fixed policy. Define the conditional fairness score by
\[
F_c(\pi_d):=-\max_{m\in\mathbb M}\;
\mathbb E_{t\sim p(\theta)}\!\left[
\operatorname{EIG}_{\phi\mid\theta=t}^{m}(\pi_d)
\right].
\]
The maximum in this definition is assumed to exist in $[0,\infty]$ before negation; expectations of the nonnegative information quantities are interpreted as extended nonnegative integrals.

For downstream prediction, fix a predictive probability kernel with density $p(z\mid\theta)$ depending on $\theta$ only, and define
\[
p_m(z\mid\phi,D,\pi_d)
=\int p(z\mid\theta)\,p_m(\theta\mid D,\phi,\pi_d)\,d\theta.
\]
Demographic parity means that, for every model $m$ and every prediction value $z$, the equality
\[
p_m(z\mid\phi_1,D,\pi_d)
=p_m(z\mid\phi_2,D,\pi_d)
\]
holds for $p_m(\phi_1)p_m(\phi_2)p_m(D\mid\pi_d)$-almost every $(\phi_1,\phi_2,D)$.

## Task

Prove the following theorem: if $F_c(\pi_d)=0$, then the above downstream predictor achieves demographic parity in every model, in this almost-sure sense.
