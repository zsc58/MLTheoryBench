# Reference Proof

## Proof Structure

1. Identify the normalized terminal tilt and verify that it preserves the prescribed initial law.
2. Establish the value backward dynamics, including compatibility with the terminal observation.
3. Derive the optimal transition family, infinitesimal rates, and jump intensities.
4. Compute the correct Dynkin drifts and prove the conditional terminal-expectation identity.
5. Verify the adjoint solution and its conditional expectation.
6. Establish the analytic formula at every starting state and check boundary cases.

## Standard CTMC facts used

For a rate-generated finite-state CTMC, write
\[
(L_t\varphi)(r)=\sum_z u_t(z,r)\varphi(z)
=\sum_{z\ne r}u_t(z,r)(\varphi(z)-\varphi(r)).
\]
On a compact interval [a,b] contained in [0,1), the integrated rates are finite. The stipulated compensated transition counts imply, by summing the changes of a state function at jumps and its time derivative between jumps, that
\[
f_s(X_s)-f_a(X_a)-\int_a^s(\partial_r f_r+L_r f_r)(X_{r-})\,dr
\]
is a martingale for a bounded, time-absolutely-continuous state function f. Indeed, the jump part is the sum over distinct states v,w of the integrals of f_r(v)-f_r(w) against their compensated transition counts. Its expected absolute jump sum is bounded by a constant times the integral of the sum of the rates. The time derivative is integrable because the state space is finite and f is absolutely continuous. Taking conditional expectations gives Dynkin's formula
\[
\mathbb E[f_s(X_s)\mid X_t=x]-f_t(x)
=\mathbb E\left[\int_t^s(\partial_r f_r+L_r f_r)(X_r)\,dr\,\middle|\,X_t=x\right].
\]
Using X_r instead of X_{r-} in the time integral makes no difference.

The corresponding componentwise Kolmogorov backward equation is
\[
-\partial_t p^{\rm base}_{s|t}(z\mid y)
=\sum_v p^{\rm base}_{s|t}(z\mid v)u_t^{\rm base}(v,y)
\]
on compact intervals before the terminal time, in the absolutely continuous sense. With destination-row/source-column matrices this is \(\partial_tP_{s|t}=-P_{s|t}U_t\), and terminal functions are propagated by \(P_{s|t}^{\mathsf T}\). An ordinary exponential of an integrated time-varying generator is not used.

The public model additionally requires \(X_{1-}=X_1\) under every starting law. Therefore, for any vector b continuous on [0,1],
\[
b_s(X_s)\longrightarrow b_1(X_1)\quad\text{almost surely as }s\uparrow1.
\]
Finite E and continuity of b give a deterministic bound, so bounded convergence applies. Nonexplosion or right infinitesimal rate limits alone would not justify this terminal assertion.

## Complete Proof

### 1. The optimizer and its initial law

Let \(\mu\) be the prescribed initial law and put
\[
Z=\mathbb E_{p^{\rm base}}e^{-g(X_1)},\qquad
\frac{dq}{dp^{\rm base}}=Z^{-1}e^{-g(X_1)}.
\]
Since E is finite and g is real-valued, Z is finite and strictly positive, and this density is bounded above and away from zero. Independence of the base terminal and initial states gives
\[
q(X_0=x)=\frac{\mu(x)}Z\mathbb E_{p^{\rm base}}[e^{-g(X_1)}\mid X_0=x]=\mu(x)
\]
for x in the support of \(\mu\); both sides are zero at other states.

For every admissible p of finite relative entropy,
\[
\mathbb E_p g(X_1)+\operatorname{KL}(p\|p^{\rm base})
=\operatorname{KL}(p\|q)-\log Z.
\]
This follows by substituting \(\log(dq/dp^{\rm base})=-g(X_1)-\log Z\). Laws not absolutely continuous with respect to the base law have infinite objective. Boundedness of the log density also verifies the identity in the extended-real case of infinite relative entropy. Nonnegativity and the equality condition for relative entropy prove that \(p_\star=q\) is the unique optimizer.

### 2. Backward dynamics and terminal compatibility

Define
\[
h_t(r)=\sum_z p^{\rm base}_{1|t}(z\mid r)e^{-g(z)}=e^{-V_t(r)}.
\]
Writing \(c=\min_z e^{-g(z)}>0\) and \(C=\max_z e^{-g(z)}<\infty\), stochasticity gives
\[
c\le h_t(r)\le C.
\]
We first justify its backward equation and continuity through the terminal time, rather than assuming them from right infinitesimal rates.

Choose any fixed terminal state w. Divide the well-posed adjoint terminal-value solution for w by \(e^{g(w)}\), and call the resulting vector b. By its definition, b is absolutely continuous on [0,1], bounded, and satisfies
\[
b'_t(r)=-\sum_z u_t^{\rm base}(z,r)b_t(z),\qquad b_1(r)=e^{-g(r)}.
\]
For any starting pair (t,r) with t<1, Dynkin's formula on [t,s], s<1, is applicable: the rates are integrable on this compact interval and b is bounded and absolutely continuous. It gives
\[
b_t(r)=\mathbb E^{\rm base}_{t,r}[b_s(X_s)].
\]
Under this starting law, \(X_s\to X_1\) almost surely as s increases to 1, by the explicit terminal compatibility assumption. Since b is continuous and bounded, bounded convergence yields
\[
b_t(r)=\mathbb E^{\rm base}_{t,r}[e^{-g(X_1)}]=h_t(r).
\]
At t=1 both vectors equal \(e^{-g}\). This holds for every starting state, not merely those reached under \(\mu\). Thus h is absolutely continuous on [0,1], attains its terminal value, and satisfies
\[
h'_t(r)=-\sum_z u_t^{\rm base}(z,r)h_t(z),\qquad h_1(r)=e^{-g(r)}.
\]
Its positive lower bound permits differentiation of \(V=-\log h\), giving
\[
V'_t(r)=\sum_z u_t^{\rm base}(z,r)e^{-V_t(z)+V_t(r)}
\]
almost everywhere. This argument does not require a global integrable bound on all rates.

### 3. The optimal Markov kernel and rates

Let \(\mathcal F_t\) be the coordinate history through t. The base Markov property gives
\[
\mathbb E_{p^{\rm base}}[e^{-g(X_1)}\mid\mathcal F_t]=h_t(X_t).
\]
For t<s and every positive-mass conditioning state r, Bayes' formula therefore yields
\[
p^\star_{s|t}(z\mid r)
=p^{\rm base}_{s|t}(z\mid r)\frac{h_s(z)}{h_t(r)}.
\]
The same calculation for the conditional future shows that the tilted law is Markov. The displayed expression specifies its canonical extension to every starting state. It is stochastic because
\[
\sum_z p^{\rm base}_{s|t}(z\mid r)h_s(z)=h_t(r),
\]
and it satisfies Chapman--Kolmogorov by cancellation of the intermediate h factors.

For y distinct from x and t<1, the stipulated base infinitesimal limit and continuity of h imply
\[
\begin{aligned}
u_t^\star(y,x)
&=\lim_{\varepsilon\downarrow0}\frac{p^{\rm base}_{t+\varepsilon|t}(y\mid x)}{\varepsilon}
\frac{h_{t+\varepsilon}(y)}{h_t(x)}\\
&=u_t^{\rm base}(y,x)\frac{h_t(y)}{h_t(x)}
=u_t^{\rm base}(y,x)e^{-V_t(y)+V_t(x)}.
\end{aligned}
\]
The optimal diagonal is minus the sum of these off-diagonal rates. It is not obtained by applying the off-diagonal ratio formula to the base diagonal. The ratio of h values is bounded by C/c, so the optimal rates are locally integrable.

For completeness, these rates also describe all jumps of the tilted process, rather than merely its right derivatives. Start at (a,r) and restrict to a compact interval [a,b] with b<1. The density of the tilted future law, restricted to \(\mathcal F_s\), is \(h_s(X_s)/h_a(r)\). For a bounded nonnegative predictable process H and distinct v,w, conditioning the terminal density at each jump and then using the base transition-count compensator gives
\[
\mathbb E^\star_{a,r}\!\int_{(a,b]}H_s\,dN_s^{v,w}
=\frac1{h_a(r)}\mathbb E^{\rm base}_{a,r}\!\int_a^b
H_s\mathbf1_{\{X_{s-}=w\}}u_s^{\rm base}(v,w)h_s(v)\,ds.
\]
The conditioning step is justified by the bounded density martingale; truncating the jump sum and using the finite expected number of jumps on [a,b] justifies passage to the full sum. Changing measure in the time integral shows that its right-hand side is
\[
\mathbb E^\star_{a,r}\!\int_a^b
H_s\mathbf1_{\{X_{s-}=w\}}u_s^{\rm base}(v,w)\frac{h_s(v)}{h_s(w)}\,ds.
\]
Thus these are precisely the optimal jump intensities, so Dynkin's formula applies under the optimal law. Equivalence with the base future law also preserves nonexplosion and \(X_{1-}=X_1\). No extra terminal transition is introduced by tilting.

### 4. The correct Dynkin calculation

Put \(m_t(r)=1/h_t(r)=e^{V_t(r)}\). Then
\[
\partial_t m_t(r)=\frac{\sum_z u_t^{\rm base}(z,r)h_t(z)}{h_t(r)^2}.
\]
Using the off-diagonal rate formula and the conservative optimal diagonal gives
\[
\begin{aligned}
(L_t^\star m_t)(r)
&=\sum_{z\ne r}u_t^{\rm base}(z,r)\frac{h_t(z)}{h_t(r)}
\left(\frac1{h_t(z)}-\frac1{h_t(r)}\right)\\
&=-\frac{\sum_z u_t^{\rm base}(z,r)h_t(z)}{h_t(r)^2}.
\end{aligned}
\]
Consequently \((\partial_t+L_t^\star)m_t=0\). The vector m is bounded and absolutely continuous, by the corresponding facts for h and its positive lower bound. Dynkin's formula on [t,s], followed by bounded convergence using \(X_{1-}=X_1\) under the optimal law, yields
\[
\mathbb E_{p_\star}[e^{g(X_1)}\mid X_t=x]=m_t(x)=\frac1{h_t(x)}
\]
whenever the conditioning event has positive mass. Alternatively, substituting s=1 in the conditional tilted kernel proves this identity directly.

The exponential value-difference function is
\[
f_t(r;y)=h_t(y)m_t(r).
\]
Its drift is
\[
(\partial_t+L_t^\star)f_t(r;y)
=h'_t(y)m_t(r)
=-\sum_z u_t^{\rm base}(z,y)f_t(r;z),
\]
which is generally nonzero. Dynkin's formula therefore gives
\[
f_t(x;y)=\mathbb E_{p_\star}\left[e^{-g(y)+g(X_1)}+
\int_t^1\sum_z u_\tau^{\rm base}(z,y)f_\tau(X_\tau;z)\,d\tau
\,\middle|\,X_t=x\right].
\]
The summed integrand equals \(-h'_\tau(y)m_\tau(X_\tau)\); its absolute integrability follows from absolute continuity of h and boundedness of m. Thus the terminal passage in this integral formula is also justified. This is not a terminal-only martingale identity for f.

### 5. Adjoint verification and conditional expectation

For a fixed terminal state w, define
\[
A_t(y;w)=h_t(y)e^{g(w)}.
\]
This vector is absolutely continuous and satisfies
\[
\frac d{dt}A_t(y;w)=-\sum_z u_t^{\rm base}(z,y)A_t(z;w),
\qquad A_1(y;w)=e^{-g(y)+g(w)}.
\]
Uniqueness in the stated terminal-value class identifies A with the adjoint. Substituting w=X_1 gives
\[
\mathbb E_{p_\star}[\widetilde a_t(y;X)\mid X_t=x]
=h_t(y)\mathbb E_{p_\star}[e^{g(X_1)}\mid X_t=x]
=\frac{h_t(y)}{h_t(x)}.
\]
Multiplication by the base off-diagonal rate proves the second rate representation. This verification does not infer samplewise ODE equality from an equality of expectations.

### 6. Analytic formula and boundary cases

Expanding h gives
\[
\widetilde a_t(y;X)
=\sum_z p^{\rm base}_{1|t}(z\mid y)e^{-g(z)+g(X_1)}.
\]
For each fixed terminal state this is an identity of deterministic vectors. It holds at every starting state, regardless of reachability under \(\mu\). It is also the componentwise backward-propagator solution, with the transpose convention stated above.

At t=1, the identity transition kernel gives the prescribed terminal adjoint. Conditional on X_1=x, its expectation is \(e^{-g(y)+g(x)}\). If the base rate in question has a finite left limit at 1, continuity and positivity of h imply that its canonical optimal counterpart has the finite left limit
\[
u_1^\star(y,x)=u_1^{\rm base}(y,x)e^{-g(y)+g(x)}.
\]
This proves both endpoint rate identities on positive-terminal-mass states. The terminal marginal is the left limit of the earlier marginals because \(X_{1-}=X_1\); thus a state of positive terminal mass also has positive mass at all sufficiently nearby earlier times. No forward rate beyond time 1 is used.

Zero base rates require no division by rates and produce zero optimal rates. Conditional expectations are only taken on positive-mass events. A singleton state space makes the off-diagonal claims vacuous while leaving the analytic formula valid. All exponential quantities are bounded because E is finite and g is real-valued.

## Obligation Closure

Step 1 derives the optimizer and verifies the initial constraint. Step 2 derives the backward dynamics and justifies the terminal passage under every starting law. Step 3 derives the optimal transition family and verifies both its infinitesimal rates and ordinary jump intensities. Step 4 checks the correct drifts, expectation identity, and integrability. Step 5 identifies the adjoint and proves its conditional expectation. Step 6 handles all starting states, zero rates, singleton spaces, and the endpoint convention. All previous source-local index, normalization, transpose, and propagator corrections remain incorporated. No unresolved theorem-critical obligation remains.
