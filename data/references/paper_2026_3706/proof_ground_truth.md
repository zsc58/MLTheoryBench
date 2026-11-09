# Reference Proof

## Proof structure and obligations

We prove the following obligations in order: (1) choose smooth paths with no collisions at equal times, including when targets coincide with other starting anchors; (2) construct localized contraction and transport fields; (3) establish logarithmic-in-tolerance Lipschitz and Fourier-Barron bounds and a cell-independent trajectory bound; (4) apply a precisely stated scalar approximation theorem with correct total-width accounting; and (5) transfer the construction through a first-exit stability argument and verify the advertised width condition. Disjoint spatial images of the paths are neither assumed nor required.

## 1. Degenerate cells and collision-free paths

Let J be the set of indices of nonempty cells. If J is empty, take every output weight to be zero. The identity flow satisfies every inclusion vacuously and has norm at most sqrt(d)R. Thus suppose J is nonempty. Choose an anchor a_k in Q_k for each k in J. These anchors are distinct.

Set
\[
Y=\max_{1\le k\le K}\|y_k\|_2,\qquad H=1+Y+\sqrt d\,R.
\]
All anchors and targets belong to the open ball B(0,H). We construct paths within that ball, fixed independently of eta.

Choose distinct temporary points in B(0,H) avoiding all anchors and targets. First move each anchor, one at a time, to its temporary point. Then move each temporary point, one at a time, to its assigned target. During each move the other positions form a finite obstacle set, and neither moving endpoint is an obstacle. Two endpoints in B(0,H) can be connected by a two-segment polygonal path avoiding those obstacles: choose an intermediate vertex in the ball outside all lines through either endpoint and an obstacle. A finite union of lines cannot fill an open ball when d>=2. Convexity of the ball keeps both segments inside it.

Schedule these finitely many moves in disjoint subintervals of (2T/3,T). Traverse each segment using a smooth nondecreasing parametrization flat at both endpoints. The resulting paths gamma_k are smooth, constant on [0,2T/3] and near T, satisfy gamma_k(0)=a_k and gamma_k(T)=y_k, and never collide at equal times. Smoothness also holds at polygonal vertices because every time derivative vanishes there. Their spatial images may intersect at different times.

If |J|>=2, put
\[
s=\min_{i,j\in J,\ i\ne j}\operatorname{dist}(Q_i,Q_j)>0,
\qquad
m=\min_{t\in[0,T]}\min_{i,j\in J,\ i\ne j}
\|\gamma_i(t)-\gamma_j(t)\|_2>0.
\]
The second minimum is positive by continuity and compactness. Also m<=2sqrt(d)R, by evaluating at time zero. If |J|=1, instead set s=1 and m=min{1,2sqrt(d)R}; no pairwise separation is needed in this case. In either case m>0 and m<=2sqrt(d)R.

## 2. Smooth contraction and transport

Let D=max_{k in J} diam(Q_k), allowing D=0. Fix a nonnegative smooth radial mollifier psi supported in B(0,1), with integral one, and write psi_r(x)=r^{-d}psi(x/r). Define
\[
\chi_k=\mathbf 1_{Q_k+(s/32)B(0,1)}*\psi_{s/32},
\qquad
\nu(x)=\sum_{k\in J}\chi_k(x)(a_k-x).
\]
Then 0<=chi_k<=1, chi_k=1 on Q_k, and chi_k is smooth with support contained in Q_k+(s/16)B(0,1). These supports are pairwise disjoint when there is more than one cell. These facts remain true for lower-dimensional cells: their positive-radius neighborhoods, not the cells themselves, are mollified.

Choose a smooth radial function xi with values in [0,1], equal to one on the closed unit ball and supported in B(0,2). Put
\[
w(t,x)=\sum_{k\in J}\dot\gamma_k(t)
\xi\!\left(\frac{8(x-\gamma_k(t))}{m}\right).
\]
At each time, its summand supports lie in pairwise disjoint balls B(gamma_k(t),m/4). On the closed m/8-ball about gamma_k(t), the field equals dot(gamma_k)(t). Extend the paths constantly outside [0,T]. Because they are constant near both endpoints, w is a smooth compactly supported function of space and time, zero before the transport phase and near the temporal endpoints.

Choose a smooth nondecreasing phi on [0,T], equal to zero on [0,T/3] and one on [2T/3,T]. Extend 1-phi to a fixed smooth compactly supported function a on the real line, unchanged on [0,T]. Such an extension is obtained by keeping it constant just before zero and multiplying there by a smooth cutoff; it is already zero near T.

For 0<eta<=1 define
\[
\lambda_\eta=\frac3T\log_+\!\left(\frac{4D}{\eta}\right),
\qquad
v_\eta(t,x)=\lambda_\eta a(t)\nu(x)+w(t,x),
\]
where log_+(r)=max{log r,0} for r>0 and log_+(0)=0. Thus v_eta is globally smooth and compactly supported. On [0,T] this is the source's concatenated contraction and transport field: w vanishes before 2T/3, while a vanishes thereafter. Write Psi_t for its flow.

For x in Q_k, convexity and uniqueness give, through time 2T/3,
\[
\Psi_t(x)=a_k+
\exp\!\left(-\lambda_\eta\int_0^t(1-\varphi(r))\,dr\right)(x-a_k).
\]
This path stays in Q_k, where chi_k=1. The integral at 2T/3 is at least T/3. Consequently
\[
\|\Psi_{2T/3}(x)-a_k\|_2
\le D\exp(-\lambda_\eta T/3)\le\eta/4.
\]
This estimate also holds for D=0, when the cell points remain at their anchors during contraction.

Set eta_0=min{1,m/2}. For eta<=eta_0 the last offset has norm at most m/8. During transport the path gamma_k(t)+Psi_{2T/3}(x)-a_k therefore solves the ODE exactly. Hence
\[
\|\Psi_T(x)-y_k\|_2\le\eta/4\quad(x\in Q_k).
\]
We retain closed intermediate balls; the final theorem will have strict tolerance slack.

## 3. Quantitative bounds

### Trajectories from the entire cube

During contraction, a point outside the supports is fixed. A point affected by the k-th cutoff moves toward a_k along its straight segment to a_k, with nonnegative scalar speed. Its containing neighborhood Q_k+(s/8)B(0,1) is convex and disjoint from the others, so it cannot switch to another contraction field. If the initial point lies in D_R, that segment lies in D_R. Therefore all trajectories from D_R have norm at most sqrt(d)R during contraction.

During transport the field vanishes outside the union of B(gamma_k(t),m/4). Wherever a trajectory has nonzero velocity, its norm is less than H+m/4. The same bound, with non-strict inequality, holds at limits of such times and on stationary intervals, since the initial bound is smaller. Thus
\[
\sup_{x\in D_R,\ 0\le t\le T}\|\Psi_t(x)\|_2
\le M_0:=1+Y+\tfrac32\sqrt d\,R.
\]
Crucially, M_0 does not depend on the cells, their separation, or eta.

### Lipschitz and Fourier-Barron quantities

All functions other than lambda_eta were fixed before eta was chosen. Put U(t,x)=a(t)nu(x) and W(t,x)=w(t,x), so v_eta=lambda_eta U+W. Both are fixed smooth compactly supported vector fields. For eta<=1,
\[
\lambda_\eta\le\frac3T\bigl(\log_+(4D)+|\log\eta|\bigr),
\]
with the D=0 case understood separately as lambda_eta=0. Consequently there is L>=1, depending only on the fixed geometric data and T, such that
\[
\sup_{0\le t\le T}\operatorname{Lip}_x v_\eta(t,\cdot)
\le L(1-\log\eta).
\]
Indeed, one can use the bound lambda_eta sup_t||D_x U||_infinity+sup_t||D_x W||_infinity and the preceding estimate for lambda_eta.

For a compactly supported smooth vector field f on R^{d+1}, define
\[
\mathcal B(f)=\sum_{\ell=1}^d\int_{\mathbb R^{d+1}}
\|\zeta\|_1^2\,|\widehat{f^{(\ell)}}(\zeta)|\,d\zeta.
\]
Fix any Fourier convention; its normalization is absorbed into dimensional constants. Let n=d+4. Since ||zeta||_1^2/(1+||zeta||_1)^n is integrable in dimension d+1, expansion of the polynomial weight and the Fourier derivative identity imply, for scalar g,
\[
\int\|\zeta\|_1^2|\widehat g(\zeta)|\,d\zeta
\le C_d\sum_{|\alpha|\le d+4}\|\partial^\alpha g\|_{L^1}.
\]
Here each weighted Fourier monomial is the Fourier transform of the corresponding derivative, up to a fixed constant, and its supremum is bounded by that derivative's L1 norm. This proves both finiteness and the displayed estimate.

Apply this estimate componentwise to U and W. Their derivative norms are finite constants independent of eta. By linearity and the triangle inequality,
\[
\mathcal B(v_\eta)\le\lambda_\eta\mathcal B(U)+\mathcal B(W)
\le B(1-\log\eta)
\]
for a fixed B>=1. These are the quantitative bounds needed for the frozen theorem; an explicit formula in terms of every geometric separation is unnecessary because C is allowed to depend on the full fixed configuration.

## 4. Standard independent approximation input and width accounting

We use the scalar uniform Fourier-Barron/ReLU approximation theorem, in the corollary invoked by the source: for a real g in C_c^infinity(R^n), S>=1, and integer q>=3, a scalar q-unit affine-ridge ReLU network h exists with
\[
\sup_{z\in[-S,S]^n}|g(z)-h(z)|
\le\frac{A_n S^2}{\sqrt q}
\int_{\mathbb R^n}\|\zeta\|_1^2|\widehat g(\zeta)|\,d\zeta.
\]
A_n depends only on n and the Fourier convention. Any affine part is represented by ReLU units within this width convention. This is the standard independent scalar approximation result recorded as theory_025, attributed in the source to the uniform ridge approximation theorem of Klusowski and Barron. No ODE conclusion or approximating-network Lipschitz estimate is assumed from it.

Take n=d+1. For integer p>=3d, assign q=floor(p/d)>=3 units to each component of v_eta. Since q>=p/(2d), summing component errors yields a vector field
\[
v_p(t,x)=\sum_{i=1}^p u_i(\alpha_i\cdot x+\beta_i t+\gamma_i)_+
\]
with
\[
\sup_{(t,x)\in[-S,S]^{d+1}}\|v_\eta(t,x)-v_p(t,x)\|_2
\le\frac{C_dS^2\mathcal B(v_\eta)}{\sqrt p}
=: \varepsilon_p.
\]
Unused units are padded with zero output weights. The scalar theorem's hypotheses hold because each component of v_eta is smooth and compactly supported and its Fourier quantity was bounded explicitly above. The variables (t,x) give exactly an affine dependence on time in each ridge.

Every such finite network is globally Lipschitz in x, with constant at most sum_i ||u_i||_2||alpha_i||_2, and has at most linear growth on [0,T]. It therefore generates a global flow Phi_t on that interval. No bound on this network Lipschitz constant is used in the stability exponent.

## 5. First-exit stability, width threshold, and final conclusions

Choose
\[
S=2+\max\{T,Y+\tfrac32\sqrt d\,R\},\qquad M=S.
\]
Then S>=1 and
\[
[0,T]\times\bigcup_{0\le t\le T}\Psi_t(D_R)
\subset[-(S-1),S-1]^{d+1}.
\]
Thus the reference trajectories have a one-unit margin inside the approximation cube.

Fix x in D_R and stop the network trajectory at its first exit from [-S,S]^d, or at T if it does not exit. Up to this stopping time, adding and subtracting v_eta(t,Phi_t(x)) gives
\[
e(t)\le\varepsilon_p t+
L(1-\log\eta)\int_0^t e(r)\,dr,
\qquad e(t)=\|\Phi_t(x)-\Psi_t(x)\|_2.
\]
Gronwall gives
\[
e(t)\le\varepsilon_p T\exp\!\bigl(TL(1-\log\eta)\bigr)
\le\frac{A(1-\log\eta)}{\sqrt p}\eta^{-TL},
\qquad A=C_dS^2TB e^{TL}.
\]
If the right side is less than one, a first exit is impossible: at the supposed exit time the network trajectory is still strictly inside the cube because it is less than one away from a reference trajectory in the inner cube. This proves the estimate for all times and all initial points, without assuming containment of the approximating trajectories in advance.

Choose a fixed constant
\[
C\ge\max\{1,3d,2TL,4A^2\}.
\]
It has exactly the dependencies permitted in the public task. If
\[
p\ge C\eta^{-2-C}(1-\log\eta)^2,
\]
then p>=3d and
\[
\frac{A(1-\log\eta)}{\sqrt p}\eta^{-TL}
\le\frac{A}{\sqrt C}\eta^{1+C/2-TL}
\le\eta/2\le1/2.
\]
This both closes the first-exit argument and yields uniform flow error at most eta/2.

For x in a nonempty Q_k,
\[
\|\Phi_T(x)-y_k\|_2
\le\|\Phi_T(x)-\Psi_T(x)\|_2+
\|\Psi_T(x)-y_k\|_2
\le\eta/2+\eta/4<\eta.
\]
For empty Q_k the inclusion is vacuous. Finally,
\[
\sup_{x\in D_R}\|\Phi_T(x)\|_2
\le M_0+\eta/2\le(S-1)+1/2<S=M.
\]
M depends only on d,T,R and the targets, while C and eta_0 may depend on the fixed cells and paths. The construction works for every eta in (0,eta_0] and every integer p meeting the threshold. In the all-empty case discussed initially, use the same M, eta_0=1 and, for example, C=3d. This completes every obligation of the frozen target.
