# Reference Proof

## Proof Structure

Interpret the forecast mean under the conditional predictive distribution, establish its finiteness, subtract the two recursions, and expand the error. Factor its characteristic function using independence. For distinct positive scales, derive the partial-fraction coefficients and verify the hypotheses of Fourier inversion. Integrate the density and establish a measurable, unique positive central radius and exact coverage for the fitted predictive path.

## Complete Proof

### 1. Conditional law and conditional means

Fix the finite horizon k. The future innovation vector is independent of F_N and has the product of k standard Laplace laws. The initial value and all fitted coefficients used through N+k are finite and F_N-measurable. Thus, conditional on origin information, the predictive path is obtained by applying its displayed recursion with fixed coefficients to that product law. This also specifies a measurable conditional probability kernel for the path.

All means in the task are conditional-distribution integrals. Their absolute first moments are finite. Indeed, at a fixed history let M_t denote the integral of |hat y_t| under the conditional law. Then M_N=|y_N|<infinity and, since E|xi_t|=1,
\[
M_t\le |\hat c(t)|+|\hat\Phi(t)|M_{t-1}+\hat b(t)<\infty
\]
by induction. The innovation at time t has conditional mean zero. Integrating the recursion therefore gives
\[
m_N=y_N,\qquad m_t=\hat c(t)+\hat\Phi(t)m_{t-1}.
\]
This argument does not assume unconditional integrability of fitted coefficients or forecasts. Measurability of m_t follows from the recursion.

### 2. Error recursion and expansion

Write e_t=hat y_t-m_t. Subtraction gives e_N=0 and
\[
e_{N+j}=\hat\Phi(N+j)e_{N+j-1}+\hat b(N+j)\xi_{N+j}.
\]
For j=1 this gives e_{N+1}=hat b(N+1)xi_{N+1}. If the expansion holds at a horizon h<k, substitution into the next recursion multiplies each old coefficient by hat Phi(N+h+1) and introduces the coefficient hat b(N+h+1) for the new innovation. These are exactly the coefficients defined by the products in the task. Hence
\[
e_{N+k}=\sum_{j=1}^k a_{j,k}\xi_{N+j},\qquad
 a_{j,k}=\hat b(N+j)\prod_{r=j+1}^k\hat\Phi(N+r).
\]
The proof allows zero and negative autoregressive coefficients.

### 3. Conditional characteristic function

Direct integration of the standard Laplace density gives, for real v,
\[
\mathbb E e^{iv\xi}
=\frac12\int_0^\infty e^{-(1-iv)x}\,dx
 +\frac12\int_0^\infty e^{-(1+iv)x}\,dx
=\frac12\left(\frac1{1-iv}+\frac1{1+iv}\right)
=\frac1{1+v^2}.
\]
Conditional on F_N the coefficients are fixed and the innovations retain their independent product law. Consequently,
\[
\varphi_k(t)=\mathbb E[e^{it e_{N+k}}\mid F_N]
=\prod_{j=1}^k\frac1{1+a_{j,k}^2t^2}.
\]
A zero coefficient contributes the factor one. This proves the characteristic-function assertion without any distinctness condition.

### 4. Partial fractions

For the remaining claims assume the scales are positive and pairwise distinct almost surely. Fix a history satisfying this condition and abbreviate s_j=s_{j,k}, A_j=A_{j,k}. Put
\[
Q(u)=\prod_{j=1}^k(1+s_j^2u),\qquad
P(u)=\sum_{j=1}^k A_j\prod_{\ell\ne j}(1+s_\ell^2u).
\]
The polynomial P has degree at most k-1. At each of the k distinct points u=-1/s_i^2, every summand except the i-th vanishes, and
\[
P(-1/s_i^2)
=A_i\prod_{\ell\ne i}(1-s_\ell^2/s_i^2)=1
\]
by the definition of A_i. Therefore P-1 is a polynomial of degree at most k-1 with k distinct zeros, so P=1. Dividing by Q proves
\[
\prod_{j=1}^k(1+s_j^2u)^{-1}
=\sum_{j=1}^k\frac{A_j}{1+s_j^2u}
\]
away from the poles. At u=0 this gives sum_j A_j=1. The argument includes k=1 with empty products equal to one.

### 5. Fourier inversion, density, and CDF

Use the following standard independent Fourier-inversion theorem: if a probability law has an integrable characteristic function phi, it has a bounded continuous density equal to (2pi)^(-1) times the integral of exp(-itx)phi(t) over the real line. The standard transform identity for s>0 is
\[
\frac1{2\pi}\int_{\mathbb R}\frac{e^{-itx}}{1+s^2t^2}\,dt
=\frac1{2s}e^{-|x|/s}.
\]
These are the audited background statements associated with theory_010.

Their hypotheses hold at the fixed history. In particular,
\[
0<\varphi_k(t)\le (1+s_1^2t^2)^{-1},
\]
and the upper bound is integrable on R. Every term in the finite partial-fraction expansion is also integrable. Substituting u=t^2 and inverting the finite sum yields
\[
f_k(x)=\frac12\sum_{j=1}^k A_{j,k}s_{j,k}^{-1}e^{-|x|/s_{j,k}}.
\]
The coefficients A_j need not be nonnegative: this is a signed representation of an actual probability density, not necessarily a probabilistic mixture. Its integral is sum_j A_j=1.

For x>=0, termwise tail integration gives
\[
\mathbb P(e_{N+k}>x\mid F_N)
=\frac12\sum_{j=1}^k A_{j,k}e^{-x/s_{j,k}}.
\]
Subtracting from one proves the stated CDF. At x=0 its value is 1/2.

### 6. Positivity, continuity, and central probability

Here is an explicit justification of positivity and continuity, independent of the signs of the partial-fraction coefficients. At the fixed history, write
\[
e_{N+k}=a_{k,k}\xi_{N+k}+Z,\qquad
Z=\sum_{j<k}a_{j,k}\xi_{N+j}.
\]
The two terms are independent. Since a_{k,k}=hat b(N+k)>0, the first term has bounded, continuous, strictly positive density h(x)=(2a_{k,k})^(-1)exp(-|x|/a_{k,k}). Conditioning on Z and integrating shows that the sum has density
\[
f(x)=\mathbb E[h(x-Z)].
\]
This is positive for every x. It is continuous by dominated convergence, using the constant bound h<=1/(2a_{k,k}). For k=1 take Z=0. The conditional error law is symmetric because the independent innovation vector has the same law as its negative.

Define H(q)=P(|e_{N+k}|<=q|F_N) for q>=0. The positive continuous density gives
\[
H(q)=\int_{-q}^{q}f(x)\,dx.
\]
Thus H is continuous, H(0)=0, and H is strictly increasing: whenever 0<=q_1<q_2, the added intervals have strictly positive integral. Also H(q) tends to one as q tends to infinity. Hence for each fixed alpha in (0,1) there is exactly one finite q>0 with H(q)=alpha.

### 7. Measurable radius, equation, and coverage

This history-dependent radius has an F_N-measurable version. For example, define it by
\[
q_{k,\alpha}=\inf\{r\in\mathbb Q_{>0}:H(r)\ge\alpha\}.
\]
For each rational r, H(r) is F_N-measurable. The countable infimum is measurable, and continuity and strict increase show that it is exactly the unique root just established. Definitions on the null exceptional set can be chosen arbitrarily. Any two F_N-measurable radii with the asserted conditional probability agree almost surely by pointwise strict increase.

Symmetry and the CDF give, for q>=0,
\[
H(q)=2F_k(q)-1
=1-\sum_{j=1}^k A_{j,k}e^{-q/s_{j,k}}.
\]
Therefore q_{k,alpha} is the unique solution in [0,infinity) of
\[
\sum_{j=1}^k A_{j,k}e^{-q_{k,\alpha}/s_{j,k}}=1-\alpha,
\]
and it is strictly positive. No uniqueness assertion is made for negative q.

Finally, m_{N+k} and q_{k,alpha} are F_N-measurable. Evaluating the conditional kernel at these measurable endpoints and using e_{N+k}=hat y_{N+k}-m_{N+k} proves
\[
\mathbb P\!\left(\hat y_{N+k}\in
[m_{N+k}-q_{k,\alpha},m_{N+k}+q_{k,\alpha}]\mid F_N\right)=\alpha.
\]
This is exact coverage under the fitted predictive law, not a claim that arbitrary fitted and true parameter trajectories coincide.

## Obligation Closure

Conditional-law well-definedness and mean finiteness are established in Section 1; the expansion in Section 2; transform factorization in Section 3; the paper-specific rational identity in Section 4; inversion and its hypotheses in Section 5; density regularity and quantile existence in Section 6; and measurability, uniqueness on the radius domain, and coverage in Section 7. No unresolved theorem-critical dependency remains.
