# Reference Proof

## Proof Structure

For a fixed parameter, first verify that the marginal-score and conditional-score kernel integrals are well-defined RKHS elements. Use reproduction to identify the linear functional, and complete the square to solve the inner maximization. Compute the unit-ball supremum defining the discrepancy, including the zero case. Differentiate the defining mixture and integrate the score difference to identify the conditional representation. Finally, expand its squared RKHS norm using independent joint samples and conclude the outer optimization equivalence and estimability.

## Complete Proof

Fix \(\phi\in\Phi\). Write \(q=q_\phi\), \(q_c(y\mid z)=q_\phi(y\mid z)\), and write \(Q(dz)=q(dz)\) for the mixing probability law, to distinguish it from the marginal density. Put
\[
g(y)=s_p(y)-s_q(y),\qquad
r(y,z)=s_p(y)-s_{q_c(\cdot\mid z)}(y).
\]
All Hilbert-space integrals below are Bochner integrals.

### 1. Well-defined representers and the linear functional

For a scalar RKHS kernel section, \(\|k(\cdot,y)\|_{\mathcal H_0}^2=k(y,y)\). Consequently, for \(v\in\mathbb R^d\),
\[
\|k(\cdot,y)v\|_{\mathcal H}=\sqrt{k(y,y)}\,\|v\|.
\]
The map \(y\mapsto k(\cdot,y)\) is norm-continuous: the squared norm of the difference of two sections is \(k(y,y)+k(u,u)-2k(y,u)\). Sections at points with rational coordinates have dense span, since a function orthogonal to all such sections vanishes on a dense set and is continuous. Thus the RKHS, and its finite Cartesian product, are separable. Together with the stated measurability of the scores, this verifies strong measurability of the integrands used below.

The assumptions and Cauchy-Schwarz give
\[
\mathbb E_q[\sqrt{k(X,X)}\,\|g(X)\|]
\leq \big(\mathbb E_q k(X,X)\big)^{1/2}
      \big(\mathbb E_q\|g(X)\|^2\big)^{1/2}<\infty.
\]
Therefore
\[
a:=S_{q,k}g=\int k(\cdot,y)g(y)q(y)\,dy\in\mathcal H.
\]
The conditional first-moment assumption likewise makes
\[
b:=\int\!\int k(\cdot,y)r(y,z)q_c(y\mid z)\,dy\,Q(dz)
\]
a well-defined element of \(\mathcal H\).

For every \(f\in\mathcal H\), reproduction and Cauchy-Schwarz imply
\[
|f(y)^\top g(y)|\leq
\|f\|_{\mathcal H}\sqrt{k(y,y)}\,\|g(y)\|.
\]
The right side is integrable. Applying the continuous linear functional \(\langle f,\cdot\rangle_{\mathcal H}\) to the Bochner integral yields
\[
\mathbb E_q[f(X)^\top g(X)]=\langle f,a\rangle_{\mathcal H}.
\]

### 2. Inner optimization and discrepancy

The penalty is deterministic for fixed \(f\), so the inner objective is
\[
2\langle f,a\rangle_{\mathcal H}-\|f\|_{\mathcal H}^2
=\|a\|_{\mathcal H}^2-\|f-a\|_{\mathcal H}^2.
\]
Its unique maximizer is \(f^*=a\), and its maximum is \(\|a\|_{\mathcal H}^2\). Evaluation, a continuous linear map on the RKHS, gives for every \(x\)
\[
f^*(x)=\mathbb E_{Y\sim q}[k(x,Y)(s_p(Y)-s_q(Y))].
\]
Moreover,
\[
\operatorname{KSD}_k(q\|p)
=\sup_{\|f\|_{\mathcal H}\leq1}\langle f,a\rangle_{\mathcal H}
=\|a\|_{\mathcal H}.
\]
Indeed, Cauchy-Schwarz gives the upper bound; if \(a\ne0\), equality holds at \(f=a/\|a\|_{\mathcal H}\), while if \(a=0\), every value in the supremum is zero. Hence the inner optimum equals squared KSD, including when the kernel or discrepancy is zero.

### 3. Conditional-score representation

The assumed passage of differentiation through the defining mixture gives, componentwise,
\[
\nabla q(y)=\int\nabla_y q_c(y\mid z)\,Q(dz)
=\int q_c(y\mid z)s_{q_c(\cdot\mid z)}(y)\,Q(dz).
\]
For each fixed \(y\), the integrals here are absolutely convergent by the mixture differentiation assumption. Since \(q(y)>0\) is finite and \(s_p(y)\) is finite,
\[
\int q_c(y\mid z)r(y,z)\,Q(dz)
=q(y)s_p(y)-\nabla q(y)=q(y)g(y).
\]
This calculation is pointwise in \(y\); it does not assume that the two score terms are separately integrable over \(y\).

The conditional first-moment assumption is precisely absolute integrability of the norm of the Hilbert-valued integrand defining \(b\). Bochner Fubini therefore gives
\[
b=\int k(\cdot,y)\left[\int q_c(y\mid z)r(y,z)\,Q(dz)\right]dy
=\int k(\cdot,y)q(y)g(y)\,dy=a.
\]
Evaluating at \(x\) proves the second formula for \(f^*(x)\). This pointwise expectation is absolutely integrable because
\[
|k(x,y)|\leq\sqrt{k(x,x)}\sqrt{k(y,y)}.
\]

### 4. Independent-pair expression and outer equivalence

Let \((X,Z)\) and \((X',Z')\) be independent draws from \(q_c(x\mid z)\,dx\,Q(dz)\), and define
\[
V=k(\cdot,X)r(X,Z),\qquad V'=k(\cdot,X')r(X',Z').
\]
Both have finite expected norm. Independence implies
\[
\mathbb E|\langle V,V'\rangle_{\mathcal H}|
\leq\mathbb E[\|V\|_{\mathcal H}\|V'\|_{\mathcal H}]
=(\mathbb E\|V\|_{\mathcal H})^2<\infty.
\]
Thus scalar Fubini and the defining property of the Bochner integral yield
\[
\mathbb E\langle V,V'\rangle_{\mathcal H}
=\langle\mathbb EV,\mathbb EV'\rangle_{\mathcal H}
=\|b\|_{\mathcal H}^2.
\]
Componentwise reproduction gives
\[
\langle V,V'\rangle_{\mathcal H}
=k(X,X')\langle r(X,Z),r(X',Z')\rangle.
\]
Combining this with \(a=b=f^*\) proves
\[
\max_{f\in\mathcal H}\mathbb E_{q_\phi}
\left[2f(X)^\top(s_p(X)-s_{q_\phi}(X))-\|f\|_{\mathcal H}^2\right]
=\operatorname{KSD}_k(q_\phi\|p)^2
=\mathbb E\left[k(X,X')\left\langle
s_p(X)-s_{q_\phi(\cdot\mid Z)}(X),
s_p(X')-s_{q_\phi(\cdot\mid Z')}(X')
\right\rangle\right].
\]
The equality holds separately for every \(\phi\in\Phi\). Hence the outer objectives have the same infimum and the same minimizing parameters whenever minimizers exist. No attainment assumption is needed.

Finally, the random scalar in the last expectation is integrable and evaluable using the stated kernel and score access and two independent hierarchical samples. The average of independently repeated copies is an unbiased Monte Carlo estimator of the objective. This establishes estimability without asserting a finite variance or requiring access to the marginal density or marginal score.
