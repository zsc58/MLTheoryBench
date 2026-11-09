# Reference Proof

## Contract and proof obligations

The target is a deterministic existence statement, uniform over the analytic class. All network weights are unrestricted real numbers. The architecture constants must not depend on the particular function, on the width-depth parameters, or on the fixed regime parameters except where explicitly allowed. Thresholds for sufficiently large parameters may depend on the fixed parameters.

The obligations are: (1) derive a finite polynomial approximation with quantitative degree, cardinality, coefficient, and uniform-tail bounds; (2) realize its polynomials with quantitative ReLU error and architecture bounds; (3) implement weighted sums without an unaccounted width, depth, range, or error cost; (4) derive both parameterized architecture estimates; (5) perform the integer rescalings and verify every regime and endpoint. These obligations are closed below. In particular, the analytic truncation result and the two paper-specific construction lemmas are not assumed.

## 1. Analytic polynomial approximation

Let mu_d be product uniform probability measure on [-1,1]^d. Use the normalized Legendre polynomials L_n from the source, their tensor products L_nu, and coefficients l_nu=integral f L_nu dmu_d. Put a_i=log rho_i>0 and

\[
\Lambda(t)=\{\nu\in\mathbb N_0^d:a\cdot\nu\le t\},\qquad t\ge1.
\]

All constants in this section are uniform over f in A(rho,M).

### Coefficient decay and summability

Write J(w)=(w+w^{-1})/2 and G(w)=F(J(w_1),...,J(w_d)), where F is the bounded holomorphic extension. The function G is holomorphic and bounded by M on the product annulus rho_i^{-1}<|w_i|<rho_i. Its Laurent coefficients are contour integrals

\[
 a_k=(2\pi i)^{-d}\int\cdots\int G(w)\prod_i w_i^{-k_i-1}\,dw_i.
\]

For k_i>=0 choose the corresponding contour radius r_i in (1,rho_i); for k_i<0 choose radius r_i^{-1}. The contour bound, followed by r_i increasing to rho_i, gives

\[
 |a_k|\le M\prod_i\rho_i^{-|k_i|}.
\]

The invariance under each substitution w_i->w_i^{-1} lets us group the absolutely convergent Laurent expansion on |w_i|=1. With T_j(cos theta)=cos(j theta), this yields

\[
 f(x)=\sum_{m\in\mathbb N_0^d} b_m\prod_iT_{m_i}(x_i),
 \qquad |b_m|\le 2^dM\prod_i\rho_i^{-m_i}.
\]

The expansion converges absolutely and uniformly on the cube. Orthogonality makes the integral of a summand against L_nu zero if some m_i<nu_i. Otherwise its absolute integral is at most 1 by Cauchy-Schwarz, since the tensor Legendre polynomial has L2 norm 1 and the Chebyshev product has supremum norm at most 1. Consequently

\[
 |l_\nu|\le 2^dM\prod_i\frac{\rho_i^{-\nu_i}}{1-\rho_i^{-1}},
 \qquad \sum_\nu|l_\nu|\le C(d,\rho)M.                 \tag{1}
\]

This also implies the weaker coefficient estimate used in the source.

### Legendre size and coefficient bounds

Expanding the integrand verifies directly from the source's explicit polynomial formula that, for x in [-1,1],

\[
 L_n(x)=\frac{\sqrt{2n+1}}{\pi}\int_0^\pi
 (x+i\sqrt{1-x^2}\cos\theta)^n\,d\theta.
\]

Its integrand has modulus at most 1. Thus ||L_n||_infinity<=sqrt(2n+1).

We also need the absolute monomial coefficient sum S_n of L_n. The explicit polynomial formula gives, for n>=2,

\[
 L_n=A_nxL_{n-1}-B_nL_{n-2},\quad
 A_n=\frac{\sqrt{(2n-1)(2n+1)}}n<2,\quad
 B_n=\frac{n-1}{n}\sqrt{\frac{2n+1}{2n-3}}\le2.
\]

Therefore S_n<=2S_{n-1}+2S_{n-2}. Starting from S_0=1 and S_1=sqrt(3), induction gives

\[
 S_n\le4^n.                                             \tag{2}
\]

### Tail, degree, and cardinality

Combining (1) with the supremum bound for L_n gives absolute uniform convergence of the Legendre series. Its L2 coefficients and completeness identify its sum with f. For the omitted indices,

\[
 \begin{aligned}
 \left\|f-\sum_{\nu\in\Lambda(t)}l_\nu L_\nu\right\|_\infty
 &\le C(d,\rho)M\sum_{a\cdot\nu>t}
       e^{-a\cdot\nu}\prod_i\sqrt{2\nu_i+1}\\
 &\le C(d,\rho)M e^{-t/2}\sum_\nu
       e^{-a\cdot\nu/2}\prod_i\sqrt{2\nu_i+1}
 \le C(d,\rho,M)e^{-t/2}.                         \tag{3}
 \end{aligned}
\]

The final series is a product of convergent one-dimensional series. Each index in Lambda(t) has |nu|_1<=t/min_i a_i. Enclosing Lambda(t) in the box 0<=nu_i<=t/a_i and including the box 0<=nu_i<=t/(d a_i) show

\[
 c(d,\rho)(1+t)^d\le |\Lambda(t)|\le C(d,\rho)(1+t)^d.
                                                               \tag{4}
\]

Equations (3)-(4) prove the source's exponential-in-cardinality truncation result, rather than merely invoking its nonstandard external citation.

## 2. Network primitives and exact transport

We use the standard independent multiplication result stated in the supplied source: for real u<v and positive integers B,h, there is a ReLU network of width at most 10B and depth at most h whose error in approximating xy on [u,v]^2 is at most 6(v-u)^2 B^{-h}. Every application below specifies an interval containing its actual inputs and uses positive integer B,h.

Affine maps can be incorporated at network interfaces. A signed scalar can be transported through hidden layers exactly using its two coordinates sigma(z) and sigma(-z), since z=sigma(z)-sigma(-z). Thus retaining s scalar values costs at most 2s channels and no approximation error. Parallel networks can be padded to a common depth by these identity channels. Exact affine summation introduces neither numerical error nor a bounded-weight requirement. An affine identity or constant needs no multiplication stage.

On [-2,2]^2, a multiplication node has error at most 96B^{-h}. A balanced tree with inputs in [-1,1] has level errors bounded recursively by delta+3e, where delta=96B^{-h}, as long as preceding errors are at most 1/10. In particular, a tree for at most 2k inputs has error at most Ck^2 B^{-h}, width O(kB), and depth O(h log k). Padding unused leaves with ones makes it a power network. This is the same padded multiplication-tree construction as in the source; it avoids invoking the power lemma with an inadmissible r. Degree zero and degree one are exact.

For later products of a fixed number d of factors bounded by exp(Cm), choose a multiplication interval [-R,R], where R=exp(C_d m) is large enough to contain every exact partial product and a margin of 1. A sequential product uses at most d-1 multiplication nodes. Its local error is at most 24R^2B^{-h}; telescoping multiplication and the same range induction give total error at most exp(C'_d m)B^{-h}. Its width is O_d(B) and depth O_d(h). Choosing h sufficiently large as below makes all approximate intermediate products stay inside [-R,R]. For d=1, the product is the exact identity and its error is zero.

## 3. Common construction parameters

For the next two constructions let T,Q be sufficiently large positive integers, and let 0<=lambda<=d. Set

\[
 t=T\log Q,\qquad \Lambda=\Lambda(t),\qquad S=|\Lambda|,
 \qquad m=\left\lceil C_\rho t\right\rceil,
\]

where C_rho is fixed large enough that every index in Lambda has total degree at most m. Thus m is comparable to T log Q and S is comparable to (T log Q)^d. Take

\[
 B=\lfloor\sqrt Q\rfloor,\qquad
 k=\max\{2,\lfloor\log Q\rfloor\},\qquad
 h=\left\lceil A\frac{m}{\log B}\right\rceil.              \tag{5}
\]

For sufficiently large Q, B>=2, log B is comparable to log Q, and k<=m. Hence h=O_{d,rho}(T). The fixed constant A, depending only on d, can be enlarged to dominate all exponential factors in the error calculations. In particular B^{-h}<=exp(-Am). None of these parameters depends on M or on f.

All intermediate polynomial errors below have the form exp(C_d m)B^{-h}, with constants independent of T,Q,lambda. Choosing A larger than those constants makes them at most exp(-c m), and also validates each previously stipulated range bound. This supplies the fixed-constant choice omitted by an unqualified use of asymptotic parameter choices.

## 4. First polynomial and summation architecture

Construct all powers x,...,x^k by parallel padded trees. Their combined width is O(k^2B), their depth is O(h log k), and their errors are bounded by Ck^2B^{-h}. Retain an approximation to x^k. Successively multiplying a block by this retained value generates the next k powers. The block recurrence has error bounded by a constant times the previous block error plus the initial power error and B^{-h}; after at most ceil(m/k) blocks the error is bounded by exp(Cm)B^{-h}. With A chosen in (5), all these approximate powers lie in [-1.1,1.1], within the multiplication interval.

For any n<=m, accumulate the monomial coefficients of L_n while generating the power blocks. The coefficient bound (2) multiplies the power error by at most 4^m, so the polynomial error remains exp(Cm)B^{-h}. The accumulator and original input are transported exactly by signed channels. When n<k, only the initial block and an affine readout are needed; n=0 is exactly 1. The resulting scalar polynomial network has width O(k^2B+k) and depth

\[
 O\bigl(h(\log k+m/k)\bigr).
\]

Apply this in parallel to the coordinates of a tensor polynomial, and use the fixed-d product construction from Section 2. By (2), exact factors are bounded by 4^m; approximate factors and partial products are bounded by exp(C_d m). The stipulated product interval is therefore valid. The tensor approximation error is at most exp(C_d m)B^{-h}, by a telescoping product estimate. Since k is comparable to log Q and B is comparable to sqrt Q, for all sufficiently large Q its width is at most C(d)Q and its depth is at most

\[
 C(d,\rho)T\bigl(T+\log\log Q\bigr).                    \tag{6}
\]

Its error is at most exp(-c m) after the choice of A.

Choose an integer p comparable to T^lambda(log Q)^d, capped by S if necessary. The cap changes comparisons only by constants depending on d,rho, because lambda<=d. Partition Lambda into J=ceil(S/p) blocks, zero-padding the final block. Equations (4)-(5) give J<=C(d,rho)T^{d-lambda}.

In each block evaluate at most p tensor networks in parallel. Carry x and the accumulated weighted sum exactly to the next block. The final affine output is the complete weighted sum. This is sequential affine accumulation, not clipping. Its width and depth satisfy

\[
 W_1\le C(d,\rho)T^\lambda Q(\log Q)^d,\qquad
 D_1\le C(d,\rho)T^{d-\lambda+1}
                      (T+\log\log Q).                  \tag{7}
\]

By (1), the error in the weighted sum is at most C(d,rho)M exp(-c m), with no extra S factor. Adding (3), and using m comparable to T log Q, gives

\[
 E_1\le C(d,\rho,M)Q^{-c(d,\rho)T}.                     \tag{8}
\]

## 5. Shared-feature architecture

There is a second way to form all scalar Legendre polynomials through degree m. At doubling level i, retain approximations to x^j for j<=2^i. Independently form an approximation to x^{2^i} from the original x by a padded tree, then multiply it by the retained powers to form the next block. Run this tree in parallel with the preceding-level network and transport the preceding outputs exactly through the multiplication stage.

With the same B,h, the width through all levels is O(mB) and the depth is bounded by O(h(1+log m)^2). Indeed, the new tree has depth O(ih), the preceding network has depth O(i^2h), and the final multiplication stage adds h. Widths are O(2^iB) at level i, including signed transport. The error recursion is bounded by exp(Cm)B^{-h}: each stage adds the tree error and a multiplication error, and multiplies preceding errors by at most a fixed constant once all outputs lie in [-1.1,1.1]. The choice of A ensures this range inductively.

Apply the coefficient matrix and its constant bias to these powers. Equation (2) shows that every component L_n, n<=m, has error at most exp(Cm)B^{-h}. This is a uniform m-dependent error bound, not an unjustified componentwise replacement of m by n. All components are bounded by exp(Cm). The degree-zero component is exactly 1.

Parallelizing over the d coordinates produces the shared feature table with width O_d(mB) and depth O_{d,rho}(T(1+log m)^2). For each index nu in Lambda, an affine selector extracts its d coordinate factors, inserting the constant 1 for a zero coordinate degree. Their fixed-d product has width O_d(B), depth O_d(h), and error exp(C_d m)B^{-h}. For d=1 it is simply the selected feature.

Group the terms into the same p-term blocks as before. Carry the shared table, together with a scalar accumulated sum, by signed identity channels. Thus

\[
 \begin{aligned}
 W_2&\le C_d\bigl(mB+pQ+m\bigr)
       \le C(d,\rho)T^{\max\{\lambda,1\}}Q(\log Q)^d,\\
 D_2&\le C(d,\rho)T^{d-\lambda+1}
       +C(d,\rho)T(\log T+\log\log Q)^2.                \tag{9}
 \end{aligned}
\]

Here Q is sufficiently large that the logarithms are positive, and 1+log m is bounded by a fixed multiple of log T+log log Q. The state consistently includes all shared features; constants may alternatively be inserted by affine selectors, so no dimension mismatch is involved. The final block is zero-padded, and every coefficient is included. Equations (1) and (3) give

\[
 E_2\le C(d,\rho,M)Q^{-c(d,\rho)T}.                     \tag{10}
\]

This proves both parameterized constructions rather than citing them as closed obligations.

## 6. Integer rescalings and logarithmic absorption

Return to the public parameters L,N. For kappa>0, put

\[
 \delta=\frac{\alpha}{2(\kappa+\alpha)}>0,
 \qquad Q=\lfloor N^\delta\rfloor.
\]

For all sufficiently large N, log Q>=delta log N/2 and Q<=N^delta. Also (log N)^d<=N^delta once N exceeds a threshold that may depend on kappa,alpha. Consequently, whenever a construction contributes the factor L^kappa to its width,

\[
 L^\kappa Q(\log Q)^d
 \le N^{\kappa/(\kappa+\alpha)+2\delta}=N.               \tag{11}
\]

The multiplicative width constant is independent of kappa,alpha; only the threshold depends on them. For kappa=0 instead use Q=floor(N^{1/2}); the inequality Q(log Q)^d<=C(d)N holds for sufficiently large N without any positive alpha.

If T=floor(L^s), then T is comparable to L^s and (8) or (10) becomes

\[
 C(d,\rho,M)N^{-c(d,\rho,\kappa,\alpha)L^s},             \tag{12}
\]

with the evident kappa=0 convention. Finally N<=exp(L^beta) implies log log Q<=beta log L. All floors preserve the required internal integer domains for sufficiently large parameters.

### Low-width regime

For 0<kappa<=d/2, take

\[
 s=\frac{\kappa+1}{d+2},\qquad
 \lambda=\frac{\kappa(d+2)}{\kappa+1}\in(0,d],
 \qquad T=\lfloor L^s\rfloor
\]

in (7)-(8). Since s lambda=kappa, (11) proves the width bound. Since s(d-lambda+2)=1,

\[
 D_1\le C(d,\rho)\bigl[L+\beta L^{1-s}\log L\bigr]
 \le C(d,\rho,\beta)L.
\]

The last bound is uniform in its multiplicative constant because s>=1/(d+2). For kappa=0, use s=1/(d+2), lambda=0 and the separate Q above; the same depth argument applies. This case includes alpha=0 and N fixed above a sufficiently large constant. The error exponent is s throughout this regime.

### Middle regime

For 1/(d+1)<=kappa<1/d, set

\[
 s=\kappa,\qquad \lambda=d+1-1/\kappa\in[0,1),
 \qquad T=\lfloor L^s\rfloor
\]

in (9)-(10). The width factor is T, hence at most L^kappa, and (11) applies. Also s(d-lambda+1)=1 and s<1. Therefore

\[
 D_2\le C(d,\rho)L+
 C(d,\rho,\beta)L^s(\log L)^2
 \le C(d,\rho,\beta)L.
\]

The threshold for the last inequality may depend on kappa, but its multiplicative constant need not. The error exponent is kappa.

### High-width regime

For 1/d<=kappa<=d, set

\[
 s=\frac{\kappa+1}{d+1},\qquad
 \lambda=\frac{\kappa(d+1)}{\kappa+1}\in[1,d],
 \qquad T=\lfloor L^s\rfloor.
\]

Again s lambda=kappa and s(d-lambda+1)=1. The width is bounded by (11), and

\[
 D_2\le C(d,\rho)L+
 C(d,\rho,\beta)L^s(\log L)^2.
\]

If kappa<d then s<1 and this is at most C(d,rho,beta)L for sufficiently large L. If kappa=d then s=1 and it is at most C(d,rho,beta)L(log L)^2. The error exponent is (kappa+1)/(d+1).

## 7. Assembly and boundary checks

For every d>=1, 1/(d+1)<=d/2, so the first construction covers the entire first public interval. On the overlap below 1/d, kappa is at least (kappa+1)/(d+2) exactly when kappa>=1/(d+1); at equality the exponents coincide. At kappa=1/d, the middle limiting exponent and the high-regime exponent both equal 1/d. The high-regime exponent dominates the first construction wherever both apply.

Choose the sharper applicable construction. This gives precisely the public piecewise tau. The tail and network errors were already combined in (8) and (10). Their constants depend on M only in the error prefactor; the architecture constants do not. The exponent constant can be chosen independent of beta and M. All conclusions hold uniformly over f in A(rho,M).

Dimension one is covered: constants and linear polynomials are exact, and the one-factor tensor product has no multiplication error. Zero coefficients and incomplete summation blocks are handled exactly. No positivity, nonvanishing, coefficient quantization, or extra regularity assumption has been introduced.
