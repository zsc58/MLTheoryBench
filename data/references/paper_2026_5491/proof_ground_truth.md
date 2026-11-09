# Reference Proof

## Proof Structure and Obligations

1. Check the supplied physical primitive and the finite independent-attempt interpretation; prove both escape estimates with a uniform relative remainder.
2. Recover the threshold-binomial probability from electron independence and verify the interior probability domain.
3. Obtain the signed-bit perturbation and its factorized conditional characteristic function.
4. Derive the exact affine mean from the offset-binary identity.
5. Derive the exact conditional variance.
6. Compute the MSB variance fraction and the third-absolute-moment Lyapunov ratio, including its positive limit.
7. Separately exclude a Gaussian limit. Failure of the Lyapunov condition alone does not close this obligation.

The WKB transmission formula is a supplied model primitive, not an additional theorem the solver must derive. All expectations involving bit indicators below are conditional on the displayed stored weight. No assumption concerning independence between different precisions is needed.

## Complete Proof

### 1. Escape probability and both estimates

The given inequalities on the physical parameters imply $\alpha>0$ and $0<q<1$. The number of attempts is the positive integer $n=f\tau$. Independence and forward-only escape give
\[
P_{\rm esc}=1-(1-q)^n.
\]
For a direct uniform remainder estimate, let $I_1,\ldots,I_n$ be the independent Bernoulli$(q)$ attempt-success indicators and let $M=\sum_{r=1}^n I_r$. For every nonnegative integer $M$,
\[
0\le M-\mathbf 1_{\{M\ge1\}}\le\frac{M(M-1)}2.
\]
Indeed, the expression on the left is zero for $M=0,1$, and for $M\ge2$ the upper inequality reduces to $M-1\le M(M-1)/2$. Taking expectations and using independence for pairs of attempts gives
\[
0\le nq-P_{\rm esc}\le {n\choose2}q^2\le\frac{(nq)^2}{2}.
\]
Thus $P_{\rm esc}\le nq$. Dividing the same estimate by $nq>0$ yields
\[
\left|\frac{P_{\rm esc}}{nq}-1\right|\le\frac{nq}{2}.
\]
This proves $P_{\rm esc}=nq(1+O(nq))$ as $nq\to0$, with an absolute implicit constant independent of $n$ and $q$. The case $n=1$ is included and gives equality $P_{\rm esc}=q$.

### 2. Threshold probability and domains

Different electrons have independent attempt outcomes and the same escape probability. Their escape indicators are therefore independent Bernoulli$(P_{\rm esc})$ variables. For exactly $j$ escapes, each specified set of $j$ electrons has probability $P_{\rm esc}^{j}(1-P_{\rm esc})^{N_e-j}$, and there are ${N_e\choose j}$ such sets. Consequently the probability of at least $X_{\rm thr}$ escapes is
\[
p=\sum_{j=X_{\rm thr}}^{N_e}{N_e\choose j}P_{\rm esc}^{j}(1-P_{\rm esc})^{N_e-j}.
\]
This also verifies the probabilistic interpretation of the supplied formula. Because $0<P_{\rm esc}<1$ and $1\le X_{\rm thr}\le N_e$, the event that all electrons escape has positive probability and implies a flip, while the event that none escape has positive probability and implies no flip. Hence $0<p<1$.

### 3. Perturbation and characteristic function

Fix a stored weight $w$. Flipping its $k$th bit changes that bit from $b_k(w)$ to $1-b_k(w)$, so the decoded increment is
\[
\delta\bigl(1-2b_k(w)\bigr)2^k=\delta s_k(w)2^k.
\]
Since decoding is affine in the bits, simultaneous flips add these increments. Thus, with $a_k=\delta s_k(w)2^k$,
\[
\Delta w=\sum_{k=0}^{b-1}a_k\xi_k.
\]
Conditional on $w$, the coefficients are deterministic and the indicators are independent. Each factor satisfies
\[
\mathbb E[e^{it a_k\xi_k}\mid w]=(1-p)+p e^{it a_k}.
\]
Multiplying over the independent indicators proves, for every real $t$,
\[
\phi_{\Delta w\mid w}(t)=\prod_{k=0}^{b-1}\left[1-p+p\exp\!\left(it\,s_k(w)2^k\delta\right)\right].
\]

### 4. Exact conditional mean

By linearity of expectation,
\[
\mathbb E[\Delta w\mid w]=p\delta\sum_{k=0}^{b-1}s_k(w)2^k.
\]
The offset-binary identities give
\[
\begin{aligned}
\delta\sum_{k=0}^{b-1}s_k(w)2^k
&=\delta\sum_{k=0}^{b-1}2^k-2\delta\sum_{k=0}^{b-1}b_k(w)2^k\\
&=\delta(2^b-1)-2(w+W)\\
&=-2w-\delta,
\end{aligned}
\]
where the final equality uses $\delta2^b=2W$. Therefore
\[
\mathbb E[\Delta w\mid w]=-2pw-p\delta.
\]

### 5. Exact conditional variance

Conditional independence and $s_k(w)^2=1$ imply
\[
\begin{aligned}
\operatorname{Var}(\Delta w\mid w)
&=\sum_{k=0}^{b-1}a_k^2\operatorname{Var}(\xi_k\mid w)\\
&=p(1-p)\delta^2\sum_{k=0}^{b-1}4^k\\
&=p(1-p)\delta^2\frac{4^b-1}{3}.
\end{aligned}
\]
In particular, this variance is independent of the stored bit pattern and is strictly positive in the stated domain.

### 6. MSB fraction and Lyapunov ratio

Now keep $W$ and $p\in(0,1)$ fixed and permit any sequence of representable values $w_b$. The centered contributions are
\[
Y_{b,k}=\delta_b s_k(w_b)2^k(\xi_{b,k}-p).
\]
Their variances are $p(1-p)\delta_b^2 4^k$. Thus
\[
\frac{\operatorname{Var}(Y_{b,b-1}\mid w_b)}{\sigma_b^2}
=\frac{4^{b-1}}{\sum_{k=0}^{b-1}4^k}
=\frac{3\,4^{b-1}}{4^b-1}
\longrightarrow\frac34.
\]
For a Bernoulli$(p)$ variable $\xi$,
\[
\mathbb E|\xi-p|^3=(1-p)p^3+p(1-p)^3
=p(1-p)\bigl(p^2+(1-p)^2\bigr).
\]
It follows that
\[
\mathbb E[|Y_{b,k}|^3\mid w_b]
=\delta_b^3 8^k p(1-p)\bigl(p^2+(1-p)^2\bigr),
\]
and hence
\[
L_b=\frac{p^2+(1-p)^2}{\sqrt{p(1-p)}}
\frac{\sum_{k=0}^{b-1}8^k}{\left(\sum_{k=0}^{b-1}4^k\right)^{3/2}}.
\]
Using the two geometric sums,
\[
\frac{\sum_{k=0}^{b-1}8^k}{\left(\sum_{k=0}^{b-1}4^k\right)^{3/2}}
=\frac{3^{3/2}}7\frac{8^b-1}{(4^b-1)^{3/2}}
\longrightarrow\frac{3^{3/2}}7.
\]
Therefore
\[
\lim_{b\to\infty}L_b
=\frac{3^{3/2}}7\frac{p^2+(1-p)^2}{\sqrt{p(1-p)}}\in(0,\infty).
\]
This holds also at $p=1/2$. As $p\downarrow0$, the limiting expression is asymptotic to $(3^{3/2}/7)p^{-1/2}$, recovering the source's small-flip scaling. Both the variance fraction and $L_b$ are independent of $w_b$.

### 7. Local completion of the non-Gaussianity argument

A nonvanishing Lyapunov ratio rules out using that sufficient central-limit criterion; it is not, by itself, a proof that a Gaussian limit is impossible. The actual non-Gaussianity conclusion follows here from an elementary bound using the same centered bit representation and variance already established.

Since $|\xi_{b,k}-p|\le1$, every realization satisfies
\[
\left|\Delta w_b-\mathbb E[\Delta w_b\mid w_b]\right|
\le\delta_b\sum_{k=0}^{b-1}2^k
=\delta_b(2^b-1).
\]
Consequently
\[
|Z_b|
\le\frac{\sqrt3}{\sqrt{p(1-p)}}\frac{2^b-1}{\sqrt{4^b-1}}
<\frac{\sqrt3}{\sqrt{p(1-p)}}=:C_p.
\]
The finite constant $C_p$ depends only on the fixed $p$, not on $b$, $W$, or the stored bit pattern. Therefore the conditional distribution function of every $Z_b$ equals one at $C_p$. The standard normal distribution function $\Phi$ is continuous and satisfies $\Phi(C_p)<1$, because its density is positive beyond every finite point. Convergence in distribution to $\mathcal N(0,1)$ would require convergence of these distribution functions at $C_p$, which is impossible. This proves the claimed failure of a Gaussian limit for every sequence $w_b$.

The added argument repairs the omitted implication in the source without replacing any of its characteristic-function, mean, variance, MSB, or Lyapunov calculations.

## Boundary and Completeness Check

The finite calculations include $b=1$, $n=1$, $N_e=1$, both allowed threshold endpoints, and every stored grid endpoint. The exact mean and variance identities also remain algebraically valid at $p=0$ or $p=1$, but the standardized quantities are not defined there and those endpoints are excluded from the precision-limit claim. No restriction $p<1/2$ from the separate compensation analysis is needed. All seven obligations above are closed, and no nonstandard external proof dependency remains.
