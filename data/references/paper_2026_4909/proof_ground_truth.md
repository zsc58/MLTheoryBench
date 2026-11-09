# Reference Proof

## Contract and obligations

The two models are separate experiments. The operator and starting point are fixed, all stepsizes are deterministic, and the norm is Euclidean. Independence is required only between the heavy-noise vectors at different times; identical distributions and independence between coordinates are unnecessary. The LRD argument uses unconditional second moments and the scalar inner-product covariance envelope, not a martingale-difference condition or a matrix covariance bound.

The theorem-critical obligations are: (step_001) contraction and rescaling; (step_002) the exact averaged-noise decomposition; (step_003) the independent weighted-sum moment bound; (step_004) the heavy-noise auxiliary recursion and its solution; (step_005) the LRD covariance calculation; (step_006) the LRD auxiliary recursion and its solution; and (step_007) admissible thresholds, uniform constants, and transfer to the original iterates. The scalar estimates used in steps_003 through step_006 are proved below rather than invoked as paper-specific black boxes.

## Parameter choices

Put
\[
\zeta=\frac{\mu}{L^2},\qquad
\lambda=\sqrt{1-\mu^2/L^2},\qquad
\rho=1-\lambda,\qquad
b=\frac{\beta}{\zeta},\qquad
K=K_0,\qquad
a_k=\frac{b}{k+K}.
\]
Thus zeta>0, 0<=lambda<1, and 0<rho<=1. The endpoint mu=L gives lambda=0 and rho=1 and is included throughout.

We will use
\[
C_4=\frac{\zeta[2+4(p-1)]}{\rho},\qquad
C_7=\frac{\zeta(2+4\delta)}{\rho},\qquad
C_5=C_8=\frac{\beta}{\zeta}.
\]
In the relevant model, beta exceeding its threshold and K exceeding or equaling its offset threshold imply K>=b>2 and 0<a_k<=1. In the heavy model they also imply
\[
b>2(p-1),\qquad \rho b/2>1,\qquad b>4(p-1)/\rho.
\]
In the LRD model they imply
\[
b>2,\qquad \rho b/2>1,\qquad b>4\delta/\rho.
\]
These implications follow directly from rho<=1 and respectively rho b>2+4(p-1) and rho b>2+4delta.

All moments used below exist. Indeed, for q=p in the first model or q=2 in the second,
\[
\|x_{k+1}-x^*\|\leq(1+L\beta_k)\|x_k-x^*\|+\beta_k\|\eta_k\|.
\]
The elementary inequality (s+t)^q<=2^{q-1}(s^q+t^q) gives finite qth moments at every finite time by induction. The noise second moment in the LRD model is gamma(0)<=sigma^2. Finite deterministic sums of the noises have the same required moment finiteness. Lipschitz continuity of F also ensures measurability of the recursively defined iterates.

## Step_001: Contraction and rescaling

Set G(x)=x-zeta F(x). Expanding the squared distance gives
\[
\begin{aligned}
\|G(u)-G(v)\|^2
&=\|u-v\|^2-2\zeta\langle F(u)-F(v),u-v\rangle
 +\zeta^2\|F(u)-F(v)\|^2\\
&\leq(1-2\zeta\mu+\zeta^2L^2)\|u-v\|^2
 =\lambda^2\|u-v\|^2.
\end{aligned}
\]
Since F(x*)=0, G(x*)=x*. Uniqueness also follows directly: if F(u)=F(v)=0, strong monotonicity gives mu||u-v||^2<=0. Existence is already assumed publicly, so no unproved zero-existence theorem is needed.

Define tilde-eta_k=-zeta eta_k. Since a_k zeta=beta_k, the recursion is exactly
\[
x_{k+1}=(1-a_k)x_k+a_kG(x_k)+a_k\widetilde\eta_k.
\]

## Step_002: Averaged noise and auxiliary iterates

Define U_0=0 and
\[
U_{k+1}=(1-a_k)U_k+a_k\widetilde\eta_k,
\qquad
w_{i,k}=a_i\prod_{j=i+1}^{k-1}(1-a_j),
\qquad
U_k=\sum_{i=0}^{k-1}w_{i,k}\widetilde\eta_i.
\]
Empty sums are zero and empty products are one. All weights are deterministic and nonnegative. Set z_k=x_k-U_k. Subtracting the U recursion from the x recursion yields
\[
z_{k+1}=(1-a_k)z_k+a_kG(z_k)+a_k\Delta_k,
\qquad
\Delta_k=G(x_k)-G(z_k).
\]
Contractivity gives ||Delta_k||<=lambda||U_k||<=||U_k||. Consequently, writing R_k=||z_k-x*|| and V_k=||Delta_k||,
\[
R_{k+1}\leq(1-\rho a_k)R_k+a_kV_k.
\]
Furthermore, for 1<=q<=2,
\[
\mathbb E\|x_k-x^*\|^q
\leq2^{q-1}\bigl(\mathbb ER_k^q+\mathbb E\|U_k\|^q\bigr)
\leq2\mathbb ER_k^q+2\mathbb E\|U_k\|^q.
\]
No independence between z_k and U_k is used.

## Common scalar product and convolution estimates

Let A,phi,K be positive, let phi_k=phi/(k+K), and assume A phi_k<=1 for all k.

If A phi>1, then
\[
\begin{aligned}
\prod_{i=0}^{k-1}(1-A\phi_i)
&\leq\exp\left(-A\phi\sum_{i=0}^{k-1}\frac1{i+K}\right)\\
&\leq\left(\frac K{k+K}\right)^{A\phi}
\leq\frac K{k+K}.
\end{aligned}
\]
Here the harmonic sum is at least the integral from 0 to k of 1/(x+K). The estimate includes k=0.

For the convolution, let epsilon>=0, 1<e<=2, and epsilon_k=epsilon/(k+K)^e. Suppose A phi>=2(e-1). Define
\[
S_0=0,\qquad S_{k+1}=(1-A\phi_k)S_k+\epsilon_k.
\]
Expansion gives the weighted convolution
\[
S_k=\sum_{i=0}^{k-1}\epsilon_i\prod_{j=i+1}^{k-1}(1-A\phi_j).
\]
Set D_k=2 epsilon_k/(A phi_k). We prove S_k<=D_k by induction. It holds at k=0. With r=e-1 and t=k+K, integration of the derivative of t^{-r} gives
\[
(t+1)^{-r}-t^{-r}
=-r\int_t^{t+1}s^{-r-1}\,ds\geq-r t^{-r-1}.
\]
Therefore
\[
D_{k+1}-D_k\geq-\frac{2(e-1)}{A\phi}\epsilon_k.
\]
Since A phi_k D_k=2 epsilon_k,
\[
D_{k+1}-(1-A\phi_k)D_k-\epsilon_k
\geq\epsilon_k\left(1-\frac{2(e-1)}{A\phi}\right)\geq0.
\]
Nonnegativity of 1-A phi_k now proves the induction. Thus
\[
\sum_{i=0}^{k-1}\epsilon_i\prod_{j=i+1}^{k-1}(1-A\phi_j)
\leq\frac2A\frac{\epsilon_k}{\phi_k}.
\]
The case epsilon=0 is immediate as well.

## Step_003: Independent weighted-noise moment

The standard independent-sum inequality used here is the following Euclidean-vector von Bahr--Esseen inequality: if Y_0,...,Y_{n-1} are independent, mean-zero random vectors with finite pth moments and 1<p<=2, then
\[
\mathbb E\left\|\sum_{i=0}^{n-1}Y_i\right\|^p
\leq2\sum_{i=0}^{n-1}\mathbb E\|Y_i\|^p.
\]
This is the standard_independent result recorded as theory_015 and explicitly stated in the source at L018755-L018756. Its hypotheses hold for Y_i=w_{i,k} tilde-eta_i: the weights are deterministic, the eta_i are independent and mean zero, and
\[
\mathbb E\|\widetilde\eta_i\|^p
=\zeta^p\mathbb E\|\eta_i\|^p\leq\zeta^p\sigma^p.
\]
It follows that
\[
\begin{aligned}
\mathbb E\|U_k\|^p
&\leq2\zeta^p\sigma^p\sum_{i<k}a_i^p
       \prod_{j=i+1}^{k-1}(1-a_j)^p\\
&\leq2\zeta^p\sigma^p\sum_{i<k}a_i^p
       \prod_{j=i+1}^{k-1}(1-a_j)\\
&\leq4\zeta^p\sigma^p a_k^{p-1}.
\end{aligned}
\]
The second inequality uses 0<=1-a_j<=1. The last applies the proved convolution estimate with A=1, phi=b, epsilon=b^p, e=p; b>2(p-1) verifies its threshold. The bound holds also at k=0 because U_0=0.

## Step_004: Heavy-noise auxiliary recursion

For s,t>=0 and 1<p<2, subadditivity of the power p-1 gives
\[
(s+t)^p-s^p=p\int_0^t(s+v)^{p-1}\,dv
\leq p s^{p-1}t+t^p
\leq2s^{p-1}t+t^p.
\]
Apply this to s=(1-rho a_k)R_k and t=a_kV_k. Since 0<=1-rho a_k<=1,
\[
R_{k+1}^p\leq(1-\rho a_k)R_k^p+2a_kR_k^{p-1}V_k+a_k^pV_k^p.
\]
Young's inequality with conjugate exponents p/(p-1) and p yields
\[
R^{p-1}V
\leq\frac{p-1}{p}\frac\rho4 R^p
 +\frac1p\left(\frac4\rho\right)^{p-1}V^p
\leq\frac\rho4R^p+\frac4\rho V^p.
\]
These inequalities remain valid at rho=1. As a_k^p<=a_k and rho<=1, we obtain
\[
R_{k+1}^p\leq\left(1-\frac\rho2a_k\right)R_k^p
 +\frac9\rho a_k\|U_k\|^p.
\]
Taking expectations and using step_003 gives
\[
\mathbb ER_{k+1}^p\leq\left(1-\frac\rho2a_k\right)\mathbb ER_k^p
 +\frac{36\zeta^p\sigma^p}{\rho}a_k^p.
\]
Iteration, z_0=x_0, and the scalar estimates with A=rho/2 and phi=b imply
\[
\begin{aligned}
\mathbb ER_k^p
&\leq\|x_0-x^*\|^p\frac K{k+K}
 +\frac{144\zeta^p\sigma^p}{\rho^2}a_k^{p-1}\\
&=\|x_0-x^*\|^p\frac K{k+K}
 +\frac{144\zeta\sigma^p\beta^{p-1}}{\rho^2(k+K)^{p-1}}.
\end{aligned}
\]
The product condition is rho b/2>1; the convolution condition is b>=4(p-1)/rho. Both were verified above.

## Step_005: LRD weighted-noise second moment

Define the rescaled covariance correctly by
\[
\widetilde\gamma(h)=\mathbb E\langle\widetilde\eta_{t+h},\widetilde\eta_t\rangle
=\zeta^2\gamma(h),
\qquad
|\widetilde\gamma(h)|\leq\zeta^2\sigma^2(1+h)^{-\delta}.
\]
For k>=1 let Q_k=sum_{i<k}w_{i,k}^2. Expanding the finite squared sum and grouping terms by lag gives
\[
\mathbb E\|U_k\|^2
=\widetilde\gamma(0)Q_k
 +2\sum_{h=1}^{k-1}\widetilde\gamma(h)
        \sum_{i=0}^{k-1-h}w_{i,k}w_{i+h,k}.
\]
Cauchy--Schwarz implies
\[
\left|\sum_{i=0}^{k-1-h}w_{i,k}w_{i+h,k}\right|
\leq\left(\sum_{i=0}^{k-1-h}w_{i,k}^2\right)^{1/2}
     \left(\sum_{i=0}^{k-1-h}w_{i+h,k}^2\right)^{1/2}
\leq Q_k.
\]
The convolution estimate, now with A=1, phi=b, epsilon=b^2, e=2, gives
\[
Q_k\leq\sum_{i<k}a_i^2\prod_{j=i+1}^{k-1}(1-a_j)\leq2a_k,
\]
because b>2. Also, for k>=1,
\[
\sum_{h=1}^{k-1}(1+h)^{-\delta}
\leq1+\int_1^k s^{-\delta}\,ds
\leq\frac{k^{1-\delta}}{1-\delta}.
\]
Combining these estimates gives
\[
\begin{aligned}
\mathbb E\|U_k\|^2
&\leq\left(2+\frac{4k^{1-\delta}}{1-\delta}\right)\zeta^2\sigma^2a_k\\
&\leq\frac{6\zeta^2\sigma^2}{1-\delta}k^{1-\delta}a_k
\leq\frac{6\zeta\sigma^2\beta}{(1-\delta)(k+K)^\delta}.
\end{aligned}
\]
The middle inequality uses k>=1. At k=0, U_0=0 establishes the same final bound directly, and also the intermediate bound with 0^{1-delta}=0. No integral with upper endpoint zero is used. The absolute nonsummability assumption remains part of the model but is not needed for this upper estimate.

## Step_006: LRD auxiliary recursion

Squaring the pathwise inequality from step_002 and using 0<=1-rho a_k<=1 gives
\[
R_{k+1}^2\leq(1-\rho a_k)R_k^2+a_k^2V_k^2+2a_kR_kV_k.
\]
The elementary inequality
\[
2RV\leq\frac\rho2R^2+\frac2\rho V^2
\]
and a_k<=1 imply
\[
R_{k+1}^2\leq\left(1-\frac\rho2a_k\right)R_k^2
 +\frac3\rho a_k\|U_k\|^2.
\]
Hence
\[
\mathbb ER_{k+1}^2\leq\left(1-\frac\rho2a_k\right)\mathbb ER_k^2
 +\frac{18\zeta^2\sigma^2}{\rho(1-\delta)}k^{1-\delta}a_k^2.
\]
This includes k=0 by the separate U_0 calculation. For every i>=0,
\[
i^{1-\delta}a_i^2\leq\frac{b^2}{(i+K)^{1+\delta}}.
\]
Iterate the recursion and apply the product estimate and the convolution estimate with A=rho/2, phi=b, epsilon=b^2, e=1+delta. Their conditions rho b/2>1 and b>=4delta/rho hold. We obtain
\[
\begin{aligned}
\mathbb ER_k^2
&\leq\|x_0-x^*\|^2\frac K{k+K}
 +\frac{72\zeta^2\sigma^2b}{\rho^2(1-\delta)(k+K)^\delta}\\
&=\|x_0-x^*\|^2\frac K{k+K}
 +\frac{72\zeta\sigma^2\beta}{\rho^2(1-\delta)(k+K)^\delta}.
\end{aligned}
\]

## Step_007: Transfer, constants, and uniformity

Combining steps_002 through step_004 gives
\[
\mathbb E\|x_k-x^*\|^p
\leq\frac{2K\|x_0-x^*\|^p}{k+K}
 +\frac{296\zeta\sigma^p\beta^{p-1}}{\rho^2(k+K)^{p-1}},
\]
where 288/rho^2+8<=296/rho^2 was used. Similarly, steps_002, step_005, and step_006 give
\[
\mathbb E\|x_k-x^*\|^2
\leq\frac{2K\|x_0-x^*\|^2}{k+K}
 +\frac{156\zeta\sigma^2\beta}{\rho^2(1-\delta)(k+K)^\delta}.
\]
Since K>2, k+K>=1. For either exponent s=p-1 or s=delta, 0<s<1 and (k+K)^{-1}<=(k+K)^{-s}. Thus admissible prefactors are
\[
C_6=2K_0\|x_0-x^*\|^p
 +\frac{296\zeta\sigma^p\beta^{p-1}}{\rho^2},
\qquad
C_9=2K_0\|x_0-x^*\|^2
 +\frac{156\zeta\sigma^2\beta}{\rho^2(1-\delta)}.
\]
Together with the thresholds stated at the start, these are precisely admissible appendix choices after the local notation corrections. All constants are finite, have the required dependence, and are independent of time, dimension, and the particular admissible operator and noise law. The derivation covers every k>=0, a_0=1 when K=b, mu=L, and zero initial error. No uniformity as p or delta approaches an excluded endpoint is asserted.

## Private source-repair ledger

The denominator K1 at L000183 is read as K0, as already recorded for theory_007. The offset declaration in L019032 is read with K0, as already recorded for theory_013; the positive coefficient domain used by its proof and applications is explicit in the scalar estimates. The stepsizes at L018730 and L018743 are a_k, not the constant b. At L018760 the moment is that of tilde-eta_i before substituting zeta^p E||eta_i||^p. At L018810 the displayed continuation has an addition sign. The heavy-noise Young estimate uses 0<rho<=1, including the equality case excluded by the source's incidental strict wording. At L018836 the covariance is that of tilde-eta, equal to zeta^2 gamma. At L018892 the perturbation coefficient is a_k. The LRD estimates involving k^{1-delta} are derived for k>=1, with U_0=0 treated separately. These are local repairs; all proof obligations for the two public claims are closed.
