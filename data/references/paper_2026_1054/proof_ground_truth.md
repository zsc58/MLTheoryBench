# Reference Proof

## Proof Structure

Use the complementary residual-variance functional and compare three averages: empirical ratios, empirical numerators divided by population variances, and ideal residual-variance ratios. Establish the ideal iid fluctuation, conditional denominator concentration and a simultaneous good-denominator event, numerator fluctuation including graph and tie-randomization replacement, and conditional-moment bias controlled by neighbour radii. The proof below explicitly derives all paper-specific estimates.

## Complete Proof

Let B>0 satisfy |k_Y(u,y)|≤B for all u,y. Write
\[
v(y)=V_Y(y),\qquad s_y(x)=m_{2,y}(x)-m_{1,y}(x)^2,\qquad e(y)=\int s_y(x)\,dP_X(x),
\]
and
\[
q=1-D(Y,X)=\int\frac{e(y)}{v(y)}\,dP_Y(y).
\]
These quantities use an independent population pair: the covariate in e(y) is integrated over P_X, not evaluated at the held-out X_i.

Continuity, full support, and nonconstant sections imply v(y)>0 for every y. Indeed, a continuous section equal to a constant P_Y-almost surely must equal it everywhere: any point of disagreement has an open neighbourhood of positive probability. The law of total variance, valid for each bounded section, gives
\[
v(y)=e(y)+\operatorname{Var}_X(m_{1,y}(X)).
\]
Consequently 0≤e(y)/v(y)≤1, and D is a deterministic scalar. Set
\[
M_p=\int v(y)^{-p}\,dP_Y(y),\qquad p=1,2,3.
\]
The assumption gives M_3<∞, and Holder's inequality gives M_p≤M_3^{p/3} for p=1,2.

For each i let Z_i=(X_i,Y_i), m=n-1, and abbreviate
\[
A_i=E_{n,i}^{K\text{-}NN},\quad W_i=V_{n,i}^{K\text{-}NN},\quad v_i=v(Y_i),\quad e_i=e(Y_i).
\]
Define
\[
Q_n=\frac1n\sum_i\frac{A_i}{W_i},\quad
Q'_n=\frac1n\sum_i\frac{A_i}{v_i},\quad
Q^0_n=\frac1n\sum_i\frac{e_i}{v_i},
\]
using the public zero-ratio convention for Q_n. If W_i=0, all the leave-one-out section values coincide, so every pairwise difference in A_i is zero. Thus the convention only extends a 0/0 expression.

All conditional estimates below hold for almost every held-out Z_i, with constants independent of its value, n, and the admissible deterministic K. The remaining observations are iid conditional on Z_i, and their neighbour selections use only their covariates and independent auxiliary randomization.

### 1. Ideal iid averaging

The variables e(Y_i)/v(Y_i) are iid, lie in [0,1], and have mean q. Hoeffding's inequality states that independent variables in [0,1] satisfy
\[
P\left(\left|n^{-1}\sum_i H_i-EH_i\right|>t\right)≤2e^{-2nt^2}.
\]
Its hypotheses therefore hold here. Integrating this tail yields
\[
E|Q^0_n-q|≤C n^{-1/2}.
\]
In particular Q^0_n-q=O_P(n^{-1/2}).

### 2. Denominator concentration and simultaneous stability

Conditional on Z_i, put z_j=k_Y(Y_j,Y_i), j≠i. These are iid, bounded in absolute value by B, and have variance v_i. Their empirical variance W_i has exact conditional mean
\[
E[W_i\mid Z_i]=(1-1/m)v_i.
\]
Changing one z_j changes the mean of squares by at most B^2/m and the square of the mean by at most 4B^2/m. Thus a bound 6B^2/m is valid for each coordinate sensitivity.

McDiarmid's inequality for a function of independent inputs with coordinate sensitivities c_j gives the two-sided bound
\[
P(|F-EF|>t)≤2\exp\left(-\frac{2t^2}{\sum_j c_j^2}\right).
\]
The independence and sensitivities just verified imply
\[
P(|W_i-E[W_i\mid Z_i]|>t\mid Z_i)≤2e^{-cmt^2/B^4}.
\]
Tail integration and the exact bias give
\[
E[|W_i-v_i|\mid Z_i]≤CB^2m^{-1/2}+v_i/m.
\]
Hence
\[
E\frac{|W_i-v_i|}{v_i^2}≤CB^2m^{-1/2}M_2+m^{-1}M_1=O(n^{-1/2}).
\]

Let
\[
\Omega_n=\bigcap_i\{|W_i-v_i|≤v_i/2\}.
\]
For n≥4, m≥3, and a deviation exceeding v_i/2 entails a deviation from the conditional mean exceeding v_i/6. A union bound and the conditional concentration estimate therefore give
\[
P(\Omega_n^c)≤2n\,E\exp(-cmv(Y)^2/B^4).
\]
The elementary estimate e^{-x}≤C x^{-3/2}, x>0, implies
\[
P(\Omega_n^c)≤C n m^{-3/2}M_3=O(n^{-1/2}).
\]
On Ω_n the correct implication is W_i≥v_i/2. Also 0≤A_i≤2B^2 directly from its definition. Therefore
\[
|Q_n-Q'_n|\mathbf1_{\Omega_n}≤\frac{4B^2}{n}\sum_i\frac{|W_i-v_i|}{v_i^2}.
\]
The right-hand side has expectation O(n^{-1/2}). No expectation bound on an unbounded reciprocal empirical variance, and no claimed rate for the ratio on Ω_n^c, is needed.

### 3. Numerator fluctuation, including ties

Uniform row-wise tie breaking can be realized by independent random priorities, one independent priority ordering for each centre, independent of the observations. Order candidates lexicographically by distance and priority. Restricting the same priorities after a deletion realizes uniform tie breaking on the smaller candidate set. This is a private coupling used to bound a statistic with the public randomization law.

First relate full and deleted graph degrees. Deleting vertex i preserves a centre's full K-neighbour set unless that set contains i. In the latter case it introduces exactly one replacement edge. There are at most δ_i≤C_XK such centres. Thus every vertex in the deleted graph has indegree at most
\[
\delta_\ell+\delta_i≤2C_XK.
\]
This reasoning uses only the stated full-sample assumption, not an additional deleted-graph hypothesis. The same bound holds almost surely for iid observation replacements and fresh independent priority inputs, because those inputs have the original sampling law. Conditioning on Z_i preserves these almost-sure statements for almost every Z_i.

Conditional on Z_i, A_i is a function of the m independent remaining observations and independent row-priority inputs. Replacing observation ℓ changes its entire centre row, containing K terms. For any other centre, the ordering of candidates other than ℓ is unchanged. Its selected terms can change only if ℓ is selected before or after replacement. At most 4C_XK such centres occur, by the two deleted-graph indegree bounds. Each such row changes at most one selected term, including a possible change in its response value. Every squared difference belongs to [0,4B^2]. Dividing by 2Km therefore gives
\[
|A_i-A_i^{(\ell)}|≤C/m.
\]
Replacing one centre's priority ordering changes only that centre's K outgoing terms, so its influence is also at most 2B^2/m. Priorities of the omitted centre have zero influence.

Efron-Stein states that a square-integrable function F of independent inputs satisfies
\[
\operatorname{Var}(F)≤\frac12\sum_a E[(F-F^{(a)})^2],
\]
where input a is replaced by an independent copy. Here A_i is bounded, the inputs are conditionally independent, there are O(m) nonzero influences, and each is O(m^{-1}). Consequently
\[
\operatorname{Var}(A_i\mid Z_i)≤C/m.
\]
Cauchy-Schwarz conditionally and integration yield
\[
E\frac{|A_i-E[A_i\mid Z_i]|}{v_i}≤C m^{-1/2}M_1=O(n^{-1/2}).
\]
No independence between different evaluation-index numerators is asserted or required.

### 4. Conditional pairwise bias

Fix the held-out response y. Given the covariates and the auxiliary priorities, responses at distinct remaining indices are conditionally independent. Thus for an edge j→k,
\[
E[(k_Y(Y_j,y)-k_Y(Y_k,y))^2\mid X_j=x,X_k=x']
=m_{2,y}(x)+m_{2,y}(x')-2m_{1,y}(x)m_{1,y}(x').
\]
Its difference from 2s_y(x) is
\[
\Delta_y(x,x')=m_{2,y}(x')-m_{2,y}(x)
-2m_{1,y}(x)(m_{1,y}(x')-m_{1,y}(x)).
\]
Since |m_{1,y}(x)|≤B, the Holder assumptions give the positive upper bound
\[
|\Delta_y(x,x')|≤L(1+2B)d_X(x,x')^\beta.
\]
For each centre j≠i let
\[
R_j^{\backslash i}=\max_{k\in N_j^{\backslash i}}d_X(X_j,X_k).
\]
Keeping the exact numerator normalization, the conditional expectation of A_i differs from m^{-1}∑_{j≠i}s_y(X_j) by at most
\[
\frac{L(1+2B)}{2Km}\sum_{j\ne i}\sum_{k\in N_j^{\backslash i}}d_X(X_j,X_k)^\beta
≤\frac{C}{m}\sum_{j\ne i}(R_j^{\backslash i})^\beta.
\]
Averaging over the remaining covariates gives E[m^{-1}∑s_y(X_j)]=e(y). Accordingly
\[
|E[A_i\mid Z_i]-e_i|≤C E[(R_j^{\backslash i})^\beta].
\]
The bound is uniform in y. The neighbour distance is measured from X_j, not from X_i.

### 5. Radius moments with the corrected mass domain

The quantifier over every T means the local-mass bound holds at every centre x. Set r_0=c_0^{-1/d}. The condition at r=r_0 gives
\[
P_X(d_X(X,x)≤r_0)=1
\]
for every centre x. Therefore a Kth-neighbour radius R formed from M independent candidate points is at most r_0 almost surely, conditional on the centre.

If 2K>M, then
\[
E[R^\beta\mid x]≤r_0^\beta≤\left(\frac{2K}{c_0M}\right)^{\beta/d}.
\]
If 2K≤M, let
\[
r_*=(2K/(c_0M))^{1/d}≤r_0.
\]
For r∈[r_*,r_0], the number N_r of candidates in the closed ball is binomial with mean μ_r≥Mc_0r^d≥2K. The multiplicative binomial Chernoff inequality
\[
P(N≤(1-\eta)\mu)≤e^{-\eta^2\mu/2},\qquad 0<\eta<1,
\]
with η=1/2 gives
\[
P(R>r\mid x)=P(N_r<K\mid x)≤e^{-Mc_0r^d/8}.
\]
Using the nonnegative tail-integral identity,
\[
\begin{aligned}
E[R^\beta\mid x]
&=\int_0^{r_0}\beta r^{\beta-1}P(R>r\mid x)\,dr\\
&≤r_*^\beta+\beta r_*^\beta\int_1^{r_0/r_*}u^{\beta-1}e^{-Ku^d/4}\,du\\
&≤C r_*^\beta≤C(K/M)^{\beta/d}.
\end{aligned}
\]
The last numerical integral is uniformly finite for K≥1. Only this upper-bound integral is extended to infinity; the mass assertion is never used beyond its admissible domain. No conditioning on a sample-maximum event is used.

For the actual deleted graph M=n-2, so M≥n/2 for n≥4. Both cases yield
\[
E[(R_j^{\backslash i})^\beta]≤C(K/n)^{\beta/d}
≤C\left[(K/n)^{\beta/d}+n^{-2}(\log n)^{\beta/\alpha}\right].
\]
This stronger estimate is a consequence of the exact uniform-in-centre mass contract. The exponential-tail assumption and the stated nonnegative tail term are retained in the task; no assumption or conclusion is removed. Constants can depend on the fixed displayed parameters and B, but not on n, K, or the evaluation point.

Combining bias and fluctuation, with
\[
a_n=n^{-1/2}+(K/n)^{\beta/d}+n^{-2}(\log n)^{\beta/\alpha},
\]
gives
\[
E|Q'_n-Q^0_n|≤\frac1n\sum_i E\frac{|A_i-e_i|}{v_i}≤C a_n.
\]

### 6. Probability conclusion

Let
\[
H_n=\frac{4B^2}{n}\sum_i\frac{|W_i-v_i|}{v_i^2}.
\]
On Ω_n,
\[
|Q_n-q|≤|Q^0_n-q|+|Q'_n-Q^0_n|+H_n.
\]
The expectation of the right-hand side is at most Ca_n, and P(Ω_n^c)=O(n^{-1/2})→0. Markov's inequality therefore gives, for every t>0,
\[
P(|Q_n-q|>t a_n)≤C/t+O(n^{-1/2}).
\]
This is exactly Q_n-q=O_P(a_n), uniformly over the stated deterministic admissible K sequences with fixed assumption constants. Finally,
\[
\widehat D^{K\text{-}NN}(Y,X)-D(Y,X)=-(Q_n-q),
\]
which proves the unchanged flagship rate.

## Obligation Audit

All theorem-critical obligations are explicitly closed: population definition and positivity; integrated residual rather than pointwise conditional variance; iid ideal averaging; conditional empirical-variance sensitivity and exact bias; weighted inverse-moment estimates; simultaneous denominator stability; deleted-graph degree and old/new replacement counts; auxiliary tie-randomization variance; exact pairwise bias normalization; admissible-radius counting including large K; and O_P conversion. Hoeffding, McDiarmid, Efron-Stein, binomial Chernoff, total variance, tail integration, and Markov are used with their relevant statements and verified hypotheses. No specialized or paper-specific estimate is assumed without derivation.
