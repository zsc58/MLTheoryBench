# Reference Proof

## Proof Structure

Normalize the fixed weighted predictive to obtain a likelihood ratio. Under the predictive null, condition on the past and the realized current input to show that this ratio has conditional mean one. The tower property then yields a nonnegative martingale for the running product, and Ville's inequality gives the anytime-valid boundary-crossing guarantee.

## Complete Proof

Let $\mu$ be the reference measure used by the predictive densities. For every input $x$ with $0<Z_w(x)<\infty$,
\[
Z_w(x)=\int w(y)p_s(y\mid x,D_{\rm tr})\,d\mu(y),\qquad
q_w(y\mid x,D_{\rm tr})=\frac{w(y)p_s(y\mid x,D_{\rm tr})}{Z_w(x)}.
\]
On the support of $p_s(\cdot\mid x,D_{\rm tr})$,
\[
\frac{q_w(y\mid x,D_{\rm tr})}{p_s(y\mid x,D_{\rm tr})}=\frac{w(y)}{Z_w(x)}.
\]
Thus $e_i=w(Y_i)/Z_w(X_i)$ is nonnegative and agrees with the predictive-density ratio almost surely under the null. Conditional on $(\mathcal F_{i-1},X_i)$, the null gives $Y_i$ density $p_s(\cdot\mid X_i,D_{\rm tr})$, so
\[
\mathbb E[e_i\mid\mathcal F_{i-1},X_i]
=\frac{1}{Z_w(X_i)}\int w(y)p_s(y\mid X_i,D_{\rm tr})\,d\mu(y)=1
\]
a.s. This conditions on the realized input and therefore covers deterministic, stochastic, and adaptively selected inputs satisfying the stated null.

Set $M_0=1$ and $M_t=\prod_{i=1}^t e_i$. By the tower property,
\[
\mathbb E[e_t\mid\mathcal F_{t-1}]
=\mathbb E[\mathbb E[e_t\mid\mathcal F_{t-1},X_t]\mid\mathcal F_{t-1}]=1.
\]
Since $M_{t-1}$ is $\mathcal F_{t-1}$-measurable,
\[
\mathbb E[M_t\mid\mathcal F_{t-1}]
=M_{t-1}\mathbb E[e_t\mid\mathcal F_{t-1}]=M_{t-1}.
\]
Hence $(M_t)_{t\ge0}$ is a nonnegative martingale initialized at one. Ville's inequality gives, for $\alpha\in(0,1)$,
\[
\mathbb P_{H_0^{\rm pred}}\!\left(\sup_{t\ge0}M_t>\frac1\alpha\right)\le\alpha.
\]
Because $\{\tau^*<\infty\}\subseteq\{\sup_{t\ge0}M_t>1/\alpha\}$ for $\tau^*=\inf\{t\ge1:M_t>1/\alpha\}$, we conclude $\mathbb P_{H_0^{\rm pred}}(\tau^*<\infty)\le\alpha$.
