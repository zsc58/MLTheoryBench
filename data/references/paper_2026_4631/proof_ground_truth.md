# Reference Proof

## Contract and obligations

The iteration uses one fixed constraint system and one fixed positive regularization parameter. It is the unrelaxed repair iteration, not an iteration with changing training-time boxes. The radius assumption bounds distance to C on S; it does not assert that S is bounded. No rank assumption is used. The required convergence conclusion is the explicit constraint-violation conclusion F(y^k)→0, not an additional assertion that the vector sequence converges to a single point.

The proof closes six obligations: (1) the objective's definition, differentiability, zero set, and convexity; (2) the gradient representation and well-defined update; (3) the nonlinear Taylor majorization; (4) descent and sublevel invariance under the unchanged regularization condition; (5) the metric inequality and quadratic recurrence; and (6) reciprocal telescoping, including all zero-value cases.

## 1. Objective and regularity

Let B=[ell,u] be the combined box and put
\[
\rho(z)=\tfrac12\operatorname{dist}(z,B)^2,\qquad r(z)=z-P_B(z).
\]
The box is a nonempty closed convex subset of R^{p+m}. Its nonlinear-coordinate intervals are (-infinity,0], and its linear-coordinate intervals are the specified finite closed intervals. Equality intervals cause no difficulty.

For a nonempty interval I, the scalar function a↦(1/2)dist(a,I)^2 is continuously differentiable, with derivative a-P_I(a). This follows directly by differentiating its quadratic pieces; the derivatives agree at finite endpoints. The residual a-P_I(a) is nondecreasing and 1-Lipschitz, including for one-sided intervals and singleton intervals. Summing coordinates gives
\[
\nabla\rho(z)=r(z),\qquad
\|r(z)-r(w)\|\le\|z-w\|.
\]
In particular, rho is convex and continuously differentiable. Integrating its gradient along a segment gives the explicit smoothness estimate
\[
\rho(z+w)\le\rho(z)+\langle r(z),w\rangle+\tfrac12\|w\|^2.
\tag{1}
\]
Indeed, the difference after subtracting the linear term is the integral of \(\langle r(z+tw)-r(z),w\rangle\) for t from 0 to 1, bounded by \(\int_0^1t\|w\|^2dt\).

The public objective is exactly F=rho∘g. Therefore it is finite and continuously differentiable, and
\[
\nabla F(y)=J_g(y)^T r(g(y)).
\tag{2}
\]
Also F≥0 and F^{-1}(0)=C. The scalar function a↦(1/2)[a]_+^2 is convex and nondecreasing, so its composition with each convex component of h is convex. The linear-box term is the convex function (1/2)dist(·,[ell_A,u_A])^2 composed with A. Their sum F is convex. The feasible set C is closed and convex because h is continuous and componentwise convex and the other constraints are affine. Its assumed nonemptiness implies min F=0.

Finally,
\[
J_g(y)=\begin{bmatrix}J_h(y)\\A\end{bmatrix},\qquad
\|J_g(y)-J_g(z)\|_{\mathrm{op}}\le L\|y-z\|.
\tag{3}
\]
The Lipschitz estimate is global, so it can be used before knowing that a proposed next iterate belongs to S.

## 2. Update and elementary operator estimates

At any finite point x, write J=J_g(x), r=r(g(x)), q=J^Tr, and H=J^TJ+lambda I. For every nonzero v,
\[
v^THv=\|Jv\|^2+\lambda\|v\|^2>0.
\]
Thus H is invertible and the prescribed step s=-H^{-1}q exists and is finite. Define
\[
t=\|s\|^2,\qquad Q=q^TH^{-1}q=s^THs.
\]
Then
\[
q^Ts=-Q,\qquad Q=\|Js\|^2+\lambda t.
\tag{4}
\]
For a singular value d≥0 of J, the corresponding factors of JH^{-1}J^T and H^{-1}J^T are d^2/(d^2+lambda)≤1 and d/(d^2+lambda)≤1/(2sqrt(lambda)), respectively. The latter inequality follows from (d-sqrt(lambda))^2≥0. Consequently,
\[
\|Js\|\le\|r\|,\qquad t\le\frac{\|r\|^2}{4\lambda}.
\tag{5}
\]
No positive minimum singular value is needed.

## 3. Nonlinear upper bound

For arbitrary x and s, the integral Taylor remainder
\[
e=g(x+s)-g(x)-Js
  =\int_0^1[J_g(x+vs)-J_g(x)]s\,dv
\]
satisfies
\[
\|e\|\le\tfrac L2\|s\|^2=\tfrac L2t.
\tag{6}
\]
Apply (1) at g(x) with increment Js+e, and use (2). Before estimating the remainder terms separately, group them as follows:
\[
\begin{aligned}
F(x+s)
&\le F(x)+q^Ts+\tfrac12\|Js\|^2
       +\langle r+Js,e\rangle+\tfrac12\|e\|^2\\
&\le F(x)+q^Ts+\tfrac12\|Js\|^2
       +\frac L2\left(\|r+Js\|+\frac L4t\right)t.
\end{aligned}
\tag{7}
\]
This is the source's same Lipschitz-Jacobian majorization argument, retaining the combined residual before applying Cauchy–Schwarz. Replacing ||r+Js|| by ||r||+||Js|| recovers the stated supporting upper bound.

For completeness, the squared-increment calculation underlying that supporting bound is
\[
\|g(x+s)-g(x)\|^2
\le\|Js\|^2+L\|Js\|t+\tfrac{L^2}{4}t^2.
\tag{8}
\]
Its first coefficient is 1, not the erroneous 1/2 printed in source line 352. Multiplication by the external 1/2 in (1) produces the correct supporting lemma.

## 4. Descent and invariance

Set F_0=F(y^0) and M=sqrt(2F_0). If F_0=0, (2) gives q_0=0. The first step is zero, and induction gives y^k=y^0∈C and F(y^k)=0 for every k. This closes that case without division by M or R.

Suppose F_0>0. The public condition is
\[
\lambda^2-LM\lambda-\frac{L^2M^2}{32}\ge0.
\tag{9}
\]
Since lambda>0 and L,M≥0, it implies lambda≥LM.

Assume inductively that x=y^k∈S. Then ||r||≤M. For the prescribed step, (4) gives the residual identity
\[
\begin{aligned}
\|r+Js\|^2
&=\|r\|^2+2q^Ts+\|Js\|^2\\
&=\|r\|^2-\|Js\|^2-2\lambda t.
\end{aligned}
\tag{10}
\]
Let a=||r+Js||. Thus 0≤a≤M and
\[
\lambda t\le\frac{M^2-a^2}{2}\le M(M-a).
\tag{11}
\]
Because lambda≥LM and M>0, L/4≤lambda/M. Hence
\[
a+\frac L4t\le a+\frac{\lambda}{M}t\le M.
\tag{12}
\]
Substituting (12) into (7), and again using lambda≥LM, yields
\[
\begin{aligned}
F(y^{k+1})
&\le F(y^k)+q^Ts+\tfrac12\|Js\|^2+\tfrac{LM}{2}t\\
&\le F(y^k)+q^Ts+\tfrac12\|Js\|^2+\tfrac\lambda2t\\
&=F(y^k)-\tfrac12Q.
\end{aligned}
\tag{13}
\]
Thus F(y^{k+1})≤F(y^k)≤F_0 and y^{k+1}∈S. Induction proves invariance and descent for every iterate. This proof also covers L=0 and equality in the specified regularization condition.

Source-repair note: using only the separated estimates in source lines 398–401 would require LM+L^2M^2/(32lambda)≤lambda/2. Condition (9) gives only an upper bound by lambda. Equations (7) and (10)–(12) repair that inference without strengthening (9), altering the update, or changing the rate. The operator-norm equality printed in source line 393 is also used only in its correct inequality form (5).

## 5. Metric recurrence

As F_0>0, y^0∉C. Since C is closed, its distance from y^0 is positive, so R>0. Put B_0=sigma^2+lambda>0.

For every iterate in S, the stacked Jacobian and the public operator bound give
\[
H_k=J_g(y^k)^TJ_g(y^k)+\lambda I\preceq B_0I.
\tag{14}
\]
For any y*∈C, differentiable convexity gives
\[
F(y^k)\le\langle q_k,y^k-y^*\rangle
\le\sqrt{q_k^TH_k^{-1}q_k}\sqrt{(y^k-y^*)^TH_k(y^k-y^*)}.
\]
The second inequality is ordinary Cauchy–Schwarz applied to H_k^{-1/2}q_k and H_k^{1/2}(y^k-y*). By (14), taking the infimum over C, and then applying the definition of R,
\[
F(y^k)\le R\sqrt{B_0}\sqrt{q_k^TH_k^{-1}q_k}.
\tag{15}
\]
It follows that
\[
q_k^TH_k^{-1}q_k\ge\frac{F(y^k)^2}{R^2B_0}.
\]
Combining this with (13), and writing a_k=F(y^k), gives
\[
a_{k+1}\le a_k-ca_k^2,\qquad c=\frac1{2R^2B_0}>0.
\tag{16}
\]

## 6. Telescoping and boundary cases

If a_j=0 at any iterate, its residual and gradient are zero, so all subsequent iterates remain that same feasible point. The asserted bound then holds for every subsequent index.

For an index k before any zero value has occurred, all a_0,...,a_k are positive. Descent and (16) imply, for 0≤j<k,
\[
\frac1{a_{j+1}}-\frac1{a_j}
=\frac{a_j-a_{j+1}}{a_ja_{j+1}}
\ge c\frac{a_j}{a_{j+1}}\ge c.
\]
Summing yields 1/a_k≥1/a_0+ck, and hence
\[
F(y^k)\le\frac{F(y^0)}{1+F(y^0)k/[2R^2(\sigma^2+\lambda)]}.
\]
The k=0 bound is equality. Together with the zero-value cases, this proves the assertion for all k≥0. The right side tends to zero when F_0>0, and the F_0=0 case is stationary. Thus F(y^k)→0 in every case, which is exactly the residual-feasibility conclusion requested. Every theorem-critical obligation is closed.
