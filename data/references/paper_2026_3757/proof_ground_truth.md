# Reference Proof

## Proof Obligations

1. Verify the residual indices, inverse domains, and measurability of the empirical-CDF discrepancy.
2. Establish uniform convergence of the empirical CDF of the true iid innovations.
3. Derive inverse-volatility stability and a quantitative normalization-error bound, then prove that its sample average vanishes in probability.
4. Construct bounded coordinate cutoffs and prove the product comparison with the correct absolute values.
5. Establish both directions of the uniform translated empirical-CDF sandwich.
6. Establish uniform translation continuity of the joint CDF and complete the limit in the correct order.

The independent results used below are the iid multivariate Glivenko–Cantelli theorem and the law of large numbers for iid integrable real variables. Their relevant statements and hypotheses are given at their applications. The cutoff and translation-continuity facts are derived explicitly.

## Step 1: Definitions and Well-Definedness

Write \(t_0=q+s+1\), \(m=T-q-s>0\), and
\[
X_t=(x_{t-q},\ldots,x_{t-1}),\qquad
Y_t=(\zeta_{t-s},\ldots,\zeta_{t-1}),\qquad
\widehat Y_t=(\widehat\zeta_{t-s},\ldots,\widehat\zeta_{t-1}).
\]
For \(t_0\le t\le T\), every fitted residual in \(\widehat Y_t\) has index between \(q+1\) and \(T-1\), so its definition uses only the observed sample. Put \(g_i=G_i\) and \(\widehat g_i=\widehat G_i\). The stipulated evaluated nonsingularity makes each \(\widehat\eta_t\) a finite random vector almost surely. No deterministic lower bound on fitted volatilities for every sample is assumed.

Define
\[
\widetilde P_T(y)=\frac1m\sum_{t=t_0}^T{\bf1}\{\eta_t\le y\}.
\]
The empirical CDFs are measurable at every fixed argument. For each \(y\), choose rational vectors approaching \(y\) from above componentwise. Continuity from above of the orthant indicators, together with continuity of \(P\), shows that the supremum of either empirical-CDF discrepancy over \(\mathbb R^d\) equals its supremum over \(\mathbb Q^d\). These discrepancies are therefore measurable.

## Step 2: The True-Innovation Empirical CDF

The multivariate Glivenko–Cantelli theorem states that, for iid \(\mathbb R^d\)-valued random vectors \(Z_1,Z_2,\ldots\) with joint CDF \(H\),
\[
\sup_{y\in\mathbb R^d}\left|\frac1n\sum_{k=1}^n{\bf1}\{Z_k\le y\}-H(y)\right|\xrightarrow{p}0.
\]
Apply this standard independent result to \(Z_k=\eta_{q+s+k}\). The sequence is iid with CDF \(P\), \(d,q,s\) are fixed, and \(m\to\infty\). Thus
\[
B_T:=\sup_y|\widetilde P_T(y)-P(y)|\xrightarrow{p}0. \tag{1}
\]
This application does not assume independence between coordinates of an innovation vector.

## Step 3: The Average Normalization Error

Set
\[
e_{F,T}=\sup_X\|\widehat F(X)-F(X)\|,\qquad
e_{G,T}=\max_i\sup_Y|\widehat g_i(Y)-g_i(Y)|,
\qquad
L=\max_i\sup_Y\|\nabla g_i(Y)\|<\infty.
\]
By assumption, \(e_{F,T},e_{G,T}\to_p0\). For every \(q+1\le t\le T\), the model and fitted-residual definition give
\[
\widehat\zeta_t-\zeta_t=F(X_t)-\widehat F(X_t),
\qquad
\|\widehat\zeta_t-\zeta_t\|\le e_{F,T}.
\]
Consequently,
\[
\|\widehat Y_t-Y_t\|\le\sqrt{s}\,e_{F,T}. \tag{2}
\]
Integrating the gradient of \(g_i\) along the segment between two arguments gives
\( |g_i(U)-g_i(V)|\le L\|U-V\|\).
It follows that
\[
|\widehat g_i(\widehat Y_t)-g_i(Y_t)|
\le e_{G,T}+L\sqrt{s}\,e_{F,T}. \tag{3}
\]

Consider
\[
E_T=\{e_{G,T}<c/2,\ e_{F,T}\le1\}.
\]
Its probability tends to one. The second restriction merely keeps all displayed error bounds finite on this event; it is a consequence of consistency, not an additional assumption. Since \(g_i(Y)\ge c\), on \(E_T\), uniformly in \(i,Y\),
\[
\widehat g_i(Y)\ge g_i(Y)-e_{G,T}>c/2.
\]
The correct lower bounds are therefore \(c\) for the true volatility and \(c/2\) for the fitted volatility.

Let \(\Delta_t=\widehat\eta_t-\eta_t\). Using \(\zeta_{t,i}=g_i(Y_t)\eta_{t,i}\), we obtain on \(E_T\)
\[
\Delta_{t,i}
=\frac{\widehat\zeta_{t,i}-\zeta_{t,i}}{\widehat g_i(\widehat Y_t)}
 +\frac{g_i(Y_t)-\widehat g_i(\widehat Y_t)}{\widehat g_i(\widehat Y_t)}\eta_{t,i},
\]
and hence
\[
|\Delta_{t,i}|
\le\frac2c e_{F,T}
 +\frac2c|\eta_{t,i}|\big(e_{G,T}+L\sqrt{s}\,e_{F,T}\big). \tag{4}
\]
There is no upper bound on \(g_i\) in this estimate and no moment condition on \(\zeta_t\).

Define
\[
M_T=\frac1m\sum_{t=t_0}^T\sum_{i=1}^d|\eta_{t,i}|,
\qquad
A_T=\frac1m\sum_{t=t_0}^T\|\Delta_t\|_1.
\]
The moment assumptions imply
\[
\mathbb E\sum_{i=1}^d|\eta_{1,i}|
\le\sum_{i=1}^d\sqrt{\mathbb E\eta_{1,i}^2}
\le d\sqrt C<\infty.
\]
The law of large numbers for iid integrable real variables states that their sample average converges in probability to their common expectation. Apply it to \(\sum_i|\eta_{t,i}|\); the time-indexed variables are iid and integrable. Therefore \(M_T\) converges in probability to this finite expectation and is \(O_p(1)\).

Summing (4) gives, on \(E_T\),
\[
A_T\le\frac{2d}{c}e_{F,T}
 +\frac2c\big(e_{G,T}+L\sqrt{s}\,e_{F,T}\big)M_T. \tag{5}
\]
For completeness, fix \(R>0\) and \(\varepsilon>0\). Then
\[
\Pr(A_T>\varepsilon)
\le\Pr(E_T^c)+\Pr(M_T>R)
 +\Pr\!\left(\frac{2d}{c}e_{F,T}
 +\frac{2R}{c}\big(e_{G,T}+L\sqrt{s}\,e_{F,T}\big)>\varepsilon\right).
\]
The first and third terms tend to zero for fixed \(R\); tightness of \(M_T\) makes the remaining limit superior arbitrarily small by choosing \(R\) large. Thus
\[
A_T\xrightarrow{p}0. \tag{6}
\]
The argument never uses independence between the fitted functions and the innovations.

## Step 4: Coordinate Cutoffs and Product Control

Define
\[
g_0(u)=\begin{cases}
1,&u\le0,\\
(1-u^4)^4,&0<u<1,\\
0,&u\ge1.
\end{cases}
\]
This function takes values in \([0,1]\), is continuously differentiable, and has derivative \(-16u^3(1-u^4)^3\) on \((0,1)\) and zero off \([0,1]\). The one-sided derivatives agree at both endpoints. Thus
\(g_*:=\sup_u|g_0'(u)|<\infty\).
For \(\psi>0\), put
\[
g_{\psi,a}(u)=g_0(\psi(u-a)),\qquad
h_{\psi,y}(u)=\prod_{j=1}^d g_{\psi,y_j}(u_j).
\]
Writing \(\delta=\psi^{-1}\), the definitions give
\[
{\bf1}\{u\le a\}\le g_{\psi,a}(u)\le{\bf1}\{u\le a+\delta\},
\qquad
|g_{\psi,a}'(u)|\le g_*\psi. \tag{7}
\]
For numbers \(a_j,b_j\in[0,1]\), the exact telescoping identity is
\[
\prod_{j=1}^d a_j-\prod_{j=1}^d b_j
=\sum_{j=1}^d\left(\prod_{k<j}a_k\right)(a_j-b_j)\left(\prod_{k>j}b_k\right).
\]
Taking absolute values before bounding the summands yields
\( |\prod_j a_j-\prod_j b_j|\le\sum_j|a_j-b_j|\).
Together with (7), this proves, uniformly in \(y\),
\[
|h_{\psi,y}(u)-h_{\psi,y}(v)|\le g_*\psi\|u-v\|_1. \tag{8}
\]

## Step 5: Both Sandwich Directions

Let \({\bf1}\) denote the all-ones vector in \(\mathbb R^d\). By (7) and (8),
\[
\begin{aligned}
\widehat P_T(y)
&\le\frac1m\sum_{t=t_0}^T h_{\psi,y}(\widehat\eta_t)\\
&\le\frac1m\sum_{t=t_0}^T h_{\psi,y}(\eta_t)+g_*\psi A_T\\
&\le\widetilde P_T(y+\delta{\bf1})+g_*\psi A_T.
\end{aligned}
\]
For the lower direction, (7) gives
\(h_{\psi,y-\delta{\bf1}}(u)\le{\bf1}\{u\le y\}\).
Therefore
\[
\begin{aligned}
\widehat P_T(y)
&\ge\frac1m\sum_{t=t_0}^T h_{\psi,y-\delta{\bf1}}(\widehat\eta_t)\\
&\ge\frac1m\sum_{t=t_0}^T h_{\psi,y-\delta{\bf1}}(\eta_t)-g_*\psi A_T\\
&\ge\widetilde P_T(y-\delta{\bf1})-g_*\psi A_T.
\end{aligned}
\]
Thus, for every \(y\), with exactly the displayed translation,
\[
\widetilde P_T(y-\delta{\bf1})-g_*\psi A_T
\le\widehat P_T(y)
\le\widetilde P_T(y+\delta{\bf1})+g_*\psi A_T. \tag{9}
\]

## Step 6: Uniform Translation Continuity and the Limit

Let \(H_i(a)=\Pr(\eta_{1,i}\le a)\) be the marginal CDFs. First verify that they are continuous. For fixed \(i,a\) and finite \(b\), joint continuity of \(P\), applied while the other coordinates are held at \(b\), implies
\[
\Pr(\eta_{1,i}=a,\ \eta_{1,j}\le b\text{ for all }j\ne i)=0.
\]
Indeed, this probability is the difference between the joint CDF at coordinate \(a\) and its limit as that coordinate increases to \(a\). Letting \(b\to\infty\) proves \(\Pr(\eta_{1,i}=a)=0\). For \(d=1\), this is just the assumed continuity of \(P\). Hence every \(H_i\) is continuous.

A continuous univariate CDF is uniformly continuous: on a sufficiently large compact interval use uniform continuity, and outside that interval use its limits zero and one at the two tails. Consequently,
\[
\sup_a\big(H_i(a+\delta)-H_i(a-\delta)\big)\longrightarrow0
\quad\text{as }\delta\downarrow0.
\]
By monotonicity of \(P\) and a union bound over coordinate boundary strips, whenever \(\|r\|_\infty\le\delta\),
\[
\begin{aligned}
|P(y+r)-P(y)|
&\le P(y+\delta{\bf1})-P(y-\delta{\bf1})\\
&\le\sum_{i=1}^d\big(H_i(y_i+\delta)-H_i(y_i-\delta)\big).
\end{aligned}
\]
Thus
\[
\omega_P(\delta):=
\sup_{y\in\mathbb R^d,\ \|r\|_\infty\le\delta}|P(y+r)-P(y)|
\longrightarrow0. \tag{10}
\]
No density or independence between coordinates is needed.

Combining (1) and (9),
\[
\sup_y|\widehat P_T(y)-P(y)|
\le B_T+\omega_P(\psi^{-1})+g_*\psi A_T. \tag{11}
\]
Given \(\varepsilon>0\), choose a fixed \(\psi\) large enough that \(\omega_P(\psi^{-1})<\varepsilon/3\). For this fixed \(\psi\), (1) and (6) imply that the probability that either remaining term exceeds \(\varepsilon/3\) tends to zero. Equation (11) proves the desired convergence in probability.

All six obligations are closed. The smoothing parameter is not allowed to grow with the sample size without a rate argument: the proof takes the sample-size limit for fixed smoothing and then removes smoothing.

## Private Source-Repair Notes

The chronological lag convention matches the training definitions and the appendix residual identities. The reversed order in the original model display is corrected locally to this convention. In the source telescoping display, both the coordinate indices and the missing absolute values must be corrected; the subsequent source display already states the resulting valid bound. The existing component-index and volatility-maximum repairs remain in force. The strict source lower bound and the public non-strict lower bound express the same existential positive-separation condition after reducing the constant if necessary. No source theorem assumption is replaced by an assumption about a particular training architecture or by consistency only up to scale.
