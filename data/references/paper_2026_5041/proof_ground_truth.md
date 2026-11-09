# Reference Proof

## Contract and Obligations

The contractions are independent and have a common mean; their distributions need not coincide. The initial vector is deterministic. All matrix spectra may include 0, 1/2, and 1. Constants must be independent of the dimension, the mean matrix, the distributions, the initial vector, and the lower-bound horizon.

The obligations are: establish positivity and the scalar recursion; prove stochastic domination with the correct chronological conditioning; prove the quantitative convolution inequality; handle both spectral regimes with valid time thresholds; prove the finite-horizon lower bound with a horizon-independent constant; and justify the endpoint exclusion for the deterministic recursion. A lower bound on the deterministic majorant is not a lower bound on a stochastic process.

## 1. Basic Properties and Stochastic Domination

All matrices N_t are polynomials in bar M and therefore diagonal in a common orthonormal eigenbasis. Write their eigenvalues as lambda_{k,t}, let rho_k be the corresponding eigenvalues of bar M, and put mu_t=||N_t||. Initially lambda_{k,0}=rho_k in [0,1]. If N_t is positive semidefinite, then mu_t=max_k lambda_{k,t} and
\[
\lambda_{k,t+1}=(1-2\rho_k)\lambda_{k,t}+\rho_k\mu_t
=(1-\rho_k)\lambda_{k,t}+\rho_k(\mu_t-\lambda_{k,t}).
\]
Both lambda_{k,t} and mu_t-lambda_{k,t} belong to [0,mu_t]. The last expression is their convex combination. Consequently N_{t+1} is positive semidefinite and
\[
0\le\mu_{t+1}\le\mu_t\le1.
\]
It also gives lambda_{k,t+1}>=(1-rho_k)lambda_{k,t}, hence
\[
\lambda_{k,t}\ge\rho_k(1-\rho_k)^t,\qquad
N_t\succeq\bar M(I-\bar M)^t. \tag{2}
\]
These statements include the endpoint eigenvalues.

For stochastic domination, fix a horizon h. For a deterministic symmetric matrix A define
\[
\Phi_j(A)=\mathbb E[(I-M_j)A(I-M_j)].
\]
This map preserves Loewner order. Set Q_{h,0}=bar M and
\[
Q_{h,i+1}=\Phi_{h-i-1}(Q_{h,i}),\qquad 0\le i<h.
\]
Successive conditioning, using independence and deterministic initialization, gives
\[
\mathbb E\|\Delta_h\|_{\bar M}^2=\Delta_0^\top Q_{h,h}\Delta_0.
\]
This fixed-horizon backward recursion is valid even when the laws of M_j differ.

If Q_{h,i}<=N_i in Loewner order, then
\[
\begin{aligned}
Q_{h,i+1}
&\preceq\Phi_{h-i-1}(N_i)\\
&=N_i-N_i\bar M-\bar M N_i+\mathbb E[M_{h-i-1}N_iM_{h-i-1}]\\
&\preceq N_i(I-2\bar M)+\mu_i\bar M=N_{i+1}.
\end{aligned}
\]
Here N_i commutes with bar M, and
\[
M_jN_iM_j\preceq\mu_i M_j^2\preceq\mu_i M_j
\]
follows from 0<=N_i<=mu_i I and 0<=M_j<=I. Starting with Q_{h,0}=N_0 proves
\[
\mathbb E\|\Delta_h\|_{\bar M}^2
\le\Delta_0^\top N_h\Delta_0
\le\mu_h\|\Delta_0\|^2. \tag{3}
\]
All expectations exist because the matrices are bounded.

## 2. Quantitative Convolution Bound

For an integer t>=1, 0<rho<=1/2, and 0<a<1, define
\[
A_t(\rho)=\rho(1-2\rho)^t,\qquad
B_t(\rho,a)=\rho\sum_{i=1}^t(1-2\rho)^{t-i}i^{-a},
\]
with the zeroth power interpreted as 1. Define, for theta>0,
\[
L_a(\theta)=\theta\int_0^1e^{-2\theta u}(1-u)^{-a}\,du.
\]
The integral is finite since a<1.

### Integral comparison

For 0<rho<1/2 set r=1-2rho and delta=-log r. The exact identity
\[
\rho r^k=\frac12\int_k^{k+1}\delta e^{-\delta x}\,dx
\]
yields
\[
B_t(\rho,a)=\frac12\sum_{k=0}^{t-1}\int_k^{k+1}\delta e^{-\delta x}(t-k)^{-a}\,dx.
\]
For x in [k,k+1), (t-k)^{-a}<=(t-x)^{-a}. Substitution x=tu therefore gives
\[
t^a B_t(\rho,a)\le L_a(\delta t/2). \tag{4}
\]
The singular endpoint of the upper integral is integrable because a<1. At rho=1/2 the sum instead gives exactly t^a B_t(1/2,a)=1/2; no logarithm at that endpoint is used.

### ODE and one-point criterion

Write I(theta)=integral_0^1 e^{-2 theta u}(1-u)^{-a}du and J(theta)=integral_0^1 e^{-2 theta u}(1-u)^{1-a}du. Differentiation under the integral is justified by the integrable bound 2(1-u)^{-a} for the derivative. Thus
\[
L_a'=(1-2\theta)I+2\theta J.
\]
Integration by parts, first before the singular endpoint and then taking the limit, gives
\[
(1-a)I=1-2\theta J.
\]
The boundary term at u=1 vanishes since 1-a>0. Consequently
\[
L_a'(\theta)=1-\left(2-\frac a\theta\right)L_a(\theta). \tag{5}
\]
The same integrable bounds give continuous differentiability. Also 0<=L_a(theta)<=theta/(1-a), so L_a(theta) tends to zero as theta decreases to zero.

For ell in (1/2,1), put theta_ell=a/(2-1/ell). Suppose L_a(theta_ell)<ell. At any point where L_a(theta)=ell, its derivative equals
\[
\Psi(\theta)=1-(2-a/\theta)\ell,
\]
which is positive before theta_ell and negative after it. If L_a ever reaches ell, its first hitting point tau has derivative at least zero, hence tau<theta_ell. Its derivative there is strictly positive. To be below ell at theta_ell it must then have a first return sigma in (tau,theta_ell), with derivative at most zero. But Psi(sigma)>0, a contradiction. Therefore
\[
\sup_{\theta>0}L_a(\theta)\le\ell. \tag{6}
\]
The derivative signs at first hitting and return follow directly from left difference quotients.

### Explicit certificate for a=751/1000

Take
\[
a=\frac{751}{1000},\quad \ell=\frac{499}{500},\quad
\theta_\ell=\frac{374749}{498000},\quad
x=2\theta_\ell=\frac{374749}{249000}.
\]
In particular, 301/200<x<753/500. Set x_+=753/500 and theta_+=753/1000.

Changing variables w=1-u and expanding the exponential gives
\[
L_a(\theta)=\theta e^{-2\theta}\sum_{j=0}^\infty\frac{(2\theta)^j}{j!(j+1-a)}. \tag{7}
\]
Termwise integration is valid by monotone convergence of the nonnegative partial sums.

Let a_j=x_+^j/[j!(j+1-a)]. Their first five values are
\[
a_0=\frac{1000}{249},\quad a_1=\frac{1506}{1249},\quad
 a_2=\frac{567009}{1124500},\quad
 a_3=\frac{15813251}{90250000},\quad
 a_4=\frac{107166402027}{2124500000000}.
\]
Their successive ratios are
\[
r_j=\frac{x_+}{j+1}\frac{j+1-a}{j+2-a}.
\]
For j>=1, r_{j+1}<r_j: after clearing positive denominators the required difference is
\[
j^2+(3-2a)j+(2-4a+a^2)>0.
\]
This polynomial increases for j>=0 and is positive at j=1, where its value is a^2-6a+6>0. Moreover
\[
r_4=\frac{3199497}{13122500}<\frac14.
\]
The geometric tail bound therefore gives
\[
\sum_{j=0}^\infty a_j
\le a_0+a_1+a_2+a_3+\frac43a_4
=\frac{800429153543344037119501}{134108154748420125000000}. \tag{8}
\]
For P_8(y)=sum_{j=0}^8 y^j/j!, positivity of the exponential series gives e^{-y}<1/P_8(y) for y>0. At y=301/200,
\[
P_8(y)=\frac{66414558043759180589143}{14745600000000000000000}.
\]
Using x<x_+, theta_ell<theta_+, and e^{-x}<e^{-301/200} in (7) gives
\[
L_a(\theta_\ell)
<\frac{23700038717989377538168622402764800000}
{23751290207147698032780270875855940541}
<\frac{499}{500}.
\]
The last strict comparison has the exact positive cross-product difference
\[
499\cdot23751290207147698032780270875855940541
-500\cdot23700038717989377538168622402764800000
=1874454372012549273043965669714329959>0.
\]
Thus (6) applies at the required calibrated point, not at an arbitrary theta=3/4.

### Uniform discrete estimate

By (4), the endpoint computation, and (6), t^a B_t<=ell. For t>=1000, concavity of z^a on the positive half-line gives
\[
(t+2)^aB_t\le(1+2a/t)\ell
\le\frac{249874749}{250000000}=:1-d,
\qquad d=\frac{125251}{250000000}>0. \tag{9}
\]
Here the concavity bound is the tangent inequality (1+v)^a<=1+av for v>=0.

Differentiating rho(1-2rho)^t shows its maximum over 0<rho<=1/2 is attained at rho=1/[2(t+1)], with value
\[
\frac1{2(t+1)}\left(\frac t{t+1}\right)^t.
\]
Since a<1, for t>=1000 this implies the sufficient elementary bound
\[
(t+2)^a A_t\le\frac{t+2}{2(t+1)}\le\frac{501}{1001}<1000d.
\]
For the last inequality, clearing denominators gives 125251*1001-501*250000=126251>0. Combining this with (9), for every K>=1000,
\[
A_t(\rho)+K B_t(\rho,a)\le K(t+2)^{-a}
\quad(t\ge1000,\ 0<\rho\le1/2). \tag{10}
\]
This closes the convolution obligation with explicit slack.

## 3. Upper Decay, Including Oscillatory Eigenvalues

Let a=751/1000 and D=4000. We prove the parity-sensitive induction
\[
\mu_t\le
\begin{cases}
D(t+1)^{-a},&t\text{ even},\\
D(t+2)^{-a},&t\text{ odd}.
\end{cases} \tag{11}
\]
For every 0<=t<=2000, mu_t<=1 and (t+2)^a<=2002<D, so even the stronger bound D(t+2)^{-a} holds. Assume (11) at all earlier times and take t>=2001.

If rho_k=0, its coordinate remains zero. If 0<rho_k<=1/2, unrolling the recurrence gives
\[
\lambda_{k,t}
=\rho_k(1-2\rho_k)^t+
\rho_k\sum_{i=1}^t(1-2\rho_k)^{t-i}\mu_{i-1}.
\]
The inductive hypothesis implies mu_{i-1}<=D i^{-a}. All coefficients are nonnegative, so (10), with K=D, bounds this coordinate by D(t+2)^{-a}.

Now suppose rho_k>1/2. If t is even, monotonicity gives mu_t<=mu_{t-1}<=D(t+1)^{-a}, as required. For odd t, write q=1-2rho_k and beta=2rho_k(1-rho_k). The correct two-step calculation is
\[
\begin{aligned}
\lambda_{k,t}
&=q^2\lambda_{k,t-2}+\rho_k q\mu_{t-2}+\rho_k\mu_{t-1}\\
&=q^2\lambda_{k,t-2}+\beta\mu_{t-1}
+\rho_k(2\rho_k-1)(\mu_{t-1}-\mu_{t-2})\\
&\le(1-2\beta)\lambda_{k,t-2}+\beta\mu_{t-2}.
\end{aligned} \tag{12}
\]
Both inequalities use monotonicity of mu. Also
\[
\lambda_{k,1}=\rho_k(1-2\rho_k)+\rho_k\mu_0\le\beta.
\]
If rho_k=1, then beta=0 and lambda_{k,1}=0; (12) and positivity show that all its odd coordinates vanish. Thus no application of (10) at beta=0 is necessary.

Otherwise 0<beta<=1/2. Put t=2s+1; our base range guarantees s>=1000. Iterating (12) along odd times gives
\[
\lambda_{k,2s+1}
\le\beta(1-2\beta)^s+
\beta\sum_{i=1}^s(1-2\beta)^{s-i}\mu_{2i-1}.
\]
By induction, mu_{2i-1}<=D(2i+1)^{-a}<=D(2i)^{-a}. Apply (10) at time s, parameter beta, and K=D/2^a>=1000 to obtain
\[
\lambda_{k,t}\le\frac{D/2^a}{(s+2)^a}
=\frac D{(t+3)^a}\le\frac D{(t+2)^a}.
\]
This proves (11). It follows that mu_t<=2^a D(t+2)^{-a} for all t>=0. Equation (3) proves the first public claim with C=2^a D. The zero mean matrix and zero initial vector are included without division by either.

## 4. Lower Comparison and Quantitative Certificate

For 0<b<1, theta>0, and integer t>=1 define
\[
\Gamma_{b,t}(\theta)=\theta\int_0^1e^{-2\theta u}(1-u+1/t)^{-b}\,du.
\]
Using the same exact cell-integral identity as in Section 2, but now using
\[
(t-k)^{-b}\ge(t-x+1)^{-b}\quad(k\le x\le k+1),
\]
gives
\[
t^bB_t(\rho,b)\ge
\Gamma_{b,t}\left(\frac t2[-\log(1-2\rho)]\right),
\qquad 0<\rho<1/2. \tag{13}
\]
For fixed b and theta, the integrands increase with t and converge almost everywhere to e^{-2 theta u}(1-u)^{-b}. They are nonnegative, and the limiting integral is finite. Monotone convergence therefore gives
\[
\Gamma_{b,t}(\theta)\uparrow L_b(\theta). \tag{14}
\]

Take b=753/1000 and theta_0=3/4. Taylor's theorem for e^{-x} through degree 9 has a positive degree-10 remainder at x=3/2, hence
\[
e^{-3/2}>\sum_{j=0}^9\frac{(-3/2)^j}{j!}
=\frac{102355}{458752}.
\]
The first six terms of the positive series in (7), at this b and theta_0, are
\[
\frac{1000}{247},\quad\frac{1500}{1247},\quad
\frac{375}{749},\quad\frac{1125}{6494},\quad
\frac{3375}{67952},\quad\frac{225}{18656}.
\]
They are respectively strictly greater than
\[
\frac{2024}{500},\quad\frac{601}{500},\quad
\frac{500}{999},\quad\frac{433}{2500},\quad
\frac{149}{3000},\quad\frac{301}{25000}.
\]
Each comparison follows by clearing its positive denominators. The sum of these lower bounds equals 18685693/3121875 and exceeds 299/50, since 934284650>933440625. Equation (7) consequently gives the strict certificate
\[
L_b(\theta_0)
>\frac34\frac{102355}{458752}\frac{299}{50}
=\frac{91812435}{91750400}>1. \tag{15}
\]
Thus, by (14), there is a positive integer t_ref such that Gamma_{b,t}(theta_0)>=1 for every t>=t_ref.

## 5. Finite-Horizon Construction and Endpoint Exclusion

Set rho_m=(1-e^{-2 theta_0/m})/2. Fix an integer T>=t_ref and use the T-dimensional diagonal matrix in the public task. Every rho_m lies strictly between 0 and 1/2. Write mu_t=||N_t^(T)||.

The same coordinate rho_1 is present for every such T. By (2), mu_s>=rho_1(1-rho_1)^s. Therefore
\[
c=\min_{0\le s<t_{\rm ref}}(s+1)^b\rho_1(1-\rho_1)^s>0
\]
is independent of T and supplies the desired inequality for 0<=s<t_ref.

For t_ref<=t<=T, suppose the lower bound holds at all earlier times. Unroll the coordinate with index exactly k=t, which exists because t<=T. Its coefficients are nonnegative, and mu_{i-1}>=c i^{-b}, so
\[
\mu_t\ge\lambda_{t,t}
\ge c\rho_t\sum_{i=1}^t(1-2\rho_t)^{t-i}i^{-b}
=c B_t(\rho_t,b).
\]
The parameter is exactly calibrated:
\[
\frac t2[-\log(1-2\rho_t)]=\theta_0.
\]
Equations (13)-(14) and the definition of t_ref give
\[
\mu_t\ge c t^{-b}\Gamma_{b,t}(\theta_0)
\ge c t^{-b}\ge c(t+1)^{-b}.
\]
This proves the displayed lower bound for every 0<=t<=T. Choosing an arbitrary m>=t would not justify the same parameter substitution.

For completeness, the endpoint exclusion requires more than this displayed lower bound. The source certificate (15) is strict. The map z -> L_z(theta_0) is continuous for z approaching b from below: for z in [751/1000,b], the integrands converge pointwise and are bounded by the integrable function theta_0(1-u)^{-b}. Dominated convergence applies. Consequently there is a fixed b_* in (751/1000,b) with L_{b_*}(theta_0)>1.

Repeat the preceding lower-bound argument with b_* in place of b and exactly the same spectrum rho_m. Equations (13)-(14) hold for every exponent in (0,1). Choose t_* so that Gamma_{b_*,t}(theta_0)>=1 for all t>=t_* and set
\[
c_*=\min_{0\le s<t_*}(s+1)^{b_*}\rho_1(1-\rho_1)^s>0.
\]
The already-derived induction proves
\[
\|N_t^{(T)}\|\ge c_*(t+1)^{-b_*}
\quad(0\le t\le T,\ T\ge t_*).
\]
If a finite K gave the public uniform deterministic bound for any fixed p>=b, choose the horizon T arbitrarily large and evaluate at t=T. Then
\[
c_*(T+1)^{p-b_*}\le K,
\]
which is impossible because p-b_*>0. This proves the endpoint exclusion without weakening the frozen target or asserting stochastic attainability of the majorant.

## Source-Local Corrections

The source's comparison A_sup<f_a(1000) at L001739 must read A_sup=f_a(1000), because the time and spectral maximizers are attained. The sharper source estimate is not needed here; the elementary bound preceding (10) suffices.

The source's final constant and stated initial range leave some odd reindexed times below the summation lemma's threshold. Section 3 explicitly verifies all times through 2000 and uses D=4000, so every subsequent odd application has s>=1000 and K>=1000. These local corrections preserve the theorem and its proof architecture. No unresolved private proof obligation remains.
