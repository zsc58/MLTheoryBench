# Reference Proof

## Contract and proof obligations

The source-space forward equation on lifted tests is an explicit hypothesis. No derivation of it from an unreproduced external regularity package is required. The obligations are to transfer this equation to the observed laws, use the separately assumed uniqueness, establish the conditional-mean parametrisation with the correct almost-everywhere quantifiers, verify that the conditional means lie in their convex domains, and prove the gradient equality through a finite parameter-independent loss difference.

We use the following standard conditional-expectation facts. For an integrable real random variable, conditional expectation exists, is unique almost surely, and preserves its integral. A Polish-valued random variable has a regular conditional distribution given a measurable random variable in the setting used here; integration against that kernel represents conditional expectations. Consequently, for a nonnegative or integrable measurable function of the observation and source state, its joint expectation equals the iterated conditional expectation. Pushforward change of variables gives integral f d(h_#mu) = integral (f o h) dmu. Here the source state space is Polish, h is measurable, and all applications have the scalar measurability and integrability required in the task.

For an existing norm integral of a strongly measurable vector-valued function, continuous linear functionals commute with integration: this follows first for simple functions and then by norm approximation, using |ell(v)| <= ||ell|| ||v||. In particular, the assertion holds for an inner product against a fixed vector. The stipulated existence of each vector mean in E_{t,x} handles possible incompleteness of that inner-product space.

## Transfer of the forward equation

Fix f in C. Pushforward change of variables gives
\[
\langle q_t,f\rangle=\langle\mu_t,f\circ h\rangle.
\]
The lifted test belongs to the stated source domain, and its source forward equation is assumed. Therefore, for t<1,
\[
\frac{d}{dt}\langle q_t,f\rangle
=\mathbb E[A_t(f\circ h)(S_t)].
\]
The integrability assumption and the defining conditional-expectation identity for B_tf imply
\[
\mathbb E[A_t(f\circ h)(S_t)]
=\mathbb E[B_tf(h(S_t))]
=\langle q_t,B_tf\rangle.
\]
Thus q solves the observed equation with initial law q_0. The hypothesis of at most one probability-law solution, for the fixed measurable versions B_tf and the entire path on [0,1], gives the asserted uniqueness. No terminal-time generator equation, automatic uniqueness, or independent Feller realization on O is inferred.

## Conditional means and marginal parametrisation

Fix t<1. At every observed point outside the exceptional set in the conditional-integrability assumptions, write Z for the conditional target a_t^{S_t}(x) and m for its existing norm integral a_t(x).

The integral m lies in K_{t,x}. To see this, approximate the strongly measurable, norm-integrable, K_{t,x}-valued variable Z in L^1 by simple variables whose values lie in K_{t,x}. Their expectations are finite convex combinations of points in K_{t,x}, hence belong to K_{t,x}. These expectations converge in norm to m. Because m lies in E_{t,x} and K_{t,x} is closed there, m belongs to K_{t,x}.

Now fix f in C as well. Under conditioning on h(S_t)=x, the vector J_{t,x}f is fixed. The conditional parametrisation and the norm-integral property give
\[
\begin{aligned}
B_tf(x)
&=\mathbb E\!\left[\left.\langle J_{t,x}f,a_t^{S_t}(x)\rangle_{E_{t,x}}\,\right|h(S_t)=x\right]\\
&=\left\langle J_{t,x}f,\mathbb E\!\left[a_t^{S_t}(x)\mid h(S_t)=x\right]\right\rangle_{E_{t,x}}\\
&=\langle J_{t,x}f,a_t(x)\rangle_{E_{t,x}}.
\end{aligned}
\]
This identity holds q_t-almost everywhere for this fixed pair (t,f). Agreement with the chosen scalar version B_tf is only almost everywhere. No common exceptional set over all f is asserted or needed.

## Loss identity and its integrability

Fix a parameter theta. For almost every (t,x) under lambda(dt)q_t(dx), let Z have the conditional target law, set m=a_t(x), and put b=a_t^theta(x). The conditional norm and potential assumptions make the following calculation legitimate. In particular,
\[
\mathbb E|\langle Z-b,\nabla\psi_{t,x}(b)\rangle|
\leq \|\nabla\psi_{t,x}(b)\|\bigl(\mathbb E\|Z\|+\|b\|\bigr)<\infty.
\]
Expanding the divergence and commuting the fixed linear functional with the norm integral yields
\[
\begin{aligned}
\mathbb E[D_{t,x}(Z,b)]
&=\mathbb E[\psi_{t,x}(Z)]-\psi_{t,x}(b)
 -\langle m-b,\nabla\psi_{t,x}(b)\rangle\\
&=D_{t,x}(m,b)+c(t,x),
\end{aligned}
\]
where
\[
c(t,x)=\mathbb E[\psi_{t,x}(Z)]-\psi_{t,x}(m).
\]
This finite quantity is independent of theta. Applying the same expansion with b=m also gives
\[
c(t,x)=\mathbb E[D_{t,x}(Z,m)].
\]
For a convex differentiable function on a convex domain, restricting to the segment from v to u gives
\[
\psi_{t,x}(u)\geq\psi_{t,x}(v)+\langle u-v,\nabla\psi_{t,x}(v)\rangle.
\]
Thus every displayed divergence is nonnegative, and c(t,x)>=0. In particular,
\[
0\leq c(t,x)\leq \mathbb E[D_{t,x}(Z,a_t^\theta(x))].
\]
The scalar measurability assumptions and conditional-expectation identities make these quantities measurable. Choose any theta_0 in the nonempty parameter domain. The finite conditional loss at theta_0 and the last inequality show that
\[
C:=\int c(t,x)\,q_t(dx)\lambda(dt)<\infty.
\]
There is no need to assume that the two potential terms defining c are separately integrable over (t,x).

Disintegrating the conditional loss and integrating its nonnegative conditional identity now gives, for every theta,
\[
\mathcal L_{\rm cond}(\theta)=\mathcal L_{\rm marg}(\theta)+C.
\]
This also verifies the required marginal integrability. The constant C does not depend on theta because the time law, source laws, conditional targets, and potentials do not depend on theta.

At every parameter value where both losses are differentiable, differentiating this exact identity of finite real-valued functions proves
\[
\nabla_\theta\mathcal L_{\rm cond}(\theta)
=\nabla_\theta\mathcal L_{\rm marg}(\theta).
\]
Their stationary-point sets consequently agree wherever their gradients are defined. No interchange of a derivative and an expectation is used.
