# Reference Proof

## Proof obligations

1. Establish well-defined continuous conditional predictors and verify the relevant standing regularity and well-posedness conditions in the Gaussian specialization.
2. Derive the Gaussian velocity and prove both directions of the zero-velocity characterization, including the boundary normalization.
3. Verify the normalized schedule and derive its velocity transformation from the conditional-expectation definitions.
4. Evaluate the initial endpoint without dividing by a vanishing schedule coefficient.

All four obligations are closed below. No external stochastic-interpolant theorem is required.

## 1. Gaussian predictors and ambient conditions

Put \(q_t=\alpha_t^2+\beta_t^2\). The schedule assumptions imply \(q_t>0\) throughout \([0,1]\). Since \(q\) is continuous on this compact interval, it is bounded away from zero.

For each fixed \(t\), define
\[
U=\frac{\alpha_t Z+\beta_t X}{\sqrt{q_t}},\qquad
V=\frac{\beta_t Z-\alpha_t X}{\sqrt{q_t}}.
\]
This is an orthogonal change of variables on \(\mathbb R^{2d}\). Its Jacobian has absolute determinant one, and it preserves \(\|Z\|^2+\|X\|^2\); hence the joint Gaussian density of \((U,V)\) factors into two standard Gaussian densities. Thus \(U,V\) are independent standard Gaussian vectors. Inverting the change of variables gives
\[
Z=\frac{\alpha_t U+\beta_t V}{\sqrt{q_t}},\qquad
X=\frac{\beta_t U-\alpha_t V}{\sqrt{q_t}}.
\]
Conditioning on \(I_t=\sqrt{q_t}U=x\) therefore yields
\[
\eta_Z(t,x)=\frac{\alpha_t}{q_t}x,\qquad
\eta_X(t,x)=\frac{\beta_t}{q_t}x.
\]
These are continuous versions. They are the unique spatially continuous versions because the density of \(I_t\) is strictly positive everywhere: two continuous versions equal almost everywhere cannot differ at a point without differing on an open set of positive probability. The argument also applies at both endpoints.

The interpolant has density
\[
\rho_t(x)=(2\pi q_t)^{-d/2}\exp\!\left(-\frac{\|x\|^2}{2q_t}\right)
\]
and score \(s(t,x)=-x/q_t\). Consequently the density, predictors, and score have the source's C1 time and C2 spatial regularity. The velocity is
\[
b^0(t,x)=\frac{\alpha_t\dot\alpha_t+\beta_t\dot\beta_t}{q_t}x
=\frac{\dot q_t}{2q_t}x.
\]
It is spatially smooth and continuous in time. C1 time regularity of this velocity is separately assumed in the public task, as in the standing source assumption; it does not follow from a merely C1 schedule.

For completeness, the zero-diffusion dynamics are globally well posed for every initial condition: from any time \(r\), the solution starting at \(y\) is
\[
Y_t=\sqrt{q_t/q_r}\,y.
\]
Differentiation verifies the equation, and differentiation of \(Y_t/\sqrt{q_t}\) shows uniqueness. Thus no additional ODE existence assumption is needed. The linear and normalized schedules below are smooth and satisfy the same relevant standing conditions.

The source's score-based calculation is also fully recovered by the identities
\[
\eta_Z=-\alpha s,\qquad
\eta_X=\frac{x+\alpha^2s}{\beta},\qquad
b^0=\epsilon^*s+\frac{\dot\beta}{\beta}x,
\quad
\epsilon^*=\alpha^2\frac{\dot\beta}{\beta}-\alpha\dot\alpha,
\]
valid on \(0<t<1\). Here the first two follow from the explicit predictors, and the third follows by substitution into the velocity definition. These are private proof identities, not public assumptions.

## 2. Zero velocity

Because \(d\geq1\), a scalar multiple of every vector in \(\mathbb R^d\) vanishes exactly when the scalar is zero. The velocity formula therefore gives
\[
\bigl[b^0(t,x)=0\text{ for every }t\in(0,1),x\in\mathbb R^d\bigr]
\iff \dot q_t=0\text{ for every }t\in(0,1).
\]
The latter condition says that \(q\) is constant on \((0,1)\). Continuity and \(q_0=\alpha_0^2+\beta_0^2=1\) fix that constant as one. Conversely, \(q_t=1\) on \((0,1)\) gives \(\dot q_t=0\) and hence zero velocity everywhere there. This proves the first claim.

The source's intermediate display with \(\dot q=C\) can be bypassed by the preceding identity \(\alpha\dot\alpha=-\beta\dot\beta\), which immediately gives \(\dot q=0\). There is no unresolved integration-constant issue.

## 3. Schedule and velocity conversion

Let
\[
d_t=(1-t)^2+t^2=2(t-1/2)^2+1/2.
\]
Thus \(d_t\geq1/2\), so the normalized schedule is smooth on the closed interval. Direct differentiation gives
\[
\dot\alpha_t^{\rm L}=-\frac{t}{d_t^{3/2}},\qquad
\dot\beta_t^{\rm L}=\frac{1-t}{d_t^{3/2}}.
\]
It has the specified endpoint values, positive interior coefficients, and strict interior derivative signs. Also \((\alpha_t^{\rm L})^2+(\beta_t^{\rm L})^2=1\).

To derive the conversion rather than invoke it, temporarily take any admissible schedule and set
\[
c_t=\alpha_t+\beta_t>0,\qquad u_t=\beta_t/c_t.
\]
Then \(\alpha_t=c_t(1-u_t)\), \(\beta_t=c_tu_t\), and
\[
I_t=c_t\bar I_{u_t}.
\]
Define privately \(\bar\eta_Z(u,y)=\mathbb E[Z\mid\bar I_u=y]\) and \(\bar\eta_X(u,y)=\mathbb E[X\mid\bar I_u=y]\), using continuous versions. Conditioning on the equivalent random variables gives
\[
\eta_Z(t,x)=\bar\eta_Z(u_t,x/c_t),\qquad
\eta_X(t,x)=\bar\eta_X(u_t,x/c_t).
\]
These equalities first hold almost everywhere and then everywhere by continuity and full support. Moreover, conditional expectation of \(\bar I_u=(1-u)Z+uX\) gives
\[
(1-u)\bar\eta_Z(u,y)+u\bar\eta_X(u,y)=y,
\qquad
\bar b(u,y)=\bar\eta_X(u,y)-\bar\eta_Z(u,y).
\]
Differentiating the two schedule identities and substituting into the velocity definition now gives the complete calculation
\[
\begin{aligned}
b^0(t,x)
&=\dot c_t\bigl((1-u_t)\bar\eta_Z(u_t,x/c_t)+u_t\bar\eta_X(u_t,x/c_t)\bigr)\\
&\quad+c_t\dot u_t\bigl(\bar\eta_X(u_t,x/c_t)-\bar\eta_Z(u_t,x/c_t)\bigr)\\
&=\frac{\dot c_t}{c_t}x+c_t\dot u_t\bar b(u_t,x/c_t).
\end{aligned}
\]
This derives the zero-diffusion conversion directly from the definitions. The existing source repair replacing the duplicated subscript \(\dot u_{tt}\) by \(\dot u_t\) is consistent with this calculation.

For the normalized schedule,
\[
c_t=d_t^{-1/2},\qquad u_t=t,\qquad
\frac{\dot c_t}{c_t}=\frac{1-2t}{d_t},\qquad \dot u_t=1.
\]
Substitution proves
\[
b^{\rm L}(t,x)=\frac{1-2t}{d_t}x+d_t^{-1/2}\bar b(t,\sqrt{d_t}x)
\]
for every requested interior time and spatial point.

The auxiliary source identity \(\dot u/u=\epsilon^*/(\alpha c)\), if used instead, is an interior quotient identity. At \(t=1\), its right-hand side means the continuous extension of \((\alpha\dot\beta/\beta-\dot\alpha)/c\), with value \(-\dot\alpha_1\). No division by zero is needed in the present derivation.

## 4. Initial endpoint

At \(t=0\), the normalized schedule has \(I_0^{\rm L}=Z\), \(\dot\alpha_0^{\rm L}=0\), and \(\dot\beta_0^{\rm L}=1\). Independence gives, in the continuous versions,
\[
b^{\rm L}(0,z)=\mathbb E[X\mid Z=z]=\mathbb E[X].
\]
Similarly,
\[
\bar b(0,z)=\mathbb E[X-Z\mid Z=z]=\mathbb E[X]-z.
\]
Therefore
\[
b^{\rm L}(0,z)=z+\bar b(0,z)=\mathbb E[X]
\]
for every \(z\in\mathbb R^d\). In this frozen Gaussian setting \(\mathbb E[X]=0\). This also agrees with the conversion formula at \(d_0=1\). All requested conclusions are proved.
