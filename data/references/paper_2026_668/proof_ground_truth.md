# Reference Proof

## Proof Structure and Obligations

The proof must establish: (i) well-defined, feasible online actions; (ii) the sign of the Stein solution's derivative for convex h; (iii) the exact one-round identity and the displayed remainder constants, including zero terminal smoothing; (iv) pathwise telescoping for history-dependent scales; and (v) the universal Boolean lower bound, including its strict inequality. All five obligations are closed below.

The external facts used are standard Gaussian Stein identities, solution regularity and Stein factors, and the standard Rademacher Wasserstein estimate. Their relevant statements and application hypotheses are given explicitly. No paper-specific theorem is used as an unproved substitute for the one-round argument, and Cover's characterization is not required.

## Standard Gaussian Facts

For a real-valued 1-Lipschitz function h, mu in R and sigma>0, the bounded solution f=f_{mu,sigma,h} of the stated Stein equation is C^1 and f' is Lipschitz. The standard Stein estimates are
\[
|f(x)|\le1,\qquad |f'(x)|\le\sqrt{2/\pi}/\sigma,\qquad
\operatorname{Lip}(f')\le2/\sigma^2.
\]
The source states the last bound as an essential bound on f'' together with Lipschitz regularity of f'; absolute continuity of f' converts it into the displayed global Lipschitz estimate. Continuity of f and f' converts their essential bounds into pointwise bounds.

We also use Gaussian integration by parts: if V is normal with mean m and positive variance v, and q is absolutely continuous with integrable derivative, then
\[
\mathbb E[(V-m)q(V)]=v\mathbb E[q'(V)].
\]
Every application below has bounded q=f and bounded q'=f', so its integrability hypotheses hold.

The standard solution representation is
\[
f_{\mu,\sigma,h}(x)=-\int_0^\infty e^{-\tau}\mathbb E_Z h'\!\left(\mu+e^{-\tau}(x-\mu)+\sigma\sqrt{1-e^{-2\tau}}Z\right)\,d\tau.
\]
The derivative of a Lipschitz function is bounded almost everywhere. For tau>0 the inner Gaussian is nondegenerate, so changing the derivative on a null set has no effect. The integral is absolutely convergent because its integrand in absolute value is bounded by e^{-tau}.

## Convexity and Feasibility

For convex 1-Lipschitz h, choose its right derivative as a nondecreasing, everywhere-defined representative of h', taking values in [-1,1]. For each tau>0, the argument of h' in the representation increases with x. Consequently the inner expectation is nondecreasing in x. The negative integral is therefore nonincreasing in x. Since f is C^1,
\[
f_{\mu,\sigma,h}'(x)\le0\quad\text{for every }x.
\]
This proves the required convexity consequence, rather than assuming it.

All scales rho_{t-1} used as Stein standard deviations are positive. For any realized history, the action is the expectation of a function bounded pointwise by 1 in absolute value, so |x_t|<=1, including when rho_t=0. The formula uses only the fixed h, the initial scale and the previous gradients through s_{t-1}, rho_{t-1} and rho_t. It is therefore an online action. The Gaussian integral is a deterministic operation, not an additional observation or random action.

Since |h(y)|<=|h(0)|+|y|, all Gaussian potential expectations below are finite for every realized real gradient history and every admissible scale.

## One-Round Identity and Error Bound

Fix an arbitrary realized gradient sequence and its realized scales. During the following Gaussian expectations these quantities are constants. On round t write
\[
s=s_{t-1},\quad g=g_t,\quad \sigma=\rho_{t-1}>0,\quad r=\rho_t\ge0,\quad c=\sigma^2-r^2\ge0,
\]
\[
f=f_{s,\sigma,h},\qquad X=s+rZ,\qquad
D_t=\mathbb E_Z h(X+g)-\mathbb E_Z h(s+\sigma Z).
\]
Evaluating the Stein equation at X+g gives
\[
D_t=\sigma^2\mathbb E f'(X+g)-\mathbb E[(rZ+g)f(X+g)].
\]
If r>0, Gaussian integration by parts gives
\[
\mathbb E[rZf(X+g)]=r^2\mathbb E f'(X+g).
\]
If r=0, both sides of this last identity are zero directly; no nondegenerate Gaussian lemma is needed. Thus in all cases
\[
D_t=c\mathbb E f'(X+g)-g\mathbb E f(X+g).
\]
For completeness, evaluating the same equation at X also gives the variance-change identity
\[
\mathbb E h(X)-\mathbb E h(s+\sigma Z)=c\mathbb E f'(X).
\]

Define the pointwise remainders
\[
A(y,g)=f'(y+g)-f'(y),\qquad
B(y,g)=f(y+g)-f(y)-gf'(y).
\]
The global Lipschitz estimate on f' gives, for every real y and g,
\[
|A(y,g)|\le\frac{2|g|}{\sigma^2}.
\]
The fundamental theorem of calculus gives
\[
B(y,g)=g\int_0^1\bigl(f'(y+\lambda g)-f'(y)\bigr)\,d\lambda,
\]
so
\[
|B(y,g)|\le\frac{2g^2}{\sigma^2}\int_0^1\lambda\,d\lambda=\frac{g^2}{\sigma^2}.
\]
These statements hold pointwise, including g=0 and deterministic X, and require no pointwise second derivative.

Substituting the definitions of A and B into the one-round identity yields the exact decomposition
\[
D_t=-g\mathbb E f(X)+(c-g^2)\mathbb E f'(X)+c\mathbb E A(X,g)-g\mathbb E B(X,g).
\]
By definition, E f(X)=x_t. Since f'<=0 and |f'|<=sqrt(2/pi)/sigma,
\[
(c-g^2)\mathbb E f'(X)\le\frac{\sqrt{2/\pi}}{\sigma}\max\{g^2-c,0\}.
\]
Indeed, the term is nonpositive when c>=g^2, and otherwise the absolute derivative bound applies. The two remainder terms satisfy
\[
c\mathbb E A(X,g)-g\mathbb E B(X,g)
\le\frac{2c|g|+|g|^3}{\sigma^2}.
\]
Consequently,
\[
D_t\le-g_tx_t+
\frac{\sqrt{2/\pi}\max\{g_t^2-c_t,0\}}{\rho_{t-1}}
+\frac{2c_t|g_t|+|g_t|^3}{\rho_{t-1}^2}.
\]
No bound on |g_t| was used.

## Telescoping

For this fixed realized history define
\[
H_t=\mathbb E_Z h(s_t+\rho_tZ),\qquad t=0,\ldots,T.
\]
Then D_t=H_t-H_{t-1}. The preceding inequality gives g_t x_t<=H_{t-1}-H_t plus the displayed error. Summing yields
\[
\operatorname{Loss}_T\le-\mathbb E_Z h(s_T+\rho_TZ)+\mathbb E_Z h(\rho_0Z)
+\sum_{t=1}^T\left[
\frac{\sqrt{2/\pi}\max\{g_t^2-c_t,0\}}{\rho_{t-1}}
+\frac{2c_t|g_t|+|g_t|^3}{\rho_{t-1}^2}
\right].
\]
This is a pathwise calculation: history dependence of the scales does not change the telescoping identity, and no expectation over gradient sequences is being taken. It also covers T=1, c_t=0, g_t=0, and rho_T=0.

## Boolean Lower Bound

Fix any deterministic online algorithm a_t:R^{t-1}->[-1,1] and any real-valued 1-Lipschitz h, without a convexity assumption. Let G_1,...,G_T be independent uniform signs on the finite space {-1,1}^T, and put S_T=sum_t G_t. Each a_t(G_1,...,G_{t-1}) is a bounded function on a finite probability space. Independence and zero mean give
\[
\mathbb E\bigl[G_ta_t(G_1,\ldots,G_{t-1})\mid G_1,\ldots,G_{t-1}\bigr]=0.
\]
Therefore
\[
\mathbb E\left[\sum_{t=1}^T G_ta_t(G_1,\ldots,G_{t-1})+h(S_T)\right]=\mathbb E h(S_T).
\]
The standard Rademacher Wasserstein estimate states that for every positive integer n, independent uniform signs U_1,...,U_n, and real-valued 1-Lipschitz k,
\[
\left|\mathbb E k\left(\sum_{i=1}^nU_i\right)-\mathbb E_Z k(\sqrt n Z)\right|\le K,
\qquad K=1+\sqrt{2/\pi}.
\]
Here n=T, k=h and U_i=G_i satisfy all its hypotheses. Both expectations are finite by Lipschitz growth. It follows that
\[
\mathbb E\left[\sum_{t=1}^T G_ta_t(G_1,\ldots,G_{t-1})+h(S_T)\right]
\ge\mathbb E_Z h(\sqrt T Z)-K.
\]
At least one point of the finite sign space has value at least its average. For that sequence g_1,...,g_T,
\[
\operatorname{Loss}_T\ge-h\left(\sum_{t=1}^Tg_t\right)+\mathbb E_Zh(\sqrt T Z)-K.
\]
Taking C=K+1 gives the required strict inequality. This C is independent of T, h and the algorithm. The selected Boolean sequence is an admissible adversary even if chosen in advance.

All theorem-critical obligations listed at the start are closed.
