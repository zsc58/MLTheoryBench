# Problem

## Setup

Let \((X,\mathcal F,D)\) be a probability space and let \(n\ge1\) be an integer. At every prompt \(x\in X\), the available responses are \(a_1,\ldots,a_n\). Write
\[
\Delta_n=\left\{z\in\mathbb R^n:z_i\ge0\text{ for all }i,\ \sum_{i=1}^n z_i=1\right\},
\]
and let \(\Pi\) be the class of all measurable maps from \((X,\mathcal F)\) to \(\Delta_n\), equipped with its Borel sigma algebra. Let \(r:X\to\mathbb R^n\) be measurable and satisfy
\[
\int_X\|r(x)\|_\infty\,D(dx)<\infty.
\]
For a measurable deterministic reward function \(s:X\to\mathbb R^n\) with \(\int_X\|s(x)\|_\infty\,D(dx)<\infty\), set
\[
J_s(\pi)=\mathbb E_{x\sim D}\langle\pi(x),s(x)\rangle.
\]

Fix \(1\le p\le\infty\), \(1\le q<\infty\), and \(\delta>0\). A random reward function with law \(P\) is understood to have a jointly measurable realization
\[
R:(\Omega\times X,\mathcal A\otimes\mathcal F)\longrightarrow\mathbb R^n
\]
on an auxiliary probability space \((\Omega,\mathcal A,\nu)\). Write \(P_x\) for the distribution of \(R(\cdot,x)\) under \(\nu\); the notation \(\mathbb E_{R\sim P}\) denotes expectation over this auxiliary randomness. Reward laws below range over all such jointly measurable models.

For Borel probability measures \(\mu,\eta\) on \(\mathbb R^n\), define
\[
W_{q,\|\cdot\|_p}(\mu,\eta)
=\left(\inf_{\gamma\in\Gamma(\mu,\eta)}
\int_{\mathbb R^n\times\mathbb R^n}\|u-v\|_p^q\,\gamma(du,dv)\right)^{1/q},
\]
where \(\Gamma(\mu,\eta)\) is the set of their couplings; the distance may take the value \(+\infty\). Write \(\delta_v\) for the point mass at \(v\in\mathbb R^n\). Let \(\mathcal U_{p,q,\delta}\) be the set of reward laws just described satisfying, for \(D\)-almost every \(x\),
\[
W_{q,\|\cdot\|_p}(P_x,\delta_{r(x)})\le\delta.
\]
For \(P\in\mathcal U_{p,q,\delta}\) and \(\pi\in\Pi\), its return is
\[
J_P(\pi)=\mathbb E_{R\sim P}\mathbb E_{x\sim D}\langle\pi(x),R(x)\rangle.
\]

For vectors \(z\in\Delta_n\) and \(s,r\in\mathbb R^n\), define
\[
\operatorname{Reg}(z,s)=\max_{b\in\Delta_n}\langle b-z,s\rangle,
\qquad
\Psi_p(z;r)=\max_{\|d\|_p\le\delta}\operatorname{Reg}(z,r+d).
\]
Here \(e_i\) denotes the \(i\)-th standard basis vector, \((u)_+=\max\{u,0\}\), and \(p^*\) is defined by \(1/p+1/p^*=1\), with \(1/\infty=0\).

For the final clause below, take \(p=1\) and assume the response labels have been chosen so that \(r_1(x)\ge\cdots\ge r_n(x)\) for \(D\)-almost every \(x\). Define \(t_0(x)\) as the unique real solution of
\[
\sum_{i=1}^n(r_i(x)-t)_+=\delta,
\]
and define
\[
t^*(x)=\inf\left\{t\ge t_0(x):
\sum_{i:r_i(x)>t}(r_1(x)-r_i(x))\le\delta\right\}.
\]

## Task

Prove the following integrated claim.

The robust ex-ante regret problem satisfies
\[
\inf_{\pi\in\Pi}\ \sup_{P\in\mathcal U_{p,q,\delta}}
\left\{\max_{\beta\in\Pi}J_P(\beta)-J_P(\pi)\right\}
=\mathbb E_{x\sim D}\left[\inf_{z\in\Delta_n}\Psi_p(z;r(x))\right]. \tag{1}
\]
Moreover, for every \(z\in\Delta_n\) and every fixed reward vector \(r\in\mathbb R^n\),
\[
\Psi_p(z;r)=\max_{1\le i\le n}
\left\{r_i-\langle z,r\rangle+\delta\|e_i-z\|_{p^*}\right\}. \tag{2}
\]
In particular, when \(p=1\),
\[
\Psi_1(z;r)=\delta+\max_i(r_i-\delta z_i)-\langle z,r\rangle, \tag{3}
\]
and, for any \(k\in\arg\max_i(r_i-\delta z_i)\), the perturbation \(d=\delta e_k\) attains the maximum defining \(\Psi_1\).

Finally, under the stated ordering assumption, the measurable policy
\[
\pi_i^*(x)=\frac{(r_i(x)-t^*(x))_+}{\delta}\quad(i=2,\ldots,n),
\qquad
\pi_1^*(x)=1-\frac1\delta\sum_{i=2}^n(r_i(x)-t^*(x))_+
\]
is a global minimizer in (1).
