# Reference Proof

## Scope and obligation inventory

This proof concerns the public real Gaussian experiment. It derives the necessary one-point expectation and centered two-point covariance approximations rather than treating imported deterministic-equivalence statements as proved background. All public assumptions and targets are unchanged. The covariance approximation is controlled relative to the retained deterministic kernel, so the argument also covers positive variance scales smaller than 1/n.

## 1. Experiment and terminal map

Write S=\widehat\Sigma and y=\bar x. Then
\[
S=\frac1n\sum_{i=1}^n\Sigma^{1/2}z_i z_i^T\Sigma^{1/2},\qquad ES=\Sigma.
\]
Fixing the denoiser location at \mu does not condition on a sample-mean event.

At fixed dimension and x_T=\mu+Ty, the zero-noise trajectory is
\[
\mu+S^{1/2}(I+S/T^2)^{-1/2}y.
\]
Spectral calculus gives its limit X_\infty=\mu+S^{1/2}y as T\to\infty. Differentiation of the positive-noise eigenmode coefficients verifies the stated trajectory. No inverse of S is required at zero noise.

## 2. Self-consistency, positivity, and finite-dimensional integrability

Let s_j be the eigenvalues of \Sigma. For \lambda>0, the equation for k=\kappa(\lambda) is
\[
1=\lambda/k+\frac1n\sum_j\frac{s_j}{s_j+k}.
\]
Its right side is continuous and strictly decreasing for k>0, with limits infinity and zero. Thus the positive solution is unique. Moreover,
\[
\lambda\le k\le\lambda+\operatorname{Tr}(\Sigma)/n,
\qquad df_1(k)=n(1-\lambda/k)<n.
\]
Eigenvalue comparison and Cauchy–Schwarz give
\[
0\le df_2(k)\le df_1(k),\qquad
0\le df_2(k,k')\le\sqrt{df_2(k)df_2(k')}<n.
\]
Every displayed denominator is positive for positive integration arguments.

If \Sigma y=0 or \Sigma v=0, then S annihilates the corresponding vector almost surely. Thus v^TS^{1/2}y=0 and v^TX_\infty=v^T\mu is deterministic. The displayed variance integral is also zero. Otherwise both directional factors are positive for every positive u,w, so V_n>0. This includes all zero-vector and zero-covariance cases.

The mean integral is finite by k(u^2)\ge u^2 and the bound min(1,\|\Sigma\|/u^2). For the deterministic variance integral, fix a dimension and let r=rank(\Sigma). If r=0 it vanishes. Otherwise the positive eigenvalues have a positive minimum at that dimension. Near zero there are three cases:

- If r<n, k(u^2) is of order u^2 and n-df_2(k,k')\ge n-r.
- If r=n, expansion of the finite eigenvalue sum gives k(u^2) of order u and n-df_2(k,k') of order k+k'. Thus kk'/(n-df_2(k,k')) is locally bounded.
- If r>n, k(u^2) tends to the positive solution k_0 of df_1(k_0)=n, and df_2(k_0)<n.

The directional mixed-resolvent factors are bounded near zero at fixed dimension. At infinity k(u^2)=u^2+O(1), and the full variance integrand has inverse-square decay in each large variable. For example, when k' is sufficiently large, df_2(k,k')\le Tr(\Sigma)/k'<n/2 uniformly in k; this also controls regions where just one variable is large. These observations prove finite-dimensional integrability. They do not assert uniform estimates at the endpoints across dimensions.

The matrix K_n(u,w) is positive semidefinite. Cauchy–Schwarz in its quadratic form gives
\[
0\le J_n(u,w)\le H_n(u,w),
\]
so the alignment integral is finite as well.

## 3. Gaussian one-point expectation approximation

Fix a compact interval of positive ridge parameters. Constants in the estimates below may depend on this interval, a uniform bound C for \|\Sigma\|, and an upper bound for d/n, but not on a coordinate index or on positive population eigenvalue lower bounds.

Rotate to a population eigenbasis, so \Sigma=diag(s_1,\ldots,s_d). Gaussian invariance preserves the model. Write the whitened data as a d-by-n matrix G with independent rows g_j\sim N(0,I_n). For a ridge parameter \lambda>0 put
\[
B=\frac1n\sum_j s_jg_jg_j^T,\quad
B_j=B-\frac{s_j}{n}g_jg_j^T,\quad
R_j=(B_j+\lambda I_n)^{-1},
\]
\[
a_j=\frac1n g_j^TR_jg_j,\quad
m_j=\frac1n Tr R_j,\quad
m=\frac1n Tr(B+\lambda I_n)^{-1},\quad t=Em.
\]
For Q_\lambda=S(S+\lambda I_d)^{-1}, the rectangular resolvent identity and a rank-one inverse update give
\[
(Q_\lambda)_{jj}=\frac{s_ja_j}{1+s_ja_j}.
\]
Indeed, with U=diag(\sqrt{s_j})G/\sqrt n, one has S=UU^T, B=U^TU and Q_\lambda=U(B+\lambda I_n)^{-1}U^T. A sign change of row g_j conjugates Q_\lambda by the corresponding diagonal sign matrix while preserving its distribution. Thus EQ_\lambda is diagonal.

Conditional on B_j, Gaussian quadratic-form moments give
\[
E(a_j\mid B_j)=m_j,\qquad
E[(a_j-m_j)^2\mid B_j]=\frac2{n^2}Tr(R_j^2)\le\frac2{n\lambda^2}.
\]
The rank-one update and R_j^2\preceq\lambda^{-1}R_j also give
\[
0\le m_j-m
=\frac{s_j}{n^2}\frac{g_j^TR_j^2g_j}{1+s_ja_j}
\le\frac1{n\lambda}.
\]
Changing one row changes m by at most 1/(n\lambda). The conditional-expectation martingale obtained by revealing the independent rows therefore has increments bounded by 1/(n\lambda). Its orthogonal increments imply
\[
Var(m)\le\frac d{n^2\lambda^2}.
\]
Consequently, uniformly in j,
\[
E|a_j-t|\le\frac{\sqrt2}{\sqrt n\lambda}+\frac1{n\lambda}+\frac{\sqrt d}{n\lambda}=O(n^{-1/2}).
\]
The function f_s(a)=sa/(1+sa), a\ge0, has derivative at most s\le C. Hence
\[
E(Q_\lambda)_{jj}=f_{s_j}(t)+e_j,\qquad \max_j|e_j|=O(n^{-1/2}).
\]
The shared nonzero spectrum of S and B gives the exact identity
\[
1=\lambda m+\frac1n Tr Q_\lambda.
\]
Define F_\lambda(a)=\lambda a+n^{-1}\sum_j f_{s_j}(a). Taking expectations shows |F_\lambda(t)-1|=O(n^{-1/2}). The self-consistency equation says F_\lambda(1/\kappa(\lambda))=1, while F_\lambda'(a)\ge\lambda. Thus
\[
\left|t-\frac1{\kappa(\lambda)}\right|=O(n^{-1/2}),
\]
and
\[
\left\|E Q_\lambda-\Sigma(\Sigma+\kappa(\lambda)I)^{-1}\right\|_{op}=O(n^{-1/2}).
\]
All estimates are uniform when \lambda stays in a fixed compact positive interval. This concerns the expected matrix, not operator-norm concentration of Q_\lambda.

## 4. Positive square roots, expectation, and shrinkage

For s>0, direct scalar integration gives
\[
\frac2\pi\int_0^\infty\frac{s}{s+u^2}\,du=\sqrt s.
\]
At s=0 the integrand is identically zero on u>0. Thus for every positive semidefinite S,
\[
S^{1/2}=\frac2\pi\int_0^\infty S(S+u^2I)^{-1}\,du.
\]
No inverse square root on a nullspace is used.

Put Q_u=Q_{u^2} and T_u=\Sigma(\Sigma+\kappa(u^2)I)^{-1}. Since 0\preceq Q_u\preceq I and Q_u\preceq S/u^2,
\[
0\preceq EQ_u\preceq I,\qquad EQ_u\preceq\Sigma/u^2.
\]
For bounded deterministic a_n,y_n, the expected empirical and population bilinear integrands have the integrable bound
\[
\|a_n\|\|y_n\|\min(1,C/u^2).
\]
The same bound holds for E|a_n^TQ_u y_n|: apply Cauchy–Schwarz first in the positive semidefinite quadratic form Q_u and then in expectation. Thus expectation and the finite-dimensional integral can be interchanged. Section 3 and dominated convergence prove the public expectation equivalent.

The self-consistency equation gives \kappa(\lambda)\ge\lambda, strictly if \Sigma\ne0. Therefore
\[
b_n(s)=\frac2\pi\int_0^\infty\frac{s}{s+\kappa(u^2)}\,du
\]
satisfies 0\le b_n(s)\le\sqrt s. At s=0 both coefficients vanish. For s>0 the comparison is strict at each finite dimension. This is a comparison of deterministic coefficients, not a pathwise ordering or a uniform positive limiting gap.

## 5. Exact covariance integral

Let Y_u=v^TQ_u y and C_n(u,w)=Cov(Y_u,Y_w). At each finite dimension,
\[
Var(v^TS^{1/2}y)=\frac4{\pi^2}\int_0^\infty\int_0^\infty C_n(u,w)\,du\,dw.
\]
To justify this identity, first truncate the square-root integrals. The bound
\[
\int_0^\infty |Y_u|\,du
\le\frac\pi2\|v\|\|y\|\sqrt{\|S\|}
\]
has a square with finite expectation because E\|S\|\le E Tr(S)<\infty. Hence the truncated integrals converge in L^2 and the absolute covariance is integrable on the product domain. Passing to the limit proves the identity.

## 6. Auxiliary Gaussian estimates for the centered covariance

All estimates in Sections 6–8 are uniform for ridge parameters \lambda,\nu in a fixed interval [a,b] with a>0. Enlarging this interval by a fixed amount does not change the argument. Coordinate deletions always involve at most two rows.

### 6.1 A sharper normalized-trace variance

The normalized dual trace m from Section 3 satisfies Var(m)=O(n^{-2}). To prove this, condition on all rows except g_j. Write
\[
b_j=\frac1n g_j^TR_j^2g_j,\qquad b_{0j}=\frac1n Tr R_j^2.
\]
The rank-one formula reads
\[
m=m_j-\frac{s_j}{n}\frac{b_j}{1+s_ja_j}.
\]
Conditional on the other rows, Var(a_j)=O(1/n), Var(b_j)=O(1/n), and b_{0j}\le a^{-2}. Moreover,
\[
\left|\frac{b_j}{1+s_ja_j}-\frac{b_{0j}}{1+s_jm_j}\right|
\le |b_j-b_{0j}|+s_jb_{0j}|a_j-m_j|.
\]
It follows that
\[
E\bigl[Var(m\mid \{g_\ell:\ell\ne j\})\bigr]\le K s_j^2/n^3.
\]
For completeness, the variance inequality for independent coordinates is
\[
Var(F)\le\sum_j E\bigl[Var(F\mid \{g_\ell:\ell\ne j\})\bigr].
\]
It follows directly from the Doob martingale: if E_j averages only coordinate j, its j-th increment is the conditional expectation of F-E_jF given the first j coordinates. Conditional Jensen bounds its squared expectation by E(F-E_jF)^2; orthogonality of increments then gives the inequality. Applying it to m and using \sum_j s_j^2=O(n) proves Var(m)=O(n^{-2}). The same proof applies to traces with one or two rows deleted.

### 6.2 Fourth moments and coordinate-deleted traces

If R is symmetric, independent of standard Gaussian g,h, and \|R\|\le a^{-1}, expansion in an eigenbasis gives
\[
E\left(\frac{g^TRg-Tr R}{n}\right)^4
=\frac{12(Tr R^2)^2+48Tr R^4}{n^4}=O(n^{-2}),
\]
\[
E\left(\frac{g^TRh}{n}\right)^4
=\frac{3(Tr R^2)^2+6Tr R^4}{n^4}=O(n^{-2}).
\]
These formulas follow by expanding sums of independent centered variables: E(g_\ell^2-1)^2=2, E(g_\ell^2-1)^4=60, E(g_\ell h_\ell)^2=1, and E(g_\ell h_\ell)^4=9.

Let t_\lambda=1/\kappa(\lambda). Normalized resolvent traces are bounded by 1/a. Combining their O(n^{-2}) variance with this bound gives fourth centered moments O(n^{-2}). Section 3 gives Em-t_\lambda=O(n^{-1/2}). Deleting at most two rows changes m by at most 2/(na). Therefore, for any such deleted trace m_0,
\[
\|m_0-t_\lambda\|_{L^4}=O(n^{-1/2}).
\]
If g is independent of the deleted matrix and A_\lambda=n^{-1}g^TR_0(\lambda)g, conditional use of the first fourth-moment formula yields
\[
\|A_\lambda-t_\lambda\|_{L^4}=O(n^{-1/2}).
\]
All these estimates are uniform in the deleted indices.

### 6.3 The two-argument dual trace

Define
\[
L_0(\lambda,\nu)=\frac1n Tr[R_0(\lambda)R_0(\nu)]
\]
for a dual covariance with at most two rows deleted. Then
\[
E L_0(\lambda,\nu)=\ell_n(\lambda,\nu)+O(n^{-1/4}),
\]
uniformly on [a,b]^2, where
\[
\ell_n(\lambda,\nu)=
\frac1{\kappa(\lambda)\kappa(\nu)\left(1-df_2(\kappa(\lambda),\kappa(\nu))/n\right)}.
\]
Here is the derivation, including coincident arguments. For the full dual covariance and \lambda\ne\nu, the resolvent identity gives
\[
\frac1n Tr[R(\lambda)R(\nu)]
=\frac{m(\lambda)-m(\nu)}{\nu-\lambda}.
\]
The finite-dimensional self-consistency equation gives
\[
\nu-\lambda=(\kappa(\nu)-\kappa(\lambda))
\left(1-\frac{df_2(\kappa(\lambda),\kappa(\nu))}{n}\right).
\]
Thus (t_\lambda-t_\nu)/(\nu-\lambda)=\ell_n(\lambda,\nu).

Section 3 controls E m-t uniformly by O(n^{-1/2}). For |\lambda-\nu|\ge h this proves a trace-product error O(n^{-1/2}/h). The empirical trace product is uniformly Lipschitz in its arguments because resolvent norms are at most 1/a. The deterministic divided difference is also uniformly Lipschitz: implicit differentiation of
\[
\lambda t_\lambda+\frac1n\sum_j\frac{s_jt_\lambda}{1+s_jt_\lambda}=1
\]
shows that t_\lambda' and t_\lambda'' are uniformly bounded on an enlarged compact positive interval. The coefficient of each highest derivative is at least \lambda\ge a, while all other terms are bounded using t_\lambda\le1/a, s_j\le C and d/n bounded. For |\lambda-\nu|<h, compare with a pair separated by h. Taking h=n^{-1/4} proves the claimed uniform error, including the diagonal.

Finally, deleting one row changes the normalized trace of a resolvent by at most 1/(na). Applying the rank-one update to each factor of the trace product, and bounding the other factor by 1/a, bounds the normalized trace-product change by 2/(na^2). This proves the same estimate for all the deleted versions used below.

## 7. Entrywise centered two-point estimates

Continue in the population eigenbasis. Put
\[
k=\kappa(\lambda),\quad k'=\kappa(\nu),\quad
p_j(\lambda)=1+s_j/k,\quad
q_j=\frac{s_j}{(s_j+k)(s_j+k')},\quad
P=\frac{kk'}{n-df_2(k,k')}.
\]
We prove, uniformly in the indices and in compact positive ridge rectangles,
\[
Cov((Q_\lambda)_{jj},(Q_\nu)_{jj})
=2Pq_j^2+O(s_j^2n^{-5/4}),                                      \tag{A}
\]
\[
E[(Q_\lambda)_{jk}(Q_\nu)_{jk}]
=Pq_jq_k+O(s_js_kn^{-5/4})\quad(j\ne k),                         \tag{B}
\]
\[
Cov((Q_\lambda)_{jj},(Q_\nu)_{kk})
=O(s_js_kn^{-3/2})\quad(j\ne k).                                \tag{C}
\]
Zero eigenvalues cause no difficulty: every expression involving the corresponding row or column vanishes, and the estimates retain that factor.

### 7.1 Same diagonal entry

Use the one-coordinate deletion from Section 3. Taylor expansion of f_{s_j} around t_\lambda gives
\[
(Q_\lambda)_{jj}
=f_{s_j}(t_\lambda)+\frac{s_j}{p_j(\lambda)^2}(a_j(\lambda)-t_\lambda)+\rho_j(\lambda),
\]
where |\rho_j(\lambda)|\le s_j^2|a_j(\lambda)-t_\lambda|^2. Section 6 therefore gives
\[
\|\rho_j(\lambda)\|_2=O(s_j^2/n),
\qquad \|a_j(\lambda)-t_\lambda\|_2=O(n^{-1/2}).
\]
The covariance terms involving a remainder are O(s_j^2 n^{-3/2}), using s_j\le C.

Conditional Gaussian covariance and the law of total covariance give
\[
Cov(a_j(\lambda),a_j(\nu))
=\frac2{n^2}E Tr[R_j(\lambda)R_j(\nu)]
+Cov(m_j(\lambda),m_j(\nu)).
\]
The second term is O(n^{-2}) by Section 6.1. Sections 6.3 and the Taylor expansion therefore give
\[
Cov((Q_\lambda)_{jj},(Q_\nu)_{jj})
=\frac{2s_j^2\ell_n(\lambda,\nu)}{n p_j(\lambda)^2p_j(\nu)^2}
+O(s_j^2n^{-5/4}).
\]
Substitution of \ell_n proves (A).

### 7.2 Matching off-diagonal entries

Delete coordinates j and k from the dual covariance and denote the remaining resolvent by R_0(\lambda). Set
\[
a_j(\lambda)=\frac1n g_j^TR_0(\lambda)g_j,\quad
 a_k(\lambda)=\frac1n g_k^TR_0(\lambda)g_k,\quad
 b(\lambda)=\frac1n g_j^TR_0(\lambda)g_k.
\]
The two-coordinate inverse formula gives
\[
(Q_\lambda)_{jk}=\frac{\sqrt{s_js_k}\,b(\lambda)}{D_\lambda},
\]
\[
D_\lambda=(1+s_ja_j(\lambda))(1+s_ka_k(\lambda))-s_js_k b(\lambda)^2.
\]
Since b(\lambda)^2\le a_j(\lambda)a_k(\lambda), one has D_\lambda\ge1. Sections 6.2 and elementary product estimates give
\[
\|D_\lambda-p_j(\lambda)p_k(\lambda)\|_2=O(n^{-1/2}),
\]
\[
\left\|D_\lambda^{-1}-[p_j(\lambda)p_k(\lambda)]^{-1}\right\|_2=O(n^{-1/2}).
\]
For the first estimate, expand the difference into linear deviations of a_j,a_k, the product a_ja_k-t_\lambda^2, and b^2; their L^2 bounds follow from the L^4 estimates. The second follows because both denominators are at least one.

Also \|b(\lambda)b(\nu)\|_2=O(1/n). Replacing the reciprocal denominators by their deterministic values in the expectation of the off-diagonal product therefore has error O(s_js_kn^{-3/2}). Conditional on the deleted covariance, g_j and g_k are independent, so
\[
E[b(\lambda)b(\nu)\mid R_0]
=\frac1{n^2}Tr[R_0(\lambda)R_0(\nu)].
\]
Section 6.3 now gives
\[
E[(Q_\lambda)_{jk}(Q_\nu)_{jk}]
=\frac{s_js_k\ell_n(\lambda,\nu)}{n p_j(\lambda)p_k(\lambda)p_j(\nu)p_k(\nu)}
+O(s_js_kn^{-5/4}),
\]
which is (B).

### 7.3 Distinct diagonal entries

With the same two-coordinate deletion, the diagonal formula is
\[
(Q_\lambda)_{jj}
=f_{s_j}(a_j(\lambda))
-\frac{s_js_k b(\lambda)^2}{(1+s_ja_j(\lambda))D_\lambda}.
\]
The second term has L^2 norm O(s_js_k/n). The analogous formula holds for coordinate k and argument \nu.

Conditional on the deleted covariance, f_{s_j}(a_j(\lambda)) and f_{s_k}(a_k(\nu)) are independent. Let h_j denote the conditional expectation of the former and let m_0(\lambda)=n^{-1}Tr R_0(\lambda). Taylor expansion at this conditional mean gives
\[
|h_j-f_{s_j}(m_0(\lambda))|\le K s_j^2/n.
\]
Because f_{s_j} is s_j-Lipschitz and Var(m_0)=O(n^{-2}), this implies Var(h_j)=O(s_j^2/n^2). The law of total covariance therefore bounds the covariance of the two leading f terms by O(s_js_k/n^2).

Each leading f term has standard deviation O(s_j/\sqrt n) or O(s_k/\sqrt n), by its Lipschitz bound and Section 6.2. Combining this with the L^2 bounds on the correction terms shows that the remaining cross-covariances are O(s_js_kn^{-3/2}); the product of corrections is smaller. This proves (C).

## 8. Centered bilinear covariance and alignment

Let A=v^T\Sigma v and B_y=y^T\Sigma y. In the population eigenbasis set c_j=v_jy_j and d_{jk}=v_jy_k+v_ky_j for j<k. Coordinate sign symmetry implies that a diagonal entry is uncorrelated with any off-diagonal entry, and that products of two distinct unordered off-diagonal pairs have expectation zero. Thus the exact centered covariance decomposes as
\[
Cov(v^TQ_\lambda y,v^TQ_\nu y)
=\sum_j c_j^2 Cov((Q_\lambda)_{jj},(Q_\nu)_{jj})
+\sum_{j\ne k}c_jc_k Cov((Q_\lambda)_{jj},(Q_\nu)_{kk})
+\sum_{j<k}d_{jk}^2E[(Q_\lambda)_{jk}(Q_\nu)_{jk}].
\]
Insert (A)–(C). Their leading terms sum to
\[
P\left[\left(\sum_jv_j^2q_j\right)\left(\sum_jy_j^2q_j\right)
+\left(\sum_jv_jy_jq_j\right)^2\right].
\]
Indeed, the off-diagonal sum has these two products minus 2\sum_jc_j^2q_j^2, and the same-coordinate diagonal contribution restores that last term.

The errors can be summed without a factor of d. Weighted Cauchy–Schwarz gives
\[
\sum_j c_j^2s_j^2\le A B_y,\qquad
\left(\sum_j|c_j|s_j\right)^2\le A B_y,
\qquad
\sum_{j<k}d_{jk}^2s_js_k\le2A B_y.
\]
It follows that
\[
Cov(v^TQ_\lambda y,v^TQ_\nu y)
=P[(v^TKv)(y^TKy)+(v^TKy)^2]+\mathcal R_n(\lambda,\nu),
\]
\[
|\mathcal R_n(\lambda,\nu)|\le K_{a,b}n^{-5/4}A B_y,
\qquad K=\Sigma(\Sigma+kI)^{-1}(\Sigma+k'I)^{-1}.
\]
This is a centered expansion, not subtraction of uncontrolled uncentered equivalents.

For u,w in a fixed compact positive noise rectangle, take \lambda=u^2 and \nu=w^2. The leading terms are exactly H_n(u,w) and J_n(u,w). Moreover, on that rectangle k,k' have uniform positive lower and finite upper bounds. Since n-df_2(k,k')\le n and
\[
K\succeq \frac{\Sigma}{(C+\sup k)^2},
\]
there is a positive constant c for the rectangle such that
\[
H_n(u,w)\ge \frac c n A B_y.
\]
Consequently
\[
C_n(u,w)=H_n(u,w)+J_n(u,w)+R_n(u,w),
\qquad |R_n(u,w)|\le K n^{-1/4}H_n(u,w)
\]
uniformly on that rectangle. This inequality also holds trivially when A B_y=0. In particular, it retains the correct scale even when the vectors have vanishing population quadratic forms.

The actual leading real-Gaussian alignment contribution has therefore been identified as J_n. Dataset independence alone was not used to discard it.

## 9. Integration and the variance conclusion

Work along indices with V_n>0. For a fixed compact positive rectangle E, Section 8 gives
\[
\int_E\frac{|C_n-H_n|}{V_n}
\le K_E n^{-1/4}\int_E\frac{H_n}{V_n}
+\int_E\frac{J_n}{V_n}.
\]
By definition, the full integral of H_n/V_n is \pi^2/4. The full integral of J_n/V_n tends to zero by the public alignment assumption. Hence the left side tends to zero for each E.

Take E=[R^{-1},R]^2. On its complement,
\[
\int_{E^c}\frac{|C_n-H_n|}{V_n}
\le\int_{E^c}\frac{|C_n|+H_n}{V_n}.
\]
The public tightness assumptions make the right side uniformly small as R\to\infty. Combining local convergence with this tail bound yields
\[
\int_0^\infty\int_0^\infty\frac{|C_n-H_n|}{V_n}\,du\,dw\longrightarrow0.
\]
The stronger local estimate obtained here means that the amplitude part of the public uniform-integrability assumption is not additionally needed in this final step; no assumption has been removed from or added to the task.

Using Section 5 and the definition of V_n,
\[
\left|\frac{Var(v^TX_\infty)}{V_n}-1\right|
\le\frac4{\pi^2}\int_0^\infty\int_0^\infty\frac{|C_n-H_n|}{V_n}\,du\,dw\longrightarrow0.
\]
Indices with V_n=0 were settled exactly in Section 2. This proves the variance equivalent, and Sections 3–4 prove the expectation and shrinkage claims.

## Closure

All theorem-critical obligations for the public Gaussian task are closed: the terminal-map limit; self-consistency and denominator positivity; singular and zero cases; finite-dimensional improper integrability; the anisotropic expectation approximation; the mean integral and modewise comparison; the exact covariance integral; the centered mixed-argument covariance expansion with weighted errors; identification of its alignment contribution; and the final integrated relative-variance limit. No nonstandard citation is used as a substitute for a derivation.
