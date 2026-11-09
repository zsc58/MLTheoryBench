# Reference Proof

## Proof Obligations

The proof must establish: (1) measurability of all KL quantities that will be integrated or disintegrated; (2) equality of the global and environment-averaged likelihood contributions; (3) the posterior KL mixture identity, including finiteness of its intermediate divergence; (4) the label-marginal KL mixture identity with the correct conditioning and environment average; and (5) the final equality with both residual signs correct. All conditional statements below hold almost everywhere under the relevant conditioning marginal.

## Measurability and Integration

Write \(f(e,x,y,z)=q_e(z\mid x,y)\) for the common jointly measurable variational density. The three mixture kernels admit densities
\[
\bar f_{xy}(x,y,z)=\int f(e,x,y,z)\,p(de\mid x,y),
\]
\[
f_x(e,x,z)=\int f(e,x,y,z)\,p(dy\mid x,e),
\qquad
\bar f_x(x,z)=\int f_x(e,x,z)\,p(de\mid x).
\]
These functions are jointly measurable in their displayed arguments. The integration fact used here is that integrating a nonnegative jointly measurable function against a measurable probability kernel produces a measurable function of the remaining parameters; it follows first for indicators of measurable rectangles and then for nonnegative measurable functions by simple-function approximation and monotone convergence. Tonelli's theorem with the fixed sigma-finite measure \(\lambda_Z\) verifies that these functions are densities of the setwise mixtures in the public task and that each integrates to one. Density values that are infinite can be replaced by zero on their parameterwise \(\lambda_Z\)-null sets. This is a jointly measurable modification that leaves the probability kernels unchanged.

For finite nonnegative numbers \(u,v\), set
\[
\Phi(u,v)=u\log(u/v)-u+v\quad\text{if }u>0,\ v>0,
\]
with \(\Phi(0,v)=v\), \(\Phi(u,0)=+\infty\) for \(u>0\), and \(\Phi(0,0)=0\). This is nonnegative and measurable: for \(v>0\), nonnegativity follows from \(t\log t-t+1\geq0\), whose derivative is \(\log t\) and whose minimum is at \(t=1\).

If probability measures \(U,V\) have densities \(u,v\) with respect to \(\lambda_Z\), then
\[
D(U\|V)=\int\Phi(u(z),v(z))\,\lambda_Z(dz). \tag{M}
\]
If \(U\not\ll V\), both sides are infinite because \(u>0,v=0\) on a set of positive \(U\)-measure. Otherwise the density ratio is \(u/v\), and the terms \(-u+v\) integrate to zero. The logarithmic integral is well-defined because its negative part is bounded by \(\int v/\mathrm e=1/\mathrm e\).

Thus (M), nonnegative parameter integration, and the jointly measurable densities show that every KL integrand in the proof is measurable. In particular,
\[
(e,x,y)\longmapsto D(q_e(\cdot\mid x,y)\|\bar q_x(\cdot\mid x))
\]
is jointly measurable. Its measurability does not follow merely from kernel measurability on unrestricted latent measurable spaces; here it follows from the common jointly measurable density assumption.

For a probability measure \(r(dt)\) and a measurable probability kernel \(Q_t\), write \(M=\int Q_t\,r(dt)\). Integration against this mixture satisfies
\[
\int h\,dM=\int r(dt)\int h\,dQ_t
\]
for nonnegative measurable \(h\), and for signed \(h\) when its absolute integral is finite. The first statement follows by the definition of a mixture and nonnegative approximation; the second follows by applying the first to the positive and negative parts. We also use disintegrations of the same joint probability measure, for nonnegative measurable functions or integrable signed functions.

## KL Mixture Calculation

Suppose \(Q_t\) has a jointly measurable density with respect to \(\lambda_Z\), and \(N\) is another probability measure with a density with respect to \(\lambda_Z\). Let \(M=\int Q_t\,r(dt)\), and suppose
\[
a:=\int r(dt)D(Q_t\|M)<\infty,
\qquad b:=D(M\|N)<\infty.
\]
All parameter-dependent divergences here, including \(D(Q_t\|N)\), are measurable by (M). The finiteness conditions imply \(Q_t\ll M\ll N\) for \(r\)-almost every \(t\). Multiplication of density ratios gives
\[
\log\frac{dQ_t}{dN}
=\log\frac{dQ_t}{dM}+\log\frac{dM}{dN}
\quad Q_t\text{-almost everywhere}.
\]
To justify integration, if \(U\ll V\) are probability measures with density \(w=dU/dV\), then
\[
\int\left(\log\frac{dU}{dV}\right)_{-}dU
=\int_{0<w<1}-w\log w\,dV\leq\frac1{\mathrm e}.
\]
Consequently, whenever \(D(U\|V)<\infty\),
\[
\int\left|\log\frac{dU}{dV}\right|dU
\leq D(U\|V)+\frac2{\mathrm e}.
\]
The first logarithm in the ratio decomposition is therefore absolutely integrable after averaging over \(r\). For the second, the mixture identity gives
\[
\int r(dt)\int\left|\log\frac{dM}{dN}\right|dQ_t
=\int\left|\log\frac{dM}{dN}\right|dM
\leq b+\frac2{\mathrm e}<\infty.
\]
The density ratios can be chosen measurably from the common densities. Hence the ratio decomposition can be integrated and averaged, yielding
\[
\begin{aligned}
\int r(dt)D(Q_t\|N)
&=\int r(dt)D(Q_t\|M)
 +\int r(dt)\int\log\frac{dM}{dN}\,dQ_t\\
&=\int r(dt)D(Q_t\|M)+D(M\|N).
\end{aligned} \tag{*}
\]
In particular, the left side is finite. This derives the mixture identity with both its measurability and integrability requirements verified.

## 1. Likelihood Contribution

Let
\[
H:=\int p(dx,dy,de)\int q_e(dz\mid x,y)\log p(y\mid z).
\]
The public joint absolute-integrability assumption makes \(H\) finite and permits the following mixture expansion and changes of conditioning order:
\[
\begin{aligned}
&\mathbb E_{p(x,y)}\mathbb E_{\bar q_{xy}(z\mid x,y)}\log p(y\mid z)\\
&\quad=\mathbb E_{p(x,y)}\mathbb E_{p(e\mid x,y)}
\mathbb E_{q_e(z\mid x,y)}\log p(y\mid z)\\
&\quad=H\\
&\quad=\mathbb E_{\pi(e)}\mathbb E_{p(x,y\mid e)}
\mathbb E_{q_e(z\mid x,y)}\log p(y\mid z).
\end{aligned} \tag{1}
\]
The equalities use the measure identity
\[
p(dx,dy)\,p(de\mid x,y)=p(dx,dy,de)
=\pi(de)\,p(dx,dy\mid e),
\]
not an assumption that all these measures have ordinary densities.

## 2. Posterior Mixture Identity

Define the finite quantities
\[
A:=\mathbb E_{p(x,y)}\mathbb E_{p(e\mid x,y)}
D\!\left(q_e(\cdot\mid x,y)\middle\|\bar q_{xy}(\cdot\mid x,y)\right),
\]
\[
G:=\mathbb E_{p(x,y)}
D\!\left(\bar q_{xy}(\cdot\mid x,y)\middle\|\bar q_x(\cdot\mid x)\right).
\]
For \(p(x,y)\)-almost every \((x,y)\), apply (*) with
\[
r=p(de\mid x,y),\quad Q_e=q_e(\cdot\mid x,y),\quad
M=\bar q_{xy}(\cdot\mid x,y),\quad N=\bar q_x(\cdot\mid x).
\]
The required mixture equality is the definition of \(\bar q_{xy}\), and the common-density hypotheses hold by the preliminary construction. The two finiteness hypotheses hold almost everywhere because the nonnegative averages \(A\) and \(G\) are finite. Hence
\[
\begin{aligned}
&\mathbb E_{p(e\mid x,y)}D(q_e(\cdot\mid x,y)\|\bar q_x(\cdot\mid x))\\
&\quad=\mathbb E_{p(e\mid x,y)}D(q_e(\cdot\mid x,y)\|\bar q_{xy}(\cdot\mid x,y))
 +D(\bar q_{xy}(\cdot\mid x,y)\|\bar q_x(\cdot\mid x)).
\end{aligned} \tag{2}
\]
The intermediate divergence is a nonnegative jointly measurable function, as proved using (M). Integrating (2) and disintegrating that same measurable function therefore gives
\[
\begin{aligned}
T&:=\int p(dx,dy,de)D(q_e(\cdot\mid x,y)\|\bar q_x(\cdot\mid x))\\
&=\mathbb E_{\pi(e)}\mathbb E_{p(x,y\mid e)}
D(q_e(\cdot\mid x,y)\|\bar q_x(\cdot\mid x))\\
&=A+G<\infty.
\end{aligned} \tag{3}
\]
Thus \(G=T-A\) is a subtraction of finite quantities. In particular, this step does not equate two iterated integrals of an unverified measurable function.

## 3. Label-Marginal Mixture Identity

Define
\[
C:=\mathbb E_{\pi(e)}\mathbb E_{p(x,y\mid e)}
D\!\left(q_e(\cdot\mid x,y)\middle\|q_x^e(\cdot\mid x)\right),
\]
\[
B:=\mathbb E_{p(x)}\mathbb E_{p(e\mid x)}
D\!\left(q_x^e(\cdot\mid x)\middle\|\bar q_x(\cdot\mid x)\right).
\]
These quantities are finite by the public assumptions and disintegration of their measurable nonnegative integrands. For \(p(x,e)\)-almost every \((x,e)\), apply (*) with
\[
r=p(dy\mid x,e),\quad Q_y=q_e(\cdot\mid x,y),\quad
M=q_x^e(\cdot\mid x),\quad N=\bar q_x(\cdot\mid x).
\]
The mixture equality is the definition of \(q_x^e\), the common-density hypotheses hold, and the two required finiteness hypotheses hold almost everywhere by finiteness of \(C\) and \(B\). We obtain
\[
\begin{aligned}
&\mathbb E_{p(y\mid x,e)}D(q_e(\cdot\mid x,y)\|\bar q_x(\cdot\mid x))\\
&\quad=\mathbb E_{p(y\mid x,e)}D(q_e(\cdot\mid x,y)\|q_x^e(\cdot\mid x))
 +D(q_x^e(\cdot\mid x)\|\bar q_x(\cdot\mid x)).
\end{aligned} \tag{4}
\]
Averaging under \(\pi(de)p(dx\mid e)\), and using
\[
\pi(de)p(dx\mid e)=p(dx,de)=p(dx)p(de\mid x),
\]
gives
\[
T=C+B. \tag{5}
\]
The left side is the same joint integral \(T\) from (3), justified by its established measurability. The second discrepancy is averaged under \(p(x)p(e\mid x)\), not under unconditional environment weights at a fixed \(x\).

## 4. Final Regrouping

Equations (3) and (5) yield
\[
G=C+B-A.
\]
Equation (1) and the objective definitions give
\[
\mathcal L=H-G,\qquad
\mathbb E_{\pi(e)}[\mathcal L_e]=H-C.
\]
The latter expectation is finite because the joint likelihood contribution is absolutely integrable and \(C<\infty\). Since \(R(q)=A-B\),
\[
\mathcal L=H-C-B+A
=\mathbb E_{\pi(e)}[\mathcal L_e]+R(q).
\]
All quantities regrouped here are finite. Null conditioning events do not contribute to the integrals; no division by a positive environment probability is required. The argument therefore also covers zero mixture weights, a single effective environment, and coinciding component distributions. All five proof obligations are closed.
