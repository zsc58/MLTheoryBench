# Reference Proof

## Proof Structure and Obligations

The proof must establish: (i) that the exact-expectation recursion has deterministic parameters and finite, well-defined updates; (ii) the support-aware weighted path identity with the normalization fixed by the initialization; (iii) exact gradient recovery; (iv) the smooth descent and PL one-step inequalities; and (v) legitimate geometric iteration, including constant objectives and endpoint cases. All these obligations are derived below.

The support condition is the explicit domain condition for the importance weights. It is not enough that a sampled quotient happens to be defined almost surely. The source proof also has a local normalization error at L000302: with initial weight one, both unnormalized expectations require the factor 1/Z_{theta_0}. This factor cancels from the gradient ratio.

## Complete Proof

Write Z_0=Z_{theta_0}. Each measurable real-valued potential gives a strictly positive density rho_theta, so the assumed finite normalizer satisfies 0<Z_theta<infinity.

We first prove the weighted identity and recursive well-definedness together. The initial parameter is deterministic. For j=0, omega_0=1 and X_0 has density rho_{theta_0}/Z_0, so for every nonnegative measurable scalar function varphi,
\[
\mathbb E[\varphi(X_0)\omega_0]
=\frac1{Z_0}\int\varphi(x)\rho_{\theta_0}(x)\,dx.
\]

Suppose the recursion has been constructed through time j with deterministic parameters theta_0,...,theta_j. The joint forward density is
\[
q_j(x_{0:j})=\frac{\rho_{\theta_0}(x_0)}{Z_0}
\prod_{i=1}^jM_i(x_{i-1},x_i).
\]
The recursive weights satisfy, almost surely under this law,
\[
\omega_j(x_{0:j})=
\prod_{i=1}^j
\frac{\rho_{\theta_i}(x_i)B_{i-1}(x_i,x_{i-1})}
{\rho_{\theta_{i-1}}(x_{i-1})M_i(x_{i-1},x_i)}.
\]
The empty product is one. The denominators are positive and finite almost surely along sampled transitions. Kernel densities are finite Lebesgue-almost everywhere, and the path law has a Lebesgue density, so exceptional density values do not affect these formulas.

On the support where q_j is positive, cancellation and telescoping give
\[
q_j\omega_j=\frac1{Z_0}\rho_{\theta_j}(x_j)
\prod_{i=1}^jB_{i-1}(x_i,x_{i-1}).
\]
Outside that support at least one forward density is zero, apart from null sets, since rho_{theta_0}>0. The support condition makes the corresponding backward density zero almost everywhere there. Thus the right-hand side also vanishes almost everywhere outside the proposal support. Extending the weight arbitrarily, for example by zero, on forward-null sets therefore yields the displayed equality almost everywhere on the entire path space.

For nonnegative measurable varphi, Tonelli's theorem now gives
\[
\mathbb E[\varphi(X_j)\omega_j]
=\frac1{Z_0}\int\varphi(x_j)\rho_{\theta_j}(x_j)
\prod_{i=1}^jB_{i-1}(x_i,x_{i-1})\,dx_{0:j}.
\]
Integrate successively in x_0,x_1,...,x_{j-1}. Each backward kernel integrates to one in its second argument. Consequently
\[
\mathbb E[\varphi(X_j)\omega_j]
=\frac1{Z_0}\int\varphi(x)\rho_{\theta_j}(x)\,dx
=\frac{Z_{\theta_j}}{Z_0}\mathbb E_{p_{\theta_j}}[\varphi(X)].
\tag{1}
\]
For signed or vector-valued varphi integrable under p_{theta_j}, first use (1) with |varphi| or its Euclidean norm. This proves absolute integrability under the weighted forward law, after which the same identity follows componentwise by Fubini's theorem.

In particular,
\[
\mathbb E[\omega_j]=\frac{Z_{\theta_j}}{Z_0}\in(0,\infty),
\qquad
\mathbb E[\|h_{\theta_j}(X_j)\|\omega_j]
=\frac{Z_{\theta_j}}{Z_0}\mathbb E_{p_{\theta_j}}[\|h_{\theta_j}(X)\|]<\infty.
\]
Thus the next parameter update is finite and deterministic. Applying (1) componentwise to h_{theta_j} proves
\[
\frac{\mathbb E[h_{\theta_j}(X_j)\omega_j]}
{\mathbb E[\omega_j]}
=\mathbb E_{p_{\theta_j}}[h_{\theta_j}(X)]
=\nabla F(\theta_j).
\tag{2}
\]
The next Markov transition and weight can then be constructed, establishing the induction. Hence the recursion exists for every finite time and
\[
\theta_{j+1}=\theta_j-\eta\nabla F(\theta_j)
\quad(j\ge0).
\tag{3}
\]

Let F_*=inf_theta F(theta). This is finite: F is real-valued and the PL inequality bounds F(theta)-F_* above by a finite number at any fixed theta, excluding F_*=-infinity.

We derive the smooth descent inequality directly. For any u,v, put s=v-u. Since the gradient is Lipschitz, it is continuous, and integration along the segment gives
\[
\begin{aligned}
F(v)-F(u)-\langle\nabla F(u),s\rangle
&=\int_0^1\langle\nabla F(u+ts)-\nabla F(u),s\rangle\,dt\\
&\le\int_0^1Lt\|s\|^2\,dt
=\frac L2\|s\|^2.
\end{aligned}
\tag{4}
\]
Apply this to (3). For 0<eta<=1/L,
\[
\begin{aligned}
F(\theta_{j+1})
&\le F(\theta_j)-\eta\left(1-\frac{L\eta}{2}\right)
\|\nabla F(\theta_j)\|^2\\
&\le F(\theta_j)-\frac\eta2\|\nabla F(\theta_j)\|^2.
\end{aligned}
\]
Using PL yields
\[
F(\theta_{j+1})-F_*
\le(1-\eta\mu)(F(\theta_j)-F_*).
\tag{5}
\]

It remains to justify iteration for every permitted choice of constants. If F is constant, its gradient is zero, (3) fixes every parameter, and both sides of the target inequality are zero for all k, regardless of the sign of 1-eta mu.

Otherwise there is a point u with F(u)>F_*. Applying (4) with v=u-nabla F(u)/L shows
\[
F_*\le F\left(u-\frac1L\nabla F(u)\right)
\le F(u)-\frac1{2L}\|\nabla F(u)\|^2.
\]
Combining this with PL gives
\[
2\mu(F(u)-F_*)\le\|\nabla F(u)\|^2
\le2L(F(u)-F_*).
\]
Since the gap at u is positive, mu<=L. Therefore 0<=1-eta mu<1, and (5) can be iterated without reversing inequalities:
\[
F(\theta_k)-F_*
\le(1-\eta\mu)^k(F(\theta_0)-F_*).
\]
This includes a zero initial gap. If the factor is zero, (5) makes every gap after the first step zero. At k=0 the zeroth power is one and the assertion is equality. This completes the proof.
