# Reference Proof

## Proof Structure

We construct two normalized empirical spectral laws with identical observed positive moments and different logarithmic moments. The construction preserves equal weights by perturbing the support locations. We then use a normalized two-point empirical sequence whose observed log-moments converge while its logarithmic moment tends to minus infinity.

## Complete Proof

All laws in the task are empirical laws of finite positive lists, with repetitions allowed. Consequently, their moments are finite sums, defined for every real exponent, and differentiation gives
\[
K_P'(0)=\frac{M_P'(0)}{M_P(0)}=\mathbb E_P[\log X].
\]

### Step 1: Local perturbations with exact moment constraints

Let
\[
B=\{1\}\cup\mathcal T=\{a_1,\ldots,a_r\},
\qquad N=r+1,
\]
where repeated exponents are removed. Every exponent in B is positive. In particular, a node equal to 1 adds no extra constraint. The construction also applies when the observation set is empty: then B consists only of 1.

The N functions
\[
a_1x^{a_1-1},\ldots,a_rx^{a_r-1},\frac1x
\]
are linearly independent on \((0,\infty)\). Indeed, multiplication of a putative relation by x gives a relation between the constant function and the distinct positive powers \(x^{a_1},\ldots,x^{a_r}\). Order the positive exponents increasingly. Letting x tend to zero first eliminates the constant coefficient. Dividing the remaining relation by the smallest power and again letting x tend to zero eliminates its coefficient. Repetition eliminates every coefficient.

Therefore, there exist N distinct positive points \(z_1,\ldots,z_N\) such that the evaluation matrix of these functions is invertible. To justify this directly, their evaluation vectors must span \(\mathbb R^N\); otherwise a nonzero vector orthogonal to their span would give a functional relation. Choose N evaluation vectors forming a basis. The selected points are necessarily distinct.

Define the continuously differentiable map
\[
F:(0,\infty)^N\longrightarrow\mathbb R^N,
\qquad
F(u)=\left(
\frac1N\sum_{i=1}^N u_i^{a_1},\ldots,
\frac1N\sum_{i=1}^N u_i^{a_r},
\frac1N\sum_{i=1}^N\log u_i
\right).
\]
At \(z=(z_1,\ldots,z_N)\), its Jacobian \(J=DF(z)\) is the selected invertible evaluation matrix divided by N.

Here is a direct local solvability argument, including the existence step. Use the Euclidean norm and its induced matrix norm. By continuity of DF, choose \(\rho>0\) so that the closed ball \(\overline B(z,\rho)\) is contained in \((0,\infty)^N\) and
\[
\|I-J^{-1}DF(u)\|\leq\frac12
\quad\text{throughout this ball}.
\]
For a target vector v satisfying
\[
\|J^{-1}(v-F(z))\|\leq\frac\rho2,
\]
set
\[
H_v(u)=u+J^{-1}(v-F(u)).
\]
Integration of the derivative along a line segment inside the ball shows that \(H_v\) is Lipschitz with constant at most \(1/2\). Moreover,
\[
\|H_v(u)-z\|
\leq\frac12\|u-z\|+\|J^{-1}(v-F(z))\|
\leq\rho,
\]
so it maps the closed ball into itself. Starting at z, iterate \(u^{(k+1)}=H_v(u^{(k)})\). Successive differences decrease by a factor at most \(1/2\); summing this geometric bound shows that the iterates form a Cauchy sequence. Their limit belongs to the closed ball and, by continuity, is a fixed point of \(H_v\). At this fixed point, \(F(u)=v\).

Let \(e_N\) be the last coordinate vector. Choose \(s>0\) sufficiently small that both targets
\[
v^+=F(z)+s e_N,
\qquad v^-=F(z)-s e_N
\]
satisfy the displayed condition. Obtain positive lists \(u^+\) and \(u^-\) with \(F(u^\pm)=v^\pm\). Thus
\[
\frac1N\sum_i(u_i^+)^a
=\frac1N\sum_i(u_i^-)^a
\quad(a\in B),
\]
whereas
\[
\frac1N\sum_i\log u_i^+
-\frac1N\sum_i\log u_i^-=2s\ne0.
\]
This is an exact finite-constraint perturbation with all weights fixed at \(1/N\).

### Step 2: Normalization and non-identifiability

Because \(1\in B\), the two lists have a common positive mean
\[
\mu=\frac1N\sum_i u_i^+=\frac1N\sum_i u_i^-.
\]
Define empirical laws
\[
P_+=\frac1N\sum_{i=1}^N\delta_{u_i^+/\mu},
\qquad
P_-=\frac1N\sum_{i=1}^N\delta_{u_i^-/\mu}.
\]
Their means are 1. For each observed node t_j, common rescaling multiplies both matched moments by \(\mu^{-t_j}\), so
\[
M_{P_+}(t_j)=M_{P_-}(t_j).
\]
All moments are positive, and taking logarithms gives equality of the observed K-values. Rescaling subtracts \(\log\mu\) from each logarithmic moment, leaving their difference equal to \(2s\). Hence
\[
K_{P_+}(t_j)=K_{P_-}(t_j)\quad(j=1,\ldots,m),
\qquad K_{P_+}'(0)\ne K_{P_-}'(0).
\]
This proves the first assertion. In particular, no function of the observation vector can return the target correctly for both laws.

### Step 3: Saturation and the continuity conclusion

For \(\kappa>1\), let \(P_\kappa\) place mass \(1/2\) at each of
\[
a_\kappa=\frac{2}{1+\kappa},
\qquad b_\kappa=\frac{2\kappa}{1+\kappa}.
\]
It is a positive empirical law and is normalized because \((a_\kappa+b_\kappa)/2=1\). For every fixed \(t>0\),
\[
M_{P_\kappa}(t)
=\frac{a_\kappa^t+b_\kappa^t}{2}
=2^{t-1}\frac{1+\kappa^t}{(1+\kappa)^t}
\longrightarrow 2^{t-1}>0.
\]
It follows that the observation vector
\[
y_\kappa=(K_{P_\kappa}(t_1),\ldots,K_{P_\kappa}(t_m))
\]
converges to
\[
y_*=((t_j-1)\log 2)_{j=1}^m\in\mathbb R^m.
\]
On the other hand,
\[
K_{P_\kappa}'(0)
=\frac12\log a_\kappa+\frac12\log b_\kappa
=\log\!\left(\frac{2\sqrt\kappa}{1+\kappa}\right)
\longrightarrow-\infty.
\]
Choose \(\kappa_n=n+1\) and \(P_n=P_{\kappa_n}\). This sequence works for every estimator in the task.

For an arbitrary continuous \(\Phi:\mathbb R^m\to\mathbb R\), continuity at \(y_*\) gives
\[
\Phi(y_{\kappa_n})\longrightarrow\Phi(y_*),
\]
so these estimates are bounded. Since the target tends to minus infinity,
\[
\left|\Phi(y_{\kappa_n})-K_{P_n}'(0)\right|\longrightarrow\infty.
\]
When m=0, \(\mathbb R^0\) is a singleton, the observation vectors are constant, and the same argument applies. The limiting observation vector need not correspond to an admissible strictly positive law: it lies in the stipulated domain \(\mathbb R^m\) of the estimator, which is precisely where continuity is used.

Thus every continuous estimator based on the finitely many observations has unbounded worst-case absolute error. All laws used in both parts are empirical spectral laws, and every theorem-critical obligation is established above.
