# Problem

## Setup

Let \(S\) be a Polish space, and let \((S_t)_{t\in[0,1]}\) be a time-inhomogeneous Feller process with marginal laws \(\mu_t\) and infinitesimal generators \(A_t\), defined for \(t<1\). Write \(\langle\nu,g\rangle=\int g\,d\nu\). The generator domains satisfy \(\mathcal D(A_t)\subseteq C_0(S)\), where \(C_0(S)\) consists of continuous real functions vanishing at infinity.

Let \(h:S\to O\) be measurable, where \(O\) is a measurable space, and put \(q_t=h_\#\mu_t\). Let \(\mathcal C\) be a measure-determining real linear space of bounded measurable functions on \(O\): equality of integrals against every member of \(\mathcal C\) determines a probability measure on \(O\). For every \(f\in\mathcal C\), assume that \(f\circ h\in\mathcal D(A_t)\) for every \(t<1\), that \(t\mapsto A_t(f\circ h)\) is sup-norm continuous on \([0,1)\), and that
\[
\mathbb E\bigl[|A_t(f\circ h)(S_t)|\bigr]<\infty,
\qquad
\frac{d}{dt}\langle\mu_t,f\circ h\rangle
=\langle\mu_t,A_t(f\circ h)\rangle
\quad(t<1).
\]
At \(t=0\), derivatives are right derivatives.

For every \(t<1\) and \(f\in\mathcal C\), fix an \(O\)-measurable version \(B_tf\) satisfying
\[
B_tf(h(S_t))
=\mathbb E\!\left[A_t(f\circ h)(S_t)\mid h(S_t)\right]
\quad\text{almost surely}.
\]
For these fixed versions, assume that there is at most one family \((r_t)_{t\in[0,1]}\) of probability measures on \(O\) with \(r_0=q_0\), with \(B_tf\) integrable under \(r_t\), and satisfying
\[
\frac{d}{dt}\langle r_t,f\rangle=\langle r_t,B_tf\rangle
\qquad(f\in\mathcal C,\ t<1).
\]
Uniqueness here concerns the entire family on \([0,1]\).

For every \(t<1\) and \(x\in O\), let \(E_{t,x}\) be a real inner-product space, let \(J_{t,x}:\mathcal C\to E_{t,x}\) be linear, and let \(K_{t,x}\subseteq E_{t,x}\) be nonempty, closed, and convex. Suppose there are conditional targets \(a_t^s(x)\in K_{t,x}\), defined at the arguments used below, such that
\[
A_t(f\circ h)(s)
=\langle J_{t,h(s)}f,a_t^s(h(s))\rangle_{E_{t,h(s)}}
\qquad(f\in\mathcal C).
\]
Assume, for every \(t<1\),
\[
\mathbb E\!\left[\|a_t^{S_t}(h(S_t))\|_{E_{t,h(S_t)}}\right]<\infty.
\]
For \(q_t\)-almost every \(x\), assume that the conditional target \(a_t^{S_t}(x)\), under the conditional law given \(h(S_t)=x\), is strongly measurable and has a norm integral existing in \(E_{t,x}\). Define
\[
a_t(x)=\mathbb E\!\left[a_t^{S_t}(x)\mid h(S_t)=x\right].
\]
Here vector expectations mean norm integrals; if an inner-product space is incomplete, existence in that space, not merely in its completion, is part of this assumption. Conditional objects and scalar evaluations in the formulas below are taken in measurable versions. In particular, the target norms, inner products, potential evaluations, and divergence evaluations appearing in these formulas are measurable in their sampling variables.

Let \(\lambda\) be the uniform probability measure on \([0,1)\), equivalently Lebesgue measure restricted to that interval. For every \((t,x)\), let \(\psi_{t,x}:K_{t,x}\to\mathbb R\) be strictly convex and differentiable, with its differential represented by a vector \(\nabla\psi_{t,x}(v)\in E_{t,x}\). Define, for \(u,v\in K_{t,x}\),
\[
D_{t,x}(u,v)=\psi_{t,x}(u)-\psi_{t,x}(v)
-\langle u-v,\nabla\psi_{t,x}(v)\rangle_{E_{t,x}}.
\]
Let \(\Theta\subseteq\mathbb R^p\) be a nonempty open parameter domain, and let \(a_t^\theta(x)\in K_{t,x}\) be a parameterised prediction for \(\theta\in\Theta\). All the objects specified above, other than this prediction, are independent of \(\theta\).

Assume that, for \(\lambda(dt)q_t(dx)\)-almost every \((t,x)\),
\[
\mathbb E\!\left[\left.|\psi_{t,x}(a_t^{S_t}(x))|\,\right|h(S_t)=x\right]<\infty.
\]
For every \(\theta\in\Theta\), assume that the conditional divergence has finite expectation at every fixed \(t<1\), and that both time-integrated losses below are finite:
\[
\mathcal L_{\rm cond}(\theta)
=\mathbb E_{t\sim\lambda,\,S_t\sim\mu_t}
\left[D_{t,h(S_t)}\big(a_t^{S_t}(h(S_t)),a_t^\theta(h(S_t))\big)\right]
\]
and
\[
\mathcal L_{\rm marg}(\theta)
=\mathbb E_{t\sim\lambda,\,x\sim q_t}
\left[D_{t,x}\big(a_t(x),a_t^\theta(x)\big)\right].
\]
Sampling means first sampling time and then sampling the state from its specified law at that time. Values on null sets do not affect either loss.

## Task

Prove the following integrated claim.

The laws \((q_t)_{t\in[0,1]}\) satisfy
\[
\frac{d}{dt}\langle q_t,f\rangle=\langle q_t,B_tf\rangle
\qquad(f\in\mathcal C,\ t\in[0,1)),
\]
and hence are the unique probability-law solution of this equation with initial law \(q_0\), in the sense specified above. Moreover, the conditional means belong to \(K_{t,x}\) for \(q_t\)-almost every \(x\), and for every fixed \(t<1\) and \(f\in\mathcal C\),
\[
B_tf(x)=\langle J_{t,x}f,a_t(x)\rangle_{E_{t,x}}
\quad\text{for }q_t\text{-almost every }x.
\]
Finally, at every \(\theta\in\Theta\) where both losses are differentiable,
\[
\nabla_\theta\mathcal L_{\rm cond}(\theta)
=\nabla_\theta\mathcal L_{\rm marg}(\theta).
\]
In particular, the two losses have the same stationary points wherever their gradients are defined.
