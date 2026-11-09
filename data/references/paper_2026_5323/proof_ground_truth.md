# Reference Proof

## Proof Structure and Obligations

This is a conditional theorem under the two expressly assumed private convex-optimization interfaces. Those interfaces remain imported, nonstandard dependencies; this proof does not claim to establish them from their citations. It establishes their applicability and every step of the CVaR reductions.

The obligations are: (1) construct a measurable convex lift and verify its geometry and finite population objective; (2) apply the upper interface with a distribution-independent learner and compare excess risks; (3) construct bounded nonnegative ordinary losses and prove exact equality of ordinary risk and embedded CVaR; (4) prove privacy of the randomized input transformation; (5) couple actual and ideal samples, bound the overflow probability, and transfer the lower-interface quantifiers; and (6) handle the ceiling in the effective sample size, including n alpha below one.

## Complete Proof

### Achievability

For a scale s>0, define

$$
\mathcal C_s=\mathcal K\times[0,M/s],\qquad
\phi_s(w,u;z)=su+\frac1\alpha(h(w;z)-su)_+.
$$

The domain is nonempty, closed, and convex in R^{d+1}. The sample loss is measurable and has the equivalent representation

$$
\phi_s(w,u;z)=\max\left\{su,\frac{h(w;z)}\alpha+s\left(1-\frac1\alpha\right)u\right\}.
$$

Both functions inside this maximum are convex. The first is s-Lipschitz. By the Lipschitz assumption on h and the Cauchy–Schwarz inequality, the second is Lipschitz with constant at most

$$
\sqrt{\frac{\Gamma^2}{\alpha^2}+s^2\left(1-\frac1\alpha\right)^2}
\leq\frac{\sqrt{\Gamma^2+s^2}}\alpha.
$$

The first constant is also at most the right-hand side. A maximum of two functions with a common Lipschitz bound has that bound, since the difference of their maxima is bounded in absolute value by the maximum of their absolute differences. Therefore phi_s is convex and L_s-Lipschitz, where

$$
L_s\leq\frac{\sqrt{\Gamma^2+s^2}}\alpha.
$$

This argument applies also to lower-dimensional domains and their boundaries. Product geometry gives

$$
\operatorname{diam}(\mathcal C_s)\leq H_s:=\sqrt{\Delta^2+M^2/s^2}.
$$

Moreover, 0<=phi_s<=M/alpha, so its population objective is finite for every P. Apply the upper interface with ambient dimension d+1, sample size n, and privacy parameters epsilon,delta. It supplies one learner, chosen without knowledge of P, whose output (widehat w,widehat u) satisfies, for every P,

$$
\mathbb E\left[F_{s,P}(\widehat w,\widehat u)-\inf_{(w,u)\in\mathcal C_s}F_{s,P}(w,u)\right]
\leq\widetilde O\left(L_sH_s\left[\frac1{\sqrt n}+\frac{\sqrt{(d+1)\log(1/\delta)}}{\varepsilon n}\right]\right),
$$

where F_{s,P}(w,u)=E_P phi_s(w,u;Z).

Each original record determines one lifted sample loss. Replacing one original record therefore replaces at most one lifted record, so the interface's DP inequality applies to neighboring original datasets. Releasing only widehat w preserves that inequality by taking the inverse image of each output event under coordinate projection.

The threshold formula, with eta=su, gives

$$
\inf_{u\in[0,M/s]}F_{s,P}(w,u)=\operatorname{CVaR}_{\alpha,P}(h(w;Z)),
$$

and consequently

$$
\operatorname{Exc}_P(\widehat w)
\leq F_{s,P}(\widehat w,\widehat u)-\inf_{(w,u)\in\mathcal C_s}F_{s,P}(w,u).
$$

Choose s^2=Gamma M/Delta, which is positive under the public assumptions. Then

$$
(\Gamma^2+s^2)(\Delta^2+M^2/s^2)=(\Gamma\Delta+M)^2.
$$

It follows that L_s H_s <= (Gamma Delta+M)/alpha. Substituting proves

$$
\mathbb E\operatorname{Exc}_P(\widehat w)
\leq\widetilde O\left(\frac{\Gamma\Delta+M}\alpha\left[\frac1{\sqrt n}+\frac{\sqrt{(d+1)\log(1/\delta)}}{\varepsilon n}\right]\right)
$$

simultaneously for every P, with the same learner.

### Converse: the ordinary hard family

Set

$$
\Gamma_0=\min\{\Gamma,M/\Delta\},\qquad
R_0=\Gamma_0\Delta=\min\{M,\Gamma\Delta\},\qquad
m=\lceil4n\alpha\rceil.
$$

Apply the lower interface with dimension d, diameter Delta, Lipschitz scale Gamma_0, sample size m, and the specified epsilon,delta. Its hypotheses hold because Gamma_0>0 and 0<delta<=m^{-2}. It supplies a domain, a record space X, a fixed shifted-linear loss family, and a family of distributions Q. Shift the common range interval to start at zero. This shift is independent of w, preserves excess risk, and gives losses a(w;x) in [0,R_0]. The resulting lower guarantee is: for every private ordinary learner B, some Q in the supplied family satisfies

$$
\mathbb E_{Q^m,B}\left[\mathbb E_Q a(B(S);X)-\inf_w\mathbb E_Q a(w;X)\right]
\geq\widetilde\Omega\left(R_0\min\left\{1,\frac1{\sqrt m}+\frac{\sqrt d}{\varepsilon m}\right\}\right).
$$

### Exact tail embedding

Adjoin a measurable dummy point x_0 with a(w;x_0)=0. Take the embedded record space to be {0,1} times (X union {x_0}), so that dummy records in active slots are also legitimate inputs to a private learner. Define

$$
h(w;(T,X))=T a(w;X).
$$

For each ordinary Q, let P_alpha(Q) be the distribution obtained by drawing T~Bernoulli(alpha), drawing X~Q independently when T=1, and using X=x_0 when T=0. These sample losses are measurable, convex, Gamma_0-Lipschitz, and valued in [0,R_0], hence satisfy the public assumptions.

For fixed w, write A=a(w;X) with X~Q. It is enough to evaluate the variational objective for a product T A with independent T~Bernoulli(alpha). At eta=0 the objective equals E_Q A. For eta>=0,

$$
\eta+\frac1\alpha\mathbb E(TA-\eta)_+
=\eta+\mathbb E_Q(A-\eta)_+
=\mathbb E_Q\max\{A,\eta\}
\geq\mathbb E_Q A.
$$

For eta<0, nonnegativity gives

$$
\eta+\frac1\alpha\mathbb E(TA-\eta)_+
=\mathbb E_Q A+\frac{1-\alpha}{\alpha}(-\eta)
\geq\mathbb E_Q A.
$$

Thus

$$
\operatorname{CVaR}_{\alpha,P_\alpha(Q)}(h(w;Z))=\mathbb E_Q a(w;X)
$$

for every w, including alpha=1. Ordinary excess and embedded CVaR excess are consequently identical pointwise, and both lie in [0,R_0].

### Privacy-preserving sample transformation

Fix any (epsilon,delta)-DP embedded learner A using n records. Construct an ordinary learner A' from m observations X_1,...,X_m as follows. Independently draw T_1,...,T_n iid Bernoulli(alpha). Put X_j in the j-th active slot when j<=m; use x_0 in later active slots and all inactive slots. Include each slot's indicator in its embedded record, and run A on the synthetic dataset.

For any fixed indicator vector, neighboring ordinary datasets produce neighboring synthetic datasets: an ordinary coordinate is used in at most one slot. For every output event E, apply A's DP inequality to this fixed transformation. Averaging over the indicator vector, whose distribution does not depend on the ordinary dataset, gives

$$
\Pr(A'(S)\in E)\leq e^\varepsilon\Pr(A'(S')\in E)+\delta.
$$

Hence A' has the same privacy parameters. This is an adjacency-preserving randomized preprocessing argument, not an invocation of output post-processing for a transformation of the input.

### Coupling and overflow

Fix Q for the moment. To analyze the construction, extend the m ordinary observations to an infinite iid Q sequence, independently of the indicators. Let K=sum_i T_i. Build an ideal embedded sample by putting the j-th element of this sequence in the j-th active slot for every j, without truncation. Its unconditional law is P_alpha(Q)^n. The actual and ideal datasets agree whenever K<=m. This is a joint coupling statement; conditioning either sample on K<=m need not leave its unconditional iid law unchanged.

Run A with the same internal randomness on the two coupled datasets. Their outputs agree whenever the datasets agree. Since excess risks coincide pointwise under the embedding and lie in [0,R_0],

$$
\mathbb E[\text{ordinary excess of }A']
\leq\mathbb E[\text{embedded CVaR excess of }A]
+R_0\Pr(K>m)
\leq\mathbb E[\text{embedded CVaR excess of }A]+M\Pr(K>m).
$$

For completeness, the needed binomial bound follows directly. Put t=n alpha. Independence gives

$$
\mathbb E4^K=(1+3\alpha)^n\leq e^{3t}.
$$

Markov's inequality and m>=4t imply

$$
\Pr(K>m)\leq4^{-m}\mathbb E4^K
\leq\exp\left[-\left(\log4-\frac34\right)m\right]
\leq e^{-ct}
$$

for a universal c>0. The bound is valid also when m>=n, in which case overflow is impossible.

### Lower-bound quantifiers and the ceiling

The ordinary lower interface applies to the constructed private learner A'. It therefore selects some Q in the fixed ordinary family for which A' has the asserted ordinary lower bound. The preceding coupling inequality holds for that same Q. Consequently A has, under P_alpha(Q), expected CVaR excess at least

$$
\widetilde\Omega\left(R_0\min\left\{1,\frac1{\sqrt m}+\frac{\sqrt d}{\varepsilon m}\right\}\right)-Me^{-cn\alpha}.
$$

The embedded domain, record space, loss, and distribution family were fixed before A was chosen. Only Q is selected after A, as required.

Finally let t=n alpha. If t>=1, then 4t<=m<=5t. Thus

$$
\min\left\{1,m^{-1/2}+\frac{\sqrt d}{\varepsilon m}\right\}
\geq\frac15\min\left\{1,t^{-1/2}+\frac{\sqrt d}{\varepsilon t}\right\}.
$$

If 0<t<1, the expression on the right inside its minimum is at least one, whereas m<=4 and the left-hand minimum is at least 1/2. Thus the same constant-factor comparison holds in this regime as well. The interface's logarithmic factors remain inherited at m=ceil(4t); this substitution introduces no additional polynomial or scale dependence.

We obtain the stated converse

$$
\mathbb E\operatorname{Exc}_{P_\alpha(Q)}(\widehat w)
\geq\widetilde\Omega\left(R_0\min\left\{1,\frac1{\sqrt{n\alpha}}+\frac{\sqrt d}{\varepsilon n\alpha}\right\}\right)-Me^{-cn\alpha}.
$$

Together with achievability, this gives the claimed dependence of the privacy terms on epsilon n alpha, with the displayed scales, logarithmic factors, saturation, and residual retained. All six reduction obligations are closed under the expressly assumed interfaces.
