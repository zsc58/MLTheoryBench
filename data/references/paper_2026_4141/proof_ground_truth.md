# Reference Proof

## Proof Structure and Obligations

The proof closes the following obligations: (1) separability, measurability, existence of minimizers, and differentiation of the population risk; (2) weighted Hilbert-space laws of large numbers and the estimator rate; (3) an operator-norm Hessian approximation and an exact first-order expansion; (4) the conditional score covariance and Lindeberg condition for each design; (5) projection-tail control; and (6) combination with the full-data score fluctuation. All paper-specific steps are derived below rather than assumed from named lemmas.

The standard independent probability facts used are the scalar iid LLN for integrable variables, the scalar iid finite-variance CLT, and the following Hilbert-space convergence criterion: for a separable Hilbert space and finite-rank orthogonal projections P_J increasing strongly to the identity, finite-dimensional convergence of P_J U_n to P_J U for every J, together with lim_{J to infinity}limsup_n P(||(I-P_J)U_n||>epsilon)=0 for every epsilon>0, implies U_n converges weakly to U. The criterion follows by approximating bounded Lipschitz test functions by their compositions with P_J. A positive self-adjoint trace-class operator defines a centered Hilbert-valued Gaussian, including a degenerate one, by its eigenbasis Gaussian series. These are the standard independent facts indexed by theory_029.

## 1. Analytic and Measurability Foundations

The input space is separable. Continuity of K gives continuity of the feature map because
\[
\|K_x-K_{x'}\|^2=K(x,x)+K(x',x')-2K(x,x').
\]
A countable dense set of inputs therefore generates a dense countable feature span, so H is separable. The reproducing property gives |h(x)|<=kappa||h||. These arguments also give Borel measurability of the feature map.

For a fixed bounded norm ball, choose B larger than all prediction magnitudes on that ball. For k=0,1,2,
\[
|\ell^{(k)}(h(X),Y)|\le |\ell^{(k)}(0,Y)|+B\phi_B(Y).
\]
The right side has finite fourth moment. Taylor's formula with these envelopes justifies Frechet differentiation under expectation and gives
\[
\nabla L(h_0)=G=E g(Z),\qquad
H_0:=\operatorname{Hess}R(h_0)
=E F(Z)+\lambda_0 I,
\]
where
\[
g(Z)=\ell'(h_0(X),Y)K_X,\qquad
F(Z)=\ell''(h_0(X),Y)K_X\otimes K_X.
\]
In particular, E||g||^4<infinity and E||F||_{HS}^4<infinity, since ||F||_{HS}<=kappa^2|ell''(h_0(X),Y)|. The same envelopes show that L is finite and continuous on H.

The loss is nonnegative and convex. Thus R, and every realized weighted objective R^*, are continuous, coercive, and strongly convex, with moduli lambda_0 and lambda^*, respectively. A bounded minimizing sequence has a weakly convergent subsequence, and convex continuous functions are weakly lower semicontinuous. This proves existence and uniqueness of their minimizers. It also proves H_0>=lambda_0 I; hence H_0 is boundedly invertible. No additional local-convexity assumption is needed.

For completeness, the sample minimizer is measurable. Enumerate a countable dense subset of H. For each positive integer m select its first element whose objective value is within 1/m of the infimum over that subset. These selections are measurable, and strong convexity bounds their distance from the unique minimizer by sqrt(2/(m lambda^*)). Their pointwise limit is the minimizer. An empty Poisson sample causes no difficulty: the objective is then the positive quadratic penalty and its minimizer is zero.

## 2. Weighted LLN, Consistency, and Rate

Let D_n=sigma(Z_1,...,Z_n), abbreviate s=s_n, and define
\[
w_i=(n\pi_{n,i})^{-1},\qquad a_n=\max_i w_i,
\qquad P_n f=\frac1n\sum_i f(Z_i),
\qquad P^*f=\frac1n\sum_i f(Z_i)\frac{\gamma_{n,i}}{s\pi_{n,i}}.
\]
The probability assumption gives E a_n^2=O(1), and consequently a_n=O_P(1). For a strongly measurable integrand f in a separable Hilbert space with E||f||^4<infinity, conditional unbiasedness gives E[P^*f|D_n]=P_nf.

Put Q_n(f)=n^{-2}sum_i ||f(Z_i)||^2/pi_{n,i}. Exact conditional second moments give
\[
E[\|P^*f-P_nf\|^2\mid D_n]
=\frac1s\{Q_n(f)-\|P_nf\|^2\}
\]
for multinomial sampling, and
\[
E[\|P^*f-P_nf\|^2\mid D_n]
=\frac1sQ_n(f)-\frac1{n^2}\sum_i\|f(Z_i)\|^2
\]
for Poisson sampling. In particular, both are bounded by a_n P_n||f||^2/s. These identities, rather than entrywise covariance inequalities multiplied by signed inner products, justify the bound.

Cauchy-Schwarz and Jensen imply
\[
E[a_nP_n\|f\|^2]
\le (Ea_n^2)^{1/2}\{E(P_n\|f\|^2)^2\}^{1/2}
\le (Ea_n^2)^{1/2}(E\|f\|^4)^{1/2}=O(1).
\]
Conditional centering makes P^*f-P_nf orthogonal in L2 to the data-measurable error P_nf-Ef. Independence of the original observations therefore yields
\[
E\|P^*f-Ef\|^2=O(s^{-1}+n^{-1}).
\]
This proves the weighted LLN, and gives P^*f-Ef=O_P(s^{-1/2}) whenever s=O(n), as holds in both normality regimes.

Let d_n=h^*_{s_n}-h_0. Strong monotonicity of the realized gradient, together with its zero at h^*_{s_n}, gives
\[
\lambda^*_{s_n}\|d_n\|
\le\|\nabla R^*_{s_n}(h_0)\|
\le\|P^*g-G\|+|\lambda^*_{s_n}-\lambda_0|\,\|h_0\|.
\]
Here G+lambda_0 h_0=0 by population stationarity. Since lambda^* tends in probability to lambda_0>0, the LLN proves consistency. The same inequality and the regularization rate give
\[
\sqrt{s_n}\|d_n\|=O_P(1).
\]
Only boundedness in probability, not convergence of this scaled norm to zero, is needed.

## 3. Norm-Valued Hessian Linearization

Apply the weighted LLN to F in the separable Hilbert space of Hilbert-Schmidt operators. Since operator norm is bounded by Hilbert-Schmidt norm,
\[
\|P^*F-EF\|_{op}=o_P(1).
\]
The regularization multiple of I is handled separately; I need not be Hilbert-Schmidt.

Choose B>kappa(||h_0||+1). On the event ||d_n||<=1, local Lipschitz continuity of ell'' gives
\[
\sup_{0\le t\le1}
\|\operatorname{Hess}R^*_{s_n}(h_0+td_n)
-\operatorname{Hess}R^*_{s_n}(h_0)\|_{op}
\le\kappa^3\|d_n\|P^*\phi_B.
\]
The scalar weighted LLN gives P^*phi_B=O_P(1). Consistency makes the displayed bound o_P(1), and the complementary event has probability tending to zero. Thus, for
\[
\overline H_n=\int_0^1\operatorname{Hess}R^*_{s_n}(h_0+td_n)\,dt,
\]
we have ||overline H_n-H_0||_{op}=o_P(1). Multiplication by the established rate gives
\[
\sqrt{s_n}\|(\overline H_n-H_0)d_n\|=o_P(1).
\]
The fundamental theorem of calculus gives the exact equation
\[
0=\nabla R^*_{s_n}(h_0)+\overline H_n d_n.
\]
There is no additional unspecified remainder when the integrated Hessian is used. Consequently,
\[
\sqrt{s_n}H_0d_n
=-W_n-\sqrt{s_n/n}\,V_n
-\sqrt{s_n}(\lambda^*_{s_n}-\lambda_0)h_0+o_P(1),
\]
where
\[
W_n=\sqrt{s_n}(P^*g-P_ng),\qquad
V_n=\sqrt n(P_ng-G).
\]
The regularization term tends to zero in probability, regardless of dependence between the regularizer, data, and sampling randomness.

## 4. Conditional Score Limits

Write g_i=g(Z_i), bar g_n=P_ng, m=E psi(Z), and
\[
Q_n=\frac1n\sum_i w_i g_i\otimes g_i,
\qquad A=mE\left[\frac{g\otimes g}{\psi}\right],
\qquad B_0=E[g\otimes g].
\]
The assumptions give 0<m<infinity and E[||g||^2/psi]<infinity. Thus A and B_0 are positive trace-class operators. For every fixed f in H, the ordinary scalar LLNs give
\[
\langle Q_nf,f\rangle
=(P_n\psi)P_n\left[\frac{\langle g,f\rangle^2}{\psi}\right]
\longrightarrow\langle Af,f\rangle
\]
in probability. Also bar g_n tends to G and P_n<g,f>^2 tends to E<g,f>^2.

### Multinomial design

Conditional on D_n, let I_1,...,I_s be the independent draws and set
\[
U_{n,j}=\frac{w_{I_j}g_{I_j}-\bar g_n}{\sqrt s},\qquad
W_n=\sum_{j=1}^s U_{n,j}.
\]
These increments are conditionally independent and centered, and they are martingale differences for the filtration obtained by successively revealing the indices after D_n. Their conditional covariance sum is
\[
C_n^M=Q_n-\bar g_n\otimes\bar g_n,
\]
whose quadratic forms tend to those of C^M=A-G tensor G=Sigma_M^*(psi).

The elementary inequality ||u-v||^4<=8(||u||^4+||v||^4) gives
\[
\sum_{j=1}^s E[\|U_{n,j}\|^4\mid D_n]
\le\frac8s\left(a_n^3P_n\|g\|^4+\|\bar g_n\|^4\right)=o_P(1).
\]
Indeed, P_n||g||^4=O_P(1), a_n=O_P(1), and bar g_n=O_P(1).

### Poisson design

Let p_i=s pi_{n,i} in (0,1] and set
\[
U_{n,i}=\frac{w_i g_i(\gamma_{n,i}-p_i)}{\sqrt s},\qquad
W_n=\sum_{i=1}^n U_{n,i}.
\]
These increments are conditionally independent and centered and are martingale differences for the corresponding successively revealed indicator filtration. Their conditional covariance sum is
\[
C_n^P=Q_n-\frac{s}{n}P_n(g\otimes g).
\]
Its quadratic forms tend to those of C^P=A-cB_0=Sigma_{P,c}^*(psi).

For a Bernoulli variable of mean p, |gamma-p|<=1 and E(gamma-p)^2=p(1-p)<=p, so E(gamma-p)^4<=p. Hence
\[
\sum_{i=1}^n E[\|U_{n,i}\|^4\mid D_n]
\le\frac1s\frac1n\sum_i w_i^3\|g_i\|^4
\le\frac{a_n^3}{s}P_n\|g\|^4=o_P(1).
\]
This includes p_i=1.

### Derivation of the conditional characteristic-function conclusion

For either array and any fixed f, put eta_{n,j}=<U_{n,j},f>. The conditional Lindeberg sum is bounded by epsilon^{-2}sum_j E[eta_{n,j}^4|D_n], and therefore tends to zero in probability. We can derive the needed characteristic-function limit directly, without leaving the specialized conditional CLT as an unproved dependency.

Let v_{n,j}=E[eta_{n,j}^2|D_n] and V_n(f)=sum_j v_{n,j}. We have V_n(f) tending in probability to v=<C f,f>, for C=C^M or C^P. The fourth-moment bound gives
\[
\max_j v_{n,j}\le\left(\sum_jE[\eta_{n,j}^4\mid D_n]\right)^{1/2}=o_P(1),
\]
and, by conditional Cauchy-Schwarz followed by Cauchy-Schwarz over j,
\[
\sum_jE[|\eta_{n,j}|^3\mid D_n]
\le\left(V_n(f)\sum_jE[\eta_{n,j}^4\mid D_n]\right)^{1/2}=o_P(1).
\]
For any real t, Taylor's formula gives
\[
E[e^{it\eta_{n,j}}\mid D_n]=1-\tfrac12t^2v_{n,j}+r_{n,j},
\qquad
\sum_j|r_{n,j}|\le\tfrac16|t|^3\sum_jE[|\eta_{n,j}|^3\mid D_n]=o_P(1).
\]
Writing the terms after 1 as z_{n,j}, their maximum magnitude tends to zero, their absolute sum is O_P(1), and their sum tends to -t^2v/2. On the event max_j|z_{n,j}|<=1/2,
\[
\left|\sum_j\log(1+z_{n,j})-\sum_j z_{n,j}\right|
\le C\max_j|z_{n,j}|\sum_j|z_{n,j}|=o_P(1).
\]
That event has probability tending to one. Conditional independence now yields
\[
E[e^{it\langle W_n,f\rangle}\mid D_n]
=\prod_jE[e^{it\eta_{n,j}}\mid D_n]
\longrightarrow e^{-t^2\langle Cf,f\rangle/2}
\]
in probability. The derivation also covers v=0. Applying it to arbitrary linear combinations of finitely many test vectors gives all finite-dimensional conditional characteristic-function limits.

Both C^M and C^P are self-adjoint trace-class operators. Their quadratic forms are nonnegative because they are limits in probability of the nonnegative conditional variance quadratic forms. They therefore define genuine centered H-valued Gaussian laws, without a nondegeneracy assumption.

## 5. Projection Tails and the Full-Data CLT

Let P_J project onto the first J vectors of an orthonormal basis and write T_J=I-P_J. In a finite-dimensional space take P_J=I for large J; the zero space is immediate. The exact covariance calculation in Section 2, applied to T_Jg, gives for either design
\[
E\|T_JW_n\|^2
\le E[a_nP_n\|T_Jg\|^2]
\le (Ea_n^2)^{1/2}(E\|T_Jg\|^4)^{1/2}.
\]
The second factor tends to zero as J increases by dominated convergence, since ||T_Jg||^4<=||g||^4. Markov's inequality supplies the required uniform asymptotic probability-tail bound. Together with the conditional characteristic-function limits, whose bounded errors also converge to zero in L1, this proves the unconditional H-valued score limits.

For V_n=sqrt(n)(P_ng-G), every finite collection of projections satisfies the ordinary iid multivariate CLT by the scalar CLT and linear combinations. Its limiting covariance is
\[
\Sigma=B_0-G\otimes G.
\]
Independence and centering give
\[
E\|T_JV_n\|^2
=E\|T_J(g-G)\|^2\le E\|T_Jg\|^2\longrightarrow0.
\]
The Hilbert-space convergence criterion consequently gives V_n converging weakly to GP(0,Sigma).

## 6. Covariance Combination and Conclusion

Let b_n=sqrt(s_n/n), so b_n tends to sqrt(c). For any f and t, define
\[
D_n(t,f)=E[e^{it\langle W_n,f\rangle}\mid D_n]
-e^{-t^2\langle Cf,f\rangle/2}.
\]
This error tends to zero in probability and has magnitude at most 2. Thus E|D_n(t,f)| tends to zero; explicitly it is at most epsilon+2P(|D_n(t,f)|>epsilon).

Since V_n is data-measurable,
\[
\left|E e^{it\langle W_n+b_nV_n,f\rangle}
-e^{-t^2\langle Cf,f\rangle/2}E e^{itb_n\langle V_n,f\rangle}\right|
\le E|D_n(t,f)|\longrightarrow0.
\]
The full-data CLT and b_n tending to sqrt(c) identify the limit as
\[
\exp\{-t^2\langle(C+c\Sigma)f,f\rangle/2\}.
\]
This proves the finite-dimensional limits, including c=0. No finite-sample independence between W_n and V_n is asserted or needed. Their projection-tail bounds and boundedness of b_n give the corresponding tail bound for their sum. Hence
\[
W_n+b_nV_n\Rightarrow\mathcal{GP}(0,C+c\Sigma)
\]
in H.

Substitute this result into the norm-valued linearization in Section 3. The regularization term and the Hessian remainder are o_P(1); negating a centered Gaussian does not alter its covariance. For multinomial sampling C=Sigma_M^*(psi), and for Poisson sampling C=Sigma_{P,c}^*(psi). These are precisely the two asserted estimator limits. Consistency was already proved in Section 2.

## Audit Notes

The summation-index, rate, covariance-combination scale, and regularization-target repairs already recorded in the artifacts are retained. The proof additionally repairs the source's signed-coefficient covariance inference, supplies the Hilbert-Schmidt-to-operator-norm Hessian argument, corrects conditional-characteristic-function bookkeeping, and covers zero limiting variances. No specialized result is used solely on the authority of its name or citation, and no unresolved theorem-critical obligation remains.
