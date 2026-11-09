# Reference Proof

## Source Contract and Local Repair

The source surrogate uses the complementary weight \(S-D(y',y)\) and the inner relative-score sum over a second label vector. Both are essential to the function being evaluated. The positive-parameter branch is retained with the defining sign \((u^{-\tau}-1)/\tau\). No continuity at zero or consistency theorem is used.

A two-bit cost table is equivalent to the source's four-coefficient representation. Indeed, for a table \(d(a,b)\), define
\[
\gamma^1=\tfrac14\sum_{a,b}ab\,d(a,b),\quad
\gamma^2=\tfrac14\sum_{a,b}b\,d(a,b),\quad
\gamma^3=\tfrac14\sum_{a,b}a\,d(a,b),\quad
\gamma^4=\tfrac14\sum_{a,b}d(a,b).
\]
Then \(d(a,b)=\gamma^1ab+\gamma^2b+\gamma^3a+\gamma^4\), as follows by evaluating the four binary argument pairs. Thus the table presentation does not change the source cost family.

The source permits \(D=L_\gamma+C_0\). Its decomposition at L935 must therefore read
\[
S-D(y',y)=\sum_{k=1}^l\left(\frac{S-C_0}{l}-L_{\gamma,k}(y'_k,y_k)\right).
\]
The printed expression omits \(C_0/l\). This is the local source repair recorded under theory_007. The proof below keeps the constant separate, so it never discards that shift.

## Theorem-Critical Obligations

1. Compute the global cost sum and complementary additive weight from the compact inputs.
2. Factor the actual inner relative-score sum and establish the domains of subsequent operations.
3. Evaluate the logarithmic regime, including matching terms, cross terms, and the constant cost term.
4. Evaluate the positive-parameter regime, including both terms of \(\Phi_\tau\).
5. Establish linear operation and storage bounds for all allowed inputs, including \(l=1\), zero costs, and zero scores.

All five obligations are derived below by finite distributivity and elementary algebra. No external or paper-specific theorem is invoked.

## Step 001: Cost Normalization and Additive Weights

Write \(N=2^l\). For each label, let
\[
Q_k=\sum_{a=\pm1}\sum_{b=\pm1}d_k(a,b).
\]
For a fixed pair \((v_k,w_k)\), there are \(4^{l-1}=N^2/4\) choices of the remaining coordinates of \((v,w)\). Consequently,
\[
S=N^2d_0+\frac{N^2}{4}\sum_{k=1}^l Q_k.
\]
This computes the global sum using four table entries per label, not an exponential-size oracle. The number \(N\) can be computed by \(l\) successive doublings.

Fix \(y\). Set
\[
c_0=S-d_0,\qquad c_k(b)=-d_k(b,y_k),\qquad b\in\{-1,+1\}.
\]
Then
\[
C(y,y')=c_0+\sum_{k=1}^l c_k(y'_k).
\]
Individual \(c_k\) need not be nonnegative. The complete weight is nonnegative because \(S\) is a sum of nonnegative costs containing \(D(y',y)\).

Define
\[
A_k=\sum_{b=\pm1}c_k(b),\qquad
H=\sum_{y'\in Y}C(y,y').
\]
Each fixed bit occurs \(N/2\) times, so
\[
H=Nc_0+\frac N2\sum_{k=1}^l A_k.
\]
All quantities in this step take \(O(l)\) operations.

## Step 002: The Actual Inner Sum

For each label and candidate bit, define
\[
Z_i(b)=\sum_{a=\pm1}e^{(a-b)s_i}=1+e^{-2bs_i}.
\]
Finite distributivity gives
\[
\begin{aligned}
u(y')
&=\sum_{y''\in Y}\exp\left(\sum_{i=1}^l(y''_i-y'_i)s_i\right)\\
&=\sum_{y''\in Y}\prod_{i=1}^l e^{(y''_i-y'_i)s_i}
=\prod_{i=1}^l\left(\sum_{a=\pm1}e^{(a-y'_i)s_i}\right)
=\prod_{i=1}^l Z_i(y'_i).
\end{aligned}
\]
The penultimate equality follows by expanding the product: its terms are indexed by exactly the binary vectors \(y''\).

Every score is finite, so every \(Z_i(b)\) is finite and strictly greater than one. Thus \(u(y')\), logarithms, and negative real powers are well-defined. Computing both values of every \(Z_i\) takes \(O(l)\) operations.

## Step 003: The Case \(\tau=0\)

Put
\[
g_i(b)=\log Z_i(b),\qquad
B_i=\sum_{b=\pm1}g_i(b),\qquad
R_i=\sum_{b=\pm1}c_i(b)g_i(b).
\]
The inner factorization implies
\[
\log u(y')=\sum_{i=1}^l g_i(y'_i).
\]
Hence
\[
L_0=\sum_{y'\in Y}\left(c_0+\sum_k c_k(y'_k)\right)\left(\sum_i g_i(y'_i)\right).
\]
For the constant term and matching terms, fixing a single bit leaves \(N/2\) choices, giving
\[
\sum_{y'}\sum_i c_0g_i(y'_i)=\frac N2c_0\sum_i B_i,
\qquad
\sum_{y'}c_i(y'_i)g_i(y'_i)=\frac N2 R_i.
\]
For \(k\ne i\), when \(l\ge2\), fixing the two bits leaves \(N/4\) choices, so
\[
\sum_{y'}c_k(y'_k)g_i(y'_i)=\frac N4 A_kB_i.
\]
The cross terms do not require a quadratic loop, because
\[
\sum_{k\ne i}A_kB_i
=\left(\sum_k A_k\right)\left(\sum_i B_i\right)-\sum_i A_iB_i.
\]
Combining these identities yields
\[
L_0=
\frac N2c_0\sum_i B_i
+\frac N4\left[\left(\sum_k A_k\right)\left(\sum_i B_i\right)-\sum_i A_iB_i\right]
+\frac N2\sum_i R_i.
\]
For \(l=1\), there are no cross terms and the bracket is identically zero. The same displayed formula therefore remains valid; it reduces to \(c_0B_1+R_1\), the direct binary sum.

Every marginal and aggregate in this expression requires only constant work per label. Thus the logarithmic regime takes \(O(l)\) operations.

## Step 004: The Case \(\tau>0\)

Define
\[
W_i(b)=Z_i(b)^{-\tau},\qquad
F_i=\sum_{b=\pm1}W_i(b),\qquad
G_i=\sum_{b=\pm1}c_i(b)W_i(b),\qquad
P=\prod_{i=1}^l F_i.
\]
Since all factors are positive,
\[
u(y')^{-\tau}=\prod_i W_i(y'_i),\qquad F_i>0.
\]
Expanding products of binary sums as in Step 002 gives
\[
\sum_{y'}\prod_i W_i(y'_i)=P.
\]
For each \(k\), fix its bit and independently sum all other bits:
\[
\sum_{y'}c_k(y'_k)\prod_i W_i(y'_i)
=\left(\sum_{b=\pm1}c_k(b)W_k(b)\right)
\prod_{i\ne k}\left(\sum_{b=\pm1}W_i(b)\right)
=G_k\frac{P}{F_k}.
\]
By the additive cost representation,
\[
\sum_{y'}C(y,y')u(y')^{-\tau}
=c_0P+\sum_{k=1}^l G_k\frac{P}{F_k}.
\]
Both terms in the definition of \(\Phi_\tau\) must be retained. Using the already computed \(H\),
\[
L_\tau=
\frac{c_0P+\sum_{k=1}^l G_kP/F_k-H}{\tau}.
\]
This formula has exactly the sign in the public definition. Computing the two values of \(W_i\), the two marginals, the total product, and all replacements takes \(O(l)\) operations. Every denominator \(F_k\) is strictly positive; weighted marginals \(G_k\) may vanish, but they are never divisors.

## Step 005: Complexity and Boundary Checks

The cost tables have \(4l\) entries. Steps 001 and 002 use constant work per label, and each parameter regime uses only a fixed number of label-wise arrays and aggregate sums or products. There is no loop over \(Y\), over \(Y^2\), or over all pairs of distinct label indices. Total operation count and storage are \(O(l)\) in the stated model.

For \(l=1\), empty products in Step 004 equal one, and Step 003 explicitly handles the absent cross terms. Zero costs require no division by a cost or by \(S\). In particular, if \(D\) is identically zero, then \(S,C,H\), and both loss formulas are zero. Zero scores give \(u(y')=N\), so the formulas agree with \(L_0=H\log N\) and \(L_\tau=H(N^{-\tau}-1)/\tau\) for \(\tau>0\). Finite scores ensure strictly positive partition marginals, regardless of zero or signed individual additive cost terms. The two parameter regimes are separate; no limiting or continuity assertion at zero is needed.

All identities are exact real identities. Large magnitudes and floating-point overflow or underflow concern numerical implementation, not the stipulated operation count. Every theorem-critical obligation is closed.
