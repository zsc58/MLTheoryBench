# Reference Proof

## Source Contract and Proof Obligations

The source evaluates the ambient Hessian at the realized weight associated with a nondegenerate local minimizer of the fixed-SPD objective; see L001313-L001319. In the public notation this point is $\bar U$, its coordinate is $0$, and its realized weight is $\bar M$. The public local-minimum assumption together with positive strong convexity supplies the source's nondegeneracy condition. The coordinates used for conditioning and for the iteration are the same coordinates, adapted to the stated tangent directions.

The source objective is $\mathcal J(Q,S)=F(QS^{1/2})+\lambda_S\|\log S\|_F^2/2$. At fixed $S$, the second term is constant. Replacing the fixed-$S$ objective by the corresponding loss therefore preserves coordinate derivatives, minimizers, and objective differences. No stochastic product-update theorem is needed for this deterministic local conclusion.

The obligations are: identify the spectral interpretation; verify the aligned differential; establish the comparison minimum and positivity of the conditioning constants; obtain the one-step descent and gradient-error inequalities on the stated domain; iterate without losing boundary cases; and prove the inverse-alignment comparison. The spectral and differential calculations explain the setup but are not additional public conclusions. The actual contraction uses the separately assumed local conditioning.

## Step 1: Spectral Interpretation

For $M=UA^{1/2}$ with $U\in\operatorname{St}(n,r)$,
$$
M^{\mathsf T}M
=A^{1/2}U^{\mathsf T}UA^{1/2}
=A.
$$
The standard SVD identity identifies the eigenvalues of $M^{\mathsf T}M$ with the squared singular values of $M$. Thus the $d_i$ are the squared singular values as a multiset; no ordering of the $d_i$ relative to their indices is required.

## Step 2: Aligned Differential and Its Limitation

For fixed $A$, the ambient extension of $U\mapsto\Psi(U,A)$ is linear, and hence
$$
D_U\Psi(\bar U,A)[E]=EA^{1/2}.
$$
The orthogonal eigendecomposition gives
$$
A^{1/2}=\sum_j\sqrt{d_j}\,r_jr_j^{\mathsf T}.
$$
Consequently,
$$
D_U\Psi(\bar U,A)[E_i]
=\sum_j\sqrt{d_j}(E_ir_j)r_j^{\mathsf T}
=\sqrt{d_i}\,e_ir_i^{\mathsf T}.
$$
Its Frobenius norm is $\sqrt{d_i}$, and
$$
Z_i=e_ir_i^{\mathsf T},\qquad \|Z_i\|_F=1.
$$
The chart compatibility gives the same first-order realized displacement for coordinate directions $\varepsilon_i$. Therefore the ambient Hessian evaluated on a first-order displacement $\sum_i\sqrt{d_i}z_iZ_i$ has quadratic form $\sum_i d_ih_i z_i^2$.

This is not, by itself, the full coordinate Hessian. Writing $W(x)=\varphi(x)A^{1/2}$, the second-order chain rule gives
$$
D^2\widetilde g(0)[v,w]
=\nabla^2\ell(\bar M)[DW(0)[v],DW(0)[w]]
+\langle\nabla\ell(\bar M),D^2W(0)[v,w]\rangle_F.
$$
A constrained local minimum does not imply that the ambient gradient vanishes. The existing repair of the source proof therefore remains necessary: do not identify pullback-Hessian eigenvalues solely from the ambient Hessian and the first differential. Instead, use the express $m_A$-strong-convexity and $L_A$-smoothness assumption.

## Step 3: The Comparison Minimum and Constants

Every $d_i h_i$ is positive and finite, and the index set is finite and nonempty. Thus
$$
0<m_A\le L_A<\infty,\qquad K_A\ge1,\qquad K_0\ge1.
$$
Since $\bar U$ is a local minimizer and $\varphi(0)=\bar U$, differentiability on the open domain gives $\nabla\widetilde g(0)=0$. Strong convexity then yields, for every $x\in\Omega$,
$$
\widetilde g(x)\ge\widetilde g(0)+\frac{m_A}{2}\|x\|_2^2.
$$
Hence $0$ is the unique minimizer on $\Omega$, and
$$
\widetilde g(0)=g_A(\bar U)=g_*.
$$
Since $\widetilde g$ is twice continuously differentiable, strong convexity also gives $D^2\widetilde g(0)\succeq m_A I$. Thus the critical point is nondegenerate, as required by the source.

## Step 4: Descent and Iteration

For brevity write $f=\widetilde g$, $m=m_A$, and $L=L_A$. On the convex domain $\Omega$, $L$-smoothness gives
$$
f(y)\le f(x)+\langle\nabla f(x),y-x\rangle+\frac L2\|y-x\|_2^2,
\qquad x,y\in\Omega.
$$
Indeed, integrate the gradient along the segment from $x$ to $y$ and use
$\|\nabla f(x+s(y-x))-\nabla f(x)\|_2\le Ls\|y-x\|_2$.
The entire segment lies in $\Omega$ by convexity. Iterate containment makes this applicable to $x=x_t$ and $y=x_{t+1}$. Substituting the update gives
$$
f(x_{t+1})\le f(x_t)-\frac{1}{2L}\|\nabla f(x_t)\|_2^2.
$$

Strong convexity, applied to $x_t$ and $0$, gives
$$
f(0)\ge f(x_t)+\langle\nabla f(x_t),-x_t\rangle+\frac m2\|x_t\|_2^2
\ge f(x_t)-\frac{1}{2m}\|\nabla f(x_t)\|_2^2.
$$
The second inequality follows by completing the square. Therefore
$$
\|\nabla f(x_t)\|_2^2\ge2m\bigl(f(x_t)-f(0)\bigr).
$$
Combining the two inequalities proves
$$
f(x_{t+1})-f(0)
\le\left(1-\frac mL\right)\bigl(f(x_t)-f(0)\bigr).
$$
These calculations explicitly verify the local form of the standard strongly-convex smooth descent result represented by theory_027; no further external proof obligation is used.

Set $c=1-m/L=1-K_A^{-1}\in[0,1)$. Induction gives, for every integer $T\ge1$,
$$
f(x_T)-f(0)\le c^T\bigl(f(x_0)-f(0)\bigr).
$$
For $T=0$, the assertion is equality under the stated zeroth-power convention. If $m=L$, then $c=0$ and the one-step inequality, together with nonnegative objective error, gives $f(x_t)=f(0)$ for every $t\ge1$; no division by $c$ is used. Finally, $f(x_t)=g_A(U_t)$ and $f(0)=g_*$ give the required estimate.

## Step 5: Inverse-Alignment Comparison

Suppose $a/h_i\le d_i\le b/h_i$ for every $i$. Multiplying by $h_i>0$ yields
$$
a\le d_ih_i\le b.
$$
Thus $m_A\ge a$, $L_A\le b$, and
$$
K_A=\frac{L_A}{m_A}\le\frac ba.
$$
If $b/a\le K_0$, then $K_A\le K_0$. Since $K\mapsto1-1/K$ is increasing on $[1,\infty)$,
$$
0\le1-K_A^{-1}\le1-K_0^{-1}<1.
$$
Taking nonnegative integer powers, with the declared convention at $T=0$, proves the factor comparison. Multiplication by the nonnegative initial objective error is legitimate.

## Boundary and Closure Check

The case $r=1$, equality $a=b$, and the case $K_A=1$ are included. The existence of the aligned tangent directions is conditional, not asserted for every Stiefel dimension. In particular, the square case introduces no counterexample: the alignment conditions imply $E_i=e_ir_i^{\mathsf T}$, and tangency implies $\bar U^{\mathsf T}e_i=0$. When $n=r$, this contradicts $\|e_i\|_2=1$, so no such data satisfy the hypotheses. No extra public restriction $n>r$ is needed. All obligations needed for the frozen conclusion are closed.
