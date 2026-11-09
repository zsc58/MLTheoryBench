# Reference Proof

## Proof Structure and Obligations

The proof has six obligations: justify the three-term decomposition without subtracting infinite expectations; control distribution shift in both directions; derive sub-Gaussianity of the orbit-averaged loss; establish its per-sample information bound under the learner's marginal channel; establish augmentation decoupling conditional only on the indicated training example; and justify averaging, including zero and infinite information cases. All six obligations are discharged below.

The only information-theoretic input needed is the standard relative-entropy inequality. Its relevant statement and an elementary derivation are included. In particular, no product-law concentration of an uncentered loss is assumed.

## Entropy Inequality and Centered Decoupling

For probability measures \(\nu,\mu\), the entropy inequality is
\[
\mathbb E_\nu F\le D_{\rm KL}(\nu\Vert\mu)+\log\mathbb E_\mu e^F.
\]
For bounded measurable \(F\) and finite relative entropy, define \(d\mu_F=e^F d\mu/\mathbb E_\mu e^F\). Nonnegativity of relative entropy gives
\[
0\le D_{\rm KL}(\nu\Vert\mu_F)
=D_{\rm KL}(\nu\Vert\mu)-\mathbb E_\nu F+\log\mathbb E_\mu e^F.
\]
Nonnegativity itself follows by integrating \(t\log t\ge t-1\). The same argument applies to integrable unbounded \(F\) with a finite exponential moment, after the integrability verification below.

Suppose a real measurable \(h\) satisfies
\[
\mathbb E_\mu e^{t h}\le e^{t^2R^2/2}\qquad(t\in\mathbb R),
\]
and write \(K=D_{\rm KL}(\nu\Vert\mu)<\infty\). For \(t>0\), apply the bounded-function entropy inequality to \(t\min\{|h|,M\}\). Since
\[
\mathbb E_\mu e^{t|h|}\le\mathbb E_\mu e^{th}+\mathbb E_\mu e^{-th}\le2e^{t^2R^2/2},
\]
monotone convergence gives
\[
\mathbb E_\nu|h|\le\frac{K+\log2}{t}+\frac{tR^2}{2}.
\]
Optimizing proves
\[
\mathbb E_\nu|h|\le R\sqrt{2(K+\log2)}. \tag{A}
\]
Thus the entropy inequality is applicable to both \(th\) and \(-th\), yielding
\[
|\mathbb E_\nu h|\le\frac Kt+\frac{tR^2}{2}.
\]
For \(K>0\), minimize at \(t=\sqrt{2K}/R\); for \(K=0\), let \(t\downarrow0\). Therefore
\[
|\mathbb E_\nu h|\le R\sqrt{2K}. \tag{B}
\]

The form of decoupling needed here follows directly. Let \((X,V)\) have joint law \(\nu\), let \(\mu=P_X\otimes P_V\), and suppose \(f(v,X)\) is \(R\)-sub-Gaussian for every fixed \(v\). Assume its fixed-parameter mean \(b(v)=\mathbb E_{P_X}f(v,X)\) is finite. Define
\[
h(x,v)=f(v,x)-b(v).
\]
Then, by integration of the fixed-parameter exponential-moment bounds,
\[
\mathbb E_{P_X\otimes P_V}e^{t h(X,V)}
=\int\mathbb E_{P_X}e^{t(f(v,X)-b(v))}\,P_V(dv)
\le e^{t^2R^2/2}.
\]
Applying (A) and (B) gives, when \(I(X;V)<\infty\),
\[
\mathbb E|f(V,X)-b(V)|\le R\sqrt{2(I(X;V)+\log2)},
\]
\[
\left|\mathbb E[f(V,X)-b(V)]\right|\le R\sqrt{2I(X;V)}. \tag{C}
\]
These are expectations of centered differences. They do not require \(\mathbb E b(V)\) or the two uncentered loss expectations to be finite. This verifies, rather than assumes, the product-law hypothesis underlying decoupling.

## Step 1: Cases and Pointwise Decomposition

Let \(Q=D_G\circ D\). If the proposed right-hand side is infinite, the conclusion follows immediately from the stipulated existence of the extended-real generalization expectation. Henceforth suppose that right-hand side is finite. In particular,
\[
K_0=D_{\rm KL}(D\Vert Q)<\infty,\qquad I(Z_i;W)<\infty
\]
for every \(i\), and each expected square root of conditional augmentation information is finite.

The two sub-Gaussian assumptions ensure that \(L_Q(w)\) and \(\ell_G(w,z)\) are finite for every fixed \(w,z\). Step 2 will also establish finiteness of \(L_D(w)\). Define the centered residuals
\[
r_i=\ell_G(W,Z_i)-L_Q(W),\qquad
u_{ij}=\ell(W,G_jZ_i)-\ell_G(W,Z_i).
\]
The algebraic identity is
\[
H=L_D(W)-L_Q(W)-\frac1m\sum_i r_i-\frac1{mn}\sum_{i,j}u_{ij}. \tag{D}
\]
We prove integrability of all these differences before taking expectations of this identity.

## Step 2: Distribution Shift

For fixed \(w\), set \(h_w(z)=\ell(w,z)-L_Q(w)\). Assumption 1 supplies the exponential-moment hypothesis of (A) and (B) with reference law \(Q\) and comparison law \(D\). Consequently \(h_w\) is integrable under \(D\), \(L_D(w)<\infty\), and
\[
|L_D(w)-L_Q(w)|\le R\sqrt{2K_0}.
\]
This bound is uniform in \(w\). Therefore the difference is integrable under \(P_W\), and
\[
A:=\mathbb E_W[L_D(W)-L_Q(W)]
\quad\text{satisfies}\quad
|A|\le R\sqrt{2D_{\rm KL}(D\Vert Q)}. \tag{E}
\]
Both signs follow by applying the entropy inequality with a positive parameter to \(h_w\) and \(-h_w\), not by retaining the direction of an inequality after division by a negative parameter.

## Step 3: Sub-Gaussianity of the Orbit-Averaged Loss

For every fixed \(w\) and \(t\in\mathbb R\), Jensen's inequality and Assumption 1 give
\[
\begin{aligned}
\mathbb E_{Z\sim D}e^{t(\ell_G(w,Z)-L_Q(w))}
&=\mathbb E_Z\exp\!\left(t\,\mathbb E_G[\ell(w,GZ)-L_Q(w)]\right)\\
&\le\mathbb E_{Z,G}e^{t(\ell(w,GZ)-L_Q(w))}\\
&=\mathbb E_{Z'\sim Q}e^{t(\ell(w,Z')-L_Q(w))}\\
&\le e^{t^2R^2/2}.
\end{aligned}
\]
Thus \(\ell_G(w,Z)\) is \(R\)-sub-Gaussian under \(D\), with mean \(L_Q(w)\).

## Step 4: Per-Sample Orbit-Loss Bound

Integrating out augmentation randomness gives the learner's marginal channel
\[
P_{W\mid S=s}=\int P_{W\mid S=s,E=e}\,D_G^n(de).
\]
This is the same output law as in the original experiment, not a new learner trained with a different objective.

For each \(i\), apply (C) to the joint law of \((Z_i,W)\), reference product law \(D\otimes P_W\), loss \(f(w,z)=\ell_G(w,z)\), and mean \(b(w)=L_Q(w)\). Step 3 verifies the fixed-parameter sub-Gaussian hypothesis. It follows that \(r_i\) is integrable and
\[
|\mathbb E r_i|\le R\sqrt{2I_{\ell_G}(Z_i;W)}.
\]
This is also an explicit derivation of the per-sample information inequality used here. Hence
\[
B:=\mathbb E\left[L_Q(W)-\frac1m\sum_i\ell_G(W,Z_i)\right]
=-\frac1m\sum_i\mathbb E r_i
\]
is well-defined and satisfies
\[
|B|\le\frac Rm\sum_i\sqrt{2I_{\ell_G}(Z_i;W)}. \tag{F}
\]

## Step 5: Augmentation Decoupling Given One Example

Fix \(i,j\), and condition only on \(Z_i=z\). Independence of \(S\) and \(E\) implies that the conditional marginal of \(G_j\) is still \(D_G\). Write
\[
\nu_{ij,z}=P_{G_j,W\mid Z_i=z},\qquad
\mu_{ij,z}=D_G\otimes P_{W\mid Z_i=z},
\]
\[
K_{ij}(z)=D_{\rm KL}(\nu_{ij,z}\Vert\mu_{ij,z})=I_\ell^z(G_j;W).
\]
The conditional output law integrates over the other training examples and the other augmentation variables. It is not \(P_{W\mid S=s}\).

Use the centered function
\[
h_{i,z}(g,w)=\ell(w,gz)-\ell_G(w,z).
\]
Assumption 2 and integration over \(P_{W\mid Z_i=z}\) show
\[
\mathbb E_{\mu_{ij,z}}e^{t h_{i,z}(G,W)}\le e^{t^2R^2/2}
\qquad(t\in\mathbb R).
\]
Since the right-hand side of the theorem is finite, \(K_{ij}(z)<\infty\) for \(D\)-almost every \(z\). Applying (A) and (B) under these conditional laws gives
\[
\mathbb E[|u_{ij}|\mid Z_i=z]\le R\sqrt{2(K_{ij}(z)+\log2)},
\]
\[
\left|\mathbb E[u_{ij}\mid Z_i=z]\right|\le R\sqrt{2K_{ij}(z)}.
\]
The first bound proves unconditional integrability: indeed,
\[
\sqrt{K_{ij}(z)+\log2}\le\sqrt{K_{ij}(z)}+\sqrt{\log2},
\]
and the expectation of \(\sqrt{K_{ij}(Z_i)}\) is finite. This argument does not require \(\mathbb E K_{ij}(Z_i)<\infty\).

The tower property and the second bound therefore imply
\[
|\mathbb E u_{ij}|\le R\,\mathbb E_{Z_i}\sqrt{2I_\ell^{Z_i}(G_j;W)}.
\]
Thus
\[
C:=\mathbb E\left[\frac1m\sum_i\ell_G(W,Z_i)-\frac1{mn}\sum_{i,j}\ell(W,G_jZ_i)\right]
=-\frac1{mn}\sum_{i,j}\mathbb E u_{ij}
\]
is well-defined, and
\[
|C|\le\frac R{mn}\mathbb E_S\sum_{i=1}^m\sum_{j=1}^n\sqrt{2I_\ell^{Z_i}(G_j;W)}. \tag{G}
\]
The outer expectation is exactly the one in the task because its \((i,j)\) summand is a function of \(Z_i\). No independence among the \(mn\) augmented observations is asserted or used.

## Step 6: Combination

The bounds above establish integrability of every difference in (D). Taking expectations now legitimately gives
\[
\operatorname{gen}(D,P_{W\mid S,E})=A+B+C.
\]
Applying the triangle inequality and (E), (F), and (G) proves
\[
\left|\operatorname{gen}(D,P_{W\mid S,E})\right|
\le R\left[\sqrt{2D_{\rm KL}(D\Vert D_G\circ D)}
+\frac1m\sum_{i=1}^m\sqrt{2I_{\ell_G}(Z_i;W)}
+\frac1{mn}\mathbb E_S\sum_{i=1}^m\sum_{j=1}^n\sqrt{2I_\ell^{Z_i}(G_j;W)}\right].
\]
Zero divergences were covered by the positive-parameter limit, and infinite right-hand sides were covered before introducing the decomposition. The proof applies unchanged when \(m=1\), \(n=1\), or the augmentation law is deterministic.

## Private Source-Repair Notes

The source's divided entropy inequality is used only for positive parameters; its variational KL orientation is corrected. The missing factor R in its orbit-loss estimate and the mistaken inner summation index are restored. Its augmentation argument is reconstructed conditional on Z_i, as required by the source's definition of disintegrated information and confirmed by its single-example conditional Gaussian calculation. Fixed-parameter centering supplies the product-law exponential-moment hypothesis omitted from the source application. These repairs preserve the substantive theorem and its three-term proof architecture. No unresolved private proof obligation remains.
