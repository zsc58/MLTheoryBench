# Reference Proof

## Proof obligations

1. Verify the conditioning, normalization, and well-definedness of the observables. The quadratic-form identities supplied in the problem may be used directly.
2. Justify a finite resolvent expansion and its expected remainders without exchanging expectation with an uncontrolled infinite series.
3. Obtain all three quadratic and all four cubic training terms, distinguishing the covariance-controlled quadratic coefficient from the third-moment coefficient.
4. Obtain every quadratic population term, including both kernel–population-matrix contractions and the population-vector–kernel contraction.
5. Subtract coefficients at the same insertion order to obtain the quadratic generalization correction.
6. Verify the moment counting and identify precisely which assumptions, rather than external results, close the proof.

## 1. Setting and exact identities

Everything except Θ is fixed. In particular, the training label vector is not averaged over and is not allowed to depend on Θ. Both K and its finite mean \bar K are positive semidefinite. Consequently G and G_0 exist for every γ>0, including when either kernel is singular.

The population assumptions imply that C is finite almost surely and has an integrable operator norm, since ||C||_2≤∫||k(x)||_2^2 dμ(x). Cauchy–Schwarz gives
\[
\|b\|_2\le\sqrt c\left(\int\|k(x)\|_2^2\,d\mu(x)\right)^{1/2},
\]
so b is integrable as well. Thus all three means and centered fluctuations are well defined. Also ||G||_2≤γ^(-1), which makes the test-error quadratic form integrable.

For completeness, the ridge normal equations give
\[
w^*=(\Phi^T\Phi+N\lambda I_n)^{-1}\Phi^Ty
=\Phi^T(\Phi\Phi^T+N\lambda I_N)^{-1}y
=\frac1n\Phi^TGy.
\]
The middle equality follows by multiplying either side by the invertible matrix Φ^TΦ+NλI_n. Therefore the training prediction is KGy and the population prediction is k(x)^TGy. The identity KG=I_N−γG gives the supplied training error. Expanding the population square and applying the definitions of C,b,c gives the supplied test error. These calculations check the normalization; proving them is not an additional obligation when the supplied identities are used directly.

## 2. Finite expansions and remainder control

Write D=ΔK. For a fixed realization introduce, only for the proof,
\[
R(t)=(\bar K+tD+\gamma I_N)^{-1},\qquad 0\le t\le1.
\]
The matrix inside the inverse equals (1−t)\bar K+tK+γI_N, so it is positive definite and ||R(t)||_2≤γ^(-1) throughout this interval. In particular R is smooth on the interval. Differentiating its inverse identity gives R'(t)=−R(t)DR(t). Induction using the product rule then gives
\[
R^{(r)}(t)=(-1)^r r!(R(t)D)^rR(t),\qquad
\|R^{(r)}(t)\|_2\le r!\gamma^{-(r+1)}\delta_K^r.
\]

For a matrix-valued function F with m+1 continuous derivatives, repeated integration of its derivative yields
\[
F(1)=\sum_{r=0}^m\frac{F^{(r)}(0)}{r!}
+\frac1{m!}\int_0^1(1-t)^mF^{(m+1)}(t)\,dt.
\]
This identity holds entrywise, and its remainder norm is bounded by sup_{0≤t≤1}||F^{(m+1)}(t)||/(m+1)!. All functions to which it is applied below are smooth by the preceding positivity argument. Thus only finite sums and integrable, explicitly bounded remainders will be averaged.

Let
\[
A_r=(-1)^r(G_0D)^rG_0.
\]
These are the Taylor coefficients of R(t) at zero and are also the coefficients of the source's resolvent expansion. The assumed almost-sure Neumann condition is therefore consistent with the calculation, but no uniform margin below one and no expectation of an infinite Neumann sum is needed.

## 3. Training expansion

For F(t)=R(t)^2, the product rule and the derivative bound above imply
\[
\|F^{(r)}(t)\|_2\le r!(r+1)\gamma^{-(r+2)}\delta_K^r.
\]
Indeed, the r+1 Leibniz terms each contain r copies of D and r+2 resolvent factors after the factorials are combined. The coefficient of t^r is
\[
\sum_{j=0}^r A_jA_{r-j}.
\]
For r=0 this is G_0^2. For r=1 its expectation vanishes because ED=0. The degree-two coefficient has expectation
\[
L_1=\mathbb E[A_2A_0+A_0A_2+A_1A_1],
\]
which expands into exactly the three displayed quadratic products in the task. The degree-three coefficient has expectation
\[
L_2=\mathbb E[A_3A_0+A_0A_3+A_2A_1+A_1A_2],
\]
which expands into exactly the four displayed cubic products, all with negative signs. No commutativity between D and G_0 is used.

Taylor expansion through degree three gives
\[
\mathbb EG^2=G_0^2+L_1+L_2+R_{\rm tr,4},\qquad
\|R_{\rm tr,4}\|_2\le5\gamma^{-6}\mathbb E\delta_K^4.
\]
This proves the required matrix remainder assertion and hence the training-error formula after multiplication by (γ²/N)y^T and y.

For later subtraction, the same argument through degree two also gives
\[
\mathbb EG^2=G_0^2+L_1+R_{\rm tr,3},\qquad
\|R_{\rm tr,3}\|_2\le4\gamma^{-5}\mathbb E\delta_K^3.
\]
This second formula is an order-consistent truncation, not a claim that L_2 vanishes.

The covariance premise can be applied directly to the three degree-two terms:
\[
L_1=\frac1n\left[G_0(V\star G_0)G_0^2+G_0^2(V\star G_0)G_0+G_0(V\star G_0^2)G_0\right].
\]
All matrices contracted with V here are deterministic. In contrast, L_2 contains third moments of D; the covariance tensor alone does not determine it. Its norm is bounded by 4γ^(-5)Eδ_K^3. Thus L_1 is the quadratic, nominal n^(-1) contribution, and L_2 is a cubic, nominal n^(-3/2) contribution, with the stated dependence on resolvent factors.

## 4. Test expansion

Put H=ΔC and e=Δb. Consider the scalar expression
\[
T(t)=y^TR(t)(\bar C+tH)R(t)y-2(\bar b+te)^TR(t)y+c.
\]
At t=1 this is E_te. Its degree-zero term is
\[
E_{\rm te}^{(0)}=y^TG_0\bar C G_0y-2\bar b^TG_0y+c.
\]
Set S_1=A_1=−G_0DG_0 and S_2=A_2=G_0DG_0DG_0. The degree-one term is
\[
y^T(S_1\bar C G_0+G_0\bar C S_1+G_0HG_0)y
-2(\bar b^TS_1y+e^TG_0y).
\]
Its expectation is zero by the three centering identities, not by independence.

The complete degree-two expectation is
\[
\begin{aligned}
\mathbb E\{&y^T[S_2\bar C G_0+G_0\bar C S_2+S_1\bar C S_1
+S_1HG_0+G_0HS_1]y\\
&-2[\bar b^TS_2y+e^TS_1y]\}.
\end{aligned}
\]
Substituting S_1 and S_2 gives exactly E_te^(1) in the task: three positive pure-kernel terms weighted by \bar C; two negative D–H terms; one negative pure-kernel term weighted by \bar b; and one positive e–D term. The two matrix mixed terms are both present, including when they can be combined by symmetry in the scalar quadratic form. No H², e², or H–e term occurs because the original loss is separately linear in C and b.

For a complete remainder bound, expand R(t)\bar C R(t) through degree two and R(t)H R(t) through degree one, the latter being multiplied by t. Similarly expand \bar b^TR(t)y through degree two and e^TR(t)y through degree one. For any fixed matrix B, the same product-rule count gives
\[
\left\|\frac{d^r}{dt^r}[R(t)BR(t)]\right\|_2
\le r!(r+1)\gamma^{-(r+2)}\delta_K^r\|B\|_2.
\]
The finite Taylor bounds therefore show that the unaveraged remainder after the degree-two terms has absolute value at most
\[
\begin{aligned}
&\left(4\|y\|_2^2\|\bar C\|_2\gamma^{-5}
+2\|y\|_2\|\bar b\|_2\gamma^{-4}\right)\delta_K^3\\
&\quad+3\|y\|_2^2\gamma^{-4}\delta_K^2\delta_C
+2\|y\|_2\gamma^{-3}\delta_K^2\delta_b.
\end{aligned}
\]
The stated moments make this bound integrable. Taking expectation proves
\[
\mathbb EE_{\rm te}=E_{\rm te}^{(0)}+E_{\rm te}^{(1)}+O(\Delta^3)
\]
with precisely the public remainder convention. In particular, no unspecified mixed covariance formula is needed to prove this target: the mixed expectations are retained in its explicit coefficient.

## 5. Generalization gap

Subtract the degree-two training expansion from the test expansion. Linearity of expectation is applicable because both errors are integrable. The constant term is
\[
E_{\rm gen}^{(0)}=E_{\rm te}^{(0)}-\frac{\gamma^2}{N}y^TG_0^2y,
\]
and the degree-two coefficient is
\[
E_{\rm gen}^{(1)}=E_{\rm te}^{(1)}-\frac{\gamma^2}{N}y^TL_1y.
\]
The additional training remainder has absolute value at most
\[
\frac{4\|y\|_2^2}{N\gamma^3}\mathbb E\delta_K^3,
\]
so it is included in O(Δ³) under the public definition. This proves the gap formula. L_2 remains part of the separate cubic training expansion; it is not part of the quadratic gap coefficient. Including its subtraction in a different approximation with a cubic remainder would not determine the cubic gap coefficient, since cubic test terms have not been retained.

The mixed terms occur structurally in the formula. They can vanish for particular feature laws or targets; no universal nonvanishing or non-representability claim is required.

## 6. Closure and source alignment

Every expectation used above is a finite sum of terms bounded by the explicit moments in the task. The moment bounds give quadratic insertion order n^(-1), cubic insertion order n^(-3/2), and the fourth-order training moment n^(-2). These insertion counts do not supply uniform bounds when γ tends to zero or deterministic coefficients grow; all such dependence remains in the displayed remainder constants.

The argument covers zero labels, vanishing fluctuations, zero covariance, singular kernels, and N=n=1. No division by a fluctuation size, covariance, or label norm was used.

The source locations for the coefficient calculations are L000132-L000179, L000229-L000260, and L000441-L000450. The covariance law is supplied as a premise at L000099-L000105. The adopted result at L000071-L000087 is a nonstandard background dependency for the paper's ensemble motivation, but is not invoked to establish that premise from neural-network parameters in this conditional task. In particular, this proof does not claim that layerwise second moments alone establish the kernel covariance or any cubic moment. Nor does it invoke the downstream population-vertex or spectral results. The finite-remainder argument is a routine completion of the source's same resolvent-product expansion. All six obligations are closed.
