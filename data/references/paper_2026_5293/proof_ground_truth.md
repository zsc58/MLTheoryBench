# Reference Proof

## Proof Structure

We compute the empirical marginal after de-scaling. We justify the continuous density and conditional-mean versions by finite-mixture conditioning, differentiate the Gaussian mixture, derive the velocity--score relation directly, and simplify it to the local-mean formula. Finally, the normalized exponential weights are identified with the Gaussian weights, so the affine output map gives the stated velocity.

## Theorem-Critical Obligations

1. Establish the conditional Gaussian law, the positive continuous marginal density, and the positivity of all denominators.
2. Derive the de-scaled density identity by Gaussian scaling.
3. Construct the conditional means from the finite mixture and establish the existence and uniqueness of the continuous velocity version.
4. Derive the local-mean score identity and the velocity--score relation, rather than invoke an unproved specialized identity.
5. Verify the spatial chain rule and all time-dependent coefficients in the velocity formula.
6. Identify the attention weights and verify the affine output identity throughout the stated domain.

All six obligations are closed below.

## Complete Proof

Fix \(t\in(0,1]\), and write \(\tau=\tau_t\), \(h=h_t\), and \(a=1-\epsilon\). Since
\[
\tau=1-at\geq\epsilon>0,\qquad h=\tau/t>0,
\]
every Gaussian kernel used below is finite and strictly positive. All normalizing sums are finite and strictly positive because \(m\geq1\). Also, \(B\) takes finitely many values and \(Y_0\) is Gaussian, so the conditional expectations defining the velocity have integrable arguments.

Conditional on \(J=i\), independence gives
\[
Y_t\sim N(ts_i,\tau^2 I_d).
\]
Consequently, a density of \(Y_t\) is
\[
p_t(x)=\frac1m\sum_{i=1}^m\phi_\tau(x-ts_i).
\]
This density is smooth and strictly positive everywhere. It is the unique continuous density: two continuous densities of the same law agree almost everywhere, and a continuous difference that is nonzero somewhere is nonzero on a nonempty open ball, contradicting almost-everywhere equality.

For \(x=ty\), Gaussian scaling gives
\[
t^d\phi_\tau\bigl(t(y-s_i)\bigr)
=\phi_{\tau/t}(y-s_i)=\phi_h(y-s_i).
\]
Consequently,
\[
t^dp_t(ty)=\frac1m\sum_{i=1}^m\phi_h(y-s_i),
\]
which proves the density assertion.

Let \(\widetilde p_t(y)=t^dp_t(ty)\). Differentiating its finite Gaussian mixture yields
\[
\nabla_y\widetilde p_t(y)
=\frac1m\sum_{i=1}^m\phi_h(y-s_i)\frac{s_i-y}{h^2}.
\]
After division by \(\widetilde p_t(y)>0\),
\[
\nabla_y\log\widetilde p_t(y)=\frac{M_t(y)-y}{h^2}. \tag{1}
\]

We next justify the conditional means and their pointwise versions. Define
\[
\pi_i(x)=\frac{\phi_\tau(x-ts_i)}{\sum_{j=1}^m\phi_\tau(x-ts_j)},
\qquad
\mu_t(x)=\sum_{i=1}^m\pi_i(x)s_i.
\]
For every bounded Borel function \(g:\mathbb R^d\to\mathbb R\), the joint law gives
\[
\begin{aligned}
\mathbb E[\mathbf 1_{\{J=i\}}g(Y_t)]
&=\frac1m\int_{\mathbb R^d}g(x)\phi_\tau(x-ts_i)\,dx\\
&=\int_{\mathbb R^d}g(x)\pi_i(x)p_t(x)\,dx.
\end{aligned}
\]
Thus \(\pi_i(Y_t)\) is a version of \(\mathbb P(J=i\mid Y_t)\), and \(\mu_t\) is a continuous version of \(x\mapsto\mathbb E[B\mid Y_t=x]\). The path identity gives
\[
Y_0=\frac{Y_t-tB}{\tau},
\]
so a continuous version of its conditional mean is
\[
\mathbb E[Y_0\mid Y_t=x]=\frac{x-t\mu_t(x)}{\tau}.
\]
It follows that a continuous version of the velocity is
\[
\mu_t(x)-a\frac{x-t\mu_t(x)}{\tau}
=\frac{\mu_t(x)-ax}{\tau},
\]
where the equality uses \(\tau+at=1\). This constructs the continuous velocity version required in the task. It is unique: two continuous conditional-mean versions agree \(p_t(x)\,dx\)-almost everywhere, and every nonempty open ball has positive probability because \(p_t\) is strictly positive. A nonzero continuous difference would contradict this agreement. Hence the constructed version is precisely \(v_t\).

Differentiating the finite mixture for \(p_t\) at a general point \(x\) now gives explicitly
\[
\begin{aligned}
\nabla_x p_t(x)
&=\frac1m\sum_{i=1}^m\phi_\tau(x-ts_i)\frac{ts_i-x}{\tau^2}\\
&=\frac{p_t(x)}{\tau^2}\bigl(t\mu_t(x)-x\bigr).
\end{aligned}
\]
Therefore
\[
\mu_t(x)=\frac{x+\tau^2\nabla_x\log p_t(x)}{t}. \tag{2}
\]
Using the continuous velocity version just constructed, (2), and \(\tau=1-at\),
\[
\begin{aligned}
v_t(x)
&=\frac{\mu_t(x)-ax}{\tau}\\
&=\frac1\tau\left(\frac{x}{t}+\frac{\tau^2}{t}\nabla_x\log p_t(x)-ax\right)\\
&=\frac{x}{t}+\frac{\tau}{t}\nabla_x\log p_t(x). \tag{3}
\end{aligned}
\]
Indeed, the coefficient of \(x\) is \((1/t-a)/\tau=1/t\).

The change of variables \(\widetilde p_t(y)=t^dp_t(ty)\) implies
\[
\nabla_y\log\widetilde p_t(y)=t\nabla_x\log p_t(ty).
\]
Putting \(x=ty\) in (3), then using this identity and (1), gives
\[
\begin{aligned}
v_t(ty)
&=y+\frac{\tau}{t^2}\nabla_y\log\widetilde p_t(y)\\
&=y+\frac{\tau}{t^2h^2}\bigl(M_t(y)-y\bigr)\\
&=y+\frac{M_t(y)-y}{\tau},
\end{aligned}
\]
because \(h=\tau/t\).

Finally, the normalized exponential weights defining \(H_t\) are
\[
\frac{\exp(-\|y-s_i\|^2/(2h^2))}
{\sum_j\exp(-\|y-s_j\|^2/(2h^2))}.
\]
The common Gaussian prefactor \((2\pi h^2)^{-d/2}\) cancels in the definition of \(\omega_i\), so these weights equal \(\omega_i(t,y)\). Therefore \(H_t(y)=M_t(y)\), and hence
\[
A_t\bigl(y,H_t(y)\bigr)
=y+\frac{H_t(y)-y}{\tau_t}
=y+\frac{M_t(y)-y}{\tau_t}
=v_t(ty).
\]
All stated identities hold for every \(t\in(0,1]\) and \(y\in\mathbb R^d\). The argument includes \(t=1\), \(\epsilon=1\), \(m=1\), and repeated support points; none introduces a zero denominator or requires a separate assumption. No assertion at \(t=0\) or \(\epsilon=0\) is required.
