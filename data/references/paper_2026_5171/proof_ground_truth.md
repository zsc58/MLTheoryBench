# Reference Proof

## Proof Structure

The proof derives train and test displacements through the propagator, proves that the dissipation reservoir is invisible to test outputs, identifies the kernels of the train displacement operator and dissipation Gramian using constant curvature, and then applies the Moore-Penrose factorization to obtain exact coupling.

## Private Proof Notation

Let m be the fixed dimension of the training-output vector. Introduce the auxiliary matrix

W := int_s^T P(t)^T K_SS(t)P(t) dt.

This matrix is a private proof construction, not an additional public assumption or a quantity that solvers must use. All matrices in this integral are evaluated on the same realized trajectory as the public operators G and D. The C^2 output maps and the realized gradient-flow trajectory make J_S(t), J_Q(t), and K_SS(t) continuous on the compact window. The solution P(t) of the displayed ODE is continuously differentiable. Consequently W is a finite real m-by-m matrix.

## Complete Proof

### 1. Propagation and displacement identities

Both g(t) and P(t)g(s) solve the displayed output-gradient equation with the same initial value. To verify their equality directly, set e(t)=g(t)-P(t)g(s). Then

e'(t)=-B K_SS(t)e(t), and e(s)=0.

Because B is symmetric positive definite and K_SS(t)=J_S(t)J_S(t)^T is symmetric positive semidefinite,

d/dt [e(t)^T B^{-1}e(t)] = -2 e(t)^T K_SS(t)e(t) <= 0.

The quantity on the left is nonnegative and starts at zero, so it is identically zero. Positive definiteness of B^{-1} implies e(t)=0. Thus

g(t)=P(t)g(s).

Along gradient flow, the chain rule gives

U_Q'(t)=J_Q(t)w'(t)=-K_QS(t)g(t),

U_S'(t)=J_S(t)w'(t)=-K_SS(t)g(t).

Substituting g(t)=P(t)g(s) and integrating yields

U_Q(T)-U_Q(s)=-Gg(s),

U_S(T)-U_S(s)=-Dg(s).

### 2. The dissipation kernel is invisible to G

The definition of W makes it symmetric. For every h in R^m,

h^T W h = int_s^T ||J_S(t)^T P(t)h||^2 dt >= 0,

so W is positive semidefinite. If h belongs to ker(W), this nonnegative integral is zero, hence J_S(t)^T P(t)h=0 almost everywhere. Since K_QS(t)=J_Q(t)J_S(t)^T,

Gh = int_s^T J_Q(t)[J_S(t)^T P(t)h] dt = 0.

Therefore ker(W) is a subset of ker(G).

We will also use the following consequence of the same integral representation: if h^TWh=0, then J_S(t)^TP(t)h=0 almost everywhere, and therefore

Wh = int_s^T P(t)^T J_S(t)[J_S(t)^T P(t)h] dt = 0.

Thus vanishing of the quadratic form implies membership in ker(W), including when W is singular.

### 3. Constant curvature identifies ker(D) with ker(W)

Because B is constant and invertible, integration of P'(t)=-B K_SS(t)P(t), with P(s)=I, gives

D=B^{-1}(I-P(T)).

Using symmetry of B and K_SS(t), differentiation gives

d/dt [P(t)^T B^{-1}P(t)]

= (-P(t)^T K_SS(t)B)B^{-1}P(t) + P(t)^T B^{-1}(-B K_SS(t)P(t))

= -2 P(t)^T K_SS(t)P(t).

No commutation between B and K_SS(t) is used. Integrating and evaluating the quadratic form at h gives

2 h^T W h = h^T B^{-1}h - (P(T)h)^T B^{-1}P(T)h.

If h belongs to ker(D), the formula for D gives P(T)h=h. The energy identity then gives h^TWh=0, and the preceding integral argument gives Wh=0. Hence ker(D) is a subset of ker(W).

Conversely, if h belongs to ker(W), then J_S(t)^TP(t)h=0 almost everywhere. It follows that K_SS(t)P(t)h=0 almost everywhere, and integration gives Dh=0. Hence ker(W) is a subset of ker(D).

We have proved

ker(D)=ker(W) subset of ker(G).

### 4. Factorization and exact coupling

The defining Moore-Penrose identity DD^dagger D=D gives

D(I-D^dagger D)=0.

Consequently, for every h, the vector (I-D^dagger D)h belongs to ker(D), and the established kernel inclusion implies

G(I-D^dagger D)h=0.

Thus G=GD^dagger D. With A_circ=GD^dagger and the displacement identities from Step 1,

U_Q(T)-U_Q(s)

= -Gg(s)

= -GD^dagger Dg(s)

= A_circ(U_S(T)-U_S(s)).

No invertibility of D or W is needed. In particular, if D=0, the kernel inclusion forces G=0, and the same argument applies. A zero initial output gradient and rank-deficient kernels also require no separate assumption. If Q is empty, the conclusion is the identity in its zero-dimensional output space; if an empty S is admitted under the usual zero-dimensional matrix conventions, w'=0 and both displacements vanish. The public task requires s<T; the source's zero-length endpoint is also consistent, since then D=G=W=0 and both displacements vanish.

The proof applies to every finite realized window in the public task and uses neither a kernel-drift bound nor an asymptotic limit.
