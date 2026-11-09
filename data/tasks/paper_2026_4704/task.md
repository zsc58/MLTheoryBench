# Problem

## Setup

Fix a dimension $d\ge 2$. Let $V:\mathbb R^d\to\mathbb R$ be twice continuously differentiable, minimized at the origin, and suppose that for constants $0<\ell\le L<\infty$,
$$\ell I_d\preceq\nabla^2V(x)\preceq LI_d\qquad\text{for all }x\in\mathbb R^d.$$
Let
$$Z=\int_{\mathbb R^d}e^{-V(x)}\,dx,\qquad \pi(dx)=Z^{-1}e^{-V(x)}dx.$$
Let $\mathcal C_{\rm rad}$ be the set of radially symmetric probability measures on $\mathbb R^d$ with finite second moment, and assume that this class contains at least one measure with finite $\mathrm{KL}(\mu\|\pi)$. Define the spherical average
$$\bar V(r)=\int_{S^{d-1}}V(r\theta)\,d\sigma(\theta)\qquad(r\ge 0),$$
where $\sigma$ is uniform probability measure on $S^{d-1}$. Write $\bar V(x):=\bar V(\|x\|)$. Let $\rho=\mathcal N(0,I_d)$. For a radial monotone map write
$$T(x)=\Psi(\|x\|)\frac{x}{\|x\|}\quad(x\ne0).$$

## Task

Prove the following integrated theorem. The minimization problem
$$\inf_{\mu\in\mathcal C_{\rm rad}}\mathrm{KL}(\mu\|\pi)$$
has a unique optimizer $\pi_*^{\rm rad}$. Its density is
$$d\pi_*^{\rm rad}(x)=Z_*^{-1}e^{-\bar V(\|x\|)}dx,\qquad Z_*=\int_{\mathbb R^d}e^{-\bar V(\|x\|)}\,dx,$$
so the optimizer is characterized by spherical averaging. Moreover, $\bar V$ is $\ell$-strongly convex and $L$-smooth, so the optimizer preserves these conditioning parameters. The quadratic-cost optimal transport from $\rho$ to $\pi_*^{\rm rad}$ is unique up to $\rho$-almost-everywhere equality and has a continuous radial representative with $T(0)=0$ and
$$T(x)=\Psi(\|x\|)\frac{x}{\|x\|}\quad(x\ne0),$$
where $\Psi:[0,\infty)\to[0,\infty)$ is continuous and strictly increasing, with $\Psi(0)=0$. For this profile and every $r>0$,
$$\frac1{\sqrt L}\le\Psi'(r)\le\frac1{\sqrt\ell},$$
and there is a universal numerical constant $C$ such that
$$|\Psi''(r)|\le C\frac{\kappa}{\sqrt\ell}\left(1+\frac d{r^2}\right)\left(1+|r-\sqrt d|\right),\qquad \kappa=\frac L\ell.$$
