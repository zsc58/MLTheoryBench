# Reference Proof

## Proof Structure

1. Derive the drift and identify the preterminal diagonal.
2. Integrate the flow equation to prove the off-diagonal simplex property, handling terminal time by continuity.
3. Establish that the continuous terminal diagonal is a conditional-expectation version.
4. Derive composition and both time identities, including their terminal cases.
5. Reverse the algebra and use uniqueness to prove the converse.

## Complete Proof

Write
\[
a_{s,t}=\frac{1-t}{1-s},\qquad b_{s,t}=\frac{t-s}{1-s},
\qquad \Phi_{s,t}=a_{s,t}x+b_{s,t}m_{s,t}.
\]
Here these scalar coefficients are used only for \(s<t\), so \(1-s>0\) and \(b_{s,t}>0\).

### 1. Drift and preterminal diagonal

Since \(Z_0\) is integrable and \(Z_1\) is bounded, the conditional velocities are integrable. For \(t<1\),
\[
\dot Z_t=Z_1-Z_0=\frac{Z_1-Z_t}{1-t}.
\]
Conditioning gives the stipulated compatible version
\[
v_t(x)=\frac{q_t(x)-x}{1-t}.
\]
The affine formula is equivalently
\[
m_{s,t}(x)=x+(1-s)\frac{\Phi_{s,t}(x)-x}{t-s}.
\]
For fixed \(s<1\), let \(t\downarrow s\). Flow tangency and the continuous diagonal extension give
\[
m_{s,s}(x)=x+(1-s)v_s(x)=q_s(x).
\]
This includes \(s=0\) by the right derivative.

### 2. Off-diagonal simplex property

Fix \(s<t<1\) and \(x\in D\), and put \(x_u=\Phi_{s,u}(x)\). Direct differentiation yields
\[
\frac{d}{du}\left(\frac{x_u}{1-u}\right)
=\frac{q_u(x_u)}{(1-u)^2}.
\]
Integrating and comparing with the affine representation gives
\[
m_{s,t}(x)=\int_s^t
\frac{(1-s)(1-t)}{(t-s)(1-u)^2}q_u(x_u)\,du.
\]
The integrand is well-defined and integrable on this compact preterminal interval. In particular, along the trajectory \(q_u(x_u)=x_u+(1-u)\dot x_u\), and the assumed regularity supplies continuity. The weight is nonnegative, and
\[
\frac{(1-s)(1-t)}{t-s}
\int_s^t\frac{du}{(1-u)^2}
=\frac{(1-s)(1-t)}{t-s}
\left(\frac1{1-t}-\frac1{1-s}\right)=1.
\]
Each component of the integral is nonnegative and its components sum to one. Thus \(m_{s,t}(x)\in\Delta^{K-1}\).

For fixed \(s<1\), the affine formula and terminal continuity give
\[
m_{s,1}(x)=\lim_{r\uparrow1}m_{s,r}(x)=\Phi_{s,1}(x).
\]
The simplex is closed, so \(m_{s,1}(x)\) also lies in it. One must not obtain this conclusion by substituting \(t=1\) into the ordinary density formula: that substituted weight is zero almost everywhere. Continuity of the diagonal extension also shows that every diagonal value, including \(m_{1,1}\), is simplex-valued.

### 3. Terminal conditional-expectation version

Choose any deterministic sequence \(r_n\uparrow1\). On a probability-one set, all the states \(Z_{r_n}\) and \(Z_1\) lie in \(D\), and \(Z_{r_n}\to Z_1\). Joint continuity of the extended denoiser and the preterminal diagonal identity imply
\[
q_{r_n}(Z_{r_n})=m_{r_n,r_n}(Z_{r_n})
\longrightarrow m_{1,1}(Z_1)
\quad\text{almost surely}.
\]
On the other hand, the conditional triangle inequality gives
\[
\mathbb E\|q_r(Z_r)-Z_r\|
\leq\mathbb E\|Z_1-Z_r\|
=(1-r)\mathbb E\|Z_1-Z_0\|.
\]
Together with \(Z_r\to Z_1\) in \(L^1\), this proves \(q_r(Z_r)\to Z_1\) in \(L^1\). Consequently the almost-sure limit above equals \(Z_1\) almost surely. Since \(m_{1,1}\) is measurable and bounded,
\[
m_{1,1}(Z_1)=Z_1\quad\text{almost surely}
\]
means precisely that \(m_{1,1}\) is a version on \(D\) of \(\mathbb E[Z_1\mid Z_1=\cdot]\). Set \(q_1=m_{1,1}\). This does not assert equality with an independently prescribed version on terminal null sets.

### 4. Composition and time identities

Uniqueness of the preterminal ODE gives
\[
\Phi_{u,t}(\Phi_{s,u}(x))=\Phi_{s,t}(x)
\quad(s<u<t<1).
\]
For fixed \(s<u<1\), continuity in the target time extends this equality to \(t=1\). Substituting the affine formulas, canceling the coefficient of \(x\), and dividing by \(b_{s,t}\) gives
\[
m_{s,t}(x)=
\frac{(1-t)(u-s)}{(1-u)(t-s)}m_{s,u}(x)
+\frac{(t-u)(1-s)}{(1-u)(t-s)}
m_{u,t}(\Phi_{s,u}(x)).
\]
This calculation is valid also at \(t=1\), where the two coefficients are respectively zero and one.

For \(s<t<1\), differentiation in target time gives
\[
\partial_t\Phi_{s,t}
=\frac{m_{s,t}-x}{1-s}
+\frac{t-s}{1-s}\partial_t m_{s,t}.
\]
Substitute the target-time ODE and \(q_t=m_{t,t}\), and multiply by \(1-t\). Collecting terms gives
\[
m_{s,t}(x)=m_{t,t}(\Phi_{s,t}(x))
-\frac{(1-t)(t-s)}{1-s}\partial_t m_{s,t}(x).
\]
To prove this identity at \(t=1\) without using an undefined \(v_1\), fix \(s<1\), put \(y=\Phi_{s,1}(x)\), and use composition to write, for \(s<u<1\),
\[
y=\Phi_{u,1}(\Phi_{s,u}(x))
=m_{u,1}(\Phi_{s,u}(x)).
\]
Letting \(u\uparrow1\) and using joint continuity of \(m\) yields \(y=m_{1,1}(y)\). Since \(m_{s,1}(x)=y\), this is the terminal Lagrangian identity; its derivative coefficient is zero and its one-sided derivative is finite by the stated regularity.

For \(s<t\leq1\), differentiate
\[
\Phi_{s+h,t}(\Phi_{s,s+h}(x))=\Phi_{s,t}(x)
\]
at \(h=0\) from the right. The chain rule and preterminal flow tangency give
\[
\partial_s\Phi_{s,t}(x)+D_x\Phi_{s,t}(x)v_s(x)=0.
\]
This argument includes \(t=1\). The coefficient derivatives are
\[
\partial_s a_{s,t}=\frac{a_{s,t}}{1-s},
\qquad \partial_s b_{s,t}=-\frac{a_{s,t}}{1-s}.
\]
Thus substitution into the source-time equation, followed by use of \(v_s=(m_{s,s}-x)/(1-s)\), gives
\[
0=\frac{a_{s,t}}{1-s}(m_{s,s}-m_{s,t})
+b_{s,t}(\partial_s m_{s,t}+D_xm_{s,t}v_s).
\]
Dividing by \(b_{s,t}>0\) proves
\[
\partial_s m_{s,t}(x)+D_xm_{s,t}(x)v_s(x)
=\frac{1-t}{(1-s)(t-s)}(m_{s,t}(x)-m_{s,s}(x)).
\]
At terminal time the coefficient on the right is zero, with no singular division.

### 5. Converse

Let \(n\) be a family as in the converse statement and write
\[
F_{s,t}(x)=a_{s,t}x+b_{s,t}n_{s,t}(x),\qquad F_{s,s}(x)=x.
\]
The assumed range condition makes every composition meaningful. Multiplying the denoiser semigroup identity by \(b_{s,t}\) and using the displayed coefficients gives \(F_{u,t}\circ F_{s,u}=F_{s,t}\).

For \(s<t<1\), reverse the target-time calculation, using \(n_{t,t}=q_t\), to obtain
\[
\partial_tF_{s,t}(x)=\frac{q_t(F_{s,t}(x))-F_{s,t}(x)}{1-t}
=v_t(F_{s,t}(x)).
\]
Continuity at the preterminal diagonal gives the initial condition \(F_{s,s}(x)=x\). Uniqueness of the ODE therefore implies \(F_{s,t}=\Phi_{s,t}\) for \(t<1\). Continuity in target time implies equality also for \(t=1\).

Reversing the source-time calculation gives
\[
\partial_sF_{s,t}+D_xF_{s,t}v_s=0
\quad(0\leq s<t\leq1).
\]
There is no claim of a target-time equation involving an undefined \(v_1\). Since \(b_{s,t}>0\), equality of the affine maps implies \(n_{s,t}=m_{s,t}\) off the diagonal, and continuity gives equality on the diagonal as well.

All obligations are closed by these calculations, the assumed ODE uniqueness, and elementary conditional-expectation and continuity arguments. No unresolved external dependency remains.
