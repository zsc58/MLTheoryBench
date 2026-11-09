# Problem

## Setup

Let \((M,g)\) be a complete stochastically complete Riemannian manifold with volume measure \(\mathrm{vol}\) and geodesic distance \(d\). Write \(\Delta_g=\operatorname{div}_g\nabla_g\), and let \(p_t(x,z)\) be the heat kernel for the equation \(\partial_t u=\Delta_g u\). For \(t>0\), set
\[
\mu_x^t(dz):=p_t(x,z)\,\mathrm{vol}(dz).
\]
Thus \(\mu_x^t\) is the time-\(t\) Brownian law with generator \(\Delta_g\), started at \(x\). At time zero, set \(\mu_x^0=\delta_x\), the Dirac probability measure at \(x\).

Assume that for some signed constant \(K\in\mathbb R\),
\[
\mathrm{Ric}_x(v,v)\ge -K\,\|v\|_g^2
\quad\text{for all }x\in M,\ v\in T_xM.
\]

Let \(\mathcal D\) be a dataset space with a symmetric adjacency relation \(\sim\), and let \(s:\mathcal D\to M\) satisfy a global sensitivity bound \(\Delta\in[0,\infty)\):
\[
 d(s(D),s(D'))\le \Delta
 \quad\text{whenever }D\sim D'.
\]
For \(t\ge0\), define the Brownian mechanism by its output law \(\mathcal M_t(D)=\mu_{s(D)}^t\). For probability measures \(P,Q\) and \(\alpha>1\), define
\[
D_\alpha(P\|Q)=\frac1{\alpha-1}\log\int \left(\frac{dP}{dQ}\right)^\alpha dQ
\]
when \(P\ll Q\), allowing the value \(+\infty\); set \(D_\alpha(P\|Q)=+\infty\) when \(P\not\ll Q\). A mechanism is \((\alpha,\varepsilon)\)-Renyi differentially private if \(D_\alpha(\mathcal M(D)\|\mathcal M(D'))\le\varepsilon\) for every adjacent ordered pair.

## Task

Prove the following integrated theorem. For every \(\alpha>1\) and \(t>0\), \(\mathcal M_t\) is \((\alpha,\varepsilon_K(\alpha,t,\Delta))\)-Renyi differentially private, where
\[
\varepsilon_K(\alpha,t,\Delta)=\frac{K\alpha\Delta^2}{2(1-e^{-2Kt})}
\]
for \(K\ne0\), with continuous value \(\varepsilon_0(\alpha,t,\Delta)=\alpha\Delta^2/(4t)\) at \(K=0\). Show that this bound is nonincreasing in \(t\), and strictly decreasing when \(\Delta>0\); for \(K<0\) it tends to zero, for \(K>0\) it tends to \(K\alpha\Delta^2/2\), and the flat expression is the \(K\to0\) limit.

Finally, for every target budget \(\varepsilon>0\), when \(K<0\), show that the choice
\[
 t=\frac{\log(2\varepsilon)-\log(2\varepsilon-K\alpha\Delta^2)}{2K}
\]
produces \((\alpha,\varepsilon)\)-RDP, while for \(K=0\) the corresponding choice is \(t=\alpha\Delta^2/(4\varepsilon)\).
