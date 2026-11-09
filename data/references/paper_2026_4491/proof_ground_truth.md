# Reference Proof

## Status and obligations

This reference proves the auxiliary Gaussian construction, both composition inequalities, the operation counts, and the transfer to the actual adaptive matrix mechanism. The latter transfer is derived explicitly in Section 7; it is not assumed from a specialized citation.

The theorem-critical obligations are: (1) identify the history posterior in the correct auxiliary experiment; (2) derive usable history-tail bounds; (3) construct deterministic normalized comparison weights with controlled failure; (4) transfer their order to both scalar Gaussian-pair orientations; (5) compose outside history-measurable failures; (6) count construction operations; and (7) connect the auxiliary laws to actual neighboring mechanism outputs. All seven obligations are closed below.

## 1. Auxiliary experiment and history posteriors

Write the component vectors as $m_j=(m_{j,1},\ldots,m_{j,N})$. Under $P$, choose $J$ uniformly once from $\{1,\ldots,b\}$ and generate $X=m_J+\sigma W$, where $W\sim\mathcal N(0,I_N)$ independently. Under $Q$, generate $X=\sigma W$. These are auxiliary laws, not assertions that actual neighboring mechanism transcripts have these distributions.

Fix round $n$. Choose a deterministic permutation $\pi$ sorting the nonnegative current means, with a deterministic rule for ties. Put $a_i=m_{\pi(i),n}$ and $\mu_i=m_{\pi(i),1:n-1}$. The permutation changes with the round and carries the entire component label with it. Thus $0\le a_1\le\cdots\le a_b$, while the history vectors need not be ordered.

Let $\phi_i(h)$ be the density of $\mathcal N(\mu_i,\sigma^2I_{n-1})$. For empty history this density is 1. The mixture posterior is
\[
\rho_i(h)=\frac{\phi_i(h)}{\sum_{j=1}^b\phi_j(h)}.
\]
It is positive and measurable. Under either orientation the conditional mixture uses this same function of $h$; changing orientation changes the law of the history, not the posterior formula. The conditional zero-mean law is always $\mathcal N(0,\sigma^2)$.

For $i\ge2$, define
\[
L_i(h)=\log\frac{(i-1)^{-1}\sum_{j<i}\phi_j(h)}{\phi_i(h)}.
\]
Bayes' rule gives
\[
\lambda_i(h):=\frac{\rho_i(h)}{\sum_{j\le i}\rho_j(h)}
=\frac1{1+(i-1)e^{L_i(h)}}.
\]
The first reverse hazard is $\lambda_1(h)=1$; no $L_1$ is defined.

## 2. Variational and Gaussian tail bounds

Let $u_j=1/(i-1)$ for $j<i$, and let $\psi$ be any probability vector on these indices. Set $\ell_{ij}(x)=\log(\phi_j(x)/\phi_i(x))$. Jensen's inequality, applied on the support of $\psi$, gives
\[
\begin{aligned}
L_i(x)&=\log\sum_{j<i}u_j e^{\ell_{ij}(x)}\\
&\ge\log\sum_{j:\psi_j>0}\psi_j\frac{u_j e^{\ell_{ij}(x)}}{\psi_j}\\
&\ge\sum_{j<i}\psi_j\ell_{ij}(x)-\sum_{j:\psi_j>0}\psi_j\log\frac{\psi_j}{u_j}.
\end{aligned}
\]
Gaussian density expansion yields
\[
\ell_{ij}(x)=\frac{x^T(\mu_j-\mu_i)}{\sigma^2}
+\frac{\|\mu_i\|^2-\|\mu_j\|^2}{2\sigma^2}.
\]
Consequently the lower bound is $A^Tx+c$, where
\[
A=\frac{\mathbb E_\psi\mu_j-\mu_i}{\sigma^2},\qquad
c=\frac{\|\mu_i\|^2-\mathbb E_\psi\|\mu_j\|^2}{2\sigma^2}
-\mathrm{KL}(\psi\|u).
\]
Under a reference component $X\sim\mathcal N(r,\sigma^2I)$ this affine function has mean $\nu_r=A^Tr+c$ and variance $\xi^2=\sigma^2\|A\|^2$. This follows directly by taking its expectation and variance. Since $L_i\ge A^Tx+c$, each strict lower-tail event $\{L_i<t\}$ is contained in $\{A^TX+c<t\}$, and the analogous inclusion holds for non-strict tails.

For the construction take $\psi=u$, so the KL term vanishes. Write
\[
v_i=\frac1{i-1}\sum_{j<i}\mu_j-\mu_i,\quad
c_i=\frac{\|\mu_i\|^2-(i-1)^{-1}\sum_{j<i}\|\mu_j\|^2}{2\sigma^2},\quad
\xi_i=\frac{\|v_i\|}{\sigma},\quad
\nu_{ik}=c_i+\frac{\mu_k^Tv_i}{\sigma^2}.
\]
Define the strict normal-tail function
\[
T(t;\nu,\xi)=
\begin{cases}
\Phi((t-\nu)/\xi),&\xi>0,\\
\mathbf1\{t>\nu\},&\xi=0.
\end{cases}
\]
Then
\[
P\{L_i(X_{<n})<t\}\le B_i^-(t):=\frac1b\sum_{k=1}^bT(t;\nu_{ik},\xi_i),
\qquad
Q\{L_i(X_{<n})<t\}\le B_i^+(t):=T(t;c_i,\xi_i).
\]
The remove sum is over **all** components. A sum over $k=i,\ldots,b$ with weights $1/b$ is not the history probability law. For non-strict tails the zero-variance indicator is instead $\mathbf1\{t\ge\nu\}$.

## 3. Deterministic thresholds and weights

If $b=1$, use weight 1 in both orientations. There are no failure events.

Suppose $b>1$ and set $\alpha_i=\beta_n/(b-1)$ for $i=2,\ldots,b$. Construct the two orientations separately. Choose finite $\tau_i^r$ with $B_i^r(\tau_i^r)\le\alpha_i$, for $r\in\{-,+\}$.

These thresholds exist deterministically. If $\xi_i>0$, let $z_i=\Phi^{-1}(\alpha_i)$. For add, $\tau_i^+=c_i+\xi_i z_i$ is feasible. For remove,
\[
\ell_i=\min_k\nu_{ik}+\xi_i z_i,\qquad
u_i=\max_k\nu_{ik}+\xi_i z_i
\]
are respectively feasible lower and upper brackets for a root of $B_i^-(t)=\alpha_i$. Bisection retaining the feasible lower endpoint preserves the certified inequality after any fixed number of iterations. If the endpoints coincide, no search is needed. If $\xi_i=0$, then $v_i=0$ and all $\nu_{ik}=c_i$; choose $\tau_i^r=c_i$. Its strict-tail bound is zero. Thus empty history, repeated history vectors, and other zero-variance cases require no excluded regime.

Set
\[
\bar\lambda_1^r=1,\qquad
\bar\lambda_i^r=\frac1{1+(i-1)e^{\tau_i^r}},\qquad
w_i^r=\bar\lambda_i^r\prod_{j=i+1}^b(1-\bar\lambda_j^r).
\]
For $i\ge2$ the hazards lie strictly between zero and one. Define $F_i^r=\prod_{j=i+1}^b(1-\bar\lambda_j^r)$, with $F_0^r=0$. Then $w_i^r=F_i^r-F_{i-1}^r$, so the weights are positive and sum to $F_b^r=1$. Their reverse hazards are exactly the specified $\bar\lambda_i^r$.

Let
\[
E_n^r=\bigcup_{i=2}^b\{h:L_i(h)<\tau_i^r\}.
\]
These sets are measurable. The tail bounds and a union bound give $P\{X_{<n}\in E_n^-\}\le\beta_n$ and $Q\{X_{<n}\in E_n^+\}\le\beta_n$. Outside the appropriate set, the decreasing logistic expression gives $\lambda_i(h)\le\bar\lambda_i^r$ for every $i$.

At $n=1$ all history vectors are empty, $c_i=\xi_i=0$, and the construction yields $\bar\lambda_i^r=1/i$, hence uniform weights and no failure. Zero current means and ties cause no difficulty.

## 4. From categorical order to both Gaussian orientations

For a categorical law with positive prefix probabilities, its reverse hazards satisfy
\[
F_i=F_{i+1}(1-\lambda_{i+1}),\qquad F_b=1,
\]
so $F_i=\prod_{j=i+1}^b(1-\lambda_j)$. Thus $\lambda_i(h)\le\bar\lambda_i^r$ implies $F_i(h)\ge F_i^r$: the posterior index is stochastically no larger than the comparison index.

Here is an explicit proof of the Gaussian-mixture transfer, rather than an appeal to its specialized citation. For nonnegative ordered scalar means $a_i$, let $R_w=\sum_iw_i\mathcal N(a_i,\sigma^2)$ and $G=\mathcal N(0,\sigma^2)$. Stochastic order of the index laws gives stochastic order of $R_w$: couple indices by a common uniform quantile and add the same centered Gaussian. Moreover,
\[
\frac{dR_w}{dG}(x)=\sum_iw_i\exp\left(\frac{a_ix}{\sigma^2}-\frac{a_i^2}{2\sigma^2}\right)
\]
is nondecreasing in $x$. Therefore a maximizing set for $H_\gamma(R_w\|G)$ is an upper ray, and one for $H_\gamma(G\|R_w)$ is a lower ray. If $R_w$ is stochastically no larger than $R_v$, then every upper-ray expression $R_w(S)-\gamma G(S)$ is no greater than its counterpart for $R_v$, while every lower-ray expression $G(S)-\gamma R_w(S)$ is no greater than its counterpart for $R_v$. Taking suprema proves both domination inequalities for every $\gamma>0$. Empty and full rays cover constant ratios, including the case of all means zero.

Consequently, in sorted coordinates define
\[
A_n^-=\sum_iw_i^-\mathcal N(a_i,\sigma^2),\quad B_n^-=\mathcal N(0,\sigma^2),
\]
\[
A_n^+=\mathcal N(0,\sigma^2),\quad B_n^+=\sum_iw_i^+\mathcal N(a_i,\sigma^2).
\]
The remove pair dominates $(P_n^h,Q_n^h)$ off $E_n^-$; the add pair dominates $(Q_n^h,P_n^h)$ off $E_n^+$. Assign the sorted weights back to their original component labels to obtain the public probability vectors. The weights are fixed before any history is observed and may differ between orientations.

## 5. Conditional composition with the correct exceptional measure

We prove the needed composition statement for positive densities, which all laws here have. Let $(U,V)$ be an oriented joint pair and let $(A_n,B_n)$ be its fixed conditional comparison pairs. Let $E$ be the union of its history-measurable failures, with $U(E)\le\eta$. Define the subprobability law $U^*$ by $dU^*=\mathbf1_{E^c}\,dU$. In this argument extend the notation to the subprobability first argument by $H_\gamma(U^*\|V)=\int(u^*-\gamma v)_+$. Pointwise positive-part subadditivity gives
\[
H_\gamma(U\|V)\le H_\gamma(U^*\|V)+U(E).
\]
Write $r_n(h,x)=u_n(x\mid h)/v_n(x\mid h)$ and $\hat r_n=dA_n/dB_n$. Under $V$, the density ratio $dU^*/dV$ is the product of the $r_n$, killed to zero at the first bad history.

For independent comparison observations under $\bigotimes B_n$, define
\[
f_n(a)=\mathbb E\left[\left(a\prod_{j=n+1}^N\hat r_j-\gamma\right)_+\right],\qquad a\ge0.
\]
In particular $f_N(a)=(a-\gamma)_+$ and $f_n(0)=0$. For a good history and $a>0$, put $T=\prod_{j=n+1}^N\hat r_j$. Conditional domination for every positive threshold gives, for each $T>0$,
\[
\int(aT r_n-\gamma)_+\,dV_n
=aT H_{\gamma/(aT)}(U_n\|V_n)
\le aT H_{\gamma/(aT)}(A_n\|B_n).
\]
Integrating over $T$ gives $\int f_n(a r_n)\,dV_n\le f_{n-1}(a)$. For $a=0$ both sides are zero. At a bad history killing gives zero, which is also at most $f_{n-1}(a)$. Backward induction over the remaining actual-history kernels therefore yields
\[
H_\gamma(U^*\|V)\le f_0(1)
=H_\gamma\left(\bigotimes_n A_n\middle\|\bigotimes_n B_n\right).
\]
All interchanges are of nonnegative integrands; the quantities are finite since positive parts are bounded by the relevant likelihood ratio. This proves the composition statement explicitly.

Apply it first to $(U,V)=(P,Q)$ with the remove construction. Its union of failures has probability at most $\sum_n\beta_n=\delta_E$ under $P$. Apply it separately to $(U,V)=(Q,P)$ with the add construction, measuring the failures under $Q$. Thus, for every $\gamma\ge1$,
\[
H_\gamma(P\|Q)\le H_\gamma\left(\bigotimes_n A_n^-\middle\|\bigotimes_n B_n^-\right)+\delta_E,
\]
\[
H_\gamma(Q\|P)\le H_\gamma\left(\bigotimes_n A_n^+\middle\|\bigotimes_n B_n^+\right)+\delta_E.
\]
No extra factor of two is needed: each orientation uses its own probability bound and privacy inequality.

## 6. Accountant and operation counts

Let $D_-(\varepsilon)$ and $D_+(\varepsilon)$ denote the respective product divergences at $\gamma=e^\varepsilon$. The deterministic reported profile is
\[
\delta_{\rm acc}(\varepsilon)=\min\{1,\delta_E+\max(D_-(\varepsilon),D_+(\varepsilon))\}.
\]
The truncation at 1 is valid because hockey-stick divergence at $\gamma\ge1$ is at most 1. Section 7 proves that every actual remove-oriented neighboring output pair is dominated by $(P,Q)$ and every add-oriented pair by $(Q,P)$. Combining that conclusion with Section 5 bounds both actual neighboring divergences by $\delta_{\rm acc}$. The defining supremum for $H_{e^\varepsilon}$ then proves $(\varepsilon,\delta)$-privacy for every $\delta\in[0,1]$ with $\delta\ge\delta_{\rm acc}(\varepsilon)$. This holds for every permitted choice of the adaptive maps. These are deterministic mathematical bounds, not confidence statements. Numerically computed upper bounds for the product divergences can replace the exact values; numerical approximation error must not be silently discarded.

The following counts concern construction of the per-step pairs from the already available mean array, not the final product-divergence calculation. Count scalar arithmetic and scalar normal-function evaluations in the fixed numerical-iteration model and use a fixed number $\kappa$ of scalar search iterations.

At round $n$, sorting costs $O(b\log(2b))$. Prefix vector sums and prefix sums of squared norms cost $O(nb)$. They yield all $v_i,c_i,\xi_i$ in $O(nb)$. The add thresholds then need $O(b\kappa)$ operations. The remove means $\nu_{ik}$ require $O(nb^2)$ operations, and their CDF searches cost $O(b^2\kappa)$. Weight formation costs $O(b)$ using a backward product. Summing over rounds and using $b\le N$ gives $O(N^2b)$ add and $O(N^2b^2)$ remove for fixed $\kappa$.

The finite brackets in Section 3 can also be initialized without evaluating an inverse normal CDF: for reference means $\nu_k$ and positive standard deviation $\xi$, use $\min_k\nu_k-\xi/\sqrt{\alpha}$ as a feasible lower endpoint and $\max_k\nu_k+\xi/\sqrt{1-\alpha}$ as an upper endpoint. The inequalities follow from $\Pr(|Z|\ge t)\le1/t^2$ for a standard normal $Z$, itself obtained from $\mathbb E Z^2=1$. They apply to the single-component add case as well. A fixed number of CDF bisection steps retaining the lower endpoint gives certified thresholds with the same operation counts. Thus the bounds do not depend on exact inverse-CDF evaluation.

Cache the coefficients before division by $\sigma^2$ and $\sigma$. On changing only the common $\sigma$, the cached means scale by $\sigma^{-2}$ and standard deviations by $\sigma^{-1}$. Repeating the scalar searches and weight formation then costs $O(Nb^2)$ remove and $O(Nb\log b)$ add for $b\ge2$, retaining the source's sorting allowance. Cached permutations can only improve this upper bound. For $b=1$ both constructions require $O(N)$ work. Equivalently the add bound is $O(Nb\log(2b))$ uniformly. Feasible search endpoints preserve validity at any fixed iteration count; the counts do not assert arbitrary-precision evaluation at parameter-independent bit cost.

## 7. Transfer to the actual adaptive matrix mechanism

### 7.1 Common-record conditioning and a triangular residual map

Fix arbitrary neighboring datasets $D_0$ and $D_1=D_0\cup\{x_*\}$. Let $S$ contain the batch assignments of the common record occurrences. Its law is the same in both experiments. It is independent of the Gaussian noise and, under $D_1$, of the differing record's uniform batch index $J$. We may first compare the enlarged outputs $(S,T)$: discarding $S$ cannot increase either hockey-stick divergence, since every event depending only on $T$ is also an event in the enlarged space. We do not reveal $J$.

Fix a value $s$ of $S$. Let $G^{\rm c}(t)$ denote the common records' gradient array evaluated using their fixed assignments and the indicated transcript prefixes. Define the same map in the two neighboring experiments by
\[
\mathcal R_s(t)=C\bigl(E^{-1}t-G^{\rm c}(t)\bigr).
\]
This is a measurable bijection with a measurable, causal inverse. Indeed, its $n$th row has the form $C_{nn}t_n$ plus a measurable function of $t_{<n}$. The term $G_n^{\rm c}$ depends only on $t_{<n}$, and $C_{nn}>0$ by nonnegativity and invertibility. Solve successively for each $t_n$. In particular the inverse prefix $t_{<n}$ depends only on the residual prefix $y_{<n}$. A common measurable bijection preserves the defining supremum over events in either hockey-stick orientation.

Under $D_0$, the residual $Y=\mathcal R_s(T)$ equals $Z$. Under $D_1$, conditional on $J=j$, it satisfies
\[
Y_n=Z_n+u_{j,n}(Y_{<n}),
\]
where
\[
u_{j,n}(y_{<n})=
\sum_{\substack{t\le n\\t\equiv j\ ({\rm mod}\ b)}}
C_{nt}\,g_t\bigl(x_*;T_{<t}(y_{<t})\bigr).
\]
For the residue convention, $j=b$ means multiples of $b$. These functions are measurable and predictable. The public clipping and matrix assumptions give, for every history,
\[
\|u_{j,n}(y_{<n})\|
\le\sum_{\substack{t\le n\\t\equiv j\ ({\rm mod}\ b)}} C_{nt}
=m_{j,n}.
\]
The equality uses lower triangularity, so future columns contribute zero to the definition of $m_{j,n}$. This is only a bound on adaptive shifts; it does not identify their laws with fixed-mean Gaussians. The comparison needed to use this bound is proved next.

### 7.2 A Gaussian exponential comparison

Let $K$ and $K'$ be positive-semidefinite $b\times b$ matrices with $K_{ij}\le K'_{ij}$ for all entries. The difference need not be positive semidefinite. For a positive vector $l$, define
\[
X_i=l_i\exp(G_i-K_{ii}/2),\qquad G\sim\mathcal N(0,K),
\]
and define $X'$ analogously using $K'$. We will use the following fact: if $f$ is smooth and $\partial_{ij}f\ge0$ throughout the positive orthant, with the integrability conditions verified below, then
\[
\mathbb E f(X)\le\mathbb E f(X').
\]

Here is a derivation. Put $D=K'-K$ and $K(t)=K+tD$. This is positive semidefinite for $0\le t\le1$. First add $\eta I$ to both endpoint matrices, with $\eta>0$, so the covariance is positive definite. Write $V(t)$ for a Gaussian with covariance $K(t)+\eta I$ and mean $-\operatorname{diag}(K(t)+\eta I)/2$. For $F(v)=f(l_1e^{v_1},\ldots,l_be^{v_b})$, differentiating the Gaussian density and integrating by parts gives
\[
\frac{d}{dt}\mathbb E F(V(t))
=\frac12\sum_{i,j}D_{ij}\mathbb E[\partial_{ij}F(V(t))]
-\frac12\sum_iD_{ii}\mathbb E[\partial_iF(V(t))].
\]
Explicitly, the density derivative is the sum of one half of $\sum_{ij}D_{ij}$ times its second spatial derivatives and one half of $\sum_iD_{ii}$ times its first spatial derivatives; moving these derivatives onto $F$ gives the displayed signs. If $x_i=l_ie^{v_i}$, then
\[
\partial_iF=x_i\partial_if,\qquad
\partial_{ij}F=x_ix_j\partial_{ij}f+\mathbf1\{i=j\}x_i\partial_if.
\]
The first-derivative terms cancel, leaving
\[
\frac{d}{dt}\mathbb E f(X(t))
=\frac12\sum_{i,j}D_{ij}\mathbb E\bigl[X_i(t)X_j(t)\partial_{ij}f(X(t))\bigr]\ge0.
\]
Integrate in $t$ and let $\eta\downarrow0$ to obtain the claim, including singular endpoint covariances.

The functions used below are expectations of a smooth convex Lipschitz function of a positive weighted sum of the coordinates, with random lognormal weights having all moments. Their first and second derivatives are bounded by constants times first and second moments of those weights. After the exponential substitution, the integrands and required derivatives have at most exponential growth in the Gaussian coordinates. Gaussian densities therefore make the differentiations and integrations by parts integrable, with vanishing boundary terms. The regularized covariances stay bounded, so their exponential moments are uniformly bounded; this also justifies the limit as $\eta\downarrow0$.

### 7.3 Adaptive joint likelihood ratios

For the fixed common assignment $s$, write $\mathsf Q$ for the residual law under $D_0$, namely the product of $N$ independent $\mathcal N(0,\sigma^2I_d)$ laws. Let $\mathsf P_j$ be the residual law under $D_1$ conditional on $J=j$, and let $\mathsf P=b^{-1}\sum_j\mathsf P_j$.

Because the shifts are predictable, the conditional density in component $j$ is $\mathcal N(u_{j,n}(y_{<n}),\sigma^2I_d)$. Let $L_{j,n}$ be the density ratio of its first $n$ residual coordinates against the corresponding $\mathsf Q$ marginal. Then $L_{j,0}=1$, and under $\mathsf Q$, writing $Y_n=\sigma W_n$,
\[
L_{j,n}=L_{j,n-1}
\exp\left(\frac{u_{j,n}(Y_{<n})^TW_n}{\sigma}
-\frac{\|u_{j,n}(Y_{<n})\|^2}{2\sigma^2}\right).
\]
Here the $W_n$ are independent standard $d$-dimensional Gaussians. Conditional on the preceding history, the centered Gaussian vector in these log increments has covariance
\[
K_{ij,n}=\frac{u_{i,n}^Tu_{j,n}}{\sigma^2}
\le\frac{\|u_{i,n}\|\|u_{j,n}\|}{\sigma^2}
\le\frac{m_{i,n}m_{j,n}}{\sigma^2}
=:K'_{ij,n}.
\]
Both covariance matrices are positive semidefinite; $K'_n$ is the rank-one covariance obtained by using a single scalar standard Gaussian for all components. Negative entries in $K_n$ are allowed. All bounds hold at every history.

The final mixture density ratio is
\[
\frac{d\mathsf P}{d\mathsf Q}=\frac1b\sum_jL_{j,N}.
\]
In the auxiliary scalar experiment, under $Q$, define independent-across-round multipliers
\[
R_{j,n}=\exp\left(\frac{m_{j,n}Z_n'}{\sigma}-\frac{m_{j,n}^2}{2\sigma^2}\right),
\qquad Z_n'\sim\mathcal N(0,1),
\]
using the same $Z_n'$ for every $j$ at round $n$. Their log-increment covariance is $K'_n$, and
\[
\frac{dP}{dQ}=\frac1b\sum_j\prod_{n=1}^N R_{j,n}.
\]

Fix $\gamma>0$. To treat either orientation, take one of the convex Lipschitz functions
\[
\varphi_-(t)=(t-\gamma)_+,\qquad
\varphi_+(t)=(1-\gamma t)_+.
\]
For $\epsilon>0$, smooth it by $\varphi_\epsilon(t)=\mathbb E\varphi(t+\epsilon Z)$ with $Z\sim\mathcal N(0,1)$. This is smooth and convex with bounded first and second derivatives. If $L$ is the Lipschitz constant of $\varphi$, then $|\varphi_\epsilon(t)-\varphi(t)|\le L\epsilon\mathbb E|Z|$ uniformly in $t$.

For $n=0,\ldots,N$, define deterministic continuation functions on positive vectors $l$ by
\[
V_n(l)=\mathbb E\left[\varphi_\epsilon\left(\frac1b\sum_j l_j\prod_{t=n+1}^N R_{j,t}\right)\right].
\]
An empty product is 1. Put $A_j=\prod_{t=n+1}^N R_{j,t}$. All their moments are finite, and differentiation under the expectation gives
\[
\partial_{ij}V_n(l)=\frac1{b^2}\mathbb E\left[A_iA_j\varphi_\epsilon''\left(\frac1b\sum_j l_jA_j\right)\right]\ge0.
\]
Thus these functions satisfy the hypotheses verified in Section 7.2.

Apply that comparison conditionally on the actual preceding residual history, with $l=(L_{1,n-1},\ldots,L_{b,n-1})$, covariance $K_n$, and comparison covariance $K'_n$. It yields
\[
\mathbb E_{\mathsf Q}[V_n(L_{1,n},\ldots,L_{b,n})\mid Y_{<n}]
\le V_{n-1}(L_{1,n-1},\ldots,L_{b,n-1}).
\]
The right side is exactly the comparison expectation because the reference multipliers at round $n$ are independent of all its future multipliers. Iterating this inequality gives
\[
\mathbb E_{\mathsf Q}\varphi_\epsilon\left(\frac1b\sum_jL_{j,N}\right)
\le
\mathbb E_Q\varphi_\epsilon\left(\frac1b\sum_j\prod_{n=1}^N R_{j,n}\right).
\]
The relevant expectations are finite: the component likelihood ratios have expectation 1, and the payoffs have at most linear growth. Letting $\epsilon\downarrow0$ is justified by the uniform smoothing-error bound. Using $\varphi_-$ proves
\[
H_\gamma(\mathsf P\|\mathsf Q)\le H_\gamma(P\|Q),
\]
and using $\varphi_+$ proves
\[
H_\gamma(\mathsf Q\|\mathsf P)\le H_\gamma(Q\|P).
\]
This proves a joint adaptive comparison, not merely a per-component norm bound. It allows arbitrary measurable predictable shifts satisfying the displayed bounds, so it applies to every adaptive map in the public mechanism. Zero shifts and singular covariances are included by the argument above.

### 7.4 Undo conditioning and conclude

For each fixed $s$, the residual map is a common measurable bijection, so the two inequalities apply to the original transcript laws conditional on $S=s$. The enlarged output laws have the same distribution of $S$. Since a fixed finite dataset gives finitely many common-record assignment configurations, their hockey-stick divergences are the corresponding weighted sums of the conditional divergences. Each summand has the same auxiliary upper bound. Consequently the enlarged neighboring pair is dominated by $(P,Q)$ in the remove orientation and by $(Q,P)$ in the add orientation. Discarding $S$ preserves these inequalities.

Thus every actual neighboring pair has the domination required in Section 6, without revealing the differing record's batch index or assuming that adaptive residual shifts are fixed means. The accountant and the mechanism-level conclusion follow. No reference-proof obligation remains unresolved.
