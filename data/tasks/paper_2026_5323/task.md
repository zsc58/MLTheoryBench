# Problem

## Setup

Let $d,n$ be positive integers, $\alpha\in(0,1]$, $\varepsilon\in(0,1]$, and $M,\Gamma,\Delta>0$. Record spaces are measurable spaces. Decision domains are nonempty and carry their Borel sigma-algebras; losses are jointly measurable. A learner is a measurable randomized map from a dataset to the stated decision domain. It may depend on the specified domain, loss, and numerical parameters, but not on the unknown data distribution.

Datasets of the same size are neighboring if they differ in at most one coordinate. A randomized algorithm $\mathcal A$ is $(\varepsilon,\delta)$-differentially private if, for every neighboring pair $S,S'$ and measurable output event $E$,

$$
\Pr(\mathcal A(S)\in E)\leq e^\varepsilon\Pr(\mathcal A(S')\in E)+\delta.
$$

For a random variable $X\in[0,M]$, define

$$
\operatorname{CVaR}_\alpha(X)
=\inf_{\eta\in\mathbb R}\left\{\eta+\frac1\alpha\mathbb E[(X-\eta)_+]\right\},
\qquad (x)_+=\max\{x,0\}.
$$

The infimum may equivalently be restricted to $\eta\in[0,M]$.

For a probability distribution $P$ on a record space $\mathcal Z$, a nonempty closed convex set $\mathcal K\subseteq\mathbb R^d$, and a loss $h:\mathcal K\times\mathcal Z\to[0,M]$, write

$$
\operatorname{Exc}_P(w)
=\operatorname{CVaR}_{\alpha,P}(h(w;Z))
-\inf_{v\in\mathcal K}\operatorname{CVaR}_{\alpha,P}(h(v;Z)),
\qquad Z\sim P.
$$

Assume $\operatorname{diam}(\mathcal K)\leq\Delta$ and, for every $z$, $h(\cdot;z)$ is convex and $\Gamma$-Lipschitz in Euclidean norm. A learner using $n$ records observes only $S\sim P^n$, in addition to the specified loss, domain, and parameters. Expectations below include both the iid sample and algorithmic randomness.

Assume the following distribution-free Euclidean private convex-optimization interfaces. In these interfaces, $p,N$ are positive integers, $H,L>0$, $\Theta\subseteq\mathbb R^p$ is a nonempty closed convex domain, and $g(\theta;x)$ is a measurable sample loss. For a distribution $Q$ on its record space, define

$$
\mathcal L_Q(\theta)=\mathbb E_{X\sim Q}g(\theta;X),
\qquad
\mathcal L_Q^\star=\inf_{\theta\in\Theta}\mathcal L_Q(\theta).
$$

Population excess in the interfaces means

$$
\mathbb E_{S\sim Q^N,\mathcal B}
\left[\mathcal L_Q(\mathcal B(S))-\mathcal L_Q^\star\right].
$$

For the upper interface, distributions are required to satisfy $\mathbb E_Q|g(\theta_0;X)|<\infty$ for one $\theta_0\in\Theta$, so these population objectives are finite.

**Upper interface.** For every such domain of diameter at most $H$ and every sample-loss family whose members are convex and $L$-Lipschitz, and for every $0<\delta\leq N^{-2}$, there is one $(\varepsilon,\delta)$-DP learner $\mathcal B$ returning an element of $\Theta$ such that, for every distribution $Q$ satisfying the stated integrability condition,

$$
\mathbb E_{S\sim Q^N,\mathcal B}
\left[\mathcal L_Q(\mathcal B(S))-\mathcal L_Q^\star\right]
\leq\widetilde O\left(LH\left[\frac1{\sqrt N}+\frac{\sqrt{p\log(1/\delta)}}{\varepsilon N}\right]\right).
$$

**Lower interface.** For every $p,H,L,N$ and every $0<\delta\leq N^{-2}$, there exist a nonempty closed convex domain $\Theta\subseteq\mathbb R^p$ of diameter $H$, a record space, a convex $L$-Lipschitz shifted-linear sample-loss family, and a family $\mathfrak Q$ of data distributions with the following property. All values of these losses lie in a common interval of length at most $LH$, and every $(\varepsilon,\delta)$-DP learner $\mathcal B$ returning an element of $\Theta$ has, for some $Q\in\mathfrak Q$,

$$
\mathbb E_{S\sim Q^N,\mathcal B}
\left[\mathcal L_Q(\mathcal B(S))-\mathcal L_Q^\star\right]
\geq\widetilde\Omega\left(LH\min\left\{1,\frac1{\sqrt N}+\frac{\sqrt p}{\varepsilon N}\right\}\right).
$$

Here shifted-linear means affine in the decision variable. Both interfaces use the same record-replacement privacy definition and $\varepsilon\in(0,1]$.

All implicit numerical constants are universal. Tilde notation suppresses only polylogarithmic factors in dimensionless parameters: sample sizes, dimensions, $1/\alpha$, $1/\varepsilon$, and $1/\delta$, as applicable. It suppresses no additional polynomial dependence and no dependence on the scale parameters $M,\Gamma,\Delta,L,H$. The tildes in the conclusions retain the logarithmic factors of the two assumed interfaces.

## Task

Prove the following integrated upper and lower theorem.

**Achievability.** For every admissible record space $\mathcal Z$, domain $\mathcal K$, and loss $h$, if $0<\delta\leq n^{-2}$, there exists an $(\varepsilon,\delta)$-DP learner returning $\widehat w\in\mathcal K$ such that, for every distribution $P$ on $\mathcal Z$,

$$
\mathbb E\operatorname{Exc}_P(\widehat w)
\leq\widetilde O\left(
\frac{\Gamma\Delta+M}{\alpha}
\left[\frac1{\sqrt n}+\frac{\sqrt{(d+1)\log(1/\delta)}}{\varepsilon n}\right]
\right).
$$

**Converse.** Let $m=\lceil4n\alpha\rceil$ and suppose $0<\delta\leq m^{-2}$. There exist an admissible domain, record space, convex loss family, and family of data distributions such that every $(\varepsilon,\delta)$-DP learner returning a point in that domain has, for some distribution in the family,

$$
\mathbb E\operatorname{Exc}_P(\widehat w)
\geq\widetilde\Omega\left(
R_0\min\left\{1,\frac1{\sqrt{n\alpha}}+\frac{\sqrt d}{\varepsilon n\alpha}\right\}
\right)-M e^{-c n\alpha},
\qquad R_0=\min\{M,\Gamma\Delta\},
$$

where $c>0$ is universal. In particular, up to the inherited logarithmic factors and the displayed residual, the matching privacy dependence is governed by the effective private tail sample size $\varepsilon n\alpha$.
