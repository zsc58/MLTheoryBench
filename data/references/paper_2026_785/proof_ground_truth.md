# Reference Proof

## Proof Structure and Obligations

We verify: (1) almost-sure invertibility and a square-integrable common envelope for logarithmic increments; (2) a one-step minorization for each matrix law, giving unique stationarity and uniform geometric mixing; (3) the spherical/additive decomposition and a bounded Poisson-equation solution; (4) the almost-sure and uniform-in-input L1 laws; and (5) convergence of the martingale conditional variances and the Gaussian limit. The specialized abstract centerable-cocycle CLT is not assumed. We give the direct martingale argument suggested by the source.

## 1. Nonvanishing and logarithmic moments

Put m_alpha=min(1,|alpha|)>0 and M_alpha=max(1,|alpha|). Coordinatewise, phi(v)_i is one of v_i and alpha v_i, so

\[
m_\alpha\|v\|\leq\|\phi(v)\|\leq M_\alpha\|v\|.
\]

The map phi is continuous and positively homogeneous for positive scalars, including when alpha is negative. For invertible W and unit s,

\[
\frac{m_\alpha}{\|W^{-1}\|}\leq\|\phi(Ws)\|\leq M_\alpha\|W\|.
\]

Since N(W)>=1, it follows that

\[
|\log\|\phi(Ws)\||\leq H(W):=|\log m_\alpha|+|\log M_\alpha|+\log N(W).
\]

Here and below norms on matrices without a subscript are induced operator norms.

Under (A), let L be a common finite upper bound for the entry densities. We establish the smallest-singular-value bound rather than assume it. Write the columns as C_1,...,C_d and let H_j be the span of the columns other than C_j. If s_min(W)<=epsilon, choose a unit vector u with ||Wu||<=epsilon and an index j with |u_j|>=1/sqrt(d). The identity

\[
C_j=-\sum_{k\ne j}\frac{u_k}{u_j}C_k+\frac{Wu}{u_j}
\]

implies dist(C_j,H_j)<=sqrt(d) epsilon. Thus the small-singular-value event is contained in the union of these d column-distance events.

Condition on all columns other than C_j. Choose measurably a unit normal n_j to H_j and a coordinate index r with |(n_j)_r|>=1/sqrt(d), breaking ties deterministically. Such a normal can be selected by projecting the fixed coordinate basis onto H_j's orthogonal complement and taking the first nonzero projection, normalized. Condition additionally on the entries of C_j other than its r-th entry. On each event specifying r, independence leaves that remaining entry with its original density, bounded by L. The event

\[
|\langle n_j,C_j\rangle|\leq\sqrt d\,\varepsilon
\]

restricts that entry to an interval of length at most 2d epsilon. Consequently

\[
\Pr\{s_{\min}(W)\leq\varepsilon\}\leq 2Ld^2\varepsilon.
\]

Letting epsilon decrease to zero proves almost-sure invertibility. This argument also works for d=1, with the span of the empty collection interpreted as {0}.

Let A_2=E||W||_F^2=sum_{i,j} E W_{ij}^2<infinity. For t>=0, Markov's inequality and the singular-value bound give

\[
\Pr\{\log N(W)>t\}
\leq A_2e^{-2t}+2Ld^2e^{-t}.
\]

The tail-integral formula therefore yields, for every real p>=1,

\[
\mathbb E[(\log N(W))^p]
=\int_0^\infty p t^{p-1}\Pr\{\log N(W)>t\}\,dt<\infty.
\]

Local positivity was not needed for this moment argument; it will be used for minorization.

Under (B), W is invertible and N(W)=max(|eta|,|eta|^{-1}) deterministically. In either case E H(W)^2<infinity. With probability one every W_j is invertible, so the norm lower bound proves that every X_j is nonzero for every nonzero initial vector. All spherical states and logarithms are thus defined on a common probability-one event.

## 2. Minorization and uniform mixing

Write

\[
T_W(s)=\frac{\phi(Ws)}{\|\phi(Ws)\|}.
\]

Under (A), choose r>0 and b>0 so that every entry density is at least b on [-r,r]. On the Frobenius ball B_r={W:||W||_F<r}, the joint density is at least b^{d^2}. Let beta_r be normalized Lebesgue measure on B_r. Singular matrices have beta_r-measure zero, so T_W(s) is defined beta_r-almost surely.

The probability

\[
\theta(A)=\int_{B_r}\mathbf 1_A(T_W(s))\,\beta_r(dW)
\]

does not depend on s. Indeed, if s=R s_* for an orthogonal R, the change of variables W to WR preserves the ball and its normalized Lebesgue measure, and T_W(s)=T_{WR}(s_*). Hence, for every s and every Borel A,

\[
P(s,A)\geq b^{d^2}\operatorname{Leb}(B_r)\theta(A).
\]

Under (B), let beta be Haar probability on O(d), and let the actual density of Q relative to beta be at least b>0. Define

\[
\theta(A)=\int_{O(d)}\mathbf 1_A(T_{\eta R}(s))\,\beta(dR).
\]

Right invariance of the auxiliary Haar law makes this probability independent of s, and the density lower bound gives P(s,A)>=b theta(A). The actual law of Q need not be Haar invariant, and its transition kernel need not be independent of s. This argument also covers eta<0 and d=1.

In either case, decrease the minorization constant if necessary to obtain 0<delta<1 and P(s,.)>=delta theta(.) for all s. Write

\[
P(s,\cdot)=\delta\theta(\cdot)+(1-\delta)R(s,\cdot)
\]

for a Markov kernel R. In the total-variation norm defined by the supremum over measurable functions of absolute value at most one, Markov kernels are contractions. Thus, with rho=1-delta<1,

\[
\|\mu_1P-\mu_2P\|_{\rm TV}\leq\rho\|\mu_1-\mu_2\|_{\rm TV}.
\]

The space of probability measures is complete in this norm. The contraction gives a unique stationary probability nu and

\[
\sup_s\|P^k(s,\cdot)-\nu\|_{\rm TV}\leq2\rho^k.
\]

In particular, for every bounded measurable f with nu(f)=0,

\[
\|P^k f\|_\infty\leq2\rho^k\|f\|_\infty.
\]

## 3. Additive decomposition and the Poisson equation

Define c(s,W)=log||phi(Ws)|| and bar c(s)=E c(s,W). Positive homogeneity gives

\[
S_j=T_{W_j}(S_{j-1}),\qquad
\log\frac{\|X_n\|}{\|x\|}=\sum_{j=1}^n c(S_{j-1},W_j).
\]

The envelope H makes bar c bounded. Continuity of T_W and c(.,W) for invertible W, together with dominated convergence, shows that P maps continuous functions to continuous functions and that bar c is continuous. The stationary integral

\[
\lambda=\int\bar c(s)\,\nu(ds)
\]

is finite. It depends only on the matrix law and alpha, not on the initial input.

Set f=bar c-lambda. Since nu(f)=0, the mixing estimate proves uniform convergence of

\[
\psi=\sum_{k=0}^\infty P^k f.
\]

Each summand is continuous, so psi is continuous and bounded. Uniform convergence permits application of P term by term, giving

\[
\psi-P\psi=\bar c-\lambda.
\]

Let F_j=sigma(W_1,...,W_j), with the initial direction deterministic. Set

\[
D_j=c(S_{j-1},W_j)-\lambda-\psi(S_{j-1})+\psi(S_j),
\qquad M_n=\sum_{j=1}^nD_j.
\]

Independence of W_j from F_{j-1} and the Poisson equation give E[D_j|F_{j-1}]=0. Thus M_n is a square-integrable martingale. Define the common envelope

\[
B(W)=H(W)+|\lambda|+2\|\psi\|_\infty,
\qquad K=\mathbb E B(W)^2<\infty.
\]

Then |D_j|<=B(W_j), E[D_j^2|F_{j-1}]<=K, and martingale orthogonality gives E M_n^2<=nK, uniformly over initial directions. Finally,

\[
\log\frac{\|X_n\|}{\|x\|}-n\lambda
=M_n+\psi(S_0)-\psi(S_n).
\]

This decomposition is the required centering argument. No assertion that subtracting a constant from a full semigroup cocycle preserves its cocycle identity is needed.

## 4. Almost-sure and uniform L1 convergence

We use the elementary L2 martingale maximal inequality: a square-integrable martingale starting at zero satisfies E[max_{j<=m}|M_j|^2]<=4 E|M_m|^2. Applied at m=2^k, it gives, for epsilon>0,

\[
\Pr\left\{\max_{j\leq2^k}|M_j|>\varepsilon2^k\right\}
\leq\frac{4K}{\varepsilon^2 2^k}.
\]

These probabilities are summable. Borel-Cantelli and comparison with adjacent powers of two imply M_n/n->0 almost surely for every fixed initial direction. The bounded endpoint term and the fixed number log||x|| then yield

\[
\frac1n\log\|X_n\|\longrightarrow\lambda
\quad\text{almost surely for every fixed }x\ne0.
\]

Moreover, Cauchy-Schwarz gives the uniform bound

\[
\sup_{x\ne0}\mathbb E\left|
\frac1n\log\frac{\|X_n\|}{\|x\|}-\lambda
\right|
\leq\sqrt{\frac Kn}+\frac{2\|\psi\|_\infty}{n}\longrightarrow0.
\]

Positive homogeneity makes the normalized expression depend on x only through its direction. The displayed supremum is outside the expectation, exactly as required; no simultaneous almost-sure assertion over all inputs is used.

## 5. Conditional variance and Gaussian fluctuations

For a unit s define

\[
v(s)=\mathbb E\left[
\big(c(s,W)-\lambda-\psi(s)+\psi(T_W(s))\big)^2
\right].
\]

This is a measurable function with 0<=v(s)<=K, and

\[
\mathbb E[D_j^2\mid F_{j-1}]=v(S_{j-1}).
\]

Put gamma^2=nu(v), which is finite, nonnegative, and independent of the initial input. Let h=v-gamma^2. For 0<=i<j, the Markov property and uniform mixing give

\[
\left|\mathbb E[h(S_i)h(S_j)]\right|
=\left|\mathbb E[h(S_i)(P^{j-i}h)(S_i)]\right|
\leq2\|h\|_\infty^2\rho^{j-i}.
\]

The diagonal terms are bounded by ||h||_infinity^2. Summing these estimates shows, from every initial direction,

\[
\mathbb E\left[
\left(\frac1n\sum_{j=1}^n v(S_{j-1})-\gamma^2\right)^2
\right]\longrightarrow0.
\]

For completeness, we now derive the Gaussian limit directly rather than invoke the nonstandard cocycle theorem. Fix a real t and write a=t^2/2. Conditional Taylor expansion, using the zero conditional mean, gives

\[
\mathbb E[e^{itD_j/\sqrt n}\mid F_{j-1}]
=1-\frac{a}{n}v(S_{j-1})+r_{n,j}.
\]

The elementary Taylor remainder bound

\[
|e^{iu}-1-iu+u^2/2|\leq C u^2\min(|u|,1)
\]

implies

\[
|r_{n,j}|\leq\frac{\varepsilon_n}{n},\qquad
\varepsilon_n=Ct^2\mathbb E\left[
B(W)^2\min\left(\frac{|t|B(W)}{\sqrt n},1\right)
\right]\longrightarrow0.
\]

Here the conditional bound is deterministic because W_j is independent of the past, and convergence follows by dominated convergence from E B^2<infinity. This bound also verifies the usual conditional Lindeberg requirement, since its sum is bounded by E[B^2 1_{B>epsilon sqrt(n)}], tending to zero.

Let

\[
V_k=\sum_{j=1}^k v(S_{j-1}),\qquad
Z_{n,k}=\exp\left(\frac{itM_k}{\sqrt n}+\frac{aV_k}{n}\right),
\quad 0\leq k\leq n.
\]

Since V_k<=nK, |Z_{n,k}|<=exp(aK). Conditional on F_{k-1}, the multiplier for Z_{n,k-1} has expectation

\[
e^{a v(S_{k-1})/n}
\left(1-\frac{a v(S_{k-1})}{n}+r_{n,k}\right)
=1+O(n^{-2})+O(\varepsilon_n/n),
\]

uniformly in k and the past. Telescoping expectations therefore yields E Z_{n,n}->1. On the other hand V_n/n->gamma^2 in L2, and these averages are bounded. Thus

\[
\mathbb E Z_{n,n}
-e^{a\gamma^2}\mathbb E e^{itM_n/\sqrt n}\longrightarrow0.
\]

Consequently

\[
\mathbb E e^{itM_n/\sqrt n}\longrightarrow
\exp(-t^2\gamma^2/2).
\]

The characteristic-function continuity theorem gives M_n/sqrt(n) converging in distribution to N(0,gamma^2). This includes gamma^2=0. Finally,

\[
\frac{\log\|X_n\|-n\lambda}{\sqrt n}
=\frac{M_n}{\sqrt n}
+\frac{\log\|x\|+\psi(S_0)-\psi(S_n)}{\sqrt n},
\]

and the second term tends to zero for every fixed nonzero x. This proves the stated CLT and completes all obligations.
