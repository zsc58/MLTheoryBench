# Reference Proof

## Audited background and obligations

The only non-elementary random-matrix input is the ordinary sample-covariance bilinear deterministic equivalent recorded as theory_018: under the public design assumptions, for any deterministic dimension-dependent bounded vectors a,b,

`a^T(Q-Qbar)b -> 0` in probability,

where `Qbar=lambda^(-1)(I+mtilde Sigma)^(-1)` and mtilde solves the public positive fixed-point equation. Its hypotheses are exactly the public assumptions. No operator-norm convergence of Q-Qbar and no maximum-coordinate rate are assumed.

The independent tools in theory_020 are the rank-one inverse identity, the fourth-moment quadratic-form variance bound, and the Efron-Stein variance inequality. Their statements are given below where used. The paper-specific leave-one-out closure is derived, not imported as a named result.

The theorem-critical obligations are: well-defined normalization and mtilde; replacement of the random diagonal normalization; existence and uniqueness of the specified chi; concentration and closure of the dependent resolvent; fixed-point stability; normalized-trace convergence; and the probability-measure interpretation. Each is closed below.

Throughout the proof, constants may depend on fixed lambda, fixed z, the covariance norm bound, the uniform moment bound, and upper and lower bounds for n/d. They do not depend on individual rows, coordinates, or dimensions. All assertions are along the public sequence. Write C for a uniform covariance norm bound.

## 1. Basic definitions and the constrained minimizer

Since S>=0 and lambda>0, Q is positive definite and Q_{kk}>0. Thus Lambda exists. Coordinate stationarity, with a scalar multiplier t_k, gives

`(S+lambda I) ahat_k = S e_k-t_k e_k`.

Consequently `ahat_k=e_k-(lambda+t_k)Qe_k`. The constraint gives `lambda+t_k=1/Q_{kk}`, so

`Ahat=I-Q[diag(Q)]^(-1)`.

For m>=0 define

`h(m)=lambda m+n^(-1)Tr[m Sigma(I+m Sigma)^(-1)]`.

It is continuous, strictly increasing, starts at zero, and tends to infinity. Therefore h(m)=1 has exactly one positive solution, which is the public mtilde equation. Also mtilde<=1/lambda. It follows that

`(lambda+C)^(-1) I <= Qbar <= lambda^(-1) I`,

and, writing D=Lambdabar,

`lambda I <= D <= (lambda+C)I`.

These bounds include singular and zero covariance.

## 2. Averaged diagonal replacement under finite moments

The bilinear deterministic equivalent, applied to coordinate vectors, and the bounds on Q and Qbar imply

`max_k E|Q_{kk}-Qbar_{kk}|^2 ->0`.

This is a maximum of deterministic expectations, not a maximum of random deviations. To justify it, if it failed, choose at each dimension a deterministic violating coordinate. The background result applies to that coordinate sequence; boundedness then upgrades convergence in probability to convergence in L2, a contradiction.

The Schur complement gives

`Lambda_{kk}=1/Q_{kk} <= lambda+S_{kk}`.

For every coordinate, the row variable x_{ik} has a uniformly bounded fourth moment: expand the fourth power of the independent-entry linear form defining x_{ik}, using ||Sigma||<=C. Thus

`sup_k E(lambda+S_{kk})^2 < infinity`.

Since D_{kk}=1/Qbar_{kk},

`|Lambda_{kk}-D_{kk}| <= (lambda+C)(lambda+S_{kk}) |Q_{kk}-Qbar_{kk}|`.

Cauchy-Schwarz now proves

`E[d^(-1)sum_k |Lambda_{kk}-D_{kk}|] ->0`.

Let R=Lambda^(1/2)-D^(1/2). The scalar square-root inequality implies

`d^(-1)||R||_F^2 <= d^(-1)sum_k |Lambda_{kk}-D_{kk}| ->0`

in probability. Moreover d^(-1)Tr Lambda is bounded in probability, since Lambda_{kk}<=lambda+S_{kk} and E[d^(-1)Tr S]<=C. Expanding the difference of the two symmetrized matrices and using the Schatten Cauchy-Schwarz inequality gives

`d^(-1)||Lambda^(1/2)Q Lambda^(1/2)-D^(1/2)QD^(1/2)||_1 ->0`.

Indeed its bound is

`lambda^(-1) (d^(-1)||R||_F^2)^(1/2) [(d^(-1)Tr Lambda)^(1/2)+(d^(-1)Tr D)^(1/2)]`.

For eta=Im z>0, the resolvent identity and the Hermitian resolvent bound therefore show that replacing Lambda by D changes d^(-1)Tr G by o_p(1). This argument requires no Gaussian maximum-diagonal concentration or covariance norm concentration.

## 3. The exact lower-block resolvent and its bounds

Fix z and put

`beta=Im z/|z|^2`, `T=D/z-lambda I`, `B=(T-S)^(-1)`.

For row i, set `S_i=S-x_i x_i^T/n` and `B_i=(T-S_i)^(-1)`, where x_i is the transposed row. Since

`Im(T-S_i)=-beta D <= -beta lambda I`,

all these inverses exist and

`||B||, ||B_i|| <= K := 1/(beta lambda)`.

They satisfy

`Im B=beta B* D B >= beta lambda B*B`.

The source two-block linearization, with its local algebraic errors corrected, is

`H=[-zI, D^(1/2); D^(1/2), -S-lambda I]`.

Its upper-left inverse block is the resolvent G_D of D^(1/2)QD^(1/2); its lower-right inverse block is B. Block inversion gives the exact identity

`G_D=-I/z+D^(1/2)BD^(1/2)/z^2`.

## 4. Existence and uniqueness of the specified scalar

If Sigma=0, the scalar equation is chi=0 and Gcal=(I-zI)^(-1). This case is already proved. Assume Sigma!=0 and write r=n^(-1)Tr Sigma>0.

For w in the closed upper half-plane with w!=1, define

`B_w=(T-Sigma/(1-w))^(-1`,

where the closing parenthesis is understood as `B_w=(T-Sigma/(1-w))^(-1)`, and set

`F(w)=n^(-1)Tr(Sigma B_w)`.

Because Im[1/(1-w)]>=0, ||B_w||<=K. In particular |F(w)|<=Kr. Extend F continuously to w=1 by F(1)=0. For completeness, decompose the space into the range and kernel of Sigma. The kernel block of T is invertible because its imaginary part is strictly negative. The Schur complement on the range is a fixed matrix minus Sigma restricted to that range divided by 1-w. Its inverse tends to zero as w->1, proving the extension.

F maps the closed upper half-disk of radius Kr+1 into itself. The finite-dimensional continuous fixed-point theorem gives a fixed point. It is not 1, since F(1)=0. At every other real argument, Im B_w is positive definite, so Im F(w)>0. Hence every fixed point has positive imaginary part.

Here is uniqueness and the stability identity needed later. Write v=Im w and define

`a_w=beta n^(-1)Tr(Sigma B_w* D B_w)`,

`b_w= [n |1-w|^2]^(-1)Tr(Sigma B_w* Sigma B_w)`.

Taking imaginary parts gives

`Im F(w)=a_w+v b_w`.

At a fixed point, a_w>0 and v>0, so b_w<1. For two arguments u,w, the inverse identity gives

`F(u)-F(w)=(u-w) Tr(Sigma B_u Sigma B_w)/[n(1-u)(1-w)]`.

Matrix Cauchy-Schwarz bounds the modulus of the coefficient by sqrt(b_u b_w). Two fixed points would therefore satisfy |u-w|<=sqrt(b_u b_w)|u-w| with a coefficient strictly below one. They must coincide. Denote this solution by chi.

The same coefficient bound makes the derivative of F at chi have modulus below one. The implicit function theorem consequently makes chi analytic in z in the upper half-plane. Thus the stated imaginary-part specification identifies the resolvent branch without an undefined selection convention.

## 5. Conditional variance and trace concentration

Put

`c=n^(-1)Tr(Sigma E B)`, `q_i=n^(-1)x_i^T B_i x_i`.

The deleted row is independent of B_i, and E[x_i x_i^T]=Sigma. The independent-entry fourth-moment variance bound states

`E[|u^T A u-Tr A|^2 | A] <= C_4 Tr(AA*)`

for a complex matrix A independent of a centered unit-variance independent-entry vector u; replacing A by its transpose-symmetric part only improves the needed bound. Expanding the quadratic form proves this inequality by separating diagonal and off-diagonal terms. Applying it to A=Sigma^(1/2)B_i Sigma^(1/2), whose norm is bounded, gives

`E|q_i-n^(-1)Tr(Sigma B_i)|^2=O(1/n)`.

We also need concentration of the traces, not merely of each quadratic form. Replacing one row changes B by a matrix of rank at most two and norm at most 2K. Thus, for a deterministic matrix U of uniformly bounded norm, the change in d^(-1)Tr(UB) is O(1/d). The Efron-Stein inequality, applied separately to real and imaginary parts, yields

`Var(d^(-1)Tr(UB))=O(n/d^2)=O(1/n)`.

The same argument with normalization n applies to the Sigma-weighted trace and to B_i. Deleting one row changes n^(-1)Tr(Sigma B) by O(1/n). Combining these facts proves, uniformly in i,

`E|q_i-c|^2=O(1/n)`.

No maximum over random row errors is required.

The imaginary-part bound for B and Cauchy-Schwarz give

`Im c >= beta lambda |c|^2/r`, `|c|<=Kr`.

Since r is uniformly bounded, these inequalities imply a uniform positive lower bound for |1-c|: if |c|<1/2 use |1-c|>1/2; otherwise use |1-c|>=Im c>=beta lambda/(4r_max). The identical bound holds for |1-chi|, by the fixed-point imaginary-part identity.

## 6. Derivation of the tested expectation equation

The correctly signed and scaled rank-one identity is

`B=B_i+B_i x_i x_i^T B_i/[n(1-q_i)]`,

and hence `Bx_i=B_i x_i/(1-q_i)`. The denominator is nonzero since both inverses exist. Rearranging this exact identity gives

`B x_i x_i^T = B_i x_i x_i^T/(1-c)+(q_i-c)B x_i x_i^T/(1-c)`.

Independence gives E[B_i x_i x_i^T]=(E B_i)Sigma. For any deterministic bounded-norm test U,

`d^(-1)|Tr U E[(q_i-c)B x_i x_i^T]| <= K||U|| d^(-1) E[|q_i-c| ||x_i||^2]=O(n^(-1/2))`.

The last estimate follows from the L2 estimate in Section 5 and E||x_i||^4=O(d^2). It avoids estimating a random inverse denominator.

Now use the exact equation

`BT-n^(-1)sum_i Bx_i x_i^T=I`.

Replacing its row terms by the preceding identities, and replacing E B_i by E B in tested traces using their rank-one, bounded-norm difference, proves

`d^(-1)Tr U[(E B)(T-Sigma/(1-c))-I] ->0`

for every deterministic uniformly bounded U. All errors here are deterministic; their bounds are O(n^(-1/2))+O(d^(-1)).

Let B_c=(T-Sigma/(1-c))^(-1). Its norm is at most K. Taking U=B_c V, with V any deterministic bounded-norm matrix, gives

`d^(-1)Tr V(E B-B_c) ->0`.

In particular,

`c-F(c) ->0`.

This explicitly derives the scalar closure rather than assuming that an expected inverse is already a deterministic equivalent.

## 7. Stability of the approximate fixed point

Because the fixed-point equation varies with dimension, uniqueness alone is not sufficient. We supply a uniform stability argument.

If r->0 along a subsequence, |c| and |chi| are both at most Kr, so |c-chi|->0. On a subsequence with r>=delta>0, the lower bound on |1-c| and |1-chi| implies a uniform bound L on the norms of B_c^(-1) and B_chi^(-1). Consequently

`a_c >= beta lambda r/L^2`, `a_chi >= beta lambda r/L^2`.

These lower bounds follow from B_w*B_w>=L^(-2)I and D>=lambda I. Set e=c-F(c), so e->0. The imaginary-part identity reads

`Im c = a_c+(Im c)b_c+Im e`.

It implies Im c is bounded below by a positive constant, and, since Im c is bounded above, b_c<=1-delta_0 for some delta_0>0 at sufficiently large dimensions. The exact fixed-point identity similarly gives b_chi<=1-delta_0, reducing delta_0 if needed.

The two-argument identity from Section 4 now gives

`|c-chi| <= |e|+sqrt(b_c b_chi)|c-chi|`,

so |c-chi|->0. Every subsequence has a further subsequence in one of these two regimes, proving this convergence along the entire sequence. The inverse identity and the uniform bounds on |1-c| and |1-chi| then give

`||B_c-B_chi|| ->0`.

Together with Section 6, this proves d^(-1)Tr V(E B-B_chi)->0 for every bounded deterministic V.

## 8. Recovering the deterministic resolvent and the spectral measures

The trace concentration from Section 5 and the tested expectation approximation with V=D give

`d^(-1)Tr(D B)-d^(-1)Tr(D B_chi) ->0`

in probability. Define C_chi=lambda I+Sigma/(1-chi). It is invertible: when Sigma!=0, its eigenvalues corresponding to positive covariance eigenvalues have positive imaginary parts, while those on the kernel equal lambda. For Sigma=0 it equals lambda I.

Block inversion gives

`Gcal=-I/z+D^(1/2)B_chi D^(1/2)/z^2`

and equivalently

`Gcal=[D^(1/2)C_chi^(-1)D^(1/2)-zI]^(-1)`.

The latter inverse exists because its imaginary part before inversion is at most -(Im z)I. Comparing this identity with the exact identity for G_D proves the target trace approximation. Section 2 transfers it to the original G.

We finish by checking that the deterministic transform has the asserted probability-measure meaning. Analyticity was proved in Section 4. Since Im C_chi>=0, Im C_chi^(-1)<=0, so Im Gcal>=0 and ||Gcal||<=1/Im z. For z=iy, the map F preserves the quadrant Re w<=0, Im w>=0; the fixed-point existence argument can be performed in that quadrant. Uniqueness therefore gives Re chi(iy)<=0. It follows that Re C_chi>=lambda I and ||C_chi^(-1)||<=1/lambda. Thus, uniformly in dimensions,

`d^(-1)Tr Gcal(iy)=-1/(iy)+O(y^(-2))` as y->infinity.

The elementary Stieltjes representation criterion now shows that this analytic positive-imaginary-part function, with this normalization, is the Stieltjes transform of a probability measure. Its representing measure is supported on the nonnegative real axis: at z=-t<0 the scalar map preserves the negative real half-line, where the same fixed-point argument gives chi<=0; C_chi is positive definite and the displayed Gcal has a positive, nonsingular denominator. Local scalar stability supplies analytic continuation and a real transform across this half-line.

The random measures are tight deterministically, since the diagonal of Lambda^(1/2)Q Lambda^(1/2) is identically one and hence their first moment equals one. The deterministic probability measures are uniformly tight as well: the uniform estimate on the imaginary axis makes y Im[d^(-1)Tr Gcal(iy)] tend uniformly to one. These facts and the trace approximation, first on a countable dense set and then by the resolvent bounds, give the usual weak-convergence interpretation of Stieltjes transforms. In particular, along any subsequence on which the deterministic transforms converge pointwise on the upper half-plane, their limit is the transform of a probability measure and the empirical measures converge weakly to it in probability. No limiting spectral distribution of Sigma has been added as an assumption.

All theorem-critical obligations listed at the start are closed. The source-local sign and scaling repairs do not change the target.
