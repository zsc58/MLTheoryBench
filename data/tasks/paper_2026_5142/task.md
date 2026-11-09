# Problem

## Setup

Let \(Y\) be finite, and let \(\phi(y)\in\mathbb R^D\), for \(y\in Y\), satisfy
\[
\langle\phi(y),\phi(z)\rangle=\mathbf 1\{y=z\}.
\]
For \(\theta\in\mathbb R^D\), define
\[
\pi_\theta(y)=\frac{\exp(\langle\phi(y),\theta\rangle)}{\sum_{z\in Y}\exp(\langle\phi(z),\theta\rangle)}.
\]
For any reward function \(r:Y\to[-1,1]\), let
\[
V_r(\theta)=\sum_{y\in Y}\pi_\theta(y)r(y).
\]

Let \(y_{\mathrm{star}}\) and \(y_{\mathrm{med}}\) be distinct outputs, and let \(Y_{\mathrm{bad}}\) be nonempty, with
\[
Y=\{y_{\mathrm{star}}\}\mathbin{\dot\cup}\{y_{\mathrm{med}}\}\mathbin{\dot\cup}Y_{\mathrm{bad}}.
\]
Let \(r_G:Y\to[-1,1]\) be constant on \(Y_{\mathrm{bad}}\). Choose any \(y_{\mathrm{bad}}\in Y_{\mathrm{bad}}\), and assume
\[
r_G(y_{\mathrm{star}})>r_G(y_{\mathrm{med}})>0\ge r_G(y_{\mathrm{bad}}).
\]
Define
\[
\Delta_1=r_G(y_{\mathrm{star}})-r_G(y_{\mathrm{med}}),\qquad
\Delta_2=r_G(y_{\mathrm{med}})-r_G(y_{\mathrm{bad}}),
\]
\[
M=\min\left\{1,\frac{0.05\,r_G(y_{\mathrm{med}})^{2/7}}{\Delta_1+\Delta_2}\right\}.
\]

Let \(\theta_0\in\mathbb R^D\) and \(\pi_0=\pi_{\theta_0}\). Assume
\[
\pi_0(y_{\mathrm{star}})<M\min\left\{0.01,\left(\frac{21}{1100(\Delta_1+\Delta_2)}\right)^{7/3},\Delta_2^2\right\}^{13/14},
\]
\[
\max\left\{\frac{2\pi_0(y_{\mathrm{star}})^{7/13}}{\Delta_2M^{7/13}},\,0.05r_G(y_{\mathrm{med}})\right\}
\le\pi_0(Y_{\mathrm{bad}}):=\sum_{y\in Y_{\mathrm{bad}}}\pi_0(y)
\le0.1r_G(y_{\mathrm{med}}).
\]

Fix \(\varepsilon\in(0,\Delta_1)\). Define \(r_P(y)=r_G(y)\) for \(y\ne y_{\mathrm{med}}\) and \(r_P(y_{\mathrm{med}})=r_G(y_{\mathrm{bad}})\). Let \(\theta_t^G\) and \(\theta_t^P\), for \(t\ge0\), solve
\[
\dot\theta_t^G=\nabla V_{r_G}(\theta_t^G),\qquad
\dot\theta_t^P=\nabla V_{r_P}(\theta_t^P),
\]
using the Euclidean gradient and the common initial value \(\theta_0\). Set
\[
t_\varepsilon=\inf\{t\ge0:V_{r_G}(\theta_t^G)\ge r_G(y_{\mathrm{star}})-\varepsilon\},
\]
\[
t_\varepsilon^{\mathrm{no\text{-}med}}=\inf\{t\ge0:V_{r_G}(\theta_t^P)\ge r_G(y_{\mathrm{star}})-\varepsilon\},
\]
with the infimum of an empty set equal to \(+\infty\).

## Task

Prove
\[
t_\varepsilon\ge C\pi_0(y_{\mathrm{star}})^{-14/13},\qquad
C=\frac{2\sqrt2 M^{14/13}\Delta_1r_G(y_{\mathrm{med}})(1-e^{-\sqrt2(\Delta_1-\varepsilon)})}{(\Delta_1+\Delta_2)(1+8\Delta_1)},
\]
and
\[
t_\varepsilon^{\mathrm{no\text{-}med}}\le U_\varepsilon,
\qquad
U_\varepsilon:=\frac{(r_G(y_{\mathrm{star}})+1)^2}{\varepsilon^2[r_P(y_{\mathrm{star}})-V_{r_P}(\theta_0)]}\pi_0(y_{\mathrm{star}})^{-1}.
\]
Moreover, prove that for every \(t\ge U_\varepsilon\),
\[
\pi_{\theta_t^P}(y_{\mathrm{star}})\ge1-\frac{\varepsilon}{\Delta_1+\Delta_2}.
\]

Finally, with \(Y,\phi,r_G\), and \(\varepsilon\) fixed, prove that for every \(T\ge0\) there exists \(\eta>0\) such that every initialization satisfying the displayed assumptions and \(0<\pi_0(y_{\mathrm{star}})<\eta\) satisfies
\[
t_\varepsilon-t_\varepsilon^{\mathrm{no\text{-}med}}\ge T.
\]
If \(t_\varepsilon=+\infty\), interpret its difference with the finite proxy hitting time as \(+\infty\).
