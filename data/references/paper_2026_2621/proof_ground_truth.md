# Reference Proof

## Proof Structure

Approximate the arbitrary density by a compactly supported Gaussian convolution. Derive an explicit uniform score-Hessian bound for this convolution on every finite time interval, including time zero. Use the Fokker–Planck equation and the characteristic Jacobian identity to verify that the probability-flow ODE transports the initial density to the VP marginal. The resulting flow is a bi-Lipschitz C1 diffeomorphism. The VP marginal converges to the standard Gaussian in relative entropy; Pinsker's inequality and invariance of L1 distance under a bijective pushforward transfer this to the inverse Gaussian pullback. A triangle inequality gives the claim for the original density.

## Complete Proof

Let h be the given density and fix epsilon>0.

Choose R so that
\[
\int_{B_R^c}h(x)\,dx<\frac{\varepsilon}{16}.
\]
Let
\[
m_R=\int_{B_R}h(x)\,dx,
\qquad
h_R(x)=m_R^{-1}h(x)\mathbf 1_{B_R}(x).
\]
Then h_R is a compactly supported probability density and
\[
\|h-h_R\|_1=2(1-m_R)<\frac{\varepsilon}{8}.
\]
By L1 continuity of Gaussian approximate identities, choose tau>0 such that
\[
q:=\varphi_{\tau^2 I}*h_R
\quad\text{satisfies}\quad
\|q-h_R\|_1<\frac{\varepsilon}{8}.
\]
Thus q\in\mathcal G and
\[
\|h-q\|_1<\frac{\varepsilon}{4}.
\]
Since h_R is supported in B_R, q has finite second moment.

Run the variance-preserving process from initial density q. Let U have density h_R, let G and Z be independent standard Gaussian vectors, and write
\[
X_0=U+\tau G.
\]
Then
\[
X_t=a(t)U+a(t)\tau G+\sigma(t)Z,
\]
so, with
\[
c_t^2=a(t)^2\tau^2+\sigma(t)^2,
\]
we have the Gaussian-mixture representation
\[
q_t(x)=\int_{B_R}\varphi_{c_t^2 I}(x-a(t)u)h_R(u)\,du.
\]
For t\in[0,T], c_t^2 is a convex combination of tau^2 and 1. Hence, with d=\min\{\tau^2,1\}>0,
\[
c_t^2\ge d.
\]
The compact support of h_R and this lower bound justify differentiation under the integral. Define the posterior probability measure
\[
\pi_{t,x}(du)=\frac{\varphi_{c_t^2 I}(x-a(t)u)h_R(u)\,du}{q_t(x)}.
\]
Since every Gaussian kernel is positive, q_t(x)>0. Differentiating the mixture gives
\[
s_t(x)=\nabla\log q_t(x)
=-\frac{x-a(t)\mathbb E_{\pi_{t,x}}U}{c_t^2}
\]
and
\[
\nabla s_t(x)
=-\frac{I}{c_t^2}+\frac{a(t)^2}{c_t^4}\operatorname{Cov}_{\pi_{t,x}}(U).
\]
The posterior remains supported in B_R, so
\[
\|\operatorname{Cov}_{\pi_{t,x}}(U)\|
\le \mathbb E_{\pi_{t,x}}\|U\|^2
\le R^2.
\]
Therefore, uniformly over t\in[0,T] and x\in\mathbb R^n,
\[
\|\nabla s_t(x)\|
\le \frac1d+\frac{R^2}{d^2}=:M_T<\infty.
\]
This includes t=0 because c_0^2=\tau^2>0. The same mixture formula, with differentiation in t also justified by compact support and c_t^2\ge d, shows that q_t, its spatial derivatives through order two, s_t, and \nabla s_t are continuous on [0,T]\times\mathbb R^n.

It remains to verify the transport identity. The VP marginal satisfies the Fokker–Planck equation
\[
\partial_tq_t=\frac12\nabla\cdot(xq_t)+\frac12\Delta q_t.
\]
Because q_t>0 and s_t=\nabla q_t/q_t,
\[
q_tv_t=-\frac12xq_t-\frac12\nabla q_t.
\]
Consequently,
\[
\partial_tq_t+\nabla\cdot(q_tv_t)=0.
\]
The Hessian bound makes v_t globally Lipschitz in x, uniformly on [0,T], and the displayed regularity makes it continuous in t and C1 in x. Also v_t has at most linear growth. Standard ODE theory therefore gives a global flow \Phi_t=\phi_{0\to t}, and differentiable dependence on the initial point gives a C1 flow. Gronwall's inequality gives a finite forward Lipschitz bound, and solving the ODE backward gives a finite bound for the inverse. Thus \Phi_T is a bi-Lipschitz C1 diffeomorphism.

For completeness, let J_t(x)=\det D\Phi_t(x). The variational equation gives
\[
\partial_tJ_t(x)=J_t(x)\,\nabla\cdot v_t(\Phi_t(x)),
\qquad J_0(x)=1.
\]
In particular J_t(x)>0. By the chain rule and the continuity equation,
\[
\begin{aligned}
\frac{d}{dt}\left[q_t(\Phi_t(x))J_t(x)\right]
&=J_t(x)\left[\partial_tq_t+\nabla q_t\cdot v_t+q_t\nabla\cdot v_t\right](\Phi_t(x))\\
&=J_t(x)\left[\partial_tq_t+\nabla\cdot(q_tv_t)\right](\Phi_t(x))=0.
\end{aligned}
\]
Since q_0=q and J_0=1,
\[
q_t(\Phi_t(x))J_t(x)=q(x).
\]
This is precisely the change-of-variables identity for
\[
(\Phi_t)_\#q=q_t,
\]
so in particular \((\Phi_T)_\#q=q_T\).

The standard finite-second-moment VP entropy estimate gives, for all sufficiently large T,
\[
D_{\rm KL}(q_T\|\gamma)
\le e^{-T}\left(n+\mathbb E_q\|X_0\|^2\right).
\]
The right-hand side tends to zero. Pinsker's inequality therefore gives
\[
\|q_T-\gamma\|_1\to0.
\]
Since \Phi_T is a bijection, pushforward preserves the L1 distance between probability densities. Hence
\[
\begin{aligned}
\|q-\Phi_T^{-1}\#\gamma\|_1
&=\|\Phi_T\#q-\Phi_T\#(\Phi_T^{-1}\#\gamma)\|_1\\
&=\|q_T-\gamma\|_1\to0.
\end{aligned}
\]
Choose T sufficiently large that
\[
\|q-\Phi_T^{-1}\#\gamma\|_1<\frac{3\varepsilon}{4}.
\]
Then
\[
\|h-\Phi_T^{-1}\#\gamma\|_1
\le \|h-q\|_1+\|q-\Phi_T^{-1}\#\gamma\|_1
<\frac{\varepsilon}{4}+\frac{3\varepsilon}{4}=\varepsilon.
\]
The same q and T satisfy the uniform score regularity and bi-Lipschitz transport properties, completing the proof.
