# Reference Proof

## Source Repairs and Contract

The source's displayed conjugate mean has a local divergence-sign error. Its defining loss, appendix expansion, and downstream formulas give the plus-divergence contribution inside the linear-loss coefficient, as already used in the public target. The Gaussian prior must have a negative quadratic log-density. Canonical linear coefficients must be distinguished from posterior means. In the robustness appendix, scalar constants, dropped finite factors, and the normalization of individual-observation precision increments also require local corrections. The proof below implements these corrections directly and does not use the erroneous displayed numerical constants.

The source derivative assumptions are the exact inequalities stated in the replacement public task, not separate boundedness of w∇b and div(w²∇T). The surrogate, weight, prior, and learning rate are unchanged when the observation is replaced. The theorem is pointwise in the sample, so no sampling or training argument is required.

## Proof Structure

First verify the weighted score-matching representation under the explicit integrability assumptions. Expand the exponential-family score to obtain a quadratic empirical loss, combine it with the Gaussian prior, and complete the square. Next derive bounds on the quadratic and linear coefficients from the actual derivative assumptions. These yield uniform spectral and mean bounds for both Gaussian posteriors. Finally evaluate and bound the three terms of their KL divergence.

## Complete Proof

### 1. Score-matching representation

For fixed θ, put sθ(x)=∇x log q(x|θ) and s0(x)=∇x log p0(x). Normalizing q in x does not change sθ, because its finite normalizer depends only on θ. By assumption, wsθ and ws0 belong to L²(p0). Thus the squared-score and cross-score terms below are integrable.

Let Fθ=p0w²sθ. The field and all its first partial derivatives are absolutely integrable componentwise. Consequently ∫div Fθ dx=0. To verify the absence of a boundary term, take smooth cutoffs χR equal to one on the ball of radius R, supported on the ball of radius 2R, and satisfying ||∇χR||∞≤c/R. Compactly supported integration by parts gives ∫χR div Fθ dx=−∫∇χR·Fθ dx. The right side tends to zero by integrability of Fθ, and the left side tends to ∫div Fθ dx by integrability of its derivatives.

The product rule therefore gives
\[
\int p_0\operatorname{div}(w^2s_\theta)\,dx
=-\int p_0w^2s_0^\top s_\theta\,dx.
\]
The cross term is absolutely integrable by Cauchy–Schwarz. Also div(p0w²sθ) is integrable, so this equality verifies integrability of the divergence term in the population objective. Expanding the defining squared difference yields
\[
\operatorname{SM}_w(p_0\|q(\cdot\mid\theta))
=\mathbb E_{p_0}[w^2\|s_\theta\|^2+2\operatorname{div}(w^2s_\theta)]
+\mathbb E_{p_0}[w^2\|s_0\|^2].
\]
The last term is finite and independent of θ. This justifies the stated empirical objective. The posterior calculation itself uses only the finite empirical loss.

### 2. Quadratic loss and Gaussian posterior

Write
\[
G(x)=\nabla_xT(x)\in\mathbb R^{p\times d},\qquad
r(x)=\nabla_xb(x)\in\mathbb R^d.
\]
Then
\[
\nabla_x\log q(x\mid\theta)=G(x)^\top\theta+r(x).
\]
With row-wise divergence, define
\[
A(x)=w(x)^2G(x)G(x)^\top,
\qquad
\nu(x)=w(x)^2G(x)r(x)+\operatorname{div}_x(w(x)^2G(x)).
\]
Direct expansion gives
\[
\begin{aligned}
\ell(x,\theta)
&=w(x)^2\|G(x)^\top\theta+r(x)\|^2
+2\operatorname{div}_x\bigl(w(x)^2(G(x)^\top\theta+r(x))\bigr)\\
&=\theta^\top A(x)\theta+2\theta^\top\nu(x)+c(x),
\end{aligned}
\]
where
\[
c(x)=w(x)^2\|r(x)\|^2+2\operatorname{div}_x(w(x)^2r(x))
\]
is finite at every x and independent of θ. In particular, the divergence contribution to ν has a plus sign.

Since nLn(θ)=∑iℓ(xi,θ), multiplying the empirical update by the Gaussian prior gives the log kernel
\[
-\tfrac12\theta^\top\Lambda_n\theta+\theta^\top h_n+\text{constant},
\]
where
\[
\Lambda_n=\Sigma^{-1}+2\beta\sum_{i=1}^n A(x_i),
\qquad
h_n=\Sigma^{-1}\mu-2\beta\sum_{i=1}^n\nu(x_i).
\]
Every A(x) is positive semidefinite, whereas Σ−1 is positive definite. Hence Λn is positive definite even if every data contribution is singular or zero. Completing the square gives
\[
-\tfrac12(\theta-\Lambda_n^{-1}h_n)^\top\Lambda_n
(\theta-\Lambda_n^{-1}h_n)+\text{constant}.
\]
This kernel has a finite positive integral. Therefore
\[
\pi_n=\mathcal N(m_n,C_n),\qquad C_n=\Lambda_n^{-1},\qquad m_n=C_nh_n,
\]
which gives exactly the precision and mean in the public task.

### 3. Consequences of the source derivative bounds

Let C,C′ be the finite nonnegative constants in the public derivative assumptions. For every x,
\[
w\|G\|_F\le C,\qquad
w^2\|G\|_F\|r\|_2\le C^2,\qquad
w^2\|\nabla_x^2T\|_F\le C^2,
\]
\[
\|\nabla_x(w^2)\|_2\|G\|_F\le C'.
\]
For any v∈R^p,
\[
v^\top A(x)v=w(x)^2\|G(x)^\top v\|^2\le C^2\|v\|^2,
\]
so
\[
0\preceq A(x)\preceq C^2I_p.
\]
For each statistic component Tk,
\[
[\operatorname{div}(w^2G)]_k
=\nabla(w^2)^\top\nabla T_k+w^2\operatorname{tr}(\nabla^2T_k).
\]
Using ||tr H||≤√d||H||F for each d-by-d Hessian and then summing squared component bounds gives
\[
\|\operatorname{div}(w^2G)\|_2
\le\|\nabla(w^2)\|_2\|G\|_F
+\sqrt d\,w^2\|\nabla^2T\|_F
\le C'+\sqrt d\,C^2.
\]
Consequently
\[
\|\nu(x)\|_2\le D,
\qquad D=(1+\sqrt d)C^2+C'.
\]
These bounds use the derivative-product control from the source; boundedness of w∇b is neither assumed nor needed. The product inequality also applies when ∇(w²)=0.

### 4. Uniform Gaussian parameter bounds

Fix n≥1, j∈{1,…,n}, and the original sample. Let subscripts o and c denote the original and replacement posteriors. The replacement posterior uses the same w,q,β,μ,Σ and replaces only xj by z.

Define
\[
a=\lambda_{\min}(\Sigma^{-1})>0,\qquad
K=\lambda_{\max}(\Sigma^{-1})+2\beta nC^2.
\]
For either sample, uniformly over z,
\[
aI_p\preceq\Lambda\preceq KI_p.
\]
Thus
\[
K^{-1}I_p\preceq C=\Lambda^{-1}\preceq a^{-1}I_p.
\]
In particular both Gaussian posteriors are nondegenerate. Also, with
\[
B=\|\Sigma^{-1}\mu\|_2+2\beta nD,
\]
we have ||h||2≤B and
\[
\|m\|_2\le B/a,\qquad \|m_c-m_o\|_2\le 2B/a.
\]
All constants are finite and independent of z. These statements include n=1, constant weights, and zero or rank-deficient statistic derivatives.

### 5. Gaussian KL identity and its uniform bound

For positive-definite Co,Cc, subtracting Gaussian log densities and taking expectation under Θ∼N(mo,Co) gives
\[
\operatorname{KL}(\mathcal N(m_o,C_o)\|\mathcal N(m_c,C_c))
=\tfrac12\left[
\operatorname{tr}(C_c^{-1}C_o)
+(m_c-m_o)^\top C_c^{-1}(m_c-m_o)
-p+\log\frac{\det C_c}{\det C_o}\right].
\]
Indeed, the expected original centered quadratic form is p, and the expected contaminated quadratic form is tr(Cc−1Co)+(mo−mc)⊤Cc−1(mo−mc). This proves the standard identity used here, and the preceding section verifies its hypotheses.

Since Cc−1≤KI and Co≤a−1I, trace monotonicity for positive-semidefinite products gives
\[
\operatorname{tr}(C_c^{-1}C_o)\le pK/a.
\]
The mean term satisfies
\[
(m_c-m_o)^\top C_c^{-1}(m_c-m_o)
\le K\|m_c-m_o\|^2\le 4KB^2/a^2.
\]
Every covariance eigenvalue lies in [K−1,a−1]. Therefore
\[
\left|\log\frac{\det C_c}{\det C_o}\right|
\le p\log(K/a).
\]
Combining these bounds yields
\[
\operatorname{PIF}_{\rm KL}(z)
\le\tfrac12\left[\frac{pK}{a}+\frac{4KB^2}{a^2}-p+p\log\frac Ka\right]<\infty.
\]
The right side does not depend on z. Taking the supremum over z∈R^d proves the claimed robustness.

## Proof-Obligation Audit

- Weighted score-matching finiteness and integration by parts: explicitly verified from the public integrability conditions.
- Quadratic and linear loss coefficients, including the divergence sign: explicitly expanded.
- Positive-definite precision, finite normalizer, and Gaussian mean/covariance: explicitly derived by completion of the square.
- Consequences of the exact source derivative assumptions: explicitly derived, including the Hessian contraction factor √d.
- Uniform precision, covariance, and posterior mean bounds: explicitly established.
- Gaussian KL formula: stated with its hypotheses and derived from Gaussian log densities and moments.
- Uniform bounds for the trace, mean, and determinant terms and the final supremum: explicitly established.

No unresolved proof obligation remains.
