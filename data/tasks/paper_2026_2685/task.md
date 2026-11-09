# Problem

## Setup

Fix positive integers $J$ and $d$. Let $Z=(X,A,Y)$ have observed-data law $P$, where $A\in\{0,1\}$ and $Y\in\mathbb R^d$. Observations from a fixed law are independent and identically distributed. For each $a\in\{0,1\}$, potential outcomes satisfy consistency, $Y=Y(a)$ on $\{A=a\}$, and conditional exchangeability, $Y(a)\perp A\mid X$. Define $\pi_0(a\mid x)=P(A=a\mid X=x)$ and assume there is a constant $\underline c>0$ such that $\pi_0(a\mid X)\ge\underline c$ almost surely for both arms.

Let $k:\mathbb R^d\times\mathbb R^d\to\mathbb R$ be a fixed measurable, bounded, real positive-definite kernel. For $V=(v_1,\ldots,v_J)\in(\mathbb R^d)^J$, define
\[
K_V(y)=(k(y,v_1),\ldots,k(y,v_J))^\top,\qquad
m_a(x;V)=E_P[K_V(Y)\mid A=a,X=x],
\]
\[
\mu_{a,V}=E[K_V(Y(a))],\qquad \mu_V=\mu_{1,V}-\mu_{0,V}.
\]
Identification gives $\mu_{a,V}=E_P[m_a(X;V)]$ and $\mu_V=E_P[m_1(X;V)-m_0(X;V)]$.

For gradient and local-path statements, use the nonparametric model $\mathcal P$ of observed-data laws with both arm propensities bounded away from zero. The bound may depend on the law; propensities and conditional outcome laws are not known or otherwise restricted. At any $Q\in\mathcal P$, define $m_{a,Q}$ and $\pi_Q$ by its conditional distributions and define
\[
\mu_V(Q)=E_Q[m_{1,Q}(X;V)-m_{0,Q}(X;V)].
\]
Thus $\mu_V(P)$ agrees with the causal contrast above. All conditional functions, fitted functions, and random outputs below are taken in measurable versions.

For a nuisance tuple $\eta=(\pi,r_0,r_1)$, where $\pi$ is a positive propensity model and $r_a(x;V)\in\mathbb R^J$, set
\[
\phi_V^a(Z;\eta)=\frac{1\{A=a\}}{\pi(a\mid X)}\{K_V(Y)-r_a(X;V)\}+r_a(X;V),
\qquad z_V^{\rm dr}=\phi_V^1-\phi_V^0.
\]
At law $Q$, let $\eta_Q=(\pi_Q,m_{0,Q},m_{1,Q})$ and define
\[
\psi_{V,Q}(Z)=z_V^{\rm dr}(Z;\eta_Q)-\mu_V(Q),
\qquad \Sigma_V(Q)=\operatorname{Var}_Q(\psi_{V,Q}).
\]
When the law is $P$, abbreviate these by $\eta_0$, $\psi_V$ and $\Sigma_V$.

### Fixed-Location Estimation

Let $Z_1,\ldots,Z_n$ be iid from $P$. Use a fixed number $K\ge2$ of validation folds $\mathcal I_1,\ldots,\mathcal I_K$, chosen independently of the observation values, with $\min_k|\mathcal I_k|/n\ge c_K>0$ for a fixed constant $c_K$. For $i\in\mathcal I_k$, use a common nuisance estimate
\[
\widehat\eta_k=(\widehat\pi_k,\widehat m_{0,k},\widehat m_{1,k})
\]
trained only on observations outside fold $k$. Any fitting randomization is independent of the observations. The fitted propensities are positive, and, for each fixed $V$, there are constants $c_\pi>0$ and $M<\infty$ such that, with probability tending to one,
\[
\inf_{k,a,x}\widehat\pi_k(a\mid x)\ge c_\pi,
\qquad \sup_{k,a,x}\|\widehat m_{a,k}(x;V)\|\le M.
\]
The norm on vectors is Euclidean. Define
\[
\alpha_{a,k}=\|\widehat\pi_k(a\mid\cdot)-\pi_0(a\mid\cdot)\|_{L_2(P_X)},
\qquad
\beta_{a,k}(V)=\|\widehat m_{a,k}(\cdot;V)-m_a(\cdot;V)\|_{L_2(P_X;\mathbb R^J)}.
\]
Assume, for each fixed $V$ under consideration,
\[
\max_k\sum_{a=0}^1\{\alpha_{a,k}+\beta_{a,k}(V)\}=o_p(1),
\qquad
\max_k\sum_{a=0}^1\alpha_{a,k}\beta_{a,k}(V)=o_p(n^{-1/2}).
\]
For $i\in\mathcal I_k$, set $z_{i,V}^{\rm dr}=z_V^{\rm dr}(Z_i;\widehat\eta_k)$ and define, for $n\ge2$,
\[
\bar z_{n,V}^{\rm dr}=\frac1n\sum_{i=1}^n z_{i,V}^{\rm dr},\qquad
S_{n,V}^{\rm dr}=\frac1{n-1}\sum_{i=1}^n(z_{i,V}^{\rm dr}-\bar z_{n,V}^{\rm dr})(z_{i,V}^{\rm dr}-\bar z_{n,V}^{\rm dr})^\top.
\]
Let $\gamma_n>0$ decrease to zero and put
\[
T_n(V)=n(\bar z_{n,V}^{\rm dr})^\top(S_{n,V}^{\rm dr}+\gamma_n I_J)^{-1}\bar z_{n,V}^{\rm dr}.
\]
Assume $\Sigma_V$ is positive definite for each fixed location tuple to which the inverse-covariance conclusions are applied.

### Local Analysis

Fix $V$ and $P_0\in\mathcal P$ with $\mu_V(P_0)=0$. The fixed-location nuisance conditions above are assumed under $P_0$. Let $t\mapsto P_{t,g}\in\mathcal P$ be a regular quadratic-mean differentiable path through $P_0$, with score $g\in L_2^0(P_0)$. Explicitly, for densities $p_{t,g}$ relative to a common dominating measure $\nu$,
\[
\int\left(\sqrt{p_{t,g}}-\sqrt{p_0}-\frac t2g\sqrt{p_0}\right)^2d\nu=o(t^2),
\qquad E_{P_0}g=0,\quad E_{P_0}g^2<\infty.
\]
For each fixed $h\in\mathbb R$, define $P_{n,h,g}=P_{h/\sqrt n,g}^{\otimes n}$. Under these alternatives, evaluate the same cross-fitted estimator on these $n$ observations, with the same data-independent fold and fitting-randomization rules. In this local subsection, write $\psi_V=\psi_{V,P_0}$ and $\Sigma_V=\Sigma_V(P_0)$, and define
\[
\eta_V(g)=E_{P_0}[\psi_Vg],\qquad
\lambda_V(g)=\eta_V(g)^\top\Sigma_V^{-1}\eta_V(g).
\]
Assume $t\mapsto\Sigma_V(P_{t,g})$ is continuous at zero and remains positive definite for all sufficiently small $|t|$. Where $\Sigma_V(Q)$ is nonsingular, define
\[
\Lambda_V(Q)=\mu_V(Q)^\top\Sigma_V(Q)^{-1}\mu_V(Q).
\]

### Location Learning

For this part, return to a fixed law $P$ satisfying the identification and positivity conditions. Fix $0\le R<\infty$, a nonempty compact class $\mathcal V\subset[-R,R]^{Jd}$, and a ridge parameter $\tau>0$. Define
\[
\Pi(\mathcal V)=\{v\in\mathbb R^d:v=v_j\text{ for some }V=(v_1,\ldots,v_J)\in\mathcal V\}.
\]
Use independent iid samples from $P$ of sizes $n_\eta$ and $n_{\rm tr}$, both tending to infinity. Fit $\widehat\pi$ and scalar functions $\widehat m_a(x;v)$ only on the sample of size $n_\eta$, with independent fitting randomization, and set
\[
\widehat m_a(x;V)=(\widehat m_a(x;v_1),\ldots,\widehat m_a(x;v_J))^\top.
\]
Similarly, write $m_a(x;v)=E_P[k(Y,v)\mid A=a,X=x]$ for the scalar true regressions.

There are finite constants $B_k,L_k,B_m,L_m$ and $c_\pi>0$, independent of both sample sizes, such that for all candidate locations $v,v'\in\Pi(\mathcal V)$ and all $y$,
\[
|k(y,v)|\le B_k,\qquad |k(y,v)-k(y,v')|\le L_k\|v-v'\|.
\]
With probability tending to one, for all arms, covariates and candidate locations,
\[
\widehat\pi(a\mid x)\ge c_\pi,\qquad
|\widehat m_a(x;v)|\le B_m,\qquad
|\widehat m_a(x;v)-\widehat m_a(x;v')|\le L_m\|v-v'\|.
\]
Fitted propensities are positive also outside this high-probability event. Define the nonnegative random nuisance error
\[
\rho_{n_\eta}=\sum_{a=0}^1\left[
\|\widehat\pi(a\mid\cdot)-\pi_0(a\mid\cdot)\|_{L_2(P_X)}
+\sup_{v\in\Pi(\mathcal V)}\|\widehat m_a(\cdot;v)-m_a(\cdot;v)\|_{L_2(P_X)}
\right]
\]
and assume $\rho_{n_\eta}=o_p(1)$.

Let $U_1,\ldots,U_{n_{\rm tr}}$ denote the independent sample on which locations are learned, set
\[
\widehat z_{i,V}=z_V^{\rm dr}(U_i;(\widehat\pi,\widehat m_0,\widehat m_1)),
\]
and define its empirical mean $\widehat\mu_V=n_{\rm tr}^{-1}\sum_i\widehat z_{i,V}$ and centered covariance
\[
\widehat\Sigma_V=\frac1{n_{\rm tr}-1}\sum_i(\widehat z_{i,V}-\widehat\mu_V)(\widehat z_{i,V}-\widehat\mu_V)^\top.
\]
Define
\[
P_\tau(V)=\mu_V^\top(\Sigma_V+\tau I_J)^{-1}\mu_V,
\qquad
\widehat P_\tau(V)=\widehat\mu_V^\top(\widehat\Sigma_V+\tau I_J)^{-1}\widehat\mu_V.
\]
Here the population quantities are evaluated at $P$. No nonsingularity assumption is imposed on covariances throughout the learning class. Let a measurable output $\widehat V\in\mathcal V$ satisfy
\[
\widehat P_\tau(\widehat V)\ge\sup_{V\in\mathcal V}\widehat P_\tau(V)-e_{\rm tr},\qquad e_{\rm tr}\ge0,
\]
where $e_{\rm tr}$ is a finite deterministic or measurable random optimization-error bound. All dimensions, class parameters, regularity bounds, and $\tau$ are fixed as sample sizes grow.

## Task

Prove the following integrated theorem. For every fixed $V$, the centered augmented feature $\psi_V$ is the canonical gradient of $\mu_V$ in $\mathcal P$, and the cross-fitted estimator satisfies
\[
\sqrt n(\bar z_{n,V}^{\rm dr}-\mu_V)=n^{-1/2}\sum_{i=1}^n\psi_V(Z_i)+o_p(1),\qquad
S_{n,V}^{\rm dr}\to_p\Sigma_V.
\]
Under the specified QMD alternatives, for every fixed $h\in\mathbb R$,
\[
\sqrt n\,\bar z_{n,V}^{\rm dr}\Rightarrow N(h\eta_V(g),\Sigma_V),\qquad
T_n(V)\Rightarrow\chi_J^2(h^2\lambda_V(g)).
\]
Moreover,
\[
n\Lambda_V(P_{h/\sqrt n,g})\to h^2\lambda_V(g).
\]
Finally,
\[
\sup_{V\in\mathcal V}|\widehat P_\tau(V)-P_\tau(V)|
=O_p\left(\sqrt{Jd\log n_{\rm tr}/n_{\rm tr}}+\rho_{n_\eta}\right),
\]
and for any $V^\star\in\arg\max_{V\in\mathcal V}P_\tau(V)$,
\[
P_\tau(V^\star)-P_\tau(\widehat V)
=O_p\left(\sqrt{Jd\log n_{\rm tr}/n_{\rm tr}}+\rho_{n_\eta}+e_{\rm tr}\right).
\]
The constants implicit in these learning rates may depend on the fixed dimensions, radius, regularity and positivity bounds, and $\tau$, but not on the sample sizes. For the nonnegative random rate expressions, $O_p$ means that division by the displayed rate yields a tight sequence.
