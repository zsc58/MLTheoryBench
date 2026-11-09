# Problem

## Setup

Let a finite directed acyclic graph have a source, a collection \(\mathcal X\) of terminal states, and a finite set \(\mathcal T\) of complete source-to-terminal trajectories. Write \(x(\tau)\) for the terminal state of \(\tau\).

Let \(R:\mathcal X\to(0,\infty)\), define \(A_*=\sum_{x\in\mathcal X}R(x)\), and let
\[
\rho(x)=\frac{R(x)}{A_*}.
\]
Let \(p\) be a forward probability distribution on \(\mathcal T\), with terminal marginal
\[
p_X(x)=\sum_{\tau:x(\tau)=x}p(\tau).
\]
For every \(x\), let \(b(\cdot\mid x)\) be a probability distribution over trajectories ending at \(x\). Define a second trajectory distribution
\[
q(\tau)=\rho(x(\tau))b(\tau\mid x(\tau)).
\]
Assume \(p(\tau)>0\) and \(b(\tau\mid x(\tau))>0\) for every \(\tau\in\mathcal T\), let \(A>0\), and define the squared log-ratio loss
\[
\ell(\tau)=\left[\log\frac{A\,p(\tau)}{R(x(\tau))b(\tau\mid x(\tau))}\right]^2.
\]

Fix \(c\ge0\), \(\alpha\in(0,1)\), and integers \(m,n\ge1\). All distributions and \(A\) are fixed before sampling. Independently draw \(m\) iid trajectories from \(q\) and \(n\) iid trajectories from \(p\).

## Task

Prove that, except on an event of probability at most \(2\alpha\), the following implication holds: if every one of the \(m+n\) sampled trajectories satisfies \(\ell(\tau)\le c^2\), then
\[
\operatorname{TV}(p_X,\rho)
\le e^{2c}-1+\frac{\log(1/\alpha)}{m}+\frac{\log(1/\alpha)}{n},
\]
where \(\operatorname{TV}(u,v)=\tfrac12\sum_z|u(z)-v(z)|\) for distributions on a finite set.
