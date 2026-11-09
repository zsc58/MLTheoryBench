# Reference Proof

## Proof Structure

First, condition on the fitting data and apply the uniform empirical-CDF deviation inequality to certify the mass of the selected sublevel set. Next, convert the directional-distortion bound between the restricted laws into a contamination representation. Conditioning the deployment mixture on the selected bulk and composing the representations gives the effective in-bulk tolerance. Finally, bound the bulk risk and control the complement by Holder's inequality. Zero-weight terms are omitted throughout.

## Complete Proof

### 1. Measurable finite threshold and bulk calibration

Condition on the fitting data, so that the fitted score $s$ is fixed. Independence makes $U_1,\ldots,U_m$ i.i.d. real observations with CDF

$$
F(t)=P\{z:s(z)\le t\}.
$$

The standard uniform empirical-CDF inequality states that for $m$ i.i.d. real observations with CDF $F$ and empirical CDF $G_m$, and any $\delta\in(0,1)$,

$$
\Pr\left\{\sup_{t\in\mathbb R}|G_m(t)-F(t)|\le \sqrt{\frac{\log(2/\delta)}{2m}}\right\}\ge1-\delta.
$$

It applies conditionally here because the held-out sample is independent of the fitting data and $s$ is a measurable real-valued function. Hence the event

$$
H=\left\{\sup_t|G_m(t)-F(t)|\le r_m\right\}
$$

has conditional probability at least $1-\delta$.

Put $u_0=1-\gamma+r_m$. Since $\gamma\ge r_m$ and $\gamma<1$, we have $0<u_0\le1$. Let $U_{(1)}\le\cdots\le U_{(m)}$ denote the order statistics and let $k=\lceil mu_0\rceil\in\{1,\ldots,m\}$. Because $1-\gamma>0$,

$$
\{t:L_m(t)\ge1-\gamma\}=\{t:G_m(t)\ge u_0\}=[U_{(k)},\infty).
$$

Thus $\tau=U_{(k)}$ is finite, the infimum is attained, and $L_m(\tau)\ge1-\gamma$. This includes the boundary $\gamma=r_m$, where $k=m$.

Joint measurability of score evaluation makes the scores measurable random variables. Finite order statistics are measurable, so $\tau$ is measurable. The function of the data and $z$ given by $\mathbf1\{s(z)\le\tau\}$ is jointly measurable; integration against the fixed law $P$ shows that $P(B)$ and the event $E$ are measurable. The event $H$ is also measurable: right-continuity of the two CDFs allows its supremum to be taken over rational thresholds.

On $H$, for every $t$,

$$
F(t)\ge G_m(t)-r_m,\qquad F(t)\ge0,
$$

and therefore $F(t)\ge L_m(t)$. Evaluating at the selected threshold gives

$$
P(B)=F(\tau)\ge L_m(\tau)\ge1-\gamma.
$$

Thus $H\subseteq E$. Averaging the conditional DKW bound over the fitting data proves $\Pr(E)\ge1-\delta$.

### 2. Restricted-law domination and residual measure

Fix a realization in $E$. Any data-dependent centre is now a fixed probability law. We have $P(B)\ge1-\gamma>0$ and, by assumption, $C(B)>0$.

Write $e=e_c$. In the definition of $d_-$ the whole space gives ratio zero, and every ratio is at most one. Consequently $0\le e<1$. For every measurable $A$,

$$
P_B(A)\ge(1-e)C_B(A).
$$

For $C_B(A)>0$ this is the defining distortion inequality; for $C_B(A)=0$ it follows from nonnegativity. Hence

$$
S=P_B-(1-e)C_B
$$

is a nonnegative countably additive measure of total mass $e$. Both restricted laws assign mass one to $B$, so $S(B^c)=0$. If $e>0$, the probability law $K=S/e$ assigns mass one to $B$ and

$$
P_B=(1-e)C_B+eK.
$$

If $e=0$, the nonnegative measure $S$ has total mass zero, so $P_B=C_B$. No residual probability needs to be defined in that case.

### 3. Conditioned deployment mixture and composition

Write $b=R(B)$. Since $\alpha<1$ and $P(B)>0$,

$$
D(B)=(1-\alpha)P(B)+\alpha b>0.
$$

Define

$$
\eta=\frac{\alpha b}{D(B)}=\alpha\rho.
$$

Then $0\le\eta<1$, because

$$
1-\eta=\frac{(1-\alpha)P(B)}{D(B)}>0.
$$

If $b>0$, direct normalization gives, for every measurable $A$,

$$
D_B(A)=\frac{(1-\alpha)P(A\cap B)+\alpha R(A\cap B)}{D(B)}
       =(1-\eta)P_B(A)+\eta R_B(A).
$$

If $b=0$, $\eta=0$ and $D_B=P_B$ directly, without defining $R_B$. These statements also cover $\alpha=0$.

Substitute $P_B=(1-e)C_B+S$. The result is

$$
D_B=(1-\eta)(1-e)C_B+T,
$$

where $T=(1-\eta)S+\eta R_B$ if $b>0$, and $T=S$ if $b=0$. This is a nonnegative measure concentrated on $B$, with total mass

$$
T(\mathsf Z)=(1-\eta)e+\eta
=e+\alpha\rho-\alpha e\rho=e_{\mathrm{eff}}.
$$

Moreover,

$$
1-e_{\mathrm{eff}}=(1-\eta)(1-e)>0,
$$

so $0\le e_{\mathrm{eff}}<1$. If $e_{\mathrm{eff}}>0$, let $K_{\mathrm{eff}}=T/e_{\mathrm{eff}}$. It is a probability law concentrated on $B$, and

$$
D_B=(1-e_{\mathrm{eff}})C_B+e_{\mathrm{eff}}K_{\mathrm{eff}}.
$$

Equivalently, its residual is the normalized sum of the positive-weight components $(1-\eta)eK$ and $\eta R_B$. If $e_{\mathrm{eff}}=0$, $T$ is the zero measure and $D_B=C_B$.

### 4. Well-defined bulk expectation bound

Fix any $a\in\mathcal I$. The moment assumption and Holder's inequality against the constant function one imply $\mathbb E_D\ell_a\le M_p(a)<\infty$. Also,

$$
\mathbb E_{D_B}\ell_a^p
=\frac{\mathbb E_D[\ell_a^p\mathbf1_B]}{D(B)}
\le\frac{M_p(a)^p}{D(B)}<\infty.
$$

The preceding measure domination yields

$$
(1-e_{\mathrm{eff}})\mathbb E_{C_B}\ell_a^p
\le\mathbb E_{D_B}\ell_a^p.
$$

Since the coefficient on the left is strictly positive, the centre p-moment, and hence its first moment, is finite. On $E$, $B$ is nonempty, so $\sup_{z\in B}\ell_a(z)$ is a well-defined element of $[0,+\infty]$. Boundedness of $B$ alone does not imply that this supremum is finite.

When $e_{\mathrm{eff}}>0$, integrate the composed mixture and bound the residual expectation by the pointwise supremum. When $e_{\mathrm{eff}}=0$, use $D_B=C_B$ and omit the supremum term. In both cases, with the stated zero-weight convention,

$$
\mathbb E_{D_B}\ell_a
\le (1-e_{\mathrm{eff}})\mathbb E_{C_B}\ell_a
   +e_{\mathrm{eff}}\sup_{z\in B}\ell_a(z)
=:V_a.
$$

This is an inequality in the nonnegative extended reals. If the supremum is infinite and its coefficient is positive, $V_a=+\infty$ and the final certificate is immediate. Otherwise $V_a$ is finite and nonnegative.

### 5. Tail control and simultaneous conclusion

The deployment tail mass satisfies

$$
D(B^c)=(1-\alpha)P(B^c)+\alpha R(B^c)
\le(1-\alpha)\gamma+\alpha(1-b)=:\beta.
$$

In particular $0\le\beta\le(1-\alpha)\gamma+\alpha<1$. Holder's inequality, with $1/p+1/q=1$, gives

$$
\mathbb E_D[\ell_a\mathbf1_{B^c}]
\le (\mathbb E_D\ell_a^p)^{1/p}
    (\mathbb E_D\mathbf1_{B^c}^{q})^{1/q}
=M_p(a)D(B^c)^{1/q}
\le M_p(a)\beta^{1/q}.
$$

If $V_a<\infty$, splitting the deployment risk and using $0<D(B)\le1$ gives

$$
\begin{aligned}
\mathbb E_D\ell_a
&=D(B)\mathbb E_{D_B}\ell_a+\mathbb E_D[\ell_a\mathbf1_{B^c}]\\
&\le D(B)V_a+M_p(a)\beta^{1/q}\\
&\le V_a+M_p(a)\beta^{1/q}.
\end{aligned}
$$

The last step uses $V_a\ge0$. Together with the already settled case $V_a=+\infty$, this proves exactly

$$
\mathbb E_D\ell_a
\le(1-e_{\mathrm{eff}})\mathbb E_{C_B}\ell_a
+e_{\mathrm{eff}}\sup_{z\in B}\ell_a(z)
+M_p(a)\left[(1-\alpha)\gamma+\alpha\bigl(1-R(B)\bigr)\right]^{1/q}.
$$

The argument is deterministic for each realization in $E$ and applies to every member of the entire loss family. There is no decision-dependent exceptional event and no union bound over $\mathcal I$. Thus the certificate holds simultaneously for every $a$ on the measurable event $E$, whose probability is at least $1-\delta$.
