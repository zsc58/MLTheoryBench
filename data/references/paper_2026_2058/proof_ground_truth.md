# Reference Proof

## Contract and obligations

All expectations below are over the fresh honest oracle draws and any measurable Byzantine randomization. Conditioning is on the history before the indicated round. The proof must establish: honest-gradient and momentum dispersion control; all-input robustness control; momentum-bias and objective recursions; valid stochastic initialization; coefficient bounds and telescoping for the exact nonconvex constants; the exact PL last-iterate constants, including small horizons and constant objectives; and a uniform lower-bound construction covering both algorithms, every specified schedule, and zero parameters. Each obligation is derived below. No specialized external convergence theorem is invoked.

## 1. Oracle and momentum recursions

Write \(f=f_H\), \(\bar g^t=h^{-1}\sum_{i\in H}g_i^t\), \(\bar m^t=h^{-1}\sum_{i\in H}m_i^t\), and
\[
\eta^t=\bar g^t-\nabla f(x^{t-1}),\quad
\delta^t=\bar m^t-\nabla f(x^{t-1}),\quad
\zeta^t=A(m_1^t,\ldots,m_n^t)-\bar m^t,
\]
\[
\Gamma^t=h^{-1}\sum_{i\in H}\|m_i^t-\bar m^t\|^2.
\]
Conditional unbiasedness and independence imply
\[
\mathbb E_t\eta^t=0,\qquad \mathbb E_t\|\eta^t\|^2\le\sigma^2/h.
\]
The honest sample mean minimizes the sum of squared distances. Expanding around \(\nabla f(x^{t-1})\), and eliminating the noise cross terms, therefore gives
\[
h^{-1}\sum_{i\in H}\mathbb E_t\|g_i^t-\bar g^t\|^2
\le \sigma^2+G^2+B^2\|\nabla f(x^{t-1})\|^2.
\]
Expand the centered momentum recursion and use \(2\langle u,v\rangle\le\|u\|^2+\|v\|^2\). After averaging and conditioning, the two coefficients of local-gradient dispersion sum to \((1-\beta_t)^2+\beta_t(1-\beta_t)=1-\beta_t\). Thus, including \(t=1\),
\[
\mathbb E\Gamma^t\le\beta_t\mathbb E\Gamma^{t-1}
 +(1-\beta_t)(G^2+B^2\mathbb E\|\nabla f(x^{t-1})\|^2)
 +(1-\beta_t)^2\sigma^2. \tag{1}
\]
All-input robustness immediately gives
\[
\|\zeta^t\|^2\le\kappa\Gamma^t. \tag{2}
\]

Put \(a_t=\gamma_tL\). The exact bias identity is
\[
\delta^{t+1}=\beta_{t+1}\bigl(\delta^t+\nabla f(x^{t-1})-\nabla f(x^t)\bigr)
 +(1-\beta_{t+1})\eta^{t+1}.
\]
Conditioning before round \(t+1\) removes its noise cross term. Smoothness bounds the gradient difference by \(a_t\|g^t\|\). Young's inequality then bounds the non-noise part by
\[
(1+a_t)\beta_{t+1}^2\|\delta^t\|^2
 +a_t(1+a_t)\beta_{t+1}^2\|g^t\|^2.
\]
Since
\[
\|g^t\|^2\le2\|\zeta^t\|^2+4\|\nabla f(x^{t-1})\|^2+4\|\delta^t\|^2,
\]
we obtain, with \(\nu_t=\mathbb E\|\eta^t\|^2\le\sigma^2/h\),
\[
\begin{aligned}
\mathbb E\|\delta^{t+1}\|^2\le{}&
 (1+a_t)(1+4a_t)\beta_{t+1}^2\mathbb E\|\delta^t\|^2\\
&+4a_t(1+a_t)\beta_{t+1}^2\mathbb E\|\nabla f(x^{t-1})\|^2\\
&+2a_t(1+a_t)\beta_{t+1}^2\mathbb E\|\zeta^t\|^2
 +(1-\beta_{t+1})^2\nu_{t+1}. \tag{3}
\end{aligned}
\]
Keep the final variance term exact rather than replacing it immediately by its upper bound.

Smoothness of the objective and \(g^t=\nabla f(x^{t-1})+\delta^t+\zeta^t\) give
\[
\begin{aligned}
2\mathbb E[f(x^t)-f(x^{t-1})]\le{}&
 -\gamma_t(1-4a_t)\mathbb E\|\nabla f(x^{t-1})\|^2\\
&+2\gamma_t(1+2a_t)\mathbb E\|\delta^t\|^2
 +2\gamma_t(1+a_t)\mathbb E\|\zeta^t\|^2. \tag{4}
\end{aligned}
\]
Indeed, each of the two gradient-error cross terms is bounded using \(2|\langle u,v\rangle|\le2\|u\|^2+\|v\|^2/2\), and the squared update is bounded by the preceding inequality.

The required expectations are finite. Starting from deterministic finite initialization, smoothness bounds the global gradient by an affine function of \(\|x\|\), dissimilarity bounds each honest local gradient's second moment in terms of the global gradient, the oracle supplies finite noise second moments, and robustness bounds the aggregate by honest moments. Induction gives finite second moments of iterates, honest momenta, and aggregates. No moment bound on individual Byzantine messages is needed beyond their being finite vectors.

## 2. Correct stochastic initialization and coefficient collection

Let \(c_1=1/(8L)\), \(c_2=\kappa/(2L)\), and define
\[
D_t=\mathbb E\left\|\beta_t\bigl(\bar m^{t-1}-\nabla f(x^{t-1})\bigr)\right\|^2,
\qquad
W^t=2\mathbb E[f(x^{t-1})-f^*]+c_1D_t+c_2\mathbb E\Gamma^{t-1}.
\]
Conditional orthogonality gives
\[
\mathbb E\|\delta^t\|^2=D_t+(1-\beta_t)^2\nu_t.
\]
Consequently \(W^t\) is the source's potential \(V^t\) minus \(c_1(1-\beta_t)^2\nu_t\), and \(W^t\ge0\). This subtraction corrects the source's omitted first-round noise; it does not change the algorithm or oracle.

Assume \(0<a_t\le1/36\), \(\gamma_{t+1}\in[2\gamma_t/3,\gamma_t]\), and \(\beta_t=1-36a_t\). Set \(p=\beta_{t+1}^2\), \(a=a_t\), and \(q=\kappa B^2\). Combining (1)--(4), the coefficient multiplying the dispersion recursion is at most
\[
K=1+\frac92a(1+a)\le\frac76.
\]
This formula may be multiplied by \(c_2\) directly, so no division by \(\kappa\) is needed when \(\kappa=0\).

After substituting the dispersion recursion, upper bounds for the normalized gradient, bias, and previous-dispersion coefficients are
\[
A_1=-1+4a+\tfrac12(1+a)p+21q,
\]
\[
A_2=16a(1+2a)+(1+a)(1+4a)p,
\qquad A_3=[1+\tfrac92a(1+a)]\beta_t.
\]
The ratio condition implies \(0\le\beta_{t+1}\le1-24a\). Therefore
\[
A_1\le-\tfrac12+21q+a(-\tfrac{39}{2}+264a+288a^2)
\le-\tfrac12+21q,
\]
because the expression in parentheses is negative for \(0\le a\le1/36\). Also, using \(p\le\beta_{t+1}\le1-24a\),
\[
A_2\le1-3a-84a^2-96a^3\le1-a,
\qquad A_3\le1-a.
\]
These coefficients are nonnegative before their upper bounds are applied.

In the recursion for \(W^{t+1}\), the exact final term of (3) cancels. Replacing the current \(\mathbb E\|\delta^t\|^2\) by \(D_t+(1-\beta_t)^2\nu_t\), its noise contribution is at most
\[
A_2c_1(1-\beta_t)^2\nu_t\le162\gamma_t^2L\sigma^2/h.
\]
The dispersion noise is at most \(756\kappa\gamma_t^2L\sigma^2\), and its heterogeneity term is at most \(21\kappa\gamma_tG^2\). We have thus derived
\[
\begin{aligned}
W^{t+1}\le{}&2\mathbb E[f(x^{t-1})-f^*]
 -(\tfrac12-21q)\gamma_t\mathbb E\|\nabla f(x^{t-1})\|^2\\
&+(1-\gamma_tL)(c_1D_t+c_2\mathbb E\Gamma^{t-1})
 +\alpha_5\gamma_t^2+\alpha_6\gamma_t, \tag{5}
\end{aligned}
\]
where \(\alpha_5=(162L/h+756\kappa L)\sigma^2\) and \(\alpha_6=21\kappa G^2\).

Initialization gives \(\Gamma^0=0\) and
\[
W^1=2\Delta_0+\frac{\beta_1^2}{8L}\|\nabla f(x^0)\|^2\le\frac94\Delta_0. \tag{6}
\]
Here \(\|\nabla f(x)\|^2\le2L(f(x)-f^*)\) follows by applying smoothness at \(x-\nabla f(x)/L\) and using the definition of the infimum. In contrast, the original \(V^1\) has the additional term \((1-\beta_1)^2\nu_1/(8L)\); it cannot simply be omitted.

## 3. Exact nonconvex bound

Let \(C=3/8-21q>0\). Weaken \(1/2-21q\) in (5) to \(C\), discard the nonpositive error-component changes, and take constant \(\gamma\). Then
\[
W^{t+1}-W^t\le-C\gamma\mathbb E\|\nabla f(x^{t-1})\|^2+\alpha_5\gamma^2+\alpha_6\gamma.
\]
Sum from \(t=1\) through \(T\), use (6) and \(W^{T+1}\ge0\), and divide by \(C\gamma T\). The result is exactly the first requested inequality, including all three numerical coefficients.

## 4. Exact PL bound

If \(f\) is constant, \(f-f^*\equiv0\) and the requested inequality is immediate for every positive \(\mu\). Otherwise the PL inequality together with \(\|\nabla f\|^2\le2L(f-f^*)\) implies \(\mu\le L\).

Set \(\alpha=\alpha_4=\mu C\) and \(\lambda=4\alpha/3\). Since
\[
\tfrac12-21q=C+\tfrac18\ge\tfrac43C,
\qquad \lambda\le\mu/2\le L,
\]
(5) and PL give the stronger recursion
\[
W^{t+1}\le(1-\lambda\gamma_t)W^t+\alpha_5\gamma_t^2+\alpha_6\gamma_t. \tag{7}
\]
All its multiplicative factors are nonnegative. The prescribed schedule is nonincreasing, satisfies \(\gamma_tL<1/36\), and has successive ratio at least \(s_0/(s_0+1)>2/3\), including its phase transition.

For \(T\ge2\), put \(k=\lfloor T/2\rfloor\), \(N=T-k\), and \(a=s_0-1\). Separate the solution of (7) into its homogeneous initial contribution and forcing. For the initial contribution, \(1-u\le e^{-u}\) handles the constant phase. In the diminishing phase, Bernoulli's inequality gives
\[
1-\frac{8}{3u}\le\left(1-\frac1u\right)^{8/3}.
\]
Its product telescopes, yielding an initial contribution to \(W^T/2\) at most
\[
\frac98\Delta_0 e^{-\lambda\gamma_0(k-1)}
\left(\frac{a}{a+N}\right)^{8/3}. \tag{8}
\]
This is bounded by the requested initial term. Indeed, writing \(y=N/a\) and using \(T\le2N\), the ratio of the coefficient in (8) to \(2a^2/T^2\) is at most
\[
\frac94\frac{y^2}{(1+y)^{8/3}}
\le\frac{81}{4\,4^{8/3}}<1.
\]
The maximum follows by differentiation, with maximizer \(y=3\). Also \(e^{-\lambda\gamma_0(k-1)}\le e^{-\alpha\gamma_0(k-1)}\).

For the forcing, weaken the contraction to \(\alpha\) and consider the scalar equality recursion with zero initial value. Its value at \(k\) is at most \((\alpha_5\gamma_0+\alpha_6)/\alpha\) by the geometric sum. In the diminishing phase multiply by \((s_0+t-k)^2\), use
\[
u^2(1-2/u)=u^2-2u\le(u-1)^2,
\]
and telescope. Its value at \(T\) is at most
\[
\frac{a^2}{(a+N)^2}\frac{\alpha_5\gamma_0+\alpha_6}{\alpha}
+\frac{4\alpha_5N}{\alpha^2(a+N)^2}
+\frac{2\alpha_6N}{\alpha(a+N)}.
\]
After division by two, \(a+N\ge N\ge T/2\) bounds these terms by
\[
\frac{2(\alpha_5\gamma_0+\alpha_6)a^2}{\alpha T^2}
+\frac{4\alpha_5}{\alpha^2T}+\frac{\alpha_6}{\alpha}.
\]
Combining this with (8) proves the exact second inequality. The argument includes \(T=2\), where the constant phase is empty. For \(T=1\), the left side is \(\Delta_0\), and the first term on the right is \(2(s_0-1)^2e^{\alpha\gamma_0}\Delta_0\ge\Delta_0\); the other terms are nonnegative.

## 5. Uniform lower bounds for both variants

The source's fixed parameter choice does not establish the claimed uniform denominator dependence: its limiting gradient error divided by \(\kappa G^2/(1-q)\) tends to zero as \(q\uparrow1\). Repair the choice within the same quadratic family as follows.

Fix \(G,B,\kappa\ge0\), \(q=\kappa B^2<1\), \(\mu>0\), and the prescribed initial point \(x^0\). Define
\[
\delta=\mu B\sqrt q,\qquad \epsilon=G\sqrt{1-q},\qquad
r=\frac{\sqrt\kappa G}{\mu\sqrt{1-q}},\qquad z=x-(x^0-r).
\]
Take two honest workers, no Byzantine workers, exact gradients, and
\[
f_1(x)=\frac{\mu+\delta}{2}z^2+\epsilon z,
\qquad f_2(x)=\frac{\mu-\delta}{2}z^2-\epsilon z.
\]
Then \(f_H(x)=\mu z^2/2\), \(f_H^*=0\), and \(L=\mu\) is both a smoothness and PL parameter. Individual local convexity or lower boundedness is not assumed by the source and is not needed.

The honest gradient dispersion is \((\delta z+\epsilon)^2\). Cauchy--Schwarz gives, including all zero cases,
\[
(\delta z+\epsilon)^2
=(\sqrt q\,B\mu z+\sqrt{1-q}\,G)^2
\le B^2\mu^2z^2+G^2.
\]
This parameter choice is the elementary optimizer of the source's two-parameter construction: for \(u=\delta/(B\mu)\), feasibility permits \(\epsilon=G\sqrt{1-u^2}\), and maximizing the squared displacement amounts to maximizing \((1-u^2)/(1-\sqrt q\,u)^2\), whose positive optimizer is \(u=\sqrt q\).

Define a single fixed aggregator on all real input pairs by
\[
A(v_1,v_2)=\frac{v_1+v_2}{2}-\sqrt\kappa\frac{v_1-v_2}{2}.
\]
For every input pair its squared displacement from the mean is exactly
\[
\frac{\kappa}{4}(v_1-v_2)^2
=\frac\kappa2\sum_{i=1}^2(v_i-\bar v)^2.
\]
Thus it satisfies the full robustness definition, including \(\kappa=0\), and requires neither access to the model nor to historical iterates.

On exact gradients this linear map gives the derivative of the drifted quadratic
\[
F(x)=\frac{\mu(1-q)}2z^2-\sqrt\kappa\epsilon z.
\]
Its minimizer is \(z=r\), which is precisely the prescribed initialization. Consequently the no-momentum aggregate is zero there. For local momentum, linearity gives
\[
A(m_1^t,m_2^t)=\beta_t A(m_1^{t-1},m_2^{t-1})+(1-\beta_t)F'(x^{t-1}).
\]
The initial aggregate is zero. Induction therefore shows that both algorithms remain at \(x^0\), with zero aggregated update, for every round and every specified schedule. The instance, initialization and aggregator are fixed before the horizon and schedule parameters are selected. This stationary special case of the same drifted-objective construction eliminates any need to invoke an unspecified momentum-convergence result.

At every iterate,
\[
\|\nabla f_H(x^{T-1})\|^2=\mu^2r^2=\frac{\kappa G^2}{1-q},
\qquad
f_H(x^{T-1})-f_H^*=\frac{\mu r^2}{2}=\frac{\kappa G^2}{2\mu(1-q)}.
\]
Thus the two requested inequalities hold with the same universal \(c=1/2\), in fact for every integer \(T\ge1\). When \(G=0\) or \(\kappa=0\), both target floors are zero and the construction remains valid. When \(B=0\), the same formulas directly apply. Exact gradients satisfy every nonnegative stochastic variance upper bound.

## Audit closure

The replacement closes all obligations using explicit calculations. The stochastic initialization error, the PL prefactor gap, the nonuniform lower-bound comparison, trajectory-only aggregator definition, momentum indexing errors, and degenerate cases are not retained as assumptions or unresolved citations.
